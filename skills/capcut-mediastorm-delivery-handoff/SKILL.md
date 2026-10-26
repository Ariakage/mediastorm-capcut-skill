---
name: capcut-mediastorm-delivery-handoff
description: Prepare CapCut exports, versions, archives, covers, desktop/mobile handoff, and publication checks using source-aware settings and explicit authorization. Use at final delivery or handoff, not for creative editing decisions.
metadata:
  short-description: Export, archive, and hand off edits
  status: provisional-unverified-audiovisual
---

# MediaStorm Delivery Handoff

Deliver a project that can be identified, reopened, reviewed, and published without pretending that a proxy preview is the final product.

## Core workflow

1. Confirm the delivery target, source frame rate and resolution, edit draft settings, aspect ratio, audio needs, platform constraints, and whether a sample or final master is required.
2. Choose cover imagery deliberately; never assume the first frame is representative or free of black.
3. Use filenames and folders that distinguish date, project, resolution, version, and purpose. Keep editable project files, linked media, manifests, sample exports, and final masters traceable.
4. Check offline media, proxy/original links, missing effects, membership-dependent resources, captions, safe areas, audio integrity, and downstream mobile/desktop differences before export.
5. Choose codec, resolution, frame rate, and bitrate from source quality and destination needs. Do not invent detail through export settings or treat a course example as a platform rule.
6. Inspect AI upscaling or frame interpolation segment by segment for texture artifacts, over-smoothing, and motion errors.
7. Distinguish containers from codecs. Use H.264 as a compatibility starting point and HEVC as an efficiency option that requires compatibility and speed checks.
8. Verify the real final output in the intended player or platform preview. Treat `capcut render` only as an FFmpeg proxy and the experimental UI export command as unverified until separately tested.
9. For desktop/mobile handoff, transfer an editable draft rather than only a flattened video, then verify media, effects, timeline structure, magnetic behavior, captions, and versions after sync.
10. Publish only after explicit user authorization and after checking current platform requirements rather than relying on historical course screens.

## Boundaries

- The course's 4K/60 fps desktop example and 1080p/30 fps mobile example address different conditions; neither is a universal preset.
- A course table showed `KB/s` with values that appear ambiguous for video bitrate. Preserve that ambiguity and do not convert it into command parameters without fresh official evidence.
- Do not assume file-embedded cover and platform-page cover are synchronized.
- Do not upload drafts, sync private projects, or spend on export/membership features without authorization.
- Treat this skill as provisional until continuous course audio/video review is completed.

Read [references/delivery-checklist.md](references/delivery-checklist.md) for the full gate list and course timecodes.
