---
id: mean-field-approximation
type: concept
fields: [complex-systems, bayesian, information-theory]
fields_strong: [complex-systems, bayesian, information-theory]
n_sources: 6
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [castellano-2009-socialdynamics/main-p1, castellano-2009-socialdynamics/main-p2, castellano-2009-socialdynamics/main-p3, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch10-variational-p2, polyanskiy-2025-information/ch05-variational]
raw_ids: [mean-field approximation]
canon_spine: [complex-systems]
generated_by: build_kg.py
---

# mean-field-approximation

## Canon spine entry

- **mean-field approximation** (complex-systems): replacing each agent's neighbors with the population average to get solvable equations (grad)

## Definitions in the sources

### complex-systems

- [[castellano-2009-socialdynamics/main-p1]] (p. 4): all-to-all interaction ("homogeneous mixing"), which guarantees that the mean-field approximation is correct
- [[castellano-2009-socialdynamics/main-p2]] (pp. 25, 31): rate equations assuming homogeneous mixing, used for Axelrod bonds and Eq. (36) [as `mean-field approximation`]
- [[castellano-2009-socialdynamics/main-p3]] (p. 41): spatial correlations ignored, density is the meeting probability

### bayesian

- [[murphy-2023-pml2/ch07-inference]] (p. 354): Gaussian $q$ with diagonal $\Sigma$, i.e. fully factorised [new]
- [[murphy-2023-pml2/ch10-variational-p2]] (p. 456): fully factorised $q(z)=\prod_jq_j(z_j)$ [new]

### information-theory

- [[polyanskiy-2025-information/ch05-variational]] (p. 75): restricting the Gibbs sup to product distributions [new]

## Candidate bridges

- [structural-analogy] Modular approximation of a log-submodular distribution ↔ bayesian: mean-field variational inference — the author says it is "like a mean-field approximation" with independent variables (p. 341). — from [[murphy-2023-pml2/ch06-optimization-p3]] (bayesian → bayesian)
- [structural-analogy] Aggregate-only long-run dependence ↔ complex-systems: mean-field approximation — both replace detailed neighbors with an average (p. 474). — from [[simon-1962-architecture/main]] (complex-systems → complex-systems)
- [structural-analogy] Averaging over the fast phase to get slow equations ↔ complex-systems: mean-field approximation — both replace fast fluctuations by an average. — from [[strogatz-2024-nonlinear/ch07-limit-p2]] (complex-systems → complex-systems)
