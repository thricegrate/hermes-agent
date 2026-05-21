import React from "react";
import {
  AbsoluteFill,
  spring,
  useCurrentFrame,
  useVideoConfig,
  Video,
  staticFile,
} from "remotion";
import { z } from "zod";

const captionWordSchema = z.object({
  word: z.string(),
  startFrame: z.number(),
  endFrame: z.number(),
});

export const captionedVideoSchema = z.object({
  videoSrc: z.string(),
  captions: z.array(captionWordSchema).default([]),
  captionColor: z.string().default("#ffffff"),
  activeColor: z.string().default("#FFD700"),
  captionFontSize: z.number().default(56),
  captionPosition: z.enum(["top", "center", "bottom"]).default("bottom"),
  fontFamily: z.string().default("Inter"),
  wordsPerGroup: z.number().default(4),
  showBackground: z.boolean().default(true),
  bgColor: z.string().default("rgba(0,0,0,0.7)"),
});

type CaptionedVideoProps = z.infer<typeof captionedVideoSchema>;

export const CaptionedVideo: React.FC<CaptionedVideoProps> = ({
  videoSrc,
  captions,
  captionColor,
  activeColor,
  captionFontSize,
  captionPosition,
  fontFamily,
  wordsPerGroup,
  showBackground,
  bgColor,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const groups: (typeof captions)[] = [];
  for (let i = 0; i < captions.length; i += wordsPerGroup) {
    groups.push(captions.slice(i, i + wordsPerGroup));
  }

  const currentGroup = groups.find((group) => {
    const start = group[0]?.startFrame ?? 0;
    const end = group[group.length - 1]?.endFrame ?? 0;
    return frame >= start && frame <= end;
  });

  const positionStyle: React.CSSProperties =
    captionPosition === "top"
      ? { top: "10%", bottom: "auto" }
      : captionPosition === "center"
        ? { top: "50%", transform: "translateY(-50%)" }
        : { bottom: "10%", top: "auto" };

  return (
    <AbsoluteFill>
      <Video
        src={staticFile(videoSrc)}
        style={{ width: "100%", height: "100%", objectFit: "cover" }}
      />

      {currentGroup && (
        <div
          style={{
            position: "absolute",
            left: 0,
            right: 0,
            display: "flex",
            justifyContent: "center",
            ...positionStyle,
          }}
        >
          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              justifyContent: "center",
              gap: "8px 12px",
              padding: showBackground ? "16px 32px" : "0",
              backgroundColor: showBackground ? bgColor : "transparent",
              borderRadius: showBackground ? 12 : 0,
              maxWidth: "80%",
            }}
          >
            {currentGroup.map((word, i) => {
              const isActive =
                frame >= word.startFrame && frame <= word.endFrame;
              const wordScale = isActive
                ? spring({
                    frame: frame - word.startFrame,
                    fps,
                    config: { damping: 15, stiffness: 200 },
                  })
                : 1;

              return (
                <span
                  key={`${word.word}-${i}`}
                  style={{
                    fontSize: captionFontSize,
                    fontFamily,
                    fontWeight: 800,
                    color: isActive ? activeColor : captionColor,
                    transform: `scale(${isActive ? 1 + wordScale * 0.1 : 1})`,
                    textShadow: "0 2px 8px rgba(0,0,0,0.6)",
                  }}
                >
                  {word.word}
                </span>
              );
            })}
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};
