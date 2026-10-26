#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p public

# 8s, 1280x720, 30fps synthetic spiral gradient.
ffmpeg -y -v error \
  -f lavfi -i "gradients=s=1280x720:d=8:r=30:speed=0.35:nb_colors=6:type=spiral:c0=0x0b0d17:c1=0x7c5cff:c2=0x2ad2ff:c3=0xff5f7e:c4=0xffb347:c5=0x4ee1a0" \
  -c:v libx264 -pix_fmt yuv420p -movflags +faststart \
  public/demo.mp4

# 24s ambient bed: two sine waves, slow tremolo, fade in/out.
ffmpeg -y -v error \
  -f lavfi -i "sine=frequency=220:duration=24" \
  -f lavfi -i "sine=frequency=330:duration=24" \
  -filter_complex "[0:a][1:a]amix=inputs=2:duration=longest,volume=0.05,tremolo=f=0.15:d=0.25,afade=t=in:st=0:d=2,afade=t=out:st=22:d=2" \
  -c:a libmp3lame -b:a 128k public/tone.mp3

echo "Wrote public/demo.mp4 and public/tone.mp3"
