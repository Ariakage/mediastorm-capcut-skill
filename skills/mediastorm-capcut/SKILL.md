---
name: mediastorm-capcut
description: Route MediaStorm-inspired CapCut editing requests across project prep, story, dialogue, sound, speed, motion, compositing, color, generative media, and delivery. Use for requests that need editing judgment plus CapCut execution, not for generic CapCut file operations already covered by capcut-edit.
metadata:
  short-description: Route MediaStorm CapCut editing workflows
  status: provisional-unverified-audiovisual
  source: MediaStorm course study notes, sampled frames, ASR, and local tool contracts
---

# MediaStorm CapCut Router

Route video-editing work by intent and evidence, then apply the matching child skill. This bundle is an original, unofficial study aid derived from a paid MediaStorm CapCut course. It is not affiliated with or endorsed by MediaStorm.

## Evidence boundary

Treat this bundle as a **provisional draft** until continuous video and original-audio review is completed:

- Completed evidence: all subtitle cues; two rounds of still-frame sampling (20-second and **2-second** intervals); full-track local ASR; limited local experiments; capcut-cli 0.31.1 contracts. The 2-second pass covered all 18 lessons — 6,656 frames / 1,658 timestamped sheets — and added targeted full-resolution grabs for interface parameters.
- Still incomplete: continuous video understanding and original-audio listening. Do not claim the course videos were natively understood as continuous audio/video. The current session's Read interface rejected local MP4 paths as binary, and no API upload was authorized.
- Preserve uncertainty about music, sound effects, tone, fast motion, frame-level effects, and actual playback quality.
- Distinguish `[画面]`, `[字幕]`, `[课程]`, `[推论]`, and `[工具]` in decisions that matter.
- Keep course videos, full subtitles, extracted audio, frame dumps, and transcript caches out of any skill package or repository commit.
- Course references in this bundle use **actual file numbers 01–18**. The promo board uses 01–14; 03–16 map to board 01–14, 17–18 are DLC. Say which numbering you mean.
- Read [references/visual-evidence-2026-10.md](references/visual-evidence-2026-10.md) for the verified picture corrections, course-internal conflicts, and exact case values from the 2-second pass.

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

For a request spanning multiple stages, state the planned sequence before editing. Example: dialogue cleanup → B-roll structure → sound bridge → motion label → color match → delivery QC.

## Execute safely

1. Establish the target draft, source assets, desired output, and whether edits are authorized.
2. Prefer an isolated new draft or an explicit copy for implementation tests. Preserve encrypted or production originals.
3. Use the existing `capcut-edit` skill for generic CapCut draft mechanics when it is available. Keep this bundle responsible for editorial judgment, routing, and acceptance criteria.
4. Run `scripts/check_capcut_contract.py` when CLI behavior matters. It verifies the installed CLI via `describe --compact` and selected `describe --command` calls; do not use the truncated bare `capcut describe` output observed on this machine.
5. Before using a mutating command, fetch its current contract with `capcut describe --command <name>` and check option-level side effects. Do not infer safety from the command-level `mutates` flag.
6. Close the project in CapCut before writing, avoid `--force-write` unless the user explicitly accepts the risk, and reopen the project for visual/audio acceptance after edits.
7. Treat `capcut render` as an FFmpeg proxy preview, never as CapCut's final render. Treat `matting` as configuration until the resulting pixels are inspected in CapCut.
8. Stop before uploads, cloud AI, paid effects, publishing, external sharing, or destructive cleanup until the user explicitly authorizes that action.

## Minimal output contract

Return a result that separates:

- editorial decisions and their reasons;
- operations actually performed;
- evidence type and remaining uncertainty;
- validation performed, including draft structure, proxy preview, CapCut reopen, and final audiovisual checks;
- unresolved limitations that require the interface, a person, or a verified multimodal path.

Do not report “done” from JSON structure or a successful CLI exit alone when the requested change needs visible or audible confirmation.
