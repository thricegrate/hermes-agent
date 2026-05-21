---
name: infographic-gen
description: Generate infographic and explanation images using Gemini API. Use when the user wants to create visual explanations, diagrams, or illustrations in the hand-drawn excalidraw aesthetic. Supports parallel generation of multiple variations with configurable timeout. Triggers on requests like "generate an infographic image", "create a visual explanation", "make a diagram for [concept]", or "illustrate [topic]" or "make an infographic for [concept]".
---

## Prompt Content Rule — CRITICAL

**ALWAYS pass the entire raw content verbatim as the prompt.** Never summarize, paraphrase, or condense the content. Whether it's a single section or a whole file, the full text goes into the generate command as-is (with the white background prefix/suffix wrapped around it). This gives Gemini the richest context to produce accurate visuals.

## Semantic Chunking

Don't chunk solely by `## ` headings. Look for:
- Concept definitions ("What is X?", "X are the boundaries where...")
- Distinct examples or scenarios
- Shifts in topic within a section
- Before/after comparisons
- Standalone explanations (like "**What are contracts?**" paragraphs)

Each chunk = one image. A single `## ` section might produce 2-4 chunks if it covers multiple concepts. When analyzing content, identify these semantic boundaries first, then generate images for each chunk.

---

## First: Ask the User

Before generating, ask the user which mode they want:

1. **Specific section** — Generate images for one section only (user provides the content)
2. **Whole file** — Parse a markdown file into `## sections`, generate images for ALL sections in parallel using subagents

Use AskUserQuestion with options:
- "Specific section" — I'll generate images for content you provide
- "Whole file" — I'll split the file by ## headings and generate for all sections in parallel

## Mode 1: Specific Section

For a single section:

1. Get the section content from the user
2. Create a descriptive subfolder name (kebab-case from section title)
3. Run the generate command, passing the **entire section content verbatim** as the prompt (never summarize):

```bash
cd skills/infographic-gen && npx ts-node scripts/generate.ts "<entire section content verbatim>" -n 3 -o "private project notes/media/infographics/<section-name>"
```

4. Add all 3 image embeds to the markdown after the section (see "Adding Image Embeds" below)

## Mode 2: Whole File (Batched)

For an entire markdown file:

1. Read the file and split by `## ` headings (or semantic chunks)
2. **Process in batches of 2** to avoid Google API rate limits:
   - Launch 2 background Bash tasks at a time
   - Wait for both to complete before starting the next batch
   - Repeat until all sections are done
3. For each section, spawn a **background subagent** (Bash type) to generate images:
   - Subfolder: `private project notes/media/infographics/<section-name-kebab-case>/`
   - Prompt: The **entire section content verbatim** — NEVER summarize, always pass the full raw text
   - Use `run_in_background: true`
4. Add all 3 image embeds after each section in the markdown (see "Adding Image Embeds" below)

**Rate limit constraint:** Never run more than 2 generation tasks simultaneously. The Gemini API will rate-limit if you exceed this.

**Subagent template:**
```
Run this bash command (timeout 900000ms):
cd "skills/infographic-gen" && npx ts-node scripts/generate.ts "<entire section content verbatim>" -n 3 -o "private project notes/media/infographics/<section-name>"
```

**Batch workflow:**
```
Batch 1: section-1, section-2 → wait for completion
Batch 2: section-3, section-4 → wait for completion
...continue until done
```

## Generate Command

```bash
cd .claude/skills/infographic-gen && npx ts-node scripts/generate.ts <prompt> [options]
```

**Prompt requirements — CRITICAL:**
- **START every prompt with:** `"CRITICAL: Use a plain white background (#FFFFFF). No gradients, no colors, no textures — pure white only."`
- This instruction MUST appear at the very beginning of the prompt, before any content description
- The excalidraw style requires a clean white background — Gemini tends to add colored/gradient backgrounds if not explicitly forbidden
- **END every prompt with:** `"At the bottom of the infographic, include: [your website URL from private project notes/MEMORY.md]"` -- this is mandatory branding on every generated visual.

**Options:**
- `-n, --count` — Number of images (default: 5)
- `-o, --output` — Output directory (default: `private project notes/media/infographics/`; use subfolder per section)
- `-t, --timeout` — Timeout per image in seconds (default: 180)
- `-c, --character` — Character style to use (default: `no-character`). See "Character Styles" below.
- `--aspect-ratio` — Image aspect ratio (default: `3:4`). Use `16:9` for horizontal, `9:16` for tall vertical.
- `--list-characters` — Print available character styles and exit
- `-f, --prompt-file` — Read prompt from a file instead of CLI arg (avoids shell escaping issues)

## Adding Image Embeds

After generation completes, add **all 3 images** to the markdown file under the relevant section. The user picks their favorite(s) later.

**Embed format (Obsidian):**
```markdown
![[images/section-name/excalidraw_1.png]]
![[images/section-name/excalidraw_2.png]]
![[images/section-name/excalidraw_3.png]]
```

Place embeds at the end of each section, before the next `---` or `##` heading.

## Important Notes

- **No overwrites:** Script auto-increments filenames if images exist
- **Subfolders:** Always use a descriptive subfolder per section (e.g., `private project notes/media/infographics/core-insight/`, `private project notes/media/infographics/kitchen-sink/`)
- **Default 3 variants:** Generate 3 images by default. User will ask if they want more.
- **Timeout:** Allow 15 minutes for generation. Use 900000ms timeout for subagents and Bash calls.

## MANDATORY: Send Images to Telegram After Generation

**Every time images are generated, ALWAYS send them to Telegram immediately after generation completes.** Do not wait for the user to ask. This is automatic.

```bash
python tools/telegram-send/send_image.py <image_paths> --caption "<description>"
```

This applies to ALL generation modes (single section, whole file, one-off requests). The user should never have to ask for the images -- they arrive in Telegram automatically.

## Character Styles

Characters are auto-discovered from subfolders in `references/`. Each subfolder contains:
- Reference PNG images (the visual style Gemini should match)
- `prompt.txt` — character-specific system prompt fragment

**Available characters:**
- `no-character` (default) — Clean infographic without character illustrations. Icons, typography, and geometric shapes only. Best for LinkedIn cheatsheets and professional reference graphics.
- `blue-robot` — Cute light blue robot with rounded head, glowing blue eyes, screen on chest
- `pirate-robot` — Purple/teal armored pirate robot with hat, parrot companion, corsair aesthetic

**Adding new characters:**
1. Create a new subfolder: `references/<character-name>/`
2. Add 2-4 reference PNG images showing the character in excalidraw style
3. Add a `prompt.txt` describing the character for Gemini (one paragraph)
4. The character is immediately available via `--character <character-name>`

## LinkedIn Cheatsheet Workflow

Pinterest-to-Gemini reverse-prompting workflow for creating LinkedIn-optimized infographics. Source: Ruben Hassid (770K LinkedIn followers, 1.56M across 5 accounts).

### The Process

1. **Source layout from Pinterest:** Search `[niche] + cheat sheet` or `[niche] + infographic` or `[niche] + graph` on Pinterest. Find layouts that organize information well.
2. **Reverse-prompt the layout:** Upload the Pinterest reference to Gemini with: "Extract all the information from this image so another designer could recreate it from scratch." This gives you the structural blueprint without copying the design.
3. **Find a handwritten/sketch style reference:** Search Pinterest for hand-drawn or sketch-style infographics. This is the STYLE target.
4. **Generate with style fusion:** Combine the content (from step 2) + the organic style (from step 3) + your actual content. Use the `no-character` style which already targets the excalidraw aesthetic.
5. **Use LinkedIn dimensions:** Always use `--aspect-ratio 3:4` for LinkedIn (produces 1080x1350).
6. **Anti-brand rule:** NO logos, NO brand colors. The excalidraw hand-drawn aesthetic IS the optimal LinkedIn visual style. Do not "upgrade" to polished corporate design.

### Quick Command

```bash
cd skills/infographic-gen && npx ts-node scripts/generate.ts "<content>" -n 3 -o "private project notes/media/infographics/<topic>" --aspect-ratio 3:4 -c no-character
```

### Why This Works

- Cheat sheets are the #1 saved content type on LinkedIn
- 3:4 portrait takes 80% of mobile screen (maximum visual real estate)
- Scrappy/hand-drawn beats polished corporate (signals authenticity)
- Reverse-prompting gives you proven layouts without plagiarizing designs
- Each infographic = a social post + newsletter asset + lead magnet component

---

## Requirements

- Node.js with dependencies installed (`npm install` in skill folder)
- `GEMINI_API_KEY` in `.env` file (already configured)

## Reference Images

The `references/` folder contains character subfolders with reference images that define the excalidraw style. These load automatically based on the selected `--character`.
