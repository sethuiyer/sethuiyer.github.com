# Verifiable MaxSAT for Hard Planning Problems

ShunyaBar Labs builds **constraint-solving tools that come with proof**. Our flagship product, [Navokoj](https://navokoj.shunyabar.foo), is a MaxSAT API that returns the best possible answer — and the mathematical evidence to back it up.

---

## What we solve

Every day, enterprises solve constraint-satisfaction problems under hard time pressure:

| Problem | Why it's hard | What we do |
|---|---|---|
| **Scheduling 10,000 nurses across three shifts** | Contract rules, fairness constraints, last-minute sick calls | Lock the parts that already work, repair only what changed — in milliseconds |
| **Routing 5,000 vehicles with delivery windows** | Time windows, vehicle capacity, traffic disruption | Preserve promised delivery slots, adjust only affected routes |
| **Placing 100,000 VMs on a GPU cluster** | Affinity rules, hardware fit, live-migration cost | Find a feasible placement in seconds with a certificate you can audit |

These are all [MaxSAT](glossary.md) problems. Classical solvers find good answers; we return the best answer **with proof you can verify offline**.

---

## Why us

1. **Verifiable, not just fast.** Every Pro+ response includes a structured proof artifact. Our verifier is [open source](glossary.md#verification--trust). You don't trust us — you check.

2. **Lock-preserving repair.** When the world changes (a truck breaks down, a nurse calls in sick), we don't restart from scratch. We preserve the parts that already work and repair only what changed. **847× faster than full recomputation.**

3. **Honest numbers.** Where our solver works, we tell you. Where it doesn't, [we tell you that too](limitations.md). We benchmark against certified optimal solutions and report the gaps.

---

## Results

### Academic benchmarks (peer-reviewed, academic test suites)

| What we solve | Real-world test | What that means for you |
|---|---|---|
| **Scheduling** | University timetabling — 147K variables, 80M clauses | 100% solved in 73 seconds. Schedules a full university in under two minutes. |
| **Hardware verification** | 512×512 multiplier circuit — 788K variables | 100% correct in 5.9 seconds. Replaces hours of formal-verification work. |
| **Combinatorial search** | R(5,5,5) Ramsey problem — N=52 | Solved with zero errors in 5.6 seconds. A benchmark most SAT solvers can't crack. |
| **Fluid simulation** | 2D Navier-Stokes equations | 99.64% residual reduction, **100,000× faster than traditional CFD**. |
| **Incremental repair** | CPU task scheduling under disruption | 847×–12,495× faster than recomputing from scratch, with 95%+ of prior decisions preserved. |
| **Local search** | 64-spin frustrated spin glass | 4,169% better than standard simulated annealing on hard energy landscapes. |

### Production performance (live API, 2026-04-04 → 2026-06-19)

> **The headline:** Across **308 production runs**, NitroSAT processed **3.98M clauses** with **median satisfaction 1.0** and **median solve time 65.5 ms**.

| What we solve | Production test | What that means for you |
|---|---|---|
| **Massive clause-density problems** | 10K vars / **1.65M clauses** / clause-var ratio 165× | 100% perfect satisfaction in 278 seconds. The largest clause-density instance ever recorded in production. |
| **Sub-second structural solves** | 2.5K vars / 122K clauses / clause-var ratio 49× | **0.296 seconds**, perfect satisfaction. The "excuse-me-what" datapoint. |
| **Massive variable count** | 49K vars / 73.5K clauses | 100% perfect satisfaction in 0.291 seconds. Production workloads at 49K-variable scale. |
| **Quality at scale** | 308 runs, 79.87% at ≥99% satisfaction | Almost 4 out of 5 production calls reach 99%+ satisfaction. |

### Research breakthroughs (GitHub repo, Jan–Apr 2026)

| What we solve | Research test | What that means for you |
|---|---|---|
| **Edwards-Anderson 3D spin glass** | 40×40×40 lattice — 64,000 fully-coupled frustrated spins | **99.47% satisfaction in 4.3 seconds.** First gradient-based solver to crack EA-3D at this scale. |
| **v1 → v2 generational leap** | 80M-clause enterprise timetabling | **5.2 hours → 73 seconds (250× speedup)** from algorithmic changes alone, on the same laptop. |
| **Titan Ramsey R(5,5)** | 780 vars, 1.32M clauses, density α=1,687 | 99.995% satisfaction in 3,403s. Each variable appears in ~1,687 clauses. |
| **CDCL adversarial trap** | pit.cnf — 2,950 vars, 1.05M clauses | 100% perfect in ~400s. Solves a formula engineered to break CDCL. |
| **Prime weighting ablation** | clique_4_20 (structured geometry) | 3.4× faster than uniform weighting; topological cycles drop from 79 to 20. |

Full benchmark methodology: [research report](research-report.md) · [NitroSAT production ledger](projects/nitrosat.md) · [GitHub benchmark heritage](https://github.com/sethuiyer/NitroSAT/blob/main/benchmarks/README.md) · [Limitations](limitations.md)

---

## How it works (in one paragraph)

Every constraint in your problem gets a unique weight derived from a prime number. No two constraints compete for the same gradient signal, so the solver can navigate hard landscapes without getting stuck. The same five ideas — prime weighting, multiplicative loss, phase-transition detection, partition functions, and a stability condition rooted in the Riemann Hypothesis — show up across every project we ship. For the full theory, see [The Arithmetic Manifold](core-vision.md).

---

## Pricing

Start free. Pay when you scale.

| Tier | Price | What you get |
|---|---|---|
| **Free** | $0 | 1K vars, 5K clauses, 500 req/hr — hobbyists and CI |
| **Dev** | $99/mo | 10K vars, 50K clauses, 5K req/hr — indie devs |
| **Pro** | $499/mo | 100K vars, 500K clauses, 50K req/hr, **proof artifacts included** |
| **Enterprise** | Custom ($5K+/mo) | Unlimited, on-prem optional, SOC2 in flight |

Full pricing details: [pricing.md](marketing/pricing.md)

---

## Use cases

We have detailed pages for the verticals where Navokoj is strongest:

- [Logistics & transportation](marketing/use-cases.md#1-logistics--transportation)
- [Healthcare workforce scheduling](marketing/use-cases.md#2-healthcare-workforce-scheduling)
- [Cloud infrastructure & DevOps](marketing/use-cases.md#3-cloud-infrastructure--devops)
- [Financial services](marketing/use-cases.md#4-financial-services)
- [Telecom & spectrum](marketing/use-cases.md#5-telecom--spectrum)
- [Manufacturing & supply chain](marketing/use-cases.md#6-manufacturing--supply-chain)

---

## For the technical reader

| If you want to… | Read this |
|---|---|
| Understand the math behind the engine | [Core Vision: The Arithmetic Manifold](core-vision.md) |
| Read the rigorous research paper | [Axiom Architecture essay](axiom-architecture.md) |
| See the unified systems report | [Research report](research-report.md) |
| Call the API | [Quick Start Guide](getting-started/quick-start.md) · [Lua Module Reference](getting-started/lua-module.md) |
| Look up a term | [Glossary](glossary.md) |
| Understand our limits | [Where the solver works (and where it doesn't)](limitations.md) |
| See our roadmap and pricing strategy | [Product Strategy, H2 2026](product-strategy.md) · [Roadmap](TODO.md) |
| Understand why our sites look different | [The Design Philosophy](design-philosophy.md) |

---

## Each project has its own live site

| Project | URL |
|---|---|
| **Navokoj** (Production API) | [navokoj.shunyabar.foo](https://navokoj.shunyabar.foo) |
| **BAHA** | [sethuiyer.github.io/baha](https://sethuiyer.github.io/baha) |
| **NitroSAT** | [sethuiyer.github.io/NitroSAT](https://sethuiyer.github.io/NitroSAT) |
| **Multiplicative PINN** | [sethuiyer.github.io/multiplicative-pinn-framework](https://sethuiyer.github.io/multiplicative-pinn-framework) |
| **Spectral-Multiplicative** | [sethuiyer.github.io/spectral-multiplicative-framework](https://sethuiyer.github.io/spectral-multiplicative-framework) |
| **Geometry of Conditional Logic** | [sethuiyer.github.io/geometry-of-conditional-logic](https://sethuiyer.github.io/geometry-of-conditional-logic) |
| **Casimir SAT Solver** | [sethuiyer.github.io/casimir-sat-solver](https://sethuiyer.github.io/casimir-sat-solver) |
| **Factor Agent** | [sethuiyer.github.io/factor-agent](https://sethuiyer.github.io/factor-agent) |
| **Thermodynamic Number Line** | [sethuiyer.github.io/thermodynamic-number-line](https://sethuiyer.github.io/thermodynamic-number-line) |
| **Authorization Lattice** | [sethuiyer.github.io/authorization-lattice](https://sethuiyer.github.io/authorization-lattice) |

---

## See Also

- [Concepts: Prime Weighting](concepts/prime-weighting.md) · [Partition Function](concepts/partition-function.md) · [Multiplicative vs Additive](concepts/multiplicative-vs-additive.md) · [Phase Transitions](concepts/phase-transitions.md) · [Riemann Hypothesis](concepts/riemann-hypothesis.md)
- [Projects Overview](projects/index.md) — all 10 projects mapped
- [Marketing: Why Navokoj](marketing/index.md) · [Use Cases](marketing/use-cases.md) · [Pricing](marketing/pricing.md) · [Results](marketing/results.md)
- [Design Philosophy](design-philosophy.md) — why our surfaces look different
- [Product Strategy](product-strategy.md) · [Roadmap](TODO.md) — H2 2026 plan