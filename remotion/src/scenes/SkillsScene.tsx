import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {SceneHeader} from '../components/SceneHeader';
import {COLORS, FONT, MONO} from '../theme';

const SKILLS = [
  {name: 'Project Prep', task: 'Media, codecs, relink, proxies', color: COLORS.violet},
  {name: 'Story Structure', task: 'Promise, order, density, rhythm', color: COLORS.magenta},
  {name: 'Dialogue & Interview', task: 'Takes, breaths, captions, multicam', color: COLORS.cyan},
  {name: 'Music & Sound', task: 'Cuts, tails, J/L-cuts, effects', color: COLORS.green},
  {name: 'Speed & Time', task: 'Slow motion, ramps, frame supply', color: COLORS.warm},
  {name: 'Motion Graphics', task: 'Keyframes, easing, labels, timers', color: COLORS.violet},
  {name: 'Compositing', task: 'Keying, masks, layers, tracking', color: COLORS.cyan},
  {name: 'Color Grading', task: 'Log, LUT, curves, scopes, match', color: COLORS.red},
  {name: 'Generative B-roll', task: 'Prompt, cost, review, disclose', color: COLORS.warm},
  {name: 'Delivery', task: 'Cover, export, archive, handoff', color: COLORS.green},
];

export const SkillsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <AbsoluteFill style={{fontFamily: FONT}}>
      <Background variant="cyan" />
      <SceneHeader
        kicker="THE SKILL MAP"
        title="Ten skills, one editorial router."
        subtitle="Each skill owns a decision boundary. Compose them in the order the material needs, not the order the buttons appear."
        accent={COLORS.cyan}
      />

      <div
        style={{
          position: 'absolute',
          left: 137,
          top: 306,
          display: 'grid',
          gridTemplateColumns: 'repeat(5, 310px)',
          gap: 24,
        }}
      >
        {SKILLS.map((skill, index) => {
          const enter = spring({
            frame: Math.max(0, frame - 12 - index * 3),
            fps,
            config: {damping: 200},
            durationInFrames: 26,
          });
          return (
            <div
              key={skill.name}
              style={{
                height: 158,
                padding: '18px 20px',
                borderRadius: 16,
                background: 'rgba(11,14,28,0.78)',
                border: '1px solid rgba(255,255,255,0.12)',
                boxShadow: '0 18px 40px rgba(0,0,0,0.22)',
                opacity: enter,
                translate: `0 ${(1 - enter) * 18}px`,
                scale: 0.96 + enter * 0.04,
              }}
            >
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  marginBottom: 14,
                }}
              >
                <span
                  style={{
                    fontFamily: MONO,
                    fontSize: 12,
                    color: skill.color,
                    letterSpacing: 1.6,
                    fontWeight: 700,
                  }}
                >
                  {String(index + 1).padStart(2, '0')}
                </span>
                <span
                  style={{
                    width: 34,
                    height: 4,
                    borderRadius: 2,
                    background: skill.color,
                  }}
                />
              </div>
              <div
                style={{
                  fontSize: 24,
                  fontWeight: 800,
                  color: COLORS.text,
                  lineHeight: 1.1,
                  letterSpacing: -0.3,
                }}
              >
                {skill.name}
              </div>
              <div
                style={{
                  marginTop: 10,
                  fontSize: 15,
                  lineHeight: 1.35,
                  color: COLORS.muted,
                }}
              >
                {skill.task}
              </div>
            </div>
          );
        })}
      </div>

      <div
        style={{
          position: 'absolute',
          left: 137,
          right: 137,
          bottom: 96,
          display: 'flex',
          alignItems: 'center',
          gap: 16,
          opacity: interpolate(frame, [70, 95], [0, 1], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          }),
        }}
      >
        <span
          style={{
            fontFamily: MONO,
            fontSize: 12,
            letterSpacing: 1.5,
            color: COLORS.muted,
            whiteSpace: 'nowrap',
          }}
        >
          ROUTE
        </span>
        <div style={{height: 1, flex: 1, background: 'rgba(255,255,255,0.14)'}} />
        <span
          style={{
            fontFamily: MONO,
            fontSize: 12,
            letterSpacing: 1.2,
            color: COLORS.muted,
            whiteSpace: 'nowrap',
          }}
        >
          PREP → STORY → DIALOGUE → SOUND → SPEED → MOTION → COMPOSITE → COLOR → GEN → DELIVER
        </span>
      </div>
    </AbsoluteFill>
  );
};
