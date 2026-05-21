import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { z } from "zod";

export const introOutroSchema = z.object({
  logoSrc: z.string().default("logo.png"),
  title: z.string().default("My Newsletter"),
  subtitle: z.string().default("AI Newsletter Automation"),
  bgColor: z.string().default("#0a0a1a"),
  accentColor: z.string().default("#e94560"),
  textColor: z.string().default("#ffffff"),
  style: z.enum(["minimal", "bold", "animated"]).default("bold"),
  showCta: z.boolean().default(false),
  ctaText: z.string().default("Subscribe Now"),
});

type IntroOutroProps = z.infer<typeof introOutroSchema>;

export const IntroOutro: React.FC<IntroOutroProps> = ({
  logoSrc,
  title,
  subtitle,
  bgColor,
  accentColor,
  textColor,
  style,
  showCta,
  ctaText,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const logoScale = spring({ frame, fps, config: { damping: 12 } });
  const titleOpacity = interpolate(frame, [15, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const titleY = interpolate(frame, [15, 30], [30, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const subtitleOpacity = interpolate(frame, [25, 40], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fadeOut = interpolate(
    frame,
    [durationInFrames - 15, durationInFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );
  const lineWidth = interpolate(frame, [20, 45], [0, 200], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: bgColor,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        opacity: fadeOut,
      }}
    >
      <div style={{ transform: `scale(${logoScale})`, marginBottom: 30 }}>
        <Img
          src={staticFile(logoSrc)}
          style={{
            width: style === "bold" ? 160 : 120,
            height: style === "bold" ? 160 : 120,
            objectFit: "contain",
          }}
        />
      </div>

      <div
        style={{
          width: lineWidth,
          height: 3,
          backgroundColor: accentColor,
          marginBottom: 30,
        }}
      />

      <div
        style={{
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
          fontSize: style === "bold" ? 72 : 56,
          fontWeight: 800,
          color: textColor,
          fontFamily: "Inter, sans-serif",
          letterSpacing: style === "bold" ? -2 : 0,
        }}
      >
        {title}
      </div>

      <div
        style={{
          opacity: subtitleOpacity * 0.6,
          fontSize: style === "bold" ? 28 : 24,
          color: textColor,
          fontFamily: "Inter, sans-serif",
          fontWeight: 400,
          marginTop: 12,
        }}
      >
        {subtitle}
      </div>

      {showCta && (
        <Sequence from={40}>
          <AbsoluteFill
            style={{
              justifyContent: "flex-end",
              alignItems: "center",
              paddingBottom: 80,
            }}
          >
            <div
              style={{
                padding: "16px 48px",
                backgroundColor: accentColor,
                color: textColor,
                fontSize: 24,
                fontWeight: 700,
                borderRadius: 8,
                fontFamily: "Inter, sans-serif",
                transform: `scale(${spring({ frame: frame - 40, fps, config: { damping: 10 } })})`,
              }}
            >
              {ctaText}
            </div>
          </AbsoluteFill>
        </Sequence>
      )}
    </AbsoluteFill>
  );
};
