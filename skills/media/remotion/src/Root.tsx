import React from "react";
import { Composition, Folder } from "remotion";
import { Transition3D } from "./Transition3D";
import { TextOverlay, textOverlaySchema } from "./TextOverlay";
import { IntroOutro, introOutroSchema } from "./IntroOutro";
import { SocialClip, socialClipSchema } from "./SocialClip";
import { CaptionedVideo, captionedVideoSchema } from "./CaptionedVideo";
import { DataViz, dataVizSchema } from "./DataViz";
import { PromoClip, promoClipSchema } from "./PromoClip";
import { NoiseDemo } from "./demos/NoiseDemo";
import { ShapesDemo } from "./demos/ShapesDemo";
import { PathsDemo } from "./demos/PathsDemo";
import { MotionBlurDemo } from "./demos/MotionBlurDemo";
import { GifDemo } from "./demos/GifDemo";
import { ThreeDemo } from "./demos/ThreeDemo";
import { LottieDemo } from "./demos/LottieDemo";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Folder name="Templates">
        <Composition
          id="TextOverlay"
          component={TextOverlay}
          schema={textOverlaySchema}
          durationInFrames={90}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            text: "My Newsletter",
            subtitle: "AI Newsletter Automation",
            fontSize: 80,
            textColor: "#ffffff",
            bgColor: "#1a1a2e",
            fontFamily: "Inter",
            fontWeight: "700" as const,
            animation: "spring" as const,
            textAlign: "center" as const,
            subtitleFontSize: 36,
          }}
        />
        <Composition
          id="IntroOutro"
          component={IntroOutro}
          schema={introOutroSchema}
          durationInFrames={90}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            logoSrc: "logo.png",
            title: "My Newsletter",
            subtitle: "AI Newsletter Automation",
            bgColor: "#0a0a1a",
            accentColor: "#e94560",
            textColor: "#ffffff",
            style: "bold" as const,
            showCta: false,
            ctaText: "Subscribe Now",
          }}
        />
        <Composition
          id="SocialClipVertical"
          component={SocialClip}
          schema={socialClipSchema}
          durationInFrames={150}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            bgColor: "#000000",
            overlayText: "5 AI Tools That Changed My Business",
            overlayPosition: "center" as const,
            fontSize: 64,
            textColor: "#ffffff",
            textShadow: true,
            fontFamily: "Inter",
            fontWeight: "800" as const,
          }}
        />
        <Composition
          id="SocialClipSquare"
          component={SocialClip}
          schema={socialClipSchema}
          durationInFrames={150}
          fps={30}
          width={1080}
          height={1080}
          defaultProps={{
            bgColor: "#1a1a2e",
            overlayText: "Newsletter Growth Hack #7",
            overlayPosition: "center" as const,
            fontSize: 56,
            textColor: "#ffffff",
            textShadow: true,
            fontFamily: "Inter",
            fontWeight: "800" as const,
          }}
        />
        <Composition
          id="CaptionedVideo"
          component={CaptionedVideo}
          schema={captionedVideoSchema}
          durationInFrames={300}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            videoSrc: "sample.mp4",
            captions: [
              { word: "Welcome", startFrame: 0, endFrame: 15 },
              { word: "to", startFrame: 15, endFrame: 22 },
              { word: "Cyber", startFrame: 22, endFrame: 35 },
              { word: "Corsairs", startFrame: 35, endFrame: 50 },
            ],
            captionColor: "#ffffff",
            activeColor: "#FFD700",
            captionFontSize: 56,
            captionPosition: "bottom" as const,
            fontFamily: "Inter",
            wordsPerGroup: 4,
            showBackground: true,
            bgColor: "rgba(0,0,0,0.7)",
          }}
        />
        <Composition
          id="DataViz"
          component={DataViz}
          schema={dataVizSchema}
          durationInFrames={120}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            data: [
              { label: "Jan", value: 12400 },
              { label: "Feb", value: 18700 },
              { label: "Mar", value: 24300 },
              { label: "Apr", value: 31500 },
              { label: "May", value: 42100 },
            ],
            chartType: "bar" as const,
            title: "Subscriber Growth",
            bgColor: "#1a1a2e",
            barColor: "#e94560",
            textColor: "#ffffff",
            fontFamily: "Inter",
            showValues: true,
            animationDelay: 3,
          }}
        />
        <Composition
          id="DataVizHorizontal"
          component={DataViz}
          schema={dataVizSchema}
          durationInFrames={120}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            data: [
              { label: "Email", value: 42, color: "#e94560" },
              { label: "Social", value: 28, color: "#0ea5e9" },
              { label: "SEO", value: 18, color: "#22c55e" },
              { label: "Ads", value: 12, color: "#f59e0b" },
            ],
            chartType: "horizontalBar" as const,
            title: "Traffic Sources (%)",
            bgColor: "#1a1a2e",
            barColor: "#e94560",
            textColor: "#ffffff",
            fontFamily: "Inter",
            showValues: true,
            animationDelay: 3,
          }}
        />
        <Composition
          id="PromoClipVertical"
          component={PromoClip}
          schema={promoClipSchema}
          durationInFrames={210}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            bgColor: "#111111",
            accentColor: "#fa6bfa",
            textColor: "#ffffff",
            mutedColor: "#aaaaaa",
            fontFamily: "Inter",
            starRating: "4.9",
            headline: "You are about to get our 5,000+ best ChatGPT prompts",
            bullets: [
              "Our 5,000+ ChatGPT prompts right now",
              "500+ AI side hustles you can start this week",
              "Cyber Corsairs: AI Productivity Newsletter (215,000+ subscribers)",
            ],
            ctaText: "Join Free Now",
            footerText: "100% Free | Unsubscribe anytime",
          }}
        />
      </Folder>

      <Folder name="Demos">
        <Composition
          id="NoiseDemo"
          component={NoiseDemo}
          durationInFrames={120}
          fps={30}
          width={1920}
          height={1080}
        />
        <Composition
          id="ShapesDemo"
          component={ShapesDemo}
          durationInFrames={120}
          fps={30}
          width={1920}
          height={1080}
        />
        <Composition
          id="PathsDemo"
          component={PathsDemo}
          durationInFrames={120}
          fps={30}
          width={1920}
          height={1080}
        />
        <Composition
          id="MotionBlurDemo"
          component={MotionBlurDemo}
          durationInFrames={90}
          fps={30}
          width={1920}
          height={1080}
        />
        <Composition
          id="GifDemo"
          component={GifDemo}
          durationInFrames={150}
          fps={30}
          width={1920}
          height={1080}
        />
        <Composition
          id="ThreeDemo"
          component={ThreeDemo}
          durationInFrames={120}
          fps={30}
          width={1920}
          height={1080}
        />
        <Composition
          id="LottieDemo"
          component={LottieDemo}
          durationInFrames={120}
          fps={30}
          width={1920}
          height={1080}
        />
      </Folder>

      <Folder name="Transitions">
        <Composition
          id="Transition3DDemo"
          component={Transition3D}
          durationInFrames={30}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            imageSrc: "https://picsum.photos/1920/1080",
            startSwivel: -25,
            startTilt: 12,
            endSwivel: 0,
            endTilt: 0,
            perspective: 1200,
            easeType: "easeOut" as const,
          }}
        />
        <Composition
          id="Transition3DSpring"
          component={Transition3D}
          durationInFrames={45}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            imageSrc: "https://picsum.photos/1920/1080",
            startSwivel: -35,
            startTilt: 18,
            endSwivel: 0,
            endTilt: 0,
            perspective: 1000,
            easeType: "spring" as const,
          }}
        />
        <Composition
          id="Transition3DSubtle"
          component={Transition3D}
          durationInFrames={20}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            imageSrc: "https://picsum.photos/1920/1080",
            startSwivel: -15,
            startTilt: 8,
            endSwivel: 0,
            endTilt: 0,
            perspective: 1500,
            easeType: "easeOut" as const,
          }}
        />
      </Folder>
    </>
  );
};
