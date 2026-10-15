---
id: condition-number
type: concept
fields: [linear-algebra]
n_sources: 9
tiers: [core, deep]
grounding: digests
sources: [deisenroth-2020-mml/ch07-continuous, spielman-2025-sagt/ch34-iterative, spielman-2025-sagt/ch36-preconditioning, spielman-2025-sagt/ch37-augmented, spielman-2025-sagt/ch38-fast, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch07-singular, strang-2023-introduction/ch08-linear, strang-2023-introduction/ch09-linear]
raw_ids: [condition number]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# condition-number

## Canon spine entry

- **condition number** (linear-algebra): σ_max/σ_min; how much input errors are amplified in solving Ax = b (grad)

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch07-continuous]] (p. 230): here $\sigma_{\max}/\sigma_{\min}$ of $A$, governs gradient-descent speed on $Ax=b$
- [[spielman-2025-sagt/ch34-iterative]] (p. 274): $\lambda_n/\lambda_1$ for symmetric $A$; ratio of extreme singular values in general; sets iteration counts [as `condition number`]
- [[spielman-2025-sagt/ch36-preconditioning]] (p. 287): here the relative condition $\kappa(A,B)=\beta/\alpha$, with $\alpha B\preceq A\preceq\beta B$
- [[spielman-2025-sagt/ch37-augmented]] (p. 298): here the relative $\kappa(L_G,L_H)$; it is submultiplicative across a chain of approximations, $\kappa(L_G,L_H)\le\kappa(L_G,L_{\widetilde G})\kappa(L_{\widetilde G},L_H)$
- [[spielman-2025-sagt/ch38-fast]] (p. 301): $\kappa$ is the condition number in the running time (p. 300); it also appears as the gap in the top eigenvalue $1-\kappa$ of $B$ [as `condition number`]
- [[strang-2023-introduction/app1-ranks]] (p. 407): relative condition = ‖A⁻¹‖‖A‖ = σ_max/σ_min [as `condition number`]
- [[strang-2023-introduction/ch07-singular]] (p. 306): $\sigma_1/\sigma_r$; squared when forming $AA^T$
- [[strang-2023-introduction/ch08-linear]] (p. 331): a large ratio of extreme eigenvalues of BᵀB (the Hilbert matrix) marks a bad basis
- [[strang-2023-introduction/ch09-linear]] (p. 344): λmax/λmin = 1/b of S; controls zig-zag and momentum rates

## Instances that use it

- [[expander-laplacian-solve]] — condition number about $1+2\epsilon$; fast iterative solve versus $\Omega(n^3)$ elimination — from [[spielman-2025-sagt/ch34-iterative]]

## Candidate bridges

- [structural-analogy] $\|Sv\|=\|v\|$ and $S^*S=I$ ↔ condition-number intuition: unitary maps have no error amplification (canon link; not stated in this unit). — from [[axler-2024-ladr/ch07-operators-p2]] (linear-algebra → other)
- [same-math] $\|T\|\,\|T^{-1}\|=s_1/s_n$ (from 7.85 and Exercise 10 of §7E) ↔ condition number — Example 7.90 gives $0.8\times10^6$ for the $1/(j^2+k)$ matrix; the text does not use the term. — from [[axler-2024-ladr/ch07-operators-p3]] (linear-algebra → unspecified)
- [same-math] condition number $\sigma_{\max}/\sigma_{\min}$ ↔ linear-algebra: condition number from the SVD — same quantity, here controlling gradient-descent speed. — from [[deisenroth-2020-mml/ch07-continuous]] (linear-algebra → linear-algebra)
- [structural-analogy] Dominating a multiple of $K_n$ ↔ condition numbers: $c$-approximation bounds the ratio of quadratic forms, as relative bounds on a matrix pair. — from [[spielman-2025-sagt/ch06-comparing]] (linear-algebra → other)
- [same-math] Forming $AA^T$ squares $\sigma_1/\sigma_r$ ↔ numerical analysis: squaring the condition number when solving via normal equations. — from [[strang-2023-introduction/ch07-singular]] (linear-algebra → other)
- [structural-analogy] Hilbert matrix BᵀB with large condition number ↔ regression: nearly collinear predictors give an ill-conditioned XᵀX — both are bad bases or near-dependent columns. — from [[strang-2023-introduction/ch08-linear]] (linear-algebra → other)
- [same-math] Zig-zag rate in 1/b ↔ linear-algebra: condition number λmax/λmin — b = λmin/λmax is exactly the author's setting. — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → linear-algebra)
- [metaphor] Eigengap as "how well-separated the communities are" ↔ condition number: both measure spectral separation affecting stability. — from [[vonluxburg-2007-spectralclustering/main]] (linear-algebra → other)
