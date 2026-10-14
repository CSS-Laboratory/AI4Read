---
id: strang-2023-introduction/ch04-orthogonality-p1
work: strang-2023-introduction
unit: "4 Orthogonality (part 1/2): chapter opening, 4.1 Orthogonality of Vectors and Subspaces, 4.2 Projections onto Lines and Subspaces, 4.3 Least Squares Approximations"
pages: 143-175
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Orthogonality, projections and least squares (Strang, Ch. 4, Sections 4.1–4.3)

## L0 — One line
When Ax = b has no solution, the best substitute is the projection p = Ax̂ of b onto the column space, and x̂ solves the normal equation AᵀAx̂ = Aᵀb because the error b − Ax̂ is orthogonal to that column space.

## L1 — The gist (≤ 120 words)
Section 4.1 asks how the four fundamental subspaces sit relative to each other. Answer: they are orthogonal complements in pairs (row space ⊥ nullspace, column space ⊥ left nullspace). Section 4.2 asks for the closest point p in a subspace to a vector b. Answer: when A has independent columns, p = A(AᵀA)⁻¹Aᵀb, with projection matrix P = A(AᵀA)⁻¹Aᵀ satisfying P² = P = Pᵀ. Section 4.3 uses this for unsolvable systems with too many equations. The least squares solution x̂ solves AᵀAx̂ = Aᵀb, which geometry, algebra and calculus all give. Fitting a line or parabola to data is the main application.

**Prerequisites:** dot product and transpose; column space, nullspace, rank, independence (Ch. 3); matrix shapes; partial derivatives. Terms used above: orthogonal complement of V = all vectors orthogonal to V; left nullspace = N(Aᵀ); projection matrix P = the matrix with p = Pb; normal equation = AᵀAx̂ = Aᵀb; pseudoinverse = only previewed here (Section 4.5).

## L2 — Key ideas
- Vectors are orthogonal when vᵀw = 0. Then ‖v‖² + ‖w‖² = ‖v+w‖² (Pythagoras). (p. 144)
- Row space ⊥ nullspace and column space ⊥ N(Aᵀ). They are orthogonal complements: dimensions r + (n−r) = n and r + (m−r) = m. Every x splits uniquely as x_r + x_n. (pp. 145–147)
- Every b in the column space comes from exactly one x_r in the row space. A is invertible from row space to column space. (p. 146)
- Projection onto the line through a: p = a(aᵀb/aᵀa), P = aaᵀ/aᵀa (rank one). The error e = b − p is perpendicular to a. (pp. 153–154)
- Projection onto C(A) with independent columns: x̂ = (AᵀA)⁻¹Aᵀb, p = Ax̂, P = A(AᵀA)⁻¹Aᵀ, with P² = P = Pᵀ. (p. 155)
- AᵀA is invertible if and only if A has independent columns, because AᵀA and A have the same nullspace. (p. 157)
- Least squares minimizes ‖Ax − b‖². Geometry (e ⊥ columns), algebra (e in N(Aᵀ)) and calculus (partial derivatives = 0) all give AᵀAx̂ = Aᵀb. (pp. 164–166)
- Fitting a line C + Dt to m points gives a 2×2 system with entries m, Σtᵢ, Σtᵢ², Σbᵢ, Σtᵢbᵢ. Centred times make AᵀA diagonal. (pp. 167–168)
- With dependent columns, x̂ is not unique. The pseudoinverse (Section 4.5) picks the shortest solution. (p. 169)

## L3 — Walkthrough

### Chapter opening (p. 143)
- Orthogonal vectors have v·w = vᵀw = 0. Then ‖v‖² + ‖w‖² = ‖v+w‖², since (v+w)ᵀ(v+w) = vᵀv + wᵀw when vᵀw = wᵀv = 0. (p. 143)
- Strang previews: N(A) contains all vectors orthogonal to the row space, and N(Aᵀ) contains all vectors orthogonal to the column space. (p. 143)
- Projection: if b is outside C(A), find the closest p inside. The error e is perpendicular to C(A). The least squares equation AᵀAx̂ = Aᵀb gives the best x̂. (p. 143)
- AᵀAx̂ = Aᵀb is easy when AᵀA = I, i.e. orthonormal columns. Section 4.4 (not in this unit) makes columns orthonormal, giving QᵀQ = I and A = QR. (p. 143)

### 4.1 Orthogonality of Vectors and Subspaces

**Orthogonal vectors.** vᵀw = 0 and ‖v‖² + ‖w‖² = ‖v+w‖². Expanding: (v+w)ᵀ(v+w) = vᵀv + wᵀw + vᵀw + wᵀv = vᵀv + wᵀw + 0 + 0. Orthogonal means perpendicular, also in Rⁿ. (p. 144)

**Orthogonal subspaces.** V and W are orthogonal when vᵀw = 0 for every v in V and every w in W. (p. 144)

**Nullspace ⊥ row space.** Write Ax = 0 row by row: (row i of A)·x = 0 for i = 1,…,m \tag{1}. Every row has zero dot product with x, so every combination of rows does too. Hence the whole row space C(Aᵀ) is orthogonal to the whole nullspace. (p. 144)

Short proof, with row-space vectors written as Aᵀy:
$$x^{\mathsf T}(A^{\mathsf T}y) = (Ax)^{\mathsf T}y = 0^{\mathsf T}y = 0. \tag{2}$$
Strang prefers the first proof, where you see each row multiply x to give zero. (p. 144)

**Column space ⊥ N(Aᵀ).** Apply the same proof to Aᵀ. The row space of Aᵀ is C(A), so C(A) is perpendicular to N(Aᵀ) inside Rᵐ. (p. 145)

**Example 1.** A = [[1, −2, 1],[1, 0, −1]], x = (1,1,1). Row dot products: 1−2+1 = 0 and 1+0−1 = 0, so x is in N(A). The three columns of A are the rows of Aᵀ, and Aᵀy = 0 holds for y = 0, the only vector in N(Aᵀ). Here C(A) = R² and N(Aᵀ) = {0}. The row space plus nullspace has dimensions 2 + 1 = 3 and fills R³. The column space plus N(Aᵀ) has dimensions 2 + 0 = 2 and fills R². (p. 145)

**Dimension restriction.** If V and W are orthogonal subspaces in Rⁿ, then dim V + dim W ≤ n. Example: a wall and the floor are 2-dimensional subspaces of R³. They cannot be orthogonal, because 2 + 2 > 3 and they share the line where wall meets floor. (p. 145)

**Orthogonal complements.** The orthogonal complement V^⊥ of V contains all vectors orthogonal to V. The two pairs of fundamental subspaces are orthogonal complements: row space and nullspace (r + (n−r) = n), column space and left nullspace (r + (m−r) = m). Any x in Rⁿ is x = x_row + x_null. Any y in Rᵐ is y = y_col + y_null (component in N(Aᵀ)). (p. 145)

**Fundamental Theorem of Linear Algebra, Part 2.** N(A) is the orthogonal complement of C(Aᵀ) in Rⁿ. N(Aᵀ) is the orthogonal complement of C(A) in Rᵐ. Part 1 gave dimensions. Part 2 gives the 90° angles. (p. 146)

*Intuition note.* Every input vector splits into a part A keeps (row space) and a part A kills (nullspace), and these two parts are at right angles. Together they use up exactly n dimensions, so nothing is left over and nothing overlaps.

**Consequences (Figure 4.1).**
- Ax_n = 0 and Ax_r = Ax. The complete solution of Ax = b is one x_r plus any x_n. Also ‖x‖² = ‖x_r‖² + ‖x_n‖². The minimum-norm solution is x = x_r, i.e. x_n = 0. (p. 146)
- Every b in the column space comes from exactly one x_r in the row space. Proof: if Ax_r = Ax_r′, then x_r − x_r′ is in the nullspace and in the row space. Those spaces are perpendicular, so the difference is 0. (p. 146)
- So an r×r invertible matrix hides inside A: A is invertible from row space to column space. Section 4.5's pseudoinverse A⁺ will invert that part. (p. 146)
- **Example 2.** A = [[1,2,3,4,5],[1,2,4,5,6],[1,2,4,5,6]] has rank 2 and contains the invertible submatrix [[1,3],[1,4]] in its pivot rows and pivot columns. Proof for any A: the submatrix C of r independent columns has rank r. So Cᵀ has r independent columns, i.e. C has r independent rows. This locates an r×r invertible submatrix. (p. 146)
- The only vector in two orthogonal subspaces is the zero vector. (p. 147)

**Combining bases.** When the count is right, one basis property implies the other. Any n independent vectors in Rⁿ span Rⁿ. Any n vectors that span Rⁿ are independent. For an n×n matrix A:
- independent columns span Rⁿ, so Ax = b is solvable;
- spanning columns are independent, so Ax = b has only one solution;
- AB = I for square matrices implies BA = I.

Uniqueness implies existence and existence implies uniqueness, so A is invertible. (p. 147)

Putting a basis of the row space (r vectors) with a basis of the nullspace (n−r vectors) gives n vectors. They are independent (footnote: if a combination gives x_r + x_n = 0, then x_r = −x_n lies in both subspaces, so both are 0, so all coefficients are 0). Hence they span Rⁿ, and each x is x_r + x_n. (p. 147)

**Example 3.** A = [[1,2],[3,6]], x = (4,3). The split is x_r + x_n = (2,4) + (2,−1). (2,4) is in the row space and (2,−1) is orthogonal to it, in the nullspace. (p. 147)

**Example 4.** S is a six-dimensional subspace of R⁹. Strang's answers: (a) subspaces orthogonal to S have dimension 0, 1, 2 or 3. (b) S^⊥ has dimension 3. (c) The smallest matrix A with row space S is 6 by 9. (d) The smallest matrix B with nullspace S^⊥ is 6 by 9. (p. 147)

### 4.2 Projections onto Lines and Subspaces

**Summary list (p. 151).** The projection of b onto the line through a is the closest point to b: p = a(aᵀb/aᵀa). The error e = b − p is perpendicular to a, so ‖p‖² + ‖e‖² = ‖b‖². The projection onto a subspace S is the closest vector p in S, and b − p is orthogonal to S. AᵀA is invertible when A has independent columns. Then p = A(AᵀA)⁻¹Aᵀb and P = A(AᵀA)⁻¹Aᵀ, with p = Pb and P² = P = Pᵀ. (p. 151)

**Easy case (Figures 4.2).** Project b = (x, y, z) onto the z axis and the xy plane:
$$P_1=\begin{bmatrix}0&0&0\\0&0&0\\0&0&1\end{bmatrix},\quad P_2=\begin{bmatrix}1&0&0\\0&1&0\\0&0&0\end{bmatrix},\quad p_1=(0,0,z),\ p_2=(x,y,0).$$
For b = (2,3,4): p₁ = (0,0,4), p₂ = (2,3,0). The line and the plane are orthogonal complements, so p₁ + p₂ = b and P₁ + P₂ = I, P₁P₂ = 0 \tag{1}. P₁ has rank one and P₂ rank two. Every subspace of Rᵐ has its own m×m projection matrix. A subspace has many bases: the xy plane is the column space of [[1,0],[0,1],[0,0]] and of [[1,2],[2,3],[0,0]], so these give the same P. (pp. 151–152)

**Projection onto a line (A is m×1, equal to a).** Write p = x̂a. The error b − x̂a must be perpendicular to a:
$$a\cdot(b-\hat x a)=0\ \Rightarrow\ a\cdot b-\hat x\,a\cdot a=0\ \Rightarrow\ \hat x=\frac{a\cdot b}{a\cdot a}=\frac{a^{\mathsf T}b}{a^{\mathsf T}a}. \tag{2}$$
The order of steps is: find x̂, then p, then P. Special cases: if b = a then x̂ = 1 and Pa = a. If b ⊥ a then p = 0. (pp. 153)

Length check, with aᵀb = ‖a‖‖b‖cosθ:
$$\|p\|=\frac{\|a\|\,\|b\|\cos\theta}{\|a\|^2}\,\|a\|=\|b\|\cos\theta. \tag{3}$$
(p. 154)

*Intuition note.* x̂ says how many copies of a you need. The leftover b − x̂a is as short as it can be only when it makes a right angle with a.

**Projection matrix for a line.** p = a(aᵀb/aᵀa) = Pb with P = aaᵀ/aᵀa. P is a column times a row divided by a number, so it is m×m of rank one, and the line is its column space. Doubling a leaves P unchanged. P² = P. (p. 154)

**Example 1.** b = (1,1,1), a = (1,2,2). aᵀb = 5, aᵀa = 9, so x̂ = 5/9 and p = (5/9, 10/9, 10/9). Then e = b − p = (4/9, −1/9, −1/9), and eᵀa = 4/9 − 2/9 − 2/9 = 0. (p. 153)

**Example 2.** P = (1/9)[[1,2,2],[2,4,4],[2,4,4]]. Check: Pb for b = (1,1,1) is (1/9)(5,10,10), the same p. The diagonal entries add to (1+4+4)/9 = 1. P² = P. I − P projects onto the perpendicular subspace, here the plane orthogonal to a. (p. 154)

**Projection onto a subspace (A is m×n with independent columns a₁,…,aₙ).** Find the combination p = x̂₁a₁ + ⋯ + x̂ₙaₙ = Ax̂ closest to b. The error b − Ax̂ is perpendicular to every aᵢ, giving n equations:
$$a_i^{\mathsf T}(b-A\hat x)=0\ (i=1..n)\iff A^{\mathsf T}(b-A\hat x)=0\iff A^{\mathsf T}A\hat x=A^{\mathsf T}b. \tag{4,5}$$
Shapes: x̂ is n×1, AᵀA is n×n (symmetric), p is m×1, P is m×m. If the columns are independent, AᵀA is invertible and
$$\hat x=(A^{\mathsf T}A)^{-1}A^{\mathsf T}b \tag{5}$$
$$p=A\hat x=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}b \tag{6}$$
$$P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}. \tag{7}$$
For n = 1 these reduce to x̂ = aᵀb/aᵀa, p = a·aᵀb/aᵀa, P = aaᵀ/aᵀa \tag{8}: the number aᵀa becomes the matrix AᵀA ("when it is a number, we divide by it; when it is a matrix, we invert it"). Linear algebra also gives the normal equation quickly: C(A) is the column space and the error e = b − Ax̂ lies in the perpendicular subspace N(Aᵀ), so Aᵀ(b − Ax̂) = 0. (pp. 155–156)

**Example 3.** A = [[1,0],[1,1],[1,2]], b = (6,0,0).
- AᵀA = [[3,3],[3,5]], Aᵀb = (6,0).
- Normal equations [[3,3],[3,5]]x̂ = (6,0) give x̂ = (5, −3) \tag{9}.
- p = 5(1,1,1) − 3(0,1,2) = (5,2,−1) and e = (1,−2,1) \tag{10}. Check: e is perpendicular to (1,1,1) and (0,1,2).
- det(AᵀA) = 15 − 9 = 6, (AᵀA)⁻¹ = (1/6)[[5,−3],[−3,3]], and
$$P=\tfrac16\begin{bmatrix}5&2&-1\\2&2&2\\-1&2&5\end{bmatrix}. \tag{11}$$
- Pb = (5,2,−1), as above. P² = P because a second projection changes nothing. (p. 156)

*Intuition note.* The recipe is the same for a line and for a subspace: make the error perpendicular to every basis vector, then solve a small square system.

**Warning.** Do not split (AᵀA)⁻¹ into A⁻¹(Aᵀ)⁻¹. That would give P = I. A is rectangular (m > n) and has no inverse. (p. 157)

**AᵀA is invertible if and only if A has linearly independent columns.** Proof (p. 157):
- Show that AᵀA and A have the same nullspace. If Ax = 0, then AᵀAx = 0.
- Conversely, suppose AᵀAx = 0. Multiply by xᵀ:
$$(x^{\mathsf T})A^{\mathsf T}Ax=0\ \Rightarrow\ (Ax)^{\mathsf T}(Ax)=0\ \Rightarrow\ \|Ax\|^2=0. \tag{12}$$
So Ax = 0. The nullspaces are equal.
- If A has independent columns, its nullspace is {0}, so AᵀA (square, n×n) has nullspace {0} and is invertible.

AᵀA is also symmetric, since (AᵀA)ᵀ = Aᵀ(Aᵀ)ᵀ = AᵀA. Examples: A = [[1,2],[1,2],[0,0]] (dependent columns) gives AᵀA = [[2,4],[4,8]], singular. A = [[1,2],[1,2],[0,1]] (independent) gives AᵀA = [[2,4],[4,9]], invertible. (p. 157)

*Intuition note.* AᵀA can only lose information that A already loses. Since ‖Ax‖² = xᵀAᵀAx, a vector killed by AᵀA must have length zero after A.

**Brief summary.** Solve AᵀAx̂ = Aᵀb. Then p = Ax̂, e = b − p, p = Pb. P² = P. The distance from b to C(A) is ‖e‖. Strang says "P is invertible only if P = I". (p. 157)

**Worked Example 4.2 A.** b = (3,4,4), a = (2,2,1). The projection onto the line is p = (18/9)a = (4,4,2), with e = (−1,0,2) perpendicular to a. Now take the plane of a and a* = (1,0,0), A = [a a*]. Then AᵀA = [[9,2],[2,1]] and (AᵀA)⁻¹ = (1/5)[[1,−2],[−2,9]]. The projection matrix is P = [[1,0,0],[0,.8,.4],[0,.4,.2]]. Then p* = Pb = (3, 4.8, 2.4) and e* = (0, −.8, 1.6) is perpendicular to a and a*. This e* is in the nullspace of P, so its projection is zero. (p. 158)

**Worked Example 4.2 B.** Pulse measured as 70, 80, 120. The system Ax = b has Aᵀ = [1 1 1] and b = (70,80,120). Minimizing E = (x−70)² + (x−80)² + (x−120)² by dE/dx = 0, or projecting b onto (1,1,1), gives x̂ = average = 90. (p. 158)

**Worked Example 4.2 C.** The new average of 1000 numbers is a combination of the old average (of 999 numbers) and the mismatch: x̂_new = x̂_old + (1/1000)(b₁₀₀₀ − x̂_old), which Strang calls a "Kalman filter" with gain 1/1000. (p. 158)

**Problem Set 4.2, orthogonal projection (Problem 0).** A projection satisfies P² = P. The extra condition Pᵀ = P makes it an "orthogonal projection". For p = Pb to be perpendicular to e = b − p, one needs P² = P = Pᵀ. (p. 159)

### 4.3 Least Squares Approximations

**Setting.** Often Ax = b has no solution, usually because there are too many equations (m > n). The n columns span a small part of Rᵐ, and b is outside it unless measurements are perfect. When ‖b − Ax̂‖² reaches its minimum, x̂ is a least squares solution. The projection p = Ax̂ links this section to 4.2. The short rule: when Ax = b has no solution, multiply by Aᵀ and solve AᵀAx̂ = Aᵀb. (p. 163)

**Example 1.** Fit b = C + Dt to the points (0,6), (1,0), (2,0). Equations: C = 6, C + D = 0, C + 2D = 0. So A = [[1,0],[1,1],[1,2]], x = (C,D), b = (6,0,0), unsolvable since b is not a combination of (1,1,1) and (0,1,2). This is the same data as Example 3 of Section 4.2, so x̂ = (5,−3). The best line is 5 − 3t. (pp. 163–164)

**Minimizing the error: three views (pp. 164–166).**
- *Geometry.* Every Ax lies in the plane of the columns. The nearest point to b is the projection p. The smallest error is e = b − p, perpendicular to the columns. The heights p = (5, 2, −1) do lie on a line, because p is in C(A).
- *Algebra.* b = p + e, where Ax = b is impossible but Ax̂ = p is solvable. Squared error for any x:
$$\|Ax-b\|^2=\|Ax-p\|^2+\|e\|^2. \tag{2}$$
This holds because Ax − p is in the column space and e is in the left nullspace (right-triangle law). Choosing x = x̂ reduces Ax − p to zero and leaves the unavoidable ‖e‖².
- *Check on the example.* The errors are e = (1, −2, 1), the vertical distances to the line (Figure 4.6). They add to zero because e is perpendicular to the first column (1,1,1).
- *Calculus.* E = ‖Ax − b‖² = (C+D·0−6)² + (C+D·1)² + (C+D·2)² \tag{3}. Setting ∂E/∂C = 0 and ∂E/∂D = 0, and cancelling 2:
$$3C+3D=6,\qquad 3C+5D=0, \tag{4}$$
whose matrix [[3,3],[3,5]] is AᵀA. The extra factors 0, 1, 2 in ∂E/∂D (chain rule) are the second column of A. These are the normal equations. In general, E = xᵀAᵀAx − 2xᵀAᵀb + bᵀb has zero partial derivatives when AᵀAx̂ = Aᵀb. Here C = 5, D = −3, and the line passes through p = (5,2,−1), not through b = (6,0,0). (pp. 165–166)

*Intuition note.* "Smallest sum of squared errors" and "error at a right angle to the columns" are the same condition. The square makes the derivative linear, which is why the answer comes from a linear system.

**The big picture (Figure 4.7).** In Section 4.1, x was split into x_r + x_n and there were many solutions. Here there are no solutions to Ax = b, so b is split into p + e. We solve Ax̂ = p. With independent columns, N(A) = {0}, AᵀA is invertible and Aᵀe = 0. Strang says Chapter 7 will give the complete picture, in which the best solution is x̂ = x̂_r in the row space. (pp. 166–167)

**Fitting a straight line to m points (t₁,b₁),…,(t_m,b_m).** Equations C + Dtᵢ = bᵢ give
$$A=\begin{bmatrix}1&t_1\\ \vdots&\vdots\\1&t_m\end{bmatrix}\ (m\times2) \tag{5}$$
The two columns are independent unless all tᵢ are the same. Then (shapes: AᵀA is 2×2, Aᵀb is 2×1)
$$A^{\mathsf T}A=\begin{bmatrix}m&\sum t_i\\ \sum t_i&\sum t_i^2\end{bmatrix} \ (6),\qquad A^{\mathsf T}b=\begin{bmatrix}\sum b_i\\ \sum t_ib_i\end{bmatrix}\ (7)$$
$$\begin{bmatrix}m&\sum t_i\\ \sum t_i&\sum t_i^2\end{bmatrix}\begin{bmatrix}C\\D\end{bmatrix}=\begin{bmatrix}\sum b_i\\ \sum t_ib_i\end{bmatrix}. \tag{8}$$
The errors are eᵢ = bᵢ − C − Dtᵢ. The error vector is perpendicular to the columns (geometry) and in N(Aᵀ) (linear algebra). E(x) = ‖Ax − b‖² minimized by calculus gives the same equation. With n parameters and n < m, the derivatives of ‖Ax − b‖² give n equations AᵀAx̂ = Aᵀb. "The derivative of a square is linear", which is one reason least squares is popular. (pp. 167–168)

**Example 2 (orthogonal columns).** b = 1, 2, 4 at t = −2, 0, 2. The times add to zero, so (1,1,1) ⊥ (−2,0,2). Then AᵀA is diagonal:
$$\begin{bmatrix}3&0\\0&8\end{bmatrix}\begin{bmatrix}C\\D\end{bmatrix}=\begin{bmatrix}7\\6\end{bmatrix}\ \Rightarrow\ C=\tfrac73,\ D=\tfrac68. \tag{9}$$
The diagonal entries are m = 3 and t₁² + t₂² + t₃² = 8. Shifting times by subtracting the average t̂ = (t₁+⋯+t_m)/m makes the columns orthogonal. For times 1, 3, 5 the average is 3, the shifted times are −2, 0, 2, and A_newᵀA_new = [[3,0],[0,8]]. The best line is then C + D(t − t̂) = C + D(t − 3). Strang calls this the "Gram–Schmidt idea" of the next section: make the columns orthogonal in advance. (p. 168–169)

**Dependent columns (what is x̂?).** Example: A = [[1,1],[1,1]], b = (3,1): two measurements at the same time T. The projection is p = (2,2), with errors (1, −1), and Ax̂ = p has infinitely many solutions because (1,−1) is in the nullspace. All the dashed lines in the figure have the same errors. Strang's instinct is the horizontal line at height 2, but with the line written as ct + d the same instinct gives (c,d) = (0,2) instead of (C,D) = (2,0). He says "I don't see any way out." Section 4.5's pseudoinverse picks the shortest solution x⁺ = (1,1), of length √2 (the solutions (2,0) and (0,2) have length 2). That is the solution in the row space, with nullspace component zero. With independent columns, x⁺ is the usual (AᵀA)⁻¹Aᵀb. A MATLAB comment lists three difficulties: singular with no solution, singular with many solutions, very close to singular. (p. 169)

**Fitting by a parabola.** For b = C + Dt + Et², the unknowns C, D, E still enter linearly, so this is still linear algebra. With m > 3 points,
$$A=\begin{bmatrix}1&t_1&t_1^2\\ \vdots&\vdots&\vdots\\1&t_m&t_m^2\end{bmatrix}\ (m\times3),\qquad A^{\mathsf T}A\hat x=A^{\mathsf T}b\ \text{(three normal equations)}. \tag{10}$$
Strang notes that Galileo's stone has a ½gt² term, and that Fourier series is least squares in infinite dimensions (integral of the squared error instead of a sum). **Example 3.** For b = 6, 0, 0 at t = 0, 1, 2 the system is square and solved exactly: (C,D,E) = (6, −9, 3), parabola 6 − 9t + 3t². (p. 170)

**Worked Example 4.3 A (outlier).** Data (1,0),…,(9,0),(10,40), best horizontal line y = C under three error measures:
- Least squares (sum of squares): C = 4 (10C = 40).
- Least maximum error: C = 20 (halfway between 0 and 40).
- Least sum of absolute errors: C = 0, the median. Statisticians who worry about outliers prefer this, but the equations become nonlinear.

Least squares line C + Dt: AᵀA = [[10,55],[55,385]], Aᵀb = (40,400), so C = −8, D = 24/11. Scaling: multiplying b by 3 multiplies C and D by 3, and adding 30 to every bᵢ adds 30 to C. (p. 171)

**Worked Example 4.3 B.** Parabola for b = (0,0,1,0,0) at t = −2,−1,0,1,2. A is a 5×3 Vandermonde matrix with rows (1, t, t²); AᵀA = [[5,0,10],[0,10,0],[10,0,34]], Aᵀb = (1,0,0). Column 2 is orthogonal to columns 1 and 3 because the times are symmetric, so D uncouples. Result: C = 34/70, D = 0, E = −10/70. (pp. 171–172)

**Review of key ideas (pp. 175).** x̂ minimizes ‖Ax−b‖² = xᵀAᵀAx − 2xᵀAᵀb + bᵀb. The normal equations are AᵀAx̂ = Aᵀb. Aᵀe = 0 is a key equation. For m points and n < m functions the least squares solution is the combination with smallest mean square error. (p. 175)

**Problem Sets (overview).** Problem Set 4.1 covers Fredholm's Alternative (Problems 6–7: if b is not in C(A), there are numbers y with Aᵀy = 0 and yᵀb = 1, "exactly one problem has a solution"), and AᵀAx = 0 ⇒ Ax = 0 (Problem 9). Set 4.2 covers orthogonal projections and the properties P² = P = Pᵀ (Problems 22–27, 34). Set 4.3 covers four data points b = (0,8,8,20) at t = 0,1,3,4 (Problems 1–11), basic statistics (Problems 12–16), and challenge problems including the closed-form line fit with centred times (Problem 30). (pp. 148–150, 159–162, 172–175)

## Toy example (ours, not from the text)
Fit b = C + Dt to the points (0,1), (1,2), (2,2).

1. A = [[1,0],[1,1],[1,2]], b = (1,2,2).
2. AᵀA = [[3,3],[3,5]] (entries m = 3, Σt = 3, Σt² = 5). Aᵀb = (1+2+2, 0·1+1·2+2·2) = (5, 6).
3. det(AᵀA) = 15 − 9 = 6, so (AᵀA)⁻¹ = (1/6)[[5,−3],[−3,3]].
4. x̂ = (1/6)(5·5 − 3·6, −3·5 + 3·6) = (1/6)(7, 3) = (7/6, 1/2). The best line is 7/6 + t/2.
5. p = Ax̂ = (7/6, 7/6+1/2, 7/6+1) = (7/6, 5/3, 13/6). e = b − p = (−1/6, 1/3, −1/6).
6. Check Aᵀe = 0: sum of entries = −1/6 + 2/6 − 1/6 = 0, and 0·(−1/6) + 1·(1/3) + 2·(−1/6) = 0. ✓.
7. E = ‖e‖² = 1/36 + 4/36 + 1/36 = 1/6 ≈ 0.167.
8. Compare another line, C = 1, D = 1/2: heights (1, 1.5, 2), errors (0, 0.5, 0), E = 0.25 > 1/6. The projection gives the smaller E, as the theory says.

## Concepts
- [[orthogonality]] — vᵀw = 0; for subspaces, every vector of one is orthogonal to every vector of the other (pp. 143–144)
- [[four-fundamental-subspaces]] — here shown as two orthogonal pairs: C(Aᵀ) ⊥ N(A) and C(A) ⊥ N(Aᵀ) (pp. 144–146)
- [[orthogonal-complement]] (new) — V^⊥ = all vectors orthogonal to V; dimensions of V and V^⊥ add to the ambient dimension for these pairs (p. 145)
- [[rank-nullity]] — used for the counts r + (n−r) = n and r + (m−r) = m (p. 145)
- [[projection]] — closest point p in a subspace to b; e = b − p is orthogonal to the subspace (p. 151)
- [[projection-matrix]] (new) — P = A(AᵀA)⁻¹Aᵀ, with P² = P = Pᵀ (called an orthogonal projection); P = aaᵀ/aᵀa for a line (pp. 154–155, 159)
- [[rank-one-matrix-outer-product]] — aaᵀ/aᵀa is a column times a row, rank one (p. 154)
- [[normal-equations]] (new) — AᵀAx̂ = Aᵀb, meaning Aᵀ(b − Ax̂) = 0 (p. 155)
- [[least-squares]] — x̂ minimizing ‖Ax − b‖² when Ax = b is unsolvable (pp. 163–164)
- [[linear-independence]] — independent columns of A are exactly what makes AᵀA invertible (p. 157)
- [[null-space]] and [[column-space]] — N(AᵀA) = N(A); the error lies in N(Aᵀ) (pp. 156–157, 168)
- [[pseudoinverse]] — only previewed: the shortest least squares solution x⁺ in the row space (p. 169)

## Canonical instances
- [[wall-and-floor-not-orthogonal]] — two 2-dim subspaces of R³ cannot be orthogonal since 2+2 > 3 (p. 145)
- [[line-fit-three-points]] — points (0,6),(1,0),(2,0), best line 5 − 3t, errors (1,−2,1) (pp. 163–165)
- [[pulse-average-projection]] — best single value for 70, 80, 120 is the average 90 (p. 158)
- [[outlier-three-error-measures]] — C = 4 (squares), 20 (max), 0 (sum of absolutes) for nine zeros and a 40 (p. 171)
- [[parabola-fit-galileo]] — b = C + Dt + Et² still a linear problem in C, D, E (p. 170)
- [[kalman-filter-running-average]] — x̂_new = x̂_old + (1/1000)(b₁₀₀₀ − x̂_old) (p. 158)

## Bridges (candidates)
- [same-math] normal equations AᵀAx̂ = Aᵀb ↔ statistics/regression: ordinary least squares estimator (Problems 13–14 on p. 173–174 call x̂ unbiased and give its covariance σ²(AᵀA)⁻¹)
- [same-math] Pythagoras ‖Ax−b‖² = ‖Ax−p‖² + ‖e‖² ↔ statistics: decomposition of squared error into fitted and residual parts
- [structural-analogy] Fourier series as least squares in infinite dimensions (p. 170) ↔ analysis: expansion in orthogonal functions
- [same-math] recursive average update (4.2 C) ↔ signal processing: Kalman filter with gain 1/n
- [structural-analogy] x = x_r + x_n and b = p + e ↔ the same orthogonal splitting seen from input side and output side

## Questions this raises
- How does Gram–Schmidt (Section 4.4) turn the columns of A into orthonormal ones so that AᵀA = I and least squares becomes easy?
- What does the pseudoinverse (Section 4.5) do when the columns are dependent, and why does x⁺ lie in the row space?
- How do the assumptions on the errors (mean zero, independent, equal variance) lead to the unbiased estimate and covariance formula in Problems 13–14?
- When a few points are outliers, how does the choice of error measure (squares, maximum, absolute sum) change the fit, and what do we lose by leaving the linear equations?

## Exercises worth doing
- Ex. 9 (p. 149) — AᵀAx = 0 implies Ax = 0, so AᵀA has the same nullspace as A — difficulty: easy
- Ex. 6–7 (p. 148) — Fredholm's Alternative: combine equations into 0 = 1 using a vector in N(Aᵀ) — difficulty: medium
- Ex. 18 (p. 161) — if P² = P then (I−P)² = I−P, and I−P projects onto the orthogonal complement — difficulty: easy
- Ex. 12 (p. 173) — projecting onto (1,…,1) gives the mean; variance and standard deviation appear — difficulty: easy
- Ex. 14 (p. 174) — covariance matrix of x̂ is σ²(AᵀA)⁻¹ — difficulty: hard
- Ex. 34 (p. 162) — P₁P₂ is a projection matrix iff P₁P₂ = P₂P₁ — difficulty: hard

## Reading notes
- This is part 1 of Chapter 4. It starts at the chapter opening page (printed p. 143, with the list of sections 4.1–4.5) and ends at the end of Section 4.3 (printed p. 175: challenge problems and "Review of the key ideas"). Sections 4.4 and 4.5 are in part 2. The split is at a section boundary.
- Page offset: printed = pdf − 10 (pdf 153 = printed 143).
- The text layer is heavily garbled in equations and matrices on many pages. All matrices and equations here were checked against the page images.
- Problem Set 4.3 refers to "Figure 4.9a/b" (e.g. Problems 1, 7, 9, 10, pp. 172–173), but the figure shown on p. 172 is Figure 4.8. Figure 4.9 does not appear in these pages.
- Problem 11 on p. 160 says "P (m by n) projects Rᵐ onto a subspace S". Per p. 152 a projection matrix is m by m, so "m by n" looks like a misprint.
- Some blanks (e.g. "dimension ____" on p. 170, "the ____ of 70, 80, 120" on p. 158) are fill-in-the-blank prompts in the source. I filled only those the text answers (x̂ = average = 90).
- Example 4 on p. 147 prints its answers next to the questions. I give them as printed.
- Strang's first-person remarks (e.g. "My instinct…", "I don't see any way out", p. 169) are the author's opinion and are reported as such.
