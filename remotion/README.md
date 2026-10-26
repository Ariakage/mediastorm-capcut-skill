# Remotion Skill Atlas

A **synthetic** 24-second Remotion demo for the MediaStorm CapCut skill bundle. It contains no course footage, no course audio, and no paid assets. The clip is generated locally from gradients and sine tones.

- Composition: `SkillAtlas`
- Canvas: 1920×1080, 30 fps, 720 frames
- Output: `out/skill-atlas.mp4`
- Poster: `../assets/demo/skill-atlas-poster.jpg`
- Rendered copy: `../assets/demo/skill-atlas.mp4`

## What it demonstrates

| Scene | Time | Frames | What it shows |
| --- | --- | --- | --- |
| Title | 0–3.2s | 0–96 | Project identity, stats, a short timeline strip |
| Skills | 2.8–8.0s | 84–240 | Ten skill cards with staggered spring entrances |
| Timeline | 7.6–12.8s | 228–384 | Clips, waveform, captions, keyframes, moving playhead |
| Color | 12.4–16.6s | 372–498 | Log/flat vs. graded using `colorCorrection()` |
| Motion | 16.2–20.4s | 486–612 | Keyframe interpolation and a Bezier easing curve |
| Delivery | 20.0–24.0s | 600–720 | Render/review/deliver steps and a progress bar |

The scene boundaries overlap by 12 frames because `TransitionSeries` crossfades shorten the total timeline.

## Run it

```bash
npm install
npm run dev      # open Remotion Studio
npm run still    # render out/skill-atlas-poster.png at frame 48
npm run render   # render out/skill-atlas.mp4
```

Node 20.19+, 22.13+, or 24+ is required by the current Remotion template.

## Dependencies used

- `remotion`: `Composition`, `Sequence`, `interpolate`, `Easing`, `spring`, `useCurrentFrame`, `useVideoConfig`, `staticFile`
- `@remotion/media`: `<Video>`, `<Audio>`
- `@remotion/transitions`: `TransitionSeries`, `linearTiming`, `fade`
- `@remotion/effects`: `colorCorrection()` from `@remotion/effects/color-correction`
- `@remotion/captions`: `Caption` type for the timeline captions
- React 19 + TypeScript

The project intentionally does **not** use `@remotion/motion-blur`, `@remotion/shapes`, or `@remotion/three` in the render path; they are listed in the skill adapters but are not required by this demo.

## Synthetic assets

`public/demo.mp4` is an 8-second 1280×720 gradient generated with FFmpeg. `public/tone.mp3` is a 24-second two-sine ambient bed generated with FFmpeg. Regenerate them with:

```bash
./scripts/make-assets.sh
```

They are original synthetic assets, not course material.

## What this demo does not prove

- It does not prove the CapCut path, course footage handling, or actual course audio.
- It does not prove platform acceptance, upload behavior, or mobile/desktop handoff.
- It does not prove the full skill bundle's judgment; it is a visual smoke test of the Remotion implementation path.
- The audio was generated but not perceptually reviewed; the mix is not a reference.

## Mapping to the skills

- `mediastorm-project-prep`: `staticFile()`, fixed composition metadata, local asset paths.
- `mediastorm-story-structure`: `TransitionSeries` scenes and section jobs.
- `mediastorm-dialogue-interview`: `Caption` type and caption timing.
- `mediastorm-music-sound`: `<Audio>` with a volume level and a real duration.
- `mediastorm-speed-time`: `playbackRate`/`trimBefore` patterns are documented in the skill; this demo uses normal-speed playback.
- `mediastorm-motion-graphics`: `interpolate`, `spring`, `Easing`, frame-driven values.
- `mediastorm-compositing-tracking`: layered composition and masks in CSS; no planar solver.
- `mediastorm-color-grading`: `colorCorrection()` on a `<Video>`.
- `mediastorm-generative-broll`: not exercised; no paid generation.
- `mediastorm-delivery-handoff`: render command, canvas/fps, poster; no platform upload.

See `../skills/mediastorm-capcut/references/remotion-adapter.md` for the full package mapping.
