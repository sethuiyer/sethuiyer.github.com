# Roadmap: Post-Funding TODO

> This document captures planned work for after external funding.
> Current focus: shipping the product, growing revenue, publishing research.

---

## Priority: High

### Marketing & Documentation

- [ ] **Rewrite blog post** with honest positioning: drop "beats Kissat", fix 2^1024 framing, emphasize deterministic + structured + anytime
- [ ] **Create ZK Circuit Auditing wedge page** — soundness verification for under-constrained circuits, not witness generation
- [ ] **Create Timetabling Middleware wedge page** — ERP integration, 80M-clause proof point
- [ ] **Create Real-Time Agent Orchestration wedge page** — inline policy enforcement for AI agents

### Pricing

- [ ] Raise **Pro tier to $199/mo** (currently $0.25 + $0.10/min)
- [ ] Raise **Enterprise tier to $1,999/mo** (currently $100/mo base + $10/hr)
- [ ] Add **ZK Audit seat license**: $1,500/mo or $5,000 per audit run

### Engineering

- [ ] **Stabilize zk_binary_v2.py SDK** — replace brute-force forbidden-combination enumeration
- [ ] **Integrate PySAT primitives** for Wallace-tree / lookup table compilation pipeline
- [ ] **Rewrite boolean expression parser** for infinite nesting (fix stack overflow)
- [ ] **Optimize /v1/schedule** for monthly/quarterly planning horizons

---

## Priority: Medium

### Engineering

- [ ] **Metered billing API** — pay-per-solve with accurate usage tracking
- [ ] **On-Prem / VPC deployment** — Docker container for defense, healthcare, fintech
- [ ] **Implement SSO & RBAC** — granular control over problem submission and diagnostics
- [ ] **Audit Logs** — immutable logs of every constraint solved (compliance)
- [ ] **SLA Guarantees** — contractually guaranteed 99.99% uptime for Enterprise

### SDK Ecosystem

- [ ] **Official Go SDK** — maintained client library
- [ ] **Official Rust SDK** — maintained client library
- [ ] Maintain **Python SDK** — keep current client up to date

---

## Priority: Low

### Sales

- [ ] Cold outreach to **5 ZK teams** (Polygon, StarkWare, Risc Zero, Succinct, Aztec)
- [ ] Cold outreach to **5 scheduling teams** (universities, hospitals, logistics)
- [ ] **Free optimization audit** offer: "reduce compute by 30% or pay nothing"

---

## Research (Funded by Credibility)

- [ ] **Publish EA 3D paper** — 64K spins at 99.47% in 4.3s
  - Target venues: NeurIPS, ICML, Physical Review E
  - Claim: "First gradient-based solver to crack Edwards-Anderson 3D at scale"

---

## What We Shipped (Pre-Funding)

| Item | Status |
|------|--------|
| MATH.md (continuous relaxation + Wasserstein flow) | Done |
| Limitations & Boundaries page | Done |
| Remove "beats Kissat" claims | Done |
| Fix 2^1024 XOR framing | Done |
| CDCL comparison honest (anytime vs exact) | Done |
| Industrial-Scale results section (80M-clause, EA 3D, MSE 2022) | Done |
| CSS improvements (code blocks, tables, math, links, sidebar) | Done |
| Project pages with live URLs | Done |

---

*Last updated: June 2026*
