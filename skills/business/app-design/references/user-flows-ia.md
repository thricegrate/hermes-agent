# User Flows & Information Architecture

Templates for mapping app structure before visual design. All copy-paste formats -- fill in for your app.

---

## 1. Screen Inventory

List every screen the app needs. Categorize by navigation depth.

### Template

```
PRIMARY (in bottom nav / always accessible):
  1. Home
  2. Search
  3. Cart
  4. Profile

SECONDARY (reached by tapping into a primary screen):
  5. Product Detail (from Home, Search)
  6. Order History (from Profile)
  7. Settings (from Profile)
  8. Checkout (from Cart)

MODALS / SHEETS (overlay, not a full screen):
  9. Filter Sheet (from Search)
  10. Add to Cart Confirmation (from Product Detail)
  11. Delete Account Confirmation (from Settings)

AUTH (gated, shown conditionally):
  12. Login
  13. Sign Up
  14. Forgot Password
  15. OTP Verification
```

### Rules
- Primary screens: 3-5 max (bottom nav limit)
- Every screen must be reachable from at least one other screen
- If a screen has no path leading to it, it's dead weight -- cut it

---

## 2. Navigation Architecture Patterns

### Flat (Bottom Tabs)
All primary screens at the same level. User switches between tabs freely.

```
[Home] [Search] [Create] [Inbox] [Profile]
   |       |        |        |        |
   v       v        v        v        v
 Feed   Results   Editor   Messages  Settings
```

**Use when:** 3-5 equally important top-level destinations. Most common pattern (Instagram, Spotify, Uber).

### Hierarchical (Hub-and-Spoke)
One hub screen. Everything branches off it and returns to it.

```
              [Home]
            /   |   \
           v    v    v
        [A]   [B]   [C]
        |      |      |
        v      v      v
       [A1]  [B1]   [C1]
```

**Use when:** One clear entry point with drill-down paths. Works for settings, documentation, file managers.

### Hybrid (Tabs + Stack)
Bottom tabs for top-level. Stack navigation (push/pop) within each tab.

```
[Home]          [Search]        [Profile]
  |                |                |
  v                v                v
Feed             Results          Settings
  |                |                |
  v                v                v
Post Detail      Item Detail      Edit Profile
  |
  v
Comments
```

**Use when:** Most production apps. Tabs for global nav, stack for drill-down within each section.

### Decision Tree

```
How many top-level destinations?
  ├── 1-2 → Hierarchical (hub-and-spoke)
  ├── 3-5 → Flat (bottom tabs) or Hybrid (tabs + stack)
  └── 6+  → Reorganize. Group features under fewer tabs. Use "More" tab as last resort.

Are destinations equally important?
  ├── Yes → Bottom tabs (equal visual weight)
  └── No  → One dominant + drawer/secondary nav for the rest
```

---

## 3. User Flow Notation

Map the path a user takes to complete a task. Text-based format Claude can produce.

### Happy Path (Linear)

```
1. [Splash] → 2. [Onboarding] → 3. [Home] → 4. [Product] → 5. [Checkout] → 6. [Confirmation]
```

### Branching Flow

```
1. [App Launch]
   ├── Returning user → 2a. [Home] (skip onboarding)
   └── New user → 2b. [Onboarding] → 2c. [Permissions] → 2a. [Home]

2a. [Home] → 3. [Product Detail]
   ├── Authenticated → 4a. [Add to Cart] → 5. [Checkout]
   └── Guest → 4b. [Login/Signup] → 4a. [Add to Cart] → 5. [Checkout]

5. [Checkout]
   ├── Success → 6a. [Order Confirmation]
   └── Payment failed → 6b. [Error + Retry]
```

### Entry Points

```
ENTRY POINTS:
  - Organic: App icon → Splash → Home
  - Deep link: Product URL → Product Detail (skip Home)
  - Push notification: "Your order shipped" → Order Tracking
  - Widget: Quick action → Specific feature screen
```

### Notation Rules
- Number every screen
- Use → for forward navigation
- Use ├── / └── for branches
- Label branches with the condition (authenticated, guest, error, etc.)
- Every branch must converge or terminate (no dangling paths)

---

## 4. Screen Spec Template

Define each screen before visual design. One spec per screen.

```
Screen: [Name]
Purpose: [One sentence -- what does the user accomplish here?]
Arrives from: [Previous screen(s) or entry point]
Primary action: [The ONE thing the user should do]
Secondary actions: [Optional actions, lower priority]

Content zones:
  - Header: [App bar, title, back button, actions]
  - Body: [Main content type -- list, form, media, etc.]
  - Actions: [Primary CTA, secondary buttons]
  - Navigation: [Bottom tabs, contextual nav, none]

Data displayed: [What info this screen shows]
Data collected: [What input this screen captures, if any]
User exits to: [Next screen(s) on primary action]

States:
  - Empty: [What shows when no data exists]
  - Loading: [Skeleton layout]
  - Error: [What shows on failure]
  - Populated: [Normal state]
```

### Example

```
Screen: Product Detail
Purpose: Convince user to add item to cart
Arrives from: Home feed, Search results, Deep link
Primary action: Add to Cart
Secondary actions: Save to wishlist, Share, Read reviews

Content zones:
  - Header: Back button, share icon, wishlist heart
  - Body: Image carousel, title, price, rating, description, reviews
  - Actions: "Add to Cart" button (sticky bottom), quantity selector
  - Navigation: None (stack screen, back button returns)

Data displayed: Product images, name, price, rating, reviews, availability
Data collected: Quantity, selected variant (size/color)
User exits to: Cart (on add), Home (on back)

States:
  - Empty: N/A (always has product data or 404)
  - Loading: Skeleton with image placeholder + text blocks
  - Error: "Product not found" + "Browse similar items" CTA
  - Populated: Full product info with sticky Add to Cart
```

---

## 5. Common Flow Patterns

### Onboarding → Home
```
1. [Splash/Logo] → 2. [Value Prop 1-3 slides, skippable] → 3. [Permissions] → 4. [Home]
```
- Max 3 slides. Always provide skip.
- Ask permissions only when relevant (e.g., location permission on a map screen, not at launch).

### Browse → Detail → Action
```
1. [Feed/List] → 2. [Detail] → 3. [Action] → 4. [Confirmation]
```
- E-commerce: Products → Product Detail → Checkout → Order Confirmation
- Content: Feed → Article → Share/Save
- Social: Timeline → Post → Comment/Like

### Tab + Stack Navigation
```
Tab 1: [Home] → [Detail] → [Sub-detail]
Tab 2: [Search] → [Results] → [Detail]
Tab 3: [Profile] → [Settings] → [Edit]
```
- Each tab maintains its own navigation stack
- Switching tabs preserves scroll position and stack depth
- Back button pops within the current tab, never switches tabs

### Authentication Flow
```
1. [Login]
   ├── Biometric success → [Home]
   ├── Email + password → [Home]
   ├── "Forgot password" → 2. [Reset] → 3. [OTP] → 4. [New Password] → [Login]
   └── "Sign up" → 5. [Register] → 6. [OTP] → 7. [Profile Setup] → [Home]
```

### Settings Flow
```
1. [Settings List] → 2. [Setting Detail] → 3. [Edit/Toggle] → 4. [Confirm if destructive]
```
- Group settings by category (Account, Notifications, Privacy, About)
- Destructive actions (delete account, log out) require confirmation
- Toggle switches take effect immediately (no save button needed)
