#!/usr/bin/env python3
"""Local course evidence helpers. Derived course media stays under cheese/.analysis."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / "cheese" / ".analysis"
LEDGER = ROOT / "progress" / "course-ledger.json"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(2**20), b""):
            h.update(chunk)
    return h.hexdigest()


def seconds(stamp: str) -> float:
    h, m, s = stamp.replace(",", ".").split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def clock(value: float) -> str:
    return f"{int(value)//3600:02}:{int(value)%3600//60:02}:{int(value)%60:02}"


def cues(path: Path) -> list[dict]:
    result = []
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip()):
        lines = block.splitlines()
        idx = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if idx is None:
            raise ValueError(f"Subtitle block lacks timestamp in {path.name}")
        a, b = lines[idx].split("-->", 1)
        start, end = seconds(a.strip()), seconds(b.strip().split()[0])
        if end < start:
            raise ValueError(f"Reversed subtitle in {path.name}")
        result.append({"start": start, "end": end, "text": " ".join(lines[idx + 1:])})
    return result


def load() -> dict:
    return json.loads(LEDGER.read_text())


def save(data: dict) -> None:
    LEDGER.parent.mkdir(exist_ok=True)
    tmp = LEDGER.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(LEDGER)


def inventory() -> None:
    old = load() if LEDGER.exists() else {"lessons": []}
    previous = {row["id"]: row for row in old["lessons"]}
    rows = []
    for video in sorted((ROOT / "cheese/视频").glob("*.mp4")):
        lesson = video.name.split(" - ", 1)[0]
        matches = list((ROOT / "cheese/字幕").glob(f"{lesson} - *.srt"))
        if len(matches) != 1:
            raise ValueError(f"Expected exactly one subtitle for {video.name}")
        subtitle = matches[0]
        data = json.loads(subprocess.check_output([
            "ffprobe", "-v", "error", "-show_entries",
            "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate",
            "-of", "json", str(video)], text=True))
        duration = float(data["format"]["duration"])
        entries = cues(subtitle)
        if any(c["end"] > duration + 1 for c in entries):
            raise ValueError(f"Subtitle beyond video: {subtitle.name}")
        sha = digest(video)
        prior = previous.get(lesson, {})
        if prior and (prior["video_sha256"] != sha or prior["subtitle_sha256"] != digest(subtitle)):
            raise ValueError(f"Source changed: {lesson}; review coverage before resetting")
        rows.append({
            "id": lesson, "title": video.stem.split(" - ", 1)[1],
            "video": str(video.relative_to(ROOT)), "subtitle": str(subtitle.relative_to(ROOT)),
            "video_sha256": sha, "subtitle_sha256": digest(subtitle),
            "duration_seconds": duration, "streams": data["streams"],
            "subtitle_cues": len(entries), "subtitle_last_end": entries[-1]["end"],
            **({"subtitle_gap_candidates": prior["subtitle_gap_candidates"]}
               if "subtitle_gap_candidates" in prior else {}),
            "review": prior.get("review", {
                "subtitles": {"state": "pending", "reviewed_cues": 0},
                "visual_samples": {"state": "pending", "reviewed_sheets": [], "interval_seconds": None},
                "continuous_video": {"state": "pending", "reason": "No verified continuous-video input"},
                "audio_dialogue_asr": {"state": "pending"},
                "audio_listening": {"state": "unavailable", "reason": "Current model interface rejects audio input"},
                "notes": {"state": "pending"}, "complete_multimodal_review": False,
            }),
        })
    if len(rows) != 18 or {row["id"] for row in rows} != {f"{n:02}" for n in range(1, 19)}:
        raise ValueError("Expected lessons 01 through 18 exactly")
    save({"source": "影视飓风（MediaStorm）付费剪映教学课程；个人学习，非官方",
          "schema_version": 1, "total_duration_seconds": sum(r["duration_seconds"] for r in rows),
          "completion_rule": "All subtitle cues + continuous video review + actual audio listening; ASR and sampled frames do not suffice",
          "lessons": rows})
    print(f"Inventoried {len(rows)} lessons, {clock(sum(r['duration_seconds'] for r in rows))}")


def read(ids: list[str]) -> None:
    for row in load()["lessons"]:
        if row["id"] not in ids:
            continue
        print(f"\nLESSON {row['id']} {row['title']} ({clock(row['duration_seconds'])})")
        entries = cues(ROOT / row["subtitle"])
        # Preserve every cue's text. Group only display lines, with range identifiers.
        for start in range(0, len(entries), 12):
            part = entries[start:start + 12]
            print(f"[{start+1}-{start+len(part)} {clock(part[0]['start'])}-{clock(part[-1]['end'])}] " + " / ".join(x["text"] for x in part))
        print(f"END LESSON {row['id']} {len(entries)} CUES")


def sheets(ids: list[str], interval: float) -> None:
    from PIL import Image, ImageDraw, ImageFont
    font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 17)
    for row in load()["lessons"]:
        if row["id"] not in ids:
            continue
        out = PRIVATE / "visual" / row["id"]
        out.mkdir(parents=True, exist_ok=True)
        manifest_file=out/"manifest.json"
        if manifest_file.is_file():
            existing=json.loads(manifest_file.read_text())
            if (existing.get("video_sha256")==row["video_sha256"]
                    and existing.get("interval_seconds")==interval
                    and all((out/s["file"]).is_file() for s in existing["sheets"])):
                print(f"Visual {row['id']} cached; not newly reviewed",flush=True)
                continue
        # Frame 0, then one frame each interval. Samples are never recorded as continuous viewing.
        with tempfile.TemporaryDirectory(prefix="frames-", dir=PRIVATE) as working:
            decoded = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "info", "-threads", "2",
                            "-i", str(ROOT / row["video"]), "-vf",
                            f"select='isnan(prev_selected_t)+gte(t-prev_selected_t,{interval})',showinfo,scale=480:-1",
                            "-fps_mode", "vfr", "-q:v", "4", str(Path(working)/"%06d.jpg")],
                            check=True, capture_output=True, text=True)
            frames = sorted(Path(working).glob("*.jpg"))
            timestamps = [float(t) for t in re.findall(r"pts_time:([0-9.]+)", decoded.stderr)]
            if len(timestamps) != len(frames):
                raise ValueError(f"Frame/timestamp mismatch for {row['id']}")
            manifest = {"lesson": row["id"], "video_sha256":row["video_sha256"],
                        "interval_seconds": interval, "mode": "sampled_stills", "sheets": []}
            for base in range(0, len(frames), 24):
                group = frames[base:base+24]
                canvas = Image.new("RGB", (1920, math.ceil(len(group)/4) * 298), "#121212")
                draw = ImageDraw.Draw(canvas)
                times = []
                for j, frame in enumerate(group):
                    t = timestamps[base+j]
                    times.append(round(t, 3))
                    x, y = j%4*480, j//4*298
                    draw.text((x+8, y+4), f"L{row['id']}  {clock(t)}  sample {base+j+1}", font=font, fill="white")
                    with Image.open(frame) as pic:
                        canvas.paste(pic, (x, y+28))
                filename = f"sheet-{base//24+1:03}.jpg"
                canvas.save(out/filename, quality=88)
                manifest["sheets"].append({"file": filename, "source_timestamps": times})
            (out/"manifest.json").write_text(json.dumps(manifest, indent=2))
            print(json.dumps({"id":row["id"],"samples":len(frames),"sheets":len(manifest["sheets"]),"directory":str(out)},ensure_ascii=False),flush=True)


def transcribe(model: str, ids: list[str]) -> None:
    import os
    os.environ.setdefault("HF_HOME", str(PRIVATE/"models"))
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    import mlx_whisper
    out = PRIVATE/"asr"
    out.mkdir(parents=True,exist_ok=True)
    for row in load()["lessons"]:
        if row["id"] not in ids:
            continue
        target = out/f"{row['id']}.json"
        if target.exists():
            cached=json.loads(target.read_text())
            if cached.get("audit",{}).get("video_sha256") != row["video_sha256"]:
                raise ValueError(f"Cached ASR/source mismatch for {row['id']}")
            if cached.get("audit",{}).get("model") != model:
                raise ValueError(f"Cached ASR model differs for {row['id']}; use a separate output directory")
            print(f"ASR {row['id']} cached",flush=True)
            continue
        print(f"ASR {row['id']} start {row['title']}",flush=True)
        result = mlx_whisper.transcribe(str(ROOT/row["video"]),path_or_hf_repo=model,
                                       language="zh",verbose=None,condition_on_previous_text=False,
                                       initial_prompt="影视飓风，剪映，蒙太奇，关键帧，达芬奇，A-roll，B-roll，Vlog，H.264，HEVC，H.265")
        result["audit"]={"model":model,"video_sha256":row["video_sha256"],
                         "input_range_seconds":[0,row["duration_seconds"]],
                         "scope":"full audio submitted to speech recognition; no actual listening"}
        tmp=target.with_suffix(".tmp")
        tmp.write_text(json.dumps(result,ensure_ascii=False,indent=2))
        tmp.replace(target)
        print(f"ASR {row['id']} completed: {len(result.get('segments',[]))} segments",flush=True)
        # Release per-lesson tensors/cached allocations before opening the next long file.
        del result
        import gc
        import mlx.core as mx
        gc.collect()
        mx.clear_cache()


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command",choices=["inventory","read","sheets","transcribe"])
    parser.add_argument("ids",nargs="*")
    parser.add_argument("--interval",type=float,default=10)
    parser.add_argument("--model",default="mlx-community/whisper-small-mlx")
    args=parser.parse_args()
    PRIVATE.mkdir(parents=True,exist_ok=True)
    if args.interval <= 0:
        parser.error("interval must be positive")
    ids=[f"{int(x):02}" for x in args.ids] or [f"{x:02}" for x in range(1,19)]
    if args.command=="inventory": inventory()
    elif args.command=="read": read(ids)
    elif args.command=="sheets": sheets(ids,args.interval)
    else: transcribe(args.model,ids)


if __name__=="__main__":
    main()
