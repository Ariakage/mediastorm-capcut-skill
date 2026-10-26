#!/usr/bin/env python3
"""Validate evidence accounting without opening or staging paid course materials."""
import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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
                available={s["file"] for s in manifest["sheets"]}
                for sheet in visual["reviewed_sheets"]:
                    if sheet not in available or not (manifest_path.parent/sheet).is_file():
                        errors.append(f"{row['id']}: reviewed sheet absent: {sheet}")
        if review["complete_multimodal_review"]:
            if sub["state"] != "read_all_cues" or review["continuous_video"]["state"] != "reviewed_full" or review["audio_listening"]["state"] != "reviewed_full":
                errors.append(f"{row['id']}: full multimodal completion lacks actual viewing/listening")
    tracked=subprocess.check_output(["git","ls-files","-z"],cwd=ROOT).decode().split("\0")
    for name in tracked:
        if name.startswith("cheese/") or Path(name).suffix.lower() in {".mp4",".mov",".wav",".mp3",".srt"}:
            errors.append(f"Course/media-like file in Git index: {name}")
    return errors


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger",type=Path,default=ROOT/"progress/course-ledger.json")
    args=parser.parse_args()
    data=json.loads(args.ledger.read_text())
    problems=check(data)
    if problems:
        for problem in problems: print("ERROR:",problem)
        raise SystemExit(1)
    print(f"PASS: {len(data['lessons'])} lessons; evidence states consistent; no course media in Git index")
