# Roadmap: ShunyaBar Labs, H2 2026

> Based on CPO Product Strategy (June 2026). Primary focus: Wedge A (Verifiable MaxSAT API), Secondary: Wedge B (ZK Pre-Processor).

---

## Phase 1: Q3 2026 — Ship Wedge A MVP

### Marketing & Positioning
- [ ] **Drop "ZK" from homepage title** — we're MaxSAT, not ZK
- [ ] Rewrite homepage copy: "Verifiable MaxSAT API" not "constraint intelligence"
- [ ] Create Wedge A landing page (Verifiable MaxSAT)
- [ ] Create Wedge B teaser page (ZK Pre-Processor — "coming Q4")

### Product
- [ ] **Add Dev tier: $99/mo** (10K vars, 50K clauses, 5K req/hr)
- [ ] **Lock Pro tier at $499/mo** (100K vars, 500K clauses, 50K req/hr)
- [ ] Move free tier from 100 req/hr → 500 req/hr

### Engineering
- [ ] **Audit mini engine correctness** — 99.77% → 99.9%+? If not achievable, lower the number honestly
- [ ] **Proof-of-optimality artifact** — UNSAT core + assignment witness in API response (this is the moat)
- [ ] Stabilize zk_binary_v2.py SDK — replace brute-force forbidden-combination enumeration

### Research
- [ ] Submit EA 3D paper (Physical Review E or ML venue)

### Sales
- [ ] First 3 paying enterprise pilots ($5K-$20K contracts)
- [ ] Target: decision optimization teams, scheduling, ML feature selection

**ARR target: $20K by Sept 2026**

---

## Phase 2: Q4 2026 — Ship Wedge B

### Product
- [ ] **ZK Pre-Processor sidecar** — free for decomposition, paid for re-encoding optimizer
- [ ] Per-circuit pricing: $50–$500 per decomposition
- [ ] Partner integration: snarkjs or gnark "use NitroSAT as preprocessor"

### Engineering
- [ ] **Verifiable-optimality proof artifacts** in API response (if not shipped in Q3)
- [ ] Optimize /v1/schedule for monthly/quarterly horizons
- [ ] On-prem Docker container (beta)

### Sales
- [ ] First paid ZK preprocessor contract ($5K-$25K)
- [ ] 10 enterprise customers on Pro tier

**ARR target: $80K cumulative by Dec 2026**

---

## Phase 3: Q1 2027 — Enterprise + Open Source

### Product
- [ ] **Enterprise tier launch** — on-prem + SOC2 in flight
- [ ] **Open-source engine core** (Apache 2.0) — API + proof artifacts stay commercial
- [ ] Proof artifact verification library (open source)

### Engineering
- [ ] Metered billing API
- [ ] SSO & RBAC
- [ ] Audit logs (compliance)

### Sales
- [ ] First paid ZK audit firm pilot (~$25K contract)

**ARR target: $250K cumulative by Mar 2027**

---

## Phase 4: Q2 2027 — Decision Gate

### ZK Re-Entry Decision (Requires ALL of):
- [ ] 100% verifiable solver (mini audit shows we're 40-60% there)
- [ ] <1s p99 latency on depth-4-equivalent
- [ ] At least one paying ZK customer in production

**If yes:** Spin out "Shunyabar ZK" as separate product line
**If no:** Stay MaxSAT; revisit ZK in 2028

### Hiring Plan
1. Solutions Engineer (sales-engineering hybrid)
2. DevRel (community + open-source)
3. Backend engineer
4. ZK engineer (part-time until ZK validated)

**ARR target: $500K cumulative by Jun 2027**

---

## Kill List (12 months)

| Do NOT do | Why |
|-----------|-----|
| Real-time crypto / wallet / signing | Latency + audit surface |
| Build ZK DSL | Circom/gnark/Noir own this |
| General SAT market | Z3/Kissat/CaDiCaL dominate |
| Mobile / edge deployment | Engine footprint too big |
| Custom hardware (GPUs) | Research play, not 2027 product |
| ZK homepage framing | Until paying ZK customer exists |

---

## Current vs Target Pricing

| Tier | Current | Target |
|------|---------|--------|
| Free | $0 (100 req/hr) | $0 (500 req/hr) |
| Dev | — | $99/mo |
| Pro | $0.25 + $0.10/min | $499/mo |
| Enterprise | $100/mo + $10/hr | Custom $5K+/mo |

---

## What We Shipped (Pre-Strategy)

| Item | Status |
|------|--------|
| MATH.md (886 lines, rigorous) | Done |
| Limitations & Boundaries page | Done |
| Remove "beats Kissat" claims | Done |
| Fix 2^1024 XOR framing | Done |
| CDCL honest comparison (anytime vs exact) | Done |
| Industrial-Scale results (80M-clause, EA 3D, MSE 2022) | Done |
| CSS improvements (code, tables, math, links, sidebar) | Done |
| Project pages with live URLs | Done |
| Product Strategy document | Done |

---

*The ZK story is a 2027+ bet. The MaxSAT story is now.*
