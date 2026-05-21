import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { z } from "zod";

const dataPointSchema = z.object({
  label: z.string(),
  value: z.number(),
  color: z.string().optional(),
});

export const dataVizSchema = z.object({
  data: z.array(dataPointSchema).default([
    { label: "Mon", value: 65 },
    { label: "Tue", value: 78 },
    { label: "Wed", value: 52 },
    { label: "Thu", value: 91 },
    { label: "Fri", value: 85 },
  ]),
  chartType: z.enum(["bar", "horizontalBar"]).default("bar"),
  title: z.string().default(""),
  bgColor: z.string().default("#1a1a2e"),
  barColor: z.string().default("#e94560"),
  textColor: z.string().default("#ffffff"),
  fontFamily: z.string().default("Inter"),
  showValues: z.boolean().default(true),
  animationDelay: z.number().default(3),
});

type DataVizProps = z.infer<typeof dataVizSchema>;

export const DataViz: React.FC<DataVizProps> = ({
  data,
  chartType,
  title,
  bgColor,
  barColor,
  textColor,
  fontFamily,
  showValues,
  animationDelay,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const maxValue = Math.max(...data.map((d) => d.value));

  const fadeOut = interpolate(
    frame,
    [durationInFrames - 15, durationInFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const titleOpacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  if (chartType === "horizontalBar") {
    return (
      <AbsoluteFill
        style={{
          backgroundColor: bgColor,
          padding: "80px 100px",
          flexDirection: "column",
          justifyContent: "center",
          opacity: fadeOut,
        }}
      >
        {title && (
          <div
            style={{
              fontSize: 48,
              fontWeight: 700,
              color: textColor,
              fontFamily,
              marginBottom: 50,
              opacity: titleOpacity,
            }}
          >
            {title}
          </div>
        )}
        {data.map((item, i) => {
          const delay = i * animationDelay;
          const barProgress = spring({
            frame: frame - delay - 10,
            fps,
            config: { damping: 15, stiffness: 80 },
          });
          const barWidth = (item.value / maxValue) * 100 * barProgress;
          const labelOpacity = interpolate(
            frame,
            [delay + 5, delay + 15],
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
          );

          return (
            <div
              key={item.label}
              style={{
                display: "flex",
                alignItems: "center",
                marginBottom: 24,
                opacity: labelOpacity,
              }}
            >
              <div
                style={{
                  width: 120,
                  fontSize: 22,
                  color: textColor,
                  fontFamily,
                  fontWeight: 600,
                  textAlign: "right",
                  marginRight: 20,
                  opacity: 0.8,
                }}
              >
                {item.label}
              </div>
              <div
                style={{
                  flex: 1,
                  height: 40,
                  backgroundColor: "rgba(255,255,255,0.1)",
                  borderRadius: 6,
                  overflow: "hidden",
                  position: "relative",
                }}
              >
                <div
                  style={{
                    width: `${barWidth}%`,
                    height: "100%",
                    backgroundColor: item.color || barColor,
                    borderRadius: 6,
                  }}
                />
                {showValues && barProgress > 0.5 && (
                  <div
                    style={{
                      position: "absolute",
                      right: 12,
                      top: "50%",
                      transform: "translateY(-50%)",
                      fontSize: 18,
                      fontWeight: 700,
                      color: textColor,
                      fontFamily,
                    }}
                  >
                    {item.value}
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill
      style={{
        backgroundColor: bgColor,
        padding: "80px 100px",
        flexDirection: "column",
        justifyContent: "center",
        opacity: fadeOut,
      }}
    >
      {title && (
        <div
          style={{
            fontSize: 48,
            fontWeight: 700,
            color: textColor,
            fontFamily,
            marginBottom: 50,
            textAlign: "center",
            opacity: titleOpacity,
          }}
        >
          {title}
        </div>
      )}
      <div
        style={{
          display: "flex",
          alignItems: "flex-end",
          justifyContent: "center",
          gap: 30,
          height: 500,
        }}
      >
        {data.map((item, i) => {
          const delay = i * animationDelay;
          const barHeight = spring({
            frame: frame - delay - 10,
            fps,
            config: { damping: 15, stiffness: 80 },
          });
          const height = (item.value / maxValue) * 400 * barHeight;
          const labelOpacity = interpolate(
            frame,
            [delay + 5, delay + 15],
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
          );

          return (
            <div
              key={item.label}
              style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: labelOpacity,
              }}
            >
              {showValues && barHeight > 0.5 && (
                <div
                  style={{
                    fontSize: 22,
                    fontWeight: 700,
                    color: textColor,
                    fontFamily,
                    marginBottom: 8,
                  }}
                >
                  {item.value}
                </div>
              )}
              <div
                style={{
                  width: 60,
                  height,
                  backgroundColor: item.color || barColor,
                  borderRadius: "6px 6px 0 0",
                }}
              />
              <div
                style={{
                  fontSize: 18,
                  color: textColor,
                  fontFamily,
                  fontWeight: 600,
                  marginTop: 12,
                  opacity: 0.8,
                }}
              >
                {item.label}
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
