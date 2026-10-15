---
id: eigenvector-eigenvalue
type: concept
fields: [linear-algebra, information-theory]
n_sources: 31
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch05-eigenvalues-p1, axler-2024-ladr/ch05-eigenvalues-p2, axler-2024-ladr/ch07-operators-p1, axler-2024-ladr/ch08-operators, axler-2024-ladr/ch09-multilinear-p2, brin-1998-anatomy/main, bryan-2006-eigenvector/main, deerwester-1990-lsa/main, deisenroth-2020-mml/ch04-matrix-p1, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch10-dimensionality, mackay-2003-information/ch51-appendices, spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch02-eigenvalues, spielman-2025-sagt/ch03-laplacian, spielman-2025-sagt/ch05-fundamental, spielman-2025-sagt/ch07-cayley, spielman-2025-sagt/ch09-strongly, spielman-2025-sagt/ch16-lov, spielman-2025-sagt/ch23-spectral, spielman-2025-sagt/ch26-planar, spielman-2025-sagt/ch31-psrgs, spielman-2025-sagt/ch38-fast, spielman-2025-sagt/ch40-testing, strang-2023-introduction/app10-computer, strang-2023-introduction/ch06-eigenvalues-p1, strang-2023-introduction/ch06-eigenvalues-p2, strang-2023-introduction/ch06-eigenvalues-p3, strang-2023-introduction/ch07-singular, strang-2023-introduction/ch08-linear, vonluxburg-2007-spectralclustering/main]
raw_ids: [eigenvector / eigenvalue]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# eigenvector-eigenvalue

## Canon spine entry

- **eigenvector / eigenvalue** (linear-algebra): a direction the map only stretches, Av = λv (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch05-eigenvalues-p1]] (pp. 134–135): nonzero $v$ with $Tv=\lambda v$; $\lambda$ is the eigenvalue; same as the canon meaning, defined for operators on any $\mathbf F$
- [[axler-2024-ladr/ch05-eigenvalues-p2]] (p. 157): read off the diagonal of a triangular matrix (5.41) [as `eigenvector / eigenvalue`]
- [[axler-2024-ladr/ch07-operators-p1]] (pp. 233, 237): real eigenvalues for self-adjoint operators; shared eigenvectors for normal ones
- [[axler-2024-ladr/ch08-operators]] (p. 301): $Tv=\lambda v$; generalized to powers of $T-\lambda I$
- [[axler-2024-ladr/ch09-multilinear-p2]] (pp. 358–359): $\lambda$ is an eigenvalue iff $\det(\lambda I-T)=0$. Over $\mathbf C$, $\det T$ is the product of eigenvalues with multiplicity [as `eigenvector / eigenvalue`]
- [[brin-1998-anatomy/main]] (pdf 4): the paper only states that PageRank "corresponds to the principal eigenvector of the normalized link matrix" and does not derive this [as `eigenvector / eigenvalue`]
- [[bryan-2006-eigenvector/main]] (p. 3): here, scores solve $Ax=x$, an eigenvector for $\lambda=1$
- [[deerwester-1990-lsa/main]] (pdf 13): footnote 4: $T_0$ and $D_0$ are eigenvector matrices of $XX'$ and $X'X$, with eigenvalues $S_0^2$
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 105–106): $Ax=\lambda x$ with $x\neq0$ [as `eigenvector / eigenvalue`]
- [[deisenroth-2020-mml/ch04-matrix-p2]] (pp. 123–124): right-singular vectors are eigenvectors of $A^\top A$, with $\sigma_i^2=\lambda_i$ [as `eigenvector / eigenvalue`]
- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 322): principal components are eigenvectors of $S$; the eigenvalue is the variance along them [as `eigenvector / eigenvalue`]
- [[spielman-2025-sagt/ch01-introduction]] (p. 5): $M\psi=\lambda\psi$, $\psi\ne0$
- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 21): $M\psi=\mu\psi$
- [[spielman-2025-sagt/ch03-laplacian]] (p. 30): $\mathbf 1$ has eigenvalue 0; $\psi_2,\dots$ give drawing coordinates [as `eigenvector / eigenvalue`]
- [[spielman-2025-sagt/ch05-fundamental]] (pp. 44–52): computed explicitly for the fundamental graphs [as `eigenvector / eigenvalue`]
- [[spielman-2025-sagt/ch07-cayley]] (p. 65, p. 68): characters ψ_b, x_k are eigenvectors for all generator sets
- [[spielman-2025-sagt/ch09-strongly]] (p. 85): here $k$ (multiplicity 1), $r>s$ with multiplicities $f,g$
- [[spielman-2025-sagt/ch16-lov]] (p. 146): ψ with Wψ = (1−λ)ψ, orthogonal to constants
- [[spielman-2025-sagt/ch23-spectral]] (p. 190): second eigenvector of the adjacency matrix used as a partition indicator
- [[spielman-2025-sagt/ch26-planar]] (p. 215): used with multiplicity; minimal-support eigenvectors [as `eigenvector / eigenvalue`]
- [[spielman-2025-sagt/ch31-psrgs]] (pp. 254–255): $W\mathbf 1=\mathbf 1$; the other eigenvalues have $|\omega_i|\le1/10$
- [[spielman-2025-sagt/ch38-fast]] (p. 304): eigenvalues of $D^{-1}A$ control pairs [as `eigenvector / eigenvalue`]
- [[spielman-2025-sagt/ch40-testing]] (p. 319): $d$ (multiplicity 1) plus two roots $r>s$ of $\lambda^2=(\alpha-\beta)\lambda+d-\beta$
- [[strang-2023-introduction/app10-computer]] (p. 415): the rotation axis is a line of eigenvectors with λ = 1 [as `eigenvector / eigenvalue`]
- [[strang-2023-introduction/ch06-eigenvalues-p1]] (p. 216, p. 217): x ≠ 0 with Ax = λx; λ is the stretching factor [as `eigenvector / eigenvalue`]
- [[strang-2023-introduction/ch06-eigenvalues-p2]] (p. 234): Ax = λx; distinct eigenvalues give independent eigenvectors
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 271): direction only scaled by A; here it gives pure solutions $e^{\lambda t}x$
- [[strang-2023-introduction/ch07-singular]] (p. 290; SPD case p. 286, p. 288): $\sigma_i^2$ are eigenvalues of $A^TA$ and $AA^T$; for SPD $S$, $\sigma_i=\lambda_i$
- [[strang-2023-introduction/ch08-linear]] (p. 322): used as a basis that makes the matrix Λ
- [[vonluxburg-2007-spectralclustering/main]] (p. 3): used with eigenvalues ordered increasingly; "first k" means smallest

### information-theory

- [[mackay-2003-information/ch51-appendices]] (pp. 606–607): left/right eigenvectors, degeneracy, principal eigenvector, orthonormal set for symmetric matrices [new]
