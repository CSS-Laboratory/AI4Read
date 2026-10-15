---
id: saddle-point
type: concept
fields: [control-theory, information-theory, llm]
fields_strong: [control-theory, information-theory, llm]
n_sources: 3
n_works: 3
tiers: [reference, core]
grounding: digests
sources: [bellman-1957-dp/ch10-x, polyanskiy-2025-information/ch06-extremization, prince-2023-udl/ch06-fitting]
generated_by: build_kg.py
---

# saddle-point

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch10-x]] (pp. 294, 303): pair $(G_1,G_1')$ at which neither player gains by deviating; used in Lemma 1 and §18 [new]

### information-theory

- [[polyanskiy-2025-information/ch06-extremization]] (p. 93): pair $(x^*,y^*)$ with $f(x,y^*)\le f(x^*,y^*)\le f(x^*,y)$; it implies minimax equality [new]

### llm

- [[prince-2023-udl/ch06-fitting]] (p. 83): zero gradient, loss rises in some directions and falls in others [new]

## Instances that use it

- [[zero-sum-minmax-case]] — the saddle-point theorem's validity rests on admitting mixtures, so Arrow says a pairwise-built model does not seem to suit this case well — from [[arrow-1951-socialchoice/ch02-ii]]
- [[gabor-model-fitting]] — two-parameter non-convex loss with local minima and a saddle point; global loss 0.64 — from [[prince-2023-udl/ch06-fitting]]

## Candidate bridges

- [same-math] Laplace approximation ↔ physics: saddle-point approximation — the source names them as the same method (p. 341) — from [[mackay-2003-information/ch28-model]] (information-theory → other:physics)
- [structural-analogy] Saddle-point capacity ↔ information-theory (universal coding): a min-max over a divergence — the text only says the saddle-point result is applied later in universal data compression (p. 94). — from [[polyanskiy-2025-information/ch06-extremization]] (information-theory → information-theory)
- [structural-analogy] Backward-channel construction for $R(D)$ ↔ information-theory: capacity-achieving input distributions and the saddle-point in Ch. 5 — the same KL-decomposition trick is used on both sides. — from [[polyanskiy-2025-information/ch29-evaluating]] (information-theory → information-theory)
- [structural-analogy] Primal–dual (minimax = worst-case Bayes) ↔ capacity: $C=\min_{P_X}\max_{Q_Y}=\max_{Q_Y}\min_{P_X}D(P_{Y|X}\|Q_Y|P_X)$ with saddle point — the text recalls it as an example of a similar minimax theorem (p. 566). — from [[polyanskiy-2025-information/ch31-basics]] (information-theory → other:capacity)
