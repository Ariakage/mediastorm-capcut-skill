# Parameter Animation and Information Motion Design

## Push-in and easing

- `[course evidence][08 01:00–02:40]` Parameters belong to the clip; after the same material is cut into two segments, they do not automatically share all settings.
- `[course evidence][08 02:40–04:39]` First determine the start and end of the motion and the target composition, then add keyframes.
- `[course evidence][08 04:39–07:19]` Post-production push-ins often change scale and position at the same time; the start and end times of the related parameters should be aligned.
- `[course evidence][08 07:19–10:01]` Easing the scale while X/Y remain linear causes the rhythm to fall out of sync; check the curves parameter by parameter. When the offset is intentional, record the design intent.

## Attribution clarification

- `[sampled stills]` All 82 index pages of lesson 08 cover only **keyframes, scale/position parameters, and curve easing**; they do not cover point-tracking labels, number flicker, or timers.
- Point tracking/text tracking, device labels, number flicker, and in/out animations are in lesson **12**; timer packaging is in lesson **15**; planar tracking is in lesson **13**. Do not present the four as one capability.

## Keyframes and easing (08)

- `[sampled stills][08 05:58.5 / 06:22.5]` The phone push-in example ends at scale `286%`, position X `0`, Y `-2219`; the start is scale `100%`, position `0/0`. The 354% at 01:46.5 and the 214% at 05:12.5 are intermediate drag values, not the final presets.
- `[sampled stills][08 07:59.0 / 08:20.5]` The right-click menu reads “显示关键帧变速曲线” (show keyframe speed curves); the panel shows all three curves at once—scale, position X, and position Y—with scales of `4.00–0.00` for scale, `768–-768` for X, and `432–-2160` for Y, all linear by default.
- `[sampled stills][08 09:18.5]` Complete easing preset list: `无 / 缓入 / 二次方缓入 / 三次方缓入 / 缓出 / 二次方缓出 / 三次方缓出 / 缓动 / 二次方缓动 / 三次方缓动 / 回弹展开 / 线性` (None / Ease In / Quadratic Ease In / Cubic Ease In / Ease Out / Quadratic Ease Out / Cubic Ease Out / Ease In-Out / Quadratic Ease In-Out / Cubic Ease In-Out / Bounce Out / Linear); the example selects `二次方缓入` (Quadratic Ease In) and changes all three curves to the same preset.
- `[pending verification][08 06:22.5]` The diamond on the scale row looks hollow and the position row looks solid, which superficially conflicts with “the ending scale keyframe already exists”; higher resolution or continuous-operation review is needed.

## Point-tracking labels (12)

- `[sampled stills][12 08:24–08:26]` The tracking panel has two switches, “缩放/距离” (scale/distance); this example turns both off, so the text follows position only and does not grow or shrink with the person's distance.
- `[sampled stills][12 06:19–08:49]` Choose features that are stable, high-contrast, and unlikely to disappear; when only a position label is needed, avoid unintentionally inheriting scale or perspective.
- `[sampled stills][12 09:19–10:57]` Trim the usable shot range before tracking; for moving labels, check mutual occlusion and the readability of important information.

## Number flicker and timers

- `[sampled stills][12 12:48–14:35]` The design unit of number flicker is a short text segment; the spoken commentary says “about 2 frames, 8–10 changes”, but the finished film's frame grid only reliably resolves the first segment's 8 values/15 frames (about 0.50s) and the second segment's 6 values/11 frames (about 0.37s), with each value lasting 1–3 frames—**not strictly 2 frames per segment**. The final segment holds the final value.
- `[inference]` Convert durations into whole frames using the project frame rate to avoid cumulative millisecond drift; the last frame or final segment must hold long enough to read. Verify against the finished film's frame grid; do not substitute the spoken numbers.
- `[sampled stills][12 14:35–17:29]` Paired upward exits/entrances, same-style positions, and local masks form a scrolling window; the panel is set to about `0.4s`, but in the preview the two number segments visibly overlap on screen for about 5 frames (about 0.17s). 0.4s is the setting value, not the visible overlap duration.
- `[sampled stills][12 10:20 / 12:52 / 13:31]` Device label: font `JY-Glee`, font size 15, scale 28%, white text, shadow 20% (the shadow value comes from the text panel at 06:48–06:56). Price text: font `ZY Vigorous-Medium`, font size 15, bold, centered, scale 199%, X0 / Y2609, white text, black stroke width 12; the shadow opacity reads successively 27%→50%→8%→10%, with the final value [pending verification].
- `[sampled stills][15 16:30–19:47]` Timer structure: black-screen material + rectangular mask `538×540`, corner radius 27, white stroke 2, shadow `100/19/0/0`, image opacity 45%; text font size 15, scale 134%, text shadow `45/16/0/0`; duplicate six background blocks + six number texts + upward slide + reverse stair-step offset + two compound clips, and finally save as “我的预设2” (My Preset 2).
- `[sampled stills/subtitle conflict][15 18:49–18:56]` The animation panel clearly reads `0.5s`, while the spoken commentary/subtitle at the same frame says “about 0.3 seconds”; until listening verification or confirmation from the original project, 0.3 seconds cannot be treated as the final parameter.

## Tool boundary

- `[tool boundary][capcut-cli 0.31.1]` `keyframe` supports batch and `linear/ease-in/ease-out/ease-in-out/hold`; easing requires adjacent keyframes on the same property, and hold requires a subsequent keyframe.
- Previous capcut-edit verification records show that alpha keyframes are unreliable on the macOS path; when fades are needed, evaluate `image-anim` or the animated-material path first.
- `image-anim`, `text-anim`, and `add-text` all have CLI contracts, but this combined Skill has not yet performed CapCut UI acceptance of their visual effects.
- Check the in/out animations, transitions, and covering tracks of adjacent clips to avoid mistaking a neighboring effect for the target animation.

## Acceptance

- The composition's start and end are correct, and the motion is readable.
- Each parameter's interpolation matches the intent.
- Labels do not obscure the subject, subtitles, or platform UI.
- Number changes are aligned to the frame grid, and the final value holds.
- The animation is still visible after reopening CapCut; proxy preview is not used as the sole evidence.
