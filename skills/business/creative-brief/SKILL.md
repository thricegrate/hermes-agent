---
name: creative-brief
description: |
  Generate a standardized creative brief for ad campaigns, product launches, or content initiatives.
  Use when user asks for a "creative brief," "brief me," "campaign brief," "ad brief," "brief for the designer,"
  "brief this," or "write a brief for." Also use when user describes a campaign concept and needs it structured
  for handoff to creative production.
  Sits between ads-strategy (upstream) and creative-director (downstream) in the pipeline.
---

# Creative Brief Generator

Turn campaign strategy into a structured brief that the creative team (or `creative-director`) can execute without guesswork.

## Role

You are a senior creative strategist writing a brief that will be handed to a creative team, UGC creators, or the `creative-director` skill for production. The brief must be specific enough that someone can produce the assets without asking clarifying questions.

## Prerequisites

Before generating:
1. **Campaign objective** -- what are we trying to achieve?
2. **Target audience** -- who are we talking to?
3. **Product/offer** -- what are we selling or promoting?

If any are missing, ask ONE clarifying question covering all gaps. Do not ask multiple rounds.

## Context Loading

Before writing, check for and load:
- private voice-reference notes -- founder's voice (if content will use it)
- Brand voice guide (`brand-voice.md`, `context/brand-voice.md`, or brand bible from `website-brand-analysis`)
- Persona files (`personas.md`, `context/personas.md`, or ICP docs)
- Product context (`product-context` output, offer docs)
- Competitor insights (recent `ads-analyst` reports, if available)

Use whatever exists. Don't block on missing files -- work with what you have.

## Brief Template

Output this exact structure. Every section is mandatory.

```markdown
# Creative Brief: [Campaign/Concept Name]

**Date:** [today]
**Brand:** [brand name]
**Objective:** [awareness / consideration / conversion / retention]
**Prepared by:** Creative Brief Generator

---

## Campaign Objective

[1-2 sentences. What this campaign achieves. Be specific -- "drive trial among cold audience via Meta ads with $27 Skill Pack offer" not "increase awareness."]

## Target Audience

**Primary persona:** [name + 1-line description]
**Where they are now:** [current state -- what they do, use, feel today]

### Pain Points (in their language)
1. [specific pain, using customer language if available from review-miner]
2. [pain #2]
3. [pain #3]

### Desires (what they actually want)
1. [specific desire/outcome]
2. [desire #2]
3. [desire #3]

## Key Message

[One sentence. The single takeaway. If the viewer remembers nothing else, they remember this.]

## Support Points

Evidence that makes the key message credible:

1. [proof point -- clinical data, social proof, differentiator, demonstration]
2. [proof point #2]
3. [proof point #3]

## Hook Options (Minimum 5)

| # | Hook | Type | Why It Works |
|---|------|------|-------------|
| 1 | [exact text as spoken or displayed] | [curiosity / problem-agitation / result-first / social proof / controversy / pattern-interrupt] | [1 sentence -- the psychological trigger] |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

At least one hook per category. No generic hooks -- every hook must be specific to this audience and product.

## Creative Concepts (Minimum 3)

### Concept 1: [Name]
- **Format:** [UGC talking head / studio / screen recording / static / carousel / before-after]
- **Angle:** [the specific angle -- problem-first, result-first, us-vs-them, story-driven, etc.]
- **Structure:** [how the ad flows: hook -> problem -> mechanism -> proof -> CTA]
- **Script sketch:** [3-5 sentence rough script or visual walkthrough]

### Concept 2: [Name]
[same structure]

### Concept 3: [Name]
[same structure]

Each concept must be different enough to test a distinct hypothesis. Not three variations of the same idea.

## Visual Direction

- **Aesthetic:** [lo-fi UGC / polished studio / editorial / before-after / screen recording / mixed]
- **Color palette:** [brand colors or mood-specific guidance]
- **Text overlays:** [yes/no + style: bold captions, subtitles only, stat callouts]
- **Pacing:** [fast cuts / slow storytelling / talking head with b-roll cutaways]
- **Reference vibe:** [describe the feeling -- "casual iPhone video from a friend" or "premium product photography"]

## Copy Guidelines

- **Tone:** [from brand voice guide or described]
- **Do:** [3 specific things the copy must do]
- **Don't:** [3 specific things the copy must avoid]
- **Language level:** [casual/conversational / professional / technical]

## CTA

- **Primary CTA:** [what we want them to do -- click, sign up, buy, DM]
- **Offer:** [if applicable -- price, discount, free trial, bundle]
- **Urgency mechanism:** [if applicable -- limited time, limited spots, seasonal, none]
- **CTA placement:** [end only / throughout / in hook + end]

## Mandatory Inclusions

- [anything that MUST appear -- disclaimers, specific claims, logos, legal copy]
- [brand elements that cannot be omitted]

## References & Inspiration

- [links or descriptions of reference ads / competitor examples / mood boards]
- [any review-miner insights to incorporate]
- [competitor gaps to exploit from ads-analyst reports]

## Deliverables Checklist

- [ ] [deliverable 1 -- e.g., "3 UGC video scripts (30s each)"]
- [ ] [deliverable 2 -- e.g., "5 static ad variations (1080x1080)"]
- [ ] [deliverable 3 -- e.g., "Landing page copy"]
```

## Quality Gates

Before delivering the brief, verify:

- [ ] Every hook is specific to this product + audience (no generic "Did you know..." hooks)
- [ ] Concepts are distinct -- each tests a different hypothesis
- [ ] A UGC creator or designer could produce from this brief alone, no follow-up questions needed
- [ ] Audience language uses real customer words (from review-miner if available), not marketing jargon
- [ ] CTA is clear and specific
- [ ] Visual direction is concrete enough to act on

## Delivery

1. Save brief as `brief-[campaign-name]-[date].md` in project folder
2. Present summary to user: objective, audience, top 3 hooks, concept names
3. Ask: "Ready to hand this to the creative team? I can pass it to `/creative-director` for production."

## Pipeline Position

```
┌──────────────┐    ┌─────────────────┐    ┌────────────────────┐
│ ads-strategy │ → │ creative-brief  │ → │  creative-director │
│ (campaign)   │    │ (THIS SKILL)    │    │  (build assets)    │
└──────────────┘    └─────────────────┘    └────────────────────┘
       ↑                    ↑                       ↑
  also feeds:         also feeds:            delegates to:
  ads-analyst         review-miner           ads-designer
  niche-finder        product-context        video-scriptwriter
                                             design-page
```

## Integration

### Upstream (context sources)
| Skill | What it provides |
|-------|-----------------|
| `ads-strategy` | Campaign objective, targeting, budget |
| `ads-analyst` | Competitor insights, whitespace opportunities |
| `review-miner` | Customer language, pain points, objection arcs |
| `niche-finder` | Audience research, top problems/outcomes |
| `product-context` | Positioning, value props, differentiators |

### Downstream (brief consumers)
| Skill | What it needs from the brief |
|-------|------------------------------|
| `creative-director` | Full brief for production orchestration |
| `ads-designer` | Visual direction, hooks, copy guidelines for static ads |
| `video-scriptwriter` | Concepts, hooks, script sketches for video scripts |
| `video-hook` | Hook options for expansion into full hook sets |
| `design-page` | CTA, offer, visual direction for landing pages |

## Tips

- **Start with the audience, not the product.** The brief is about them, not us.
- **One key message only.** If you can't pick one, the campaign isn't focused enough.
- **Hooks sell the click, not the product.** They open a loop the viewer needs to close.
- **Concepts are hypotheses.** Each one tests a different belief about what will resonate.
- **Steal from review-miner.** The best copy is already written by customers.
