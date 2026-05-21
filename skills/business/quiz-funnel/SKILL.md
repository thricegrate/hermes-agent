---
name: quiz-funnel
description: |
  Designs quiz funnels that convert cold social/UGC traffic 2-4x better than
  product pages. Covers 5 quiz types (product match, pricing plan, upsell,
  diagnostic, scorecard), question architecture, recommendation screen copy,
  email capture placement, lead qualification, and quiz-path segmented
  follow-ups. Use when user mentions "quiz funnel," "product quiz,"
  "recommendation quiz," "UGC conversion," "why isn't my product page
  converting social traffic," "interactive quiz," "quiz lead gen,"
  "diagnostic quiz," "pricing quiz," "product match quiz," "post-purchase
  quiz," "quiz for lead capture," "scorecard quiz," "lead qualification
  quiz," "score-based quiz," or "Priestley quiz."
---

# Quiz Funnel Architect

## Why This Exists

Standard product pages waste 97-99% of traffic from UGC reels and social content. The reel builds emotional momentum, the visitor clicks, and the product page kills it with a transactional environment that doesn't continue the conversation. Quiz funnels fix this by meeting the visitor in the emotional register the content created and guiding them to a personalized recommendation.

The typical improvement: 2-4x the conversion rate of a standard product page on the same traffic, plus email capture on every quiz completion for follow-up sequences.

**Where quiz funnels fit in the lead magnet taxonomy:** Quiz funnels are a natural Type 2 (Trial of the Solution) lead magnet in Hormozi's framework. Instead of giving people a PDF, you give them a personalized result -- their score, their diagnosis, their recommendation. They experience a taste of your expertise firsthand. This is why quiz funnels convert 2-4x better than static lead magnets: experiencing a result is more persuasive than reading about one. For the full lead magnet taxonomy, see `free-tool-strategy` SKILL.md.

## Prerequisites

Before starting, gather:
- Product catalog or offer details (what are you selling, how many variants/tiers)
- Traffic source (UGC reels, paid social, organic, email -- this matters)
- Current conversion rate if known (even a rough estimate helps)
- Email platform they're using (Beehiiv, Klaviyo, ConvertKit, etc.)
- Existing quiz if they have one (so we're improving, not reinventing)

## Workflow

### Step 1: Diagnose the Fit

Not every situation needs a quiz funnel. Run this checklist:

**Green lights (quiz funnel is a good fit):**
- Traffic comes from emotional/entertainment content (UGC reels, TikTok, Instagram, social)
- Product catalog has 3+ items OR multiple pricing tiers OR multiple use cases
- Current product page conversion is below 2% on social traffic
- Audience arrives interested but unsure which specific product is right for them

**Red flags (quiz funnel may hurt):**
- Traffic is high-intent search (Google Ads to product page) -- quiz adds friction here
- Single product with no variants -- just optimize the product page instead
- Audience already knows exactly what they want -- don't slow them down

If it's a red flag situation, route to `cro` for product page optimization instead.

### Step 2: Pick the Quiz Type

Five types. Pick the one that matches their business model. See `references/quiz-types-playbook.md` for the full decision framework with example questions.

**1. Best Product Match Quiz**
For catalogs with 3+ products serving different segments of the same audience. The quiz identifies which product fits the visitor's specific situation. Most common type.

**2. Best Pricing Plan Quiz**
For offers with multiple pricing tiers or subscription options. Eliminates decision paralysis by making the tier decision for the visitor based on their usage patterns and needs.

**3. Income Product / Upsell Match Quiz**
Post-purchase quiz. Asks 3-4 questions about how they plan to use what they just bought, then recommends the specific complementary product that adds the most value. Converts at extraordinary rates because the visitor is already in a high-trust state.

**4. Diagnostic Awareness Quiz**
Top-of-funnel. Instead of leading to a product recommendation directly, it generates a personalized problem assessment. Educates the visitor about their specific situation and positions the product as the logical solution to the root cause the diagnosis identified. Most powerful for higher-price-point offers.

**5. Scorecard Quiz (Priestley Model)**
For service businesses, coaching, consulting, and multi-tier offers where lead qualification matters as much as conversion. Uses a 20-question, 3-phase structure: contact-first capture, 10 yes/no scoring questions, and 5 qualification questions that route leads to different CTAs based on their readiness and budget signal. See `references/priestley-scorecard-framework.md` for the full framework.

### Step 3: Design the Architecture

Six principles. See `references/quiz-psychology.md` for the psychological reasoning behind each.

1. **Conversation, not form.** Every question should feel like something a knowledgeable friend would ask before giving a recommendation. "What's been the biggest obstacle when you've tried to fix this before?" not "Rate your barriers on a scale of 1 to 5."

2. **5-7 questions.** Fewer than 5 doesn't generate enough personalization signal. More than 7 creates drop-off. Sweet spot completion time: 90 seconds to 2.5 minutes.

3. **Recommendation screen is the money page.** This is where the entire psychological setup pays off. Invest more effort here than on any other element. It must affirm answers, deliver a personalized recommendation, show relevant social proof, and create urgency. Use `templates/recommendation-screen.md`.

4. **Email capture goes between the last question and the recommendation.** Frame it as the delivery mechanism: "Enter your email and we'll send your personalized results." They've invested 90 seconds already -- they'll give the email to see what the quiz recommends.

5. **Mobile-first everything.** UGC/social traffic is overwhelmingly mobile. Large tap targets on answer options. No text input fields unless absolutely necessary. Fast load times at every transition. Recommendation screen communicates above the fold on mobile.

6. **Segment email follow-ups by quiz path.** Each distinct path through the quiz = distinct persona = distinct follow-up sequence. A visitor matched to the entry-level product needs different emails than one matched to the premium product. Hand off to `email-sequence` for the sequence design.

7. **Contact capture placement is a strategic choice.** The default (Principle 4) captures email between the last question and the recommendation. An alternative: capture contact info upfront (Q1-4) so partial completions still yield leads. Use contact-first for high-ticket service offers where a partial lead has value (sales team can follow up with just a name and email). Use end-capture for e-commerce and low-ticket offers where quiz momentum and completion rate matter more. See the Priestley Scorecard framework in `references/priestley-scorecard-framework.md` for the contact-first architecture.

### Step 3b: DM Automation Entry Point (Optional)

Instead of routing quiz traffic through link-in-bio, consider comment-gated delivery via DM automation (ManyChat). Viewers comment a keyword on the reel, receive the quiz link via DM, and enter the funnel with higher intent.

**When to use DM automation:**
- Traffic is primarily from Instagram Reels or Facebook
- You want the algorithm boost from comment volume (comments are the highest-weight engagement signal)
- You want a dual-channel follow-up (DM + email)

**When to skip it:**
- Traffic is from TikTok (DM automation less mature)
- Traffic is from paid ads (link click is simpler)
- You're sending email traffic to the quiz (they're already on your list)

**Full setup, message templates, and metrics:** See `references/dm-automation.md`

This changes the UGC script CTA (Section 6) from "link below" to "comment [KEYWORD] and I'll send you the quiz." See `references/ugc-quiz-integration.md` for how the UGC content system maps to quiz entry.

### Step 4: Write the Questions

Work backward from the recommendation:

1. **Start with the end.** List all recommendation buckets (the distinct products, tiers, or diagnoses the quiz can recommend).
2. **Identify discriminating factors.** What information separates a visitor who should get Recommendation A from one who should get Recommendation B?
3. **Turn discriminating factors into conversational questions.** Each question should feel natural and build on the previous one.
4. **Use image-based answers where possible.** Visual options get higher engagement and faster completion than text-only.

**Example for a skincare brand with 4 product lines:**
- Q1: "What's your skin doing right now that's driving you crazy?" (identifies primary concern)
- Q2: "How would you describe your skin type on most days?" (narrows product match)
- Q3: "What have you tried before that didn't work?" (builds commitment, identifies mechanism bridge)
- Q4: "What does your morning routine look like right now?" (usage context for recommendation)
- Q5: "What matters most to you in a skincare product?" (final discriminator)

**Alternative: The Big 5 Qualification Framework**

For service/coaching businesses with multi-tier offers, consider structuring the final 5 questions using the Big 5 qualification pattern. These question types qualify leads without feeling like interrogation:
1. Current situation (reveals starting point and experience level)
2. Desired outcome in 90 days (reveals urgency and ambition -- the timeframe anchor is intentional)
3. What hasn't worked (reveals pain AND failed solutions, which tells you what objections to address)
4. Solution preference: free resources, course, coaching, or done-for-you (reveals budget indirectly -- someone who picks "done-for-you" signals a completely different budget than someone who picks "self-paced learning")
5. Anything else? (open text, optional -- sometimes surfaces gold like "have budget, must spend by month end")

Full framework with examples for multiple industries: `references/priestley-scorecard-framework.md`

### Step 4b: Kennedy Diagnosis-and-Prescription Architecture

Kennedy's diagnosis model maps perfectly to quiz funnels. The quiz IS the diagnosis. The recommendation screen IS the prescription. Layer these principles into the quiz design.

**Quiz as diagnosis:** Each question should make the prospect feel like an expert is examining their specific situation. Kennedy's 10 Smart Market Diagnosis Questions are great inspiration for quiz questions: What keeps them up at night? What are they afraid of? What are their daily frustrations? What do they secretly desire most? Adapt these to your niche.

**Recommendation screen as prescription:** Don't just recommend a product. Diagnose their situation first ("Based on your answers, your biggest gap is X"), then prescribe the solution ("That's exactly what [Product] addresses"). Diagnosis before prescription converts 2-4x better than a straight product recommendation.

**Take-away selling on results page:** For higher-tier recommendations, add qualification language. "This program is designed for people who scored above 70 and are ready to invest in implementation. If that's you, here's the next step." Making it harder to access makes it more desirable.

### Step 5: Build the Recommendation Screen

This is the highest-leverage page in the entire funnel. Use `templates/recommendation-screen.md` as the starting structure.

The recommendation screen must do 4 things:
1. **Affirm their answers** -- reflect their situation back accurately ("You told us your biggest challenge is X and you've already tried Y and Z")
2. **Deliver the recommendation with a reason** -- "Based on what you shared, we recommend [Product] because it specifically addresses [the thing they said matters most]"
3. **Show relevant social proof** -- testimonial from someone with a similar quiz profile, not generic reviews
4. **Create urgency** -- time-limited offer, limited stock, or next-step momentum ("Start your personalized plan today")

The copy should reference their specific answers. Not "based on your answers" generically, but "because you told us X, Y, and Z" specifically.

Hand off to `sales-page-writer` for the recommendation screen copy if the offer is complex.

**Tiered CTA Routing (for multi-tier offers)**

When the business has multiple offer levels, the recommendation screen should route prospects to different CTAs based on their qualification signals:
- **High-qualified** (urgent need + premium solution preference + high score) -> Book a call
- **Mid-qualified** (clear need + moderate timeline + coaching/education preference) -> Register for webinar
- **Low-qualified** (exploring + free resources preference + early stage) -> Download free resource

This prevents the "one CTA fits all" problem where high-value prospects get the same generic next step as casual browsers. See `references/priestley-scorecard-framework.md` for the full routing logic.

### Step 6: Wire the Email Follow-Up

The email capture between last question and recommendation creates your list-building engine. Every quiz completion = a segmented lead.

**Hand off to `email-sequence`** to build quiz-path-segmented follow-ups:
- Each quiz result bucket gets its own 3-5 email sequence
- Email 1: Reinforce the recommendation ("Here's why [Product] is right for you based on what you told us")
- Emails 2-3: Handle objections specific to that product/tier
- Emails 4-5: Social proof from similar customers + purchase incentive

This follow-up consistently recovers 20-40% of leads who didn't purchase from the recommendation screen. That's revenue that would have been permanently lost without the quiz's email capture.

### Ghost Recovery Sequences

When a prospect starts the quiz but disappears, or completes but goes dark after follow-up, don't send "just checking in." That's the laziest message in sales. Always lead with NEW value they haven't seen.

**Recovery timeline:**
- **Day 3** after last contact: Send a new value piece related to their quiz result. "Hey, just pulled a case study from someone who scored similar to you on the quiz. They were stuck on [their #1 problem from quiz]. Here's what worked for them."
- **Day 7**: Different angle entirely.
  - If they asked about pricing: "btw we just added a [lower tier/payment plan] that might work better."
  - If they asked about features: "just recorded a quick demo showing [specific feature they asked about]. want me to send it?"
- **Day 14**: Final soft touch. "No worries if timing's off. Just wanted to share [one specific resource] before I forget. It's relevant to what you were looking at."
- **After Day 14**: Move to long-term nurture list. No more active outreach.

**The rule:** Every recovery message must contain something NEW. A new case study, a new pricing option, a new demo, a new resource. If you don't have something new to offer, don't send the message.

### Step 7: Choose Tools

Pick based on quiz type and e-commerce platform. Full comparison in `references/tools-and-stack.md`.

- **Typeform** -- conversational one-at-a-time format, strong integrations (Zapier, Klaviyo, Mailchimp). Best for: general purpose, any quiz type.
- **Interact Quiz Builder** -- purpose-built for B2C product matching, complex branching logic. Best for: product match quizzes with multiple recommendation paths.
- **Octane AI** -- Shopify-native, connects directly to product catalog. Best for: Shopify stores, zero-code product recommendations.
- **ScoreApp** -- score-based diagnostic assessments with detailed written analysis. Best for: diagnostic awareness quizzes, higher-price-point offers.

### Step 8: Measure and Iterate

Track these metrics weekly:

| Metric | Benchmark |
|--------|-----------|
| Quiz start rate (of page visitors) | 40-60% |
| Quiz completion rate (of starters) | 60-75% |
| Email capture rate (of completers) | 70-85% |
| Recommendation-to-purchase rate | 4-8% |
| Email sequence recovery rate | 20-40% |

See `references/revenue-architecture.md` for the full revenue math and 6-month compounding model.

**Scorecard quiz benchmarks differ.** A 20-question scorecard quiz has different baseline metrics than a 5-7 question product match quiz. Expect 20-40% page-to-completion (lower than shorter quizzes) but higher lead quality, richer data per lead, and more total leads when counting partial completions captured via contact-first. See `references/priestley-scorecard-framework.md` for scorecard-specific benchmarks.

**Scale Decision Threshold:** Before scaling production investment (more accounts, more content, paid amplification), all 3 criteria must be met:
1. 4 consecutive weeks of revenue without >15% week-over-week decline
2. Quiz conversion rate >5% (recommendation-to-purchase) on 500+ completions
3. At least 3 validated hook/avatar combinations across multiple accounts

A campaign that doesn't meet all 3 has an unsolved problem that scaling will amplify. See `references/ugc-quiz-integration.md` for the full framework.

Hand off to `cro-funnel` for ongoing funnel optimization once the quiz is live.

### Step 9: Content-to-Quiz Feedback Loop

The quiz is also a continuous audience research instrument. After 30+ days of data:

- **Most common pain points in quiz responses** become priority hook angles for the next content cycle
- **Most frequently mentioned failed alternatives** become mechanism bridge language in the next script batch
- **Transformation language visitors use** becomes the exact wording in the next generation of reels and emails

Feed this data back into `content-social` and `ads-strategy` for increasingly precise targeting.

## Output

Use `templates/quiz-blueprint.md` to deliver the complete quiz funnel design. The blueprint includes questions, answer mapping, recommendation buckets, email capture placement, follow-up sequence briefs, tool recommendation, and success metrics.

## Integration

- **Receives handoff from:** `cro-funnel` (product page is the bottleneck for social traffic), `free-tool-strategy` (quiz chosen as lead gen tool type), `ads-strategy` (UGC campaign needs a landing destination)
- **Hands off to:** `email-sequence` (quiz-path follow-up emails), `design-page` (quiz landing page and recommendation screen design), `sales-page-writer` (recommendation screen copy), `cro` (optimizing quiz completion rate and recommendation screen), `content-social` (content that drives to quiz)
- **Data feedback:** quiz response data feeds back into `content-social` (content angles), `ads-strategy` (audience targeting), and `cro-funnel` (funnel optimization)
- **UGC integration:** See `references/ugc-quiz-integration.md` for how the 6-section UGC script CTA maps to quiz entry, conversion benchmarks by traffic source, scale decision thresholds, and the revenue-per-quiz-completion north star metric
- **DM automation:** See `references/dm-automation.md` for comment-gated quiz delivery via ManyChat (alternative to link-in-bio)
- **Persona depth:** `niche-finder` 5-Layer Persona Depth Profile feeds quiz question design (Layer 3 pain points become Q1-Q2, Layer 4 failed alternatives become Q3 answer options)
