# Ranked List Slideshow Template

Reverse-order list reveal. 5 to 7 slides. Anchor metric: swipe-through to final reveal.

For the universal format reference, see [references/slideshow-formats.md](../references/slideshow-formats.md).

## When this format wins

- Tool comparisons
- Recommendation roundups
- Curated picks where the curation work has value
- "Best of" lists in a specific niche
- the product skill rankings (which skills replace which paid tools)

## Slot-fill skeleton

```
SLIDE 1 (THEME):
Format: List theme + reveal promise. The audience knows they will see N items, ranked, with #1
last.
Slot: [The list theme] + [The category being ranked] + [The promise of a #1 reveal].

SLIDE 2 (ITEM 5 or N):
Format: The first item in the reveal. Name + brief explanation of why it ranks here.
Slot: [Item N] + [Why it ranks at this spot].

SLIDE 3 (ITEM 4 or N-1):
Format: Same structure.
Slot: [Item N-1] + [Brief reason].

SLIDE 4 (ITEM 3 or N-2):
Format: Same structure.
Slot: [Item N-2] + [Brief reason].

SLIDE 5 (ITEM 2):
Format: Tease that #1 is coming.
Slot: [Item 2] + [Brief reason] + [Hint that #1 is going to surprise them].

SLIDE 6 (ITEM 1, the reveal):
Format: The top item. Strongest visual. Most decisive framing.
Slot: [Item 1] + [Why it wins].

SLIDE 7 (CTA): [Use only if going to 7 slides; otherwise CTA is on slide 6]
Format: Low-friction CTA.
Slot: [Comment keyword / Bio link / Save this].
```

## Worked example

A Ranked List slideshow for top AI tools that replaced paid software:

```
# Slideshow: 5 free AI tools that replaced $400 of paid software

**Format:** Ranked List
**Slide count:** 6
**Audio:** Playful upbeat track in tech/AI niche, fits the discovery frame
**Posting hint:** Tuesday or Thursday 11am-1pm ET

---

## Slide 1: Theme

**Text overlay:** I tested 12 free AI tools. 5 replaced paid software in my workflow. Number 1
surprised me.

**Image prompt:** [Wide flat-lay of laptop, notebook, coffee on a wooden desk, soft warm afternoon
light from window at right. Phone camera framing, organic not studio quality, casual home office.
Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 2: #5

**Text overlay:** #5: Tool name. Replaced [paid tool, $X/mo]. Does the same thing for free if you
do not need [feature].

**Image prompt:** [Hero shot of laptop showing the tool's interface in screenshot or browser tab,
soft warm afternoon light. Phone camera framing, organic not studio quality. Clean negative space
in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 3: #4

**Text overlay:** #4: Tool name. Replaced [paid tool, $Y/mo]. Better for [specific use case].

**Image prompt:** [Same desk setup, slight angle change, laptop showing different tool's interface,
soft warm afternoon light. Phone camera framing, organic not studio quality. Clean negative space
in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 4: #3

**Text overlay:** #3: Tool name. Replaced [paid tool, $Z/mo]. The only one that handles
[specific complex task].

**Image prompt:** [Close-up of laptop showing the tool in action, hand visible at edge of frame.
Soft warm afternoon light. Realistic skin texture on visible hand. Phone camera framing, organic
not studio quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 5: #2

**Text overlay:** #2: Tool name. Replaced [paid tool, $W/mo]. Almost won the top spot. #1 is
free and you have probably never heard of it.

**Image prompt:** [Wide shot of desk with laptop, notebook with handwritten notes visible, soft
warm afternoon light. Phone camera framing, organic not studio quality. Clean negative space in
upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 6: #1 + CTA

**Text overlay:** #1: [Surprise tool name]. Free. Replaces [the most paid tool, $V/mo]. Comment
TOOLS and I will send you the full list with links.

**Image prompt:** [Hero close-up of laptop showing the surprise tool's interface, hand visible
hovering over keyboard. Soft warm afternoon light, natural shadows, late afternoon quality.
Realistic skin texture on visible hand. Phone camera framing, organic not studio quality. Clean
negative space in upper third for text overlay. 9:16 aspect ratio.]

---

After producing the slideshow, generate the 6 images using NB2:
01-theme.png, 02-rank5.png, 03-rank4.png, 04-rank3.png, 05-rank2.png, 06-rank1-cta.png
```

## Failure modes specific to Ranked List

### Items presented in normal order

If you present #1 first, the curiosity gap collapses. Always reveal #1 last. This is the whole mechanic of the format. Operators who push back ("but #1 should come first") are misunderstanding the format. The format exists because of the reverse-order reveal.

### #1 reveal is obvious from slide 1

If the audience can guess #1 from the theme statement, they have no reason to swipe. Hint at the surprise in slide 1 ("Number 1 surprised me", "#1 is free", "you have probably never heard of #1"). The slideshow promises a payoff. Deliver one.

### Items are too similar in quality

If 5 items are roughly the same usefulness, the ranking feels arbitrary. The audience reads the ranking as fake. Either find items with clearly different value, or shift the format to something else (a non-ranked list, a routine breakdown, a personal story).

### Items not actually ranked

If the slideshow lists items without any ordering logic, call it a list, not a ranking. Operators who title a slideshow "Top 5..." but list items in arbitrary order are confusing the format. Either rank the items or change the framing.

### The reasoning per slide is generic

"This tool is great" is not a reason. "Replaces [specific paid tool] for free if you do not need [specific advanced feature]" is. Each rank slide needs ONE specific differentiator that explains the position.

## The Claude prompt for spinning a fresh Ranked List slideshow

```
Write a TikTok Ranked List slideshow with 6 slides (theme + 5 ranked items, with item 1 last).

PERSONA: [Paste persona]

LIST THEME: [What is being ranked. Be specific. "Top 5 AI tools" is too broad; "Top 5 free AI
tools that replaced paid software in my newsletter workflow" is the right shape.]

CATEGORY OF ITEMS: [Tools, products, frameworks, routines, etc.]

5 ITEMS IN REVERSE ORDER (5, 4, 3, 2, 1):
- Item 5 (lowest): [Name] + [Brief reasoning for this rank]
- Item 4: [Name] + [Brief reasoning]
- Item 3: [Name] + [Brief reasoning]
- Item 2 (close to winning): [Name] + [Brief reasoning] + [Hint that #1 is surprising]
- Item 1 (the surprise): [Name] + [Why it wins decisively]

CTA: [Comment keyword for the full list with links, bio link, or save this.]

VISUAL AESTHETIC BASELINE: [Default for CC: warm interior, authentic phone selfie feel, soft
natural framing, organic not studio quality, casual home environment.]

For each slide, output:
1. Beat name (Theme / #5 / #4 / #3 / #2 / #1 + CTA)
2. Text overlay (the exact words appearing on the slide)
3. Image prompt (full prompt with scene direction, lighting clause, skin texture clause if face
   in frame, anti-polish language, aesthetic baseline, clean negative space for text overlay,
   9:16 aspect ratio)

Voice rules: coffee shop rule, no em-dashes, short sentences, simple words, specific numbers and
specific differentiators per item. CC voice: blunt, self-deprecating, no business jargon.
```

Run this. Voice-check. Generate images. Match audio. Route through humanizer and content-review before delivery.
