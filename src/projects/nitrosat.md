# NitroSAT: A Physics-Informed Anytime MaxSAT Approximator

## What It Is

NitroSAT is a continuous-relaxation MaxSAT solver that approaches hard constraint satisfaction problems through physics-informed optimization rather than classic discrete backtrack-search paradigms. It operates as a **deterministic, sub-second anytime approximator** — designed for massive, structured industrial instances where finding a high-quality solution quickly matters more than proving optimality.

The core insight: by translating discrete logical constructs into continuous topological manifolds, NitroSAT bypasses the exponential search spaces that cripple CDCL solvers on structured geometries like hardware verification circuits, university timetabling, and grid-coloring problems.

---

## Architecture

### 1. Continuous Relaxation and Gradient-Based Flow

Traditional SAT solvers operate in the discrete boolean domain \(\{0, 1\}^n\), where moving between states requires discrete variable flips. This makes the search space highly non-convex and susceptible to combinatorial explosions.

NitroSAT relaxes variables from discrete bits to continuous coordinates within a bounded hypercube \([0, 1]^n\). This transforms the discrete constraint satisfaction problem into a continuous energy minimization problem.

**WAdam Optimizer**: The engine uses gradient-based flows to traverse the energy landscape. By computing gradients of a differentiable loss function constructed from the clauses, the solver navigates toward regions of high constraint satisfaction without committing to premature discrete branching choices.

**Thermal/Langevin Annealing**: To prevent the gradient flow from getting trapped in shallow local minima, the system incorporates thermal noise (\(\beta\) sensitivity via Langevin dynamics). This allows the system to probabilistically "jump" over energy barriers during early optimization phases, cooling down over iterations to settle into a deep attraction basin.

### 2. Spectral Initialization and Basin Navigation

A critical challenge in non-convex optimization is the starting point. Random initialization often lands the solver in highly chaotic regions of the landscape.

**Spectral Methods**: By leveraging spectral properties of the constraint graph (the Laplacian and adjacency matrices of the variable-clause incidence), NitroSAT computes an initial coordinate mapping that positions the solver inside a favorable valley of the global energy landscape.

**Basin Recovery**: On adversarial planted 3-SAT testing, NitroSAT consistently navigates into the *planted basin* — generating assignments that are 94% to 96% bit-similar to the optimum, even when it doesn't find the exact unique planted assignment. The spectral initialization effectively reduces the search space by positioning the continuous trajectory inside the correct attraction region.

### 3. Topological Repair and Cycle Resolution

Highly structured constraint graphs (such as grids, circuit multipliers, and timetables) contain topological loops or "frustrations" where satisfying one local cluster of constraints violates another nearby cluster.

**Persistent Homology (\(\beta_1\) Tracking)**: The engine tracks topological cycles through the first Betti number \(\beta_1\). High topological complexity scores correlate with regions where the solver's continuous coordinates are conflicted — the gradients dissolve into noise because every local improvement creates a corresponding local violation elsewhere.

**Topological Repair Phase**: Once the continuous flow plateaus, the engine applies targeted topological repairs to resolve localized cyclical contradictions. This phase surgically adjusts variables involved in high-friction cycles, resolving the topological bottlenecks that would otherwise cause pure gradient descent to stall.

### 4. Prime Number Weighting and Symmetry Breaking

One of the distinctive theoretical aspects of the engine is the use of prime weights derived from the Prime Number Theorem, rather than uniform clause weights.

**Breaking Algebraic Symmetry**: In uniform weighting, multiple configurations of unsatisfied clauses can yield the exact same energy output, leading to flat plateaus ("glassy" states) where gradients vanish. The solver loses all signal about which direction to move.

**Topological Smoothing**: Assigning prime-based weights creates a mathematically unique signature for different combinations of unsatisfied constraints. According to ablation studies, this prime-weighting mechanism reduces \(\beta_1\) post-solve topological cycles from 79 to 20 on structured geometries, accelerating convergence by approximately 3x to 4x compared to uniform weighting.

### 5. The Metric Space

NitroSAT uses the **Inverted Poincaré Disk** metric for probability-valued variables:

\[ds^2 = \frac{4|dz|^2}{(|z|^2(1-|z|^2)^2)}\]

This provides a natural geometry for the \([0,1]\) variable domain, ensuring that probability mass is appropriately concentrated near boundaries where discrete solutions live.

### 6. Free Energy Framework

The optimization follows a free energy functional:

\[F[x] = \lambda E_{kin}[x] + E_{pot}[x] - \frac{1}{\beta}S[x]\]

with gradient flow:

\[\frac{\partial x}{\partial t} = -\frac{\delta F}{\delta x}\]

where \(E_{kin}\) encodes kinetic energy from the optimizer momentum, \(E_{pot}\) encodes constraint violations, and \(S[x]\) is an entropy term modulated by the inverse temperature \(\beta\).

---

## Performance Characteristics

### Where It Excels: Regular and Structured Geometries

NitroSAT performs exceptionally well on problems with high local symmetry, regular degree distributions, and low-dimensional manifold structure:

| Problem Class | Example | Why NitroSAT Works |
|--------------|---------|-------------------|
| Hardware multipliers | 512-bit circuit verification | Regular gate structure enables efficient heat kernel propagation |
| University timetabling | 80M-clause instances | Structured conflict graph with exploitable topology |
| Grid coloring | Edwards-Anderson 3D spin glasses | Low-dimensional manifold aligns with spectral initialization |
| Planted satisfiability | Adversarial 3-SAT | Spectral method finds the planted basin reliably |

**Why**: The heat kernel diffusion and continuous relaxation can propagate local constraint signals globally across a regular grid. The gradient descent step efficiently locates the optimal basin because the underlying geometry provides a coherent global structure.

### Where It Encounters Limits: High-Expansion and Unstructured Graphs

NitroSAT plateaus on problems designed to lack local bottlenecks and low-dimensional representations:

| Problem Class | Example | Why It Struggles |
|--------------|---------|-----------------|
| Expander graphs | Urquhart formulas | No local geometry to exploit — landscape is flat and frustrated |
| Random 3-SAT | Phase transition (\(\alpha \approx 4.27\)) | Exponential conflicts without topological structure |
| Sparse random graphs | High-degree random regular graphs | Global connectivity destroys basin structure |

**Why**: In expander graphs, every variable cluster is highly connected to every other cluster without regular geometric structure. The continuous energy landscape becomes almost completely flat and frustrated. The gradient signal dissolves into chaotic noise because local improvements are immediately offset by global violations.

On expanders, NitroSAT typically achieves approximately 90% satisfaction and cannot improve further — the topological repair phase has no low-hanging cycles to fix because the frustration is global, not local.

---

## Results

| Instance | Variables | Clauses | Result | Time |
|----------|-----------|---------|--------|------|
| Planted Coloring | 105K | 232K | SAT (100%) | 13.78s |
| Hardware Verification | 788,480 | — | SAT (100%) | 5.92s |
| University Timetabling | 80M clauses | — | SAT (100%) | 73s |
| Random CNF (5000+ instances) | Various | Various | **77% perfect SAT** | — |
| Median satisfaction | — | — | **99.7%** | — |

**Median satisfaction across 5,000+ random CNF instances**: 99.7%

---

## Limitations (Self-Assessment)

NitroSAT is **not** designed to replace exact solvers when mathematical certificates of unsatisfiability or global optimality proofs are required. It is an anytime approximator.

Known limitations:

- **Expander graphs**: Plateaus around 90% satisfaction; no path to improvement via topological repair
- **Random 3-SAT at phase transition**: Structured approaches struggle here; CDCL solvers have structural advantages
- **UNSAT certification**: Does not produce proofs of unsatisfiability
- **Exact optimum**: Returns high-quality approximations, not proven-optimal solutions

The 2^1024 framing in earlier documentation was incorrect. XOR chains define affine subspaces (dimension \(n - r\) where \(r\) is rank), not the full power set. The relevant metric is basin fidelity — how close the returned assignment is to the planted optimum — not the cardinality of the unconstrained solution space.

---

## Connection to the Arithmetic Manifold

NitroSAT is the **flagship implementation** of the Arithmetic Manifold framework. It combines:

- **Prime weighting**: From partition function theory — unique constraint signatures via the Fundamental Theorem of Arithmetic
- **Spectral initialization**: Heat kernel trace \(\text{Tr}(e^{-tL})\) as a basin-finding prior
- **Topological repair**: Persistent homology tracking (Betti numbers) for guided repair
- **Phase transitions**: BAHA/Lambert W detection for when to transition between optimization strategies
- **Riemann Hypothesis connection**: The asymptotic stability condition \(1 - \sigma > \gamma\) governs when the continuous relaxation remains valid at scale

> "NitroSAT does not prove the Riemann Hypothesis. But it embeds RH as a phase boundary: the solver functions as a physical instrument whose asymptotic stability threshold coincides exactly with the critical line Re(s) = 1/2."

---

## Website

**Live:** [sethuiyer.github.io/NitroSAT](https://sethuiyer.github.io/NitroSAT)

## Key Files

- `NitroSAT/README.md` — Full project overview and benchmark methodology
- `NitroSAT/src/c/v2/nitrosatv2.c` — Core C99 implementation
- DOI: [10.5281/zenodo.18753235](https://doi.org/10.5281/zenodo.18753235)
- API: [api.navokoj.shunyabar.foo](https://api.navokoj.shunyabar.foo)

---

## Citing

If you use NitroSAT in research, please cite:

```bibtex
@software{nitrosat2026,
  author = {Sethurathinam Iyer},
  title = {NitroSAT: A Physics-Informed MaxSAT Approximator},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.18753235},
  url = {https://github.com/sethuiyer/NitroSAT}
}
```
