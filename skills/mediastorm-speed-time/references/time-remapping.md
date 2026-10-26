# Speed Changes and Time Remapping

## First distinguish the purpose

- `[course evidence][09 01:26–02:38]` Trimming and speed changes are different; a constant-speed change must consider the source range, target duration, and downstream position together.
- `[course evidence][09 05:01–06:21]` Slightly extending the duration and artistically reconstructing time are not the same goal; do not slow material down to an unnatural degree just to fill a gap.

## Source frame-rate screening

- `[course evidence][09 02:38–05:01]` Extremely slow motion from low frame rates lacks real motion samples; `帧融合` (frame blending) may ghost, and optical flow may warp.
- `[inference]` Without frame interpolation, if the playback multiplier is `v`, the source frame rate is `Fs`, and the output frame rate is `Fo`, then `Fs × v ≥ Fo` can serve as the first screening test for unique-frame supply.
- This formula does not guarantee shutter blur, exposure, encoding quality, motion complexity, or optical-flow results.

## Speed curves

- `[course evidence][09 06:21–09:25]` Design around the action peak or the transition: first locate the key points, then arrange acceleration, peak slow motion, and recovery.
- `[course evidence][09 09:25–10:50]` Automatic beat-synced speed changes are only candidates; first judge whether the content needs them and avoid overuse.
- The 0.3× and 0.1× in the example are not default values; they must be checked against the source frame rate and the actual picture.

## Tool boundary

- `[tool boundary][capcut-cli 0.31.1]` `speed <project> <id> <multiplier>` applies a constant speed multiplier.
- `[tool boundary][capcut-cli 0.31.1]` `keyframe` supports position/scale/rotation/alpha/volume and basic easing; ordinary keyframes are not the same as the course's curve speed.
- After changing the speed, check the relationship between `source_timerange` and `target_timerange`; insufficient source produces a black tail or a silent tail.
- Downstream clips, subtitles, audio, keyframes, and music sync must all be rechecked.

## 2026-10 visual review supplement

- `[sampled stills][09 01:55.5 / 02:06.5 / 03:36.5]` Regular speed change reads `1.97x` (4.2s), `0.46x` (9.1s), `0.10x` (41.4s); the slow-motion readings basically satisfy “duration ≈ source duration ÷ multiplier”, while the fast-motion readings show inconsistency during adjustment.
- `[sampled stills][09 02:56–03:18]` The 30fps grid illustration runs `1.0x → 0.9x → 0.5x`, with blank cells and “repeated frame” cells; this directly explains the stutter at 0.1x. `智能补帧` (Smart frame interpolation) offers `帧融合` (default, faster, prone to ghosting) and `光流法` (optical flow; slower, better results).
- `[sampled stills][09 04:36.5]` The camera monitor reads `4096×2160`, `800 fps` (720/750/780/800 selectable, 24x/25x/26x), ISO400, Rec.709, 4800K; this is the camera menu, not the CapCut sequence frame rate. The instructor separately recommends shooting at 60/120fps in production.
- `[sampled stills][09 07:10.5 / 08:14.5 / 09:04.5]` The curve editor spans 4 seconds, its vertical axis is `10x/1x/0.1x`, and it has three sets of handles; a flat-topped curve can produce “accelerate–constant–decelerate”. Preset names include `无/自定义/蒙太奇/英雄时刻/子弹时间/跳跃/闪进/闪出` (None / Custom / Montage / Hero moment / Bullet time / Jump / Flash in / Flash out).
- `[sampled stills][09 09:52–10:06]` The speed-change beat presets are `无/闪光/摇摆模糊/闪黑变焦/复古运镜/彩虹` (None / Flash / Sway blur / Flash-black zoom / Retro camera move / Rainbow); the example selects `闪光` (Flash), with music source `Master`, beat frequency `踩节拍II` (Beat Sync II), and speed-change rate `一般` (Normal).
- `[sampled stills][08 09:18.5]` Project settings show `草稿帧率：30.00帧/秒` (draft frame rate: 30.00 frames/second); the source video is 1920×1080 at 29.97fps. When checking frame supply, use the actual output frame rate as the basis.

## Acceptance

1. Source-material frame rate and motion complexity have been recorded.
2. The purpose of the speed change is clear and not merely filling a gap.
3. The entire slow-motion section is checked at normal output speed, not replaced by sparse frame sampling.
4. Optical-flow/frame-blending artifacts, motion judder, and out-of-range tails have been checked.
5. Music or action peaks are actually aligned, not judged only from timecodes.

## Currently pending verification

The before/after slow motion, optical-flow defects, and action-peak-to-music alignment in lesson 09 still require continuous video and original-audio review.
