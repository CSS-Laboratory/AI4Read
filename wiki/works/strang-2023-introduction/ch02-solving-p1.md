---
id: strang-2023-introduction/ch02-solving-p1
work: strang-2023-introduction
unit: "2 Solving Linear Equations Ax = b (part 1/2): chapter opener, 2.1 Elimination and Back Substitution, 2.2 Elimination Matrices and Inverse Matrices, 2.3 Matrix Computations and A = LU"
pages: 39-63
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
# Elimination, Inverses and A = LU (Strang, Ch. 2, part 1)

## L0 — One line
Elimination turns Ax = b into a triangular system Ux = c that back substitution solves, and recording the steps gives A = LU, with the multipliers sitting in L.

## L1 — The gist (≤ 120 words)
How can we solve n equations in n unknowns systematically, and tell whether a solution exists? Elimination subtracts multiples of pivot rows (the pivot is the diagonal entry that clears its column) from lower rows until the matrix is upper triangular (U); back substitution then finds x from the bottom up. Nonzero pivots (after row exchanges if needed) signal independent columns. A missing pivot signals dependent columns. In matrix form EA = U, and inverting the steps gives A = LU, where L stores the multipliers. Forming U costs about n³/3 multiplications. Each extra right side costs n². This matters because elimination is the practical way to solve Ax = b, and the inverse is rarely computed.

**Prerequisites:** matrix–vector multiplication; row and column pictures of Ax = b; linear independence; matrix multiplication (including columns-times-rows); a little summation.

## L2 — Key ideas (5–10 bullets)
- Ax = b has no solution, exactly one, or infinitely many. Elimination decides which, without changing the solution set (pp. 40–41).
- Elimination makes zeros below each pivot to reach an upper triangular U. Back substitution then solves Ux = c from the bottom up, dividing by the pivots (pp. 41–42).
- A zero where a pivot is needed may be fixed by a row exchange. If no pivot is available, the columns are dependent and the matrix is singular, meaning it has no inverse (pp. 43–45).
- Each elimination step is a matrix E_ij, so EA = U. Its inverse adds back what E subtracted (pp. 49, 52).
- A square matrix is invertible exactly when its columns are independent. Equivalently elimination gives n pivots, and for 2 by 2, ad − bc ≠ 0. (AB)⁻¹ = B⁻¹A⁻¹ in reverse order (pp. 50–52).
- E⁻¹ = L is clean: the multipliers ℓ_ij (the numbers by which pivot rows are multiplied before subtracting) drop into place below the diagonal of 1's, while E itself is messy (pp. 52–53).
- Cost: about n³/3 multiplications to reach U, but only n² per right side. Gauss–Jordan inversion is slower than solving Ax = b (pp. 57–58).
- A = LU is proved two ways: pivot rows are rows of U, or A is a sum of column-times-row rank-one pieces ℓ_k u_k. Without row exchanges all upper-left corners must be invertible (pp. 59–61).

## L3 — Walkthrough

### Chapter opener (p. 39)
- The matrices here are square, n by n. Ax = b gives n equations in n unknowns. Often but not always there is one solution for each b. Then A has an inverse, and x = A⁻¹b symbolically (p. 39).
- The aim is to find x **without computing A⁻¹** (that would solve for every b). We go column by column, assuming independent columns, and stop only if this proves wrong. Ax = b becomes a triangular system Ux = c (p. 39).
- Elimination is described as an idea going back thousands of years to China. Each step puts a zero in the matrix. Row exchanges may be needed (p. 39).
- Plan: A → EA = U → A = E⁻¹U = LU → x. Strang says elimination adds up to the greatest cost in all of scientific computing, and that "we don't know a better way to solve Ax = b" (p. 39). Section 2.5 is not in this part.

### 2.1 Elimination and Back Substitution (pp. 40–45)
**Three possibilities (n = 2), p. 40.** Our job is to decide among them and find all solutions.
1. *Exactly one solution.* A has independent columns and rank 2. Ax = 0 only for x = 0, and A⁻¹ exists. Example: 2x+3y = 5, 4x+2y = 6, with solution (1,1).
2. *No solution.* b is not in the column space. The rank is 1. Example: 2x+3y = 6, 4x+6y = 15. Subtracting 2 times equation 1 from equation 2 gives 0 = 3.
3. *Infinitely many solutions to AX = 0* when the columns are dependent. If x solves Ax = b, then for any number α:

$$A(x+\alpha X)=Ax+\alpha AX=b+0=b \tag{1}$$

Example: 2x+3y = 6, 4x+6y = 12. A particular solution is x = (0,2), and X = (3,−2) solves AX = 0. So $x+\alpha X=(3\alpha,\,2-2\alpha)$ is a line of solutions (p. 40).

**Back substitution (p. 41).** Elimination does the same reversible operations to both sides. It keeps all solutions and creates no new ones. Take

$$Ux=c:\quad \begin{bmatrix}2&3&4\\0&5&6\\0&0&7\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}19\\17\\14\end{bmatrix}.$$

- Last equation: $7x_3=14$, so $x_3=2$.
- Next: $5x_2+6(2)=17$, so $x_2=1$.
- First: $2x_1+3(1)+4(2)=19$, so $x_1=4$. The only solution is $x=(4,1,2)$.
- We divide by the **pivots** 2, 5, 7 (the diagonal entries of U). A zero pivot would give an equation like $0x_3=8$, which has no solution. The test for independent columns is n nonzero pivots in U, after possible row exchanges (p. 41).

> Intuition note: Triangular systems are easy because the last equation has one unknown, the one above has two, and so on. Elimination changes the problem, not the answer, so solving Ux = c solves Ax = b.

**Elimination column by column (p. 42).** Take

$$A=\begin{bmatrix}2&3&4\\4&11&14\\2&8&17\end{bmatrix},\quad b=\begin{bmatrix}19\\55\\50\end{bmatrix}. \tag{2}$$

- $E_{21}$ subtracts 2 times row 1 from row 2. It gives row 2 = (0,5,6) and $E_{21}b=(19,17,50)$ (eq. 3).
- $E_{31}$ subtracts 1 times row 1 from row 3. It gives row 3 = (0,5,13) and right side (19,17,31) (eq. 4).
- $E_{32}$ subtracts 1 times row 2 from row 3. It gives $U=\begin{bmatrix}2&3&4\\0&5&6\\0&0&7\end{bmatrix}$ and $c=(19,17,14)$ (eq. 5).
- So $E_{32}E_{31}E_{21}A=U$, and $x=(4,1,2)$ solves both $Ux=c$ and $Ax=b$. A and U have full rank. Recipe: clear column 1 below the first pivot, then column 2 below pivot 2, and so on. The same steps are applied to b (p. 42).

**Possible breakdown (pp. 43–44).**
- $A=\begin{bmatrix}2&3&4\\4&6&14\\2&8&17\end{bmatrix}$ becomes $B=\begin{bmatrix}2&3&4\\0&0&6\\0&5&13\end{bmatrix}$. A zero sits in pivot position 2.
- The cure, if it works, is to exchange rows 2 and 3 by a permutation matrix P. Then $PB=\begin{bmatrix}2&3&4\\0&5&13\\0&0&6\end{bmatrix}$ with pivots 2, 5, 6.
- A slightly different $A^*=\begin{bmatrix}2&3&4\\4&6&14\\2&3&17\end{bmatrix}$ gives $U^*=\begin{bmatrix}2&3&4\\0&0&6\\0&0&13\end{bmatrix}$ (eq. 6). There is no second pivot, so $A^*$ lacks full rank.
- Column 2 is 3/2 times column 1, and $X=(3,-2,0)$ solves $A^*X=0$. Whether $A^*x=b$ is solvable depends on b: "probably not" (p. 43).
- Author's statement: a triangular matrix U has full rank exactly when its main diagonal has no zeros. Then its columns, and its rows, are independent (p. 43).
- For a 4 by 4 upper triangular $U^*$ with one zero on the diagonal, the matrix is singular (no inverse) (p. 44).

> Intuition note: A missing pivot is how elimination exposes dependent columns. The failure is informative: it says the system is singular.

**Row and column pictures (p. 44).**
- Row picture: each equation is a line (in 3D, a plane). Parallel lines (x−2y = −1 and x−2y = 1) mean no solution. One line twice means a line of solutions. Lines x−2y = −1 and x+y = 2 meet at (1,1).
- Column picture: combine the columns of A to produce b. With $A=\begin{bmatrix}1&-2\\1&1\end{bmatrix}$, column 1 + column 2 = b = (−1,2), so $x=(1,1)$.
- When the n columns are independent, the column space contains every b in $\mathbb R^n$, and exactly one combination Ax equals b. Elimination finds it (p. 44).

**Examples (p. 45).**
- $A=\begin{bmatrix}2&4&-2\\4&9&-3\\-2&-3&7\end{bmatrix}$ goes by $E_{21}$ (multiplier 2), $E_{31}$ (−1) and $E_{32}$ (1) to $U=\begin{bmatrix}2&4&-2\\0&1&1\\0&0&4\end{bmatrix}$.
- For $b=(2,8,10)$ the same steps give $c=(2,4,8)$.
- The **augmented matrix** $[A\;\,b]$ carries b along as an extra column and becomes $[U\;\,c]$ (eq. 7).
- A case needing a row exchange is $A=\begin{bmatrix}1&1&1\\2&2&3\\0&4&5\end{bmatrix}$. After $E$ the second row is (0,0,1). $P_{23}$ then swaps rows 2 and 3, giving $U=\begin{bmatrix}1&1&1\\0&4&5\\0&0&1\end{bmatrix}$.
- With exchanges the final form is PA = LU, with $L=E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}$. Often no permutation is needed and A = LU. There are n! permutation matrices (p. 45).

Problem Set 2.1 (pp. 46–48): 26 problems on 2 by 2 and 3 by 3 elimination, breakdown, row and column pictures, and MATLAB commands.

### 2.2 Elimination Matrices and Inverse Matrices (pp. 49–53)
**Elimination matrices (p. 49).** The step "subtract $\ell_{ij}$ times equation j from equation i" is the matrix $E_{ij}$. It is I with $-\ell_{ij}$ in position (i,j). Example: $E_{31}=\begin{bmatrix}1&0&0\\0&1&0\\-2&0&1\end{bmatrix}$ subtracts 2 times row 1 from row 3. With no exchanges,

$$E=E_{32}E_{31}E_{21},\qquad EA=U\ \text{upper triangular.}\tag{1}$$

- $\ell_{32}$ is computed from the *new* row 2, after $\ell_{21},\ell_{31}$ were applied (p. 49).
- Example 1: $A=\begin{bmatrix}3&1&0\\-3&1&1\\6&8&4\end{bmatrix}$. $E_{21}$ (multiplier −1) then $E_{31}$ (multiplier 2) give $\begin{bmatrix}3&1&0\\0&2&1\\0&6&4\end{bmatrix}$ (eq. 2).
- $E_{32}$ subtracts $\ell_{32}=3$ times the new row 2. The result is $U=\begin{bmatrix}3&1&0\\0&2&1\\0&0&1\end{bmatrix}$ (eq. 3). The pivots are 3, 2, 1.
- The inverse of $E_{ij}$ adds back $\ell_{ij}$(row j) to row i (p. 49).

**Facts about inverses (pp. 50–51).** An inverse undoes A, so $A^{-1}Ax=x$. It might not exist.

*Definition (two-sided inverse):* A is invertible if some matrix $A^{-1}$ has

$$A^{-1}A=I\ \text{ and }\ AA^{-1}=I.\tag{4}$$

- **Note 1.** The inverse exists if and only if elimination produces n pivots (row exchanges allowed).
- **Note 2.** There cannot be two different inverses. If BA = I and AC = I, then B(AC) = (BA)C gives BI = IC, so B = C (eq. 5). A left inverse and a right inverse are the same matrix.
- **Note 3.** If A is invertible, the one and only solution of Ax = b is $x=A^{-1}b$.
- **Note 4 (important).** If a nonzero x has Ax = 0, then A has dependent columns and no inverse. If A is invertible, Ax = 0 only has x = 0.
- **Note 5.** A square matrix is invertible if and only if its columns are independent.
- **Note 6.** A 2 by 2 matrix is invertible if and only if ad − bc ≠ 0:

$$\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1}=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}\tag{6}$$

ad − bc is the determinant. The author says a matrix is invertible if its determinant is not zero (Chapter 5), but the test for n pivots usually comes first.
- **Note 7.** A triangular matrix has an inverse provided no diagonal entry $d_i$ is zero. Its inverse is triangular with diagonal entries $1/d_i$.

Example 2: $\begin{bmatrix}1&2\\1&2\end{bmatrix}$ fails Note 6 (ad = bc) and Note 4 (Ax = 0 for x = (2,−1)). It also fails Note 1: row 2 becomes zero, so there is no second pivot (p. 51).

Example 3 (order A, B, C, D, S, T; p. 51):
- A = [[4,3],[8,6]], B = [[4,3],[8,7]], C = [[6,6],[6,0]], D = [[6,6],[6,6]].
- S = [[1,0,0],[1,1,0],[1,1,1]], T = [[1,1,1],[1,1,0],[1,1,1]].
- B, C, S are invertible: $B^{-1}=\tfrac14\begin{bmatrix}7&-3\\-8&4\end{bmatrix}$, $C^{-1}=\tfrac1{36}\begin{bmatrix}0&6\\6&-6\end{bmatrix}$, $S^{-1}=\begin{bmatrix}1&0&0\\-1&1&0\\0&-1&1\end{bmatrix}$.
- A has determinant 4·6 − 3·8 = 0. D has one pivot. T has two equal rows, and Tx = 0 for x = (−1,1,0).

**Inverse of a product (pp. 51–52).** If A and B are invertible (same size), AB is invertible with

$$(AB)^{-1}=B^{-1}A^{-1},\qquad (AB)(B^{-1}A^{-1})=AIA^{-1}=AA^{-1}=I.\tag{7}$$

By the author's statement AB has an inverse if and only if A and B are separately invertible (and the same size). For three factors, $(ABC)^{-1}=C^{-1}B^{-1}A^{-1}$ (eq. 8). The author's common-sense picture is socks then shoes: you take off the shoes first (p. 52). A sum a + b of invertible numbers may fail to be invertible (3 + (−3) = 0), but the product is fine (p. 51).

Example 4 (p. 52): E subtracts 5 times row 1 from row 2, and $E^{-1}$ adds it. $EE^{-1}=E^{-1}E=I$. For square matrices, an inverse on one side is automatically an inverse on the other.

Example 5 (p. 52): F subtracts 4 times row 2 from row 3, and $F^{-1}$ adds it back. Then

$$FE=\begin{bmatrix}1&0&0\\-5&1&0\\20&-4&1\end{bmatrix}\ \text{ is inverted by }\ E^{-1}F^{-1}=\begin{bmatrix}1&0&0\\5&1&0\\0&4&1\end{bmatrix}.\tag{9}$$

In the order FE, row 3 feels an effect of size 20 from row 1. In the order $E^{-1}F^{-1}$ it does not. The multipliers 5 and 4 fall into place below the diagonal of 1's (p. 52).

> Intuition note: Elimination order FE mixes the multipliers (the product 5·4 = 20 appears). The reversed inverse order does not mix them. That is why A = LU is the nicer way to record elimination.

**L is the inverse of E (p. 53).** For n = 3, E is messy (eq. 10):

$$E=E_{32}E_{31}E_{21}=\begin{bmatrix}1&0&0\\-\ell_{21}&1&0\\(\ell_{32}\ell_{21}-\ell_{31})&-\ell_{32}&1\end{bmatrix}.$$

Its inverse, built in reverse order, is clean (eq. 11):

$$E^{-1}=\begin{bmatrix}1&&\\\ell_{21}&1&\\0&0&1\end{bmatrix}\begin{bmatrix}1&&\\0&1&\\\ell_{31}&0&1\end{bmatrix}\begin{bmatrix}1&&\\0&1&\\0&\ell_{32}&1\end{bmatrix}=\begin{bmatrix}1&&\\\ell_{21}&1&\\\ell_{31}&\ell_{32}&1\end{bmatrix}=L.$$

So EA = U becomes A = LU. The author says "the next section" shows this holds for all sizes (p. 53).

Problem Set 2.2 (pp. 53–56): 40 problems (0–39) on elimination matrices, inverses, Gauss–Jordan, and block matrices.

### 2.3 Matrix Computations and A = LU (pp. 57–61)
**Gauss–Jordan (p. 57).** Computing $A^{-1}$ then $A^{-1}b$ is a slow way to find x. But $AA^{-1}=I$ means n equations $Ax_k=e_k$ with the same A, where $x_k$ is column k of $A^{-1}$ and $e_k$ is column k of I (eq. 1). Solve them together on $[A\;\,I]$:

$$\left[\begin{array}{ccc|ccc}1&0&0&1&0&0\\-1&1&0&0&1&0\\0&-1&1&0&0&1\end{array}\right]\to\left[\begin{array}{ccc|ccc}1&0&0&1&0&0\\0&1&0&1&1&0\\0&-1&1&0&0&1\end{array}\right]\to\left[\begin{array}{ccc|ccc}1&0&0&1&0&0\\0&1&0&1&1&0\\0&0&1&1&1&1\end{array}\right]=[I\;\,A^{-1}].$$

The elimination steps on A are done once and applied to all n right sides. This is slower than solving Ax = b. Here A subtracts rows and $A^{-1}$ adds. The author calls $AA^{-1}=I$ linear algebra's version of the Fundamental Theorem of Calculus (derivative of integral of f is f) (p. 57).

**Cost of elimination (p. 58).**
- Stage 1 costs about n² multiplications and n² subtractions (exactly n² − n, because row 1 is unchanged).
- Stage 2 works on an (n−1)-size matrix, about (n−1)², and so on. The total is the sum of squares $n^2+(n-1)^2+\dots+2^2+1^2$. The exact formula is $\tfrac13 n(n+\tfrac12)(n+1)$. For large n only $\tfrac13 n^3$ matters (like $\int_0^n x^2dx$).
- **Reducing A to U takes about ⅓n³ multiplications and ⅓n³ subtractions.**
- Right side b, forward: $(n-1)+(n-2)+\dots+1$ steps. Back substitution: $1+2+\dots+n$ steps. Pairing terms, the total is exactly

$$[(n-1)+(n-2)+\dots+1]+[1+2+\dots+(n-1)+n]=n^2.\tag{2}$$

- Each right side needs n² multiplications and n² subtractions. A random matrix of order 1000 typically takes about 1 second on a PC. Doubling n multiplies the time by about 8. Order 10,000 would take about a thousand seconds, and order 100,000 about a million seconds. Most large practical matrices are sparse, and then A = LU is much faster (p. 58).

> Intuition note: Factoring A is the expensive part (n³). Reusing the factors for a new b is cheap (n²). The author calls computing A⁻¹ and multiplying A⁻¹b a very slow way to find x (p. 57).

**The great factorization A = LU, first proof (p. 59).** Row exchanges are not yet allowed. The pivot rows subtracted from lower rows are rows of U, not rows of the original A, because pivot rows never change again. For row 3:

$$\text{Row 3 of }U=(\text{Row 3 of }A)-\ell_{31}(\text{Row 1 of }U)-\ell_{32}(\text{Row 2 of }U).\tag{3}$$

$$\text{Row 3 of }A=\ell_{31}(\text{Row 1 of }U)+\ell_{32}(\text{Row 2 of }U)+1(\text{Row 3 of }U).\tag{4}$$

This is exactly row 3 of LU, since row 3 of L is $[\ell_{31}\ \ell_{32}\ 1]$. All rows look like this, so with no row exchanges A = LU (p. 59).

**Second proof: columns times rows (p. 60).**
- Step 1 uses pivot row = row 1. With $\ell_{i1}=a_{i1}/a_{11}$ it subtracts $\ell_1\,(\text{row }1)$ from A. Here $\ell_1=(1,\ell_{21},\ell_{31},\ell_{41})$. This is a **rank-one matrix** (column times row) and leaves $A_2$ with zeros in column 1.
- Step 2 removes $\ell_2\,(\text{row 2 of }A_2)$, with $\ell_2=(0,1,\ell_{32},\ell_{42})$. Row 2 of $A_2$ is the second row $u_2$ of U. This leaves $A_3$.
- Every step removes a column $\ell_k$ of L times a pivot row $u_k$ of U. Adding the pieces back:

$$A=\ell_1u_1+\ell_2u_2+\dots+\ell_nu_n=\begin{bmatrix}\ell_1&\cdots&\ell_n\end{bmatrix}\begin{bmatrix}u_1\\\vdots\\u_n\end{bmatrix}=LU\tag{5}$$

- $u_k$ begins with k−1 zeros. L is lower triangular with 1's on the diagonal, and $\ell_k$ also begins with k−1 zeros (p. 60).

**Elimination without row exchanges (p. 61).** Question: when is A = LU possible with no row exchanges and no zero pivots? Author's answer: all upper-left k by k submatrices of A must be invertible (k = 1 to n). Reason: elimination also factors every corner, so

$$\begin{bmatrix}A_k&*\\ *&*\end{bmatrix}=\begin{bmatrix}L_k&0\\ *&*\end{bmatrix}\begin{bmatrix}U_k&*\\0&*\end{bmatrix}\ \Rightarrow\ A_k=L_kU_k.\tag{6}$$

The corners $L_k,U_k$ are invertible, so each $A_k$ must be invertible to reach A = LU (p. 61).

Problem Set 2.3 (pp. 61–63, Problems 1–17 in this part): computing A = LU and A = LDU, symmetric and tridiagonal cases, solving Lc = b then Ux = c, uniqueness of the factors, and column-times-row expansions.

## Toy example (ours, not from the text)
Take $A=\begin{bmatrix}1&1&1\\2&3&4\\3&6&10\end{bmatrix}$ and $b=(3,9,19)$.
- Column 1: $\ell_{21}=2/1=2$ gives row 2 → (2,3,4) − 2(1,1,1) = (0,1,2). $\ell_{31}=3$ gives row 3 → (3,6,10) − 3(1,1,1) = (0,3,7).
- Column 2: pivot 1, $\ell_{32}=3/1=3$ gives row 3 → (0,3,7) − 3(0,1,2) = (0,0,1).
- So $U=\begin{bmatrix}1&1&1\\0&1&2\\0&0&1\end{bmatrix}$ and $L=\begin{bmatrix}1&0&0\\2&1&0\\3&3&1\end{bmatrix}$. The multipliers sit in L exactly where they were used.
- Check row 3 of LU: 3(1,1,1) + 3(0,1,2) + 1(0,0,1) = (3,6,10) ✓. Row 2: 2(1,1,1) + (0,1,2) = (2,3,4) ✓.
- Solve Lc = b: $c_1=3$; $c_2=9-2\cdot3=3$; $c_3=19-3\cdot3-3\cdot3=1$. Then Ux = c: $x_3=1$; $x_2=3-2(1)=1$; $x_1=3-1-1=1$. So $x=(1,1,1)$, and A(1,1,1) = (3,9,19) ✓.
- Columns times rows: $\ell_1u_1=(1,2,3)^T(1,1,1)$ is the matrix with rows (1,1,1), (2,2,2), (3,3,3). Then $A-\ell_1u_1$ has rows (0,0,0), (0,1,2), (0,3,7). Next $\ell_2u_2=(0,1,3)^T(0,1,2)$ has rows (0,0,0), (0,1,2), (0,3,6). The remainder is only entry (3,3) = 1, which is $\ell_3u_3$ ✓.

## Concepts
- [[linear-independence]] — columns are independent when n nonzero pivots appear; dependent columns give nonzero X with AX = 0 (pp. 40–43)
- [[inverse-matrix]] — A⁻¹ with A⁻¹A = I = AA⁻¹; exists iff n pivots (row exchanges allowed); (AB)⁻¹ = B⁻¹A⁻¹ (pp. 50–52)
- [[rank]] — here: full rank means n nonzero pivots in a square matrix; rank 1 example for 2 by 2 singular (pp. 40, 43)
- [[column-space]] — b has a solution iff b lies in the combinations of the columns of A (pp. 40, 44)
- [[null-space]] — nonzero X with AX = 0 exist exactly when columns are dependent; solutions of Ax = b then come in lines x + αX (pp. 40, 50)
- [[determinant]] — ad − bc for 2 by 2; invertible iff nonzero (p. 50)
- [[rank-one-matrix-outer-product]] — column times row; A = Σ ℓ_k u_k (p. 60)
- [[elimination]] (new) — subtract multiples of pivot rows from lower rows to reach upper triangular U (p. 40)
- [[pivot]] (new) — diagonal entry of U used to clear its column; must be nonzero (p. 41)
- [[back-substitution]] (new) — solve Ux = c from the last equation upward (p. 41)
- [[elimination-matrix]] (new) — E_ij: I with −ℓ_ij in position (i,j); E = E₃₂E₃₁E₂₁ (p. 49)
- [[lu-factorization]] (new) — A = LU, L has the multipliers below a diagonal of 1's; PA = LU when exchanges are needed (pp. 45, 59)
- [[permutation-matrix]] (new) — P exchanges rows to avoid a zero pivot; there are n! of them (p. 45)
- [[gauss-jordan-elimination]] (new) — eliminate on [A I] to reach [I A⁻¹] (p. 57)
- [[elimination-cost]] (new) — ⅓n³ to reach U, n² per right side (p. 58)

## Canonical instances
- [[elimination-example-2-3-4]] — 3 by 3 system with multipliers 2, 1, 1 and pivots 2, 5, 7; x = (4,1,2) (pp. 41–42)
- [[singular-2x2-three-cases]] — one solution, none, and a line of solutions for n = 2 (p. 40)
- [[zero-pivot-row-exchange]] — A with zero in pivot 2 fixed by P; A* with no second pivot (p. 43)
- [[fe-vs-einv-finv-20]] — FE contains 20, but E⁻¹F⁻¹ has multipliers 5 and 4 in place (p. 52)
- [[gauss-jordan-difference-matrix]] — [A I] → [I A⁻¹] with A⁻¹ lower triangular of 1's (p. 57)

## Bridges (candidates)
- [structural-analogy] Inverses come in reverse order, (AB)⁻¹ = B⁻¹A⁻¹ ↔ everyday: socks and shoes (undo the last operation first) — used by the author as a picture (p. 52)
- [structural-analogy] A = LU as a sum of rank-one matrices ℓ_k u_k ↔ low-rank structure: building a matrix from outer products (p. 60)
- [metaphor] AA⁻¹ = I ↔ calculus: derivative of integral of f is f (the author's own remark, p. 57)
- [same-math] Solving Ax = e_k for each k to build A⁻¹ ↔ solving many right sides with one factorization: both reuse the same elimination steps (pp. 57–58)

## Questions this raises
- When row exchanges are needed, how exactly does A = LU change to PA = LU, and which P should one choose?
- How does the n³/3 count change for sparse matrices, where the author says A = LU is much faster (p. 58)?
- The condition "all upper-left corners invertible" (p. 61): how does it relate to the pivots, and to pivots of the corner A_k (see Problem 15, p. 63)?
- Are L and U unique? Problem 12 (p. 63) suggests the factors in A = LDU are unique.

## Exercises worth doing
- Ex. 2.1-11 (p. 47) — a linear system cannot have exactly two solutions (uses eq. 1) — difficulty: medium
- Ex. 2.2-16 (p. 55) — row 1 + row 2 = row 3 implies not invertible, seen via elimination and via solvability — difficulty: medium
- Ex. 2.2-34 (p. 56) — find pivots and the values of c making a matrix singular — difficulty: medium
- Ex. 2.3-1 (p. 61) — forward elimination, the reverse step L, and L multiplying Ux = c to give b — difficulty: easy
- Ex. 2.3-7 (p. 62) — L and U for a symmetric matrix and the four conditions for four pivots — difficulty: medium
- Ex. 2.3-12 (p. 63) — uniqueness of L, D, U — difficulty: hard

## Reading notes
- This is part 1 of Chapter 2. It starts at the chapter opener (printed p. 39) and ends at Problem 17 of Problem Set 2.3 (printed p. 63). Sections 2.4 (Permutations and Transposes) and 2.5 (Derivatives and Finite Difference Matrices) are listed on p. 39 but do not appear in these pages. The text of Section 2.3 is complete here; the pages end at Problem 17 of Set 2.3 and do not show whether that set continues.
- Page offset: printed = pdf − 10.
- The text layer is heavily garbled in matrices and equations. I checked all matrices, multipliers, and equations against the page images.
- Several problems contain printed fill-in blanks (e.g. Problems 2, 5 and 7 of Set 2.2 and Problem 1 of Set 2.3); these blanks are part of the printed questions.
- Equation numbers restart in each section; I label them by section where needed.
- Strang calls A = LU "the best equation of all" (p. 45) and says A = LU "is one of the great matrix factorizations" (p. 59).
