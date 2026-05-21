---
name: review-miner
description: |
  Mine customer language for emotive headlines, pain points, transformation stories, and social proof copy.
  Two pillars: (1) customer reviews (Amazon, Shopify, app store, post-purchase surveys) for solution-aware
  and product-aware language, and (2) Reddit threads for unaware and problem-aware language. The first feeds
  bottom/middle of funnel. The second feeds top of funnel.
  Outputs ready for direct injection into ad templates (ads-designer, ads-creative) and copywriting.
  Use when user asks to "mine reviews", "find ad copy from reviews", "extract testimonials",
  "Parker-style review mining", "find emotive language for ads", "mine Reddit for ICP", "Reddit pain
  point mining", "subreddit research for ads", "top-of-funnel customer language", or "unaware audience
  language extraction".
---

# Review Miner

Extract high-converting ad copy ingredients from customer reviews. Inspired by Parker AI Creative Director methodology -- find the exact words customers use, then inject them into ad templates.

## Why This Exists

The best ad copy comes from customers, not copywriters. Real reviews contain:
- Emotional language that resonates with other buyers
- Specific details that make claims credible
- Objections that were overcome (for bait-and-switch ads)
- Before/after transformations (for comparison ads)
- Social validation stories (for testimonial ads)

This skill extracts those raw materials and formats them for direct injection into the 40 ad templates in `ads-designer`.

## Input Sources

Accept reviews from any of these:

1. **Pasted review text** -- user copies reviews directly into chat
2. **Product URL** -- scrape reviews from the page (Amazon, Shopify, DTC sites)
3. **Social media comments** -- pasted or scraped comment threads
4. **App store reviews** -- pasted or scraped from App Store / Google Play
5. **CSV/spreadsheet** -- bulk review data
6. **Reddit threads** -- pasted post + comment text from category-relevant subreddits (see [`references/reddit-icp-mining.md`](references/reddit-icp-mining.md) for the workflow)

If the user provides a URL, use browser tools to navigate and extract reviews. If browser access is unavailable, ask the user to paste the reviews.

### Two pillars: reviews vs Reddit

- Customer reviews (Amazon, Shopify, app store, post-purchase surveys): the language of buyers. Product-aware and solution-aware. Best for middle and bottom of funnel.
- Reddit threads: the language of people who have not bought yet. Unaware and problem-aware. Best for top of funnel.

A complete creative system needs both pillars. The 6-category extraction below (Steps 1-6) applies to reviews. For Reddit-specific mining (subreddit selection, thread filtering, community dialect extraction, weak-signal flagging), see [`references/reddit-icp-mining.md`](references/reddit-icp-mining.md) and the ready-to-paste prompt at `skills/ads-creative/templates/reddit-icp-mining.md`.

## Workflow

### Step 1: Collect Reviews

Gather as many reviews as possible. Minimum 20 for useful output, 50+ is ideal.

For each review, capture:
- Full review text
- Star rating (if available)
- Reviewer name/initial (for attribution)
- Date (if available)
- Any photos or context

### Step 2: Analyze & Categorize

Read every review and extract language into six categories:

#### Category 1: Emotive Headlines
Single sentences or phrases with maximum emotional punch. These become ad headlines.

**What to look for:**
- Superlative statements ("best X I've ever used")
- Emotional reactions ("I literally cried when I saw the results")
- Unexpected outcomes ("my husband won't stop asking about it")
- Strong before/after contrasts in one sentence

**Output:** Top 10 ranked by emotional impact, each with:
- The exact quote
- Reviewer attribution (first name + last initial)
- Recommended ad templates: which of the 40 formats this fits best

#### Category 2: Pain Language
How customers describe the problem BEFORE the product. These become the "before" in comparison ads and the agitation in PAS copy.

**What to look for:**
- Descriptions of frustration, failure, wasted money
- Specific competitor callouts ("I tried X and it didn't work")
- Time/money wasted ("spent hundreds on products that did nothing")
- Physical/emotional symptoms described

**Output:** Top 5 pain statements with:
- The exact quote
- What it agitates (time, money, frustration, health, appearance)

#### Category 3: Transformation Language
Before/after descriptions. These become the core narrative for comparison and testimonial ads.

**What to look for:**
- Time-stamped results ("within 2 weeks", "after 3 months")
- Measurable outcomes ("lost 15 lbs", "saved 4 hours per week")
- Lifestyle changes ("I can finally wear shorts again")
- Identity shifts ("I feel like a new person")

**Output:** Top 5 transformation statements with:
- Before state (exact quote)
- After state (exact quote)
- Timeframe (if mentioned)

#### Category 4: Social Validation
Compliments received, partner reactions, peer comments. These are gold for social proof ads.

**What to look for:**
- Partner/spouse reactions ("my wife keeps saying I smell amazing")
- Colleague/friend comments ("everyone at work asks what I'm using")
- Stranger compliments ("got stopped on the street")
- Social media reactions ("posted a selfie and got 200 likes")

**Output:** Top 5 social validation quotes with:
- The exact quote
- Who gave the validation (partner, friend, stranger, online)

#### Category 5: Specificity Gold
Exact numbers, timeframes, details that make copy credible. These get injected into stat-based ad templates.

**What to look for:**
- Exact measurements ("down 2 pant sizes")
- Specific timeframes ("day 3 is when I noticed")
- Usage details ("I use it every morning with my coffee")
- Reorder frequency ("on my 5th box now")
- Comparison numbers ("half the price of what I was using")

**Output:** Top 5 specific details with:
- The exact quote
- What metric it supports (efficacy, value, convenience, taste)

#### Category 6: Objection Language
Doubts customers had BEFORE buying. These become the "bait" in negative marketing/bait-and-switch ads (Template #9) and objection-handling copy.

**What to look for:**
- "I was skeptical about..."
- "I almost didn't buy because..."
- "I thought it would be..."
- Price concerns mentioned then resolved
- Competitor loyalty that was broken

**Output:** Top 5 objection-to-conversion arcs with:
- The objection (exact quote)
- The resolution (exact quote)
- Best ad template match

### Step 3: Generate Output

Format the analysis into a structured document:

```markdown
# Review Mining Report: [BRAND / PRODUCT]

## Source
- [X] reviews from [SOURCE]
- Date range: [EARLIEST] to [LATEST]
- Average rating: [X.X] / 5

---

## Emotive Headlines (Top 10)

| # | Quote | Attribution | Best Templates |
|---|-------|------------|----------------|
| 1 | "[quote]" | [Name] | #1, #15, #21 |
| ... | | | |

## Pain Language (Top 5)

| # | Quote | Agitates |
|---|-------|----------|
| 1 | "[quote]" | [category] |

## Transformation Language (Top 5)

| # | Before | After | Timeframe |
|---|--------|-------|-----------|
| 1 | "[before]" | "[after]" | [time] |

## Social Validation (Top 5)

| # | Quote | Source |
|---|-------|--------|
| 1 | "[quote]" | [who] |

## Specificity Gold (Top 5)

| # | Detail | Supports |
|---|--------|----------|
| 1 | "[quote]" | [metric] |

## Objection Arcs (Top 5)

| # | Objection | Resolution | Best Template |
|---|-----------|------------|---------------|
| 1 | "[objection]" | "[resolution]" | #9 |

---

## Recommended Ad Combinations

Based on the strongest review language, here are the top 5 template + copy combinations to generate first:

1. **Template #[X]** -- [format name]
   - Headline: "[mined quote]"
   - Supporting copy: "[mined detail]"
   - Why: [rationale]

2. ...
```

### Step 4: Generate Ad-Ready Phrases

Take the strongest raw quotes from Categories 1-6 and polish them into headline-length, platform-compliant phrases. These are ready to paste into ad templates without editing.

```markdown
## Ad-Ready Phrases (Top 10)

| # | Phrase | Source Quote | Char Count | Best Template Slots |
|---|--------|-------------|------------|-------------------|
| 1 | "[polished phrase]" | "[original quote]" | [count] | [YOUR HEADLINE], [STAT] |
| 2 | | | | |
```

**Rules for polishing:**
- Keep the customer's voice -- don't make it sound like a copywriter
- Trim to headline length (under 80 chars for most ad templates)
- Fix grammar only if it blocks comprehension
- Preserve emotional words and specific numbers
- Map each phrase to specific `ads-designer` template slots it fits

### Step 5: Build Transformation Stories

Combine before/after quotes, timeframes, and context from Categories 2-3 into ready-to-paste narrative arcs. These go directly into testimonial ads, advertorial copy, and email sequences.

```markdown
## Transformation Stories (Top 3)

### Story 1: "[Reviewer Name]"
**Before:** "[1-2 sentences combining their pain state, in their words]"
**Turning point:** "[what made them try the product / moment of decision]"
**After:** "[1-2 sentences combining their transformation, in their words]"
**Timeline:** [timeframe from before to after]
**Best use:** [testimonial ad / advertorial section / email proof block / UGC script seed]

### Story 2: "[Reviewer Name]"
[same structure]

### Story 3: "[Reviewer Name]"
[same structure]
```

**Rules for stories:**
- Use only real quotes -- attribute everything
- Each story must have a clear before/after arc (not just "I love it")
- Include timeline when available -- specificity = credibility
- Flag which stories have UGC potential (reviewer seems articulate + passionate)
- Stories with objection-to-conversion arcs are highest priority

### Step 6: Deliver

1. Save report to `private project review-mining/{brand}-reviews.md`
2. Present summary to user with top 3 recommended ad combinations
3. Offer to feed results directly into `ads-designer` batch mode

## Integration

### With ads-designer (batch mode)
The review mining report can be used as input for batch prompt generation:
- Emotive headlines fill [YOUR HEADLINE] slots
- Pain language fills [WEAKNESS] and [BEFORE STATE] slots
- Transformation language fills [AFTER STATE] slots
- Social validation fills [FULL QUOTE] and [REVIEW TEXT] slots
- Specificity gold fills [STAT] slots
- Objection arcs fill [BAIT] slots for Template #9

### With copy-writing
Mined language serves as raw material for:
- Landing page headlines (from emotive headlines)
- Objection handling sections (from objection arcs)
- Social proof sections (from social validation)
- Feature/benefit copy (from specificity gold)

### With ads-creative
Compare mined language to competitor ad copy to find:
- Angles competitors aren't using
- Language that resonates but isn't being leveraged
- Unique selling points hiding in reviews

For the integrated Meta-specific 5-phase creative workflow that consumes the output of this skill, see `skills/ads-creative/references/meta-ads-master-workflow.md`. Phase 1 of that workflow uses both pillars of this skill (reviews + Reddit) to seed the customer language library that feeds everything downstream.

The ready-to-paste prompts for both pillars live in `skills/ads-creative/templates/`:
- `customer-review-extraction.md`: the deeper 5-section angle extraction from reviews
- `reddit-icp-mining.md`: the 5-section pain map from Reddit threads

## Tips

- **5-star reviews** are best for testimonial/social proof copy
- **3-star reviews** often have the most specific, balanced language
- **1-star competitor reviews** are gold for us-vs-them comparisons
- **Repeat phrases** across multiple reviews signal strong patterns
- **Unusual metaphors** from real customers outperform copywriter-crafted lines
- **Questions in reviews** ("why didn't I find this sooner?") make great hooks
