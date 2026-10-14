---
id: strang-2023-introduction/ch06-eigenvalues-p2
work: strang-2023-introduction
unit: "6 Eigenvalues and Eigenvectors (part 2/3): 6.2 Diagonalizing a Matrix and 6.3 Symmetric Positive Definite Matrices"
pages: 232–261
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Diagonalizing a matrix; symmetric positive definite matrices

## L0 — One line
Eigenvectors turn a matrix into a diagonal one (A = XΛX⁻¹), which makes powers and recurrences easy, and real symmetric matrices always allow this with orthonormal eigenvectors (S = QΛQᵀ); positive definite symmetric matrices have five equivalent tests.

## L1 — The gist (≤ 120 words)
How can eigenvectors simplify a matrix, its powers and its recurrences, and what extra structure do symmetric matrices have? If A has n independent eigenvectors, then A = XΛX⁻¹ and Aᵏ = XΛᵏX⁻¹, so uₖ₊₁ = Auₖ is solved eigenvector by eigenvector. Fibonacci numbers are the main example. Repeated eigenvalues can leave too few eigenvectors. A real symmetric matrix always has real eigenvalues and orthonormal eigenvectors, S = QΛQᵀ. Positive definite symmetric matrices have five equivalent tests, best summarised by positive energy xᵀSx > 0. These matrices give ellipses and convex minimum problems.

**Prerequisites:** eigenvalues and eigenvectors (Ax = λx), det(A − λI) = 0, independence, matrix multiplication by columns, transpose, orthogonal matrices, elimination/LU, nullspace and column space.

## L2 — Key ideas (5–10 bullets)
- If A has n independent eigenvectors (columns of X), then X⁻¹AX = Λ, A = XΛX⁻¹ and Aᵏ = XΛᵏX⁻¹. The eigenvectors are unchanged and the eigenvalues are powered (p. 232–233).
- uₖ = Aᵏu₀ = c₁(λ₁)ᵏx₁ + ⋯ + cₙ(λₙ)ᵏxₙ with c = X⁻¹u₀. Fibonacci's F₁₀₀ comes from this in three steps (p. 237–238).
- Distinct eigenvalues give independent eigenvectors, so such a matrix is diagonalizable. Repeated eigenvalues may leave too few eigenvectors (geometric multiplicity GM, the number of independent eigenvectors, below algebraic multiplicity AM, the number of times λ is a root). Invertibility concerns eigenvalues; diagonalizability concerns eigenvectors (p. 234, 239–240).
- Similar matrices BCB⁻¹ share the eigenvalues of C. AB and BA share their nonzero eigenvalues (p. 235–236).
- Spectral theorem: every real symmetric S = QΛQᵀ with real eigenvalues and orthonormal q's. Symmetric matrices are never short of eigenvectors (p. 246, 256).
- A positive definite S (symmetric, with energy xᵀSx > 0 for all x ≠ 0) has five equivalent tests: eigenvalues, energy, S = AᵀA with independent columns, leading determinants, pivots. Energy xᵀSx > 0 is the best definition (p. 247–250).
- Elimination gives S = LDLᵀ and the Cholesky factorization S = AᵀA with A = √D Lᵀ (p. 250).
- Geometry and calculus: xᵀSx = 1 is an ellipse with axes along eigenvectors. Where the first derivatives are zero and the second-derivative matrix is positive definite, f has a minimum; convex functions are the best to optimize (p. 252–255).
- Semidefinite matrices (energy ≥ 0) sit on the edge. AᵀSA stays semidefinite, and is definite if S is positive definite and Ax ≠ 0 whenever x ≠ 0 (p. 253).

## L3 — Walkthrough

### 6.2 Diagonalizing a Matrix

**Diagonalization.** Suppose the n×n matrix A has n linearly independent eigenvectors x₁,…,xₙ. Put them in the columns of the invertible eigenvector matrix X (n×n). Then X⁻¹AX = Λ, the diagonal eigenvalue matrix with λ₁,…,λₙ on its diagonal (p. 232):
$$X^{-1}AX=\Lambda=\begin{bmatrix}\lambda_1&&\\&\ddots&\\&&\lambda_n\end{bmatrix}\tag{1}$$

*Why AX = XΛ.* The columns of AX are Axₖ = λₖxₖ. XΛ also multiplies each column of X by its eigenvalue. (ΛX would multiply rows of X, so the order matters.) So AX = XΛ, i.e.
$$AX=X\Lambda \iff X^{-1}AX=\Lambda \iff A=X\Lambda X^{-1}\tag{2}$$
X is invertible because its columns are independent. Without n independent eigenvectors, A cannot be diagonalized (p. 233).

*Powers.* Because X⁻¹X = I, $A^k=(X\Lambda X^{-1})\cdots(X\Lambda X^{-1})=X\Lambda^kX^{-1}$ (p. 233).

*Example 1.* A = [[2,4],[0,6]] is triangular, with λ = 2 and 6. X = [[1,1],[0,1]], X⁻¹ = [[1,−1],[0,1]] (p. 232). Then
$$A^k=\begin{bmatrix}2^k&6^k-2^k\\0&6^k\end{bmatrix}$$
For k = 2 this gives [[4,32],[0,36]]. k = 0 gives I and k = −1 gives A⁻¹. A² has the same eigenvectors and squared eigenvalues 4 and 36 (p. 232–233).

*Four remarks (p. 233–234).*
1. n different eigenvalues make the n eigenvectors independent, so a matrix with no repeated eigenvalue can be diagonalized.
2. Eigenvectors can be multiplied by any nonzero constant. Codes usually return unit vectors.
3. Eigenvalues in Λ come in the same order as eigenvectors in X. Putting (1,1) before (1,0) gives Λ_new = diag(6, 2).
4. Some matrices have too few eigenvectors and cannot be diagonalized. Examples: A = [[1,−1],[1,−1]] and B = [[0,1],[0,0]], both with eigenvalues 0, 0. For A, Ax = 0 gives only multiples of (1,1). The problem is the repetition of λ, not λ = 0 itself. Non-diagonalizable matrices are the best test cases for true/false statements.

*Invertible vs diagonalizable.* Invertibility concerns eigenvalues (need λ ≠ 0). Diagonalizability concerns eigenvectors (need n independent ones). Each eigenvalue has at least one eigenvector, since A − λI is singular (p. 234).

**Independent eigenvectors from different eigenvalues.** Eigenvectors for distinct eigenvalues are linearly independent. So an n×n matrix with n different eigenvalues must be diagonalizable (p. 234).
*Proof (n = 2).* Suppose c₁x₁ + c₂x₂ = 0.
- Multiply by A: c₁λ₁x₁ + c₂λ₂x₂ = 0.
- Multiply by λ₂: c₁λ₂x₁ + c₂λ₂x₂ = 0.
- Subtract: (λ₁ − λ₂)c₁x₁ = 0. Since λ₁ ≠ λ₂ and x₁ ≠ 0, c₁ = 0. Similarly c₂ = 0 (p. 234).

For n eigenvectors, multiply by A and by λₙ and subtract to remove xₙ. Repeat to remove xₙ₋₁, and so on. Eventually
$$(\lambda_1-\lambda_2)\cdots(\lambda_1-\lambda_n)c_1x_1=0\tag{3}$$
which forces c₁ = 0, and similarly every cᵢ = 0 (p. 235).

*Intuition note.* Writing A = XΛX⁻¹ says: change to eigenvector coordinates, scale each coordinate by its own λ, change back. Powers repeat only the scaling step, because the X's cancel in the middle.

**Example 2 (Markov powers).** A = [[.8,.3],[.2,.7]] has λ₁ = 1, λ₂ = .5. A = XΛX⁻¹ with X = [[.6,1],[.4,−1]], Λ = diag(1, .5), X⁻¹ = [[1,1],[.4,−.6]] (p. 235). A² = XΛ²X⁻¹ with the same X (4), and
$$A^k=\begin{bmatrix}.6&1\\.4&-1\end{bmatrix}\begin{bmatrix}1&0\\0&(.5)^k\end{bmatrix}\begin{bmatrix}1&1\\.4&-.6\end{bmatrix}$$
As k → ∞, (.5)ᵏ → 0 and A^∞ = [[.6,.6],[.4,.4]], with eigenvector x₁ in both columns. The text asks "When does Aᵏ → zero matrix?" and answers: all |λ| < 1 (p. 235). Problem 15 states this as "if and only if" (p. 243).

**Similar matrices: same eigenvalues.** Fix Λ and vary X: the matrices XΛX⁻¹ are called *similar*. More generally, A = BCB⁻¹ for any invertible B (C need not be diagonal) is similar to C. Similar matrices have the same n eigenvalues (p. 235).
*Proof.* If Cx = λx, then
$$(BCB^{-1})(Bx)=BCx=B\lambda x=\lambda(Bx)\tag{5}$$
so BCB⁻¹ has eigenvalue λ with new eigenvector Bx (p. 236).

- If C = I, the family has one member, I. The identity is the only diagonalizable matrix with all λ = 1 (p. 236).
- For λ = 1, 1 with one eigenvector (Jordan form C = [[1,1],[0,1]], developed in Appendix 5), the similar matrices are
$$A=BCB^{-1}=\begin{bmatrix}1-rs&r^2\\-s^2&1+rs\end{bmatrix}\tag{6}$$
with r, s not both zero, always with det = 1 and trace = 2 (p. 236). (Added step: det = (1−rs)(1+rs) + r²s² = 1.)
- For λ = 1 and 0 (not repeated), the whole family is diagonalizable with trace 1 and det 0. Examples: [[1,0],[0,0]], [[1,1],[0,0]], [[.5,.5],[.5,.5]], or any xyᵀ/(yᵀx) (p. 236).

*AB and BA.* If A is m×n and B is n×m, then AB and BA have the same nonzero eigenvalues (p. 236).
*Proof.* With E = [[AB,0],[B,0]], D = [[I,A],[0,I]] (D⁻¹ = [[I,−A],[0,I]]), and block sizes [[m×m, m×n],[n×m, n×n]]:
$$D^{-1}ED=\begin{bmatrix}I&-A\\0&I\end{bmatrix}\begin{bmatrix}AB&0\\B&0\end{bmatrix}\begin{bmatrix}I&A\\0&I\end{bmatrix}=\begin{bmatrix}0&0\\B&BA\end{bmatrix}=F$$
So F is similar to E, and both have m + n eigenvalues. E has the m eigenvalues of AB plus n zeros. F has the n eigenvalues of BA plus m zeros. Hence AB and BA have the same eigenvalues except for |n − m| zeros (p. 236).

**Fibonacci numbers.** The rule F_{k+2} = F_{k+1} + F_k gives 0, 1, 1, 2, 3, 5, 8, 13, … (p. 236). To get F₁₀₀, turn the two-step scalar rule into a one-step vector rule. Put uₖ = (F_{k+1}, F_k):
$$u_{k+1}=\begin{bmatrix}1&1\\1&0\end{bmatrix}u_k=Au_k\tag{7}$$
with u₀ = (1,0), u₁ = (1,1), u₂ = (2,1), u₃ = (3,2), …, u₁₀₀ = A¹⁰⁰u₀ = (F₁₀₁, F₁₀₀) (p. 237).
- det(A − λI) = λ² − λ − 1. The quadratic formula gives λ₁ = (1+√5)/2 ≈ 1.618 and λ₂ = (1−√5)/2 ≈ −.618 (p. 237).
- Eigenvectors: x₁ = (λ₁, 1), x₂ = (λ₂, 1).
- Step 2: the starting vector is a combination of them:
$$u_0=\frac{x_1-x_2}{\lambda_1-\lambda_2}\tag{8}$$
- Step 3: the x's stay separate under A¹⁰⁰:
$$u_{100}=\frac{(\lambda_1)^{100}x_1-(\lambda_2)^{100}x_2}{\lambda_1-\lambda_2}\tag{9}$$
- F₁₀₀ is the second component. The second components of x₁, x₂ are 1, λ₁ − λ₂ = √5, and λ₂¹⁰⁰ ≈ 0. So
$$F_{100}=\frac{\lambda_1^{100}-\lambda_2^{100}}{\lambda_1-\lambda_2}=\text{nearest integer to }\frac1{\sqrt5}\Big(\frac{1+\sqrt5}{2}\Big)^{100}\tag{10}$$
- Every Fₖ is a whole number. F₁₀₁/F₁₀₀ is very close to the limiting ratio (1+√5)/2, called the "golden mean" (p. 237).

**Matrix powers Aᵏ.** For uₖ₊₁ = Auₖ the solution is uₖ = Aᵏu₀ = XΛᵏX⁻¹u₀, found in three steps (p. 238):
1. Write u₀ = Xc = c₁x₁ + ⋯ + cₙxₙ, so c = X⁻¹u₀ (n×1).
2. Multiply each xᵢ by (λᵢ)ᵏ, giving ΛᵏX⁻¹u₀.
3. Add up the pieces:
$$u_k=A^ku_0=c_1(\lambda_1)^kx_1+\cdots+c_n(\lambda_n)^kx_n\tag{11}$$
In matrix form u₀ = Xc (12) and Aᵏu₀ = XΛᵏX⁻¹u₀ = XΛᵏc (13), with X n×n, Λᵏ n×n and c n×1. This factorization is like A = LU or A = QR, and is suited to powers (p. 238).

*Example 3.* A = [[1,2],[1,0]] has λ₁ = 2, x₁ = (2,1), λ₂ = −1, x₂ = (1,−1). It is Fibonacci with the rule F_{k+2} = F_{k+1} + 2Fₖ. Start with u₀ = (1,0) = (1/3)(2,1) + (1/3)(1,−1), so c₁ = c₂ = 1/3. Then
$$u_k=\tfrac13 2^k\begin{bmatrix}2\\1\end{bmatrix}+\tfrac13(-1)^k\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}F_{k+1}\\F_k\end{bmatrix}$$
So Fₖ = (2ᵏ − (−1)ᵏ)/3, starting 0, 1, 1, 3, and F₁₀₀ ≈ 2¹⁰⁰/3 (p. 238–239). The text says the idea "Follow the eigenvectors" links later to differential equations (λᵏ becomes e^{λt}, Section 6.5) and Fourier series (p. 239).

*Intuition note.* Each eigenvector evolves on its own: it is multiplied by λᵏ at step k. In the Fibonacci example λ₂¹⁰⁰ ≈ 0, so the λ₁ part decides F₁₀₀ (p. 237).

**Nondiagonalizable matrices (optional).** An eigenvalue has two multiplicities (p. 239):
- Geometric multiplicity GM = number of independent eigenvectors for λ = dim null(A − λI).
- Algebraic multiplicity AM = number of repetitions of λ among the n roots of det(A − λI) = 0.

Always GM ≤ AM. If λ = 4, 4, 4, then AM = 3 and GM = 1, 2 or 3. The standard trouble: A = [[0,1],[0,0]] has det(A − λI) = λ², so AM = 2, but only the eigenvector (1,0), so GM = 1 (p. 239–240). A shortage of eigenvectors (GM below AM) means A is not diagonalizable. The matrices [[5,1],[0,5]], [[6,−1],[1,4]], [[7,2],[−2,3]] all have det(A − λI) = (λ − 5)². Each A − 5I has rank 1, so AM = 2 and GM = 1 (p. 240). Review item 5: A is diagonalizable if every eigenvalue has enough eigenvectors (GM = AM) (p. 240).

**Worked example 6.2 A (Lucas numbers).** L₁ = 1, L₂ = 3, same rule L_{k+2} = L_{k+1} + Lₖ, so the same A. Take u₁ = (3,1). Then c₁ = λ₁ and c₂ = λ₂, because
$$\lambda_1x_1+\lambda_2x_2=\begin{bmatrix}\lambda_1^2+\lambda_2^2\\\lambda_1+\lambda_2\end{bmatrix}=\begin{bmatrix}\operatorname{trace}A^2\\\operatorname{trace}A\end{bmatrix}=\begin{bmatrix}3\\1\end{bmatrix}$$
So L₁₀₀ = c₁λ₁⁹⁹ + c₂λ₂⁹⁹ = λ₁¹⁰⁰ + λ₂¹⁰⁰. Lucas numbers end up larger than Fibonacci by a factor near √5 (p. 240–241).

**Worked example 6.2 B.** A = 5·eye(4) − ones(4) has 4 on the diagonal and −1 elsewhere (p. 241).
- ones(4) has rank 1, so three eigenvalues are 0, and its trace 4 gives the fourth, 4. Subtracting from 5I, A has eigenvalues 1, 5, 5, 5, so det A = 125.
- The eigenvector for λ = 1 is (1,1,1,1). The others are perpendicular to it since A is symmetric. X = H, the symmetric orthogonal Hadamard matrix (1/2)[[1,1,1,1],[1,−1,1,−1],[1,1,−1,−1],[1,−1,−1,1]], with Hᵀ = H⁻¹.
- A⁻¹ has eigenvalues 1, 1/5, 1/5, 1/5 and A⁻¹ = (1/5)(eye(4) + ones(4)), a rank-one change from I/5.
- The text says the determinant 125 counts spanning trees in a graph with 5 nodes. With 6 nodes, 6·eye(5) − ones(5) has eigenvalues 1, 6, 6, 6, 6 (p. 241).

**Problem Set 6.2 (p. 242–245).** Contents: factoring and powers (1–7), Fibonacci and "Gibonacci" averages (8–10), diagonalizability (11–14), powers and limits (15–19), det = ∏λ and trace = Σλ (20–21), subspaces of matrices with the same X (23), square roots (26), Cayley–Hamilton (29–30), Lax's examples (32), rotation powers (33), left eigenvectors and A = Σλᵢxᵢyᵢᵀ (34), similarity (36–37).

### 6.3 Symmetric Positive Definite Matrices

**Summary box (p. 246).** A symmetric S has n real eigenvalues and n orthonormal eigenvectors qᵢ, and S = QΛQ⁻¹ = QΛQᵀ. Positive definite S has all λ > 0, all pivots > 0 and all upper left determinants > 0. The energy test is xᵀSx > 0 for all x ≠ 0, and then S = AᵀA with independent columns in A. Positive semidefinite allows λ = 0, pivot = 0, det = 0, energy = 0.

**Symmetric matrices.** For S = Sᵀ: (1) all eigenvalues are real; (2) the eigenvectors can be chosen orthogonal. "Can be chosen" because S = I has every nonzero x as an eigenvector, so repeated eigenvalues give a choice. Rescaled to unit length, the q's are orthonormal, and QᵀQ = I, Qᵀ = Q⁻¹ (p. 246).
**Spectral theorem:** every real symmetric S has the form S = QΛQᵀ. Every matrix of that form is symmetric, since (QΛQᵀ)ᵀ = QΛQᵀ (p. 246).

*Quick proof of orthogonality.* Let Sx = λx with λ ≠ 0, and Sy = 0y. Then y is in the nullspace and x = Sx/λ is in the column space. For symmetric S, column space = row space, and row space ⟂ nullspace, so x ⟂ y (p. 246). For Sy = αy, apply the same argument to S − αI: (S − αI)y = 0 and (S − αI)x = (λ − α)x with λ − α ≠ 0. So eigenvectors for different eigenvalues are orthogonal (p. 247).
*Reality of λ (sketch only).* Multiply Sx = λx by the conjugate transpose x̄ᵀ to get x̄ᵀSx = λ x̄ᵀx. When x̄ᵀx and x̄ᵀSx are shown to be real, λ is real. The author postpones complex numbers to the end of the section (p. 247).

**Positive definite matrices.**
*Test 1:* a positive definite S has all positive eigenvalues (p. 247). Five examples: (1) diag(2,6) is positive definite. (2) Q diag(2,6) Qᵀ is, if Qᵀ = Q⁻¹ (same λ). (3) C diag(2,6) Cᵀ is, if C is invertible (energy test). (4) [[a,b],[b,c]] is when a > 0 and ac > b² (det test). (5) diag(2,0) is only semidefinite. Test 1 applied to [[1,2],[2,1]] (λ = 3, −1), S = vvᵀ (λ = ‖v‖², 0) and [[2,1,0],[1,2,1],[0,1,2]] (λ = 2, 2 − √2, 2 + √2) gives No, No, Yes (p. 247).

*Test 2 (energy).* S is positive definite if xᵀSx > 0 for all x ≠ 0 (1) (p. 248). Example: S = [[2,4],[4,9]] has
$$x^TSx=2x_1^2+8x_1x_2+9x_2^2=2(x_1+2x_2)^2+x_2^2>0$$
- If Sx = λx then xᵀSx = λxᵀx, so λ > 0 gives positive energy.
- Conversely, suppose xᵀSx > 0 for each eigenvector. Write x = c₁x₁ + ⋯ + cₙxₙ with orthogonal eigenvectors. Then
$$x^TSx=(c_1x_1^T+\cdots+c_nx_n^T)(c_1\lambda_1x_1+\cdots+c_n\lambda_nx_n)=c_1^2\lambda_1x_1^Tx_1+\cdots+c_n^2\lambda_nx_n^Tx_n>0$$
if every λᵢ > 0. Orthogonality (xᵢᵀxⱼ = 0) is used from line 2 to line 3 (p. 248).
- If S₁, S₂ are symmetric positive definite, so is S₁ + S₂, because xᵀ(S₁+S₂)x = xᵀS₁x + xᵀS₂x > 0 + 0 (p. 248).

*Intuition note.* Energy xᵀSx is a number you can check for any x, with no eigenvalues needed. Positive eigenvalues and positive energy say the same thing, because x splits into orthogonal eigenvector pieces whose energies add with weights c².

*Tests 3, 4, 5 (p. 249).* Test 3: S = AᵀA for some A with independent columns. Test 4: all leading determinants D₁,…,Dₙ are positive. Test 5: all pivots from elimination are positive.
- *Test 3.* S = AᵀA is symmetric, and its energy is xᵀAᵀAx = ‖Ax‖². This is positive provided Ax ≠ 0; to assure Ax ≠ 0 when x ≠ 0, the columns of A must be independent (2).
- Dependent columns: A = [[1,1,1],[1,2,3]] (columns (1,1), (1,2), (1,3); col 1 + col 3 = 2·col 2). Then S = AᵀA = [[2,3,4],[3,5,7],[4,7,10]] has rank 2, and x = (1,−2,1) has zero energy and is an eigenvector with λ = 0. S is only semidefinite. AᵀA is always at least semidefinite, and semidefinite allows energy, eigenvalues, determinants and pivots to be zero.
- *Test 4 example.* The 4×4 second-difference matrix (2 on the diagonal, −1 beside it) has D₁ = 2, D₂ = 3, D₃ = 4, D₄ = 5, all positive.
- *Tests 4 and 5 are linked.* The pivots are 2, 3/2, 4/3, 5/4, ratios of determinants. The kth pivot equals D_k / D_{k−1}. So Test 5 is passed exactly when Test 4 is passed (p. 249).

*LDLᵀ and Cholesky (p. 250).* For S = [[2,−1,0],[−1,2,−1],[0,−1,2]]:
- S = LU (3) with U rows (2,−1,0), (0,3/2,−1), (0,0,4/3).
- Put the pivots in D: S = LDLᵀ (4), with L = [[1,0,0],[−1/2,1,0],[0,−2/3,1]] and D = diag(2, 3/2, 4/3).
- Sharing pivots between Aᵀ and A gives S = AᵀA (5) with A = √D Lᵀ upper triangular. Its rows are (√2, −√(1/2), 0), (0, √(3/2), −√(2/3)), (0, 0, √(4/3)).
- This is the Cholesky factorization: elimination factors every positive definite S into AᵀA, with √pivots on the diagonal of A.
- Other choices of A: the symmetric one A = Q√ΛQᵀ = Aᵀ, and the triangular one A = √D Lᵀ, since S = (L√D)(√D Lᵀ).

*Summary (p. 250).* The five tests (pivots, determinants, eigenvalues, S = AᵀA, energy) each give a complete answer by themselves: positive definite, semidefinite, or neither. For [[a,b],[b,c]]: determinants a > 0, ac − b² > 0; pivots a > 0, (ac − b²)/a > 0; eigenvalues λ₁, λ₂ > 0; energy ax² + 2bxy + cy² > 0. Positive energy "is the best definition. It connects them all."

**Two examples (p. 251).**

| | S = [[9,3],[3,3]] (definite) | T = [[9,3],[3,1]] (semidefinite) |
|---|---|---|
| determinants | 9, 18 | 9, 0 |
| pivots | 9, 2 | 9, 0 |
| energy | 9x²+6xy+3y² = (3x+y)² + 2y² | 9x²+6xy+y² = (3x+y)² |
| trace, det | 12, 18 | 10, 0 |
| eigenvalues | 6 ± 3√2 | 10, 0 |
| factor | LDLᵀ = AᵀA, A = [[3,1],[0,√2]] | A = [[3,1],[0,0]] |
| graph | bowl; strictly convex; E = 1 is an ellipse | valley; convex; E = 1 is the band 3x + y = ±1 |
| minimum | at a point | along a line |

**Minimum problems (p. 252).** E = xᵀSx = 5x² + 8xy + 5y² for S = [[5,4],[4,5]] is a bowl opening upward with minimum 0 at (0,0). For a function f, the text's test for a minimum at (x₀,y₀) is ∂f/∂x = ∂f/∂y = 0 and the matrix of second derivatives [[∂²f/∂x², ∂²f/∂x∂y],[∂²f/∂x∂y, ∂²f/∂y²]] positive definite there. The text describes the best minimization problems as those where f is strictly convex, with the second-derivative matrix positive definite at all points. Example: f = e^{x²+y²}, with ∂f/∂x = 2x e^{x²+y²}, has second-derivative matrix [[2+4x², 4xy],[4xy, 2+4y²]]e^{x²+y²}. The text says this is positive definite for every x and y, so f is strictly convex (p. 252).

**Positive semidefinite matrices (p. 253).** All λ ≥ 0 and all xᵀSx ≥ 0.
- S = [[1,2],[2,4]]: eigenvalues 5, 0, trace 5, upper-left determinants 1 and 0, rank 1. S = AᵀA with A = [[1,2],[0,0]] (dependent columns). If the entry 4 is increased by any small number, S becomes positive definite.
- The cyclic T = [[2,−1,−1],[−1,2,−1],[−1,−1,2]] has det 0. x = (1,1,1) has Tx = 0 and zero energy, and other directions give positive energy. T is a first-difference matrix times its transpose, and its columns add to (0,0,0).
- If S is positive semidefinite, so is AᵀSA, since (Ax)ᵀS(Ax) ≥ 0.
- If xᵀSx > 0 and Ax ≠ 0 whenever x ≠ 0, then AᵀSA is positive definite (energy test). It is called "congruent" to S. The text says this is important in engineering equations AᵀSAx = f.
- **Law of Inertia:** if S = Sᵀ has P positive, N negative and Z zero eigenvalues, so does AᵀSA, provided A is invertible (p. 253).

**The ellipse ax² + 2bxy + cy² = 1 (p. 254–255).** The tilted ellipse xᵀSx = 1 becomes XᵀΛX = 1 with X = Qx as the text writes it (see Reading notes: the computation below uses Qᵀx). *Example 1:* 5x² + 8xy + 5y² = 1, S = [[5,4],[4,5]], with eigenvectors (1,1), (1,−1) (divide by √2) and eigenvalues 9, 1. Then S = QΛQᵀ with Q = (1/√2)[[1,1],[1,−1]] and
$$x^TSx=9\Big(\frac{x+y}{\sqrt2}\Big)^2+1\Big(\frac{x-y}{\sqrt2}\Big)^2\tag{6}$$
With X = (x+y)/√2, Y = (x−y)/√2 this is 9X² + Y² = 1. The axes point along the eigenvectors (the "principal axis theorem"). The bigger eigenvalue λ₁ = 9 gives the shorter axis, half-length 1/√λ₁ = 1/3. λ₂ = 1 gives half-length 1/√λ₂ = 1 (p. 254).

**Optimization and machine learning (p. 255).** At a minimum x*, all ∂f/∂xᵢ = 0 (calculus) and the matrix S of second derivatives ∂²f/∂xᵢ∂xⱼ is positive definite (linear algebra). If S is positive definite (or semidefinite) at all points, f is convex. If the eigenvalues of S stay above some positive number δ, f is strictly convex. Such functions have one minimum, and gradient descent (to be covered in Chapter 9) will find it. Machine-learning loss functions have hundreds of thousands of variables, so computing all second derivatives is barely possible; first derivatives give a direction to move, the steepest descent direction.

**All symmetric matrices are diagonalizable (p. 256).** Repeated eigenvalues can leave a shortage of eigenvectors for nonsymmetric matrices, but "never" for symmetric ones. The proof uses Schur's theorem: A = QTQ⁻¹ = QTQᵀ with T triangular (proved on the book's website, not in these pages). If A is symmetric, T = QᵀAQ is symmetric, and a symmetric triangular matrix is diagonal. For diagonalizable A, factor X = QR by Gram–Schmidt: A = XΛX⁻¹ = QRΛR⁻¹Q⁻¹ = QTQ⁻¹ with T = RΛR⁻¹ (p. 256).

**Worked example 6.3 A (p. 256).** S = [[2,−1,0],[−1,2,−1],[0,−1,2]]: pivots 2, 3/2, 4/3, determinants 2, 3, 4, eigenvalues 2 − √2, 2, 2 + √2. "Any one test is decisive". Three ways S = AᵢᵀAᵢ, from xᵀSx = 2x₁² − 2x₁x₂ + 2x₂² − 2x₂x₃ + 2x₃²:
- ‖A₁x‖² = x₁² + (x₂ − x₁)² + (x₃ − x₂)² + x₃²
- ‖A₂x‖² = 2(x₁ − ½x₂)² + (3/2)(x₂ − ⅔x₃)² + (4/3)x₃² (S = LDLᵀ)
- ‖A₃x‖² = λ₁(q₁ᵀx)² + λ₂(q₂ᵀx)² + λ₃(q₃ᵀx)² (S = QΛQᵀ)

For T = [[2,−1,c],[−1,2,−1],[c,−1,2]]: det T = 4 + 2c − 2c² = (1 + c)(4 − 2c). It is zero at c = −1 and c = 2, and T is positive definite between c = −1 and c = 2 (p. 256).

**Problem Set 6.3 (p. 257–261).** Contents: similar symmetric matrices (1), spectral decompositions (2–8), antisymmetric and complex matrices (9–13), true/false (14), tests for positive definiteness (24–49), including Cholesky (41–42), the ellipse (40) and saddle points (44–45).

## Toy example (ours, not from the text)
A = [[4,1],[2,3]]. Trace 7, det 10, so λ² − 7λ + 10 = 0 and λ = 5, 2.
- λ = 5: A − 5I = [[−1,1],[2,−2]], so x₁ = (1,1). λ = 2: A − 2I = [[2,1],[2,1]], so x₂ = (1,−2).
- X = [[1,1],[1,−2]], det X = −3, X⁻¹ = (1/3)[[2,1],[1,−1]]. Check: XΛ = [[5,2],[5,−4]]; times [[2,1],[1,−1]] gives [[12,3],[6,9]]; divide by 3: [[4,1],[2,3]] = A ✓.
- Solve uₖ₊₁ = Auₖ from u₀ = (3,0). c = X⁻¹u₀ = (1/3)(2·3 + 0, 3 − 0) = (2,1). Check: 2(1,1) + 1(1,−2) = (3,0) ✓.
- So uₖ = 2·5ᵏ(1,1) + 2ᵏ(1,−2). For k = 2: 50(1,1) + 4(1,−2) = (54, 42).
- Direct check: u₁ = A(3,0) = (12,6), u₂ = A(12,6) = (48+6, 24+18) = (54,42) ✓.

## Concepts
- [[diagonalization]] — A = XΛX⁻¹ when A has n independent eigenvectors; Aᵏ = XΛᵏX⁻¹ (p. 232–233)
- [[eigenvector-eigenvalue]] — Ax = λx; distinct eigenvalues give independent eigenvectors (p. 234)
- [[characteristic-polynomial]] — det(A − λI) = 0 gives eigenvalues; for Fibonacci λ² − λ − 1 (p. 237)
- [[similar-matrices]] (new) — A = BCB⁻¹ for invertible B; share eigenvalues with C (p. 235–236)
- [[algebraic-geometric-multiplicity]] (new) — AM = repetitions of λ as a root; GM = number of independent eigenvectors; GM ≤ AM (p. 239)
- [[spectral-theorem]] — real symmetric S = QΛQᵀ, real λ, orthonormal q (p. 246)
- [[positive-semidefinite-matrix]] — S = Sᵀ with xᵀSx > 0 (definite) or ≥ 0 (semidefinite); five tests (p. 247–250)
- [[energy-test]] (new) — S positive definite iff xᵀSx > 0 for all x ≠ 0, the author's preferred definition (p. 248, 250)
- [[cholesky-factorization]] (new) — S = AᵀA with A = √D Lᵀ upper triangular from elimination (p. 250)
- [[quadratic-form]] — xᵀSx; level set xᵀSx = 1 is an ellipse with axes along eigenvectors (p. 254)
- [[law-of-inertia]] (new) — AᵀSA has the same counts of positive, negative, zero eigenvalues as S if A is invertible (p. 253)
- [[orthonormal-basis-orthogonal-matrix]] — Q with QᵀQ = I (p. 246)
- [[gram-schmidt-and-qr]] — used to turn X into QR in Schur's argument (p. 256)

## Canonical instances
- [[fibonacci-numbers]] — F₁₀₀ from eigenvalues (1±√5)/2; nearest-integer formula (p. 236–237)
- [[lucas-numbers]] — same matrix, different start; L₁₀₀ = λ₁¹⁰⁰ + λ₂¹⁰⁰ (p. 240–241)
- [[markov-matrix-powers]] — A = [[.8,.3],[.2,.7]], Aᵏ → steady state with λ = 1, .5 (p. 235)
- [[nondiagonalizable-examples]] — [[0,1],[0,0]], [[5,1],[0,5]] with AM = 2, GM = 1 (p. 239–240)
- [[second-difference-matrix]] — 2, −1, −1 pattern: determinants 2, 3, 4, 5, pivots 2, 3/2, 4/3, 5/4 (p. 249–250)
- [[tilted-ellipse-5-8-5]] — 5x² + 8xy + 5y² = 1 becomes 9X² + Y² = 1 (p. 254)
- [[all-ones-rank-one-shift]] — 5I − ones(4): eigenvalues 1, 5, 5, 5, det 125 (p. 241)

## Bridges (candidates)
- [same-math] Spectral theorem S = QΛQᵀ ↔ PCA: eigen-decomposition of a covariance matrix gives orthogonal principal directions.
- [same-math] Aᵏ = XΛᵏX⁻¹ with λ = 1, .5 ↔ Markov chains: powers converge to a steady-state eigenvector.
- [same-math] Positive definite second-derivative matrix ↔ optimization: Hessian positive definite means a local minimum and convexity.
- [structural-analogy] Cholesky S = AᵀA ↔ statistics: factoring a covariance matrix into a triangular factor (not in this unit).
- [structural-analogy] det of 5I − ones counts spanning trees ↔ graph theory: matrix-tree style counting (the unit only says so, p. 241).

## Questions this raises
- What happens to Aᵏ when A is not diagonalizable (Jordan form, Appendix 5)?
- If all |λ| < 1 gives Aᵏ → 0, is it also necessary for non-diagonalizable A?
- How do energy and eigenvalue tests extend to complex Hermitian matrices (the postponed complex-number note)?
- Why does gradient descent behave well on strictly convex f, and how does the size of the smallest eigenvalue of S matter?

## Exercises worth doing
- Ex. 6.2 #16 (p. 243), recommended — diagonalize a Markov-type matrix, find the limit of XΛᵏX⁻¹ and read the steady state from its columns — difficulty: easy
- Ex. 6.2 #21 (p. 244) — trace XY = trace YX, so trace A = sum of eigenvalues, and AB − BA = I is impossible — difficulty: medium
- Ex. 6.2 #25 (p. 244), recommended — nullspace and column space dimensions add to n, so why is there no full eigenvector set? — difficulty: medium
- Ex. 6.3 #40 (p. 261) — draw an ellipse and read axis lengths from eigenvalues — difficulty: easy
- Ex. 6.3 #47 (p. 261) — energy test proves AᵀCA is positive definite when C is positive definite and A has independent columns — difficulty: medium
- Ex. 6.3 #48 (p. 261) — λ₁I − S is semidefinite, so the maximum of xᵀSx/xᵀx is λ₁ — difficulty: medium

## Reading notes
- This part starts at the beginning of Section 6.2 (printed p. 232) and ends with Problem Set 6.3 (printed p. 261). Printed = pdf − 10.
- The text layer is garbled in equations and tables. I checked all equations against the page images.
- Schur's theorem is stated for "every real square matrix" with no further condition, and its proof is only referenced to a website (p. 256).
- The sentence "The family contains all 2×2 matrices with A² = A" (p. 236) is loose: 0 and I also satisfy A² = A but have eigenvalues 0, 0 and 1, 1, so they are not in the family. The family described is the one with eigenvalues 1 and 0.
- The text says the determinant 125 counts spanning trees "in a graph with 5 nodes" while the matrix shown is 4×4 (p. 241). The connection is not explained in these pages.
- On p. 254 the text writes X = Qx; with S = QΛQᵀ the lined-up coordinates are Qᵀx, and the worked example uses X = (x+y)/√2, which matches Qᵀx.
- On p. 252 the text links strict convexity to a positive definite second-derivative matrix at all points. On p. 255 it says positive definite (or semidefinite) gives convex, and eigenvalues above some δ > 0 give strictly convex.
- Problem solutions are not printed in these pages.
