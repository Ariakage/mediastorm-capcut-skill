# Talking-head, interview, and multicam

## Semantic editing

- `[course evidence][04 03:01–04:39]` The waveform can only locate pause candidates; repetition, slips of the tongue, and completeness of expression require semantic judgment.
- `[course evidence][04 04:39–06:29]` Smart talking-head rough cutting can speed things up, but preserve the breaths and pauses the delivery needs; if the cut points feel too tight, then consider spacing, short dissolves, or room tone.
- `[course evidence][17 01:22–03:53]` Pause trimming and semantic filtering are two different kinds of work; do not treat low volume as no value.
- `[course evidence][17 03:53–05:16]` The verbatim transcript can assist take selection; keep the original media, the selection rationale, and a rollback version.
- `[course evidence][17 05:16–07:33]` Topic search yields a candidate set, which is not the same as the complete interview.
- `[course evidence][17 07:33–08:43]` When instructing the AI, explicitly state what to keep, what to exclude, the topic, and the output format; deleting a word from the audio does not prove the picture has also been removed.

## A-roll / B-roll

- `[course evidence][04 06:29–08:59]` A-roll carries the main information and B-roll supplements it; browse the candidates first, then select complete semantic intervals.
- `[course evidence][04 08:59–10:56]` B-roll should work in groups to serve one complete idea; exposed jump cuts can be handled with related footage or intentional changes in shot size.
- Do not permanently mute all B-roll; narrative sync sound should be judged separately.

## Pickups, subtitles, and audio channels

- `[course evidence][04 10:56–12:59]` For pickups, prioritize improving distance and the environment; unifying loudness in post is not the same as giving every clip the same gain.
- `[course evidence][04 12:59–14:28]` Before adding BGM, identify and correct subtitles as much as possible, and check the platform UI safe zone.
- Checking left/right channels, noise floor, and clipping requires actual listening; current ASR cannot replace it.

## Multicam

- `[course evidence][14 01:09–02:50]` Before syncing, first prove that all cameras belong to the same real moment; peaks, claps, and timecode can serve as synchronization evidence.
- `[course evidence][14 03:24–04:40]` Auto-alignment and the multicam view can reduce the rough-cut burden, but afterward still check lip sync, shared events, and long-term drift.
- `[course evidence][14 04:40–06:52]` Favor the speaker, with reaction shots as support; reactions must not fabricate context.
- `[course evidence][14 06:52–08:23]` Lower-thirds and highlight-quote packaging serve recognition and clip segmentation; they do not promise view counts.

## 2026-10 sampled stills review supplement

- `[sampled stills][04 03:44–03:46]` In the track adjustment popover, `波形占比` (waveform proportion) has a 60% hover tooltip; after raising the waveform, flat segments are only pause candidates and cannot prove that no one is speaking.
- `[sampled stills][04 03:56–04:16]` Manual rough-cut sequence: place the playhead at the start of the flat waveform → `Command+B` (Windows `Ctrl+B`) for the first cut → cut again at the end → select the middle segment and delete, i.e. `两刀删中间` (two cuts, delete the middle).
- `[sampled stills][04 05:04–05:18]` Smart talking-head cut presents the transcript on the left, the player on the right, and the timeline below; the transcript marks tokens such as `停顿 [...0.2s]` (pause [...0.2s]) and `语气词 这个` (filler word "this"); deleting text also deletes the corresponding video.
- `[sampled stills][04 05:50–06:08]` Breath-gap repair: split into two segments → drag the audio handle (tooltip `0.1s`) to add a small dissolve → lay a short piece of room tone on the second track; this is operational evidence, and the final listening impression still requires listening verification.
- `[sampled stills][04 12:42–12:54]` `声道配置` (channel configuration) has only three entries: `无` (none), `将左侧声道填充至右侧声道` (fill the right channel from the left channel), and `将右侧声道填充至左侧声道` (fill the left channel from the right channel).
- `[sampled stills][04 13:45.5–13:57.5]` Subtitle font `系统` (system), size 8 → `思源黑体 CN` (Source Han Sans CN), size 5; white text, letter/line spacing 0; the shadow ends at `不透明度 59%、模糊 7%、距离 5、角度 -45°` (opacity 59%, blur 7%, distance 5, angle -45°), of which 68% was an intermediate value during dragging.
- `[sampled stills][04 14:02–14:10]` The preview overlays a `16:9视频播放安全区` (16:9 video playback safe zone) mask; do not place subtitles against the edge, and check platform UI occlusion before publishing.
- `[sampled stills][14 01:34–02:40]` The sync basis is the audio waveform/slate clap and a hardware timecode generator; at 01:50 the four-camera timecodes are A `1:10:04:27`, B `1:10:03:24`, C `1:10:03:26`, and D `1:10:03:26`. A and B differ by about 1 second 3 frames, so they cannot be aligned directly by the file start; the old note `相差约 3 秒` (about 3 seconds apart) should be corrected with this on-screen reading.
- `[sampled stills][14 02:22–02:30]` The timeline's four tracks are `TimCook机位.mov`, `Tim机位.mov`, `Links机位.mov`, and `全景机位.mov` (Tim Cook camera, Tim camera, Links camera, wide camera), all about `00:16:42:29` long and all starting at `1:10:03:25`.
- `[sampled stills][14 03:32–04:16]` `新建多机位片段` (New Multicam Clip) dialog: clip name `多机位片段1` (Multicam Clip 1); alignment `自动` (Automatic, checked)/`声音` (Sound); a proxy mode switch described as `可提升剪辑流畅度，不影响最终导出视频质量` (can improve editing smoothness without affecting final exported video quality); after creation, the multicam preview is on the left and the program monitor on the right.
- `[sampled stills][14 04:15–04:22]` The top-right of the multicam preview can switch between `4机位` (4-camera) and `9机位` (9-camera) views.
- `[sampled stills][14 05:20–06:40]` Multicam switching: park the playhead on the target frame; the left preview becomes a razor, and clicking a camera cuts automatically; if the cut is wrong, click the correct camera again to change it back, and the timeline distinguishes them by color. The camera numbering order differs between 04:16 and 05:30 (01 Tim Cook/02 Tim/03 wide/04 Links vs 01 wide/02 Tim/03 Links/04 Tim Cook); no reordering operation was seen, [pending verification].
- `[sampled stills][14 06:54–08:00]` The lower-third workflow goes `文字 → 文字模板 → 搜索人名条/角标` (Text → Text templates → search name bar/lower third); the cases are `Tim / 采访者` (Tim / interviewer), `Links / 采访者` (Links / interviewer), and `Tim Cook / 被访者` (Tim Cook / interviewee); the template text panel shows font `剪映简明` (CapCut Jianming), size 15. The template placeholder text is `姓名`, `xingming`, and `某某公司亚太地区执行副总裁` (name, xingming, Executive Vice President, Asia Pacific, XX Company).
- `[sampled stills][17 02:08–02:18]` The smart talking-head cut transcript panel filters include `气息/重复/停顿` (breath/repetition/pause) and `最短停顿时长 0.5s` (minimum pause duration 0.5s); no separate take-selection panel was found; the closest thing is transcript check/replace.
- `[sampled stills][17 04:24]` The long prompt explicitly states `比较情绪与流畅度、自动切除失败 Take、只保留效果最好的一段放在主轨` (compare emotion and fluency, automatically cut failed takes, keep only the best-performing segment on the main track); the resulting segments are dense and butt end to end.

## Tool boundary

- `[tool boundary][capcut-cli 0.31.1]` `detect-silence` only produces silence candidates.
- `[tool boundary][capcut-cli 0.31.1]` `detect-retakes` uses subtitle word-order similarity and prefers the later occurrence; it does not judge emotion or fluency.
- Save a rollback version before writing; preview the candidate range before deleting an existing timeline.
