import React from "react";
import { AbsoluteFill, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { evolvePath, getLength } from "@remotion/paths";

const wavePath =
  "M 100 540 Q 280 340, 460 540 Q 640 740, 820 540 Q 1000 340, 1180 540 Q 1360 740, 1540 540 Q 1720 340, 1820 540";

export const PathsDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const drawProgress = spring({
    frame,
    fps,
    config: { damping: 20, stiffness: 40 },
  });

  const pathLength = getLength(wavePath);
  const { strokeDasharray, strokeDashoffset } = evolvePath(drawProgress, wavePath);

  // Animated dot following the path
  const dotProgress = spring({
    frame: Math.max(0, frame - 15),
    fps,
    config: { damping: 20, stiffness: 40 },
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#0a0a1a" }}>
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <div
          style={{
            fontSize: 56,
            fontWeight: 800,
            color: "#ffffff",
            fontFamily: "Inter",
            marginTop: -200,
          }}
        >
          @remotion/paths
        </div>
      </AbsoluteFill>

      <svg width={1920} height={1080} viewBox="0 0 1920 1080">
        {/* Glow layer */}
        <path
          d={wavePath}
          fill="none"
          stroke="#fa6bfa44"
          strokeWidth={12}
          strokeDasharray={strokeDasharray}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
          filter="blur(8px)"
        />
        {/* Main path */}
        <path
          d={wavePath}
          fill="none"
          stroke="#fa6bfa"
          strokeWidth={5}
          strokeDasharray={strokeDasharray}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
        />
      </svg>

      <div
        style={{
          position: "absolute",
          bottom: 100,
          width: "100%",
          textAlign: "center",
          color: "#aaaaaa",
          fontSize: 28,
          fontFamily: "Inter",
          opacity: drawProgress,
        }}
      >
        SVG path drawing + evolution
      </div>
    </AbsoluteFill>
  );
};
