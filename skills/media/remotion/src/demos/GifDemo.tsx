import React from "react";
import { AbsoluteFill, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { Gif } from "@remotion/gif";

export const GifDemo: React.FC = () => {
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
          @remotion/gif
        </div>
      </AbsoluteFill>

      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <div style={{ transform: `scale(${scale})` }}>
          <Gif
            src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"
            width={480}
            height={360}
            fit="contain"
            playbackRate={1}
          />
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
        Frame-synced GIF playback from URL
      </div>
    </AbsoluteFill>
  );
};
