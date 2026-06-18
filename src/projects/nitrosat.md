# NitroSAT: Physics-Informed MaxSAT Solver

## What It Solves

High-performance maximum satisfiability (MaxSAT) solving with O(M) linear time complexity. Handles massive CNF instances (100K+ variables) where traditional solvers fail.

## Key Innovation

NitroSAT maps Boolean satisfiability to a **physics-informed dynamical system on a Riemannian manifold**:

1. **Continuous Relaxation**: Maps Boolean variables to continuous values in [0,1]
2. **Prime Weighting**: Number-theoretic clause weights via Prime Number Theorem
3. **Heat Kernel Diffusion**: Spectral smoothing via $\exp(t\Delta)$
4. **BAHA**: Lambert W function for phase transitions
5. **Persistent Homology**: Tracks Betti numbers to guide repair
6. **NADAM Optimization**: Nesterov-accelerated adaptive moment estimation

### The Metric

Uses the **Inverted Poincaré Disk** metric:

$$ds^2 = \frac{4|dz|^2}{(|z|^2(1-|z|^2)^2)}$$

This provides a natural geometry for probability-valued variables.

### Free Energy

$$F[x] = \lambda E_{kin}[x] + E_{pot}[x] - \frac{1}{\beta}S[x]$$

Gradient flow:

$$\frac{\partial x}{\partial t} = -\frac{\delta F}{\delta x}$$

## Results

| Instance | Variables | Clauses | Result | Time |
|----------|-----------|---------|--------|------|
| Planted Coloring | 105K | 232K | SAT (100%) | 13.78s |
| Hardware Verification | 788,480 | — | SAT (100%) | 5.92s |
| Random CNF (5000+ instances) | Various | Various | **77% perfect SAT** | — |
| Median satisfaction | — | — | **99.7%** | — |

## Key Files

- `NitroSAT/README.md` — Overview
- `NitroSAT/docs/MATH.md` — Mathematical foundations
- DOI: [10.5281/zenodo.18753235](https://doi.org/10.5281/zenodo.18753235)

## Connection to Core Vision

NitroSAT is the **flagship implementation** of the Arithmetic Manifold. It combines:
- Prime weighting (from partition function theory)
- Phase transition detection (BAHA/Lambert W)
- Riemann Hypothesis embedding (asymptotic stability condition)

> "NitroSAT does not prove the Riemann Hypothesis. But it embeds RH as a phase boundary: the solver functions as a physical instrument whose asymptotic stability threshold coincides exactly with the critical line Re(s) = 1/2."
