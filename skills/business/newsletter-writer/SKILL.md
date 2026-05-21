---
name: newsletter-writer
description: "Generates ideas, plans publishing calendars, and writes newsletter issues using proven templates and engagement frameworks. Use for newsletter content, subject lines, hooks, calendars, and publishing."
---

# Newsletter Writer

Generates ideas, plans publishing calendars, and writes AI newsletter issues on Beehiiv using the CNC (Category Newsletter Creator) methodology. This skill takes you from blank page to published newsletter issue using proven frameworks for ideation, structure, and engagement.

## Prerequisites

- **Newsletter Positioning Brief** from `newsletter-positioner` (ideal input: provides newsletter identity, sub-niche, target reader, differentiation)
- At minimum you need: newsletter name, sub-niche, and target reader description
- Access to Beehiiv account for publishing and A/B testing
- Familiarity with the AI niche you're covering

## Emotional Hook Rule (MANDATORY)

Every newsletter issue must open with a hook that triggers a specific emotion in the first 1-2 sentences. Before writing, pick your target emotion: WOW (awe), WTF (disbelief), OMG (shock), LOL (humor), UGH (frustration), WHOA (revelation), NAH (contrarian), YEP (validation), OOF (shared pain), HMM (curiosity), DAMN (admiration), SMH (disapproval). For newsletters, evoke the emotion without using the abbreviation literally. "Claude just wrote 3000 lines of production code from one prompt. My developer took 3 weeks on the same feature." beats "In this issue, we explore how AI is changing software development." If your opening doesn't make the reader feel something, they won't scroll past the fold. See `skills/humanizer/SKILL.md` for the full emotional abbreviation list and usage rules.

---

## AI-Era Newsletter Principles (2025+)

Readers now get 90% of generic AI advice from chatbots before they open your newsletter. If your issue repeats the same tips as everyone else, it gets archived.

### The Novelty Principle

For every newsletter topic, research what everyone else is saying. Find the consensus. Then write the issue from a DIFFERENT angle: a contrarian take, a personal discovery, a surprising result. If your newsletter could have been written by ChatGPT about any business, it won't stand out.

**Process for every issue:**
1. Before writing, ask: "What does every other newsletter say about this topic?"
2. Find YOUR angle: what do you believe that contradicts the consensus? What personal experience taught you something different?
3. Lead with the contrarian angle or personal discovery, not the standard advice

### The Personal Story Mandate

Every newsletter issue MUST include at least one personal story with specific details. Generic tips are dead. Stories with names, dates, numbers, and "what went wrong" are what get read, forwarded, and remembered.

**Before writing any issue, ask the creator:**
> "What personal experience do you have with this topic? What failure, surprise, or discovery can we build the issue around? The more specific (names, dates, dollar amounts, what went wrong), the better. If you don't have one, what's a customer story we can use?"

If the creator can't provide a story, help them surface one:
- "What's the biggest mistake you've made with [topic]?"
- "When did the conventional wisdom about [topic] fail you?"
- "What result surprised you most when you tried [approach]?"
- "What do you believe about [topic] that most people get wrong?"

### Bot-Demo-Per-Issue Format

Each CC issue should feature one skill packaged as a tryable tool. Structure:
1. Personal story hook (the problem I had)
2. Introduce the skill/bot as the hero (this tool fixed it)
3. What it did for me (specific results with numbers)
4. CTA button: "Try it free" linking to the artifact/demo

The tool is the hero. The story is the setup. Every email is propaganda for a specific bot.

### Reduced Frequency Guidance

4-5 issues per week, not daily. Fewer but better. Each issue must have:
- A personal story (not generic advice)
- A clickable tool CTA (not just "read more")
- Less 3rd-party advertising, more own product CTAs

Quality and engagement over volume.

### 80/20 Effort Allocation Per Issue

Not every issue deserves the same effort. Power law math says most issues will get average engagement and a few will break out. Optimize accordingly:

- **Standard issues (80%):** Use templates, pick a format, fill it in, ship in 60 minutes. Good enough keeps you visible and buys lottery tickets. Don't rewrite three times.
- **Moonshot issues (20%):** These get 3-5x the effort. Original research, bold contrarian takes, deep personal stories, or a new tool demo that could go viral. Plan these intentionally and mark them on the content calendar.
- **After a hit:** If an issue gets 2x+ your average open rate or generates unusual replies/forwards, the NEXT issue should be a follow-up from a related angle. Do not move on to an unrelated topic. A breakout issue is the most valuable signal you'll get. Compound it.

Full framework with probability math and the Double-Down Playbook: See `content-strategy/references/power-law-framework.md`

---

## Workflow

### Step 1: Generate Ideas with "10 Magical Ways"

The 10 Magical Ways framework gives you a systematic method to generate dozens of newsletter ideas from any single AI topic. The 10 ways are:

1. **Tips**: Actionable advice readers can use immediately
2. **Stats**: Data-driven insights that surprise or validate
3. **Steps**: Sequential how-to processes
4. **Lessons**: Wisdom gained from experience (yours or others')
5. **Benefits**: Advantages readers haven't considered
6. **Reasons**: Arguments that persuade or reframe thinking
7. **Mistakes**: Common errors and how to avoid them
8. **Examples**: Real-world case studies and demonstrations
9. **Questions**: Thought-provoking questions that open loops
10. **Personal Stories**: Narrative-driven content that builds connection

Take any AI topic and run it through all 10 ways to generate a minimum of 10 distinct angles. Full detail and worked examples are in `references/idea-generator-matrix.md`.

### Step 2: Multiply Ideas

Once you have your base ideas from Step 1, multiply them using two dimensions:

**Audience Archetypes:** Cross each idea with different reader segments:
- Beginners just discovering AI
- Professionals integrating AI into existing workflows
- Specific roles (marketers, developers, writers, designers, managers)
- Demographics (solopreneurs, enterprise teams, freelancers, students)
- Situational contexts (career changers, scaling a business, automating tasks)

**Sub-Topic Variation:** For each audience-specific idea, develop 2-3 sub-topics:
- Adjacent areas that naturally connect to the main topic
- Natural progressions (what comes before/after this topic)
- Trending angles tied to current AI developments

The multiplication math: 1 topic x 10 ways x 3 archetypes x 2 sub-topics = 60+ ideas from ONE topic. You should never run out of content.

### Step 3: Plan 90-Day Publishing Calendar

Choose your publishing frequency based on your capacity and goals:

| Frequency | Content Style | Time Per Issue |
|---|---|---|
| Daily | Short, punchy, single-idea | 30-60 min |
| 2-3x per week | Mixed format, moderate depth | 45-60 min |
| Weekly | Deep, comprehensive | 60-90 min |
| Bi-weekly | Very detailed, high-production | 90-120 min |

**The 60-Minute Timer Workflow:**
1. Set a timer for 60 minutes
2. Write until it rings
3. Publish whatever you have

This prevents perfectionism paralysis. Done beats perfect. Your readers want consistency more than polish.

**Structure weeks by content type rotation:**
- Week 1: Deep Dive (educational framework or concept)
- Week 2: Curation (resource roundup with commentary)
- Week 3: Listicle (actionable list or how-to)
- Week 4: Deep Dive (case study or personal story)

Use the publishing calendar template at `templates/publishing-calendar.md` to plan your full 90-day schedule.

### Step 4: Write Newsletter Issues

Choose the right template based on your content goal:

| Template | Best For | File |
|---|---|---|
| Deep Dive | Educational content, frameworks, case studies | `templates/newsletter-deep-dive.md` |
| Curation | Resource roundups, news commentary, link collections | `templates/newsletter-curation.md` |
| Listicle | Actionable lists, how-to guides, step-by-step processes | `templates/newsletter-listicle.md` |
| Welsh Narrative | Personal story essays, reflections, build-in-public | `templates/newsletter-welsh-narrative.md` |
| Roundup | Daily/frequent news, multiple stories per issue | `templates/newsletter-roundup.md` |
| Trends Report | Weekly industry shifts, timely analysis | `templates/newsletter-trends-report.md` |

**Template selection guidance:**
- **Welsh Narrative** when you have a personal story that connects to a business lesson, when reflecting on a decision or pivot, or for build-in-public content. This is your 20% moonshot format -- more effort, much higher engagement.
- **Deep Dive** for educational frameworks and step-by-step teaching.
- **Listicle** for actionable tips and scannable how-to guides.
- **Curation** for resource roundups with commentary (standard or 3-2-1 variant).
- **Roundup** when covering 3+ news stories in one issue, for daily/frequent sends. Morning Brew / The Rundown format with repeatable story micro-templates, sponsor block, and quick hits.
- **Trends Report** when highlighting industry shifts and why they matter. Shorter sections (~150 words each), image-led, timely (not evergreen). Chasing Creative style.

Deep Dive, Curation, and Listicle follow the 7-section structure in Step 5. **Welsh Narrative, Roundup, and Trends Report issues use their own structures** -- see their respective template files.

### Multi-Newsletter Routing

When writing for a specific newsletter other than Cyber Corsairs, use the dedicated template. These templates override the generic 7-section structure with newsletter-specific formats, word counts, and constraints.

- **Cyber Corsairs**: Use standard templates above (deep-dive, curation, listicle). Default workflow.
- **Feel Better Live Better**: Use `templates/newsletter-feel-better.md`. 2-step process: research biohacking topics, then write 600-word issue. Audience: 50+ wellness readers.
- **Grow Monetize**: Use `templates/newsletter-grow-monetize.md`. JSON structural divergence rewrite system. 600-word max. Audience: newsletter creators.
- **Naples Brief**: Use `templates/newsletter-local-brief.md` with [CITY]=Naples, FL. Sub-template A (news) or B (events).
- **Fort Myers Brief**: Use `templates/newsletter-local-brief.md` with [CITY]=Fort Myers, FL. Sub-template A (news) or B (events).

For ALL newsletters, also run the universal email components after writing (see Step 6).

### Step 5: The 7-Section Newsletter Structure (Deep Dive / Listicle / Curation)

The following 7-section structure applies to Deep Dive, Listicle, and Curation templates. **Welsh Narrative issues use a different structure** -- see `templates/newsletter-welsh-narrative.md` for the 8-beat arc.

**Section 1: Intro**
Hook the reader with a story, observation, or bold statement. Then preview what's inside today. Keep it to 2-3 sentences. The goal is to stop the scroll and give readers a reason to keep reading.

**Section 2: Deep Dive**
The main educational content. Structure around 3 main points, each with:
- The concept explained clearly
- Why it matters to the reader
- A concrete example or case study
- An actionable takeaway they can use immediately

This is where you deliver your core value. Go deep, be specific, use examples.

**Section 3: Curated Links & Resources**
5-7 links readers would find valuable, each with:
- Resource name and link
- Estimated reading/watching time
- 1-sentence description of why it's worth their time

Curation is a value-add, you're saving readers hours of scrolling by filtering the best content for them.

**Section 4: Promotion / Sponsorship**
Either your own product plug or a sponsor ad. Keep it:
- Relevant to the newsletter topic
- Honest and genuinely useful to readers
- Short: 1 hook sentence, 3 benefit sentences, 1 CTA

**Section 5: Conclusion**
Summarize key takeaways (bullet points work well). Reinforce why this matters. Give the reader ONE specific action step to take before the next issue.

**Section 6: Poll**
A quick feedback question using Beehiiv's built-in poll feature. Options:
- Rate today's issue (Great / Ok / Bad)
- Topic-specific question to learn about reader preferences
- "What should I cover next?" with 3-4 options

Polls boost engagement metrics and give you direct reader intelligence.

**Section 7: P.S.**
The most valuable real estate in your newsletter. Readers who skim everything else will still read the P.S. Use it for:
- Your strongest CTA (product, lead magnet, referral program)
- A personal note that builds connection
- A tease for the next issue that creates anticipation

### Step 6: Write Subject Lines, Hooks & Preview Images

After writing the newsletter body, generate these universal email components:

1. **Hook**: For Deep Dive/Listicle/Curation: run `references/hook-generator.md` for 3 emotional personal story openings. For **Welsh Narrative**: the scene hook IS the opening -- use scene-hook patterns from `references/hook-generator.md` (Welsh Scene Hook section) or `references/welsh-narrative-framework.md`.
2. **Subject lines**: Use the rules below AND run `references/subject-line-generator.md` for 20 Reddit-style clickbait variants. For **Welsh Narrative issues**, also generate 5 Welsh Fragment Style subjects (2-5 word provocative fragments -- see `references/subject-line-swipe-file.md`, Welsh Fragment section).
3. **Preview image**: Run `references/preview-image-generator.md` to get 10 ChatGPT image prompt ideas for the header image.
4. **Banned words check**: Verify all output against `references/banned-words.md` (includes spam triggers, AI slop, and newsletter-specific forbidden words).

Subject lines determine whether your newsletter gets opened. Follow these rules:

**Golden Rules:**
- 5-15 words maximum
- Sentence-case (not Title Case or ALL CAPS)
- Use 1 of 4 proven hooks (see below)
- Use visceral language (OUCH!, URGENT!, FREE!, Seriously..., Steal this!)
- Name & Claim your ideas (give frameworks catchy names)
- Be SUPER SPECIFIC (numbers, timeframes, outcomes)

**4 Proven Hooks:**
1. Value for minimal time ("Master X in 5 minutes")
2. Value for minimal cost ("The free tool that replaces $500/mo software")
3. Solve problem without effort ("Stop doing X: do this instead")
4. Unlock outcome instantly ("Copy this template and 2x your output today")

**A/B Testing on Beehiiv:**
- Always A/B test subject lines (Beehiiv has this built in)
- Test different IDEAS, not just word order
- Give the test at least 1-2 hours before picking a winner
- Track open rates by subject line type to learn what your audience responds to

### Hormozi Hook Types for Email Subject Lines

Apply Hormozi's 7 verbal hook types to subject lines (from $100M Hooks Playbook):
1. **Labels** -- "Newsletter creators, I have a gift for you" (names the audience)
2. **Questions** -- "Would you pay $100 to save 10 hours this week?" (yes-questions pull opens)
3. **Conditionals** -- "If your open rate is under 30%, read this" (self-selects the right reader)
4. **Commands** -- "Stop writing subject lines like this" (direct, pattern-interrupt)
5. **Statements** -- "The smartest thing you can do before hitting send" (authority)
6. **Lists/Steps** -- "7 subject lines that got me 45%+ open rates" (specificity + curiosity)
7. **Narratives** -- "I almost deleted this email. Then it made $4,200." (story hook)

### Awareness-Level Hooks for Email
Match subject line style to subscriber awareness:
- **Most Aware** (loyal readers): Offer-driven. "50% off, 24 hours only"
- **Product-Aware** (engaged subs): Proof-driven. "Why 10,000 people opened this"
- **Solution-Aware** (warm subs): Promise-driven. "The fastest way to [result]"
- **Problem-Aware** (new subs): Pain-driven. "Tired of [problem]?"
- **Unaware** (cold/re-engagement): Curiosity-driven. "The hidden danger in your daily routine"

Use broader (colder) hooks to re-engage inactive subscribers. Use offer/proof hooks for your most engaged segment. See `video-hook/references/hormozi-hooks.md` for 121 proven hooks (18 specifically for email) and the full Awareness Pyramid.

Full subject line templates and swipe file in `references/subject-line-swipe-file.md`.

### Step 7: Create Pinned/Evergreen Issue

After publishing 10-15 issues:
1. Analyze which posts got the highest open rates, click rates, and replies
2. Identify your best-performing issue
3. Update it if needed (refresh links, tighten the writing)
4. Pin it on Beehiiv so every new subscriber sees it first

The pinned issue is your newsletter's "greatest hit", it sets expectations and delivers immediate value to new subscribers.

### Step 8: Repurpose as Social Content

Every newsletter issue contains 5-10 social media posts waiting to be extracted. Reference the `content-social` skill for platform-specific formats. Common repurposing approaches:

- Pull each main point from Section 2 into a standalone social post
- Turn the curated links into a "thread" or carousel
- Extract the hook/intro as a standalone attention-grabber
- Convert the listicle items into individual tips
- Use the poll question as social engagement content
- Turn the P.S. into a direct CTA post

## Output Format

The final deliverable is a complete newsletter issue ready for Beehiiv, including:

- **Subject Line** (with A/B variant)
- **Preview Text** (using one of the 4 whisper types)
- **Full newsletter body** with all 7 sections filled in
- **Suggested social repurposing** (3-5 post ideas extracted from the issue)

All content should be in the newsletter's established voice and tone, aligned with the positioning brief.

## Integration

- **Input from:** `newsletter-positioner` (newsletter identity, sub-niche, target reader, differentiation, voice/tone)
- **Output feeds into:** `newsletter-automator` (newsletter content referenced in welcome sequence and automation flows), `newsletter-grower` (repurposed social content drives new subscribers)
- **Run through:** `humanizer` before publishing (all newsletter content is outward-facing and must pass as human-written)
- **Reference:** `content-social` for social media repurposing formats and platform-specific best practices

## References

- `references/welsh-narrative-framework.md`: The Justin Welsh Narrative Newsletter Framework -- 8-beat story arc, scene-hook patterns, parallel story technique, specificity rules, recurring character strategy (The Jennifer Effect), anti-patterns, and when to use Welsh Narrative vs other templates. Based on analysis of 20 consecutive issues.
- `references/idea-generator-matrix.md`: The 10 Magical Ways framework for generating 60+ newsletter ideas from any single topic
- `references/mirror-framework.md`: How to study and reverse-engineer successful newsletter formats without copying content
- `references/subject-line-swipe-file.md`: 55+ subject line templates organized by hook type, plus the 4 Whisper Types for preview text and A/B testing guidance
- `references/engagement-psychology.md`: Newsletter retention psychology, frequency vs. quality tradeoffs, reader retention techniques (open loops, future pacing, pattern interrupts, controversy), 7-day first impression window, re-engagement tactics for cold subscribers, metrics that matter for newsletter health
- `references/storytelling-for-newsletters.md`: 8 storytelling hacks (specificity, metaphor, transformation arc, vulnerability, contrast, curiosity gap, sensory detail, dialogue), Pixar's rules adapted for newsletters, TORS/SBI/mini-story structures, story-to-CTA narrative arc, story triggers by emotion
- `references/kennedy-newsletter-doctrine.md`: Dan Kennedy's Herd Concept (frequency = retention fence), 40/60 content rule, Rule #1 (every issue has an offer), newsletter as business engine (front end, back end, continuity, big paydays), offer checklist
- `references/brunson-frameworks.md`: Brunson's Seinfeld Email Formula (90/10 entertainment-to-content ratio for standard issues), Hook-Story-Offer (HSO) structure for every issue, Attractive Character identity system (Captain YAR = Adventurer/Crusader). Use for voice calibration and daily-issue rhythm.
- `references/hook-generator.md`: Universal emotional personal story hook generator. Produces 3 different opening hooks (2 paragraphs each) for any newsletter issue. Audience-aware with per-newsletter overrides.
- `references/plutus-app-hooks.md`: 34 fill-in-the-blank templates + 300 proven UGC hooks across 10 categories + 5 performance insights. Use for subject lines and opening hooks on issues demoing a product, tool, or the product skill. Gatekeeper, Impossible Claim, and Regret Reveal categories work best for email subject lines; Someone Showed Me and Authority Endorsement are strong for trust-building issues.
- `references/static-headline-formulas.md`: Static headline playbook (4 features, awareness-stage targeting, 5 formulas, power-words library). The 3–5 word rule maps cleanly to mobile-truncated subject lines (~50 chars). Use for subject lines, preview text, and above-the-fold newsletter H2s. Pair with `subject-line-swipe-file.md` for broader email-specific patterns.
- `references/subject-line-generator.md`: Reddit-style clickbait subject line generator. Produces 20 variants (5 words or less) from any newsletter text. Complementary to `subject-line-swipe-file.md`.
- `references/preview-image-generator.md`: ChatGPT/DALL-E image prompt generator. Produces 10 non-ordinary 16:9 image concepts for newsletter headers.
- `references/banned-words.md`: Centralized registry of banned words, spam triggers, AI slop markers, and newsletter-specific forbidden terms. Cross-references `content-review/references/banned-patterns.md` and `email-optimizer/references/subject-line-frameworks.md`.
- `references/sponsor-block-anatomy.md`: The 5-part anatomy for writing sponsor content blocks that feel native and justify premium CPMs (clickable heading, simple visual, summary in YOUR voice, bulleted benefits, clear CTA). Includes placement rules per template type, CPM guidance ($25-50+ main block, $5-15 quick hits), anti-patterns, and own-product promotion structure.
- `references/quick-hits-block.md`: Reusable quick hits / quick bites content block for end-of-issue links. Format (emoji + bold headline + 1 sentence, 5-7 items), content sourcing, placement, monetization at $5-15 CPMs per slot, quality rules. Used by Roundup (default) and optionally by other templates.

## Learned Principles (Conference Insights, March 2026)

### Content Framing (Sean Devlin)
The main questions that should frame your entire newsletter and each individual section:
- **What is your goal? What are you optimizing for?**

### Section-Specific Insights
- **Intro section:** Form personal connection between audience and team, even if you're a brand. Humans like humans. Trust is the moat.
- **Consistency + Variety:** Consistency forms habits, but too much sameness lulls people to sleep. Experiment with new sections to keep fresh. **80/20 rule** -- 80% familiar structure, 20% experimentation.
- **End well:** How do you want readers to FEEL when they finish? Align final content to that goal:
  - Entertained? Meme or fun fact.
  - Think deeply? Profound quote.
  - Sense of awe? Image of nature.
  - **Images evoke emotion more quickly than words.**

### Storytelling Retention Techniques for Newsletters

Apply these techniques from top-performing creator content to newsletter writing. They dramatically improve read-through rates and engagement.

**Recurring Character:** Reference the same person, company, or example across multiple newsletter issues. Each appearance builds reader investment. By the 3rd or 4th mention, readers care about that character. The payoff (success, failure, update) only lands because of prior appearances.

**Full-Circle Callback:** End the email by returning to the opening image, scenario, or line with new meaning. Open with "Last week I almost deleted my entire automation." Close with "That automation I almost deleted? It made $4,200 this month." The callback proves transformation and makes the email feel complete.

**Hidden Thesis:** Don't state the lesson in the intro. Let the story prove it. The reader discovers the point before you state it, which makes the conclusion land harder. State the thesis explicitly only in the P.S. or final paragraph.

**Question Framework:** Frame the entire email around ONE driving question, not a topic. "Can a newsletter actually replace a six-figure salary?" creates tension. "Newsletter monetization strategies" just informs. Every section becomes evidence for or against the answer.

**"But/Therefore" Flow:** Never connect story beats with "and then." Use "but" (introduces conflict) or "therefore" (shows consequence). "I grew to 50K subs, BUT my revenue was $0. THEREFORE I completely rethought monetization." This creates unpredictability that keeps readers scrolling.

**Vulnerability Before Victory:** Show the lowest point RIGHT BEFORE the breakthrough. "I was ready to shut it down. The open rate was 12%. I told my wife I'd wasted a year." Then the turn. Without vulnerability, victory feels hollow and unearned.

**Naming the Abstract:** Give tools, strategies, and concepts a name. "The $0 Stack" instead of "free tools." "The Trust Moat" instead of "building trust." Named concepts are quotable, shareable, and memorable.

Full technique library: `private project content/storytelling-analysis-car-theft-video.md` and `private project content/storytelling-analysis-100hrs-ai-video.md`

### The Trust Economy (Anik Singal)
- AI is creating The Trust Economy. Trust is the moat.
- Trust takes more time to build than it does to break.
- Optimize every newsletter for trust-building, not just clicks.

### Kennedy Offer Check (MANDATORY)

Every issue must include at least one clear offer with a specific CTA. Not a hard sell. A clear ask with a clear next step. "Try this free tool." "Reply with your biggest challenge." "Grab the prompt pack." If the issue has zero offers, it's a missed opportunity. The P.S. is the second most-read element after the subject line. Use it for your strongest CTA or a second offer. Before hitting send, verify: (1) at least one offer exists, (2) the CTA tells readers exactly what to do, (3) there's a reason to act now. See `references/kennedy-newsletter-doctrine.md` for the full doctrine: Herd Concept (frequency = retention), 40/60 content rule (40% about readers, 60% soft promotion), and newsletter as business engine.
