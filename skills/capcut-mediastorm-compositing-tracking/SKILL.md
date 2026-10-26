---
name: capcut-mediastorm-compositing-tracking
description: Handle CapCut matting, chroma keying, masks, layer compositing, blend modes, and planar tracking with motion-wide acceptance checks. Use for spatial layering or perspective tracking, not for simple point labels or color grading.
metadata:
  short-description: Composite, mask, and track footage
  status: provisional-unverified-audiovisual
---

# MediaStorm Compositing Tracking

Build layered images that survive the entire shot, not just one inspected frame.

## Core workflow

1. Choose the separation method from the footage: smart matting, chroma key, garbage mask, manual mask, layer ordering, or blend mode.
2. Inspect the whole moving range for hair, edges, background leaks, missing subject parts, spill, mask coverage, and propagation of manual fixes.
3. Build subject-behind-text or similar layers as explicit background/text/subject relationships. Keep duplicated layers synchronized in time and temporarily hide or isolate layers to expose defects.
4. Tune chroma keying to the actual lighting, wrinkles, color spill, and edge quality. Do not expand thresholds until the subject is damaged or use feathering as a substitute for despill and edge recovery.
5. Use garbage masks to exclude known off-screen or non-green regions, then verify that the mask remains valid through the subject's full movement.
6. Use blend modes only for their color-compositing behavior. Do not treat them as a precise alpha channel.
7. For planar tracking, choose a reference frame with a large visible plane and strong features, fit all four corners to the real surface, and define where the target leaves the frame.
8. Split work when the tracked plane disappears and later returns. Validate tracking stability, texture shape, perspective, and motion drift as separate checks.
9. Preserve an editable original before baking or re-importing heavy tracked sections, and inspect intermediate codec quality if baking is necessary.

## Boundaries

- `capcut matting` writes a smart-matting configuration flag; it does not prove the matte was computed or looks good.
- `capcut mix-mode` has a CLI contract, but the current bundle has not visually verified CapCut blend results.
- The local FFmpeg experiment showed `hardlight` blackened a gray base under a black overlay; do not generalize “hard light removes black” to CapCut.
- No current CLI evidence proves full planar-solver capability. Use the CapCut interface or a dedicated tracking tool where necessary.
- Treat this skill as provisional until continuous course audio/video review is completed.

Read [references/compositing-playbook.md](references/compositing-playbook.md) for layered checklists and source timecodes.
