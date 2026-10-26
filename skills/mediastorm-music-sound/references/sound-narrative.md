# Music and Sound Narrative

## Music closure

- `[course evidence][06 00:39–03:43]` Close the music on a suitable strong beat; when the tail is cut off, you can preserve the decay by extending the container, using a compound clip, and adding echo/reverb, so that only the needed tail is brought in.
- During acceptance, confirm that the tail is not cut off again, that the main music does not repeat unexpectedly, and that the tail volume does not mask dialogue.

## Sound-first and continuation

- `[course evidence][06 03:43–05:22]` Associate ambient sound from the picture, and use sound-first to establish expectations for the scene; continuing the previous shot's sound can form an L-cut.
- Advancing the wave sound by about 2–3 seconds is only the course example, not a fixed lead time for a J-cut.

## Designed sound effects

- `[course evidence][06 05:22–07:16]` Sound effects such as rises and low frequencies can change expectation and reinforce actions and turns, but their narrative purpose must be stated.
- `[course evidence][06 09:34–10:51]` Everyday recordings can become designed sound through speed changes, pitch shifting, layering, and reverb; the parameters are decided by listening.
- Avoid stacking sound effects just to have “something happening”.

## Resources and licensing

- `[course evidence][06 08:24–09:34]` Build a sound-effects library that is searchable and clearly licensed; Musicbed, Artlist, Storyblocks, and Envato Elements are examples from the course's resource table.
- Before use, check the license item by item for track, project, platform, and term. AI sound effects are only candidate sources; they are not automatically commercially usable or suitable for the final cut.

## Loudness and mix checks

- `[course evidence][04 10:56–12:59]` The quality of re-recorded audio and consistency of ambience take priority; uniform loudness does not mean the same gain on every clip.
- `[course evidence][04 14:28–15:26]` Fade out the end of the music to avoid a hard cut, but the specific duration must be decided by listening.
- `[tool boundary][capcut-cli 0.31.1]` `loudness` measures by default, `--target` calculates gain, and only `--apply` writes segment volume; `--per-clip` changes the overall mix-balance strategy.
- `[tool boundary]` `render` is an FFmpeg proxy preview and cannot prove the final export or CapCut audio behavior.

## 2026-10 visual review supplement

- `[sampled stills][06 01:37]` The audio clip panel tabs are `基础 / 换音色 / 声音效果 / 变速 / 改词翻唱` (Basic / Change voice / Sound effects / Speed / Rewrite lyrics and cover); under “声音效果” there are `场景音` (Scene sound) and `声音成曲` (Sound to song), with categories `热门 / 环境 / 美化 / 模拟` (Trending / Ambient / Beautify / Simulation).
- `[sampled stills][06 02:48–02:58]` Tail handling is actually: duplicate the music into two segments → mute the second → drag it behind the original clip → press `Option+G` (Mac) / `Alt+G` (Windows) to wrap it as an audio compound clip → choose `回音` (Echo) under “声音效果” → trim a second time to keep only the tail. Without the compound-clip step, clicking Echo directly on the truncated audio “does not work”.
- `[sampled stills][06 04:24]` The start of `海浪声` (Wave sounds) is about 2–3 seconds ahead of the next video segment's in-point and has a fade-in; this is the example's lead time for a J-cut, not a fixed value.
- `[sampled stills][06 06:15 / 07:06]` The sound-effects library list shows `RISE_TRANSITION_FX_*`, `Noise Riser`, `大鼓重击` (heavy bass drum hit), `电影级低音音效素材` (cinematic low-frequency sound effects), `转场低音` (transition bass), `boom, 低音波` (boom, low-frequency wave), and others; the list is a search result from the example, not a recommendation list or proof of licensing.
- `[sampled stills][06 07:06]` The burned-in subtitle clearly reads “this is called sub in English, or **Drone**”; the `drum` in the SRT is a misrecognition.
- `[sampled stills][06 10:07–10:14]` The speed-change demo for the original sound effect reads `1.00x / 3.0s → 0.58x / 5.1s → 0.19x / 15.6s → 0.26x / 11.4s（声音变调开）→ 0.71x / 4.4s` (`声音变调开` = pitch shift on); the parameters are decided by listening, not a fixed chain. The screen has no separate “音调” (pitch) numeric slider.
- `[sampled stills][04 12:42–12:54]` Three channel-configuration options: `无` (None), `将左侧声道填充至右侧声道` (fill the right channel from the left channel), `将右侧声道填充至左侧声道` (fill the left channel from the right channel); before repairing, first confirm which side is missing.
- `[sampled stills][06 08:30–08:52]` The resource table is readable word for word: `https://www.musicbed.com/`, `https://artlist.io/`, `https://www.storyblocks.com/`, `https://elements.envato.com/audio`; the local asset library is organized in two levels, “音效/BGM” (sound effects/BGM), with file names such as `人名条动效.wav`, `过场标题.wav`, `高能预警.wav`, `鼠标.wav`, `耳鸣.wav`. The Musicbed file names in the course materials only prove source attribution; they do not constitute permission to redistribute.

## Currently pending verification

The music closure and before/after comparison in lesson 06, the fade-out in lesson 04, and the sound bridge in lesson 16 have not yet been verified by listening to the original audio. Any plan given to the user must be marked “pending actual listening verification”. Frame sampling at 2-second intervals can confirm the waveform, tracks, and parameter names, but cannot confirm whether the tail sounds natural, whether the J-cut is smooth, or whether the channel repair is effective.
