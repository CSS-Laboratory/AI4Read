---
id: strang-2023-introduction/ch03-four-p2
work: strang-2023-introduction
unit: "3 The Four Fundamental Subspaces (part 2/3): §3.3 The Complete Solution to Ax = b; §3.4 Independence, Basis, and Dimension"
pages: 104-128
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
# The Complete Solution to Ax = b; Independence, Basis, and Dimension

## L0 — One line
Every solution of Ax = b is one particular solution plus any nullspace vector, and the size of a subspace is the number of vectors in any of its bases.

## L1 — The gist (≤ 120 words)
Section 3.3 asks what all solutions of Ax = b look like and when any exist. Elimination on the augmented matrix gives R₀x = d. A solution exists exactly when zero rows of R₀ have zeros in d, and then x = x_p + x_n. The rank r against m and n gives four cases: 1, ∞, 0 or 1, or 0 or ∞ solutions. Section 3.4 makes "true size" precise: independent vectors, spanning sets, bases, and dimension, the number of vectors in every basis. The ideas extend to matrices and functions as "vectors". This is the vocabulary for the four subspaces.

**Prerequisites:** Gaussian elimination to echelon form R₀; pivot and free variables; special solutions of Ax = 0; column space, nullspace, rank; matrix multiplication; solving Ax = 0 when a matrix is short and wide.

## L2 — Key ideas (5–10 bullets)
- Complete solution of Ax = b: one particular solution x_p (free variables zero) plus any x_n from the nullspace. It is not multiplied by an arbitrary constant (p. 107).
- Solvability: Ax = b is solvable when every zero row of R₀ has a zero in d. Equivalently, b must satisfy the same relations as the rows of A (pp. 104, 110).
- Full column rank (r = n) gives at most one solution. Full row rank (r = m) gives at least one solution for every b (pp. 106, 108).
- Rank against m and n gives four cases: 1 solution; ∞ solutions; 0 or 1; 0 or ∞ (p. 108).
- Independence means Ax = 0 only for x = 0. Any n vectors in Rᵐ with n > m are dependent (pp. 115, 117).
- A basis is independent and spanning, and each vector has a unique combination of basis vectors. Every basis has the same number of vectors, the dimension (pp. 118–120).
- The n − r special solutions are a basis of N(A), and the pivot columns are a basis of C(A) (pp. 119–120, 122).
- Matrices and functions can also be "vectors" with bases and dimensions (p. 121).

## L3 — Walkthrough

### 3.3 The Complete Solution to Ax = b

**Setup (p. 104).** Row operations must act on b too. Add b as an extra column to get the *augmented matrix* $[A\ b]$. Elimination turns it into $[R_0\ d]$ and the system into $R_0x = d$, with the same solutions (if any) (p. 104).

Author's example: $A=\begin{bmatrix}1&3&0&2\\0&0&1&4\\1&3&1&6\end{bmatrix}$, $b=(1,6,7)$. Subtracting rows 1 and 2 from row 3 gives $R_0=\begin{bmatrix}1&3&0&2\\0&0&1&4\\0&0&0&0\end{bmatrix}$ and $d=(1,6,0)$. The third equation is $0=0$, so the system is solvable. Row 1 plus row 2 equals row 3 in A, so b needs $b_1+b_2=b_3$, and $1+6=7$ does (p. 104). For general b, the last row of $[R_0\ d]$ is $(0,0,0,0,\ b_3-b_1-b_2)$, so solvability needs $b_3-b_1-b_2=0$ (p. 104).

**Particular solution (p. 105).** Set the free variables to zero ($x_2=x_4=0$). The pivot variables then come straight from d: $x_p=(1,0,6,0)$. The particular solution solves $Ax_p=b$. The $n-r$ special solutions solve $Ax_n=0$. Here they are $(-3,1,0,0)$ and $(-2,0,-4,1)$, from the free columns of $R_0$ with signs reversed (p. 105). The complete solution is

$$x=x_p+x_n=\begin{bmatrix}1\\0\\6\\0\end{bmatrix}+x_2\begin{bmatrix}-3\\1\\0\\0\end{bmatrix}+x_4\begin{bmatrix}-2\\0\\-4\\1\end{bmatrix}.$$

If A is square invertible ($m=n=r$), then $x_p=A^{-1}b$ is the only solution and $x_n=0$. In this case $[A\ b]$ reduces to $[I\ A^{-1}b]$ (p. 105).

*Intuition note.* Any two solutions differ by a vector that A sends to zero. So you find one solution and add the whole nullspace. The particular solution is a single point, not a multiple of anything.

**Full column rank, $r=n$ (p. 106).** Example 1: $A=\begin{bmatrix}1&1\\1&2\\-2&-3\end{bmatrix}$. Subtract row 1 from row 2 and add 2·row 1 to row 3 (the author then finishes upward to $R_0$):

$$[A\ b]\to[R_0\ d]=\begin{bmatrix}1&0&2b_1-b_2\\0&1&b_2-b_1\\0&0&b_3+b_1+b_2\end{bmatrix}.$$

The condition is $b_3+b_1+b_2=0$. The rows of A add to the zero row, so the entries of b must add to zero. There are no free variables, so $x_n=0$ and $x=x_p=(2b_1-b_2,\ b_2-b_1)$ (p. 106). In general $R_0=\begin{bmatrix}I\\0\end{bmatrix}$ ($n$ by $n$ identity, $m-n$ zero rows) (eq. 1, p. 106). Every matrix with full column rank has:
1. all columns pivot columns (independent) and no free variables;
2. $N(A)=\{0\}$;
3. at most one solution if $Ax=b$ has any (p. 106).

There are $m-n$ conditions on b. With full column rank, $Ax=b$ has one solution or no solution (p. 106). The author says $A^TA$ will be added later to this list as invertible when the rank is n (p. 106).

**Full row rank, $r=m$ (pp. 107–108).** A must be short and wide ($m\le n$). Every row has a pivot. Then $Ax=b$ has one or infinitely many solutions (p. 107).

Example 2: $x+y+z=3$, $x+2y-z=4$. These are two non-parallel planes meeting in a line. Elimination down then up:

$$\begin{bmatrix}1&1&1&3\\1&2&-1&4\end{bmatrix}\to\begin{bmatrix}1&1&1&3\\0&1&-2&1\end{bmatrix}\to\begin{bmatrix}1&0&3&2\\0&1&-2&1\end{bmatrix}=[R\ d].$$

The particular solution with $x_3=0$ is $(2,1,0)$, read from d. The special solution with $x_3=1$ is $s=(-3,2,1)$, from the free column with signs reversed. Checks: $2+1=3$, $2+2=4$, $-3+2+1=0$, $-3+4-1=0$. The complete solution is $x=(2,1,0)+x_3(-3,2,1)$, the whole line of Figure 3.1. Any point of the line could have been the particular solution (p. 107).

Every matrix with full row rank has: all rows pivots and $R_0=R$ (no zero rows); $Ax=b$ solvable for every b; $C(A)=\mathbb R^m$; and if $m<n$, $Ax=b$ is underdetermined (many solutions) (p. 108). The m rows are independent, so the columns of $A^T$ are independent and $N(A^T)=\{0\}$ (p. 108).

**Four cases (p. 108).**

| rank | type | $Ax=b$ has |
|---|---|---|
| $r=m=n$ | square, invertible | 1 solution |
| $r=m<n$ | short, wide | ∞ solutions |
| $r=n<m$ | tall, thin | 0 or 1 solution |
| $r<m,\ r<n$ | not full rank | 0 or ∞ solutions |

If the pivot columns come first, $R_0$ is $[I]$, $[I\ F]$, $\begin{bmatrix}I\\0\end{bmatrix}$ or $\begin{bmatrix}I&F\end{bmatrix}$ over a zero row block, respectively. For solvability, d must end in $m-r$ zeros (p. 108).

**Computation note (p. 108).** In practice, elimination steps are reordered for speed and stability. Systems of order 1000 can be solved on a laptop. Beyond the size limit, *randomized linear algebra* samples columns of A and accepts some error, giving $A\approx CMR$. Here C holds sampled columns, R sampled rows, and M is a smaller mixing matrix. The author says results are with high probability surprisingly accurate (p. 108).

**Worked Example 3.3A (p. 109).** $A=\begin{bmatrix}1&2&3&5\\2&4&8&12\\3&6&7&13\end{bmatrix}$, rank 2. Elimination (multipliers 2, 3, −1) gives $U$ rows $(1,2,3,5\,|\,b_1)$, $(0,0,2,2\,|\,b_2-2b_1)$, $(0,0,0,0\,|\,b_3+b_2-5b_1)$. The condition is $b_3+b_2-5b_1=0$. Then:
- $C(A)$ is the plane spanned by the pivot columns $(1,2,3)$ and $(3,8,7)$. It is also the plane $b_3+b_2-5b_1=0$.
- Special solutions: $s_1=(-2,1,0,0)$ and $s_2=(-2,0,-1,1)$.
- With $c=(0,6,0)$, $R_0=\begin{bmatrix}1&2&0&2\\0&0&1&1\\0&0&0&0\end{bmatrix}$ and $d=(-9,3,0)$, so $x_p=(-9,0,3,0)$.
- For $Ax=(0,6,-6)$ the complete solution is $x=x_p+c_1s_1+c_2s_2$ (p. 109).

**Worked Example 3.3B (p. 110).** What do the solution sets say about A?
- Exactly one solution: full column rank $r=n$, and b is in $C(A)$.
- $x=(2,1)+c(1,1)$: $n=2$, column 2 is the negative of column 1, rank 1, and $b=2(\text{col }1)+\text{col }2$.
- No solutions: b is not in $C(A)$ and $r<m$.
- $x=(1,1,0)+c(1,0,1)$: $n=3$, column 3 is −column 1, rank $3-1=2$, and $b=\text{col }1+\text{col }2$ (p. 110).

**Worked Example 3.3C (p. 110).** $A=\begin{bmatrix}1&2&1&0\\2&4&4&8\\4&8&6&8\end{bmatrix}$, $b=(4,2,10)$. Then $R_0=\begin{bmatrix}1&2&0&-4\\0&0&1&4\\0&0&0&0\end{bmatrix}$, $d=(7,-3,0)$, $s_1=(-2,1,0,0)$, $s_2=(4,0,-4,1)$, $x_p=(7,0,-3,0)$. The rows satisfy $2(\text{row }1)+(\text{row }2)-(\text{row }3)=0$, and the same combination of b gives $8+2-10=0$. If a combination of rows of A gives the zero row, the same combination of b must give zero. Equivalently, with $y=(2,1,-1)$ in $N(A^T)$, y is perpendicular to every b in $C(A)$ (p. 110).

*Intuition note.* Solvability is a consistency test: any relation among the equations must also hold among the right-hand sides.

### 3.4 Independence, Basis, and Dimension

**Independence (pp. 115–117).** The columns of A are *linearly independent* when the only solution of $Ax=0$ is $x=0$, i.e. $N(A)=\{0\}$ (p. 115). For vectors in any space: $x_1v_1+\cdots+x_nv_n=0$ only when all $x$'s are zero (eq. 1, p. 116). Otherwise they are dependent. The correct phrasing is that a sequence of vectors is linearly independent. The author calls it unacceptable to say that a matrix is independent (p. 116).

- Three vectors in $\mathbb R^3$ are independent if not in one plane, dependent if in one plane (p. 116).
- In $\mathbb R^2$: $(1,0),(1,0.00001)$ independent. $(1,1),(-1,-1)$ dependent. $(1,1),(0,0)$ dependent (zero vector). Any three vectors are dependent (p. 116).

Example 1: $A=\begin{bmatrix}1&0&3\\2&1&5\\1&0&3\end{bmatrix}$ has $x=(-3,1,1)$ with $Ax=0$. Rank $r=2$. $R_0=\begin{bmatrix}1&0&3\\0&1&-1\\0&0&0\end{bmatrix}$, $F=\begin{bmatrix}3\\-1\end{bmatrix}$ (p. 117). Columns are independent exactly when $r=n$ (p. 117).

**Theorem:** any set of $n$ vectors in $\mathbb R^m$ is dependent if $n>m$. Reason: $Ax=0$ has at least $n-m$ free variables (p. 117). If $n\le m$, the columns may or may not be independent. The $r$ pivot columns are independent (p. 117). The author gives this test rather than the wording that one vector is a combination of the others, because the test does not single out one vector as guilty and treats all columns alike (p. 117).

*Intuition note.* Independent columns means no redundancy. Dependence shows up as a nonzero x with Ax = 0, so more vectors than dimensions forces redundancy.

**Span (p. 118).** The columns of a matrix span $C(A)$, possibly while dependent. Example 2: $A=\begin{bmatrix}1&4\\2&7\\3&5\end{bmatrix}$. $C(A)$ is a plane in $\mathbb R^3$. The row space is spanned by the three rows (columns of $A^T$) and is all of $\mathbb R^2$ (p. 118).

**Basis (pp. 118–119).** A basis is independent and spans the space. Every v is a combination of basis vectors, and uniquely: if $v=\sum a_iv_i=\sum b_iv_i$, subtracting gives $\sum(a_i-b_i)v_i=0$, so each $a_i=b_i$ (p. 118).
- Example 3: columns of $I$ are the standard basis (p. 118).
- Example 4: columns of $A=\begin{bmatrix}1&0&0\\1&1&0\\1&1&1\end{bmatrix}$ (invertible) are a basis of $\mathbb R^3$. $B=\begin{bmatrix}1&0&1\\1&1&2\\1&1&2\end{bmatrix}$ is singular, with column space $\ne\mathbb R^3$. Its first two (pivot) columns are independent and span $C(B)$ (p. 119).
- Rule: $v_1,\dots,v_n$ are a basis for $\mathbb R^n$ exactly when they are the columns of an invertible n by n matrix. $\mathbb R^n$ has infinitely many bases (p. 119).
- Every independent set extends to a basis; every spanning set reduces to a basis (p. 119).
- Example 5: $A=\begin{bmatrix}2&4\\3&6\end{bmatrix}\to R_0=\begin{bmatrix}1&2\\0&0\end{bmatrix}$, so not invertible (p. 119).
- Example 6: $R_0=\begin{bmatrix}1&2&0&3\\0&0&1&4\\0&0&0&0\end{bmatrix}$. Columns 1 and 3 (pivots) are a basis for its column space, the "xy plane" in $\mathbb R^3$. The two nonzero rows are a basis for the row space in $\mathbb R^4$. The zero vector is never in a basis (p. 119).
- To get a basis for the span of five vectors in $\mathbb R^7$: put them in the rows of A and keep the nonzero rows of R, or put them in the columns and keep the pivot columns (p. 119).

**Dimension (p. 120).** *Theorem:* if $v_1,\dots,v_m$ and $w_1,\dots,w_n$ are both bases of one space, then $m=n$.
*Proof.* Suppose $n>m$. Each $w_j$ is a combination of the v's, so $W=VA$ with $V$ $(\text{dim}\times m)$, $A$ ($m\times n$), $W$ ($\text{dim}\times n$). A is short and wide, so $Ax=0$ has a nonzero solution. Then $VAx=0$, i.e. $Wx=0$, so the w's are dependent, which contradicts their being a basis. If $m>n$, swap the roles (p. 120).

*Definition:* the dimension is the number of vectors in every basis. Example: the line through $(1,5,2)$ has dimension 1. The plane $x+5y+2z=0$ has basis $(-5,1,0),(-2,0,1)$, so dimension 2. It is the nullspace of $[1\ 5\ 2]$. The $n-r$ special solutions always give a basis of $N(A)$, with dimension $n-r$ (p. 120). The author warns that the phrases rank of a space, dimension of a basis and basis of a matrix have no meaning. The dimension of $C(A)$ equals the rank (p. 120).

*Intuition note.* If a space had a bigger and a smaller basis, the bigger one would be forced to be dependent. So the number of independent directions in a space is well defined.

**Matrix and function spaces (p. 121).** The space M of 2 by 2 matrices has dimension 4, with basis $\begin{bmatrix}1&0\\0&0\end{bmatrix},\begin{bmatrix}0&1\\0&0\end{bmatrix},\begin{bmatrix}0&0\\1&0\end{bmatrix},\begin{bmatrix}0&0\\0&1\end{bmatrix}$. Here $c_1A_1+\cdots+c_4A_4=\begin{bmatrix}c_1&c_2\\c_3&c_4\end{bmatrix}$, zero only if all c's are zero. The 3 by 4 matrix space has dimension 12. Upper triangular 2 by 2 matrices: dimension 3 ($A_1,A_2,A_4$). Diagonal: $A_1,A_4$. Symmetric: $A_1,A_4,A_2+A_3$. For n by n: whole space $n^2$; upper triangular $\tfrac12n^2+\tfrac12n$; diagonal $n$; symmetric $\tfrac12n^2+\tfrac12n$ ("why?", left as a question) (p. 121).

Functions: $y''=0$ is solved by $y=cx+d$. $y''=-y$ by $y=c\sin x+d\cos x$. $y''=y$ by $y=ce^x+de^{-x}$. Each solution space has dimension 2 (second-order equations). $y''=0$ is the "nullspace" of the second derivative. The solutions of $y''=2$ are not a subspace (right side nonzero). A particular solution is $x^2$ and the complete solution is $x^2+cx+d$, like $x_p+x_n$. The space $\mathbf Z=\{0\}$ has dimension 0. The empty set is its basis (p. 121).

**Summary (p. 122).** Independent means only $x=0$ solves $Ax=0$. Vectors span if their combinations fill the space. A basis is independent and spanning, with unique combinations. All bases have the same size, the dimension. The pivot columns are a basis for $C(A)$, and $\dim C(A)=r$ (p. 122).

**Worked Example 3.4A (p. 122).** If $v_1,\dots,v_n$ is a basis of $\mathbb R^n$ and A is invertible, then $Av_1,\dots,Av_n$ is a basis. Matrix proof: they are the columns of $AV$, which is invertible. Vector proof: $\sum c_iAv_i=0$; multiply by $A^{-1}$ to get $\sum c_iv_i=0$, so all $c_i=0$. For spanning: $\sum c_iAv_i=b$ is $\sum c_iv_i=A^{-1}b$, which is solvable (p. 122).

**Worked Example 3.4B (p. 122).** $v_1=(1,2,0)$, $v_2=(2,3,0)$ are independent and a basis for $V$ = all $(x,y,0)$, of dimension 2. V is the column space of any 3 by n rank-2 matrix whose columns are combinations of $v_1,v_2$. V is the nullspace of any m by 3 rank-1 matrix whose rows are multiples of $(0,0,1)$, e.g. $B=[0\ 0\ 1]$. A third vector $v_3=(a,b,c)$ completes a basis of $\mathbb R^3$ provided $c\ne0$ (p. 122).

**Worked Example 3.4C (p. 123).** $V=WB$ with $W=[w_1\ w_2\ w_3]$ independent and $B=\begin{bmatrix}1&1&0\\1&2&1\\0&1&c\end{bmatrix}$. If $c=1$: $v_1+v_3=v_2$, so $v_1-v_2+v_3=0$. Equivalently $x=(1,-1,1)$ is in $N(B)$, so $WBx=0$. If $c\ne1$: B is invertible, so $x\ne0$ gives $Bx\ne0$, and $WBx\ne0$ since the w's are independent. So the v's are independent. General rule: independent v's come from independent w's when B is invertible; in $\mathbb R^3$ they are then a basis (p. 123).

## Toy example (ours, not from the text)
Solve $Ax=b$ with $A=\begin{bmatrix}1&2&1\\2&4&3\end{bmatrix}$, $b=(3,8)$ ($m=2$, $n=3$).
1. Row 2 − 2·row 1: $[A\ b]\to\begin{bmatrix}1&2&1&3\\0&0&1&2\end{bmatrix}$ (since $8-2\cdot3=2$).
2. Row 1 − row 2: $\begin{bmatrix}1&2&0&1\\0&0&1&2\end{bmatrix}=[R\ d]$, with $d=(1,2)$. There are no zero rows, so it is solvable. Pivots are in columns 1 and 3, so $r=2=m$ (full row rank). The free variable is $x_2$.
3. Set $x_2=0$: $x_p=(1,0,2)$. Check: $A x_p=(1+0+2,\ 2+0+6)=(3,8)$ ✓.
4. Special solution ($x_2=1$): $s=(-2,1,0)$. Check: $A s=(-2+2,\ -4+4)=(0,0)$ ✓.
5. Complete solution: $x=(1,0,2)+c(-2,1,0)$, a line of solutions, as the text predicts for $r=m<n$.

Contrast: for the tall matrix $A=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$, row 3 − row 1 − row 2 is zero, so the condition is $b_3-b_1-b_2=0$. For $b=(1,2,3)$ the only solution is $x=(1,2)$.

## Concepts
- [[complete-solution]] (new) — $x=x_p+x_n$: one particular solution plus all nullspace vectors (p. 104).
- [[augmented-matrix]] (new) — $[A\ b]$, b added as a column so row operations act on both sides (p. 104).
- [[particular-solution]] (new) — the solution with all free variables zero, pivot variables read from d (p. 105).
- [[solvability-condition]] (new) — zero rows of $R_0$ must have zeros in d; b must obey the row relations of A (pp. 104, 110).
- [[full-column-rank]] (new) — $r=n$: no free variables, $N(A)=\{0\}$, at most one solution (p. 106).
- [[full-row-rank]] (new) — $r=m$: $C(A)=\mathbb R^m$, always solvable, one or infinitely many solutions (p. 108).
- [[linear-independence]] — only $x=0$ gives $Ax=0$ (columns) or $\sum x_iv_i=0$ (p. 115).
- [[span]] — all combinations; the columns of A span $C(A)$ (p. 118).
- [[basis]] — independent and spanning; gives unique coordinates (p. 118).
- [[dimension]] — number of vectors in every basis (p. 120).
- [[null-space]] — $N(A)$ has basis the $n-r$ special solutions (p. 120).
- [[column-space]] — basis: the pivot columns; dimension $r$ (pp. 119, 122).
- [[rank]] — dimension of $C(A)$ (p. 120).

## Canonical instances
- [[two-planes-line-of-solutions]] — $x+y+z=3$, $x+2y-z=4$: solutions form a line $x_p+x_n$ (p. 107).
- [[solutions-of-y-double-prime-2]] — $y''=2$ has solution $x^2+cx+d$, like $x_p+x_n$ (p. 121).
- [[matrix-space-2x2]] — 2 by 2 matrices form a space of dimension 4 (p. 121).
- [[solution-space-y-double-prime-minus-y]] — basis $\sin x,\cos x$; dimension 2 (p. 121).

## Bridges (candidates)
- [structural-analogy] $x_p+x_n$ for $Ax=b$ ↔ differential equations: particular solution plus homogeneous solution of a linear ODE (the text draws this analogy on p. 121).
- [structural-analogy] Sampling columns and rows, $A\approx CMR$ ↔ numerical computing: trading exact elimination for a fast approximate solution that is accurate with high probability (p. 108).
- [structural-analogy] $V=WB$ with B invertible ↔ change of basis: the same space described by different basis vectors (p. 123).

## Questions this raises
- Does $\dim C(A)=\dim C(A^T)$ always hold (row rank = column rank)? Problem 24(c) hints at it.
- How is the particular solution with free variables zero related to the shortest solution? Problem 13(c) asks for a counterexample.
- How does the dimension formula for sums and intersections of subspaces (Problem 42) follow from bases?
- What is the dimension of the n by n symmetric matrix space, and why is it $\tfrac12n^2+\tfrac12n$?

## Exercises worth doing
- Ex. 3.3-1 (p. 111) — the six steps of 3.3A on a new rank-2 matrix: column space, nullspace, complete solution — difficulty: medium
- Ex. 3.3-2 (p. 111) — rank-one matrix: two conditions on b put b in a line — difficulty: easy
- Ex. 3.3-13 (p. 112) — why four statements are false (the complete solution is any combination of x_p and x_n; there is at most one particular solution; x_p is the shortest solution; an invertible A has no x_n in the nullspace) — difficulty: medium
- Ex. 3.3-31 (p. 114, recommended) — from one special solution, find the rank, $R_0$ and solvability — difficulty: medium
- Ex. 3.4-2 (p. 124, recommended) — the largest set of independent vectors among six given vectors — difficulty: medium
- Ex. 3.4-42 (p. 128) — prove $\dim V+\dim W=\dim(V\cap W)+\dim(V+W)$ via bases — difficulty: hard

## Reading notes
- This part starts at the opening of §3.3 (printed p. 104) and ends at the end of Problem Set 3.4, including Challenge Problems (printed p. 128). It splits at a section boundary (as stated in the unit metadata); earlier and later pages of the chapter are not covered here.
- Printed page = pdf − 10.
- The text layer is heavily garbled in equations and matrices. I read the matrices and equations from the page images.
- p. 105 says the special solutions came in Section 3.3, which is the current section, although p. 104 says they were found in the last section. This may be a misprint, but I cannot confirm that from these pages. The text layer garbles the free-column entries; the image shows 3, 2 and 4.
- p. 122, key-point 2 uses $v_r$ for the last vector while the index elsewhere is $n$ or $k$; a minor notation inconsistency.
- Problem sets have blanks to fill in (e.g. Problems 14–17); I did not solve any exercises.
