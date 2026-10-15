---
id: span
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 6
n_works: 3
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch02-finite, axler-2024-ladr/ch03-linear-p1, deisenroth-2020-mml/ch02-linear-p2, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch03-four-p1, strang-2023-introduction/ch03-four-p2]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# span

## Canon spine entry

- **span** (linear-algebra): all linear combinations of a set of vectors; the "reachable" subspace (HS)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch02-finite]] (p. 29): the set of all linear combinations of a list; the smallest subspace containing it; span of empty list is $\{0\}$
- [[axler-2024-ladr/ch03-linear-p1]] (p. 54, 62–63): used throughout the proofs
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 44): set of all linear combinations of a set of vectors; $V=\mathrm{span}[\mathcal A]$ if it spans $V$
- [[strang-2023-introduction/ch01-vectors]] (p. 21): all linear combinations of a set of vectors; the span of the columns is the column space
- [[strang-2023-introduction/ch03-four-p1]] (p. 88): all combinations of a set S; the smallest vector space containing S; independence not required
- [[strang-2023-introduction/ch03-four-p2]] (p. 118): all combinations; the columns of A span $C(A)$

## Instances that use it

- [[example-span-17-4-2]] — $(17,-4,2)$ is in, and $(17,-4,5)$ is not in, the span of $(2,1,-3),(1,-2,4)$ — from [[axler-2024-ladr/ch02-finite]]
- [[annihilator-of-span-e1-e2]] — U⁰ = span(φ₃,φ₄,φ₅) in (𝐑⁵)′ — from [[axler-2024-ladr/ch03-linear-p3]]
- [[squad-v1-v2]] — span-extraction QA, with a [CLS]-span null answer for v2.0 — from [[devlin-2019-bert/main]]
- [[life-span-prediction]] — Gaussian prior, nonlinear prediction function — from [[griffiths-2006-optimal/main]]
- [[bert]] — encoder, 340M parameters, masked-word pre-training, fine-tuned for classification, NER, span prediction — from [[prince-2023-udl/ch12-transformers]]

## Candidate bridges

- [structural-analogy] Sum of subspaces = smallest containing subspace ↔ span (canon link; not stated in this unit): both are "everything reachable by adding". — from [[axler-2024-ladr/ch01-vector]] (linear-algebra → linear-algebra)
- [structural-analogy] reducing a spanning list to a basis (2.30) ↔ numerical methods: a greedy, left-to-right procedure that keeps only vectors outside the span of earlier ones — compare with Gram–Schmidt in the canon. — from [[axler-2024-ladr/ch02-finite]] (linear-algebra → other:numerical-methods)
- [same-math] $v,Tv,T^2v,\dots$ dependent ⇒ polynomial kills $v$ ↔ Krylov subspaces: the span of $v,Tv,\dots,T^{k-1}v$ (Ex. 5B.23 says this span is invariant when $k=\dim V$). — from [[axler-2024-ladr/ch05-eigenvalues-p1]] (linear-algebra → other:krylov-subspaces)
- [same-math] $D_q=X_q'TS^{-1}$ ↔ linear-algebra: coordinates of the projection of a vector onto the span of the columns of $T$ (since $T'T=I$, $T'X_q$ gives the coordinates, then rescaled by $S^{-1}$). — from [[deerwester-1990-lsa/main]] (linear-algebra → linear-algebra)
- [structural-analogy] $\boldsymbol w=\sum\alpha_ny_n\boldsymbol x_n$ ↔ column space/span: the solution lives in the row space (span) of the data matrix $\boldsymbol X$. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → linear-algebra)
- [structural-analogy] Orthogonal-projection estimate ↔ statistics: least-squares regression as projection onto a span — both minimize squared error by making the residual orthogonal to the regressors. — from [[kalman-1960-filtering/main]] (control-theory → other:statistics)
- [structural-analogy] Burt's leader as broker "at the edge" ↔ structural holes in network theory: the leader spans group boundaries. — from [[rogers-2003-diffusion/ch08-diffusion-p1]] (communication-theory → other:structural-holes-in-network)
- [metaphor] "Portable method" ↔ methodological individualism across disciplines (economics, sociology, law) — the text only says the approach spans them. — from [[shepsle-2010-analyzing/ch17-final]] (political-science → unspecified)
