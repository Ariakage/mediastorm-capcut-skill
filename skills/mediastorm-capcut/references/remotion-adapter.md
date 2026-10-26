# Remotion / TypeScript 适配

本参考把 10 个子 Skill 的剪辑判断映射到 Remotion 官方 API。它是**实现建议**，不是已渲染验收；课程画面证据仍以 CapCut 路径为准。

## 先决条件

- Node.js、Git；新建工程用 `npx create-video@latest`，已有工程直接安装所需包。
- 用 `npx remotion add <package>` 安装，版本由当前 Remotion 解析；不要手工拼不兼容版本。
- Studio 用 `npx remotion studio` 打开；渲染是另一个明确动作：`npx remotion render`。

```bash
npx create-video@latest --yes --blank --no-tailwind mediastorm-remotion
cd mediastorm-remotion
npm i
npx remotion add @remotion/media
npx remotion add @remotion/transitions
npx remotion add @remotion/captions
npx remotion add @remotion/effects
npx remotion add @remotion/layout-utils
npx remotion add @remotion/motion-blur
npx remotion add @remotion/shapes
npx remotion studio
```

## 子 Skill 映射

| 子 Skill | 建议包 / API | 不能直接映射的部分 |
| --- | --- | --- |
| `mediastorm-project-prep` | `mediabunny`、`calculateMetadata`、`staticFile()`、`zod`、`@remotion/zod-types` | 剪映的媒体重链接、缓存/代理 UI；需自建 manifest 与错误处理 |
| `mediastorm-story-structure` | `Sequence`、`Series`、`@remotion/transitions` 的 `TransitionSeries`、`@remotion/layout-utils` | 自动踩点、剪映的磁吸/主轨 UI |
| `mediastorm-dialogue-interview` | `@remotion/captions` 的 `Caption`、`@remotion/media`、`@remotion/whisper-webgpu`、`@huggingface/transformers` | 剪映智能剪口播的逐字稿面板、多机位 4/9 宫格 |
| `mediastorm-music-sound` | `@remotion/media` 的 `<Audio>`、`@remotion/media-utils`、`mediabunny` | 剪映“回音/大厅混响”预设、复合片段容器 |
| `mediastorm-speed-time` | `<Video playbackRate>`、`trimBefore`、`durationInFrames`、`@remotion/motion-blur`、`mediabunny` | 剪映速度曲线编辑器、内置光流补帧 |
| `mediastorm-motion-graphics` | `interpolate`、`Easing`、`spring`、`@remotion/shapes`、`@remotion/layout-utils`、`@remotion/motion-blur`、`@remotion/rough-notation` | 剪映的跟踪面板、数字闪变/计时器预设 |
| `mediastorm-compositing-tracking` | `@remotion/effects` 的 `colorKey`/`cornerPin`/`mirror`/`blur`、CSS `mask`/`clip-path`、`@remotion/three` | 剪映平面跟踪求解器、智能抠像的发丝像素结果 |
| `mediastorm-color-grading` | `colorCorrection()`、`lut()`、`@remotion/effects` 的 `glow`/`lightLeak`/`vignette` | 剪映色轮/示波器 UI、Log 自动识别 |
| `mediastorm-generative-broll` | 外部生成 API + `staticFile()`、`@remotion/player`、`zod` | 剪映内置模型、积分/价格/可用性 |
| `mediastorm-delivery-handoff` | `@remotion/cli`、`@remotion/renderer`、`@remotion/lambda`、`@remotion/player`、`mediabunny` | 平台二审、会员素材、剪映云空间 |

## 代码骨架

### 组合与时间线

```tsx
import {Composition, Sequence, staticFile, useVideoConfig} from 'remotion';
import {Video} from '@remotion/media';
import {TransitionSeries} from '@remotion/transitions';

const Shot = ({src, trimBefore, durationInFrames}: {
  src: string; trimBefore: number; durationInFrames: number;
}) => {
  const {fps} = useVideoConfig();
  return (
    <Video
      src={staticFile(src)}
      trimBefore={trimBefore * fps}
      durationInFrames={durationInFrames * fps}
    />
  );
};

export const Main = () => (
  <TransitionSeries>
    <TransitionSeries.Sequence durationInFrames={90} name="Opening">
      <Shot src="a-roll.mp4" trimBefore={3} durationInFrames={3} />
    </TransitionSeries.Sequence>
    <TransitionSeries.Sequence durationInFrames={120} name="B-roll">
      <Shot src="b-roll.mp4" trimBefore={12} durationInFrames={4} />
    </TransitionSeries.Sequence>
  </TransitionSeries>
);

export const Root = () => (
  <Composition
    id="Main"
    component={Main}
    durationInFrames={210}
    fps={30}
    width={1920}
    height={1080}
  />
);
```

### 字幕

```tsx
import type {Caption} from '@remotion/captions';

const captions: Caption[] = [
  {text: '第一句', startMs: 0, endMs: 1200, timestampMs: 600, confidence: null},
];
```

字幕时间相对原素材；把 `trimBefore` 放在承载视频和字幕的同一个 `Sequence` 上，避免两层时钟错位。

### 调色

```tsx
import {Video} from '@remotion/media';
import {colorCorrection, lut} from '@remotion/effects/color-correction';
import {staticFile} from 'remotion';

<Video
  src={staticFile('footage.mp4')}
  effects={[
    colorCorrection({exposure: 0.2, temperature: 0.1, shadows: 0.15, highlights: -0.1, contrast: 1.1}),
    // lut({content: cubeText})
  ]}
/>
```

### 动效

```tsx
import {Easing, interpolate, useCurrentFrame} from 'remotion';

const frame = useCurrentFrame();
const scale = interpolate(frame, [0, 30], [1, 1.2], {
  easing: Easing.bezier(0.16, 1, 0.3, 1),
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
  output: 'perceptual-scale',
});
```

### 色度抠图

```tsx
import {Video} from '@remotion/media';
import {colorKey} from '@remotion/effects/color-key';

<Video src={staticFile('green-screen.mp4')} effects={[colorKey({color: '#00ff00', similarity: 0.4})]} />
```

实际参数名以当前 `@remotion/effects` 文档为准；课程中的 `强度/阴影/羽化/清除` 不是 Remotion 的同名参数。

## 边界

- Remotion 没有剪映的平面跟踪求解器。需要先在 Mocha/AE 等工具得到四角数据，再用 `cornerPin` 或自定义 `transform` 关键帧。
- Remotion 没有内置波形/矢量示波器。需要外部工具或自建 Canvas/WebGL 分析。
- Remotion 没有剪映智能抠像、智能剪口播、多机位宫格、回音预设的等价 UI；这些只能近似或走外部处理。
- 课程参数是案例值；Remotion 代码里的数值必须按当前素材、画布和输出目标重算。
- 无论 CapCut 还是 Remotion，渲染成功都不等于平台验收；仍需实际播放、听辨和目标平台复核。
