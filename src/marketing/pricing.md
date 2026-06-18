# Pricing

## Simple, Usage-Based Pricing

Pay for what you use. No subscriptions. No lock-in. Scale as you grow.

---

## Tier Comparison

| Feature | Free | L4 GPU | H100 GPU |
|---------|------|--------|----------|
| **Price** | $0* | $0.25 + $0.10/min | $1.50 + $1.00/min |
| **Variables** | 5,000 | 100,000 | 1,000,000 |
| **Clauses** | 35,000 | 300,000 | 8,000,000 |
| **XOR Variables** | 1,000 | 10,000 | 100,000 |
| **Q-SAT Nodes** | 500 | 15,000 | 100,000 |
| **Scheduling Resources** | 20 | 200 | 1,000 |
| **Concurrency** | 2 | 3 | 4 |
| **Engines** | Nano, Mini | Nano, Mini, Pro | All engines |

*\*Free until June 2026, then $0.01 + $0.01/min*

---

## Example Costs

| Problem | Engine | Solve Time | Cost |
|---------|--------|------------|------|
| Quick validation (100 vars) | Nano | 5ms | ~$0.00 |
| Medium scheduling (10k vars) | Mini | 200ms | ~$0.01 |
| Complex optimization (100k vars) | Pro | 10s | ~$0.17 |
| Industrial scale (1M vars) | Pro H100 | 2min | ~$3.50 |
| PSPACE problem | Pro H100 | 30min | ~$31.50 |

**Estimation:** A 10-minute industrial solve costs approximately **$1.25** on H100.

---

## Engines

| Engine | Best For | Satisfaction Rate | Speed |
|--------|----------|------------------|-------|
| **Nano** | Real-time APIs, quick checks | 3.24% | Ultra-fast |
| **Mini** | Balanced optimization | 31.37% | 10.64/sec |
| **Pro** | Mission-critical, 100% needed | 92.57% | 7.90/sec |
| **Nitro** | High-performance MaxSAT | Best for PSPACE | Fast |
| **QState** | N-ary scheduling, graph coloring | 100% when feasible | Variable |

---

## Search Space at Included Limits

| Model | Standard (CPU) | L4 GPU | H100 GPU |
|-------|---------------|--------|----------|
| Boolean SAT | 2^5000 ≈ 10^1505 | 2^100000 ≈ 10^30103 | 2^1000000 ≈ 10^301030 |
| XOR-SAT | 2^1000 ≈ 10^301 | 2^10000 ≈ 10^3010 | 2^100000 ≈ 10^30103 |
| Q-SAT (k-ary) | 5^500 ≈ 10^349 | 20^15000 ≈ 10^19415 | 50^100000 ≈ 10^169897 |

> These numbers illustrate the size of the full assignment space. Real difficulty depends on structure, not just size.

---

## Enterprise Pricing

For larger workloads or custom requirements:

| Component | Price |
|-----------|-------|
| **Base fee** | $100/month |
| **Compute** | $10/hour (dedicated H100) |
| **Custom engines** | Quote-based |
| **On-prem deployment** | Quote-based |
| **SLA** | Custom contracts available |

**Contact:** shunyabarlabs@zohomail.com

---

## Why Pay for Navokoj?

| Free Alternatives | Navokoj |
|-------------------|---------|
| Hours to solve | Milliseconds |
| Black-box output | DEFEKT diagnostics |
| Guess if satisfiable | Pre-solve hardness prediction |
| 10k variable cap | 1M variable native |
| No support | Community + paid support |

---

## Getting Started

```bash
# Free tier - no credit card required
curl -X POST https://api.navokoj.shunyabar.foo/v1/solve \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"num_vars": 1000, "clauses": [[1,2,3],[-1,4]], "engine": "nano"}'

# L4 GPU - $0.25 setup + per-minute
curl -X POST https://api.navokoj.shunyabar.foo/v1/solve \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"num_vars": 50000, "clauses": [...], "engine": "pro", "hardware": "l4"}'

# H100 GPU - $1.50 setup + per-minute
curl -X POST https://api.navokoj.shunyabar.foo/v1/solve \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"num_vars": 500000, "clauses": [...], "engine": "pro-deepthink", "hardware": "h100"}'
```

---

## Service Guarantees

| Guarantee | Details |
|-----------|---------|
| **Timeout handling** | All solves have 30-min hard timeout. Best partial result always returned. |
| **Billing** | Per-second billing, no rounding. |
| **Partial results** | Never returns empty error. Always returns best effort. |
| **Availability** | Alpha tier: best-effort. Enterprise: custom SLA. |

> **Note:** Self-serve tiers operate best-effort during alpha. Contact us for contractual uptime guarantees.
