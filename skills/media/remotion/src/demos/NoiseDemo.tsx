import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { noise2D } from "@remotion/noise";

export const NoiseDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();

  const cols = 20;
  const rows = 12;
  const cellW = width / cols;
  const cellH = height / rows;

  const cells: React.ReactNode[] = [];

  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      const n = noise2D("cyber", x * 0.3 + frame * 0.02, y * 0.3 + frame * 0.015);
      const hue = interpolate(n, [-1, 1], [280, 340]); // magenta range
      const lightness = interpolate(n, [-1, 1], [15, 55]);
      const scale = interpolate(n, [-1, 1], [0.6, 1.1]);

      cells.push(
        <div
          key={`${x}-${y}`}
          style={{
            position: "absolute",
            left: x * cellW,
            top: y * cellH,
            width: cellW,
            height: cellH,
            backgroundColor: `hsl(${hue}, 80%, ${lightness}%)`,
            transform: `scale(${scale})`,
            borderRadius: 8,
          }}
        />
      );
    }
  }

  return (
    <AbsoluteFill style={{ backgroundColor: "#0a0a0a" }}>
      {cells}
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <div
          style={{
            fontSize: 72,
            fontWeight: 800,
            color: "#ffffff",
            fontFamily: "Inter",
            textShadow: "0 0 40px rgba(250,107,250,0.8), 0 2px 10px rgba(0,0,0,0.8)",
            letterSpacing: 4,
          }}
        >
          PERLIN NOISE
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
