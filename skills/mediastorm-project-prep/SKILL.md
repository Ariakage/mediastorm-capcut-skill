---
name: mediastorm-project-prep
description: Prepare and audit CapCut or Remotion media projects before editing — inventory codecs, frame rates, resolutions, audio, file provenance, relinking, proxies, and draft settings. Use for intake and playback-risk checks, not for story, sound, or color decisions.
metadata:
  short-description: Prepare and audit editing projects
  status: provisional-unverified-audiovisual
---

# MediaStorm Project Prep

Prepare the project so later editing decisions rest on reliable media, paths, and playback conditions. This skill owns the intake gate: if a source is missing, mislabeled, or unreadable, stop before the timeline becomes the place where the problem is discovered.

## When to use

- A new project, a handed-off project, or a folder of camera/phone/screen recordings needs an intake check.
- Media is offline, playback stutters, a proxy/relink decision is needed, or the draft settings are unclear.
- A CapCut draft is about to be edited by `capcut-cli` or by a person, and the source/proxy relationship must be recorded.
- A Remotion project needs deterministic `calculateMetadata`, `staticFile()`, or asset checks.

Do not use this skill for story order, take selection, sound design, color grading, or export specs; route those to the matching child skill.

## Inputs to establish

- Target draft or project folder, and whether it is an isolated copy.
- Source folders, camera/phone/screen origin, and whether the media may be uploaded or synced.
- Delivery target and any hard constraints (aspect ratio, frame rate, resolution, platform).
- Whether the user authorized cache cleanup, relinking, proxy generation, or cloud sync.

## Workflow

1. Freeze the originals and record a manifest: path, filename, size, hash if available, and source device.
2. Probe every source for container, codec, resolution, frame rate, duration, audio channels, and sample rate; do not infer from the extension.
3. Decode-test at least one frame/audio block per source. A playable extension is not proof; a failed decode is a stop condition.
4. Organize by project and purpose: exports/finals/samples, A-roll/B-roll/other video, packaging/images, music/SFX, drafts, and archives. Keep camera filenames when they carry provenance; put human-readable meaning in folders or a manifest.
5. Relink missing media and reopen the draft. In the course demo the link-media dialog shows `0/19 条媒体已链接` (0/19 media linked) and supports folder-level auto-matching [course evidence][02 03:12–03:20].
6. Read the draft settings before editing: draft name, save path, import mode, color space, floating-point pipeline, free layer order, proxy mode, timeline name, aspect ratio, resolution, and frame rate. The demo shows `Rec.709 SDR` and `30.00帧/秒`, but its draft name and save path do not match, so treat the demo as a copy [course evidence][03 02:20 / 05:44].
7. If free layer order is enabled and saved, the course warns that it cannot be disabled afterward. Confirm that the project needs it before turning it on [course evidence][03 05:44].
8. Reduce playback load deliberately: identify cache/background load first, then lower preview quality or use a proxy. The course cache panel shows `5.85GB` and an auto-delete option for caches older than `30` days [course evidence][02 03:48–04:00].
9. Record the proxy policy: `720P` / `540P` are preview aids; the final output must use the original. Do not let a proxy replace the source in the export path [course evidence][03 09:32–10:29].
10. Record the handoff gate: originals intact, media online, source parameters known, proxy/original relationship explicit, permissions respected, and the next skill named.

## Decision rules

- Unknown source frame rate or resolution → no promise about delivery resolution, slow motion, or frame-rate conversion yet.
- Extension and actual codec disagree → trust the decode test, not the filename.
- Proxy exists but the original is missing → stop; do not grade, track, or export from the proxy as if it were the master.
- Draft name/path disagree → treat the project as a copy until the user confirms which copy is authoritative.
- Cache cleanup is requested but the scope, file types, and backup are unconfirmed → stop and ask.
- Cloud sync is convenient but not automatic permission; confirm account, project, and upload scope first.

## CapCut execution notes

- Use `capcut projects`, `info`, `materials`, `tracks`, `segments`, and `diagnose` for read-only diagnosis.
- Before any write, fetch the current `capcut describe --command <name>` contract; command-level `mutates` does not capture option-level side effects.
- Do not use bare `capcut describe` as a machine-contract source; stdout truncation was observed on local version 0.31.1.
- Close the project in CapCut before writing and reopen it for visual acceptance afterward.

## Remotion / TypeScript Adapter

- Use `mediabunny` for duration/dimensions and `calculateMetadata` to set `durationInFrames`, `width`, `height`, and `fps` from the actual asset.
- Put media in `public/` and reference it with `staticFile()`; define editable props with `zod` or `@remotion/zod-types`.
- Remotion has no built-in relink/cache/proxy UI. Keep a manifest, relative paths, and checksums; fail loudly when a source is missing.
- A proxy can improve Studio preview but must not replace the original at render time.

## Failure conditions

- Media exists only in an unknown cloud location or on a dead path.
- Source files are mutable network links, and their version cannot be traced.
- A cache cleanup is requested without scope, file types, or backup confirmation.
- Only a low-resolution proxy exists, yet a high-resolution final is promised.
- Cloud sync or an external model is required, but there is no authorization.
- The intake gate is skipped and the first timeline action is already destructive.

## Acceptance checklist

- [ ] Originals unchanged, with a traceable source record.
- [ ] Every required source decodes; stream parameters recorded.
- [ ] Missing media relinked and the draft reopened.
- [ ] Draft settings read and consistent with the intended timeline.
- [ ] Proxy/original relationship explicit; export path uses originals.
- [ ] Private media not uploaded or synced without permission.
- [ ] The next child skill and its required evidence are named.

## Output contract

Return a short intake report with: source inventory summary, decode/relink result, draft settings that matter, proxy policy, permissions, stop conditions, and the recommended next skill. Separate observed facts, inferred risks, and tool results; do not report “ready” from a file listing alone.

Read [references/intake-checks.md](references/intake-checks.md) for detailed checks, failure conditions, and course timecode evidence.
