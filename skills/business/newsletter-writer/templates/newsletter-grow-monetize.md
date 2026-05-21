# Newsletter Template: Grow Monetize (Newsletter Industry)

## Newsletter Identity

- **Name:** Grow Monetize
- **Niche:** Newsletter industry, growth strategies, monetization
- **Tone:** Thoughtful, confident, grounded. Not salesy. No forced hype.
- **Language:** Plain, concrete, specific. Avoid jargon unless the domain requires it.
- **Word count:** 600 words max
- **Headings:** Title, subtitle, and section subtitles in **bold**

---

## Rewrite System

This newsletter uses a structural divergence rewrite system. The input is a source text about newsletter growth/monetization. The output is a completely restructured, rewritten version that preserves the core message but shares no structural resemblance to the original.

### Run this prompt with the source text appended after "TEXT:":

```json
{
  "Objective": "Help the user write or rewrite text into natural, specific, human-sounding prose. When rewriting, transform the structure and phrasing so the result does not resemble the original, while preserving any user-provided facts and the core intent.",
  "Reasoning_Order": "Output the final text only. Do not include a reasoning summary, process notes, rubric, scoring, or self-evaluation.",
  "Hard_Constraints": {
    "Forbidden_Mentions": [
      "Smart Pixel",
      "Chris",
      "podcast",
      "podcasts",
      "guests",
      "host",
      "interview",
      "episode"
    ],
    "No_Summary_Or_Self_Eval": true,
    "Output_Text_Only": true,
    "Max_Output_Words": 600
  },
  "Prompt_Steps": [
    "Scope & Intent Check: Identify the audience, goal, channel, and constraints the user supplied. If something essential is missing, ask up to 3 targeted questions; otherwise proceed.",
    "Ingest Inputs: Parse the user's text and notes. Extract: (a) must-keep facts (numbers, dates, outcomes) and (b) must-change elements (names, brands, identifying details, examples, stories).",
    "Deep Rewrite Plan: Identify the original text's backbone (order of ideas, transitions, cadence). Then choose a different backbone: reorder points, change the opening, swap the emphasis, and vary paragraph breaks.",
    "Change the Case: Shift to a different setting (industry, location, roles, timeline, stakes). Replace every original anecdote, example, and story beat with brand-new ones that support the same message.",
    "Structural Divergence Rules: Ensure the rewrite differs from the original by doing ALL of the following: (a) change the first two sentences completely, (b) change the paragraph count, (c) reorder at least two major points, (d) replace any signature phrases or repeated motifs, (e) avoid mirroring sentence lengths and transition words from the original.",
    "Replace Details Safely: Keep user-provided concrete facts. If specifics are missing, use clearly hypothetical details without implying real personal experience.",
    "Headings Rule: If the output includes a title, subtitle, or section subtitles, format them in **bold**. Use **Title** on the first line, **Subtitle** on the second line (if present), then **Section Subtitle** lines throughout as needed.",
    "Voice & Rhythm: Write in a natural, conversational style appropriate to the channel. Use varied sentence lengths and contractions. Keep paragraphs short and readable.",
    "Punctuation Guardrails: Do not use em dashes (—). Prefer commas, periods, and hyphens. Avoid gimmicky formatting.",
    "Length Check: If the draft exceeds 600 words, cut or compress until it is under 600 without adding new sections.",
    "Similarity Check: Before returning, confirm the output does not track the original's phrasing or structure. If it feels too close, rewrite again with a different opening, different order, and fresh wording.",
    "Final Pass: Verify the output contains none of the forbidden mentions and that all examples/stories are newly created. Then return only the finished text."
  ],
  "Style_Guidelines": {
    "Tone": "Thoughtful, confident, and grounded. Not salesy. No forced hype.",
    "Language": "Plain, concrete, specific. Avoid jargon unless the user's domain requires it.",
    "Cadence": "Mix short lines with longer sentences. Allow occasional fragments for emphasis."
  },
  "Output_Format": {
    "Type": "PlainTextOnly",
    "Instructions": "Return ONLY the rewritten or newly written text for the requested channel. If you include headings, format the title, subtitle, and section subtitles in **bold**. Keep the output under 600 words. Do not add labels like 'Summary' or any self-evaluation."
  },
  "Few_Shot_Examples": [
    {
      "Input": {
        "Task": "Rewrite a short origin story for a landing page with headings.",
        "Audience": "Potential customers considering a service.",
        "Constraints": "Human, specific, calm. Replace all anecdotes. Different structure than the original. Include title + subtitle + section subtitles in bold.",
        "Materials": "[PLACEHOLDER: original paragraph]"
      },
      "Output_Text": "**A Cleaner Way to Run the Day**\n**Simple systems for small teams that are tired of juggling messages**\n\n**What kept breaking**\nA neighborhood print shop was doing great work and still losing money in the cracks. Quotes lived in DMs. Deadlines lived in someone's head. Customers asked for updates, and nobody had a single place to look.\n\n**What we changed**\nWe built one intake form, a basic status board, and automatic reminders before a job goes late. No fancy dashboards. No big promises.\n\n**Why it matters**\nWhen the noise drops, the work gets easier to finish, and customers feel it immediately."
    },
    {
      "Input": {
        "Task": "Rewrite a teammate email with a bold subject line and a bold section subtitle.",
        "Audience": "A peer you work with weekly.",
        "Constraints": "Candid, calm. One ask + deadline. New details only. Different structure than the original.",
        "Materials": "[PLACEHOLDER: rough notes]"
      },
      "Output_Text": "**Quick tighten pass today?**\n\n**What I need from you**\nCan you scan the draft and flag any places where we sound confident without showing the why, especially in the rollout section? If you can leave comments by 5 pm, I'll revise tonight and send the final in the morning."
    },
    {
      "Input": {
        "Task": "Turn an excerpt into a short blog post with bold headings.",
        "Audience": "General readers.",
        "Constraints": "No strained metaphors. Replace the original story. Don't mirror the original structure.",
        "Materials": "[PLACEHOLDER: excerpt]"
      },
      "Output_Text": "**Advice That Actually Lands**\n**Make it usable on a normal Tuesday**\n\n**The quick test**\nPick one situation you really face and write the next sentence you'll send. When feedback is vague, reply with two options and a deadline. Now the idea has somewhere to live.\n\n**Why this works**\nYour writing stops floating because your thinking stops floating. Everything points at something real."
    }
  ],
  "Important_Considerations": [
    "Do not mention any forbidden terms or near-synonyms that point back to the original source.",
    "Do not provide summaries, rubrics, scores, or commentary about how the text was written.",
    "Do not claim real personal experiences unless the user explicitly provided them; use hypothetical or third-person vignettes if needed.",
    "When rewriting, keep the core message but rebuild the examples and stories from scratch in a new setting.",
    "Actively enforce structural divergence so the rewrite does not resemble the original.",
    "Enforce Max_Output_Words: 600.",
    "Format title, subtitle, and structural section subtitles in **bold** when they appear."
  ]
}
TEXT:
```

---

## Quality Checklist

- [ ] 600 words or fewer
- [ ] Title, subtitle, section subtitles in **bold**
- [ ] No forbidden mentions (Smart Pixel, Chris, podcast, guests, host, interview, episode)
- [ ] No em-dashes
- [ ] Structural divergence from source (different opening, paragraph count, point order)
- [ ] All examples/stories are newly created, not from source
- [ ] No summaries or self-evaluation in output
- [ ] Run through `humanizer` before publishing
- [ ] Run through `content-review` before publishing
