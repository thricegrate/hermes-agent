import React, { useEffect, useState } from "react";
import { AbsoluteFill, continueRender, delayRender, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { Lottie, getLottieMetadata } from "@remotion/lottie";
import type { AnimationItem } from "lottie-web";

// Simple inline Lottie animation (pulsing circle)
const simpleLottieData = {
  v: "5.7.1",
  fr: 30,
  ip: 0,
  op: 60,
  w: 400,
  h: 400,
  assets: [],
  layers: [
    {
      ty: 4,
      nm: "Circle",
      sr: 1,
      ks: {
        o: { a: 0, k: 100 },
        r: { a: 0, k: 0 },
        p: { a: 0, k: [200, 200, 0] },
        a: { a: 0, k: [0, 0, 0] },
        s: {
          a: 1,
          k: [
            { t: 0, s: [80, 80, 100], i: { x: [0.5], y: [1] }, o: { x: [0.5], y: [0] } },
            { t: 30, s: [120, 120, 100], i: { x: [0.5], y: [1] }, o: { x: [0.5], y: [0] } },
            { t: 60, s: [80, 80, 100] },
          ],
        },
      },
      shapes: [
        {
          ty: "el",
          d: 1,
          s: { a: 0, k: [200, 200] },
          p: { a: 0, k: [0, 0] },
        },
        {
          ty: "fl",
          c: { a: 0, k: [0.98, 0.42, 0.98, 1] },
          o: { a: 0, k: 100 },
          r: 1,
        },
      ],
      ip: 0,
      op: 60,
      st: 0,
    },
  ],
};

export const LottieDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({
    frame,
    fps,
    config: { damping: 12, stiffness: 100 },
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#111111" }}>
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <div
          style={{
            fontSize: 56,
            fontWeight: 800,
            color: "#ffffff",
            fontFamily: "Inter",
            marginTop: -350,
          }}
        >
          @remotion/lottie
        </div>
      </AbsoluteFill>

      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <div style={{ transform: `scale(${scale * 1.5})` }}>
          <Lottie animationData={simpleLottieData} />
        </div>
      </AbsoluteFill>

      <div
        style={{
          position: "absolute",
          bottom: 100,
          width: "100%",
          textAlign: "center",
          color: "#aaaaaa",
          fontSize: 28,
          fontFamily: "Inter",
          opacity: scale,
        }}
      >
        Lottie animation synced to video frames
      </div>
    </AbsoluteFill>
  );
};
