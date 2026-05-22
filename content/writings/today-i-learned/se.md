+++
date = '2026-05-22T11:46:33+05:30'
title = 'Se'
+++

### 1. CPM / PERT / Project Scheduling (Guaranteed Numericals)

You need to calculate ES, EF, LS, LF, and Slack.
**The Trick:** Two passes. Forward pass for Earliest times, Backward pass for Latest times.

- **Earliest Start (ES):** Max of the Earliest Finish (EF) of all immediate predecessors. (Start at 0).

- **Earliest Finish (EF):** $ES + \text{Duration}$.

- **Minimum Time (MT) / Critical Path:** The max EF at the very end of the network.

- **Latest Finish (LF):** Min of the Latest Start (LS) of all immediate successors. (Start at the end using MT).
- **Latest Start (LS):** $LF - \text{Duration}$.
- **Slack Time:** $LS - ES$ (or $LF - EF$). If Slack is 0, that activity is on the Critical Path.

2. COCOMO & Cost Estimation

Always identify the software class first:

- **Organic:** Small team, familiar environment.

- **Semi-detached:** Mixed experience.

- **Embedded:** Complex hardware/real-time constraints.

**The Formulas:**

- $Effort = a1 \times (KLOC)^{a2}$ (in Person-Months)

- $Tdev = b1 \times (Effort)^{b2}$ (in Months)

**The EAF Trick (Intermediate COCOMO):**
If they give you Cost Drivers (like Pool 1 vs Pool 2 developers), multiply the base Effort by the Effort Adjustment Factor (EAF).

- $Effort_{new} = Effort_{nominal} \times EAF$.

- _Note:_ Time ($Tdev$) is calculated using the _new_ Effort.

3. Putnam Model & Schedule Compression

- **The Trick:** Putnam models effort over time using a Rayleigh curve.

- **The Core Equation:** $K = L^{3} / ({C_{k}}^{3} \times {t_{d}}^{4})$. (Where $K$ is effort, $L$ is size, $t_{d}$ is time, $C_{k}$ is environment constant) .

- **Exam Phrase to Drop:** "Extreme penalty for schedule compression." Because $t_{d}$ is to the power of 4 in the denominator, reducing the schedule slightly causes effort and cost to explode exponentially.

4. Control Flow Graph (CFG) & Cyclomatic Complexity

If they ask you to estimate independent paths (like in the Binary Search PYQ):

- **The Formula:** $V(G) = E - N + 2$ (Edges - Nodes + 2).
- **The Quick Trick:** Count the number of predicates (condition nodes like `if`, `while`, `for`) and add 1.
- _Example:_ A `while` loop containing an `if` and an `else if` = 3 conditions. Complexity = 4. This is your upper bound for independent paths.

5. Coupling and Cohesion

- **Coupling (Between modules - Want LOW):**

- _Best to Worst:_ Data $\rightarrow$ Stamp $\rightarrow$ Control $\rightarrow$ External $\rightarrow$ Common $\rightarrow$ Content.

- _Keywords:_ **Data** (passing only simple parameters) , **Stamp** (passing whole data structures) , **Control** (passing flags to change logic) , **Common** (shared global variables).

- **Cohesion (Inside module - Want HIGH):**

- _Best to Worst:_ Functional $\rightarrow$ Sequential $\rightarrow$ Communicational $\rightarrow$ Procedural $\rightarrow$ Temporal $\rightarrow$ Logical $\rightarrow$ Coincidental.

- _Keywords:_ **Functional** (one single task) , **Sequential** (output of A is input to B) , **Temporal** (tasks executed at the same time, e.g., initialization).

6. Testing Terminology

- **Verification vs. Validation:** Verification is phase-containment (did we build the phase right?). Validation checks the final product against the SRS (did we build the right product?).

- **Why Branch > Statement Coverage:**

- _Proof:_ Consider an `if (x > 0)` statement without an `else`. Executing with `x = 1` gives 100% statement coverage. However, it ignores what happens if `x = -1`. Branch coverage forces you to test both the True and the implicit False branches, catching errors Statement coverage misses.

- **Black Box:** Equivalence Partitioning (grouping inputs into valid/invalid sets) and Boundary Value Analysis (testing the exact edges of those sets, e.g., if range is 1-5000, test 0, 1, 5000, 5001).

### 7. Software Maintenance

Memorize these three buckets:

- **Corrective:** Fixing actual bugs and failures.
- **Adaptive:** Porting software to a new OS, database, or hardware environment.
- **Perfective:** Adding new features or improving performance based on user requests.
