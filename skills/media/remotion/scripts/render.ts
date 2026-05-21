import path from "path";
import { fileURLToPath } from "url";
import { bundle } from "@remotion/bundler";
import { getCompositions, renderMedia } from "@remotion/renderer";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const args = process.argv.slice(2);

function getArg(name: string, defaultValue?: string): string | undefined {
  const index = args.indexOf(`--${name}`);
  if (index === -1) return defaultValue;
  return args[index + 1];
}

async function main() {
  const compositionId = getArg("comp");
  const propsJson = getArg("props", "{}");
  const outputLocation = getArg("out", "out/output.mp4");
  const codec = (getArg("codec", "h264") as "h264" | "h265" | "vp8" | "vp9");
  const crf = Number(getArg("crf", "18"));
  const concurrency = Number(getArg("concurrency", "4"));

  if (!compositionId) {
    console.error(
      "Usage: npx ts-node scripts/render.ts --comp <CompositionId> [--props <json>] [--out <path>] [--codec h264] [--crf 18]"
    );
    process.exit(1);
  }

  const inputProps = JSON.parse(propsJson!);

  console.log("Bundling...");
  const bundleLocation = await bundle({
    entryPoint: path.resolve(__dirname, "../src/index.ts"),
    onProgress: (progress: number) => {
      if (progress % 25 === 0) process.stdout.write(`  ${progress}%\r`);
    },
  });
  console.log("Bundle complete.");

  const compositions = await getCompositions(bundleLocation, { inputProps });
  const composition = compositions.find((c) => c.id === compositionId);

  if (!composition) {
    console.error(`Composition "${compositionId}" not found.`);
    console.error(
      `Available: ${compositions.map((c) => c.id).join(", ")}`
    );
    process.exit(1);
  }

  console.log(
    `Rendering "${compositionId}" (${composition.width}x${composition.height}, ${composition.durationInFrames}f @ ${composition.fps}fps)...`
  );

  await renderMedia({
    composition,
    serveUrl: bundleLocation,
    codec,
    crf,
    outputLocation: path.resolve(outputLocation!),
    inputProps,
    concurrency,
    onProgress: ({ progress }: { progress: number }) => {
      process.stdout.write(`  ${Math.round(progress * 100)}%\r`);
    },
  });

  console.log(`\nDone: ${outputLocation}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
