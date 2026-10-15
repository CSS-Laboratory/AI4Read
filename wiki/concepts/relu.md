---
id: relu
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [prince-2023-udl/ch03-shallow, strang-2023-introduction/ch10-learning]
generated_by: build_kg.py
---

# relu

## Definitions in the sources

### linear-algebra

- [[strang-2023-introduction/ch10-learning]] (p. 370): ReLU(y) = max(y,0), the ramp activation, applied to each component [new]

### llm

- [[prince-2023-udl/ch03-shallow]] (p. 25): $a[z]=\max(0,z)$; clips negatives to zero [new]

## Instances that use it

- [[random-relu-features]] — 5000 features $\max\{0,(Rx)_j\}$ with random $\pm1$ matrix $R$; cut test error sharply — from [[boyd-2018-vmls/ch14-least]]
- [[relu-output-toy-model]] — $x'=\mathrm{ReLU}(W^TWx+b)$, a very simple model that does show superposition (§ "The Model (x → x')") — from [[elhage-2022-superposition/main-p1]]
- [[ten-parameter-relu-network]] — three-unit scalar network of Eq. 3.1 and Fig. 3.3 — from [[prince-2023-udl/ch03-shallow]]
- [[dying-relu]] — if all training examples give a unit negative input, its zero derivative means its incoming weights cannot be improved — from [[prince-2023-udl/ch03-shallow]]
- [[relu-sum-example]] — ReLU(x)+ReLU(y)+ReLU(z) gives 8 pieces; a 4th fold gives 15 — from [[strang-2023-introduction/ch10-learning]]

## Candidate bridges

- [structural-analogy] Random ReLU features ↔ neural-network hidden layer: the text says neural network features are another feature-engineering route (p. 302); it does not say the two are the same. — from [[boyd-2018-vmls/ch14-least]] (linear-algebra → other:neural-network-hidden-layer)
- [structural-analogy] Hidden-layer ReLU network ↔ llm: the per-token feed-forward block of a Transformer — same layer shape (linear, nonlinearity, linear), but the book here covers only the shallow case. — from [[prince-2023-udl/ch03-shallow]] (llm → llm)
- [structural-analogy] Composition F_L(…F₁(v)) with ReLU ↔ linear algebra: matrix product A_L⋯A₁ — without the nonlinearity the chain would be one matrix (p. 379) — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)
- [metaphor] ReLU folds making an "origami" graph ↔ geometry: folding paper — the author's own picture, with pieces extending to infinity (p. 376) — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → other:mathematics)
