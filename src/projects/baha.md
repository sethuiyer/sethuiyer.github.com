# BAHA: Branch-Aware Holonomy Annealing

## What It Solves

Simulated annealing gets stuck in local minima because it treats the solution landscape as one smooth surface. BAHA detects when the landscape **fractures** (thermodynamic fracture) and uses complex-plane branch enumeration to jump to entirely different solution basins.

## Key Innovation

**Thermodynamic Fracture Detection**: BAHA monitors $\rho(\beta) = |d/d\beta \ln Z|$ to detect when the landscape shatters into multiple disconnected basins.

**Lambert W Branch Enumeration**: When fracture is detected, BAHA uses both $W_0$ (principal) and $W_{-1}$ (secondary) branches of the Lambert W function to enumerate new basins and jump selectively.

**Why it works**: The ln K / ln ln K scaling of the phase transition is a fingerprint of prime-weighted systems. No other weighting function produces this exact asymptotic.

## Architecture

```
FractureDetector
├── Monitors: β-history, log Z history
├── Computes: ρ(β) = |d/dβ log Z|
└── Flags when: ρ > threshold

LambertWOptimizer
├── Computes: K* = exp(-C·W(-1/C))
├── Enumerates: W₀ and W₋₁ branches
└── Jumps to: New basin estimated via Monte Carlo

BranchAwareOptimizer
├── Estimates: log Z via Monte Carlo
├── Scores: Each branch by fitness
└── Selects: Jump to highest-scoring basin
```

## Results

| Benchmark | BAHA | Simulated Annealing | Improvement |
|-----------|------|---------------------|-------------|
| Spin Glass (64 spins) | 100% | 6% | **4169%** |
| Graph Isomorphism (N=50) | 100% | 40% | **60% absolute** |
| Overall pass rate | **84%** | — | across 26 problem domains |

## Key Files

- `baha/README.md` — Overview and quick start
- `baha/docs/README.md` — Detailed documentation
- `shunyabar.lua/src/shunyabar.lua` — Lua implementation (lines 196-500)

## Connection to Core Vision

BAHA is the **phase transition engine** of the Arithmetic Manifold. It detects when the landscape fractures (via $\rho(\beta)$) and provides the navigation mechanism (Lambert W branches) to escape. All other algorithms use BAHA or a BAHA-like detection when operating near criticality.
