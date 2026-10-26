#!/usr/bin/env python3
"""Validate evidence accounting while keeping course media out of Git."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(data):
    errors = []
    lessons = data.get("lessons", [])
    if {r["id"] for r in lessons} != {f"{i:02}" for i in range(1, 19)} or len(lessons) != 18:
        errors.append("Expected exactly 18 distinct lessons")
    for row in lessons:
        review = row["review"]
        sub = review["subtitles"]
        if sub["state"] == "read_all_cues" and sub["reviewed_cues"] != row["subtitle_cues"]:
            errors.append(f"{row['id']}: incomplete cue count claims complete reading")
        notes = review["notes"].get("file")
        if notes and (not (ROOT / notes).is_file() or "cheese" in Path(notes).parts):
            errors.append(f"{row['id']}: invalid public notes path")
        visual = review["visual_samples"]
        if visual.get("reviewed_sheets"):
            manifest_path = ROOT/"cheese/.analysis/visual"/row["id"]/"manifest.json"
            if not manifest_path.is_file():
                errors.append(f"{row['id']}: visual manifest missing")
            else:
                manifest=json.loads(manifest_path.read_text())
                if visual.get("manifest_sha256") != digest(manifest_path):
                    errors.append(f"{row['id']}: reviewed visual manifest hash mismatch")
                if manifest.get("video_sha256") and manifest["video_sha256"] != row["video_sha256"]:
                    errors.append(f"{row['id']}: visual manifest/source hash mismatch")
                available={s["file"] for s in manifest["sheets"]}
                for sheet in visual["reviewed_sheets"]:
                    if sheet not in available or not (manifest_path.parent/sheet).is_file():
                        errors.append(f"{row['id']}: reviewed sheet absent: {sheet}")
                count=sum(len(s["source_timestamps"]) for s in manifest["sheets"]
                          if s["file"] in visual["reviewed_sheets"])
                if visual.get("reviewed_frame_count") != count:
                    errors.append(f"{row['id']}: reviewed sample frame count mismatch")
        fine = review.get("fine_visual_samples")
        if fine:
            # 细抽帧索引页是可复现的派生产物，校验 manifest 哈希与计数，
            # 不要求每张 JPEG 长期留在磁盘上。
            fine_manifest_path = ROOT/"cheese/.analysis/fine"/row["id"]/"manifest.json"
            if not fine_manifest_path.is_file():
                errors.append(f"{row['id']}: fine visual manifest missing")
            else:
                fine_manifest = json.loads(fine_manifest_path.read_text())
                if fine.get("manifest_sha256") != digest(fine_manifest_path):
                    errors.append(f"{row['id']}: fine visual manifest hash mismatch")
                if (fine_manifest.get("video_sha256")
                        and fine_manifest["video_sha256"] != row["video_sha256"]):
                    errors.append(f"{row['id']}: fine visual manifest/source hash mismatch")
                if fine.get("interval_seconds") != fine_manifest.get("interval_seconds"):
                    errors.append(f"{row['id']}: fine visual interval mismatch")
                if fine.get("reviewed_sheet_count") != len(fine_manifest.get("sheets", [])):
                    errors.append(f"{row['id']}: fine visual sheet count mismatch")
                if fine.get("reviewed_frame_count") != fine_manifest.get("frame_count"):
                    errors.append(f"{row['id']}: fine visual frame count mismatch")
            fine_doc = fine.get("document")
            if fine_doc and (not (ROOT / fine_doc).is_file() or "cheese" in Path(fine_doc).parts):
                errors.append(f"{row['id']}: invalid fine visual document path")
        asr=review["audio_dialogue_asr"]
        if asr["state"] == "transcribed_full_input":
            path=ROOT/"cheese/.analysis/asr"/f"{row['id']}.json"
            if not path.is_file() or asr.get("asr_sha256") != digest(path):
                errors.append(f"{row['id']}: ASR file/hash mismatch")
            else:
                audit=json.loads(path.read_text()).get("audit",{})
                if (audit.get("video_sha256") != row["video_sha256"]
                        or audit.get("input_range_seconds") != [0,row["duration_seconds"]]):
                    errors.append(f"{row['id']}: ASR lacks matching full input range")
        if review["complete_multimodal_review"]:
            if sub["state"] != "read_all_cues" or review["continuous_video"]["state"] != "reviewed_full" or review["audio_listening"]["state"] != "reviewed_full":
                errors.append(f"{row['id']}: full multimodal completion lacks actual viewing/listening")
    tracked=subprocess.check_output(["git","ls-files","-z"],cwd=ROOT).decode().split("\0")
    for name in tracked:
        if name.startswith("cheese/") or Path(name).suffix.lower() in {".mp4",".mov",".wav",".mp3",".srt"}:
            errors.append(f"Course/media-like file in Git index: {name}")
    return errors


def summary(data):
    lines=["# 课程证据状态", "", "来源：影视飓风（MediaStorm）付费剪映教学课程；个人学习、非官方。", "",
           "本表由证据账本生成；抽样画面与机器转写均不代表完整音画理解。", "",
           "| 课号 | 课程 | 字幕条目已读 | 全音轨 ASR | 已看 20s 抽样帧 | 细抽帧（2s） | 连续音画验收 |",
           "| --- | --- | ---: | --- | ---: | --- | --- |"]
    total_frames=0
    total_fine=0
    for row in data["lessons"]:
        review=row["review"]
        frames=review["visual_samples"].get("reviewed_frame_count",0)
        total_frames+=frames
        fine=review.get("fine_visual_samples")
        if fine:
            total_fine+=fine.get("reviewed_frame_count",0)
            fine_text=f"{fine['reviewed_frame_count']}/{fine['reviewed_sheet_count']} 页"
        else:
            fine_text="待完成"
        asr="已处理，非听辨" if review["audio_dialogue_asr"]["state"]=="transcribed_full_input" else "待完成"
        complete="已完成" if review["complete_multimodal_review"] else "待完成"
        lines.append(f"| {row['id']} | {row['title']} | {review['subtitles']['reviewed_cues']}/{row['subtitle_cues']} | {asr} | {frames} | {fine_text} | {complete} |")
    lines.extend(["", f"合计 {len(data['lessons'])} 课、{sum(r['subtitle_cues'] for r in data['lessons'])} 条字幕、{total_frames} 个 20 秒抽样画面、{total_fine} 个 2 秒细抽帧（不含局部回查图）。", "",
                  "详细时间码、源哈希和各模态状态见 [course-ledger.json](course-ledger.json)；后续所需输入见 [remaining-review.md](remaining-review.md)。", ""])
    return "\n".join(lines)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger",type=Path,default=ROOT/"progress/course-ledger.json")
    parser.add_argument("--write-summary",action="store_true",help="Regenerate the public evidence status table after validation")
    args=parser.parse_args()
    data=json.loads(args.ledger.read_text())
    problems=check(data)
    if problems:
        for problem in problems: print("ERROR:",problem)
        raise SystemExit(1)
    print(f"PASS: {len(data['lessons'])} lessons; evidence states consistent; no course media in Git index")
    if args.write_summary:
        (ROOT/"progress/status.md").write_text(summary(data))
