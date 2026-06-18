# ShunyaBar Labs — Product Strategy, H2 2026

**Author:** CPO
**Status:** Decision document. Not a wishlist.

**Anchored in:** 60+ live API tests, MSE 2022 benchmark validation, depth-4 Merkle root-cause diagnostic, engine spectrum analysis.

---

## 1. State of the Union (What We Actually Know)

### What Works Today

- Navokoj API live and stable: `/v1/solve`, `/v1/diagnose`, hybrid XOR+CNF modes, batch, Q-SAT (N-ary)
- Engines form a real spectrum: nano (94% / 870ms) → nitro (99.4% / 830ms) → pro (99.4% / 0.1–7s) → mini (99.77% / 40s+)
- Per-instance engine choice matters: pro beats nitro on multi-constraint chains; mini is the high-quality fallback
- Soundness preserved: UNSAT detection is correct on certified benchmarks (8/10 MSE 2022 WCNF matched optimal)
- Honest limits: 1,000 vars / 5,000 clauses / 100 req/hr on free tier

### What Doesn't Work Today

- **Depth-4+ ZK Merkle paths fail across every engine.** Root-caused: not the mult chain (engine handles it in 150ms when exactly-one is removed), it's the one-hot "exactly-one" constraints choking local search at this constraint density
- **No real ZK customer can use us.** 254-bit field circuits need 254 Boolean vars per R1CS var — 25M+ vars for a typical circuit, vs our 1K ceiling
- **No native modular arithmetic at the API.** Everything goes through CNF enumeration, which doesn't scale
- **Gadget-layer quality is on the user.** Bit-blasting, witness extraction, and ZK framing are the user's problem today

---

## 2. The Honest Product Read

We're not a ZK company. We're a local-search MaxSAT engine company with a ZK-shaped marketing layer.

The engine is real and interesting — hybrid systematic+local-search is genuinely a research contribution. But the ZK framing is aspirational, not operational. Three reasons:

1. **Tier math doesn't work.** Real ZK needs 10⁶–10⁸ Boolean ops per proof. Our free tier is 5×10³ clauses. That's 5 orders of magnitude off.
2. **Latency math doesn't work.** Real ZK proofs need <1s. Our pro engine hits 7s on small chains. mini takes 40s+.
3. **Soundness UX doesn't work.** The 99.4% accuracy on single-shot means ~0.6% of proofs are wrong. For ZK that's catastrophic. mini gets to 99.77% but at 40s — still wrong 0.23% of the time, and 40s is unusable for proving.

The ZK story isn't dead — it's a **2027+ bet**, contingent on getting to 100% with a verifiable certificate (which nitro+local-search can't give).

---

## 3. Where We Play (Positioning)

Three plausible wedges. Pick one, kill the others.

### Wedge A: "The Verifiable MaxSAT API" ✓ Recommended

| | |
|---|---|
| **What** | Sell Navokoj as a MaxSAT solver with optional proof-of-optimality (UNSAT core + assignment witness) |
| **Why** | Crowded field (MaxHS, SATLike, RC2) but our engine is competitive on speed/quality, and the proof artifact is a real differentiator |
| **Customer** | Decision optimization teams, scheduling, planning systems, ML feature selection |
| **Price** | Free tier → Pro $499/mo (500K clauses) → Enterprise $5K/mo+ (custom) |
| **12-mo ARR target** | $300K (60 enterprise customers, conservative) |

### Wedge B: "ZK Pre-Processor"

| | |
|---|---|
| **What** | Don't solve ZK. Be the best-in-class offline gadget that decomposes a ZK circuit into MaxSAT-shaped subproblems |
| **Why** | Every ZK project has a gadget bottleneck (hash functions, range proofs, lookups). We can be useful without being the proving system |
| **Customer** | ZK circuit engineers, snarkjs/gnark users, audit teams |
| **Price** | Per-circuit pricing, $50–$500 per decomposition |
| **12-mo ARR target** | $150K (low base, but real ZK $ flow) |

### Wedge C: "Hybrid AI Inference Routing"

| | |
|---|---|
| **What** | Local-search for fuzzy/cost-sensitive decisions, fallback to exact solver for verification |
| **Why** | Real demand, less crowded than pure MaxSAT, plays to the pro engine's strength |
| **Customer** | Robotics, real-time bidding, ad ranking, supply chain |
| **Price** | Usage-based, $0.01–$0.10 per call |
| **12-mo ARR target** | $500K (high if productized right, low if we can't get to <50ms p99) |

> **Recommendation:** Wedge A primary, Wedge B secondary. Kill Wedge C for now — it's a feature, not a company.

---

## 4. 12-Month Roadmap (Specific Bets, Dates)

### Q3 2026 (now → Sept)

- [ ] Ship **Wedge A MVP**. Position the API as MaxSAT-first, drop "ZK" from the homepage title
- [ ] **Engine improvement: mini correctness.** Audit the 99.77% → 99.9%+ claim. If can't get there, lower the marketing number honestly
- [ ] **Pricing:** Lock the $499 Pro tier. Add a $99/month dev tier (5K clauses, 1K req/hr) for indie users
- [ ] Hire: 1 DevRel, 1 Solutions Engineer
- [ ] **ARR target:** $20K (early enterprise pilots)

### Q4 2026

- [ ] Ship **Wedge B (ZK Pre-Processor)** as a sidecar product. Free tier of the solver for decomp; paid for the optimizer that actually re-encodes
- [ ] Add **verifiable-optimality proof artifacts** to the API response. This is the long-term moat
- [ ] Partner with one ZK framework (snarkjs or gnark) for a "use NitroSAT as preprocessor" integration
- [ ] Hire: 1 backend, 1 ZK engineer (joint with research)
- [ ] **ARR target:** $80K cumulative

### Q1 2027

- [ ] Launch enterprise tier with **on-prem deployment + SOC2** in flight
- [ ] **Open-source the engine core** (Apache 2.0) to drive adoption; keep the API and the proof artifacts as the commercial layer
- [ ] First paid pilot of the ZK preprocessor (target: a real ZK audit firm, ~$25K contract)
- [ ] **ARR target:** $250K cumulative

### Q2 2027

**Decision gate:** Do we re-enter ZK as primary? Requires:
- 100% verifiable solver (we're 40-60% of the way there based on mini audits)
- <1s p99 latency on depth-4-equivalent
- At least one paying ZK customer in production

- [ ] If yes: spin out "Shunyabar ZK" as a separate product line
- [ ] If no: stay MaxSAT
- [ ] **ARR target:** $500K cumulative

---

## 5. Kill List

Things we explicitly **are NOT** doing in the next 12 months:

| ❌ | Reason |
|---|---|
| Real-time crypto / wallet / signing applications | Latency floor too high, audit surface too big |
| Building our own ZK DSL | Circom, gnark, Noir, ZoKrates are crowded. We integrate, we don't compete |
| General SAT solving market | Z3, Kissat, CaDiCaL dominate and we're not catching up. We're MaxSAT, not SAT |
| Mobile / edge deployment | Engine footprint too big; we'd be shipping someone else's runtime anyway |
| Custom hardware acceleration | GPUs are a research play, not a 2027 product. Revisit in 2028 if ZK lights up |
| The "ZK with NitroSAT" framing on the homepage | Until we have a paying ZK customer. Stops misleading buyers |

---

## 6. Pricing & Tier Strategy

| Tier | Price | Limits | Target |
|------|-------|--------|--------|
| **Free** | $0 | 1K vars, 5K clauses, 100 req/hr | Hobbyists, evaluation |
| **Dev** | $99/mo | 10K vars, 50K clauses, 5K req/hr | Indie devs, small apps |
| **Pro** | $499/mo | 100K vars, 500K clauses, 50K req/hr | Startups, mid-market |
| **Enterprise** | Custom | Unlimited, on-prem optional | Large teams, regulated |

**API key throttling note:** Free tier 100 req/hr forces conversion but also blocks serious testing. Move to 500 req/hr for free to drive dev adoption. Gate Pro at $499 by clauses, not requests — enterprise pays for complexity, not volume.

**Proof artifacts:** Free tier gets assignment-only; Pro+ gets assignment + UNSAT proof certificate. This is the actual moat — don't give it away.

---

## 7. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| MaxSAT market commoditizes (MaxHS goes cloud, etc.) | Med | High | Open-source core; compete on proof artifacts + UX |
| ZK framing attracts wrong-fit customers | High | Med | Aggressively rebrand Q3; redirect ZK interest to preprocessor |
| Engine accuracy claims don't hold under audit | Med | Critical | Audit mini Q3; honest numbers if lower |
| Research team leaves or pivots | Low | Critical | Open-source the engine; reduce single-point-of-failure |
| Competitor ships 100% verifiable MaxSAT first | Med | High | Invest in proof artifacts NOW (Q3-Q4); this is the moat |
| Funding / runway | Med | Critical | Cut burn to <$50K/mo; target $300K ARR by end of 2027 |

---

## 8. The Single Most Important Thing

> **Get to 100% verifiable MaxSAT with a proof artifact in the API response.**

Everything else is positioning. This is the technical moat. If we have:
- **100% accuracy** (provable, not just measured)
- **<5s p99** on real instances
- **A certificate** the user can verify independently

…then we're the only game in town for high-stakes MaxSAT. ZK, audit, regulated industries all become adjacent.

If we don't get there, we're a fast MaxSAT API competing on price against free open-source tools. That's a bad place to be.

**Q3 engineering priority: proof-of-optimality artifact. Everything else is marketing.**

---

## 9. Honest Verdicts

1. **The ZK framing is hurting us.** It attracts customers we can't serve and dilutes our actual value prop. Cut it from the homepage in Q3.
2. **The engine is real but undersold.** The hybrid local-search + systematic architecture is novel. Open-source the core in Q1 2027 to drive adoption; the API + proof artifacts stay commercial.
3. **We're not a ZK company yet.** We might become one in 2028 if the technical moat (verifiable proofs) lands. Until then, lean into MaxSAT and don't pretend otherwise.
4. **Hiring is critical and we can't do it wrong.** First 3 hires: Solutions Engineer (sells Pro tier), DevRel (community + open-source), ZK engineer (part-time until ZK wedge is validated).
5. **The depth-4 Merkle result is research, not product.** It proved we understand the failure mode (exactly-one constraints, not the mult chain). That's valuable IP. But nobody's paying for it.

---

*Assumptions: 1 founder + 4 hires by Q4, $300K seed extension in Q3, runway through Q2 2027.*
