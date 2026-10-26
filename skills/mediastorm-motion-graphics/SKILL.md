---
name: mediastorm-motion-graphics
description: Design CapCut parameter animation, easing, point-tracked labels, frame-grid number flashes, timers, and information packaging. Use for motion that communicates or guides attention, not for planar perspective replacement, keying, or story structure.
metadata:
  short-description: Design motion graphics and tracked labels
  status: provisional-unverified-audiovisual
---

# MediaStorm Motion Graphics

Use motion to clarify information, guide attention, and land changes on a stable frame grid. This skill covers four related but distinct jobs: parameter animation, point-tracked labels, number flashes, and timer/package builds.

## When to use

- A push-in, pan, or composition change needs scale/position keyframes and easing.
- A label must follow a moving feature without inheriting unwanted scale or perspective.
- A number, price, counter, or timer must change quickly and remain readable.
- A packaging element needs entrance/exit animation, a mask window, or a preset.
- A motion design must be handed to Remotion or implemented in TypeScript.

Do not use this skill for planar tracking (route to `mediastorm-compositing-tracking`), keying/masks, color grading, or story order.

## Inputs to establish

- The informational job: what should the viewer notice, read, or understand?
- The start/end composition, the exact action time, and the project frame rate.
- The target: a segment-local parameter, a tracked label, a number flash, or a timer.
- Whether the motion is decorative or carries meaning; if decorative, why it is needed.
- The delivery frame rate and whether the final motion will be judged at normal speed.

## Workflow

1. Define the purpose and the exact action time before adding keyframes. A push-in should have a target composition, not just “make it bigger”.
2. Treat keyframed values as segment-local. Splitting or replacing media can reset parameters that looked shared [course evidence][08 01:00–02:40].
3. For a push-in, combine scale and position deliberately. The course’s mobile-push example ends at scale `286%`, position X `0`, Y `-2219`; the start is scale `100%`, position `0/0`. The 354% and 214% readings are dragging intermediates, not final presets [sampled stills][08 05:58.5 / 06:22.5].
4. Open the keyframe speed-curve panel and inspect all three curves: scale, position X, and position Y. The panel ranges are scale `4.00–0.00`, X `768–-768`, Y `432–-2160`; the default is linear [sampled stills][08 07:59.0 / 08:20.5].
5. Apply easing consistently. The course preset list is `无 / 缓入 / 二次方缓入 / 三次方缓入 / 缓出 / 二次方缓出 / 三次方缓出 / 缓动 / 二次方缓动 / 三次方缓动 / 回弹展开 / 线性` (None / Ease In / Quadratic In / Cubic In / Ease Out / Quadratic Out / Cubic Out / Ease In-Out / Quadratic In-Out / Cubic In-Out / Bounce Out / Linear). The demo selects quadratic in for all three curves [sampled stills][08 09:18.5].
6. For point-tracked labels, choose a stable, high-contrast feature that remains visible. Enable only the dimensions the label should inherit; the course turns off `缩放/距离` (scale/distance) at 08:26 so the text follows position only [sampled stills][12 08:24–08:26].
7. Trim unused footage before tracking. Tracking the whole clip wastes computation and makes the label harder to control [course evidence][12 09:19–10:57].
8. For number flashes, build short text segments on the frame grid. The course’s design unit is about 2 frames/segment, but the finished frame grid shows 8 values/15 frames (about 0.50s) in the first run and 6 values/11 frames (about 0.37s) in the second, with each value held 1–3 frames [sampled stills][12 12:48–14:35]. Do not repeat “2 frames” as a literal result; verify the finished grid.
9. For a timer/package, build the structure explicitly: black-screen source, rectangular mask, corner radius, stroke, shadow, opacity, repeated background blocks, text numerals, shadow, entrance animation, and offset ladder. The course timer uses a `538×540` mask, radius 27, white stroke 2, shadow `100/19/0/0`, image opacity 45%, text size 15, text scale 134%, text shadow `45/16/0/0` [sampled stills][15 16:30–19:47].
10. Pair entrance and exit animations with consistent style, position, and slight overlap only when the package benefits. The course pairs upward exit/entrance at about `0.4s` panel setting; the visible overlap in the preview is about 5 frames (about 0.17s) [sampled stills][12 14:35–17:29].
11. Check occlusions, safe areas, readability, neighboring animations, and whether a transition or overlay makes the test target impure.
12. Validate in the actual player at normal speed. A still frame cannot prove easing feel, number readability, or tracking stability.

## Decision rules

- If the motion has no informational job, remove it; “looks dynamic” is not a job.
- If scale and position are animated together, align their start/end times and check both curves; a scale-only ease next to a linear position move reads as two events.
- If a keyframe marker looks solid on the segment, still inspect the parameter row; the course’s 06:22.5 view shows a hollow scale diamond and a solid position diamond, a conflict to verify, not a preset [pending verification].
- For tracked labels, position-only is the default; add scale/distance only when the label should inherit depth.
- For number flashes, use integer frame math and hold the final value long enough to read.
- If a timer/package uses a preset, record the preset and the project frame rate; a preset saved at another size may not fit.
- If a motion effect is only visible in the proxy preview, do not approve it; check the interface/export.

## CapCut execution notes

- `capcut keyframe` supports batch and `linear/ease-in/ease-out/ease-in-out/hold`; easing needs adjacent keyframes of the same property, and hold needs a following keyframe.
- Alpha keyframes are not a reliable fade mechanism on the previously verified macOS path; use an animation material or `image-anim` where appropriate.
- `add-text`, `image-anim`, and `text-anim` have CLI contracts, but the visual result still needs CapCut acceptance.
- For a tracked label, the course uses the text/tracking panel; do not assume CLI keyframes equal the CapCut tracking solver.

## Remotion / TypeScript Adapter

- Drive values with `interpolate` + `Easing.bezier`/`Easing.spring`; read `useCurrentFrame()` and `useVideoConfig().fps`.
- Use `@remotion/shapes` for rects/circles/stars, `@remotion/layout-utils` to measure/fit text, and `@remotion/motion-blur` for blur.
- Number flashes: derive the current value from `Math.floor(frame / framesPerValue)`, then hold the final value on the frame grid.
- Remotion has no point-tracking panel; feed tracked coordinates from external data into transforms.

## Failure conditions

- The action time is unknown and the keyframes are placed by feel.
- Scale and position curves are mismatched.
- A tracking label inherits scale or perspective unintentionally.
- A number flash is designed in milliseconds and drifts over the edit.
- The final value does not hold long enough to read.
- A timer package is built from a preset without checking size/frame rate.
- The motion is approved from a still or a proxy preview.

## Acceptance checklist

- [ ] The motion has a stated informational job.
- [ ] Start/end compositions and action times are recorded.
- [ ] Scale/position curves are aligned and eased consistently.
- [ ] Tracked labels use only the intended dimensions.
- [ ] Number flashes are on the frame grid; final value holds.
- [ ] Timer/package geometry and text are checked at the target size.
- [ ] Occlusion, safe area, and neighboring animations are checked.
- [ ] The result is watched at normal speed in CapCut/export.

## Output contract

Return: the motion job, exact keyframe timing, parameter values, easing choice, tracking dimensions, frame-grid math, and what was verified vs still pending. Do not present a course preset as a universal default.

Read [references/motion-design.md](references/motion-design.md) for course-derived patterns, failure checks, and timecodes.
