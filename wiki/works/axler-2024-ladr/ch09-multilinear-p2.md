---
id: axler-2024-ladr/ch09-multilinear-p2
work: axler-2024-ladr
unit: "9 Multilinear Algebra and Determinants (part 2/2): 9C Determinants, 9D Tensor Products"
pages: 354–382
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Determinants and Tensor Products (Axler, §9C–9D)

## L0 — One line
The determinant of an operator is the scalar by which the operator acts on the one-dimensional space of alternating $n$-linear forms (functions linear in each argument that vanish when two arguments are equal), and tensor products are built, also without bases, as spaces of bilinear functionals (functions linear in each of two arguments) on the dual spaces.

## L1 — The gist (≤ 120 words)
How can the determinant be defined without bases and without the $n!$-term formula? Axler defines $\det T$ as the scalar with $\alpha_T=(\det T)\alpha$ for alternating $n$-linear forms $\alpha$. The matrix determinant, the permutation formula, multiplicativity, the invertibility test, the eigenvalue product (over $\mathbf C$), the characteristic polynomial, Cayley–Hamilton for real spaces, Hadamard's inequality and the Vandermonde determinant are then derived, some with help from earlier results. Then a second question: how do we multiply $v\in V$ by $w\in W$ in a basis-free way? Answer: $V\otimes W=\mathcal B(V',W')$. It has dimension $(\dim V)(\dim W)$, turns bilinear maps into linear maps, and carries a natural inner product.

**Prerequisites:** alternating multilinear forms and the permutation formula 9.36 (part 1 of chapter 9); eigenvalues; upper-triangular matrices; dual space; inner products; unitary and positive operators; singular values; QR factorization; linear map lemma.

## L2 — Key ideas
- $\det T$ is defined by $\alpha_T=(\det T)\alpha$ on the one-dimensional space $V_{\rm alt}^{(\dim V)}$. The determinant of a matrix is the determinant of the associated operator on $\mathbf F^n$ (pp. 354–355).
- Columns-to-determinant is the alternating $n$-linear form taking the identity to 1. This gives the $n!$-term permutation formula and $\det=\prod\lambda_k$ for triangular matrices (pp. 355–356).
- $\det(ST)=\det S\det T$ has a short proof. $T$ is invertible iff $\det T\neq0$. $\det$ is a similarity invariant, so $\det T=\det\mathcal M(T)$ in any basis (pp. 357–359).
- Over $\mathbf C$, $\det T$ is the product of the eigenvalues with multiplicity. $\det(zI-T)$ defines the characteristic polynomial for real and complex spaces, which gives Cayley–Hamilton for real spaces and the trace/determinant coefficients (pp. 359, 363–364).
- Transpose invariance gives row/column rules, which justify Gaussian elimination for computing determinants (pp. 360–361).
- On inner product spaces: unitary means $|\det|=1$, positive means $\det\ge0$, $|\det T|$ is the product of singular values, and $T$ scales volume by $|\det T|$ (pp. 362–363).
- Hadamard's inequality bounds $|\det A|$ by the product of column norms. The Vandermonde determinant is $\prod_{j<k}(\beta_k-\beta_j)$, proved by switching between matrices and maps (pp. 365–366).
- $V\otimes W:=\mathcal B(V',W')$, with $(v\otimes w)(\varphi,\tau)=\varphi(v)\tau(w)$. It has dimension $(\dim V)(\dim W)$, and products of basis vectors form a basis (pp. 371–373).
- Universal property: bilinear maps on $V\times W$ correspond one-to-one to linear maps on $V\otimes W$ (p. 375).
- $V\otimes W$ has a unique inner product with $\langle v\otimes w,u\otimes x\rangle=\langle v,u\rangle\langle w,x\rangle$. Everything extends to $m$ factors (pp. 376–380).

## L3 — Walkthrough

Notation: $V_{\rm alt}^{(m)}$ is the space of alternating $m$-linear forms on $V$ (multilinear, zero whenever two arguments are equal). $n=\dim V$ unless stated.

### 9C Defining the Determinant

**9.40 Definition.** For $m$ a positive integer, $T\in\mathcal L(V)$ and $\alpha\in V_{\rm alt}^{(m)}$, define $\alpha_T\in V^{(m)}_{\rm alt}$ by
$$\alpha_T(v_1,\dots,v_m)=\alpha(Tv_1,\dots,Tv_m).$$
(p. 354) It is alternating because $v_j=v_k$ ($j\ne k$) gives $Tv_j=Tv_k$, so $\alpha_T(v_1,\dots,v_m)=\alpha(Tv_1,\dots,Tv_m)=0$. So $\alpha\mapsto\alpha_T$ is a linear map $V_{\rm alt}^{(m)}\to V_{\rm alt}^{(m)}$ (p. 354).

Since $\dim V_{\rm alt}^{(\dim V)}=1$ (9.37), every linear map of this space to itself is multiplication by a unique scalar (p. 354).

**9.41 Definition.** $\det T$ is the unique number in $\mathbf F$ with $\alpha_T=(\det T)\alpha$ for all $\alpha\in V_{\rm alt}^{(\dim V)}$ (p. 354).

**9.42 Examples** (p. 354), with $n=\dim V$:
- $I$: $\alpha_I=\alpha$, so $\det I=1$.
- $\lambda\in\mathbf F$: $\alpha_{\lambda I}=\lambda^n\alpha$, so $\det(\lambda I)=\lambda^n$.
- $\alpha_{\lambda T}=\lambda^n\alpha_T=\lambda^n(\det T)\alpha$, so $\det(\lambda T)=\lambda^n\det T$.
- If $e_1,\dots,e_n$ is a basis of eigenvectors with eigenvalues $\lambda_k$, then $\alpha_T(e_1,\dots,e_n)=\alpha(\lambda_1e_1,\dots,\lambda_ne_n)=(\lambda_1\cdots\lambda_n)\alpha(e_1,\dots,e_n)$. If $\alpha\neq0$, then 9.39 gives $\alpha(e_1,\dots,e_n)\ne0$. Hence $\det T=\lambda_1\cdots\lambda_n$.

*Intuition note.* The space of "signed volume" functions on $n$ vectors is a single line. An operator maps that line to itself by a scalar, and that scalar is the determinant. No basis is needed.

**9.43 Definition.** For an $n\times n$ matrix $A$ over $\mathbf F$, let $T\in\mathcal L(\mathbf F^n)$ have matrix $A$ in the standard basis. Then $\det A:=\det T$ (p. 355).

**9.44 Examples.** The identity matrix has determinant 1. A diagonal matrix with $\lambda_1,\dots,\lambda_n$ on the diagonal has determinant $\lambda_1\cdots\lambda_n$, because the standard basis is an eigenbasis (p. 355).

**9.45 Determinant is an alternating multilinear form.** Writing $(v_1\ \cdots\ v_n)$ for the matrix with columns $v_k$, the map $v_1,\dots,v_n\mapsto\det(v_1\ \cdots\ v_n)$ is an alternating $n$-linear form on $\mathbf F^n$ (p. 355).

*Proof.* Let $e_1,\dots,e_n$ be the standard basis and $T$ the operator with $Te_k=v_k$. Its matrix is $(v_1\cdots v_n)$. Take an alternating $n$-linear form $\alpha$ with $\alpha(e_1,\dots,e_n)=1$. Then
$$\det(v_1\ \cdots\ v_n)=\det T=(\det T)\,\alpha(e_1,\dots,e_n)=\alpha(Te_1,\dots,Te_n)=\alpha(v_1,\dots,v_n),$$
where the third step is the definition of $\det T$. So the map is $\alpha$ (p. 355). A matrix with two identical columns therefore has determinant 0 (p. 356).

**9.46 Formula for determinant of a matrix.**
$$\det A=\sum_{(j_1,\dots,j_n)\in\operatorname{perm}n}\bigl(\operatorname{sign}(j_1,\dots,j_n)\bigr)A_{j_1,1}\cdots A_{j_n,n}.$$
*Proof.* Apply 9.36 (part 1, not on these pages) with $V=\mathbf F^n$, the standard basis, and $\alpha=\det(v_1\cdots v_n)$ from 9.45. With $v_k$ the $k$th column of $A$, each $b_{j,k}$ of 9.36 equals $A_{j,k}$. Also $\alpha(e_1,\dots,e_n)=\det I=1$, so 9.36 becomes the stated formula (p. 356).

**9.47 Examples** (p. 356).
- $2\times2$: $\det A=A_{1,1}A_{2,2}-A_{2,1}A_{1,2}$.
- $3\times3$: $\det A=A_{1,1}A_{2,2}A_{3,3}-A_{2,1}A_{1,2}A_{3,3}-A_{3,1}A_{2,2}A_{1,3}-A_{1,1}A_{3,2}A_{2,3}+A_{3,1}A_{1,2}A_{2,3}+A_{2,1}A_{3,2}A_{1,3}$.

The sum has $n!$ terms. $10!$ is over three million and $100!$ is about $10^{158}$, so 9.46 is not a viable way to compute determinants (p. 356).

**9.48 Upper-triangular matrix.** If $A$ is upper-triangular with diagonal $\lambda_1,\dots,\lambda_n$, then $\det A=\lambda_1\cdots\lambda_n$.
*Proof.* If $(j_1,\dots,j_n)\ne(1,\dots,n)$, then $j_k>k$ for some $k$, so $A_{j_k,k}=0$. Only the identity permutation contributes, and $A_{k,k}=\lambda_k$ (p. 356).

### Properties of Determinants

**9.49 Multiplicative.** (a) $\det(ST)=(\det S)(\det T)$ for $S,T\in\mathcal L(V)$. (b) $\det(AB)=(\det A)(\det B)$ for square matrices of the same size (p. 357).

*Proof.* (a) For $\alpha\in V_{\rm alt}^{(n)}$:
$$\alpha_{ST}(v_1,\dots,v_n)=\alpha(STv_1,\dots,STv_n)=(\det S)\alpha(Tv_1,\dots,Tv_n)=(\det S)(\det T)\alpha(v_1,\dots,v_n).$$
The three equalities use the definitions of $\alpha_{ST}$, of $\det S$ and of $\det T$. (b) Take $S,T\in\mathcal L(\mathbf F^n)$ with $\mathcal M(S)=A$, $\mathcal M(T)=B$ in the standard basis. Then $\mathcal M(ST)=AB$ (3.43), so $\det(AB)=\det(ST)=(\det S)(\det T)=(\det A)(\det B)$ (p. 357).

**9.50 Invertible iff nonzero determinant.** $T\in\mathcal L(V)$ is invertible iff $\det T\ne0$. If $T$ is invertible, $\det(T^{-1})=1/\det T$ (p. 357).

*Proof.* ($\Rightarrow$) $1=\det I=\det(TT^{-1})=(\det T)(\det T^{-1})$, so $\det T\neq0$. ($\Leftarrow$) Let $\det T\ne0$ and $v\ne0$. Extend to a basis $v,e_2,\dots,e_n$ and take $\alpha\in V_{\rm alt}^{(n)}$ with $\alpha\ne0$. Then $\alpha(v,e_2,\dots,e_n)\neq0$ by 9.39, and $\alpha(Tv,Te_2,\dots,Te_n)=(\det T)\alpha(v,e_2,\dots,e_n)\ne0$. So $Tv\ne0$ and $T$ is invertible (p. 357). A square matrix is thus invertible iff $\det A\ne0$ (p. 358).

**9.51 Eigenvalues.** $\lambda$ is an eigenvalue of $T$ iff $\det(\lambda I-T)=0$. *Proof:* $\lambda$ is an eigenvalue iff $T-\lambda I$ is not invertible, iff $\lambda I-T$ is not invertible, iff $\det(\lambda I-T)=0$ by 9.50 (p. 358).

**9.52 Similarity invariant.** For $T\in\mathcal L(V)$ and invertible $S:W\to V$ ($W$ may differ from $V$), $\det(S^{-1}TS)=\det T$ (p. 358). The quick proof $(\det S^{-1})(\det T)(\det S)$ fails when $W\ne V$, since $\det S$ is then undefined (p. 358).

*Proof.* Let $n=\dim W=\dim V$ and $\tau\in W_{\rm alt}^{(n)}$. Define $\alpha\in V_{\rm alt}^{(n)}$ by $\alpha(v_1,\dots,v_n)=\tau(S^{-1}v_1,\dots,S^{-1}v_n)$. For $w_1,\dots,w_n\in W$:
$$\tau_{S^{-1}TS}(w_1,\dots,w_n)=\tau(S^{-1}TSw_1,\dots)=\alpha(TSw_1,\dots,TSw_n)=\alpha_T(Sw_1,\dots,Sw_n)=(\det T)\alpha(Sw_1,\dots,Sw_n)=(\det T)\tau(w_1,\dots,w_n).$$
By the definition of $\det(S^{-1}TS)$, the two determinants are equal (p. 358).

**9.53 Operator vs. its matrix.** For a basis $e_1,\dots,e_n$ of $V$: $\det T=\det\mathcal M(T,(e_1,\dots,e_n))$. The left side does not depend on the basis, so neither does the right (p. 359).

*Proof.* Let $f_k$ be the standard basis of $\mathbf F^n$ and $S:\mathbf F^n\to V$ with $Sf_k=e_k$. Two applications of 3.43 give (9.54) $\mathcal M(S^{-1}TS,(f_1,\dots,f_n))=\mathcal M(T,(e_1,\dots,e_n))$. Then $\det T=\det(S^{-1}TS)$ by 9.52, which is $\det\mathcal M(S^{-1}TS,(f))$ by the definition of the determinant of a matrix, which is $\det\mathcal M(T,(e))$ by 9.54 (p. 359).

**9.55 If $\mathbf F=\mathbf C$:** $\det T$ equals the product of the eigenvalues, each counted with multiplicity (p. 359). *Proof:* some basis gives an upper-triangular matrix whose diagonal lists the eigenvalues with multiplicity (8.37). Then apply 9.53 and 9.48. Axler says this could serve as the definition on complex spaces (p. 359).

*Intuition note.* Over $\mathbf C$, an operator is triangular in some basis. Its determinant is the product of the diagonal, which lists the eigenvalues. The basis-free definition and the "multiply the eigenvalues" picture agree.

**9.56 Transpose, dual, adjoint** (p. 360).
(a) $\det A^{\rm t}=\det A$. (b) $\det T'=\det T$. (c) On an inner product space, $\det(T^*)=\overline{\det T}$.

*Proof.* (a) Define $\alpha(v_1,\dots,v_n)=\det((v_1\cdots v_n)^{\rm t})$. By 9.46, $\alpha$ is $n$-linear. If $v_j=v_k$ ($j\ne k$), then for any $B$ rows $j,k$ of $(v_1\cdots v_n)^{\rm t}B$ coincide, so this product is never $I$. Hence $(v_1\cdots v_n)^{\rm t}$ is not invertible and $\alpha=0$, so $\alpha$ is alternating. It equals 1 on the standard basis, and the space of such forms is one-dimensional (9.37), so $\alpha$ is the determinant function. (b) follows from (a), 9.53 and 3.132. (c) In an orthonormal basis, $\mathcal M(T^*)$ is the conjugate transpose of $\mathcal M(T)$ (7.9). Then use 9.53, 9.46 and (a) (p. 360).

**9.57 Helpful rules** (p. 360). (a) Two equal columns or rows: $\det=0$. (b) Swapping two columns or two rows: $\det B=-\det A$. (c) Multiplying one column or row by a scalar multiplies $\det$ by that scalar. (d) Adding a scalar multiple of one column to another leaves $\det$ unchanged. (e) The same for rows.

*Proof sketch.* All follow because both $v\mapsto\det(v_1\cdots v_n)$ and $v\mapsto\det(v_1\cdots v_n)^{\rm t}$ are alternating $n$-linear (9.45, 9.56(a)). For (d):
$$\det(v_1+cv_2\ \ v_2\cdots v_n)=\det(v_1\ v_2\cdots v_n)+c\det(v_2\ v_2\ v_3\cdots v_n)=\det(v_1\ v_2\cdots v_n).$$
The first step is multilinearity, the second is the alternating property. (e) follows from (d) and 9.56(a). (a)–(c) are left to the reader (p. 361).

**Computing and eigenvalue remarks** (p. 361):
- For numerical matrices, run Gaussian elimination to upper-triangular form. Row swaps multiply $\det$ by $-1$ (9.57(b)), scaling a row by a nonzero constant multiplies it by that constant (9.57(c)), and adding a row multiple changes nothing (9.57(e)). Then multiply the diagonal (9.48), correcting for the swaps and constants.
- Solving $\det(\lambda I-A)=0$ for eigenvalues is "rarely efficient", except when $\dim V=2$ (or 3 or 4 with the cubic or quartic formulas). Elimination with a symbol $\lambda$ is hard because it requires deciding whether quantities equal 0.

**9.58 Unitary operators.** If $S$ is unitary on an inner product space, $|\det S|=1$ (p. 362). *Proof:* $I=S^*S$ (7.53), so $1=\det(S^*S)=(\det S^*)(\det S)=\overline{\det S}\,\det S=|\det S|^2$, using 9.49(a) and 9.56(c). The text first notes that for $\mathbf F=\mathbf C$ this follows from eigenvalues of modulus 1 (7.54) and 9.55. 9.58 needs no such assumption (pp. 361–362).

**9.59 Positive operators.** If $T$ is positive, $\det T\ge0$ (p. 362). *Proof:* the spectral theorem gives an orthonormal eigenbasis. By the last bullet of 9.42, $\det T$ is a product of eigenvalues, each nonnegative (7.38).

**9.60** $|\det T|=\sqrt{\det(T^*T)}=$ product of singular values of $T$ (p. 362). *Proof:* $|\det T|^2=\overline{\det T}\,\det T=\det(T^*)\det T=\det(T^*T)$ by 9.56(c) and 9.49(a). If $s_1,\dots,s_n$ are the singular values, $s_1^2,\dots,s_n^2$ are the eigenvalues of $T^*T$ with an orthonormal eigenbasis, so $\det(T^*T)=s_1^2\cdots s_n^2$ by 9.42 (p. 362).

**9.61 Volume.** For $T\in\mathcal L(\mathbf R^n)$ and $\Omega\subseteq\mathbf R^n$: $\operatorname{volume}T(\Omega)=|\det T|\operatorname{volume}\Omega$. It follows from 7.111 (an operator scales volume by the product of singular values) and 9.60. Axler says this explains the absolute value of the determinant in the change-of-variables formula (p. 363).

*Intuition note.* $T$ changes volume by the product of its singular values (7.111), and by 9.60 that product is $|\det T|$.

**9.62 If $\mathbf F=\mathbf C$:** with distinct eigenvalues $\lambda_1,\dots,\lambda_m$ of multiplicities $d_1,\dots,d_m$, $\det(zI-T)=(z-\lambda_1)^{d_1}\cdots(z-\lambda_m)^{d_m}$ (p. 363). *Proof:* take a triangular basis (8.37), so $zI-T$ has $z-\lambda_k$ on the diagonal exactly $d_k$ times. Apply 9.48.

**9.63 Definition.** For any $T\in\mathcal L(V)$ (real or complex), the *characteristic polynomial* is $z\mapsto\det(zI-T)$. By 9.62 it agrees with the earlier definition 8.26 when $\mathbf F=\mathbf C$. The earlier definition was not used for real spaces because an operator there may have no eigenvalues. By 9.46 it is monic of degree $\dim V$, and its zeros in $\mathbf F$ are exactly the eigenvalues (by 9.51) (p. 363).

**9.64 Cayley–Hamilton.** If $q$ is the characteristic polynomial of $T\in\mathcal L(V)$, then $q(T)=0$ (p. 364).
*Proof.* For $\mathbf F=\mathbf C$, use 9.62 and 8.29. For $\mathbf F=\mathbf R$, fix a basis, let $A$ be the matrix of $T$, and let $S$ on $\mathbf C^{\dim V}$ have matrix $A$. Then $q(z)=\det(zI-T)=\det(zI-A)=\det(zI-S)$, so $q$ is the characteristic polynomial of $S$. The complex case gives $0=q(S)=q(A)=q(T)$ (p. 364).

Consequences: the characteristic polynomial is a polynomial multiple of the minimal polynomial (5.29). If the minimal polynomial has degree $\dim V$, the two are equal. This happens for over 99.999% of $4\times4$ integer matrices with entries in $[-100,100]$ (p. 364).

**9.65 Characteristic polynomial, trace, determinant.** With $n=\dim V$, the characteristic polynomial is $z^n-(\operatorname{tr}T)z^{n-1}+\cdots+(-1)^n(\det T)$ (p. 364).
*Proof.* The constant term is the value at $z=0$, namely $\det(-T)=(-1)^n\det T$ (third bullet of 9.42). For the $z^{n-1}$ coefficient, take the matrix $A$ of $T$. The identity permutation in 9.46 contributes $(z-A_{1,1})\cdots(z-A_{n,n})$, whose $z^{n-1}$ coefficient is $-(A_{1,1}+\cdots+A_{n,n})=-\operatorname{tr}T$. Every other permutation has at most $n-2$ factors of the form $z-A_{k,k}$, so it does not contribute to $z^{n-1}$ (p. 364). The last sentence was proved over $\mathbf C$ earlier (8.54); this proof works on real and complex spaces.

**9.66 Hadamard's inequality.** For an $n\times n$ matrix $A$ with columns $v_1,\dots,v_n$ (norms from the standard inner product of $\mathbf F^n$),
$$|\det A|\le\prod_{k=1}^n\|v_k\|.$$
*Proof.* If $A$ is not invertible, $\det A=0$ and the claim holds. Otherwise the QR factorization (7.58) gives $A=QR$ with $Q$ unitary and $R$ upper-triangular with positive diagonal. Then
$$|\det A|=|\det Q||\det R|=|\det R|=\prod_k R_{k,k}\le\prod_k\|R_{\cdot,k}\|=\prod_k\|QR_{\cdot,k}\|=\prod_k\|v_k\|.$$
The justifications are 9.49(b), 9.58, 9.48, and the fact that $Q$ is an isometry. (added step) The fourth step holds because $R_{k,k}>0$ is one coordinate of the column $R_{\cdot,k}$, so $R_{k,k}\le\|R_{\cdot,k}\|$ (p. 365).

Geometry for $\mathbf F=\mathbf R$: $T e_k=v_k$ maps the unit box $P(e_1,\dots,e_n)$ (volume 1) onto the parallelepiped $P(v_1,\dots,v_n)$ with volume $|\det T|=|\det A|$ (by 9.61). So among parallelepipeds with edge lengths $\|v_k\|$, those with largest volume have orthogonal edges, with volume $\prod\|v_k\|$. A necessary and sufficient equality condition is Exercise 18 (p. 365).

**9.67 Vandermonde determinant.** For $n>1$ and $\beta_1,\dots,\beta_n\in\mathbf F$, the $n\times n$ matrix $A$ with row $j$ equal to $(1,\beta_j,\beta_j^2,\dots,\beta_j^{n-1})$ satisfies
$$\det A=\prod_{1\le j<k\le n}(\beta_k-\beta_j).$$
*Proof* (p. 366). Let $S:\mathcal P_{n-1}(\mathbf F)\to\mathbf F^n$, $Sp=(p(\beta_1),\dots,p(\beta_n))$. Then $A=\mathcal M(S,(1,z,\dots,z^{n-1}),(e_1,\dots,e_n))$, an $n\times n$ matrix. Define $T$ on $\mathcal P_{n-1}(\mathbf F)$ by $T1=1$ and $Tz^k=(z-\beta_1)(z-\beta_2)\cdots(z-\beta_k)$ for $k=1,\dots,n-1$. Let $B=\mathcal M(T,(1,\dots,z^{n-1}),(1,\dots,z^{n-1}))$. It is upper-triangular with all diagonal entries 1, so $\det B=1$ (9.48). Let $C=\mathcal M(ST,\dots)$. Then $C=AB$ (3.81), so $\det A=(\det A)(\det B)=\det C$. By the definitions, $C$ has first row $(1,0,\dots,0)$ and second row $(1,\beta_2-\beta_1,0,\dots,0)$. Row $j$ is $\bigl(1,\ \beta_j-\beta_1,\ (\beta_j-\beta_1)(\beta_j-\beta_2),\ \dots\bigr)$ up to its diagonal position and zeros after it. Its last row is $\bigl(1,\ \beta_n-\beta_1,\ \dots,\ (\beta_n-\beta_1)\cdots(\beta_n-\beta_{n-1})\bigr)$. So $C$ is lower-triangular and its diagonal entries multiply to $\prod_{j<k}(\beta_k-\beta_j)$. By 9.56(a) and 9.48, $\det A=\det C=\prod_{1\le j<k\le n}(\beta_k-\beta_j)$.

*Intuition note.* Evaluating polynomials at points is a linear map, and the Vandermonde matrix is its matrix. Swapping to the basis $1,(z-\beta_1),(z-\beta_1)(z-\beta_2),\dots$ makes the matrix triangular, and a triangular determinant is easy.

367–369).

### 9D Tensor Products

**Tensor product of two vector spaces.** Goal: a product $v\otimes w$ for $v\in V,w\in W$ in a new space $V\otimes W$ (p. 370). Desired properties:
- Distributivity: $(v_1+v_2)\otimes w=v_1\otimes w+v_2\otimes w$ and $v\otimes(w_1+w_2)=v\otimes w_1+v\otimes w_2$.
- Scalars: $\lambda(v\otimes w)=(\lambda v)\otimes w=v\otimes(\lambda w)$.
- If $e_1,\dots,e_m$ and $f_1,\dots,f_n$ are bases, the $e_j\otimes f_k$ (any order) form a basis, so $\dim(V\otimes W)=(\dim V)(\dim W)$.

The product space $V\times W$ does not work: it has no natural multiplication and $\dim(V\times W)=\dim V+\dim W$ (3.92) (p. 370).

**9.68 Definition.** A *bilinear functional* on $V\times W$ is $\beta:V\times W\to\mathbf F$ that is a linear functional in each slot with the other fixed. $\mathcal B(V,W)$ is the vector space of these, with pointwise operations and the zero function as zero. For $W=V$ this is a bilinear form (9.1) (p. 370).

**9.69 Examples** (p. 371). $\beta(v,w)=\varphi(v)\tau(w)$ for $\varphi\in V',\tau\in W'$. $\beta(\varphi,\tau)=\varphi(v)\tau(w)$ on $V'\times W'$ for fixed $v,w$. $\beta(v,\varphi)=\varphi(v)$ on $V\times V'$. $\beta(v,T)=\varphi(Tv)$ on $V\times\mathcal L(V)$ for fixed $\varphi\in V'$. $\beta(A,B)=\operatorname{tr}(AB)$ on $\mathbf F^{m,n}\times\mathbf F^{n,m}$.

**9.70** $\dim\mathcal B(V,W)=(\dim V)(\dim W)$ (p. 371).
*Proof.* Take bases $e_1,\dots,e_m$ of $V$ and $f_1,\dots,f_n$ of $W$. For $\beta\in\mathcal B(V,W)$ let $\mathcal M(\beta)\in\mathbf F^{m,n}$ have entry $\beta(e_j,f_k)$ in row $j$, column $k$. Then $\beta\mapsto\mathcal M(\beta)$ is linear. For $C\in\mathbf F^{m,n}$ define
$$\beta_C(a_1e_1+\cdots+a_me_m,\ b_1f_1+\cdots+b_nf_n)=\sum_{k=1}^n\sum_{j=1}^mC_{j,k}a_jb_k.$$
The maps $\beta\mapsto\mathcal M(\beta)$ and $C\mapsto\beta_C$ are inverses ($\beta_{\mathcal M(\beta)}=\beta$, $\mathcal M(\beta_C)=C$, left for the reader to verify), so both are isomorphisms. Thus $\dim\mathcal B(V,W)=\dim\mathbf F^{m,n}=mn$.

Axler notes that $\mathcal B(V,W)$, $\mathcal L(V,W)$ and $\mathbf F^{\dim V,\dim W}$ all have the right dimension, so it is tempting to define $V\otimes W$ as one of them. None of these gives a basis-free definition of $v\otimes w$ (p. 371).

**9.71 Definition.** $V\otimes W:=\mathcal B(V',W')$, the bilinear functionals on $V'\times W'$. For $v\in V,w\in W$, $v\otimes w\in V\otimes W$ is
$$(v\otimes w)(\varphi,\tau)=\varphi(v)\tau(w)\quad\text{for all }(\varphi,\tau)\in V'\times W'.$$
(p. 372)

**9.72** $\dim(V\otimes W)=(\dim V)(\dim W)$. *Proof:* $\dim V'=\dim V$ and $\dim W'=\dim W$ (3.111). Then use 9.70 (p. 372).

**9.73 Bilinearity.** The distributive and scalar rules above hold. *Proof of the first:* for $(\varphi,\tau)\in V'\times W'$, $((v_1+v_2)\otimes w)(\varphi,\tau)=\varphi(v_1+v_2)\tau(w)=\varphi(v_1)\tau(w)+\varphi(v_2)\tau(w)=(v_1\otimes w+v_2\otimes w)(\varphi,\tau)$. The other equalities are similar (p. 372). Axler says the abstract form of $v\otimes w$ should not matter; the important point is the behavior (p. 372).

**9.74 Basis of $V\otimes W$.** (a) If $e_1,\dots,e_m$ and $f_1,\dots,f_n$ are linearly independent lists, then $\{e_j\otimes f_k\}_{j=1..m;k=1..n}$ is linearly independent. (b) If they are bases, it is a basis of $V\otimes W$ (p. 373).

*Proof.* (a) By the linear map lemma (3.4) there exist $\varphi_j\in V'$ and $\tau_k\in W'$ with $\varphi_j(e_k)=1$ if $j=k$ and $0$ otherwise, and $\tau_j(f_k)$ likewise. Suppose (9.75) $\sum_{k}\sum_ja_{j,k}(e_j\otimes f_k)=0$. Now $(e_j\otimes f_k)(\varphi_M,\tau_N)$ is 1 if $j=M,k=N$ and 0 otherwise. Applying both sides of 9.75 to $(\varphi_M,\tau_N)$ gives $a_{M,N}=0$. (b) follows from (a), 9.72, and the fact that an independent list of the right length is a basis (2.38).

Every element of $V\otimes W$ is a finite sum of elements $v\otimes w$. But if $\dim V>1$ and $\dim W>1$, Exercise 4 shows $\{v\otimes w\}\ne V\otimes W$ (p. 373).

*Intuition note.* Think of $V\otimes W$ as the space of "$m\times n$ tables of coefficients". A pure tensor $v\otimes w$ is a special table. General elements need sums of pure tensors.

**9.76 Example: $\mathbf F^m\otimes\mathbf F^n$.** For $v=(v_1,\dots,v_m)$ and $w=(w_1,\dots,w_n)$, bilinearity gives
$$v\otimes w=\Bigl(\sum_jv_je_j\Bigr)\otimes\Bigl(\sum_kw_kf_k\Bigr)=\sum_{k=1}^n\sum_{j=1}^m(v_jw_k)(e_j\otimes f_k).$$
So $v\otimes w$ is identified with the $m\times n$ matrix with entry $v_jw_k$ in row $j$, column $k$ (p. 374). Exercises 5 and 6 use this.

**9.77 Definition.** A *bilinear map* $\Gamma:V\times W\to U$ ($U$ any vector space) is linear in each slot with the other fixed. **9.78 Examples:** bilinear functionals; $(v,w)\mapsto v\otimes w$ into $V\otimes W$ (by 9.73); $(S,T)\mapsto ST$ on $\mathcal L(V)\times\mathcal L(V)$; $(v,T)\mapsto Tv$ on $V\times\mathcal L(V,W)$ (p. 374).

**9.79 Converting bilinear maps to linear maps** (called the "universal property" in the literature) (p. 375). Let $U$ be a vector space.
(a) A bilinear $\Gamma:V\times W\to U$ gives a unique linear $\hat\Gamma:V\otimes W\to U$ with $\hat\Gamma(v\otimes w)=\Gamma(v,w)$.
(b) A linear $T:V\otimes W\to U$ gives a unique bilinear $T^\#:V\times W\to U$ with $T^\#(v,w)=T(v\otimes w)$.

*Proof.* (a) With bases $e_j,f_k$, the linear map lemma and 9.74(b) give a unique linear $\hat\Gamma$ with $\hat\Gamma(e_j\otimes f_k)=\Gamma(e_j,f_k)$. For $v=\sum a_je_j$ and $w=\sum b_kf_k$:
$$\hat\Gamma(v\otimes w)=\hat\Gamma\Bigl(\sum_k\sum_j(a_jb_k)(e_j\otimes f_k)\Bigr)=\sum_k\sum_ja_jb_k\hat\Gamma(e_j\otimes f_k)=\sum_k\sum_ja_jb_k\Gamma(e_j,f_k)=\Gamma(v,w).$$
The second step uses linearity of $\hat\Gamma$, the third its definition, and the last bilinearity of $\Gamma$. Uniqueness follows from 9.74(b). (b) $T^\#$ is bilinear by 9.73 and linearity of $T$, and the choice is clearly unique.

We cannot just define $\hat\Gamma(v\otimes w)=\Gamma(v,w)$ and extend linearly, because elements of $V\otimes W$ lack unique representations as sums of $v\otimes w$'s. The bases get around this. The final $\hat\Gamma$ does not depend on the bases (p. 376).

*Intuition note.* Any rule that is linear in $v$ and in $w$ separately is the same as one linear rule on $V\otimes W$. The tensor product is the space that makes this exchange exact.

**Tensor product of inner product spaces.**

**9.80** For inner product spaces $V,W$, there is a unique inner product on $V\otimes W$ with $\langle v\otimes w,u\otimes x\rangle=\langle v,u\rangle\langle w,x\rangle$ (p. 376).
*Proof.* With orthonormal bases $e_j$ and $f_k$, define (9.81)
$$\Bigl\langle\sum_k\sum_jb_{j,k}\,e_j\otimes f_k,\ \sum_k\sum_jc_{j,k}\,e_j\otimes f_k\Bigr\rangle=\sum_k\sum_jb_{j,k}\overline{c_{j,k}}.$$
That this is an inner product is left to the reader (use 9.74(b)). Writing $v=\sum v_je_j$ etc.,
$$\langle v\otimes w,u\otimes x\rangle=\sum_k\sum_jv_j\overline{u_j}\,w_k\overline{x_k}=\Bigl(\sum_jv_j\overline{u_j}\Bigr)\Bigl(\sum_kw_k\overline{x_k}\Bigr)=\langle v,u\rangle\langle w,x\rangle.$$
Uniqueness holds because every element of $V\otimes W$ is a linear combination of elements $v\otimes w$ (9.74(b)).

**9.82 Definition.** This unique function is *the* inner product on $V\otimes W$. It cannot be defined directly by the formula without proof, again because representations are not unique. Taking $u=v,x=w$ gives $\|v\otimes w\|=\|v\|\|w\|$ (p. 377).

**9.83** If $e_j$ and $f_k$ are orthonormal bases of $V$ and $W$, then $\{e_j\otimes f_k\}$ is an orthonormal basis of $V\otimes W$ (p. 377). *Proof:* it is a basis (9.74(b)), and $\langle e_j\otimes f_k,e_M\otimes f_N\rangle=\langle e_j,e_M\rangle\langle f_k,f_N\rangle$ is 1 if $j=M,k=N$ and 0 otherwise. The bases here may differ from those used to build the inner product in 9.80. Exercise 11 shows how this structure interacts with operators (p. 377).

**Tensor product of multiple vector spaces.** No proofs are given; they follow the $m=2$ patterns (p. 378).

- **9.84** Notation: $m>1$, and $V_1,\dots,V_m$ are finite-dimensional vector spaces (p. 378).
- **9.85** An *$m$-linear functional* is a function $V_1\times\cdots\times V_m\to\mathbf F$ linear in each slot with the others fixed. $\mathcal B(V_1,\dots,V_m)$ is the space of these. **9.86:** $\beta(v_1,\dots,v_m)=\varphi_1(v_1)\times\cdots\times\varphi_m(v_m)$ for $\varphi_k\in V_k'$ is $m$-linear. **9.87:** $\dim\mathcal B(V_1,\dots,V_m)=(\dim V_1)\cdots(\dim V_m)$, by imitating 9.70 (p. 378).
- **9.88** $V_1\otimes\cdots\otimes V_m:=\mathcal B(V_1',\dots,V_m')$, and $(v_1\otimes\cdots\otimes v_m)(\varphi_1,\dots,\varphi_m)=\varphi_1(v_1)\cdots\varphi_m(v_m)$. **9.89:** $\dim(V_1\otimes\cdots\otimes V_m)=(\dim V_1)\cdots(\dim V_m)$ (p. 379).
- **9.90** If $\dim V_k=n_k$ and $e^k_1,\dots,e^k_{n_k}$ is a basis of $V_k$, then $\{e^1_{j_1}\otimes\cdots\otimes e^m_{j_m}\}$ over all index choices is a basis. For $m=2$ the coefficients form an $n_1\times n_2$ matrix. For general $m$ an array with $m$ indices is needed, so tensor products may appear when we deal with objects specified by arrays with multiple indices (p. 379).
- **9.91** An *$m$-linear map* $\Gamma:V_1\times\cdots\times V_m\to U$ is linear in each slot. **9.92:** (a) every $m$-linear $\Gamma$ gives a unique linear $\hat\Gamma$ on $V_1\otimes\cdots\otimes V_m$ with $\hat\Gamma(v_1\otimes\cdots\otimes v_m)=\Gamma(v_1,\dots,v_m)$. (b) Every linear $T$ gives a unique $m$-linear $T^\#$ with $T^\#(v_1,\dots,v_m)=T(v_1\otimes\cdots\otimes v_m)$ (p. 380).
- Exercises 12 and 13 cover inner products on multiple tensor products (p. 380).

## Toy example (ours, not from the text)

**Part A: the determinant as a scalar on forms.** Take $V=\mathbf F^2$ ($n=2$). Let $\alpha(v_1,v_2)=v_{1,1}v_{2,2}-v_{1,2}v_{2,1}$, an alternating bilinear form with $\alpha(e_1,e_2)=1$. Let $T$ have matrix $\begin{pmatrix}2&1\\0&3\end{pmatrix}$, so $Te_1=(2,0)$ and $Te_2=(1,3)$.
- $\alpha_T(e_1,e_2)=\alpha((2,0),(1,3))=2\cdot3-0\cdot1=6=6\,\alpha(e_1,e_2)$.
- Check on other vectors: $v_1=(1,1)$, $v_2=(1,2)$ give $\alpha(v_1,v_2)=1\cdot2-1\cdot1=1$. Then $Tv_1=(3,3)$ and $Tv_2=(4,6)$, so $\alpha_T(v_1,v_2)=3\cdot6-3\cdot4=6=6\cdot1$. The ratio is again 6.
- So $\det T=6$. This agrees with 9.48 ($2\cdot3$), with the eigenvalue product (eigenvalues 2 and 3), and with 9.47 ($2\cdot3-0\cdot1$).
- Multiplicativity: $S=\begin{pmatrix}1&0\\1&1\end{pmatrix}$ has $\det S=1\cdot1-0\cdot1=1$. $ST=\begin{pmatrix}2&1\\2&4\end{pmatrix}$ has $\det=8-2=6=1\cdot6$.

**Part B: a tensor as a matrix.** For $v=(1,2)\in\mathbf F^2$ and $w=(3,4)\in\mathbf F^2$, 9.76 gives the matrix $\begin{pmatrix}1\cdot3&1\cdot4\\2\cdot3&2\cdot4\end{pmatrix}=\begin{pmatrix}3&4\\6&8\end{pmatrix}$. Its rows are proportional, so the determinant is $24-24=0$. This matrix is a pure tensor.

## Concepts
- [[determinant]] — scalar $\det T$ with $\alpha_T=(\det T)\alpha$ on $V_{\rm alt}^{(\dim V)}$. For a matrix, the determinant of its operator on $\mathbf F^n$ (pp. 354–355).
- [[alternating-multilinear-form]] (new) — multilinear function that vanishes when two arguments are equal. Its space on $V$ with $\dim V$ arguments is one-dimensional (pp. 354–355).
- [[permutation-formula-determinant]] (new) — $\det A=\sum\operatorname{sign}(j_1,\dots,j_n)A_{j_1,1}\cdots A_{j_n,n}$, with $n!$ terms (p. 356).
- [[inverse matrix]] — an operator or matrix is invertible iff its determinant is nonzero (p. 357).
- [[matrix multiplication as composition]] — $\det(ST)=\det S\det T$ (p. 357).
- [[change of basis]] — $\det(S^{-1}TS)=\det T$, so $\det\mathcal M(T)$ is basis-independent (pp. 358–359).
- [[eigenvector / eigenvalue]] — $\lambda$ is an eigenvalue iff $\det(\lambda I-T)=0$. Over $\mathbf C$, $\det T$ is the product of eigenvalues with multiplicity (pp. 358–359).
- [[characteristic polynomial]] — here defined for any $V$ as $z\mapsto\det(zI-T)$ (p. 363).
- [[cayley-hamilton-theorem]] (new) — $q(T)=0$ for the characteristic polynomial $q$, now on real and complex spaces (p. 364).
- [[trace]] (new) — appears as minus the coefficient of $z^{n-1}$ in the characteristic polynomial (p. 364).
- [[singular value decomposition]] — here only singular values are used: $|\det T|$ is their product (p. 362).
- [[orthonormal basis / orthogonal matrix]] — unitary operators have $|\det|=1$ (p. 362).
- [[positive (semi)definite matrix]] — positive operators have $\det\ge0$ (p. 362).
- [[Gram–Schmidt and QR]] — used in the proof of Hadamard's inequality (p. 365).
- [[hadamard-inequality]] (new) — $|\det A|\le\prod\|v_k\|$ (p. 365).
- [[vandermonde-determinant]] (new) — $\prod_{j<k}(\beta_k-\beta_j)$ (p. 366).
- [[bilinear-functional]] (new) — function $V\times W\to\mathbf F$ linear in each slot. Space $\mathcal B(V,W)$ has dimension $(\dim V)(\dim W)$ (pp. 370–371).
- [[tensor-product]] (new) — $V\otimes W:=\mathcal B(V',W')$, with $(v\otimes w)(\varphi,\tau)=\varphi(v)\tau(w)$ (p. 372).
- [[universal-property-tensor-product]] (new) — bilinear maps on $V\times W$ correspond to linear maps on $V\otimes W$ (p. 375).
- [[rank-one matrix / outer product]] — $v\otimes w$ identified with the matrix $(v_jw_k)$ (p. 374). Exercise 5 asks the reader to show these are exactly the matrices of rank at most one.

## Canonical instances
- [[vandermonde-matrix]] — determinant $\prod_{j<k}(\beta_k-\beta_j)$, via $S$, $T$, $C=AB$ (p. 366).
- [[hadamard-box-volume]] — parallelepiped volume is at most the product of edge lengths, with equality for orthogonal edges (p. 365).
- [[ellipsoid-volume-via-linear-map]] — Exercise 17 asks for the volume of an ellipsoid via a set $\Omega$ and an operator $T$ with $T(\Omega)$ equal to the ellipsoid (p. 368).
- [[tensor-of-two-column-vectors]] — $v\otimes w\leftrightarrow(v_jw_k)$ (p. 374).

## Bridges (candidates)
- [same-math] $|\det T|$ is the product of singular values ↔ linear-algebra/SVD: volume scaling of a map equals the product of its stretch factors.
- [same-math] Over $\mathbf C$, $\det T$ is the product of eigenvalues ↔ characteristic polynomial and the trace as sum of eigenvalues, since the coefficients are $\operatorname{tr}T$ and $\det T$.
- [same-math] $v\otimes w\leftrightarrow(v_jw_k)$ ↔ rank-one matrix / outer product $vw^{\rm t}$.
- [structural-analogy] Universal property of $\otimes$ ↔ "bilinear in two arguments equals linear on a product space", the pattern behind covariance-style bilinear forms on data.
- [structural-analogy] $\det(zI-T)$ and Cayley–Hamilton ↔ matrix powers and eigenvalue methods: the polynomial annihilates $T$.

## Questions this raises
- Why is the set of pure tensors $\{v\otimes w\}$ not a subspace when both dimensions exceed 1 (Ex. 4), and how does matrix rank measure "how far" a tensor is from pure?
- If $S\in\mathcal L(V)$ and $T\in\mathcal L(W)$ act on $V\otimes W$ by $v\otimes w\mapsto Sv\otimes Tw$ (Ex. 9), how do its determinant, eigenvalues and adjoint relate to those of $S$ and $T$?
- Hadamard's inequality is a bound. Is the better estimate of Exercise 20 ($|\det A|\le c^nn^{n/2}$) also provable by the volume picture?
- Can the $n!$-term formula be avoided entirely, and how does the cost of Gaussian elimination compare?

## Exercises worth doing
- Ex. 9C.16 (p. 368) — $g(x)=\det(I+xT)$ has $g'(0)=\operatorname{tr}T$; the text asks for a clean argument without the explicit determinant formula — difficulty: medium
- Ex. 9C.17 (p. 368) — volume of an ellipsoid via a linear map and 9.61 — difficulty: easy
- Ex. 9C.18 (p. 368) — equality case in Hadamard's inequality — difficulty: medium
- Ex. 9C.21 (p. 369) — a multiplicative function with the right values on diagonal matrices must be $\det$ — difficulty: hard
- Ex. 9D.4 (p. 380) — pure tensors do not form a subspace when both dimensions exceed 1 — difficulty: medium
- Ex. 9D.5 (p. 381) — $\{v\otimes w\}$ is exactly the set of $m\times n$ matrices of rank at most one — difficulty: medium

## Reading notes
- This is part 2 of 2 of Chapter 9. It starts at §9C "Determinants" (printed p. 354, "Defining the Determinant") and ends at the end of Exercises 9D (p. 382, Exercise 13). The split is at a section boundary. Results 9.36, 9.37 and 9.39 are cited here from part 1 and not restated.
- Page offset: printed = pdf − 14 (pdf 368 = printed 354).
- The extracted text garbles Greek letters and some math. I checked all math against the page images. I found no misprints.
- Page 369 ends with an epigraph by Felix Klein (from *Elementary Mathematics from an Advanced Standpoint: Geometry*) on determinants and their meaning. I did not use it.
- Exercises 9C (pp. 367–369, 21 exercises) and 9D (pp. 380–382, 13 exercises) are only listed selectively above; none is solved.
- In 9.64 the real-case proof's step "$q(S)=q(A)=q(T)$" identifies operators with their matrices without further comment, as printed.
