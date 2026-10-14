---
id: strang-2023-introduction/ch03-four-p3
work: strang-2023-introduction
unit: "3.5 Dimensions of the Four Subspaces (part 3/3 of Chapter 3)"
pages: 129-142
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
# Dimensions of the Four Subspaces

## L0 — One line
For an m by n matrix of rank r, the row and column spaces have dimension r and the two nullspaces have dimensions n − r and m − r; elimination from A to R₀ preserves all four dimensions.

## L1 — The gist (≤ 120 words)
How big are the four fundamental subspaces of A, and what does elimination change? Strang first reads the dimensions off the echelon form R₀, where bases are visible. He then shows that A has the same row space and nullspace as R₀, and that its column space has the same dimension but is a different space. Transposing gives the left nullspace dimension. This is Part 1 of the Fundamental Theorem of Linear Algebra. A graph's incidence matrix illustrates it: loops and trees appear as dependent and independent rows, and Euler's formula follows. The unit ends with A = CR, a record of elimination, and a review of row operations.

**Prerequisites:** rank, pivots and free variables, rref, special solutions of Ax = 0, basis and dimension, transpose; row space, column space and nullspace; the left nullspace N(Aᵀ) (solutions of Aᵀy = 0) is defined in L3.

## L2 — Key ideas (5–10 bullets)
- **Dimension count.** Row space and column space have dimension r. N(A) has dimension n − r and N(Aᵀ) has dimension m − r (p. 129, p. 133).
- **Read bases off R₀.** The nonzero rows are a row space basis, the pivot columns a column space basis, and the special solutions a nullspace basis. Zero rows of R₀ give the left nullspace (pp. 130–131).
- **Elimination keeps the row space and nullspace, not the column space.** Same row space, same nullspace, different column space, same dimension. Reason: Ax = 0 exactly when R₀x = 0 (p. 132).
- **Counting theorem.** r + (n − r) = n. Applying it to Aᵀ gives r + (m − r) = m (p. 133).
- **Incidence matrix of a graph.** The four subspaces become constants, trees, the voltage law, loops and the current law. Euler's formula follows (pp. 134–135).
- **Rank r = r rank-one pieces.** A = CR is "columns of C times rows of R" (p. 136).
- **Rank bounds.** rank(AB) ≤ rank(A) and rank(AB) ≤ rank(B). Multiplying by an invertible matrix keeps the rank (p. 137).
- **Left nullspace from E.** If EA = R₀, the last m − r rows of E are a basis for N(Aᵀ). Also A = CR = C[I F]P (p. 141).

## L3 — Walkthrough

### 3.5 Introduction (p. 129)
- **Rank** counts independent columns. The **dimension** of a subspace is the number of vectors in a basis (p. 129).
- The four subspaces and their dimensions (p. 129):

| Subspace | Lives in | Dimension |
|---|---|---|
| row space C(Aᵀ) | ℝⁿ | r |
| column space C(A) | ℝᵐ | r |
| nullspace N(A) | ℝⁿ | n − r |
| left nullspace N(Aᵀ) | ℝᵐ | m − r |

- The left nullspace solves Aᵀy = 0, an n by m system. For an incidence matrix this is Kirchhoff's Current Law (p. 129).
- Part 1 of the Fundamental Theorem gives the dimensions. Part 2 (stated here only as a preview) says N(A) ⊥ row space and N(Aᵀ) ⊥ C(A) (p. 129).

### The four subspaces for R₀ (pp. 130–131)
Main point: the four dimensions are the same for A and R₀. Between A and R, one of the four subspaces can have a different dimension, because R drops zero rows, which changes m (p. 130).

Example, m = 3, n = 5, r = 2 (pivot rows 1, 2; pivot columns 1, 4):
$$R_0=\begin{bmatrix}1&3&5&0&7\\0&0&0&1&2\\0&0&0&0&0\end{bmatrix}$$

1. **Row space, dimension r.** The nonzero rows are a basis. The pivot columns show an r by r identity, so no combination of the pivot rows gives the zero row (p. 130).
2. **Column space, dimension r.** The pivot columns are independent, since they contain the identity. They span, because every free column is a combination of them (p. 130). The coefficients are the special solutions:
   - column 2 = 3(column 1), special solution (−3, 1, 0, 0, 0);
   - column 3 = 5(column 1), special solution (−5, 0, 1, 0, 0);
   - column 5 = 7(column 1) + 2(column 4), special solution (−7, 0, 0, −2, 1) (p. 130).
3. **Nullspace, dimension n − r = 3.** There is one special solution per free variable, giving $x = x_2 s_2 + x_3 s_3 + x_5 s_5$. They are independent because the identity appears in rows 2, 3, 5 (p. 131).
4. **Left nullspace, dimension m − r.** R₀ has r independent rows and m − r zero rows. So R₀ᵀ has m − r zero columns, and y can have nonzeros in its last m − r entries. In the example, $R_0^T y=0$ is solved by $y=(0,0,y_3)$ (eq. 1, p. 131). It is "left" because $R_0^Ty=0$ transposes to $y^TR_0=0^T$ (p. 131).

Summary (p. 131): in ℝⁿ the row space and nullspace have dimensions r and n − r (total n). In ℝᵐ the column space and left nullspace have r and m − r (total m).

*Intuition note:* In R₀ the pivots and zero rows make each basis visible. Counting pivots, free variables and zero rows gives r, n − r and m − r.

Example matrix reducing to R₀ (p. 131): $A=\begin{bmatrix}1&3&5&0&7\\0&0&0&1&2\\1&3&5&1&9\end{bmatrix}$ has the same row space as R₀ and a different column space, but the same dimension.

### The four subspaces for A (pp. 132–133)
Figure 3.3 shows the big picture: C(Aᵀ) and N(A) in ℝⁿ, C(A) and N(Aᵀ) in ℝᵐ, with dimensions r, n − r, r, m − r (p. 132).

1. **Row space.** Every row of A is a combination of rows of R₀, and vice versa. "Elimination changes rows, but not row spaces" (p. 132). So the first r rows of R₀ are a basis. One may also choose r rows of A, namely those that end up as pivot rows. These need not be the first r rows (p. 132).
2. **Column space has dimension r (column rank = row rank).**
   - *Wrong reason* (Strang's label): "A and R₀ have the same column space." This is false, because columns of R₀ often end in zeros (p. 132).
   - *Right reason:* the same combinations of columns are zero for A and R₀. Ax = 0 exactly when R₀x = 0. So the column spaces differ but the dimensions agree.
   - The r pivot columns of A are a basis for C(A) (p. 132).
3. **Nullspace.** Elimination does not change the solutions of Ax = 0. The special solutions are a basis, and there are n − r free variables. This is the **Counting Theorem**: dim C(A) + dim N(A) = dim ℝⁿ, i.e. r + (n − r) = n (p. 133).
4. **Left nullspace.** Aᵀ is n by m with column space of dimension r, and its whole space is ℝᵐ. So r + (m − r) = m (p. 133).

**Fundamental Theorem of Linear Algebra, Part 1** (p. 133): column space and row space both have dimension r. The nullspaces have dimensions n − r and m − r.

*Intuition note:* Row operations are reversible and only mix rows, so they cannot change which combinations of columns give zero. That is why the dependency pattern, and the rank, survive.

Further remarks (p. 133):
- Every vector Ax = b in C(A) comes from exactly one x in the row space. If Ay = b too, then A(x − y) = 0, so x − y lies in both N(A) and the row space, forcing x = y. From row space to column space, A acts like an r by r invertible matrix.
- The nullspaces force the "pseudoinverse" of Section 4.5 (the section is only mentioned here).

**Example 1** (p. 133): $A=\begin{bmatrix}1&2&3\\2&4&6\end{bmatrix}$, m = 2, n = 3, r = 1. The row space is the line through (1, 2, 3). The nullspace is the plane x₁ + 2x₂ + 3x₃ = 0, and 1 + 2 = 3. C(A) is the line through (1, 2) and N(Aᵀ) the line through (2, −1). They are perpendicular lines in ℝ², and 1 + 1 = 2. Final point: the y's in the left nullspace combine the rows of A to give the zero row.

### Example 2: an incidence matrix (pp. 134–135)
Five equations, one per edge, in four unknowns, one per node (eq. 2, p. 134). The matrix A is 5 by 4, with rows (−1, 1, 0, 0), (−1, 0, 1, 0), (0, −1, 1, 0), (0, −1, 0, 1), (0, 0, −1, 1), meaning $Ax=b$ gives differences across edges (p. 134).
- **N(A):** with b = 0 all four unknowns are equal, so $x=(c,c,c,c)$. A basis is (1, 1, 1, 1), so dim N(A) = 1 and r = 4 − 1 = 3 (p. 134).
- **C(A):** r = 3. Rref gives pivots in columns 1–3, with the fourth column free:
$$R_0=\begin{bmatrix}1&0&0&-1\\0&1&0&-1\\0&0&1&-1\\0&0&0&0\\0&0&0&0\end{bmatrix}$$
  A basis for C(A) is columns 1, 2, 3 of A, not of R₀ (p. 134).
- **Row space:** dimension 3. Row 3 = row 2 − row 1, so rows 1, 2, 4 are a basis. Edges 1, 2, 3 form a loop (dependent rows). Edges 1, 2, 4 form a tree (independent rows). Trees have no loops (p. 135).
- **N(Aᵀ):** dimension m − r = 5 − 3 = 2. One solution is y = (1, −1, 1, 0, 0), the upper loop. Another is y = (0, 0, −1, 1, −1), the lower loop. These are independent, so they form a basis (p. 135).
- Elimination on Aᵀ (4 by 5) would also give two special solutions. Loops and trees identify dependent and independent rows for every incidence matrix (p. 135).
- Ax = b gives "voltages" at nodes (Kirchhoff's Voltage Law). Aᵀy = 0 gives "currents" on edges (Current Law) (p. 135).

**Summary for a connected graph with n nodes and m edges** (p. 135): r = n − 1; dim N(A) = 1 (constant vectors); the edges of any tree give r independent rows; the components of Ax add to zero around loops (dim C(A) = n − 1); N(Aᵀ) is solved by loop currents, with m − n + 1 independent small loops. For every graph in a plane, Euler's formula follows:
$$(\text{nodes})-(\text{edges})+(\text{small loops})=n-m+(m-n+1)=1$$

*Intuition note:* The abstract counts become graph facts. The one free direction in N(A) is "shift every node's value equally", and the m − r independent relations among edges are the loops.

### Rank two = rank one + rank one (p. 136)
Rank-one matrices have the form $uv^T$. For a rank-2 matrix, reduce to R₀, drop the zero row to get R, then write
$$A=\begin{bmatrix}1&0&3\\1&1&7\\4&2&20\end{bmatrix}=\begin{bmatrix}1&0\\1&1\\4&2\end{bmatrix}\begin{bmatrix}1&0&3\\0&1&4\end{bmatrix}=CR\tag{3}$$
C holds the pivot columns of A: $u_1=(1,1,4)$ and $u_2=(0,1,2)$. They sit in the same first two columns because R has identity columns there. So $A=u_1v_1^T+u_2v_2^T$. Every rank r matrix is a sum of r rank-one matrices, "columns of C times rows of R" (p. 136).

### Worked examples (pp. 136–137)
- **3.5A** (four 1's in a 5 by 6 zero matrix). The rank is 1 if the 1's share a row, share a column, or fill two rows and two columns ($a_{ii}=a_{ij}=a_{ji}=a_{jj}=1$). Row and column space then have dimension 1. The nullspace is smallest, 6 − 4 = 2, when r = 4, which needs four different rows and four different columns. The sum r + (n − r) + r + (m − r) = n + m = 11 whatever the placement (p. 136). The follow-up (other entries all 2's) is left open.
- **3.5B** (rank of products). Rows of AB are combinations of rows of B, so rank(AB) ≤ rank(B). Columns of AB are combinations of columns of A, so rank(AB) ≤ rank(A). Multiplying by an invertible matrix does not change the rank. It cannot drop, since multiplying by the inverse could not make it rise again (p. 137).

### Problem Set 3.5 and Challenge Problems (pp. 137–140)
Problems 1–26 and Challenge Problems 27–35 are listed under "Exercises worth doing". Problem 11 and Problem 24 are marked "Important" (pp. 138–139).

### Thoughts on Chapter 3: the big picture of elimination (p. 141)
- One pass of elimination answers two questions. Is this column a combination of previous columns? (No, if it contains a pivot.) Is this row a combination of previous rows? (No, if it contains a pivot.) Zero rows of R₀ are not independent and disappear in R, which is r by n (p. 141).
- Elimination acts on rows but tells us about columns. The identity in R locates the independent columns of A. The free columns F give the combinations producing dependent columns, easy to miss without A = CR (p. 141).
- R is always the same, because special solutions are fully decided by A. R gives:
  - a basis for C(A): the r pivot columns of A;
  - a basis for the row space: the r rows of R;
  - a basis for N(A): the n − r special solutions (p. 141).
- **Left nullspace:** from EA = R₀, the last m − r rows of E are a basis for N(Aᵀ). Reducing [A I] to [R₀ E] keeps this record (p. 141).
- Fix C (m by r) and B (r by n), both of rank r, and choose any invertible r by r matrix M. All matrices CMB, and only those, have the same four subspaces (author's claim, p. 141).

### Row operations: review (p. 142)
- The three row operations are subtract a multiple of one row from another, exchange rows, and multiply a row by a nonzero constant. Each is reversible, so the total effect is an invertible m by m matrix E (p. 142).
- Nullspace is unchanged: Ax = 0 ⇒ EAx = 0 ⇒ Ax = 0. A and EA have different rows but the same row space and nullspace (p. 142).
- $EA=R_0=\begin{bmatrix}I&F\\0&0\end{bmatrix}P=\mathrm{rref}(A)$, with I r by r, F r by n − r, and P putting the columns in order (p. 142).
- **Factorization:** $A=CR=C\,[I\ \ F]\,P=[C\ \ CF]\,P$ (independent columns, then dependent columns, then reorder) (p. 142).
- Special solutions: $s_k=P^T\begin{bmatrix}-\text{column }k\text{ of }F\\ +\text{column }k\text{ of }I\end{bmatrix}$, and $P^T$ puts the n entries in the right order (p. 142).
- Example (P = I, r = 3): $R=\begin{bmatrix}1&0&0&3\\0&1&0&4\\0&0&1&5\end{bmatrix}$, $s_1=(-3,-4,-5,1)$, $Rs_1=0$ and $As_1=CRs_1=0$ (p. 142).

## Toy example (ours)
Let $A=\begin{bmatrix}1&2&3\\0&1&1\\1&3&4\end{bmatrix}$, so m = n = 3.
- Row 3 = row 1 + row 2. Subtract 2·(row 2) from row 1 to get $R_0=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}$, so r = 2.
- **Row space:** basis (1, 0, 1), (0, 1, 1); dimension 2 = r.
- **Column space:** pivot columns of A, (1, 0, 1) and (2, 1, 3); dimension 2. Column 3 is (1, 0, 1) + (2, 1, 3) = (3, 1, 4) ✓. C(A) ≠ C(R₀): (1, 0, 1) is in C(A), but every column of R₀ has third entry 0.
- **Nullspace:** the free variable is x₃, giving s = (−1, −1, 1). Check A s: −1 − 2 + 3 = 0; −1 + 1 = 0; −1 − 3 + 4 = 0 ✓. Dimension 1 = n − r.
- **Left nullspace:** E = [[1, −2, 0], [0, 1, 0], [−1, −1, 1]] gives EA = R₀. Check row 3 of EA: −(1, 2, 3) − (0, 1, 1) + (1, 3, 4) = (0, 0, 0) ✓. The last row of E, (−1, −1, 1), is in N(Aᵀ). Dimension 1 = m − r. (It equals s here by coincidence of the numbers.)
- **Counts:** 2 + 1 = 3 = n and 2 + 1 = 3 = m.

## Concepts
- [[rank]] — number of pivots = number of independent columns = number of independent rows (pp. 129, 132).
- [[dimension]] — number of vectors in any basis of a subspace (p. 129).
- [[four fundamental subspaces]] — C(Aᵀ) and N(A) in ℝⁿ, C(A) and N(Aᵀ) in ℝᵐ, with dimensions r, n − r, r, m − r (p. 129).
- [[rank–nullity (Fundamental Theorem of Linear Maps)]] — here the Counting Theorem r + (n − r) = n (p. 133).
- [[column space (range)]] — spanned by the pivot columns of A; not preserved by elimination (p. 132).
- [[null space (kernel)]] — solutions of Ax = 0; preserved by elimination; basis = special solutions (pp. 131–133).
- [[left nullspace]] (new) — N(Aᵀ), the y with yᵀA = 0ᵀ; dimension m − r (p. 131).
- [[special solutions]] (new) — one solution of Rx = 0 per free variable; a nullspace basis (p. 131).
- [[rank-one matrix / outer product]] — uvᵀ; every rank r matrix is a sum of r of them (p. 136).
- [[incidence matrix]] — rows with −1 and 1 for the nodes at each edge's ends (p. 134).
- [[A = CR factorization]] (new) — independent columns C times R = rref without zero rows (pp. 136, 142).
- [[row operations as invertible matrix E]] (new) — EA = R₀; E records elimination (p. 142).

## Canonical instances
- [[incidence-matrix-5-edges-4-nodes]] — Figure 3.4 graph; dimensions 1, 3, 3, 2; loops and trees (pp. 134–135).
- [[kirchhoff-laws]] — Ax = b voltages, Aᵀy = 0 currents (p. 135).
- [[euler-formula]] — nodes − edges + small loops = 1 for planar graphs (p. 135).
- [[rank-two-CR-example]] — A = CR with 3 by 3 rank-2 matrix (p. 136).

## Bridges (candidates)
- [structural-analogy] Left nullspace of an incidence matrix ↔ network science: loop currents / cycle space — independent loops count m − n + 1.
- [same-math] Aᵀy = (flow in) − (flow out) = 0 ↔ graph theory: flow conservation as a nullspace condition.
- [structural-analogy] A = CR (independent columns plus mixing matrix) ↔ data science: low-rank factorization of a matrix.

## Questions this raises
- Why must N(A) be perpendicular to the row space, and N(Aᵀ) to C(A) (Part 2, only previewed here, p. 129)?
- If A maps its row space one-to-one onto C(A) (p. 133), how does one build an inverse on those spaces (the pseudoinverse, Section 4.5)?
- How do loops and trees give a basis for N(Aᵀ) and C(Aᵀ) for any connected graph, not just this example?
- How would the answers of Worked Example 3.5A change if the other entries were 2's (left open, p. 136)?

## Exercises worth doing
- Ex. 1 (p. 137) — dimensions of the four subspaces from m, n, r alone — difficulty: easy
- Ex. 4 (p. 137) — construct matrices with prescribed subspaces, or show impossibility — difficulty: medium
- Ex. 11 (p. 138) — inequalities among m, n, r when Ax = b has no solution for some b — difficulty: medium
- Ex. 19 (p. 139) — the combination of rows that gives the zero row, and the left nullspace — difficulty: medium
- Ex. 24 (p. 139) — when Aᵀy = d is solvable, and when y is unique — difficulty: medium
- Ex. 31 (p. 140) — incidence matrix of the complete graph on 4 nodes, with its rank and a vector in each subspace — difficulty: medium

## Reading notes
- This part starts at the opening of Section 3.5 (printed p. 129) and ends at the end of the row-operations review page (printed p. 142). Earlier sections of Chapter 3 are in other parts. The split is at a section boundary.
- Printed page = pdf − 10.
- The text layer is badly garbled in equations and matrices (for example Problems 3, 19, 27, 34, 35). I checked the images for all matrices used above.
- Small misprints in the source: p. 130 has a stray comma in "(−5, 0, 1, 0, 0, )". The Problem Set number "34" is missing in the text layer but present in the layout.
- Problem 28 refers to a "Figure 3.5", which is not on these pages. Page 142 refers to "page 88, Example I", also not on these pages.
- Strang's note on p. 141 says this is the first textbook to give elimination in the form A = CR = C[I F]P.
