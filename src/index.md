<div class="sb-thesis-title">
<h1>ShunyaBar Labs</h1>
<p class="sb-subtitle">The Arithmetic Manifold</p>
<p class="sb-tagline">Constraint is the engine.</p>
</div>

<div class="sb-abstract">

We build constraint-solving tools that come with proof. Our work unifies ideas from analytic number theory, statistical mechanics, and category theory into a single framework — the **Arithmetic Manifold** — and ships them as production [MaxSAT](glossary.md) solvers. Every constraint gets a unique prime-derived weight; every solver is a physical instrument whose stability threshold coincides with the Riemann critical line.

</div>

---

## Key Results

| Area | Result | What it means |
|---|---|---|
| **Prime Weighting** | 3.4–4× speedup; topological cycles 79 → 20 | No two constraints compete for the same gradient signal |
| **Enterprise Timetabling** | 80M clauses, 100% in 73 seconds | 250× faster than v1 (5.2 hours → 73s, same laptop) |
| **Production MaxSAT** | 3.98M clauses, 308 runs, median 65.5ms | 54% perfect solves, 80% at ≥99% satisfaction |
| **Edwards-Anderson 3D** | 64K frustrated spins, 99.47% in 4.3s | First gradient-based solver at this scale |
| **Titan Ramsey R(5,5)** | 780 vars, 1.32M clauses, α=1687 | 99.995% satisfaction — each variable in ~1687 clauses |
| **CDCL Trap (pit.cnf)** | 2,950 vars, 1.05M clauses | 100% perfect — solves formulas engineered to break CDCL |

Full methodology: [research report](research-report.md) · [production ledger](projects/nitrosat.md) · [limitations](limitations.md)

Launch context: [Navokoj in production](blog/navokoj-launch.md) explains how the Arithmetic Manifold maps into the public API and solver tiers.

---

## Projects

| Project | Description |
|---|---|
| [**NitroSAT**](projects/nitrosat.md) | Physics-informed continuous-relaxation MaxSAT solver |
| [**Navokoj**](projects/navokoj.md) | Production MaxSAT API with proof artifacts |
| [**BAHA**](projects/baha.md) | Fracture detection via Lambert W / thermal signal analysis |
| [**Multiplicative PINN**](projects/multiplicative-pinn.md) | PINNs with prime-weighted multiplicative loss |
| [**Spectral-Multiplicative**](projects/spectral-multiplicative.md) | Spectral graph methods + multiplicative optimization |
| [**Geometry of Conditional Logic**](projects/geometry-of-conditional-logic.md) | Spatial embeddings of logical conditionals |
| [**Casimir SAT Solver**](projects/casimir-sat-solver.md) | SAT solving via vacuum energy analogy |
| [**Factor Agent**](projects/factor-agent.md) | LLM agent with certified tool-use via MaxSAT |
| [**Thermodynamic Number Line**](projects/thermodynamic-number-line.md) | Primes as thermodynamic fuel |
| [**Authorization Lattice**](projects/authorization-lattice.md) | Lattice-based access control with MaxSAT verification |

---

## Pricing

| Tier | Price | Limits |
|---|---|---|
| **Free** | $0 | 1K vars, 5K clauses, 500 req/hr |
| **Dev** | $99/mo | 10K vars, 50K clauses, 5K req/hr |
| **Pro** | $499/mo | 100K vars, 500K clauses, 50K req/hr, proof artifacts |
| **Enterprise** | Custom ($5K+/mo) | Unlimited, on-prem, SOC2 in flight |

Details: [pricing](marketing/pricing.md) · [use cases](marketing/use-cases.md) · [benchmarks](getting-started/benchmarks.md)

---

## For the Technical Reader

| If you want to… | Start here |
|---|---|
| Understand the math | [Core Vision: The Arithmetic Manifold](core-vision.md) |
| Read the rigorous paper | [Axiom Architecture essay](axiom-architecture.md) |
| See the unified report | [Research report](research-report.md) |
| Call the API | [Quick Start Guide](getting-started/quick-start.md) |
| Understand our limits | [Where it works (and where it doesn't)](limitations.md) |
| See the roadmap | [Product Strategy](product-strategy.md) · [TODO](TODO.md) |
| Why our surfaces look different | [The Design Philosophy](design-philosophy.md) |

---

## See Also

- [Prime Weighting](concepts/prime-weighting.md) · [Partition Function](concepts/partition-function.md) · [Multiplicative vs Additive](concepts/multiplicative-vs-additive.md) · [Phase Transitions](concepts/phase-transitions.md) · [Riemann Hypothesis](concepts/riemann-hypothesis.md) · [Asymptotically Fair Stopping](concepts/asymptotically-fair-stopping.md)
- [All Projects](projects/index.md) · [Why Navokoj](marketing/index.md) · [Glossary](glossary.md)
- [Navokoj Launch](blog/navokoj-launch.md) · [Navokoj Developer Guide](navokoj/index.md) · [Pricing](marketing/pricing.md)
