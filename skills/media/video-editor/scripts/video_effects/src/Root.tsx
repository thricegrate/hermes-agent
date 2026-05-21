import React from "react";
import { Composition } from "remotion";
import { Pan3D } from "./Pan3D";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Pan3D"
      component={Pan3D}
      durationInFrames={300}
      fps={60}
      width={1920}
      height={1080}
      defaultProps={{
        frameCount: 300,
        playbackRate: 12,
      }}
      calculateMetadata={async ({ props }) => {
        // Duration adapts to frameCount at 60fps
        // Default 5s teaser = 300 frames at 60fps
        return {
          durationInFrames: props.frameCount || 300,
        };
      }}
    />
  );
};
