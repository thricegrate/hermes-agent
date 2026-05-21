# Reality Check — Aschenbrenner Predictions vs. Market Events

**Companion to:** [macroeconomic-thesis.md](macroeconomic-thesis.md), [thesis-catalysts.md](thesis-catalysts.md).

**Last updated:** 2026-05-13 (initial population). This file gets refreshed monthly by the scheduled refresh agent — see [sizing-overlay.md](sizing-overlay.md) for cadence rules.

**Purpose:** Track which Aschenbrenner predictions (from June 2024) have already played out, are in flight, or remain pending. The goal is to distinguish what the market has priced in from what is still ahead.

**Status legend:**
- `[FIRED]` — Event happened, prediction confirmed (or refuted)
- `[IN PROGRESS]` — Partially confirmed, in flight, observable trajectory
- `[PENDING]` — Not yet visible in market, future-dated

---

## Quick Score (as of 2026-05-13)

| Bucket | Count | Notes |
|--------|-------|-------|
| `[FIRED]` confirming the thesis | 11 | Largely capex, PPAs, capability benchmarks |
| `[FIRED]` refuting the thesis | 1 | DeepSeek efficiency surprise (small drag, not thesis-breaking) |
| `[IN PROGRESS]` | 6 | Cluster scaling, AGI capability, government project signals |
| `[PENDING]` | 8 | Intelligence explosion, 10 GW cluster, $1T cluster, full Project |

**Bottom line:** The capex and physical buildout half of the thesis is largely confirmed. The capability and government-project halves are still ahead. Tier 1 nuclear/power/semi names already reflect significant thesis pricing. Defense AI and government IT contractors have less of the thesis priced in (PLTR aside).

---

## Predictions vs. Events Table

### Compute Scaling & Capability (Ch.1, Ch.2)

| Prediction | Chapter | Date Predicted | Event(s) | Status |
|------------|---------|----------------|----------|--------|
| Compute scaling ~0.5 OOMs/year continues through 2027 | Ch.1 | through 2027 | Confirmed through 2024-2025; H100 → H200 → Blackwell ramp; ~3-4x cluster size growth per year | `[IN PROGRESS]` |
| Algorithmic efficiency ~0.5 OOMs/year | Ch.1 | through 2027 | Confirmed; smaller models matching larger ones (Llama 3.3, Claude 3.5 Sonnet matching Opus, GPT-4o cost reductions) | `[IN PROGRESS]` |
| "Unhobbling" from chatbot to agent | Ch.1 | by 2026 | Substantial progress: Claude 3.5 Sonnet computer use (Oct 2024), OpenAI Operator (Jan 2025), Anthropic agentic SWE | `[IN PROGRESS]` |
| AGI by 2027 (researcher-level capability) | Ch.1 | 2027 | TBD; SWE-bench Verified pass rates climbing fast (50%+ for top models in 2025); GPQA scores at PhD level for top models | `[IN PROGRESS]` |
| Intelligence explosion within ~1 year of AGI | Ch.2 | post-AGI | Not yet | `[PENDING]` |
| 100M human-equivalent AI researchers | Ch.2 | post-AGI | Not yet | `[PENDING]` |
| Economic growth 30%/year+ | Ch.2 | post-intelligence-explosion | Not yet | `[PENDING]` |
| Capability plateau (potential kill switch) | Ch.1 implicitly refuted | predicted continued progress | DeepSeek-R1 (Jan 2025) and DeepSeek-V3 showed efficiency surprises; modest negative for raw compute demand thesis but not thesis-breaking | `[FIRED]` (refuting at margin) |

### Physical Buildout — Compute Infrastructure (Ch.3)

| Prediction | Chapter | Date Predicted | Event(s) | Status |
|------------|---------|----------------|----------|--------|
| Hyperscaler capex $50B+ each in 2024 | Ch.3 | 2024 | Confirmed: MSFT $55B FY24, GOOGL $52B, AMZN $77B (FY24, AI heavy), META $40B → guided to $60-65B for FY25 | `[FIRED]` |
| Hyperscaler capex acceleration through 2026 | Ch.3 | 2025-2026 | Confirmed: cumulative Big 4 capex pointing to $300B+ in 2025, $400B+ in 2026 | `[FIRED]` |
| 1 GW cluster by 2026 | Ch.3 | 2026 | In flight: Stargate Phase 1 Abilene TX (~1.2 GW target), xAI Memphis Phase 2 (~1 GW), Meta Louisiana | `[IN PROGRESS]` |
| 10 GW cluster by 2028 | Ch.3 | 2028 | Not yet operational. Multiple sites in planning. Stargate ultimate scale targets ~5+ GW. | `[PENDING]` |
| $100B cluster slated for 2028 (MSFT/OpenAI) | Ch.3 | 2028 | Stargate ($500B over 4 years) announced Jan 2025 with OpenAI + Oracle + SoftBank — this is the predicted cluster, materialized | `[FIRED]` (announcement); `[IN PROGRESS]` (build) |
| Trillion-dollar cluster by 2030 | Ch.3 | 2030 | Trajectory consistent. Stargate $500B is the down payment. | `[PENDING]` |
| Total AI investment $500B in 2026 | Ch.3 | 2026 | Tracking; sum of hyperscaler capex + Stargate + neoclouds + sovereign clusters approaching this in 2026 | `[IN PROGRESS]` |
| ~100% of TSMC output to support trillion-dollar cluster | Ch.3 | 2030 | TSMC capex itself ramping; advanced node share rising | `[PENDING]` |

### Power Buildout (Ch.3)

| Prediction | Chapter | Date Predicted | Event(s) | Status |
|------------|---------|----------------|----------|--------|
| Power becomes binding bottleneck | Ch.3 | late decade | Already visible in grid interconnection queue lengths (5-7 year waits in PJM, ERCOT); power transformer shortages | `[FIRED]` |
| Hyperscalers sign nuclear PPAs | Ch.3 | implied 2024-2026 | Amazon-Talen 1 GW Susquehanna (March 2024); Microsoft-Constellation Three Mile Island restart PPA (Sept 2024); Google-Kairos SMR (Oct 2024); Amazon-X-Energy SMR ($500M, Oct 2024); Oracle (Three Mile Island adjacent); Meta-Constellation (June 2025) | `[FIRED]` |
| Natural gas bridge buildout (Marcellus/Utica) | Ch.3 | 2024-2027 | New pipeline approvals (Mountain Valley Pipeline), expansions, gas-to-datacenter direct deals (EQT-direct power supply discussion ongoing) | `[IN PROGRESS]` |
| US grid investment surge | Ch.3, Ch.6 | through decade | Federal Energy Regulatory Commission Order 1920 (May 2024) accelerating transmission planning; states like Texas, Virginia, Georgia approving 10+ GW of new generation tied to datacenters | `[IN PROGRESS]` |
| 100 GW per cluster by 2030 | Ch.3 | 2030 | Nowhere close yet; would be a single facility >20% of US electricity | `[PENDING]` |

### Lab Security & Espionage (Ch.4)

| Prediction | Chapter | Date Predicted | Event(s) | Status |
|------------|---------|----------------|----------|--------|
| 12-24 month leak window | Ch.4 | by mid-2026 | No confirmed major weight exfiltration publicly. DeepSeek arrival (Jan 2025) could indicate independent capability or partial leakage — ambiguous. | `[IN PROGRESS]` |
| Labs adopt nation-state security | Ch.4 | reactive | Anthropic, OpenAI have ramped security teams; DOE / NSA engagement reported but no public airgapped infrastructure yet | `[IN PROGRESS]` |
| Cybersecurity sector tailwind from AI security needs | Ch.4 | secular | PANW, CRWD, ZS all bull moves through 2024-2026; HACK ETF up substantially | `[FIRED]` |
| Government mandates AI lab security standards | Ch.4 | medium-term | Biden EO 14110 (Oct 2023) included some; Trump admin EO (Jan 2025) reportedly extends to security; National Security Memorandum on AI (Oct 2024) | `[IN PROGRESS]` |

### Alignment / Safety (Ch.5)

| Prediction | Chapter | Date Predicted | Event(s) | Status |
|------------|---------|----------------|----------|--------|
| RLHF breaks down above human level | Ch.5 | post-AGI | TBD — only relevant once AGI hit | `[PENDING]` |
| Few dozen serious alignment researchers | Ch.5 | 2024 | Confirmed at time of writing; some growth in 2024-2026 (Anthropic alignment team expanded, new institutions like METR) | `[IN PROGRESS]` |
| EU AI Act enforcement actions | Ch.5 implicit | from 2025 | EU AI Act in force from Feb 2025; first enforcement decisions on systemic-risk models in progress through 2026 | `[IN PROGRESS]` |
| Visible alignment incident | Ch.5 | possible during transition | None confirmed yet at the scale Aschenbrenner describes | `[PENDING]` |

### Geopolitics & Defense (Ch.6)

| Prediction | Chapter | Date Predicted | Event(s) | Status |
|------------|---------|----------------|----------|--------|
| Export controls tighten | Ch.6 | through 2025+ | Confirmed: October 2023 controls, October 2024 expansion, Jan 2025 additional restrictions on Huawei + advanced HBM | `[FIRED]` |
| Defense AI procurement surge | Ch.6 | 2024-2027 | PLTR commercial + government growth (TITAN contract, AIP commercial wins); Anduril valuations exploding (private); AVAV, KTOS contract awards | `[FIRED]` (early innings) |
| Huawei Ascend ~2-3x worse per dollar than Nvidia | Ch.6 | 2024 | Confirmed at time; Huawei has narrowed gap with 910C/910D in 2025 but moat still holds | `[IN PROGRESS]` |
| China outbuilds US on electricity | Ch.6 | ongoing | Confirmed: China added ~300 GW in 2024 alone (mostly solar + coal); US flat | `[IN PROGRESS]` |
| 2027 Taiwan flashpoint risk | Ch.6 | 2027 | TBD; tension elevated but no conflict | `[PENDING]` |

### Government AGI Project (Ch.7)

| Prediction | Chapter | Date Predicted | Event(s) | Status |
|------------|---------|----------------|----------|--------|
| US government absorbs AGI development | Ch.7 | late 2026 / 2027 | National Security Memorandum on AI (Oct 2024) is the closest precursor. No formal "Manhattan Project for AI" yet. Trump admin signals divergent (more private-sector-led). | `[PENDING]` |
| Defense contractor relationships with frontier labs | Ch.7 | 2026-2027 | PLTR is the cleanest example. OpenAI has DoD contracts (Jan 2025+). Anthropic Palantir partnership for defense (late 2024). | `[FIRED]` (early; not full Project framework) |
| Trillions in congressional appropriations | Ch.7 | 2027+ | CHIPS Act ($52B, 2022) was prologue; no AI-specific trillion-dollar appropriation yet | `[PENDING]` |
| Frontier AI moves to classified infrastructure | Ch.7 | 2027+ | Not yet observable in public market — labs still operate publicly | `[PENDING]` |

### Closing / Synthesis (Ch.8)

| Prediction | Chapter | Date Predicted | Event(s) | Status |
|------------|---------|----------------|----------|--------|
| "Trillions" into GPU/datacenter/power buildout this decade | Ch.8 | through 2030 | On trajectory; cumulative announced spend through 2025 already >$1T | `[IN PROGRESS]` |
| Superintelligence before 2030 | Ch.8 | by 2030 | Far from observable today | `[PENDING]` |
| Few hundred people in SF realize what's coming | Ch.8 | observation | Awareness has clearly spread beyond a few hundred (mainstream coverage, AI infra trade is now widely held) | `[FIRED]` (refuted as time-of-writing observation; thesis becoming consensus) |

---

## Major Refutation Risks (Watch For)

Events that would force a thesis re-rate downward:

| Risk | Status | Action if fired |
|------|--------|------------------|
| Capability plateau across all frontier labs | Not seen — top labs still releasing 2026-2027 generations | Kill switch #3 in [sizing-overlay.md](sizing-overlay.md) |
| DeepSeek-class efficiency breakthrough AT frontier scale | Modest pressure already from DeepSeek-V3/R1 — but frontier labs still scaling compute | Monitor; downgrade tiers if frontier compute demand falls |
| Big 4 hyperscaler capex cut | Not seen — capex still rising | Kill switch #2 |
| Major alignment incident | Not seen | Kill switch #5 (regulatory pause possible) |
| Government caps frontier training | Not seen at US/EU level; EU AI Act allows it for systemic risk | Kill switch #5 |
| China steals AGI weights | Ambiguous (DeepSeek arrival could be independent OR partial leakage) | Re-evaluate Ch.4 thesis intensity |

---

## Confirmation Bias Check

To avoid only counting hits, here are predictions that did NOT play out as Aschenbrenner expected:

- **"Basically nobody outside a few hundred people realizes":** false — AI infra has become consensus trade by 2025. Nuclear utilities, semis, defense AI all widely held. Market has priced in significant Aschenbrenner-aligned outcomes.

- **DeepSeek arrival (Jan 2025):** Demonstrates that algorithmic efficiency can advance OUTSIDE the leading US labs, somewhat undermining the assumption that compute will be the only edge.

- **Stargate as private-sector project (Jan 2025):** Aschenbrenner predicted government absorbing frontier development. Stargate is a private consortium (OpenAI + Oracle + SoftBank + others) with government cheerleading rather than ownership. Doesn't match Ch.7's "Manhattan Project" framework directly.

- **No major alignment incident:** Predicted as a meaningful tail risk during the transition. So far quiet. Reduces near-term kill-switch probability.

- **No confirmed weight exfiltration:** Despite 12-24 month prediction window now elapsed, no public confirmation of major lab compromise.

These do not refute the core thesis but suggest the timing and exact form may differ from Aschenbrenner's specific path-dependent predictions.

---

## Monthly Refresh Checklist (for the scheduled agent)

The full automation prompt lives in [monthly-refresh-prompt.md](monthly-refresh-prompt.md). Schedule via `/schedule` or run manually first business day after market close each month.

Items to update each month:

1. **Hyperscaler capex updates** — review prior-month earnings prints (MSFT, GOOGL, AMZN, META). Update capex confirmation row.
2. **NVDA/AMD/TSM/MU earnings** — update capability and supply rows.
3. **Nuclear PPAs and SMR permits** — add any new utility-hyperscaler deals or NRC permit decisions.
4. **Model releases** — log any new flagship model from OpenAI/Anthropic/Google/Meta with benchmark deltas.
5. **Policy events** — log executive orders, EU AI Act actions, congressional hearings.
6. **Kill switch tripwire status** — re-run worksheet in [sizing-overlay.md](sizing-overlay.md) Appendix B.
7. **Tag changes** — escalate `[PENDING]` to `[IN PROGRESS]` or `[FIRED]` as appropriate. Add a one-line note with event date.
8. **Score the bucket counts** — update the Quick Score table at the top of this file.

Refresh format:

```
## Update for YYYY-MM
- [prediction row]: status [PENDING → IN PROGRESS] — [event date] — [event description] — [source URL or earnings transcript]
- ...

## Kill switch status (re-checked YYYY-MM-DD):
- Tripwire 1 (NVDA DC YoY < 30% for 2 Q): NOT TRIPPED — latest Q YoY = X%
- Tripwire 2 (Sum hyperscaler capex cut > 15%): NOT TRIPPED — sum direction = +Y%
- ... (etc per worksheet)
```

Append the monthly update at the bottom of this file under a `## Monthly Update Log` heading (not yet created — first refresh will create it).
