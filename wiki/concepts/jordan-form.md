---
id: jordan-form
type: concept
fields: [linear-algebra, control-theory]
n_sources: 4
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch06-linear, axler-2024-ladr/ch08-operators, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch08-linear]
generated_by: build_kg.py
---

# jordan-form

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch08-operators]] (pp. 322–324): a basis in which blocks have $\lambda_k$ on the diagonal and 1's directly above [new]
- [[strang-2023-introduction/app1-ranks]] (p. 405): nearly diagonal form with one block per independent eigenvector [new]
- [[strang-2023-introduction/ch08-linear]] (p. 327–329): J has Jordan blocks (λ on the diagonal, 1's above) and is nearly diagonal when eigenvectors are missing [new]

### control-theory

- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-9): block form with eigenvalues on the diagonal; 1's may appear on the superdiagonal, coupling states, when there are equal eigenvalues [new]

## Candidate bridges

- [structural-analogy] Jordan form's instability ↔ numerical analysis: tiny perturbations split repeated eigenvalues, so discontinuous structure is lost. — from [[strang-2023-introduction/ch08-linear]] (linear-algebra → other)
