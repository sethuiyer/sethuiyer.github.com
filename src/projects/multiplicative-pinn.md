# Multiplicative PINN Framework

## What It Solves

Physics-informed neural networks (PINNs) suffer from gradient conflicts when enforcing physical laws. Standard PINNs use additive penalty terms — this causes the physics loss to fight the data loss, leading to oscillations, slow convergence, and monotonicity violations.

## Key Innovation

**Multiplicative Constraint Enforcement** replaces additive penalties:

```
Traditional: Loss = DataLoss + λ × PhysicsLoss  (additive)
            ↓ (causes gradient conflicts)
Arithmetic Manifold: Loss = DataLoss × ConstraintFactor(PhysicsLoss)  (multiplicative)
```

The **Euler Gate**:
\(G(\mathbf{v}) = \prod_{c} (1 - p_c^{-\tau v_c})\)

The **Exponential Barrier**:
\(B(\mathbf{v}) = \exp(\gamma \|\mathbf{v}\|_2^2)\)

Combined: \(C(\mathbf{v}) = G(\mathbf{v}) \times B(\mathbf{v})\)

### Why It Works

When constraints are satisfied, \(G(\mathbf{v}) \to 1\) and \(B(\mathbf{v}) \approx 1\). When violated, \(G(\mathbf{v}) \to 0\) and \(B(\mathbf{v}) \to \infty\). The product **zeroes out** any solution that violates a constraint.

### Superconducting Phase

At critical \(\beta = 1\), the Riemann zeta function diverges:
\(\zeta(1) = \infty\)

This nucleates a "superconducting phase" where constraints propagate without dissipation — gradients flow freely when physics is satisfied.

## Results

| Metric | Additive (Standard) | Multiplicative PINN |
|--------|---------------------|---------------------|
| Residual reduction (Navier-Stokes) | baseline | **99.64%** |
| Monotonicity violations | 31.31% | **0%** |
| Speedup over CFD | 1x | **100,000x** |

## Website

**Live:** [sethuiyer.github.io/multiplicative-pinn-framework](https://sethuiyer.github.io/multiplicative-pinn-framework)

## Key Files

- `multiplicative-pinn-framework/README.md` — Overview
- `multiplicative-pinn-framework/docs/RESULTS_SUMMARY.md` — Detailed benchmarks
- DOI: [10.5281/zenodo.18214172](https://doi.org/10.5281/zenodo.18214172)

## Connection to Core Vision

The Multiplicative PINN is the **proof of concept** that multiplicative constraint enforcement works in neural networks. It demonstrates:
- The Euler gate structure eliminates gradient conflicts
- The Riemann zeta divergence creates a superconducting phase
- The approach scales to real PDEs (Navier-Stokes)

---

## See Also

- [All Projects](index.md) — project overview
- [NitroSAT](nitrosat.md) — applies multiplicative principles to MaxSAT
- [Spectral-Multiplicative](spectral-multiplicative.md) — multiplicative constraints in graph optimization
- [Multiplicative vs Additive](../concepts/multiplicative-vs-additive.md) — the mathematical foundation
- [Prime Weighting](../concepts/prime-weighting.md) — prime-weighted physics constraints
- [Partition Function](../concepts/partition-function.md) — local partition function per constraint
- [Benchmarks](../getting-started/benchmarks.md) — Navier-Stokes results comparison
