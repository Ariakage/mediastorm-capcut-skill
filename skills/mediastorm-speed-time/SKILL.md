---
name: mediastorm-speed-time
description: Evaluate and design constant-speed changes, slow motion, speed ramps, and source-frame-rate constraints for CapCut edits. Use when changing time or motion feel, not for ordinary cuts or unrelated keyframed transforms.
metadata:
  short-description: Design speed changes and slow motion
  status: provisional-unverified-audiovisual
---

# MediaStorm Speed Time

Reconstruct time only when the source material and the editorial purpose can support it.

## Core workflow

1. Distinguish trimming from speed change, then calculate source range, target duration, output frame rate, and downstream timeline impact before editing.
2. Identify whether the goal is a small timing repair, a rhythmic emphasis, or an expressive reconstruction of motion. Do not use extreme slow motion merely to fill a gap.
3. Screen source feasibility before promising smooth slow motion. Use the derived supply check `source_fps × speed >= output_fps` as a first-pass warning, then still inspect shutter blur, exposure, motion complexity, and artifacts.
4. Locate the action peak or transition point before designing a ramp. Plan acceleration, peak hold or slow passage, and recovery around that action rather than applying a generic curve.
5. Choose the frame interpolation method only after checking whether duplicated frames, blending ghosts, or optical-flow warping would damage the shot.
6. Recheck edge cases after the change: source overrun, black tails, silent audio tails, shifted downstream segments, captions, keyframes, and musical sync.
7. Validate at normal playback speed and at the target output frame rate. Do not approve slow motion from sparse thumbnails or a muted, slowed review alone.

## Remotion / TypeScript 适配

- Use `<Video playbackRate>` with `trimBefore`/`durationInFrames`; recompute `durationInFrames` in `calculateMetadata`.
- A speed ramp is multiple sequences or a custom frame→source-time mapping; Remotion has no curve-speed editor.
- `@remotion/motion-blur` adds frame-driven blur; optical-flow interpolation is external (FFmpeg or a dedicated tool).
- Verify source frame supply (`Fs × speed ≥ Fo`) before promising smooth slow motion.

## Boundaries

- `capcut speed` is a constant multiplier. Do not present it as full curve-speed control.
- Ordinary keyframes do not prove curve-speed or frame-interpolation capability.
- Course values such as 0.3× or 0.1× are case examples, not defaults.
- The frame-supply formula is an assistant-derived screening aid, not a course guarantee.
- The 2-second picture pass verified multiplier readouts, frame-grid diagrams, interpolation options, and ramp presets; smoothness, artifacts, and audio pitch remain unverified.
- Treat this skill as provisional until continuous course audio/video review is completed.

Read [references/time-remapping.md](references/time-remapping.md) for decision cards, checks, and timecodes.

Coordinate with `mediastorm-music-sound` when speed follows a beat and `mediastorm-motion-graphics` when separate transform keyframes are also changing.
