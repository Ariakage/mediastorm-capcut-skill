import React from 'react';
import {
  AbsoluteFill,
  Easing,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {Background} from '../components/Background';
import {COLORS, FONT, MONO} from '../theme';

const STATS = [
  ['18', 'lessons'],
  ['6,656', 'sampled stills'],
  ['10', 'editorial skills'],
  ['1', 'router'],
];

const STRIP = [
  {label: 'A-ROLL', color: COLORS.violet, width: 180},
  {label: 'B-ROLL', color: COLORS.cyan, width: 230},
  {label: 'TITLE', color: COLORS.warm, width: 150},
  {label: 'SOUND', color: COLORS.green, width: 200},
  {label: 'GRADE', color: COLORS.red, width: 170},
];

export const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const titleIn = spring({frame, fps, config: {damping: 200}, durationInFrames: 42});
  const subIn = interpolate(frame, [10, 36], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const playhead = interpolate(frame, [0, 96], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{fontFamily: FONT}}>
      <Background variant="violet" />

      <div style={{position: 'absolute', left: 120, top: 104}}>
        <div
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: 10,
            padding: '9px 16px',
            borderRadius: 20,
            border: '1px solid rgba(255,255,255,0.16)',
            background: 'rgba(255,255,255,0.05)',
            color: '#cfd2ff',
            fontFamily: MONO,
            fontSize: 15,
            letterSpacing: 2.4,
            fontWeight: 700,
          }}
        >
          <span
            style={{
              width: 8,
              height: 8,
              borderRadius: 4,
              background: COLORS.violet,
              display: 'inline-block',
            }}
          />
          MEDIASTORM · PERSONAL STUDY
        </div>
      </div>

      <div
        style={{
          position: 'absolute',
          left: 120,
          top: 250,
          width: 980,
          opacity: titleIn,
          translate: `0 ${(1 - titleIn) * 28}px`,
          scale: 0.96 + titleIn * 0.04,
        }}
      >
        <div
          style={{
            fontSize: 94,
            lineHeight: 0.98,
            fontWeight: 800,
            letterSpacing: -1.5,
            color: COLORS.text,
          }}
        >
          Cut with
          <br />
          judgment.
        </div>
        <div
          style={{
            marginTop: 24,
            fontSize: 30,
            lineHeight: 1.35,
            color: COLORS.muted,
            maxWidth: 860,
            opacity: subIn,
            translate: `0 ${(1 - subIn) * 14}px`,
          }}
        >
          A CapCut × Remotion editorial atlas. Ten skills, one router, and a
          boundary between evidence and taste.
        </div>
      </div>

      <div
        style={{
          position: 'absolute',
          left: 120,
          bottom: 150,
          display: 'flex',
          gap: 58,
          opacity: subIn,
        }}
      >
        {STATS.map(([value, label]) => (
          <div key={label}>
            <div
              style={{
                fontSize: 42,
                fontWeight: 800,
                color: COLORS.text,
                letterSpacing: -0.5,
              }}
            >
              {value}
            </div>
            <div
              style={{
                marginTop: 4,
                fontFamily: MONO,
                fontSize: 13,
                color: COLORS.muted,
                letterSpacing: 1.4,
                textTransform: 'uppercase',
              }}
            >
              {label}
            </div>
          </div>
        ))}
      </div>

      <div
        style={{
          position: 'absolute',
          right: 120,
          top: 250,
          width: 700,
          padding: 28,
          borderRadius: 22,
          background: 'rgba(11,14,28,0.78)',
          border: '1px solid rgba(255,255,255,0.14)',
          boxShadow: '0 30px 80px rgba(0,0,0,0.35)',
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            fontFamily: MONO,
            fontSize: 13,
            color: COLORS.muted,
            letterSpacing: 1.4,
            marginBottom: 18,
          }}
        >
          <span>EDIT BAY / 01</span>
          <span>00:00:24:00</span>
        </div>

        <div
          style={{
            position: 'relative',
            display: 'flex',
            gap: 10,
            alignItems: 'center',
            height: 112,
          }}
        >
          {STRIP.map((clip, index) => {
            const appear = spring({
              frame: Math.max(0, frame - 14 - index * 5),
              fps,
              config: {damping: 200},
              durationInFrames: 24,
            });
            return (
              <div
                key={clip.label}
                style={{
                  width: clip.width * 0.64,
                  height: 64 + index * 8,
                  borderRadius: 8,
                  background: `linear-gradient(135deg, ${clip.color}, ${clip.color}99)`,
                  opacity: appear,
                  scale: 0.85 + appear * 0.15,
                  display: 'flex',
                  alignItems: 'flex-end',
                  justifyContent: 'center',
                  paddingBottom: 8,
                  color: 'rgba(255,255,255,0.8)',
                  fontFamily: MONO,
                  fontSize: 10,
                  fontWeight: 700,
                  letterSpacing: 1,
                }}
              >
                {clip.label}
              </div>
            );
          })}

          <div
            style={{
              position: 'absolute',
              top: -10,
              bottom: -10,
              left: `${playhead * 100}%`,
              width: 2,
              background: 'rgba(255,255,255,0.85)',
            }}
          >
            <div
              style={{
                position: 'absolute',
                top: -7,
                left: -5,
                width: 12,
                height: 12,
                background: COLORS.text,
                borderRadius: 2,
              }}
            />
          </div>
        </div>

        <div
          style={{
            marginTop: 20,
            display: 'flex',
            justifyContent: 'space-between',
            fontFamily: MONO,
            fontSize: 12,
            color: COLORS.muted,
            letterSpacing: 1.2,
          }}
        >
          <span>V1 / A1 / T1</span>
          <span>FRAME-GRID READY</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};
