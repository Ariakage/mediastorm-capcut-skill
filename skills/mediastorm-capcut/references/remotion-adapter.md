# Remotion / TypeScript adapter

This reference maps the editing judgments of the 10 child skills to official Remotion APIs. It is an **implementation suggestion**, not a rendered acceptance; course picture evidence still follows the CapCut path.

## Prerequisites

- Node.js and Git; for a new project, use `npx create-video@latest`; for an existing project, install the required packages directly.
- Install with `npx remotion add <package>`; the version is resolved by the current Remotion; do not hand-assemble incompatible versions.
- Open Studio with `npx remotion studio`; rendering is a separate, explicit action: `npx remotion render`.

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

## Child skill mapping

| Child skill | Suggested packages / APIs | What cannot be mapped directly |
| --- | --- | --- |
| `mediastorm-project-prep` | `mediabunny`, `calculateMetadata`, `staticFile()`, `zod`, `@remotion/zod-types` | CapCut's media relinking and cache/proxy UI; you must build your own manifest and error handling |
| `mediastorm-story-structure` | `Sequence`, `Series`, `TransitionSeries` from `@remotion/transitions`, `@remotion/layout-utils` | Automatic beat detection and CapCut's magnetic/main-track UI |
| `mediastorm-dialogue-interview` | `Caption` from `@remotion/captions`, `@remotion/media`, `@remotion/whisper-webgpu`, `@huggingface/transformers` | CapCut's word-level transcript panel for smart talking-head cutting, and the multicam 4/9 grid |
| `mediastorm-music-sound` | `<Audio>` from `@remotion/media`, `@remotion/media-utils`, `mediabunny` | CapCut's `回音/大厅混响` (Echo/Hall Reverb) presets and compound-clip container |
| `mediastorm-speed-time` | `<Video playbackRate>`, `trimBefore`, `durationInFrames`, `@remotion/motion-blur`, `mediabunny` | CapCut's speed-curve editor and built-in optical-flow frame interpolation |
| `mediastorm-motion-graphics` | `interpolate`, `Easing`, `spring`, `@remotion/shapes`, `@remotion/layout-utils`, `@remotion/motion-blur`, `@remotion/rough-notation` | CapCut's tracking panel and number-flicker/timer presets |
| `mediastorm-compositing-tracking` | `colorKey`/`cornerPin`/`mirror`/`blur` from `@remotion/effects`, CSS `mask`/`clip-path`, `@remotion/three` | CapCut's planar-tracking solver and the hair-pixel result of smart keying |
| `mediastorm-color-grading` | `colorCorrection()`, `lut()`, `glow`/`lightLeak`/`vignette` from `@remotion/effects` | CapCut's color-wheel/scopes UI and automatic Log detection |
| `mediastorm-generative-broll` | External generation APIs + `staticFile()`, `@remotion/player`, `zod` | CapCut's built-in models, credits/pricing/availability |
| `mediastorm-delivery-handoff` | `@remotion/cli`, `@remotion/renderer`, `@remotion/lambda`, `@remotion/player`, `mediabunny` | Platform second review, membership assets, CapCut cloud space |

## Code skeleton

### Composition and timeline

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

### Captions

```tsx
import type {Caption} from '@remotion/captions';

const captions: Caption[] = [
  {text: '第一句', startMs: 0, endMs: 1200, timestampMs: 600, confidence: null},
];
```

Caption times are relative to the source asset; put `trimBefore` on the same `Sequence` that carries both the video and the captions, to avoid a two-layer clock mismatch.

### Color grading

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

### Motion

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

### Chroma keying

```tsx
import {Video} from '@remotion/media';
import {colorKey} from '@remotion/effects/color-key';

<Video src={staticFile('green-screen.mp4')} effects={[colorKey({color: '#00ff00', similarity: 0.4})]} />
```

Actual parameter names follow the current `@remotion/effects` documentation; the course's `强度/阴影/羽化/清除` labels (Strength/Shadow/Feather/Clear) are not parameters with the same names in Remotion.

## Boundaries

- Remotion has no CapCut planar-tracking solver. Obtain four-corner data in a tool such as Mocha/AE first, then use `cornerPin` or custom `transform` keyframes.
- Remotion has no built-in waveform/vectorscope. Use an external tool or build your own Canvas/WebGL analysis.
- Remotion has no equivalent UI for CapCut smart keying, smart talking-head cutting, multicam grids, or echo presets; these can only be approximated or handled externally.
- Course parameters are case values; numbers in Remotion code must be recomputed for the current assets, canvas, and output target.
- Whether CapCut or Remotion, a successful render does not equal platform acceptance; you still need actual playback, listening, and review on the target platform.
