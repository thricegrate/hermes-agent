import React, { useRef } from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ThreeCanvas } from "@remotion/three";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

const RotatingBox: React.FC<{ progress: number }> = ({ progress }) => {
  const meshRef = useRef<THREE.Mesh>(null!);

  useFrame(() => {
    if (meshRef.current) {
      meshRef.current.rotation.x = progress * Math.PI * 2;
      meshRef.current.rotation.y = progress * Math.PI * 3;
    }
  });

  return (
    <mesh ref={meshRef} scale={[1.5, 1.5, 1.5]}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color="#fa6bfa" metalness={0.6} roughness={0.3} />
    </mesh>
  );
};

export const ThreeDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const progress = interpolate(frame, [0, durationInFrames], [0, 1]);

  return (
    <AbsoluteFill style={{ backgroundColor: "#0a0a1a" }}>
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <div
          style={{
            fontSize: 56,
            fontWeight: 800,
            color: "#ffffff",
            fontFamily: "Inter",
            marginTop: -400,
            zIndex: 10,
            textShadow: "0 2px 10px rgba(0,0,0,0.8)",
          }}
        >
          @remotion/three
        </div>
      </AbsoluteFill>

      <ThreeCanvas
        orthographic={false}
        width={1920}
        height={1080}
        camera={{ position: [0, 0, 4], fov: 50 }}
        style={{ position: "absolute", top: 0, left: 0 }}
      >
        <ambientLight intensity={0.4} />
        <directionalLight position={[5, 5, 5]} intensity={1} />
        <pointLight position={[-3, -3, 2]} intensity={0.5} color="#fa6bfa" />
        <RotatingBox progress={progress} />
      </ThreeCanvas>

      <div
        style={{
          position: "absolute",
          bottom: 100,
          width: "100%",
          textAlign: "center",
          color: "#aaaaaa",
          fontSize: 28,
          fontFamily: "Inter",
          zIndex: 10,
        }}
      >
        Three.js 3D scene rendered to video
      </div>
    </AbsoluteFill>
  );
};
