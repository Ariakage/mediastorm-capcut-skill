#!/usr/bin/env python3
"""Summarize video-storyboard sheet.json files as a Markdown density table.

The input directory is expected to contain one subdirectory per lesson, each with
a sheet.json produced by:
  storyboard.mjs <video> --transcript-file <srt> --strategy compact --max-sheets 1 --text --json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DEFAULT_DIR = Path("cheese/.analysis/storyboard-metrics")


def duration_clock(seconds: float) -> str:
    total = int(round(seconds))
    hours, rest = divmod(total, 3600)
    minutes, secs = divmod(rest, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def load_row(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    probe = data.get("probe", {})
    plan = data.get("plan", {})
    duration = float(probe.get("duration", 0) or 0)
    cuts = plan.get("inputs", {}).get("cuts")
    text = data.get("text", "")
    match = re.search(r'cuts="(\d+) \(avg ([0-9.]+)s\)"', text)
    if match:
        cuts = int(match.group(1))
        average = float(match.group(2))
    else:
        average = round(duration / cuts, 2) if cuts else None
    if not duration or cuts is None:
        return None
    return {
        "lesson": path.parent.name,
        "duration": duration,
        "cuts": cuts,
        "average": average,
        "per_minute": round(cuts / duration * 60, 1),
        "frames": plan.get("frames"),
        "sheets": plan.get("sheets"),
        "sheet": (data.get("sheets") or [{}])[0].get("path"),
        "mean_lufs": plan.get("inputs", {}).get("meanLufs"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR)
    parser.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    args = parser.parse_args()

    rows = []
    for path in sorted(args.dir.glob("*/sheet.json")):
        row = load_row(path)
        if row:
            rows.append(row)
    if not rows:
        raise SystemExit(f"No sheet.json found under {args.dir}")
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return
    print("| Lesson | Duration | Scene cuts | Avg interval | Cuts/min | Sheets |")
    print("| --- | ---: | ---: | ---: | ---: | ---: |")
    for row in rows:
        print(
            f"| {row['lesson']} | {duration_clock(row['duration'])} | {row['cuts']} | "
            f"{row['average']}s | {row['per_minute']} | {row['sheets']} |"
        )
    total_duration = sum(row["duration"] for row in rows)
    total_cuts = sum(row["cuts"] for row in rows)
    print(
        f"\nTotal: {total_cuts} scene changes over {duration_clock(total_duration)} "
        f"({total_cuts / total_duration * 60:.1f} cuts/min)."
    )


if __name__ == "__main__":
    main()
