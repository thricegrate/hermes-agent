import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { z } from "zod";

export const promoClipSchema = z.object({
  bgColor: z.string().default("#111111"),
  accentColor: z.string().default("#fa6bfa"),
  textColor: z.string().default("#ffffff"),
  mutedColor: z.string().default("#aaaaaa"),
  fontFamily: z.string().default("Inter"),
  starRating: z.string().default("4.9"),
  headline: z.string().default("You are about to get our 5,000+ best ChatGPT prompts"),
  bullets: z.array(z.string()).default([
    "Our 5,000+ ChatGPT prompts right now",
    "500+ AI side hustles you can start this week",
    "Cyber Corsairs: AI Productivity Newsletter (215,000+ subscribers)",
  ]),
  ctaText: z.string().default("Join Free Now"),
  footerText: z.string().default("100% Free | Unsubscribe anytime"),
});

type PromoClipProps = z.infer<typeof promoClipSchema>;

const AnimatedElement: React.FC<{
  children: React.ReactNode;
  delay: number;
  style?: React.CSSProperties;
}> = ({ children, delay, style }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const progress = spring({
    frame: Math.max(0, frame - delay),
    fps,
    config: { damping: 14, stiffness: 100 },
  });

  const opacity = interpolate(progress, [0, 1], [0, 1]);
  const translateY = interpolate(progress, [0, 1], [40, 0]);

  return (
    <div
      style={{
        opacity,
        transform: `translateY(${translateY}px)`,
        ...style,
      }}
    >
      {children}
    </div>
  );
};

export const PromoClip: React.FC<PromoClipProps> = ({
  bgColor,
  accentColor,
  textColor,
  mutedColor,
  fontFamily,
  starRating,
  headline,
  bullets,
  ctaText,
  footerText,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const fadeOut = interpolate(
    frame,
    [durationInFrames - 15, durationInFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Glow pulse on CTA
  const ctaDelay = 20 + bullets.length * 12;
  const ctaFrame = Math.max(0, frame - ctaDelay);
  const glowPulse = Math.sin(ctaFrame * 0.08) * 0.3 + 0.7;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: bgColor,
        fontFamily,
        opacity: fadeOut,
      }}
    >
      {/* Subtle gradient overlay */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at 50% 30%, ${accentColor}15 0%, transparent 70%)`,
        }}
      />

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          height: "100%",
          padding: "80px 60px",
          gap: 0,
        }}
      >
        {/* Star rating */}
        <AnimatedElement delay={5}>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 12,
              marginBottom: 40,
            }}
          >
            <span style={{ fontSize: 48, letterSpacing: 4 }}>
              {"★".repeat(5)}
            </span>
            <span
              style={{
                fontSize: 52,
                color: textColor,
                fontWeight: 700,
              }}
            >
              {starRating}
            </span>
          </div>
        </AnimatedElement>

        {/* Headline */}
        <AnimatedElement delay={12} style={{ marginBottom: 50 }}>
          <div
            style={{
              fontSize: 52,
              fontWeight: 800,
              color: textColor,
              textAlign: "center",
              lineHeight: 1.25,
              maxWidth: 900,
            }}
          >
            {headline}
          </div>
        </AnimatedElement>

        {/* Subtext */}
        <AnimatedElement delay={18} style={{ marginBottom: 40 }}>
          <div
            style={{
              fontSize: 32,
              color: mutedColor,
              textAlign: "center",
            }}
          >
            Put your email below & you'll get:
          </div>
        </AnimatedElement>

        {/* Bullet points */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 24,
            marginBottom: 50,
            width: "100%",
            maxWidth: 850,
          }}
        >
          {bullets.map((bullet, i) => (
            <AnimatedElement key={i} delay={24 + i * 12}>
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 16,
                  fontSize: 36,
                  color: textColor,
                  fontWeight: 600,
                }}
              >
                <span style={{ color: accentColor, fontSize: 32 }}>✓</span>
                <span>{bullet}</span>
                {i === 2 && (
                  <span style={{ fontSize: 32, marginLeft: -4 }}>👈</span>
                )}
              </div>
            </AnimatedElement>
          ))}
        </div>

        {/* CTA Button */}
        <AnimatedElement delay={ctaDelay}>
          <div
            style={{
              backgroundColor: accentColor,
              color: "#000000",
              fontSize: 42,
              fontWeight: 800,
              padding: "22px 64px",
              borderRadius: 16,
              textAlign: "center",
              boxShadow: `0 0 ${30 * glowPulse}px ${accentColor}88, 0 4px 20px rgba(0,0,0,0.4)`,
              marginBottom: 24,
            }}
          >
            {ctaText}
          </div>
        </AnimatedElement>

        {/* Footer */}
        <AnimatedElement delay={ctaDelay + 8}>
          <div
            style={{
              fontSize: 24,
              color: mutedColor,
              textAlign: "center",
            }}
          >
            {footerText}
          </div>
        </AnimatedElement>
      </div>
    </AbsoluteFill>
  );
};
