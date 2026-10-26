---
name: mediastorm-motion-graphics
description: Design CapCut parameter animation, easing, point-tracked labels, frame-grid number flashes, timers, and information packaging. Use for motion that communicates or guides attention, not for planar perspective replacement or story structure.
metadata:
  short-description: Design motion graphics and tracked labels
  status: provisional-unverified-audiovisual
---

# MediaStorm Motion Graphics

Use motion to clarify information, guide attention, and land changes on a stable frame grid.

## Core workflow

1. Define the informational purpose, start and end composition, and the exact action time before adding keyframes.
2. Treat keyframed values as segment-local. Check whether splitting or replacing media reset parameters that looked shared.
3. Combine scale and position deliberately for push-ins and pans. Align the relevant start/end times and inspect each parameter's interpolation rather than counting keyframe markers.
4. Use easing to match the desired energy. If parameters intentionally diverge, record the reason and inspect the composite motion.
5. For point-tracked labels, choose a stable, high-contrast feature that remains visible, enable only the dimensions the label should inherit, and trim unused footage before tracking.
6. Put fast number changes on the project frame grid. Keep the final value visible long enough to read, and accumulate integer frames rather than rounded milliseconds.
7. Pair entrance and exit animations with consistent style, position, and slight overlap only when the package benefits from that continuity.
8. Check occlusions, safe areas, readability, neighboring animations, and whether transitions or overlays make the test target impure.

## Remotion / TypeScript 适配

- Drive values with `interpolate` + `Easing.bezier`/`Easing.spring`; read `useCurrentFrame()` and `useVideoConfig().fps`.
- Use `@remotion/shapes` for rects/circles/stars, `@remotion/layout-utils` to measure/fit text, and `@remotion/motion-blur` for blur.
- Number flashes: derive the current value from `Math.floor(frame / framesPerValue)`, then hold the final value on the frame grid.
- Remotion has no point-tracking panel; feed tracked coordinates from external data into transforms.

## Boundaries

- Course 08 covers keyframes and easing only; point-tracked labels and number flashes are in course 12, timers in course 15, and planar tracking in course 13. Do not merge them.
- Course values such as two-frame flashes, 0.4-second movement, 45% opacity, or one-second openings are case parameters, not universal presets.
- Ordinary keyframes do not provide planar perspective solving. Route planar surfaces to `mediastorm-compositing-tracking`.
- Prefer current CLI contracts for `keyframe`, `add-text`, `image-anim`, and `text-anim`; alpha keyframes are not a reliable fade mechanism in the previously verified macOS path.
- JSON writes and FFmpeg proxy previews do not prove the animation looks right in CapCut.
- Treat this skill as provisional until continuous course audio/video review is completed. The 2-second picture pass verified panel values and curve names, not motion smoothness.

Read [references/motion-design.md](references/motion-design.md) for course-derived patterns, failure checks, and timecodes.
