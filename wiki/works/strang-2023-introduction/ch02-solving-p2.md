---
id: strang-2023-introduction/ch02-solving-p2
work: strang-2023-introduction
unit: "2 Solving Linear Equations Ax = b (part 2/2): §2.4 Permutations and Transposes, §2.5 Derivatives and Finite Difference Matrices, Thoughts on Chapter 2"
pages: 64-83
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Permutations, Transposes, and Finite Difference Matrices

## L0 — One line
Row exchanges (permutations) rescue elimination as PA = LU, the transpose is the matrix that moves between inner products, and second-difference matrices K, T, B show how boundary conditions decide invertibility.

## L1 — The gist (≤ 120 words)
This part asks how elimination copes with a zero pivot, and what the transpose really is. Answers: a permutation matrix P reorders rows so that PA = LU; the transpose satisfies (Ax)ᵀy = xᵀ(Aᵀy) and (AB)ᵀ = BᵀAᵀ; the product AᵀA is always symmetric, and a symmetric matrix keeps its symmetry in the triple product S = LDLᵀ (shown on p. 70 with U = Lᵀ after the pivots are divided out). Section 2.5 turns derivatives into differences and builds the second-difference matrices K, T, B for different boundary conditions. K and T are invertible; B is singular. The author calls K one of the most important matrices in scientific computing (p. 78).

**Prerequisites:** matrix multiplication by rows and columns; elimination and A = LU; inverse of a product; the derivative, second derivative and integration by parts.

## L2 — Key ideas
- A permutation matrix has the rows of I in some order; PᵀP = I, so P⁻¹ = Pᵀ, and a product of permutations is a permutation (pp. 64–65).
- If A is invertible, some P gives PA = LU with no zero pivots. Codes also exchange rows to get large pivots ("partial pivoting"), which makes elimination more stable (pp. 65–66).
- Transpose rules: (A+B)ᵀ = Aᵀ+Bᵀ, (AB)ᵀ = BᵀAᵀ, (A⁻¹)ᵀ = (Aᵀ)⁻¹ (p. 67).
- The better definition of Aᵀ: it is the matrix with (Ax)ᵀy = xᵀ(Aᵀy). For A = d/dt this gives Aᵀ = −d/dt, via integration by parts (pp. 68–69).
- AᵀA and AAᵀ are symmetric. S = LDLᵀ keeps the symmetry that LU loses. The block matrix [[I,A],[Aᵀ,0]] (called the saddle-point matrix) is invertible exactly when AᵀA is (p. 70).
- Differences approximate derivatives. Centered differences are second-order accurate (the leading O(h) error cancels); forward and backward ones are only first-order accurate (pp. 75–76).
- K (fixed-fixed: both ends held at zero) is symmetric, tridiagonal (nonzeros only on three diagonals), Toeplitz (constant diagonals) and invertible. T (free-fixed) is invertible with T = LLᵀ. B (free-free) is singular because Bx = 0 for constant x (pp. 77–80).
- Chapter 2 solves Ax = b for square invertible A. The author says the questions of non-invertible, non-square and very large matrices are real ones, and the answers will fill the book (p. 83).

## L3 — Walkthrough

### 2.4 Permutations and Transposes

**Permutation matrices (p. 64).** A permutation matrix P has the same rows as I, in any order; there are n! orders. It has a 1 in every row and every column, and zeros elsewhere. Px puts the components of x in a new order. Example: P = [[0,0,1],[1,0,0],[0,1,0]] gives Px = (x₃, x₁, x₂), a circular shift. Then P³ = I.

Size 3 has 3! = 6 permutation matrices; size 4 has 4! = 24. The author lists 4×4 examples: reverse the order (P² = I), keep x₄ fixed (P³ = I), circular shift (P⁴ = I), and "evens before odds" (the Fast Fourier Transform ordering). The author says half of the n! permutations are "even" (an even number of row exchanges reaches I) and half are "odd". The author also reports that Diaconis proved 7 random permutations shuffle a new deck well (p. 64).

The rows of P are the columns of P⁻¹ = Pᵀ, so PᵀP = I (p. 64).

**Properties (p. 65).**
1. The n 1's lie in n different rows and n different columns.
2. The columns of P are orthogonal (all dot products between columns are zero).
3. P₁P₂ is a permutation, and so is P⁻¹.
4. If A is invertible, some P orders its rows so that elimination on PA meets no zero pivot, giving PA = LU.

*Intuition note.* A permutation only shuffles; it loses no information, so shuffling back (Pᵀ) undoes it exactly. That is why PᵀP = I.

**PA = LU (p. 65).** Take A = [[1,2,a],[2,4,b],[3,7,c]]. Elimination subtracts 2·row 1 from row 2 and 3·row 1 from row 3:
$$A \xrightarrow{E} \begin{bmatrix}1&2&a\\0&0&b-2a\\0&1&c-3a\end{bmatrix} \xrightarrow{P} \begin{bmatrix}1&2&a\\0&1&c-3a\\0&0&b-2a\end{bmatrix}=U.$$
The zero second pivot is rescued by exchanging rows 2 and 3. A is invertible if and only if b−2a is not zero (the third pivot). If b = 2a, row 2 equals 2·(row 1), so A is surely not invertible (p. 65).

Exchanging rows first gives PA = LU:
$$\underbrace{\begin{bmatrix}1&0&0\\0&0&1\\0&1&0\end{bmatrix}}_{P}\underbrace{\begin{bmatrix}1&2&a\\2&4&b\\3&7&c\end{bmatrix}}_{A}=\underbrace{\begin{bmatrix}1&2&a\\3&7&c\\2&4&b\end{bmatrix}}_{PA}=\underbrace{\begin{bmatrix}1&0&0\\3&1&0\\2&0&1\end{bmatrix}}_{L}\underbrace{\begin{bmatrix}1&2&a\\0&1&c-3a\\0&0&b-2a\end{bmatrix}}_{U}$$
With several exchanges, P holds them all. Drucker's bookkeeping adds a column 1 2 3 to A. It is carried along and tracks the original row numbers. Here it ends as 1 3 2, which gives P (p. 65).

**Partial pivoting (p. 66).** Small pivots are unsafe. A good code exchanges rows to put the largest available number in the pivot position (it chooses the largest in the column below). The computation is then more stable. For the same A, column 1 offers 1, 2, 3, so rows 1 and 3 are exchanged. The result is
$$U=\begin{bmatrix}3&7&c\\0&-\tfrac23&b-\tfrac23c\\0&0&a-\tfrac12 b\end{bmatrix},\quad L=\begin{bmatrix}1&0&0\\ \tfrac23&1&0\\ \tfrac13&\tfrac12&1\end{bmatrix},\quad P=\begin{bmatrix}0&0&1\\0&1&0\\1&0&0\end{bmatrix},\quad PA=LU.$$
All entries of L are ≤ 1 when each pivot is larger than all the numbers below it (p. 66).

**PAQ (p. 66).** P reorders rows; Q reorders columns. For P = rows (2,3,1) and Q = columns (3,2,1):
$$PAQ=\begin{bmatrix}a_{23}&a_{22}&a_{21}\\a_{33}&a_{32}&a_{31}\\a_{13}&a_{12}&a_{11}\end{bmatrix}\tag{2}$$
There are 6 row orders times 6 column orders = 36 matrices PAQ. These are not all 9! = 362,880 orders of the nine entries: the first index is constant along each row and the second constant down each column. The author then asks whether C(PAQ) equals C(A); no answer is given here (p. 66).

**The transpose (p. 67).** The columns of Aᵀ are the rows of A: (Aᵀ)ᵢⱼ = Aⱼᵢ. If A is m×n, Aᵀ is n×m. Example: A = [[1,2,3],[0,0,4]] gives Aᵀ = [[1,0],[2,0],[3,4]]. The transpose of a lower triangular matrix is upper triangular, and (Aᵀ)ᵀ = A.
$$(A+B)^T=A^T+B^T\tag{1}$$
$$(AB)^T=B^TA^T\tag{2}$$
$$(A^{-1})^T=(A^T)^{-1}\tag{3}$$
*Proof of (2).* Ax combines the columns of A, and xᵀAᵀ combines the rows of Aᵀ. These are the same combination of the same vectors, so (Ax)ᵀ = xᵀAᵀ. If B has columns x₁, x₂, …, then AB has columns Ax₁, Ax₂, …. Transposing puts the rows x₁ᵀAᵀ, x₂ᵀAᵀ, … into the matrix BᵀAᵀ (p. 67, labelled (6) in print).

Numerical check (p. 68): A = [[1,0],[1,1]], B = [[5,0],[4,1]]. Then AB = [[5,0],[9,1]] and BᵀAᵀ = [[5,4],[0,1]]·[[1,1],[0,1]] = [[5,9],[0,1]], which is (AB)ᵀ. The rule extends: (ABC)ᵀ = CᵀBᵀAᵀ (p. 68).

*Proof of (3).* Transpose A⁻¹A = I: Aᵀ(A⁻¹)ᵀ = I. Likewise AA⁻¹ = I gives (A⁻¹)ᵀAᵀ = I. So (A⁻¹)ᵀ is the inverse of Aᵀ, and Aᵀ is invertible exactly when A is (p. 68). Example: A = [[1,0],[6,1]], A⁻¹ = [[1,0],[−6,1]], Aᵀ = [[1,6],[0,1]]. Both (A⁻¹)ᵀ and (Aᵀ)⁻¹ equal [[1,−6],[0,1]] (p. 68).

**Inner products (p. 68).** The dot (inner) product is xᵀy, a (1×n)(n×1) product, so a number. The outer (rank-one) product is xyᵀ, an (n×1)(1×n) product, so an n×n matrix. The author gives three uses of the inner product: work = xᵀf (mechanics), heat loss = eᵀy (circuits), income = qᵀp (economics).

*Definition of Aᵀ.* The author calls "flip across the diagonal" not a real definition. Aᵀ is the matrix that makes the inner products equal:
$$(Ax)^Ty=x^T(A^Ty).$$

*Example 1 (p. 69).* A = [[−1,1,0],[0,−1,1]], x = (x₁,x₂,x₃), y = (y₁,y₂). Then (Ax)ᵀy = (x₂−x₁)y₁ + (x₃−x₂)y₂ = x₁(−y₁) + x₂(y₁−y₂) + x₃y₂, and Aᵀy = (−y₁, y₁−y₂, y₂). So xᵀ(Aᵀy) is the same number.

*Example 2 (p. 69).* Take A = d/dt. For functions the inner product is defined by
$$x^Ty=\int_{-\infty}^{\infty}x(t)y(t)\,dt\tag{8}$$
$$\int_{-\infty}^{\infty}\frac{dx}{dt}\,y(t)\,dt=\int_{-\infty}^{\infty}x(t)\left(-\frac{dy}{dt}\right)dt\tag{9}$$
This is integration by parts, with x(±∞) assumed zero. The derivative moves from x to y and a minus sign appears. So the transpose of d/dt is Aᵀ = −A = −d/dt: the derivative is anti-symmetric (Aᵀ = −A). The 3×2 matrix Aᵀ of Example 1 is minus a difference matrix, which follows the same pattern.

*Intuition note.* Aᵀ is the matrix that lets A act on the other side of an inner product (our paraphrase of the defining identity). For a difference matrix this is minus the opposite difference, just as moving a derivative across an integral costs a minus sign.

**Symmetric matrices (pp. 69–70).** S is symmetric if Sᵀ = S, i.e. sⱼᵢ = sᵢⱼ. Examples: S = [[1,2],[2,5]], D = diag(1,10). The author says these are, in his opinion, the most important matrices. The inverse of a symmetric invertible matrix is symmetric, since (S⁻¹)ᵀ = (Sᵀ)⁻¹ = S⁻¹. Examples: S⁻¹ = [[5,−2],[−2,1]], D⁻¹ = diag(1, 0.1).

**Symmetric products (p. 70).** For any (possibly rectangular) A, (AᵀA)ᵀ = Aᵀ(Aᵀ)ᵀ = AᵀA (10). So AᵀA is square and symmetric, and AAᵀ is symmetric too, but in general a different matrix. Example 3: A = [[−1,1,0],[0,−1,1]] gives AAᵀ = [[2,−1],[−1,2]] (m×m) and AᵀA = [[1,−1,0],[−1,2,−1],[0,−1,1]] (n×n). Both have positive diagonal (the author asks "why?"), and even if m = n it is very likely that AᵀA ≠ AAᵀ.

**S = LDLᵀ (p. 70).** Symmetry makes elimination twice as fast. LU misses the symmetry of S; dividing the pivots out of U leaves U = Lᵀ:
$$\begin{bmatrix}1&2\\2&7\end{bmatrix}=\begin{bmatrix}1&0\\2&1\end{bmatrix}\begin{bmatrix}1&2\\0&3\end{bmatrix}=\begin{bmatrix}1&0\\2&1\end{bmatrix}\begin{bmatrix}1&0\\0&3\end{bmatrix}\begin{bmatrix}1&2\\0&1\end{bmatrix}.$$
The pivots 1, 3 sit in D.

*Example 4 (p. 70).* The saddle-point matrix from least squares is S = [[I,A],[Aᵀ,0]] = Sᵀ, of size m+n. Block elimination subtracts Aᵀ(row 1), which gives U = [[I,A],[0,−AᵀA]]. Then
$$S=LDL^T=\begin{bmatrix}I&0\\A^T&I\end{bmatrix}\begin{bmatrix}I&0\\0&-A^TA\end{bmatrix}\begin{bmatrix}I&A\\0&I\end{bmatrix}.$$
S is invertible ⇔ AᵀA is invertible ⇔ Ax ≠ 0 whenever x ≠ 0 (as printed).

*Intuition note.* AᵀA is invertible when A destroys no nonzero vector. The saddle-point matrix S inherits this test through its block pivot −AᵀA.

**Problem Set 2.4 (pp. 71–73).** Thirty problems on transposes, permutations, symmetric factorizations and PA = LU. Selected ones are listed under Exercises.

### 2.5 Derivatives and Finite Difference Matrices

**Derivatives and differences (pp. 74–75).** dy/dx > 0 means the graph of y goes upward; d²y/dx² > 0 means it bends upward. For y = x², dy/dx = 2x and d²y/dx² = 2, so the graph bends up everywhere. With Δy = y(x+h) − y(x), the author gives three statements (p. 74):
1. Δy ≈ h·dy/dx.
2. A better approximation adds ½h²·d²y/dx².
3. The exact Δy is the integral of dy/dx from x to x+h.

For y = x²: Δy = 2hx + h² = h·dy/dx + ½h²·d²y/dx² (first order: tangent line; adding the second-order term: tangent parabola) (p. 74). Here the tangent parabola is the actual parabola (p. 75).

The **Taylor series** includes all derivatives; each term is hⁿ/n! times the nth derivative (p. 75):
$$y(x+h)=y(x)+hy'(x)+\tfrac12h^2y''(x)+\cdots+\tfrac1{n!}h^n\frac{d^ny}{dx^n}(x)+\cdots$$
The first form uses derivatives at 0: y(x) = y(0) + x·y′(0) + … + (1/n!)xⁿ·y⁽ⁿ⁾(0) + …. For eˣ the series converges at all points (entire analytic function). For 1/(1−x), the series 1 + x + x² + … converges only for |x| < 1; x = 1 is a singularity called a pole (p. 75).

**Derivatives from differences (pp. 75–76).** Start from the tangent-parabola approximation (1): y(x+h) ≈ y(x) + h·y′(x) + ½h²y″(x). Write it at x+h and at x−h (replace h by −h):
$$y(x+h)-y(x)\approx h\frac{dy}{dx}+\tfrac12h^2\frac{d^2y}{dx^2}\tag{2a}$$
$$y(x-h)-y(x)\approx -h\frac{dy}{dx}+\tfrac12h^2\frac{d^2y}{dx^2}\tag{2b}$$
Subtract (2b) from (2a) and divide by 2h (the h² terms cancel; added step: left side becomes y(x+h) − y(x−h)):
$$\frac{y(x+h)-y(x-h)}{2h}\approx\frac{dy}{dx}\quad\text{(centered difference)}\tag{3}$$
Add (2b) to (2a) and divide by h² (the first-derivative terms cancel):
$$\frac{y(x+h)-2y(x)+y(x-h)}{h^2}\approx\frac{d^2y}{dx^2}\quad\text{(second difference)}\tag{4}$$
For the second-order equation $y''+ay'+by=f(x)$ (5), the finite difference version is
$$\frac{y(x+h)-2y(x)+y(x-h)}{h^2}+a\frac{y(x+h)-y(x-h)}{2h}+by(x)=f(x)\tag{6}$$
Forward and backward differences, (y(x+h)−y(x))/h and (y(x)−y(x−h))/h, have O(h) error (7). Averaging them gives the centered difference, in which the leading O(h) error cancels. So the centered difference has second-order accuracy (p. 76).

*Intuition note.* Using points on both sides of x lets the errors from the two sides cancel. That is why the centered and second differences are the workhorse formulas.

**Second difference matrices K, T, B (pp. 76–77).** The matrices use the pattern −1, 2, −1 (this approximates −d²y/dx²). The approach is to replace a differential equation by N difference equations at N meshpoints xᵢ = ih. The boundary points are x₀ = 0 and x_{N+1} = 1, so the meshwidth is h = 1/(N+1). For −u″ = f(x) with u(0) = u(1) = 0, the unknowns are u₁,…,u_N, with u₀ = u_{N+1} = 0. They approximate u(h),…,u(Nh). For N = 4 and h = 1/5:
$$\frac1{h^2}\begin{bmatrix}2&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&2\end{bmatrix}\begin{bmatrix}u_1\\u_2\\u_3\\u_4\end{bmatrix}=\begin{bmatrix}f(h)\\f(2h)\\f(3h)\\f(4h)\end{bmatrix},\quad\text{i.e. } KU/h^2=F.$$
Row 1 times U is 2u₁ − u₂. The first and last rows have the fixed boundary conditions built in (p. 77).

**Properties of K (pp. 77–78).**
1. *Symmetric:* Kᵀ = K.
2. *Banded (tridiagonal):* nonzeros lie on three diagonals, so elimination is easy and fast. For N = 100, K has 100+99+99 nonzeros out of 10000 entries, less than 3%.
3. *Constant diagonals (Toeplitz, shift-invariant):* this reflects the constant coefficient of the differential equation. Shift-invariance fails at the boundaries. Constant diagonals link K to Fourier transforms, filters and convolution matrices.
4. *Invertible:*
$$K_4^{-1}=\frac15\begin{bmatrix}4&3&2&1\\3&6&4&2\\2&4&6&3\\1&2&3&4\end{bmatrix}\tag{9}$$
The inverse is symmetric but dense. Its determinant is 5. The determinant must not be zero, but the author says computing det or K⁻¹ is almost never done in practice. One runs elimination instead; nonzero pivots show K is invertible. MATLAB's backslash `K\F` is the fastest solution.
5. *Positive definite* (to be explained in Chapter 6). Pivots table (p. 79): invertible = n nonzero pivots; positive definite symmetric = n positive pivots; positive semidefinite symmetric = n nonnegative pivots.

**Free-fixed T (p. 79).** Tₙ is symmetric and tridiagonal like Kₙ, but its (1,1) entry is 1 instead of 2. The first row (1, −1) represents a free boundary condition du/dx = 0. T is positive definite but not Toeplitz. Every pivot is 1, giving
$$T_4=\begin{bmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&2\end{bmatrix}=LU,\quad L=\begin{bmatrix}1&&&\\-1&1&&\\0&-1&1&\\0&0&-1&1\end{bmatrix},\ U=L^T\tag{11}$$
L is a backward difference matrix and U is minus a forward difference. T = LLᵀ is positive definite. The inverses are U⁻¹ = all-ones upper triangle, L⁻¹ = all-ones lower triangle, and T⁻¹ = U⁻¹L⁻¹ = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]] (12).

**Free-free B is singular (pp. 79–80).** "Singular" means not invertible. A practical test: a nonzero x with Bx = 0. If such x exists, B⁻¹ cannot exist, since it would give B⁻¹Bx = x but also B⁻¹0 = 0 (p. 80). B₃ = [[1,−1,0],[−1,2,−1],[0,−1,1]] has 1 (not 2) in the (1,1) and (3,3) corners. B₃(1,1,1)ᵀ = 0 (13), so every constant vector (c,c,c) is in the nullspace. This holds because all rows of B₃ add to zero.

*Springs (p. 80, Fig. 2.3).* K₃ is three masses with both ends fixed, T₃ is free at the top and fixed at the bottom, and B₃ is free at both ends. With a weight W in the middle, K₃ and T₃ adjust to balance it:
$$K_3\begin{bmatrix}W/2\\W\\W/2\end{bmatrix}=\begin{bmatrix}0\\W\\0\end{bmatrix},\qquad T_3\begin{bmatrix}2W\\2W\\W\end{bmatrix}=\begin{bmatrix}0\\W\\0\end{bmatrix}\tag{14}$$
The B₃ springs have no support and cannot adjust. "Masses and springs lead to matrices. Elastic bars lead to differential equations" (p. 80).

*Intuition note.* K and T are pinned down by at least one fixed end, so a load has one balanced answer. B has no support at either end, so its springs cannot adjust to a weight (p. 80), and every constant vector (c,c,c) is in its nullspace. Reading the constant vector as the whole chain shifting as one block is our own picture.

**Problem Set 2.5 (pp. 81–82).** Eighteen problems on Taylor series, the three first differences, third and fourth-order formulas, K⁻¹, and solving −u″ = cos 4πx with K₄ and K₈ (p. 82). Selected ones are listed under Exercises.

### Thoughts on Chapter 2 (p. 83)
The author says Chapter 2 solves Ax = b for a square invertible A, and that one seldom computes A⁻¹. For upper triangular U, back substitution solves Ux = c from the last equation to the first. Elimination subtracts aᵢ₁/a₁₁ times equation 1 from equation i, and the author states it takes n³/3 steps to reach Ux = c. A = LU, with L the lower triangular matrix of multipliers. If a pivot is zero or small, one exchanges equations to make the pivot as large as possible. The "matrix ideas" list includes inverse, singular, triangular, elimination, permutation, transpose, symmetric, A = LU, S = LDLᵀ, finite difference matrices, and K, T, B. Invertible n×n matrices have column space and row space Rⁿ, and independent columns and rows. Open questions: A not invertible, not square, or with very many rows/columns (p. 83).

## Toy example (ours)
Solve −u″ = 9 on [0,1] with u(0) = u(1) = 0, using N = 2 meshpoints, so h = 1/3 and h² = 1/9.
- Equation: K₂U = h²F = (1/9)(9, 9) = (1, 1), with K₂ = [[2,−1],[−1,2]].
- Equations: 2u₁ − u₂ = 1 and −u₁ + 2u₂ = 1. Doubling the first equation and adding the second gives 3u₁ = 3, so u₁ = 1, then u₂ = 2·1 − 1 = 1.
- Check with the inverse: det K₂ = 4 − 1 = 3 and K₂⁻¹ = (1/3)[[2,1],[1,2]]. Then K₂⁻¹(1,1) = (1/3)(3,3) = (1,1). Also K₂K₂⁻¹ = (1/3)[[4−1, 2−2],[−2+2, −1+4]] = I.
- Symmetric factorization: pivots 2 and 3/2, L = [[1,0],[−1/2,1]], D = diag(2, 3/2). LDLᵀ = [[2,−1],[−1,1/2+3/2]] = K₂.
- Exact solution u = 4.5x(1−x) gives u(1/3) = 4.5·(1/3)·(2/3) = 1. This matches the numbers above.

## Concepts
- [[permutation-matrix]] (new) — matrix with the rows of I in some order; n! of them; Pᵀ = P⁻¹ (p. 64)
- [[transpose]] (new) — (Aᵀ)ᵢⱼ = Aⱼᵢ; defined better by (Ax)ᵀy = xᵀ(Aᵀy) (pp. 67–68)
- [[symmetric-matrix]] (new) — Sᵀ = S; AᵀA and AAᵀ are always symmetric (pp. 69–70)
- [[pa-lu-factorization]] (new) — row exchanges P chosen so PA = LU meets no zero pivot (p. 65)
- [[partial-pivoting]] (new) — exchange rows to put the largest available number in the pivot, for stability (p. 66)
- [[ldlt-factorization]] (new) — S = LDLᵀ, with U = Lᵀ after dividing out the pivots (p. 70)
- [[dot (inner) product]] — xᵀy; for functions an integral ∫x(t)y(t)dt (pp. 68–69)
- [[rank-one matrix / outer product]] — xyᵀ, an n×n matrix, versus the inner product xᵀy, a number (p. 68)
- [[orthogonality]] — columns of a permutation matrix have zero dot products (p. 65)
- [[orthonormal basis / orthogonal matrix]] — Q with Qᵀ = Q⁻¹; permutations satisfy PᵀP = I (pp. 64, 73)
- [[inverse matrix]] — (AB)⁻¹ = B⁻¹A⁻¹; (A⁻¹)ᵀ = (Aᵀ)⁻¹ (pp. 67–68, 83)
- [[null space (kernel)]] — Bx = 0 for a nonzero x shows B is singular (p. 80)
- [[positive (semi)definite matrix]] — n positive (nonnegative) pivots; K, T positive definite, B semidefinite (p. 79)
- [[finite-difference]] (new) — forward, backward and centered differences approximating derivatives (pp. 75–76)
- [[second-difference-matrix]] (new) — K, T, B built from the −1, 2, −1 pattern with fixed or free ends (pp. 76–79)
- [[toeplitz-matrix]] (new) — constant diagonals; tied to filters, convolution and Fourier (p. 78)
- [[banded-sparse-matrix]] (new) — mostly zeros near a diagonal band; tridiagonal K is fast to solve (p. 78)
- [[taylor-series]] (new) — y(x+h) as a sum of hⁿ/n! times nth derivatives (p. 75)
- [[singular-matrix]] (new) — not invertible; test Bx = 0 with x ≠ 0 (p. 79)
- [[saddle-point-block-matrix]] (new) — S = [[I,A],[Aᵀ,0]]; invertible iff AᵀA is (p. 70)

## Canonical instances
- [[pa-lu-3x3-example]] — rescue of a zero second pivot by exchanging rows 2 and 3 (p. 65)
- [[difference-matrix-transpose-example]] — A = [[−1,1,0],[0,−1,1]] with (Ax)ᵀy = xᵀ(Aᵀy) (p. 69)
- [[d-dt-antisymmetric]] — transpose of d/dt is −d/dt by integration by parts (p. 69)
- [[K4-fixed-fixed]] — K₄ and its inverse (1/5)[[4,3,2,1],…], det 5 (pp. 77–78)
- [[T4-free-fixed-LLT]] — T₄ = LLᵀ with all pivots 1 (p. 79)
- [[B3-free-free-nullspace]] — B₃(1,1,1) = 0 (p. 80)
- [[spring-mass-chain]] — K₃, T₃, B₃ as three masses with different supports (p. 80)

## Bridges (candidates)
- [same-math] AᵀA with A a ±1 difference matrix (Example 3, p. 70; B₃ = AᵀA) ↔ graph theory: Laplacian L = BᵀB of an incidence matrix — same product of a ±1 edge-difference matrix with its transpose.
- [same-math] PᵀP = I for a permutation ↔ orthogonal matrices: permutations are among the matrices with Qᵀ = Q⁻¹ (Problem 30).
- [structural-analogy] transpose of d/dt is −d/dt ↔ functional analysis: adjoint operator defined by ⟨Ax,y⟩ = ⟨x,A*y⟩ — same defining inner-product identity, on functions.
- [structural-analogy] constant-diagonal K ↔ signal processing: convolution filters and Fourier transform (the author links these, p. 78).
- [structural-analogy] spring chain K, T, B ↔ circuits: voltage drops e and currents y with heat loss eᵀy (p. 68).
- [metaphor] fixed vs free boundary and singular B ↔ statistics: a quantity determined only up to an added constant.

## Questions this raises
- Does C(PAQ) equal C(A), the question p. 66 leaves open? What does column permutation change about rows and columns?
- Why must AᵀA have a positive diagonal, and when is AᵀA positive definite rather than only semidefinite?
- Why does constant-diagonal structure connect so tightly to Fourier transforms?
- Chapter 3 will treat non-invertible and non-square A: which of the ideas here (nullspace, transpose) will it organise?

## Exercises worth doing
- Ex. 2.4-4 (p. 71) — A² = 0 is possible but AᵀA = 0 is not (unless A = 0) — difficulty: easy
- Ex. 2.4-12 (p. 72) — why PᵀP = I from dot products; Px·y ≠ x·Py — difficulty: medium
- Ex. 2.4-19 (p. 72) — PA = LU practice on two 3×3 matrices — difficulty: easy
- Ex. 2.4-26 (p. 73) — A = LS, triangular times symmetric, from A = LDU — difficulty: medium
- Ex. 2.5-13 (p. 82) — four samples give fourth-order accuracy for du/dx — difficulty: hard
- Ex. 2.5-17 (p. 82) — solve −u″ = cos 4πx with K₄ and K₈, compare with exact u(x) — difficulty: medium

## Reading notes
- This is part 2 of Chapter 2. It starts at §2.4 (p. 64) and ends with "Thoughts on Chapter 2" (p. 83). Part 1 (earlier sections) is not covered.
- Page offset: printed = pdf − 10.
- The text layer is garbled on many matrices and equations. All matrices above were checked against the page images.
- The transpose-of-AB display is numbered (6) in print right after (3); equations (4) and (5) are skipped there. Equation numbers restart in §2.5.
- p. 77: the text says "A typical row is (−u₁ + 2u₂ − u₃)/h² = f(h)". By the matrix equation just above it, row 2 should read f(2h). This is probably a misprint in the source.
- Quotes: only one short quoted line (p. 80); everything else is paraphrase.
- The partial-pivoting example on p. 66 and the PA = LU example on p. 65 use the same A. The tracking column 1 2 3 is marked * and is not part of the matrix.
