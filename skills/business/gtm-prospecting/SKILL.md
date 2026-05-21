---
name: gtm-prospecting
description: |
  Find and tier net-new accounts that match your ICP into a prioritized prospect list.
  Use when user asks to "find prospects", "build a prospect list", "find target accounts",
  "account sourcing", "pipeline building", "find companies to sell to", "prospecting",
  or "build a target list". Also trigger when user needs to identify new accounts for
  outbound, ABM programs, or pipeline generation. Run gtm-icp-definition first if no ICP exists.
---

# GTM Prospecting

Find and prioritize net-new accounts to pursue. Prospecting is not list-building -- it is the disciplined process of identifying companies that have the right characteristics, in the right moment, to become customers. The output is a prioritized, qualified prospect list with enough context on each account to know why it belongs there and what the first move is.

## Context Gathering

Before starting, collect from the user:

- **What you sell** -- product/service, value proposition, average deal size
- **Your ICP** -- industry, company size, geography, growth stage, business model, tech stack signals, intent signals
- **Disqualifiers** -- signals that make a company a clear no
- **Buying triggers** -- events that create urgency (funding, leadership hire, product launch, etc.)
- **Personas to target** -- primary and secondary titles
- **Existing pipeline & customers** -- best customers (for lookalikes), segments already covered, accounts to exclude
- **Prospecting goal** -- what you're trying to achieve (fill Q2 pipeline, break into fintech, find 20 ABM accounts, etc.)

## What This Skill Produces

A prioritized, tiered prospect list with fit reasoning, timing signals, named contacts, and a defined next move for each account.

---

## Prospecting Methodology

### Step 1 -- Define the Ideal Account Profile

Sharpen targeting criteria into a precise profile. Broad targeting wastes time. The best prospecting lists are small and accurate, not large and approximate.

**Firmographic criteria (who they are):**
- Industry / sub-vertical
- Headcount range
- Revenue range
- Geography
- Ownership type (VC-backed, PE-backed, public, bootstrap)
- Business model

**Technographic criteria (what they use):**
- Platforms and tools that indicate fit
- Tools that indicate they have the problem you solve
- Tools that indicate they're solving it with a competitor (decide: displacing or disqualifying?)

**Situational criteria (where they are):**
- Funding stage and recency
- Growth rate signals (headcount change over 6-12 months)
- Hiring patterns (what roles?)
- Recent events (launches, expansions, leadership changes)

**Behavioral criteria (what they're doing):**
- Content consumption in your category
- Job postings signaling a problem you solve
- Conference attendance in your space
- Public statements about relevant priorities

> Separate must-haves from nice-to-haves. A must-have disqualifies if absent. A nice-to-have raises or lowers priority.

### Step 2 -- Source Identification

Use multiple sources -- no single source is complete.

| Source Type | Best for | Watch out for |
|-------------|----------|---------------|
| Company databases (Apollo, Clay, ZoomInfo) | Firmographic filtering at scale | Data staleness, headcount inflation |
| LinkedIn Sales Navigator | Title + company filters, recent activity | Limited to what's on LinkedIn |
| G2 / Capterra / review sites | Companies evaluating competitor tools | Only captures companies that write reviews |
| Job boards | Companies hiring for roles that signal pain | Lags real hiring decisions by weeks |
| News & PR | Funding, M&A, expansion, leadership changes | Requires ongoing monitoring |
| Conference attendee lists | Concentrated ICP density | Requires access or research |
| Your CRM | Churned accounts, cold leads, lost deals | Often underutilized |
| Customer referrals | Warm intros into lookalike accounts | Requires asking |
| Lookalike modeling | Finding companies similar to best customers | Requires clear "best customer" definition |

For each source, note: what filter criteria applied, how many raw results, estimated yield after qualification.

### Step 3 -- Qualification Pass

Raw lists contain noise. Run every account through qualification before adding to the working list.

**Pass 1 -- Hard disqualifiers (remove immediately):**
- Outside target geography
- Outside headcount/revenue range
- Wrong industry
- Already a customer, opportunity, or blacklisted
- Competitor

**Pass 2 -- ICP scoring:**

| Criterion | Weight | Score (1-3) | Weighted score |
|-----------|--------|-------------|----------------|
| Industry fit | High | | |
| Company size fit | High | | |
| Growth stage fit | Medium | | |
| Tech stack fit | Medium | | |
| Trigger / timing signal | High | | |
| Persona presence confirmed | Medium | | |

**Tier the output:**
- **Tier 1 -- High priority:** Strong fit on must-haves + at least one timing signal. Active outreach.
- **Tier 2 -- Medium priority:** Strong on firmographics, no clear trigger. Monitor and warm up.
- **Tier 3 -- Low priority / watch list:** Partial fit. Don't invest now; revisit in 90 days.

### Step 4 -- Lookalike Expansion

Use existing customers as templates for finding more accounts like them.

For each reference customer, identify:
- Industry sub-vertical
- Headcount and stage when they bought
- What triggered the deal
- Tech stack alongside your product
- Who initiated the conversation

Search for companies matching that precise pattern -- the specific archetype, not the broad ICP.

> Cluster best customers into 2-3 archetypes if diverse. Prospect each as a separate motion with its own messaging.

### Step 5 -- Prioritization Logic

| Fit + Timing | Action |
|--------------|--------|
| High fit + clear trigger | Move now -- windows close |
| High fit + no trigger | Build awareness -- stay close until trigger fires |
| Partial fit + clear trigger | Investigate before committing |
| Partial fit + no trigger | Deprioritize -- don't manufacture urgency |

Stack-rank Tier 1. Top of list gets highest-effort, most-personalized outreach.

### Step 6 -- Contact Identification

For each prioritized account:
1. **Find primary persona** -- search for target titles. Confirm active (LinkedIn activity, current role tenure).
2. **Assess multi-thread opportunity** -- map buying committee before outreach starts.
3. **Verify contact info** -- confirm email addresses before sending. Bounces damage sender reputation.
4. **Document gaps** -- note accounts where right contact can't be found. May need different entry approach.

### Step 7 -- Prospecting Output Format

One record per account:

    ACCOUNT NAME:
    Domain:
    Industry:
    Headcount:
    Location:
    Funding stage & last round:
    ICP tier: [1 / 2 / 3]
    Fit summary: [2 sentences -- why this account fits]
    Trigger: [specific signal and when it occurred, or "none identified"]
    Primary contact: [name, title, LinkedIn]
    Secondary contact (optional): [name, title]
    Recommended first move: [outreach / monitor / research deeper / skip]
    Open questions: [what you still need to know before outreach]

### Step 8 -- Prospecting Cadence

Prospecting is not a one-time event. Build a rhythm:

| Activity | Frequency |
|----------|-----------|
| New account sourcing | Weekly or bi-weekly |
| Trigger monitoring on Tier 2 accounts | Weekly |
| Tier 3 review and re-qualification | Monthly |
| Lookalike refresh from new customer wins | After every closed deal |
| CRM hygiene pass (remove dead accounts) | Monthly |

---

## Relationship to Other GTM Skills

- **gtm-prospecting** -- find and tier accounts (this skill)
- **gtm-icp-definition** -- run first if no ICP exists
- **gtm-account-research** -- deep-dive on Tier 1 accounts before outreach
- **gtm-outreach-strategy** -- execute outreach against the prioritized list
- **gtm-qualification-scoring** -- score inbound or identified accounts
- **gtm-signal-based-outbound** -- act on triggers as they fire on monitored accounts
