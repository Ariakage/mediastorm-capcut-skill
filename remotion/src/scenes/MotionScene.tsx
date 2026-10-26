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
import {SceneHeader} from '../components/SceneHeader';
import {COLORS, FONT, MONO} from '../theme';

const bezierPoint = (t: number) => {
  // Cubic Bezier from (40, 260) to (600, 60), with control points
  // (180, 260) and (220, 60), matching the drawn curve.
  const p0 = {x: 40, y: 260};
  const p1 = {x: 180, y: 260};
  const p2 = {x: 220, y: 60};
  const p3 = {x: 600, y: 60};
  const u = 1 - t;
  return {
    x: u * u * u * p0.x + 3 * u * u * t * p1.x + 3 * u * t * t * p2.x + t * t * t * p3.x,
    y: u * u * u * p0.y + 3 * u * u * t * p1.y + 3 * u * t * t * p2.y + t * t * t * p3.y,
  };
};

export const MotionScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 200}, durationInFrames: 36});
  const t = interpolate(frame, [10, 100], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const point = bezierPoint(t);
  const value = Math.round(t * 100);

  return (
    <AbsoluteFill style={{fontFamily: FONT}}>
      <Background variant="violet" />
      <SceneHeader
        kicker="MOTION / FRAME GRID"
        title="Animate the idea, then align the parameters."
        subtitle="Keyframes are local to the segment. Scale and position should share a rhythm; the frame grid decides when a number is readable."
        accent={COLORS.violet}
      />

      <div
        style={{
          position: 'absolute',
          left: 120,
          top: 306,
          width: 900,
          height: 500,
          borderRadius: 20,
          background: 'rgba(11,14,28,0.8)',
          border: '1px solid rgba(255,255,255,0.14)',
          overflow: 'hidden',
          boxShadow: '0 30px 80px rgba(0,0,0,0.3)',
          opacity: enter,
        }}
      >
        <div
          style={{
            position: 'absolute',
            left: 40,
            top: 32,
            fontFamily: MONO,
            fontSize: 12,
            letterSpacing: 1.5,
            color: COLORS.muted,
          }}
        >
          SCALE + POSITION / ONE CLOCK
        </div>

        <div
          style={{
            position: 'absolute',
            left: 40,
            right: 40,
            top: 96,
            height: 250,
            borderRadius: 16,
            background:
              'linear-gradient(135deg, rgba(124,92,255,0.18), rgba(42,210,255,0.08))',
            border: '1px solid rgba(255,255,255,0.1)',
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              position: 'absolute',
              left: 80 + t * 470,
              top: 60 + t * 40,
              width: 160,
              height: 110,
              borderRadius: 18,
              background: 'linear-gradient(135deg, #7c5cff, #2ad2ff)',
              scale: 0.65 + t * 0.55,
              boxShadow: '0 18px 50px rgba(42,210,255,0.3)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: COLORS.text,
              fontFamily: MONO,
              fontSize: 13,
              letterSpacing: 1.2,
              fontWeight: 700,
            }}
          >
            FRAME {String(Math.round(t * 90)).padStart(2, '0')}
          </div>

          <div
            style={{
              position: 'absolute',
              right: 26,
              top: 22,
              fontSize: 86,
              fontWeight: 800,
              color: COLORS.text,
              fontFamily: MONO,
              letterSpacing: -3,
            }}
          >
            {String(value).padStart(3, '0')}
          </div>
        </div>

        <div
          style={{
            position: 'absolute',
            left: 40,
            right: 40,
            bottom: 54,
            height: 50,
          }}
        >
          <div
            style={{
              position: 'absolute',
              left: 0,
              right: 0,
              top: 24,
              height: 1,
              background: 'rgba(255,255,255,0.15)',
            }}
          />
          {[0, 1, 2, 3].map((i) => (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: `${i * 33}%`,
                top: 18,
                width: 13,
                height: 13,
                background: COLORS.text,
                rotate: '45deg',
                boxShadow: '0 0 12px rgba(255,255,255,0.4)',
              }}
            />
          ))}
          <div
            style={{
              position: 'absolute',
              left: `calc(${t * 100}% - 2px)`,
              top: 17,
              width: 4,
              height: 15,
              background: COLORS.warm,
              borderRadius: 2,
            }}
          />
        </div>

        <div
          style={{
            position: 'absolute',
            left: 40,
            bottom: 22,
            fontFamily: MONO,
            fontSize: 11,
            letterSpacing: 1.3,
            color: COLORS.muted,
          }}
        >
          KEYFRAME A → KEYFRAME B · EASE IN-OUT
        </div>
      </div>

      <div
        style={{
          position: 'absolute',
          left: 1080,
          top: 306,
          width: 720,
          height: 500,
          borderRadius: 20,
          background: 'rgba(11,14,28,0.8)',
          border: '1px solid rgba(255,255,255,0.14)',
          boxShadow: '0 30px 80px rgba(0,0,0,0.3)',
          opacity: enter,
        }}
      >
        <div
          style={{
            position: 'absolute',
            left: 34,
            top: 30,
            fontFamily: MONO,
            fontSize: 12,
            letterSpacing: 1.5,
            color: COLORS.muted,
          }}
        >
          EASING / BEZIER(0.16, 1, 0.3, 1)
        </div>

        <svg
          width="720"
          height="500"
          viewBox="0 0 720 500"
          style={{position: 'absolute', inset: 0}}
        >
          {[0, 1, 2, 3, 4].map((i) => (
            <line
              key={`h${i}`}
              x1="40"
              x2="680"
              y1={80 + i * 70}
              y2={80 + i * 70}
              stroke="rgba(255,255,255,0.08)"
              strokeWidth="1"
            />
          ))}
          {[0, 1, 2, 3, 4].map((i) => (
            <line
              key={`v${i}`}
              x1={40 + i * 160}
              x2={40 + i * 160}
              y1="80"
              y2="420"
              stroke="rgba(255,255,255,0.08)"
              strokeWidth="1"
            />
          ))}
          <path
            d="M 40 420 C 180 420 220 220 600 220"
            fill="none"
            stroke="rgba(255,255,255,0.18)"
            strokeWidth="2"
            strokeDasharray="6 8"
          />
          <path
            d="M 40 420 C 180 420 220 220 600 220"
            fill="none"
            stroke={COLORS.cyan}
            strokeWidth="4"
            strokeLinecap="round"
            strokeDasharray="1000"
            strokeDashoffset={1000 - t * 1000}
          />
          <circle
            cx={point.x}
            cy={point.y - 160}
            r="13"
            fill={COLORS.warm}
            stroke={COLORS.bg}
            strokeWidth="4"
          />
          <text
            x="40"
            y="462"
            fill={COLORS.muted}
            fontFamily={MONO}
            fontSize="12"
            letterSpacing="1"
          >
            INPUT / FRAME
          </text>
          <text
            x="600"
            y="462"
            fill={COLORS.muted}
            fontFamily={MONO}
            fontSize="12"
            letterSpacing="1"
          >
            OUTPUT / VALUE
          </text>
        </svg>
      </div>
    </AbsoluteFill>
  );
};
