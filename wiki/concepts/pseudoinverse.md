---
id: pseudoinverse
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 24
n_works: 6
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch06-inner-p2, axler-2024-ladr/ch07-operators-p3, boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch11-matrix, boyd-2018-vmls/ch12-least, boyd-2018-vmls/ch13-least, boyd-2018-vmls/ch15-multi, boyd-2018-vmls/ch16-constrained, deisenroth-2020-mml/ch02-linear-p1, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch06-probability-p2, spielman-2025-sagt/ch11-walks, spielman-2025-sagt/ch13-random, spielman-2025-sagt/ch14-approximating, spielman-2025-sagt/ch17-monotonicity, spielman-2025-sagt/ch32-sparsification, spielman-2025-sagt/ch33-linear, spielman-2025-sagt/ch35-conjugate, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch04-orthogonality-p1, strang-2023-introduction/ch04-orthogonality-p2, strang-2023-introduction/ch08-linear, strang-2023-introduction/ch10-learning, vonluxburg-2007-spectralclustering/main]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# pseudoinverse

## Canon spine entry

- **pseudoinverse** (linear-algebra): A⁺ = VΣ⁺Uᵀ; the minimum-norm least-squares solution (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch06-inner-p2]] (pp. 221–222): $T^\dagger=(T|_{(\operatorname{null}T)^\perp})^{-1}P_{\operatorname{range}T}$; best-fit, minimum-norm solution
- [[axler-2024-ladr/ch07-operators-p3]] (p. 275): $T^\dagger$, obtained from the SVD by swapping $e,f$ and inverting each $s_k$ (7.78)
- [[boyd-2018-vmls/app-appendices]] (p. 442): $3mn^2$ flops (tall), $3m^2n$ (wide)
- [[boyd-2018-vmls/ch11-matrix]] (pp. 214–215): here $A^\dagger=(A^TA)^{-1}A^T$ for independent columns, $A^T(AA^T)^{-1}$ for independent rows; equals $A^{-1}$ if square invertible. The text defines it for any matrix but only for these cases as a one-sided inverse
- [[boyd-2018-vmls/ch12-least]] (p. 229): $A^\dagger=(A^TA)^{-1}A^T$ for independent columns; $\hat x=A^\dagger b$
- [[boyd-2018-vmls/ch13-least]] (p. 247): θ̂ = A†yᵈ = (AᵀA)⁻¹Aᵀyᵈ when A has independent columns
- [[boyd-2018-vmls/ch15-multi]] (p. 337): reused; exact inversion $x=A^\dagger y$ (p. 316); defined as a Tikhonov limit in exercise 15.11
- [[boyd-2018-vmls/ch16-constrained]] (p. 351): $C^\dagger=C^T(CC^T)^{-1}$ gives the least-norm solution
- [[deisenroth-2020-mml/ch02-linear-p1]] (pp. 34–35): here $(A^\top A)^{-1}A^\top$ for A with independent columns; gives the minimum-norm least-squares solution
- [[deisenroth-2020-mml/ch03-analytic]] (p. 86): here $(B^\top B)^{-1}B^\top$ for full-column-rank $B$
- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 204): $(A^\top A)^{-1}A^\top$ used to invert $y=Ax$ when $A$ is not invertible
- [[spielman-2025-sagt/ch11-walks]] (p. 110): $L^+=\sum_{\lambda_i\ne0}\lambda_i^{-1}\psi_i\psi_i^T$
- [[spielman-2025-sagt/ch13-random]] (p. 127): $L_G^+$ with $L_G^+L_G=\Pi$
- [[spielman-2025-sagt/ch14-approximating]] (pp. 129, 131): $L^+$, whose square root or any factor $M$ with $M^TM=L^+$ gives the distances
- [[spielman-2025-sagt/ch17-monotonicity]] (p. 149): $v=L^+i_{ext}$ solves for voltages
- [[spielman-2025-sagt/ch32-sparsification]] (p. 260): $L_G^{+/2}$ is the square root of $L_G^+$
- [[spielman-2025-sagt/ch33-linear]] (p. 264): $L_G^{+/2}$ is used to normalise the Laplacian
- [[spielman-2025-sagt/ch35-conjugate]] (p. 285): for a Laplacian, we want a polynomial in $L$ approximating it; exact solving would need $p(L)L=\Pi$
- [[strang-2023-introduction/app1-ranks]] (p. 402): A⁺ = VΣ⁺Uᵀ; x⁺ = A⁺b is the shortest least-squares solution
- [[strang-2023-introduction/ch04-orthogonality-p1]] (p. 169): only previewed: the shortest least squares solution x⁺ in the row space
- [[strang-2023-introduction/ch04-orthogonality-p2]] (pp. 190–191): $A^+$: inverts $A$ from row space to column space, zero on the left nullspace; minimum-norm least-squares solution
- [[strang-2023-introduction/ch08-linear]] (p. 313, 320): the integral is the pseudoinverse of the derivative, with A⁺A ≠ I and AA⁺ = I
- [[strang-2023-introduction/ch10-learning]] (p. 382): not named in the text; only the minimum norm solution with no nullspace component appears
- [[vonluxburg-2007-spectralclustering/main]] (p. 15): $L^\dagger=U\Lambda^\dagger U'$ computes commute distance

## Instances that use it

- [[pseudoinverse-f4-to-f3]] — worked $T^\dagger$ for $T(a,b,c,d)=(a+b+c,2c+d,0)$ — from [[axler-2024-ladr/ch06-inner-p2]]
- [[derivative-as-linear-map]] — d/dx on polynomials has matrix [[0,1,0],[0,0,2]], a kernel of constants, and the integral as pseudoinverse — from [[strang-2023-introduction/ch08-linear]]

## Candidate bridges

- [same-math] Pseudoinverse $T^\dagger$ (6.68) ↔ linear-algebra: $A^+=V\Sigma^+U^\top$ of the concept list — same operator. The SVD formula is not in this unit; the author points to 7.78. — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → linear-algebra)
- [same-math] Tikhonov limit $\lim_{\lambda\to0}(A^TA+\lambda I)^{-1}A^T$ ↔ pseudoinverse: exercise 15.11 defines $A^\dagger$ this way for any matrix. — from [[boyd-2018-vmls/ch15-multi]] (linear-algebra → linear-algebra)
- [same-math] effective resistance $i^TL^+i$ ↔ linear algebra: pseudoinverse solving $Lv=b$ — the same quadratic form. — from [[spielman-2025-sagt/ch17-monotonicity]] (linear-algebra → linear-algebra)
- [same-math] $A^+=V\Sigma^+U^{\mathsf T}$ ↔ SVD (Ch. 7): the same pseudoinverse (p. 195). — from [[strang-2023-introduction/ch04-orthogonality-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Double descent's minimum-norm solution ↔ linear algebra: pseudoinverse solution of underdetermined Ax = b — the unit's setting is nonlinear and it does not mention the pseudoinverse — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)
- [same-math] $L^\dagger$ and commute distance ↔ pseudoinverse: $A^+=V\Sigma^+U^T$ restricted to non-zero eigenvalues. — from [[vonluxburg-2007-spectralclustering/main]] (linear-algebra → linear-algebra)
