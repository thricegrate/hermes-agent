# Email Automation Setup for Low-Ticket Products (Cole/Bush)

Source: Nicolas Cole & Dickie Bush (Ship 30 for 30), Low-Ticket Product M&M Course, Module 8

---

## Tag Naming Conventions

| Tag Type | Naming Pattern | Example |
|----------|---------------|---------|
| Purchase | `Purchased - {Product Name}` | `Purchased - Skill Pack v1` |
| Status | `Status - In {Product Name} {Sequence Name}` | `Status - In Skill Pack v1 Post-Purchase Sequence` |
| Opt-out | `Opt Out - {Product Name} {Sequence Name}` | `Opt Out - Skill Pack v1 Post-Purchase Sequence` |
| Flag | `Flag - Clicked {Product Name} Buy` | `Flag - Clicked Skill Pack v1 Buy` |
| Trigger | `Flag - Start {Product Name} Launch Sequence - {Month} {Year}` | `Flag - Start Skill Pack v1 Launch Sequence - April 2026` |

**Rules:**
- The `Purchased` tag must be connected to your e-commerce platform (direct integration or Zapier).
- The `Status` tag is added at sequence start, removed at sequence end -- used to exclude people from other sends.
- The `Opt Out` tag is applied when someone clicks the opt-out link inside a sequence.
- The `Flag` tag fires when someone clicks a sales page link (via Link Trigger) and feeds them into the Click Scoring automation.
- The `Trigger` tag kicks off the Combined Pre-Launch + Launch automation for a specific launch window.

---

## Custom Field Conventions

| Field Type | Naming Pattern | Example |
|------------|---------------|---------|
| Click scoring (abandoned cart) | `{offername}_buy_score` | `skillpack_buy_score` |
| Launch scoring (launch sequence) | `{offername}_launch_score` | `skillpack_launch_score` |

These fields are integer counters. The Click Scoring automation increments them by 1 each time someone clicks a sales page link. Used to identify warm leads and trigger the Abandoned Cart sequence (threshold: 2+ clicks).

---

## Automation Flow 1: Post-Purchase Sequence

**Template URL:** https://app.kit.com/a/5b9e1f25cc

**Trigger:** `Purchased - {Product Name}` tag is added (via e-commerce integration or Zapier).

**Flow:**
1. Tag added: `Purchased - {Product Name}` (entry point)
2. Add tag: `Status - In {Product Name} Post-Purchase Sequence`
3. Run 6-email sequence with timing:
   - Email 1 -- Immediately
   - Email 2 -- 24 hours later
   - Email 3 -- 2-4 days later
   - Email 4 -- 2-4 days later
   - Email 5 -- 2-4 days later
   - Email 6 -- 5-7 days later
4. Remove tag: `Status - In {Product Name} Post-Purchase Sequence`
5. Exit tag (opt-out): `Opt Out - {Product Name} Post-Purchase Sequence`

**Setup checklist:**
- Rename automation: `{Product Name} - Post-Purchase Sequence`
- Replace trigger tag with your `Purchased` tag
- Create and assign the `Status` tag (added at start, removed at end)
- Create and assign the `Opt Out` tag
- Rename the sequence: `{Product Name} - Post-Purchase Sequence`
- Upload all 6 emails with subject lines, preview text, content, images, links
- Add opt-out link to sequence template

---

## Automation Flow 2: Click Scoring

**Template URL:** https://app.kit.com/a/48c08b997c

**Trigger:** `Flag - Clicked {Product Name} Buy` tag is added (via Link Trigger on sales page links).

**Flow:**
1. Tag added: `Flag - Clicked {Product Name} Buy` (entry point)
2. Remove the same flag tag (so subscriber can re-enter on next click)
3. Filter: check if `{offername}_launch_score` custom field exists
4. If exists -- increment the custom field value by 1
5. If doesn't exist -- set custom field to 1
6. Loop back (subscriber exits, can re-enter when flag tag is added again)

**Setup checklist:**
- Rename automation: `{Product Name} - Click Scoring Automation`
- Replace trigger tag (step 1) with your `Flag - Clicked {Product Name} Buy` tag
- Replace removal tag (step 2) with the same flag tag
- Create custom field: `{offername}_launch_score`
- Update the filter (step 3) and increment steps (steps 5-6) to use your custom field
- Update the code block to match your custom field name
- Turn on and test by adding the flag tag to yourself

---

## Automation Flow 3: Abandoned Cart Sequence

**Template URL:** https://app.kit.com/a/355f512d1f

**Prerequisite:** Click Scoring automation must be installed and active. Link Triggers must be on all sales page links in your launch emails.

**Trigger:** `{offername}_launch_score` custom field changes (value reaches 2+).

**Flow:**
1. Custom field change detected: `{offername}_launch_score` (entry point)
2. Advanced filter: check if subscriber has `Purchased - {Product Name}` tag -- if yes, exit immediately
3. Add tag: `Status - In {Product Name} Abandoned Cart Sequence`
4. Run Part 1 sequence (core abandoned cart emails)
5. Branch based on objection link clicks from "Why Didn't You Buy" email:
   - Each objection type gets its own mini-sequence
   - Link Triggers on objection links route subscribers to the right branch
6. 1-day delay after objection sequences complete
7. Remove tag: `Status - In {Product Name} Abandoned Cart Sequence`
8. Exit tags:
   - `Opt Out - {Product Name} Abandoned Cart Sequence`
   - `Purchased - {Product Name}`

**Setup checklist:**
- Rename automation: `{Product Name} - Abandoned Cart Sequence`
- Replace custom field trigger with your `{offername}_launch_score` field
- Update Advanced Filter to use your `Purchased` tag
- Create and assign the `Status` tag
- Rename Part 1 sequence: `{Product Name} - Abandoned Cart Sequence - Part 1`
- Rename objection sequences: `{Product Name} - Abandoned Cart Sequence - Objection - {Objection Type}`
- Create and assign both exit tags (`Opt Out` and `Purchased`)
- Upload emails with subject lines, preview text, content, images, links
- Add Link Triggers to the "Why Didn't You Buy" email for objection routing
- Add opt-out link to sequence template

**Objection routing ("Why Didn't You Buy" email):**
- Each objection option links to a lightweight confirmation redirect page
- Each link has a Link Trigger that tags the subscriber with their objection type
- The automation branches based on which objection tag was applied

**Redirect page boilerplate:**
- Headline: "Thanks for sharing your input!"
- Body: "This is going to be super helpful as I continue to improve {product name}. Talk soon, {your name}"

---

## Automation Flow 4: Combined Pre-Launch + Launch Sequence

**Template URL:** https://app.kit.com/a/0d28fa5e84

**Trigger:** `Flag - Start {Product Name} Launch Sequence - {Month} {Year}` tag is added.

This automation handles both the Pre-Launch and Product Launch sequences in one flow, gated by date events.

**Flow:**
1. Tag added: `Flag - Start {Product Name} Launch Sequence - {Month} {Year}` (entry point)
2. Date event: wait until Pre-Launch start date
3. Add tag: `Status - In {Product Name} Launch Sequence - {Month Year}`
4. Run Pre-Launch Sequence: `{Product Name} - {Month} {Year} - Pre-Launch Sequence`
5. Date event: wait until Product Launch start date
6. Run Product Launch Sequence: `{Product Name} - {Month} {Year} - Product Launch Sequence`
7. Date event: wait until 6 hours before launch sequence ends
8. Filter: check `{offername}_launch_score` custom field (identifies warm leads who clicked 2+)
   - If score meets threshold -- run Last Chance Email: `{Product Name} - {Month} {Year} - Product Launch Sequence Last Chance Email`
   - If not -- skip Last Chance Email
9. Date event: morning after launch sequence ends
10. Remove tag: `Status - In {Product Name} Launch Sequence - {Month Year}`
11. Exit tags:
    - `Opt Out - {Product Name} Product Launch Sequence`
    - `Purchased - {Product Name}`

**Setup checklist:**
- Rename automation: `{Product Name} - Pre-Launch & Launch Sequences`
- Replace trigger tag with your `Flag - Start` tag
- Set all 4 date events to match your launch calendar
- Create and assign the `Status` tag (added at step 3, removed at step 10)
- Rename all 3 sequences with product name + month/year
- Update the filter to use your `{offername}_launch_score` custom field
- Create and assign both exit tags
- Upload all emails (pre-launch + launch + last chance)
- Add Link Triggers to all sales/landing page links in launch emails
- If using a waitlist, link to waitlist landing page in Pre-Launch emails
- Add opt-out link to sequence template (one template covers both sequences)

---

## Link Trigger Setup

Link Triggers connect sales page clicks to the Click Scoring automation. They are reusable -- set up once, apply to any email.

**Setup steps:**
1. Go to ConvertKit Rules > New Rule
2. Set trigger: subscriber clicks your sales page link
3. Add a descriptive name to the Link Trigger for easy access later
4. Set action: add `Flag - Clicked {Product Name} Buy` tag
5. Save the rule
6. Apply the Link Trigger to every sales/landing page link in your launch emails

**Things to have handy:**
- Your sales page URL
- The `Flag - Clicked {Product Name} Buy` tag name

---

## Clickers Segment Creation

A segment of warm leads who clicked your sales page but haven't purchased. Used for targeted follow-up broadcasts.

**Setup:**
1. Create a new segment in ConvertKit
2. Name it descriptively (e.g., `{Product Name} - Clickers`)
3. Include condition: anyone with a value in your `{offername}_launch_score` (or `_buy_score`) custom field
4. Exclude condition: anyone with the `Purchased - {Product Name}` tag

**Broadcast template for Clickers:**
1. Create a new broadcast
2. Use the subject line field as a template name (for easy retrieval)
3. Add placeholder body copy
4. In sending settings, select your Clickers segment
5. Reuse this template whenever you want to send a targeted follow-up to warm leads

---

## Testing Checklist (All Automations)

Run this for every automation before going live:

1. Review all steps in the flow -- verify tags, custom fields, filters, and date events are correct
2. Turn on the automation
3. Add yourself to the flow (apply the trigger tag to your own subscriber profile)
4. Check the flow to confirm you appear inside it
5. Send yourself a preview of each email
6. Review every email from both phone and desktop
7. Click every link in every email -- verify they go to the right pages
8. Verify you receive all emails in the correct order with correct timing
9. For the Combined Pre-Launch + Launch automation: double-check all date events match your launch calendar
10. For the Abandoned Cart automation: test each objection branch by clicking each objection link
11. Verify opt-out links work correctly
12. Verify that purchasing removes the subscriber from active sequences

---

## Quick Reference: Automation Naming Conventions

| Automation | Naming Pattern |
|-----------|---------------|
| Post-Purchase | `{Product Name} - Post-Purchase Sequence` |
| Click Scoring | `{Product Name} - Click Scoring Automation` |
| Abandoned Cart | `{Product Name} - Abandoned Cart Sequence` |
| Pre-Launch + Launch | `{Product Name} - Pre-Launch & Launch Sequences` |

## Quick Reference: Sequence Naming Conventions

| Sequence | Naming Pattern |
|----------|---------------|
| Post-Purchase | `{Product Name} - Post-Purchase Sequence` |
| Abandoned Cart Part 1 | `{Product Name} - Abandoned Cart Sequence - Part 1` |
| Abandoned Cart Objections | `{Product Name} - Abandoned Cart Sequence - Objection - {Objection Type}` |
| Pre-Launch | `{Product Name} - {Month} {Year} - Pre-Launch Sequence` |
| Product Launch | `{Product Name} - {Month} {Year} - Product Launch Sequence` |
| Last Chance | `{Product Name} - {Month} {Year} - Product Launch Sequence Last Chance Email` |

---

## Integration Options (Purchased Tag)

Two ways to connect your e-commerce platform to ConvertKit for automatic `Purchased` tag assignment:

1. **Direct integration** -- Check ConvertKit's App Store. ThriveCart has a direct integration even though it isn't listed in the App Store.
2. **Zapier** -- Free no-code integration. Works with any platform that Zapier supports.
