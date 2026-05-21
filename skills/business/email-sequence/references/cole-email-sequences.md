# 5 Email Sequences for Low-Ticket Products (Cole/Bush)

Source: Nicolas Cole & Dickie Bush (Ship 30 for 30), Low-Ticket Product M&M Course, Module 8

---

## Table of Contents

1. [Sequence #1: Post-Purchase/Onboarding (6 emails)](#sequence-1-post-purchaseonboarding)
2. [Sequence #2: Abandoned Cart (5 emails)](#sequence-2-abandoned-cart)
3. [Sequence #3: Weekly Objection Handling for Clickers](#sequence-3-weekly-objection-handling)
4. [Sequence #4: 10-Day Launch (10 emails)](#sequence-4-10-day-launch)
5. [Sequence #5: 10-Day Pre-Launch (10 emails)](#sequence-5-10-day-pre-launch)
6. [Automation Logic & Tag Conventions](#automation-logic)

---

## Sequence #1: Post-Purchase/Onboarding

**Purpose:** Maximize customer success and satisfaction, reduce refund requests, gather feedback, and bridge to next product. Runs on autopilot via ConvertKit automation after purchase tag is applied.

### Overview Table

| # | Name | Timing | Purpose |
|---|------|--------|---------|
| 1 | The Warm Welcome | Immediately | Onboard, set expectations, deliver access |
| 2 | The Quick Follow-Up | 24 hours | Nudge to start, check if set up |
| 3 | The Biggest Challenge | 2-4 days | Preempt #1 obstacle, prevent dropout |
| 4 | The Underrated Feature | 2-4 days | Highlight overlooked value, referral ask |
| 5 | The Check-In Survey | 2-4 days | Gather feedback, offer bonus incentive |
| 6 | The Bridge | 5-7 days | Upsell to next product in ladder |

### Email #1: The Warm Welcome

- **Subject:** [emoji] [IMPORTANT] Welcome to {Product Name}
- **Preview:** Ready to {unlock outcome}?
- **Structure:**
  1. Greeting + excitement statement
  2. Restate promise: help them {overcome problem} and {unlock outcome}
  3. Walk through X onboarding steps (numbered, bolded headers)
  4. Link to start the product/course
  5. Sign-off
- **Key technique:** Step-by-step onboarding removes friction. Bold headers for scannability. Instruction to "read in its entirety" increases completion.

### Email #2: The Quick Follow-Up

- **Subject:** Have you dove into Onboarding yet?
- **Preview:** Just want to make sure you're all set!
- **Structure:**
  1. Check-in greeting
  2. If started -- great, disregard
  3. If not started -- "no worries!" + CTA to onboarding
  4. Bullet list: what they will find inside onboarding
  5. Ask to whitelist email address + emoji recognition tip
- **Key technique:** No pressure tone. Provides "permission" to start late. Whitelist ask improves deliverability.

### Email #3: The Biggest Challenge

- **Subject:** How are things going?
- **Preview:** Just checking in!
- **Structure:**
  1. Check-in question
  2. Acknowledge if doing well
  3. Name the #1 common challenge (normalize it with stats: "more than XX% experience this")
  4. Share specific tip/solution with explanation
  5. Offer to reply for help
  6. PS with resource link
- **Key technique:** Normalizes the struggle ("100% part of the process"). Proactively addresses the thing most likely to cause dropout.

### Email #4: The Underrated Feature

- **Subject:** Have you seen this yet?
- **Preview:** Dive into {feature name} today!
- **Structure:**
  1. Ask if they have used the feature
  2. Explain biggest benefit
  3. Step-by-step "Here's how it works" (3-4 bullets)
  4. Social proof: "customers constantly tell me this is one of the most underrated benefits"
  5. CTA to use feature
  6. PS: Referral/gift ask
- **Key technique:** Surfaces hidden value. The referral PS turns happy customers into word-of-mouth. Keeps engagement high mid-sequence.

### Email #5: The Check-In Survey

- **Subject:** A 3-minute request
- **Preview:** (And a free gift)
- **Structure:**
  1. Context: "Since it's been a few weeks..."
  2. Ask for 3-minute survey
  3. What their answers will help you do (2 bullets)
  4. BONUS incentive: "Everyone who fills out this survey gets FREE access to {bonus}"
  5. Describe bonus value (bullets + screenshot)
  6. Repeat CTA
- **Key technique:** Reciprocity -- bonus in exchange for feedback. "3 minutes" reduces perceived effort. Survey data becomes copywriting gold for future emails.

### Email #6: The Bridge

- **Subject:** What's next on your {topic/niche} journey?
- **Preview:** I'd love to help!
- **Structure:**
  1. Acknowledge milestone reached with current product
  2. List next-level activities they are probably doing (bullets)
  3. Ask: "Do you have an exact path?" / "Or does it feel fragmented?"
  4. Empathize: "I struggled with that too"
  5. Name the NEXT big problem
  6. List negative consequences of NOT solving it (bullets)
  7. Stack credibility (numbered list of achievements)
  8. Introduce upsell product with outcomes list
  9. CTA to upsell
  10. PS: Free preview/sneak peek
- **Key technique:** Future-pacing into the next problem. "Fragmented information" concept creates a gap only the upsell fills. This is the money email of the sequence.

### Automation Setup (ConvertKit)

- **Trigger:** Tag added -- `Purchased - {Product Name}`
- **Status tag:** `Status - In {Product Name} Post-Purchase Sequence` (added at start, removed at end)
- **Opt-out tag:** `Opt Out - {Product Name} Post-Purchase Sequence`
- **Naming convention:** `{Product Name} - Post-Purchase Sequence`

---

## Sequence #2: Abandoned Cart

**Purpose:** Follow up with warm leads who clicked your sales page 2+ times but did not buy. Self-segments by objection via link clicks, then sends targeted objection-handling emails.

### 3 Mistakes to Avoid

1. Only sending one email
2. Not gathering data to send targeted follow-ups
3. Sending abandoned cart emails manually (instead of automating)

### Flow Logic

1. Triggered when click score >= 2 (from Click Scoring Automation)
2. Filter: exclude anyone with `Purchased - {Product}` tag
3. Send Email #1 (The Follow-Up) after a few hours
4. Wait 24 hours, send Email #2 (Why Didn't You Buy) -- contains 3 clickable objection links
5. If no engagement, send a bump email re-sending the survey
6. Based on link click, route to one of 3 objection-specific emails
7. Exit automation immediately if purchase tag is applied

### Overview Table

| # | Name | Purpose | Sent To |
|---|------|---------|---------|
| 1 | The Follow-Up | Last nudge before survey | All clickers (2+) |
| 2 | Why Didn't You Buy | Self-segmenting survey via link clicks | Non-buyers |
| 3 | Price Objection Handler | Address price barrier | Clicked "too expensive" |
| 4 | Time Objection Handler | Address time barrier | Clicked "no time" |
| 5 | Not Ready Objection Handler | Address readiness barrier | Clicked "not ready" |

### Email #1: The Follow-Up

- **Subject:** hey - what happened?
- **Preview:** saw you almost joined {product name}
- **Structure:**
  1. "Just following up on your enrollment"
  2. "Looks like you were ready... what happened?"
  3. Remind of refund policy + lifetime access
  4. Social proof: link to testimonials/Wall of Love
  5. CTA
  6. PS: Price increase warning + testimonial screenshot
- **Key technique:** Casual, non-pushy tone. Refund policy removes risk. "Lifetime access" handles time objection preemptively.

### Email #2: Why Didn't You Buy

- **Subject:** Quick question?
- **Preview:** Your input would be appreciated
- **Structure:**
  1. "We noticed you checked out {product} a couple times but decided not to buy"
  2. Bold heading: "Is there a reason why?"
  3. Three clickable links (each links to a thank-you page but applies a tag via Link Trigger):
     - "It's still too expensive for me"
     - "I'm just not sure I have the time"
     - "I'm just not sure I'm ready"
  4. "Thanks in advance -- just want to be helpful"
- **Key technique:** Self-segmenting via link clicks. Each click triggers a ConvertKit tag that routes to the correct objection email. The redirect page is a simple "Thanks for sharing" confirmation.

### Email #3: Price Objection Handler

- **Subject:** Is price an issue?
- **Preview:** Let's remove that!
- **Structure:**
  1. "Thanks for letting me know price is an obstacle"
  2. Bold: "Let's remove that."
  3. Mission statement: "I NEVER want price to be a barrier"
  4. Introduce payment plan option
  5. CTA to payment plan checkout
  6. "Please don't share this publicly (honor system)"
- **Key technique:** Does NOT discount. Instead offers payment plan to "cashflow the investment." Mission-driven framing. Exclusivity via "don't share publicly."

### Email #4: Time Objection Handler

- **Subject:** What do you mean you "don't have time"?
- **Preview:** Some tough love for you.
- **Structure:**
  1. "Thanks for letting me know time is an obstacle"
  2. Personal story: "I was also busy when I started"
  3. Parkinson's Law framework (task expands to fill allotted time)
  4. Quote: "Give it to a busy person"
  5. "Constraints are your friend, not your enemy"
  6. "There will never be a perfect time" -- minimize regret framing
  7. Practical: "Only need X minutes per day" + lifetime access
  8. CTA
- **Key technique:** Tough love angle. Reframes "no time" as a feature, not a bug. Parkinson's Law provides intellectual framework. "Minimize regret" is the emotional closer.

### Email #5: Not Ready Objection Handler

- **Subject:** Nervous to get started?
- **Preview:** I get it -- but...
- **Structure:**
  1. "Thanks for letting me know you're hesitant"
  2. Social proof: "Do you know who else said that? The XXX people who already joined"
  3. "Over and over we hear: 'I don't think I'm ready.' Then they START... and suddenly THEY'RE READY"
  4. Mantra: "You can't steer a stationary ship"
  5. "I'm not ready" is a self-inflicted obstacle
  6. If-then list: if you have gotten value from content, if you find yourself learning... let me help
  7. "You have always been ready."
  8. CTA
- **Key technique:** Pattern interrupt -- uses the reader's own objection as proof they are ready. Mantra/quote provides memorable mental hook. "You have always been ready" is the emotional gut-punch.

### Automation Setup (ConvertKit)

- **Prerequisite:** Click Scoring Automation must be installed (see Sequence #3 below)
- **Trigger:** Custom field `{offername}_buy_score` >= 2
- **Filter:** Exclude `Purchased - {Product Name}`
- **Status tag:** `Status - In {Product Name} Abandoned Cart Sequence`
- **Naming:** `{Product Name} - Abandoned Cart Sequence`
- **Link Triggers on Email #2:** Each objection link applies a tag via ConvertKit Link Trigger; redirect goes to simple "Thanks for sharing" page
- **Objection sequences named:** `{Product Name} - Abandoned Cart Sequence - Objection - {Price|Time|Not Ready}`
- **Exit tags:** `Opt Out - {Product Name} Abandoned Cart Sequence` and `Purchased - {Product Name}`

---

## Sequence #3: Weekly Objection Handling

**Purpose:** Weekly broadcast emails sent ONLY to "Clickers" segment (people who clicked a buy link but did not purchase). Runs every Thursday (while free-value emails go to full list on Mondays).

### The 4 Core Objection Categories

1. **Price** -- "It's too expensive"
2. **Timing** -- "I don't have time right now"
3. **Fear/Doubt** -- "Will this actually work for me?"
4. **Comparison** -- "Is this better than other options?"

### The 7-Step Objection Handling Formula

1. **Call out the objection directly** -- Put it in the subject line. Don't dance around it.
2. **Validate before countering** -- "You aren't alone!" Let them know it is a common concern.
3. **Reframe the objection into an opportunity** -- This is the entire game. Whatever the objection, flip it into a reason to move forward.
4. **Use real numbers** -- Make the value calculation concrete, not theoretical.
5. **Address skepticism head-on** -- Say what they are thinking before they can think it. ("Yea, yea... of course you would say that.")
6. **Social proof with one real story** -- One detailed customer transformation > a thousand claims from you. Include specific results and a direct quote.
7. **End with a clear next step** -- Make it OBVIOUS what they should do. Include descending price anchors then reveal actual price as a bargain.

### Email Template Structure

```
Subject: "[Product Name] is [Objection]"
Preview: [Benefit-focused question]

Hey there!

Are you thinking of joining [Product Name] but [restate objection from their perspective]?

You aren't alone!

We have heard (from literally thousands of potential customers) the following reason:
"[Objection in quotes]"

OK... let's [strong reframe that shifts perspective].

[SPECIFIC numbers/data that make your case]
[Personality/humor to keep it conversational]
[VALUE calculation with actual numbers]

And no, we aren't just "throwing numbers in the air."
[Credibility statement]

"[What they're probably thinking]"

Then don't take our word for it.

[Customer story with SPECIFIC results]
[Relatable details -- let them see themselves]
[Actual quotes from the customer]

So, how much would you pay to unlock these sorts of outcomes?
$X,000?
$X,000?
$X,000?

Well, [Product] isn't anywhere near that -- it's cheaper!

[Strong CTA with future benefits]

(Or [restate the alternative] trying to figure it out on your own.)
```

### AI Prompt for Writing Objection Emails

Cole/Bush provide a mega-prompt for LLMs. Key inputs required:

- Product type, name, price
- Specific objection being addressed
- 3 key product benefits
- Target audience description
- Customer success story (name, background, transformation, quote)

The prompt instructs the LLM to follow the 7-step formula above, use conversational tone, 400-600 words, short paragraphs, occasional humor. See source material for full prompt text.

### Clickers Segment Setup (ConvertKit/Kit)

1. **Click Scoring Automation:**
   - Tag: `Flag - Clicked {Product Name} Buy` (applied via Link Trigger on every buy link)
   - Custom field: `{offername}_buy_score` (incremented each time someone enters the automation)
   - Naming: `{Product Name} - Click Scoring Automation`

2. **Link Triggers:**
   - Create a reusable rule: Trigger = sales page link, Action = apply flag tag
   - Add this Link Trigger to every buy/sales page link in every email

3. **Clickers Segment:**
   - Include: anyone where `{offername}_buy_score` >= 1
   - Exclude: anyone tagged `Purchased - {Product Name}`

4. **Broadcast Template:**
   - Create a broadcast template pre-configured to send to Clickers segment
   - Each Thursday: duplicate template, write new objection email, send

---

## Sequence #4: 10-Day Launch

**Purpose:** Hard-pitch sequence to maximize sales during a defined launch window. Sent daily for 10 consecutive days. Runs alongside (after) the Pre-Launch Sequence.

### Core Principles

- **Send more emails, not fewer.** More emails = more money. Unsubscribers who would never buy are no loss.
- **Every email gets a PS.** PS sections increase CTR by 30-40%.
- **Track clicks and send additional emails to warm leads.** Use Click Scoring Automation to identify hottest prospects.
- **Education continues during the pitch.** Even sales emails must answer the questions buyers need answered to feel confident purchasing.

### Overview Table

| # | Name | Subject Template | Purpose |
|---|------|-----------------|---------|
| 1 | Everything Included | "{Product} should cost ${XYZ}" | Full value breakdown, feature by feature |
| 2 | Bonuses | "These X bonuses are worth $XXX" | Highlight limited-time or hidden bonuses |
| 3 | Testimonial Roundup | "These {X} success stories will blow you away" | Multiple testimonials, each addressing a different objection |
| 4 | Where Will You Be 1 Year | "Where would you be if you started {action} last year?" | Future-pacing -- contrast action vs inaction |
| 5 | Testimonial Deep Dive | "{Crazy Outcome} in {X} months after {Product}?" | Single customer case study with financials |
| 6 | Tale of 2 Archetypes | "A tale of 2 {type of person}..." | Story of action-taker vs non-action-taker |
| 7 | Financial Outcomes | "${X,000} per month {doing thing}?" | Customer financial success story |
| 8 | If Not Now Then When | "If not now, then when?" | Demolish "timing" objection |
| 9 | Reasons Why Others Joined | "{X} challenges everyone faces" | Use actual customer survey responses as copy |
| 10 | Last Chance | "last call! (don't want you to miss out)" | Final deadline reminder + full feature recap |

### Email #1: Everything That's Included

- **Subject:** "{Product} should cost ${XYZ} -- at least." (use customer quote or financial metric)
- **Preview:** Social proof quote about value
- **Structure:**
  1. "Today we give you a full behind-the-scenes tour"
  2. Top-level feature list (bullets)
  3. "Let's dive in" -- then detailed breakdown of EACH feature with:
     - Feature name as H2 header
     - Description of outcomes it unlocks
     - "Normally this would cost {$X}"
  4. "Wowza! That's a lot!" summary
  5. Statement: "single most valuable {category} on the Internet"
  6. Reveal actual price
  7. CTA
  8. PS: One more feature they also get
- **Key technique:** Value stacking with dollar amounts per feature. Creates massive perceived value gap vs actual price. Screenshots/images make it tangible.

### Email #2: Bonuses

- **Subject:** These X bonuses are worth $XXX
- **Preview:** But... you can get them for free!
- **Structure:**
  1. "Quick reminder" -- bonus offer framing
  2. Each bonus with:
     - Name + dollar value
     - 3 benefit bullets
     - Screenshot/image
  3. "There's just one caveat" -- deadline
  4. "I only reward people who: take action, commit, are serious"
  5. CTA
- **Key technique:** Deadline creates urgency. Dollar values attached to each bonus increase perceived loss of inaction. "Reward" framing appeals to identity.

### Email #3: Testimonial Roundup

- **Subject:** These {X} success stories will blow you away
- **Preview:** Chances are, you're struggling with the same things they were.
- **Structure:**
  1. Social proof header: "Helped {X,000}+ people"
  2. Normalize their situation: "They were exactly where you are"
  3. List of common problems (bullets with "yet" -- implying temporary)
  4. For each testimonial (3-6):
     - Numbered with objection as header quote
     - Customer situation before buying
     - Specific results after (bullets)
     - Link to full story
  5. "We hope you see yourself in one of these stories"
  6. CTA
  7. PS: Additional short testimonial quotes
- **Key technique:** Each testimonial is framed around a SPECIFIC objection. Reader self-selects the story that matches their hesitation. "Yet" language implies these problems are solvable.

### Email #4: Where Will You Be 1 Year From Now?

- **Subject:** Where would you be if you started {action} last year?
- **Preview:** Are you going to let another year go by?
- **Structure:**
  1. Announce enrollment/availability
  2. Three "Have you been..." pain point questions
  3. "{Product} was made for you"
  4. Story of "Pray & Stay" vs "Ship & Sail" archetypes
  5. "If you had started 1 year ago, this is where you'd be:" (5 numbered outcomes)
  6. "Think about that!"
  7. Testimonial quotes (5-7 short ones)
  8. "Way more than just a {product type}" -- list benefits
  9. CTA
  10. PS: "There will never be a perfect time" regret minimization with repetition pattern ("So we put it off, again. And again. And again.")
- **Key technique:** Future-pacing via contrast: where you could be vs where you will be without action. The PS uses rhythmic repetition to make procrastination feel visceral.

### Email #5: Testimonial Deep Dive

- **Subject:** {Crazy Financial Outcome} in {timeframe} after {Product}?
- **Preview:** This could be you one year from now.
- **Structure:**
  1. Urgency: "Only {time} until {deadline}"
  2. One customer's complete story:
     - Financial metrics (with screenshot)
     - Before/after journey
     - ROI calculation: "~15,000% return on their ${price} investment"
  3. "A year from now, I hope we're writing this about you"
  4. "But most people will read this, have a little spark, then take no action"
  5. "No progress. No closer to their goals. And then the cycle repeats."
  6. CTA
  7. PS: Link to case study video/interview
- **Key technique:** Single deep-dive story is more persuasive than breadth. Financial ROI calculation makes the investment decision feel obvious. "Cycle repeats" creates urgency.

### Email #6: Tale of 2 Archetypes

- **Subject:** A tale of 2 {type of person}...
- **Preview:** Which one are you?
- **Structure:**
  1. "Still looking to {outcome}? Click here." (early CTA)
  2. "But if you're still unsure, I want to tell you a story."
  3. Introduce M (action-taker) and L (non-action-taker)
  4. L's inner obstacles (3 bullets: didn't need help, thought it was weakness, could figure it out alone)
  5. M's mindset (3 bullets: why do it alone, others are succeeding, best investment is myself)
  6. Contrast pairs: "L doubted himself, M trusted herself"
  7. Reveal: "This is actually our story -- and it's true"
  8. Share personal investment example and ROI
  9. "Be like M"
  10. CTA
  11. PS: Authority quote (e.g., Hormozi on investing in yourself)
- **Key technique:** Based on the Wall Street Journal's "A Tale of Two Young Men" -- one of the highest-grossing sales letters ever. Identity-level persuasion: reader chooses which archetype they want to be.

### Email #7: Financial Outcomes

- **Subject:** ${X,000} per month {doing thing}?
- **Preview:** This could be you in a few months!
- **Structure:**
  1. "We talk a lot about how {Product} can change your life"
  2. Social proof: "Helped {X} people {outcomes}"
  3. One customer's financial success story (Before/After with quotes)
  4. Link to full post/case study
  5. "If their story reminds you of yourself, take ACTION"
  6. CTA
  7. PS: Update on customer's continued success + CTA
- **Key technique:** Financial outcomes are the most persuasive proof for income-oriented products. The UPDATE in the PS shows ongoing, compounding results.

### Email #8: If Not Now, Then When?

- **Subject:** If not now, then when?
- **Preview:** Why it will never be the "right time" to start {action}.
- **Structure:**
  1. Direct question: "If you don't start now, when do you plan to?"
  2. Name the excuse: "I don't have the time"
  3. Personal story of being busy
  4. Reframe: "For things you care about, you don't find time -- you MAKE time"
  5. "Once" trap list: "Once work slows down... Once I feel ready..." (5 examples)
  6. "These 'onces' never go away"
  7. Practical: "Do you have X minutes per day?"
  8. Product designed for busy people + lifetime access
  9. "If not NOW, then when?"
  10. CTA
- **Key technique:** Systematically destroys every variant of the timing excuse. The "onces" list is universally relatable. Practical time commitment makes it feel doable.

### Email #9: Reasons Why Others Joined

- **Subject:** {X} challenges everyone faces
- **Preview:** How we solve them, and why thousands have taken the leap
- **Structure:**
  1. "When you join, first thing we ask is why + what you're struggling with"
  2. Section 1 -- "Why do you want {outcome}?" (5-8 real customer quotes)
  3. Section 2 -- "Biggest challenge?" (5-7 real customer quotes)
  4. "Everyone has different goals but the same problems" (problem list)
  5. "We built {Product} to demolish each one"
  6. Section 3 -- "What had you on the fence?" (5 real quotes showing how they overcame hesitation)
  7. CTA
  8. PS: Refund policy reminder
- **Key technique:** Uses actual customer survey language as copy. Reader sees their own words reflected back. "Mirror neurons" effect -- they think "this was made for me." Pro tip: copy/paste exact phrases from your onboarding survey.

### Email #10: Last Chance

- **Subject:** last call! (don't want you to miss out)
- **Preview:** {X} hours left!
- **Structure:**
  1. Deadline reminder (GIF countdown if possible)
  2. CTA (early)
  3. "You can always join later (for full price)" OR "wait for perfect conditions (which never come)"
  4. Full feature/benefit recap (bullets with emoji)
  5. "All that on top of gaining unbelievable momentum"
  6. CTA (repeated)
  7. Testimonial quotes (5)
  8. PS: Refund policy
  9. PPS: Payment plan option
- **Key technique:** Final email must include: full feature recap, refund policy, deadline, and payment plan. These 4 elements combine to remove every remaining barrier simultaneously.

### Automation Setup (ConvertKit)

- **Combined automation:** Pre-Launch + Launch in one flow
- **Naming:** `{Product Name} - Pre-Launch & Launch Sequences`
- **Trigger:** Tag -- `Flag - Start {Product Name} Launch Sequence - {Month} {Year}`
- **Flow:**
  1. Wait until pre-launch start date
  2. Add status tag: `Status - In {Product Name} Launch Sequence - {Month Year}`
  3. Run Pre-Launch Sequence (10 emails)
  4. Wait until launch start date
  5. Run Launch Sequence (emails 1-9)
  6. Wait until 6 hours before launch ends
  7. Filter: only continue if click score >= threshold
  8. Send Last Chance email (email 10)
  9. Wait until morning after launch ends
  10. Remove status tag
- **Exit tags:** `Opt Out - {Product Name} Product Launch Sequence` and `Purchased - {Product Name}`

---

## Sequence #5: 10-Day Pre-Launch

**Purpose:** Fill the "Education Deficit" before pitching. Educate potential customers about the problems your product solves and the outcomes it enables so they feel informed when the sale opens. Every email includes a CTA to join the waitlist (measures buying intent + triggers Consistency Bias).

### Core Concept: The Education Deficit

Before buying anything, people need to answer a series of internal questions to FEEL like they are making an educated decision. If you do not educate them, they will not buy. Most failed launches are not a pricing problem or a landing page problem -- they are an education problem.

### 3 Mistakes to Avoid

1. **Focusing on features instead of problems/outcomes.** Pre-launch is about educating on problems, not bragging about features.
2. **Not sending enough emails.** More emails = more sales. Let the uninterested unsubscribe.
3. **No CTA.** Even though you are not selling yet, always include a waitlist CTA. It measures intent and activates Consistency Bias.

### Overview Table

| # | Name | Subject Template | Purpose |
|---|------|-----------------|---------|
| 1 | Plain Waitlist Announcement | "[ANNOUNCEMENT] Introducing: {Product}" | Announce product, state problem solved, open waitlist |
| 2 | Who This Is For | "Quiz: Is {Product} right for you?" | Self-identification via pain-point questions + archetypes |
| 3 | Biggest Problems | "Which of these problems sounds familiar?" | List 5-10 problems your product solves |
| 4 | Desired Outcomes | "Where you could be one year from now..." | Future-pacing visualization of life after transformation |
| 5 | Origin Story | "{Approach} will change your life" | Your before/after journey -- reader is the hero |
| 6 | Stop/Start | "X skills {group} need to {capitalize on trend}" | Old way vs new way -- what to stop and start doing |
| 7 | Biggest Myths | "X faulty beliefs keeping you from {outcome}" | Demolish 3 faulty beliefs with reframes |
| 8 | Quick Tips | "X simple tips to {outcome}" | Give away actionable value, then highlight execution gap |
| 9 | Biggest Mistake | "Are you making any progress?" | Name the #1 mistake, introduce your method as the fix |
| 10 | Templates | "How to {outcome} -- 10x faster" | Tease product templates to show actionability |

### Email #1: Plain Waitlist Announcement

- **Subject:** [ANNOUNCEMENT] Introducing: {Your Product Name}
- **Preview:** The waitlist is officially open!
- **Structure:**
  1. "I have a very special announcement"
  2. "In X days, I'm launching my best product yet"
  3. Credibility: "Over the past X years, I've {big milestone}"
  4. Proof bullets (3-4 tangible milestones)
  5. Introduce product name with bold header
  6. "You don't achieve {outcome} by just {common advice}. You need to..."
  7. "How do I know? This is the exact blueprint I've used"
  8. Exclusivity: "ONLY available for X days" with specific dates
  9. "I only reward people who take ACTION"
  10. Waitlist CTA
  11. Promise: "Over the next X days, I'll send you a FREE masterclass"
  12. Waitlist CTA (repeated)
- **Key technique:** Combines announcement, credibility proof, scarcity (limited window), and waitlist CTA. Promise of free education in upcoming emails keeps them opening.

### Email #2: Who This Is For

- **Subject:** Quiz: Is {Product} right for you?
- **Preview:** Let's find out!
- **Structure:**
  1. "Here are 10 questions to help you decide"
  2. 9-10 "Do you..." questions targeting specific pain points (bold key phrases)
  3. "If you answered Yes to any -- you're in luck"
  4. Social proof: "{XXX} others who went through {Product} faced the same problems"
  5. 3 archetypes of people the product serves (brief description each)
  6. "If you fall into one of these categories, {Product} was made for you"
  7. CTA
- **Key technique:** Quiz format drives self-identification. Each question mirrors an internal dialogue the reader already has. The archetype list gives them permission to see themselves as the target customer.

### Email #3: Biggest Problems

- **Subject:** Which of these problems sounds familiar?
- **Preview:** Hint: it's probably more than one
- **Structure:**
  1. "What's keeping you from {outcome}?"
  2. Three common scenarios (sentence each)
  3. "I designed {Product} to solve these exact problems"
  4. For each of 5-9 problems:
     - Bold problem name as header
     - Describe the symptom
     - Introduce your specific solution/framework
     - "I'll show you how inside {Product}"
  5. Summary CTA
- **Key technique:** Problem-aware selling. Each problem section names the pain, then immediately teases the solution. Reader counts how many problems apply to them -- more = stronger purchase intent.

### Email #4: Desired Outcomes

- **Subject:** Where you could be one year from now...
- **Preview:** If you joined {Product} today.
- **Structure:**
  1. "Let's fast forward. Imagine it's {date one year out}."
  2. "It has been a year since you {started approach}"
  3. "Not because you {did extreme thing}. But because you {did manageable thing}."
  4. 3 major changes (each as H3 header):
     - Change #1: Internal transformation
     - Change #2: Skill/capability unlocked
     - Change #3: External/financial outcomes (bullet list of specifics)
  5. "Does this seem too good to be true? It shouldn't."
  6. Real customer examples proving these outcomes
  7. CTA
- **Key technique:** Immersive future-pacing. The reader is placed IN the future and walks through their transformed life. Third change is always the most tangible/financial to anchor desire.

### Email #5: Origin Story

- **Subject:** {Your approach} will change your life.
- **Preview:** Because it changed mine.
- **Structure:**
  1. Bold claim + "How do I know? Because it changed MINE"
  2. "Since I started, I have..." (4 big outcomes, bulleted)
  3. "I'd like to share my story. Because you're in the same boat I was."
  4. Starting point: "I started {trying outcome} back in {year}"
  5. The struggle: wrong methods, wasted time, painful experience
  6. "Sound familiar?"
  7. The turning point: "I threw the old playbook out"
  8. Results: Before/After contrast list
  9. Compounding benefits list
  10. "Turns out there was something to this {approach}"
  11. From personal discovery to product creation story
  12. "Now, I've helped XXX people"
  13. Their results mirror yours (outcomes list)
  14. Promise: "{Approach} is the fastest way to {solve problem}"
  15. CTA
- **Key technique:** Reader is the hero, not you. Your story exists to show: I was where you are, I found the way, now I can guide you. The turning point is always the unique methodology/approach that becomes the product.

### Email #6: Stop/Start

- **Subject:** X skills/changes {group} need to {capitalize on trend}
- **Preview:** {Old way group} will struggle. {New way group} will thrive.
- **Structure:**
  1. "{Old way group} are going to struggle a LOT"
  2. Define who old-way people are (3 bullet examples)
  3. Binary choice: "Do you want to {old way} and struggle? Or {new way} and thrive?"
  4. Consequences of each path
  5. For each change (3-5):
     - Named header
     - What people currently do wrong
     - Consequences of continuing
     - What they should do instead
     - How your product helps
  6. "When you join {Product}, I'll show you how to implement ALL of these"
  7. Feature list tied to each change
  8. CTA
- **Key technique:** Creates an identity-level binary. Reader must choose a camp. The old way is painted so unappealingly that "doing nothing" feels like choosing the wrong side.

### Email #7: Biggest Myths

- **Subject:** X faulty beliefs keeping you from {outcome}
- **Preview:** Most beginner {group} struggle with these...
- **Structure:**
  1. "If you're reading this, you probably want {outcome}"
  2. Three scenarios with red X emoji
  3. "Why haven't you seen the progress you wanted?"
  4. "99% of the time, what holds people back are faulty beliefs"
  5. For each myth (3):
     - Named as quoted belief
     - "Let's stress-test this"
     - Logical argument dismantling the belief
     - "This is a faulty belief."
  6. "You will never overcome these by {unproductive method}"
  7. "If you could, you would have already"
  8. CTA
- **Key technique:** Names the enemy (faulty beliefs) rather than blaming the reader. Each myth is stress-tested with logic, making the reader feel smart for seeing through it. "If you could, you would have already" is the closer.

### Email #8: Quick Tips

- **Subject:** X simple tips to {outcome}
- **Preview:** That you can implement TODAY
- **Structure:**
  1. "Today I want to share X tips to help you {outcome}"
  2. For each tip (5-12):
     - Named tip with numbered header
     - Explanation + benefit
     - How it connects to your product/methodology
  3. Divider
  4. "Want help actually putting these into action?"
  5. "Reading tips alone will NOT help you {outcome}. You need to put them into practice."
  6. "That's easier said than done. So if you'd like help..."
  7. CTA
- **Key technique:** Give away the WHAT (information) for free. Charge for the HOW (implementation, accountability, templates). The "knowing-doing gap" is the sales mechanism. Reader realizes they already knew most of this but have not acted.

### Email #9: Biggest Mistake

- **Subject:** Are you making any progress?
- **Preview:** Chances are, you're making this simple mistake.
- **Structure:**
  1. "How long have you been trying?" (time range options)
  2. Name the ineffective method most people use
  3. "They have no idea they're doing things the hard way"
  4. Explain WHY the common method does not work
  5. "That's why in {Product} we teach {your method} instead"
  6. Explain why your method works
  7. "There's an art to it -- otherwise everyone would do it"
  8. Name the actual key to success
  9. "Is your approach not working?"
  10. "I've helped {X} others -- I'd love to help YOU"
  11. CTA
- **Key technique:** Positions common approaches as "the hard way" and your method as "the shortcut." Reader feels validated (their effort was not wasted, just misdirected) and hopeful (there IS a better way).

### Email #10: Templates

- **Subject:** How to {outcome} -- 10x faster
- **Preview:** My secret {topic} templates
- **Structure:**
  1. "Do you struggle with {problem templates solve}?"
  2. Personal story: "I used to spend hours on {process}. It was exhausting."
  3. "That's why I included templates in {Product}"
  4. For each template (3-5):
     - Template name as H2
     - Screenshot/teaser image
     - Frustration it eliminates
     - How it works
     - Biggest benefit
  5. "Ready to {outcome} -- 10x faster?"
  6. "Why waste time reinventing the wheel?"
  7. CTA
- **Key technique:** Templates are the most concrete, tangible proof of product value. They answer: "What will I actually GET?" Screenshots make it real. "10x faster" anchors the speed benefit.

---

## Automation Logic

### ConvertKit Tag Naming Conventions

| Tag Type | Convention | Example |
|----------|-----------|---------|
| Purchase | `Purchased - {Product Name}` | `Purchased - Ship 30` |
| Status (in sequence) | `Status - In {Product Name} {Sequence Type}` | `Status - In Ship 30 Post-Purchase Sequence` |
| Opt-out | `Opt Out - {Product Name} {Sequence Type}` | `Opt Out - Ship 30 Abandoned Cart Sequence` |
| Click flag | `Flag - Clicked {Product Name} Buy` | `Flag - Clicked Ship 30 Buy` |
| Launch start | `Flag - Start {Product Name} Launch Sequence - {Month} {Year}` | `Flag - Start Ship 30 Launch Sequence - Jan 2024` |

### Custom Fields

| Field | Convention | Used In |
|-------|-----------|---------|
| Click score (launch) | `{offername}_launch_score` | Click Scoring Automation (launch) |
| Click score (evergreen) | `{offername}_buy_score` | Click Scoring Automation (evergreen) |

### Click Scoring Automation Flow

1. Triggered by flag tag (applied via Link Trigger on buy links)
2. Remove the flag tag (so it can be re-triggered)
3. Check if custom field exists
4. Increment custom field by 1
5. Loop back to listen for next click

### Combined Pre-Launch + Launch Automation Flow

1. Add all subscribers to automation via flag tag
2. Wait until pre-launch start date
3. Add status tag
4. Run Pre-Launch Sequence (10 emails, daily)
5. Wait until launch start date
6. Run Launch Sequence (emails 1-9, daily)
7. Wait until 6 hours before launch close
8. Filter: only proceed if click score >= 2
9. Send "Last Chance" email to warm leads
10. Wait until morning after launch close
11. Remove status tag
12. Exit conditions: purchase tag or opt-out tag at any point

### Abandoned Cart Automation Flow

1. Triggered by custom field (`{offername}_buy_score` >= 2)
2. Filter: exclude anyone with purchase tag
3. Add status tag
4. Wait a few hours
5. Send "The Follow-Up" email
6. Wait 24 hours
7. Send "Why Didn't You Buy" email (with 3 link-trigger options)
8. Wait for link click or 48 hours
9. Branch based on tag applied by link click:
   - Price tag -> Send Price Objection Handler
   - Time tag -> Send Time Objection Handler
   - Not Ready tag -> Send Not Ready Objection Handler
   - No click -> Send bump email, then branch again
10. Wait 1 day
11. Remove status tag
12. Exit conditions: purchase tag or opt-out tag at any point
