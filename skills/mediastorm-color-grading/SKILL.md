---
name: mediastorm-color-grading
description: Restore Log footage, read exposure and color, use adjustment layers, scopes, curves, and shot matching for CapCut or Remotion projects. Use for technical correction and creative grade decisions, not for compositing, tracking, or export settings.
metadata:
  short-description: Correct, match, and grade color
  status: provisional-unverified-audiovisual
---

# MediaStorm Color Grading

Correct the technical input before creating a look, then verify the grade across the moving shot and neighboring shots. This skill separates restoration, balance, contrast, and style; it does not treat a LUT or a reference still as a universal preset.

## When to use

- Log/RAW footage looks flat, or the source profile/color space is unknown.
- A project needs exposure, white balance, contrast, saturation, HSL, or color-wheel work.
- Shots from different cameras or lighting need matching.
- A curve, LUT, or color-clone/smart-grade tool is being considered.
- A grade looks right in a still but wrong in motion or on a neighboring shot.

Do not use this skill for keying, masks, tracking, or export/bitrate decisions; route those to the matching child skill.

## Inputs to establish

- Camera/profile, Log curve, color space, exposure, and whether the clip is already restored.
- The look reference: a still, a film, a previous shot, or a verbal description.
- Delivery color space and whether the target is SDR Rec.709 or another pipeline.
- The actual shot content: skin, neutral objects, known whites/blacks, mixed lighting.
- Whether the grade is technical restoration, shot matching, or a stylistic look.

## Workflow

1. Identify the real camera profile and Log curve. Do not choose a LUT because the image “looks flat”.
2. Apply a matching technical restoration first. The course demonstrates an incorrect pairing: a Fuji F-Log2 → ETERNA LUT on Apple Log footage at 02:22, then a `C-Log3 To Rec709.cube` card at 03:04.4, a transition frame at 03:05.6, and the correct `AppleLog2 To Rec709.cube` from 03:06.2 [sampled stills][11 02:22–03:06.2]. The mismatch is an instructional example, not a valid pairing.
3. Prefer an independent adjustment layer or a separate grade stage when available. It allows on/off comparison and protects the original; an in-clip grade is not physically destructive, but it is harder to compare [course evidence][11 05:44–06:30].
4. Establish the big four before style: exposure, white balance, contrast, saturation. In the course case, base values include tint -5, saturation 12, vibrance 4, brightness 7, contrast -4, highlights 8, shadows -6, whites 7, blacks 0 [sampled stills][11 03:50–03:52].
5. Use targeted controls when the problem is regional. The course demonstrates brightness -25/+50, highlights 47 with shadows 0/-6, and shadows 12 on their own [sampled stills][11 04:10–04:32].
6. Use HSL when one color is the problem. The course selects the green ring and sets hue 100, saturation -28, lightness 0 [sampled stills][11 05:16–05:18].
7. Understand color-wheel labels. The `log色轮` (Log Color Wheel) tab reads `阴影/中间调/高光/偏移` (Shadows/Midtones/Highlights/Offset); the `一级色轮` (Primary Color Wheel) shows `暗部/中灰` (Shadows/Mid-gray), which does not match the narration. The lower row was not fully in frame [pending verification][sampled stills][11 06:26–06:32].
8. Read the wheels as hue/saturation direction plus a luminance slider. The course’s highlight wheel moves from `0.18/-0.02/-0.38` to `0.41/0.22/-0.15` when the anchor is pushed toward orange-red and the luminance slider is raised [sampled stills][11 07:42–07:46].
9. Use scopes as quantitative references, not decoration. The course shows an RGB parade, a waveform with 1023/512/0 marks, and a vectorscope. A flat top at 1023 means the signal is clipping at the scope; it does not by itself prove the original information is unrecoverable [sampled stills][11 08:42–09:58].
10. Correct a cast with the offset wheel after reading the scope direction. The course moves a horse shot from `0.02/0.00/-0.10` to `0.07/0.01/-0.30`, and a mountain shot from `-0.15/0.00/-0.30` to `-0.17/0.00/-0.31` [sampled stills][11 10:46–11:42].
11. Use curves deliberately. The RGB curve’s horizontal axis is `画面原亮度` (Original Image Luminance) and the vertical axis is `调整后亮度` (Adjusted Luminance), with the 45-degree line meaning no change. Drag up to brighten, down to darken; a lower-left shadow point plus an upper-right highlight point creates an S curve [sampled stills][16 11:00–12:34]. The burned-in subtitle confirms “drag up to brighten” (`往上拖变亮`); the SRT’s “drag up to darken” is a misrecognition.
12. Use color clone/smart grade as a starting point. The course uses color clone strength 80, color correction strength 80, smart grade scene “General” strength 80, and LUT strength 100 with skin protection 0 [sampled stills][16 12:56.5–13:18]. Check skin, lighting, blacks, highlights, and whether a second technical restoration was applied.
13. Compare before/after, neighboring shots, scopes, and normal-speed playback. Reject a single-frame match that fails in motion.

## Decision rules

- If the source profile is unknown, do not apply a technical LUT; identify it first.
- If the clip has already been restored, do not restore it again.
- If the problem is regional, use highlights/shadows/HSL/qualifier; do not flatten the whole image.
- If the vectorscope shows an intentional color separation, do not drag it to the center by reflex.
- If a curve S-shape clips highlights or crushes shadows, reduce it; contrast is not a free operation.
- If a smart grade “looks close”, still check skin and known neutrals; it is a starting point.
- If a scope shows clipping, check the signal range and the original media before claiming the data is gone.
- If the grade only works in a still, reject it; check motion and neighbors.

## CapCut execution notes

- The course uses a separate adjustment layer (`调节`) for comparison; keep the original, restoration, and look stages distinct.
- LUT strength and skin protection are separate controls; a technical LUT should not be used as a style LUT.
- The color panel tabs include `基础 / HSL / 曲线 / 色轮 / 蒙版` (Basic/HSL/Curves/Color Wheels/Mask); do not assume every tab is available in every version.
- Export color space is a delivery decision; route it to `mediastorm-delivery-handoff`.

## Remotion / TypeScript Adapter

- `colorCorrection()` performs exposure, white balance, shadows/highlights, contrast, saturation, and vibrance in one WebGL pass.
- `lut()` applies a `.cube` LUT from its text content; keep LUTs in `public/` or import them as text.
- `@remotion/effects` adds `glow`, `lightLeak`, `vignette`, and related looks; these are style, not technical restoration.
- Remotion has no waveform/vectorscope UI. Use external scopes or a custom Canvas/WebGL analysis.

## Failure conditions

- A LUT is applied without identifying the source profile.
- A technical restoration is applied twice.
- A global brightness change is used for a regional problem.
- A curve clips highlights or crushes shadows.
- A smart grade is accepted without checking skin or a known neutral.
- A scope reading is over-interpreted as “data lost”.
- The grade is approved from a still, not from motion and neighbors.

## Acceptance checklist

- [ ] Source profile/Log/color space identified.
- [ ] Technical restoration applied once and verified.
- [ ] Exposure/white balance/contrast/saturation set before style.
- [ ] Regional tools used for regional problems.
- [ ] HSL/color wheel changes have a stated target.
- [ ] Scopes checked against known content, not in isolation.
- [ ] Curve direction and clipping checked.
- [ ] Smart grade/clone checked for skin and neutral objects.
- [ ] Before/after and neighboring shots compared in motion.
- [ ] Delivery color space handed to the delivery skill.

## Output contract

Return: the source diagnosis, the restoration/LUT used, the base and regional values, the scope reading, the style stage, what was compared, and the remaining uncertainties. Distinguish technical restoration from style, and case values from reusable parameters.

Read [references/color-workflow.md](references/color-workflow.md) for decision order, scope interpretation, and timecodes.
