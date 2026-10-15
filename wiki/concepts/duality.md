---
id: duality
type: concept
fields: [control-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch08-output, kalman-1960-filtering/main]
canon_spine: control-theory
generated_by: build_kg.py
---

# duality

## Canon spine entry

- **duality** (control-theory): controllability and observability are mathematically mirror images (grad)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-7): $A\leftrightarrow A^T,B\leftrightarrow C^T,K\leftrightarrow L^T,W_r\leftrightarrow W_o^T$; observer design mirrors state feedback
- [[kalman-1960-filtering/main]] (p. 42): Theorem 4: filtering Problem I and noise-free regulator Problem II share the same recursions under the Table 1 substitutions

## Candidate bridges

- [structural-analogy] weak duality and pairing (2.5) ↔ optimisation: LP duality with complementary slackness, in function space — same inequality structure. — from [[bellman-1957-dp/ch07-vii]] (control-theory → other)
- [structural-analogy] control/estimation duality ↔ optimization: both are the same stacked constrained least squares, with inputs chosen (control) or inputs unknown (estimation) — the text itself calls this duality (p. 373). — from [[boyd-2018-vmls/ch17-constrained]] (linear-algebra → other)
- [same-math] Voter-model duality ↔ probability: exact mapping to coalescing random walkers; transience of random walks in $d>2$ is linked to the lack of consensus there (p. 9–10). — from [[castellano-2009-socialdynamics/main-p1]] (complex-systems → other)
- [same-math] Theorem 4 duality (filter ↔ noise-free regulator) ↔ control-theory: the LQR design equations — the paper itself gives the substitution $X\to\hat X'(T-\tau)$ between (28–30) and (35–37). — from [[kalman-1960-filtering/main]] (control-theory → control-theory)
- [same-math] CQ rules ↔ logic: duality of ∀ and ∃ — ¬∃ ≡ ∀¬ is the same equivalence. — from [[magnus-2025-forallx/ch39-rules]] (analytic-philosophy → analytic-philosophy)
- [structural-analogy] DNF and CNF swap ∧ and ∨ ↔ duality in logic: the two definitions mirror each other, and so do the two constructions (true lines versus false lines). — from [[magnus-2025-forallx/ch45-normal]] (analytic-philosophy → analytic-philosophy)
- [structural-analogy] Natural parameters vs moment parameters ↔ exponential-family duality: ordinary gradient in $\mu$ equals natural gradient in $\lambda$ (p. 284) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → other)
- [same-math] Donsker–Varadhan duality ↔ convex analysis: Fenchel–Legendre conjugacy of $D(\cdot\|Q)$ and $f\mapsto\psi_f$ (p. 73). — from [[polyanskiy-2025-information/ch05-variational]] (information-theory → other)
- [structural-analogy] Greedy maximal packing is a covering ↔ optimization duality: converse proofs turn into achievability (footnote 3, p. 524). — from [[polyanskiy-2025-information/ch30-metric]] (information-theory → other)
- [metaphor] Two-filter smoothing ↔ control-theory: duality of filtering and control. This is only a loose picture of a backward recursion complementing a forward one; the book makes no such link. — from [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (control-theory → control-theory)
