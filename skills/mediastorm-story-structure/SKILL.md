---
name: mediastorm-story-structure
description: Design video structure, pacing, montage, B-roll meaning, information density, and long-form rhythm using MediaStorm-inspired editorial judgment. Use for story and shot-order decisions before tool-specific execution; not for take-level cleanup, sound design, or export settings.
metadata:
  short-description: Design story, pacing, and montage
  status: provisional-unverified-audiovisual
---

# MediaStorm Story Structure

Build the edit around information, viewer attention, and relationships between shots rather than around effects or command names. This skill decides what the audience learns, in what order, and why the next shot earns its place.

## When to use

- The material exists but the story order, opening promise, section jobs, or ending are unclear.
- A dialogue-free montage needs a shot-size framework, music coordinates, or a transition policy.
- A long video needs paragraph units, peak/valley planning, or a “clock” diagnostic.
- A Vlog or documentary needs a mind map, narrative order, or a bridge between sections.
- Juxtaposition may be creating a false causal or emotional reading.

Do not use this skill for breath-level dialogue cleanup, music mixing, keyframe mechanics, or export specs; route those to the matching child skill.

## Inputs to establish

- Viewer promise: what question the piece answers, and what the ending must prove.
- Material map: people, events, locations, themes, repetitions, contradictions, and usable visual/auditory echoes.
- Delivery shape: duration range, platform context, aspect ratio, and whether music is required.
- Evidence boundary: what the user has actually watched or listened to, and what is still assumed.

## Workflow

1. Write the promise in one sentence: “After watching, the viewer will understand / feel / be able to …”.
2. Map the material without ordering it yet. Put themes, people, events, and echoes on one board; mark gaps and duplicates.
3. Choose an organizing frame supported by the footage: issue-driven explanation, spatial progression, time reconstruction, comparison, character/event flow, or another frame.
4. Give every section a job: establish context, add information, change state, create contrast, answer a promise, or release tension. Remove or compress sections that do no job.
5. Decide the opening. The course’s long-video example uses three timeline blocks: `抛出问题 → 揭示主题 → 混剪预告` (raise the question → reveal the theme → montage teaser) [sampled stills][15 05:10–05:20]. The hook must be fulfilled later.
6. For dialogue-free montage, build a shot-size framework first: wide/environment → medium/action → close-up/detail. The course demonstrates it with a 4×4 grid and a four-panel storyboard, but presents it as a method, not a fixed order [sampled stills][05 03:18–04:16].
7. Establish music/rhythm coordinates only after the information shape is clear. Use beat markers as candidate coordinates; cut before, on, or after the beat to avoid predictability.
8. Check juxtaposition. The course’s Kuleshov demonstration shows the same face read as “gaze” or “imagination” depending on the neighboring image; verify that the edit is not inventing a fact or emotion [sampled stills][05 05:28–05:38].
9. Choose transitions only at real turning points. In the course example the flare transition is shortened from `1.0s` to `0.9s`; effects are a separate track used for atmosphere, not a default layer on every cut [sampled stills][05 08:46–10:59].
10. For long-form work, build paragraph units by stage. Each unit answers: what is happening, what state is the subject in, what changed, and what is the result. Package units as compound clips, then assemble and check the joins [sampled stills][15 09:52–09:55].
11. For Vlogs, use an unordered mind map before a timeline. The course example has four branches: Giant Sequoia, Santa Barbara, Movie City, and Venice Beach [sampled stills][16 05:18–06:22].
12. Review the full structure at normal speed: promise fulfillment, section jobs, peak/valley contrast, B-roll meaning, and whether any deletion removed necessary explanation.

## Decision rules

- If a section has no informational or emotional job, cut or compress it; do not keep it because the footage is beautiful.
- If the opening promise is not answered by the ending, fix the structure before adding music or effects.
- If shot length is being justified by a universal seconds-per-shot rule, stop; use information density, emotional contrast, and the actual material.
- If music is carrying a section that has no information, fix the section first; not every piece needs music.
- If a match cut relies only on “two similar shots”, check shape, position, motion, or direction; otherwise it is decoration.
- If an effect or transition is added before the shot relationship works, remove it and re-check the cut.
- Clock positions are diagnostic checkpoints, not audience-fatigue laws. The course’s own clock graphic is internally inconsistent at 15 12:34–13:16; do not treat it as a precise law.

## CapCut execution notes

- Keep candidate material on a second timeline, then move selected ranges into the assembly timeline; do not destructively trim the only copy.
- Use compound clips for paragraph units and long-form sections so a section can move as one object.
- Keep transitions and effects on separate tracks; then a later removal does not damage the cut.
- Do not use `detect-scenes`/beat markers as final cut points; they are candidates.

## Remotion / TypeScript Adapter

- Use `<Sequence>`/`<Series>` for sections and `@remotion/transitions` `TransitionSeries` for adjacent shots that need transitions.
- Keep `trimBefore`/`durationInFrames` on the JSX node and derive seconds with `useVideoConfig().fps`.
- Shot length remains an editorial decision; do not replace it with a fixed `secondsPerShot` constant.
- Use `@remotion/layout-utils` for text fitting and safe-area checks.

## Failure conditions

- The story is a chronological dump of the shoot order.
- The opening asks a question the piece never answers.
- Every section is intensity-maxed; there is no relief or contrast.
- B-roll is used as wallpaper and does not clarify the idea.
- Juxtaposition creates a false cause, a false identity, or a false emotion.
- A transition or effect is hiding a cut that does not work.
- A duration preference from one channel is presented as a platform or audience law.

## Acceptance checklist

- [ ] The promise is stated and fulfilled.
- [ ] Every section has a named job.
- [ ] Shot lengths follow information and emotion, not a fixed target.
- [ ] The opening hook is honest about what follows.
- [ ] B-roll adds meaning or evidence, not just motion.
- [ ] Juxtaposition has been checked for false causality.
- [ ] Transitions/effects are used at real turning points.
- [ ] The piece has contrast between intensity and relief.
- [ ] The ending does not outstay its informational job.

## Output contract

Return: the promise, the chosen organizing frame, the section map with jobs, the opening strategy, the montage/transition policy, the risks (especially false juxtaposition), and the unresolved evidence needs. Separate course evidence, inference, and pending verification.

Read [references/structure-playbook.md](references/structure-playbook.md) for practical patterns, checks, and source timecodes.
