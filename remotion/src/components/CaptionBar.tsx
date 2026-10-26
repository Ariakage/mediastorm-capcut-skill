import type {Caption} from '@remotion/captions';
import React from 'react';
import {COLORS, FONT} from '../theme';

export const CaptionBar: React.FC<{caption: Caption | null}> = ({caption}) => {
  if (!caption) return null;
  return (
    <div
      style={{
        position: 'absolute',
        left: '50%',
        bottom: 72,
        translate: '-50% 0',
        maxWidth: 1280,
        padding: '14px 26px',
        borderRadius: 12,
        background: 'rgba(8,10,20,0.78)',
        border: '1px solid rgba(255,255,255,0.14)',
        color: COLORS.text,
        fontFamily: FONT,
        fontSize: 34,
        fontWeight: 700,
        textAlign: 'center',
        boxShadow: '0 18px 50px rgba(0,0,0,0.35)',
      }}
    >
      {caption.text}
    </div>
  );
};
