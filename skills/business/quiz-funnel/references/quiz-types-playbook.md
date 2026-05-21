# Quiz Types Playbook

Detailed breakdown of all 5 quiz types. Use this to pick the right type and design the question structure.

---

## Type 1: Best Product Match Quiz

### When to Use
- Catalog has 3+ distinct products or product lines serving different segments
- Product differences are meaningful enough that the wrong product produces a worse outcome
- Visitor from the reel has been sold on the category but not on a specific product

### Question Structure (5-7 questions)

**Opening question:** Establishes primary segmentation.
"Which of these best describes your main goal right now?"
Options map to the distinct product lines.

**Middle questions:** Narrow the match within that segment based on factors that differentiate product performance across user profiles.

**Closing questions:** Final discriminators that confirm the recommendation.

### Example: Supplement Brand (4 Product Lines)

Q1: "What's your #1 goal right now?"
- Lose weight and feel lighter -> Weight line
- Build muscle and get stronger -> Performance line
- Sleep better and reduce stress -> Recovery line
- More energy throughout the day -> Energy line

Q2: "How active are you on a typical week?"
- I barely move (honest answer) -> Beginner variants
- 2-3 workouts -> Moderate variants
- 5+ sessions, I'm a gym rat -> Advanced variants

Q3: "What have you tried before that didn't stick?"
- Protein shakes that tasted like chalk -> Taste matters, flavor options
- Pills I forgot to take -> Convenience matters, daily pack
- Expensive stuff that did nothing -> Value matters, starter size

Q4: "Any dietary restrictions we should know about?"
- Vegan / plant-based -> Plant-based variants
- Gluten-free -> Gluten-free variants
- No restrictions -> Full catalog

Q5: "What's your budget comfort zone for monthly supplements?"
- Under $30 -> Starter size
- $30-60 -> Standard size
- $60+ -> Bundle / subscription

### Recommendation Logic
Each answer combination maps to a specific product SKU. The recommendation screen presents that product with a brief explanation of why it was matched: "Because you told us your main goal is [X] and you prefer [Y], we recommend [Product Z]."

### Email Follow-Up Strategy
- Bucket A (weight loss): 5 emails focused on transformation stories, before/after, consistency tips
- Bucket B (performance): 5 emails focused on workout results, stacking protocols, athlete testimonials
- (Repeat for each bucket)

### Common Mistakes
- Too many recommendation buckets (keep it to 3-5, not 15)
- Questions that don't actually discriminate between products
- Generic recommendation screen that doesn't reference answers

---

## Type 2: Best Pricing Plan Quiz

### When to Use
- Multiple pricing tiers, subscription options, or bundle configurations
- Visitors experience decision paralysis on the pricing page
- Different tiers genuinely serve different use cases (not just more-of-the-same)

### Question Structure (4-6 questions)

**Opening questions:** Establish primary use case and intensity of need.
**Middle questions:** Identify specific features or capabilities that matter most.
**Closing questions:** Budget signals, timeline urgency, experience level.

### Example: SaaS Tool (3 Tiers)

Q1: "How are you planning to use [Tool]?"
- Just me, personal projects -> Starter
- Small team, a few collaborators -> Pro
- Company-wide, multiple teams -> Business

Q2: "How many [units] do you expect to handle per month?"
- Under 100 -> Starter
- 100-1,000 -> Pro
- 1,000+ -> Business

Q3: "Which of these would make the biggest difference for you?"
- Just the basics, keep it simple -> Starter (doesn't need advanced features)
- Automations and integrations -> Pro (power user features)
- Analytics, SSO, and admin controls -> Business (enterprise features)

Q4: "Have you used a tool like this before?"
- First time -> Starter (lower risk entry)
- Used competitors -> Pro (ready for more)
- Migrating from another tool -> Business (needs migration support)

Q5: "What's your timeline?"
- Just exploring -> Starter or free trial
- Need it this month -> Pro (urgency = higher tier tolerance)
- Yesterday -> Business (urgency + likely bigger operation)

### Recommendation Framing
The key differentiator: frame the recommendation as what they DON'T need as much as what they DO.

"Based on what you told us, the Pro plan is the right fit because it includes [automations they said matter] without requiring you to pay for [enterprise features they said aren't relevant]. You're not overpaying and you're not under-equipped."

This is what a trusted advisor does. Not upselling, not downselling. Right-sizing.

### Email Follow-Up Strategy
- Starter leads: nurture toward upgrade as usage grows, highlight Pro features they're missing
- Pro leads: reinforce value of their tier, share power-user tips, build case for annual commitment
- Business leads: white-glove onboarding content, ROI calculators, case studies from similar companies

### Common Mistakes
- Recommending the most expensive tier to everyone (destroys trust)
- Not explaining WHY this tier over the others
- Forgetting to offer a comparison link for visitors who want to see all options

---

## Type 3: Income Product / Upsell Match Quiz

### When to Use
- Customer just completed a purchase (post-purchase moment)
- Core product has complementary products, add-ons, or subscription upgrades
- You want to capture the highest-trust conversion window

### Question Structure (3-4 questions, keep it light)

Post-purchase quizzes must be SHORT. The buyer is in a high-trust state but also has low patience for more steps. 3-4 questions max.

### Example: Online Course (Post-Purchase)

Q1: "Now that you've got [Course], what are you most excited to work on first?"
- Getting my first client -> Recommend: Client Acquisition Toolkit
- Building my portfolio -> Recommend: Portfolio Templates Pack
- Learning the advanced techniques -> Recommend: Masterclass Upgrade

Q2: "How much time can you dedicate to this per week?"
- A few hours -> Recommend: self-paced add-on
- 10+ hours -> Recommend: cohort or live component

Q3: "Would having direct feedback on your work speed things up?"
- Absolutely, I learn better with feedback -> Recommend: coaching add-on
- I prefer working independently -> Recommend: template/resource add-on

### Recommendation Framing
"Now that you've got [Course], let's make sure you get the most out of it." Reframe the upsell as a natural extension of what they just bought, not a separate purchase.

Present ONE product, not a menu. "Based on how you're planning to use [Course], the [Add-On] will make the biggest difference for you because [specific reason tied to their answers]."

### Email Follow-Up Strategy
Post-purchase quiz leads who don't buy the upsell immediately get a 3-email sequence:
- Email 1 (Day 1): Onboarding for the main product + soft mention of the recommended add-on
- Email 2 (Day 3): Case study from someone who used the main product + the add-on together
- Email 3 (Day 5): Limited-time offer on the recommended add-on

### Common Mistakes
- Making the quiz too long (3-4 questions max post-purchase)
- Offering multiple upsell options instead of one clear recommendation
- Generic upsell that ignores the quiz answers

---

## Type 4: Diagnostic Awareness Quiz

### When to Use
- Target audience has low awareness of the specific mechanism behind their problem
- Your unique mechanism is genuinely differentiated from category defaults
- Organic traffic is emotionally engaged but not yet convinced of your specific approach
- Higher-price-point offers that need more educational context before purchase

### Question Structure (5-7 questions)

This quiz asks about the visitor's current situation, past experiences, and specific symptoms. Instead of leading to a product recommendation, it generates a personalized diagnosis.

### Example: Business Coaching (High-Ticket)

Q1: "What's your current monthly revenue?"
- Under $5K -> Early stage diagnosis
- $5K-$25K -> Growth stage diagnosis
- $25K-$100K -> Scale stage diagnosis
- $100K+ -> Optimization stage diagnosis

Q2: "What's the ONE thing that feels like the biggest bottleneck right now?"
- Not enough leads -> Lead generation diagnosis
- Leads but no sales -> Conversion diagnosis
- Sales but no profit -> Operations/margins diagnosis
- Everything depends on me -> Systems/delegation diagnosis

Q3: "How many of these have you tried in the last 12 months?"
(Checkbox: paid ads, social media, content marketing, referrals, cold outreach, SEO)
-> Maps to: "tried everything" vs "barely started" diagnosis paths

Q4: "What happened when you tried those?"
- Some worked, couldn't scale them -> Diagnosis: systems problem
- Nothing moved the needle -> Diagnosis: strategy problem
- Worked then stopped -> Diagnosis: sustainability problem

Q5: "If you could fix ONE thing in the next 90 days, what would matter most?"
- Predictable lead flow -> Route to lead gen product
- Higher close rate -> Route to sales product
- More time, less chaos -> Route to operations product
- Bigger vision, clearer path -> Route to strategy product

### Diagnosis Screen (Instead of Recommendation Screen)

The diagnosis screen explains the visitor's problem to them before asking for a purchase. This is what makes diagnostic quizzes the most powerful trust-building tool in the B2C toolkit.

Structure:
1. **Their situation reflected back:** "Based on your answers, you're at the [stage] with a primary bottleneck in [area]."
2. **Why previous approaches didn't work:** "The approaches you've tried ([list from Q3]) typically fail for businesses at your stage because [mechanism explanation]."
3. **The root cause:** "What's actually driving this is [root cause] -- and until that's addressed, [surface-level fixes] will keep producing temporary results."
4. **The solution (your product):** "This is exactly what [Product] was built to solve. Here's how it works for someone in your specific situation..."

### Email Follow-Up Strategy
Diagnostic quiz leads are warmer than they look. They've just received a personalized analysis of their problem. The follow-up sequence deepens the diagnosis:
- Email 1: Expanded version of their diagnosis with additional insights
- Email 2: Case study from someone with the same diagnosis who solved it
- Email 3: "The 3 things businesses at your stage get wrong about [their bottleneck]"
- Email 4: Product deep-dive with a time-limited offer or call booking CTA
- Email 5: Final urgency + recap of their specific diagnosis

### Common Mistakes
- Making the diagnosis generic instead of referencing their specific answers
- Jumping to the product too quickly without earning the educational trust
- Diagnosis that's too short or superficial to feel credible

---

## Type 5: Scorecard Quiz (Priestley Model)

### When to Use
- Service business, coaching, consulting, or B2B offer with multiple tiers
- Lead qualification matters as much as (or more than) immediate conversion
- Sales team needs pre-qualified leads routed to the right offer level
- Product ladder spans free content to done-for-you ($0 to $15K+)
- Audience is willing to invest 3 minutes for a personalized assessment

### Key Differentiator vs Type 4 (Diagnostic)
Type 4 educates about a problem and positions the product as the solution. Type 5 qualifies the lead and routes them to the right offer tier. Type 4 says "here's what's wrong and how to fix it." Type 5 says "here's how you're doing and here's your personalized next step based on where you are."

### Question Structure (20 questions, 3 phases)

**Phase 1: Contact-First Capture (Q1-4)**
Name, email, phone (optional), location. Captured upfront so partial completions still yield leads.

**Phase 2: Best Practices Scoring (Q5-14)**
10 yes/no questions generating a score out of 100. Each "No" identifies a specific gap the business can address.

**Phase 3: The Big 5 Qualification (Q15-19)**
Five strategic questions that qualify leads without feeling like interrogation:
1. Current situation (starting point / experience level)
2. Desired outcome in 90 days (urgency + ambition)
3. Obstacles / what hasn't worked (pain + failed solutions)
4. Solution preference (reveals budget indirectly)
5. Anything else? (open text, optional)

Full framework with examples: `references/priestley-scorecard-framework.md`

### Example: Business Coaching (4-Tier Offer)

**Phase 1:** Name, email, phone (optional), location (auto)

**Phase 2 (abbreviated):**
- Q5: "Do you have a documented business plan?" Yes/No
- Q6: "Do you track your key metrics weekly?" Yes/No
- Q7: "Do you have a repeatable lead generation system?" Yes/No
- ... (7 more yes/no best practices)

**Phase 3:**
- Q15: "Which best describes you?" -> Pre-revenue / $0-5K/mo / $5-25K/mo / $25-100K/mo / $100K+
- Q16: "What do you want to achieve in 90 days?" -> First clients / $10K/mo / Build team / New revenue stream / Systemize
- Q17: "What's held you back?" -> Don't know where to start / Tried courses, couldn't implement / Can't afford to invest / No time
- Q18: "What support would suit you best?" -> Free resources / Course / Group coaching / 1-on-1 / Done-for-you
- Q19: "Anything else we should know?" (open text, optional)

### Recommendation Logic

Score determines the personalized insights on the results page. Big 5 answers determine CTA routing:

- **High-qualified** (coaching/DFY preference + ambitious goal + tried-and-failed) -> Book a call
- **Mid-qualified** (course/community preference + clear goal + early stage) -> Register for webinar
- **Low-qualified** (free resources preference + just starting + budget constraint) -> Download free guide

### Email Follow-Up Strategy
Segment by qualification tier, not by score alone:
- High-qualified: Sales team follow-up + booking reminders + case studies from similar profiles
- Mid-qualified: Webinar invite + value sequence addressing their specific obstacle + upgrade path
- Low-qualified: Free resource delivery + nurture sequence + periodic re-qualification ("retake your scorecard")

### Green Lights
- Multiple offer tiers spanning free to premium
- Sales team that benefits from pre-qualified, pre-segmented leads
- High LTV per customer (justifies the longer quiz experience)
- B2B or service-based business model

### Red Flags
- Single product at a single price point (no routing needed, use Type 1)
- E-commerce with physical products (Product Match is better)
- Younger/casual demographics who won't tolerate 20 questions
- Low-ticket impulse purchases where friction kills momentum

### Common Mistakes
- Making the best practices questions too niche or technical (keep them accessible)
- Forgetting that Q18 (solution preference) must map to offers you actually sell
- Generic results page that doesn't reference their specific score and gaps
- Same CTA for all qualification levels (defeats the purpose of qualification)

---

## Decision Tree: Which Quiz Type?

```
Start here: What's the primary goal?
|
├── Convert browsers to buyers (they're close to buying)
|   ├── Multiple products? -> Product Match Quiz (Type 1)
|   ├── Multiple pricing tiers? -> Pricing Plan Quiz (Type 2)
|   └── Single product, single price? -> Skip quiz, optimize product page (use `cro`)
|
├── Increase AOV on existing buyers (post-purchase)
|   └── Have complementary products? -> Upsell Match Quiz (Type 3)
|
├── Warm up cold traffic (they're not ready to buy yet)
|   └── Need education before purchase? -> Diagnostic Quiz (Type 4)
|
└── Qualify leads for multi-tier offers (they need routing)
    └── Service/coaching/B2B with 3+ offer tiers? -> Scorecard Quiz (Type 5)
```

When in doubt, start with Type 1 (Product Match) for e-commerce or Type 5 (Scorecard) for service/coaching businesses. Type 1 produces the fastest revenue impact for product businesses. Type 5 produces the highest-quality leads for service businesses.
