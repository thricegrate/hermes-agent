# Universal Design Principles

13 principles that apply across all app design decisions. Complements the 7 UI principles in `ui-principles.md` and the psychology/UX patterns in `mobile-ux-psychology.md`.

Source: Universal Design Principles (Lidwell, Holden, Butler) + mobile adaptations.

---

## Perception & Cognition

### 1. Priming

First visual elements set expectations for everything that follows. What users see first shapes how they interpret everything after.

**Mobile application:**
- Hero image or illustration on landing screen sets emotional tone for the entire app
- Onboarding screens prime users for the app's value before they see the interface
- Color and imagery on the first screen should match the app's core emotion (calm, urgent, playful)
- Positive visual cues (progress, success indicators) early in a flow prime users to continue

**Check:** Does your first screen prime users to feel the way you want them to feel about the app?

### 2. Attractive Bias (Aesthetic-Usability Effect)

Attractive designs are perceived as easier to use, more trustworthy, and more competent -- even when they aren't. Users forgive usability issues in beautiful interfaces.

**Mobile application:**
- Invest in visual polish: clean typography, balanced spacing, consistent color palette
- Rounded corners, smooth animations, and quality imagery increase perceived usability
- First impressions are disproportionately important -- app store screenshots and splash screens carry outsized weight
- A polished UI creates a halo effect: users assume the backend, security, and support are also high quality

**Check:** Would a user screenshot this screen to show someone? If it looks cheap, users will assume the product is cheap.

### 3. Depth of Processing

Information processed deeply (analyzed, connected to existing knowledge) is remembered better than information processed superficially. Offer multiple engagement depths.

**Mobile application:**
- Provide scan-level content (headline + image) AND deep-dive content (full text, details, data)
- Let users choose their depth: expandable sections, "Read more" links, detail screens
- Combine visual and textual representations of the same information (icon + label, chart + number)
- Interactive elements (tap to explore, swipe through options) encourage deeper processing than passive reading

**Check:** Can a user get value from this screen in 3 seconds (scanning)? Can they also spend 30 seconds going deeper?

---

## Visual Structure

### 4. Uniform Connectedness

Elements sharing visual properties (color, border, background, container) are perceived as a single group. Stronger grouping signal than proximity alone.

**Mobile application:**
- Use shared background color or card containers to group related items (settings section, form fieldset)
- Connected elements should share the same visual treatment: same text color, same icon style, same border
- Avoid applying the same background/border to unrelated items -- it falsely signals they belong together
- Cards with consistent padding and radius create natural content groups on mobile

**Check:** If you removed all text labels, would the visual grouping still communicate which elements belong together?

### 5. Symmetry

Visual equivalence among elements creates balance, harmony, and perceived stability. Asymmetry draws attention (useful for CTAs) but excess asymmetry feels chaotic.

**Mobile application:**
- Balance header elements: left action (back) mirrors right action (share/settings) in visual weight
- Center-align hero content and CTAs for a stable, focused feel
- Card grids work best with equal-width columns (2-col or 3-col on mobile)
- Intentional asymmetry highlights the primary action -- one bold button vs one text link

**Check:** Cover the left half of the screen. Now cover the right half. Does each half feel roughly balanced in visual weight?

### 6. Golden Ratio

Proportions approximating 1.618:1 feel naturally pleasing. Found in nature, art, and architecture. Not a rigid rule but a useful proportion guide.

**Mobile application:**
- Content-to-whitespace ratio: ~62% content, ~38% breathing room works well on mobile
- Image-to-text split on detail screens: image takes roughly 62% of above-fold space, text 38%
- Sidebar/drawer width to remaining content: roughly 62/38 split
- Not prescriptive -- use as a gut-check when proportions feel off, not as a mathematical constraint

**Check:** If the layout feels cramped, try giving the dominant element ~62% of the space. If it feels empty, the secondary content may need more room.

### 7. Layering

Organizing information into visual depth layers (foreground, midground, background) helps users understand relationships and hierarchy. Includes z-index, elevation, overlays.

**Mobile application:**
- Base content layer: the main screen content (list, feed, form)
- Overlay layer: bottom sheets, modals, dialogs -- focused actions that sit above base content
- System layer: status bar, navigation bar, keyboard -- highest elevation, always accessible
- Use elevation (shadow, backdrop dimming) to communicate depth: higher = more urgent/focused
- Don't stack more than 2 overlay layers (modal on top of bottom sheet = confusing)

**Check:** Can the user always tell which layer they're interacting with? Is there a clear way to dismiss overlays and return to the base layer?

---

## Interaction Design

### 8. Affordance

Elements must look like what they do. Buttons look tappable. Links look clickable. Sliders look draggable. If it doesn't look interactive, users won't try.

**Mobile application:**
- Buttons need visual affordance: fill color, border, elevation, or underline. Flat text that happens to be tappable is invisible interaction
- Use universally understood icons: hamburger = menu, magnifying glass = search, heart = like/save, X = close
- Swipeable elements should hint at the gesture: partially visible content at the edge signals horizontal scroll
- Toggle switches must look like toggles (not checkboxes). Date pickers must look like date pickers.
- If an element IS interactive, it must LOOK interactive. If it's NOT interactive, it must NOT look tappable.

**Check:** Show the screen to someone for 5 seconds. Can they point to every interactive element without guessing?

### 9. Mimicry

Copy surface, behavioral, and functional patterns from apps users already know. Familiarity reduces learning time to near zero.

**Three types:**
- **Surface mimicry:** Making your design look similar to familiar apps (same icon placement, same color coding conventions)
- **Behavioral mimicry:** Same gestures produce same results (pull-to-refresh, swipe-to-delete, pinch-to-zoom)
- **Functional mimicry:** Same features work the same way (search bar filters results as you type, settings use toggles)

**Mobile application:**
- Study the 5 apps your target users use most. Mirror their patterns where appropriate.
- Don't reinvent navigation, search, or settings. Users already know how these work.
- Platform mimicry matters: iOS apps should feel like iOS. Android apps should feel like Android.

**Check:** Would a user of Instagram/Spotify/your-competitor's-app feel immediately at home in your app?

### 10. Iconic Representation

Icons convey ideas faster than text and work across languages. Universally recognized icons reduce cognitive load and screen clutter.

**Mobile application:**
- Use established icons: home (house), search (magnifying glass), profile (person silhouette), settings (gear), back (left arrow/chevron)
- Icon + short label is more effective than icon alone (except for universally known icons like back/close)
- Maintain one icon style throughout the app: all outlined OR all filled, consistent stroke width, same visual weight
- Don't invent novel icons for standard actions -- users won't guess correctly

**Check:** Would a first-time user correctly guess what each icon does without reading any label?

### 11. Constraint

Limiting available actions reduces errors, confusion, and cognitive load. Fewer options = faster, more confident decisions.

**Mobile application:**
- Disable or hide options that aren't available in the current context (grayed-out buttons with 0.38 opacity)
- Character limits on inputs prevent data entry errors (phone: 10 digits, zip: 5 digits)
- Date pickers prevent impossible dates. Numeric keyboards prevent letter input in number fields.
- Multi-step flows constrain users to one decision per screen -- they can't skip ahead or act out of order
- "Are you sure?" confirmations before destructive actions (delete, cancel subscription)

**Check:** Is there anything the user can do on this screen that would be a mistake? If yes, can you prevent it through constraints rather than error messages?

### 12. Redundancy

Providing multiple paths to the same destination prevents frustration and accommodates different user mental models.

**Mobile application:**
- Key features reachable via multiple routes: bottom nav tab + search + deep link + push notification
- Donation/upgrade accessible from settings AND from contextual prompts within the app
- Search finds the same content as browsing/filtering -- two mental models, same destination
- Swipe gestures AND visible buttons for the same action (swipe to delete + delete button in edit mode)
- Don't force one path. Different users think differently.

**Check:** Can a user reach the app's 3 most important features from at least 2 different starting points?

### 13. 80/20 Rule (Pareto Principle)

80% of usage comes from 20% of features. The most-used 20% of features should be the most visible and accessible. The other 80% should be reachable but not prominent.

**Mobile application:**
- Bottom nav tabs = your top 3-5 features (the 20%). Everything else goes in secondary navigation, settings, or profile.
- Home screen surfaces the most-used actions as primary CTAs. Rare actions go behind menus.
- Settings screen: most-changed settings at top. Rarely-touched options (advanced, developer) at bottom or behind "Advanced" section.
- Analytics-driven: measure which features users actually use. Promote the winners, demote or remove the rest.

**Check:** Are your most-used features the easiest to reach (1-2 taps from anywhere)? Are rarely-used features hidden but findable?

---

## Quick Cross-Reference

| Principle | Primary Check | Where Else in Skill |
|-----------|--------------|---------------------|
| Priming | Does first screen set right expectations? | `mobile-ux-psychology.md` Laws of UX |
| Attractive Bias | Would users screenshot this? | `mobile-ux-psychology.md` Laws of UX |
| Depth of Processing | 3-sec scan AND 30-sec deep dive? | -- |
| Uniform Connectedness | Groups visible without text labels? | `mobile-ux-psychology.md` Gestalt |
| Symmetry | Left/right halves balanced? | -- |
| Golden Ratio | ~62/38 content-to-space split? | -- |
| Layering | Clear which layer is active? | `design-patterns.md` bottom sheets, modals |
| Affordance | All interactive elements look interactive? | -- |
| Mimicry | Feels familiar to target users? | `mobile-ux-psychology.md` Jakob's Law |
| Iconic Representation | Icons guessable without labels? | -- |
| Constraint | Can user make mistakes? Prevent them. | -- |
| Redundancy | Top 3 features reachable from 2+ paths? | -- |
| 80/20 Rule | Most-used features = most accessible? | `mobile-ux-psychology.md` Hick's Law |
