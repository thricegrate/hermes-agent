#!/usr/bin/env npx ts-node
/**
 * Generate excalidraw-style explanation images using Gemini API.
 * Supports parallel generation with timeout.
 */

import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";
import * as path from "path";

let MODEL_NAME = "gemini-3-pro-image-preview";

const BASE_SYSTEM_PROMPT = `Generate an Excalidraw-style explanation image matching the reference images. This is for visual explanations that teach concepts clearly.

Match the Excalidraw aesthetic from the references: white/cream background, hand-drawn sketch lines, soft color palette, annotations and labels, arrows showing flow. Use split comparison layouts when appropriate.`;

const DEFAULT_CHARACTER = "no-character";

const SCRIPT_DIR = path.dirname(__filename);
const SKILL_DIR = path.dirname(SCRIPT_DIR);
const REFS_DIR = path.join(SKILL_DIR, "references");
const ENV_FILE = path.join(SKILL_DIR, ".env");
const ROOT_ENV_FILE = path.join(SKILL_DIR, "..", "..", ".env");

// Load .env file
function loadEnv() {
  for (const envPath of [ENV_FILE, ROOT_ENV_FILE]) {
    if (fs.existsSync(envPath)) {
      const content = fs.readFileSync(envPath, "utf-8");
      for (const line of content.split("\n")) {
        const trimmed = line.trim();
        if (trimmed && !trimmed.startsWith("#") && trimmed.includes("=")) {
          const [key, ...valueParts] = trimmed.split("=");
          const value = valueParts.join("=").trim().replace(/^["']|["']$/g, "");
          if (!process.env[key.trim()]) {
            process.env[key.trim()] = value;
          }
        }
      }
    }
  }
}

function loadImageAsBase64(imagePath: string): { data: string; mimeType: string } {
  const ext = path.extname(imagePath).toLowerCase();
  const mimeTypes: Record<string, string> = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
  };
  const mimeType = mimeTypes[ext] || "image/png";
  const data = fs.readFileSync(imagePath).toString("base64");
  return { data, mimeType };
}

function listCharacters(): string[] {
  if (!fs.existsSync(REFS_DIR)) return [];
  return fs.readdirSync(REFS_DIR).filter((f) => {
    const fullPath = path.join(REFS_DIR, f);
    return fs.statSync(fullPath).isDirectory();
  }).sort();
}

function getCharacterReferences(character: string): string[] {
  const charDir = path.join(REFS_DIR, character);
  if (!fs.existsSync(charDir)) return [];
  const files = fs.readdirSync(charDir);
  return files
    .filter((f) => /\.(png|jpg|jpeg|webp)$/i.test(f))
    .sort()
    .map((f) => path.join(charDir, f));
}

function getCharacterPrompt(character: string): string {
  const promptFile = path.join(REFS_DIR, character, "prompt.txt");
  if (fs.existsSync(promptFile)) {
    return fs.readFileSync(promptFile, "utf-8").trim();
  }
  return "";
}

function buildSystemPrompt(character: string, customSystemPrompt?: string): string {
  if (customSystemPrompt) return customSystemPrompt;
  const charPrompt = getCharacterPrompt(character);
  if (charPrompt) {
    return `${BASE_SYSTEM_PROMPT}\n\nIMPORTANT: ${charPrompt}`;
  }
  return BASE_SYSTEM_PROMPT;
}

function findNextAvailableIndex(outputDir: string): number {
  // Find the highest existing excalidraw_N.png and return N+1
  if (!fs.existsSync(outputDir)) {
    return 1;
  }
  const files = fs.readdirSync(outputDir);
  let maxIndex = 0;
  for (const file of files) {
    const match = file.match(/^excalidraw_(\d+)\.png$/);
    if (match) {
      const index = parseInt(match[1], 10);
      if (index > maxIndex) {
        maxIndex = index;
      }
    }
  }
  return maxIndex + 1;
}

async function generateSingleImage(
  genai: GoogleGenAI,
  prompt: string,
  referenceImages: { data: string; mimeType: string }[],
  index: number,
  aspectRatio: string = "16:9"
): Promise<{ index: number; image?: Buffer; error?: string }> {
  try {
    const parts: Array<{ text: string } | { inlineData: { data: string; mimeType: string } }> = [
      { text: prompt },
    ];

    for (const img of referenceImages) {
      parts.push({
        inlineData: {
          data: img.data,
          mimeType: img.mimeType,
        },
      });
    }

    const response = await genai.models.generateContent({
      model: MODEL_NAME,
      contents: [
        {
          role: "user",
          parts,
        },
      ],
      config: {
        responseModalities: ["TEXT", "IMAGE"],
        imageConfig: {
          aspectRatio: aspectRatio,
          imageSize: "2K",
        },
      } as any,
    });

    const candidate = response.candidates?.[0];
    if (!candidate?.content?.parts) {
      return { index, error: "No response from model" };
    }

    for (const part of candidate.content.parts) {
      if (part.inlineData?.data) {
        return {
          index,
          image: Buffer.from(part.inlineData.data, "base64"),
        };
      }
    }

    return { index, error: "No image in response" };
  } catch (error) {
    return {
      index,
      error: error instanceof Error ? error.message : "Unknown error",
    };
  }
}

async function main() {
  loadEnv();

  const args = process.argv.slice(2);

  // Parse arguments
  let prompt = "";
  let count = 5;
  const PROJECT_ROOT = path.resolve(SKILL_DIR, "..", "..");
  let outputDir = path.join(PROJECT_ROOT, ".memory", "media", "infographics");
  let timeout = 180;
  let apiKey = process.env.GEMINI_API_KEY || "";
  let customRefs: string[] = [];
  let customSystemPrompt: string | undefined;
  let aspectRatio = "3:4";
  let character = DEFAULT_CHARACTER;
  let doListCharacters = false;

  let promptFile = "";

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === "-n" || arg === "--count") {
      count = parseInt(args[++i], 10);
    } else if (arg === "-o" || arg === "--output") {
      outputDir = args[++i];
    } else if (arg === "-t" || arg === "--timeout") {
      timeout = parseInt(args[++i], 10);
    } else if (arg === "-r" || arg === "--reference") {
      customRefs.push(args[++i]);
    } else if (arg === "--api-key") {
      apiKey = args[++i];
    } else if (arg === "--system-prompt") {
      customSystemPrompt = args[++i];
    } else if (arg === "-f" || arg === "--prompt-file") {
      promptFile = args[++i];
    } else if (arg === "--aspect-ratio") {
      aspectRatio = args[++i];
    } else if (arg === "-c" || arg === "--character") {
      character = args[++i];
    } else if (arg === "-m" || arg === "--model") {
      MODEL_NAME = args[++i];
    } else if (arg === "--list-characters") {
      doListCharacters = true;
    } else if (!arg.startsWith("-")) {
      prompt = arg;
    }
  }

  // Handle --list-characters
  if (doListCharacters) {
    const chars = listCharacters();
    if (chars.length === 0) {
      console.log("No characters found. Add subfolders to references/ with PNGs + prompt.txt");
    } else {
      console.log("Available characters:");
      for (const c of chars) {
        const refs = getCharacterReferences(c);
        const hasPrompt = fs.existsSync(path.join(REFS_DIR, c, "prompt.txt"));
        const defaultTag = c === DEFAULT_CHARACTER ? " (default)" : "";
        console.log(`  ${c}${defaultTag} — ${refs.length} reference(s)${hasPrompt ? ", has prompt.txt" : ""}`);
      }
    }
    process.exit(0);
  }

  if (promptFile && fs.existsSync(promptFile)) {
    prompt = fs.readFileSync(promptFile, "utf-8").trim();
  }

  if (!apiKey) {
    console.error("Error: Gemini API key required. Set GEMINI_API_KEY or use --api-key");
    process.exit(1);
  }

  if (!prompt) {
    console.error("Usage: generate.ts <prompt> [-n count] [-o output] [-t timeout] [-r reference]");
    process.exit(1);
  }

  // Load reference images
  const refPaths = customRefs.length > 0 ? customRefs : getCharacterReferences(character);
  if (refPaths.length === 0) {
    const available = listCharacters();
    console.error(`Error: No reference images found for character "${character}"`);
    if (available.length > 0) {
      console.error(`Available characters: ${available.join(", ")}`);
    }
    process.exit(1);
  }

  const systemPrompt = buildSystemPrompt(character, customSystemPrompt);
  console.log(`Character: ${character}`);
  console.log(`Loading ${refPaths.length} reference image(s)...`);
  const referenceImages: { data: string; mimeType: string }[] = [];
  for (const refPath of refPaths) {
    if (!fs.existsSync(refPath)) {
      console.warn(`Warning: Reference image not found: ${refPath}`);
      continue;
    }
    const img = loadImageAsBase64(refPath);
    referenceImages.push(img);
    console.log(`  Loaded: ${path.basename(refPath)}`);
  }

  if (referenceImages.length === 0) {
    console.error("Error: No valid reference images loaded");
    process.exit(1);
  }

  // Create output directory
  fs.mkdirSync(outputDir, { recursive: true });

  // Build full prompt
  const fullPrompt = `${systemPrompt}\n\nContent to visualize:\n${prompt}`;

  // Find starting index to avoid overwrites
  const startIndex = findNextAvailableIndex(outputDir);
  if (startIndex > 1) {
    console.log(`Found existing images, starting at index ${startIndex}`);
  }

  console.log(`\nGenerating ${count} image(s)...`);
  console.log(`Timeout: ${timeout}s per image`);

  const genai = new GoogleGenAI({ apiKey });

  // Define variation styles for consistent cross-chunk generation
  const VARIATION_STYLES = [
    "Variation Style 1: Structured mind map or hierarchical diagram outlining the core concepts.",
    "Variation Style 2: Sequential flow or step-by-step process diagram.",
    "Variation Style 3: Split-screen comparison layout or pros/cons list.",
    "Variation Style 4: Central metaphorical illustration heavily annotated with key points.",
    "Variation Style 5: Simplified, minimalist core concept diagram using basic shapes."
  ];

  // Generate images in parallel
  const promises = Array.from({ length: count }, (_, i) => {
    // Determine variation style based on index (cycles if > 5 images)
    const styleInstruction = VARIATION_STYLES[i % VARIATION_STYLES.length];
    const promptWithStyle = `${fullPrompt}\n\nSTYLE INSTRUCTION FOR THIS VARIATION:\n${styleInstruction}`;

    return Promise.race([
      generateSingleImage(genai, promptWithStyle, referenceImages, i, aspectRatio),
      new Promise<{ index: number; error: string }>((resolve) =>
        setTimeout(() => resolve({ index: i, error: `Timeout after ${timeout}s` }), timeout * 1000)
      ),
    ]);
  });

  const results = await Promise.all(promises);
  results.sort((a, b) => a.index - b.index);

  // Save results with non-conflicting filenames
  let successCount = 0;
  for (const result of results) {
    if ("image" in result && result.image) {
      const fileIndex = startIndex + result.index;
      const outputPath = path.join(outputDir, `excalidraw_${fileIndex}.png`);
      fs.writeFileSync(outputPath, result.image);
      console.log(`  Saved: ${outputPath}`);
      successCount++;
    } else {
      console.log(`  Failed image ${result.index + 1}: ${result.error}`);
    }
  }

  console.log(`\nGenerated ${successCount}/${count} images in ${outputDir}`);

  if (successCount === 0) {
    process.exit(1);
  }
}

main().catch((err) => {
  console.error("Error:", err);
  process.exit(1);
});
