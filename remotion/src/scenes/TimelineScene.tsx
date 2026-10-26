import type {Caption} from '@remotion/captions';
import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {CaptionBar} from '../components/CaptionBar';
import {SceneHeader} from '../components/SceneHeader';
import {COLORS, FONT, MONO} from '../theme';

const CLIPS = [
  {label: 'A-ROLL 01', width: 300, color: COLORS.violet},
  {label: 'B-ROLL 02', width: 350, color: COLORS.cyan},
  {label: 'TITLE', width: 220, color: COLORS.warm},
  {label: 'A-ROLL 03', width: 320, color: COLORS.violet},
  {label: 'B-ROLL 04', width: 300, color: COLORS.cyan},
];

const CAPTIONS: Caption[] = [
  {text: 'Cut on the information, not the waveform.', startMs: 0, endMs: 1800, timestampMs: 900, confidence: null},
  {text: 'Then let the sound bridge the cut.', startMs: 1800, endMs: 3600, timestampMs: 2700, confidence: null},
  {text: 'Check the frame grid before the render.', startMs: 3600, endMs: 5200, timestampMs: 4400, confidence: null},
];

let wavePath = '';
for (let i = 0; i < 250; i++) {
  const x = i * 6;
  const h = 4 + Math.abs(Math.sin(i * 1.73)) * 18;
  wavePath += `M${x} ${26 - h}h3v${h * 2}h-3z`;
}

export const TimelineScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const playhead = interpolate(frame, [0, 156], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const nowMs = (frame / fps) * 1000;
  const caption = CAPTIONS.find((c) => nowMs >= c.startMs && nowMs < c.endMs) ?? null;

  let cursor = 80;
  const positioned = CLIPS.map((clip) => {
    const item = {...clip, x: cursor};
    cursor += clip.width + 12;
    return item;
  });

  return (
    <AbsoluteFill style={{fontFamily: FONT}}>
      <Background variant="cyan" />
      <SceneHeader
        kicker="EDITORIAL TIMELINE"
        title="Clips, captions, keyframes, and a moving playhead."
        subtitle="A timeline is a set of decisions with time coordinates. The picture, the sound, and the words must share one clock."
        accent={COLORS.warm}
      />

      <div
        style={{
          position: 'absolute',
          left: 120,
          right: 120,
          top: 300,
          height: 520,
          borderRadius: 22,
          background: 'rgba(11,14,28,0.82)',
          border: '1px solid rgba(255,255,255,0.14)',
          boxShadow: '0 30px 80px rgba(0,0,0,0.35)',
          overflow: 'hidden',
        }}
      >
        <div
          style={{
            height: 46,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '0 24px',
            borderBottom: '1px solid rgba(255,255,255,0.1)',
            fontFamily: MONO,
            fontSize: 13,
            letterSpacing: 1.4,
            color: COLORS.muted,
          }}
        >
          <span>TIMELINE 01 · 30 FPS</span>
          <span>{`00:00:${String(Math.floor(frame / fps)).padStart(2, '0')}:${String(frame % fps).padStart(2, '0')}`}</span>
        </div>

        <div style={{position: 'relative', height: 474}}>
          <TrackLabel label="V1" y={82} />
          <TrackLabel label="A1" y={200} />
          <TrackLabel label="T1" y={318} />

          <div style={{position: 'absolute', left: 80, right: 40, top: 64, height: 70}}>
            {positioned.map((clip, index) => {
              const enter = spring({
                frame: Math.max(0, frame - 12 - index * 5),
                fps,
                config: {damping: 200},
                durationInFrames: 22,
              });
              return (
                <div
                  key={clip.label}
                  style={{
                    position: 'absolute',
                    left: clip.x,
                    top: 0,
                    width: clip.width,
                    height: 58,
                    borderRadius: 8,
                    background: `linear-gradient(135deg, ${clip.color}, ${clip.color}99)`,
                    opacity: enter,
                    scale: 0.92 + enter * 0.08,
                    transformOrigin: 'left center',
                    display: 'flex',
                    alignItems: 'flex-end',
                    padding: '0 12px 9px',
                    color: 'rgba(255,255,255,0.88)',
                    fontFamily: MONO,
                    fontSize: 11,
                    fontWeight: 700,
                    letterSpacing: 1,
                  }}
                >
                  {clip.label}
                </div>
              );
            })}

            {[420, 720, 1040].map((x, index) => (
              <div
                key={x}
                style={{
                  position: 'absolute',
                  left: x,
                  top: 24,
                  width: 12,
                  height: 12,
                  background: COLORS.text,
                  rotate: '45deg',
                  scale: 0.85 + Math.sin(frame * 0.12 + index) * 0.15,
                  boxShadow: '0 0 14px rgba(255,255,255,0.45)',
                }}
              />
            ))}
          </div>

          <div
            style={{
              position: 'absolute',
              left: 80,
              right: 40,
              top: 182,
              height: 58,
              borderRadius: 8,
              background: '#12304a',
              border: '1px solid rgba(42,210,255,0.28)',
              overflow: 'hidden',
            }}
          >
            <svg width="100%" height="58" viewBox="0 0 1500 52" preserveAspectRatio="none">
              <path d={wavePath} fill="rgba(42,210,255,0.5)" />
            </svg>
          </div>

          <div
            style={{
              position: 'absolute',
              left: 80,
              right: 40,
              top: 300,
              height: 58,
              display: 'flex',
              gap: 10,
            }}
          >
            {[0, 1, 2, 3, 4].map((i) => (
              <div
                key={i}
                style={{
                  flex: i === 4 ? 0.8 : 1,
                  borderRadius: 8,
                  background: 'rgba(58,42,94,0.75)',
                  border: '1px solid rgba(196,107,255,0.35)',
                  opacity: interpolate(frame, [40 + i * 6, 60 + i * 6], [0, 1], {
                    extrapolateLeft: 'clamp',
                    extrapolateRight: 'clamp',
                  }),
                }}
              />
            ))}
          </div>

          <div
            style={{
              position: 'absolute',
              left: 80 + playhead * 1420,
              top: 46,
              bottom: 40,
              width: 2,
              background: 'rgba(255,255,255,0.88)',
              boxShadow: '0 0 18px rgba(255,255,255,0.4)',
            }}
          >
            <div
              style={{
                position: 'absolute',
                top: -8,
                left: -6,
                width: 14,
                height: 14,
                borderRadius: 3,
                background: COLORS.text,
              }}
            />
          </div>
        </div>
      </div>

      <CaptionBar caption={caption} />
    </AbsoluteFill>
  );
};

const TrackLabel: React.FC<{label: string; y: number}> = ({label, y}) => (
  <div
    style={{
      position: 'absolute',
      left: 24,
      top: y,
      width: 42,
      fontFamily: MONO,
      fontSize: 12,
      letterSpacing: 1.2,
      color: COLORS.muted,
    }}
  >
    {label}
  </div>
);
