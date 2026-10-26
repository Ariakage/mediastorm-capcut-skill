# Keying, Masking, and Spatial Compositing

## Keying Acceptance

- `[course evidence][10 01:46–03:55]` After AI keying, check hair, edges, background leaks, and mistakenly removed subject areas along the entire motion; even after correcting a single frame with a custom brush, still check how the algorithm propagates.
- `[course evidence][10 03:55–05:12]` Text behind a person consists of three layers: background, text, and keyed-out person; the duplicated person layer must stay time-synced with the background, and temporarily hiding the background can expose defects.
- `[course evidence][10 05:12–07:49]` Chroma keying is adjusted for lighting, wrinkles, and spill; expanding the threshold may damage the subject, and feathering cannot replace spill removal and edge recovery.
- `[course evidence][10 07:49–09:23]` A garbage mask must cover the subject's complete range of motion and cannot be judged from a single point in time.

## Blend Modes

- `[course evidence][10 09:23–10:51]` Blend modes change color mixing; they do not equal producing a precise alpha channel.
- `[course evidence][10 00:10:25]` The on-screen UI does list `强光` (Hard Light) in the brighten-related group; the subtitle must not be treated as a misrecognition, but the course's table also must not be written up as a universal parameter.
- `[tool boundary][FFmpeg local experiment]` When pure black is composited over an RGB128 gray background, `screen` and `lighten` keep the gray background, while `hardlight` outputs black. This proves that "Hard Light removes black backgrounds" cannot be written as a universal rule; it is not a CapCut test.

## Planar Tracking

- `[course evidence][13 01:58–03:37]` Watch the complete shot first and identify the target plane; text can be packaged as a compound clip to gain the planar-tracking entry point while retaining editing headroom.
- `[course evidence][13 04:02–05:23]` Choose a reference frame where the target plane has a large exposed area and sufficient features, and fit the four corners to the actual plane.
- `[course evidence][13 05:23–06:16]` In the course version, the target is not automatically re-acquired after it leaves; trim and stage its exit before it disappears, and track the reappearance as a separate segment. The actual version needs re-checking.
- `[course evidence][13 08:30–09:46]` When stretching a texture, distinguish the text proportions inside the compound clip from the outer plane's perspective, and do not break the tracking relationship.
- `[course evidence][13 09:46–10:54]` After returning from the inner packaging, separately verify that tracking is stable, the shape is correct, and the motion does not drift.

## 2026-10 Sampled Stills Review Supplement

- `[sampled stills][10 01:52]` The AI keying panel shows `羽化 0` (Feather 0) and `边缘缩放 0` (Edge Scaling 0), while `抠像描边` (Keying Outline) is collapsed and unchecked; the course never demonstrates a non-zero value throughout.
- `[sampled stills][10 02:36–03:34]` The custom keying tools are `智能画笔 / 智能橡皮 / 画笔 / 橡皮擦` (Smart Brush / Smart Eraser / Brush / Eraser), with `大小 20` (Size 20), `羽化 0` (Feather 0), and `边缘缩放 0` (Edge Scaling 0); the blue highlight is the kept selection, not an effect.
- `[sampled stills][10 05:44–07:38.5]` Complete chroma-key value chain: default `强度20/阴影0/羽化0/清除0` (Strength 20 / Shadow 0 / Feather 0 / Remove 0) → `37/32/0/0` → final `强度43/阴影31/边缘羽化7/边缘清除26` (Strength 43 / Shadow 31 / Edge Feather 7 / Edge Remove 26). The `边缘羽化 38` at 06:42 is a transient value that returns to 0 at 06:50 and must not be treated as the final value.
- `[sampled stills][10 08:34–08:58]` There are 9 mask shapes: Linear / Mirror / Circle / Rectangle / Keying / Pen / Text / Star / Heart; the rectangle reads `宽1075 高1080` (width 1075, height 1080) and `X0/Y0`, and the circle reads `X-86/Y-387`, `宽2876 高2662` (width 2876, height 2662), `羽化0` (Feather 0), and `双向跟踪` (Bidirectional Tracking).
- `[sampled stills][10 09:38 / 10:14]` 11 blend modes: `正常 / 颜色减淡 / 线性加深 / 强光 / 正片叠底 / 颜色加深 / 叠加 / 变亮 / 变暗 / 柔光 / 滤色` (Normal / Color Dodge / Linear Burn / Hard Light / Multiply / Color Burn / Overlay / Lighten / Darken / Soft Light / Screen). Course grouping: darken group = Linear Burn / Multiply / Color Burn / Darken; brighten group = Color Dodge / **Hard Light** / Lighten / Screen; composite-overlay group = Overlay / Soft Light. The SRT's “变量组” (variable group) is a misrecognition of “变亮组” (brighten group).
- `[sampled stills][10 04:34–04:38]` Keying sandwich: keyed layer on top, text layer in the middle, background layer at the bottom; place the duplicated clip on a secondary track and check after disabling the main track with `V` or the right-click `禁用` (Disable). The SRT's “浮轨” (floating track) is a misrecognition of “辅轨” (secondary track).
- `[sampled stills][10 02:08]` The preview-axis tooltip reads “关闭预览轴(S)” (Close Preview Axis (S)), showing that it was already enabled during the demonstration; `S` is a toggle, not a one-way enable.
- `[sampled stills][13 03:04–03:30]` Plain text cannot be planar-tracked directly and must first be turned into a “新建复合片段（子草稿）” (Create Compound Clip (Sub-draft)) via right-click; the text example uses font `系统` (System), size 15, shadow opacity 44%, and blur 15%, then “保存预设” (Save Preset).
- `[sampled stills][13 03:46–03:58]` Planar-tracking entry: select the compound clip → “跟踪” (Tracking) in the upper-right parameter panel → “平面跟踪” (Planar Tracking). The panel shows “无/运动跟踪/平面跟踪” (None / Motion Tracking / Planar Tracking), “编辑跟踪平面” (Edit Tracking Plane), “调整素材角度” (Adjust Material Angle), “当前跟踪平面 平面2-运镜源素材.mov” (Current Tracking Plane: Plane 2 – Camera-Move Source Footage.mov), “跟踪方向 双向跟踪” (Tracking Direction: Bidirectional Tracking), and “开始跟踪” (Start Tracking).
- `[sampled stills][13 04:40–05:18]` The first reference frame was too oblique and the phone screen occupied too small an area, so tracking drifted; switching to the frame with the largest screen area, re-drawing the four corners, and re-tracking made it fit.
- `[sampled stills][13 05:26–05:30]` The tracking plane and the texture position can be separated: the text was moved outside the phone screen yet still followed the phone's bezel and moved with the plane.
- `[sampled stills][13 05:40–06:08]` In the current version, tracking is lost after the target plane leaves the frame, and it is not automatically re-acquired even when it reappears; the handling is to split at the disappearing frame, delete the later segment, and add “渐隐” (Fade Out) to the earlier segment.
- `[sampled stills][13 07:26–08:00]` For the same material, the tracking-plane dropdown shows “平面1-运镜源素材” through “平面9-运镜源素材” (Plane 1 – Camera-Move Source Footage through Plane 9 – Camera-Move Source Footage); the case renames the planes to “电脑屏幕” (Computer Screen), “手机” (Phone), and “电脑” (Computer).
- `[sampled stills][13 08:52–09:16]` When the text is stretched horizontally, enter the compound clip and disable “等比缩放” (Uniform Scaling); the case changes it to scale width 212% and scale height 146%.
- `[sampled stills][13 09:26–09:36]` When the material's perspective is wrong, use “调整素材角度” (Adjust Material Angle) to drag the material's four corners, not to redo the outer tracking plane.
- `[sampled stills][12 17:24–17:52]` The sticker `背景相机跑-贴纸.png` lasts about `00:00:01:5`; the rectangle mask is width `2612`, height `364`, feather `0`, and the corner-radius value was not read.
- `[sampled stills]` Lesson 12 is point tracking / text tracking, while Lesson 13 is planar tracking; their entry points and degrees of freedom differ, so do not merge them into one “tracking” topic.

## Tool Boundaries

- `[tool boundary][capcut-cli 0.31.1]` `matting` writes a material configuration flag; it is not proof that pixel keying was completed.
- `[tool boundary][capcut-cli 0.31.1]` `chroma` can set color and intensity; visual acceptance is still required.
- `[tool boundary][capcut-cli 0.31.1]` The `mix-mode` mode is a string contract; no visual acceptance has been completed in the CapCut UI.
- There is currently no CLI evidence for plane solving; switch to the CapCut UI or a dedicated tracking tool when necessary.

## Failure Conditions

- Looking only at a still frame or verifying only the first frame.
- The mask does not cover the complete range of motion.
- Expanding the threshold damages the subject.
- Using a blend mode as a stand-in for precise alpha.
- Assuming automatic re-acquisition after the target disappears.
- Losing the editable project after baking, or not checking intermediate encode quality.
