#!/usr/bin/env python3
"""
Generate an HTML gallery from ads-designer batch output.

Reads the output directory structure and creates a single gallery.html file
with all generated ads organized by template, filterable by category.

Usage:
    python generate_gallery.py --input ./output/
    python generate_gallery.py --input ./output/ --output ./gallery.html
"""

import argparse
import json
import sys
from pathlib import Path


# Category mapping for template numbers (matches ad-format-catalog.md)
CATEGORIES = {
    "copy-forward": [1, 2, 5, 21, 23, 30],
    "social-proof": [3, 6, 11, 15, 16, 17, 19],
    "comparison": [7, 8, 25, 31],
    "data-authority": [4, 10, 13, 18, 20, 26, 28],
    "product-showcase": [12, 14, 22, 27, 35, 37],
    "native-organic": [9, 33, 34, 36, 40],
    "hybrid": [24, 29, 32, 38, 39],
}

# Reverse lookup: template number -> category
TEMPLATE_CATEGORY = {}
for cat, nums in CATEGORIES.items():
    for num in nums:
        TEMPLATE_CATEGORY[num] = cat


def get_template_number(dir_name: str) -> int | None:
    """Extract template number from directory name like '01_headline'."""
    parts = dir_name.split("_", 1)
    try:
        return int(parts[0])
    except (ValueError, IndexError):
        return None


def build_gallery(input_dir: str, output_path: str | None = None):
    """Build the HTML gallery from the output directory."""
    in_path = Path(input_dir)
    if not in_path.exists():
        print(f"Error: Directory not found: {input_dir}")
        sys.exit(1)

    # Load results.json if available
    results_data = {}
    results_file = in_path / "results.json"
    if results_file.exists():
        with open(results_file) as f:
            results_data = json.load(f)

    # Scan template directories
    templates = []
    for template_dir in sorted(in_path.iterdir()):
        if not template_dir.is_dir():
            continue

        num = get_template_number(template_dir.name)
        if num is None:
            continue

        # Find all images in this template dir
        images = []
        for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
            images.extend(sorted(template_dir.glob(ext)))

        if not images:
            continue

        # Read prompt if available
        prompt_file = template_dir / "prompt.txt"
        prompt_text = prompt_file.read_text(encoding="utf-8") if prompt_file.exists() else ""

        # Get template name from directory
        name_part = template_dir.name.split("_", 1)
        name = name_part[1].replace("_", " ").title() if len(name_part) > 1 else template_dir.name

        category = TEMPLATE_CATEGORY.get(num, "other")

        templates.append({
            "number": num,
            "name": name,
            "category": category,
            "prompt": prompt_text[:500],
            "images": [str(img.relative_to(in_path)) for img in images],
            "image_count": len(images),
        })

    if not templates:
        print("No generated ads found in the directory")
        sys.exit(1)

    def escape_html(text: str) -> str:
        """Escape text for safe HTML insertion."""
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

    # Build HTML
    brand = escape_html(results_data.get("brand", "Ad Creatives"))
    total_images = sum(t["image_count"] for t in templates)
    categories_used = sorted(set(t["category"] for t in templates))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{brand} - Ad Gallery</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0a0a0a; color: #e0e0e0; }}

.header {{
    padding: 32px 40px;
    border-bottom: 1px solid #222;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
}}
.header h1 {{ font-size: 24px; font-weight: 600; }}
.header .stats {{ font-size: 14px; color: #888; }}

.filters {{
    padding: 16px 40px;
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    border-bottom: 1px solid #1a1a1a;
}}
.filter-btn {{
    padding: 6px 16px;
    border-radius: 20px;
    border: 1px solid #333;
    background: transparent;
    color: #aaa;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s;
}}
.filter-btn:hover {{ border-color: #555; color: #fff; }}
.filter-btn.active {{ background: #fff; color: #000; border-color: #fff; }}

.gallery {{ padding: 24px 40px; }}

.template-section {{
    margin-bottom: 40px;
    display: none;
}}
.template-section.visible {{ display: block; }}

.template-header {{
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid #1a1a1a;
}}
.template-number {{
    font-size: 14px;
    font-weight: 700;
    color: #555;
    font-variant-numeric: tabular-nums;
}}
.template-name {{ font-size: 18px; font-weight: 600; }}
.template-category {{
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 10px;
    background: #1a1a1a;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.image-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
}}

.image-card {{
    border-radius: 8px;
    overflow: hidden;
    background: #111;
    cursor: pointer;
    transition: transform 0.2s;
}}
.image-card:hover {{ transform: scale(1.02); }}
.image-card img {{
    width: 100%;
    height: auto;
    display: block;
}}

/* Lightbox */
.lightbox {{
    display: none;
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0,0,0,0.95);
    z-index: 1000;
    justify-content: center;
    align-items: center;
    cursor: zoom-out;
}}
.lightbox.open {{ display: flex; }}
.lightbox img {{
    max-width: 90vw;
    max-height: 90vh;
    object-fit: contain;
    border-radius: 4px;
}}
.lightbox-close {{
    position: fixed;
    top: 20px; right: 24px;
    font-size: 28px;
    color: #888;
    cursor: pointer;
    z-index: 1001;
}}
.lightbox-close:hover {{ color: #fff; }}

.prompt-toggle {{
    font-size: 12px;
    color: #555;
    cursor: pointer;
    margin-top: 8px;
}}
.prompt-toggle:hover {{ color: #888; }}
.prompt-text {{
    display: none;
    margin-top: 8px;
    padding: 12px;
    background: #111;
    border-radius: 6px;
    font-size: 12px;
    line-height: 1.5;
    color: #777;
    white-space: pre-wrap;
    word-break: break-word;
}}
.prompt-text.visible {{ display: block; }}
</style>
</head>
<body>

<div class="header">
    <h1>{brand} Ad Gallery</h1>
    <div class="stats">{total_images} images across {len(templates)} templates</div>
</div>

<div class="filters">
    <button class="filter-btn active" data-filter="all">All ({total_images})</button>
"""

    # Add category filter buttons
    for cat in categories_used:
        cat_count = sum(t["image_count"] for t in templates if t["category"] == cat)
        cat_label = cat.replace("-", " ").title()
        html += f'    <button class="filter-btn" data-filter="{cat}">{cat_label} ({cat_count})</button>\n'

    html += """</div>

<div class="gallery">
"""

    # Add template sections
    for t in templates:
        safe_name = escape_html(t['name'])
        safe_category = escape_html(t['category'].replace('-', ' '))
        html += f"""    <div class="template-section visible" data-category="{escape_html(t['category'])}">
        <div class="template-header">
            <span class="template-number">#{t['number']:02d}</span>
            <span class="template-name">{safe_name}</span>
            <span class="template-category">{safe_category}</span>
        </div>
        <div class="image-grid">
"""
        for img_path in t["images"]:
            safe_path = escape_html(img_path)
            html += f'            <div class="image-card"><img src="{safe_path}" alt="{safe_name}" loading="lazy"></div>\n'

        html += "        </div>\n"

        if t["prompt"]:
            escaped_prompt = escape_html(t["prompt"])
            html += f'        <div class="prompt-toggle" onclick="this.nextElementSibling.classList.toggle(\'visible\')">Show prompt</div>\n'
            html += f'        <div class="prompt-text">{escaped_prompt}</div>\n'

        html += "    </div>\n\n"

    html += """</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox()">
    <span class="lightbox-close">&times;</span>
    <img id="lightbox-img" src="" alt="">
</div>

<script>
// Category filtering
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;
        document.querySelectorAll('.template-section').forEach(section => {
            if (filter === 'all' || section.dataset.category === filter) {
                section.classList.add('visible');
            } else {
                section.classList.remove('visible');
            }
        });
    });
});

// Lightbox
document.querySelectorAll('.image-card img').forEach(img => {
    img.addEventListener('click', (e) => {
        e.stopPropagation();
        document.getElementById('lightbox-img').src = img.src;
        document.getElementById('lightbox').classList.add('open');
    });
});

function closeLightbox() {
    document.getElementById('lightbox').classList.remove('open');
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
});
</script>

</body>
</html>"""

    # Write gallery
    if output_path:
        gallery_path = Path(output_path)
    else:
        gallery_path = in_path / "gallery.html"

    gallery_path.write_text(html, encoding="utf-8")
    print(f"Gallery saved: {gallery_path}")
    print(f"  {total_images} images across {len(templates)} templates")


def main():
    parser = argparse.ArgumentParser(
        description="Generate HTML gallery from ads-designer batch output"
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the output directory containing generated ads",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output path for gallery.html (default: inside input directory)",
    )

    args = parser.parse_args()
    build_gallery(args.input, args.output)


if __name__ == "__main__":
    main()
