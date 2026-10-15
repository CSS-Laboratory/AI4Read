---
id: eigenspace
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch05-eigenvalues-p2, bryan-2006-eigenvector/main]
aliases: [eigenspace-v1]
generated_by: build_kg.py
---

# eigenspace

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `eigenspace-v1` — 1 digest(s)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch05-eigenvalues-p2]] (p. 164): $E(\lambda,T)=\operatorname{null}(T-\lambda I)$ [new]
- [[bryan-2006-eigenvector/main]] (p. 3): $V_1(A)$, the eigenspace for eigenvalue 1; its dimension decides uniqueness of scores [as `eigenspace-V1`; alias `eigenspace-v1`; new]

## Instances that use it

- [[ex-t-4z2-0-5z3]] — $T(z)=(4z_2,0,5z_3)$: eigenvectors too few, but generalized eigenspaces give $\mathbf C^3=G(0,T)\oplus G(5,T)$ — from [[axler-2024-ladr/ch08-operators]]

## Candidate bridges

- [structural-analogy] generalized eigenspace decomposition ↔ linear-algebra: spectral theorem — both split $V$ into $T$-invariant pieces, one per eigenvalue, without needing orthogonality in the first. — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [structural-analogy] Null-space coordinate vectors giving a 3D drawing ↔ spectral graph drawing: low-eigenspace vectors as vertex coordinates. — from [[spielman-2025-sagt/ch26-planar]] (linear-algebra → linear-algebra)
