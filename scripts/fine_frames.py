#!/usr/bin/env python3
"""细粒度抽帧：生成带时间码的索引页，或按时间点抓取全分辨率画面。

课程原件只读。所有产物写入被忽略的 cheese/.analysis/ 下。

用法：
  # 每 3 秒一帧，2x2 索引页，960x540 单格
  python scripts/fine_frames.py sheets 03 --interval 3

  # 只抽指定课程，自定义输出目录
  python scripts/fine_frames.py sheets 01 02 --interval 2 --out cheese/.analysis/fine

  # 按精确时间抓全分辨率帧（可裁剪、放大）
  python scripts/fine_frames.py grab 03 05:12.5
  python scripts/fine_frames.py grab 03 05:12.5 --crop 1420:80:520:700 --scale 1560
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "progress" / "course-ledger.json"
PRIVATE = ROOT / "cheese" / ".analysis"
FONT_PATH = "/System/Library/Fonts/Menlo.ttc"


def clock(seconds: float) -> str:
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int(seconds % 3600 // 60)
    s = seconds % 60
    if h:
        return f"{h}:{m:02d}:{s:05.2f}"
    return f"{m:02d}:{s:05.2f}"


def parse_time(value: str) -> float:
    if ":" in value:
        parts = [float(p) for p in value.split(":")]
        total = 0.0
        for part in parts:
            total = total * 60 + part
        return total
    return float(value)


def lessons() -> dict[str, dict]:
    data = json.loads(LEDGER.read_text())
    return {row["id"]: row for row in data["lessons"]}


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, **kwargs)


def extract_sheets(
    ids: list[str],
    interval: float,
    out_root: Path,
    cols: int,
    rows: int,
    tile_width: int,
    quality: int,
    keep_frames: bool,
    clean: bool,
) -> None:
    from PIL import Image, ImageDraw, ImageFont

    font = ImageFont.truetype(FONT_PATH, max(15, tile_width // 52))
    label_h = max(24, tile_width // 36)
    tile_h = round(tile_width * 9 / 16)
    sheet_w = cols * tile_width
    sheet_h = rows * (tile_h + label_h)
    per_sheet = cols * rows

    table = lessons()
    for lesson_id in ids:
        row = table.get(lesson_id)
        if row is None:
            raise SystemExit(f"未知课程编号：{lesson_id}")
        video = ROOT / row["video"]
        out = out_root / lesson_id
        out.mkdir(parents=True, exist_ok=True)
        if clean:
            for old in out.glob("sheet-*.jpg"):
                old.unlink()
            manifest_path = out / "manifest.json"
            if manifest_path.exists():
                manifest_path.unlink()

        select = (
            "select='isnan(prev_selected_t)+"
            f"gte(t-prev_selected_t,{interval})',showinfo,"
            f"scale={tile_width}:-2"
        )
        with tempfile.TemporaryDirectory(prefix=f"frames-{lesson_id}-", dir=PRIVATE) as tmp:
            tmp_path = Path(tmp)
            proc = run(
                [
                    "ffmpeg", "-hide_banner", "-loglevel", "info", "-threads", "2",
                    "-i", str(video), "-vf", select, "-fps_mode", "vfr",
                    "-q:v", "3", str(tmp_path / "%06d.jpg"),
                ],
                capture_output=True, text=True,
            )
            frames = sorted(tmp_path.glob("*.jpg"))
            timestamps = [float(t) for t in re.findall(r"pts_time:([0-9.]+)", proc.stderr)]
            # showinfo 每帧一行；若解析数量不符，退回等间隔估算并记警告。
            warning = None
            if len(timestamps) != len(frames):
                warning = f"timestamp/frame mismatch {len(timestamps)}/{len(frames)}; 使用序号×interval"
                timestamps = [i * interval for i in range(len(frames))]
            manifest = {
                "lesson": lesson_id,
                "video_sha256": row["video_sha256"],
                "interval_seconds": interval,
                "mode": "sampled_stills",
                "layout": f"{cols}x{rows}",
                "tile": [tile_width, tile_h],
                "source_size": [1920, 1080],
                "frame_count": len(frames),
                "warning": warning,
                "sheets": [],
            }
            for base in range(0, len(frames), per_sheet):
                group = frames[base:base + per_sheet]
                canvas = Image.new("RGB", (sheet_w, sheet_h), "#0d0d0d")
                draw = ImageDraw.Draw(canvas)
                times = []
                for j, frame in enumerate(group):
                    t = timestamps[base + j]
                    times.append(round(t, 3))
                    x = (j % cols) * tile_width
                    y = (j // cols) * (tile_h + label_h)
                    draw.text(
                        (x + 6, y + 2),
                        f"L{lesson_id} {clock(t)} #{base + j + 1}",
                        font=font,
                        fill="#f2f2f2",
                    )
                    with Image.open(frame) as pic:
                        canvas.paste(pic, (x, y + label_h))
                filename = f"sheet-{base // per_sheet + 1:03d}.jpg"
                canvas.save(out / filename, quality=quality, optimize=True)
                manifest["sheets"].append({"file": filename, "source_timestamps": times})
            (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
            if not keep_frames:
                shutil.rmtree(tmp_path, ignore_errors=True)
            print(json.dumps({
                "lesson": lesson_id,
                "frames": len(frames),
                "sheets": len(manifest["sheets"]),
                "interval": interval,
                "directory": str(out),
                "warning": warning,
            }, ensure_ascii=False))


def grab(
    lesson_id: str,
    time_value: str,
    out: Path,
    crop: str | None,
    scale: int | None,
    quality: int,
) -> None:
    row = lessons().get(lesson_id)
    if row is None:
        raise SystemExit(f"未知课程编号：{lesson_id}")
    t = parse_time(time_value)
    out.parent.mkdir(parents=True, exist_ok=True)
    filters = []
    if crop:
        c = crop.replace(",", ":").replace("x", ":")
        parts = c.split(":")
        if len(parts) != 4:
            raise SystemExit("--crop 需要 x:y:w:h")
        x, y, w, h = parts
        # 用户输入 x:y:w:h；ffmpeg 的 crop 顺序是 w:h:x:y。
        filters.append(f"crop={w}:{h}:{x}:{y}")
    if scale:
        filters.append(f"scale={scale}:-2:flags=lanczos")
    vf = ",".join(filters) if filters else "null"
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error",
        "-ss", f"{t:.3f}", "-i", str(ROOT / row["video"]),
        "-frames:v", "1", "-vf", vf, "-q:v", str(quality), str(out), "-y",
    ])
    print(json.dumps({
        "lesson": lesson_id,
        "time": clock(t),
        "file": str(out),
        "crop": crop,
        "scale": scale,
    }, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_sheets = sub.add_parser("sheets", help="生成带时间码的索引页")
    p_sheets.add_argument("ids", nargs="+", help="课程编号，如 01 03")
    p_sheets.add_argument("--interval", type=float, default=3.0)
    p_sheets.add_argument("--out", type=Path, default=PRIVATE / "fine")
    p_sheets.add_argument("--cols", type=int, default=2)
    p_sheets.add_argument("--rows", type=int, default=2)
    p_sheets.add_argument("--tile-width", type=int, default=960)
    p_sheets.add_argument("--quality", type=int, default=78)
    p_sheets.add_argument("--keep-frames", action="store_true")
    p_sheets.add_argument("--clean", action="store_true", help="先删除该课旧索引页")

    p_grab = sub.add_parser("grab", help="抓取指定时间点的全分辨率画面")
    p_grab.add_argument("id")
    p_grab.add_argument("time", help="秒数或 mm:ss(.x)")
    p_grab.add_argument("--out", type=Path, default=PRIVATE / "grabs")
    p_grab.add_argument("--crop", help="x:y:w:h")
    p_grab.add_argument("--scale", type=int, help="输出宽度")
    p_grab.add_argument("--quality", type=int, default=3)

    args = parser.parse_args()
    if args.command == "sheets":
        extract_sheets(
            args.ids, args.interval, args.out, args.cols, args.rows,
            args.tile_width, args.quality, args.keep_frames, args.clean,
        )
    elif args.command == "grab":
        name = f"L{args.id}-{args.time.replace(':', '-')}"
        if args.crop:
            name += "-crop"
        target = args.out / f"{name}.jpg"
        grab(args.id, args.time, target, args.crop, args.scale, args.quality)


if __name__ == "__main__":
    main()
