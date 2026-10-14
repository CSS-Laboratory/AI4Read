---
id: deisenroth-2020-mml/ch04-matrix-p1
work: deisenroth-2020-mml
unit: "4 Matrix Decompositions (part 1/2): intro, 4.1–4.3, start of 4.4"
pages: 98–118
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Matrix Decompositions (part 1): determinant, trace, eigenvalues, Cholesky, start of eigendecomposition

## L0 — One line
A square matrix can be summarised by its determinant, trace and eigenvalues (det = product, trace = sum of eigenvalues), and it can be factored into simpler matrices, e.g. $A=LL^\top$ (Cholesky, for symmetric positive definite $A$) or $A=PDP^{-1}$ (eigendecomposition, when the eigenvectors form a basis).

## L1 — The gist (≤ 120 words)
How can a square matrix be described by a few numbers, and how can it be factored into simpler matrices? The chapter first gives the determinant, trace and characteristic polynomial. It then defines eigenvalues and eigenvectors, and shows that the determinant is the product of the eigenvalues and the trace is their sum. Next it gives the Cholesky factorization $A=LL^\top$ for symmetric positive definite matrices. Finally it starts eigendecomposition, $A=PDP^{-1}$, which exists exactly when the eigenvectors of $A$ form a basis. Diagonal matrices make determinants, powers and inverses cheap to compute; the Cholesky factor gives cheap determinants and eigendecomposition gives cheap powers. The text says these methods become important later in probability, dimensionality reduction and density estimation.

**Prerequisites:** matrix multiplication and inverse; rank; linear independence and basis; change of basis and similar matrices; null space; Gram–Schmidt; positive definite matrices; Gaussian elimination.

## L2 — Key ideas
- The determinant is defined only for square matrices. $A$ is invertible iff $\det(A)\neq 0$ iff $\operatorname{rk}(A)=n$ (Thm 4.1, Thm 4.3, pp. 100, 103). It can be computed by Laplace expansion or by Gaussian elimination to triangular form (pp. 102–103).
- $|\det A|$ is the volume of the parallelepiped (a solid whose faces are parallel parallelograms) spanned by the columns of $A$. The sign records orientation (p. 101).
- The trace (sum of diagonal entries) satisfies $\operatorname{tr}(AB)=\operatorname{tr}(BA)$. Hence the trace of a linear map does not depend on the basis (p. 104). The determinant is basis-independent too, because similar matrices have the same determinant (p. 103).
- A number $\lambda$ is an eigenvalue (there is $x\neq0$ with $Ax=\lambda x$) iff it is a root of $p_A(\lambda)=\det(A-\lambda I)$, and the eigenspace is $\ker(A-\lambda I)$ (pp. 105–106). The algebraic multiplicity of an eigenvalue (how often it is a root of $p_A$) can exceed its geometric multiplicity (the dimension of its eigenspace) (pp. 106, 108). A defective matrix (fewer than $n$ independent eigenvectors) has at least one such eigenvalue (p. 111).
- $\det(A)=\prod\lambda_i$ and $\operatorname{tr}(A)=\sum\lambda_i$ (Thms 4.16–4.17, pp. 112–113).
- Symmetric matrices have real eigenvalues and an eigenbasis of mutually orthogonal unit vectors (spectral theorem). $A^\top A$ is always symmetric and positive semidefinite, i.e. $x^\top A^\top Ax\ge0$ for all $x$ (Thms 4.14–4.15, p. 111).
- The Cholesky factorization $A=LL^\top$ exists and is unique for symmetric positive definite $A$. It is a square-root analogue and gives cheap determinants (pp. 114–115).
- $A=PDP^{-1}$ exists iff the eigenvectors of $A$ form a basis of $\mathbb R^n$. Then $A^k=PD^kP^{-1}$ (Thm 4.20, pp. 116, 118).

## L3 — Walkthrough

### Chapter introduction (pp. 98–99)
- Matrices describe linear maps and also hold data, e.g. rows are people and columns are features (p. 98).
- The chapter has three aims: summarise matrices, decompose them, and use decompositions for approximation (p. 98).
- Matrix decomposition is like factoring $21=7\cdot 3$, so it is also called *matrix factorization* (p. 98).
- Plan: determinants (4.1) and eigenvalues (4.2) for square matrices; Cholesky (4.3); diagonalization (4.4); SVD (4.5, which extends this to non-square matrices); and a matrix taxonomy (4.7) (p. 98). Figure 4.1 is a mind map of the concepts, with links to Chapters 6 (probability) and 10 (dimensionality reduction); the text also names Chapter 11 (density estimation) as a place of use (p. 99).
- This part ends inside Section 4.4.

### 4.1 Determinant and Trace (pp. 99–105)
**Definition.** For $A\in\mathbb R^{n\times n}$ the determinant $\det(A)$, also written $|A|$, is a function mapping $A$ to a real number. It is defined only for square matrices (p. 99). The book warns that $|A|$ must not be confused with the absolute value (p. 99).

**Example 4.1 (invertibility test).**
- For $1\times1$, $A=a$ has $A^{-1}=1/a$, so $A$ is invertible iff $a\neq0$ (p. 100).
- For $2\times2$:
$$A^{-1}=\frac{1}{a_{11}a_{22}-a_{12}a_{21}}\begin{bmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{bmatrix}\tag{4.2}$$
- So $A$ is invertible iff $a_{11}a_{22}-a_{12}a_{21}\neq 0$ (4.3). This quantity is $\det(A)$ (4.4) (p. 100).

**Theorem 4.1.** For square $A\in\mathbb R^{n\times n}$: $A$ is invertible iff $\det(A)\neq0$ (p. 100).

**Closed forms.**
- $n=1$: $\det(a_{11})=a_{11}$ (4.5).
- $n=2$: $a_{11}a_{22}-a_{12}a_{21}$ (4.6).
- $n=3$ (Sarrus' rule):
$$\det A = a_{11}a_{22}a_{33}+a_{21}a_{32}a_{13}+a_{31}a_{12}a_{23}-a_{31}a_{22}a_{13}-a_{11}a_{32}a_{23}-a_{21}a_{12}a_{33}\tag{4.7}$$
(p. 100)

**Triangular matrices.** $T$ is upper-triangular if $T_{ij}=0$ for $i>j$ (zero below the diagonal). Lower-triangular means zeros above the diagonal. For triangular $T\in\mathbb R^{n\times n}$:
$$\det(T)=\prod_{i=1}^n T_{ii}\tag{4.8}$$
(p. 101)

**Example 4.2 (determinant as volume).**
- $\det(A)$ is the signed volume of the $n$-dimensional parallelepiped (a solid with faces that are parallel parallelograms) formed by the columns of $A$ (p. 101).
- For $n=2$, $|\det[b,g]|$ is the area of the parallelogram with vertices $0,b,g,b+g$.
- If $b=\lambda g$ (linearly dependent), the area is 0.
- If $b=(b,0)^\top$ and $g=(0,g)^\top$, then $\det=bg-0=bg$.
- The sign gives the orientation relative to $(e_1,e_2)$. Swapping the columns reverses it (p. 101).
- In $\mathbb R^3$, $|\det[r,b,g]|$ is the volume of the solid.
- Numbers: $r=(2,0,-8)^\top$, $g=(6,1,0)^\top$, $b=(1,4,-1)^\top$, with $A=[r,g,b]$ as in (4.10). Then $V=|\det A|=186$ (4.11) (pp. 101–102).

**Theorem 4.2 (Laplace expansion).** For $A\in\mathbb R^{n\times n}$ and all $j=1,\dots,n$:
$$\det(A)=\sum_{k=1}^n(-1)^{k+j}a_{kj}\det(A_{k,j})\quad\text{(column }j)\tag{4.12}$$
$$\det(A)=\sum_{k=1}^n(-1)^{k+j}a_{jk}\det(A_{j,k})\quad\text{(row }j)\tag{4.13}$$
- $A_{k,j}\in\mathbb R^{(n-1)\times(n-1)}$ is $A$ with row $k$ and column $j$ deleted.
- $\det(A_{k,j})$ is a *minor*, and $(-1)^{k+j}\det(A_{k,j})$ a *cofactor*.
- Applying it recursively reduces any $n\times n$ determinant to $2\times2$ ones (p. 102).

**Example 4.3.** For $A=\begin{bmatrix}1&2&3\\3&1&2\\0&0&1\end{bmatrix}$, expand along row 1 (4.15):
$$\det A=1(1-0)-2(3-0)+3(0-0)=-5\tag{4.16}$$
Sarrus' rule gives $1-6=-5$ (4.17) (pp. 102–103).

**Properties of the determinant** (p. 103):
- $\det(AB)=\det A\det B$, and $\det A=\det A^\top$.
- If $A$ is invertible, $\det(A^{-1})=1/\det A$.
- Similar matrices have the same determinant. So all transformation matrices of a map $\Phi:V\to V$ share it, and the determinant does not depend on the basis.
- Adding a multiple of one row/column to another does not change $\det A$.
- Scaling a row/column by $\lambda$ scales $\det A$ by $\lambda$. In particular $\det(\lambda A)=\lambda^n\det A$.
- Swapping two rows/columns flips the sign.
- By the last three properties, Gaussian elimination to triangular form plus (4.8) computes $\det A$ (p. 103).

**Theorem 4.3.** $\det(A)\neq0$ iff $\operatorname{rk}(A)=n$; i.e. $A$ is invertible iff it is full rank (p. 103).
Author's remark: in machine learning, direct numerical methods have superseded explicit determinant calculation. Determinants stay important theoretically, through the characteristic polynomial (p. 103).

> **Intuition note.** If the columns of a matrix are linearly dependent, the volume they span is 0, so the determinant is 0 and (Theorem 4.1) there is no inverse. A non-zero determinant means the columns span a full-dimensional solid.

**Trace (Def. 4.4).**
$$\operatorname{tr}(A):=\sum_{i=1}^n a_{ii}\tag{4.18}$$
- Properties: $\operatorname{tr}(A+B)=\operatorname{tr}A+\operatorname{tr}B$; $\operatorname{tr}(\alpha A)=\alpha\operatorname{tr}A$; $\operatorname{tr}(I_n)=n$; $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ for $A\in\mathbb R^{n\times k}$, $B\in\mathbb R^{k\times n}$.
- The text states that only one function satisfies these four properties together, the trace, citing Gohberg et al. (p. 104).
- Cyclic invariance: $\operatorname{tr}(AKL)=\operatorname{tr}(KLA)$ for $A\in\mathbb R^{a\times k}$, $K\in\mathbb R^{k\times l}$, $L\in\mathbb R^{l\times a}$ (4.19). It extends to any number of matrices.
- Special case: $\operatorname{tr}(xy^\top)=\operatorname{tr}(y^\top x)=y^\top x$ (4.20) (p. 104).
- Trace of a linear map $\Phi$: take the trace of its matrix $A$. In another basis the matrix is $B=S^{-1}AS$, and
$$\operatorname{tr}(B)=\operatorname{tr}(S^{-1}AS)\overset{(4.19)}{=}\operatorname{tr}(ASS^{-1})=\operatorname{tr}(A)\tag{4.21}$$
- So the trace of a map is basis-independent, although its matrix is not (p. 104).

**Characteristic polynomial (Def. 4.5).** For $\lambda\in\mathbb R$ and $A\in\mathbb R^{n\times n}$:
$$p_A(\lambda):=\det(A-\lambda I)\tag{4.22a}$$
$$=c_0+c_1\lambda+c_2\lambda^2+\dots+c_{n-1}\lambda^{n-1}+(-1)^n\lambda^n\tag{4.22b}$$
In particular
$$c_0=\det(A)\tag{4.23}$$
$$c_{n-1}=(-1)^{n-1}\operatorname{tr}(A)\tag{4.24}$$
(pp. 104–105)

### 4.2 Eigenvalues and Eigenvectors (pp. 105–114)
**Definition 4.6.** For square $A$, $\lambda\in\mathbb R$ is an eigenvalue and $x\in\mathbb R^n\setminus\{0\}$ the corresponding eigenvector if
$$Ax=\lambda x\tag{4.25}$$
This is the eigenvalue equation. "Eigen" is German for "characteristic", "self" or "own" (p. 105).
- Remark: software often sorts eigenvalues in descending order. The book does not assume an ordering unless it says so (p. 105).
- Equivalent statements (p. 105):
  - $\lambda$ is an eigenvalue of $A$.
  - $(A-\lambda I_n)x=0$ has a non-trivial solution.
  - $\operatorname{rk}(A-\lambda I_n)<n$.
  - $\det(A-\lambda I_n)=0$.
- Def. 4.7: *codirected* vectors point the same way. *Collinear* vectors point the same or opposite ways (p. 105).
- Non-uniqueness: if $x$ is an eigenvector for $\lambda$ and $c\neq0$, then $A(cx)=cAx=c\lambda x=\lambda(cx)$ (4.26). So all vectors collinear with $x$ are eigenvectors too (p. 105).

**Theorem 4.8.** $\lambda$ is an eigenvalue of $A$ iff it is a root of $p_A(\lambda)$ (p. 106).

**Definitions 4.9–4.10.**
- *Algebraic multiplicity* of $\lambda_i$: how many times it appears as a root of $p_A$.
- *Eigenspace* $E_\lambda$: the subspace spanned by all eigenvectors for $\lambda$. It is the solution space of $(A-\lambda I)x=0$.
- *Eigenspectrum* (spectrum): the set of all eigenvalues (p. 106).
- Geometry: an eigenvector for a nonzero eigenvalue points in a direction that the map stretches. The eigenvalue is the stretch factor, and a negative eigenvalue flips the direction (p. 106).

**Example 4.4.** The identity $I$ has $p_I(\lambda)=(1-\lambda)^n$. It has the single eigenvalue 1, occurring $n$ times. Its only eigenspace $E_1$ is $n$-dimensional, and all standard basis vectors are eigenvectors (p. 106).

**Further properties** (p. 106):
- $A$ and $A^\top$ have the same eigenvalues, but not necessarily the same eigenvectors.
- $E_\lambda=\ker(A-\lambda I)$, since $Ax=\lambda x\iff(A-\lambda I)x=0$ (4.27a,b).
- Similar matrices have the same eigenvalues. So eigenvalues, determinant and trace are all invariant under change of basis.
- Symmetric positive definite matrices always have positive, real eigenvalues.

**Example 4.5.** $A=\begin{bmatrix}4&2\\1&3\end{bmatrix}$ (pp. 107–108).
1. Step 1: since $x\neq0$ and $(A-\lambda I)x=0$, $A-\lambda I$ is not invertible, so $\det(A-\lambda I)=0$.
2. Step 2:
$$p_A(\lambda)=(4-\lambda)(3-\lambda)-2\cdot1=10-7\lambda+\lambda^2=(2-\lambda)(5-\lambda)$$
so $\lambda_1=2$, $\lambda_2=5$ (4.29–4.30).
3. Step 3, $\lambda=5$: $\begin{bmatrix}-1&2\\1&-2\end{bmatrix}x=0$ gives $E_5=\operatorname{span}[(2,1)^\top]$ (4.32–4.33).
4. Step 3, $\lambda=2$: $\begin{bmatrix}2&2\\1&1\end{bmatrix}x=0$ gives $x_2=-x_1$, so $E_2=\operatorname{span}[(1,-1)^\top]$ (4.34–4.35).

**Definition 4.11 (geometric multiplicity).** For $\lambda_i$: the number of linearly independent eigenvectors for $\lambda_i$, i.e. $\dim E_{\lambda_i}$.
- Remark: it is at least 1, it cannot exceed the algebraic multiplicity, but it may be lower (p. 108).

**Example 4.6.** $A=\begin{bmatrix}2&1\\0&2\end{bmatrix}$ has $\lambda_1=\lambda_2=2$ (algebraic multiplicity 2). It has only one distinct unit eigenvector $(1,0)^\top$, so its geometric multiplicity is 1 (p. 108).

**Graphical intuition in 2D (Fig. 4.4, pp. 108–110).** Five maps act on a grid of points:
- $A_1=\begin{bmatrix}1/2&0\\0&2\end{bmatrix}$: the vertical axis is stretched by 2 ($\lambda=2$) and the horizontal axis compressed by $1/2$. It is area preserving, $\det=1=2\cdot\frac12$.
- $A_2=\begin{bmatrix}1&1/2\\0&1\end{bmatrix}$: a shear, area preserving. $\lambda_1=\lambda_2=1$ and the eigenvectors are collinear, so the map acts along one direction only.
- $A_3$ = rotation by $\pi/6$ (30°) counter-clockwise. It has only complex eigenvalues, so no eigenvectors are drawn. $\det=1$.
- $A_4=\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$: collapses the plane onto a line. $\lambda_1=0$ (that direction collapses), $\lambda_2=2$, image area 0.
- $A_5=\begin{bmatrix}1&1/2\\1/2&1\end{bmatrix}$: shear and stretch. $|\det A_5|=3/4$. It stretches by 1.5 along one eigenvector and compresses by 0.5 along the orthogonal one.

**Example 4.7 (C. elegans network).**
- The adjacency matrix $A\in\mathbb R^{277\times277}$ has $a_{ij}=1$ if neuron $i$ talks to neuron $j$ through a synapse, else 0 (p. 110).
- $A$ is not symmetric, so its eigenvalues may not be real. The authors therefore use $A_{sym}:=A+A^\top$, which has a nonzero entry iff two neurons are connected, in either direction.
- The eigenvalues of $A_{sym}$, sorted in descending order, form an S-like curve (Fig. 4.5b). The text says this shape is typical of many biological neural networks, and its cause is an active research area (p. 110).

**Theorem 4.12.** Eigenvectors $x_1,\dots,x_n$ of $A\in\mathbb R^{n\times n}$ with $n$ distinct eigenvalues are linearly independent, so they form a basis of $\mathbb R^n$ (p. 111).

**Definition 4.13 (defective).** $A$ is defective if it has fewer than $n$ linearly independent eigenvectors (p. 111).
- A non-defective matrix does not need $n$ distinct eigenvalues, but its eigenvectors must form a basis of $\mathbb R^n$.
- A defective matrix has at least one eigenvalue with algebraic multiplicity $m>1$ and geometric multiplicity below $m$.
- A defective matrix cannot have $n$ distinct eigenvalues (Thm 4.12) (p. 111).

**Theorem 4.14.** For $A\in\mathbb R^{m\times n}$, $S:=A^\top A\in\mathbb R^{n\times n}$ is symmetric and positive semidefinite (4.36). Remark: if $\operatorname{rk}(A)=n$, then $S$ is positive definite (p. 111).
- Symmetry: $S=A^\top A=A^\top(A^\top)^\top=(A^\top A)^\top=S^\top$.
- Positive semidefiniteness: $x^\top Sx=x^\top A^\top Ax=(Ax)^\top(Ax)\ge0$, because a dot product of a vector with itself is a sum of squares (p. 111).

**Theorem 4.15 (spectral theorem).** If $A\in\mathbb R^{n\times n}$ is symmetric, there is an orthonormal basis (ONB) of the space consisting of eigenvectors of $A$, and every eigenvalue is real. Consequence: $A=PDP^\top$ with $D$ diagonal and the eigenvectors in the columns of $P$ (p. 111).

**Example 4.8.** $A=\begin{bmatrix}3&2&2\\2&3&2\\2&2&3\end{bmatrix}$ (pp. 111–112).
- $p_A(\lambda)=-(\lambda-1)^2(\lambda-7)$, so $\lambda_1=1$ (repeated) and $\lambda_2=7$ (4.38).
- $E_1=\operatorname{span}[x_1,x_2]$ with $x_1=(-1,1,0)^\top$, $x_2=(-1,0,1)^\top$; $E_7=\operatorname{span}[x_3]$ with $x_3=(1,1,1)^\top$ (4.39).
- $x_3$ is orthogonal to $x_1$ and $x_2$, but $x_1^\top x_2=1\neq0$.
- Any combination $\alpha x_1+\beta x_2$ is again an eigenvector for $\lambda=1$ (4.40). So Gram–Schmidt (Section 3.8.3) can orthogonalise inside $E_1$. The result is
$$x_1'=(-1,1,0)^\top,\qquad x_2'=\tfrac12(-1,-1,2)^\top\tag{4.41}$$
which are orthogonal to each other and to $x_3$.

**Theorem 4.16.** $\det(A)=\prod_{i=1}^n\lambda_i$, with $\lambda_i\in\mathbb C$ the possibly repeated eigenvalues (4.42).
**Theorem 4.17.** $\operatorname{tr}(A)=\sum_{i=1}^n\lambda_i$, same convention (4.43) (pp. 112–113).

**Geometric intuition (Fig. 4.6, p. 113).** Take $A\in\mathbb R^{2\times2}$ whose eigenvectors $x_1,x_2$ form an ONB, so they span a unit square.
- $A$ maps them to $v_1=\lambda_1x_1$ and $v_2=\lambda_2x_2$. These are still orthogonal and span a rectangle of area $|\lambda_1\lambda_2|$.
- The unit square has perimeter $2(1+1)$, and the image has perimeter $2(|\lambda_1|+|\lambda_2|)$. So the sum of absolute eigenvalues tells how the perimeter changes (p. 113).

> **Intuition note.** An eigenvector is a direction where the map only stretches. If the eigenvectors are orthonormal, the unit square's area changes by $|\lambda_1\lambda_2|$ and its perimeter by a factor $\tfrac12(|\lambda_1|+|\lambda_2|)$. This is the text's geometric picture for the two theorems (it uses absolute values).

**Example 4.9 (PageRank).**
- Google uses the eigenvector for the maximal eigenvalue of a matrix $A$ to rank pages (p. 113).
- Idea: a page's importance is approximated by the importance of the pages linking to it. The web is a directed graph, and the weight $x_i\ge0$ of page $a_i$ counts and weighs its in-links (p. 113).
- User navigation is modelled by a transition matrix $A$ of click probabilities. The text states that for any initial vector $x$ the sequence $x,Ax,A^2x,\dots$ converges to $x^*$ with $Ax^*=x^*$. So $x^*$ is an eigenvector with eigenvalue 1.
- After normalising to $\|x^*\|=1$, the entries can be read as probabilities (p. 114).

### 4.3 Cholesky Decomposition (pp. 114–115)
- Motivation: on positive reals, the square root splits a number into equal factors ($9=3\cdot3$). For symmetric positive definite matrices, Cholesky is a square-root-like operation (p. 114).

**Theorem 4.18.** A symmetric positive definite $A$ can be factored as $A=LL^\top$ with $L$ lower-triangular with positive diagonal entries (4.44). $L$ is the Cholesky factor and is unique (p. 114).

**Example 4.10 ($3\times3$).** Multiplying out $LL^\top$ gives (4.46):
$$A=\begin{bmatrix}l_{11}^2&l_{21}l_{11}&l_{31}l_{11}\\l_{21}l_{11}&l_{21}^2+l_{22}^2&l_{31}l_{21}+l_{32}l_{22}\\l_{31}l_{11}&l_{31}l_{21}+l_{32}l_{22}&l_{31}^2+l_{32}^2+l_{33}^2\end{bmatrix}$$
Matching entries with (4.45) gives
$$l_{11}=\sqrt{a_{11}},\quad l_{22}=\sqrt{a_{22}-l_{21}^2},\quad l_{33}=\sqrt{a_{33}-(l_{31}^2+l_{32}^2)}\tag{4.47}$$
$$l_{21}=\tfrac{1}{l_{11}}a_{21},\quad l_{31}=\tfrac{1}{l_{11}}a_{31},\quad l_{32}=\tfrac{1}{l_{22}}(a_{32}-l_{31}l_{21})\tag{4.48}$$
Key point: each $l_{ij}$ is computed backwards from $a_{ij}$ and earlier $l_{ij}$ (p. 115).

**Uses (p. 115).**
- The covariance matrix of a multivariate Gaussian is symmetric positive definite. Its Cholesky factor lets us generate Gaussian samples and apply linear transformations to random variables. The text says the linear transformation of random variables is heavily exploited when computing gradients in deep stochastic models such as variational auto-encoders.
- Determinants: $\det A=\det(L)\det(L^\top)=\det(L)^2=\prod_i l_{ii}^2$, since $L$ is triangular.

> **Intuition note.** Just as $9=3\cdot3$, a positive definite matrix splits into a triangular factor times its transpose. Because triangular matrices are easy to handle, the factor gives cheap determinants and a way to generate samples from a Gaussian with covariance $A$ (p. 115).

### 4.4 Eigendecomposition and Diagonalization (pp. 115–118; section continues in part 2)
**Diagonal matrices** $D=\operatorname{diag}(c_1,\dots,c_n)$ (4.49) allow fast computation (p. 115):
- the determinant is the product of the diagonal entries;
- $D^k$ raises each diagonal entry to the power $k$;
- $D^{-1}$ has the reciprocals of the diagonal entries, if all are nonzero.

**Definition 4.19.** $A\in\mathbb R^{n\times n}$ is diagonalizable if it is similar to a diagonal matrix: there is an invertible $P\in\mathbb R^{n\times n}$ with $D=P^{-1}AP$. Diagonalizing is the same map in a different basis, which will turn out to be an eigenbasis (p. 116).

**Derivation.** Let $P:=[p_1,\dots,p_n]$ (shape $n\times n$) and $D$ diagonal $n\times n$ with entries $\lambda_1,\dots,\lambda_n$. Then
$$AP=PD\tag{4.50}$$
holds iff the $\lambda_i$ are eigenvalues of $A$ and the $p_i$ corresponding eigenvectors. Reason:
$$AP=[Ap_1,\dots,Ap_n]\tag{4.51}$$
$$PD=[\lambda_1p_1,\dots,\lambda_np_n]\tag{4.52}$$
so (4.50) gives $Ap_i=\lambda_ip_i$ (4.53–4.54), hence the columns of $P$ are eigenvectors. Invertibility of $P$ (full rank, Thm 4.3) needs $n$ linearly independent eigenvectors, i.e. a basis of $\mathbb R^n$ (p. 116).

**Theorem 4.20 (eigendecomposition).** $A\in\mathbb R^{n\times n}$ can be factored as
$$A=PDP^{-1}\tag{4.55}$$
with $D$ diagonal holding the eigenvalues, iff the eigenvectors of $A$ form a basis of $\mathbb R^n$ (p. 116).
- The author concludes that only non-defective matrices can be diagonalized, and that the columns of $P$ are the $n$ eigenvectors (p. 117).

**Theorem 4.21.** A symmetric $S\in\mathbb R^{n\times n}$ can always be diagonalized. It follows from the spectral theorem. Since an ONB of eigenvectors exists, $P$ is orthogonal and $D=P^\top AP$ (p. 117).
- Remark: the Jordan normal form handles defective matrices but is beyond the book (p. 117).

**Geometric intuition (Fig. 4.7, p. 117).** $A$ acts in the standard basis. $P^{-1}$ changes basis from the standard basis to the eigenbasis. $D$ scales along the eigen-axes by $\lambda_i$. $P$ maps the result back to standard coordinates, giving $\lambda_ip_i$.

> **Intuition note.** In the eigenbasis the map is only independent stretches. So $A$ means: switch to eigen-coordinates, stretch each axis, switch back.

**Example 4.11.** $A=\tfrac12\begin{bmatrix}5&-2\\-2&5\end{bmatrix}$ (p. 118).
1. Step 1: $\det(A-\lambda I)=(\tfrac52-\lambda)^2-1=\lambda^2-5\lambda+\tfrac{21}{4}=(\lambda-\tfrac72)(\lambda-\tfrac32)$ (4.56). So $\lambda_1=\tfrac72$, $\lambda_2=\tfrac32$.
2. Normalised eigenvectors: $p_1=\tfrac1{\sqrt2}(1,-1)^\top$, $p_2=\tfrac1{\sqrt2}(1,1)^\top$ (4.58).
3. Step 2: they form a basis of $\mathbb R^2$, so $A$ is diagonalizable.
4. Step 3: $P=\tfrac1{\sqrt2}\begin{bmatrix}1&1\\-1&1\end{bmatrix}$ (4.59) and $P^{-1}AP=\operatorname{diag}(\tfrac72,\tfrac32)=D$ (4.60).
5. Since the $p_i$ form an ONB, $P^{-1}=P^\top$ and $A=PDP^\top$ (4.61).

**Powers.** If the eigendecomposition exists, $A^k=(PDP^{-1})^k=PD^kP^{-1}$ (4.62). $D^k$ is cheap because each diagonal entry is raised separately (p. 118).

**Determinant via eigendecomposition.** The text begins $\det(A)=\det(PDP^{-1})=\det(P)\det(D)\det(P^{-1})$ (4.63a), and the part given here ends there (p. 118).

## Toy example (ours, not from the text)
Let $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$.
- Characteristic polynomial: $\det(A-\lambda I)=(2-\lambda)^2-1=\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)$. So $\lambda_1=3$, $\lambda_2=1$.
- Eigenvectors: for $\lambda=3$, $(A-3I)x=\begin{bmatrix}-1&1\\1&-1\end{bmatrix}x=0$ gives $x=(1,1)^\top$. For $\lambda=1$, $\begin{bmatrix}1&1\\1&1\end{bmatrix}x=0$ gives $x=(1,-1)^\top$.
- Check of the two theorems: $\det A=4-1=3=3\cdot1$ and $\operatorname{tr}A=4=3+1$.
- Eigendecomposition: $P=\tfrac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ (orthogonal, so $P^{-1}=P^\top$) and $D=\operatorname{diag}(3,1)$.
- Power: $A^2=PD^2P^\top$ with $D^2=\operatorname{diag}(9,1)$. First $PD^2=\tfrac1{\sqrt2}\begin{bmatrix}9&1\\9&-1\end{bmatrix}$. Then $(PD^2)P^\top=\tfrac12\begin{bmatrix}9+1&9-1\\9-1&9+1\end{bmatrix}=\begin{bmatrix}5&4\\4&5\end{bmatrix}$.
- Direct check: $A^2=\begin{bmatrix}2\cdot2+1\cdot1&2\cdot1+1\cdot2\\1\cdot2+2\cdot1&1\cdot1+2\cdot2\end{bmatrix}=\begin{bmatrix}5&4\\4&5\end{bmatrix}$. ✓.

## Concepts
- [[determinant]] — real number from a square matrix; $|\det|$ is the volume spanned by the columns, sign is orientation; non-zero iff invertible (pp. 99–103)
- [[inverse matrix]] — exists iff $\det\neq0$ iff full rank (Thms 4.1, 4.3) (pp. 100, 103)
- [[rank]] — full rank $n$ is equivalent to invertibility; $\operatorname{rk}(A-\lambda I)<n$ characterises eigenvalues (pp. 103, 105)
- [[trace]] (new) — sum of diagonal entries; cyclic invariance; basis-independent for a linear map; equals the sum of eigenvalues (pp. 103–104, 113)
- [[laplace-expansion]] (new) — recursive determinant formula along a row or column using cofactors (p. 102)
- [[triangular-matrix]] (new) — zeros on one side of the diagonal; determinant = product of the diagonal (p. 101)
- [[characteristic polynomial]] — $p_A(\lambda)=\det(A-\lambda I)$; roots are the eigenvalues; $c_0=\det A$, $c_{n-1}=(-1)^{n-1}\operatorname{tr}A$ (pp. 104–106)
- [[eigenvector / eigenvalue]] — $Ax=\lambda x$ with $x\neq0$ (pp. 105–106)
- [[null space (kernel)]] — eigenspace $E_\lambda=\ker(A-\lambda I)$ (p. 106)
- [[eigenspace-and-spectrum]] (new) — $E_\lambda$ is the span of eigenvectors for $\lambda$; the spectrum is the set of eigenvalues (p. 106)
- [[algebraic-geometric-multiplicity]] (new) — root multiplicity in $p_A$ versus $\dim E_\lambda$; geometric ≤ algebraic (pp. 106, 108)
- [[defective-matrix]] (new) — fewer than $n$ independent eigenvectors; not diagonalizable (pp. 111, 117)
- [[positive (semi)definite matrix]] — $A^\top A$ is always symmetric PSD, and PD if $\operatorname{rk}A=n$ (p. 111)
- [[spectral theorem]] — symmetric ⇒ real eigenvalues and an orthonormal eigenbasis, $A=PDP^\top$ (p. 111)
- [[Gram–Schmidt and QR]] — used here to orthogonalise eigenvectors within one eigenspace (p. 112)
- [[cholesky-decomposition]] (new) — $A=LL^\top$, $L$ lower-triangular with positive diagonal, unique, for symmetric PD $A$ (p. 114)
- [[diagonalization]] — $A=PDP^{-1}$ exists iff the eigenvectors form a basis of $\mathbb R^n$; $A^k=PD^kP^{-1}$ (pp. 116–118)
- [[change of basis]] — diagonalization is a basis change to the eigenbasis; similar matrices share det, trace, eigenvalues (pp. 103, 106, 116)
- [[adjacency matrix]] — $a_{ij}=1$ if neuron $i$ synapses onto $j$; symmetrised as $A+A^\top$ (p. 110)
- [[Markov (stochastic) matrix]] — the PageRank transition matrix of click probabilities; the limit vector $x^*$ of $x,Ax,A^2x,\dots$ is an eigenvector with eigenvalue 1 (pp. 113–114)

## Canonical instances
- [[parallelepiped-volume-det]] — $|\det[r,g,b]|=186$ for the given $3\times3$ example (p. 102)
- [[laplace-expansion-3x3]] — $\det=-5$, cross-checked with Sarrus' rule (pp. 102–103)
- [[eigen-2x2-example]] — $\begin{bmatrix}4&2\\1&3\end{bmatrix}$, eigenvalues 2 and 5 (p. 107)
- [[defective-2x2]] — $\begin{bmatrix}2&1\\0&2\end{bmatrix}$, algebraic multiplicity 2, geometric multiplicity 1 (p. 108)
- [[eigen-2d-gallery]] — five 2D maps (scaling, shear, rotation, collapse, shear-stretch) with their eigenvalues and determinants (pp. 108–110)
- [[c-elegans-spectrum]] — S-shaped eigenspectrum of the symmetrised connectivity matrix of a 277-neuron network (p. 110)
- [[pagerank]] — a page's rank as the eigenvector of the click-probability matrix, eigenvalue 1 (pp. 113–114)
- [[repeated-eigenvalue-symmetric-3x3]] — $\begin{bmatrix}3&2&2\\2&3&2\\2&2&3\end{bmatrix}$, Gram–Schmidt inside $E_1$ (pp. 111–112)
- [[cholesky-3x3]] — entry-by-entry construction of $L$ (p. 115)
- [[eigendecomposition-example]] — $\tfrac12\begin{bmatrix}5&-2\\-2&5\end{bmatrix}=PDP^\top$ (p. 118)

## Bridges (candidates)
- [structural-analogy] Cholesky $A=LL^\top$ ↔ scalar arithmetic: $9=3\cdot3$, a square root of a positive quantity — the text draws this analogy itself.
- [same-math] PageRank vector $Ax^*=x^*$ via repeated multiplication $x,Ax,A^2x,\dots$ ↔ power iteration / Markov steady state — same eigenvector equation, with the iteration as described on p. 114.
- [same-math] Cholesky sampling of a Gaussian with covariance $\Sigma=LL^\top$ ↔ probability (Chapter 6): linear transformation of random variables (as sketched on p. 115).
- [structural-analogy] Eigendecomposition as $P^{-1}$, then $D$, then $P$ ↔ change of basis: do the easy operation in the right coordinates, then return.
- [metaphor] Trace and determinant as "sum and product of stretches" ↔ geometry: perimeter and area of the image of a unit square (valid only for the orthonormal-eigenvector picture on p. 113).

## Questions this raises
- What can be done when a matrix is defective or non-square? (The text points to the Jordan normal form, which it leaves aside, and to SVD in 4.5.)
- Why does the PageRank sequence $x, Ax, A^2x,\dots$ converge, and why to the eigenvalue-1 eigenvector? (The text asserts it; the original report is cited.)
- Why does the Cholesky factor exist and why is it unique? (The text constructs $l_{ij}$ for $n=3$ only.)
- Why is the sum of the dimensions of the eigenspaces equal to $n$ for symmetric matrices, i.e. why does the spectral theorem hold? (It is stated without proof.)

## Reading notes
- This is part 1 of Chapter 4. It starts at the chapter opening (printed p. 98) and ends on printed p. 118, inside Section 4.4, right after (4.63a), the first step of the determinant-via-eigendecomposition derivation. The rest of the chapter (4.4 continued, 4.5 SVD, onward) is not covered here.
- Page offset: printed = pdf − 6.
- No exercises appear in these pages, so the Exercises section is omitted.
- Equations were checked against the page images. The text layer was garbled in places, e.g. the matrices in Fig. 4.4 and the $x_1^\top x_2$ line in Example 4.8, but the images were clear.
- Example 4.5 states "$x_2=-x_1$" and takes the representative $(1,-1)^\top$; this is consistent with (4.34).
- Example 4.8 shows $x_2'$ with a factor $\tfrac12$ in (4.41); it is not normalised to unit length.
- In Fig. 4.4 the rotation $A_3$ is labelled with eigenvalues $0.87\mp0.5j$; the text calls them "complex" without giving formulas.
- Example 4.9 (PageRank) gives its convergence claim without proof, and the 1996 date and authors are as printed in the text.
