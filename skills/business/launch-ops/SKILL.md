---
name: launch-ops
description: |
  Coordinates the full launch of a digital product funnel including tech stack setup,
  OTO pages, post-purchase flow, call booking automation, onboarding process, and
  go-live sequence. Aligned with the Automatic Clients Launch Checklist. Use when user
  wants to launch their product, set up their tech stack, configure Skool, set up
  payment processing, create automations, plan their launch sequence, "launch my
  product," "set up my funnel," or "go live."
---

# Launch Orchestrator

## Prerequisites

- All product assets ready:
  - Product content written (from `product-writer`)
  - Offer details finalized including OTOs and guarantee (from `product-offer`)
  - Sales page + OTO pages + call booking page copy written (from `sales-page-writer`)
  - Email sequences written including value bombs + awareness bridge (from `email-sequence`)
  - Content calendar with value bombs created (from `content-social`)
  - Sales call script and process designed (from `high-ticket-closer`, if backend included)
- User has accounts on chosen platforms (or is ready to create them)

## Workflow

### Phase 1: Product Hosting Setup

#### Option A: Skool ($99/mo - Recommended)

**Skool Setup Checklist:**

1. **Create Skool group**
   - Sign up at Skool
   - One plan: $99/mo for all features, unlimited everything, no additional fees

2. **Set up group branding**
   - Go to Settings > General
   - Upload group Icon (square logo)
   - Upload group Cover (banner image)
   - Fill in Group Description

3. **Set up discussion categories** (optional)
   - Go to Settings > Categories
   - Add categories for organizing member posts (e.g., Introductions, Wins, Questions)

4. **Create modules in Classroom**
   - Navigate to Classroom section
   - Create a "course" for each major module from your curriculum
   - Arrange in logical progression (drag to reorder)
   - Add a banner image to each module (use Canva)

5. **Upload all content**
   - Add lessons to each module with clear titles
   - Upload videos, PDFs, or other resources
   - Include descriptions for each lesson

6. **Create "Start Here" module**
   - First module new customers see
   - Welcome message, navigation instructions, community guidelines
   - Link to any quick-start resources

7. **Create pinned post**
   - Pin a post with important info, links, and getting-started steps
   - Reference the Start Here module

8. **Set up automated welcome DM**
   - Go to Settings > Plugins
   - Click "Auto DM new members"
   - Write welcome message linking to pinned post
   - Toggle ON

#### Option B: Notion (Free - Budget Alternative)

**Notion Setup Checklist:**

1. Create a new Notion workspace or page for the product
2. Build module structure using nested pages
3. Add lesson content to each page
4. Create a "Start Here" landing page
5. Set sharing to "Anyone with the link can view"
6. Note: No built-in access control (sharing risk is minimal when starting out)

### Phase 2: Payment Processing Setup

**Recommended options:**
- **Gumroad** - Simplest setup, handles everything, takes a % fee
- **Stripe + Checkout page** - More control, lower fees at scale
- **Stan Store** - Creator-focused, built-in landing pages

**Setup checklist:**
1. Create account on chosen platform
2. Connect bank account for payouts
3. Create product listing with price from `product-offer`
4. Set up checkout page or embed checkout on sales page
5. Configure receipt/confirmation email
6. Test purchase flow (use test mode or $1 test)

### Phase 2b: OTO Page and Payment Setup

If the offer includes OTOs (from `product-offer`):

1. **Create OTO 1 page**
   - Use copy from `sales-page-writer` (OTO page template)
   - Host on same platform as sales page (or standalone landing page builder)
   - Keep it short: 500-800 words, single CTA, countdown timer optional
   - Must load immediately after main purchase (redirect from thank-you page)

2. **Create OTO 2 page** (if applicable)
   - Downsell positioning: lower price, different angle
   - Shows only if OTO 1 is declined
   - Same hosting as OTO 1

3. **Configure OTO payment links**
   - Create separate products in payment platform for each OTO
   - Set up one-click upsell if platform supports it (no re-entering payment info)
   - If using Gumroad: use "Offer Codes" or separate product links
   - If using Stripe: use Stripe Checkout sessions with pre-filled customer data

4. **Set up OTO purchase flow**
   - Main purchase -> Thank You / OTO 1 page -> OTO 1 accepted or declined -> OTO 2 page (if OTO 1 declined) -> Final Thank You
   - Test the full redirect chain end-to-end

5. **OTO-specific automations**
   - OTO 1 purchase -> Tag subscriber as "OTO1_buyer" in email platform
   - OTO 2 purchase -> Tag subscriber as "OTO2_buyer"
   - OTO purchase -> Grant access to OTO content in Skool/Notion

### Phase 3: Email Platform Setup

**Recommended platforms:**
- **ConvertKit** - Best for creators, free up to 1,000 subscribers
- **Beehiiv** - Free tier, good for newsletters
- **Mailchimp** - Established, free tier available

**Setup checklist:**
1. Create account
2. Import email sequences from `email-sequence`:
   - Educational Email Course (5-day automation)
   - Post-purchase welcome email
   - Weekly nurture email template
   - Objection-handling emails (segment: "Clickers" only)
3. Create opt-in form/landing page for EEC
4. Set up segments:
   - All subscribers
   - EEC subscribers (in-progress)
   - EEC completed
   - Product landing page clickers (haven't bought)
   - Customers (have bought)
5. Schedule first weekly nurture email

### Phase 4: Automation Setup (Zapier)

**Critical automation: Purchase -> Skool Access**

```
Trigger: New purchase on [payment platform]
Action: Add member to Skool group
```

**Additional automations:**
- Purchase -> Tag subscriber as "Customer" in email platform
- Purchase -> Remove from "Clickers" objection sequence
- EEC Day 5 complete -> Move to weekly newsletter segment
- New Skool member -> Send welcome DM (if not using Skool's built-in)

### Phase 4b: Call Booking Automation

If the funnel includes a high-ticket backend (from `high-ticket-closer`):

1. **Set up scheduling tool**
   - Calendly (free tier), Cal.com (open source), or Acuity Scheduling
   - Configure availability windows (recommend 3-5 slots per week to start)
   - Set buffer time between calls (15 min minimum)
   - Set maximum advance booking (14 days recommended)

2. **Configure booking page**
   - Use call booking page copy from `sales-page-writer`
   - Embed calendar widget on booking page
   - Add application/qualification questions (from `high-ticket-closer` intake form)
   - Set up redirect to confirmation page after booking

3. **Booking automations**
   - Booking confirmed -> Send confirmation email with prep checklist
   - Booking confirmed -> Send SMS reminder (if using Twilio or platform built-in)
   - 24 hours before -> Automated reminder email
   - 1 hour before -> SMS reminder
   - No-show -> Trigger no-show follow-up sequence (from `high-ticket-closer`)
   - Booking confirmed -> Tag subscriber as "call_booked" in email platform

4. **Confirmation page setup**
   - Use call confirmation page copy from `sales-page-writer`
   - Include: what to prepare, pre-call content link, calendar add button
   - Embed a short "what to expect" video (optional but improves show rates)

### Phase 5: Post-Purchase Flow Verification

Test the entire customer journey end-to-end:

1. Visit sales page -> Verify all copy is correct
2. Click checkout -> Verify payment processes
3. Redirect to Thank You page -> Verify copy and instructions
4. Check email -> Verify welcome email arrives
5. Check email -> Verify Skool invite arrives
6. Click Skool link -> Verify access granted
7. Navigate Skool -> Verify all modules and content accessible
8. Verify Zapier automations fired correctly

### Phase 5b: Onboarding Process Setup

Set up the post-purchase customer experience (critical for backend conversion):

1. **Welcome video** (2-3 min max)
   - Record or script a personal welcome from the creator
   - Cover: what they just bought, what to do first, where to get help
   - Host in Skool "Start Here" module or Notion landing page

2. **Quick-start guide**
   - One-page PDF or Notion doc with the 3-5 first actions
   - Remove all friction: direct links, step-by-step screenshots
   - Goal: get the customer their first small win within 24 hours (conversion velocity)

3. **Community access** (if applicable)
   - Skool group invite (automated via Zapier from Phase 4)
   - Welcome DM with quick-start link
   - Tag new members so they're visible to community managers

4. **Milestone check-ins**
   - Day 1: "Did you complete the Start Here module?" (automated email)
   - Day 7: "Here's what to focus on this week" (automated email)
   - Day 30: Check-in email with progress questions + soft CTA to backend offer
   - Day 60: Results check + escalation CTA to backend offer (awareness bridge already running since Day 14)

5. **Onboarding -> backend bridge**
   - After Day 7, begin value bomb delivery (from `email-sequence` Step 7)
   - After Day 14-21, begin awareness bridge sequence (from `email-sequence` Step 8)
   - Goal: move buyers from DIY customer to DWY/DFY prospect naturally

### Phase 6: Pre-Launch Checklist

Use `templates/launch-checklist.md` for the complete pre-launch checklist. It covers all sections: Deliverables (core product, bonuses, OTOs, value bombs, awareness bridge, backend plan), Marketing (branding, sales page, OTO pages, email setup, follow-up timelines), Back End Sales (call booking, sales scripts, onboarding), and Miscellaneous (support, social, legal).

Go through every item before going live. Do not skip sections.

### Phase 7: Go-Live Sequence

**Day-by-day launch plan:**

| Day | Action |
|-----|--------|
| Day -7 | Tease the product on social media (build anticipation) |
| Day -3 | Share behind-the-scenes of building it |
| Day -1 | "Launching tomorrow" announcement |
| Day 0 | LAUNCH - Announce on all platforms + send email to list |
| Day 1 | Share first piece of social proof or feedback |
| Day 3 | Send follow-up email to list (for non-openers of launch email) |
| Day 7 | Weekly content rhythm begins (content-social calendar kicks in) |

### Phase 8: Value Bomb Distribution Plan

Schedule and distribute value bombs (from `content-social` Tier 2 content) across channels:

1. **Email distribution** (primary channel)
   - Value bomb email series lives in `email-sequence` Step 7
   - Schedule: one value bomb every 2-3 days post-purchase, starting Day 3
   - Each email delivers a standalone high-value insight + links to full content piece

2. **Social distribution** (amplification)
   - Pull value bomb topics into `content-social` calendar as Tier 2 posts
   - Create 2-3 social posts per value bomb (teaser, key insight, results/proof)
   - Schedule social posts to go live same day as email delivery

3. **Paid amplification** (optional, after organic validation)
   - Boost top-performing value bomb social posts as ads
   - Target: existing email subscribers + lookalike audiences
   - Goal: reinforce brand authority, not direct sales

4. **Timing with launch sequence**
   - Day -7 to Day -1: Pre-launch teaser content (standard)
   - Day 0: Launch
   - Day 3-14: Value bomb delivery begins for buyers
   - Day 14-21: Awareness bridge sequence begins
   - Day 21+: High-ticket nurture begins (from `email-sequence` Step 9)

## Integration

- **Input from:** ALL previous skills (product content, offer, sales page, emails, content calendar, sales call process)
- **This is the coordination skill** that brings everything together
- **After launch:** `cro-funnel` takes over for optimization
- **Routes to:** `high-ticket-closer` (when backend calls begin), `cro-funnel` (for ongoing optimization)
