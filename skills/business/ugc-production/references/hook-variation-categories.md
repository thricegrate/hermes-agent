# Hook Variation Categories for the Winner Variation Pipeline

The 4 hook categories used in the Winner Variation Pipeline. Each category pulls on a distinct psychological trigger. The underlying pain angle stays the same across all 25 hook variations. Only the trigger changes.

This file is specific to the Winner Variation Pipeline. For the broader UGC hook taxonomy used in concept-level variation, see `skills/video-hook/references/ugc-cold-traffic-hooks.md` (5 categories: Specificity-Driven, Result Specificity, Counterintuitive, Before-State Immersion, Peer Observation).

The mapping between the two:

| Pipeline Category (4) | video-hook Category (5) | Notes |
|---|---|---|
| Specificity hooks | Specificity-Driven Identification | Direct match |
| Result specificity hooks | Result Specificity | Direct match |
| Identity hooks | Peer Observation (partial) | Identity hooks include self-recognition triggers, broader than peer observation |
| False opening hooks | Not in the 5-category taxonomy | New category specific to this pipeline |

The Winner Variation Pipeline uses 4 categories because the goal is psychological-trigger differentiation, not surface-style differentiation. The 5-category taxonomy in `video-hook` works for concept-level variation. The 4-category taxonomy works for component-level variation where every variation must hit a clearly distinct trigger.

## Generating 25 hooks across the 4 categories

Default split: 6-7 hooks per category. Adjust based on which category historically performs in the niche. If specificity hooks consistently outperform in the audience, weight 8-9 specificity / 5-6 result specificity / 5-6 identity / 5-6 false opening.

Always produce at least 4 hooks per category. Less than 4 makes it hard to read which category is winning when the data comes back.

---

## Category 1: Specificity hooks

Concrete numbers, specific timeframes, named details. The hook stops the scroll because the specificity reads as real.

### Why this works

Generic statements get scrolled past. Specific statements get read. "I lost weight" is generic. "I lost 23 pounds in 11 weeks" is specific. The number creates the mental pull. The viewer wants to know HOW.

### Hook patterns

- "[Specific number] [outcome] in [specific timeframe]"
- "I spent [specific amount] on [specific category] before this worked"
- "On day [specific number] I noticed [specific detail]"
- "[Specific quantity] of my customers said [specific thing]"

### Example variations (same pain angle: weight management)

- "I lost 23 pounds in 11 weeks"
- "Dropped 4 inches off my waist in 6 weeks"
- "I tracked my food for 47 days before I noticed this"
- "Cut 800 calories a day without trying"

The pain angle (weight management) stays constant. The specific number and frame changes. Each hook is a different number-pull on the same audience.

### Common failure modes

- Numbers that feel made up ("I lost 17.3 pounds in 8.5 weeks" reads as fake)
- Numbers without context ("23 pounds" without timeframe)
- Numbers that are not differentiated enough ("I lost 23 pounds" then "I lost 24 pounds in another variation")

---

## Category 2: False opening hooks

The hook appears to be about a different topic, then redirects into the actual content. The viewer is pulled in by the unexpected setup, then locked into the body once the redirect lands.

### Why this works

The viewer's brain expects pattern. A hook that sets up one pattern then breaks it forces a moment of attention. The redirect creates the curiosity gap. The body gets the viewer's attention because they want to see how the unexpected setup connects to the actual topic.

### Hook patterns

- Setup: a different topic than the audience expects. Redirect: connects back to the actual topic.
- Setup: a personal story unrelated to the niche. Redirect: the story turns out to be about the niche.
- Setup: a complaint about something adjacent. Redirect: the actual fix is the topic.

### Example variations (same pain angle: weight management)

- "I went to the doctor for back pain. He told me to lose weight." (setup: back pain, redirect: weight)
- "I almost got into a fight at the gym last week. I should not have been there." (setup: gym fight, redirect: weight insecurity)
- "My daughter asked me a question that ruined my whole day. Now I am doing this." (setup: family moment, redirect: weight)
- "I broke a chair at my friend's birthday party. That is when I started this." (setup: embarrassment, redirect: weight)

Each hook starts somewhere unexpected. The redirect lands the actual topic. The viewer is past the 3-second mark before they realize where the hook is going.

### Common failure modes

- Setup too long (hook is 8 seconds before the redirect, viewer drops at 3 seconds)
- Redirect too predictable (viewer guesses where it is going from the first sentence)
- Redirect that does not actually connect (the false opening is just gimmicky, the body has nothing to do with it)

---

## Category 3: Result specificity hooks

Lead with the specific outcome the audience wants. The hook is a vivid before-and-after compressed to 3-5 seconds. The viewer wants the result, so they keep watching to find out the path.

### Why this works

Result specificity sells the destination. The viewer projects themselves into the outcome. They keep watching because they want to know HOW to get to the place the hook describes.

### Hook patterns

- "[Specific result that the audience wants, stated as already happened]"
- "[Specific transformation between two specific states]"
- "[Specific number that signals the outcome]"
- "[Specific quality of life change tied to the outcome]"

### Example variations (same pain angle: weight management)

- "My jeans fit again for the first time in 3 years"
- "I am off blood pressure medication for the first time since I turned 40"
- "I can chase my kids around the yard without losing my breath"
- "I bought clothes from the regular section yesterday"

Each one is a result the audience can picture themselves living. Different angles on the same broad outcome (weight loss + life-quality change).

### Common failure modes

- Results that feel exaggerated ("I lost 80 pounds in a month")
- Results that are not specific enough ("I feel better")
- Results that are about the journey, not the outcome ("I started exercising every morning"). That is body, not hook

---

## Category 4: Identity hooks

Open with a label or self-recognition trigger. The viewer recognizes themselves in the hook and stops scrolling because the hook is talking to them specifically.

### Why this works

When the hook names the viewer's situation precisely, the viewer's pattern recognition fires. "Oh, that is me." The hook becomes about them, not about the creator. The body then has the viewer's attention because the hook proved the content is for them.

### Hook patterns

- "If you are someone who [specific pattern]..."
- "[Specific demographic descriptor], this is for you"
- "[Specific situation the audience is in], here is what I learned"
- "Anyone who has ever [specific experience], you know what I mean"

### Example variations (same pain angle: weight management)

- "If you are someone who has tried every diet and given up by week 3, this is for you"
- "Moms over 40 who have tried to lose the baby weight for years, listen up"
- "If you have ever stood in front of a mirror at 11pm and said 'tomorrow', read this"
- "Anyone who has bought gym clothes hoping they would motivate you, you know what I mean"

Each hook names a specific identity the audience can self-identify into. The pain angle (weight management) is the same. The identity framing changes.

### Common failure modes

- Identity too broad ("If you have ever been overweight" is too generic, no self-recognition trigger)
- Identity too narrow ("If you are a 43-year-old mom in Ohio" narrows the audience too much)
- Identity that feels accusatory ("If you are lazy"). The audience does not self-identify into negative labels.

---

## How to generate the 25 hook variations in one Claude call

Use the variation-from-winner-reel template (`templates/variation-from-winner-reel.md`). It includes the prompt structure for generating the 25 hooks across the 4 categories in a single call.

Key elements of the prompt:
1. Specify the pain angle (which stays constant)
2. Specify the audience and persona
3. Request 6-7 hooks per category, hitting the distinct psychological trigger of each
4. Specify the 3-5 second clip duration constraint
5. Specify the same character + scene baseline as the original

Output should be 25 hook lines with one-sentence Seedance prompts attached, ready for video generation.

## What does NOT change across the 25 hooks

- The pain angle (the underlying problem the audience is feeling)
- The character reference (same character across all clips)
- The scene baseline (same setting, same lighting, same wardrobe family)
- The duration (3-5 seconds, same across all)
- The voice register (high energy or calm authority, locked from the original)

The only thing that changes between hooks is the psychological trigger pulling the viewer in.

## Cross-references

- Pipeline overview: [winner-variation-pipeline.md](winner-variation-pipeline.md)
- Compatibility tagging: [compatibility-matrix.md](compatibility-matrix.md)
- Seedance generation patterns: [seedance-consistency.md](seedance-consistency.md)
- Body framings: [body-variation-framings.md](body-variation-framings.md)
- Original UGC hook taxonomy (5 categories for concept-level variation): `skills/video-hook/references/ugc-cold-traffic-hooks.md`
