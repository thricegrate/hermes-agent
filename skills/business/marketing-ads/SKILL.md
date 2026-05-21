---
name: marketing-ads
description: "When the user wants to plan, create, publish, or optimize paid advertising campaigns, especially Meta Ads. Also use when the user mentions 'campaign planner,' 'performance marketer,' 'campaign-planner,' 'performance-marketer,' 'Meta Ads,' 'Facebook Ads,' 'ad campaign,' 'ad strategy,' 'ad creative,' 'funnel strategy,' 'TOFU MOFU BOFU,' 'ad optimization,' 'ROAS,' 'ad budget,' 'campaign proposal,' 'publish campaign,' 'ad performance,' 'CPM,' 'CPC,' 'CTR,' 'retargeting,' or 'paid acquisition.' This is the combined campaign-planner + performance-marketer skill covering the full ads lifecycle from strategy through optimization."
metadata:
  version: 2.0.0
---

# Marketing Ads

You handle the full lifecycle of paid advertising campaigns, from strategic planning through publishing and ongoing optimization. The skill has two phases: Strategy/Planning (designing the campaign) and Publishing/Optimization (running and improving it).

## Prerequisites

Before running this skill, you should have:

1. **Brand Bible**: Run `/website_brand_analysis` first, or have existing brand guidelines
2. **Competitor Analysis** (optional but recommended): Run `/ads_meta` on 1-2 competitors to identify winning patterns
3. **Product Marketing Context**: If private product-marketing context notes exists, read it first

## Pipeline Position

This skill covers the last two stages of the marketing pipeline:

```
ads_analyst (research) -> head_of_marketing (brand + campaign) -> creative_director (build assets) -> marketing-ads (plan + publish + optimize)
```

---

## Phase 1: Strategy & Planning

Design a comprehensive campaign proposal based on brand guidelines and competitive intelligence.

### Step 1: Gather Context

1. **Load brand bible**: Products, pricing, voice, visual style
2. **Load competitor analysis** (if available): Winning patterns, funnel structures
3. **Identify product ladder**: Free -> Low-ticket -> High-ticket -> Enterprise
4. **Note existing assets**: What landing pages/lead magnets already exist?

### Step 2: Design Funnel Strategy

Map the customer journey:

```
TOFU (Cold Traffic)
├── Lead magnets (quiz, free course, valuable content)
├── Goal: Email capture, pixel building
└── Budget: 50-60%

MOFU (Warm Traffic, Retargeting)
├── Low-to-mid ticket offers
├── Goal: First purchase, course sales
└── Budget: 30-40%

BOFU (Hot Traffic, High Intent)
├── High-ticket / enterprise offers
├── Goal: Sales calls, team deals
└── Budget: 10-15%
```

### Step 3: Define Landing Pages

For each funnel stage, recommend landing pages:

**TOFU Landing Pages:**
- Quiz/assessment pages (high conversion, low friction)
- Free course/lead magnet pages
- Tutorial/value content pages

**MOFU Landing Pages:**
- Paid traffic variants of product pages
- More aggressive than organic pages
- Include: price anchoring, urgency, testimonials

**BOFU Landing Pages:**
- Existing sales pages
- "Book a call" pages
- Case study pages

### Step 4: Design Ad Creatives

Create 6-10 ad concepts across the funnel:

**TOFU Ads (3-4 creatives):**
- Video: Hook + problem + free offer CTA (25-35s)
- Image: Native/organic style (doesn't look like ad)
- Carousel: Value bomb / tutorial teaser

**MOFU Ads (2-3 creatives):**
- Video: Identity + agitation + solution + proof (30-40s)
- Image: Price anchoring, transformation

**BOFU Ads (1-2 creatives):**
- Video: Case study, results-focused (35-45s)
- Image: Social proof, consultation CTA

### Step 5: Write Video Scripts

For each video ad, write a full script with:

```
[TIMESTAMP] SECTION NAME
"Dialogue / voiceover text"

Visual notes: What's on screen
```

**Script structure:**
1. **Hook (0-3s)**: Pattern interrupt, curiosity, or identity call-out
2. **Problem (3-10s)**: Agitate the pain point
3. **Solution (10-20s)**: Introduce the offer
4. **Proof (20-30s)**: Testimonials, numbers, credibility
5. **CTA (last 5s)**: Clear next step

### Step 6: Define Image Ad Concepts

For each image ad, describe:
- **Concept**: What style/approach
- **Text on image**: Actual copy
- **Visual notes**: Design direction
- **Landing page**: Where it drives

**Image styles that work:**
- Native/organic (notebook, text post)
- Bold claim + price
- Before/after
- Tutorial preview
- Quote/testimonial

### Step 7: Budget & Testing Plan

**Budget allocation:**
- TOFU: 50-60%
- MOFU: 30-40%
- BOFU: 10-15%

**Testing phases:**
1. Weeks 1-2: TOFU testing, find winning lead magnet
2. Weeks 3-4: MOFU activation, first sales
3. Weeks 5-8: Optimization, scaling winners

### Step 8: Generate Proposal Outputs

Create two files:

1. **Markdown**: `{brand}-campaign-proposal.md`
2. **HTML**: `{brand}-campaign-proposal.html` (use `templates/proposal-template.html`)

Both should include:
- Executive summary
- Funnel strategy with diagram
- Landing page recommendations
- Ad creative cards (with scripts/concepts)
- Budget allocation
- Testing plan
- Approval checklist

**Save to:** `~/clawd/output/`

### Step 9: Deliver & Get Approval

Send both files to user with summary:
- Number of landing pages proposed
- Number of ad creatives
- Key strategic decisions to approve

**Include approval checklist:**
1. Overall funnel strategy
2. Landing page concepts
3. Ad creative concepts
4. Video scripts
5. Budget allocation

**Wait for approval before creating actual assets or publishing.**

---

## Phase 2: Publishing & Optimization

Take approved assets and manage them through Meta Ads Manager.

### Step 1: Pre-Flight Check

Before publishing, verify everything is ready:

```
Pre-Flight Check

Assets received:
- Landing pages: {N} pages ready
- Image ads: {N} creatives ready
- Video scripts: {N} scripts ready

Campaign structure:
- TOFU: {N} ads -> {landing page}
- MOFU: {N} ads -> {landing page}
- BOFU: {N} ads -> {landing page}

Budget allocation:
- TOFU: {X}%
- MOFU: {Y}%
- BOFU: {Z}%

Ready to create campaigns in Meta Ads Manager?
All campaigns will be created as PAUSED for your review.
```

**Wait for user confirmation before proceeding.**

### Step 2: Campaign Creation

Run `/meta_ads_publisher` to create:

1. **Campaign**: One campaign per funnel stage (or combined)
2. **Ad Sets**: Targeting, budget, placements
3. **Ads**: Creative + copy combinations

**All created as PAUSED.**

Report back with campaign structure and link to Ads Manager. Ask user to:
- Approve and activate
- Request changes
- Hold for now

### Step 3: Launch

On approval, activate campaigns:
- List all live campaigns with daily budgets
- Remind user: don't make changes for first 48-72 hours (let Meta's algorithm learn)
- Set expectation for first performance check in 24-48 hours

### Step 4: Performance Monitoring

**Daily Check (first week):**
- Spend vs budget
- CPM / CPC / CTR
- Any ads with issues (rejected, low delivery)

**Weekly Review:**
- Cost per result (lead, purchase, etc.)
- ROAS if tracking revenue
- Top performing ads
- Underperforming ads to pause

**Report format:**

```
Performance Report, Week {N}

Summary
- Total spend: ${X}
- Results: {N} {result type}
- Cost per result: ${X}
- ROAS: {X}x (if applicable)

Top Performers
1. {Ad name}: {metric} (keep scaling)
2. {Ad name}: {metric} (keep running)

Underperformers
1. {Ad name}: {metric} (recommend: pause)
2. {Ad name}: {metric} (recommend: test new creative)

Recommendations
- {Action 1}
- {Action 2}

Want me to implement these changes?
```

### Step 5: Optimization

Based on performance data:

**Quick wins:**
- Pause underperforming ads (high cost, low results)
- Increase budget on winners
- Adjust targeting based on audience insights

**Creative iterations:**
- Request new creatives from `/creative_director` based on learnings
- A/B test variations of top performers
- Refresh fatigued ads

**Scaling:**
- Duplicate winning ad sets with broader targeting
- Test new audiences
- Increase budgets gradually (20% max per change)

---

## Patterns from Competitor Analysis

When competitor analysis is available, apply these patterns:

| Pattern | How to Apply |
|---------|--------------|
| Quiz/assessment TOFU | Create a quiz lead magnet if none exists |
| Credibility stacking | Add logos/credentials in first 10s of video |
| Two-tier funnel | Separate cold and warm audiences clearly |
| Native creative | Include at least one "doesn't look like an ad" image |
| Identity-driven copy | Use "you're the kind of person who..." language |
| Price anchoring | Compare low-ticket to high-ticket alternative |

## Example Funnel Structures

### Education/Course Business
```
FREE: Crash course / Quiz / Tutorials
$200-500: Beginner course
$500-1000: Advanced course
$5k+: Coaching / Team training
```

### SaaS Business
```
FREE: Trial / Freemium / Lead magnet
$50-200/mo: Individual plan
$200-500/mo: Team plan
$1k+/mo: Enterprise
```

### Agency/Services
```
FREE: Audit / Assessment / Calculator
$500-2k: Entry service / Workshop
$5-20k: Main service package
$50k+: Retainer / Enterprise
```

## Quality Gates

### Gate 1: Pre-Publish
- [ ] All assets received and approved?
- [ ] Campaign structure makes sense?
- [ ] Budget allocation approved?
- [ ] Tracking/pixel configured?

### Gate 2: Post-Publish
- [ ] All campaigns created successfully?
- [ ] Ads approved by Meta (no rejections)?
- [ ] User reviewed in Ads Manager?

### Gate 3: Post-Launch
- [ ] Campaigns delivering?
- [ ] No unexpected issues?
- [ ] Tracking firing correctly?

### Gate 4: Optimization
- [ ] Enough data to make decisions (48-72h minimum)?
- [ ] Changes are incremental (not dramatic)?
- [ ] User approved optimization actions?

## Error Handling

**Ad rejected by Meta:**
- Review rejection reason
- Suggest creative/copy fixes
- Request revision from `/creative_director`
- Resubmit

**Low delivery:**
- Check audience size (too narrow?)
- Check bid/budget (too low?)
- Check creative quality score
- Suggest adjustments

**Tracking issues:**
- Verify pixel installation
- Check event configuration
- Test conversion tracking

## Tips for Better Campaigns

1. **Lead with strategy, not tactics**: Explain the funnel logic before listing ads
2. **Show the math**: If possible, estimate CAC, LTV, ROAS
3. **Include native creative**: At least one ad that doesn't look like an ad
4. **Write real scripts**: Don't leave placeholders, write actual dialogue
5. **Make approval easy**: Clear checklist at the end
6. **Visual mockups help**: Even text-based mockups of image ads

## Integration with Other Skills

1. **`/website_brand_analysis`**: Generate brand bible first
2. **`/meta_ads_extractor`** -> **`/meta_ads_analyser`**: Analyze competitor ads
3. **`/creative_director`**: Build assets before publishing, iterate based on performance
4. **`marketing-foundations`**: Psychology and tactics to inform creative strategy

## Sub-Skills Reference

| Skill | Purpose | When Used |
|-------|---------|-----------|
| `/meta_ads_publisher` | Create campaigns/ads in Meta | Phase 2, Step 2 |
| `/meta_ads_extractor` | Extract competitor ads | Phase 1, research |
| `/meta_ads_analyser` | Analyze competitor patterns | Phase 1, research |
