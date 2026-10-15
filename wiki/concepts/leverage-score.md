---
id: leverage-score
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 3
n_works: 2
tiers: [deep]
grounding: digests
sources: [elhage-2022-superposition/main-p2, spielman-2025-sagt/ch13-random, spielman-2025-sagt/ch32-sparsification]
generated_by: build_kg.py
---

# leverage-score

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch13-random]] (p. 126): $\ell_e=w_eR_{\rm eff}(e)=\Gamma(e,e)$ [new]
- [[spielman-2025-sagt/ch32-sparsification]] (p. 261): $\ell_{a,b}=w_{a,b}R_{\rm eff}(a,b)$; sums to $n-1$ [new]

### llm

- [[elhage-2022-superposition/main-p2]]: maximal share of $\|Wx\|^2$ a row can contribute; sums to rank (Zhang comment) [new]

## Instances that use it

- [[leverage-score-edge-sampling]] — the sparsification algorithm of this chapter — from [[spielman-2025-sagt/ch32-sparsification]]
- [[sum-of-leverage-scores-is-n-minus-1]] — trace proof $\mathrm{Tr}(\Pi)=n-1$ — from [[spielman-2025-sagt/ch32-sparsification]]

## Candidate bridges

- [same-math] Feature dimensionality $D_i$ ↔ numerical linear algebra: leverage score, roughly equal when the vectors are in isotropic position (Zhang's argument). — from [[elhage-2022-superposition/main-p2]] (llm → linear-algebra)
