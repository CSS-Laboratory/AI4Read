---
id: spectral-theorem
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 17
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch07-operators-p1, axler-2024-ladr/ch07-operators-p2, axler-2024-ladr/ch07-operators-p3, axler-2024-ladr/ch09-multilinear-p1, deisenroth-2020-mml/ch04-matrix-p1, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch10-dimensionality, eckart-1936-lowrank/main, spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch02-eigenvalues, spielman-2025-sagt/ch04-adjacency, spielman-2025-sagt/ch11-walks, spielman-2025-sagt/ch31-psrgs, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch06-eigenvalues-p2, strang-2023-introduction/ch06-eigenvalues-p3, strang-2023-introduction/ch10-learning]
raw_ids: [spectral theorem]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# spectral-theorem

## Canon spine entry

- **spectral theorem** (linear-algebra): real symmetric (self-adjoint) matrices have real eigenvalues and an orthonormal eigenbasis, S = QΛQᵀ (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch07-operators-p1]] (pp. 245–246): real: self-adjoint ⟺ orthonormal eigenbasis; complex: normal ⟺ orthonormal eigenbasis (pp. 245–246). Here stated for operators, not only symmetric matrices.
- [[axler-2024-ladr/ch07-operators-p2]] (pp. 252–253, 262): used for the eigenbasis behind 7.38, 7.39, 7.55 [as `spectral theorem`]
- [[axler-2024-ladr/ch07-operators-p3]] (pp. 273–274): used on $T^*T$ to build the SVD; the SVD is compared with it
- [[axler-2024-ladr/ch09-multilinear-p1]] (p. 339): real spectral theorem used to get an orthonormal diagonalisation in 9.13
- [[deisenroth-2020-mml/ch04-matrix-p1]] (p. 111): symmetric ⇒ real eigenvalues and an orthonormal eigenbasis, $A=PDP^\top$ [as `spectral theorem`]
- [[deisenroth-2020-mml/ch04-matrix-p2]] (pp. 123–124): used to diagonalise $A^\top A$ and $AA^\top$ [as `spectral theorem`]
- [[deisenroth-2020-mml/ch10-dimensionality]] (pp. 322–323): used to get an orthonormal eigenbasis of the symmetric $S$ and $\hat S$ [as `spectral theorem`]
- [[eckart-1936-lowrank/main]] (pp. 213–214): Theorem II generalises the commuting-symmetric-matrices result; $u$ comes from diagonalising the symmetric $\alpha\alpha'$
- [[spielman-2025-sagt/ch01-introduction]] (p. 5): real symmetric $M$ has real eigenvalues and an orthonormal eigenbasis
- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 26): symmetric $M=\sum\mu_i\psi_i\psi_i^T$ with orthonormal $\psi_i$; proved here by optimization
- [[spielman-2025-sagt/ch04-adjacency]] (p. 39): used (cited, not restated) to simplify the symmetric case
- [[spielman-2025-sagt/ch11-walks]] (p. 110): orthonormal eigenbasis used in Claim 11.8.2
- [[spielman-2025-sagt/ch31-psrgs]] (p. 255): used implicitly: for symmetric $M$, the norm equals the largest $|$eigenvalue$|$
- [[strang-2023-introduction/app1-ranks]] (p. 401): S = QΛQᵀ for real symmetric S [as `spectral theorem`]
- [[strang-2023-introduction/ch06-eigenvalues-p2]] (p. 246): real symmetric S = QΛQᵀ, real λ, orthonormal q
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 264): symmetric/Hermitian S = QΛQ̄ᵀ via Schur's theorem
- [[strang-2023-introduction/ch10-learning]] (p. 397): V = QΛQᵀ with λᵢ ≥ 0 [as `spectral theorem`]

## Candidate bridges

- [structural-analogy] Simultaneous diagonalization of commuting operators (5.76) ↔ spectral theorem: orthonormal eigenbasis for symmetric matrices (the text only points forward to 7.29, 7.31). — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [same-math] spectral theorem for real symmetric matrices ($S=Q\Lambda Q^{\mathrm t}$) ↔ linear-algebra canon "spectral theorem": 7.29 in matrix form (orthonormal basis ↔ columns of $Q$). — from [[axler-2024-ladr/ch07-operators-p1]] (linear-algebra → linear-algebra)
- [structural-analogy] generalized eigenspace decomposition ↔ linear-algebra: spectral theorem — both split $V$ into $T$-invariant pieces, one per eigenvalue, without needing orthogonality in the first. — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [same-math] Diagonalising a symmetric form in an orthonormal basis (9.13) ↔ spectral theorem: it follows from that theorem, using $C^{-1}=C^{\mathrm t}$. — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → linear-algebra)
- [same-math] Footnote 4 (SVD vs eigen-analysis of $XX'$, $X'X$) ↔ spectral theorem for symmetric matrices $S=Q\Lambda Q^\top$; eigenvalues equal squared singular values. — from [[deerwester-1990-lsa/main]] (linear-algebra → unspecified)
- [same-math] covariance matrix symmetric PSD (p. 190) ↔ linear-algebra: spectral theorem — real symmetric PSD matrices have orthonormal eigenbases and nonnegative eigenvalues. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [same-math] Spectral theorem S = QΛQᵀ ↔ PCA: eigen-decomposition of a covariance matrix gives orthogonal principal directions. — from [[strang-2023-introduction/ch06-eigenvalues-p2]] (linear-algebra → linear-algebra)
