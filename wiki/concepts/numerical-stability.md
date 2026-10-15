---
id: numerical-stability
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [spielman-2025-sagt/ch34-iterative, strang-2023-introduction/ch04-orthogonality-p2]
raw_ids: [numerical stability]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# numerical-stability

## Canon spine entry

- **numerical stability** (linear-algebra): whether an algorithm's rounding errors stay small (e.g., Householder QR vs. classical Gram–Schmidt) (grad)

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch34-iterative]] (p. 279): the naive polynomial form of Chebyshev is unstable in finite precision [as `numerical stability`]
- [[strang-2023-introduction/ch04-orthogonality-p2]] (pp. 183–184): modified Gram-Schmidt (one projection at a time) is more stable than (8); Householder reflections used in good software

## Candidate bridges

- [structural-analogy] Gershgorin disks (5.67) ↔ numerical stability / conditioning: small off-diagonal entries keep eigenvalues near the diagonal. — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [metaphor] factor-solve with caching ↔ numerical stability / conditioning: factor once, reuse; sensitivity of $A^{-1}b$ appears in exercise 11.26 — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → linear-algebra)
- [structural-analogy] raw-score variance instability (p. 193) ↔ numerical stability: algebraically equal formulas can differ in rounding behaviour. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
