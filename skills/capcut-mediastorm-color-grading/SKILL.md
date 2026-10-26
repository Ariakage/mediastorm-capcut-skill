---
name: capcut-mediastorm-color-grading
description: Restore Log footage, read exposure and color, use adjustment layers, scopes, curves, and shot matching for CapCut projects. Use for technical correction and creative grade decisions, not for compositing or export settings.
metadata:
  short-description: Correct, match, and grade color
  status: provisional-unverified-audiovisual
---

# MediaStorm Color Grading

Correct the technical input before creating a look, then verify the grade across the moving shot and neighboring shots.

## Core workflow

1. Identify the real camera profile, Log curve, color space, exposure, and whether the clip has already been restored. Never choose a LUT because the image merely looks flat.
2. Apply a matching technical restoration first. Stop when the profile is unknown or the selected transform conflicts with the source evidence.
3. Establish luminance, white balance, saturation, and hue priorities before local or stylistic moves. Use targeted highlight/shadow controls instead of global changes when the problem is regional.
4. Prefer a separate adjustment layer for comparison and rollback where the workflow supports it. Preserve original, restoration, and look stages as distinct inspectable states.
5. Read waveform position and RGB channels only in the context of known scene content. Do not force channel overlap without a neutral reference, and do not “fix” intentional color separation by dragging vectors to the center.
6. Treat curves as input-to-output mappings. Check how contrast moves affect highlight/shadow range and detail before applying an S curve.
7. Use reference images or smart matching as a starting point, then inspect skin, scene lighting, blacks, highlights, and whether a second technical restoration was accidentally applied.
8. Compare before/after, neighboring shots, scopes, and normal-speed playback. Reject a single-frame match that fails in motion.

## Boundaries

- A course frame showing Apple Log2 beside a C-Log3 LUT documented an incorrect-match demonstration, not a valid pairing.
- Do not turn stylistic examples such as warm highlights or cool shadows into a universal formula.
- Current CLI support does not prove access to every course color operation; route unresolved interface work to CapCut.
- Do not resolve subtitle ambiguities by guessing; verify graph direction and actual visual change.
- Treat this skill as provisional until continuous course audio/video review is completed.

Read [references/color-workflow.md](references/color-workflow.md) for decision order, scope interpretation, and timecodes.
