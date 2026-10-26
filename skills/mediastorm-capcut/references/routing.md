# Routing matrix

This reference maps user requests to child skills. The entry point only identifies the target, composition order, and evidence boundary; it does not carry all the detail.

## Determine the delivery form first

- If the request only changes subtitles, timing, speed, volume, or ordinary assets in an existing CapCut draft, prefer the generic capabilities of the existing `capcut-edit`; this bundle is responsible for editorial judgment and acceptance.
- If the request involves "why edit it this way, how to judge it, how to accept it", use this bundle.
- If the request requires uploading private assets, calling cloud AI, spending credits, publishing content, or overwriting disk state, stop first and obtain explicit authorization.

## Child skill routing

| User goal or material state | Route | Do not mistake it for |
| --- | --- | --- |
| Whether assets can be imported, unknown codec/frame rate, offline media, disordered directories, proxy stutter | `mediastorm-project-prep` | Story problem |
| Unclear video message, section order, information density, whether B-roll serves the narrative, long-form/short-form pacing | `mediastorm-story-structure` | Beat-sync or transitions alone |
| Talking-head fine cut, interviews, take selection, breath pauses, captions, multicam sync | `mediastorm-dialogue-interview` | Music/sound design |
| Musical resolution, sound leading/continuing, ambience, designed sound effects, tail sound, loudness intent | `mediastorm-music-sound` | Dialogue semantic choices |
| Slow motion, speed-up, action peaks, whether the source frame rate is sufficient, frame-interpolation risk | `mediastorm-speed-time` | Ordinary keyframe animation |
| Push-in/pan, per-parameter easing, point-tracked labels, number flicker, timers | `mediastorm-motion-graphics` | Planar tracking or keying |
| Smart/chroma keying, masks, blend modes, layer occlusion, planar-tracking failure | `mediastorm-compositing-tracking` | Color grading or ordinary point tracking |
| Log restoration, scopes, curves, shot-to-shot matching, skin tone and style | `mediastorm-color-grading` | Export settings |
| AI-generated B-roll, concept shots, localized generative effects, cost and authenticity | `mediastorm-generative-broll` | AI take selection or upscaling acceptance |
| Cover images, versions, export, archiving, phone/desktop handoff, pre-publication checks | `mediastorm-delivery-handoff` | Creative stage |

## Common composition orders

1. Talking-head short: project intake → semantic rough cut/breath pauses → B-roll structure → captions → music/sound effects → delivery.
2. Dialogue-free montage: project intake → asset relationships and sections → music/sound → speed/motion → color → delivery.
3. Tutorial packaging: project intake → structure → parameter animation/number packaging → spatial tracking/compositing → sound → delivery.
4. Interview: project intake → multicam sync and primary audio → semantic editing → reaction shots and B-roll → captions → delivery.
5. Phone to desktop: phone rough cut → editable draft handoff → desktop fine cut → cross-device consistency → export and archiving.

## Routing output

Write a one-line route before starting work, for example:

`Project intake → semantic talking-head edit → sound bridge → planar-tracking packaging → delivery check.`

If any step lacks inputs, authorization, or a verification path, mark that step blocked; do not skip acceptance and still declare completion.
