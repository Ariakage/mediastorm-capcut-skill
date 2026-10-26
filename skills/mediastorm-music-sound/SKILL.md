---
name: mediastorm-music-sound
description: Shape music edits, sound bridges, J-cuts, L-cuts, ambience, sound effects, and loudness intent for CapCut or Remotion projects. Use when sound carries pacing or meaning, not for speech take selection or picture-only motion design.
metadata:
  short-description: Shape music and sound narrative
  status: provisional-unverified-audiovisual
---

# MediaStorm Music Sound

Make sound an editorial layer with a reason to enter, change, and leave. This skill owns the sound job, the edit point, the tail, and the mix intent; it does not replace actual listening.

## When to use

- Music needs a cut, a tail, a loop, a bridge, or a less abrupt ending.
- Sound should arrive before the picture (J-cut) or continue after it (L-cut).
- Ambience, risers, low-frequency weight, or designed effects need a narrative reason.
- Dialogue, music, and effects need a balance intent and a channel check.
- A phone recording or everyday object is being turned into a designed sound.

Do not use this skill for choosing spoken takes, cutting dialogue by transcript, or final platform loudness compliance without measurement.

## Inputs to establish

- The sound job: establish place, bridge ideas, prepare a turn, support movement, release energy, or preserve silence.
- The musical phrase/beat map and the picture cut points.
- Whether the target is a hard cut, a decayed tail, a loop, a J/L-cut, or a designed effect.
- Dialogue priority, intended playback device, and whether the final mix will be heard on headphones, phone speaker, or both.
- Licensing/source for every track and effect.

## Workflow

1. Define the sound job in one sentence and the point where it should change. If there is no job, do not add sound.
2. Find phrase boundaries and meaningful beats. Treat auto beat markers as candidate coordinates; cut against the intended shot or story change.
3. For a music cut that would clip the tail, preserve decay by extending the container: duplicate the music, mute the second copy, place it after the original, wrap both as an audio compound clip (`Option+G` on Mac / `Alt+G` on Windows), apply `回音` (Echo) or hall reverb, then trim again to keep only the tail [sampled stills][06 02:48–02:58]. Without the compound-clip step, Echo on a truncated clip “does not work” in the course.
4. Verify the tail: the main phrase is not repeated, the tail is not clipped again, and the tail does not mask dialogue. This is a listening check, not a waveform-only check.
5. Use J-cuts to bring sound in before the picture. The course places `海浪声` (wave sounds) about 2–3 seconds before the next shot and adds a fade-in [sampled stills][06 04:24]. The lead time is a case value; derive it from the material.
6. Use L-cuts to let the previous sound continue under the next picture. The same logic applies in reverse: the sound belongs to the outgoing scene, not the incoming one.
7. Choose ambience from what the image implies: waves, wind, fire, room tone, traffic. Use risers and low-frequency weight for expectation, impact, or a turn, not as constant decoration.
8. For designed sound, start from a real recording; change speed and pitch, layer copies, and add reverb. The course’s original-effect demo reads `1.00x / 3.0s → 0.58x / 5.1s → 0.19x / 15.6s → 0.26x / 11.4s → 0.71x / 4.4s` with pitch shift on [sampled stills][06 10:07–10:14]. These are case values.
9. Check licensing and usage scope for every music track and effect. Musicbed, Artlist, Storyblocks, and Envato Elements appear in the course resource table; a filename in the course is attribution, not redistribution permission [sampled stills][06 08:30–08:52].
10. Balance dialogue first, then music and effects around it. Distinguish measured loudness from perceived clarity; do not apply the same gain to every clip.
11. Check channels. The audio panel offers `无` (None), fill right from left, or fill left from right; confirm which side is missing before repairing [sampled stills][04 12:42–12:54].
12. Validate by listening through the real transitions and the ending, on more than one device if the delivery matters. Check tail decay, room tone, left/right integrity, and whether effects mask speech.

## Decision rules

- A beat marker is a candidate, not a cut decision.
- If the tail is cut, fix the container first; do not just add a fade over a truncated phrase.
- If a J-cut’s lead time is justified only by “2–3 seconds” from the course, re-derive it from the scene.
- If the music is covering a weak section, fix the section; do not raise the music.
- If an effect has no narrative job, remove it; “something happening” is not a reason.
- If dialogue is masked, the music/effect loses, not the dialogue.
- AI-generated sound is a candidate source; it is not proof of quality, clearance, or fit.
- A loudness number is not a mix; check clarity, dynamics, and device context.

## CapCut execution notes

- `capcut loudness` measures by default; `--target` calculates gain; only `--apply` writes segment volume. `--per-clip` changes the overall mix-balance strategy.
- `capcut render` is an FFmpeg proxy preview; it cannot prove final CapCut audio behavior.
- Use audio compound clips for tails; keep the original music and the tail on separate tracks until the edit is accepted.
- Keep a copy of the original audio before destructive trims.

## Remotion / TypeScript Adapter

- Use `<Audio>` from `@remotion/media` with `trimBefore`, `from`, `durationInFrames`, `volume`, `playbackRate`, and `loop`.
- J/L-cuts are audio nodes with positive/negative `from` offsets relative to the picture cut.
- `@remotion/media-utils` exposes audio data for waveforms; `mediabunny` reads durations.
- Remotion has no built-in Echo or Hall Reverb preset. Render or prepare a tail externally and place it as an audio node.

## Failure conditions

- The tail is clipped, the main phrase repeats, or the tail masks dialogue.
- A J/L-cut is applied with a fixed lead/lag regardless of the scene.
- The music is used to hide a structural problem.
- An effect is stacked without a narrative reason.
- Licensing is assumed from a filename or a course screen.
- Only the waveform was checked; nobody listened.
- One channel is missing and a fill option was chosen without confirming which side is broken.

## Acceptance checklist

- [ ] The sound job and entry/exit points are stated.
- [ ] Music phrase and beat choices are intentional.
- [ ] Tails are preserved and not re-clipped.
- [ ] J/L-cut lead/lag is derived from the material.
- [ ] Ambience/effects serve a narrative purpose.
- [ ] Licensing is recorded.
- [ ] Dialogue remains intelligible.
- [ ] Channels, room tone, and ending are checked by listening.
- [ ] The final mix is checked on the intended device.

## Output contract

Return: the sound map (job, entry, exit, tail), the music/effect sources, the J/L-cut decisions, the mix intent, what was actually heard vs inferred, and the remaining listening checks.

Read [references/sound-narrative.md](references/sound-narrative.md) for course-derived techniques, checks, and timecodes.
