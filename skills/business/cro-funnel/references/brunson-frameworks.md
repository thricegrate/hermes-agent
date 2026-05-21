# Brunson Funnel Frameworks

Russell Brunson's funnel diagnosis, hacking, and benchmarking frameworks. Use alongside the economics framework and Kennedy funnel economics for a complete diagnosis.

---

## Traffic Temperature Diagnosis

Every funnel receives three temperatures of traffic. If you don't diagnose by temperature, you'll misread your conversion data.

### The Three Temperatures

**Hot traffic:** People who already know you. Email list, social followers, past buyers, podcast listeners. They trust you. They've consumed your content. They just need the right offer at the right time.

**Warm traffic:** People who know someone who knows you. Referred by a friend, saw a share, came through an affiliate, landed on a guest post. They have borrowed trust but haven't built their own yet.

**Cold traffic:** Strangers. Paid ads, SEO, random social discovery. Zero trust. Zero context. They don't know you, don't know your story, don't know if you're legit.

### Expected Conversion Multipliers

```
Hot traffic should convert 2-5x what cold traffic converts.
Warm traffic should convert 1.5-3x what cold traffic converts.

Example (sales page conversion):
  Cold: 1% conversion rate
  Warm: 1.5-3% conversion rate
  Hot:  2-5% conversion rate
```

### Diagnosis by Temperature

Use this to find the real problem when "conversions are low":

**If hot traffic isn't converting:**
- The offer is broken. Period.
- Hot traffic already trusts you. If they see the offer and don't buy, the offer itself is the problem.
- Don't touch ads. Don't rewrite emails. Fix the offer first.
- Route to `product-offer`.

**If warm traffic converts but cold doesn't:**
- The pre-frame is broken.
- Cold traffic needs more context before they see the offer.
- Fix: add a bridge page, video sales letter, or warming sequence between the ad and the offer.
- The ad is doing its job (getting clicks). The landing experience isn't building enough trust before the ask.

**If only hot traffic converts:**
- Both pre-frame and offer need work.
- You're surviving on loyalty, not on a compelling offer.
- The offer might be "good enough" for fans but not strong enough to stand on its own.
- Fix: strengthen the offer (route to `product-offer`), then fix the pre-frame for cold/warm.

**If cold converts but hot doesn't:**
- Rare, but it means your existing audience doesn't want this offer.
- You may have a market-message mismatch with your current list.
- The cold traffic is finding you through different positioning than your existing audience expects.

### Temperature Diagnosis Checklist

- [ ] Segment conversion data by traffic source (email list vs. ads vs. referrals vs. organic)
- [ ] Calculate conversion rate for each temperature bucket
- [ ] Check if hot converts 2-5x cold. If not, offer problem.
- [ ] Check if warm converts 1.5-3x cold. If not, pre-frame problem.
- [ ] Identify which temperature is underperforming relative to benchmarks
- [ ] Prescribe fix based on which temperature is broken (see above)

---

## Funnel Hacking

Reverse-engineer what's already working in your market. Don't guess. Don't theorize. Go through competitors' funnels as a customer and document everything.

### The Process

**Step 1: Identify 3-5 competitors or adjacent players**
- Direct competitors selling similar products
- Adjacent players selling to the same audience (different product, same people)
- Players in other niches using funnel models you want to replicate

**Step 2: Go through their funnel as a real customer**
- Click their ads. Screenshot the ad creative and copy.
- Land on their page. Screenshot above the fold, full page, mobile view.
- Opt in with a real email. Note what happens on the confirmation page.
- Read every email in their sequence. Save all of them. Note timing and subject lines.
- Buy their cheapest product. See the checkout page, OTO sequence, thank you page.
- If they have a webinar, attend it. Note the pitch structure and timing.
- If they have a call booking step, book the call. Note the application questions.

**Step 3: Document the flow**

For each competitor, map:

```
Traffic source: [Where you found them -- ad platform, social, search]
Ad/hook: [What the ad said, what made you click]
Landing page: [Headline, lead magnet offer, opt-in mechanism]
Confirmation page: [What happens after opt-in -- redirect, upsell, video?]
Email sequence: [# of emails, timing, tone, CTAs, subject lines]
Sales page: [Price, headline, proof elements, guarantee, bonuses]
OTO sequence: [What upsells appear, prices, take-or-leave framing]
Backend: [Do they pitch a call? Webinar? Higher-tier offer?]
```

**Step 4: Identify patterns**
- What do the top 3 all have in common? That's probably table stakes.
- What does the #1 player do differently? That's probably their edge.
- Where do they all seem weak? That's your opportunity.

### What to Steal vs. What to Skip

**Steal the structure, not the copy.**
- Funnel architecture (what pages in what order)
- Email sequence timing and cadence
- Price anchoring and OTO structure
- Traffic sources that are clearly working (they keep running the same ads)

**Skip:**
- Exact copy (yours needs to match your voice and audience)
- Design details (unless they're clearly driving conversion)
- Anything that feels like it works only because of their specific brand/audience

### Funnel Hacking Checklist

- [ ] Identified 3-5 competitors or adjacent players to study
- [ ] Signed up for all their funnels with a real email
- [ ] Screenshotted every page in the flow (ads, landing, confirmation, sales, OTOs)
- [ ] Saved all emails in their sequences (note timing between each)
- [ ] Bought at least one product to see the post-purchase flow
- [ ] Mapped the complete flow for each (traffic -> landing -> nurture -> sales -> upsell -> backend)
- [ ] Identified 3+ patterns shared across top competitors
- [ ] Identified 1-2 gaps or weaknesses to exploit
- [ ] Documented findings in a swipe file for reference during builds

---

## Brunson Funnel Benchmarks

Conversion rate ranges by funnel type. Use these to diagnose whether your funnel is underperforming, on track, or crushing it.

### Tripwire Funnel ($1-$47 front end)

The goal is to convert a lead into a buyer, not to profit. Profit comes from OTOs and backend.

```
Landing page opt-in:        25-50% (cold), 40-65% (warm/hot)
Tripwire purchase rate:      8-12% of front-end visitors
OTO 1 take rate:             15-25% of buyers
OTO 2 take rate:             5-12% of buyers
Average cart value:          1.5-2.5x front-end price (with OTOs)
```

**Diagnosis:**
- Below 8% front-end conversion: headline or price-value mismatch. Test lower price or stronger hook.
- Below 15% OTO 1: OTO isn't a logical next step, or the transition is jarring. OTO should feel like "you'll also need this."
- Above 12% front-end: you might be underpricing. Test a higher price point.

### Webinar Funnel (free or paid webinar -> $297-$2,000 offer)

```
Registration rate:           15-30% of landing page visitors (cold), 30-50% (warm/hot)
Show-up rate:                25-40% (live), 60-80% (automated/replay)
Stay to pitch:               50-70% of attendees
Attendee-to-buyer rate:       5-15%
Registration-to-buyer rate:   2-5% (overall, factoring dropoff)
```

**Diagnosis:**
- Registration below 15%: headline doesn't promise a clear, specific result. "How to [specific outcome] in [timeframe]" outperforms vague titles.
- Show-up below 25%: reminder sequence is weak or registration-to-webinar gap is too long. Same-day or next-day webinars show higher.
- Attendee-to-buyer below 5%: pitch is too early, too long, or the offer doesn't match the webinar content. The webinar should create the problem the offer solves.
- Above 15% attendee-to-buyer: consider raising the price or testing a higher-tier offer.

### Application Funnel (qualify -> call -> $2,500-$50,000 offer)

```
Landing page to application:   10-25%
Application completion:         50-70%
Application to call booked:     30-60% (depends on qualification strictness)
Call show rate:                  60-80%
Call-to-close rate:              10-30%
Overall application-to-close:   10-30% (of completed applications)
```

**Diagnosis:**
- Application rate below 10%: the page isn't selling the outcome of the call, or the application feels too long. Keep to 5-8 questions max.
- Completion below 50%: too many questions, or questions feel invasive too early. Front-load easy questions, save revenue/budget questions for last.
- Show rate below 60%: confirmation sequence is weak. Add a video from the founder, a case study, and 2-3 reminders.
- Close rate below 10%: either unqualified leads are getting through (tighten application) or the sales process needs work (route to `high-ticket-closer`).

### Challenge Funnel (free or paid 5-14 day challenge -> $97-$997 offer)

```
Registration rate:              20-40% of landing page visitors
Day 1 participation:            40-60% of registrants
Completion rate (all days):     15-30% of registrants
Participant-to-buyer rate:       5-10% of active participants
Registration-to-buyer rate:      2-5% (overall)
```

**Diagnosis:**
- Registration below 20%: the challenge promise is too vague. Specific transformation ("Build your first funnel in 5 days") beats generic ("Learn about funnels").
- Day 1 below 40%: gap between registration and start is too long, or Day 1 content isn't immediately actionable. Start the challenge within 24 hours of sign-up.
- Completion below 15%: daily tasks are too hard or too time-consuming. Each day should take 15-30 minutes max.
- Participant-to-buyer below 5%: the challenge didn't create enough momentum or the offer doesn't feel like the natural next step. The challenge should get them 80% of the way there, and the offer should be the remaining 20%.

### Cross-Funnel Temperature Adjustments

All benchmarks above assume mixed traffic. Adjust by temperature:

```
Cold traffic:   multiply conversion benchmarks by 0.5-0.7x
Warm traffic:   use benchmarks as-is (1x)
Hot traffic:    multiply conversion benchmarks by 1.5-2.5x
```

If your hot traffic numbers fall below the "cold" range, the offer is fundamentally broken regardless of funnel type.

---

## Quick Reference: When to Use Which Funnel Type

| Situation | Funnel Type | Why |
|-----------|-------------|-----|
| Building a buyer list fast | Tripwire | Low friction, high volume, profit on backend |
| Selling $297-$2K offers | Webinar | Education builds trust for mid-ticket purchases |
| Selling $2.5K+ offers | Application | Qualification protects your time and close rate |
| Launching to a warm list | Challenge | Engagement builds momentum and social proof |
| Testing a new offer | Tripwire | Cheapest to test, fastest feedback loop |
| Reactivating a dead list | Challenge | Re-engages through participation, not just emails |

---

## Integration with Existing Frameworks

**With economics framework:** Use Brunson benchmarks to set realistic targets per funnel type, then apply the LTV/CAC math from `economics-framework.md` to determine if the economics work at those conversion rates.

**With Kennedy funnel economics:** Brunson benchmarks tell you what's possible. Kennedy's "compete on economics" tells you whether hitting those benchmarks actually makes you money. A 10% tripwire conversion means nothing if your LTV:CAC is below 1x.

**With traffic temperature diagnosis:** Always segment your benchmark comparison by traffic temperature. A 3% webinar close rate on cold traffic is actually decent. A 3% close rate on hot traffic means the offer or pitch is broken.
