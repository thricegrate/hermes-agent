---
name: gtm-signal-based-outbound
description: |
  Turn a buying signal into a personalized, timed outreach sequence.
  Use when user asks about "signal-based outreach", "intent-based outreach",
  "trigger-based outbound", "react to a buying signal", "website visitor outreach",
  "job change outreach", "funding round outreach", or "event-triggered outbound".
  Also trigger when user has a specific behavioral signal (website visit, job change,
  funding, hiring surge, content engagement) and needs to act on it with personalized
  messaging. Distinct from gtm-outreach-strategy which handles planned outreach --
  this skill handles reactive, signal-driven outbound where timing is the advantage.
---

# GTM Signal-Based Outbound

Turn a specific behavioral signal -- a website visit, job change, funding round, hiring surge, or content engagement -- into a personalized, timed outreach sequence. This is distinct from planned outreach (gtm-outreach-strategy); this handles reactive, signal-driven outbound where timing is the competitive advantage.

## Context Gathering

Before starting, collect from the user:

- **What you sell** -- product/service, ICP, key use cases
- **Your senders** -- who is reaching out (name, role, tone)
- **Signal sources** -- which signals you have access to (website visitor data, LinkedIn alerts, intent tools, news feeds)
- **Outreach channels** -- email, LinkedIn, phone, or combination
- **Message examples** -- 2-3 examples of outreach that has worked in the past
- **The specific signal** -- what happened, when, who/what company

## What This Skill Produces

A classified signal assessment, a research-backed angle, and a ready-to-send personalized message (or sequence) that references the signal without being creepy.

---

## Outbound Methodology

### Step 1 -- Classify the Signal

Before doing anything, identify the signal type. Type determines urgency, research depth, and angle.

**Tier 1 -- High-intent (act within 24h):**
- Website visit to pricing, product, or demo pages
- Inbound form fill or demo request
- Direct reply to prior outreach
- Review site activity (G2, Capterra, etc.)
- Re-engagement from a previously cold or lost account

**Tier 2 -- Moderate-intent (act within 72h):**
- Job change -- known contact or ICP persona joined a new company
- New relevant hire at a target company (e.g., Head of RevOps)
- Funding round announced
- Company expansion into new market or geography
- Former champion or customer moved to a new company

**Tier 3 -- Weak-intent (act within 1 week, lower priority):**
- LinkedIn content engagement (likes, comments on relevant posts)
- News mention without clear buying signal
- Technology install or removal detected
- Hiring volume increase in relevant department
- Conference or event attendance

> If signal type is unclear, default to Tier 2 handling.

### Step 2 -- Research Before Writing

Never write outreach before researching. Research determines whether to reach out at all and what angle to use.

**For the company:**
- What do they do, how big, what's their current moment (growth, transition, pressure)?
- ICP fit? If not, stop.
- Existing relationship (current customer, past deal, prior outreach)?

**For the signal:**
- What specifically happened? Get details (not just "they got funding" -- the amount, stage, stated use of funds)
- How recent? Signals older than 30 days lose relevance fast
- Clear connection between this signal and what you sell?

**For the contact:**
- Who is the right person given this signal? (Not always the person who triggered it)
- Role, seniority, likely priorities?
- Shared context -- mutual connections, past interaction, content they've published?

> If you cannot establish a clear connection between signal and specific pain, do not reach out. A weak hook is worse than no outreach.

### Step 3 -- Determine the Angle

The signal is the reason you're reaching out. The angle is the insight or value you bring. These are different.

| Signal | Angle |
|--------|-------|
| Funding | They have budget and mandate to move fast. Connect to stated use of funds. |
| New hire | Fresh mandate. Position as a tool helping them succeed early. |
| Hiring spree | Scaling something. Identify friction that comes with scale and address it. |
| Website visit | They already know you exist. Remove friction, don't re-introduce. Reference what they looked at. |
| Job change | Congratulate without being hollow. Reference what you achieved together or their situation. |
| Intent data / review site | They're evaluating. Be direct. Don't pretend you don't know. |

**Angle quality test** -- finish this sentence honestly:

> "I'm reaching out because [signal], which tells me you might be dealing with [specific problem], and we help with that specifically by [specific capability]."

If forced or vague, rethink the angle.

### Step 4 -- Write the Outreach

**Principles (channel-agnostic):**
- Lead with the signal, not with yourself
- One idea per message. No feature lists, no company overviews
- Make the ask small and specific (a reply, a quick call -- not "let me know if interested")
- Subject lines: specific, not clever. Reflect actual content
- LinkedIn messages: 3-5 sentences max
- Sequence length: 2-3 touches max per signal. No response = signal wasn't strong enough -- find a new one

**Message structure:**

    Signal hook -- what you noticed and why it matters (1 sentence)

    Connection -- why that's relevant to what you do (1-2 sentences)

    Specific ask -- one clear, low-friction next step (1 sentence)

**Personalization check before sending:**
- Does this message work if you remove company and contact name? If yes, not personalized enough.
- Would the recipient feel like you did your homework? If not, do more research or don't send.

### Step 5 -- Sequence Logic

**Single-signal, single contact:**

| Touch | Purpose | Timing |
|-------|---------|--------|
| Touch 1 | Signal-driven message | Day 0-1 |
| Touch 2 | Value-add follow-up -- share something relevant. Don't just bump. | Day 5-7 |
| Touch 3 | Break-up or pivot -- acknowledge they're busy, offer different framing | Day 12-14 |

**Multi-signal or high-priority account:**
- Multiple signals within 30 days = high-priority. Consider multi-threaded outreach (different contacts, different angles)
- Do not send the same message to multiple contacts at the same company

**After 3 touches with no response:**
- Stop. Archive the sequence.
- Set reminder to revisit if new signal fires.
- Do not add to generic nurture without a fresh reason.

### Step 6 -- Log and Learn

After outreach is sent, record:
- Which signal triggered it
- What angle was used
- Channel and sequence used
- Outcome (reply, meeting, no response, unsubscribe)

Over time, this reveals which signals convert for your ICP and which are noise. Prune signals that consistently produce no replies after 20+ attempts.

---

## Quick Reference

| Signal | Tier | Angle | Channel | Timing |
|--------|------|-------|---------|--------|
| Pricing page visit | 1 | Remove friction, they know you | Email or DM | Same day |
| Funding announced | 2 | Connect to stated use of funds | Email | Within 48h |
| ICP hire made | 2 | Help new hire win early | LinkedIn first | Within 72h |
| Contact changed jobs | 2 | Build on prior relationship | LinkedIn + Email | Within 48h |
| Hiring surge | 3 | Scale-related pain | Email | Within 1 week |
| Content engagement | 3 | Extend the conversation | LinkedIn | Within 1 week |

---

## Relationship to Other GTM Skills

- **gtm-signal-based-outbound** -- reactive signal-triggered outreach (this skill)
- **gtm-outreach-strategy** -- planned outreach campaigns (not signal-triggered)
- **gtm-account-research** -- deeper research for high-priority signal accounts
- **gtm-qualification-scoring** -- confirm account is worth acting on before building sequence
