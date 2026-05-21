# Aschenbrenner Watchlist — Tier 1 / 2 / 3 Lineup

**Companion to:** [macroeconomic-thesis.md](macroeconomic-thesis.md), [sizing-overlay.md](sizing-overlay.md), [thesis-catalysts.md](thesis-catalysts.md).

This is the curated universe for the macro overlay. Jeff Sun hard gates (VCP, RVOL, RS, ADR%, ATR-from-50-MA, etc.) still apply for entry. The overlay modifies WHICH themes get priority and HOW MUCH size to take per setup.

---

## Tier Definitions

| Tier | Hold horizon | Sizing multiplier | Stop override |
|------|--------------|-------------------|----------------|
| **Tier 1** | Multi-year (through 2027-2028 inflection) | 2-3x Jeff Sun base | YES if catalyst within 30 days AND no kill switch tripped |
| **Tier 2** | 6-12 months (current capex cycle) | 1.5x base | NO (standard 3-stop) |
| **Tier 3** | 1-3 months (catalyst-driven) | 1.25x base | NO (tighter stops, 0.5x ATR multiplier on Stop 3) |

Full sizing math, override rules, and kill-switch tripwires in [sizing-overlay.md](sizing-overlay.md).

---

## TIER 1 — Multi-Year Conviction (2-3x sizing, override allowed)

### Theme: Nuclear / Uranium

**Why Tier 1:** Power is THE binding bottleneck per Ch.3. Nuclear is the only zero-carbon 24/7 baseload that scales to 100 GW grid-level demand. Hyperscalers already signing direct PPAs (Amazon-Talen, CEG-Microsoft, Google-Kairos). Multi-year revenue visibility once PPAs sign.

| Symbol | Why | Notes |
|--------|-----|-------|
| **CEG** | Already has Microsoft Three Mile Island restart PPA. Cleanest pure-play merchant nuclear. | Anchor name. |
| **VST** | Vistra-Energy Harbor acquisition gave it nuclear fleet + merchant gas. Hyperscaler PPA optionality. | Anchor name. Aschenbrenner reportedly holds. |
| **TLN** | Talen Energy — Amazon 1 GW Susquehanna deal already done. | Anchor name. Aschenbrenner reportedly holds. |
| **CCJ** | Cameco — uranium mining, demand pull from utility restarts. | Upstream play. |
| **OKLO** | Small modular reactor (SMR) speculative. Sam Altman-backed. | Lottery ticket within Tier 1. Use Tier 3 sizing despite Tier 1 theme. |
| **NNE** | Nano Nuclear — SMR microreactor speculative. | Same as OKLO — Tier 3 sizing within Tier 1 theme. |

**ETF:** `URA` (broad uranium + nuclear).

**Kill conditions:** Hyperscaler PPA pipeline freezes (3+ months no new signed deals), NRC permitting reform reverses, fusion breakthrough announced with credible commercial timeline <10 years, or a major nuclear incident anywhere globally.

---

### Theme: Power Grid / Generation

**Why Tier 1:** Same Ch.3 thesis as nuclear, but covers the broader grid buildout (gas peakers, transformers, switchgear, transmission). US capacity has been flat for a decade per Ch.6 while China outbuilt the entire US base. Massive catch-up required.

| Symbol | Why | Notes |
|--------|-----|-------|
| **GEV** | GE Vernova — gas turbines, the bridge fuel of choice for fast 10 GW buildouts. | Anchor name. Pure-play AI power infrastructure. |
| **VST** | Already in Nuclear. Counted once. | (duplicate position note) |
| **CEG** | Already in Nuclear. Counted once. | (duplicate position note) |
| **NRG** | NRG Energy — merchant power, datacenter PPA exposure. | Secondary. |
| **ETN** | Eaton — power management, datacenter electrical infra. | Anchor name for picks-and-shovels exposure. |
| **TLN** | Already in Nuclear. Counted once. | (duplicate position note) |

**ETF:** `GRID` (broad grid infrastructure).

**Kill conditions:** US grid demand growth slows materially (EIA monthly data), policy push for distributed/microgrid solutions undermines centralized grid investment, transformer supply constraint resolves to surplus.

---

### Theme: Semiconductors

**Why Tier 1:** Ch.1, Ch.2, Ch.3 all reinforce. Compute demand grows ~0.5 OOMs/year structurally. AMD forecasts $400B AI accelerator market by 2027. TSMC is sole advanced fab. ASML is sole EUV supplier.

| Symbol | Why | Notes |
|--------|-----|-------|
| **NVDA** | Dominant. 80%+ AI training share. | Anchor. Default Tier 1 with override eligibility. |
| **AMD** | Challenger. MI300/MI350 ramp. Memory-reframed CPU:GPU shift per Lisa Su. | Anchor. |
| **TSM** | Sole leading-edge logic fab. ~100% of TSMC output supports trillion-dollar cluster per Ch.3. | Anchor but watch Taiwan geopolitical tail risk. |
| **AVGO** | Custom ASIC + networking. Hyperscaler design wins. | Anchor. Aschenbrenner reportedly holds 11.7% in fund. |
| **ASML** | EUV monopoly. Export control regime pillar. | Anchor for lithography. |
| **AMAT** | Wafer fab equipment. Sustained capex driver. | Secondary. |
| **LRCX** | Etch / deposition. Same thesis as AMAT. | Secondary. |
| **INTC** | Government foundry play; CHIPS Act funded. Aschenbrenner reportedly held 45.7% in fund Q1 2025 (high conviction position). | Speculative within Tier 1. Use Tier 2 sizing until execution improves. |

**ETF:** `SMH`.

**Kill conditions:** Compute scaling drops below 0.5 OOMs/year for 2+ consecutive years, major efficient-AI architecture eliminates compute demand (DeepSeek-class breakthrough at frontier scale), TSMC physical disruption (Taiwan event), hyperscaler capex cut >15% across MSFT/GOOGL/AMZN/META.

---

### Theme: AI Infrastructure

**Why Tier 1:** Broader basket that captures NVDA + PLTR + cloud + networking. Highest-correlation ETF to the overall thesis. Use as a sleeve, not for individual entries (entries via the constituent Tier 1 names).

| Symbol | Why | Notes |
|--------|-----|-------|
| **AIQ** | The ETF. Use for sleeve exposure when no individual setup. | ETF only. |

**Kill conditions:** Same as Semiconductors + AI revenue ramp falters (OpenAI revenue trajectory, Anthropic, Google).

---

### Theme: Defense AI / Primes

**Why Tier 1:** Ch.6, Ch.7. Whoever wins AGI wins militarily (Gulf War tech-gap analogy, Cortes-Aztec). US government AGI project (Ch.7) channels trillions through defense contractor relationships. PLTR is the pure-play.

| Symbol | Why | Notes |
|--------|-----|-------|
| **PLTR** | Pure-play government AI data platform. Already trading like Tier 1 sized in. | Anchor. Single-name risk is real — use 3-stop strategy strictly. |
| **LMT** | Defense prime. AI-integrated systems (F-35, hypersonics). | Anchor. |
| **RTX** | Iron Dome, missile defense (Ch.6 references Iran missile 99% intercept). | Anchor. |
| **NOC** | Stealth, autonomous platforms. | Secondary. |
| **AVAV** | AeroVironment — drone warfare. | Tier 2 sizing inside Tier 1 theme. |
| **KTOS** | Kratos — autonomous weapons, drone targets. | Tier 2 sizing inside Tier 1 theme. |

**ETF:** `ITA`.

**Kill conditions:** US-China diplomatic de-escalation (low probability), defense budget cuts (low probability across administrations), Taiwan-Strait stability resolved (would reduce urgency), PLTR-specific accounting/governance event.

---

## TIER 2 — Capex-Cycle Conviction (1.5x sizing, standard stops)

### Theme: Memory / HBM

**Why Tier 2:** Ch.3 names HBM as a co-bottleneck. 100k GPUs to 100M GPUs by 2030 = ~1000x HBM demand. Only SK Hynix, Micron, Samsung supply.

| Symbol | Why | Notes |
|--------|-----|-------|
| **MU** | Sole US-listed HBM producer. HBM3E ramp. | Anchor. |
| **SNDK** | SanDisk — broader storage. | Secondary. |
| **WDC** | Western Digital — broader storage. | Secondary. |

**No ETF.** Use MU as primary expression.

**Kill conditions:** Per [sizing-overlay.md](sizing-overlay.md) kill switches — MU guides HBM revenue down 2+ consecutive quarters → exit position immediately.

---

### Theme: Datacenter Infrastructure & REITs

**Why Tier 2:** Ch.3 — powered land is scarce, liquid cooling required at 10 GW density. REITs benefit from hyperscaler lease demand.

| Symbol | Why | Notes |
|--------|-----|-------|
| **VRT** | Vertiv — liquid cooling, datacenter infra. Pure-play. | Anchor. |
| **EQIX** | Equinix — interconnect-heavy colocation. | Anchor. |
| **DLR** | Digital Realty — hyperscale leases. | Secondary. |

**ETF:** `DTCR`.

**Kill conditions:** Hyperscalers shift to owned campuses exclusively (removes REIT demand), liquid cooling commoditizes (compresses VRT margins).

---

### Theme: Cybersecurity

**Why Tier 2:** Ch.4 demands lab security uplift from "level 0 of 4" to nation-state-grade. Ch.6 names superhuman hacking as a primary AI weapon. Both offensive and defensive cyber budgets ramp.

| Symbol | Why | Notes |
|--------|-----|-------|
| **PANW** | Palo Alto — broad platform. | Anchor. |
| **CRWD** | CrowdStrike — endpoint, threat intel. | Anchor. |
| **ZS** | Zscaler — zero-trust architecture (called out in Ch.4 framing). | Secondary. |
| **FTNT** | Fortinet — broader stack. | Secondary. |
| **S** | SentinelOne — endpoint challenger. | Tier 3 sizing within Tier 2 theme. |

**ETF:** `HACK`.

**Kill conditions:** Major cyber vendor consolidation (acquisitions), AI-native security disrupts incumbents (low near-term probability).

---

### Theme: Government IT / Cleared Contractors

**Why Tier 2:** Ch.4 + Ch.7 — airgapped datacenters need cleared contractors. The Project (Ch.7) is implemented by Boeing/Lockheed-style relationships. SCIF/SCI-cleared firms benefit directly.

| Symbol | Why | Notes |
|--------|-----|-------|
| **BAH** | Booz Allen — DoD AI integrator. | Anchor. |
| **LDOS** | Leidos — federal IT, classified work. | Anchor. |
| **SAIC** | Science Applications — same. | Secondary. |

No clean ETF. Use BAH as primary.

**Kill conditions:** Federal budget reconciliation cuts defense IT spending materially (low probability), competitive bid losses for major contracts.

---

## TIER 3 — Catalyst-Driven (1.25x sizing, tighter stops)

### Theme: Natural Gas Producers (Bridge Fuel)

**Why Tier 3:** Ch.3 names Marcellus/Utica gas as fastest path to 10 GW scale. ~1200 new wells and ~40 rigs can be deployed in under a year. But: this is a bridge, not the destination — nuclear takes over by late decade. Catalyst-bounded.

| Symbol | Why | Notes |
|--------|-----|-------|
| **EQT** | EQT — largest Marcellus producer. Aschenbrenner reportedly holds. | Anchor for Tier 3. |
| **AR** | Antero — Appalachian. | Secondary. |
| **CNX** | CNX Resources — same basin. | Secondary. |

**ETF:** `XLE` (broader, not pure-play).

**Kill conditions:** Pipeline opposition / ESG financing freeze, nuclear permitting reform accelerates timeline so gas bridge shrinks, fed gas price collapse (oversupply).

---

### Theme: Speculative / Lottery Tickets

These are smaller positions with high upside if specific thesis bullets play out, but they don't earn Tier 1/2 sizing because of execution risk or speculative valuation.

| Symbol | Theme | Catalyst | Sizing |
|--------|-------|----------|--------|
| **OKLO** | SMR commercialization | First NRC permit, first signed PPA | 0.5-1x base size |
| **NNE** | SMR microreactor | Same | 0.5x base |
| **LEU** | Centrus — domestic HALEU enrichment | DOE contracts, HALEU production milestones | 0.5x base |
| **CRWV** | CoreWeave — neocloud GPU compute | Public earnings cadence, hyperscaler partnerships | 1x base |
| **APLD** | Applied Digital — HPC datacenter conversion | Lease signings, REIT conversion | 0.5x base |

**Kill conditions:** Standard speculative kill — break of 50-day MA, single setup failure, news-driven gap >2 ATR.

---

### Theme: Hyperscaler Proxies

**Why Tier 3:** Trade these via Jeff Sun setups only when they fire. Macro overlay does NOT add multipliers here — these names already represent the entire market's AI thesis, no edge in concentrating.

| Symbol | Notes |
|--------|-------|
| **MSFT** | OpenAI partner. Watch capex guides. |
| **GOOGL** | TPU + Gemini + DeepMind. |
| **AMZN** | AWS + Anthropic stake. |
| **META** | Llama + AI infra capex. |

**No tier sizing modification.** Trade only on Jeff Sun setups, at standard size. Ch.7 risk: if AGI project nationalizes frontier labs, these companies' equity in those labs could be diluted/restructured.

---

## Cross-Reference to themes.py

After Phase C edits, `scripts/data/themes.py` will contain:

- `"Power Grid / Generation"` → GRID + [VST, CEG, TLN, NRG, GEV, ETN, AES]
- `"Memory / HBM"` → no ETF + [MU, SNDK, WDC]
- `"Defense AI / Primes"` → ITA + [PLTR, LMT, RTX, NOC, AVAV, KTOS]

Plus existing themes that already cover Aschenbrenner zones:
- `"Semiconductors"` → SMH
- `"Nuclear / Uranium"` → URA
- `"AI Infrastructure"` → AIQ
- `"Data Center / Tower REITs"` → DTCR
- `"Cybersecurity"` → HACK
- `"Energy"` → XLE

Run `python skills/trading/scripts/data/themes.py` to see updated theme counts.

---

## Appendix: Why Each Tier 1 Ticker

### Nuclear / Uranium tier

- **CEG** — Anchor because Microsoft Three Mile Island restart PPA is signed and dated. Multi-year cash flow visibility on contracted power. Single most concrete "Aschenbrenner is right" trade in the market today. (Ch.3, "Amazon bought a 1GW datacenter campus [adjacent to nuclear power]" — same playbook, CEG variant.)

- **VST** — Anchor because Vistra-Energy Harbor created the largest nuclear-heavy merchant portfolio. Sells into ERCOT and PJM where hyperscaler demand is densest. (Aschenbrenner reportedly holds in his Situational Awareness fund per public filings.)

- **TLN** — Anchor because Amazon-Susquehanna 1 GW deal is the original template (Ch.3, "Amazon bought a 1GW datacenter campus"). PPA-style backlog visibility.

- **CCJ** — Upstream play. If reactor restarts and SMR fleet builds out as expected through 2030, uranium fuel demand reprices. Slower revenue visibility than the utilities but cleaner uranium beta.

- **OKLO** / **NNE** — Speculative SMR builders. Tier 3 sizing within Tier 1 theme because commercial revenue is still 3-5 years away and binary on NRC permitting.

### Power Grid tier

- **GEV** — Pure-play picks-and-shovels for the bridge fuel buildout. Gas turbines for new combined-cycle plants supporting AI datacenters. Multi-year orderbook visibility. (Ch.3, "Powering a 10 GW cluster via natural gas requires ~1200 new wells and ~40 rigs.")

- **ETN** — Power management, electrical infrastructure, busways. Datacenter electrical content per rack is rising. (Datacenter electrification is a structural growth segment regardless of cluster size.)

### Semis tier

- **NVDA** — Dominance. Ch.1's 0.5 OOMs/year compute scaling is realized through NVDA's product roadmap (Hopper → Blackwell → Rubin). The market has priced a lot of this in, so the trade is "don't fade it on valuation" rather than "buy on weakness." (Ch.8, "Do not short AI infrastructure on valuation.")

- **AMD** — Challenger thesis only works if MI series achieves credible market share. Lisa Su's CPU:GPU TAM reframing (per recent commentary cited in user's market notes) adds optionality.

- **TSM** — The single binding constraint named in Ch.3: "~100% of TSMC's output for a year could already support the trillion-dollar cluster." If TSM expands as planned, every other semi name benefits.

- **AVGO** — Custom ASIC for hyperscalers (Google TPU, Meta MTIA derivatives). Aschenbrenner's own fund reportedly holds. Networking exposure (Tomahawk/Jericho) compounds.

- **ASML** — EUV monopoly. Export control regime depends on ASML license enforcement. Sole supplier of leading-edge lithography.

- **INTC** — Government foundry play. CHIPS Act funded. Speculative in current form, but if Ch.7 "government AGI project" plays out, INTC foundry becomes strategic asset. Aschenbrenner's reported 45.7% fund concentration in INTC is a high-conviction bet on this thesis, not a recommendation to copy directly.

### Defense AI tier

- **PLTR** — The cleanest expression of Ch.6 + Ch.7. Pure-play government AI data platform. AIP rollout to commercial adds optionality. Single-name risk is real — strict 3-stop discipline required.

- **LMT** / **RTX** / **NOC** — Defense primes. AI-integrated weapons platforms. Multi-decade defense budget visibility regardless of administration.

- **AVAV** / **KTOS** — Drone warfare per Ch.6 "roboarmies and autonomous drone swarms." Smaller market caps = higher volatility = Tier 2 sizing within Tier 1 theme.
