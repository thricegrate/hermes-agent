# Script Format Selector

10 script formats. Picking the right one matters more than the script quality.

This file is the decision tree. The format theory (what makes each format work, fail modes, voice patterns) lives in `skills/video-scriptwriter/references/`. The templates with ready-to-paste prompts live in `ads-creative/templates/`.

## The anti-ad principle

Every format below mimics organic feed content. The viewer should not realize they are watching an ad until the CTA. The moment a script reads like advertising, retention craters and the algorithm punishes the placement.

Polished is not the goal. Native is the goal.

## The decision tree

Start with the awareness level. That narrows the format set. Then pick by persona and emotional trigger.

```
Unaware audience
  -> Organic POV (lifestyle, situational hook)
  -> Silent / Text-Only (high-volume top-funnel testing)

Problem Aware audience
  -> B-Roll + Voiceover (visual product, scrollable feed)
  -> Listicle / Authority (educational, expert positioning)
  -> Organic POV (when the problem is socially relatable)

Solution Aware audience
  -> Hook-Hold-Payoff (direct response, qualified audiences)
  -> Before & After (transformation, failed-solution narrative)
  -> Podcast Two-Actor (skeptical audiences, complex mechanism)

Product Aware audience
  -> Hook-Hold-Payoff (with risk reversal in payoff)
  -> Founder Story (mission, repeat-buyer audience)
  -> UGC Creator (single-person testimonial with proof)

Most Aware audience
  -> Founder Story (closing the loyalty loop)
  -> UGC Creator (high-volume social proof)
  -> Static (offer-led, urgency, scarcity)
```

## The 10 formats

### 1. Hook Writer (5 variations per angle)

The first-pass tool. Not a script format. Used to generate 5 hook variations for one angle, each tagged with awareness level, hook type, and best-fit format. Run this before picking a format when the angle is set but the entry point is not.

- Template: `templates/hook-writer.md`
- Theory: `skills/video-scriptwriter/references/hook-engineering.md`, `skills/video-hook/references/desire-hook-templates.md`

### 2. UGC Creator Brief

Not a script. A brief for a creator to execute one of the 8 actual script formats. Use when the creator has freedom in the body but the hook is non-negotiable.

- Template: `templates/ugc-creator-brief.md`
- Theory: `skills/ugc-production/references/cross-platform-brief-structure.md`

### 3. Hook-Hold-Payoff

The 4-beat direct response script: Hook (qualify viewer in 3 seconds), Hold (twist the knife on the pain, name failed solutions), Shift (introduce the mechanism), Payoff (specific outcome + low-friction CTA). Best for solution-aware audiences who need to be convinced the mechanism is different.

- Template: `templates/hook-hold-payoff-script.md`
- Theory: `skills/video-scriptwriter/references/ugc-6-section-architecture.md`, `skills/video-scriptwriter/references/hook-engineering.md`
- Failure mode: the hook qualifies the viewer but the hold does not twist the knife deep enough. The viewer scrolls before the shift.

### 4. B-Roll + Voiceover

Visuals do 80% of the work. The voiceover narrates what the viewer is already seeing. Every 3 seconds the visual changes. Pattern interrupts (extreme close-ups, satisfying applications, bizarre textures) force the pause. Best for visual products and scrollable feeds.

- Template: `templates/b-roll-director.md`
- Theory: `skills/video-scriptwriter/references/long-form-formats.md`
- Failure mode: the script is written for a talking head and pasted into a B-roll brief. The visuals do not earn the voiceover.

### 5. Before & After Narrative

The emotional transformation arc. Specific failed solutions named (the harsh chemicals, the failed medications, the wasted money). The catalyst named. The mechanism explained. The after state shown with proof. Best for transformation products where the before is socially recognizable.

- Template: `templates/before-after-narrative.md`
- Theory: `skills/video-scriptwriter/references/frameworks.md` (Story Bridge framework)
- Failure mode: the before state is generic. "I was tired all the time" is not a before state. "I was so tired I cancelled my sister's birthday dinner for the third time" is.

### 6. Founder Story

Mission, gratitude, behind-the-scenes. The founder filming from the warehouse or walking the dog. Authority comes from the problem they personally solved. Best for product-aware and most-aware audiences.

- Template: `templates/founder-story-script.md`
- Theory: `skills/video-scriptwriter/references/frameworks.md` (Story Bridge, Sheridan), `skills/storyteller/references/sheridan-framework.md`
- Failure mode: the founder reads like a CMO. Studio backdrop. Polished delivery. Kills the format.

### 7. Listicle / Authority

"3 mistakes most [audience] make." Authority-led, value-front-loaded, the product appears as the logical solution to mistake #3. Pacing is rapid. Best for problem-aware audiences who need education.

- Template: `templates/listicle-authority-script.md`
- Theory: `skills/video-scriptwriter/references/authority-led-formats.md`
- Failure mode: the mistakes are framed as benefits ("Save more time" is not a mistake). The format needs warnings, not promises.

### 8. Podcast Two-Actor

Host + Guest. Host is the skeptic asking the questions the audience is thinking. Guest is the expert dropping value. Interruptions, filler words, casual phrasing. Looks like a viral podcast clip. Best for solution-aware audiences with skepticism.

- Template: `templates/podcast-two-actor-script.md`
- Theory: `skills/video-scriptwriter/references/two-actor-formats.md`
- Failure mode: the host agrees with everything. Without pushback, the format reads as scripted endorsement. The host must actively push back.

### 9. Organic POV

"POV: [specific situation]" text overlay. The hook is situational, not promotional. The product enters as a creator recommendation. Best for unaware to problem-aware audiences and top-of-funnel discovery.

- Template: `templates/organic-pov-script.md`
- Theory: `skills/video-scriptwriter/references/long-form-formats.md`, `skills/video-hook/references/creator-organic-hooks.md`
- Failure mode: the POV is too narrow ("POV: you take this exact supplement"). The POV needs to be relatable to a large audience, then bridged to the product.

### 10. Silent / Text-Only

No voiceover. Continuous ASMR-style background visual. Text overlays at 2-3 seconds per card. Hook -> problem -> mechanism -> guarantee/CTA. Best for high-volume testing and captions-off feeds. Also the cheapest format to produce.

- Template: `templates/silent-text-only-script.md`
- Theory: `skills/video-scriptwriter/references/silent-text-only-format.md`
- Failure mode: too much text per card. The viewer cannot read it in 2 seconds. Always cap at one bold claim per card.

## Pairing formats with the angle bank

For each angle in your bank (see `awareness-and-angle-system.md`), you should produce at least 2 different format executions. Same angle, different format, different awareness level entry. The library compounds because the algorithm reads format variation as fresh creative even when the underlying angle is proven.

Example: angle = "you cannot fix hormonal acne with cleansers."

- Format 1: Listicle / Authority (problem-aware, dermatologist-style)
- Format 2: Before & After (solution-aware, customer transformation)
- Format 3: Podcast Two-Actor (solution-aware, skeptical host)
- Format 4: Silent / Text-Only (problem-aware, high-volume test)

One angle becomes 4 ads. Each ad lives at a slightly different funnel position. The account compounds.

## The naming convention

Every script produced from these templates uses the standard creative tracker name:

`[Persona]_[Angle]_[Concept]_[Format]_[AwarenessLevel]_[HookType]`

Example: `Insomnia_FirstTimeSinceKid_TalkingHead_HookHoldPayoff_SolutionAware_PreviousFailed`

The Format field is one of: HookHoldPayoff, BRoll, BeforeAfter, FounderStory, Listicle, Podcast, POV, Silent, UGC, Static.

## Voice gate

Every script produced by these templates must be routed through `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md` before production. The templates voice-pass the seed prompts. The outputs need a second pass.

## Cross-references

- `meta-ads-master-workflow.md`: Phase 3 fits inside the 5-phase workflow
- `awareness-and-angle-system.md`: how to pick which awareness level a script targets
- `skills/video-scriptwriter/SKILL.md`: format theory home
- `skills/video-hook/SKILL.md`: hook theory home
- `skills/ugc-production/SKILL.md`: production orchestration for the briefs
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate
