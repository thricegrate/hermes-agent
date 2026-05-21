---
name: linkedin-profile
description: |
  Audit and optimize LinkedIn profiles for coaches, consultants, and B2B service providers.
  Use when the user wants to "audit my LinkedIn", "optimize my LinkedIn profile", "rewrite my headline",
  "fix my about section", "LinkedIn banner", "featured section strategy", "LinkedIn makeover",
  "profile review", "LinkedIn profile audit", "profile optimization", "LinkedIn positioning",
  "experience section rewrite", or anything related to making a LinkedIn profile convert visitors into leads.
  For LinkedIn content/posts, see content-social. For LinkedIn outreach, see gtm-outreach-strategy.
  For LinkedIn competitor analysis, see competitor-alternatives.
---

# LinkedIn Profile Audit & Optimization

Your LinkedIn profile is a landing page, not a resume. Every section either converts visitors into leads or loses them. This skill audits, scores, and rewrites LinkedIn profiles for coaches, consultants, and B2B service providers selling high-ticket services ($1K+).

## Prerequisites

- User's current LinkedIn profile text (pasted or URL)
- Who they help (ideal client)
- What outcome they deliver
- How they deliver it (method, service, or offer)
- Optionally: `niche-finder` output (persona depth, ICP)

**Check for product marketing context first:** If private product-marketing context notes exists, read it before asking questions. Use that context and only ask for information not already covered.

## Core Principles

**Your profile speaks to ONE person.** Not your industry. Not your peers. Not recruiters. Your ideal client. Every word on the profile should make that person think "this is exactly who I need."

**First 3 lines are everything.** LinkedIn truncates the About section after ~300 characters with a "see more" fold. The headline is always visible. If those two things don't hook your ideal client, nothing else matters.

**Proof beats claims.** "I help businesses grow" means nothing. "Helped 47 coaches add $10K/mo in 90 days" means everything. Specificity is credibility.

**The Coffee Shop Rule applies.** If you wouldn't say it across a cafe table, don't put it on your profile. No corporate speak. No buzzword soup. Talk like a human.

---

## Workflow

### Step 1: Gather Profile Context

Ask for what's missing:

**Current profile sections** (paste text for each):
- Headline
- About section
- Featured section (what's pinned, or "empty")
- Most recent Experience entry
- Banner image (describe it, or "none")

**Business context:**
- Who do you help? (specific client type, not "businesses")
- What outcome do you deliver? (measurable result)
- How do you deliver it? (method, framework, service name)
- Biggest proof points (client results, revenue numbers, case studies)

### Step 2: Score Current Profile

Rate each dimension 1-5 and explain why. Use the scoring rubric:

| Dimension | 1 (Broken) | 3 (Decent) | 5 (Converts) |
|-----------|-----------|-------------|---------------|
| **Headline Clarity** | Job title only, no client benefit | Has client mention but vague outcome | WHO + OUTCOME in under 120 chars, stranger knows what you do in 3 sec |
| **About Section Hook** | Opens with credentials or bio | Opens with mild client reference | Opens with client's #1 pain point, impossible to not click "see more" |
| **About Section Body** | Wall of text, no structure | Some structure, unclear CTA | Scannable, WHO + WHAT + HOW + CTA, reads like a mini sales page |
| **Banner Image** | Default LinkedIn banner or unrelated photo | Professional but generic | Reinforces positioning, has value statement or CTA text |
| **Featured Section** | Empty or random | Has some content but no strategy | Lead magnet first, then case study, then testimonial post |
| **Experience Section** | Reads like a resume | Lists responsibilities | Achievement-focused, reads like a mini sales page for your offer |
| **Skills & Endorsements** | Random or default | Some relevant skills | Top 3 skills match what clients search for |
| **Recommendations** | None or generic | A few but unfocused | Client testimonials that describe transformation and results |
| **Profile Photo** | No photo or casual selfie | Professional but forgettable | High-quality, approachable, stands out in feed |
| **Activity & Consistency** | Ghost profile, no posts | Occasional posts, inconsistent | Regular content that demonstrates expertise, engages with others |

**Overall Score:** Sum / 50, convert to percentage. Include "Would your ideal client reach out after seeing this? Yes/No and why."

### Step 3: Rewrite Headline

Use formula library from [references/headline-formulas.md](references/headline-formulas.md).

Generate 5 headline options ranked best to worst. Each must:
- Say WHO you help + WHAT outcome in under 120 characters
- Be written for the client, not for you
- Pass the "stranger test" -- would someone landing on your profile know exactly what you do in 3 seconds?
- Avoid: buzzword soup, emoji overload, vague titles ("Entrepreneur | Visionary | Thought Leader")

### Step 4: Rewrite About Section

Use frameworks from [references/about-section-frameworks.md](references/about-section-frameworks.md).

**Hard constraints:**
- 2,600 character max (LinkedIn limit)
- First 300 characters must hook (visible before "see more" fold)
- Open with client's pain, NOT your credentials
- End with clear CTA (DM me, book a call, download X)
- Scannable: short paragraphs (1-3 sentences), white space between thoughts
- Include: who you help, what you help them do, how you do it, proof it works

**Structure the rewrite:**
1. Hook (first 3 lines): Client's biggest pain point or a bold, specific claim
2. Empathy bridge: Show you understand their world
3. Your method: Name your framework/process, explain it simply
4. Proof: 2-3 specific results (numbers, timeframes, client types)
5. CTA: One clear next step

### Step 5: Banner Design Brief

The banner is free billboard space. Most people waste it.

**Provide a brief with:**
- Recommended text (positioning statement or CTA, max 8-10 words)
- Layout suggestion (text placement, visual balance)
- Elements to include: your offer name, result statement, CTA, optional URL or QR
- What to avoid: cluttered design, tiny text, stock imagery that says nothing
- Tool recommendations: Canva (free), `infographic-gen` skill, or hire a designer
- Dimensions: 1584 x 396 pixels (4:1 ratio)

### Step 6: Featured Section Strategy

The featured section is your profile's "above the fold." Pin order matters.

**Recommend exactly what to feature and why:**

Ideal order (top = most visible):
1. **Lead magnet** -- free resource that captures email (PDF, checklist, quiz, tool)
2. **Case study or testimonial post** -- best proof of results
3. **Signature content piece** -- your most-shared post, article, or thread
4. **Newsletter or external link** -- secondary conversion path

For each recommendation: what it is, why it belongs there, and what to create if they don't have it yet.

### Step 7: Experience Section Rewrite

The current role should read like a mini sales page, not a job description.

**Rewrite rules:**
- Company name = your business or offer name
- Title = client-facing role description (not just "Founder")
- Description: what you do for clients, proof it works, CTA
- Use bullet points for scanability
- Include keywords clients search for

### Step 8: Deliver Audit Report

Output everything using [templates/profile-audit-template.md](templates/profile-audit-template.md).

**Before delivering:** Route through `humanizer` and `content-review` skills (this is outward-facing content).

---

## What Happens Next

After the profile is optimized:
- **Start posting:** Use `content-social` for LinkedIn content creation
- **Build content pillars:** Use `content-strategy` with LinkedIn calendar reference
- **Research competitors:** Use `competitor-alternatives` with LinkedIn positioning analysis
- **Create a lead magnet:** Use `free-tool-strategy` with LinkedIn distribution reference
- **Start outreach:** Use `gtm-outreach-strategy` for LinkedIn DM sequences
