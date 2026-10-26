---
name: mediastorm-capcut
description: Route MediaStorm-inspired CapCut or Remotion editing requests across project prep, story, dialogue, sound, speed, motion, compositing, color, generative media, and delivery. Use for requests that need editing judgment plus CapCut execution or a Remotion/TypeScript implementation path, not for generic CapCut file operations already covered by capcut-edit.
metadata:
  short-description: Route MediaStorm CapCut editing workflows
  status: provisional-unverified-audiovisual
  source: MediaStorm course study notes, 2-second sampled stills, ASR, and local tool contracts
---

# MediaStorm CapCut Router

Route video-editing work by intent and evidence, then apply the matching child skill. This bundle is an original, unofficial study aid derived from a paid MediaStorm CapCut course. It is not affiliated with or endorsed by MediaStorm.

## Use this bundle when

- The request needs **editorial judgment**: what to cut, why, in what order, how to verify.
- The work spans more than one stage: e.g. dialogue cleanup → B-roll → sound → color → delivery.
- The user wants the same edit expressed in **CapCut** and/or **Remotion/TypeScript**.
- The request needs a boundary between course-derived knowledge, tool behavior, and unverified assumptions.

## Do not use this bundle when

- The task is only generic CapCut draft mechanics (read/write text, trim, speed, volume, template). Use `capcut-edit`.
- The task is only a file conversion, a codec probe, or an export command with no editorial decision.
- The user wants an unverified claim presented as a course fact; use the evidence labels and say what is pending.

## Routing protocol

1. Identify the deliverable: a CapCut draft, a Remotion composition, a review/analysis, a script, or a delivery file.
2. Identify the material condition: footage type, dialogue/no dialogue, multicam, green screen, Log, generated media, mobile/desktop.
3. Choose the narrowest child skill; add others only when the task genuinely crosses a boundary.
4. State the route in one line before editing, e.g. `project-prep → dialogue → sound → motion → delivery`.
5. Name the evidence needed for the current step and the acceptance layer that will prove it.
6. Stop before uploads, cloud AI, paid effects, publishing, or destructive cleanup until the user explicitly authorizes that action.

## Route by task

Read [references/routing.md](references/routing.md) for the decision matrix. Route to the narrowest child skill first, then compose skills for multi-stage work:

| Request pattern | Child skill |
| --- | --- |
| Organize media, check codecs/frame rates, relink, prepare proxies or drafts | `mediastorm-project-prep` |
| Design story, pacing, shot order, information density, B-roll meaning, or long-video structure | `mediastorm-story-structure` |
| Edit talking heads, interviews, takes, dialogue cuts, captions, or multicam sync | `mediastorm-dialogue-interview` |
| Fit music, design sound bridges, J/L-cuts, ambience, effects, or loudness intent | `mediastorm-music-sound` |
| Slow down, speed ramp, evaluate source frame rate, or reconstruct time around action peaks | `mediastorm-speed-time` |
| Animate scale/position or ease parameters (08), point-tracked labels and flash numbers (12), timers (15), or package motion | `mediastorm-motion-graphics` |
| Key, mask, layer subjects, use blend modes, or solve planar tracking and failures | `mediastorm-compositing-tracking` |
| Restore Log footage, use scopes, match shots, apply curves, or unify color | `mediastorm-color-grading` |
| Generate B-roll, concept shots, or local AI effects with cost and authenticity controls | `mediastorm-generative-broll` |
| Export, archive, version, transfer desktop/mobile drafts, or prepare publication | `mediastorm-delivery-handoff` |
| Implement the same edit in Remotion/TypeScript, or choose between CapCut and Remotion | Matching child skill + [references/remotion-adapter.md](references/remotion-adapter.md) |

## Composition patterns

- **Talking-head short**: project-prep → dialogue (semantic cut, breath, captions) → story (B-roll structure) → sound (music/SFX) → delivery.
- **Dialogue-free montage**: project-prep → story (shot-size/music framework) → sound (beat/tail) → speed/motion (if needed) → color → delivery.
- **Interview**: project-prep → dialogue (multicam sync, primary audio, reaction) → story (section order) → sound → color → delivery.
- **Packaging/tutorial**: project-prep → story → motion (labels/flash/timer) → compositing (tracking/keying) → sound → delivery.
- **Mobile-to-desktop**: mobile draft → editability check → desktop refine → cross-device verification → delivery.

## Evidence boundary

Treat this bundle as a **provisional draft** until continuous video and original-audio review is completed:

- Completed evidence: all subtitle cues; two rounds of still-frame sampling (20-second and **2-second** intervals); full-track local ASR; limited local experiments; capcut-cli 0.31.1 contracts. The 2-second pass covered all 18 lessons — 6,656 frames / 1,658 timestamped sheets — and added targeted full-resolution grabs for interface parameters.
- Still incomplete: continuous video understanding and original-audio listening. Do not claim the course videos were natively understood as continuous audio/video. The current session's Read interface rejected local MP4 paths as binary, and no API upload was authorized.
- Preserve uncertainty about music, sound effects, tone, fast motion, frame-level effects, and actual playback quality.
- Distinguish `[sampled stills]`, `[course narration]`, `[course evidence]`, `[inference]`, `[tool boundary]`, and `[pending verification]` in decisions that matter.
- Keep course videos, full subtitles, extracted audio, frame dumps, and transcript caches out of any skill package or repository commit.
- Course references in this bundle use **actual file numbers 01–18**. The promo board uses 01–14; 03–16 map to board 01–14, 17–18 are DLC. Say which numbering you mean.
- Read [references/visual-evidence-2026-10.md](references/visual-evidence-2026-10.md) for the verified picture corrections, course-internal conflicts, and exact case values from the 2-second pass.
- Read [references/remotion-adapter.md](references/remotion-adapter.md) when implementing the same edit in Remotion/TypeScript. That path is an official-API mapping, not a rendered or accepted result in this repository.

## Execute safely

1. Establish the target draft, source assets, desired output, and whether edits are authorized.
2. Prefer an isolated new draft or an explicit copy for implementation tests. Preserve encrypted or production originals.
3. Use the existing `capcut-edit` skill for generic CapCut draft mechanics when it is available. Keep this bundle responsible for editorial judgment, routing, and acceptance criteria.
4. Run `scripts/check_capcut_contract.py` when CLI behavior matters. It verifies the installed CLI via `describe --compact` and selected `describe --command` calls; do not use the truncated bare `capcut describe` output observed on this machine.
5. Before using a mutating command, fetch its current contract with `capcut describe --command <name>` and check option-level side effects. Do not infer safety from the command-level `mutates` flag.
6. Close the project in CapCut before writing, avoid `--force-write` unless the user explicitly accepts the risk, and reopen the project for visual/audio acceptance after edits.
7. Treat `capcut render` as an FFmpeg proxy preview, never as CapCut's final render. Treat `matting` as configuration until the resulting pixels are inspected in CapCut.
8. Stop before uploads, cloud AI, paid effects, publishing, external sharing, or destructive cleanup until the user explicitly authorizes that action.

## Quality gates

1. **Intent gate**: the requested outcome and the evidence needed are stated.
2. **Structure gate**: draft/timeline changes are inspected at the JSON/contract level.
3. **Preview gate**: a proxy or Studio preview has been watched.
4. **Interface gate**: CapCut can open/save the draft; Remotion Studio can render the composition.
5. **Audiovisual gate**: the result has been watched and heard at normal speed.
6. **Delivery gate**: the target platform/device has been checked.

No lower gate substitutes for a higher one.

## Minimal output contract

Return a result that separates:

- editorial decisions and their reasons;
- operations actually performed;
- evidence type and remaining uncertainty;
- validation performed, including draft structure, proxy preview, CapCut reopen/Remotion render, and final audiovisual checks;
- unresolved limitations that require the interface, a person, or a verified multimodal path.

Do not report “done” from JSON structure or a successful CLI exit alone when the requested change needs visible or audible confirmation.
