---
name: mediastorm-dialogue-interview
description: Edit talking-head, interview, A-roll/B-roll, captions, and multicam material with semantic take selection and synchronization checks. Use for speech-centric edits rather than music design, story structure, or generic file mechanics.
metadata:
  short-description: Edit dialogue, interviews, and multicam
  status: provisional-unverified-audiovisual
---

# MediaStorm Dialogue Interview

Protect meaning, breath, and human performance while removing repetition and production friction. This skill owns the spoken-word edit: which take, where the cut lands, what the audience reads, and whether multiple cameras share one real moment.

## When to use

- A talking-head or interview needs a rough cut, take comparison, breath repair, or jump-cut coverage.
- A-roll and B-roll must be coordinated without losing the spoken argument.
- Captions need correction, safe-area checks, and a style that survives the platform UI.
- Multicam material needs syncing, camera switching, reaction shots, or lower-thirds.
- AI transcript tools are being used to propose cuts or select takes.

Do not use this skill for music-led montage, pure sound design, color grading, or export specs; route those to the matching child skill.

## Inputs to establish

- The full spoken argument or interview topic; what must not be lost.
- All takes and camera angles, with source timecode and audio channels.
- Whether the deliverable is a short, a long interview, a multicam package, or a captioned clip.
- The intended platform, safe areas, caption style constraints, and whether captions are burned in.
- Which audio track is primary, and whether sync sound from B-roll is useful.

## Workflow

1. Listen/read for meaning first: mark the claim, the evidence, the turn, the conclusion, and any negation or condition. Do not start by deleting low-volume regions.
2. Inventory takes by content completeness, intelligibility, performance, energy, and context. Do not automatically prefer the latest take.
3. Run a candidate pass with waveforms, silence detection, ASR, or `detect-retakes`; treat every result as a proposal, not a decision.
4. Manual rough cut: put the playhead at the candidate start, cut with `Command+B`/`Ctrl+B`, cut again at the end, select the middle, delete. The course calls this “two cuts, delete the middle”; the waveform share is set to `60%` in the demo [sampled stills][04 03:44–04:16].
5. Use smart talking-head cut as a first pass when available. The course’s transcript panel marks `停顿 [...0.2s]`, `语气词 这个` (pause/filler), and deleting a token deletes the matching video range [sampled stills][04 05:04–05:18]. Review every deletion; AI is not the final editor.
6. Repair exposed seams deliberately: split the audio at the seam, drag the audio handle for a short crossfade (the demo shows a `0.1s` hint), and add a small room-tone bed on a second track [sampled stills][04 05:50–06:08]. The picture does not prove the result sounds natural; that is a listening check.
7. Keep A-roll as the information carrier. Add B-roll for semantic support, not as a default wallpaper. Group related B-roll when an idea needs time to land [course evidence][04 06:29–10:56].
8. Check B-roll end points against the spoken phrase. In the course, a too-short B-roll makes the last word “disappear”; prefer a longer relevant shot over stretching a short one [course evidence][04 08:59–10:56].
9. For re-records, improve distance and environment before repairing in post; then match loudness intent, not identical gain [course evidence][04 10:56–12:59].
10. Check channel integrity. The audio panel’s channel configuration offers `无` (None), fill right from left, or fill left from right; confirm which side is missing before repairing [sampled stills][04 12:42–12:54].
11. Create captions before final music balancing when practical. Correct names and terms; the course uses `思源黑体 CN`, size 5, white, tracking/leading 0, with shadow opacity 59%, blur 7%, distance 5, angle -45° [sampled stills][04 13:45.5–13:57.5].
12. Check the safe area. The course overlays a “16:9 video play safe area” mask and warns that platform UI can cover captions near the edge [sampled stills][04 14:02–14:10].
13. For multicam, sync before cutting. The course reads four timecodes: A `1:10:04:27`, B `1:10:03:24`, C `1:10:03:26`, D `1:10:03:26`; A and B differ by about 1 second 3 frames, so aligning file starts is wrong [sampled stills][14 01:34–02:40].
14. Build the multicam clip with automatic (picture + metadata) or sound alignment; the course uses automatic and enables proxy mode. The four angles are `全景机位.mov`, `Links机位.mov`, `Tim机位.mov`, and `TimCook机位.mov` [sampled stills][14 03:32–04:16].
15. Switch cameras with the playhead on the target frame and the multicam view set to a razor; a click cuts and switches. If the wrong angle is chosen, select the clip and click the correct angle to change it back [sampled stills][14 05:20–06:40].
16. Add lower-thirds and quote cards only when they clarify identity or emphasis. The course uses a name-bar template with `剪映简明` at size 15 [sampled stills][14 06:54–08:00].
17. Review the full cut with picture and sound at normal speed: lip sync, drift, breath, room tone, caption accuracy, and whether any reaction shot changes the meaning.

## Decision rules

- Waveform/silence is a candidate signal, not proof that a region is meaningless.
- Preserve negation, conditions, qualifiers, conclusions, and emotional turns; a cut that removes “not” changes the argument.
- Do not mute every B-roll clip by default; keep useful sync sound when it supports the scene.
- Do not hide every jump cut with a cover shot; use a visible framing change or a relevant insert when it serves the meaning.
- Multicam sync must be verified against a shared event; “auto-aligned” is not “verified”.
- Cut to the speaker by default; cut to a listener only for a genuine reaction. Never manufacture context.
- Captions are part of the information layer; correct names and terms before beauty passes.
- AI take selection is a proposal. Keep the original media, the selection reason, and a rollback path.

## CapCut execution notes

- `detect-silence` and `detect-retakes` produce candidates only; they do not judge meaning, emotion, or performance.
- Use `capcut segment`/`segments` to inspect exact IDs and time ranges before batch edits.
- For multicam, keep the angle mapping visible; the course’s own 04:16 and 05:30 views show different numbering, so do not assume a stable order [pending verification].
- Check captions in the actual platform safe area; the CapCut preview alone may not show platform UI.

## Remotion / TypeScript Adapter

- Use `@remotion/captions` `Caption` (`startMs`/`endMs`/`timestampMs`) and import SRT into that shape.
- Use `<Video>`/`<Audio>` from `@remotion/media`; keep each camera angle in its own `Sequence` and sync with `trimBefore`.
- Local transcription can use `@remotion/whisper-webgpu` + `@huggingface/transformers`; it is dialogue evidence, not listening evidence.
- Multicam switching is component/prop driven; Remotion has no 4/9-grid multicam UI.

## Failure conditions

- A cut removes a negation, condition, or conclusion.
- The waveform is treated as a semantic editor.
- Multicam is aligned by file start rather than a shared event.
- A reaction shot is manufactured or a listener’s expression is used out of context.
- Captions are placed in the platform UI dead zone.
- The only copy of the source is destructively trimmed before a rollback exists.
- AI transcript edits are accepted without checking the picture.

## Acceptance checklist

- [ ] The spoken argument survives the cut.
- [ ] Every take choice has a reason.
- [ ] Breath/seam repairs have been checked by listening, not only by waveform.
- [ ] A/B-roll roles are explicit; B-roll end points do not orphan a word.
- [ ] Channel integrity is checked.
- [ ] Captions are accurate, styled, and inside the safe area.
- [ ] Multicam sync is verified on a shared event; angle mapping is recorded.
- [ ] Reactions and lower-thirds do not change the context.
- [ ] A rollback copy exists.

## Output contract

Return: the edit decision summary (takes, cuts, B-roll, captions, multicam), what was verified visually vs by listening, the remaining sync/audio uncertainties, and the next skill if color/music/delivery work follows.

Read [references/speech-editing.md](references/speech-editing.md) for decision cards, stop conditions, and timecode sources.
