# ShunyaBar Labs

ShunyaBar Labs is a research program exploring **the Arithmetic Manifold** — a unified framework connecting physics-inspired optimization, number theory, and constraint satisfaction.

---

## The Core Insight

> Hard computational problems (SAT, scheduling, PDEs, neural network constraints) share a common structure: they exhibit **phase transitions** with **spectral signatures**. These signatures can be detected, navigated, and exploited through **prime-weighted operators** and **multiplicative dynamics**.

The key insight: **primes are the irreducible atoms of both arithmetic and constraint satisfaction**. Their multiplicative independence (guaranteed by the Fundamental Theorem of Arithmetic) provides unique spectral signatures for each constraint. Their asymptotic distribution (governed by the Riemann Hypothesis) determines whether gradient flow on the constraint manifold remains stable or collapses.

---

## The Project Family

```
┌─────────────────────────────────────────────────────────────────────┐
│                      THE ARITHMETIC MANIFOLD                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐   │
│   │    BAHA     │  │  NitroSAT   │  │   Spectral-Multiplic.   │   │
│   │  Lambert W  │  │   Physics-  │  │   Crystal Heat Kernel   │   │
│   │  Phase Trans│  │  informed   │  │   + Casimir Forces      │   │
│   └──────┬──────┘  └──────┬──────┘  └────────────┬────────────┘   │
│          │                │                        │                 │
│          └────────────────┼────────────────────────┘               │
│                           │                                          │
│                    ┌──────▼──────┐                                  │
│                    │   Navokoj   │  Geometric Flow SAT Framework    │
│                    └──────┬──────┘                                  │
│                           │                                          │
│          ┌─────────────────┼─────────────────┐                       │
│          │                 │                 │                       │
│   ┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐               │
│   │ Multiplic.  │  │    CRT      │  │   Casimir   │               │
│   │    PINN     │  │Incremental  │  │     SAT     │               │
│   └─────────────┘  └─────────────┘  └─────────────┘               │
│                                                                     │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐   │
│   │   Factor    │  │ Thermodyn.  │  │    Authorization        │   │
│   │   Agent     │  │   Number    │  │       Lattice           │   │
│   │   (Multi-   │  │   Line     │  │   (Capabilities as     │   │
│   │   Agent)    │  │  Primes+RH  │  │    p-adic numbers)     │   │
│   └─────────────┘  └─────────────┘  └─────────────────────────┘   │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                      shunyabar.lua                          │  │
│   │            Unified Lua Module (all algorithms)              │  │
│   └─────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Key Results

| Project | Problem | Result |
|---------|---------|--------|
| **BAHA** | Hardness detection + optimization | 84% pass rate across 26 domains; 4169% better than SA on Spin Glass |
| **NitroSAT** | MaxSAT solving | 77% perfect satisfaction on 5,000+ CNF instances; 100% on 788K-var hardware check |
| **Navokoj** | Geometric flow SAT | 99.4% on 3-SAT at critical density; 100% on graph coloring |
| **Multiplicative PINN** | Physics neural networks | 99.64% residual reduction; 100,000x speedup over CFD |
| **Spectral-Multiplicative** | Graph partitioning | 100% constraint satisfaction; $1.4M/year cost savings |
| **Geometry of Conditional Logic** | Incremental repair | 847x faster repair vs full restart |

---

## The Five Pillars

1. **Partition Function Z(β)** — Universal object across all projects; monitors ρ = |d/dβ log Z| to detect landscape fractures

2. **Prime Weighting** — Each constraint receives unique weight W(p) = 1/(1+ln p); guarantees no gradient resonance

3. **Multiplicative Dynamics** — Euler product structure replaces additive penalties; eliminates gradient conflicts

4. **Phase Transitions** — Lambert W function governs bifurcation between convex/non-convex regimes

5. **Riemann Hypothesis** — Embedded as stability condition; asymptotic stability requires σ → 1/2

---

## Project Websites

Each project has its own live website:

| Project | Website |
|---------|---------|
| **Navokoj** (Production API) | [navokoj.shunyabar.foo](https://navokoj.shunyabar.foo) |
| **BAHA** | [sethuiyer.github.io/baha](https://sethuiyer.github.io/baha) |
| **NitroSAT** | [sethuiyer.github.io/NitroSAT](https://sethuiyer.github.io/NitroSAT) |
| **Multiplicative PINN** | [sethuiyer.github.io/multiplicative-pinn-framework](https://sethuiyer.github.io/multiplicative-pinn-framework) |
| **Spectral Multiplicative** | [sethuiyer.github.io/spectral-multiplicative-framework](https://sethuiyer.github.io/spectral-multiplicative-framework) |
| **Geometry of Conditional Logic** | [sethuiyer.github.io/geometry-of-conditional-logic](https://sethuiyer.github.io/geometry-of-conditional-logic) |
| **Casimir SAT Solver** | [sethuiyer.github.io/casimir-sat-solver](https://sethuiyer.github.io/casimir-sat-solver) |
| **Factor Agent** | [sethuiyer.github.io/factor-agent](https://sethuiyer.github.io/factor-agent) |
| **Thermodynamic Number Line** | [sethuiyer.github.io/thermodynamic-number-line](https://sethuiyer.github.io/thermodynamic-number-line) |
| **Authorization Lattice** | [sethuiyer.github.io/authorization-lattice](https://sethuiyer.github.io/authorization-lattice) |

---

## Quick Links

- [Core Vision: The Arithmetic Manifold](core-vision.md)
- [Quick Start Guide](getting-started/quick-start.md)
- [Lua Module Reference](getting-started/lua-module.md)
- [Benchmarks](getting-started/benchmarks.md)
