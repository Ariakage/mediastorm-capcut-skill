import {Composition} from 'remotion';
import {SkillAtlas} from './SkillAtlas';

export const Root = () => (
  <Composition
    id="SkillAtlas"
    component={SkillAtlas}
    durationInFrames={720}
    fps={30}
    width={1920}
    height={1080}
  />
);
