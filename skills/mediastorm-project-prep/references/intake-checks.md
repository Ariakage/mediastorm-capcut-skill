# Project intake checks

Evidence tags: `[course evidence]` denotes course evidence, `[inference]` denotes engineering organization, and `[tool boundary]` denotes a local tool fact.

## Check order

1. `[course evidence][02 03:02–03:40]` Check the actual codec and decodability; do not let the file extension substitute for that judgment.
2. `[course evidence][07 05:03–07:53]` Record source resolution, frame rate, duration, audio channels, and sample rate; export decisions are deferred to the delivery stage.
3. `[course evidence][04 01:25–02:50]` Organize media by project and split it by purpose into sample/final versions, A-roll/B-roll, packaging, images, sound effects, and BGM.
4. `[course evidence][16 01:01–03:05]` Keep the camera's original filenames and add meaning through directories and lists, so traceability relationships are not lost.
5. `[course evidence][07 02:21–05:03]` After migration, perform relink and reopen checks; do not assume that moving an entire directory will necessarily restore every reference.
6. `[course evidence][02 03:40–04:17]` Locate cache, background tasks, and preview load first, then decide whether proxies are needed.
7. `[course evidence][03 09:32–10:29]` Proxies are used to reduce preview load; confirm that original media is used before final output.

## Intake gate

- Originals are unchanged, and hash or source records are traceable.
- All required media is decodable, locatable, and relinked.
- Source frame rate, resolution, audio tracks, duration, and key time ranges have been recorded.
- The relationship between proxies and original files is explicit.
- Private media will not be uploaded or synchronized automatically.
- The draft is an isolated copy or a target explicitly authorized by the user.

## 2026-10 sampled stills review supplement

- `[sampled stills][02 01:50–02:42]` The editing interface has four regions: media panel, player, parameter/properties panel, and timeline; the layout can be changed and panels can be dragged; the course uses the `Final Cut Pro X` keyboard preset.
- `[sampled stills][02 03:12–03:20]` The link-media dialog shows `0/19 条媒体已链接` (0/19 media linked) and supports `链接文件夹时自动匹配缺失媒体` (automatically match missing media when linking a folder).
- `[sampled stills][02 03:48–04:00]` The cache panel shows `5.85GB` and can be set to automatically delete caches older than `30` days; automatic backup is an independent switch.
- `[sampled stills][02 04:40–04:52]` Cloud sync path: right-click the draft on desktop → `上传至云空间` (Upload to Cloud Space) → download from `我的云空间` (My Cloud Space) on the phone; `43.5GB` is visible on the phone.
- `[sampled stills][03 02:16–02:48]` The imported folder `课程1-1` (Course 1-1) is labeled `19 个项目` (19 items), with 13 videos + 1 audio visible; the audio `...musicbed-licen.wav` is `04:27` long.
- `[sampled stills][03 02:20 / 05:44]` Draft parameters include name, save location, import method, color space `Rec.709 SDR`, floating-point pipeline, free layer order, proxy mode, timeline name, aspect ratio, resolution, and `30.00帧/秒` (30.00 fps); the draft name `3月18日` (March 18) and the save path `4月2日 (2)` (April 2 (2)) do not match, so the demo project may be a copy.
- `[sampled stills][16 01:07–02:22]` Real project directory example `2026-02-03-加州样片日记` (2026-02-03 California sample diary), with subdirectories `01_工程文件、02_素材、03_音乐、04_音效、05_特效、06_字幕、07_导出、08_封面、09_归档` (01_project files, 02_media, 03_music, 04_sound effects, 05_effects, 06_subtitles, 07_export, 08_cover, 09_archive); second-level media use the naming pattern `日期_设备_机位编号_地点/事件` (date_device_camera-number_location/event).
- `[sampled stills][18 10:32]` The desktop export dialog shows `以草稿尺寸（720×1280）导出` (export at draft size (720×1280)); a phone project can be edited further on desktop.

## Failure and stop conditions

- Media exists only in an unknown cloud location or on a dead path.
- Source files are mutable network links, and their version cannot be traced.
- The user asks to clear caches, but the scope, file types, and backups are unconfirmed.
- The media only supports a low-resolution proxy, yet a high-resolution final cut is promised.
- Cloud sync or an external model is required, but there is no authorization.

## capcut-cli boundary

- Use `capcut projects`, `info`, `materials`, `tracks`, `segments`, and `diagnose` for read-only diagnosis.
- Before writing, obtain the corresponding `describe --command` contract; command-level `mutates` does not represent the side effects of a specific option.
- Do not use bare `capcut describe` as a machine-contract source; stdout truncation was previously observed on local version 0.31.1.
