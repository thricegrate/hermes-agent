# Template Prompts (Adapted)

Adapted versions of the 40 Nano Banana 2 ad templates, integrated with our brand analysis pipeline.

**Key differences from originals:**
- `{BRAND_MODIFIER}` placeholder at the start of each prompt (auto-filled from `website-brand-analysis` Image Generation Prompt Modifier)
- Funnel stage tags (TOFU/MOFU/BOFU) for campaign planning
- **Product images** tag: whether passing real product photos as reference improves output quality
- Aspect ratio removed from prompt body (set in platform UI)
- Copy quality notes where `review-miner` or `copy-writing` can upgrade the output
- Our naming conventions matching `ads-strategy` categories

**Usage in batch mode:** When running batch generation, prepend the Brand Modifier paragraph to each prompt automatically.

**Usage in automated mode (Mode 3):** When running `generate_ads.py`, templates tagged `Product images: Yes` will pass your product photos as reference images via `inlineData` so Nano Banana 2 matches your real packaging. Templates tagged `No` use text-to-image only.

---

## Copy-Forward Templates

### 1. Headline
**Funnel:** TOFU/MOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad with a [BACKGROUND] background. Top third: large bold sans-serif headline reading "[YOUR HEADLINE, under 10 words]". Below in smaller text: "[YOUR SUBHEAD, one sentence]". Bottom half: [YOUR PRODUCT] centered on a clean surface with [DETAILS like soft shadow, slight angle]. Shot at 50mm f/2.8 from slightly above. Brand logo bottom right. Clean, authoritative.

> **Copy upgrade:** Use `review-miner` emotive headlines for the headline slot. Use `copy-writing` headline formulas if no reviews available.

---

### 2. Offer/Promotion
**Funnel:** MOFU/BOFU | **Ratio:** 9:16 | **Product images:** Yes

{BRAND_MODIFIER}

Create a promotional ad with a split background. Top 60% is [PRIMARY BRAND COLOR] and bottom 40% is [CONTRAST COLOR like warm cream]. [YOUR PRODUCT] sits centered where colors meet, soft studio lighting. Upper area: large [CONTRAST TEXT] sans-serif reading "[YOUR OFFER like YOUR FIRST MONTH FREE]". Below: "[OFFER DETAILS]". Lower section: small [BRAND COLOR] text with [VALUE ADDS]. Brand logo bottom right.

> **Copy upgrade:** Run actual offer details through `copy-writing` CTA guidelines. Test multiple offer framings.

---

### 5. Bullet-Points
**Funnel:** MOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a benefit-list ad, split composition on [BACKGROUND] background. Left 40%: [YOUR PRODUCT] on [SURFACE], shot at 85mm f/2.8. Right 60%: vertical stack of five lines with filled [BRAND COLOR] circles: "[BENEFIT 1-5]". Clean sans-serif, generous spacing. Brand logo bottom right.

> **Copy upgrade:** Use `review-miner` specificity gold for concrete benefit claims. Avoid generic benefits.

---

### 21. Bold Statement / Reaction Headline
**Funnel:** TOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on a bold [GRADIENT like warm-to-hot gradient: deep coral to vivid hot pink]. Top half: very large, dominant, bold white all-caps condensed sans-serif headline centered, reading "[HEADLINE -- provocative, under 15 words]" -- text should fill approximately 40% of the frame height. Bottom half: [YOUR PRODUCT LINEUP] arranged in a staggered row, each at a slightly different angle, on the gradient surface with soft reflections. Brand logo bottom center in small white text. No stars, no reviews, no badges. The statement and the gradient carry all the energy.

> **Copy upgrade:** Use `review-miner` emotive headlines or `copy-writing` contrarian positioning formula.

---

### 23. Long-Form Manifesto / Letter Ad
**Funnel:** MOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on a clean [BACKGROUND like soft off-white / warm cream] background. Top: small [BRAND COLOR] all-caps sans-serif label reading "[LABEL like A NOTE FROM OUR FOUNDER]". Below: a long-form text block in medium-weight dark sans-serif spanning the width: "[MANIFESTO TEXT, 4-8 sentences: direct, personal, slightly raw. Address the customer. Name the problem. Explain why this exists. End with a line that lands.]" Below the text: [YOUR PRODUCT] small, bottom-right or bottom-center, soft studio lighting. Brand logo bottom left, small. Generous margins. Magazine letter feel, not crowded ad.

> **Copy upgrade:** This template benefits most from authentic founder voice. Use `review-miner` pain language for the problem-naming section.

---

### 30. Hero Statement + Icon Benefit Bar
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on a [BACKGROUND like clean white or soft gradient] background with three horizontal zones. TOP (25%): bold [TEXT COLOR] all-caps condensed sans-serif headline reading "[HEADLINE]". MIDDLE (50%): [YOUR PRODUCT] centered, large, shot at 50mm f/2.8, soft studio lighting. BOTTOM (25%): horizontal bar with [BAR COLOR] background spanning full width, containing four to five icon + label pairs. Each: simple line icon in [ICON COLOR] above a two-to-three word label: "[BENEFIT 1-5]". Brand logo centered below the icon bar, small. Balanced, authoritative, retail-ready.

> **Copy upgrade:** Benefits should be factual claims from product spec or `review-miner` specificity gold.

---

## Social Proof Templates

### 3. Testimonials
**Funnel:** MOFU | **Ratio:** 9:16 | **Product images:** Yes

{BRAND_MODIFIER}

Create a testimonial ad set in [SETTING like bright bathroom / kitchen] with warm natural light. [YOUR PRODUCT] on [SURFACE], slightly out of focus. Overlaid: large bold white sans-serif "[SHORT HEADLINE]". Below: "[FULL QUOTE 2-3 sentences]. [NAME], [CREDENTIAL]." Five filled [BRAND COLOR] stars. Brand logo bottom right in white. Shot on 35mm f/2.0.

> **Copy upgrade:** Use `review-miner` social validation quotes. Real customer language always outperforms written testimonials.

---

### 6. Social Proof Stack
**Funnel:** MOFU/BOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a social proof ad on [BACKGROUND like warm cream]. Top: "[HEADLINE like Join 1,000,000+ Members]" in bold [BRAND COLOR]. Five filled stars with "Rated [X] out of 5". Center: [YOUR PRODUCT] at 50mm f/4. Below: frosted white card with five-star rating, "[REVIEW TITLE]", "[2-3 SENTENCE REVIEW]", "[ATTRIBUTION]" in italic. Below card: "As Featured In" with five grayscale logos. Brand logo bottom right.

> **Copy upgrade:** Use `review-miner` top-scored quote for the review card. Verify star rating and member count are accurate.

---

### 11. Pull-Quote Review Card
**Funnel:** MOFU | **Ratio:** 1:1 or 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a review-driven ad with a solid [BRAND COLOR with hex] color block background. Top half: large bold italic serif text in white with curly quotation marks reading "[PULL-QUOTE -- the most emotional 4-8 word phrase]". Below: five large filled gold star icons. Bottom left, overlapping: white rounded-corner review card with subtle shadow containing: gray avatar icon, "[NAME]" in bold with [FLAG EMOJI], blue checkmark with "Verified Buyer", review body text (4-6 lines, trails off mid-sentence), ending with "...Read more" in bold [BRAND COLOR]. Below: "Was this review helpful?" with thumbs-up and count. Bottom right: [YOUR PRODUCT] angled slightly toward viewer. No brand logo needed if packaging shows it.

> **Copy upgrade:** This is a direct `review-miner` output template. Pull the highest-scored emotive headline for the quote, use the full review for the card body.

---

### 15. Social Comment Screenshot + Product
**Funnel:** TOFU/MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on clean white background. Top: oversized bold black sans-serif headline reading "[HOOK HEADLINE]" with [EMOJI] at the end. Center: a social media comment card with light gray rounded-rectangle background containing: circular profile avatar, bold name "[REVIEWER NAME]", and a multi-sentence review in regular-weight sans-serif: "[FULL REVIEW, 3-4 sentences, conversational and emotional]". Small gray timestamp below. Bottom center: [YOUR PRODUCT] photographed at a slight angle on white. No brand logo. No stars. The rawness is the point.

> **Copy upgrade:** Use `review-miner` social validation or unexpected reaction quotes. The more raw and conversational, the better.

---

### 16. Curiosity Gap / Hook Quote Testimonial
**Funnel:** TOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on clean white background. Top center: large [ACCENT COLOR] opening quotation marks. Below: mixed-weight headline -- first line in italic serif "[SETUP LINE]", next lines in enormous heavy-weight bold all-caps sans-serif "[BAIT PHRASE -- sounds provocative, reframed by reveal]", followed by smaller sentence-case "[REVEAL that reframes the bait]". Closing quotes and "[ATTRIBUTION]". Left bottom third: [YOUR PRODUCT] at slight angle with [DETAILS]. Trust badge to the left. Right bottom: [NUMBER] filled stars and "[COUNT] 5-Star Reviews". Bottom edge: small disclaimer text.

> **Copy upgrade:** Use `review-miner` skeptic conversion arcs. The objection becomes the bait, the resolution becomes the reveal.

---

### 17. Verified Review Card
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on solid [BRAND COLOR] background. Top: large bold white serif pull-quote reading "[HEADLINE QUOTE]" in quotation marks. Below: five filled gold stars. Center-left: white rounded-rectangle review card with shadow containing: gray avatar, bold name with [FLAG EMOJI], blue checkmark and "Verified Reviewer" in [BRAND COLOR], 3-4 sentences of review body. Bottom of card: "...Read more" link and "Was this review helpful?" with thumbs-up count. Right side, overlapping card: [YOUR PRODUCT] at slight angle, soft lighting. No brand logo. The review UI is the trust mechanic.

> **Copy upgrade:** Direct `review-miner` output. Use highest-scored reorder signal or identity shift quote.

---

### 19. Highlighted / Annotated Testimonial
**Funnel:** MOFU/BOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on clean white background. Top left: circular customer headshot of [PERSON DESCRIPTION]. Beside: bold name "[NAME]" with verified checkmark. Below: long-form customer quote in large regular-weight black sans-serif: "[FULL QUOTE, 3-5 sentences]". Key phrases highlighted with [HIGHLIGHT COLOR like bright lime green] rectangular fills: "[PHRASE 1]", "[PHRASE 2]". Bottom right: [YOUR PRODUCT] at slight angle, partially cropped. Left of product: circular guarantee seal. Brand logo bottom left, small.

> **Copy upgrade:** Use `review-miner` transformation language. Highlight the specific outcome phrases.

---

## Comparison Templates

### 7. Us vs Them
**Funnel:** MOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a side-by-side divided vertically. Left: muted gray-blue background. Right: [PRIMARY BRAND COLOR]. Center top: white circle with "VS". Left header: "[COMPETITOR CATEGORY]" + generic competitor product + list with X marks: "[WEAKNESS 1-5]". Right header: "[YOUR BRAND]" + [YOUR PRODUCT] + list with checkmarks: "[STRENGTH 1-5]". Brand logo bottom right.

> **Copy upgrade:** Use `review-miner` competitor breakup language for the weakness list. Use specificity gold for the strength list.

---

### 8. Before & After (UGC Native)
**Funnel:** TOFU/MOFU | **Ratio:** 9:16 | **Product images:** Yes

{BRAND_MODIFIER} -- for product color ONLY. This should look like a real person's post.

Create TikTok before-and-after. LEFT: grainy iPhone mirror selfie, [PERSON] in dimly lit bathroom, [BEFORE STATE], harsh lighting. White handwritten text: "[BEFORE DATE]". RIGHT: same person, same bathroom, bright natural light, [AFTER STATE], [PRODUCT] visible on counter. White text: "[AFTER DATE]". Top center: "[TIMEFRAME] on [BRAND]" with emoji. Should look stitched in CapCut.

> **Copy upgrade:** Use `review-miner` transformation language for the before/after states and timeframes.

---

### 25. Us vs. Them Color Split
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad with hard vertical split. Left: [NEGATIVE COLOR like desaturated gray] background. Right: [BRAND COLOR, vibrant]. Top center: "[HEADER like CHOOSE YOUR FIGHTER]" in bold. Left: generic competitor product, dull lighting, list with X marks: "[WEAKNESS 1-3]". Right: [YOUR PRODUCT] lit warmly, list with checkmarks: "[STRENGTH 1-3]". Brand logo bottom center in white. Mood contrast between sides should be immediately obvious.

> **Copy upgrade:** Same as #7. Competitor breakup reviews are the copy source.

---

### 31. Comparison Grid / Table
**Funnel:** MOFU/BOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on clean [BACKGROUND] background. Top: bold headline "[SEE HOW WE COMPARE]". Below: comparison table with 3-4 columns. First column: row labels "[ROW 1-5 like Protein, Sugar, Ingredients, Price, Rating]". Competitor columns in gray. Your brand column highlighted with [BRAND COLOR] tint, values in bold with checkmarks. Below table: [YOUR PRODUCT] small, bottom-center. Brand logo bottom right.

> **Copy upgrade:** Use `review-miner` specificity gold for your brand's column. Verify all competitor data is accurate.

---

## Data/Authority Templates

### 4. Features/Benefits Point-Out
**Funnel:** MOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create an educational diagram-style ad on white background. Top: bold [BRAND COLOR] text "[HEADER like What Makes [PRODUCT] Different]". Below: [YOUR PRODUCT] centered, even studio lighting. Four callout boxes with connecting lines: "[BENEFIT 1-4]". Each has a small [BRAND COLOR] circle. Website bottom center. Brand logo bottom right. Scientific diagram redesigned by a luxury agency.

---

### 10. Press/Editorial
**Funnel:** TOFU/MOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a press ad on off-white linen background. Top: "As Featured In" in small [BRAND COLOR] uppercase wide-tracked text. Below: five grayscale publication logos. Center: italic serif pull-quote in [BRAND COLOR]: "[PRESS QUOTE]" with attribution. Lower third: [PRODUCT] at 85mm f/2.8, soft side light. Brand logo bottom left. Generous white space. Full-page Vogue energy.

---

### 13. Stat Surround / Callout Radial (Product Hero)
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on white-to-[LIGHT GRADIENT] gradient background. Top: bold headline "[HEADLINE]". Center: [YOUR PRODUCT] on white, soft studio lighting. Near product: circular price badge "[PRICE POINT]". Flanking both sides: four stat callouts with curved hand-drawn arrows pointing at product. Left: "[STAT 1] / [LABEL]", "[STAT 2] / [LABEL]". Right: "[STAT 3] / [LABEL]", "[STAT 4] / [LABEL]" with five gold stars. Bottom: [FLAVOR PROPS] for appetite appeal. No brand logo.

> **Copy upgrade:** Use `review-miner` specificity gold for stats. Verify all numbers.

---

### 18. Stat Surround / Callout Radial (Lifestyle Flatlay)
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on white background with lifestyle flatlay. Top: bold [ACCENT COLOR] filled banner bar, white all-caps sans-serif "[HEADLINE]". Center: [PERSON DETAIL] holding [YOUR PRODUCT]. Scattered edges: [FLATLAY PROPS] slightly out of focus. Four stat callouts with curved [ACCENT COLOR] arrows: "[STAT 1-4] / [LABEL 1-4]" with gold stars. Bright, flat studio lighting. Energetic, scannable.

---

### 20. Advertorial / Editorial Content Card
**Funnel:** TOFU | **Ratio:** 4:5 | **Product images:** No

{BRAND_MODIFIER} -- for tone ONLY. Do NOT use polished ad layouts.

Create a full-bleed moody portrait of [PERSON DESCRIPTION], warm amber-toned lighting, 50mm f/1.8, shallow DoF. Lower 45%: white rounded-rectangle pill label "[CATEGORY TAG like HOT TOPIC]". Below: very large bold all-caps condensed headline in white with [HIGHLIGHT COLOR] keywords: "[HEADLINE]". Oversized -- at least 35% of frame height. Bottom: "[@HANDLE]" in small white. No product shot, no CTA, no stars. Should read like a blog post.

---

### 26. Stat Callout (Data-Driven Lifestyle)
**Funnel:** TOFU/MOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad with full-bleed lifestyle photo of [LIFESTYLE SCENE]. Overlaid: one very large bold stat "[STAT like 93%]" in oversized condensed sans-serif (largest element in frame). Below stat: "[STAT CONTEXT like of customers report more energy within 7 days]". Product either visible in scene or as small shot in bottom corner. Brand logo bottom corner, small, white.

> **Copy upgrade:** Verify stat accuracy. Use `review-miner` specificity gold for real numbers.

---

### 28. Feature Arrow Callout / Product Annotation
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on clean [BACKGROUND] background. Center: [YOUR PRODUCT] large, 50-60% of frame, straight-on or slight angle, even studio lighting. Around product: 4-5 thin [LINE COLOR] straight lines from specific product points to text labels in margins. Each label: bold text with small circle at product end. Labels: "[FEATURE 1-5]". Top or bottom: small headline "[What's Inside]" in [BRAND COLOR]. Brand logo bottom corner. Diagram-meets-luxury aesthetic.

---

## Product Showcase Templates

### 12. Lifestyle Action + Product Colorway Array
**Funnel:** TOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad with [LIFESTYLE PHOTO DESCRIPTION] occupying left two-thirds, shot outdoors in [SETTING], bright natural daylight. Brand logo top center. Below logo: large bold sans-serif "[ENDORSEMENT HEADLINE]" in [TEXT COLOR]. Bottom right: three [PRODUCT VARIANTS] fanned in overlapping arrangement showing [COLOR 1], [COLOR 2], [COLOR 3]. Products crisp and studio-lit against lifestyle background. 50mm f/2.0, lifestyle slightly softer than foreground product.

---

### 14. Bundle Showcase + Benefit Bar
**Funnel:** MOFU/BOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on [BACKGROUND like gradient] background. Top: oversized bold white all-caps sans-serif "[HEADLINE]". Below headline: horizontal [ACCENT COLOR] banner bar divided into [NUMBER] segments with benefit labels: "[BENEFIT 1-5]". Center-to-bottom: open [PACKAGING] at slight overhead angle showing [PRODUCTS] nestled inside. Lower foreground: [LIFESTYLE PROP]. Brand logo bottom left. Bright studio lighting, saturated, energetic.

---

### 22. Flavor Story / "Tastes Like"
**Funnel:** TOFU/MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on [BACKGROUND like creamy off-white to warm golden gradient]. Center: [YOUR PRODUCT] angled dynamically, [LIGHTING like warm side light]. Surrounding: [INGREDIENT PROPS like fresh banana slices, chocolate chips, walnut halves] scattered naturally as if mid-fall. Top or bottom: bold [TEXT COLOR] headline "[HEADLINE like TASTES LIKE GRANDMA'S BANANA BREAD. FUELS LIKE A PRE-WORKOUT.]" Below in lighter weight: "[SUBHEAD like 20g protein. No artificial sweetness. Just real food.]" Appetite-forward, warm, indulgent-but-healthy mood.

> **Copy upgrade:** Use `review-miner` for taste/flavor descriptions. Customers describe flavors better than copywriters.

---

### 27. Benefit Checklist Showcase
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad with vertical split. Left 45%: [YOUR PRODUCT] on [SURFACE], 50mm f/2.8, soft studio lighting. Right 55%: [BACKGROUND] background. Top right: bold [BRAND COLOR] header "[WHY [PRODUCT]?]". Below: checklist of 5-6 benefits, each with [BRAND COLOR] checkmark: "[BENEFIT 1-6]". Below checklist: small [CTA] in rounded [BRAND COLOR] pill button. Brand logo bottom right. Clean, trustworthy, scannable.

---

### 35. Hero Product Showcase + Stat Bar
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on [BACKGROUND like rich brand gradient or solid color]. Top: bold [TEXT COLOR] all-caps headline "[HEADLINE]". Center: [YOUR PRODUCT] LARGE, 40-50% of frame, studio lighting, clear hero. Bottom: horizontal stat bar spanning full width, divided into 3-4 sections: "[STAT 1] / [LABEL 1]", "[STAT 2] / [LABEL 2]", "[STAT 3] / [LABEL 3]", "[STAT 4] / [LABEL 4]". Brand logo bottom center, small. Premium, confident, retail-ready.

---

### 37. Hero Statement + Icon Bar + Offer Burst (Promo)
**Funnel:** BOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on [BACKGROUND like brand gradient]. TOP: bold all-caps condensed headline "[HEADLINE]". MIDDLE: [YOUR PRODUCT] centered and large. Near product: circular burst badge in [BURST COLOR] with "[OFFER like 25% OFF / FIRST ORDER / CODE: [CODE]]". BOTTOM: horizontal icon bar with 4 benefit icon + label pairs. Below bar: small terms text. Brand logo centered, small. Urgent but premium -- offer burst should feel upscale.

---

## Native/Organic Templates

### 9. Negative Marketing (Bait & Switch)
**Funnel:** TOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create: background is close-up of [PRODUCT], slightly blurred. Center: white rounded-rectangle review card (Amazon-style). Gray user icon, "[NAME]", one gold star + four gray, orange "Verified Purchase" badge, bold text: "[BAIT that sounds negative but is positive]". Bottom: bold white sans-serif "[PUNCHLINE like THE REVIEWS ARE IN.]". Brand logo bottom right.

> **Copy upgrade:** Use `review-miner` objection arcs. The objection is the bait, the resolution is hidden. Best pattern: skeptic conversion reviews.

---

### 33. Faux Press / News Article Screenshot
**Funnel:** TOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER} -- match brand tone only.

Create: a static ad designed to look like a news article screenshot on white background. Top: thin gray divider. Small gray byline "[PUBLICATION]" and "[DATE]". Large bold black serif headline: "[HEADLINE like New Study Reveals Why Thousands Are Switching to [BRAND]]". Below: product photo spanning article width with gray credit. Below: 2-3 paragraphs of article-style serif body text referencing [KEY CLAIMS]. No brand logo outside product. No CTA. Indistinguishable from real article screenshot.

---

### 34. Faux iPhone Notes / App Screenshot
**Funnel:** TOFU | **Ratio:** 9:16 | **Product images:** No

Do NOT use brand colors. This should look exactly like a real iPhone Notes screenshot.

Create: white background. Top: standard iOS Notes UI -- gray timestamp, horizontal divider. Below: default iOS font (San Francisco), casual typed notes: "[TITLE in slightly larger bold]" followed by bullet list: "[ITEM 1-4 -- casual product recommendation language]". Below: additional casual note like "[update: just found out they have a [NEW VARIANT]. ordering immediately.]" No brand logo. No product image. No colors. Just text on white. Screenshottable.

---

### 36. Whiteboard Before / After + Product Hold
**Funnel:** TOFU/MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER} -- for product color ONLY.

Create: whiteboard photo. White/off-white surface with texture and faint marker smudges. LEFT: [MARKER COLOR] handwriting: "BEFORE" underlined, bulleted list: "[BEFORE 1-4]". RIGHT: [DIFFERENT MARKER COLOR]: "AFTER" underlined, list: "[AFTER 1-4]". CENTER: hand holding [YOUR PRODUCT] overlapping the whiteboard. Hand-drawn arrow or circle around "AFTER" in different color. No brand logo outside product.

> **Copy upgrade:** Use `review-miner` transformation language for before/after lists.

---

### 40. Native / Ugly Post-It Note Style
**Funnel:** TOFU | **Ratio:** 1:1 | **Product images:** Yes

Do NOT use polished design, brand colors, or clean typography. Intentionally messy.

Create: photo of [YOUR PRODUCT] on [SURFACE like wooden table], slightly above angle, natural lighting. Overlaid: 2-3 [POST-IT COLORS] post-it notes at different angles with handwritten-style text: "[NOTE 1-3 -- casual reactions, use exclamation marks and question marks]". Thick hand-drawn [ARROW COLOR] arrow pointing at product. Maybe a hand-drawn circle or underline. Quick-photo-plus-notes aesthetic. No brand logo. The ugliness is the scroll-stopper.

> **Copy upgrade:** Use `review-miner` emotive headlines as the post-it text. Short, punchy, authentic.

---

## Hybrid Templates

### 24. Product + Comment Callout (Faux Social)
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on [BACKGROUND] background. Center: [YOUR PRODUCT] large and prominent, slight angle, soft shadow. Floating around: 3-4 rounded-rectangle white "comment bubbles" with shadows, each containing: small avatar, bold "@username", and 1-2 sentences of conversational review. Bubbles overlap product at different angles -- mood board feel. No stars, no logo, no headline. The social proof IS the ad.

> **Copy upgrade:** Use `review-miner` social validation quotes for comment bubbles.

---

### 29. UGC + Viral Post Overlay
**Funnel:** TOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER} -- for product color ONLY.

Create: full-bleed lifestyle photo of [PERSON holding YOUR PRODUCT, smiling], warm natural lighting, phone camera quality. Overlaid on lower two-thirds: white rounded-rectangle "social post" card with: avatar, "[USERNAME]", verified checkmark, post text in regular sans-serif: "[POST TEXT -- 3-4 sentences, casual, 'not sponsored just obsessed' energy]". Below: heart/comment/share icons with counts. Post card tilted very slightly. No brand logo outside the post.

---

### 32. UGC Story Callout / Text Bubble Explainer
**Funnel:** TOFU | **Ratio:** 9:16 | **Product images:** Yes

{BRAND_MODIFIER} -- for product color ONLY.

Create: vertical image of [PERSON holding YOUR PRODUCT up to camera, genuine smile], phone camera quality. Around person/product: 3-4 [BUBBLE COLOR like soft pastel] rounded text bubbles with pointer tails directed at product. Each bubble: short casual text in handwritten or clean sans-serif: "[BUBBLE 1-4 -- casual benefit statements]". Bubbles overlap naturally at different sizes. No logo, no stars, no headline.

> **Copy upgrade:** Use `review-miner` emotive headlines shortened to 3-5 word bubble format.

---

### 38. UGC Lifestyle + Product + Review Card (Split)
**Funnel:** MOFU | **Ratio:** 1:1 | **Product images:** Yes

{BRAND_MODIFIER}

Create a three-panel horizontal layout on [BACKGROUND]. LEFT (35%): lifestyle/UGC photo of [PERSON using product, candid], phone quality, warm-toned. CENTER (30%): [YOUR PRODUCT] on clean surface, studio lighting, crisp. Small [BRAND COLOR] label below. RIGHT (35%): white card with gold stars, bold "[REVIEW HEADLINE]", "[REVIEW BODY, 2-3 sentences]", "[ATTRIBUTION -- Verified Buyer]". Thin [BRAND COLOR] dividers between panels. Brand logo bottom center, small.

> **Copy upgrade:** Use `review-miner` top-scored quote for the review card panel.

---

### 39. Curiosity Gap + Scroll-Stopper Hook
**Funnel:** TOFU | **Ratio:** 4:5 | **Product images:** Yes

{BRAND_MODIFIER}

Create a static ad on [BACKGROUND like dark/moody brand color or dramatic gradient]. Center: very large bold white all-caps condensed headline "[HOOK -- maximum intrigue, under 15 words]" -- dominate the frame, 40-50% of image height. Below in smaller contrasting text: "[SUBHOOK -- one sentence that deepens the curiosity]". Bottom: [YOUR PRODUCT] small, slightly blurred or in shadow -- visible but creates tension. No stars, no reviews, no benefits, no price. Maximally simple.

> **Copy upgrade:** Use `review-miner` unexpected reaction pattern as the hook source. Or `ads-creative` hook library.
