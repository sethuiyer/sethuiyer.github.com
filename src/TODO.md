# Roadmap: ShunyaBar Labs, H2 2026

> Based on CPO Product Strategy v2 (June 2026). Primary: Wedge A (Verifiable MaxSAT API). Secondary: Wedge B (ZK Pre-Processor). Kill: Wedge C.

---

## Critical Fixes (Schema Bugs)

- [ ] **Integer weights only** — float weights invalidate dual-bound theory. Document this in API docs.
- [ ] **Derivation graphs, not strings** — `resolution_chain` must be structured (clause IDs + resolution steps), not English text.
- [ ] **Infeasibility case** — Add `satisfiable: false` response with hard-clause UNSAT core and derivation. Clients must distinguish "optimal" from "infeasible" from "engine gave up."

---

## Phase 1: Q3 2026 — Revenue First

### Human Moves (Priority Over Engineering)

- [ ] **3 design partner LOIs signed** by Sept 30
  - 1 scheduling / timetabling ($5K–$20K)
  - 1 ML feature selection ($5K)
  - 1 ZK preprocessor evaluation (free → paid)
- [ ] **Pilot template ready** — problem, success criteria, timeline, payment terms, IP clause
- [ ] **First hire: Solutions Engineer** — starts Q3 week 1
  - 30-day mandate: prospect list, pilot template, 10 outreach calls

### Marketing & Positioning

- [ ] **Drop "ZK" from homepage** — MaxSAT-first
- [ ] Rewrite homepage copy: "Verifiable MaxSAT API" not "constraint intelligence"
- [ ] Create Wedge A landing page (Verifiable MaxSAT)
- [ ] Wedge B teaser page ("ZK Pre-Processor — coming Q4")

### Product

- [ ] **Fix API schema** — integer weights, derivation graphs, infeasibility case
- [ ] **Dev tier: $99/mo** (10K vars, 50K clauses, 5K req/hr)
- [ ] **Pro tier: $499/mo** (100K vars, 500K clauses, 50K req/hr)
- [ ] Free tier: 100 req/hr → **500 req/hr**

### Engineering

- [ ] Audit mini engine correctness — 99.77% → 99.9%+? If not, lower the number honestly.
- [ ] Stabilize zk_binary_v2.py SDK

### Research

- [ ] Submit EA 3D paper (Physical Review E or ML venue)

**ARR target: $20K by Sept 2026**

---

## Phase 2: Q4 2026 — Ship Wedge B + Proof Artifacts

### Product

- [ ] **ZK Pre-Processor sidecar** — free decomposition, paid re-encoding optimizer
- [ ] Per-circuit pricing: $50–$500
- [ ] Partner integration: snarkjs or gnark "use NitroSAT as preprocessor"
- [ ] **Proof-of-optimality artifact** in API response (UNSAT cores + derivation graph)

### Open Source

- [ ] **Open-source verifier + proof format spec** (Apache 2.0)
  - Proof format JSON schema
  - Verifier implementation
  - Example clients
  - Download + run offline = independent verification

### Engineering

- [ ] Optimize /v1/schedule for monthly/quarterly horizons
- [ ] On-prem Docker container (beta)

### Hiring

- [ ] **Second hire: DevRel** — open-source community, SDK docs, 3 posts

**ARR target: $80K cumulative by Dec 2026**

---

## Phase 3: Q1 2027 — Enterprise + Open Core

### Product

- [ ] **Enterprise tier launch** — on-prem + SOC2 in flight
- [ ] **Open-source engine core** (Apache 2.0) — parsing, CNF/XOR, basic local-search loop
  - Closed layer: proof generation tuning, telemetry, RBAC, audit logging, ZK heuristics
- [ ] Proof artifact verification library (open source)

### Engineering

- [ ] Metered billing API
- [ ] SSO & RBAC
- [ ] Audit logs

### Sales

- [ ] First paid ZK audit firm pilot (~$25K contract)

**ARR target: $250K cumulative by Mar 2027**

---

## Phase 4: Q2 2027 — Decision Gate

### ZK Re-Entry (Requires ALL of):

- [ ] 100% verifiable solver (mini audit: 40-60% there today)
- [ ] <1s p99 latency on depth-4-equivalent
- [ ] At least one paying ZK customer in production

**If yes:** Spin out "Shunyabar ZK" as separate product line
**If no:** Stay MaxSAT; revisit ZK in 2028

### Hiring (Full Team)

1. Solutions Engineer (Q3 — first hire)
2. DevRel (Q4)
3. Backend Engineer (Q4)
4. ZK Engineer (Q1 2027 — only if ZK wedge validated)

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
| Wedge C (Agent Guardrails) | CENTS test failed — kill it |
| Hire ZK engineer in Q3 | Premature — ZK wedge not validated |

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
| CENTS test table | Done |
| Proof-of-optimality API schema (integer weights, derivation graphs, infeasibility case) | Done |
| Corrected open-source split (open verifier, closed proof generation) | Done |
| Hiring sequence + pilot template | Done |

---

*Revenue first. LOIs before artifacts. Open-source verifier. Ship the vehicle, not just the engine.*
