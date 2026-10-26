# Evidence and safety boundaries

This bundle stores original synthesis, judgment frameworks, and tool adaptations; it does not store course footage, full subtitles, audio, frame extracts, or full transcripts.

## Current evidence status

- Read: all 6,198 AI-generated Chinese subtitle cues across 18 lessons.
- Viewed: first pass, 36 sheets / 674 sampled stills at 20-second intervals; second pass, all 18 lessons sampled at **2-second intervals**, totaling **6,656 frames / 1,658 timestamped index sheets**, reviewed sheet by sheet, with targeted full-resolution grabs of interface parameters.
- Run: local ASR on the full audio tracks of all 18 lessons, comparison of 453 30-second windows, and a small number of localized re-recognitions.
- Not completed: continuous video understanding, original-audio listening, perception of music/sound effects/tone/rhythm, and frame-by-frame acceptance of fast motion.
- 2026-10-26 supplemental probe in this session: the user referenced a local MP4 with `@`; the context supplied only the path, and Read returned "Cannot display content of binary file". Kimi API documentation says video can be sent through Base64 in `video_url` or through file upload, but the user had not yet authorized external API uploads, API-key use, or costs; this round chose to build the not-yet-accepted skill first.
- Picture corrections and course-internal contradictions are in [visual-evidence-2026-10.md](visual-evidence-2026-10.md); 2-second sampling is not continuous video and cannot replace listening or motion acceptance.

## Tag conventions

- `[course evidence]`: original synthesis derived from course subtitles, sampled stills, or verified frames; retain the lesson number and timecode.
- `[sampled stills]`: a fact visible in the 2-second sampled frames or a targeted full-resolution grab, not proof of continuous motion.
- `[course narration]`: a claim taken from the burned-in subtitle or spoken explanation, not independently verified from the picture.
- `[inference]`: advice derived from the course or engineering logic; do not present it as the instructor's own words.
- `[tool boundary]`: local command contracts, independent experiments, or script results; do not extrapolate them to unverified CapCut interface capabilities.
- `[pending verification]`: still requires continuous audio/video, interface operation, or real output for confirmation.

Chinese UI labels inside backticks or quotes are literal interface evidence, followed by an English gloss. They are not a second language for the prompt.

## Numeric rules

By default, treat values in the course as case parameters, including 2–3 seconds, 0.3×/0.1×, about 2 frames, 0.4 seconds, 45%, 1080p/30fps, 4K/60fps, and so on. Convert them into project parameters only when the user's project conditions match and actual acceptance has passed.

The bitrate table at 10:38 in lesson 07 is printed in `KB/s` with values in the tens of thousands; do not convert this unit directly into FFmpeg parameters or platform rules.

## External actions

The following actions require separate user authorization:

- uploading course material, client assets, or private projects;
- calling cloud models or cloud AI, syncing, or publishing;
- consuming credits, API quota, or subscription benefits, or incurring costs;
- overwriting existing drafts, force-writing, deleting assets, or clearing caches;
- publicly distributing material that contains paid-course information.

## Acceptance layers

1. Structure layer: JSON/schema/lint succeeds.
2. Proxy layer: an FFmpeg preview is generated and duration/media checks pass.
3. Interface layer: CapCut can open and save the draft and shows the expected structure and effects.
4. Audiovisual layer: the final result has been watched and listened to at normal speed.
5. Delivery layer: review on the target device or platform passes.

Success at any one layer does not automatically substitute for subsequent layers.
