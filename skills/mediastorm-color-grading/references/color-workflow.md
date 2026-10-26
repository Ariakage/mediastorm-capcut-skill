# Technical Restoration and Color-Grading Workflow

## Order

1. `[course evidence][11 01:27–03:36]` Identify the footage's true Log/gamut, then choose a matching technical restoration; a gray-looking image does not mean a LUT can be applied arbitrarily.
2. `[course evidence][11 01:27–03:36]` Already-restored footage must not be restored again.
3. `[course evidence][11 03:36–05:44]` Judge brightness, saturation, and hue first, then use zone tools such as highlights/shadows.
4. `[course evidence][11 05:44–06:30]` An independent adjustment layer makes on/off comparison easy; adjustments inside a clip are not physical destruction of the original footage.
5. `[course evidence][11 06:30–08:31]` Color wheels handle casts and brightness by luminance zone, judged against the target and reference.
6. `[course evidence][16 10:19–12:40]` In RGB curves the horizontal axis is input and the vertical axis is output; an S-curve affects range and detail and must not be applied unconditionally.
7. `[course evidence][16 12:40–13:28]` Smart color adjustment / color cloning serves only as a matching starting point; still check skin tones, brightness, scene lighting, and double restoration.

## Reading the Scopes

- `[course evidence][11 08:31–10:41]` The waveform displays luminance distribution according to horizontal position in the image; RGB components help observe white balance only when a neutral reference actually exists.
- Non-alignment of the three channels does not automatically equal a white-balance error.
- `[course evidence][11 10:41–12:07]` The vectorscope's direction and distance from center can help judge hue/saturation; intentional color distributions should not all be pulled back to center.
- Whether clipping at the top of a scope can be recovered still requires considering the signal range and the original footage, and cannot be asserted outright.

## 2026-10 Sampled Stills Review Supplement

- `[sampled stills][11 02:14–02:24]` The LUT library import shows “正在导入素材 0/86” (Importing material 0/86); built-in style LUTs include `黑白.cube` (Black & White), `绿谷.cube` (Green Valley), `罗马.cube` (Rome), `曼哈顿.cube` (Manhattan), and others; after clicking `黑白.cube` at 02:18 the image turns black and white, showing that a style LUT cannot serve as technical restoration.
- `[sampled stills][11 02:22]` `XH2S_FLog2_FGamut_to_ETERN…_BT.709_33grid_V.0.90.cube` is selected (partially visible) and applied to Apple Log footage as a “mismatch” example.
- `[sampled stills][11 03:04.4–03:06.2]` At 03:04.4 the card is `C-Log3 To Rec709.cube`; the transition frame at 03:05.6 reveals both `C-Log3 To Rec709.cube` and `AppleLog2 To R…`; from 03:06.2 `AppleLog2 To Rec709.cube` is fully displayed. The old note's “same screen” only occurs on the transition frame; the correct LUT starts at 03:06.2.
- `[sampled stills][11 03:50–03:52]` Basic-panel case values: tint -5, saturation 12, vibrance 4, brightness 7, contrast -4, highlights 8, shadows -6, whites 7, blacks 0, light 0, effect 0, sharpen 5, clarity 0. Note that “明度” (Lightness) is a group heading, not a standalone slider.
- `[sampled stills][11 04:10–04:14]` At brightness -25 the image is nearly black, and at +50 it is overexposed overall; at `04:28–04:32` highlights 47 / shadows 0 → highlights 47 / shadows -6 → highlights 0 / shadows 12; at `04:40` saturation -50 makes the image black and white.
- `[sampled stills][11 05:16–05:18]` HSL green ring: hue 100, saturation -28, lightness 0; a single color can be adjusted independently.
- `[sampled stills][11 06:26–06:32]` The `log色轮` (Log Color Wheel) tab reads “阴影/中间调/高光/偏移” (Shadows / Midtones / Highlights / Offset); the `一级色轮` (Primary Color Wheel) shows “暗部/中灰” (Shadows / Mid-gray), differing from the narration's wording; the lower row's “高光/偏移” (Highlights / Offset) is not fully in frame, [pending verification].
- `[sampled stills][11 07:42–07:46]` Dragging the highlight-wheel anchor toward orange-red plus pushing the luminance slider up changes the values from `0.18/-0.02/-0.38` to `0.41/0.22/-0.15`.
- `[sampled stills][11 08:42–09:58]` Three scopes: RGB parade, waveform (scale 1023/512/0), and vectorscope; a flat top only means that area clips on the scope, and it cannot be directly asserted that the original information is unrecoverable.
- `[sampled stills][11 10:46–11:42]` Offset correction: horse-ranch footage `0.02/0.00/-0.10 → 0.07/0.01/-0.30`; purple-red mountain `-0.15/0.00/-0.30 → -0.17/0.00/-0.31`; the vectorscope ring is labeled RED/YELLOW/GREEN/CYAN/BLUE/MAGENTA.
- `[sampled stills][16 11:00–12:34]` The RGB curve's horizontal axis is “画面原亮度” (Original Image Luminance) and the vertical axis is “调整后亮度” (Adjusted Luminance), with the 45-degree line meaning no change; pressing down the lower left and lifting the upper right forms an S-curve; individual R/G/B channels can perform color balance. The burned-in subtitle states explicitly “往上拖变亮、往下拖变暗” (drag up to brighten, drag down to darken).
- `[sampled stills][16 12:56.5–13:18]` Color cloning `强度 80` (Strength 80), color correction `强度 80` (Strength 80), smart color adjustment `场景 通用/强度 80` (Scene: General / Strength 80), LUT `强度 100/肤色保护 0` (Strength 100 / Skin Tone Protection 0); color cloning is a matching starting point, not a final guarantee.
- `[sampled stills][16 10:30.5]` In the basic color parameters, temperature / tint / saturation / vibrance are all visibly 0; the brightness slider value is clipped by the panel's lower edge.

## Known Corrections

- `[sampled stills][11 03:04.4–03:06.2]` Apple Log2 and C-Log3 LUTs appearing on the same screen is a wrong-matching demonstration, not a correct pairing; the correct LUT is fully displayed only from 03:06.2.
- `[sampled stills][16 12:31–12:34]` The burned-in subtitle is “往上拖**变亮**” (drag up to **brighten**); the SRT's “往上拖变暗” (drag up to darken) is a misrecognition, and the old note's question about “the course contradicting itself” can be closed.
- `[inference]` Color acceptance order: technical input → exposure/white balance → shot matching → style → combined motion and scope re-check.

## Failure Conditions

- Applying a LUT automatically while the Log source is unknown.
- Repeated technical restoration of the same footage.
- Forcing the RGB channels to align when there is no neutral object.
- Treating an artistic cast as an error.
- Matching on a single frame but failing on motion or adjacent shots.
- Writing the course case's parameters up as a fixed style for all projects.

## Currently Pending Verification

The correct restoration operations in Lesson 11, the continuous scope changes, and the before/after effects of the curves/matching in Lesson 16 still require continuous-video comparison.
