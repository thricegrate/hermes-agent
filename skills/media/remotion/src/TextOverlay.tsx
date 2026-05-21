import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { z } from "zod";

export const textOverlaySchema = z.object({
  text: z.string().default("Hello World"),
  fontSize: z.number().default(80),
  textColor: z.string().default("#ffffff"),
  bgColor: z.string().default("#1a1a2e"),
  bgGradient: z.string().optional(),
  fontFamily: z.string().default("Inter"),
  fontWeight: z.enum(["400", "600", "700", "800", "900"]).default("700"),
  animation: z
    .enum(["fadeIn", "slideUp", "typewriter", "spring", "scaleIn"])
    .default("spring"),
  textAlign: z.enum(["left", "center", "right"]).default("center"),
  subtitle: z.string().optional(),
  subtitleFontSize: z.number().default(36),
});

type TextOverlayProps = z.infer<typeof textOverlaySchema>;

export const TextOverlay: React.FC<TextOverlayProps> = ({
  text,
  fontSize,
  textColor,
  bgColor,
  bgGradient,
  fontFamily,
  fontWeight,
  animation,
  textAlign,
  subtitle,
  subtitleFontSize,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const fadeOut = interpolate(
    frame,
    [durationInFrames - 10, durationInFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const getAnimationStyle = (): React.CSSProperties => {
    switch (animation) {
      case "fadeIn": {
        const opacity = interpolate(frame, [0, 20], [0, 1], {
          extrapolateRight: "clamp",
        });
        return { opacity: opacity * fadeOut };
      }
      case "slideUp": {
        const translateY = interpolate(frame, [0, 25], [60, 0], {
          extrapolateRight: "clamp",
        });
        const opacity = interpolate(frame, [0, 15], [0, 1], {
          extrapolateRight: "clamp",
        });
        return {
          transform: `translateY(${translateY}px)`,
          opacity: opacity * fadeOut,
        };
      }
      case "typewriter":
        return { opacity: fadeOut };
      case "spring": {
        const scale = spring({ frame, fps, config: { damping: 12, stiffness: 150 } });
        return { transform: `scale(${scale})`, opacity: fadeOut };
      }
      case "scaleIn": {
        const scale = interpolate(frame, [0, 20], [0.5, 1], {
          extrapolateRight: "clamp",
        });
        const opacity = interpolate(frame, [0, 15], [0, 1], {
          extrapolateRight: "clamp",
        });
        return { transform: `scale(${scale})`, opacity: opacity * fadeOut };
      }
      default:
        return { opacity: fadeOut };
    }
  };

  const displayText =
    animation === "typewriter" ? text.slice(0, Math.floor(frame / 2)) : text;

  const subtitleStyle = (): React.CSSProperties => {
    const delay = 10;
    const opacity = interpolate(frame, [delay, delay + 15], [0, 1], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
    return { opacity: opacity * fadeOut };
  };

  const background = bgGradient || bgColor;

  return (
    <AbsoluteFill
      style={{
        background,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems:
          textAlign === "center"
            ? "center"
            : textAlign === "right"
              ? "flex-end"
              : "flex-start",
        padding: "80px",
      }}
    >
      <div style={getAnimationStyle()}>
        <div
          style={{
            fontSize,
            color: textColor,
            fontFamily,
            fontWeight: Number(fontWeight),
            textAlign,
            lineHeight: 1.2,
            maxWidth: "90%",
          }}
        >
          {displayText}
        </div>
      </div>
      {subtitle && (
        <div style={subtitleStyle()}>
          <div
            style={{
              fontSize: subtitleFontSize,
              color: textColor,
              fontFamily,
              fontWeight: 400,
              textAlign,
              opacity: 0.7,
              marginTop: 20,
              maxWidth: "80%",
            }}
          >
            {subtitle}
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};
