---
name: mediastorm-dialogue-interview
description: Edit talking-head, interview, A-roll/B-roll, captions, and multicam material with semantic take selection and synchronization checks. Use for speech-centric edits rather than music design or generic file mechanics.
metadata:
  short-description: Edit dialogue, interviews, and multicam
  status: provisional-unverified-audiovisual
---

# MediaStorm Dialogue Interview

Protect meaning, breath, and human performance while removing repetition and production friction.

## Core workflow

1. Separate candidate detection from semantic deletion. Use silence detection, waveforms, ASR, or repeated-take detection only to propose ranges.
2. Preserve negation, conditions, qualifiers, conclusions, and emotional turns. Check whether a candidate cut breaks a breath, phrase, emphasis, or listener reaction.
3. Compare takes by content completeness, intelligibility, performance, energy, and context; do not automatically prefer the latest or most similar take.
4. Use A-roll for the primary information and B-roll for semantic support, grouping related B-roll where the idea needs time to land. Preserve useful sync sound instead of muting every overlay by default.
5. Repair jump cuts deliberately with relevant B-roll, a visible change in framing, or another choice the viewer can understand. Do not hide every cut just because a cover shot exists.
6. For multicam, establish a common real-world moment with clap, timecode, waveform peaks, or shared events; then verify lip sync, camera drift, and the chosen primary audio.
7. Cut to the speaker as the default information carrier, then to listeners for genuine reactions. Never manufacture a reaction that changes the context.
8. Create captions before final music balancing when practical, correct names and terms, and check safe areas against the intended platform and device.

## Boundaries

- `detect-silence` and `detect-retakes` produce candidates only. They do not judge meaning, emotion, or performance quality.
- Local ASR is dialogue evidence, not listening evidence for music, effects, tone, or actual sync quality.
- Prefer improving a re-record through distance and environment before trying to repair everything in post.
- Do not apply one fixed fade, room-tone duration, gain, or subtitle style as a universal preset.
- The 2-second picture pass verified waveform 60%, two-cut deletion, smart-script tokens, the 0.1s handle prompt, shadow values, channel options, and the multicam dialog; actual audio, breath repair, and sync quality remain unverified.
- Treat this skill as provisional until continuous course audio/video review is completed.

Read [references/speech-editing.md](references/speech-editing.md) for decision cards, stop conditions, and timecode sources.

For story-level B-roll selection, coordinate with `mediastorm-story-structure`; for loudness intent, hand off to `mediastorm-music-sound`.
