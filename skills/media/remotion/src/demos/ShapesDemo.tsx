import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { makeCircle, makeRect, makeStar, makeTriangle } from "@remotion/shapes";

export const ShapesDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const shapes = [
    { fn: () => makeCircle({ radius: 80 }), color: "#fa6bfa", label: "Circle", x: 300 },
    { fn: () => makeRect({ width: 160, height: 160 }), color: "#0ea5e9", label: "Rect", x: 600 },
    { fn: () => makeTriangle({ length: 180, direction: "up" }), color: "#22c55e", label: "Triangle", x: 900 },
    { fn: () => makeStar({ points: 5, innerRadius: 50, outerRadius: 100 }), color: "#f59e0b", label: "Star", x: 1200 },
  ];

  return (
    <AbsoluteFill style={{ backgroundColor: "#111111" }}>
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <div
          style={{
            fontSize: 56,
            fontWeight: 800,
            color: "#ffffff",
            fontFamily: "Inter",
            marginBottom: 80,
            marginTop: -120,
            textAlign: "center",
          }}
        >
          @remotion/shapes
        </div>
      </AbsoluteFill>

      {shapes.map((shape, i) => {
        const delay = i * 8;
        const progress = spring({
          frame: Math.max(0, frame - delay),
          fps,
          config: { damping: 12, stiffness: 100 },
        });
        const rotation = interpolate(frame, [0, 120], [0, 360]);
        const { path, width, height } = shape.fn();

        return (
          <div
            key={shape.label}
            style={{
              position: "absolute",
              left: shape.x - 80,
              top: 400,
              transform: `scale(${progress}) rotate(${rotation}deg)`,
              opacity: progress,
            }}
          >
            <svg width={width} height={height} viewBox={`0 0 ${width} ${height}`}>
              <path d={path} fill={shape.color} />
            </svg>
            <div
              style={{
                textAlign: "center",
                color: "#ffffff",
                fontSize: 24,
                fontFamily: "Inter",
                fontWeight: 600,
                marginTop: 16,
                opacity: progress,
              }}
            >
              {shape.label}
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
