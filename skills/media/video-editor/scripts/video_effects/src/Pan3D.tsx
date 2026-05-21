import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

export type Pan3DProps = {
  frameCount: number;
  playbackRate: number;
};

export const Pan3D: React.FC<Pan3DProps> = ({ frameCount }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Map current render frame to the extracted frame index (1-based for file naming)
  const frameIndex = Math.min(
    Math.floor((frame / durationInFrames) * frameCount) + 1,
    frameCount
  );
  const paddedIndex = String(frameIndex).padStart(4, "0");
  const frameSrc = staticFile(`frames/frame_${paddedIndex}.jpg`);
  const bgSrc = staticFile("frames/bg_image.png");

  // Normalized progress 0..1
  const progress = frame / durationInFrames;

  // 3D rotation: swivel in from left, hold center, swivel out to right
  // Phase 1 (0-20%): rotate in from -60deg to 0deg
  // Phase 2 (20-80%): hold at 0deg with subtle drift
  // Phase 3 (80-100%): rotate out from 0deg to 60deg
  const rotateY = interpolate(
    progress,
    [0, 0.15, 0.85, 1],
    [-55, 0, 0, 55],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Scale: start slightly smaller, expand to full, shrink on exit
  const scale = interpolate(
    progress,
    [0, 0.15, 0.85, 1],
    [0.7, 0.88, 0.88, 0.7],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Opacity: fade in and out at edges
  const opacity = interpolate(
    progress,
    [0, 0.08, 0.92, 1],
    [0, 1, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Subtle vertical float
  const translateY = interpolate(
    progress,
    [0, 0.5, 1],
    [15, -5, 15],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Shadow intensity based on rotation
  const shadowOffset = Math.abs(rotateY) * 0.4;
  const shadowBlur = 20 + Math.abs(rotateY) * 0.5;
  const shadowOpacity = 0.3 + Math.abs(rotateY) * 0.005;

  return (
    <AbsoluteFill>
      {/* Background image */}
      <AbsoluteFill>
        <Img
          src={bgSrc}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </AbsoluteFill>

      {/* 3D perspective container */}
      <AbsoluteFill
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          perspective: 1200,
        }}
      >
        <div
          style={{
            transform: `rotateY(${rotateY}deg) scale(${scale}) translateY(${translateY}px)`,
            transformStyle: "preserve-3d",
            opacity,
            borderRadius: 12,
            overflow: "hidden",
            boxShadow: `${shadowOffset}px 8px ${shadowBlur}px rgba(0,0,0,${shadowOpacity})`,
          }}
        >
          <Img
            src={frameSrc}
            style={{
              width: "100%",
              height: "auto",
              display: "block",
            }}
          />
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
