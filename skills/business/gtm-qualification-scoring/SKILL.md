---
name: gtm-qualification-scoring
description: |
  Score any company across four dimensions (Fit, Timing, Access, Intent) and get a
  clear next action. Use when user asks to "score an account", "qualify a lead",
  "prioritize accounts", "lead scoring", "account scoring", "qualification framework",
  "should we pursue this company", or "rank these accounts". Also trigger when user
  needs to evaluate inbound leads, prioritize pipeline, or make go/no-go decisions
  on specific companies. Eliminates gut-feel prioritization.
---

# GTM Qualification & Scoring

Evaluate any company or inbound lead and produce a clear, data-backed priority decision. Scores accounts across four dimensions -- Fit, Timing, Access, Intent -- and outputs a composite score with a specific recommended next action.

## Context Gathering

Before starting, collect from the user:

- **Your ICP** -- ideal company profile (industry, size, geography, tech stack, business model)
- **Your buyer personas** -- titles, seniority, typical pain points
- **Deal characteristics** -- average deal size, typical sales cycle, what good vs. bad deals look like
- **Disqualifiers** -- hard stops that automatically make a company not worth pursuing
- **Signal sources** -- what data you have access to (enrichment tools, CRM, intent data, website analytics)

Without this, scores will be directionally correct but not calibrated to your business.

## What This Skill Produces

A composite score (1-12) across four dimensions, a tier classification, and a specific recommended next action -- so every account leaves with a clear decision, not a maybe.

---

## Scoring Methodology

### Step 1 -- Collect the Raw Data

Don't score on assumptions. Gather what's knowable first.

**Minimum required to score:**
- Company name and website
- Headcount (or range)
- Industry / vertical
- Geography
- What triggered this evaluation (inbound, signal, outbound response, manual review)

**Better scoring requires:**
- Revenue or funding stage
- Tech stack
- Growth signals (hiring trends, funding, expansion news)
- Current contact -- who engaged, their role and seniority
- Prior relationship -- have we spoken before? What happened?

> If minimum data isn't available, enrich before scoring. Scoring on incomplete data produces misleading scores.

### Step 2 -- Score Across Four Dimensions

Score each dimension **1-3**. No halves. Forced precision.

#### Dimension 1 -- Fit (Does this company match our ICP?)

| Score | Criteria |
|-------|---------|
| **3** | Matches all major ICP criteria. Looks like existing best customers. |
| **2** | Matches most criteria. One or two gaps that aren't disqualifying. |
| **1** | Significant gaps. Could work but requires adapting product, process, or pitch. |
| **0** | Hard disqualifier present -- stop evaluation. |

**Hard disqualifiers (score = 0, stop all scoring):**
- Blocked industry or geography
- Competitor
- Size far outside viable range
- Known bad history (churned badly, legal issue, do-not-contact)

> If score = 0 on Fit, stop. Do not continue scoring. Log the disqualifier and move on.

#### Dimension 2 -- Timing (Is there a reason to buy now?)

Timing is the hardest dimension to fake. Perfect ICP fit with no timing signal = future deal, not current.

| Score | Criteria |
|-------|---------|
| **3** | Clear forcing function present. |
| **2** | Soft timing indicators. Growing team, relevant hiring, prior interest gone cold. |
| **1** | No visible timing signal. Good company, wrong moment. |

**What counts as a forcing function (score = 3):**
- New budget (funding, new fiscal year, budget approved)
- New mandate (leadership change, new hire with specific brief)
- External pressure (regulatory change, competitor move, market shift)
- Active pain (clearly feeling the problem right now)
- Inbound or self-initiated contact (they came to you -- that IS the timing signal)

#### Dimension 3 -- Access (Can we reach the right people?)

A qualified company you can't reach is not a qualified opportunity.

| Score | Criteria |
|-------|---------|
| **3** | Decision maker or strong champion identified, reachable, engaged or likely to engage. |
| **2** | Right company, but only peripheral contacts (wrong seniority/department) or no warm path. |
| **1** | No contact identified, no warm intro path, cold outreach unlikely to land. |

**Access accelerators (upgrade by 1):**
- Mutual connection or warm intro available
- Contact in CRM with prior positive interaction
- Contact engaged with your content or visited your site
- Worked with this person at a previous company

**Access killers (downgrade by 1):**
- Only contact is a gatekeeper or procurement
- Company has "no cold outreach" policy or explicit opt-out
- Prior outreach rejected or marked spam

#### Dimension 4 -- Intent (Do they show signs of actively looking?)

Intent is distinct from timing. Timing = reason to buy. Intent = behavioral signals of evaluation.

| Score | Criteria |
|-------|---------|
| **3** | Direct behavioral signal: visited pricing/demo pages, requested demo, downloaded eval content, mentioned competitors, asked specific product questions. |
| **2** | Indirect signal: engaged with thought leadership, attended webinar, LinkedIn activity on relevant topics, intent data showing category research. |
| **1** | No detectable intent signal. Outbound-initiated with no response yet. |

> If you have no intent signal access (no website tracking, no intent tool), score as **2** for all accounts and note the data gap. Absence of data is not absence of intent.

### Step 3 -- Calculate the Composite Score

Add the four dimension scores. Maximum = 12.

| Score | Band | Action |
|-------|------|--------|
| 10-12 | **Priority** | Act immediately. Assign to rep, engage within 24 hours, multi-thread if possible. |
| 7-9 | **Active** | Worth pursuing now. Build sequence, personalize outreach, move into active pipeline. |
| 4-6 | **Nurture** | Not the right moment. Low-touch track, review trigger in 60-90 days. |
| 1-3 | **Deprioritize** | Poor fit or too early. Log, don't spend cycles. Revisit only on strong new signal. |
| 0 | **Remove** | Disqualifier hit. Log reason. Do not requeue without explicit instruction. |

### Step 4 -- Validate Before Acting

A score is a starting point, not a final answer.

**Recency check:** Is the data current? Funding from 18 months ago, a contact who left, a filled job posting all produce stale scores. Flag data points older than 6 months.

**Consistency check:** Does the score feel right holistically? If a company scores 10 but something feels off, flag for human review.

**Competing signals check:** Are positive and negative signals canceling each other out? A company that visited pricing AND unsubscribed from your email scores 10 on paper but needs a different approach. Note conflicts explicitly.

### Step 5 -- Recommend a Next Action

Every scored company leaves with one clear next step.

**Priority (10-12):**
- Identify best contact and outreach angle immediately
- Inbound: respond within the hour
- Outbound-identified: trigger signal-based outreach today

**Active (7-9):**
- Determine right sequence (channel, length, angle)
- Personalize based on highest-scoring dimension
- Set follow-up checkpoint at 2 weeks

**Nurture (4-6):**
- Add to relevant list with lower frequency
- Identify what would upgrade this account (what signal would make it Priority?)
- Set review date -- don't let it sit indefinitely

**Deprioritize (1-3):**
- Log score and reason
- No outreach
- 90-day review trigger tied to new signal activity only

**Disqualified (0):**
- Log disqualifier
- Remove from active pipeline
- Tag company to prevent re-entry

### Step 6 -- Log the Score

Record for every evaluated company:
- Date scored
- Score per dimension and total
- Data sources used
- Key reasoning (1-2 sentences)
- Recommended next action taken

> Calibrate quarterly against actual outcomes. If 7-9 band closes at the same rate as 10-12, scoring is too generous at the top.

---

## Quick Reference

| Dimension | 3 | 2 | 1 | 0 |
|-----------|---|---|---|---|
| **Fit** | Perfect ICP match | Most criteria met | Significant gaps | Disqualifier |
| **Timing** | Clear forcing function | Soft indicators | No signal | -- |
| **Access** | DM identified + reachable | Wrong contact or no path | No contact, no path | -- |
| **Intent** | Direct behavioral signal | Indirect engagement | No signal detected | -- |

---

## Relationship to Other GTM Skills

- **gtm-qualification-scoring** -- score and tier accounts (this skill)
- **gtm-icp-definition** -- provides the Fit criteria (Dimension 1)
- **gtm-account-research** -- enrichment input for scoring; deep-dive on Priority accounts
- **gtm-prospecting** -- qualification pass on candidate lists
- **gtm-outreach-strategy** -- execute against Priority and Active accounts
- **gtm-signal-based-outbound** -- when a new signal upgrades a Nurture account
