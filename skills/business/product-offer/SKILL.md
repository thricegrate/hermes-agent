---
name: product-offer
description: |
  Develops complete offer strategy: pricing, bonus stacks, OTO design, guarantees, value
  propositions, and packaging for digital products at any price point. Covers AC-funnel
  economics (frontend $5-97, mid-ticket $99-350, high-ticket $3K-$35K+) AND SaaS/subscription
  pricing (tiers, value metrics, packaging, pricing research). Use when user wants to price
  their product, design bonuses, create an offer stack, design OTOs, add a guarantee, figure
  out what to charge, structure pricing tiers, or says "price my offer," "bonus stack," "one
  time offer," "OTO," "guarantee," "value stack," "pricing strategy," "pricing tiers,"
  "freemium," "free trial," "packaging," "price increase," "value metric," "Van Westendorp,"
  "willingness to pay," "monetization," "offer-engineer," or "pricing-strategy."
---

# Product Offer

Design offers that convert and pricing that captures value. This skill combines two workflows: AC-funnel offer engineering (digital products, info products, coaching) and SaaS/subscription pricing strategy (tiers, packaging, research). Use whichever applies to the product type, or blend both for hybrid models.

## Prerequisites

- A product with a defined curriculum or feature set (from `product-architect`, `product-frontend`, or user-provided)
- Knowledge of target customer and primary problem being solved
- Optional: frontend offer brief, competitor pricing research, existing testimonials

**Check for product marketing context first:**
If private product-marketing context notes exists, read it before asking questions. Use that context and only ask for information not already covered.

---

## Part 1: AC-Funnel Offer Engineering

Use this path for digital products, info products, coaching, and service-based offers where you control the price and there is a defined product ladder.

### Step 0: Pre-Launch Economics Check (For Content-Driven Offers)

Before selecting pricing or building creative, run 3 calculations to validate the offer economics. This step is mandatory when the primary acquisition channel is content (UGC, organic social, paid social). Skip for offers sold through warm channels (existing list, referrals, direct sales).

**3 calculations:**
1. **Maximum Rational Content Investment** -- What's the most you should spend on content production per month? If your planned production cost exceeds this number, the offer needs repositioning.
2. **Cold Traffic Offer Fit Check** -- Does the offer have the characteristics that convert cold social traffic? ($30-150 first purchase, specific transformation, unique mechanism, low friction)
3. **Revenue Target Reverse Calculator** -- How many content pieces does your specific offer require to hit the revenue target? Higher AOV + quiz funnel = dramatically less content needed.

**Full calculations, examples, and scale decision thresholds:** See `references/pre-launch-economics.md`

If the numbers don't work, adjust pricing, funnel architecture (add quiz funnel via `quiz-funnel`), or offer structure before proceeding to Step 1.

### Step 1: Select Pricing Tier

For Brunson's Value Ladder and New Opportunity frameworks, see `references/brunson-frameworks.md`.

Five pricing tiers covering the full Automatic Clients product ladder:

| Tier | Price Range | Product Type | Examples |
|------|------------|--------------|----------|
| Tier 0 (AC Frontend) | $5-47 | Authority Book / Low-Ticket Entry | eBook, short book, mini toolkit (AC break-even model) |
| Tier 1 | $9-99 | Single Asset/Template | Ultimate guide, swipe file, email course, template pack |
| Tier 2 | $99-199 | Bundle of Assets | Bundle of eBooks, guides, swipe files, or template packs |
| Tier 3 | $199-350 | Full Text & Video Course | Complete course with modules, lessons, exercises |
| Tier 4 (High-Ticket) | $3,000-35,000+ | Coaching / DFY / Mastermind | Group program, 1:1 coaching, done-for-you service |

**Tier selection depends on the funnel position:**
- **AC Frontend (Tier 0)**: If coming from `product-frontend` with the Authority Book format. The $350 default does NOT apply. Price for maximum buyer volume, not per-unit profit.
- **Standalone product (Tier 1-3)**: Default recommendation is $350 (top of Tier 3). This is the sweet spot for stand-alone digital products.
- **Backend offer (Tier 4)**: Use the 3 Levels of Customers framework (see `references/pricing-frameworks.md`).

**Why $350 for Tier 3:**
- Below $350: you're undercharging (people would have bought anyway)
- Above $350: crosses the "impulse buy" threshold, requires more deliberation
- At $350: maximizes revenue per sale while staying in low-ticket territory

**Why $5-47 for Tier 0 (AC Frontend):**
- The goal is NOT per-unit profit. The goal is buyer volume.
- Revenue comes from OTOs (break even on ad spend) and backend ascension (profit).
- See `product-frontend/references/ac-formula.md` for the economics.

### Step 2: Backward-Plan the Value Justification

Start with the price, work backward to justify it.

**Process:**
1. Set price at $350 (or chosen tier)
2. Ask: "What does my customer need to accomplish to make $350 feel like a no-brainer?"
3. Calculate the 5x-10x upside:
   - If course helps them make $1,750-$3,500+ in value, $350 is "laughably cheap"
   - Value can be: money earned, money saved, time saved, stress reduced, status gained

**Output format:**
```
Price: $[X]
Customer ROI: $[X] (5x-10x of price)
ROI Breakdown:
- [Money earned/saved]: $[X]
- [Time saved]: [X hours] = $[X equivalent]
- [Status/opportunity gained]: [description]
```

### Step 2b: Design OTO Stack (If Applicable)

If the product is a frontend offer (Tier 0 or Tier 1), design one-time offers presented immediately after purchase. Use `templates/oto-brief.md`.

**OTO Design Rules:**
- **OTO 1**: Complements the frontend. Solves the next logical problem after the initial purchase. Priced at 1.5-3x the frontend price.
- **OTO 2**: Addresses a related need or is a downsell. Priced at 0.5-1x the frontend price.
- Each OTO must deliver standalone value
- OTO pages: single offer, single CTA, urgency copy ("this disappears when you leave")

**OTO Pricing Examples:**

| Frontend Price | OTO 1 Price | OTO 2 Price |
|---------------|-------------|-------------|
| $5.60 | $9.40-$17 | $5-$9.99 |
| $27 | $40-$81 | $14-$27 |
| $47 | $70-$141 | $24-$47 |
| $97 | $145-$291 | $49-$97 |

**Revenue math**: Average revenue per buyer with OTOs = Frontend price + (OTO1 price x 15-25% take rate) + (OTO2 price x 5-10% take rate). This number must exceed your CPA for the AC model to work.

### Step 2c: Select Guarantee Type

Every offer should have a guarantee. The type depends on the price point and product type.

**4 Guarantee Types:**

| Type | What It Is | Best For | Example |
|------|-----------|----------|---------|
| Unconditional | Full refund, no questions asked, within X days | Low-ticket ($5-99). Removes all risk. | "30-day money-back guarantee. No questions asked." |
| Conditional | Full refund IF they complete specific actions and don't get results | Mid-ticket ($99-350). Ensures buyer effort. | "Complete all modules and exercises within 60 days. If you don't see results, full refund." |
| Performance-Based | Specific measurable outcome guaranteed or money back | High-ticket ($3K+). Shows confidence. | "If you don't land 3 clients in 90 days using our system, we refund 100%." |
| Anti-Guarantee | No refund, but strong justification for why | Premium/limited offers. Screens for committed buyers. | "Due to the personalized nature of this service, all sales are final." |

**Selection guide:**
- Tier 0-1 ($5-99): Always unconditional. The risk is too low to justify anything else.
- Tier 2-3 ($99-350): Conditional preferred. Shows you believe in the product AND expect effort.
- Tier 4 ($3K+): Performance-based if you can back it up. Otherwise conditional.

### Step 3: Design the Bonus Stack

Bonuses make the price feel like a steal. Every bonus MUST have a dollar value attached.

**5 Proven Bonus Types:**

| Bonus Type | What It Is | Example |
|-----------|-----------|---------|
| Templates | Bundle of assets to automate/accomplish core promise | "The [X] Template Pack" |
| AI Prompts | Bundle of AI prompts to help accomplish core promise | "The [X] AI Prompt Library" |
| Automations | Walkthroughs of automations for core promise | "The [X] Automation Toolkit" |
| Swipe Files | Curated collection of proven examples | "The [X] Swipe File" |
| Behind-the-Scenes | Walkthrough of your proprietary process | "Inside My [X] Process" |

**Rules:**
- Design 2-3 bonuses
- Price each as if sold separately (reference the 3 tiers above)
- Total bonus value should EXCEED the product price
- Example: Product = $350, Bonus 1 = $149, Bonus 2 = $99, Bonus 3 = $97 = $345 in "free" bonuses

### Step 3b: Contrarian Positioning

Before writing the value proposition, identify what every competitor in this space claims. Then position the offer differently.

**Process:**
1. List what competitors promise (faster, cheaper, easier, more features)
2. Identify the consensus claim (what do they ALL say?)
3. Find your contrarian angle: what do you do DIFFERENTLY? What do you believe that contradicts the industry consensus?
4. Build the value proposition around the contrarian angle, not the consensus claim

**Ask the user:**
> "What do most products in this space promise? What do you do differently? What do you believe about [problem space] that most competitors get wrong? What personal experience or specific result can we lead with?"

### Step 4: Write the Value Proposition

Before writing the value proposition, define your Big Domino Statement -- the ONE belief that makes all other objections irrelevant. See `references/brunson-frameworks.md` (Section 4).

Compile the offer into a clear value statement:

```
## Offer Stack

### Core Product: [Product Name] - $[Price]
[One sentence: what it is and the transformation it delivers]

### What's Included:
- Module 1: [Name] - [What they'll learn/do]
- Module 2: [Name] - [What they'll learn/do]
- ...

### Bonuses (Included Free):

**Bonus #1: [Name]** ($[Value] value)
[1-2 sentences: what it is and why it's valuable]

**Bonus #2: [Name]** ($[Value] value)
[1-2 sentences: what it is and why it's valuable]

**Bonus #3: [Name]** ($[Value] value)
[1-2 sentences: what it is and why it's valuable]

### Total Value: $[Product + All Bonuses]
### Your Price: $[Actual Price]
### You Save: $[Difference]
```

### Step 5: Write Price Anchoring Statement

Create the copy that frames the price in context of value:

**Template:**
"[Product Name] gives you everything you need to [transformation]. If this product helps you [specific measurable outcome], that's a [X]x return on a $[price] investment. And with $[bonus total] in bonuses included free, you're getting $[total value] of proven resources for just $[price]."

### Step 5b: Kennedy Offer Stack Gate (Mandatory)

Before finalizing any offer, run the Kennedy Offer Stack checklist from `references/kennedy-offer-engineering.md`. Every "no" is a conversion leak.

- [ ] Value build happens before price reveal
- [ ] 2-3 bonuses, each tied to a specific buying objection
- [ ] Real deadline with a specific date (not "limited time")
- [ ] Fast-action incentive for early buyers
- [ ] Penalty for late response (price increase or bonus removal)
- [ ] Guarantee selected and written as a selling tool, not fine print
- [ ] Thud factor created (visual volume of what they receive)
- [ ] Take-away selling language included (mid/high ticket)
- [ ] P.S. restates the offer and deadline
- [ ] Ascension path defined (what do they buy next?)

For full frameworks: the 4 guarantee types, 9 premium pricing failures, the ascension ladder, and the complete 7-component offer stack are in `references/kennedy-offer-engineering.md`.

### Step 6: Economics Analysis (AC Model)

If this is a frontend offer in an AC funnel, calculate the unit economics:

```
Frontend Revenue Per Buyer:
  Book/product sale: $[X]
  + OTO 1 (at [Y]% take rate): $[Z]
  + OTO 2 (at [Y]% take rate): $[Z]
  = Average Revenue Per Buyer: $[TOTAL]

Customer Acquisition Cost (CPA):
  Target CPA from ads: $[X]
  Break-even?: [Yes/No] (Revenue Per Buyer >= CPA)

Backend Economics:
  Backend price: $[X]
  Expected ascension rate: [Y]% of frontend buyers
  Revenue per 100 frontend buyers: $[X] frontend + [Y] x $[Z] backend = $[TOTAL]
  Effective value per frontend buyer: $[TOTAL / 100]
  Maximum affordable CPA: $[Effective value per buyer]
```

This analysis determines whether the funnel is economically viable BEFORE building it. If the numbers don't work, adjust pricing, OTOs, or backend offer before proceeding.

---

## Part 2: SaaS & Subscription Pricing

Use this path for SaaS products, subscription services, marketplaces, and any recurring-revenue model where tiers, packaging, and value metrics matter. For deep-dive methodology, see `references/saas-pricing.md`.

### Value-Based Pricing

Price should be based on value delivered, not cost to serve:

- **Customer's perceived value**: The ceiling
- **Your price**: Between alternatives and perceived value
- **Next best alternative**: The floor for differentiation
- **Your cost to serve**: Only a baseline, not the basis

**Key insight:** Price between the next best alternative and perceived value.

### Value Metrics

The value metric is what you charge for. It should scale with the value customers receive.

**Good value metrics:**
- Align price with value delivered
- Are easy to understand
- Scale as customer grows
- Are hard to game

Ask: "As a customer uses more of [metric], do they get more value?" If yes, good metric. If no, price doesn't align with value.

### Good-Better-Best Tier Framework

**Good tier (Entry):** Core features, limited usage, low price
**Better tier (Recommended):** Full features, reasonable limits, anchor price
**Best tier (Premium):** Everything, advanced features, 2-3x Better price

For detailed tier structures and persona-based packaging, see `references/saas-pricing.md`.

### When to Raise Prices

**Market signals:** Competitors raised prices, prospects don't flinch, "so cheap!" feedback
**Business signals:** Very high conversion (>40%), very low churn (<3%), strong unit economics
**Product signals:** Significant value added since last pricing, product more mature

**Price Increase Strategies:**
1. Grandfather existing customers (new price for new only)
2. Delayed increase (announce 3-6 months out)
3. Tied to value (raise price but add features)
4. Plan restructure (change plans entirely)

### Pricing Page Best Practices

- Clear tier comparison table with recommended tier highlighted
- Monthly/annual toggle with 17-20% annual discount
- Feature comparison, who each tier is for, FAQ, trust signals
- **Psychology:** Anchoring (show higher-priced first), decoy effect (middle = best value), charm pricing ($49 vs $50 for value), round pricing ($50 vs $49 for premium)

### Pricing Research Methods

**Van Westendorp:** Four questions to identify acceptable price range (too expensive, too cheap, expensive but might consider, a bargain). See `references/saas-pricing.md` for full methodology.

**MaxDiff Analysis:** Identifies which features customers value most. Results inform tier packaging.

### SaaS Pricing Checklist

Before setting prices:
- [ ] Defined target customer personas
- [ ] Researched competitor pricing
- [ ] Identified your value metric
- [ ] Conducted willingness-to-pay research
- [ ] Mapped features to tiers
- [ ] Chosen number of tiers and differentiated clearly
- [ ] Set price points based on research
- [ ] Created annual discount strategy

---

## Hormozi Pricing Frameworks

Deep pricing and offer frameworks from $100M Pricing/LTV/Offers Playbooks. See `references/hormozi-pricing-playbook.md` for full detail.

### Frameworks Available:

| Framework | What It Does | When to Use |
|-----------|-------------|-------------|
| **Business Genie** | Proves 2x price = 6x profit mathematically | Client asks "how to double revenue" -- pricing first |
| **10 Instant Profit Pricing Plays** | 10 tactical changes adding 26-64% revenue | Quick wins, no new customers needed |
| **RAISE Letter** | 5-section framework for communicating price raises | Client needs to raise prices on existing customers |
| **Crazy Eight LTV** | 8 ways to increase lifetime value | LTV optimization, revenue per customer |
| **Value Grid** | Replaces linear Value Ladder with multi-entry grid | Non-linear product portfolio design |
| **CFA Deep (3 Levels/3 Levers)** | Customer Financed Acquisition with LTGP formulas | Scaling economics, break-even analysis |
| **Vicious/Virtuous Cycle** | Two opposing spirals from pricing direction | Diagnosing why client is in a price race to bottom |
| **5-Step Grand Slam Creation** | Sequential offer building process | New offer design from scratch |
| **Guarantee Stacking** | Multi-layer guarantee construction | Strengthening offer risk reversal |
| **Bonus Bullets (11 Rules)** | Rules for bonus presentation | Auditing bonus stack effectiveness |

### Integration with Existing Steps:

- **Step 1 (Pricing Tier):** Use Business Genie math to justify premium pricing. Reference 16 Rules of Pricing for decision framework.
- **Step 2 (Value Justification):** Use CFA with 3 Levels/3 Levers for break-even analysis. Lookback Window for subscription pricing.
- **Step 2c (Guarantee):** Use Guarantee Stacking for multi-layer guarantee construction.
- **Step 3 (Bonus Stack):** Apply Bonus Bullets 11 Rules. Use Customer Surplus model for value-price gap.

---

## Cole's Offer Creation System

Nicolas Cole's 10-Point Offer Creation Checklist, 20 Product Naming Conventions, and AI prompts for offer generation. Complements Hormozi/Kennedy with tangibility emphasis and practical naming system. See `references/cole-offer-creation.md`.

**YC pricing psychology:** Value-based pricing (price on value, not costs), three-tier Good/Better/Best strategy, Willingness to Pay research methods (Van Westendorp, behavior-based, "Shut Up" test), price elasticity by price point, and why most founders underprice. Complements Hormozi value stacking with YC's pricing research rigor. See `references/yc-hale-pricing.md`.

---

## Integration

- **Input from:** `product-architect` (curriculum structure for offer stack), `product-frontend` (format, price range, OTO requirements)
- **Output feeds into:** `sales-page-writer` (offer details + OTO copy + guarantee section), `email-sequence` (pricing/value used in objection-handling emails), `high-ticket-closer` (backend offer details for sales scripts), `launch-ops` (OTO setup requirements)

### Related Skills

- `growth-retention`: Cancel flows, save offers, reducing revenue churn
- `cro`: Optimizing pricing page conversion and testing pricing changes
- `copy-writing`: Pricing page copy
- `marketing-foundations`: Pricing psychology principles
