import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {SceneHeader} from '../components/SceneHeader';
import {COLORS, FONT, MONO} from '../theme';

const STEPS = [
  {
    index: '01',
    title: 'Render',
    body: 'npx remotion render\nH.264 MP4 · 1920×1080 · 30 fps',
    color: COLORS.violet,
  },
  {
    index: '02',
    title: 'Review',
    body: 'Watch at normal speed. Listen. Check captions, safe areas, and cut points.',
    color: COLORS.cyan,
  },
  {
    index: '03',
    title: 'Deliver',
    body: 'Cover, naming, archive, and the current platform rules. Rendering is not acceptance.',
    color: COLORS.warm,
  },
];

export const DeliveryScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const progress = interpolate(frame, [20, 100], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{fontFamily: FONT}}>
      <Background variant="cyan" />
      <SceneHeader
        kicker="DELIVERY / FINAL GATE"
        title="Render, review, then deliver."
        subtitle="A successful render is evidence of structure, not of platform acceptance. The final check still happens in the player and in your ears."
        accent={COLORS.green}
      />

      <div
        style={{
          position: 'absolute',
          left: 120,
          right: 120,
          top: 306,
          display: 'flex',
          gap: 30,
        }}
      >
        {STEPS.map((step, index) => {
          const enter = spring({
            frame: Math.max(0, frame - 12 - index * 6),
            fps,
            config: {damping: 200},
            durationInFrames: 26,
          });
          return (
            <div
              key={step.title}
              style={{
                flex: 1,
                minHeight: 250,
                padding: '24px 26px',
                borderRadius: 18,
                background: 'rgba(11,14,28,0.82)',
                border: '1px solid rgba(255,255,255,0.14)',
                boxShadow: '0 24px 60px rgba(0,0,0,0.28)',
                opacity: enter,
                translate: `0 ${(1 - enter) * 18}px`,
              }}
            >
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  marginBottom: 22,
                }}
              >
                <span
                  style={{
                    fontFamily: MONO,
                    fontSize: 13,
                    letterSpacing: 1.8,
                    color: step.color,
                    fontWeight: 700,
                  }}
                >
                  {step.index}
                </span>
                <span
                  style={{
                    width: 40,
                    height: 4,
                    borderRadius: 2,
                    background: step.color,
                  }}
                />
              </div>
              <div
                style={{
                  fontSize: 36,
                  fontWeight: 800,
                  color: COLORS.text,
                  letterSpacing: -0.5,
                }}
              >
                {step.title}
              </div>
              <div
                style={{
                  marginTop: 16,
                  fontFamily: MONO,
                  fontSize: 14,
                  lineHeight: 1.55,
                  color: COLORS.muted,
                  whiteSpace: 'pre-line',
                }}
              >
                {step.body}
              </div>
            </div>
          );
        })}
      </div>

      <div
        style={{
          position: 'absolute',
          left: 120,
          right: 120,
          bottom: 170,
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            fontFamily: MONO,
            fontSize: 12,
            letterSpacing: 1.6,
            color: COLORS.muted,
            marginBottom: 12,
          }}
        >
          <span>RENDER PROGRESS</span>
          <span>{Math.round(progress * 100)}%</span>
        </div>
        <div
          style={{
            height: 10,
            borderRadius: 5,
            background: 'rgba(255,255,255,0.08)',
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              width: `${progress * 100}%`,
              height: '100%',
              background: `linear-gradient(90deg, ${COLORS.violet}, ${COLORS.cyan})`,
              borderRadius: 5,
            }}
          />
        </div>
      </div>

      <div
        style={{
          position: 'absolute',
          left: 120,
          right: 120,
          bottom: 82,
          display: 'flex',
          justifyContent: 'space-between',
          fontFamily: MONO,
          fontSize: 12,
          letterSpacing: 1.3,
          color: COLORS.muted,
        }}
      >
        <span>SYNTHETIC DEMO · NO COURSE FOOTAGE</span>
        <span>1920×1080 · 30 FPS · H.264 · MP4</span>
      </div>
    </AbsoluteFill>
  );
};
