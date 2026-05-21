---
name: content-review
description: |
  Use when content needs analysis, scoring, critique, or quality review before publishing. Combines
  deep stylistic analysis (10 dimensions) with North Star scoring (7 criteria) into a single review
  pass. Also triggers on: "content analyst", "content critic", "analyze article", "analyze post",
  "analyze newsletter", "analyze email", "copywriting analysis", "style analysis", "content review",
  "content audit", "writing analysis", "editorial analysis", "how good is this article", "review this
  copy", "score this writing", "score this", "evaluate this post", "content quality check", "review
  this content". MUST be run on every piece of content before it ships (per CLAUDE.md). For fixing
  issues found, see copy-editing. For de-AI-ing text, see humanizer. For narrative structure, see
  storyteller.
metadata:
  version: 1.0.0
  tags: copywriting, analysis, editing, style, scoring, quality-gate
---

# Content Review

Single-pass content evaluation that combines deep stylistic analysis with North Star alignment scoring. Every piece of content gets both a craft assessment and a publication-readiness score.

This skill serves two purposes:
1. **Stylistic analysis** -- 10-dimension copywriting evaluation based on Gary Halbert, Bond Halbert, and Eddie Shleyner principles
2. **North Star scoring** -- 7-criteria evaluation against the North Star priority (Automatic Publication of Engaging AI-Related Content)

Both run in one pass. One report. No separate calls needed.

## When to Trigger

- Any content is created, drafted, or ready for review
- User shares a post, article, video script, infographic, or any content piece
- User asks to evaluate, score, or critique content
- Before any content is published or scheduled
- During content audits or batch reviews
- User says "analyze", "review", "score", "critique", or "how good is this"

## Workflow

### Step 1: Get the Content

Ask the user for:
- A URL to fetch, OR pasted text

If URL: use WebFetch or appropriate tool to extract the full article text.

### Step 2: Gather Context for North Star Scoring

Ask the user (do not guess):
- "How many minutes did you personally spend on this?" (for Automatic score)
- "What's the publication status?" (for Published score)
- "Is this already published? If yes, send a screenshot with engagement metrics." (for Engaging score)
- "Where is/will this be published?" (for Distribution score)

### Step 3: Extract and Note Metadata

Preserve formatting (headings, bullets, bold, links). Note word count, author, title, publication date if available.

### Step 4: Run the Combined Analysis

Work through both scoring systems systematically. For the stylistic dimensions, find 2-3 specific examples from the text (quote directly), note strengths and weaknesses, and assign scores.

---

## Part 1: Stylistic Analysis (10 Dimensions)

Each dimension scored 1-10. See [references/copywriting-principles.md](references/copywriting-principles.md) for the full principle reference and [references/banned-patterns.md](references/banned-patterns.md) for anti-patterns.

### 1. Punctuation
Comma splices, missing colons, inconsistent semicolons, over-reliance on one style, missing dramatic punctuation (dashes, colons, question marks in body text).

**Good:** Varied punctuation that serves rhythm. Colons before explanations. Dashes for emphasis. Zero comma splices.
**Bad:** Every sentence ends with a period. Academic feel.
**Principle:** Punctuation is a rhythm instrument, not just grammar (Gary Halbert).

### 2. Sentence Rhythm
Long/short alternation, punch lines after long build-ups, flat zones where every sentence is the same length.

**Good:** Long sentence unfolds an idea (18-25 words). Then a short one hits. Hard. Three to five words.
**Bad:** Every sentence 15-20 words. No variation. Monotone reading experience.
**Principle:** "Write like you speak. Vary the length." (Gary Halbert). Bond Halbert's "complete sentences, incomplete thoughts."

### 3. Transitions
Bucket brigades vs weak connectors. Flow between paragraphs.

**Good:** "But here's the thing." "Now." "Look." Natural conversational bridges.
**Bad:** "Furthermore," "Moreover," "Additionally," "In conclusion." Academic, stiff.
**Principle:** Gary Halbert's bucket brigades. See [references/banned-patterns.md](references/banned-patterns.md) for weak transitions.

### 4. Filler / Water
Unnecessary phrases, redundant qualifiers, throat-clearing intros, hedge words.

**Good:** Every sentence earns its place. Lean, compressed, purposeful.
**Bad:** "I think it's important to note that..." "In today's rapidly evolving landscape..."
**Principle:** Eddie Shleyner's necessity test: "If I remove this sentence, does the piece suffer? If not, kill it."

### 5. Vocabulary
Syllable economy, strong verbs vs adverb + weak verb combos, jargon level, word precision.

**Good:** "Sprinted" not "quickly ran." "Slashed" not "significantly reduced."
**Bad:** "Utilize" instead of "use." "In order to" instead of "to."
**Principle:** Eddie Shleyner's fewer syllables test. Hemingway: use short words. Gary Halbert: cut "-ly" words.

### 6. Eye Relief
Paragraph length, white space, subheading frequency, visual scanability.

**Good:** 1-3 sentences per paragraph. Subheadings every 200-300 words. Bold for key terms.
**Bad:** Paragraphs of 6+ sentences. Walls of text. No visual anchors.
**Principle:** Bond Halbert: wide margins, short paragraphs, double spacing, subheadings.

### 7. Voice / Personality
Author presence, tone consistency, brand match, distinctiveness. Coffee shop naturalness.

**Good:** Consistent tone. Author's personality shows. Opinions stated directly. Reads like a conversation with a friend.
**Bad:** Generic "helpful assistant" tone. No personality. Interchangeable with any other writer. Sounds like a presentation instead of a conversation.
**Principle:** Gary Halbert: write as if writing a letter to a friend. The Coffee Shop Rule: if it sounds weird said to a friend across a table, rewrite it.

### 8. Specificity
Numbers, names, examples, before/after demonstrations, sensory details.

**Good:** "$47,000 in 3 months" not "significant revenue." "Sarah, a freelance designer in Portland" not "one user."
**Bad:** "Many people find this useful." "It can significantly improve results."
**Principle:** Gary Halbert: sensory details create intimacy. Eddie Shleyner: specificity is persuasion.

### 9. Slippery Slide
Does each sentence compel reading the next? "Incomplete thoughts" that pull forward? Momentum throughout?

**Good:** You can't stop reading. Each paragraph ends with a hook. "But that's only half the story."
**Bad:** Natural stopping points every 2-3 paragraphs. Conclusions mid-article.
**Principle:** Joe Sugarman's concept: every element exists solely to get the reader to read the next line.

### 10. Clean Windows
Is the writing transparent or self-admiring?

**Good:** You notice the idea, not the writing. Simple words, clear structure. Writer serves the reader.
**Bad:** "Paradigm-shifting synergistic solutions." Purple prose. Writer is performing, not communicating.
**Principle:** Eddie Shleyner: "Clean windows. You don't notice a clean window. You see through it."

### Stylistic Scoring Guide

| Score | Label | Description |
|-------|-------|-------------|
| 1-3 | Weak | Systematic problems. Multiple violations per paragraph. Needs full rewrite. |
| 4-6 | Average | Some good instincts, inconsistent. Problems every few paragraphs. |
| 7-8 | Strong | Mostly solid. Occasional lapses. Professional quality. |
| 9-10 | Excellent | Masterful. Could be a teaching example. Reserve 10 for exceptional craft. |

A 5 is "competent but unremarkable." A 7 is "noticeably good." A 9 requires zero fixes needed.

---

## Part 2: North Star Scoring (7 Criteria)

Each criterion scored 1-10. Final North Star score = average of all 7.

### 1. AUTOMATIC (1-10)
How much human time did this content require?

- **10**: 0-5 min (AI did everything, quick glance/approve)
- **9**: 6-10 min (minor review, small tweak)
- **8**: 11-15 min (light editing)
- **7**: 16-20 min (moderate edits)
- **6**: 21-25 min (significant editing)
- **5**: 26-30 min (heavy editing, half manual)
- **4**: 31-35 min | **3**: 36-40 min | **2**: 41-50 min | **1**: 50+ min

Goal: 9+. If below 8, ask: "What part took the most time? Can we automate that step?"

### 2. PUBLISHED (1-10)
- **10**: Published and live | **7**: Scheduled | **5**: Ready/final draft | **3**: In progress | **1**: Just an idea

Goal: Nothing stays below 7 for more than 24 hours.

### 3. ENGAGING (1-10)

**If published:** Score by total engagements (likes + saves + reposts + comments). 100+ = 10, 80-99 = 9, 60-79 = 8, 40-59 = 7, 25-39 = 6, 15-24 = 5, 10-14 = 4, 5-9 = 3, 2-4 = 2, 0-1 = 1.

**If not yet published:** Predict engagement potential by evaluating:
- **Hook power**: Will someone stop scrolling? Escalating action verbs or quantified knowledge gaps.
- **Emotional trigger**: Curiosity, surprise, FOMO, excitement, outrage, pride.
- **Call-to-action**: Clear CTA. Implicit via deliverable ("Drop BUILD in the comments") outperforms "like if you agree."
- **Save-worthy**: Cheatsheets, frameworks, reference infographics get saved most. No save-worthy element = score -2.
- **Repost potential**: Named frameworks are more shareable.
- **Comment bait**: Invites opinions, reactions, discussion.
- **Post + Visual combo**: Infographic/cheatsheet attached? Posts with visuals that create "desire + delivery" loop score higher. No visual on LinkedIn = flag as improvement opportunity.

Prediction: 9-10 viral potential, 7-8 strong, 5-6 decent but forgettable, 3-4 scroll-past, 1-2 zero engagement expected.

> **Engagement Prediction:** Before scoring, check the content against proven virality patterns and flop signals in `references/adrian-engagement-prediction.md`. Content matching viral patterns (specific numbers, controversy, before/after) averages 250-340k views. Content matching flop patterns (generic, no hook, too polished) averages 2-5k views.

### 4. AI-RELATED (1-10)
- **9-10**: Core AI content | **7-8**: AI-adjacent | **5-6**: Tangentially related | **3-4**: Loosely connected | **1-2**: Not AI-related

### 5. DISTRIBUTION REACH (1-10)
1 point per platform: Email newsletter, YouTube, Instagram Reel, Facebook, TikTok, LinkedIn post, LinkedIn carousel, Twitter/X post, Twitter/X thread, Twitter/X article. 10 platforms = 10.

Goal: Every piece should hit 5+ platforms.

### 6. HUMAN-PASSING (1-10)

Scan for these AI tells (the 26 AI pattern detection):

**Hard fails (instant -3 each):**
- Em dashes or hyphens used as clause connectors
- Semicolons anywhere
- Excessive quotation marks (air-quoting concepts)
- Words: delve, furthermore, moreover, additionally, tapestry, landscape (abstract), testament, underscore, pivotal, crucial

**Medium fails (-2 each):**
- Rule of three lists ("innovation, inspiration, and insights")
- Negative parallelisms ("not just X, it's Y")
- Staccato same-length sentences (metronome rhythm)
- Promotional language (vibrant, nestled, breathtaking, groundbreaking)
- Generic positive conclusions ("the future looks bright")
- Fake personal anecdotes without specific names/dates/numbers
- Boldface overuse or inline-header lists
- Vague claims ("experts say", "highly effective", "proven results")
- Points without paint: educational points explained only in abstract terms with no analogy, metaphor, story, or example
- Presentation tone: reads like a lecture instead of a conversation (fails coffee shop test)

**Emotional hook fails (-2 each):**
- Opening line triggers no identifiable emotion (flat, informational start)
- No target emotion identifiable in the first 2 sentences
- Hook reads like a Wikipedia summary instead of a gut reaction

**Soft fails (-1 each):**
- No deliberate imperfections at all (too clean = suspicious)
- No filler words or casual language where medium allows it
- Perfect grammar throughout (no contractions, no sentence fragments)
- Round numbers only (no over-specific details)
- Title Case In Every Heading
- Emojis decorating headers or bullet points
- Arrow (→) used more than once per post/section (arrow obsession is an AI formatting tell)
- More than 1 exclamation point in non-social content (AI over-exclaims)
- Social post starts with "I" (AI default opener; lead with the insight, not the author)

Scoring: 9-10 undetectable, 7-8 mostly clean, 5-6 suspicious (needs humanizer), 3-4 obviously AI, 1-2 pure slop.

Goal: 7+ minimum. Below 5 = run through `humanizer`. Below 3 = rewrite from scratch.

### 7. NOVELTY & PERSONAL STORY (1-10)

**Novelty check:** What's the consensus message? Does this contradict, reframe, or add to it? Would a reader who's seen 3 pieces on this topic think "I haven't heard this before"?

**Personal story check:** Real personal story with specific details? Claims backed by proof? Lived experience vs recited information?

- **9-10**: Genuinely novel angle + rich personal story with proof
- **7-8**: Has distinct angle OR personal story, but not both at full strength
- **5-6**: Some differentiation, mostly repeats consensus. Vague personal stories
- **3-4**: Consensus content. No proof, no personal stories
- **1-2**: Pure AI slop. Zero personal touch

Goal: 7+. Below 5 = rethink the angle and ask for personal experience/proof.

---

## Part 3: Imperfection Guardrails (Pre-Publish Gate)

After humanizer runs, this checks deliberate imperfections stay within safe limits. Hard pass/fail gate.

**The golden ratio: 1 deliberate imperfection per 3 paragraphs (~100 words).**

**FAIL conditions (block publishing):**
- More than 2 imperfections in any single paragraph
- 2 imperfections in the same sentence
- More than 6 total imperfections per 500 words
- Typo in a person's name, number, URL, product name, or technical term
- 3+ skipped apostrophes in a row
- More than 1 full lowercase sentence start per 500 words (except social media)
- Filler words ("like", "honestly", "I mean") more than 2x per 500 words in newsletters/blogs
- Same type of imperfection used twice (every deliberate mistake must be a different type)

**WARN conditions (flag but allow):**
- Zero imperfections in 500+ words (too clean, might get flagged as AI)
- All imperfections the same type
- Imperfections clustered instead of spread evenly

**Check method:** Count imperfections, count paragraphs, verify ratio near 1:3. Below 1:5 = too clean. Above 1:2 = too messy.

---

## Lead Magnet Quality Check (Optional Section)

Use this when reviewing lead magnet content specifically (PDFs, cheat sheets, template packs, prompt libraries, free tools). Skip for regular articles/posts/emails.

### 5 Quality Criteria (Y/N)

1. **Pre-validated idea?** Is this based on proven content (top-performing post expanded, course compressed, competitor success replicated, paid offer unbundled) -- or a cold guess? Cold guesses have much lower success rates. See `free-tool-strategy` for the 4 ideation approaches.

2. **Compelling name?** Does it follow the [Desired Outcome] + [Topic] + [Container Word] formula? "The 6-Figure Newsletter Starter Pack" beats "Free PDF Guide." Generic format words alone (PDF, Guide, Checklist) are a red flag.

3. **Would they pay $20-50?** Is the perceived value high enough that giving an email feels like a bargain? Templates, prompts, step-by-step breakdowns, and checklists carry higher perceived value than general advice.

4. **Complete solution to narrow problem?** Does it solve one specific thing fully, not give a vague overview of many things? Hormozi's test: "a complete solution to a narrow problem." If it tries to cover everything, it covers nothing well.

5. **Natural path to paid offer?** After consuming this, is the reader more likely to want your product? The lead magnet should solve a prerequisite problem -- a step they need to take BEFORE they're ready for your main offer.

### Scoring

- 5/5 Y: Strong lead magnet. Ship it.
- 3-4/5 Y: Fix the gaps before launch. Each "N" is a specific risk.
- 0-2/5 Y: Rethink the concept. The idea or packaging needs work before building.

---

## Analysis Rules

1. **Quote directly.** Every claim must reference a specific passage. No vague "the writing tends to..."
2. **Be specific about fixes.** "Improve rhythm" is useless. "Split this 28-word sentence after 'results' and make the second half a 5-word punch" is useful.
3. **Prioritize impact.** Some dimensions matter more for certain content types.
4. **Compare to principles.** Reference Gary/Bond/Eddie by name when their specific technique applies.
5. **Before/after rewrites must be realistic.** Show how the same author could improve with minimal changes.
6. **Check for banned patterns.** Cross-reference against [references/banned-patterns.md](references/banned-patterns.md). Includes slop words, slop phrases, filler phrases, weak transitions, bloated constructions, and AI slop markers.
7. **Be brutally honest.** Low scores are good feedback, not failure.
8. If Automatic < 5, ALWAYS suggest automation. If Distribution < 5, ALWAYS list platforms to add. If Engaging < 7, ALWAYS suggest hook/CTA/shareability improvements. If Human-Passing < 7, ALWAYS flag AI tells and recommend `humanizer`. If Novelty < 5, ALWAYS ask for personal experience/proof and suggest contrarian angle.

---

## Output Format

Every report must include ALL of the following sections:

```
# Content Review Report

## Metadata

**Title:** [title]
**Author:** [author or "Unknown"]
**Source:** [URL or "pasted text"]
**Date:** [publication date or "N/A"]
**Word count:** [number]
**Content type:** [article / blog post / newsletter / social post / email / other]

---

## Stylistic Analysis (10 Dimensions)

| # | Dimension | Score (1-10) | Key Finding |
|---|-----------|:------------:|-------------|
| 1 | Punctuation | | |
| 2 | Sentence rhythm | | |
| 3 | Transitions | | |
| 4 | Filler / water | | |
| 5 | Vocabulary | | |
| 6 | Eye relief | | |
| 7 | Voice / personality | | |
| 8 | Specificity | | |
| 9 | Slippery slide | | |
| 10 | Clean windows | | |
| | **Stylistic Average** | **[avg]** | |

---

## North Star Scoring (7 Criteria)

1. Automatic: X/10 -- [one-line reason]
2. Published: X/10 -- [status]
3. Engaging: X/10 -- [one-line reason]
4. AI-Related: X/10 -- [one-line reason]
5. Distribution: X/10 -- [X platforms: list them]
6. Human-Passing: X/10 -- [AI tells found, or "clean"]
7. Novelty & Personal Story: X/10 -- [consensus broken? personal story? proof?]

### NORTH STAR AVERAGE: X.X/10

### North Star Verdict
[One of:]
- 8-10: SHIP IT. North Star aligned.
- 6-7.9: GOOD but improve [weakest criteria]. Fix and ship.
- 4-5.9: NEEDS WORK. [Specific fixes needed.]
- Below 4: KILL IT or RETHINK. Not worth publishing as-is.

---

## Top 3 Strengths

### 1. [Dimension name]
> "[Direct quote from the text]"
[Why this works and which principle it exemplifies.]

### 2. [Dimension name]
> "[Direct quote]"
[Why this works.]

### 3. [Dimension name]
> "[Direct quote]"
[Why this works.]

---

## Top 3 Weaknesses (with rewrites)

### 1. [Dimension name] (Score: [X]/10)
**Original:**
> "[Direct quote of the problematic passage]"
**Rewrite:**
> "[Improved version]"
**What changed:** [Specific technique applied and why it's stronger.]

### 2. [Dimension name] (Score: [X]/10)
**Original:** > "[Direct quote]"
**Rewrite:** > "[Improved version]"
**What changed:** [Explanation.]

### 3. [Dimension name] (Score: [X]/10)
**Original:** > "[Direct quote]"
**Rewrite:** > "[Improved version]"
**What changed:** [Explanation.]

---

## Speaker Delivery Check (video/script content only)

Source: "Give me 7 minutes, I'll change the way you speak on YouTube" (2025). Five delivery rules that apply to all on-camera content.

- [ ] **Coffee Shop Rule:** Does every line sound natural said to a friend over coffee? Flag any lines that sound like a presentation or performance. Y/N
- [ ] **Connect vs Perfect:** Is the script written for connection (conversational, personal) or perfection (stiff, impressive-sounding)? Y/N
- [ ] **Emotional Clarity:** Is the target feeling defined? Does the script consistently transmit ONE clear emotion throughout? Y/N -- Target feeling: ___
- [ ] **Points + Paint:** Does every major educational point have an analogy, metaphor, story, or example? Count: ___ points, ___ painted. Y/N
- [ ] **Warm-up Note:** Is there a warm-up reminder in the production plan? Y/N

Delivery score: X/5 rules present. Missing: [list]
Fix: [specific recommendation for worst violation]

**Coffee Shop Rule also applies to written content (newsletters, social, email).** If reviewing non-video content, still check: does this read like a conversation or a presentation? Flag any paragraph that sounds performative.

## Speaker Delivery Check (video/script content only)
- [ ] Coffee Shop Rule: Lines sound natural said to a friend? Y/N
- [ ] Connect vs Perfect: Written for connection, not impression? Y/N
- [ ] Emotional Clarity: Target feeling defined and consistent? Y/N -- Feeling: ___
- [ ] Points + Paint: Major points have analogy/metaphor/story/example? ___ of ___ painted. Y/N
- [ ] Warm-up Note: Production plan includes warm-up reminder? Y/N
- Delivery score: X/5. Missing: [list]
- Fix: [specific recommendation]

## Coffee Shop Check (ALL content types)
- Does this read like a conversation or a presentation? [conversation/presentation]
- Flag lines that sound performative: [list or "none"]
- Points without paint: [count, or "all painted"]

## Creator Video Framework Check (video/script content only)
- [ ] Act 1 HOOK: Big promise + open loop + teases payoff? Y/N
- [ ] Act 2 BRAG: Credentials + proof within first 15%? Y/N
- [ ] Act 3 VALUE BOMB: 50%+ of value delivered before integration? Y/N
- [ ] Act 4 INTEGRATION: CTA/sponsor feels natural, not jarring? Y/N
- [ ] Act 5 PAYOFF: Delivers the teased thing + emotional surprise? Y/N
- [ ] South Park rule: Story uses "but/therefore", NOT "and then"? Y/N
- Framework score: X/6 acts present. Missing: [list]
- Fix: [specific recommendation]

## Storytelling Retention Check (ALL content types)
Rate each technique (Y/partial/N). Not all apply to every piece, but flag missed opportunities:
- [ ] Oscillation: Emotion goes up AND down? (flat = boring)
- [ ] Near-Miss: Almost-wins before the real win? (straight success = unearned)
- [ ] Vulnerability Before Victory: Lowest point shown before breakthrough?
- [ ] Expectation Subversion: Ending delivers something DEEPER than promised?
- [ ] South Park "but/therefore": NOT "and then"?
- [ ] Escalating Stakes: Each section raises what's at risk?
- [ ] Triple Hook: Opening has 2-3 layered hooks?
- [ ] Show-Don't-Tell: Story PROVES the point vs just stating it?
- [ ] Reframe Close: Ending reframes what the content was really about?
- [ ] Recurring Character: Person/example appears multiple times with payoff?
- [ ] Full-Circle Callback: Returns to opening state before resolution?
- [ ] Hidden Thesis: Real message discovered by audience before stated?
- [ ] Controlled Disaster: Scene set up where audience KNOWS it will fail?
- [ ] Vulnerability Break: One raw, unperformative moment?
- [ ] Cross-Dimensional Escalation: Stakes across types (physical/social/emotional/financial)?
- [ ] Comedic Anchors: Running gags or callbacks as breathers?
- [ ] Question Framework: Framed around ONE driving question?
- [ ] Naming the Abstract: Concepts given names/personality?
- Retention score: X/18 techniques used (score only applicable ones)
- Biggest missed opportunity: [which technique would improve this piece most]

## Imperfection Guardrails
Imperfection dose: X in Y paragraphs (ratio 1:Z) -- PASS/FAIL/WARN

## Lead Magnet Quality Check (if reviewing a lead magnet)
- [ ] Pre-validated idea? (Expand/Compress/Replicate/Unbundle) Y/N
- [ ] Compelling name? ([Outcome] + [Topic] + [Container Word]) Y/N
- [ ] Would they pay $20-50? Y/N
- [ ] Complete solution to narrow problem? Y/N
- [ ] Natural path to paid offer? Y/N
- Lead magnet score: X/5. Fix: [weakest criterion]

## How to Improve
- [Bullet: specific fix for weakest stylistic dimension]
- [Bullet: specific fix for weakest North Star criterion]
- [Bullet: second weakest area fix]
- [Bullet: automation opportunity if Automatic < 7]
- [Bullet: Creator Video Framework fix if any act missing (video only)]
- [Bullet: storytelling retention technique to add (if retention score < 5/18 applicable)]
```

---

## Batch Mode

When reviewing multiple content pieces, produce individual reports plus a summary:

```
## Content Batch Summary

- "Title 1" -- NS: 8.5/10 (A:9 P:10 Eng:8 AI:9 D:6 H:9 N:8) | Style: 7.2/10
- "Title 2" -- NS: 6.0/10 (A:5 P:7 Eng:6 AI:8 D:5 H:5 N:6) | Style: 5.8/10
- "Title 3" -- NS: 3.5/10 (A:2 P:3 Eng:4 AI:7 D:2 H:3 N:3) | Style: 4.1/10 << NEEDS WORK

**Batch North Star average: X.X/10**
**Batch stylistic average: X.X/10**
**Weakest criteria across batch: [criteria]**
**Action: [what to fix first]**
```

---

## Related Skills

| Skill | When to route |
|-------|---------------|
| `copy-editing` | User wants to fix the issues found (7-pass editing) |
| `humanizer` | Text has AI patterns that need removal |
| `storyteller` | Narrative structure needs work (story arcs, hooks) |
| `copy-writing` | User wants to write new copy, not analyze existing |
| `content-social` | User wants to create social content, not review existing |
