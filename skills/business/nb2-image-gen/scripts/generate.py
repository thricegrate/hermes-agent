#!/usr/bin/env python3
"""
Generate images using Nano Banana 2 (Gemini) for any purpose.

Single image:
    python generate.py --prompt "Create a dark tech product card..." --output cover.png --aspect 16:9

Batch from JSON:
    python generate.py --batch prompts.json --output ./covers/ --count 2

With reference image:
    python generate.py --prompt "Redesign this..." --ref screenshot.png --output out.png
"""

import argparse
import base64
import io
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from PIL import Image
from google import genai
from google.genai import types

load_dotenv()

MODEL = "gemini-3-pro-image-preview"
API_KEY = os.getenv("NANO_BANANA_API_KEY") or os.getenv("GEMINI_API_KEY")

# Aspect ratio to approximate pixel dimensions (for prompt hints)
ASPECT_DIMS = {
    "1:1": (1024, 1024),
    "4:5": (1024, 1280),
    "5:4": (1280, 1024),
    "9:16": (1024, 1820),
    "16:9": (1280, 720),
    "3:1": (1200, 400),
    "4:1": (1600, 400),
}

REF_MAX_SIZE = (1024, 1024)


def load_reference_image(path: Path) -> Image.Image | None:
    """Load and resize a reference image."""
    try:
        img = Image.open(path)
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")
        img.thumbnail(REF_MAX_SIZE, Image.Resampling.LANCZOS)
        return img
    except Exception as e:
        print(f"  Warning: Could not load {path}: {e}")
        return None


def generate_image(
    prompt_text: str,
    reference_images: list[Image.Image] | None = None,
) -> Image.Image | None:
    """Generate a single image via Gemini API."""
    client = genai.Client(api_key=API_KEY)

    if reference_images:
        ref_label = "REFERENCE IMAGE(S): Use these as visual reference for style, layout, or content.\n\n"
        full_prompt = ref_label + prompt_text
        contents = list(reference_images) + [full_prompt]
    else:
        contents = [prompt_text]

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )

        if response.candidates and response.candidates[0].content:
            for part in response.candidates[0].content.parts:
                if hasattr(part, "inline_data") and part.inline_data:
                    data = part.inline_data.data
                    if data:
                        img_bytes = (
                            base64.b64decode(data)
                            if isinstance(data, str)
                            else data
                        )
                        return Image.open(io.BytesIO(img_bytes))
                elif hasattr(part, "text") and part.text:
                    print(f"    Model note: {part.text[:200]}")

        print("    No image in response")
        return None

    except Exception as e:
        print(f"    Error: {e}")
        return None


def generate_single(
    prompt: str,
    output: str,
    aspect: str = "1:1",
    ref_paths: list[str] | None = None,
    count: int = 1,
):
    """Generate a single image (or N variations)."""
    # Load reference images
    refs = []
    if ref_paths:
        for p in ref_paths:
            img = load_reference_image(Path(p))
            if img:
                refs.append(img)
                print(f"  Loaded ref: {p} ({img.size[0]}x{img.size[1]})")

    out_path = Path(output)

    for v in range(count):
        label = f" (v{v+1}/{count})" if count > 1 else ""
        print(f"Generating{label}...", end=" ", flush=True)

        result = generate_image(prompt, refs if refs else None)

        if result:
            if count > 1:
                # Multiple variations: add suffix
                stem = out_path.stem
                suffix = out_path.suffix or ".png"
                save_path = out_path.parent / f"{stem}_v{v+1}{suffix}"
            else:
                save_path = out_path

            save_path.parent.mkdir(parents=True, exist_ok=True)
            result.save(save_path, "PNG")
            print(f"Saved: {save_path} ({result.size[0]}x{result.size[1]})")
        else:
            # Retry once
            print("Failed, retrying...", end=" ", flush=True)
            time.sleep(3)
            result = generate_image(prompt, refs if refs else None)
            if result:
                save_path = out_path if count == 1 else out_path.parent / f"{out_path.stem}_v{v+1}{out_path.suffix or '.png'}"
                save_path.parent.mkdir(parents=True, exist_ok=True)
                result.save(save_path, "PNG")
                print(f"Saved on retry: {save_path} ({result.size[0]}x{result.size[1]})")
            else:
                print("Failed")

        if v < count - 1:
            time.sleep(3)


def generate_batch(
    batch_path: str,
    output_dir: str,
    count: int = 1,
    delay: float = 3.0,
):
    """Generate images from a JSON batch file."""
    with open(batch_path) as f:
        data = json.load(f)

    images = data.get("images", [])
    project = data.get("project", "unknown")

    if not images:
        print("Error: No images found in batch file")
        sys.exit(1)

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    total = len(images) * count
    completed = 0
    failed = 0

    print(f"\n{'='*60}")
    print(f"  Project: {project}")
    print(f"  Images: {len(images)}")
    print(f"  Variations: {count}")
    print(f"  Total: {total}")
    print(f"  Output: {out_path}")
    print(f"{'='*60}\n")

    results = {
        "project": project,
        "started_at": datetime.now().isoformat(),
        "results": [],
    }

    for item in images:
        img_id = item["id"]
        name = item.get("name", img_id)
        prompt = item["prompt"]
        ref_paths = item.get("reference_images", [])

        # Load references
        refs = []
        for rp in ref_paths:
            img = load_reference_image(Path(rp))
            if img:
                refs.append(img)

        # Create output dir for this image
        img_dir = out_path / img_id
        img_dir.mkdir(parents=True, exist_ok=True)
        (img_dir / "prompt.txt").write_text(prompt, encoding="utf-8")

        print(f"[{img_id}] {name}")

        for v in range(count):
            completed += 1
            label = f"v{v+1}"
            print(f"  Generating {label} ({completed}/{total})...", end=" ", flush=True)

            result = generate_image(prompt, refs if refs else None)

            if result:
                save_path = img_dir / f"image_{label}.png"
                result.save(save_path, "PNG")
                print(f"Saved ({result.size[0]}x{result.size[1]})")
                results["results"].append({
                    "id": img_id, "name": name, "variation": label,
                    "status": "success", "file": str(save_path.relative_to(out_path)),
                    "size": f"{result.size[0]}x{result.size[1]}",
                })
            else:
                print("Failed, retrying...", end=" ", flush=True)
                time.sleep(delay)
                result = generate_image(prompt, refs if refs else None)
                if result:
                    save_path = img_dir / f"image_{label}.png"
                    result.save(save_path, "PNG")
                    print(f"Saved on retry ({result.size[0]}x{result.size[1]})")
                    results["results"].append({
                        "id": img_id, "name": name, "variation": label,
                        "status": "success_retry", "file": str(save_path.relative_to(out_path)),
                        "size": f"{result.size[0]}x{result.size[1]}",
                    })
                else:
                    print("Failed")
                    failed += 1
                    results["results"].append({
                        "id": img_id, "name": name, "variation": label,
                        "status": "failed",
                    })

            if completed < total:
                time.sleep(delay)

    results["completed_at"] = datetime.now().isoformat()
    results["succeeded"] = completed - failed
    results["failed"] = failed

    with open(out_path / "results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print(f"  Done! {completed - failed}/{completed} images generated")
    if failed:
        print(f"  Failed: {failed}")
    print(f"  Output: {out_path}")
    print(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using Nano Banana 2 (Gemini)"
    )

    # Mode: single or batch
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--prompt", "-p", help="Single prompt text")
    mode.add_argument("--batch", "-b", help="Path to JSON batch file")

    parser.add_argument("--output", "-o", default="./output.png",
                        help="Output file (single) or directory (batch)")
    parser.add_argument("--ref", "-r", nargs="*",
                        help="Reference image(s) for style/content guidance")
    parser.add_argument("--aspect", "-a", default="1:1",
                        help="Aspect ratio hint (single mode only): 1:1, 4:5, 16:9, 9:16, 3:1")
    parser.add_argument("--count", "-n", type=int, default=1,
                        help="Variations per prompt (default: 1)")
    parser.add_argument("--delay", "-d", type=float, default=3.0,
                        help="Delay between API calls in seconds (default: 3.0)")

    args = parser.parse_args()

    if not API_KEY:
        print("Error: Set GEMINI_API_KEY or NANO_BANANA_API_KEY in environment")
        sys.exit(1)

    if args.prompt:
        generate_single(
            prompt=args.prompt,
            output=args.output,
            aspect=args.aspect,
            ref_paths=args.ref,
            count=args.count,
        )
    else:
        generate_batch(
            batch_path=args.batch,
            output_dir=args.output,
            count=args.count,
            delay=args.delay,
        )


if __name__ == "__main__":
    main()
