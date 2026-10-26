---
name: mediastorm-speed-time
description: Evaluate and design constant-speed changes, slow motion, speed ramps, and source-frame-rate constraints for CapCut or Remotion edits. Use when changing time or motion feel, not for ordinary cuts, keyframed transforms, or story order.
metadata:
  short-description: Design speed changes and slow motion
  status: provisional-unverified-audiovisual
---

# MediaStorm Speed Time

Reconstruct time only when the source material and the editorial purpose can support it. This skill decides whether a speed change is a small repair, a rhythmic accent, or an expressive time reconstruction, and whether the source has enough frames.

## When to use

- A clip needs a constant speed change, a slow-motion passage, or a speed ramp.
- A gap needs a small timing repair, or an action peak needs a deliberate slow passage.
- The source frame rate may be too low for the requested slow motion.
- Frame blending, optical flow, or duplicated frames need a risk check.
- A speed change shifts downstream clips, captions, keyframes, or music sync.

Do not use this skill for ordinary cuts, static keyframe animation, or music-led rhythm decisions; route those to the matching child skill.

## Inputs to establish

- Source frame rate, resolution, shutter/exposure, motion complexity, and the exact source range.
- Target duration, output frame rate, and downstream timeline impact.
- The purpose: repair a gap, emphasize an action, reconstruct time, or match a beat.
- Whether frame interpolation is allowed, and whether audio pitch should be preserved.

## Workflow

1. Distinguish trimming from speed change. A trim changes the in/out point; a speed change alters the source-to-timeline mapping.
2. Calculate the source range, target duration, and output frame rate before touching the clip. Record the relationship between `source_timerange` and `target_timerange`.
3. Screen the source supply: `source_fps × speed ≥ output_fps` is a first-pass warning for unique-frame supply. It does not guarantee shutter blur, exposure, or motion quality [inference].
4. Choose the purpose. A small gap repair should be short and invisible; an expressive slow passage should be motivated by an action peak, a turn, or a reveal.
5. For extreme slow motion, inspect the source at normal speed first. Low-frame-rate material will repeat or drop frames; `帧融合` (frame blending) may ghost, and `光流法` (optical flow) may warp [sampled stills][09 02:56–03:18].
6. Use constant speed for a uniform change. The course reads `1.97x` (4.2s), `0.46x` (9.1s), and `0.10x` (41.4s) in its demo; the slow readings roughly satisfy “duration ≈ source duration ÷ multiplier”, while the fast readings show adjustment states [sampled stills][09 01:55.5 / 02:06.5 / 03:36.5].
7. For a curve speed, locate the action peak or transition first, then design acceleration, a peak hold or slow passage, and recovery. Do not apply a generic curve before locating the action.
8. Understand what the curve editor offers: the course shows a 4-second editor, a `10x/1x/0.1x` vertical axis, and three handle groups; a flat-topped curve can express accelerate–constant–decelerate. Presets include `无/自定义/蒙太奇/英雄时刻/子弹时间/跳跃/闪进/闪出` (None/Custom/Montage/Hero moment/Bullet time/Jump/Flash in/Flash out) [sampled stills][09 07:10.5 / 08:14.5 / 09:04.5].
9. The beat-synced speed panel offers `无/闪光/摇摆模糊/闪黑变焦/复古运镜/彩虹` (None/Flash/Sway blur/Flash-black zoom/Retro camera move/Rainbow); the course selects `闪光` (Flash) with `Master` music, `踩节拍II` (Beat Sync II), and `一般` (Normal) speed [sampled stills][09 09:52–10:06]. Treat these as candidates, not defaults.
10. Recheck all downstream effects: source overrun, black tails, silent audio tails, shifted segments, captions, keyframes, and music sync.
11. Validate at normal playback speed and at the target output frame rate. Sparse thumbnails, muted playback, or a slowed review are not acceptance.
12. If the source is 30fps and the output is 30fps, a 0.1x slow passage has only about three unique source frames per output second; the rest are duplicates or synthesized. The course’s camera monitor reading of `4096×2160`, `800 fps` is a camera menu, not the sequence frame rate [sampled stills][09 04:36.5].

## Decision rules

- If the source frame rate is too low for the requested slow motion, either change the shot design or accept the artifact; do not promise “smooth” from interpolation alone.
- If the purpose is only to fill a gap, prefer a small trim or a short speed repair over an expressive ramp.
- If the action peak is unknown, do not design the curve; find the peak first.
- If a speed change shifts downstream audio or captions, fix the timeline before approving the visual.
- If audio pitch is audible and unwanted, enable pitch preservation; check by listening.
- If a preset is used, record it as a starting point, not as the final curve.
- If the output frame rate differs from the source, re-derive the supply check with the actual output rate.

## CapCut execution notes

- `capcut speed <project> <id> <multiplier>` is a constant multiplier; it is not full curve-speed control.
- Ordinary keyframes do not prove curve-speed or frame-interpolation capability.
- After a speed change, inspect `source_timerange`/`target_timerange`; insufficient source creates a black or silent tail.
- Keep a pre-change copy or a version snapshot; speed changes are easy to iterate but hard to compare after downstream edits.

## Remotion / TypeScript Adapter

- Use `<Video playbackRate>` with `trimBefore`/`durationInFrames`; recompute `durationInFrames` in `calculateMetadata`.
- A speed ramp is multiple sequences or a custom frame→source-time mapping; Remotion has no curve-speed editor.
- `@remotion/motion-blur` adds frame-driven blur; optical-flow interpolation is external (FFmpeg or a dedicated tool).
- Verify source frame supply (`Fs × speed ≥ Fo`) before promising smooth slow motion.

## Failure conditions

- The clip is slowed beyond the source’s frame supply and the result is called smooth.
- A speed change is used to hide a story problem.
- Downstream clips, captions, keyframes, or music are not rechecked.
- Audio pitch is ignored.
- A camera menu frame rate is mistaken for the sequence/output frame rate.
- The result is approved from thumbnails or a muted preview.

## Acceptance checklist

- [ ] Source range, target duration, and output frame rate are recorded.
- [ ] The purpose of the speed change is explicit.
- [ ] Frame supply has been screened.
- [ ] Interpolation artifacts have been inspected at normal speed.
- [ ] Downstream timing is rechecked.
- [ ] Audio pitch and sync are checked.
- [ ] The final speed feel is judged at normal playback, not from stills.

## Output contract

Return: the source/target timing math, the chosen speed method, the interpolation decision, the downstream checks, what was seen vs heard, and the remaining artifact risks.

Read [references/time-remapping.md](references/time-remapping.md) for decision cards, checks, and timecodes.
