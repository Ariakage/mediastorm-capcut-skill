---
name: mediastorm-delivery-handoff
description: Prepare CapCut or Remotion exports, versions, archives, covers, desktop/mobile handoff, and publication checks using source-aware settings and explicit authorization. Use at final delivery or handoff, not for creative editing decisions.
metadata:
  short-description: Export, archive, and hand off edits
  status: provisional-unverified-audiovisual
---

# MediaStorm Delivery Handoff

Deliver a project that can be identified, reopened, reviewed, and published without pretending that a proxy preview is the final product. This skill owns the final gate: source-aware settings, versioning, handoff, and platform checks.

## When to use

- A project is ready for export, review, archive, or publication.
- A cover, filename, folder structure, or version label must be chosen.
- Desktop and mobile need to hand off an editable draft.
- Export resolution, frame rate, bitrate, codec, audio, or color space must be selected.
- AI upscaling or frame interpolation is being considered.
- A platform’s current requirements must be separated from course-era examples.

Do not use this skill for story, dialogue, sound, motion, compositing, or color decisions; finish those first.

## Inputs to establish

- Delivery target: platform, device, client, archive, or internal review.
- Source resolution/frame rate, draft settings, aspect ratio, audio needs, and color space.
- Whether the deliverable is a sample, a final master, a platform upload, or an editable draft.
- Cover, naming, version, and archive requirements.
- Authorization: upload, publish, paid export, membership effects, cloud sync, or external sharing.

## Workflow

1. Confirm the delivery target and the source reality: resolution, frame rate, aspect ratio, audio, color space, and the draft’s actual settings.
2. Choose the cover deliberately. The course starts from the first frame, which is often black; use “Go to Select” to pick a representative frame, or the timeline’s cover icon [sampled stills][07 01:03–02:23].
3. Name the file for retrieval: date, project, resolution, version, and purpose. The course demonstrates `2026-01-10_混剪教学_4k_成片1_抖音` and warns against `最终版2/3/再也不改` [sampled stills][07 02:39–03:19].
4. Archive the project, media, and exports together. The course structure is `导出/成片/小样`, `视频/其他素材/Aroll/Broll`, `图片/包装设计素材/图片素材`, `音频/音效/BGM` [sampled stills][07 04:50.5].
5. Check media/effects before export: offline media, proxy/original links, missing effects, membership-dependent resources, captions, safe areas, and audio integrity.
6. Choose resolution from the source and the target. The course resolution menu includes `480P 854*480 / 720P 1280*720 / 1080P 1920*1080 / 2K 2560*1440 / 4K 3840*2160 / 8K 7680*4320 / 原始 1920*1080` [sampled stills][07 05:09]. Do not invent detail by exporting a 1080p source at 4K.
7. Choose frame rate from the draft/source and the motion. The draft menu includes `24.00 / 25.00 / 29.97 / 30.00 / 50.00 / 59.94` fps; the demo selects 30.00 [sampled stills][07 07:35].
8. Choose bitrate, codec, and audio from the target. The course’s bitrate table is printed in `KB/s` with values in the tens of thousands, while the custom field uses `Kbps`; the literal difference is 8×, and the course does not explain it [sampled stills][07 10:38.5–10:46]. Never convert the table directly into FFmpeg parameters or platform rules.
9. Distinguish containers from codecs. The course codec list is `H.264`, `HEVC`, `HEVC (Alpha)`, `Apple ProRes 422 / 422 LT / 422 HQ`; H.264 is the compatibility starting point, HEVC is an efficiency option that needs compatibility/speed checks [sampled stills][07 11:27].
10. Choose audio deliberately. The course audio-quality list is `AAC 192kbps / AAC 256kbps / AAC 320kbps / PCM 无损`; the demo ends on AAC 320kbps. The audio export section can be `MP3 320kbps / 48000Hz` with GIF 320P and subtitle SRT/UTF-8 [sampled stills][07 12:22–13:44].
11. Check AI upscaling/frame interpolation segment by segment. The course shows before/after AI-upscale comparisons and demonstrations of texture artifacts, over-smoothing, and 60fps “slippery” motion [sampled stills][07 07:50–08:56]. These are review prompts, not guarantees.
12. If desktop/mobile handoff is needed, transfer an editable draft, not only a flattened video. The course menu offers `上传` (Upload), `剪映快传` (CapCut Quick Transfer), and `我的云空间` (My Cloud Space); the desktop can download and reopen the draft [sampled stills][18 10:50–12:46].
13. Verify cross-device consistency: media, effects, timeline structure, magnetic behavior, captions, and versions. The course warns that phone/desktop magnetic rules can differ, especially when the main track has gaps [sampled stills][18 12:46–13:52].
14. Check the final output in the intended player/platform preview. A render, a proxy preview, a CapCut reopen, and a platform upload are different evidence layers.
15. Publish only after explicit authorization and after rechecking current platform requirements. Course-era screens are historical examples.

## Decision rules

- If the source is 1080p, do not promise 4K detail from an export setting; upscaling may add artifacts.
- If the frame rate is chosen only because a platform “supports” it, check the source and motion first.
- If the bitrate table’s `KB/s` value is being converted to `Kbps`, stop; the course does not resolve the 8× difference.
- If a membership effect or asset is required, confirm the account/entitlement before export.
- If a cover is the first frame and it is black, choose another frame.
- If the handoff is only an MP4, the recipient cannot revise the edit; transfer the draft instead.
- If the phone and desktop timelines differ, do not force a sync; keep the main track simple and test the round trip.
- If the final output has not been watched and heard at normal speed, it is not delivered.

## CapCut execution notes

- `capcut render` is a low-resolution FFmpeg proxy preview; `--strict` can reject unfaithful content, but it is not CapCut’s final export.
- `capcut export` is an experimental macOS UI automation path; it is not a default safe route until tested.
- Structure checks, proxy previews, CapCut reopen/save, final audiovisual review, and target-platform preview are distinct evidence.
- Cloud sync and upload require explicit authorization; a successful sync is not proof of cross-device fidelity.

## Remotion / TypeScript Adapter

- Render with `npx remotion render`, `@remotion/renderer`, or `@remotion/lambda`; use `calculateMetadata` to keep canvas/duration correct.
- `@remotion/player` is for in-app review, not final platform acceptance.
- `mediabunny`/FFmpeg can check duration, dimensions, and stream metadata after render.
- Render success does not prove platform acceptance; cover, naming, rights, and target-platform checks remain external.

## Failure conditions

- A proxy preview is reported as the final render.
- The export resolution invents detail the source does not have.
- The `KB/s` table is converted to FFmpeg/platform rules without resolving the unit.
- A membership effect is missing at export time.
- The cover is a black first frame.
- The handoff is a flattened MP4 when the recipient needs an editable draft.
- Phone/desktop timelines are assumed identical.
- Publishing happens without authorization or current platform checks.

## Acceptance checklist

- [ ] Delivery target and source reality confirmed.
- [ ] Cover chosen deliberately, not by default.
- [ ] Filename and archive structure identify date/project/resolution/version/purpose.
- [ ] Media/effects/membership/captions/safe area/audio checked.
- [ ] Resolution/frame rate chosen from source and target.
- [ ] `KB/s` vs `Kbps` ambiguity preserved.
- [ ] Codec/container/audio settings recorded.
- [ ] AI upscaling/interpolation reviewed segment by segment.
- [ ] Handoff is an editable draft when revision is expected.
- [ ] Cross-device round trip tested.
- [ ] Final output watched/listened to at normal speed.
- [ ] Current platform rules rechecked; publication authorized.

## Output contract

Return: the delivery target, source/settings matrix, cover/naming/archive decisions, what was actually verified (structure/proxy/interface/audiovisual/platform), what remains unverified, and the authorization state. Do not call a file “final” from an export dialog alone.

Read [references/delivery-checklist.md](references/delivery-checklist.md) for the full gate list and course timecodes.
