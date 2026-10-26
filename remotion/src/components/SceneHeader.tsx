import React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';
import {COLORS, FONT, MONO} from '../theme';

type Props = {
  kicker: string;
  title: string;
  subtitle?: string;
  accent?: string;
};

export const SceneHeader: React.FC<Props> = ({
  kicker,
  title,
  subtitle,
  accent = COLORS.violet,
}) => {
  const frame = useCurrentFrame();
  const enter = interpolate(frame, [0, 18], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'absolute',
        left: 120,
        top: 82,
        right: 120,
        opacity: enter,
        translate: `0 ${(1 - enter) * 18}px`,
        fontFamily: FONT,
      }}
    >
      <div
        style={{
          fontFamily: MONO,
          fontSize: 18,
          letterSpacing: 3,
          color: accent,
          fontWeight: 700,
          marginBottom: 14,
        }}
      >
        {kicker}
      </div>
      <div
        style={{
          fontSize: 58,
          lineHeight: 1.05,
          fontWeight: 800,
          color: COLORS.text,
          letterSpacing: 0.5,
          maxWidth: 1500,
        }}
      >
        {title}
      </div>
      {subtitle ? (
        <div
          style={{
            marginTop: 16,
            fontSize: 24,
            lineHeight: 1.35,
            color: COLORS.muted,
            maxWidth: 1300,
          }}
        >
          {subtitle}
        </div>
      ) : null}
    </div>
  );
};
