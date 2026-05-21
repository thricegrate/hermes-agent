# Theory of Constraints (Goldratt)

## Table of Contents
1. [5 Focusing Steps](#5-focusing-steps)
2. [Current Reality Tree](#current-reality-tree-crt)
3. [Future Reality Tree](#future-reality-tree-frt)
4. [Evaporating Cloud](#evaporating-cloud)
5. [Drum-Buffer-Rope](#drum-buffer-rope-dbr)
6. [Critical Chain Project Management](#critical-chain-project-management-ccpm)
7. [Throughput Accounting](#throughput-accounting)
8. [Constraint Migration](#constraint-migration)
9. [Industry Example: Newsletter Business](#industry-example-newsletter-business)

---

## 5 Focusing Steps

The core process for identifying and exploiting bottlenecks:

| Step | Action | Question |
|------|--------|----------|
| 1. **IDENTIFY** | Find the system's constraint | "What single thing limits overall output?" |
| 2. **EXPLOIT** | Maximize its output without investment | "How do we get more from this constraint as-is?" |
| 3. **SUBORDINATE** | Align everything else to support it | "Is every other resource serving the constraint?" |
| 4. **ELEVATE** | Add capacity through investment | "Now that we've maxed it, should we invest to expand it?" |
| 5. **REPEAT** | When broken, find the next constraint | "The constraint moved. Where is it now?" |

**Critical rules:**
- Any improvement NOT at the constraint is an illusion
- An hour lost at the bottleneck = an hour lost for the entire system
- An hour saved at a non-bottleneck = meaningless
- Activating a resource ≠ utilizing a resource (keeping people busy ≠ productive)

**Coaching application:**
- Step 1: "What's the ONE thing limiting your growth right now?"
- Step 2: "Before hiring or spending money, have you fully exploited what you have?"
- Step 3: "Is your team organized to support the constraint, or is everyone doing their own thing?"
- Step 4: "Only after steps 2-3: What investment would expand this bottleneck?"
- Step 5: "Congratulations, you broke it. Now what's the new constraint?"

---

## Current Reality Tree (CRT)

**When to use:** When the user knows things are broken but can't pinpoint why. Multiple symptoms, unclear root cause.

**Process:**
1. List all Undesirable Effects (UDEs): symptoms the business is experiencing
   - "Revenue is flat"
   - "Agency clients keep leaving"
   - "Content quality is dropping"
   - "Team is burned out"
2. Connect them with cause-and-effect arrows (if X then Y)
3. Follow chains upward to find root causes
4. Identify the CORE constraint creating multiple UDEs

**Example CRT for a newsletter business:**
```
UDE: Revenue flat at $20K/mo
  ← UDE: Can't add more newsletters (no capacity)
    ← UDE: Current team is maxed out
      ← ROOT: No documented SOPs → everything depends on founder
        ← ROOT: Founder doing too many tasks (hasn't delegated)

UDE: Agency clients leaving (low retention)
  ← UDE: Clients don't see clear results
    ← UDE: No concrete KPIs or reporting
      ← ROOT: No documented SOPs → service delivery is inconsistent
```

**The power:** Both UDEs trace to the SAME root cause (no SOPs, founder bottleneck). Fix the root, fix both symptoms.

**Coaching prompt:** "List every problem you're dealing with right now. ALL of them. We're going to find what's really going on."

---

## Future Reality Tree (FRT)

**When to use:** After identifying root cause with CRT. To validate solutions before implementing.

**Process:**
1. Take the root cause from CRT
2. Design an "injection" (proposed solution)
3. Map out the positive cascading effects
4. Validate that UDEs disappear
5. Check for negative branches (unintended consequences)

**Example FRT:**
```
Injection: Document SOPs for content creation, growth, and client delivery

→ Positive: Team can follow standardized processes
  → Positive: Founder freed from operational tasks
    → Positive: Founder focuses on strategy + growth
      → Positive: Can launch new newsletters (capacity unlocked)
        → Positive: Revenue increases

  → Positive: Client delivery becomes consistent
    → Positive: Clients see predictable results
      → Positive: Retention improves
        → Positive: Revenue stabilizes

Negative branch check: "Does SOP creation take so long it hurts current operations?"
→ Mitigation: Create SOPs incrementally, one process per week
```

---

## Evaporating Cloud

**When to use:** When facing apparent trade-offs or "either/or" decisions. Resolves conflicts by surfacing hidden assumptions.

**Structure:**
```
A (Common Goal)
├─ B (Need 1) → D (Want 1)
└─ C (Need 2) → D' (Want 2, conflicts with D)
```

**Process:**
1. State the conflict (D vs D')
2. Identify the needs each satisfies (B and C)
3. Find the common goal both serve (A)
4. Surface assumptions behind each connection
5. Challenge assumptions to find a win-win injection

**Example: Newsletter portfolio scaling conflict**
```
A: Grow revenue to $100K/mo
├─ B: Need more newsletters for more revenue
│   → D: Launch 10+ newsletters (requires more staff, more content)
└─ C: Need to maintain quality and margins
    → D': Stay focused on fewer newsletters (limits revenue)
```

**Hidden assumption:** "Each newsletter requires the same level of hands-on attention."

**Injection:** Systematize with SOPs + templates + automation. Each new newsletter uses 80% templated process, 20% custom. Quality maintained through systems, not personal attention.

**Result:** Both needs met. More newsletters AND maintained quality.

---

## Drum-Buffer-Rope (DBR)

**When to use:** When work piles up but doesn't get finished. Teams busy but throughput low. Constant firefighting.

**Three components:**
| Component | Function | Example |
|-----------|----------|---------|
| **Drum** | Constraint sets the pace for entire system | Editor can review 5 newsletters/week |
| **Buffer** | Time/work buffer before constraint | Writers submit drafts 3 days before deadline |
| **Rope** | Control work release at constraint's pace | Only assign new topics when editor has capacity |

**Rules:**
- Never release more work into the system than the constraint can process
- Protect the constraint: it should NEVER starve for work (that's what the buffer is for)
- Non-constraints should have spare capacity (this is intentional, not waste)

**Coaching application:**
- "What's your constraint? What's its capacity per week?"
- "Do you have a buffer protecting it, or does it frequently starve or get overwhelmed?"
- "Are you releasing work at the constraint's pace, or flooding the system?"

---

## Critical Chain Project Management (CCPM)

**When to use:** Complex projects with multiple dependencies (newsletter launches, course creation, agency onboarding).

**Key principles:**
1. **Remove task-level padding**: Estimate tasks at 50% confidence (median time, not worst case)
2. **Aggregate safety into buffers**: Place safety time at project end and integration points
3. **Eliminate multitasking**: One task at a time until complete (switching costs are enormous)
4. **Manage by buffer consumption**: Track how fast you're using the safety buffer

**Buffer management:**
| Buffer Used | Project Progress | Status |
|-------------|-----------------|--------|
| <33% | >33% complete | Green, on track |
| 33-66% | ~50% complete | Yellow, monitor |
| >66% | <66% complete | Red, take action |

**Applied to newsletter launch:**
- Traditional: 6 weeks with padding on every task
- CCPM: 3 weeks aggressive estimates + 1 week project buffer = 4 weeks total
- Track buffer: If buffer is 50% consumed at 25% completion → red flag, intervene

---

## Throughput Accounting

**Three metrics (replace traditional accounting for decision-making):**

| Metric | Definition | Formula |
|--------|-----------|---------|
| **Throughput (T)** | Rate of generating money through sales | Revenue - Truly Variable Costs |
| **Inventory (I)** | Money invested in things intended to sell | WIP, unsold inventory, capital |
| **Operating Expense (OE)** | Money spent turning inventory into throughput | Salaries, rent, tools, overhead |

**Decision rule:** Good decisions increase T while decreasing I and OE.

**Applied to business decisions:**
- "Should I hire a writer at $4K/mo?" → Will throughput increase by >$4K/mo?
- "Should I buy this tool at $200/mo?" → Will throughput increase by >$200/mo?
- "Should I launch newsletter #5?" → What's the incremental T vs incremental OE?

**Key insight:** Traditional accounting treats all costs equally. Throughput accounting distinguishes between costs that create throughput (invest more) and costs that don't (minimize).

---

## Constraint Migration

**As businesses scale, constraints move:**

| Revenue Range | Typical Constraint | Focus |
|--------------|-------------------|-------|
| $0-$10K/mo | Product-market fit, content quality | Create something people want |
| $10K-$50K/mo | Founder capacity (doing everything) | Systematize, delegate |
| $50K-$250K/mo | Marketing/distribution or conversion | Build systems independent of founder |
| $250K+/mo | Policy/process constraints, management | Remove bureaucracy, optimize |

**Warning signs of constraint migration:**
- The "fix" that worked last quarter stops working
- Growth stalls despite more effort
- New problems emerge that didn't exist before
- The team that was fine is suddenly overwhelmed

**Response:** Go back to Step 1 of the 5 Focusing Steps. The constraint moved. Find it again.

---

## Industry Example: Newsletter Business

*The frameworks above apply to ANY business. Below is one industry example to illustrate application.*

### Mapping the newsletter pipeline
```
Idea → Research → Draft → Edit → Publish → Distribute → Monetize
```
Measure throughput at each stage. Where does work pile up? That's your constraint.

### Common newsletter constraints by stage

**Creation constraint:**
- Symptom: Inconsistent publishing, rushed content
- Exploit: Content templates, batch creation, AI-assisted drafting
- Subordinate: All other tasks pause during writing blocks
- Elevate: Hire additional writers

**Distribution constraint:**
- Symptom: Good content, low subscriber growth
- Exploit: Optimize existing channels (better Meta ad creatives, better co-promo partners)
- Subordinate: Don't create more content until distribution is fixed
- Elevate: Add new distribution channels (SEO, social, partnerships)

**Monetization constraint:**
- Symptom: Large audience, low revenue per subscriber
- Exploit: Better ad placements, higher CPM networks, sponsored content
- Subordinate: Don't grow audience until monetization is optimized
- Elevate: Add new revenue streams (paid tier, digital products, agency)

**Operations constraint:**
- Symptom: Can't launch more newsletters, team overwhelmed
- Exploit: SOPs, automation, templates
- Subordinate: Don't launch new newsletters until operations are systematized
- Elevate: Hire operations manager, invest in better tools

### DBR for newsletter content pipeline
- **Drum**: Editor capacity (5 newsletters/week)
- **Buffer**: 3-day buffer of ready-to-edit drafts
- **Rope**: Only assign new topics when buffer drops below 3 drafts
- Result: Consistent publishing, no fire drills, editor never overwhelmed
