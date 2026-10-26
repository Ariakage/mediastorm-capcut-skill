import {Audio} from '@remotion/media';
import {linearTiming, TransitionSeries} from '@remotion/transitions';
import {fade} from '@remotion/transitions/fade';
import React from 'react';
import {AbsoluteFill, staticFile} from 'remotion';
import {ColorScene} from './scenes/ColorScene';
import {DeliveryScene} from './scenes/DeliveryScene';
import {MotionScene} from './scenes/MotionScene';
import {SkillsScene} from './scenes/SkillsScene';
import {TimelineScene} from './scenes/TimelineScene';
import {TitleScene} from './scenes/TitleScene';
import {COLORS, FONT} from './theme';

const TRANSITION = 12;

export const SkillAtlas: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: COLORS.bg, fontFamily: FONT}}>
    <Audio src={staticFile('tone.mp3')} volume={0.12} />

    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={96}>
        <TitleScene />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition
        presentation={fade()}
        timing={linearTiming({durationInFrames: TRANSITION})}
      />

      <TransitionSeries.Sequence durationInFrames={156}>
        <SkillsScene />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition
        presentation={fade()}
        timing={linearTiming({durationInFrames: TRANSITION})}
      />

      <TransitionSeries.Sequence durationInFrames={156}>
        <TimelineScene />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition
        presentation={fade()}
        timing={linearTiming({durationInFrames: TRANSITION})}
      />

      <TransitionSeries.Sequence durationInFrames={126}>
        <ColorScene />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition
        presentation={fade()}
        timing={linearTiming({durationInFrames: TRANSITION})}
      />

      <TransitionSeries.Sequence durationInFrames={126}>
        <MotionScene />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition
        presentation={fade()}
        timing={linearTiming({durationInFrames: TRANSITION})}
      />

      <TransitionSeries.Sequence durationInFrames={120}>
        <DeliveryScene />
      </TransitionSeries.Sequence>
    </TransitionSeries>
  </AbsoluteFill>
);
