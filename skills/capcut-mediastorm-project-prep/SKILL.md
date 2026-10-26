---
name: capcut-mediastorm-project-prep
description: Prepare and audit CapCut media projects using MediaStorm-inspired intake checks for codecs, frame rates, organization, relinking, proxies, and source traceability. Use before substantive editing, not for creative story or delivery decisions.
metadata:
  short-description: Prepare and audit editing projects
  status: provisional-unverified-audiovisual
---

# MediaStorm Project Prep

Prepare the project so later editing decisions rest on reliable media, paths, and playback conditions.

## Core workflow

1. Inventory sources before touching the timeline: path, filename, container, codec, resolution, source frame rate, duration, channels, and sample rate.
2. Check actual decodability rather than trusting an extension. Preserve camera/source filenames where they carry provenance, and put human-readable meaning in folders or manifests.
3. Organize material for retrieval: separate A-roll, B-roll, stills, packaging assets, music, sound effects, tests, drafts, exports, and final masters.
4. Repair missing media with relinking and verify a reopened draft before editing. Do not assume moving an entire folder preserves every absolute path.
5. Reduce playback load deliberately: identify cache/background load first, then use proxies or lower preview burden while keeping the original media linked for final output.
6. Record the intake gate before handing off: originals intact, media online, source parameters known, proxy/original relationship clear, and privacy/upload boundaries respected.

## Boundaries

- Do not upload private media or enable cloud sync without explicit authorization.
- Do not clean caches or user libraries as a substitute for diagnosing the project; deleting personal files requires separate confirmation.
- Do not convert course notes into software defaults. The course used a Final Cut Pro shortcut preset, so avoid presenting its demonstrated shortcuts as universal CapCut defaults.
- Treat this skill as provisional until continuous course audio/video review is completed.

Read [references/intake-checks.md](references/intake-checks.md) for detailed checks, failure conditions, and course timecode evidence.

When CapCut draft access is required, use current `capcut describe --command` contracts and the generic `capcut-edit` mechanics rather than reimplementing draft parsing here.
