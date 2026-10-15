---
id: minimax-theorem
type: concept
fields: [control-theory, information-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [bellman-1957-dp/ch10-x, polyanskiy-2025-information/ch31-basics]
generated_by: build_kg.py
---

# minimax-theorem

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch10-x]] (p. 286): $\min_q\max_pE_A=\max_p\min_qE_A$ for mixed strategies; assumed here without proof [new]

### information-theory

- [[polyanskiy-2025-information/ch31-basics]] (pp. 565–567): conditions under which $R^*=R^*_{\rm Bayes}$; strong duality of a convex program [new]

## Candidate bridges

- [same-math] Maxmin = minmax in a strictly competitive game ↔ decision-game-theory: the equality part of the minimax theorem for zero-sum games — here shown only under the assumption that an equilibrium exists (Prop. 341.1). — from [[osborne-2004-introduction/ch11-strictly]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Primal–dual (minimax = worst-case Bayes) ↔ capacity: $C=\min_{P_X}\max_{Q_Y}=\max_{Q_Y}\min_{P_X}D(P_{Y|X}\|Q_Y|P_X)$ with saddle point — the text recalls it as an example of a similar minimax theorem (p. 566). — from [[polyanskiy-2025-information/ch31-basics]] (information-theory → other)
