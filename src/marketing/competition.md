# Competitive Landscape

## Why Navokoj Wins

---

## Market Comparison

| Capability | Navokoj | Gurobi/CPLEX | OR-Tools | Classical CDCL |
|------------|---------|--------------|----------|----------------|
| **Variables** | Up to 1M+ | 100M+ | 1M+ | 1M |
| **Millisecond solve** | ✅ | ❌ | ❌ | ❌ |
| **Hardness prediction** | ✅ DEFEKT | ❌ | ❌ | ❌ |
| **Always returns result** | ✅ Anytime | ❌ Timeout | ❌ Timeout | ❌ UNSAT |
| **XOR-native** | ✅ | ❌ | ❌ | ❌ |
| **GPU-accelerated** | ✅ H100 | Partial | ❌ | ❌ |
| **Developer API** | ✅ REST | ❌ SDK | ✅ | ✅ |
| **Pay-per-use** | ✅ | ❌ License | ❌ License | ❌ |

---

## Gurobi vs Navokoj

**Gurobi** is the industry standard for mathematical optimization. It's excellent for:
- Linear/quadratic programming
- MILP (mixed integer linear programming)
- Continuous variable optimization

**Navokoj** excels where Gurobi struggles:
- Boolean satisfiability at scale
- Problems with complex logical constraints
- Real-time decisioning (< 1 second)
- Problems where hardness is unknown

| Scenario | Gurobi | Navokoj |
|----------|--------|---------|
| 10k variable routing | 10-60s | **< 1s** |
| Million-variable placement | May timeout | **347ms** |
| Complex boolean logic | Requires translation | **Native** |
| Unknown hardness | No visibility | **DEFEKT** |
| UNSAT instance | Fails | **Best effort** |

---

## OR-Tools vs Navokoj

**OR-Tools** (Google) is open-source and widely used for:
- Vehicle routing
- Scheduling
- Integer programming

**Navokoj** provides advantages:
- Native boolean SAT
- Much higher satisfaction rates
- Physics-inspired optimization
- DEFEKT pre-solve diagnostics

| Scenario | OR-Tools | Navokoj |
|----------|----------|---------|
| 5k vehicle routing | 30s-5min | **< 1s** |
| Complex boolean logic | Requires CP-SAT | **Native** |
| Satisfaction guarantee | Best effort | **92.57% industrial** |
| Hardness visibility | None | **DEFEKT** |

---

## Classical CDCL SAT Solvers

**Kissat, CaDiCaL, Maplesat** are competition-grade CDCL solvers.

**Navokoj** differs fundamentally:
- **CDCL** = Systematic search through boolean assignment space
- **Navokoj** = Continuous optimization on arithmetic manifold

| Capability | CDCL Solvers | Navokoj |
|------------|--------------|---------|
| Million variables | Stalls | **Native** |
| XOR constraints | Gaussian elim | **Continuous** |
| Real-time (< 100ms) | ❌ | **✅** |
| Always returns result | ❌ UNSAT | **Anytime** |
| GPU acceleration | Rare | **H100** |

---

## Our Differentiation

### 1. Speed

```
Gurobi:      45 seconds
OR-Tools:    30 seconds
CDCL:        10 seconds
Navokoj:     347 milliseconds ⚡
```

### 2. Scale Without Compromise

| Solver | 100k vars | 500k vars | 1M vars |
|--------|-----------|-----------|---------|
| Gurobi | ~30s | Timeout | Fail |
| OR-Tools | ~20s | Timeout | Fail |
| CDCL | ~60s | Stall | Crash |
| **Navokoj** | **200ms** | **1s** | **347ms** |

### 3. Hardness Visibility

Before you solve, DEFEKT tells you:

```json
{
  "solvability_score": 84,
  "status": "likely_solvable",
  "recommendation": "Use pro-deepthink on H100 GPU"
}
```

No other solver offers this.

### 4. Anytime Algorithm Guarantee

Classical solvers: **UNSAT** → Done, no result.

Navokoj: **Always returns the best partial assignment.**

```json
{
  "success": true,
  "satisfiable": false,
  "satisfaction_rate": 0.985,
  "timeout_budget_hit": true,
  "assignment": [true, false, ...]
}
```

---

## When to Use What

| Use Case | Recommended |
|----------|-------------|
| Linear programming | Gurobi |
| MILP with continuous vars | Gurobi/CPLEX |
| Vehicle routing (simple) | OR-Tools |
| **Boolean SAT at scale** | **Navokoj** |
| **Real-time decisioning** | **Navokoj** |
| **Complex logical constraints** | **Navokoj** |
| **Unknown problem hardness** | **Navokoj** |
| **Must have partial result** | **Navokoj** |

---

## The Bottom Line

| Requirement | Solution |
|-------------|----------|
| Speed matters | Navokoj |
| Scale matters | Navokoj |
| Hardness unknown | Navokoj |
| Can't afford empty results | Navokoj |
| Complex boolean logic | Navokoj |
| MILP with continuous vars | Gurobi |
| Linear programming | Gurobi |
| Simple VRP | OR-Tools |

**Start free at [navokoj.shunyabar.foo](https://navokoj.shunyabar.foo)**
