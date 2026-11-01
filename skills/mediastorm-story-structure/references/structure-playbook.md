# Structure and shot-assembly playbook

## Core judgments

- `[course evidence][01 00:19–01:11]` Judge information organization, rhythm, and the sound–picture–text relationship first; software features are only the means of implementation.
- `[course evidence][05 01:02–02:51]` For dialogue-free material, build a framework from shared characteristics, shot size, and music sections; decide the viewing rhythm first, then select shots.
- `[course evidence][16 03:25–06:23]` For a Vlog, collect themes, people, events, and echoing relationships first, then form the narrative order; shooting time is not an inherent structure.
- `[course evidence][15 08:52–11:29]` For long videos, build paragraph units by stage; each segment covers the event, state, change, and result, and then the units are assembled and joined.

## Shot relationships

- `[course evidence][05 03:18–04:16]` A gentle build-up can pair with steady shots; wide shot–medium shot–detail is one organizing method, not a fixed formula.
- `[course evidence][05 04:16–05:13]` Match cuts must find a cross-shot connection in shape, position, motion, or direction.
- `[course evidence][05 05:13–07:04]` Juxtaposition changes audience understanding; check whether it creates false causality or false emotion.
- `[course evidence][05 08:46–10:59]` Transitions should primarily serve key turning points, while effects serve atmosphere; when the material relationship does not hold, fix the structure first.

## Information and rhythm

- `[course evidence][12 02:22–03:35]` Shot length must let the audience digest information; the roughly 1-second opening in the case is not a universal rule.
- `[course evidence][12 03:35–05:49]` Primary/secondary text and information steps matter more than blindly adding transitions/BGM.
- `[course evidence][03 08:04–09:32]` Automatic beat detection only provides candidate coordinates; it does not mean the rhythm judgment is complete.
- `[course evidence][15 02:45–07:56]` The opening establishes a question and promise relevant to the audience, which later content must fulfill; compress processes that add no new information, and retain genuine state changes.
- `[inference][derived from 15 11:29–15:12]` The "clock diagram" can be mapped to checkpoints at 0, T/4, T/2, and 3T/4 of a total length T; it is not a law that "there must be a stimulus every 3 minutes".

## Structure acceptance

- The opening promise is consistent with its later fulfillment.
- Each segment has a clear informational or emotional responsibility.
- Intensity has peak–valley contrast rather than staying maxed out continuously.
- B-roll or juxtaposition has not changed the factual meaning.
- Dialogue-free segments have still been confirmed by actual viewing.
- Deleted or accelerated processes do not sacrifice necessary explanation.

## 2026-10 sampled stills review supplement

- `[sampled stills][05 03:18–04:16]` The dialogue-free montage uses a 4×4 grid and a four-panel storyboard to demonstrate the wide shot–medium shot–close-up shot-size framework; this is an organizing method, not a fixed order.
- `[sampled stills][05 05:28–05:38]` After the `Kuleshov Effect / 库里肖夫效应` title card, the left/right split screen labels `注视` (gaze) first and `想象` (imagination) second: the same face paired with different images is read as different meanings. The juxtaposition check must examine whether it changed the fact or the emotion.
- `[sampled stills][05 08:46–10:59]` The `炫光` (flare) transition duration is adjusted from `1.0s` to `0.9s`; effects are overlaid on an independent track and used only for key atmosphere. The `光晕/边缘发光/丁达尔光线/胶片漏光` (halo/edge glow/Tyndall light/film light leak) at 10:08–10:14 are the same class of atmosphere presets, not something that must be added to every shot.
- `[sampled stills][12 02:22–03:35]` The case shot lengths are `1.2 / 1.2 / 2.2 / 2.2 / 3.3 / 4.2` seconds; the first segment contains only a person plus a fan info card, so it is the shortest; the roughly 1-second opening is a design choice of the case.
- `[sampled stills][12 03:35–05:49]` The price ladder `50k → 200k → 500k → 1M → ?` is the narrative skeleton; device-model labels serve the information progression rather than relying on stacked transitions.
- `[sampled stills][15 05:10–05:20]` The opening structure can be laid out directly as three timeline blocks: `抛出问题 → 揭示主题 → 混剪预告` (raise the question → reveal the theme → montage teaser).
- `[sampled stills][15 09:52–09:55]` The long-video segment check uses three columns: `我在干什么 / 我的状态 / 测试数值` (what I am doing / my state / test values); after segmenting, package compound clips and then assemble.
- `[sampled stills][15 12:34–13:16]` The `完成测试题` (complete the test question) card is marked at 3 o'clock, but the clock hand points to 6 o'clock; this is an internal inconsistency in the course visuals and cannot be treated as a precise rhythm law.
- `[sampled stills][16 05:18–06:22]` The Vlog mind map has four main branches: Giant Sequoia, Santa Barbara, Movie City, and Venice Beach; the theme wall marks the switch positions at 0/3/6/9 o'clock.
- `[sampled stills][01]` Lesson 01 is a promotional/channel-introduction film, not editing instruction; techniques cannot be extracted from promotional language.

## 2026-11 shot-density scan with video-storyboard

`[tool boundary][video-storyboard]` A full-frame scene-change scan (threshold 20) was run on all 18 lesson videos, using the course SRT as the transcript. Generated sheets and JSON stayed in the local analysis cache; only this aggregate table is kept in the Skill. The metric is **scene changes in the lecture recording**, not the cut rhythm of the exercise being taught.

Tool source: [video-storyboard](https://github.com/Ariakage/video-storyboard).

| Lesson | Duration | Scene cuts | Avg interval | Cuts/min | What the sheet shows |
| --- | ---: | ---: | ---: | ---: | --- |
| 01 | 1:52 | 53 | 2.1s | 28.3 | Promo/lecture montage; not a teaching edit |
| 02 | 5:05 | 112 | 2.7s | 22.0 | Setup, screen switches, examples |
| 03 | 11:37 | 198 | 3.5s | 17.1 | Basic edit; UI + demo cuts |
| 04 | 15:59 | 268 | 3.6s | 16.8 | Interview/talking head + B-roll |
| 05 | 11:34 | 335 | 2.1s | 29.0 | Densest editorial lecture: montage, Kuleshov, transitions |
| 06 | 11:31 | 221 | 3.1s | 19.2 | Sound examples, waveform/UI changes |
| 07 | 14:53 | 310 | 2.9s | 20.8 | Export/delivery screens + examples |
| 08 | 10:54 | 196 | 3.3s | 18.0 | Keyframe/curve demos |
| 09 | 10:51 | 269 | 2.4s | 24.8 | Speed demos; fast visual changes |
| 10 | 12:10 | 266 | 2.7s | 21.9 | Keying/mask/UI demos |
| 11 | 12:52 | 256 | 3.0s | 19.9 | Color panels/scopes |
| 12 | 18:43 | 374 | 3.0s | 20.0 | Packaging examples, price cards, phone motion |
| 13 | 10:54 | 1,163 | 0.6s | 106.7 | **Outlier**: screen/tracking UI changes, not editorial cutting |
| 14 | 8:45 | 143 | 3.7s | 16.4 | Multicam interview; slowest pacing |
| 15 | 20:34 | 467 | 2.6s | 22.7 | Long-form sections, clock/demo inserts |
| 16 | 14:49 | 341 | 2.6s | 23.0 | Vlog/mind map/color examples |
| 17 | 14:30 | 269 | 3.2s | 18.5 | AI panels and generated candidates |
| 18 | 14:24 | 341 | 2.5s | 23.7 | Mobile/social examples |

Total: 5,582 scene changes over 13,315 seconds (about 25.2 cuts/min).

### Teaching/demo visual grammar

`[inference][18 lesson sheets]` The same three visual modes recur across the lecture sheets:

1. **Instructor medium shot** at the desk: the “why”, continuity, and human anchor.
2. **Full-screen CapCut UI**: the “how”, parameters, menus, and timeline.
3. **Result/demo footage or split-screen comparison**: the “what it looks like”.

Picture-in-picture is the bridge: the instructor stays present while the UI fills the frame. The pattern is a production grammar, not an editing rule from the course.

Practical rules for a teaching/demo video:

- Use full-screen UI when the viewer must read a parameter; do not cut away before it is readable.
- Use PIP when the explanation must stay connected to the UI; keep the instructor small enough not to cover the panel.
- Return to the result/demo after a parameter change; do not leave the viewer staring at a panel.
- Keep the instructor’s framing, lighting, and background stable; treat the UI as a neutral, high-contrast surface.
- A teaching video is not a montage: a high scene-change count can come from UI switches, not narrative cutting. Check the content type before copying a cut rate.
- `[pending verification]` The exact readable duration for a parameter and the best PIP size were not measured; verify on the target screen.

### Content-type cut economy (observed ranges)

`[inference]` From the same scan, not a rulebook:

- Interview / multicam: about 16–17 cuts/min (3.6–3.7s average).
- UI / tutorial: about 17–22 cuts/min (2.7–3.5s).
- Montage / speed / mobile: about 23–29 cuts/min (2.1–2.5s).
- Screen/UI outlier: lesson 13 at 106.7 cuts/min; not an editorial target.

Compare only within the same content type, and confirm the cut motivation on the sheet before changing an edit.

How to read the table:

- A course's lecture cut rate is **not** a target for the student's edit. It mixes camera cuts, instructor cutaways, UI/panel changes, and demo footage.
- 13's 106.7 cuts/min is a screen/UI/tracking outlier; it does not mean the lesson teaches 0.6-second cutting.
- 05's 29.0 cuts/min is the densest editorial lecture, but it still includes instructor/UI cuts; use the sheet cells to separate the montage from the lecture.
- 14's 16.4 cuts/min reflects interview pacing; do not turn it into a universal interview rule.
- The interval is `duration / cuts` (arithmetic mean), not a median; a few long takes can shift it.
- Use this table to find sections worth reviewing, then inspect the sheet cells and zoom the cells that matter. Do not approve or reject an edit from the number alone.

Reproduce with the optional `video-storyboard` skill:

```bash
node "$CLAUDE_SKILL_DIR/bin/probe.mjs" "<video>" --json
node "$CLAUDE_SKILL_DIR/bin/storyboard.mjs" "<video>" \
  --transcript-file "<course.srt>" --strategy compact --max-sheets 3 --text --json
node "$CLAUDE_SKILL_DIR/bin/zoom.mjs" "<video>" --cell-id 7 --out zoom.png --json
```

Read every generated sheet before citing it. Cite both the cell number and the absolute time range printed in the index. Keep course sheets and JSON in the ignored analysis directory; never commit them.

## Currently pending verification

The sparse-dialogue demonstrations, actual rhythm peaks and valleys, music beat sync, and sound bridges in lessons 05, 15, and 16 still require continuous video review; the static structure has been checked with 2-second sampled stills, but this Skill is still a draft pending verification.
