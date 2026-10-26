import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import {COLORS} from '../theme';

type Variant = 'violet' | 'cyan' | 'warm';

const accentFor = (variant: Variant) => {
  if (variant === 'cyan') return COLORS.cyan;
  if (variant === 'warm') return COLORS.warm;
  return COLORS.violet;
};

export const Background: React.FC<{variant?: Variant}> = ({variant = 'violet'}) => {
  const frame = useCurrentFrame();
  const accent = accentFor(variant);
  const drift = (frame * 0.04) % 20;

  return (
    <AbsoluteFill
      style={{
        background: [
          `radial-gradient(circle at ${18 + drift}% ${20 + drift * 0.6}%, ${accent}38, transparent 46%)`,
          `radial-gradient(circle at ${86 - drift}% ${78 - drift * 0.5}%, ${COLORS.cyan}22, transparent 52%)`,
          'linear-gradient(135deg, #080a14 0%, #10142a 55%, #1b0f2e 100%)',
        ].join(', '),
      }}
    >
      <AbsoluteFill
        style={{
          backgroundImage:
            'linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px)',
          backgroundSize: '48px 48px',
        }}
      />
    </AbsoluteFill>
  );
};
