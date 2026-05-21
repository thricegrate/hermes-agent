# Abandoned Cart Sequence Template (4 Emails)

4 emails targeting warm leads who clicked your product/sales page but didn't buy. These people are interested: they just need a nudge. Replace all [bracketed placeholders] with your specifics.

**Trigger:** Subscriber clicks product page link but does not purchase within 2 hours
**Total duration:** 5 days
**Goal:** Convert warm leads who showed intent but didn't follow through

---

### Email 1: Gentle Reminder

**Subject:** Did you forget something?
**Alt Subject:** Still thinking about [Product Name]?
**Preview:** I noticed you were checking it out
**Send:** 2 hours after clicking product page (no purchase)

---

Hey [First Name],

I noticed you were checking out **[Product Name]** earlier.

No pressure at all, I just wanted to make sure you had everything you needed to make a decision.

**Quick reminder of what's inside:**
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]
- [Benefit 4]
- [Benefit 5]

If you have any questions, just reply to this email. I'm happy to help.

**[CTA Button: "Take Another Look at [Product Name]": link to sales page]**

[Name]

PS: Remember, [Product Name] comes with a [X-day money-back guarantee]. You can try it completely risk-free.

---

### Email 2: Overcome #1 Objection

**Subject:** The real reason most people hesitate
**Alt Subject:** I get it: here's what I'd want to know too
**Preview:** Let me address the elephant in the room
**Send:** Day 1 (24 hours after Email 1)

---

Hey [First Name],

I know why you might be hesitating about [Product Name].

The #1 reason people don't pull the trigger is: **[State the #1 objection, e.g., "they're not sure it'll work for their specific situation" / "the price feels like a lot" / "they're worried about the time commitment"]**.

I totally get it. Let me address that head-on:

[3-4 paragraphs directly addressing the objection. Be specific and honest. Include:]

- [Evidence that counters the objection: data, testimonial, logic]
- [A relatable example of someone who had the same concern and overcame it]
- [A reframe that changes how they see the objection]

Here's the thing: **[Product Name] comes with a [X-day money-back guarantee].** That means you can try it, see if it works for you, and if it doesn't, you get every penny back. No questions asked.

The only real risk is not trying.

**[CTA Button: "Try [Product Name] Risk-Free": link to sales page]**

[Name]

---

### Email 3: Social Proof + Urgency

**Subject:** What [X] people are saying about [Product Name]
**Alt Subject:** They were on the fence too
**Preview:** Then they tried it: here's what happened
**Send:** Day 3 (2 days after Email 2)

---

Hey [First Name],

I want to share a few quick stories from people who were in your exact position, on the fence about [Product Name]:

---

**[Name 1] was hesitant because [objection].**
Result: "[Short testimonial about their outcome]"

---

**[Name 2] almost didn't buy because [objection].**
Result: "[Short testimonial about their outcome]"

---

**[Name 3] wasn't sure if [Product Name] was right for them.**
Result: "[Short testimonial about their outcome]"

---

Every one of them was exactly where you are right now. They had the same doubts. They took the step anyway. And it paid off.

**One more thing:** [Urgency element: "The current price won't last much longer" / "Bonus [X] is disappearing soon" / "[X] spots remaining in the community"]

**[CTA Button: "Join Them, Get [Product Name]", link to sales page]**

[Name]

PS: Reply to this email if you have any questions. I'll personally answer every one.

---

### Email 4: Final Chance

**Subject:** Last chance: [Product Name] + [bonus/discount]
**Alt Subject:** I don't usually do this, but...
**Preview:** A little something extra to help you decide
**Send:** Day 5 (2 days after Email 3)

---

Hey [First Name],

This is the last email I'll send you about [Product Name].

I know you've been thinking about it. You clicked through. You read about what's inside. Something about it resonated with you.

So I want to make this as easy as possible:

**[Choose one or combine:]**

**Option A: Bonus incentive:**
If you grab [Product Name] in the next 24 hours, I'll throw in **[Exclusive Bonus]** (a $[X] value) completely free. This bonus isn't available anywhere else. It's my way of saying "I appreciate you giving this a shot."

**Option B: Discount incentive:**
Use code **[DISCOUNT CODE]** at checkout for [X]% off [Product Name]. This code expires in 24 hours and won't be offered again.

**Option C: Both:**
Grab [Product Name] in the next 24 hours and you'll get **[Bonus]** free AND [X]% off with code **[CODE]**.

---

**Here's what you're getting:**
- [Product Name]: [1 sentence description]
- [Bonus 1]
- [Bonus 2]
- [Special abandoned cart bonus/discount]
- [X-day money-back guarantee]

**[CTA Button: "Get [Product Name] + [Bonus/Discount]": link to sales page]**

This is genuinely my last email about [Product Name]. No more follow-ups after this.

If it's not for you, I completely understand. The newsletter continues as always, and I'll keep delivering value every [frequency].

But if something inside you is saying "I should do this", trust that feeling.

**[Link: "Get [Product Name] before this offer expires"]**

[Name]

PS: [X-day money-back guarantee]. If you don't love it, you get a full refund. You have literally nothing to lose and [primary outcome] to gain.

---

## Sequence Setup Notes for Beehiiv

1. **Trigger:** Subscriber clicks sales page link + does NOT receive purchase confirmation tag within 2 hours
2. **Exclusions:**
   - Remove subscriber from sequence immediately if they purchase at any point
   - Don't enroll subscribers who are already in an active launch sequence
   - Don't enroll subscribers who have already been through this sequence in the last 30 days
3. **Tags:**
   - Add `abandoned-cart-active` when sequence starts
   - Remove `abandoned-cart-active` and add `abandoned-cart-complete` when sequence ends
   - Track which email converts (for optimization)
4. **Opt-out:** Include in every email: "Not interested in [Product Name]? [Click here] and I won't send you any more emails about it."
5. **Discount codes:** If using discount codes, set them to auto-expire to maintain integrity
6. **Metrics to track:**
   - Which email converts the most (usually Email 2 or Email 4)
   - Overall recovery rate (aim for 5-15% of abandoned carts)
   - Revenue recovered per sequence run
