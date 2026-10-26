# Export, Versioning, and Cross-Device Delivery Checklist

## Versions and Covers

- `[course evidence][07 00:52–02:21]` Select the cover separately; the first frame may be black, so the first frame should not be used by default.
- `[course evidence][07 02:21–05:03]` The filename carries the date, title, resolution, version, and purpose; archiving must include media and the project.
- `[course evidence][16 13:28–14:49]` Samples and final exports go into separate directories with versions retained; verify by reopening after archiving.

## Parameter Decisions

- `[course evidence][03 10:29–11:10]` The Lesson 03 example is 4K/60fps/HEVC/PCM/48kHz; it is a one-time exercise setting, not a universal preset.
- `[course evidence][07 05:03–07:53]` Resolution must not fabricate detail the source footage lacks; for frame rate, check the draft and the original footage first, then choose according to scene and goal.
- `[course evidence][18 09:40–10:50]` The mobile course's 1080p/30fps is a starting point for a different set of working conditions and is not merged with the desktop examples.
- `[course evidence][07 07:53–09:09]` AI upscaling/frame interpolation requires checking texture artifacts, over-smoothing, and motion errors segment by segment.
- `[course evidence][07 09:09–10:59]` Bitrate is affected by complexity, frame rate, resolution, and encoding efficiency; an extremely high bitrate does not guarantee a better result after platform re-compression.
- `[course evidence][07 00:10:38]` The table's `KB/s` unit is ambiguous; do not convert it directly into FFmpeg parameters or platform official requirements.
- `[course evidence][07 10:59–11:56]` Distinguish container from codec; H.264 is the compatibility starting point, and HEVC is a compression-efficiency option that requires testing.
- `[course evidence][07 12:22–13:55]` Choices such as AAC, PCM, and 48kHz are determined by the goal; misrecognitions in the subtitles must not be treated as official formats.
- `[course evidence][07 13:55–14:20]` Before exporting, check for membership-based media or feature dependencies, and do not treat a feature that was free for a limited time then as a permanent fact.

## 2026-10 Sampled Stills Review Supplement

- `[sampled stills][03 10:44–11:04]` First export demonstration: resolution `4K`, format `MP4`, frame rate `30 → 60 fps`, video bitrate `更高` (Higher), codec `HEVC`, audio `PCM 无损 / 48000 Hz` (PCM Lossless / 48000 Hz), color space `Rec.709 SDR`; estimate `1分21秒 / 357MB` (1 min 21 s / 357MB), and after changing parameters it once showed `387MB`.
- `[sampled stills][07 10:38.5–10:46]` Bitrate reference table, cell by cell: Douyin 1080p–4K/30/Recommended/`20000–35000 KB/s`; Xiaohongshu 1080p–4K/30/Recommended/`10000–25000`; Bilibili 2K–4K/60/Higher/`40000–45000`; YouTube 2K–4K/60/Higher/`40000–45000`. The table's unit is indeed `KB/s`, while the export panel uses `Kbps`, a literal 8× difference; it cannot be used directly as FFmpeg parameters or platform limits.
- `[sampled stills][07 05:09 / 07:35]` Full resolution dropdown: `480P 854*480 / 720P 1280*720 / 1080P 1920*1080 / 2K 2560*1440 / 4K 3840*2160 / 8K 7680*4320 / 原始 1920*1080` (Original 1920*1080); draft frame-rate dropdown `24.00 / 25.00 / 29.97 / 30.00 / 50.00 / 59.94 帧/秒` (frames/sec), with the case checking 30.00.
- `[sampled stills][07 11:27]` Codec dropdown: `H.264` (more universal), `HEVC` (saves more space), `HEVC (Alpha)`, `Apple ProRes 422 / 422 LT / 422 HQ`.
- `[sampled stills][07 13:46.5 / 13:54.8]` Exporting dialog: `2026-01-10_混剪教学_4k_成片1_抖音` (2026-01-10_Mashup Tutorial_4k_Final Cut 1_Douyin), 42 seconds, 138MB (estimated), 4K 3840×2160, recommended bitrate, H.264, MP4, Rec.709 SDR, 30fps, progress 11.0%; 3 membership entitlements. At 13:50.8 a different reading of `1分2秒 / 117MB` (1 min 2 s / 117MB) appears, inconsistent with 42 seconds/138MB; no corresponding project or export record was seen, [pending verification].
- `[sampled stills][07 12:22–12:34]` Audio quality dropdown: `AAC 192kbps / AAC 256kbps / AAC 320kbps / PCM 无损` (PCM Lossless); the case ends on `AAC 320kbps`.
- `[sampled stills][07 13:42–13:44]` Audio export section: format `MP3`, `320kbps`, `48000Hz`; GIF off, resolution `320P`; subtitle export off, format `SRT`, `Unicode / UTF-8`.
- `[sampled stills][07 15:27–16:31]` Concept animation: H.264 file `1.25GB` vs HEVC `650MB` (same example); HEVC exports more slowly and has worse compatibility with older devices.
- `[sampled stills][07 00:52–05:03]` The cover can be entered from the export panel or from the cover icon at the far left end of the timeline; the first frame is taken by default, and when the first frame is black you must select a frame manually. Naming example `2026-01-10_混剪教学_4k_成片1_抖音` (2026-01-10_Mashup Tutorial_4k_Final Cut 1_Douyin); archive contains `导出/成片/小样`, `视频/其他素材/Aroll/Broll`, `图片/包装设计素材/图片素材`, `音频/音效/BGM` (Exports/Finished/Samples, Video/Other Media/Aroll/Broll, Images/Packaging Design Assets/Image Assets, Audio/Sound Effects/BGM).
- `[sampled stills][18 09:50]` Mobile export settings: top `视频 / GIF / 实况(New)` (Video / GIF / Live Photo (New)); resolution `480P / 720P / 1080P / 2K / 4K`; frame rate `24 / 25 / 30 / 50 / 60 / 120`; the case stays at 1080P/30.
- `[sampled stills][18 10:08–10:14]` Mobile platform table: Douyin 1080P/30/Recommended or Higher/9:16; Xiaohongshu 1080P/30/Recommended or Higher/9:16 or 3:4; WeChat Channels 1080P or 4K/30/Recommended/9:16 or 16:9; Bilibili 1080P/30/Higher/16:9; Kuaishou 1080P/30/Recommended or Higher/9:16; TikTok 1080P/30/Recommended or Higher/9:16; for multiple platforms, follow the finished video's aspect ratio. The table is an experience-based preset from recording time, not a permanent platform rule.
- `[sampled stills][18 10:32]` Desktop export dialog: `720×1280` draft size, format `MP4` (dropdown includes MOV), 30fps, bitrate “推荐” (Recommended), audio export `MP3`, duration 41 seconds / 38MB (estimated).
- `[sampled stills][16 13:40–13:42]` Export `4K / MOV / 30fps / AI补帧开启` (AI Frame Interpolation on); paths are divided into `导出/成片` and `导出/小样` (Exports/Finished and Exports/Samples), and the template `年份-月份-日期_项目名字` (Year-Month-Date_Project Name) appears.
- `[sampled stills][12 11:05]` Vertical variety-show packaging export: `2160×3840`, 30fps, `50000 kbps`, H.264, MOV, Rec.709 SDR; duration about 18 seconds, estimated 110MB. This is a vertical-video case, not a universal preset.

## Cross-Device Handoff

- `[course evidence][18 10:50–12:46]` When continuing fine-tuning, transfer the editable draft rather than only copying the finished video; naming and covers serve to identify versions.
- `[course evidence][18 12:46–13:52]` After syncing, confirm media, effects, and timeline are consistent; mobile/desktop snapping rules may differ, and gaps in the main track must be tested.
- Cloud capacity, effect entitlements, and version differences require actual current verification.

## Tool Boundaries

- `[tool boundary][capcut-cli 0.31.1]` `render` is a low-resolution FFmpeg proxy preview; `--strict` can reject unfaithful content, but it is not CapCut's final export.
- `[tool boundary][capcut-cli 0.31.1]` `export` is an experimental automated batch export via the macOS UI; it has not yet been tested and is not treated as a default safe path.
- Structural checks, proxy previews, reopening and saving in CapCut, final audio-visual acceptance, and target-platform previews are different evidence levels.

## Final Delivery Gate

- Source parameters and export parameters match, with no fabricated detail.
- No offline media, and proxies are not mistaken for the original footage.
- Subtitle, safe-area, audio-channel, loudness, and ending checks are complete.
- Filename, cover, version, and purpose are identifiable.
- Project and media can be reopened, and cross-device results are consistent.
- Payment/membership/upload/publishing has received explicit user authorization.
- Current platform requirements have been re-checked, not relying on the UI from when the course was recorded.
