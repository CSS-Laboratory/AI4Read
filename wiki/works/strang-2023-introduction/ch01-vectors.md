---
id: strang-2023-introduction/ch01-vectors
work: strang-2023-introduction
unit: "1 Vectors and Matrices"
pages: 1-38
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Vectors and Matrices (Strang, Ch. 1)

## L0 — One line
A matrix times a vector is a combination of the matrix's columns; the independent columns give the rank and the factorization A = CR.

## L1 — The gist (≤ 120 words)
The chapter asks how to describe all combinations of vectors and how to multiply matrices. Linear combinations, dot products, lengths and angles come first. Then a matrix times a vector is read two ways: as dot products with the rows, or as a combination of the columns. The column space (all combinations of the columns) leads to independence (no column is a combination of earlier ones) and to rank (the number of independent columns). Matrix multiplication AB is built from the columns of A, and any matrix factors as A = CR, with the independent columns in C. This gives an informal argument that row rank equals column rank. It also prepares elimination in later chapters.

**Prerequisites:** vectors as arrows or lists of numbers; Pythagoras' theorem; basic trigonometry (cos θ); solving two linear equations.

## L2 — Key ideas (5–10 bullets)
- Linear algebra starts from two operations, scaling a vector and adding vectors. Their combination cv + dw raises two questions: which vectors are reachable, and which c, d reach a given b (p. 2).
- Two independent vectors in the plane reach every vector there. Dependent ones (w = 3v) reach only a line; if b is off that line, elimination ends in an impossible equation like 0 = −2 (p. 4).
- The dot product v·w gives length (‖v‖² = v·v), perpendicularity (v·w = 0) and angle (cos θ = v·w/(‖v‖‖w‖)). The Schwarz and triangle inequalities follow (pp. 9–13).
- Ax can be computed by rows (dot products) or by columns (a combination of the columns of A). The author finds the column picture better for understanding Ax (p. 19).
- The column space C(A) is the set of all Ax. The number of independent columns is the rank r; for m = 3 it decides whether C(A) is a point, a line, a plane or all of R³ (pp. 20–22).
- AB can be computed four ways: dot products, columns of AB, rows of AB, or a sum of column-times-row rank-one matrices. All use mnp small multiplications. AB ≠ BA in general, but (AB)C = A(BC) always (pp. 27–29, 34).
- Taking the independent columns, left to right, into C gives A = CR, where R = [I F] and the dependent columns of A are CF. This yields an informal proof that row rank equals column rank (pp. 30–32).
- Elimination (row reduction) finds the numbers in R. R is essentially the reduced row echelon form (pp. 32–34).

## L3 — Walkthrough

### Chapter opening (p. 1)
Linear algebra is about vectors v and matrices A, objects that can be added and multiplied when shapes match. Running example: v = (2,4), w = (1,3), v + w = (3,7). A linear combination is cv + dw for all numbers c, d. ‖w‖ = √10, and v·w = (2)(1) + (4)(3) = 14. The matrix A = [v w] = [[2,1],[4,3]] has Ax = cv + dw for x = (c,d). It has a plane as column space. With a third column z = (3,7) = v + w, B = [v w z] has B(1,1,−1) = v + w − z = 0. So v, w are independent but v, w, z are dependent. The goal is AB = A times each column of B (p. 1).

### 1.1 Vectors and Linear Combinations (pp. 2–8)
- The two basic operations are multiplying by a number and adding vectors of the same dimension. Example: v = (2,1), w = (4,3): 3v = (6,3) and 5v − 2w = (10,5) − (8,6) = (2,−1) (p. 2). Another example: 2(4,1) − 3(2,−1) = (2,5) (p. 2).
- **Two key questions** (p. 2): (1) describe all combinations cv + dw (a plane or a line?); (2) find c, d producing a specific b. For an m by n matrix A with columns v₁…vₙ: (1) describe all Ax = x₁v₁ + … + xₙvₙ; (2) find x with Ax = b.
- **Picture and an example (p. 3).** With v = (2,1), w = (2,−1), v + w = (4,0) = w + v. The multiples cv fill a line. If w is not on that line, the multiples dw fill a second line, and the author aims to show that the combinations cv + dw fill the plane (confirmed for independent v, w on p. 4). Special cases: 1v + 1w is the sum, 1v − 1w the difference, 0v + 0w the zero vector.
- **Solving** c(2,1) + d(2,−1) = (8,2). The equations are 2c + 2d = 8 and c − d = 2. Multiply equation 1 by ½ to get c + d = 4. Subtract it from equation 2 to get 0c − 2d = −2 (as printed). So d = 1, then 2c + 2 = 8 gives c = 3. Check: 3(2,1) + 1(2,−1) = (8,2) (p. 3).
- **Three ways to write the problem** (p. 4). Column way: c(v₁,v₂) + d(w₁,w₂) = (b₁,b₂). Row way: v₁c + w₁d = b₁ and v₂c + w₂d = b₂. Matrix way: [[v₁,w₁],[v₂,w₂]](c,d) = (b₁,b₂).
- If v, w and 0 are not on one line, there is exactly one solution (c,d). Then the combinations exactly fill the xy plane, the vectors are "linearly independent", and the 2 by 2 matrix [v w] is "invertible" (p. 4).
- **Can elimination fail?** Author: it fails to produce a solution "only when the equations don't have a solution in the first place". This happens when v and w lie on one line through (0,0), so they are dependent (p. 4). Example: v = (1,2), w = (3,6), b = (1,0). Equations: c + 3d = 1 and 2c + 6d = 0. Subtracting 2 × equation 1 from equation 2 gives 0 = −2, which is impossible. Here w = 3v. If b is off the line, there is no solution (p. 4).
- A zero in the pivot place is not a failure, only a reason to exchange equations. For c(0,1) + d(2,3) = (2,7), swap the equations: c + 3d = 7 and 2d = 2 give d = 1, c = 4 (p. 4).

*Intuition note.* Two vectors reach a whole plane only if they point in different directions. If not, one is wasted, and the equations contradict each other when b is off the line.

- **Three dimensions** (p. 5). With v = (2,3,1), w = (1,1,0): cv + dw = (2c + d, 3c + d, c). Two vectors can fill at most a plane; this is "not enough vectors", not dependence. Three independent vectors are needed to fill R³. The simplest are i = (1,0,0), j = (0,1,0), k = (0,0,1), with ci + dj + ek = (c,d,e) (eq. 1). Any v = v₁i + v₂j + v₃k, i.e. Iv = v for the 3 by 3 identity matrix I. A 2-dimensional vector and a 3-dimensional vector cannot be combined (p. 5).
- **Why a plane?** For independent nonzero v, w in R³, take two combinations cv + dw and Cv + Dw. The halfway point h = ½(c + C)v + ½(d + D)w is again a combination, so the surface is flat. Author: this reasoning "maybe" is not complete (it relies on intuition about planes); another proof comes in 1.2 (p. 5).
- Problem Set 1.1 (pp. 6–8) covers lines and planes of combinations, triangle and parallelogram vectors, cube and clock vectors (Fig. 1.1), cones and pyramids of combinations (Fig. 1.2), and 4D cubes.

### 1.2 Lengths and Angles from Dot Products (pp. 9–17)
- **Dot product** (1), (2): v·w = v₁w₁ + v₂w₂ in 2D, and v·w = v₁w₁ + … + vₙwₙ = w·v in n dimensions (p. 9).
- **Length:** ‖v‖² = v·v = v₁² + … + vₙ². In 2D this is Pythagoras. For w = (1,2,3), the right triangle has sides (1,2,0) and (0,0,3), so (1² + 2²) + 3² = 14 = ‖w‖² (p. 9). The vector (1,1,1,1) has length 2. The diagonal of the unit cube in n dimensions has length √n (p. 10).
- **Unit vector:** ‖u‖ = 1. If v ≠ 0, then u = v/‖v‖ is a unit vector (p. 10). Examples: u = (cos θ, sin θ) has u·u = cos²θ + sin²θ = 1 and i·u = cos θ. For v = (1,5,5,7): ‖v‖² = 1 + 25 + 25 + 49 = 100, so u = v/10 (p. 10).
- **Perpendicular vectors** (3), (4): v·w = 0 gives ‖v + w‖² = ‖v‖² + ‖w‖². Proof: ‖v + w‖² = (v + w)·(v + w) = v·v + v·w + w·v + w·w, and two terms are zero. Also ‖v − w‖² = ‖v‖² + ‖w‖² (p. 10).
- Example 2: (1,1)·(1,−1) = 0, with v + w = (2,0), v − w = (0,2), and ‖v‖² = ‖w‖² = 2, ‖v ∓ w‖² = 4 (p. 10).
- Example 3: (4,2)·(−1,2) = −4 + 4 = 0. Seesaw reading: weights (4,2) at positions (−1,2) balance, because the "moments" sum to zero (p. 11).
- Example 4: for unit vectors, cos θ = v·u. Example 5: cost = q·p = q₁p₁ + q₂p₂ + q₃p₃ (quantities times prices). q·p = 0 means "the books balance" (p. 11).
- **Angle** (p. 12). Example 6: v = (cos α, sin α), w = (cos β, sin β) have v·w = cos α cos β + sin α sin β = cos(β − α), the angle between them. The sign of v·w tells the side of a right angle: positive means angle < 90°, negative means angle > 90°. Example: v = (3,1) and w₂ = (1,−3) are perpendicular (dot 3 − 3 = 0).
- **Cosine formula** (5): for nonzero v, w, v·w/(‖v‖‖w‖) = cos θ. For unit vectors, u·U = cos θ; this stays true in n dimensions (p. 12).

*Intuition note.* Dividing by the lengths removes size and keeps direction. So v·w/(‖v‖‖w‖) = cos θ depends on the angle between the directions: it runs from −1 (opposite) through 0 (perpendicular) to 1 (same direction).

- **Inequalities** (p. 13). Since |cos θ| ≤ 1:
  - Schwarz: |v·w| ≤ ‖v‖‖w‖. Author's remark: it was found in France, Germany and Russia, "maybe elsewhere", and is the most important inequality in mathematics.
  - Triangle: ‖v + w‖ ≤ ‖v‖ + ‖w‖.
  - Derivation (6): ‖v + w‖² = v·v + v·w + w·v + w·w ≤ ‖v‖² + 2‖v‖‖w‖ + ‖w‖², using Schwarz. Take square roots. "Side 3 cannot exceed Side 1 + Side 2."
- Example 7: v = (2,1), w = (1,2): v·w = 4, ‖v‖ = ‖w‖ = √5, so cos θ = 4/5. Schwarz: 4 < 5. Triangle: v + w = (3,3) has length √18 < √5 + √5; squared, 18 < 20 (p. 13).
- Example 8: v = (a,b), w = (b,a): v·w = 2ab and ‖v‖ = ‖w‖ = √(a² + b²). Schwarz says 2ab ≤ a² + b². Equivalent: geometric mean |ab| ≤ arithmetic mean ½(a² + b²), because ½(a² + b²) − ab = ½(a − b)² is a square (p. 13).
- **A plane in 3D** (p. 13). For a unit vector n, the vectors w with w·n = 0 fill a 2D plane in R³, perpendicular to the "normal vector" n. Its equation is n₁w₁ + n₂w₂ + n₃w₃ = 0. For n = (0,0,1) this is w₃ = 0, the xy plane.
- **Worked examples** (p. 14).
  - 1.2A: v = (3,4), w = (4,3): v·w = 24, ‖v‖ = ‖w‖ = 5. Schwarz: 24 < 25. v + w = (7,7) has length 7√2 < 10, and cos θ = 24/25.
  - 1.2B: equality in both inequalities happens when one vector is a multiple of the other (w = cv, angle 0° or 180°); the triangle inequality is an equality for angle 0° (e.g. w = 2v, both sides 3‖v‖).
  - 1.2C: u = v/5 = (3/5,4/5). A perpendicular vector is (−4,3) or (4,−3); divide by 5 to make U a unit vector (two possibilities).
  - 1.2D: Law of Cosines by Pythagoras in the left triangle with a = ‖v‖, b = ‖w‖, c = ‖v − w‖: c² = (a sin θ)² + (b − a cos θ)² = a² sin²θ + b² − 2ab cos θ + a² cos²θ = a² + b² − 2ab cos θ. Compare with ‖v − w‖² = ‖v‖² + ‖w‖² − 2v·w to match v·w with ‖v‖‖w‖ cos θ.
- Problem Set 1.2 (pp. 15–17) includes: an algebraic Schwarz proof (Prob. 21), the parallelogram identity (24), and a MATLAB average |u·U| (28).

### 1.3 Matrices and Their Column Spaces (pp. 18–25)
- **Setup** (p. 18). A = [[1,2],[3,4],[5,6]] is 3 by 2 (m = 3 rows, n = 2 columns), rank 2. A square matrix has m = n. Types shown: identity, diagonal, triangular, symmetric. The 3 by 4 "difference matrix" has rows (−1,1,0,0), (0,−1,1,0), (0,0,−1,1).
- **Row picture** (p. 19): each component of Ax is a dot product (row i)·x. For the difference matrix, eq. (1): Ax = (x₂ − x₁, x₃ − x₂, x₄ − x₃). It takes mn small multiplications. A must have as many columns as x has components.
- **Column picture** (2), (3): Ax = x₁a₁ + x₂a₂ + x₃a₃ + x₄a₄, a combination of the columns of A. Same multiplications as the row picture. Numerical case: A(7,8) = (1·7 + 2·8, 3·7 + 4·8, 5·7 + 6·8) = (23,53,83) = 7(1,3,5) + 8(2,4,6) (p. 18). Author's habit: he computes with dot products but prefers the column picture to understand Ax (p. 19).

*Intuition note.* The two pictures give the same numbers. The column picture shows that the outputs of A are exactly the combinations of its columns.

- **Independence** (p. 20). Independent means the only combination of columns giving Ax = 0 is x = 0. Equivalently, each new column is not a combination of earlier ones.
  - A₁ = [[1,0,0],[2,4,0],[3,5,6]]: columns independent, combinations fill R³ (solve for x₁, x₂, x₃ one component at a time).
  - A₂ = [[1,2,3],[1,4,5],[6,0,6]]: column 1 + column 2 = column 3. Only two independent columns; the column space is a plane.
  - A₃ = [[1,3,4],[2,6,8],[5,15,20]]: a₂ = 3a₁, a₃ = 4a₁. The column space is the line of multiples of (1,2,5).
- **Column space** C(A) = all Ax = all combinations of the columns (p. 20). **Span** = all linear combinations of a set of vectors, so the span of the columns (independent or not) is C(A) (p. 21).
- A₄ (upper triangular, ones on and above the diagonal) has four independent columns. Triangular matrices are easy provided the diagonal has no zeros (p. 21). Eq. (5): every v is (v₁ − v₂)(1,0,0,0) + (v₂ − v₃)(1,1,0,0) + (v₃ − v₄)(1,1,1,0) + v₄(1,1,1,1), so C(A₄) = R⁴ (p. 21).
- A₅ = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]: eq. (4), column 4 = column 1 − column 2 + column 3. So only 3 independent columns, and A₅x = v is solvable only when v is in C(A₅) (pp. 21–22).
- **Four possibilities for C(A) with m = 3** (p. 22): all of R³ (3 independent columns), a plane through 0 (2), a line through 0 (1), the point (0,0,0) (zero matrix). The author's note says "column space" did not appear in Chapter 1 of the 5th edition; he now prefers to meet the idea early (p. 22).
- **Five questions** previewed (p. 22): the number r of independent columns is the rank; the first r independent columns are a basis for the column space; combinations of them give the other n − r columns; A = CR with C m by r and R r by n; the r rows of R are a basis for the row space (called "amazing").
- **Rank-one matrices** (p. 23). Author: every matrix of rank r is a sum of r rank-one matrices. For A₆ = [[1,3,−2],[4,12,−8],[2,6,−4]], the columns are a₁, 3a₁, −2a₁ with a₁ = (1,4,2), and every row is a multiple of one row. (added step: the blank in the text, "All rows of this matrix A₆ are multiples of ___", is filled by the first row (1,3,−2).) The 2 by 2 case [[a, ma],[b, mb]]: row 2 = (b/a) × row 1 (if a = 0, row 1 = 0 × row 2). The 3 by 3 case [[a, ma, pa],[b, mb, pb],[c, mc, pc]]: rows 2 and 3 are b/a and c/a times row 1 (for a ≠ 0). Author's guess: row rank equals column rank for every matrix. He "believes" it is the first great theorem of the subject (p. 23).
- Problem Set 1.3 (pp. 24–26): describe column spaces, find dependent columns, rank of A + B, "Ax = b is solvable if b is in the column space" (12), rank-one completion (10), dependent rows imply dependent columns (19, 22).

### 1.4 Matrix Multiplication AB and CR (pp. 27–37)
- **Column rule** (1): AB = [Ab₁ … Ab_p]; needs row length of A = column length of B (p. 27). For the exchange matrix B = [[0,1],[1,0]] and A = [[1,2],[3,4]]: AB = [[2,1],[4,3]], the columns of A exchanged.
- **Example** B = [[5,6],[7,8]] (pp. 27–28). Row way: Ab₁ = (1·5 + 2·7, 3·5 + 4·7) = (19,43). Column way: 5(1,3) + 7(2,4) = (5,15) + (14,28) = (19,43) (eq. 3). Ab₂ = 6(1,3) + 8(2,4) = (6,18) + (16,32) = (22,50) (eq. 5). So AB = [[19,22],[43,50]] (eq. 4).
- **Counting.** For A (m×n) and B (n×p), AB is m×p. Row way: mp dot products, n multiplications each. Column way: p columns, mn each. Both give mnp small multiplications (p. 28). Author: speed depends on storage; BLAS 3 matrix–matrix operations are best (p. 28).
- **Non-commutative** (6): with B the exchange matrix, AB exchanges the columns of A: [[2,1],[4,3]]. BA exchanges the rows: [[3,4],[1,2]]. So in general BA ≠ AB. Multiplying on the left gives row operations on A; on the right, column operations (p. 28).
- Footnote (p. 28): Strassen found that 7 multiplications suffice for 2 by 2 matrices (at the cost of extra additions). This lowers the n×n count to nᶜ with c = log₂7 instead of 3. Author: c cannot go below 2, since all n² entries must be used; finding the smallest c is an "extremely tough unsolved problem".
- **Associative law** (p. 29): (AB)C = A(BC), and distributive (7): A(B + C) = AB + AC. Sizes: A m×n, B n×p, C p×q, so (AB)C is m×q. Test with B the exchange matrix: (BA)B = [[3,4],[1,2]]·B = [[4,3],[2,1]] = B(AB). So row operations on A can come before or after column operations. When C is a vector x with a single 1 in position j, (AB)x = A(Bx) says that column j of AB is A times column j of B. This is the rule (1).
- **Review of AB** (p. 29): entry (i,j) is (row i of A)·(column j of B); column j of AB is A times column j of B.

*Intuition note.* Each column of AB is A applied to one column of B. So every column of AB is a combination of the columns of A.

- **Rank-one and A = CR** (pp. 29–30). Example 1: A = [[1,2,10,100],[3,6,30,300],[2,4,20,200]] equals (1,3,2)ᵀ times [1 2 10 100], i.e. C (3×1) times R (1×4) (eq. 8). Conclusion: if the column space of A is a line, so is the row space (p. 30).
- **Choosing C** (p. 30): go left to right. Put a column in C if it is not a combination of earlier columns. The r columns of C are independent: if Cx = 0 with some xⱼ ≠ 0, dividing by the last nonzero coefficient would make that column a combination of earlier ones, which the construction forbids. Example 2: A = [[2,6,4],[4,12,8],[1,3,5]]. Column 2 = 3 × column 1, so C = columns 1 and 3, rank 2.
- **R** (pp. 31–32). R tells how to produce all columns of A from C. In (9)–(10): A = [[2,4],[4,8],[1,5]]·[[1,3,0],[0,0,1]]. Properties: (1) C has r independent columns of A; (2) R = [I F], with I in the r columns that held C; (3) the dependent columns of A are CF. So A = C[I F] = [C CF] (in the correct order). C has the column space of A, and R has the row space of A. Example 3: A = [[1,2,3],[4,5,6],[7,8,9]] = [[1,2],[4,5],[7,8]]·[[1,0,−1],[0,1,2]], so F = (−1,2) (eq. 11). Column j of A = C times column j of R; row i of A = row i of C times R. If all columns are independent, C = A and R = I. Another example (p. 32): [[1,2,3,4],[1,2,4,5]] = [[1,3],[1,4]]·[[1,2,0,1],[0,0,1,1]], all ranks 2.
- **Informal proof that row rank = column rank** (p. 32). (1) The r columns of C are independent by construction. (2) Every column of A is a combination of them (A = CR). (3) The r rows of R are independent, since they contain I. (4) Every row of A is a combination of the rows of R (A = CR by rows).
- **Finding R by elimination** (pp. 32–33). Example 4: A = [[1,3,4],[2,4,2],[3,7,6]]. Is column 3 a combination x(col 1) + y(col 2)? Subtract 2 × row 1 from row 2 and 3 × row 1 from row 3, giving B = [[1,3,4],[0,−2,−6],[0,−2,−6]] (eq. 13). The new equation −2y = −6 gives y = 3. Then x = −5 from the top equation (−5 + 9 = 4). Check: −5(1,2,3) + 3(3,4,7) = (4,2,6). So A = [[1,3],[2,4],[3,7]]·[[1,0,−5],[0,1,3]] = CR (14). Subtracting row 2 from row 3 of B gives U = [[1,3,4],[0,−2,−6],[0,0,0]] (eq. 15), a zero row, so rank 2. Eliminating upward gives R₀ = [[1,0,−5],[0,1,3],[0,0,0]]. Facts (p. 33): rows of R₀ are combinations of the rows of A; the zero row shows r = 2; the 2 by 2 identity shows columns 1, 2 are independent; removing the zero row leaves R. Key facts: the r columns of C are a basis for the column space (dimension r), and the r rows of R are a basis for the row space (dimension r); "basis" and "dimension" are defined in Section 3.4 (p. 33). Chapter 1 finds C first; Chapter 3 will find R first by elimination (pp. 32–33).
- **Columns times rows** (16) (p. 34): AB = a₁b₁* + … + aₙbₙ*, where aₖ are the columns of A and bₖ* the rows of B. Each aₖbₖ* is an "outer product" of rank one. Count: n rank-one matrices, mp multiplications each, total mnp. Example: A = [[1,4],[2,5],[3,6]], B = [[7,8,9],[10,11,12]]. (1,2,3)ᵀ[7 8 9] = [[7,8,9],[14,16,18],[21,24,27]]. (4,5,6)ᵀ[10 11 12] = [[40,44,48],[50,55,60],[60,66,72]]. Sum: AB = [[47,52,57],[64,71,78],[81,90,99]]. This uses 18 multiplications and 9 additions. AB has rank 2, so it has no inverse, and its determinant is zero (Chapter 5) (p. 34).
- **Note on R** (p. 34): R is essentially the "reduced row echelon form" of A; MATLAB's rref(A) includes m − r zero rows, called R₀ (Chapter 3). Example 5: [a₁ a₂ 3a₁ + 4a₂] = [a₁ a₂]·[[1,0,3],[0,1,4]] = CR. Quick product by columns times rows: CR = a₁[1 0 3] + a₂[0 1 4] (p. 35).
- **Four ways to multiply AB = C** (p. 35, 3×2 times 2×4): dot products (12 entries), A times each column of B (4 columns), each row of A times B (3 rows), column j of A times row j of B (2 rank-one matrices).
- Problem Set 1.4 (pp. 35–37): counts, A = CR practice (6–12), probability-1 independence of random matrices (9–10), rank of AB (16–17), counts for (AB)C vs A(BC) (20).

### Thoughts on Chapter 1 (p. 38)
- Author's view: what makes the subject easy is that all equations are linear; what makes it hard is that there are so many equations, unknowns and ideas. Ax = b suits problems of every size, with linearity A(x + y) = Ax + Ay.
- Each equation in Ax = b is a flat surface: 2x + 5y − 4z = 6 is a plane in 3D; 2x + 5y − 4z + 7w = 9 is a 3D plane (hyperplane?) in 4D. Ten planes in 11-dimensional space should "hopefully" meet along a line (11 − 10 = 1).
- **Expectation for a random m by n A:** m < n, probably many solutions; m = n, probably one solution; m > n, probably no solution. But the count need not be what we get, since columns may be combinations of earlier columns or equations may be combinations of earlier equations. The rank r gives the real size of the problem: A = CR = (m×r)(r×n).
- **Proof of associativity** (author's argument): for a one-column C = c, (AB)c = c₁Ab₁ + … + cₙAbₙ and A(Bc) = A(c₁b₁ + … + cₙbₙ). Linearity makes them equal. The same holds for every column of C, so (AB)C = A(BC).
- Closing message: for Ax, AB and CR, we write about combinations of columns, "not about dot products with the rows!" (p. 38).

## Toy example (ours)
Let A = [[1,2,3],[2,4,5]] (2×3). Take x = (1,1,1).

- Row picture: row 1·x = 1 + 2 + 3 = 6; row 2·x = 2 + 4 + 5 = 11. So Ax = (6,11).
- Column picture: 1·(1,2) + 1·(2,4) + 1·(3,5) = (1 + 2 + 3, 2 + 4 + 5) = (6,11). Same answer.
- Independent columns, left to right: column 1 = (1,2) is nonzero, so it goes into C. Column 2 = (2,4) = 2·(1,2) is dependent, so it is skipped. Column 3 = (3,5) is not a multiple of (1,2) (3/1 ≠ 5/2), so it goes into C. Hence r = 2, C = [[1,3],[2,5]].
- R = [I F] arranged in column order: R = [[1,2,0],[0,0,1]]. Column 2 of R is (2,0) because column 2 of A = 2·(column 1 of C) + 0·(column 2 of C).
- Check A = CR by columns × rows: (1,2)ᵀ[1 2 0] = [[1,2,0],[2,4,0]] and (3,5)ᵀ[0 0 1] = [[0,0,3],[0,0,5]]. Sum = [[1,2,3],[2,4,5]] = A. ✓
- Row rank: A has 2 rows. They are independent, since (2,4,5) is not a multiple of (1,2,3). So row rank = column rank = 2.

## Concepts
- [[vector]] — a list of numbers (arrow from the origin) that can be added and scaled (p. 2)
- [[linear-combination]] — cv + dw, or Ax = x₁a₁ + … + xₙaₙ (pp. 2, 19)
- [[span]] — all linear combinations of a set of vectors; the span of the columns is the column space (p. 21)
- [[linear-independence]] — only the zero combination of the columns gives zero; no column is a combination of earlier ones (p. 20)
- [[column-space]] — C(A): all Ax, all combinations of the columns (p. 20)
- [[rank]] — r, the number of independent columns of A (also of rows; informal proof) (pp. 22, 32)
- [[dot-product]] — v·w = Σvᵢwᵢ; gives length, perpendicularity, angle (p. 9)
- [[norm]] — length ‖v‖ = √(v·v) (p. 9)
- [[orthogonality]] — v·w = 0, the angle is 90° (p. 10)
- [[cosine-similarity]] — cos θ = v·w/(‖v‖‖w‖) (p. 12); this unit only derives it as the angle between vectors
- [[rank-one-matrix-outer-product]] — column times row; all columns on one line; AB = Σ aₖbₖ* (pp. 23, 34)
- [[schwarz-inequality]] (new) — |v·w| ≤ ‖v‖‖w‖ (p. 13)
- [[triangle-inequality]] (new) — ‖v + w‖ ≤ ‖v‖ + ‖w‖, derived from Schwarz (p. 13)
- [[unit-vector]] (new) — length 1; v/‖v‖ for v ≠ 0 (p. 10)
- [[row-and-column-pictures]] (new) — Ax as dot products with rows, or as a combination of columns (p. 19)
- [[cr-factorization]] (new) — A = CR with C the first r independent columns, R = [I F] (pp. 30–31)
- [[associative-law-matrix-product]] (new) — (AB)C = A(BC), proved column by column (pp. 29, 38)
- [[elimination]] (new) — subtract multiples of one equation from others to create zeros; used to find R (pp. 3, 32)
- [[identity-matrix]] (new) — I with Iv = v (p. 5)
- [[basis]] and [[dimension]] — only previewed here: the r columns of C are a basis, dimension r; defined in Section 3.4 (p. 33)

## Canonical instances
- [[seesaw-balance]] — v·w = 0 as a balance of moments (p. 11)
- [[price-quantity-cost]] — cost = q·p; q·p = 0 means the books balance (p. 11)
- [[exchange-matrix]] — right multiplication swaps columns, left multiplication swaps rows; AB ≠ BA (p. 28)
- [[difference-matrix]] — Ax = (x₂ − x₁, x₃ − x₂, x₄ − x₃) (p. 18)
- [[triangular-matrix-A4]] — upper-triangular ones; its column space is all of R⁴ (p. 21)
- [[matrix-A5]] — column 4 = column 1 − column 2 + column 3; rank 3 (p. 21)
- [[CR-example-4]] — elimination finds R for [[1,3,4],[2,4,2],[3,7,6]] (pp. 32–33)

## Bridges (candidates)
- [same-math] cos θ = v·w/(‖v‖‖w‖) ↔ embeddings/NLP: cosine similarity between vectors — the same formula, read as similarity.
- [structural-analogy] AB = Σ aₖbₖ* (sum of rank-one matrices) ↔ low-rank approximation/SVD: a matrix as a sum of rank-one pieces.
- [structural-analogy] A = CR (independent columns plus coefficients) ↔ feature selection: dependent features are combinations of selected ones.
- [metaphor] "m < n probably many solutions, m > n probably none" ↔ statistics: parameters vs. observations, identifiability.

## Questions this raises
- Why must row rank equal column rank for every matrix? The informal proof (p. 32) relies on R having independent rows; how is that made rigorous?
- How does elimination find R directly, without first guessing which columns are dependent?
- If the column space is the set of reachable b in Ax = b, what does the set of inputs x with Ax = 0 look like?
- When AB is computed by outer products, how does that help with big or low-rank matrices?

## Exercises worth doing
- Ex. 8 (p. 6) — vectors v = (1,−2,1), w = (0,1,−1): what every combination has in common, and why (3,3,6) is impossible — easy
- Ex. 21 (p. 16) — Schwarz inequality by algebra, via the identity with (v₁w₂ − v₂w₁)² — medium
- Ex. 25 (p. 17) — smallest and largest ‖v − w‖ and v·w for given lengths — medium
- Ex. 19 (p. 26) — dependent rows imply dependent columns in a 2 by 2 matrix — medium
- Ex. 15 (p. 37) — logical steps from A = CR to "column rank equals row rank" — medium
- Ex. 16 (p. 37) — the column space of AB lies inside the column space of A — medium

## Reading notes
- Printed page = pdf page − 10 (pdf 11 is printed p. 1). Printed numbers are visible on the pages.
- Running header: "Chapter 1. Vectors and Matrices". The author's note on p. 22 refers to "the 5th edition". The unit title page lists sections 1.1–1.4.
- The text layer was garbled for most matrices and formulas; they were checked against the page images.
- p. 9: the text says "Figure 1.2 shows v = (1,2)…" but the figure is captioned Figure 1.3 (apparent misprint).
- p. 12: the text names w₂ = (1,−3) as perpendicular to v = (3,1). Figure 1.6 draws the vector (−1,3) at the 90° position (also perpendicular).
- p. 14, 1.2D: the image reads ‖v − w‖² = ‖v‖² + ‖w‖² − 2v·w; the text layer shows an "=" before 2v·w, an OCR artefact.
- The v and w of Section 1.1 change from example to example; each example's vectors are as stated on its page.
- The Problem Sets were skimmed for topics; no solutions were printed and none are given here.
