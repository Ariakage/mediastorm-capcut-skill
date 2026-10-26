---
name: mediastorm-generative-broll
description: Plan, prompt, review, and disclose AI-generated B-roll, concept shots, and local effects for CapCut edits. Use for generative media decisions, cost control, and authenticity checks, not for AI take selection or final export.
metadata:
  short-description: Plan and review generative B-roll
  status: provisional-unverified-audiovisual
---

# MediaStorm Generative B-roll

Use generated media as a constrained supplement, not as invisible evidence or an automatic replacement for real footage.

## Core workflow

1. Establish why real footage is unavailable or insufficient, and what the generated shot must explain.
2. Confirm aspect ratio, duration, resolution, style, number of candidates, model, credit/API cost, and data-handling terms before generation. User permission to edit does not imply permission to spend credits or upload material.
3. Convert the spoken or written intent into visible terms: subject, action, setting, camera behavior, lighting, style, duration, and exclusions. Remove filler that cannot be rendered.
4. Generate a small candidate set first, then review for factual faithfulness, anatomy/object errors, continuity, artifacts, and whether the result looks deceptively like real captured evidence.
5. Label generated or synthetic material in project metadata and delivery notes when its origin matters to interpretation.
6. Use local effects or generated inserts only where they add a clear visual hook or explanatory value; avoid covering an entire piece in unmotivated effects.
7. Preserve prompts, source instructions, selected candidates, cost authorization, and review outcome so the result can be regenerated or challenged later.
8. Recheck current model names, prices, rights, and platform policies at use time. A course-screen model name is historical evidence, not current availability.

## Remotion / TypeScript 适配

- Generation happens in an external service; store results in `public/` and reference them with `staticFile()`.
- Define prompt, aspect ratio, duration, and model as `zod`/`@remotion/zod-types` props; review candidates in `@remotion/player`.
- Remotion does not call or pay for models; cost, rights, and current availability remain external checks.
- Label generated shots in props/metadata and keep them out of documentary evidence.

## Boundaries

- Do not invoke paid generation, upload private source media, or publish generated media without explicit authorization.
- Do not present generated explanatory shots as documentary evidence.
- Do not treat the existence of an AI button or CLI command as proof of the course workflow or current product terms.
- The 2-second picture pass verified the AI panel names, candidate counts, credit prompts, and model labels as recorded; current availability, output quality, and cost remain unverified.
- Treat this skill as provisional until continuous course audio/video review is completed.

Read [references/generative-workflow.md](references/generative-workflow.md) for prompt and review checklists with course timecodes.

Route semantic take selection to `mediastorm-dialogue-interview` and final disclosure/versioning to `mediastorm-delivery-handoff`.
