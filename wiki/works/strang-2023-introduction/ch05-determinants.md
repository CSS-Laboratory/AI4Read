---
id: strang-2023-introduction/ch05-determinants
work: strang-2023-introduction
unit: "5 Determinants (5.1 3 by 3 Determinants and Cofactors; 5.2 Computing and Using Determinants; 5.3 Areas and Volumes by Determinants)"
pages: 198-215
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
# Determinants (Strang, Ch. 5)

## L0 — One line
The determinant is one number per square matrix that can be computed from pivots, cofactors, or n! signed terms; it signals invertibility and equals the volume scaling of the map (as |det|).

## L1 — The gist (≤ 120 words)
What does det A tell us, and how do we compute it? Strang gives three formulas. (1) Multiply the pivots from elimination, usually the fastest. (2) Expand by cofactors, which also gives $A^{-1}=C^{\mathsf T}/\det A$. (3) Add the n! terms of the big formula. Three basic rules (det I = 1, a row exchange flips the sign, linearity in each row) lead to det AB = (det A)(det B) and to Cramer's Rule. Geometrically, |det E| is the volume of the box whose edges are the columns of E. If det A = 0, the columns are dependent and A is not invertible.

**Prerequisites:** elimination and PA = LU; permutation matrices; orthogonal matrices ($Q^{\mathsf T}Q=I$); the names QR and SVD; matrix inverse; linear independence.

## L2 — Key ideas
- det A = 0 signals dependent columns and no inverse. A nonzero det A is the number you divide by in the formula for $A^{-1}$ (p. 198).
- Row exchange flips the sign of det. det is linear in each row separately. These rules drive everything else (pp. 199, 206).
- The cofactor $C_{ij}$ collects all terms of det A that multiply $a_{ij}$. This gives $\det A=a_{i1}C_{i1}+\dots+a_{in}C_{in}$ and $A^{-1}=C^{\mathsf T}/\det A$ (pp. 201–202).
- For the −1, 2, −1 matrix, cofactors give $\det A_n=2\det A_{n-1}-\det A_{n-2}$, and $\det A_n=n+1$ for every n fits it (p. 203).
- Elimination steps without row exchanges leave det unchanged, so det A = product of the pivots; row exchanges add only the sign ±1 from det P. Computers find determinants this way (pp. 205–206).
- det AB = (det A)(det B) is proved (assuming det B ≠ 0) by showing that det AB / det B obeys the three basic rules (p. 206).
- If det A ≠ 0, Cramer's Rule gives $x_j=\det B_j/\det A$. It is explicit but needs (n+1)! terms by the big formula (p. 207).
- The big formula sums n! terms, one per permutation, each with sign det P (p. 208).
- Volume of the box with edge matrix E is |det E|. Proof: write E = QR; Q preserves volume and |det R| is the product of the diagonal heights (p. 213).

## L3 — Walkthrough
Equation numbers restart in each section; they are the author's.

### Chapter opening (p. 198)
- det A = 0 signals dependent columns and a singular A. If det A ≠ 0, the formula for $A^{-1}$ divides by it (p. 198).
- Three formulas: the product of pivots of U in PA = LU (det P = ±1, det L = 1); cofactors of size n−1; and the big formula with n! terms, one per "path" (one entry from each row and column), with the sign reversed for odd permutations (p. 198).
- Geometry: a matrix sends a cube to a tilted box, a circle to an ellipse, a sphere to an ellipsoid. The ratio output volume / input volume is always |det A| (p. 198).

### 5.1 3 by 3 Determinants and Cofactors
**2 by 2.** det [[a,b],[c,d]] = ad − bc; the singular matrix [[a,2a],[c,2c]] has det 0. Exchanging rows gives det PA = bc − ad = −det A (p. 199). For 2 by 2, det A = 0 means a/c = b/d, so the columns are parallel. For n by n, det A = 0 means Ax = 0 for some x ≠ 0 (p. 199).

**Sign rule.** The six 3 by 3 permutation matrices have det +1, −1, +1, −1, +1, −1. Each row exchange reverses the sign (p. 199). Multiplying a row by a number multiplies det by that number. det is linear in each row separately (p. 200).

**Big formula for 3 by 3.** For rows $(a,b,c)$, $(p,q,r)$, $(x,y,z)$, linearity splits det into six terms, each with one entry per row and column (p. 200):
$$\det A = +aqz+brx+cpy-ary-bpz-cqx \tag{1}$$
A 3 by 3 matrix has 3! = 6 terms; a 4 by 4 has 4! = 24 (p. 200).

**−1, 2, −1 matrices.** $A_1=[2]$, $A_2=\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$, $A_3=\begin{bmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{bmatrix}$. Then det = 2, 4 − 1 = 3, and 8 − 2 − 2 = 4 (p. 200). The six terms of det $A_3$ are 8 (the diagonal), then −2, −2, 0, 0, 0 (p. 200). A zero entry kills every term containing it, so many zeros make det easy (p. 200).

**4 by 4.** $\det A_4 = 2\det A_3-(-1)\det\begin{bmatrix}-1&-1&0\\0&2&-1\\0&-1&2\end{bmatrix}$ (equation (2)). The first 3 by 3 is $A_3$ (det 4). The second uses columns 1, 3, 4 and has det −3 (author says "please check this"). So det $A_4$ = 8 − 3 = 5 (p. 201). The extra minus sign appears because position (1,2) has 1 + 2 odd; the pattern is already visible in 2 by 2: det = a·d − b·c (equation (3), p. 201). The determinants of $A_1,\dots,A_4$ are 2, 3, 4, 5. The author guesses det $A_5$ = 6 = 2(5) − 4 (p. 201).

**Cofactors.** For 3 by 3 the idea is to reduce to 2 by 2 (p. 201):
$$\det A=a(qz-ry)+b(rx-pz)+c(py-qx) \tag{4}$$
The cofactor of b is rx − pz, the negative of the plain 2 by 2 determinant pz − rx, because 1 + 2 is odd (p. 201).

**Definition.** For $C_{ij}$, remove row i and column j; $C_{ij}=(-1)^{i+j}$ times the determinant of the remaining (n−1) by (n−1) matrix. The cofactor formula along row i is
$$\det A=a_{i1}C_{i1}+\cdots+a_{in}C_{in} \tag{5}$$
Key point: $C_{ij}$ collects all terms of det A multiplied by $a_{ij}$ (p. 202).

**Inverse formula.** For $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$, $C=\begin{bmatrix}d&-c\\-b&a\end{bmatrix}$. Multiplying by $C^{\mathsf T}$ (not C):
$$AC^{\mathsf T}=\begin{bmatrix}ad-bc&0\\0&ad-bc\end{bmatrix}=(\det A)I \tag{6}$$
$$A^{-1}=C^{\mathsf T}/\det A \tag{7}$$
Each entry of $A^{-1}$ is a ratio of two determinants (size n−1 over size n). The matrix $C^{\mathsf T}$ is the adjugate (p. 202).
Example (8): $A=\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix}$ has det 1, and $A^{-1}=\begin{bmatrix}1&-1&0\\0&1&-1\\0&0&1\end{bmatrix}=C^{\mathsf T}$. $C_{32}$ removes row 3 and column 2, leaving a 2 by 2 matrix of det 1. With $(-1)^{2+3}=-1$ this gives −1 in row 2, column 3 of $C^{\mathsf T}$. $C_{31}$ leaves a 2 by 2 matrix of 1's with det 0, which is the 1,3 zero of $A^{-1}$ (p. 202). For 2A the det is multiplied by 8 and each cofactor by 4, so $(2A)^{-1}=4C^{\mathsf T}/(8\det A)=A^{-1}/2$ (p. 202).
The diagonal entries of $AC^{\mathsf T}$ equal det A by (5). The off-diagonal entries are determinants of matrices with two equal rows, hence zero (Problem 18) (p. 202).

*Intuition note:* Cofactor times matching entry gives det A on the diagonal. Mixing a row with the wrong cofactors repeats a row and gives 0. So $AC^{\mathsf T}$ is a multiple of I, and dividing by det A gives the inverse.

**The −1, 2, −1 matrix by cofactors.** Row 1 has only two nonzeros, so expanding along row 1 gives two cofactors. The first is $2\det A_{n-1}$. The second has the −1 from entry (1,2), the sign $(-1)^{1+2}=-1$, and its own top-left −1: three −1's in all. That last cofactor contains a cofactor of size n−2, namely $A_{n-2}$ (pp. 202–203):
$$\det A_n=2\det A_{n-1}-\det A_{n-2} \tag{9}$$
The values 2, 3, 4, 5 fit (e.g. 5 = 2(4) − 3). The author states that $\det A_n=n+1$ for every n; this fits (9) because $n+1=2(n)-(n-1)$ (p. 203). Cofactors are most useful when the matrix is mostly zeros; for dense matrices elimination is better (p. 203).

### 5.2 Computing and Using Determinants
**Facts.** Triangular or diagonal: det is the product of the diagonal entries (equation (1), p. 205). det(Aᵀ) = det A (2). det(AB) = (det A)(det B) (3) (p. 205). Adding matrices does not add determinants: det(I + I) = 2ⁿ, not 2 (p. 205). For orthogonal Q, $(\det Q)^2=(\det Q^{\mathsf T})(\det Q)=1$, so det Q = ±1 (p. 205). If A = LU then det A = (det L)(det U) = det U. With row exchanges, det P = ±1. So an invertible matrix has det A = ± product of the pivots (4) (p. 205). Elimination costs n³/3 multiplications and is how computers find determinants (p. 205). A singular matrix has det 0; later, eigenvalues satisfy det(A − λI) = 0 (p. 205).

**Proving the properties.** Three basic properties (p. 206):
1. det I = 1.
2. Exchanging two rows reverses det A to −det A.
3. If row 1 is cv + dw, then det splits: $\det[cv+dw;\ \text{row }2;\dots]=c\det[v;\dots]+d\det[w;\dots]$ (5).

Consequences (p. 206):
- Property 2 combined with linearity in row 1 (property 3) gives linearity in every row separately: exchange rows, apply the rule, exchange back, so nothing is special about row 1.
- Two equal rows give det A = −det A, so det A = 0.
- Subtracting d times row i from row j leaves det A unchanged. By linearity the new matrix gives det A − d·det(matrix with two equal rows) = det A (6).
- So elimination without row exchanges gives
$$\det A=\det U=U_{11}U_{22}\cdots U_{nn}=\text{product of the pivots} \tag{7}$$

**Proof of det AB = (det A)(det B)** (p. 206). Assume det B ≠ 0. Define $D(A)=\det AB/\det B$. It satisfies the three properties:
1. D(I) = det B / det B = 1.
2. Exchanging rows of A exchanges rows of AB, so D changes sign.
3. If row 1 of A is v + w, row 1 of AB is vB + wB, and (5) splits det(AB). Scaling row 1 by c scales D by c.

Hence, by the author's argument, D(A) = det A, so det AB = (det A)(det B).

*Intuition note:* The three rules lead to the determinant (p. 198). Since det AB / det B obeys these three rules (assuming det B ≠ 0), the author concludes it must be det A.

**Cramer's Rule** (pp. 207–208). Let $M_1$ be I with first column replaced by x. It is triangular with det $x_1$. Then $AM_1=B_1$, where $B_1$ is A with column 1 replaced by b. Taking determinants:
$$(\det A)(x_1)=\det B_1,\quad x_1=\det B_1/\det A \tag{9}$$
Likewise $x_2=\det B_2/\det A$ (10). In general, if det A ≠ 0, then $x_j=\det B_j/\det A$, where $B_j$ is A with column j replaced by b (11) (p. 207).
Example 1: $3x_1+4x_2=2$, $5x_1+6x_2=4$. det A = −2, det $B_1$ = −4, det $B_2$ = 2. So $x_1=2$, $x_2=-1$; the check gives (2, 4) (p. 207).
Cost: n + 1 determinants of n! terms each, (n+1)! terms in all. The author calls this "crazy" for numbers but explicit (p. 207).
Example 2: solve $A[x\ y]=I$ for n = 2. The four determinants are d, −c, −b, a, which are the cofactors. So $A^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$ (p. 208). For n = 3, the determinant of $B_j$ with b = (1,0,0) is a cofactor, with the correct sign. This gives
$$(A^{-1})_{ij}=\frac{C_{ji}}{\det A},\qquad A^{-1}=\frac{C^{\mathsf T}}{\det A} \tag{12}$$

**The big formula** (p. 208). Each n by n permutation matrix P (one 1 in each row and column) gives a term $D_P=a_{1\alpha}a_{2\beta}\cdots a_{n\omega}\cdot\det P$, which accounts for even or odd permutations.
$$\det A=\sum_P D_P\ (n!\text{ terms}) \tag{13}$$
For n = 2 this is ad − bc; for n = 3 it is the six terms of (1). The author says the big formula is "not so great" because it has all n! terms (p. 208), and "very slow if n > 3" (p. 205).

### 5.3 Areas and Volumes by Determinants
**2D.** A parallelogram with sides $e_1=(a,b)$, $e_2=(c,d)$ from (0,0) has fourth corner (a+c, b+d). Base × height needs square roots, but the area has none (p. 211):
$$\text{Area}=|\det E|=\left|\det\begin{bmatrix}a&c\\b&d\end{bmatrix}\right|=|ad-bc| \tag{1}$$
The absolute value avoids negative area (p. 211). The guess for a tilted 3D box is $|\det|$ of the 3 by 3 matrix of edges, equation (2) (p. 212).

**Geometric proof in 2D (Figure 5.1)** (p. 212). Put the parallelogram inside a rectangle of size (a+c) by (b+d). Subtract six pieces: two triangles of area ab/2, two of area cd/2, and two rectangles of area bc. This gives (a+c)(b+d) − 2bc − ab − cd = ad − bc. The author believes a similar construction could work in 3D but says it "doesn't look easy" and that there is a much better way, linear algebra (p. 212).

**Linear algebra proof** (pp. 212–213). The box in n dimensions has n edges $e_1,\dots,e_n$, the columns of the n by n edge matrix E. The goal is to prove volume = |det E|. Three factorizations: E = LU, E = QR, E = UΣVᵀ (SVD). Using det L = 1, |det Q| = 1, and the product rule, (3) gives
$$\text{Box volume}=|\det E|=|\det U|=|\det R|=|\det\Sigma| \tag{3}$$
- An orthogonal Q preserves $x^{\mathsf T}x$ and $x^{\mathsf T}y$, as $(Qx)^{\mathsf T}(Qx)$ and $(Qx)^{\mathsf T}(Qy)$. So lengths, angles and volumes are unchanged. For curved regions, use many small cubes plus thin pieces whose total volume can approach zero (p. 213).
- So the boxes for R and for E = QR have the same volume (p. 213).
- R is triangular. In 2D, $R=\begin{bmatrix}u&v\\0&w\end{bmatrix}$ has base u and height w, so |area| = |uw| = |det R|. In general the diagonal of R gives the height in each new dimension; their product is the volume and also det R (p. 213).
- Since |det Q| = 1, |det E| = |det R|. The author concludes the volume formula is proved in all dimensions (p. 213).

**SVD comment** (pp. 213–214). |det E| = |det Σ|, and Σ is diagonal, giving a rectangular box. But Σ gives the axes of an ellipse, not the sides of a rectangular box. For boxes, E = QR leads directly to volume = |det R|, with u, w as base and height (p. 214). "Every shape has the growth factor det E when all points are multiplied by E" (p. 214).

*Intuition note:* Q only rotates the box (the text: lengths, angles and volumes "are not changed by rotations Q"), so it cannot change volume. What is left is R, a staircase whose diagonal entries are the successive heights. A volume is a product of heights, which is the determinant of a triangular matrix.

## Toy example (ours)
Take $A=\begin{bmatrix}2&1\\4&3\end{bmatrix}$.
- **det three ways:** ad − bc = 2·3 − 1·4 = 2. Pivots: 2, then 3 − (4/2)·1 = 1; product 2 ✓.
- **Cofactors:** $C=\begin{bmatrix}3&-4\\-1&2\end{bmatrix}$, so $C^{\mathsf T}=\begin{bmatrix}3&-1\\-4&2\end{bmatrix}$. $AC^{\mathsf T}$: entries 2·3+1·(−4)=2, 2·(−1)+1·2=0, 4·3+3·(−4)=0, 4·(−1)+3·2=2. This is 2I ✓. So $A^{-1}=C^{\mathsf T}/2=\begin{bmatrix}1.5&-0.5\\-2&1\end{bmatrix}$.
- **Cramer:** b = (4, 10). $B_1=\begin{bmatrix}4&1\\10&3\end{bmatrix}$, det = 12 − 10 = 2, so $x_1=2/2=1$. $B_2=\begin{bmatrix}2&4\\4&10\end{bmatrix}$, det = 20 − 16 = 4, so $x_2=2$. Check: 2·1+1·2 = 4 ✓, 4·1+3·2 = 10 ✓.
- **Area:** the parallelogram with edges (2,4) and (1,3) has area |det A| = 2.
- **QR volume:** $E=\begin{bmatrix}3&0\\4&5\end{bmatrix}$ has det 15. $q_1=(3,4)/5$, so $R_{11}=5$. $R_{12}=(0,5)\cdot q_1=4$. Remainder (0,5) − 4(3/5, 4/5) = (−12/5, 9/5), with length $\sqrt{144/25+81/25}=3=R_{22}$. det R = 5·3 = 15 = |det E| ✓.

## Concepts
- [[determinant]] — one number per square matrix; zero signals dependent columns; |det| is the volume of the edge box (pp. 198, 211)
- [[inverse matrix]] — exists when det ≠ 0; $A^{-1}=C^{\mathsf T}/\det A$ (p. 202)
- [[cofactor]] (new) — $C_{ij}=(-1)^{i+j}\det$ of A with row i and column j removed (p. 201)
- [[cofactor-formula]] (new) — $\det A=\sum_j a_{ij}C_{ij}$ along row i (p. 201)
- [[big-formula-determinant]] (new) — sum over all n! permutations of products times det P (p. 208)
- [[pivot-formula-determinant]] (new) — det A = ± product of pivots, from PA = LU (pp. 205–206)
- [[determinant-defining-properties]] (new) — det I = 1; row exchange flips sign; linear in each row (p. 206)
- [[cramers-rule]] (new) — $x_j=\det B_j/\det A$ (p. 207)
- [[orthogonal matrix]] — QᵀQ = I; det Q = ±1; preserves lengths, angles, volume (pp. 205, 213)
- [[Gram–Schmidt and QR]] — E = QR; |det E| = |det R| = product of heights (p. 213)
- [[singular value decomposition (SVD)]] — E = UΣVᵀ; |det E| = |det Σ| (p. 213)

## Canonical instances
- [[tridiagonal-minus1-2-minus1-matrix]] (new) — det $A_n=n+1$ via recurrence $\det A_n=2\det A_{n-1}-\det A_{n-2}$ (pp. 200–203)
- [[parallelogram-in-rectangle-figure]] (new) — Figure 5.1: area ad − bc as rectangle minus six pieces (p. 212)
- [[upper-triangular-ones-inverse]] (new) — inverse of the upper triangular matrix of ones equals $C^{\mathsf T}$ (p. 202)
- [[cramers-rule-2x2-example]] (new) — $3x_1+4x_2=2$, $5x_1+6x_2=4$ gives (2, −1) (p. 207)

## Bridges (candidates)
- [same-math] det(A − λI) = 0 (p. 205) ↔ linear-algebra: characteristic polynomial, whose roots are eigenvalues.
- [structural-analogy] $\det A_n=2\det A_{n-1}-\det A_{n-2}$ ↔ second-order linear recurrences: the same pattern of "each term from the two before".
- [structural-analogy] |det A| as volume scaling (p. 198) ↔ SVD: product of singular values (the text says |det E| = |det Σ|).
- [metaphor] Cramer's Rule: explicit but slow ↔ closed-form solutions versus numerical algorithms.

## Questions this raises
- Why are the three basic rules enough to determine det uniquely for every n? (The text asserts it but does not prove it.)
- Why does the pivot formula work in practice but the big formula not? What counts as "cost"?
- How do the singular values in Σ relate to the ellipse axes, given that |det E| = |det Σ|? (Promised for Chapter 7, p. 214.)
- What does the sign of det E mean geometrically, since volume uses only |det E|?

## Exercises worth doing
- Ex. 5.1-5 (p. 203) — count row exchanges for the reverse identity $J_n$; predict the sign of det $J_{101}$ — medium
- Ex. 5.1-18 (p. 204) — why equal rows give det 0, and why $AC^{\mathsf T}$ has zero off-diagonals — medium
- Ex. 5.1-19 (p. 204) — det C = (det A)ⁿ⁻¹ from $AC^{\mathsf T}=(\det A)I$ — medium
- Ex. 5.2-8 (p. 209) — quick proof of Cramer's Rule by column linearity — medium
- Ex. 5.2-10 (p. 210) — $E_n=E_{n-1}-E_{n-2}$ for the 1,1,1 tridiagonal matrix; find $E_{100}$ — medium
- Ex. 5.3-4 (p. 214) — |det E| ≤ product of column lengths, using E = QR — hard

## Reading notes
- Printed page = pdf page − 10 (e.g. pdf 208 = printed 198).
- The text layer is heavily garbled on equations (tables of six permutations, determinants, Cramer's Rule). I checked these against the page images.
- On p. 213 the letter U is used for the upper triangular factor in E = LU and for an orthogonal factor in E = UΣVᵀ. The text "det L = |det Q| = |det U| = |det V| = 1" mixes these. In equation (3), |det U| refers to the triangular U.
- The p. 198 intro says the volume ratio is |det A|; p. 214 says the growth factor is "det E". I report both as printed.
- The geometric proof that Q preserves volume of curved regions is only sketched (p. 213). I report it as the author's sketch.
- The problem sets (pp. 203–204, 209–210, 214–215) are listed, not solved.
