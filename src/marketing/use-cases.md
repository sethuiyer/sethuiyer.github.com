# Use Cases & Target Customers

## Who Navokoj Is For

Navokoj solves **discrete commitment allocation under hard constraints** — where partial decisions must be preserved, and the cost of mistakes is high.

---

## Primary Verticals

### 1. Logistics & Transportation

**Problems Solved:**
- Vehicle routing with time windows
- Warehouse bin packing
- Fleet assignment
- Delivery slot optimization

**Decision Variables:**
- Each vehicle chooses one of a few legal routes
- Each package chooses one of a few eligible delivery windows

**Why It Fits:**
- Small legal choice set per decision
- Locked relationships matter (existing routes, driver preferences)
- Local repair needed when disruptions occur

**Why They Pay:**
- Fuel costs are directly measurable
- Customer SLA improvements are trackable
- Driver hours affect compliance

**Example Result:**
> *"Route optimization went from 45 seconds to 347ms. That's real-time decisioning, not batch processing."*

---

### 2. Healthcare Workforce Scheduling

**Problems Solved:**
- Nurse rostering with skill mix requirements
- Doctor shift scheduling with legal constraints
- Operating room allocation
- Equipment booking

**Decision Variables:**
- Each nurse/doctor chooses shifts from a legal set
- Each patient procedure chooses an OR slot

**Why It Fits:**
- Small legal shift set per person (5-7 days)
- Contractual constraints are hard (rest periods, max hours)
- Fairness constraints require explainable outputs

**Why They Pay:**
- Agency nurse costs are $100-200/hr
- Compliance violations carry legal risk
- Staff retention correlates with scheduling fairness

**Example Result:**
> *"We reduced agency nurse spend by 40% in the first quarter. The solver paid for itself in 6 weeks."*

---

### 3. Cloud Infrastructure & DevOps

**Problems Solved:**
- VM placement across physical hosts
- Container orchestration with affinity rules
- Network path optimization
- GPU cluster scheduling

**Decision Variables:**
- Each VM chooses one of a few eligible hosts
- Each container chooses one of a few legal pods

**Why It Fits:**
- Co-location, anti-affinity, and resource constraints
- Hardware heterogeneity matters
- Live migration constraints must be respected

**Why They Pay:**
- GPU idle time is pure cost ($3-4/hr per H100)
- 30% higher density = millions in savings
- Cloud margin improvement is C-suite visible

**Example Result:**
> *"15,000 VMs placed with 100% constraints satisfied. $1.4M/year in savings. 10.8 seconds."*

---

### 4. Financial Services

**Problems Solved:**
- Portfolio rebalancing with constraints
- Trade execution sequencing
- Credit limit allocation
- Insurance underwriting rules

**Decision Variables:**
- Each asset chooses rebalancing targets
- Each trade chooses execution timing

**Why It Fits:**
- Regulatory constraints are hard
- Risk limits must be strictly enforced
- Explainability required for audits

**Why They Pay:**
- Regulatory fines are massive
- Best-execution is legally mandated
- Risk management is existential

---

### 5. Telecom & Spectrum

**Problems Solved:**
- Spectrum auction optimization
- Network frequency allocation
- Cell tower placement
- Signal interference constraints

**Decision Variables:**
- Each bidder chooses one of a few legal packages
- Each frequency chooses one of a few channels

**Why It Fits:**
- Billions of dollars in play
- Interference constraints are physical
- Synergies between adjacent bands matter

**Why They Pay:**
- Revenue optimization is directly measurable
- Regulatory constraints are non-negotiable
- Speed enables dynamic pricing

**Example Result:**
> *"Spectrum auction: $2.4B revenue vs $1.18B greedy baseline. 102% improvement. 1.657ms."*

---

### 6. Manufacturing & Supply Chain

**Problems Solved:**
- Production scheduling with changeover costs
- Inventory allocation across warehouses
- Order promising with ATP/CTP
- Supplier selection with constraints

**Decision Variables:**
- Each order chooses one of a few fulfillment sources
- Each production run chooses one of a few schedules

**Why It Fits:**
- Capacity constraints are hard
- Customer commitments are already locked
- Local repair needed for disruptions

**Why They Pay:**
- Working capital tied up in inventory
- Expediting costs are massive
- Fill rate directly affects revenue

---

## Problem Categories

Beyond specific verticals, Navokoj excels at:

| Category | Examples |
|----------|----------|
| **Assignment Problems** | Task-worker, asset-location, resource-time |
| **Scheduling** | Shifts, production runs, maintenance windows |
| **Configuration** | Quote construction, plan selection, bundle rules |
| **Routing** | Vehicle, network flow, signal path |
| **Placement** | VM- host, facility-location, inventory positioning |
| **Matching** | Marketplace, auction, exchange |

---

## Not a Fit For

Navokoj is **not** the right tool when:

- Problems are continuous (use gradient-based optimization)
- Real-time control systems require sub-millisecond deterministic response (embedded systems)
- All constraints are soft preferences (multi-objective evolutionary algorithms may suffice)
- Problems have no discrete structure (pure simulation/Monte Carlo)
