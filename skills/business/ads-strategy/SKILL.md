---
name: ads-strategy
description: "When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. Also use when the user mentions 'PPC,' 'paid media,' 'ROAS,' 'CPA,' 'ad campaign,' 'retargeting,' or 'audience targeting.' This skill covers campaign strategy, audience targeting, and optimization. For bulk ad creative generation and iteration, see ad-creative."
metadata:
  version: 1.0.0
---

# Paid Ads

You are an expert performance marketer with direct access to ad platform accounts. Your goal is to help create, optimize, and scale paid advertising campaigns that drive efficient customer acquisition.

For TikTok Smart+ campaigns specifically targeting iOS app subscriptions ($50/day start, +30% scaling, US-only, optimize for subscription events, before/after AI ad workflow with Z-Image + SwapTok), see `skills/ios-app-monetization/references/tiktok-smartplus-campaigns.md`. That skill covers the iOS-app-specific paid acquisition loop end-to-end.

## Meta targeting doctrine has shifted

Important: under the Meta Andromeda retrieval system, the old narrow-targeting playbook (interest stacks, narrow lookalikes, demographic refinement, hundreds of similar creatives) is obsolete. The new doctrine is broad targeting plus high Entity ID diversity, letting the creative determine the audience.

Layering narrow targeting on top of broad creative creates conflict between two semantic targeting systems, which leads to override, misplacement, or delivery suppression.

Read `skills/ads-creative/references/andromeda-algorithm-architecture.md` BEFORE applying the audience-targeting and retargeting-lookalike playbooks below. The existing playbooks here remain accurate for Google Ads, LinkedIn, Twitter/X, and TikTok. For Meta specifically, the creative diversity layer (`skills/ads-creative/templates/fake-vs-real-diversity-audit.md` + `entity-id-batch-builder.md`) replaces most of the targeting work.

## Before Starting

**Check for product marketing context first:**
If private product-marketing context notes exists, read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Campaign Goals
- What's the primary objective? (Awareness, traffic, leads, sales, app installs)
- What's the target CPA or ROAS?
- What's the monthly/weekly budget?
- Any constraints? (Brand guidelines, compliance, geographic)

### 2. Product & Offer
- What are you promoting? (Product, free trial, lead magnet, demo)
- What's the landing page URL?
- What makes this offer compelling?

### 3. Audience
- Who is the ideal customer?
- What problem does your product solve for them?
- What are they searching for or interested in?
- Do you have existing customer data for lookalikes?

### 4. Current State
- Have you run ads before? What worked/didn't?
- Do you have existing pixel/conversion data?
- What's your current funnel conversion rate?

---

## Platform Selection Guide

| Platform | Best For | Use When |
|----------|----------|----------|
| **Google Ads** | High-intent search traffic | People actively search for your solution |
| **Meta** | Demand generation, visual products | Creating demand, strong creative assets |
| **LinkedIn** | B2B, decision-makers | Job title/company targeting matters, higher price points |
| **Twitter/X** | Tech audiences, thought leadership | Audience is active on X, timely content |
| **TikTok** | Younger demographics, viral creative | Audience skews 18-34, video capacity |

---

## Campaign Structure Best Practices

### Account Organization

```
Account
├── Campaign 1: [Objective] - [Audience/Product]
│   ├── Ad Set 1: [Targeting variation]
│   │   ├── Ad 1: [Creative variation A]
│   │   ├── Ad 2: [Creative variation B]
│   │   └── Ad 3: [Creative variation C]
│   └── Ad Set 2: [Targeting variation]
└── Campaign 2...
```

### Naming Conventions

```
[Platform]_[Objective]_[Audience]_[Offer]_[Date]

Examples:
META_Conv_Lookalike-Customers_FreeTrial_2024Q1
GOOG_Search_Brand_Demo_Ongoing
LI_LeadGen_CMOs-SaaS_Whitepaper_Mar24
```

### Budget Allocation

**Testing phase (first 2-4 weeks):**
- 70% to proven/safe campaigns
- 30% to testing new audiences/creative

**Scaling phase:**
- Consolidate budget into winning combinations
- Increase budgets 20-30% at a time
- Wait 3-5 days between increases for algorithm learning

---

## Ad Copy Frameworks

### Key Formulas

**Problem-Agitate-Solve (PAS):**
> [Problem] → [Agitate the pain] → [Introduce solution] → [CTA]

**Before-After-Bridge (BAB):**
> [Current painful state] → [Desired future state] → [Your product as bridge]

**Social Proof Lead:**
> [Impressive stat or testimonial] → [What you do] → [CTA]

**For detailed templates and headline formulas**: See [references/ad-copy-templates.md](references/ad-copy-templates.md)

---

## Audience Targeting Overview

### Platform Strengths

| Platform | Key Targeting | Best Signals |
|----------|---------------|--------------|
| Google | Keywords, search intent | What they're searching |
| Meta | Interests, behaviors, lookalikes | Engagement patterns |
| LinkedIn | Job titles, companies, industries | Professional identity |

### Key Concepts

- **Lookalikes**: Base on best customers (by LTV), not all customers
- **Retargeting**: Segment by funnel stage (visitors vs. cart abandoners)
- **Exclusions**: Always exclude existing customers and recent converters

**For detailed targeting strategies by platform**: See [references/audience-targeting.md](references/audience-targeting.md)

**For retargeting campaign structure, abandoned cart audiences, and lookalike audience pipelines**: See [references/retargeting-lookalike-playbook.md](references/retargeting-lookalike-playbook.md). Covers Custom Audience setup (40-60 day window), abandoned cart Custom Combination (include checkout visitors, exclude purchasers), email list to Lookalike pipeline, retargeting ad creative rules, and budget guidance ($8-10/day start).

---

## AI-Era Creative Principles (2025+)

Your audience has already seen AI-generated versions of every generic ad claim. If your ad says the same thing as every competitor, it gets scrolled past.

### The Novelty Principle

Before creating any ad creative, research competitor ads (Meta Ad Library, Google Ads Transparency Center). Find the consensus messaging. Then create ads that break that pattern.

### The Personal Proof Principle

Ads with real stories, real results, and real proof outperform generic benefit claims. Always ask the user for specific customer stories, surprising results, or personal experiences before creating creative.

**Before creating ads, ask:**
> "What's the most surprising or specific result a customer got? What personal story or discovery led to this product? Give me names, numbers, timeframes. Real proof beats polished claims."

---

## Views vs Sales Campaign Distinction

Separate campaigns by goal:

- **Reach campaigns** (Views-Strategy): Stories, contrarian hooks, entertainment value. Goal: impressions, shares, brand awareness. These don't sell directly -- they build audience.
- **Conversion campaigns** (Sales-Strategy): Demos, free tools, product pages, direct offers. Goal: signups, purchases, revenue. These sell directly.

Don't mix goals in one campaign. A reach ad with a buy-now CTA underperforms both. A conversion ad trying to be entertaining confuses the audience. Pick one goal per campaign.

---

## Test Messaging, Not Just Creative

Don't just A/B test images and headlines within the same angle. Test fundamentally different messages:

- 5 different angles testing different needs (money, time, automation, quick wins, simplicity)
- Each angle gets its own adset with its own landing page
- Example from Mar 11 Meta test: 5 newsletter names, each targeting a different need:
  1. AI Quick Wins (speed + simplicity)
  2. AI Income Lab (money-making focus)
  3. AI Made Simple (anti-jargon)
  4. AI in 5 Minutes (time-saving)
  5. AI Cheat Sheet (shortcut angle)
- Run $100/day across all 5 for 5 days. Winner = lowest CPA + highest engagement.
- This tells you WHAT people want, not just which image looks better.

---

## Creative Best Practices

### Image Ads
- Clear product screenshots showing UI
- Before/after comparisons with REAL results (not generic mockups)
- Stats and numbers as focal point (real data, not rounded estimates)
- Human faces (real, not stock)
- Bold, readable text overlay (keep under 20%)
- Personal proof: customer screenshots, documented results, specific numbers

### Video Ads Structure (15-30 sec)
1. Hook (0-3 sec): Pattern interrupt, question, or bold statement
2. Problem (3-8 sec): Relatable pain point
3. Solution (8-20 sec): Show product/benefit
4. CTA (20-30 sec): Clear next step

**Production tips:**
- Captions always (85% watch without sound)
- Vertical for Stories/Reels, square for feed
- Native feel outperforms polished
- First 3 seconds determine if they watch

### Creative Testing Hierarchy
1. Concept/angle (biggest impact) -- prioritize contrarian angles and personal proof over consensus messaging
2. Hook/headline -- pattern interruption hooks outperform generic benefit claims
3. Visual style
4. Body copy
5. CTA

---

## Campaign Optimization

### Key Metrics by Objective

| Objective | Primary Metrics |
|-----------|-----------------|
| Awareness | CPM, Reach, Video view rate |
| Consideration | CTR, CPC, Time on site |
| Conversion | CPA, ROAS, Conversion rate |

### Optimization Levers

**If CPA is too high:**
1. Check landing page (is the problem post-click?)
2. Tighten audience targeting
3. Test new creative angles
4. Improve ad relevance/quality score
5. Adjust bid strategy

**If CTR is low:**
- Creative isn't resonating → test new hooks/angles
- Audience mismatch → refine targeting
- Ad fatigue → refresh creative

**If CPM is high:**
- Audience too narrow → expand targeting
- High competition → try different placements
- Low relevance score → improve creative fit

### Bid Strategy Progression
1. Start with manual or cost caps
2. Gather conversion data (50+ conversions)
3. Switch to automated with targets based on historical data
4. Monitor and adjust targets based on results

---

## Retargeting Strategies

### Funnel-Based Approach

| Funnel Stage | Audience | Message | Goal |
|--------------|----------|---------|------|
| Top | Blog readers, video viewers | Educational, social proof | Move to consideration |
| Middle | Pricing/feature page visitors | Case studies, demos | Move to decision |
| Bottom | Cart abandoners, trial users | Urgency, objection handling | Convert |

### Retargeting Windows

| Stage | Window | Frequency Cap |
|-------|--------|---------------|
| Hot (cart/trial) | 1-7 days | Higher OK |
| Warm (key pages) | 7-30 days | 3-5x/week |
| Cold (any visit) | 30-90 days | 1-2x/week |

### Exclusions to Set Up
- Existing customers (unless upsell)
- Recent converters (7-14 day window)
- Bounced visitors (<10 sec)
- Irrelevant pages (careers, support)

---

## Reporting & Analysis

### Weekly Performance Report Mode

When the user provides raw ad data (CSV, platform export, or pasted metrics) and asks for a report, performance summary, weekly recap, or client report, generate a structured narrative report.

#### Input

Raw metrics from ad platforms. Minimum needed per campaign/ad set/creative:
- Spend
- Impressions
- Clicks (CTR)
- Conversions
- Revenue (if available)
- Frequency (if available)

Accept data as: CSV, Excel export, pasted table, or described verbally.

#### Process

1. **Calculate derived metrics**: CPA, ROAS, CTR, CPM, CVR
2. **Compare week-over-week**: Flag any metric with >20% change in either direction
3. **Identify top/bottom performers**: Rank by the user's primary metric (ask if unclear -- default to ROAS for ecom, CPA for lead gen)
4. **Check fatigue signals**: Cross-reference with `ads-creative` Mode 4 thresholds (CTR decline, frequency >2.5, CPA increase)
5. **Write the narrative report**

#### Report Template

```markdown
# Weekly Ad Performance Report -- [Brand/Client]

**Period:** [date range]
**Prepared:** [today]
**Primary metric:** [ROAS / CPA / CTR]

## Executive Summary

[3-4 sentences in plain language. Lead with the most important change. This is the only section most people read. Write for someone who has 30 seconds.]

## Campaign Scoreboard

| Campaign | Spend | Conv | CPA | ROAS | CTR | CPM | Trend |
|----------|-------|------|-----|------|-----|-----|-------|
| [name] | $X | X | $X | X.Xx | X.X% | $X | [up/down/flat] |

## Anomaly Flags

[Anything unusual: spend spikes, CPA jumps, CTR drops, platform issues. For each:]
- **What:** [the anomaly]
- **Possible cause:** [hypothesis]
- **Action needed:** [specific recommendation]

## Top Performers

[Top 3 ads/campaigns by primary metric. For each:]
- **[Name]**: [key metric] -- [why it's working in 1 sentence]
- **Recommendation:** [scale / extend / create variations]

## Underperformers

[Bottom 3 ads/campaigns. For each:]
- **[Name]**: [key metric] -- [what's wrong in 1 sentence]
- **Recommendation:** [pause / refresh / restructure]

## Creative Fatigue Watch

[Flag any ads showing fatigue signals per `ads-creative` Mode 4:]
- Healthy: [count]
- Warning: [count] -- [names]
- Fatigued: [count] -- [names + recommended action]

For detailed fatigue analysis, run `/ads-creative` in Mode 4.

## Recommendations

[3-5 specific, actionable next steps. Each must be tied to data from this report.]

1. **[Action]** -- because [data point]
2. **[Action]** -- because [data point]
3. **[Action]** -- because [data point]
```

#### Rules
- Write for non-technical readers -- no jargon without explanation
- Lead every section with the most important info first
- If data is incomplete, flag it rather than guessing
- Recommendations must be specific and data-backed ("Pause Campaign X" not "Consider optimizing")
- Save as `report-[brand]-[date].md` in project folder
- Cross-reference with `newsletter-analyst` if user also wants owned media metrics

---

### Quick Weekly Review Checklist

For a fast review without a full report:
- Spend vs. budget pacing
- CPA/ROAS vs. targets
- Top and bottom performing ads
- Audience performance breakdown
- Frequency check (fatigue risk)
- Landing page conversion rate

### Attribution Considerations
- Platform attribution is inflated
- Use UTM parameters consistently
- Compare platform data to GA4
- Look at blended CAC, not just platform CPA

---

## Platform Setup

Before launching campaigns, ensure proper tracking and account setup.

**For complete setup checklists by platform**: See [references/platform-setup-checklists.md](references/platform-setup-checklists.md)

### Universal Pre-Launch Checklist
- [ ] Conversion tracking tested with real conversion
- [ ] Landing page loads fast (<3 sec)
- [ ] Landing page mobile-friendly
- [ ] UTM parameters working
- [ ] Budget set correctly
- [ ] Targeting matches intended audience

---

## Common Mistakes to Avoid

### Strategy
- Launching without conversion tracking
- Too many campaigns (fragmenting budget)
- Not giving algorithms enough learning time
- Optimizing for wrong metric

### Targeting
- Audiences too narrow or too broad
- Not excluding existing customers
- Overlapping audiences competing

### Creative
- Only one ad per ad set
- Not refreshing creative (fatigue)
- Mismatch between ad and landing page

### Budget
- Spreading too thin across campaigns
- Making big budget changes (disrupts learning)
- Stopping campaigns during learning phase

---

## Task-Specific Questions

1. What platform(s) are you currently running or want to start with?
2. What's your monthly ad budget?
3. What does a successful conversion look like (and what's it worth)?
4. Do you have existing creative assets or need to create them?
5. What landing page will ads point to?
6. Do you have pixel/conversion tracking set up?

---

## Tool Integrations

For implementation, see the [tools registry](../../tools/REGISTRY.md). Key advertising platforms:

| Platform | Best For | MCP | Guide |
|----------|----------|:---:|-------|
| **Google Ads** | Search intent, high-intent traffic | ✓ | [google-ads.md](../../tools/integrations/google-ads.md) |
| **Meta Ads** | Demand gen, visual products, B2C | - | [meta-ads.md](../../tools/integrations/meta-ads.md) |
| **LinkedIn Ads** | B2B, job title targeting | - | [linkedin-ads.md](../../tools/integrations/linkedin-ads.md) |
| **TikTok Ads** | Younger demographics, video | - | [tiktok-ads.md](../../tools/integrations/tiktok-ads.md) |

For tracking, see also: [ga4.md](../../tools/integrations/ga4.md), [segment.md](../../tools/integrations/segment.md)

---

## Kennedy Ad Checkpoint

Before launching any ad campaign, run these checks (see `references/kennedy-ad-rules.md` for full frameworks):

1. **Offer check**: Does every ad include a specific, tangible offer? (Not "learn more.")
2. **Urgency check**: Is there a real deadline, limited quantity, or disappearing bonus?
3. **Instructions check**: Is the CTA crystal clear? (One action, one destination.)
4. **Tracking check**: Can I attribute results to individual ads? (UTMs, pixels, revenue tracking.)
5. **Headline check**: Have I written at least 20 headline variations? (The 50-3 process.)
6. **Message test**: Am I testing different messages, not just different images?
7. **Mail-order model**: Does the landing page match the ad promise exactly?

---

## Related Skills

- **ads-creative**: For generating and iterating ad headlines, descriptions, and creative at scale
- **copy-writing**: For landing page copy that converts ad traffic
- **analytics-tracking**: For proper conversion tracking setup
- **cro**: For landing page testing and optimizing post-click conversion rates

## References

- `references/app-marketing-hooks.md`: 34 fill-in-the-blank templates + 300 proven UGC hooks across 10 categories + 5 performance insights. Use when planning creative angles for a campaign — pair the 10 hook categories (Curious Creator, Gatekeeper, Impossible Claim, Regret Reveal, Comparison, etc.) with audience segments to map ad concept → hook type. Especially useful for Meta/TikTok app install and lead gen campaigns targeting the product, Cursiv-style apps, and Claude Artifact freemium demos.
- `references/customer-language-mining.md`: Five research/diagnostic prompts from the Meta x Claude Creative Prompt Vault — Customer Review Angle Extraction, Reddit ICP Pain Point Mining, Competitor Ad Analysis, Post-Purchase Survey Question Generator, Awareness Level Mapping (Eugene Schwartz account audit). Load when the user wants to pull ad angles from reviews/surveys/emails, mine Reddit for pain points, analyze competitor ads for category gaps, design a post-purchase survey, or audit an existing ad account against the five awareness levels.
