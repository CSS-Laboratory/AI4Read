---
id: strang-2023-introduction/ch06-eigenvalues-p1
work: strang-2023-introduction
unit: "6 Eigenvalues and Eigenvectors (part 1/3): chapter opener and Section 6.1, Introduction to Eigenvalues"
pages: 216-231
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Introduction to Eigenvalues: Ax = λx

## L0 — One line
An eigenvector is a special direction that a square matrix only stretches, shrinks or flips; its eigenvalues are the roots of det(A − λI) = 0, and they make powers of A easy.

## L1 — The gist (≤ 120 words)
Most vectors change direction when multiplied by A. Some exceptional vectors x do not: Ax = λx. The question is how to find these x and λ, and what they say about A. The answer is to solve det(A − λI) = 0 for the n eigenvalues, then solve (A − λI)x = 0 for each eigenvector. The eigenvalues multiply to det A and add to the trace (the sum of the diagonal entries). A vector written as a sum of eigenvectors evolves by powers λⁿ, so A¹⁰⁰ needs no 100 multiplications. Real matrices can have complex eigenvalues (rotations). Eigenvalues of AB or A + B are generally not products or sums of eigenvalues.

**Prerequisites:** 2 by 2 and 3 by 3 determinants; nullspace; singular vs. invertible matrix; matrix multiplication; complex number i with i² = −1 (basic).

## L2 — Key ideas (5–10 bullets)
- Eigenvectors satisfy Ax = λx, x ≠ 0. Then Aⁿx = λⁿx, and A⁻¹x = x/λ if λ ≠ 0 (p. 217).
- λ is an eigenvalue if and only if A − λI is singular. So det(A − λI) = 0 gives the n eigenvalues, and the eigenvectors make up the nullspace of A − λI (p. 220).
- Writing a vector as a combination of eigenvectors lets each eigenvector "go its own way". This explains the Markov example, where columns of Aᵏ approach the steady state x₁ = (.6, .4), a vector that A does not change (pp. 216–219).
- Product of eigenvalues = det A; sum = trace (the sum of the diagonal entries). These are quick checks (p. 222).
- Projections have λ = 1, 0; the exchange matrix has 1, −1; a 90° rotation has ±i. Real matrices can have complex eigenvalues (pp. 219–223).
- Elimination usually changes eigenvalues. Eigenvalues of AB and A + B are generally not products or sums of eigenvalues (pp. 222–224).
- A and B share n independent eigenvectors if and only if AB = BA. This test is important in quantum mechanics, where the position and momentum matrices do not commute (Heisenberg, p. 224).
- Gershgorin: every eigenvalue lies in a disc centred at some diagonal entry (p. 225).

## L3 — Walkthrough

### Chapter 6 opener (p. 216)
- Eigenvalues and eigenvectors give information about a square matrix that is deeper than its rank or column space. Eigenvectors x do not change direction under A: Ax = λx (p. 216).
- Then A²x = λ²x, A¹⁰⁰x = λ¹⁰⁰x. For a combination, A²(c₁x₁ + c₂x₂) = c₁λ₁²x₁ + c₂λ₂²x₂ (p. 216).
- Eigenvalues are growth factors in Aⁿx = λⁿx. If all |λᵢ| < 1, Aⁿ eventually approaches zero. If any |λᵢ| > 1, Aⁿ eventually grows. If λ = 1, Aⁿx never changes (p. 216).
- Preview: symmetric matrices have perpendicular eigenvectors and real eigenvalues. Symmetric positive definite matrices give a minimum of $f(x)=\tfrac12 x^TSx$. The chapter ends with du/dt = Au, solved by e^{λt}x (p. 216).

### 6.1 Introduction: the summary box and the Markov example (p. 217)
1. If Ax = λx with x ≠ 0, then x is an eigenvector and λ the eigenvalue.
2. Then Aⁿx = λⁿx for every n; (A + cI)x = (λ + c)x; A⁻¹x = x/λ if λ ≠ 0.
3. (A − λI)x = 0 ⇒ det(A − λI) = 0, which produces n values λ.
4. Check: $(\lambda_1)\cdots(\lambda_n)=\det A$ and $\lambda_1+\dots+\lambda_n=a_{11}+\dots+a_{nn}$.
5. Projections have λ = 1, 0. Rotations have $e^{i\theta}, e^{-i\theta}$ (complex).

- Part 1 of the book was Ax = b, a steady state. This part is about change: du/dt = Au or $u_{k+1}=Au_k$. Elimination does not solve these. If u stays in the direction of x, only a number multiplying x changes, which is a one-dimensional problem (p. 217).
- Model: $A=\begin{bmatrix}.8&.3\\.2&.7\end{bmatrix}$, $A^2=\begin{bmatrix}.70&.45\\.30&.55\end{bmatrix}$, $A^3=\begin{bmatrix}.650&.525\\.350&.475\end{bmatrix}$, $A^{100}\approx\begin{bmatrix}.6000&.6000\\.4000&.4000\end{bmatrix}$. A¹⁰⁰ was found from the eigenvalues 1 and 1/2, not by 100 multiplications (p. 217).
- Almost all vectors change direction; the exceptional ones with Ax = λx are eigenvectors. λ says whether x is stretched, shrunk or reversed. λ = 0 means x is in the nullspace. For A = I, all vectors are eigenvectors with λ = 1 (p. 217).

**Example 1** (p. 218). The diagonal sum is .8 + .7 = 1.5 = 3/2. The determinant is (.8)(.7) − (.3)(.2) = .5 = 1/2.
$$\det(A-\lambda I)=\lambda^2-\tfrac32\lambda+\tfrac12=(\lambda-1)\big(\lambda-\tfrac12\big).$$
- So λ₁ = 1 and λ₂ = 1/2. A − I and A − ½I are not invertible, and the eigenvectors are in their nullspaces (p. 218).
- λ₁ = 1: x₁ = (.6, .4), Ax₁ = x₁. λ₂ = 1/2: x₂ = (1, −1), Ax₂ = (.5, −.5) = ½x₂ (p. 218).
- Eigenvectors of A stay eigenvectors of A², with squared eigenvalues. An eigenvector of A is an eigenvector of every Aⁿ, with Aⁿx = λⁿx (p. 218).
- Column 1 separates into eigenvectors: (.8, .2) = (.6, .4) + (.2, −.2) = x₁ + .2x₂ (1) (p. 218).
- Multiplying by A: x₁ + ½(.2)x₂ = (.6, .4) + (.1, −.1) = (.7, .3) (2). This is column 1 of A² (p. 219).
- Column 1 of A¹⁰⁰: $A^{99}(.8,.2)=x_1+(.2)(\tfrac12)^{99}x_2=(.6,.4)+$ very small vector (3). So the printed .6000 was not exact (p. 219).
- x₁ is a "steady state" (λ = 1). x₂ is a "decaying mode" (λ = .5). This A is a Markov matrix with largest eigenvalue 1; all columns of Aᵏ approach x₁. The text says a giant Markov matrix is the key to Google's web search (p. 219).

*Intuition note.* Split the starting vector into eigenvector pieces. Each piece is only multiplied by its own λ at each step. Pieces with |λ| < 1 fade, and the piece with λ = 1 stays.

**Example 2** (p. 219). Projection $P=\begin{bmatrix}.5&.5\\.5&.5\end{bmatrix}$ has λ = 1 and 0. Eigenvectors: x₁ = (1,1) with Px₁ = x₁, and x₂ = (1,−1) with Px₂ = 0.
- P is Markov (columns add to 1, so λ = 1 is an eigenvalue), singular (λ = 0), and symmetric (perpendicular eigenvectors) (p. 219).
- The only eigenvalues of a projection are 0 and 1. Eigenvectors for λ = 0 fill the nullspace; those for λ = 1 fill the column space. Example: $v=(1,-1)+(2,2)=(3,1)$ projects to $Pv=(0,0)+(2,2)$ (p. 219).

**Example 3** (p. 220). Exchange matrix $E=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has λ = 1, −1. Eigenvectors are (1,1) and (1,−1). A matrix with no negative entries can have a negative eigenvalue. Also
$$E=2P-I:\quad \begin{bmatrix}0&1\\1&0\end{bmatrix}=2\begin{bmatrix}.5&.5\\.5&.5\end{bmatrix}-\begin{bmatrix}1&0\\0&1\end{bmatrix}\tag{4}$$
Shifting a matrix by I shifts each λ by 1 and leaves the eigenvectors unchanged (p. 220).

### The equation for the eigenvalues (pp. 220–222)
- Write Ax = λx as (A − λI)x = 0. Eigenvectors make up the nullspace of A − λI (p. 220).
- If (A − λI)x = 0 has a nonzero solution, A − λI is not invertible, so its determinant is zero:
$$\lambda\text{ is an eigenvalue of }A\iff A-\lambda I\text{ is singular};\qquad \det(A-\lambda I)=0.\tag{5}$$
- This "characteristic polynomial" involves only λ, not x. Because λ appears all down the diagonal, the determinant includes $(-\lambda)^n$. So there are n solutions; repeated λ's are possible (pp. 220–221).

**Example 4** (p. 221). $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$ is singular, so λ = 0 is an eigenvalue.
$$A-\lambda I=\begin{bmatrix}1-\lambda&2\\2&4-\lambda\end{bmatrix}\tag{6}$$
$$\det=(1-\lambda)(4-\lambda)-(2)(2)=\lambda^2-5\lambda\tag{7}$$
- Roots: λ₁ = 0, λ₂ = 5.
- λ = 0: (A − 0I)x = 0 gives (2, −1). λ = 5: $\begin{bmatrix}-4&2\\2&-1\end{bmatrix}x=0$ gives (1, 2) (p. 221).
- Zero is nothing special: if A is singular, eigenvectors for λ = 0 fill the nullspace. If A is invertible, zero is not an eigenvalue (p. 221).

**Summary of the method** (p. 221): (1) compute det(A − λI), a polynomial of degree n; (2) its n roots are the eigenvalues; (3) for each λ, solve (A − λI)x = 0.

**2 by 2 note** (p. 222). When A − λI is singular, both rows are multiples of some (a, b), and the eigenvector is any multiple of (b, −a). Here (2, 4) and (1, 2) are both correct. MATLAB's eig makes eigenvectors unit length.
- Some 2 by 2 matrices have only one line of eigenvectors. This can only happen when the two eigenvalues are equal; A = I has equal eigenvalues and plenty of eigenvectors. Without n independent eigenvectors we have no basis of eigenvectors and cannot diagonalize (Section 6.2) (p. 222).

### Determinant and trace (p. 222)
- Bad news: adding a row to another or exchanging rows usually changes eigenvalues. The pivots of U are its eigenvalues but not those of A. Example: $U=\begin{bmatrix}1&3\\0&0\end{bmatrix}$ has λ = 0, 1; $A=\begin{bmatrix}1&3\\2&6\end{bmatrix}$ has λ = 0, 7 (p. 222).
- Good news: the product of the n eigenvalues equals det A; their sum equals the trace. Here 0·7 = 0 = det A and 0 + 7 = 1 + 6. These checks "always work" and usually reveal a wrong computation (proved in Problems 16–17) (p. 222).
- For 2 by 2, trace and determinant tell everything. Trace 3 and det 2 give λ = 1, 2 for each of
$$A=\begin{bmatrix}1&9\\0&2\end{bmatrix}\ \text{or}\ \begin{bmatrix}3&1\\-2&0\end{bmatrix}\ \text{or}\ \begin{bmatrix}7&-3\\10&-4\end{bmatrix}\tag{8}$$
The triangular one shows eigenvalues on the diagonal (p. 222).

*Intuition note.* Setting λ = 0 in det(A − λI) leaves det A, which is why the product of the roots is det A (Problem 16, p. 228). For a 2 by 2 matrix the polynomial is λ² − (a + d)λ + ad − bc, so the sum of the roots is the trace a + d (Problem 17, p. 228).

### Imaginary eigenvalues (p. 223)
**Example 5.** The 90° rotation $Q=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ has no real eigenvectors, because Qx is never in the direction of x ≠ 0. Its eigenvalues are λ₁ = i and λ₂ = −i. Their sum is the trace 0 and their product is det Q = 1 (p. 223).
- Reason: Q² = −I has eigenvalues −1, −1, and squaring Q squares each λ, so λ² = −1. Also det(Q − λI) = 0 gives λ² + 1 = 0 (p. 223).
- Complex eigenvectors: Q(1, i) = −i(1, i) and Q(i, 1) = i(i, 1) (p. 223).
- Q is orthogonal, so |λ| = 1. Q is skew-symmetric, so λ is pure imaginary (p. 223).
- The author compares a symmetric matrix to a real number, a skew-symmetric one to an imaginary number, and an orthogonal one to a complex number with |λ| = 1. He calls these "more than analogies—they are facts to be proved" (p. 223).

### Eigenvalues of AB and A + B (pp. 223–224)
- **False proof:** ABx = Aβx = βAx = βλx. It would make λβ an eigenvalue of AB. It is correct when x is an eigenvector of both A and B. The mistake is to assume A and B share eigenvectors; usually they do not (p. 223).
- Counterexample (p. 224): $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$, $B=\begin{bmatrix}0&0\\1&0\end{bmatrix}$ have all eigenvalues 0. But $AB=\begin{bmatrix}1&0\\0&0\end{bmatrix}$ and $A+B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ have eigenvalue 1; A + B has 1 and −1 (p. 224).
- If x is shared, ABx = λβx = BAx. **A and B share the same n independent eigenvectors if and only if AB = BA** (p. 224).
- **Heisenberg** (p. 224): for the position and momentum matrices, QP − PQ = I (infinite matrices). Px = 0 and Qx = 0 together would force x = Ix = 0, so position and momentum cannot both be known exactly. Problem 36 derives ‖Px‖‖Qx‖ ≥ ½‖x‖² (p. 224).

### Review of key ideas (p. 224)
Eigenvectors keep direction; det(A − λI) = 0 determines n eigenvalues; sum = trace, product = det; projections, exchanges and 90° rotations have λ = 1, 0; −1; i, −i; singular matrices have λ = 0; triangular matrices have their λ's on the diagonal (p. 224).

### Worked examples (pp. 224–226)
**6.1 A** (p. 225). $A=\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$: det(A − λI) = λ² − 4λ + 3 = (λ − 1)(λ − 3). So λ = 1, 3, and the trace is 4 = 1 + 3.
- λ = 1: x₁ = (1, 1). λ = 3: x₂ = (1, −1).
- A², A⁻¹ and A + 4I keep these eigenvectors. Eigenvalues: A² has 1, 9; A⁻¹ has 1, 1/3; A + 4I has 5, 7 (p. 225).

**6.1 B, Gershgorin** (p. 225). Every eigenvalue λ lies in at least one disc $|a_{ii}-\lambda|\le R_i$, where $R_i=\sum_{j\ne i}|a_{ij}|$.
- Reason: A − λI is not invertible, so it cannot be diagonally dominant (Section 2.5). So for some row i, $|a_{ii}-\lambda|$ is not larger than $R_i$ (p. 225).
- For $\begin{bmatrix}a&b\\c&d\end{bmatrix}$: |λ − a| ≤ |b| and |λ − d| ≤ |c|, as discs in the complex plane (p. 225).

**6.1 C** (p. 226). $S=\begin{bmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{bmatrix}$ is symmetric and singular, with trace 4. Rows add to zero, so S(1,1,1) = 0 and λ = 0. Then
$$\det(S-\lambda I)=(1-\lambda)(2-\lambda)(1-\lambda)-2(1-\lambda)=(1-\lambda)[(2-\lambda)(1-\lambda)-2]=(1-\lambda)(-\lambda)(3-\lambda).$$
- λ = 0, 1, 3 with eigenvectors (1,1,1), (1,0,−1), (1,−2,1), which are perpendicular. For larger matrices he would use eig(A) (p. 226).

### Problem Set 6.1 and Eigshow (pp. 226–231)
38 problems, listed under Exercises below. Eigshow (p. 231) is a MATLAB demo. A unit vector x moves around the circle while Ax is shown. At the moments when Ax is parallel to x we have Ax = λx. The built-in choices show 0, 1 or 2 real eigenvector directions (p. 231).

## Toy example (ours)
Take the Markov matrix $A=\begin{bmatrix}.5&.25\\.5&.75\end{bmatrix}$.
- Trace = 1.25, det = .375 − .125 = .25. So λ² − 1.25λ + .25 = (λ − 1)(λ − .25), giving λ = 1, .25. Check: 1 + .25 = 1.25 and 1·.25 = .25.
- λ = 1: A − I = [[−.5, .25],[.5, −.25]] gives x₁ = (1, 2). Check: A(1,2) = (.5 + .5, .5 + 1.5) = (1, 2).
- λ = .25: A − .25I = [[.25, .25],[.5, .5]] gives x₂ = (1, −1). Check: A(1,−1) = (.25, −.25) = .25x₂.
- Start u₀ = (1, 0) = a(1,2) + b(1,−1): a + b = 1 and 2a − b = 0, so a = 1/3, b = 2/3.
- Then Aⁿu₀ = (1/3)(1,2) + (2/3)(.25)ⁿ(1,−1).
- n = 1: (1/3 + 1/6, 2/3 − 1/6) = (.5, .5), which is column 1 of A.
- n = 2: (1/3 + 1/24, 2/3 − 1/24) = (.375, .625). Direct check: A(.5, .5) = (.25 + .125, .25 + .375) = (.375, .625).
- As n grows, the result approaches (1/3, 2/3), the steady state.

## Concepts
- [[eigenvector / eigenvalue]] — x ≠ 0 with Ax = λx; λ is the stretching factor (p. 216, p. 217)
- [[characteristic polynomial]] — det(A − λI), degree n; roots are the eigenvalues (p. 220)
- [[trace-determinant-eigenvalue-checks]] (new) — Πλᵢ = det A, Σλᵢ = trace A (p. 222)
- [[null space (kernel)]] — eigenvectors for λ are the nullspace of A − λI (p. 220)
- [[Markov (stochastic) matrix]] — columns add to 1; λ = 1 with a steady-state eigenvector (p. 219)
- [[projection]] — eigenvalues only 0 and 1; keeps column space, kills nullspace (p. 219)
- [[gershgorin-discs]] (new) — every λ lies within R_i of some diagonal entry a_ii (p. 225)
- [[commuting-matrices-shared-eigenvectors]] (new) — A, B share n independent eigenvectors iff AB = BA (p. 224)
- [[diagonalization]] — previewed only: needs n independent eigenvectors (p. 222)

## Canonical instances
- [[markov-2x2-powers-example]] (new) — A = [[.8,.3],[.2,.7]], λ = 1, ½, steady state (.6, .4) (pp. 217–219)
- [[rotation-90-complex-eigenvalues]] (new) — a real matrix with eigenvalues ±i (p. 223)
- [[exchange-matrix-E]] (new) — E = 2P − I, λ = 1, −1 (p. 220)
- [[heisenberg-uncertainty]] (new) — QP − PQ = I forbids exact position and momentum (p. 224)
- [[eigshow-demo]] (new) — eigenvectors seen as moments when Ax ∥ x (p. 231)

## Bridges (candidates)
- [structural-analogy] Markov steady state (eigenvector for λ = 1) ↔ web search: the text says a giant Markov matrix is the key to Google (p. 219).
- [structural-analogy] Powers λⁿx in difference equations ↔ exponentials e^{λt}x in du/dt = Au (previewed, p. 216).
- [structural-analogy] AB = BA ↔ quantum mechanics: non-commuting position and momentum matrices (p. 224).

## Questions this raises
- When a matrix has repeated eigenvalues, when are there still n independent eigenvectors?
- Why exactly do symmetric matrices have real eigenvalues and perpendicular eigenvectors?
- Can the eigenvalues of AB be related to those of BA (Problem 6)?
- How does the e^{λt} solution of du/dt = Au relate to the λⁿ solution?

## Exercises worth doing
- Ex. 6 (p. 227) — eigenvalues of AB vs. A, B and BA — difficulty: easy
- Ex. 11 (p. 227) — columns of A − λ₁I are multiples of x₂ — difficulty: medium
- Ex. 14 (p. 228) — rotation eigenvalues cos θ ± i sin θ — difficulty: medium
- Ex. 16–17 (p. 228) — proofs of det = product and trace = sum — difficulty: medium
- Ex. 25 (p. 229) — same eigenvalues and independent eigenvectors imply A = B — difficulty: easy
- Ex. 36 (p. 231) — Heisenberg inequality via Schwarz — difficulty: hard

## Reading notes
- This part starts at the chapter opener (printed p. 216) and ends at the end of Section 6.1: Problem Set 6.1 and the Eigshow box (printed p. 231). Section 6.2 is not on these pages.
- Printed = pdf − 10. The text layer is badly garbled in equations; I used the page images.
- Page 220 labels the characteristic equation (5); the matrices in (8), Example 4 and Problem 31 were read from the images.
- Several problems (e.g. 2, 7, 8) have blanks to fill in; I do not solve them.
