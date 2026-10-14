---
id: strang-2023-introduction/ch03-four-p1
work: strang-2023-introduction
unit: "3 The Four Fundamental Subspaces (part 1/3): chapter opener, 3.1 Vector Spaces and Subspaces, 3.2 Computing the Nullspace by Elimination: A = CR"
pages: 84-103
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Vector spaces, subspaces, and the nullspace via A = CR

## L0 — One line
A subspace is a set closed under linear combinations; elimination to the reduced echelon form R turns Ax = 0 into an easy problem whose n − r special solutions form a basis for the nullspace; the same elimination also gives A = CR.

## L1 — The gist (≤ 120 words)
Which sets of vectors behave like a "space", and how do we find all solutions of Ax = 0? Section 3.1 defines subspaces (closed under adding and scaling) and the column and row spaces. Section 3.2 uses elimination to reach R₀ = rref(A), the reduced row echelon form (the simplest matrix elimination can reach). The identity block in R₀ marks the independent columns of A. The remaining columns, collected in F, say how dependent columns combine independent ones. Setting each free variable (a variable without a pivot) to 1 (others 0) gives one special solution per free variable. A matrix with more columns than rows always has nonzero solutions of Ax = 0. Block elimination restates the same process in three steps.

**Prerequisites:** linear combinations; solving linear systems by row operations; matrix–vector multiplication as a combination of columns; transpose.

## L2 — Key ideas (5–10 bullets)
- A subspace must contain 0 and stay inside under every linear combination cv + dw. Lines and planes through the origin qualify; quarter-planes and shifted planes do not (pp. 85–87).
- Ax = b is solvable if and only if b is in the column space C(A). The row space is C(Aᵀ). "Span" means all combinations and does not require independence (pp. 87–88).
- The nullspace N(A) is a subspace, because Ax = 0 and Ay = 0 give A(cx + dy) = 0 (pp. 88, 93).
- Row operations do not change the nullspace. A reduces to R₀ = rref(A), which is completely determined by A (pp. 93, 95–96).
- The identity block in R₀ sits in the columns that match the first r independent columns of A. F is defined by H = WF: dependent columns equal independent columns times F (p. 95).
- Special solutions are the columns of $\begin{bmatrix}-F\\ I\end{bmatrix}$, or of $P^T\begin{bmatrix}-F\\ I\end{bmatrix}$ when a permutation P is needed. They are n − r in number (p. 97).
- If n > m, then Ax = 0 has at least n − m free columns and so nonzero solutions (p. 98).
- Block elimination gives $P_RAP_C = CW^{-1}B$, using that W is invertible and $JW^{-1}H = K$ (p. 99).

## L3 — Walkthrough

### Chapter opener (p. 84)
- Chapter 3 allows every m by n matrix; Chapter 2 treated square invertible ones, where nullspaces held only the zero vector (p. 84).
- The author's stated goal is the Fundamental Theorem of Linear Algebra (Section 3.5, outside this part). It connects four subspaces (column space, row space, nullspace of A, nullspace of Aᵀ) with dimensions r, r, n − r, m − r (p. 84).
- The nullspace "starts with equations Ax = 0, not with columns or rows from A" (p. 84).
- Preview (p. 84): the nullspace is a subspace, because combinations of solutions of Ax = 0 are also solutions. The r independent columns of A are a basis for C(A), and the n − r special solutions are a basis for N(A). Their dimensions are r and n − r. Basis and dimension are defined later in the chapter.

### 3.1 Vector Spaces and Subspaces (pp. 85–88)
**Vector space.** Rⁿ is the set of column vectors with n real components. The key operation is the linear combination cv + dw. Any vector space must satisfy eight rules (listed in Problem Set 3.1, p. 89):
1. x + y = y + x
2. x + (y + z) = (x + y) + z
3. a unique zero vector with x + 0 = x for all x
4. a unique −x with x + (−x) = 0
5. 1x = x
6. (c₁c₂)x = c₁(c₂x)
7. c(x + y) = cx + cy
8. (c₁ + c₂)x = c₁x + c₂x

Rules 1–4 concern x + y, rules 5–6 concern cx, and rules 7–8 connect them (p. 89). The author says they need not be memorized. One important requirement is that all combinations cv + dw **stay in the space** (p. 85).

Non-examples (p. 85):
- the positive vectors (all vᵢ > 0);
- the solutions of Ax = (1,…,1);
- a line not through 0.

**Examples of spaces** (p. 85):
- Z = {0} is the smallest vector space. It is the nullspace of A when the only solution of Ax = 0 is x = 0, which means the columns are independent.
- R³ˣ³ is the space of all 3 by 3 matrices.
- The matrices with all 9 entries equal form a "line of matrices".
- The symmetric 3 by 3 matrices form a subspace. The invertible matrices do not.
- Functions: y = ceˣ solves dy/dx = y, and the quadratics a + bx + cx² solve d³y/dx³ = 0. Linear differential equations replace Ax = 0 in function space.
- The 3 by 3 matrices are "essentially the same" as R⁹. The quadratics are essentially the same as R³.

**Definition (subspace, p. 86).** A subspace is a set of vectors, including 0, such that for v, w in it and any scalar c: (i) v + w is in it; (ii) cv is in it. The eight rules are then automatic, since they are inherited from the host space. Every subspace contains 0 (take c = 0 in rule ii). The subspaces of R³ are: lines through 0 (L), planes through 0 (P), all of R³, and Z (p. 86).

**Combined rule (p. 87):** a subspace containing v and w must contain all combinations cv + dw.

**Examples in R² (p. 87).**
- Example 1: the quarter-plane x, y ≥ 0 contains (2,3) but not (−2,−3). Rule (ii) fails for c = −1.
- Example 2: two opposite quarter-planes satisfy (ii). Rule (i) fails: (2,3) + (−3,−2) = (−1,1) lies in neither.
- Example 3: in the 2 by 2 matrices M, the upper triangular matrices U and the diagonal matrices D are subspaces, and D lies inside U. The multiples cI form a line of matrices. The matrix I by itself is not a subspace; only the zero matrix alone is.

> **Intuition note.** A subspace is a flat piece of space through the origin. Adding or scaling can never push you out of it. One failed combination is enough to disqualify a set.

**Column space (p. 87).** C(A) is the set of all combinations of the columns, which is the set of all Ax. *The equations Ax = b are solvable if and only if b is in C(A)*; the coefficients of that combination solve Ax = b (p. 87). The columns themselves are not a subspace. Only their combinations are (p. 88).

**Row space (p. 88).** It is the column space C(Aᵀ), a subspace of Rⁿ. Aᵀy = c is solvable exactly when c is in it. Chapter 1 gave r independent vectors in each of C(A) and C(Aᵀ), so rank A = rank Aᵀ = r; a new proof comes in 3.5 (p. 88). Example: for the rank-1 matrix A = uvᵀ, the row space is the line of all cv, and the column space is the line of multiples of u (p. 88).

**Span (p. 88).** If a set S spans V, then V is all combinations of S, and it is the smallest vector space containing S. Independence is not required. Examples: an invertible n by n matrix has columns spanning Rⁿ. The invertible 3 by 3 matrices span R³ˣ³, and so do the singular ones (p. 88). The text leaves "show the invertible 2 by 2 matrices span R²ˣ²" as a test question. The nullspace N(A) is introduced as a vector space because Ax = 0 and Ay = 0 give A(cx + dy) = 0; finding its vectors needs new ideas (p. 88).

**Problem Set 3.1 (pp. 89–92)** has problems 1–31. Examples: other definitions of addition (1–3, 7); which subsets are subspaces (8–15); column spaces and solvability of Ax = b (16–26); challenge problems on S + T, ∩ and ODE solution spaces (27–31).

### 3.2 Computing the Nullspace by Elimination: A = CR (pp. 93–99)
**Summary box (p. 93).**
1. N(A) is all solutions of Ax = 0, including x = 0.
2. Elimination A → R₀ → R keeps the nullspace: N(A) = N(R₀) = N(R).
3. R₀ = rref(A) has I in r columns and F in n − r columns.
4. If column j depends on previous columns, there is a special solution with xⱼ = 1.
5. The n − r special solutions contain −F and I.
6. Every short wide matrix (m < n) has nonzero solutions of Ax = 0.

For invertible A the only solution is x = 0. In general A has r independent columns and n − r columns that are combinations of them, which give n − r special solutions (p. 93).

**Example 1 (p. 93).** $R=[\,I\ \ F\,]P=\begin{bmatrix}1&0&3&5\\0&1&4&6\end{bmatrix}$ with P = I, so Rx = 0 reads x₁ + 3x₃ + 5x₄ = 0 and x₂ + 4x₃ + 6x₄ = 0.
- Free variables x₃, x₄ are set to (1,0) and (0,1).
- s₁ = (−3,−4,1,0) and s₂ = (−5,−6,0,1).
- Every combination c₁s₁ + c₂s₂ is also in N(R).

**Example 2 (p. 94).** $R_0=\begin{bmatrix}1&7&0&8\\0&0&1&9\\0&0&0&0\end{bmatrix}$, with I in columns 1 and 3 and a zero row last. The free variables are x₂, x₄, and the special solutions are s₁ = (−7,1,0,0) and s₂ = (−8,0,−9,1). A permutation P is needed to bring I to the first columns.

**Plan (p. 94).** Simplest case R = [I F] (r, m, n = 2, 2, 4). General case $R_0=\begin{bmatrix}I&F\\0&0\end{bmatrix}P$ (r, m, n = 2, 3, 4). I and F have r rows, and R₀ has m − r zero rows. Removing them leaves R = [I F]P. The key question for each new column is whether it depends on the previous columns (p. 94).

**Elimination (p. 95).** The allowed steps, in any order:
1. subtract a multiple of one row from another (above or below);
2. multiply a row by a nonzero number;
3. exchange rows.

Worked example from the text:
$$A=\begin{bmatrix}1&2&11&17\\3&7&37&57\end{bmatrix}\to\begin{bmatrix}1&2&11&17\\0&1&4&6\end{bmatrix}\to\begin{bmatrix}1&0&3&5\\0&1&4&6\end{bmatrix}=R.$$
The steps are: subtract 3 × row 1 from row 2; then subtract 2 × new row 2 from row 1 (p. 95).

Elimination inverted the leading block $W=\begin{bmatrix}1&2\\3&7\end{bmatrix}$. Write $A=[\,W\ \ H\,]$. Then
$$W^{-1}A=W^{-1}[\,W\ \ H\,]=[\,I\ \ W^{-1}H\,]=[\,I\ \ F\,],$$
so H = WF. Here $\begin{bmatrix}11&17\\37&57\end{bmatrix}=\begin{bmatrix}1&2\\3&7\end{bmatrix}\begin{bmatrix}3&5\\4&6\end{bmatrix}$ (p. 95).

R is the same however elimination is carried out (p. 95). Facts (p. 95):
1. The first r independent columns of A locate the columns of R containing I; P puts them in place.
2. F is determined by (dependent columns) = (independent columns) × F.
3. The last m − r rows of R₀ are zero.

**Example 2 elimination (p. 95).** Take $A=\begin{bmatrix}1&7&3&35\\2&14&6&70\\2&14&9&97\end{bmatrix}$ (rank 2), and use the elimination steps shown on that page to reach R₀. Then (p. 96) C times F gives the dependent columns 2 and 4 of A:
$$\begin{bmatrix}1&3\\2&6\\2&9\end{bmatrix}\begin{bmatrix}7&8\\0&9\end{bmatrix}=\begin{bmatrix}7&35\\14&70\\14&97\end{bmatrix}.$$
The author notes this combination (35, 70, 97) could not have been seen in Chapter 1 (p. 96).

**Algorithm, column by column (p. 96).** After k columns the part done is in rref form, $\begin{bmatrix}I_k&F_k\\0&0\end{bmatrix}P_k$. The next column is split into an upper part u and a lower part ℓ.
- If ℓ is all zeros, the column is dependent. Then u joins F_k to give F_{k+1}.
- If ℓ is not all zero, the column is independent. Pick a nonzero in ℓ as pivot (preferably the largest), move its row up to row k + 1, and eliminate the rest of the column. The column then joins I_k to give I_{k+1}.

The pivot column numbers at the end are the first r independent columns of A, which form C. In R₀ the 1's of the identity are the first nonzeros in their rows. Zero rows go last (p. 94).

**A = CR and the nullspace (p. 97).** Reduce A to R₀. Then I in R₀ locates C. Removing zero rows gives R in A = CR. There is one special solution for each column of F. For Example 2 (p. 97) the special solutions are s₁ = (−7,1,0,0) and s₂ = (−8,0,−9,1), with 1 and 0 (or 0 and 1) in positions 2 and 4.

**Special solutions (p. 97).** For [I F]x = 0 they are the columns of $\begin{bmatrix}-F\\ I\end{bmatrix}$ (Example 1). For [I F]Px = 0 they are the columns of $P^T\begin{bmatrix}-F\\ I\end{bmatrix}$ (Example 2). The check uses $PP^T=I$:
$$[\,I\ \ F\,]P\cdot P^T\begin{bmatrix}-F\\ I\end{bmatrix}=[\,I\ \ F\,]\begin{bmatrix}-F\\ I\end{bmatrix}=[\,0\,].$$

**Review (p. 97).** For A of rank r: reduce to R₀, remove the m − r zero rows to get R = [I F]P with A = CR. The special solutions are the n − r columns of $P^T\begin{bmatrix}-F\\ I\end{bmatrix}$.

> **Intuition note.** Elimination rewrites the same equations so that each pivot variable is written in terms of the free ones. Setting one free variable to 1 and the others to 0 gives one basic solution for each. Every other solution is a combination of those.

**Example 3 (pp. 97–98).** $A=\begin{bmatrix}1&2&1\\2&4&5\\3&6&9\end{bmatrix}\to R_0=\begin{bmatrix}1&2&0\\0&0&1\\0&0&0\end{bmatrix}$, rank 2, pivot columns 1 and 3, $R=\begin{bmatrix}1&2&0\\0&0&1\end{bmatrix}$.
- Set x₂ = 1. Then x₁ = −2 and x₃ = 0, so s = (−2,1,0).
- All solutions are x = (−2c, c, 0).
- $A=CR=\begin{bmatrix}1&1\\2&5\\3&9\end{bmatrix}\begin{bmatrix}1&2&0\\0&0&1\end{bmatrix}$. C holds a column basis and R a row basis. The rows of A are combinations of the rows of R (p. 98).

**Zero nullspace and n > m (p. 98).** If the only solution of Ax = 0 is x = 0, the columns are independent and there are no special solutions. This is impossible if n > m, since n independent columns cannot fit in Rᵐ. If n > m, there are at least n − m free columns, so Ax = 0 has nonzero solutions. The nullspace dimension is the number of free variables, explained in 3.5.

**Example 4 (pp. 98–99).** $A=\begin{bmatrix}1&2\\3&8\end{bmatrix}$, $B=\begin{bmatrix}A\\2A\end{bmatrix}$ (4 by 2), $M=[\,A\ \ 2A\,]=\begin{bmatrix}1&2&2&4\\3&8&6&16\end{bmatrix}$.
- A reduces to I, so N(A) = Z, with no free variables and no F.
- B has the same nullspace Z. Extra rows add conditions and cannot enlarge the nullspace.
- M reduces to $R=\begin{bmatrix}1&0&2&0\\0&1&0&2\end{bmatrix}=[\,I\ \ F\,]$. Its free variables are x₃, x₄, and the special solutions are s₁ = (−2,0,1,0) and s₂ = (0,−2,0,1).

**Block elimination in three steps (p. 99).** Let A have rank r.
- Step 1: exchange columns by P_C and rows by P_R so the first r independent columns and rows come first: $P_RAP_C=\begin{bmatrix}W&H\\J&K\end{bmatrix}$, with $C=\begin{bmatrix}W\\J\end{bmatrix}$ and $B=[\,W\ \ H\,]$ both of rank r.
- Step 2: multiply the top r rows by W⁻¹ to get $[\,I\ \ W^{-1}H\,]=[\,I\ \ F\,]$.
- Step 3: subtract $J[\,I\ \ W^{-1}H\,]$ from the lower rows $[\,J\ \ K\,]$ to get $[\,0\ \ 0\,]$.

$$P_RAP_C=\begin{bmatrix}W&H\\J&K\end{bmatrix}\to\begin{bmatrix}I&W^{-1}H\\J&K\end{bmatrix}\to\begin{bmatrix}I&W^{-1}H\\0&0\end{bmatrix}=R_0\tag{1}$$

Two facts are needed:
1. W is invertible. From A = CR, taking the r independent rows gives B = WR. B and R have rank r and W is r by r, so W has rank r.
2. $JW^{-1}H=K$. The upper rows $[\,I\ \ W^{-1}H\,]$ are independent. Since A has rank r, the lower rows $[\,J\ \ K\,]$ must be combinations of them. The first r columns force the multipliers to be J (because JI = J). The last columns then require $JW^{-1}H=K$.

Conclusion: $P_RAP_C=\begin{bmatrix}W\\J\end{bmatrix}W^{-1}[\,W\ \ H\,]=CW^{-1}B$. The middle W⁻¹ is needed because C and B both contain W (p. 99).

> **Intuition note.** A matrix of rank r is fully determined by r independent columns, r independent rows, and the r by r block W where they cross. The inverse W⁻¹ removes the double counting of W.

**Problem Set 3.2 (pp. 100–103)** has problems 1–46: nullspace facts, true/false on pivots, constructing matrices with given nullspaces, rank inequalities rank(AB) ≤ rank(A) and rank(AB) ≤ rank(B), left and right inverses, block factorizations, and a Kirchhoff current-law problem.

## Toy example (ours, not from the text)
Let $A=\begin{bmatrix}1&2&5\\2&5&12\end{bmatrix}$, so m = 2, n = 3, and n > m forces a free variable.
1. Subtract 2 × row 1 from row 2: row 2 = (2−2, 5−4, 12−10) = (0, 1, 2).
2. Subtract 2 × new row 2 from row 1: row 1 = (1−0, 2−2, 5−4) = (1, 0, 1).
3. So $R=\begin{bmatrix}1&0&1\\0&1&2\end{bmatrix}=[\,I\ \ F\,]$, $F=\begin{bmatrix}1\\2\end{bmatrix}$, r = 2, P = I.
4. Check H = WF with $W=\begin{bmatrix}1&2\\2&5\end{bmatrix}$ and $H=\begin{bmatrix}5\\12\end{bmatrix}$: $WF=(1\cdot1+2\cdot2,\ 2\cdot1+5\cdot2)=(5,12)$ ✓.
5. The special solution is $\begin{bmatrix}-F\\ I\end{bmatrix}=(-1,-2,1)$. Check: $1(-1)+2(-2)+5(1)=0$ and $2(-1)+5(-2)+12(1)=0$ ✓.
6. $A=CR$ with C = first two columns = W: $CR$ has third column $(1\cdot1+2\cdot2,\ 2\cdot1+5\cdot2)=(5,12)$ ✓.

## Concepts
- [[vector-space]] (new) — a set with addition and scalar multiplication obeying eight rules; all combinations cv + dw stay inside (pp. 85, 89)
- [[subspace]] (new) — a vector space inside another: contains 0, closed under v + w and cv (p. 86)
- [[linear combination]] — the weighted sum cv + dw; the basic operation of every vector space (p. 85)
- [[span]] — all combinations of a set S; the smallest vector space containing S; independence not required (p. 88)
- [[column space (range)]] — all combinations of the columns of A, i.e. all Ax; Ax = b solvable iff b is in it (p. 87)
- [[null space (kernel)]] — all solutions x of Ax = 0; a subspace; unchanged by row operations (pp. 88, 93)
- [[rank]] — r, the number of independent columns; rank A = rank Aᵀ (pp. 88, 93)
- [[rank-one matrix / outer product]] — A = uvᵀ has column space the line of u and row space the line of v (p. 88)
- [[linear independence]] — here used as: columns are independent when only x = 0 gives Ax = 0 (pp. 85, 98)
- [[reduced-row-echelon-form]] (new) — R₀ = rref(A) = $\begin{bmatrix}I&F\\0&0\end{bmatrix}P$; unique for A (pp. 94–96)
- [[special-solutions]] (new) — one nullspace solution per free variable, with that variable 1 and the others 0 (pp. 93, 97)
- [[A-equals-CR]] (new) — A = CR, with C the independent columns of A and R = R₀ without zero rows (p. 97)
- [[block-elimination]] (new) — P_R A P_C = C W⁻¹ B, from the r by r block W (p. 99)
- [[four fundamental subspaces]] — column space, row space, nullspace of A and of Aᵀ; only announced here (p. 84)

## Canonical instances
- [[quarter-plane-not-subspace]] (new) — fails scaling by −1 (p. 87)
- [[two-quarter-planes-not-subspace]] (new) — satisfies scaling but fails addition (p. 87)
- [[upper-triangular-and-diagonal-subspaces]] (new) — subspaces U ⊃ D of the 2 by 2 matrices (p. 87)
- [[rref-4-column-example-1]] (new) — R = [I F], special solutions (−3,−4,1,0) and (−5,−6,0,1) (p. 93)
- [[rank-2-3x4-example-2]] (new) — R₀ with zero row, A = CR, F = $\begin{bmatrix}7&8\\0&9\end{bmatrix}$ (pp. 94–96)
- [[M-equals-A-2A]] (new) — a matrix with more columns than rows has free variables (pp. 98–99)

## Bridges (candidates)
- [structural-analogy] N(A) = solutions of Ax = 0 ↔ differential equations: solutions of dy/dx = y or d³y/dx³ = 0 form function spaces (p. 85)
- [metaphor] dependent columns H = WF ↔ regression/feature structure: F gives the combination of independent columns that rebuilds each dependent one (p. 95)
- [structural-analogy] special solutions, one per free variable ↔ parametrising a solution set: each free variable is a free parameter and the pivot variables follow from it (pp. 93, 97)
- [structural-analogy] Kirchhoff's current law Aᵀy = 0 ↔ networks: current in = current out at every node as a nullspace condition (Problem 35, p. 102)

## Questions this raises
- Why do the n − r special solutions form a basis of N(A), and what is a basis? (Section 3.4.)
- How do the column space, row space, N(A) and N(Aᵀ) fit together, and why do their dimensions add up to r, r, n − r, m − r? (Section 3.5.)
- When Ax = b has a solution, how are all solutions built from a particular solution plus the nullspace? (Section 3.3.)
- Why is rref(A) unique, whatever elimination path is used?

## Exercises worth doing
- Ex. 20 (p. 91) — when adding a column b to A enlarges the column space; links to solvability — difficulty: easy
- Ex. 9 (p. 90) — test subsets of R³ against the subspace requirements — difficulty: easy
- Ex. 13 (p. 101) — plane parallel to a subspace as particular solution plus nullspace; recommended — difficulty: medium
- Ex. 19 (p. 101) — a 2 by 2 matrix with nullspace equal to its column space — difficulty: medium
- Ex. 39 (p. 103) — AB = I implies BA = I via rank(AB) ≤ rank(A); marked important — difficulty: medium
- Ex. 43 (p. 103) — shapes of the blocks in R₀, right and left inverses; recommended — difficulty: hard

## Reading notes
- This part starts at the chapter opener (printed p. 84) and ends with Problem 46 of Problem Set 3.2 (p. 103, the last page given). Sections 3.3–3.5 are not covered here. The split falls at a section boundary.
- Printed page = pdf page − 10.
- The text layer is garbled in several places: matrices, the eight-rule list, Problem Set 3.1 and 3.2 formulas. I checked all matrices against the page images.
- The chapter opener lists Section 3.2 as "The Nullspace of A: Solving Ax = 0", while the section heading on p. 93 reads "Computing the Nullspace by Elimination: A = CR".
- The text refers to "Appendix 9" and to "the last page of Chapter 3" (pp. 94, 97). Neither is in these pages.
- In the Example 2 elimination (p. 95), the last step shown (the third arrow) combines a row exchange and division of a row by 3. Only the displayed matrices are described here.
- Exercise solutions are not given in these pages.
