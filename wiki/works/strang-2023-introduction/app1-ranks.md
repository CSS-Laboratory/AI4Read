---
id: strang-2023-introduction/app1-ranks
work: strang-2023-introduction
unit: "Appendices 1–9 (ranks of AB and A+B; factorizations; parameter counts; software; Jordan form; tensors; condition number; Markov and Perron–Frobenius; elimination and factorization)"
pages: 400–412
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Appendices 1–9: Ranks, factorizations and further topics

## L0 — One line
Multiplying matrices cannot raise rank, and matrices can be factored in many ways (CR, LU, QR, SVD, Jordan and others, each with its own requirements) that help explain rank, parameter counts, conditioning and eigenvalue behaviour.

## L1 — The gist (≤ 120 words)
These appendices collect tools used throughout the book. A1 proves rank rules for AB, A+B and AᵀA. A2 lists 16 factorizations with their requirements. A3 counts free parameters on both sides of six basic factorizations. A4 points to software. A5 covers the Jordan form and Cayley–Hamilton. A6 introduces tensors. A7 defines the condition number. A8 proves Perron's theorem for positive matrices and applies it to Markov chains and PageRank. A9 shows how elimination produces A = CR and null-space bases. Together they connect rank, eigenvalues and numerical behaviour.

**Prerequisites:** column/row/null spaces, rank, eigenvalues and eigenvectors, SVD, Gaussian elimination, matrix norms.

## L2 — Key ideas
- Rank(AB) ≤ rank A and ≤ rank B; rank(A+B) ≤ rank A + rank B; rank(AᵀA) = rank A (p. 400).
- If A is m×r and B is r×n, both of rank r, then AB has rank r. The reversed product BA can easily fail (p. 400).
- Sixteen factorizations each come with requirements, e.g. LU needs no row exchanges, the spectral theorem needs a real symmetric matrix (pp. 401–402).
- Counting parameters on both sides of A = LU, QR, QΛQᵀ, XΛX⁻¹, QS, UΣVᵀ gives agreement. A rank-r m×n matrix has (m+n−r)r free parameters (p. 403).
- A square matrix without n independent eigenvectors cannot be diagonalized, but it has a Jordan form (a nearly diagonal form). In the text's example this form produces terms like te^{3t}, and it makes the Cayley–Hamilton theorem (every matrix satisfies its own characteristic equation) easy to check for that example (p. 405).
- A tensor is a multidimensional array; the SVD format is not possible for a 3-way tensor. The CP decomposition (a sum of rank-one pieces) gives only an approximation with no orthogonality, and "rank" is not well defined (p. 406).
- cond(A) = ‖A⁻¹‖‖A‖ = σ_max/σ_min. For a simple eigenvalue, the condition number is 1/|yᵀx|, so the eigenvalue problem is perfectly conditioned for symmetric matrices (p. 407).
- For a strictly positive matrix, the top eigenvector is strictly positive (Perron). The text applies this to Markov steady states and to the Google (PageRank) matrix (p. 409).
- Gauss–Jordan elimination finds the independent columns C, the matrix F, and null-space basis vectors; separately, the r×r intersection W of r independent rows and r independent columns is invertible (pp. 410–412).

## L3 — Walkthrough

### A1 The ranks of AB and A+B (p. 400)
Known: rank A = rank Aᵀ. The five facts (the box lists four numbered items):
1. rank AB ≤ rank A and rank AB ≤ rank B.
2. rank(A+B) ≤ rank A + rank B.
3. rank AᵀA = rank AAᵀ = rank A = rank Aᵀ.
4. If A is m×r and B is r×n, both of rank r, then AB has rank r.

*Proof of 1.* Every column of AB is a combination of columns of A, so C(AB) ⊆ C(A) and its dimension cannot be larger. Every row of AB is a combination of rows of B. Row rank equals column rank, so either can be used (p. 400).

*Proof of 2.* Each column of A+B is (column of A)+(column of B). Bases for C(A) and C(B) span C(A+B), as the text puts it. Equality is not always true: it fails for A = B = I (p. 400).

*Proof of 3.* A and AᵀA both have n columns and the same nullspace (Problem 4.19, cited, not shown). So n−r is the same for both, hence so is r. Then rank(Aᵀ) ≥ rank(AᵀA) = rank(A). Exchanging A and Aᵀ gives equal ranks (p. 400).

*Proof of 4.* By fact 3, AᵀA and BBᵀ have rank r. They are r×r, so invertible, and so is their product AᵀABBᵀ. Then
$$r=\operatorname{rank}(A^TABB^T)\le \operatorname{rank}(AB)\le \operatorname{rank}A=r.$$
Note: this does not mean every product of rank-r matrices has rank r. Example: $A=\begin{bmatrix}1\\1\\1\end{bmatrix}$, $B=[1\;2\;-3]$. AB has rank 1, but BA is zero (p. 400).

*Intuition note.* Multiplication can only lose directions, never create them. In fact 4 the inner size r matches both ranks, so nothing can be lost.

### A2 Matrix factorizations (pp. 401–402)
Numbered as the author numbers them, with the stated requirements:
1. **A = CR**: C is m×r (columns of A that are not combinations of earlier ones), R holds the nonzero rows of rref(A). $A=[\,C\;\,CF\,]P$ with P permuting columns (p. 401).
2. **A = C W⁻¹ B**: C = r independent columns, B = r independent rows, W the r×r invertible intersection; $W^{-1}B=R$ (p. 401).
3. **A = LU**: L lower triangular with 1's, U upper triangular with pivots. Needs no row exchanges (p. 401).
4. **A = LDU**: D = pivot matrix. If A is symmetric then $U=L^T$ and $A=LDL^T$ (p. 401).
5. **PA = LU**: A invertible; P does the row exchanges in advance. Alternative $A=L_1P_1U_1$ (p. 401).
6. **S = CᵀC** (Cholesky): S symmetric positive definite; $C^T=L\sqrt D$ (p. 401).
7. **A = QR**: A has independent columns; Q has orthonormal columns (Gram–Schmidt or Householder). If A is square, $Q^{-1}=Q^T$ (p. 401).
8. **A = XΛX⁻¹**: needs n independent eigenvectors (p. 401).
9. **S = QΛQᵀ**: S real symmetric (Spectral Theorem) (p. 401).
10. **A = BJB⁻¹** (Jordan): A square; J has one block per independent eigenvector (p. 402).
11. **A = UΣVᵀ** (SVD): every A. U is m×m, Σ is m×n, V is n×n; $\sigma_i=\sqrt{\lambda_i(A^TA)}=\sqrt{\lambda_i(AA^T)}$; $\sigma_1\ge\dots\ge\sigma_r>0$. Then $A=\sigma_1u_1v_1^T+\dots+\sigma_ru_rv_r^T$, a sum of r rank-one matrices. If S is symmetric positive definite, then U = V = Q and Σ = Λ (p. 402).
12. **A⁺ = VΣ⁺Uᵀ** (pseudoinverse): no requirements. A⁺A = projection onto the row space, AA⁺ = projection onto the column space. $A^+=A^{-1}$ if A is invertible. The shortest least-squares solution of Ax = b is $x^+=A^+b$, which solves $A^TAx^+=A^Tb$ (p. 402).
13. **A = QS** (polar): A invertible; $S^2=A^TA$; S is semidefinite if A is singular. Reverse form A = KQ has $K^2=AA^T$. Both have $Q=UV^T$ (p. 402).
14. **A = UΛU⁻¹**: A normal ($\bar A^TA=A\bar A^T$); U unitary (p. 402).
15. **A = QTQ⁻¹** (Schur): any square A; T triangular, Q unitary (p. 402).
16. **FFT step**: $F_n=\begin{bmatrix}I&D\\I&-D\end{bmatrix}\begin{bmatrix}F_{n/2}&\\&F_{n/2}\end{bmatrix}\,[\text{even-odd permutation}]$. $F_n$ has entries $w^{jk}$ with $w^n=1$, and $F_n\bar F_n=nI$. D has $1,w,\dots,w^{n/2-1}$ on its diagonal. For $n=2^\ell$, $F_nx$ needs only $\tfrac12 n\ell=\tfrac12 n\log_2 n$ multiplications. With $m=n/2$: $y_j=y_j'+(w_n)^jy_j''$ and $y_{j+m}=y_j'-(w_n)^jy_j''$ for $j=0,\dots,m-1$ (p. 402).

### A3 Counting parameters (p. 403)
Plan: in each equation like A = LU, both sides should have the same number of free parameters (p. 403).

| Matrix | Free parameters |
|---|---|
| L (unit triangular) | ½n(n−1) |
| U (triangular) | ½n(n+1) |
| Q (orthogonal) | ½n(n−1) |
| S (symmetric) | ½n(n+1) |
| Λ (diagonal) | n |
| X (eigenvectors) | n²−n |

- **LU:** ½n(n−1) + ½n(n+1) = n² (p. 403).
- **Q:** q₁ is a unit vector (n−1 free). q₂ is a unit vector orthogonal to q₁ (n−2 free), and so on. The sum (n−1)+(n−2)+…+1 equals ½n(n−1) (p. 403).
- **X:** each eigenvector can be scaled by any c ≠ 0. Requiring the largest component to be 1 leaves n−1 parameters per eigenvector. The count then agrees for the first five factorizations (p. 403).
- **SVD, reduced form** $A_{m\times n}=U_{m\times r}\Sigma_{r\times r}V^T_{r\times n}$ (known zeros are not free). Take m ≤ n and full rank r = m. A has mn parameters. U has ½m(m−1), Σ has m, V has (n−1)+…+(n−m) = mn − ½m(m+1). The total is mn (p. 403). (Added step: ½m(m−1)+m+mn−½m(m+1) = mn.)
- **Rank r:** U has mr − ½r(r+1), V has nr − ½r(r+1), Σ has r. Total: $mr+nr-r^2=(m+n-r)r$ (p. 403).
- **CR:** C has mr; R has nr − r² (its identity block is fixed). Total mr + nr − r², the same (p. 403).

*Intuition note.* A matrix of rank r is not free: the (m+n−r)r count is smaller than mn when r < min(m, n). Factorizations spend exactly the available freedom.

### A4 Codes and algorithms (p. 404)
A reference list. LAPACK is first choice for dense problems; ScaLAPACK for very large ones; COIN/OR for optimization. The page then lists sources by task: direct solves, eigenvalues/SVD, iterative methods, optimization, randomized linear algebra, FFT (FFTW), and deep-learning software (p. 404).

### A5 The Jordan form (p. 405)
Some matrices with repeated eigenvalues lack n independent eigenvectors, so X is not invertible and XΛX⁻¹ fails. The Jordan form J has k blocks when A has k independent eigenvectors. J has the same eigenvalues as A. Each block has λᵢ on the diagonal and 1's just above it. A diagonalizable A has k = n and all blocks 1×1. Each block has one true eigenvector (1,0,…,0) and one eigenvalue. B contains eigenvectors and "generalized eigenvectors" (p. 405).

*Example (not proof).* $J=\begin{bmatrix}3&1&0\\0&3&0\\0&0&3\end{bmatrix}$ has λ = 3, 3, 3 and only two genuine eigenvectors, (1,0,0) and (0,0,1). Powers and exponential of a block (p. 405):
$$\begin{bmatrix}3&1\\0&3\end{bmatrix}^N=\begin{bmatrix}3^N&N3^{N-1}\\0&3^N\end{bmatrix},\qquad \exp\!\Big(\begin{bmatrix}3&1\\0&3\end{bmatrix}t\Big)=\begin{bmatrix}e^{3t}&te^{3t}\\0&e^{3t}\end{bmatrix}.$$
This gives the "missing solution" $te^{3t}$ of dU/dt = JU. A triple eigenvalue with one eigenvector and one block would also involve $t^2e^{3t}$ (p. 405).

**Cayley–Hamilton:** every A satisfies its own characteristic equation, p(A) = 0. For the example, $p(\lambda)=(\lambda-3)^3$ and $(J-3I)^3=\begin{bmatrix}0&1&0\\0&0&0\\0&0&0\end{bmatrix}^3=0$. The author writes $(A-3I)^3=B(J-3I)^3B^{-1}=0$ (p. 405).

*Intuition note.* When eigenvectors run out, the Jordan form keeps 1's above the diagonal and B contains generalized eigenvectors. In the 2×2 block example, that 1 is where the extra factor t (or N) appears in the exponential and in the powers.

### A6 Tensors (p. 406)
A tensor here is a multidimensional array; a matrix is a 2-way tensor, and a 3-way tensor $T_{ijk}$ is a stack of matrices. Examples: a colour image (3 slices R, G, B), and a joint probability tensor $p_{ijk}$ (age, height, weight) whose entries sum to 1 (p. 406).

For a matrix, the SVD splits A into rank-one pieces with orthogonal u's and orthogonal v's. This format is not possible for a 3-way tensor. Instead, **CP decomposition** (p. 406):
$$T\approx a_1\circ b_1\circ c_1+\dots+a_R\circ b_R\circ c_R.\tag{1}$$
Orthogonality is generally impossible. The number of pieces is not set by T, so its "rank" is not well defined. One option: solve alternately for the a's, then b's, then c's, each step reducible to least squares (p. 406).

### A7 The condition number (p. 407)
For Ax = b, the data change is Δb and the solution change is Δx = A⁻¹Δb. Equation (1) defines two versions (p. 407):
$$\text{Absolute}=\max_{b,\Delta b}\frac{\|\Delta x\|}{\|\Delta b\|}=\max\frac{\|A^{-1}\Delta b\|}{\|\Delta b\|},\qquad \text{Relative}=\max_{b,\Delta b}\frac{\|\Delta x\|/\|x\|}{\|\Delta b\|/\|b\|}.$$
The absolute version is not scale-free: dividing A by 10 multiplies A⁻¹ by 10, yet solving did not become 10 times harder. The relative version is the right choice (p. 407):
$$\operatorname{cond}(A)=\max_{b,\Delta b}\frac{\|A^{-1}\Delta b\|}{\|\Delta b\|}\frac{\|Ax\|}{\|x\|}=\|A^{-1}\|\,\|A\|=\frac{\sigma_{\max}}{\sigma_{\min}}.\tag{2}$$
Reason: for diagonal Σ, ‖Σ‖ = σ₁ and ‖Σ⁻¹‖ = 1/σ_min. Orthogonal U, V leave norms unchanged (p. 407).

σ_min (not λ_min) measures the distance from A to the nearest singular matrix: bring the smallest singular value to zero (p. 407).

**Eigenvalue conditioning.** Let λ be a simple root of det(A−λI) = 0, with Ax = λx, Aᵀy = λy and unit vectors. The condition number of λ is 1/|yᵀx| = 1/|cos θ|, where θ is the angle between right and left eigenvectors. Symmetric A has y = x, so cos θ = 1 (perfectly conditioned). Orthogonal Q has ‖Q‖‖Q⁻¹‖ = 1. The formula comes from $\Delta\lambda\approx (y^T\Delta A\,x)/y^Tx$ (p. 407).

*Intuition note.* A large σ_max/σ_min means that some input directions are stretched far more than others, so small errors in b can become large errors in x.

### A8 Markov matrices and Perron–Frobenius (pp. 408–409)
Positive matrix: all $a_{ij}>0$. Nonnegative: all $a_{ij}\ge0$. A Markov matrix has nonnegative entries with every column adding to 1 (p. 408).

**Fact:** the largest eigenvalue of a Markov matrix is always λ = 1 (stated, p. 408). The text justifies that 1 is an eigenvalue: columns of M−I add to zero, so the rows add to a zero row, so M−I is not invertible (p. 408).

*Example A* $=\begin{bmatrix}0.8&0.3\\0.2&0.7\end{bmatrix}$ has eigenvalues 1 and ½, with $x_1=(0.6,0.4)$ (steady state) and $x_2=(1,-1)$ (transient, since $Ax_2=\tfrac12x_2$). *Example B* $=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has eigenvalues 1 and −1 (p. 408).

*Rental cars.* Start $y_0=(100,0)$ in (Chicago, Denver) and set $y_{n+1}=Ay_n$: $y_1=(80,20)$, $y_2=(70,30)$, $y_3=(65,35)$, …, $y_\infty=(60,40)$. Writing $y_0=(60,40)+(40,-40)$ gives $y_n=(60,40)+(\tfrac12)^n(40,-40)$ (p. 408). So $A^n=X\Lambda^nX^{-1}$ tends to a rank-one matrix $A^\infty$ (p. 408).

For B, cars swap cities each month. $y_0=(60,40)=(50,50)+(10,-10)$, $y_1=By_0=(40,60)=(50,50)-(10,-10)$, $y_2=y_0$, … There is no steady state because |λ₂| = 1. This will not happen when all $a_{ij}>0$. |λ₁| = |λ₂| *might* happen when B has some zeros (p. 409).

**Theorem (Perron).** For positive A, all entries of $Ax=\lambda_{\max}x$ are strictly positive (p. 409).

*Proof* (p. 409):
1. Consider all numbers t with Ax ≥ tx for some nonnegative x ≠ 0. The largest, t_max, is attained.
2. Suppose Ax ≥ t_max x is not an equality. Multiply by A; since A > 0, this gives a strict inequality $A^2x>t_{\max}Ax$.
3. So the positive vector y = Ax satisfies Ay > t_max y. Then t_max could be increased, a contradiction. Hence $Ax=t_{\max}x$, so t_max = λ_max.
4. x is positive because Ax on the left is positive.
5. No eigenvalue is larger: if Az = λz, then $|\lambda||z|=|Az|\le A|z|$ by the triangle inequality. |z| is nonnegative, so |λ| is a candidate t and |λ| ≤ t_max.

Frobenius allowed zeros in the matrix. If some power $A^m$ is strictly positive ("primitive" matrices), Perron applies, and there is one steady-state eigenvector for λ = 1 (p. 409).

**Google matrix.** Start with $A_{ij}=1$ when page j links to page i. Divide column j by the number of outgoing links, so columns sum to 1. Then $G_{ij}=\alpha A_{ij}+(1-\alpha)/N$, so every $G_{ij}>0$ (Perron applies). Reference: Langville & Meyer (2011) (p. 409).

*Intuition note.* For a positive Markov matrix the text says |λ₁| = |λ₂| does not happen; in example A the second pattern fades. Zeros, as in B, allow |λ₂| = |λ₁| and the cars swap cities forever.

### A9 Elimination and factorization (pp. 410–412)
Overview: rref contains I in the first r independent columns. F multiplies them to give the n−r dependent columns, and F reveals bases for the row space and nullspace (p. 410).

**1. A = CR.** C contains the first r independent columns of A; every other column is a combination CF of them. With $R=[\,I\;\,F\,]P$,
$$A=CR=[\,C\;\;CF\,]P.\tag{1}$$
P = I if the independent columns come first. The factorization is confirmed, not computed. Allowed row operations: (a) subtract a multiple of a row from another (above or below), (b) exchange rows, (c) divide a row by its first nonzero entry (all invertible; Gauss–Jordan). Then
$$\text{rref}(A)=\begin{bmatrix}I&F\\0&0\end{bmatrix}P.\tag{2}$$
Using actual columns of A in C is more elementary and less stable than using SVD vectors (p. 410).

**2. Column-by-column construction.** After k columns, the part is $\begin{bmatrix}I_k&F_k\\0&0\end{bmatrix}P_k$; the next column is $\begin{bmatrix}u\\\ell\end{bmatrix}$ (3). If ℓ = 0, the column is dependent, and u joins $F_k$ to make $F_{k+1}$. If ℓ ≠ 0, it is independent: pick a nonzero in ℓ as pivot (preferably the largest), move that row up to row k+1, and eliminate the rest of the column. It then joins $I_k$ to make $I_{k+1}$. The pivot column numbers give the columns of C (p. 411).

**3. Nullspace.** From A = C[I F]P, the matrix $X=P^T\begin{bmatrix}-F\\I_{n-r}\end{bmatrix}$ has n−r columns with AX = 0 (4). Gauss–Jordan costs more than stopping at a triangular system Ux = c; for solving equations, LU is faster (p. 411).

**4. Block elimination.** If the top-left r×r block W is invertible, then F = W⁻¹H and
$$A=\begin{bmatrix}W&H\\J&K\end{bmatrix}\to\begin{bmatrix}I&F\\0&0\end{bmatrix}=\text{rref}(A).\tag{5}$$
The last m−r rows are combinations of the first r: $[\,J\;K\,]=JW^{-1}[\,W\;H\,]$. In general, permutations $P_r,P_c$ move W to the corner (p. 412):
$$P_rAP_c=\begin{bmatrix}W&H\\J&K\end{bmatrix}\to\begin{bmatrix}I&W^{-1}H\\0&0\end{bmatrix}.\tag{6}$$

**5. Intersection is invertible.** Take r independent rows of A (submatrix B) and r independent columns (submatrix C). Their r×r intersection W has rank r, so W is invertible. *Proof:* every column of A is a combination of the r columns of C. So every column of B (r×n) is the same combination of the columns of W. B has rank r, so its column space is all of ℝʳ. Hence the column space of W is ℝʳ and W has rank r (p. 412).

*Intuition note.* Elimination sorts columns into "new direction" or "already covered." The identity block marks the new ones, and F records how the covered ones are built from them.

## Toy example (ours)
$A=\begin{bmatrix}1&0&1\\0&1&1\\1&1&2\end{bmatrix}$. Column 3 = column 1 + column 2, so rank 2.
- Row 3 − row 1 − row 2 = 0, so $\text{rref}(A)=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}$. Thus $F=\begin{bmatrix}1\\1\end{bmatrix}$, P = I, $C=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$, $R=\begin{bmatrix}1&0&1\\0&1&1\end{bmatrix}$.
- Check CR: row 1 = (1,0,1); row 2 = (0,1,1); row 3 = (1,0,1)+(0,1,1) = (1,1,2) ✓.
- Null space: $X=\begin{bmatrix}-F\\I_1\end{bmatrix}=(-1,-1,1)^T$. AX = (−1+0+1, 0−1+1, −1−1+2) = (0,0,0) ✓.
- Rank facts: $A^TA=A^2=\begin{bmatrix}2&1&3\\1&2&3\\3&3&6\end{bmatrix}$; row 3 = row 1 + row 2, rows 1, 2 independent, so rank 2 = rank A ✓. Also $A^2X$ has first entry −2−1+3 = 0, consistent with equal nullspaces.

## Concepts
- [[rank]] — number of independent columns (= independent rows); cannot increase under multiplication (p. 400)
- [[column space (range)]] — C(AB) lies inside C(A) (p. 400)
- [[null space (kernel)]] — AᵀA and A have the same nullspace; special solutions X from F (pp. 400, 411)
- [[column-row-factorization]] (new) — A = CR with actual independent columns of A in C and R from rref (p. 401)
- [[reduced-row-echelon-form]] (new) — rref(A) = [I F; 0 0]P; I marks independent columns (p. 410)
- [[lu-factorization]] (new) — A = LU, L with 1's, U with pivots; needs no row exchanges (p. 401)
- [[cholesky-factorization]] (new) — S = CᵀC for symmetric positive definite S (p. 401)
- [[polar-decomposition]] (new) — A = QS for invertible A, with Q = UVᵀ and S² = AᵀA (p. 402)
- [[fast-fourier-transform]] (new) — F_n split into two F_{n/2} steps; ½n log₂ n multiplications when n = 2^ℓ (p. 402)
- [[parameter-counting]] (new) — equate free parameters on both sides of a factorization (p. 403)
- [[jordan-form]] (new) — nearly diagonal form with one block per independent eigenvector (p. 405)
- [[cayley-hamilton-theorem]] (new) — every matrix satisfies p(A) = 0 (p. 405)
- [[tensor-cp-decomposition]] (new) — approximate sum of R rank-one 3-way pieces; no orthogonality (p. 406)
- [[condition number]] — relative condition = ‖A⁻¹‖‖A‖ = σ_max/σ_min (p. 407)
- [[singular value decomposition (SVD)]] — A = UΣVᵀ as a sum of r rank-one matrices (p. 402)
- [[pseudoinverse]] — A⁺ = VΣ⁺Uᵀ; x⁺ = A⁺b is the shortest least-squares solution (p. 402)
- [[spectral theorem]] — S = QΛQᵀ for real symmetric S (p. 401)
- [[Markov (stochastic) matrix]] — nonnegative entries, columns add to 1; eigenvalue 1 is always present; example A reaches a steady state, example B does not (pp. 408–409)
- [[Perron–Frobenius theorem]] — here only Perron's case: positive A has a strictly positive top eigenvector (p. 409)
- [[google-pagerank-matrix]] (new) — G = αA + (1−α)/N with column-normalized links, all entries positive (p. 409)

## Canonical instances
- [[rank-one-AB-vs-BA]] — A = (1,1,1)ᵀ, B = [1 2 −3]: AB rank 1, BA = 0 (p. 400)
- [[jordan-block-example]] — J with eigenvalue 3, two genuine eigenvectors, producing te^{3t} (p. 405)
- [[rental-cars-markov]] — Chicago/Denver cars, steady state (60,40), transient decaying by ½ (p. 408)
- [[swap-cars-matrix-B]] — permutation Markov matrix with eigenvalues 1, −1: no steady state (p. 409)
- [[color-image-tensor]] — R, G, B slices as a 3-way tensor (p. 406)
- [[joint-probability-tensor]] — $p_{ijk}$ for age, height, weight (p. 406)
- [[google-matrix]] — PageRank matrix with all positive entries (p. 409)

## Bridges (candidates)
- [same-math] Perron's theorem for positive A ↔ network science: eigenvector centrality and PageRank use the dominant positive eigenvector of a nonnegative matrix.
- [structural-analogy] σ_max/σ_min ↔ statistics: near-singular design matrices make least-squares estimates unstable.
- [structural-analogy] CP tensor decomposition ↔ data science: low-rank matrix factorization, extended to three indices without orthogonality.
- [structural-analogy] Parameter counting for A = LU, UΣVᵀ ↔ geometry/statistics: degrees of freedom of a model class.

## Questions this raises
- Why is the largest Markov eigenvalue exactly 1? A8 shows 1 is an eigenvalue but only states that none is larger.
- How much does the damping α in the Google matrix change the steady state and how fast it is reached?
- How do alternating least squares for CP behave without a well-defined tensor rank?
- Why does the nearest singular matrix depend on σ_min and not on λ_min?

## Reading notes
- Printed = pdf − 10 (pdf 410 is printed 400). Text layer is garbled in places (equations, matrices); I checked the page images.
- A5 uses J = BAB⁻¹ and A = B⁻¹JB, while A2 item 10 and the Cayley–Hamilton line use A = BJB⁻¹. The conventions are inconsistent in the source.
- A7 prints the nearest singular matrix as U(Σ − σ_min I)Vᵀ. Read literally this subtracts σ_min from every singular value; the text's intent ("bring the smallest singular value to zero") is to change only the smallest one.
- A8: the printed A^∞ appears to have first row (0.6, 0.4), but XΛ^∞X⁻¹ = [0.6 0.6; 0.4 0.4] (added step: column (0.6,0.4) times row (1,1)). The columns must add to 1.
- A1, fact 2: the text says bases for C(A) and C(B) "span C(A+B)". Strictly, they span a space that contains C(A+B).
- A9 ends with a printed note that it was submitted to the American Mathematical Monthly.
- A4 gives only names and URLs, so I summarized it briefly. The text mentions Problem 4.19 but does not give it.
