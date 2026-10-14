---
id: spielman-2025-sagt/ch42-quadrature
work: spielman-2025-sagt
unit: Chapter 42 — Quadrature for the Finite Free Convolution
pages: 333-340
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Quadrature for the Finite Free Convolution

## L0 — One line
The expected characteristic polynomial of $A+QBQ^T$ over a Haar-random orthogonal $Q$ equals an average over the finite hyperoctahedral group, which gives an explicit coefficient formula for this expected polynomial, the finite free convolution.

## L1 — The gist (≤ 120 words)
Last lecture considered the expected characteristic polynomial of $A+\Pi B\Pi^T$ with a random permutation $\Pi$. This chapter treats a random orthogonal $Q$ chosen by Haar measure, the natural random choice. Such an average over a continuous group does not depend on the eigenvectors of $A$ and $B$, so it defines a product $p \boxplus_n q$ of characteristic polynomials. The key step is a quadrature result (an integral becomes a finite sum): the average over $\mathcal O(n)$ equals the average over the finite group $\mathcal B(n)$ of signed permutations. For diagonal matrices this average can be counted by hand, which gives a closed formula (42.1). A similar quadrature, over the symmetries of the simplex, handles permutations of matrices with constant row sums (Theorem 42.2.2).

**Prerequisites:** characteristic polynomial and determinant; orthogonal and rotation matrices; diagonalization; roots of unity; expectation over a finite group.

## L2 — Key ideas (5–10 bullets)
- $p\boxplus_n q := \mathbb E_{Q}\,\chi_x(A+QBQ^T)$ depends only on $p$ and $q$, by Haar invariance of $V^TQU$ (p. 334).
- Theorem 42.2.2: for symmetric $A,B$ with constant row sums, the permutation average gives $(x-(a+b))\,(p\boxplus_{n-1}q)$ (p. 334).
- Quadrature means an integral over a continuous domain becomes a finite sum; the model case is polynomials on the unit circle at roots of unity (p. 335).
- Lemma 42.3.1 gives a rotation-invariance route: a sum over equally spaced circle points is unchanged by shifting all points by $\theta$ (p. 336).
- Theorem 42.2.3: Haar average over $\mathcal O(n)$ equals average over $\mathcal B(n)$. It follows from Haar invariance plus Theorem 42.4.1, whose proof uses the group property of $\mathcal B(n)$ and the structure of $\mathcal O(n)$ (pp. 335–338).
- The key technical fact is that $\det(A+R_\theta BR_\theta^*)$ is a trigonometric polynomial of degree at most 2 in $\theta$ (a sum of terms $c_ke^{ik\theta}$ with $|k|\le2$; Lemma 42.5.2), so a 4-point rule suffices (pp. 338–339).
- Reducing to diagonal matrices and counting which permutations avoid overlap gives formula (42.1) (pp. 339–340).

## L3 — Walkthrough

### 42.1–42.2 Overview and the finite free convolution
- Overview (author): last lecture considered $\mathbb E\,\chi_x(A+\Pi B\Pi^T)$ for symmetric $A,B$. No nice expression is known for general $A,B$, but there is a very nice one when $A,B$ are Laplacian matrices or adjacency matrices of regular graphs. The goal is to prove simple analogs of the main quadrature results (from [MSS15d], [MSS15a]) and to sketch the rest (p. 333).
- Free probability studies operations on matrices in a large-dimension limit; there the matrices are determined by the moments of their spectrum, so the operations are independent of the eigenvectors (p. 333). The chapter studies a finite-dimensional analog: $\mathbb E_{Q\in\mathcal O(n)}\chi_x(A+QBQ^T)$ for symmetric $A,B$ (p. 333).
- Haar measure: the measure on $\mathcal O(n)$ with $S$ and $\{QP:Q\in S\}$ of equal measure for all $S$ and $P$ (p. 334). Example: the eigenvector matrix of a Gaussian random symmetric matrix is Haar distributed (p. 334).
- Independence from eigenvectors: write $A=VDV^T$, $B=UCU^T$. Then $\chi_x(VDV^T+QUCU^TQ^T)=\chi_x(D+(V^TQU)C(V^TQU)^T)$, and $V^TQU$ is again Haar distributed (p. 334).
- **Definition.** $p(x)\boxplus_n q(x) \overset{def}{=} \mathbb E_{Q\in\mathcal O(n)}\chi_x(A+QBQ^T)$, where $p=\chi_x(A)$, $q=\chi_x(B)$ (p. 334).
- **Theorem 42.2.1.** If $p=\sum_{i=0}^n x^{n-i}(-1)^ia_i$ and $q=\sum_{i=0}^n x^{n-i}(-1)^ib_i$, then
$$p\boxplus_n q=\sum_{k=0}^n x^{n-k}(-1)^k\sum_{i+j=k}\frac{(n-i)!\,(n-j)!}{n!\,(n-i-j)!}a_ib_j.\tag{42.1}$$
Walsh proved that if $p,q$ are real rooted, so is $p\boxplus_n q$ (p. 334).
- **Theorem 42.2.2.** Let $A,B$ be symmetric with $A\mathbf 1=a\mathbf 1$, $B\mathbf 1=b\mathbf 1$, and $\chi_x(A)=(x-a)p$, $\chi_x(B)=(x-b)q$. Then $\mathbb E_{\Pi\in S_n}\chi_x(A+\Pi B\Pi^T)=(x-(a+b))(p\boxplus_{n-1}q)$. The vector $\mathbf 1$ is an eigenvector with eigenvalue $a+b$ for every $\Pi$; the convolution appears orthogonal to it (p. 334).
- Motivation (author): it began as a lucky guess. The hoped-for nicest formula is bilinear. Examples with $B,q$ fixed showed the coefficients are linear in those of $p$ (p. 335).
- Let $\mathcal B(n)$ be the hyperoctahedral group: matrices $D\Pi$ with $D$ a $\pm1$ diagonal and $\Pi$ a permutation; it is a subgroup of $\mathcal O(n)$ (p. 335).
- **Theorem 42.2.3.** For all symmetric $A,B$: $\mathbb E_{Q\in\mathcal O(n)}\chi_x(A+QBQ^T)=\mathbb E_{P\in\mathcal B(n)}\chi_x(A+PBP^T)$. It is used to prove 42.2.1. The proof of 42.2.2 is similar (p. 335).

*Intuition note.* The random rotation hides the eigenvectors, so only the eigenvalues matter. The quadrature theorem says that, for these characteristic polynomials, a finite average already equals the full continuous average.

### 42.3 Quadrature
- Quadrature formulas evaluate integrals of a family of functions over a fixed continuous domain by summing the values at a fixed number of points. The author mentions a link with orthogonal polynomials but has no time for it (p. 335).
- Model case: for $\deg p<n$, $\int_0^{2\pi}p(e^{i\theta})d\theta=\frac1n\sum_{k=0}^{n-1}p(\omega^k)$, with $\omega=e^{2\pi i/n}$. Proof monomial by monomial. For $x^k$ with $k\ne0$ the integral is 0. For $0<|k|<n$ the sum $\sum_j\omega^{jk}=0$, since the roots are spread symmetrically. For $p=1$ both sides equal 1 (pp. 335–336).
- **Lemma 42.3.1.** For $p(x)=\sum_{|k|<n}c_kx^k$ and every $\theta$, $\sum_j p(e^{i(2\pi j/n+\theta)})=\sum_j p(e^{i2\pi j/n})$. Proof: for $x^k$ the shifted sum equals $e^{i\theta k}\sum_j(e^{i2\pi j/n})^k$. This is 0 for $k\neq0$, and the factor is 1 for $k=0$. The author notes that the lemma implies the quadrature formula above and that the identity can be checked numerically with a random $\theta$ (p. 336).

### 42.4 Quadrature by invariance
- Define $f_{A,B}(Q)=\det(A+QBQ^T)$. **Theorem 42.4.1:** for all $Q\in\mathcal O(n)$, $\mathbb E_{P\in\mathcal B(n)}f(P)=\mathbb E_{P\in\mathcal B(n)}f(QP)$ (p. 336).
- Proof of 42.2.3 (author works with determinants; the reduction from characteristic polynomials is not spelled out). Haar invariance gives $\int_{\mathcal O(n)}f(Q)=\int_{\mathcal O(n)}f(QP)$ for each $P\in\mathcal B(n)$. Hence $\mathbb E_P\int_Q f(QP)=\int_Q f(Q)$ (pp. 336–337). Since $\mathcal B(n)$ is discrete, swap the order of integration: $\int_Q f(Q)=\int_Q\mathbb E_P f(QP)=\int_Q\mathbb E_Pf(P)=\mathbb E_Pf(P)$. The second equality uses 42.4.1 (p. 337).

### 42.5 Structure of the orthogonal group
- Every matrix in $\mathcal O(n)$ is $DQ$ with $Q\in\mathcal{SO}(n)$ (determinant 1) and $D$ diagonal with first entry $\pm1$ and others 1. Every $Q\in\mathcal{SO}(n)$ is a product $Q_{1,2}Q_{1,3}\cdots Q_{n-1,n}$ of plane rotations (QR factorization computes this) (p. 337).
- So the author says it suffices to prove 42.4.1 for $Q=\mathrm{diag}(-1,1,\dots,1)$ (immediate, since it lies in $\mathcal B(n)$) and for a plane rotation. Take the plane $(1,2)$, with $R_\theta=\begin{pmatrix}\cos\theta&\sin\theta&0\\-\sin\theta&\cos\theta&0\\0&0&I_{n-2}\end{pmatrix}$ (p. 337).
- $\mathcal B(n)\ni R_\theta$ for $\theta\in\{0,\pi/2,\pi,3\pi/2\}$. By the group property, $\frac14\sum_{j=0}^3\mathbb E_P f(R_{2\pi j/4}P)=\mathbb E_Pf(P)$ (p. 337).
- **Lemma 42.5.1.** For all symmetric $A,B$ and all $\theta$: $\frac14\sum_{j=0}^3f_{A,B}(R_{\theta+2\pi j/4})=\frac14\sum_{j=0}^3f_{A,B}(R_{2\pi j/4})$. It implies $\mathbb E_Pf(P)=\mathbb E_Pf(Q_{1,2}P)$ for every $Q_{1,2}$, hence 42.4.1 and 42.2.3 (p. 338). (added step: $f_{A,B}(R_\theta P)=f_{A,PBP^T}(R_\theta)$, so the lemma applies with $B$ replaced by $PBP^T$.)
- Lemma 42.5.1 follows from Lemma 42.3.1 (taking $n=4$ is our reading) and **Lemma 42.5.2**: $f_{A,B}(R_\theta)=\sum_{k=-2}^2c_k(e^{i\theta})^k$ (p. 338).
- Proof of 42.5.2. From $\cos\theta=\frac12(e^{i\theta}+e^{-i\theta})$ and $\sin\theta=\frac{-i}2(e^{i\theta}-e^{-i\theta})$, the author diagonalizes the rotation as $U\,\mathrm{diag}(e^{i\theta},e^{-i\theta})\,U^*$ with $U=\begin{pmatrix}1&1\\i&-i\end{pmatrix}$. Then $R_\theta=U_nD_\theta U_n^*$, and
$$f(R_\theta)=\det(A+U_nD_\theta U_n^*BU_nD_\theta^*U_n^*)=\det(U_n^*AU_n+D_\theta U_n^*BU_nD_\theta^*)=\det(U_n^*AU_nD_\theta+D_\theta U_n^*BU_n).$$
$e^{i\theta}$ appears only in row and column 1, and $e^{-i\theta}$ only in row and column 2. Each term of the determinant has at most two factors $e^{i\theta}$ and two $e^{-i\theta}$, so $|k|\le2$ (pp. 338–339).
- The quadrature behind Theorem 42.2.2 sums over the symmetries of the regular $n$-simplex in $n-1$ dimensions instead of over $\mathcal B(n)$; the author says the proof is very similar. Rotations in coordinate planes are replaced by rotations of planes parallel to the affine span of triples of vertices (p. 339).

*Intuition note.* Rotating one plane changes the determinant like a short Fourier sum with at most 5 frequencies. Four equally spaced angles average such a sum exactly, so the finite average is unchanged when the group is shifted by a rotation, which is what Theorem 42.4.1 needs.

### 42.6 The formula
- The author observes that it suffices to compute for diagonal $A=\mathrm{diag}(\lambda_i)$ and $B=\mathrm{diag}(\mu_i)$, and that 42.2.3 makes this simple. Each $P\in\mathcal B(n)$ is $\Pi D$, and $\Pi DBD\Pi^T=\Pi B\Pi^T$ is diagonal with entries $\mu_{\pi(1)},\dots,\mu_{\pi(n)}$ (p. 339).
- Let $\lambda^S=\prod_{i\in S}\lambda_i$, so $a_i=\sum_{|S|=i}\lambda^S$. Write $p\boxplus_nq=\sum_kx^{n-k}(-1)^kc_k$ (p. 339).
- Case $k=n$: $c_n=\frac1{n!}\sum_\pi\prod_h(\lambda_h+\mu_{\pi(h)})=\frac1{n!}\sum_\pi\sum_{|S|=i}\lambda^S\prod_{h:\pi(h)\notin S}\mu_h$. The term $\lambda^S\mu^T$ needs $|T|=n-|S|$ and $\pi(T)\cap S=\emptyset$. This holds for a $1/\binom ni$ fraction of permutations. So $c_n=\sum_i\frac1{\binom ni}a_ib_{n-i}=\sum_i\frac{i!(n-i)!}{n!}a_ib_{n-i}$ (p. 339).
- General $k=i+j$: $\lambda^S\mu^T$ (with $|S|=i$, $|T|=j$) appears when $\pi(T)$ is disjoint from $S$. The probability is $\binom{n-i}{j}/\binom nj=\frac{(n-i)!(n-j)!}{n!(n-i-j)!}$, so $c_k=\sum_{i+j=k}a_ib_j\frac{(n-i)!(n-j)!}{n!(n-i-j)!}$, which is (42.1) (p. 340).

### 42.7 Open question (author)
For which discrete subgroups of $\mathcal O(n)$ does a result like 42.2.3 hold? Can one hold for a substantially smaller subgroup than the simplex symmetries (size $(n+1)!$)? (p. 340)

## Toy example (ours)
$n=2$, $A=\mathrm{diag}(1,3)$, $B=\mathrm{diag}(2,5)$. Then $a_1=4,\ a_2=3,\ b_1=7,\ b_2=10$.
- Direct average over the two permutations: $\frac12[(1+2)(3+5)+(1+5)(3+2)]=\frac12(24+30)=27$.
- Formula, $k=2$: $\frac{i!(2-i)!}{2!}$ gives $i=0$: $1\cdot b_2=10$; $i=1$: $\frac12a_1b_1=14$; $i=2$: $a_2=3$. Total $27$ ✓.
- $k=1$: $c_1=a_1+b_1=11$, since both coefficients equal 1. The direct expected trace is $4+7=11$ ✓.

## Concepts
- [[finite-free-convolution]] (new) — $p\boxplus_nq=\mathbb E_Q\chi_x(A+QBQ^T)$ over Haar $Q$ (p. 334)
- [[haar-measure]] (new) — the measure on $\mathcal O(n)$ invariant under multiplication by orthogonal matrices (p. 334)
- [[quadrature]] (new) — evaluating a continuous integral as a finite sum, for a family of functions (p. 335)
- [[hyperoctahedral-group]] (new) — $\mathcal B(n)$: signed permutation matrices, a subgroup of $\mathcal O(n)$ (p. 335)
- [[characteristic-polynomial]] — $\chi_x(M)$; here averaged over random matrices (p. 333)
- [[orthonormal-basis-orthogonal-matrix]] — $\mathcal O(n)$, with $\mathcal{SO}(n)$ built from plane rotations (p. 337)
- [[diagonalization]] — rotations diagonalized by a complex $U$ to expose $e^{\pm i\theta}$ (p. 338)

## Canonical instances
- [[roots-of-unity-quadrature]] — $\int p(e^{i\theta})d\theta$ equals an average at $n$th roots of unity for $\deg p<n$ (p. 335)
- [[ring-graph-eigenvectors]] — cited for $\sum_j\omega^{jk}=0$ (p. 336)

## Bridges (candidates)
- [structural-analogy] Haar-averaged characteristic polynomial ↔ free probability: operations independent of eigenvectors, in the finite-$n$ setting
- [same-math] Sum of roots of unity vanishing ↔ eigenvectors of the ring graph orthogonal to $\mathbf 1$
- [structural-analogy] Exactness of a 4-point rule for degree-2 trigonometric polynomials ↔ Gaussian quadrature (the author mentions a link with orthogonal polynomials but does not discuss it)

## Questions this raises
- Why can the reduction to $Q=\mathrm{diag}(-1,1,\dots)$ and plane rotations be justified from 42.4.1's form?
- Which smaller finite groups satisfy the quadrature (the author's open question, p. 340)?
- How does the simplex version prove 42.2.2 in detail?

## Reading notes
- Printed = pdf − 24. The chapter carries the banner "This Chapter Needs Editing".
- Pages 335–336: the identity $\int_0^{2\pi}p(e^{i\theta})d\theta=\frac1n\sum p(\omega^k)$ is printed without a $2\pi$ factor, and the text says both sides equal 1 for $p=1$. Strictly, the integral of 1 over $[0,2\pi]$ is $2\pi$. Presumably the integral is meant normalized.
- Page 336: Lemma 42.3.1 and its proof sum $j=0$ to $n$ ($n+1$ terms), while the roots are $j=0,\dots,n-1$.
- Page 338: with $U$ as printed, $UU^*=2I$, so $UDU^*=2R_\theta$. A factor $1/\sqrt2$ (normalization) is missing. Presumably this does not affect the argument.
- Page 339: the text writes $\mathcal B(n)$ elements as $D\Pi$ on p. 335 and $\Pi D$ on p. 339.
- Page 338: "We can use Lemma 42.3.1 to derive Lemma 42.5.1 follows from…" is garbled.
- The reduction of 42.4.1 to the cases $\mathrm{diag}(-1,1,\dots,1)$ and plane rotations is stated, not proved.
