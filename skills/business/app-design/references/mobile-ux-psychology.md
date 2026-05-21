# Mobile UX Psychology & Conversion

Research-backed guidelines for how users actually behave on phones and how to design for it.
Companion to `ui-principles.md` (visual principles) and `design-tokens.md` (code specs).

---

## 1. Thumb Zone / Reachability

### The Three Zones (One-Handed Use)

- **Green (easy):** Bottom third, center-to-dominant-side. Thumb rests here. Primary actions live here.
- **Yellow (stretch):** Middle rows, screen sides. Minor effort. Secondary actions, nav tabs.
- **Red (hard):** Top of screen, far corners. Grip shift needed. Destructive actions, rare settings.

### Screen Size Impact

Every 0.5 inches of additional screen = ~23% less one-handed usability. On 6.5"+ devices (most 2025 flagships), the easy zone is only ~22% of screen area.

### Placement Rules

- Primary CTA: bottom of screen, within thumb reach
- FAB: bottom-right (right-handed default), bottom-center for mixed audience
- Back/close: never top-left alone. Support edge swipe (iOS) and system back (Android)
- Destructive actions: top or buried. Where accidental taps can't reach
- Bottom nav: always beats hamburger for one-handed use

### Back Navigation

Going back must be effortless. Apps that make it frustrating to go back get abandoned.

- **One tap back:** iOS back button (top-left) + left-edge swipe. Android system back gesture/button. (See `design-patterns.md` section 10.)
- **One step, not home:** Back goes to the previous screen, not all the way to the home screen. Ever.
- **Preserve state:** When users go back and return, preserve form data, scroll position, and selections. Don't make them start over.
- **Visible and findable:** Don't remove or hide the back button. Follow platform conventions for placement.
- **Error recovery:** Let users go back to correct mistakes easily. Don't trap them in a flow with no escape.

---

## 2. Attention & Scan Patterns

### F-Pattern
Appears on text-heavy screens without formatting. Users read first line fully, scan partway across second, then read left edge only downward. Right side of mobile screens is nearly invisible unless strong visual contrast pulls the eye.

### Z-Pattern
Sparse screens: landing pages, simple forms, hero screens. Eye moves top-left -> top-right -> diagonal down -> bottom-left -> bottom-right. Sequence: hook (top-left), support (top-right), CTA (bottom).

### Layer Cake Pattern (Mobile-Specific)
Well-structured screens with clear headers: users scan headers only, diving into sections matching their intent. **This is the pattern you're designing for most of the time.** Make headers earn attention.

### Scroll Depth
- Users see only 50-60% of content before dropping off
- Put the single most important action above the fold
- Don't bury the CTA below unrelated content

---

## 3. CTA & Conversion

### Stats That Matter
- Larger CTA buttons: +90% CTR
- Single CTA per screen: 1,617% better conversion vs. multiple CTAs
- Mobile-optimized CTAs: +32.5% conversion over non-optimized
- Urgency words ("today," "limited," "now"): +14% conversions
- Inline CTAs: 121% higher CTR than sidebar/overlay CTAs
- Floating "Add to Cart": +33% cart additions vs. static bottom buttons

### What Kills Conversions
- Too many competing elements around the CTA
- CTA buried below unrelated content
- Form fields without clear labels or inline validation
- Load time >3 seconds (53% abandon)
- Forcing account creation before showing value

---

## 4. Cognitive Load Reduction

### Techniques

**Chunking (Miller's Law):** Humans hold ~7 items (plus/minus 2) in working memory. Break lists >7 into categories. Break forms into logical sections.

**Progressive disclosure:** Show only what's needed for the current decision. Advanced options reveal on demand. One question per screen on mobile forms.

**Whitespace:** Crowded screens increase cognitive load measurably. Spacing signals grouping. Whitespace is functional, not wasted.

**Smart defaults:** Reduce decision points. Pre-select options. Provide recommendations. Don't make users choose what they don't need to choose.

**Consistent patterns:** Familiarity offloads cognition. Same button = same behavior everywhere. Users stop thinking about UI mechanics and start thinking about tasks.

**Clear hierarchy:** When users don't have to figure out where to look, cognitive load drops immediately.

### Input Minimization

Typing on mobile is uncomfortable and error-prone. Every keystroke is friction.

- **Minimize required fields:** Ask only what's essential for *this step*. Collect the rest later.
- **Auto-complete & auto-fill:** Use HTML `autocomplete` attributes (`name`, `email`, `tel`, `address-line1`) so browsers and password managers fill fields automatically.
- **Match keyboard to input:** Numeric pad for PINs, email keyboard with `@` and `.com` for email, search button for search fields. (Full keyboard type specs in `design-tokens.md` section 5.)
- **Smart defaults:** Pre-fill from device settings (locale, currency, timezone). Pre-select the most common option.
- **Voice input:** Add microphone icon on search bars and long-text inputs. Increasingly expected, especially for accessibility.
- **Selection over typing:** Dropdowns, date pickers, toggles, and chips reduce typing to tapping.

---

## 5. Onboarding Patterns

### Core Principle
Show value before asking anything. Time-to-value under 60 seconds is the 2025 benchmark.

### Patterns That Work

**Value-first / demo-before-signup:** Show core functionality with sample data before requiring account creation. Delay permission requests until users reach the feature that needs them.

**Progressive (contextual):** Don't front-load feature intros. Introduce at the moment users need them. "Just-in-time" learning.

**Interactive walkthroughs:** Guide through real tasks, not slideshows. Include skip option always.

**Personalization (limited):** 3-5 strategic questions about goals. Immediate payoff from each answer. Example: Duolingo asks your goal, then tailors first lesson.

**Progress indicators:** "Step 2 of 4" reduces anxiety. Include time estimates.

### Coach Marks & Tooltips
- Work when pointing at a single, specific, non-obvious element
- Fail when overused, used for obvious things, or triggered at launch
- Best: action-triggered tooltips after relevant user actions
- Pulsing hotspots grab attention without blocking UI. Use sparingly.

### What to Avoid
- Lengthy slide tutorials before any interaction
- Permissions at launch before user has reason to care
- All-at-once feature tours
- Missing skip/back options

---

## 6. Push Notification Strategy

Push notifications are a double-edged sword. Strategic use drives engagement. Overuse drives uninstalls.

### When to Send

- **Value-based triggers:** Transaction confirmations, time-sensitive updates, direct messages, goal progress. The notification must deliver value the user can't get by opening the app later.
- **Contextual timing:** Respect time zones. Learn from user activity patterns. A fitness app pings at workout time, not 3 AM.
- **Action-triggered:** "Your order shipped" beats "We miss you!" Every time.

### What Kills Retention

- More than 3-5 notifications per week for non-messaging apps
- Generic re-engagement ("Come back!") with no specific value
- Notifications for features the user never used
- Sending at bad times (late night, during meetings)
- No way to customise frequency or categories

### Permission Request Timing

Never ask at first launch. Ask when the user reaches a feature that benefits from notifications. Example: after a user creates their first order, ask "Want updates when your order ships?"

### Design Guidelines

- **Rich notifications:** Include images, action buttons, progress bars where the platform supports it
- **Deep linking:** Every notification opens the relevant screen, never the home screen
- **Preference controls:** Let users pick categories (orders, promos, social) and frequency
- **Graceful degradation:** App works fully without notification permission

---

## 7. Personalisation

Users expect apps to adapt to their behaviour, preferences, and context. Personalisation is table-stakes for modern mobile apps.

### Content Personalisation

- **Behaviour-based recommendations:** Spotify's Discover Weekly, Netflix's "Because you watched." Surface content based on usage patterns, not just demographics.
- **Recency and frequency signals:** Weight recent behaviour over old. A user who stopped watching horror films 6 months ago shouldn't still see horror recommendations.
- **Collaborative filtering:** "Users like you also liked..." Works when individual history is thin.

### UI Personalisation

- **Remembered preferences:** Dark mode, sort order, default views, last-used filters. Don't make users re-set preferences every session.
- **Adaptive layouts:** Surface frequently-used features. Citymapper shows your regular commute routes first.
- **Greeting by name:** Small touch, big impact. "Good morning, Alex" feels human.
- **Smart defaults:** Pre-fill location, currency, language from device settings. Pre-select the most common option for that user.

### When Personalisation Backfires

- **Filter bubbles:** Over-personalised feeds narrow discovery. Always include a "explore something different" escape hatch.
- **Uncanny valley:** Showing data the user didn't knowingly share ("We noticed you visited Store X") erodes trust.
- **Privacy transparency:** Show what data drives recommendations. Offer easy opt-out. GDPR/CCPA compliance isn't optional.
- **Cold start problem:** New users have no history. Use onboarding questions (3-5 max) or popular/trending content as seed data.

---

## 8. Authentication UX

### Friction-to-Security Tradeoff

From lowest to highest friction:

| Method | Friction | Best For |
|--------|----------|----------|
| Biometric (Face ID / fingerprint) | Lowest | Returning users, frequent-use apps |
| PIN / passcode | Low | Fallback for biometric failure |
| Magic link (email) | Medium | Infrequent-use apps, no password to remember |
| Social login (Google / Apple) | Medium | Reduces form fields to one tap, offer 2-3 max |
| Email + password | Highest | Initial account creation only |

### Auth Flow UX Rules

- Default to biometric for returning users (don't show login screen)
- Show login form only after biometric fails or is unavailable
- "Stay logged in" should be the default, not an opt-in checkbox
- Never require re-authentication for non-sensitive actions
- Password requirements: show rules upfront, validate in real-time, show strength meter
- OTP input: auto-advance between digits, auto-submit on last digit, auto-read from SMS where platform supports
- Social login buttons: use official brand assets and colors, place above email/password form

---

## 9. Empty, Error, and Loading States

### Empty States
Not a blank screen. A design opportunity.

**Include:**
1. Why it's empty (context)
2. Actionable next step (CTA)
3. Illustration/icon matching brand tone
4. Optional: starter content or templates

**Good microcopy:** "You haven't saved anything yet. Add your first [item] to get started."
**Bad microcopy:** "No data." "Empty." "Nothing here."

**Pattern:** Demo content for first-use. Trello populates a sample board. Spotify suggests seed songs.

### Error States

**Requirements:**
- Human-readable explanation
- Specific recovery path (not just "try again")
- Empathetic tone
- Icon + text (not color alone)

**Good:** "That email doesn't look right. Did you mean gmail.com instead of gmal.com?"
**Bad:** "Invalid email address" / "Error 422" / "Something went wrong"

### Loading States

**Skeleton screens** (preferred over spinners): Show structural shape of content. Reduces perceived wait.

**Progress indicators** for operations >3 seconds: Show percentage or steps.

**Optimistic UI:** Update immediately assuming success, confirm in background. Roll back on failure. Used by all major social apps.

**Animated loading messages** for 5+ second operations: Witty microcopy transforms idle time.

---

## 10. Gestalt Principles on Mobile

### Proximity
Close = related. Primary grouping tool on mobile. Form labels above inputs. Error messages adjacent to the field. Nav tabs clustered together.

### Similarity
Same look = same type. All primary buttons identical. All cards consistent treatment. Breaking the pattern causes confusion.

### Continuity
Eye follows lines and alignment. Left-aligned text creates a reading edge. Progress bars guide attention forward. Bottom nav creates a stable anchor.

### Figure/Ground
Foreground vs background separation. Dimmed backdrop behind modals. Cards with shadow = tappable. Be consistent: if shadows mean "tappable," don't use them decoratively.

### Closure
Users fill in missing shapes. Partially visible cards at screen edge hint scrollability. Standard pattern for horizontal scroll affordance.

### Uniform Connectedness
Elements sharing visual properties (color, background, border, container) are perceived as a single group -- even stronger than proximity. A shared card background groups items more powerfully than just placing them close together. Use shared containers, background colors, or borders to connect related elements. Avoid applying the same visual treatment to unrelated items.

---

## 11. Laws of UX Applied to Mobile

### Fitts's Law
Time to reach a target = f(distance, size). Larger and closer = faster and more accurate.

**Mobile:** Primary actions large (44-48px+) and close to thumb. CTAs at bottom of screen. Floating buttons reduce distance. Minimize gap between content and next-step action.

### Hick's Law
Decision time increases with number of choices.

**Mobile:** 3-5 bottom tabs beat 8-item hamburger. One question per onboarding screen. Progressive filtering over showing all variants. When tempted to add another option, ask what happens if you remove it.

### Miller's Law
Working memory: ~7 items (plus/minus 2).

**Mobile:** Nav tabs 5 or fewer. Settings grouped, never 15+ flat. Onboarding 5 or fewer screens. Menu items 5-7 per category max.

### Jakob's Law
Users expect your app to work like the apps they already know.

**Mobile:** Bottom tab nav is expected. Hamburger = menu. Magnifying glass = search. Heart = like/save. Pull-to-refresh on feeds. Back = up one level. Violating these spends users' learned knowledge against them.

### Peak-End Rule
Users judge experiences by the most intense moment (peak) and the final moment (end).

**Mobile:** End of onboarding = arrival, not chore. Celebrate completion. End of purchase = secure and confident. Error recovery moments are peaks. Handle with care. Delight moments (micro-animations, witty empty states) disproportionately shape memory.

### Priming Effect
First visual elements activate mental frameworks that shape how users interpret everything after. A calming color palette and friendly illustration on the splash screen primes users to perceive the app as trustworthy. Aggressive colors and urgent copy prime anxiety. Choose your first-screen visuals deliberately -- they set the emotional baseline.

### Aesthetic-Usability Effect (Attractive Bias)
Users perceive attractive interfaces as easier to use, even when they aren't. Beautiful design creates a halo of trust: users assume that if the UI is polished, the backend, security, and support must be too. Invest in visual polish (typography, spacing, color consistency, quality imagery) -- it buys forgiveness for minor usability friction. First impressions (app store screenshots, splash, onboarding) carry outsized weight.

---

## Quick Decision Table

| Question | Answer |
|----------|--------|
| Where does primary CTA go? | Bottom, within thumb green zone |
| Min touch target? | 44x44px (iOS) / 48x48dp (Android) |
| Max nav tabs? | 5 |
| Max items per group (Miller)? | 5-7 |
| CTAs per screen? | 1 primary |
| Infinite scroll when? | Feeds, discovery. Never search results. |
| Tooltips when? | Action-triggered, contextual. Not at launch. |
| Empty state must have? | Context + actionable next step + visual |
| Error state must have? | Human explanation + recovery path |
| Loading preference? | Skeleton screen > spinner |
| Time-to-value target? | Under 60 seconds |
| When to use optimistic UI? | Non-destructive actions with high success rate |
| Returning user auth? | Biometric first, form as fallback |
