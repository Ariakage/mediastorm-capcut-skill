---
name: mediastorm-generative-broll
description: Plan, prompt, review, and disclose AI-generated B-roll, concept shots, and local effects for CapCut or Remotion edits. Use for generative media decisions, cost control, and authenticity checks, not for AI take selection, restoration, or final export.
metadata:
  short-description: Plan and review generative B-roll
  status: provisional-unverified-audiovisual
---

# MediaStorm Generative B-roll

Use generated media as a constrained supplement, not as invisible evidence or an automatic replacement for real footage. This skill covers the decision, the prompt, the cost check, the candidate review, and the disclosure.

## When to use

- Real footage cannot cover a concept, a missing insert, or a visual hook.
- A local AI effect or generated insert could add explanatory value.
- A generation tool is being considered, and cost/model/resolution/aspect ratio must be bounded.
- AI output needs a review for factual faithfulness, artifacts, and whether it looks like real evidence.

Do not use this skill for AI take selection (route to `mediastorm-dialogue-interview`), technical restoration, or final platform delivery.

## Inputs to establish

- Why real footage is unavailable or insufficient, and what the generated shot must explain.
- Aspect ratio, duration, resolution, style, number of candidates, model, and credit/API cost.
- Data-handling terms: what is uploaded, where it is processed, and whether the user authorized it.
- The intended position in the edit: opening hook, explanatory insert, transition, or background.
- The disclosure requirement: will the audience be told it is generated?

## Workflow

1. State the gap and the job. If a real shot can do the job, prefer the real shot.
2. Confirm the generation constraints before spending: aspect ratio, duration, resolution, model, candidate count, and cost. The course’s video panel reads default `Seedance 2.0 Fast`, modes `全能参考 / 图转视频 / 首尾帧` (Omni-Reference/Image to Video/First and Last Frame), resolution `480p / 720p`, and a 10-second duration slider [sampled stills][17 09:24–10:56].
3. Confirm the current model lineup and terms at use time. The course screen also shows `Seedance 2.0 Mini`, `Seedance 1.0`, `Seedream 5.0`, `豆包 Pro` (Doubao Pro), and `DeepSeek-R1`; these are recording-time UI evidence, not a current availability promise [sampled stills][17 09:28 / 12:18–12:52].
4. Write the prompt in visible terms: subject, action, setting, camera behavior, lighting, style, duration, and exclusions. Remove abstract filler that cannot be rendered.
5. Read the cost prompt before clicking generate. The course’s text-to-video page shows a credit cost of 0.100 with a balance of 3200; the AI-effects page shows an estimated cost of 0.44 and a `+44` badge after generation [sampled stills][18 01:50 / 08:26–08:38]. These are recording-time account states.
6. Generate a small candidate set first; review subject, motion, anatomy/object errors, continuity, text, edges, materials, and whether it looks deceptively like live evidence.
7. If the result is rough, revise the prompt rather than generating more at random. The course uses a text model to rewrite a spoken description into a more visual prompt before a second generation [sampled stills][17 12:18–12:52].
8. Place the generated shot where it adds value. The course uses a short AI effect only at the opening as a visual hook, not across the whole piece [sampled stills][18 08:26–08:38].
9. Label generated or synthetic material in the project metadata and delivery notes when origin matters. Keep the prompt, model, settings, selected candidates, cost authorization, and review outcome.
10. Recheck current model names, prices, rights, and platform policies at use time. Do not quote a course screen as a current price or availability guarantee.

## Decision rules

- If the user has not authorized upload or spend, do not call a cloud model; a local test is a separate decision.
- If the prompt cannot name the visible subject/action, fix the prompt before generating.
- If the output is being used as an explanatory shot, mark it as generated; never present it as documentary evidence.
- If the generated shot is only a visual hook, keep it short; do not let it cover the whole piece.
- If a model name or price is from the course UI, treat it as historical evidence.
- If the result is “good enough” but has anatomy/continuity errors, reject it; do not rely on the audience not noticing.
- If the generated shot replaces a real shot that could have been captured, state the trade-off.

## CapCut execution notes

- The course shows AI generation inside CapCut desktop and mobile; the actual model is a service, not a local effect.
- The AI-effects track is an effect layer, not a generated video file; check what is actually rendered.
- Credits, VIP/limited-free status, and model availability are account/version dependencies.
- Do not assume a generated placeholder clip has the requested duration; the course’s 10-second panel and 4-second placeholder disagree [pending verification][sampled stills][17 10:10 / 10:50].

## Remotion / TypeScript Adapter

- Generation happens in an external service; store results in `public/` and reference them with `staticFile()`.
- Define prompt, aspect ratio, duration, and model as `zod`/`@remotion/zod-types` props; review candidates in `@remotion/player`.
- Remotion does not call or pay for models; cost, rights, and current availability remain external checks.
- Label generated shots in props/metadata and keep them out of documentary evidence.

## Failure conditions

- Spending credits or uploading media without consent.
- Promising models, prices, credits, or entitlements from an outdated course UI.
- The prompt omits the subject action or aspect ratio.
- A generated shot is presented as a genuine record.
- Only “generation succeeded” is checked; nobody reviews the image.
- Generated content is used to cover a narrative or footage problem.
- A placeholder clip’s duration is assumed from the panel without checking the timeline.

## Acceptance checklist

- [ ] The gap and the job are stated.
- [ ] Aspect ratio, duration, resolution, model, and cost are confirmed.
- [ ] Upload/data-handling permission is explicit.
- [ ] The prompt names visible subject/action/style/exclusions.
- [ ] The cost prompt was read before generating.
- [ ] A small candidate set was reviewed for faithfulness and artifacts.
- [ ] The shot is placed where it adds value, not everywhere.
- [ ] Generated material is labeled in metadata/delivery.
- [ ] Current model/price/rights are rechecked at use time.

## Output contract

Return: the generation decision, prompt, model/specs, cost authorization, candidate review, placement, disclosure, and what remains unverified. Separate the course-screen evidence from current product facts.

Read [references/generative-workflow.md](references/generative-workflow.md) for prompt and review checklists with course timecodes.
