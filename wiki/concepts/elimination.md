---
id: elimination
type: concept
fields: [linear-algebra]
n_sources: 2
tiers: [core]
grounding: digests
sources: [strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch02-solving-p1]
generated_by: build_kg.py
---

# elimination

## Definitions in the sources

### linear-algebra

- [[strang-2023-introduction/ch01-vectors]] (pp. 3, 32): subtract multiples of one equation from others to create zeros; used to find R [new]
- [[strang-2023-introduction/ch02-solving-p1]] (p. 40): subtract multiples of pivot rows from lower rows to reach upper triangular U [new]

## Instances that use it

- [[gaussian-elimination-inverse-example]] — 4×4 inverse found via $[A|I]$ — from [[deisenroth-2020-mml/ch02-linear-p1]]
- [[shirt-pricing-game]] — RE versus BB pricing: equilibrium $40, a prisoners' dilemma, elimination — from [[dixit-2008-art-strategy/ch04-beautiful]]
- [[sherlock-holmes-elimination]] — eliminative inference in fiction — from [[godfreysmith-2003-theory/ch14-bayesianism]]
- [[conjunction-elimination-entailment]] — $\forall x(H(x)\land J(x))\vDash\forall x\,H(x)$ — from [[magnus-2025-forallx/ch34-reasoning]]
- [[student-network-ve]] — VE on the 8-variable student network, two elimination orders — from [[murphy-2023-pml2/ch09-message]]
- [[expander-laplacian-solve]] — condition number about $1+2\epsilon$; fast iterative solve versus $\Omega(n^3)$ elimination — from [[spielman-2025-sagt/ch34-iterative]]
- [[cr-example-4]] — elimination finds R for [[1,3,4],[2,4,2],[3,7,6]] — from [[strang-2023-introduction/ch01-vectors]]
- [[elimination-example-2-3-4]] — 3 by 3 system with multipliers 2, 1, 1 and pivots 2, 5, 7; x = (4,1,2) — from [[strang-2023-introduction/ch02-solving-p1]]

## Candidate bridges

- [metaphor] Gaussian elimination vs. dimension counting ↔  — the author offers the abstract proof as a cleaner alternative to elimination (p. 65). — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → unspecified)
- [same-math] Rule 3 successive elimination ↔ decision-game-theory: iterated elimination of dominated strategies — the same procedure (p. 124). — from [[dixit-2008-art-strategy/ch04-beautiful]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Pass/fail unraveling ↔ iterated elimination of dominated strategies: each round removes the top of the pool. — from [[dixit-2008-art-strategy/ch08-interpreting]] (decision-game-theory → other)
- [metaphor] Choosing a "typical" city by elimination ↔ case selection in comparative research: typicality is argued by excluding extremes and special cases, not by a statistical sampling rule. — from [[katz-1955-personalinfluence/appa-choice]] (communication-theory → political-science)
- [structural-analogy] Quine's "Socratizer" paraphrase ↔ logic: Russell's elimination of descriptions — a name is replaced by a predicate plus description (fn. 6). — from [[kripke-1980-naming/ch01-lecture-p1]] (analytic-philosophy → analytic-philosophy)
- [structural-analogy] backward elimination of discarded paths ↔ discrete-time optimal control: backward recursion for feedback — both build a state-dependent policy — from [[liberzon-2012-calculus/ch05-hamilton]] (control-theory → control-theory)
- [structural-analogy] choosing a bit order to shrink the trellis ↔ bayesian: choosing a variable elimination order to reduce the cost of exact inference. — from [[mackay-2003-information/ch25-exact]] (information-theory → bayesian)
- [metaphor] Bertrand undercutting ↔ iterated elimination of dominated strategies: both reason step by step about profitable deviations, though the text does not link them. — from [[osborne-2004-introduction/ch03-nash-p1]] (decision-game-theory → other)
- [structural-analogy] Finite rounds of elimination ↔ level-k reasoning: both reason a limited number of steps about others (canon link; not stated in this unit) — from [[osborne-2004-introduction/ch12-rationalizability]] (decision-game-theory → other)
- [same-math] Strictly dominated by a mixed strategy ↔ the dominance notion used in iterated elimination of dominated strategies: the same definition used on a different footing. — from [[osborne-2004-introduction/ch12-rationalizability]] (decision-game-theory → other)
- [structural-analogy] The lecture's tar-deposit example ↔ front-door adjustment; the lecture describes it only as a *do*-elimination, not by that name. — from [[pearl-2009-causality/main]] (bayesian → unspecified)
- [same-math] Elimination of dominated rows and columns in Fig. 16 ↔ backward induction: Schelling identifies the two procedures (p. 184). — from [[schelling-1960-conflict/ch05-enforcement-p2]] (decision-game-theory → other)
- [structural-analogy] Agenda setter ↔ seeding in a single-elimination sports tournament: the bracket order shapes who wins (the text notes the sports analogy, p. 47). — from [[shepsle-2010-analyzing/ch03-getting]] (political-science → other)
- [same-math] Schur complement $M_B$ ↔ linear-algebra: block Gaussian elimination, with $(M^{-1})(B,B)=(M_B)^{-1}$ — the same block formulas. — from [[spielman-2025-sagt/ch12-effective]] (linear-algebra → linear-algebra)
- [same-math] Elimination with Schur complement ↔ Gaussian elimination / sparse Cholesky: eliminating vertices leaves the Schur complement. — from [[spielman-2025-sagt/ch37-augmented]] (linear-algebra → other)
- [same-math] Solving $B(i,a)=\sum y_hB(h,a)$ over $\mathbb Z/2$ ↔ linear algebra: Gaussian elimination in a finite field — literally the same elimination. — from [[spielman-2025-sagt/ch39-testing]] (linear-algebra → linear-algebra)
- [same-math] Solving Ax = e_k for each k to build A⁻¹ ↔ solving many right sides with one factorization: both reuse the same elimination steps (pp. 57–58) — from [[strang-2023-introduction/ch02-solving-p1]] (linear-algebra → other)
- [structural-analogy] Sampling columns and rows, $A\approx CMR$ ↔ numerical computing: trading exact elimination for a fast approximate solution that is accurate with high probability (p. 108). — from [[strang-2023-introduction/ch03-four-p2]] (linear-algebra → other)
- [structural-analogy] Gram-Schmidt step ↔ elimination: both give a triangular factor, with $A^{\mathsf T}A$ pivots equal to squares of the diagonal of $R$ (Problem 19, p. 187). — from [[strang-2023-introduction/ch04-orthogonality-p2]] (linear-algebra → other)
- [same-math] Block elimination on K giving −AᵀS⁻¹A ↔ linear-algebra: Schur complement and pivots — elimination on a 2×2 block matrix. — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → linear-algebra)
