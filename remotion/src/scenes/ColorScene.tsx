import {Video} from '@remotion/media';
import {colorCorrection} from '@remotion/effects/color-correction';
import React from 'react';
import {AbsoluteFill, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {Background} from '../components/Background';
import {SceneHeader} from '../components/SceneHeader';
import {COLORS, FONT, MONO} from '../theme';

const CHIPS = [
  ['#ffb347', 'HIGHLIGHT'],
  ['#ff5f7e', 'SKIN'],
  ['#7c5cff', 'SHADOW'],
  ['#2ad2ff', 'COOL'],
  ['#4ee1a0', 'NEUTRAL'],
];

export const ColorScene: React.FC = () => {
  const frame = useCurrentFrame();
  const reveal = interpolate(frame, [8, 30], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{fontFamily: FONT}}>
      <Background variant="warm" />
      <SceneHeader
        kicker="COLOR / BEFORE AND AFTER"
        title="Correct the input before you create a look."
        subtitle="Identify the source, apply a matching technical transform, then judge exposure, balance, and contrast on a real frame."
        accent={COLORS.warm}
      />

      <div
        style={{
          position: 'absolute',
          left: 120,
          top: 306,
          width: 810,
          height: 500,
          borderRadius: 18,
          overflow: 'hidden',
          border: '1px solid rgba(255,255,255,0.14)',
          background: COLORS.panel,
          opacity: reveal,
          translate: `0 ${(1 - reveal) * 20}px`,
        }}
      >
        <Video
          src={staticFile('demo.mp4')}
          muted
          trimBefore={30}
          durationInFrames={126}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            filter: 'saturate(0.35) contrast(0.72) brightness(0.92)',
          }}
        />
        <Label text="LOG / FLAT" color={COLORS.muted} />
      </div>

      <div
        style={{
          position: 'absolute',
          left: 990,
          top: 306,
          width: 810,
          height: 500,
          borderRadius: 18,
          overflow: 'hidden',
          border: '1px solid rgba(255,255,255,0.2)',
          background: COLORS.panel,
          opacity: reveal,
          translate: `0 ${(1 - reveal) * 20}px`,
        }}
      >
        <Video
          src={staticFile('demo.mp4')}
          muted
          trimBefore={30}
          durationInFrames={126}
          effects={[
            colorCorrection({
              exposure: 0.3,
              temperature: 0.15,
              tint: -0.05,
              shadows: 0.12,
              highlights: -0.08,
              contrast: 1.18,
              saturation: 1.25,
              vibrance: 0.2,
            }),
          ]}
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
        />
        <Label text="GRADED" color={COLORS.warm} />
      </div>

      <div
        style={{
          position: 'absolute',
          left: 120,
          right: 120,
          top: 850,
          display: 'flex',
          alignItems: 'center',
          gap: 18,
        }}
      >
        <span
          style={{
            fontFamily: MONO,
            fontSize: 12,
            letterSpacing: 1.6,
            color: COLORS.muted,
          }}
        >
          SAME FRAME / DIFFERENT TECHNICAL STATE
        </span>
        <div style={{height: 1, flex: 1, background: 'rgba(255,255,255,0.12)'}} />
        {CHIPS.map(([color, label]) => (
          <div
            key={label}
            style={{display: 'flex', alignItems: 'center', gap: 8}}
          >
            <span
              style={{
                width: 16,
                height: 16,
                borderRadius: 4,
                background: color,
                display: 'inline-block',
              }}
            />
            <span
              style={{
                fontFamily: MONO,
                fontSize: 10,
                letterSpacing: 1,
                color: COLORS.muted,
              }}
            >
              {label}
            </span>
          </div>
        ))}
      </div>

      <div
        style={{
          position: 'absolute',
          left: 120,
          bottom: 78,
          fontFamily: MONO,
          fontSize: 12,
          letterSpacing: 1.3,
          color: COLORS.muted,
          opacity: interpolate(frame, [50, 80], [0, 1], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          }),
        }}
      >
        colorCorrection() → one WebGL pass · lut() → a .cube transform · scopes are external
      </div>
    </AbsoluteFill>
  );
};

const Label: React.FC<{text: string; color: string}> = ({text, color}) => (
  <div
    style={{
      position: 'absolute',
      left: 18,
      top: 18,
      padding: '7px 12px',
      borderRadius: 8,
      background: 'rgba(8,10,20,0.7)',
      border: '1px solid rgba(255,255,255,0.14)',
      fontFamily: MONO,
      fontSize: 12,
      letterSpacing: 1.4,
      color,
      fontWeight: 700,
    }}
  >
    {text}
  </div>
);
