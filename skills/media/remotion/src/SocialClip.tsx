import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  Video,
} from "remotion";
import { z } from "zod";

export const socialClipSchema = z.object({
  bgVideoSrc: z.string().optional(),
  bgImageSrc: z.string().optional(),
  bgColor: z.string().default("#000000"),
  overlayText: z.string().default(""),
  overlayPosition: z.enum(["top", "center", "bottom"]).default("center"),
  fontSize: z.number().default(64),
  textColor: z.string().default("#ffffff"),
  textShadow: z.boolean().default(true),
  fontFamily: z.string().default("Inter"),
  fontWeight: z.enum(["400", "600", "700", "800", "900"]).default("800"),
});

type SocialClipProps = z.infer<typeof socialClipSchema>;

export const SocialClip: React.FC<SocialClipProps> = ({
  bgVideoSrc,
  bgImageSrc,
  bgColor,
  overlayText,
  overlayPosition,
  fontSize,
  textColor,
  textShadow,
  fontFamily,
  fontWeight,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const textScale = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120 },
  });
  const fadeOut = interpolate(
    frame,
    [durationInFrames - 10, durationInFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const justifyContent =
    overlayPosition === "top"
      ? "flex-start"
      : overlayPosition === "bottom"
        ? "flex-end"
        : "center";

  const positionPadding: React.CSSProperties =
    overlayPosition === "top"
      ? { paddingTop: "15%" }
      : overlayPosition === "bottom"
        ? { paddingBottom: "15%" }
        : {};

  return (
    <AbsoluteFill style={{ backgroundColor: bgColor }}>
      {bgVideoSrc && (
        <AbsoluteFill>
          <Video
            src={staticFile(bgVideoSrc)}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </AbsoluteFill>
      )}
      {bgImageSrc && !bgVideoSrc && (
        <AbsoluteFill>
          <Img
            src={staticFile(bgImageSrc)}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </AbsoluteFill>
      )}

      {(bgVideoSrc || bgImageSrc) && (
        <AbsoluteFill style={{ backgroundColor: "rgba(0,0,0,0.4)" }} />
      )}

      {overlayText && (
        <AbsoluteFill
          style={{
            justifyContent,
            alignItems: "center",
            opacity: fadeOut,
            ...positionPadding,
          }}
        >
          <div
            style={{
              transform: `scale(${textScale})`,
              fontSize,
              color: textColor,
              fontFamily,
              fontWeight: Number(fontWeight),
              textAlign: "center",
              padding: "0 60px",
              lineHeight: 1.2,
              textShadow: textShadow
                ? "0 2px 20px rgba(0,0,0,0.8), 0 1px 4px rgba(0,0,0,0.6)"
                : "none",
              maxWidth: "90%",
            }}
          >
            {overlayText}
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};
