---
name: mediastorm-compositing-tracking
description: Handle CapCut or Remotion matting, chroma keying, masks, layer compositing, blend modes, and planar tracking with motion-wide acceptance checks. Use for spatial layering or perspective tracking, not for simple point labels, color grading, or story order.
metadata:
  short-description: Composite, mask, and track footage
  status: provisional-unverified-audiovisual
---

# MediaStorm Compositing Tracking

Build layered images that survive the entire shot, not just one inspected frame. This skill owns separation, layer order, blend behavior, and planar tracking; it does not treat a configuration flag as a finished matte.

## When to use

- A subject needs smart matting, custom matting, or chroma keying.
- A mask must hide a boom, light stand, screen edge, or other off-screen object.
- A text/logo must sit behind or in front of a subject.
- A black- or white-backed element needs a blend-mode treatment.
- A label or graphic must track a planar surface through perspective change.

Do not use this skill for point-tracked labels (route to `mediastorm-motion-graphics`), color grading, or story order.

## Inputs to establish

- Footage type: clean background, green screen, uneven lighting, black/white overlay, or planar surface.
- Subject motion range and the full duration that must survive.
- Whether the target is a hard matte, a soft edge, a garbage mask, or a blend-mode composite.
- For planar tracking: the surface, the reference frame, and what happens when the surface leaves the frame.
- The acceptance surface: CapCut interface, export, or Remotion render.

## Workflow

1. Choose the separation method from the footage, not from “which effect is strongest”:
   - Clean background / everyday footage → smart matting.
   - Edge problems / small corrections → custom matting.
   - Controllable solid color → chroma key.
   - Off-screen object or non-green intrusion → garbage mask.
   - Black/white-backed element → blend mode.
   - Perspective surface → planar tracking.
2. Smart matting: inspect the whole moving range for hair, edges, background leaks, and missing subject parts. The course panel shows feather 0 and edge scale 0; it does not demonstrate non-zero values [sampled stills][10 01:52].
3. Custom matting: the blue overlay is a selection, not an effect. Use smart brush/eraser, size 20, feather 0, and edge scale 0; after applying, check how the correction propagates through the shot [sampled stills][10 02:36–03:34].
4. Chroma key: sample the actual background color, then tune strength, shadow, feather, and edge clear. The course moves from `强度20/阴影0/羽化0/清除0` to `37/32/0/0` and finally `43/31/7/26` [sampled stills][10 05:44–07:38.5]. The transient `边缘羽化 38` at 06:42 returns to 0 at 06:50; treat it as an intermediate value, not a preset [pending verification].
5. Do not max the threshold. A larger value can remove the subject; the goal is “clean edge + intact subject”, not “green pixel count zero”.
6. Feather and edge clear solve different problems: feather softens the edge, clear removes residual spill. Feathering cannot replace despill or edge recovery.
7. Use a garbage mask for off-screen objects. The mask must remain valid through the subject’s full movement; a mask that works at one frame may expose the object later.
8. Blend modes are color compositing, not a precise alpha channel. The course lists 11 modes: `正常 / 颜色减淡 / 线性加深 / 强光 / 正片叠底 / 颜色加深 / 叠加 / 变亮 / 变暗 / 柔光 / 滤色` (Normal / Color Dodge / Linear Burn / Hard Light / Multiply / Color Burn / Overlay / Lighten / Darken / Soft Light / Screen). Its groups are: darken = Linear Burn/Multiply/Color Burn/Darken; brighten = Color Dodge/Hard Light/Lighten/Screen; blend = Overlay/Soft Light [sampled stills][10 09:38 / 10:14]. The SRT label “variable group” is a misrecognition of “brighten group”.
9. Build layer order explicitly. The course’s “keying sandwich” is keyed subject on top, text in the middle, background at the bottom; duplicate the clip to a secondary track, align it, and temporarily disable the main track to expose defects [sampled stills][10 04:34–04:38].
10. For planar tracking, select the compound clip, open the upper-right `跟踪` (Tracking) panel, and choose `平面跟踪` (Planar Tracking). The panel shows `无/运动跟踪/平面跟踪` (None/Motion Tracking/Planar Tracking), `编辑跟踪平面` (Edit Tracking Plane), `调整素材角度` (Adjust Material Angle), a current plane name, `双向跟踪` (Bidirectional Tracking), and `开始跟踪` (Start Tracking) [sampled stills][13 03:46–03:58].
11. Choose the reference frame carefully. The course’s first reference was too oblique and the phone screen was too small; moving to the frame where the screen occupies the most area and re-drawing the four corners made the track stick [sampled stills][13 04:40–05:18].
12. Fit the four corners to the real plane. The software solves perspective; you do not manually set perspective. The plane can be moved independently of the texture, so a label can sit outside the screen and still follow the phone [sampled stills][13 05:26–05:30].
13. Handle target disappearance deliberately. In the course version, when the plane leaves the frame, tracking is lost and is not automatically re-acquired when it returns; split at the disappearance, delete the tail, add a fade, and track the reappearance as a new segment [sampled stills][13 05:40–06:08].
14. Name and maintain planes. The course shows planes 1–9 and renames them “Computer Screen”, “Phone”, “Computer”; use names that describe the surface, not the index [sampled stills][13 07:26–08:00].
15. Separate the inner package from the outer plane. If text stretches, open the compound clip, disable proportional scaling, and adjust width/height (the course uses 212%/146%). If perspective is wrong, use `调整素材角度` instead of changing the outer plane size [sampled stills][13 08:52–09:36].
16. If you bake or re-import a tracked section, preserve the editable original and check the intermediate codec. Baking is a performance trade, not a substitute for a backup.
17. Validate the entire shot, not one frame: hair, edges, spill, mask coverage, layer order, tracking drift, texture shape, and perspective.

## Decision rules

- If the background is controllable solid color, chroma key; if the edge is the problem, custom matting; if the object is off-screen, mask; if the element is black/white-backed, blend mode.
- If a threshold change starts damaging the subject, stop; the threshold is too high.
- If feathering is being used to hide spill, fix despill/edge clear instead.
- If a blend mode is being used as alpha, stop; use a matte or mask.
- If the planar target leaves the frame, split and re-track; do not assume auto-recapture.
- If the text is stretching, fix the inner compound clip before touching the outer plane.
- If `capcut matting` wrote a flag, do not call the matte finished; inspect the pixels in CapCut.

## CapCut execution notes

- `capcut matting` writes a smart-matting configuration flag; it does not prove the matte was computed or looks good.
- `capcut chroma` can set color and strength; still needs visual acceptance.
- `capcut mix-mode` has a string contract; CapCut blend results are not visually verified by the CLI.
- There is no CLI evidence of a full planar solver; use the CapCut interface or a dedicated tracking tool.

## Remotion / TypeScript Adapter

- Chroma key with `@remotion/effects` `colorKey()`; masks with CSS `mask`/`clip-path`; blend modes with CSS `mix-blend-mode`.
- Planar tracking has no built-in solver. Export four-corner keyframes from Mocha/AE and drive `cornerPin()` or a custom transform.
- `@remotion/three` is available for 3D layers; it does not provide tracking by itself.
- Inspect the whole motion range; a clean still does not prove edge stability.

## Failure conditions

- Only the first frame or a single still is inspected.
- The mask does not cover the subject’s full movement.
- The threshold is expanded until the subject is damaged.
- A blend mode is presented as a precise alpha channel.
- The planar target disappears and the edit assumes automatic recapture.
- The baked section loses the editable original or the intermediate codec is not checked.
- A CLI configuration write is reported as a finished pixel result.

## Acceptance checklist

- [ ] The separation method matches the footage.
- [ ] The full motion range is inspected for edges, spill, and missing parts.
- [ ] Chroma values are recorded, including transient values that are not final.
- [ ] Masks cover the full movement.
- [ ] Blend modes are used for color behavior, not alpha.
- [ ] Layer order is explicit and duplicated layers are time-aligned.
- [ ] Planar reference frame, four corners, plane names, and disappearance handling are recorded.
- [ ] The editable original is preserved before baking.
- [ ] The result is checked in CapCut/export, not only in a proxy or CLI JSON.

## Output contract

Return: the chosen method and why, the parameter chain, the layer order, the tracking plan and failure handling, what was visually verified, and what remains pending (hair/edges in motion, tracking drift, interface acceptance).

Read [references/compositing-playbook.md](references/compositing-playbook.md) for layered checklists and source timecodes.
