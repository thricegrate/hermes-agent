import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { CameraMotionBlur } from "@remotion/motion-blur";

const MovingBox: React.FC = () => {
  const frame = useCurrentFrame();
  const { width } = useVideoConfig();

  const x = interpolate(frame, [0, 90], [-200, width + 200]);
  const rotation = interpolate(frame, [0, 90], [0, 720]);

  return (
    <AbsoluteFill style={{ backgroundColor: "#0a0a1a" }}>
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <div
          style={{
            fontSize: 56,
            fontWeight: 800,
            color: "#ffffff",
            fontFamily: "Inter",
            marginTop: -300,
          }}
        >
          @remotion/motion-blur
        </div>
      </AbsoluteFill>

      <div
        style={{
          position: "absolute",
          left: x,
          top: 440,
          width: 120,
          height: 120,
          backgroundColor: "#fa6bfa",
          borderRadius: 16,
          transform: `rotate(${rotation}deg)`,
          boxShadow: "0 0 30px #fa6bfa88",
        }}
      />

      <div
        style={{
          position: "absolute",
          bottom: 100,
          width: "100%",
          textAlign: "center",
          color: "#aaaaaa",
          fontSize: 28,
          fontFamily: "Inter",
        }}
      >
        Camera motion blur on a moving + rotating element
      </div>
    </AbsoluteFill>
  );
};

export const MotionBlurDemo: React.FC = () => {
  return (
    <CameraMotionBlur samples={10} shutterAngle={180}>
      <MovingBox />
    </CameraMotionBlur>
  );
};
