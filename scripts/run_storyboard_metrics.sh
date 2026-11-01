#!/usr/bin/env bash
set -euo pipefail
cd "/Users/ariakage/Documents/New project 10/cc/mediastorm-capcut-skill"
video="$1"
base=$(basename "$video")
id=${base:0:2}
srt=$(ls "cheese/字幕/${id} - "*.srt | head -1)
out="cheese/.analysis/storyboard-metrics/${id}"
mkdir -p "$out"
storyboard_dir="${VIDEO_STORYBOARD_DIR:-$HOME/.claude/skills/video-storyboard}"
node "$storyboard_dir/bin/storyboard.mjs" "$video" \
  --out "$out/sheet.png" \
  --transcript-file "$srt" \
  --strategy compact \
  --max-sheets 1 \
  --text --json > "$out/sheet.json" 2> "$out/log"
echo "done $id"
