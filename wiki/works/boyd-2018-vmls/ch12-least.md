---
id: boyd-2018-vmls/ch12-least
work: boyd-2018-vmls
unit: Chapter 12 — Least squares
pages: 225–244
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
# Least squares

## L0 — One line
When $Ax=b$ has no solution because $A$ is tall, minimizing $\|Ax-b\|^2$ gives a unique best compromise $\hat x=(A^TA)^{-1}A^Tb=A^\dagger b$, provided the columns of $A$ are linearly independent; the optimal residual is orthogonal to the columns of $A$.

## L1 — The gist (≤ 120 words)
A tall system $Ax=b$ usually has no exact solution. The chapter asks which $x$ makes the residual $Ax-b$ as small as possible. If the columns of $A$ are linearly independent, the answer is unique: $\hat x=A^\dagger b$, the solution of the normal equations $A^TA\hat x=A^Tb$. The authors derive it by calculus and by a direct algebraic check. The optimal residual is orthogonal to every column of $A$. In practice $\hat x$ is computed with a QR factorization at a cost of about $2mn^2$ flops. Matrix right-hand sides reduce to independent column problems. Examples: allocating advertising spend and setting lamp powers for even illumination.

**Prerequisites:** vector norm and inner product; linear independence; matrix transpose; partial derivatives and gradient; QR factorization and back substitution; pseudo-inverse $A^\dagger=(A^TA)^{-1}A^T$; flop counts.

## L2 — Key ideas
- A least squares approximate solution $\hat x$ minimizes $\|Ax-b\|^2$. It need not satisfy $A\hat x=b$. If an exact solution exists, it is a least squares solution (p. 226).
- Column view: $A\hat x$ is the combination of columns of $A$ closest to $b$. Row view: the objective is a sum of squared residuals of $m$ scalar equations (p. 226).
- If the columns of $A$ are linearly independent, the normal equations $A^TA\hat x=A^Tb$ have the unique solution $\hat x=(A^TA)^{-1}A^Tb=A^\dagger b$. This is the unique minimizer (pp. 229–230).
- Uniqueness and minimality can be checked without calculus. The cross term in $\|Ax-b\|^2$ vanishes by the normal equations, leaving $\|A(x-\hat x)\|^2+\|A\hat x-b\|^2$ (p. 230).
- Orthogonality principle: $\hat r=A\hat x-b$ is orthogonal to $Az$ for every $z$. It follows from the normal equations (p. 231).
- Algorithm 12.1 computes $\hat x$ by QR, then $Q^Tb$, then back substitution. It costs about $2mn^2$ flops and is formally the same as the square-system QR algorithm (pp. 231–232).
- Matrix least squares $\min\|AX-B\|^2$ splits into $k$ independent column problems, with $\hat X=A^\dagger B$ (p. 233).
- Applications: advertising purchases and lamp-power illumination. Neither is guaranteed to give nonnegative variables, since nonnegativity (and, for lamps, the maximum power) is ignored (pp. 234–236).

## L3 — Walkthrough

### 12.1 Least squares problem (pp. 225–227)
**Setting.** $A$ is $m\times n$ and tall ($m>n$), so $Ax=b$ is over-determined. It has a solution only if $b$ is a linear combination of the columns of $A$ (p. 225). Otherwise we seek $x$ making the **residual** $r=Ax-b$ small. Minimizing $\|r\|$ or $\|r\|^2$ is the same, so the **least squares problem** is

$$\text{minimize}\ \ \|Ax-b\|^2=\|r\|^2=r_1^2+\cdots+r_m^2 \tag{12.1}$$

(p. 225). $A$ and $b$ are the *data*, and $\|Ax-b\|^2$ is the *objective*. "Linear" least squares means $r$ is an affine function of $x$. Nonlinear least squares, with $r$ an arbitrary function of $x$, comes in chapter 18 (p. 226).

**Definitions.**
- Any $\hat x$ with $\|A\hat x-b\|^2\le\|Ax-b\|^2$ for all $x$ is a *least squares approximate solution* (p. 226).
- $\hat x$ need not satisfy $A\hat x=b$. The authors call the phrase "solves $Ax=b$ in the least squares sense" confusing (p. 226).
- $\|A\hat x-b\|$ is the *optimal residual norm*. If some $x$ satisfies $Ax=b$, it solves the least squares problem, since its residual norm is zero (p. 226).
- In data fitting the problem is called *regression*. $\hat x$ is the result of regressing $b$ onto the columns of $A$ (p. 226).

**Column interpretation.** With columns $a_1,\dots,a_n$: $\|Ax-b\|^2=\|(x_1a_1+\cdots+x_na_n)-b\|^2$. So $A\hat x=\hat x_1a_1+\cdots+\hat x_na_n$ is closest to $b$ among all linear combinations of the columns (p. 226).

**Row interpretation.** With rows $\tilde a_i^T$: $r_i=\tilde a_i^Tx-b_i$, and $\|Ax-b\|^2=(\tilde a_1^Tx-b_1)^2+\cdots+(\tilde a_m^Tx-b_m)^2$. Minimizing it is a reasonable compromise if we want all residuals small (p. 226).

**Worked example (p. 227).** $A=\begin{bmatrix}2&0\\-1&1\\0&2\end{bmatrix}$, $b=(1,0,-1)$. The equations $2x_1=1,\ -x_1+x_2=0,\ 2x_2=-1$ have no solution: the first gives $x_1=1/2$, the last $x_2=-1/2$, and then the second fails.
- Objective: $(2x_1-1)^2+(-x_1+x_2)^2+(2x_2+1)^2$. Unique solution $\hat x=(1/3,-1/3)$.
- Residual $\hat r=A\hat x-b=(-1/3,-2/3,1/3)$, with $\|A\hat x-b\|^2=2/3$.
- The alternative $\tilde x=(1/2,-1/2)$ solves the first and last equations exactly. It gives $\tilde r=(0,-1,0)$ and $\|A\tilde x-b\|^2=1$, which is larger.
- Column view: $(1/3)(2,-1,0)+(-1/3)(0,1,2)=(2/3,-2/3,-2/3)$ is the combination of columns closest to $b$.
- Figure 12.1 (p. 228) shows level curves of the objective, with $\hat x$ at the minimum.

### 12.2 Solution (pp. 227–231)
**Assumption** throughout: the columns of $A$ are linearly independent (12.2) (p. 227).

**Solution via calculus.** A minimizer $\hat x$ of $f(x)=\|Ax-b\|^2$ must satisfy $\partial f/\partial x_i(\hat x)=0$ for $i=1,\dots,n$, i.e. $\nabla f(\hat x)=0$ (p. 228). The gradient is

$$\nabla f(x)=2A^T(Ax-b). \tag{12.3}$$

Derivation from scratch (pp. 228–229). Write $f(x)=\sum_{i=1}^m\big(\sum_{j=1}^nA_{ij}x_j-b_i\big)^2$. Differentiate term by term:
$$\nabla f(x)_k=\frac{\partial f}{\partial x_k}(x)=\sum_{i=1}^m 2\Big(\sum_{j=1}^nA_{ij}x_j-b_i\Big)A_{ik}=\sum_{i=1}^m2(A^T)_{ki}(Ax-b)_i=\big(2A^T(Ax-b)\big)_k .$$

Setting $\nabla f(\hat x)=0$ gives the **normal equations**

$$A^TA\hat x=A^Tb. \tag{12.4}$$

$A^TA$ is the *Gram matrix* of $A$: its entries are inner products of columns of $A$ (p. 229).

Linear independence of the columns makes $A^TA$ invertible (§11.5, as cited on p. 229). So the normal equations have exactly one solution,

$$\hat x=(A^TA)^{-1}A^Tb, \tag{12.5}$$

and this must be the unique solution of (12.1). The matrix $(A^TA)^{-1}A^T$ is the pseudo-inverse $A^\dagger$ (11.5), so

$$\hat x=A^\dagger b. \tag{12.6}$$

$A^\dagger$ is a left inverse of $A$. So if $Ax=b$ has a solution, $A^\dagger b$ is it. In every case $A^\dagger b$ is the least squares approximate solution, i.e. it minimizes $\|Ax-b\|^2$ (p. 229).

**Contrast with square systems.** For square invertible $A$, $x=A^{-1}b$ satisfies $Ax=b$. For tall $A$, $\hat x=A^\dagger b$ generally does *not* satisfy $A\hat x=b$ (p. 229). Like the square case, $\hat x$ is a linear function of $b$ (p. 229).

*Intuition note.* Tall systems usually cannot be solved exactly, but we can still find the best compromise. Setting the gradient (slope) of the objective to zero gives a square system, the normal equations. Independent columns make that system have exactly one answer.

**Direct verification (no calculus) (p. 230).** Claim: for any $x\ne\hat x$, $\|A\hat x-b\|^2<\|Ax-b\|^2$.
1. Write $Ax-b=(Ax-A\hat x)+(A\hat x-b)$. Using $\|u+v\|^2=\|u\|^2+\|v\|^2+2u^Tv$:
$$\|Ax-b\|^2=\|Ax-A\hat x\|^2+\|A\hat x-b\|^2+2(Ax-A\hat x)^T(A\hat x-b). \tag{12.7}$$
2. The cross term is zero:
$$(Ax-A\hat x)^T(A\hat x-b)=(x-\hat x)^TA^T(A\hat x-b)=(x-\hat x)^T(A^TA\hat x-A^Tb)=(x-\hat x)^T0=0,$$
using the normal equations in the third step.
3. Hence $\|Ax-b\|^2=\|A(x-\hat x)\|^2+\|A\hat x-b\|^2\ge\|A\hat x-b\|^2$, so $\hat x$ minimizes.
4. Uniqueness: if equality holds, then $\|A(x-\hat x)\|^2=0$, so $A(x-\hat x)=0$. Independent columns then give $x=\hat x$. So $\|Ax-b\|^2>\|A\hat x-b\|^2$ for all $x\neq\hat x$.

**Row form.** In terms of the rows $\tilde a_i^T$ (p. 230):
$$\hat x=(A^TA)^{-1}A^Tb=\Big(\sum_{i=1}^m\tilde a_i\tilde a_i^T\Big)^{-1}\Big(\sum_{i=1}^mb_i\tilde a_i\Big). \tag{12.8}$$
The $n\times n$ Gram matrix is a sum of $m$ outer products, and the $n$-vector $A^Tb$ is a sum of $m$ $n$-vectors.

**Orthogonality principle (p. 231).** The optimal residual $\hat r=A\hat x-b$ is orthogonal to the columns of $A$, hence to every linear combination of them: for every $n$-vector $z$,
$$(Az)\perp\hat r. \tag{12.9}$$
Derivation from the normal equations $A^T(A\hat x-b)=0$: $(Az)^T\hat r=(Az)^T(A\hat x-b)=z^TA^T(A\hat x-b)=0$.
Figure 12.2 ($m=3,n=2$): the plane of combinations $z_1a_1+z_2a_2$ contains $A\hat x$, the point closest to $b$. The vector $\hat r$ from $b$ to $A\hat x$ is orthogonal to every point of the plane.

*Intuition note.* The closest point in a plane to $b$ is found by dropping a perpendicular. The leftover error then points straight out of the plane, so it has no component along any column.

### 12.3 Solving least squares problems (pp. 231–233)
**QR method.** Let $A=QR$ (it exists because the columns are independent). Since $A^\dagger=R^{-1}Q^T$,
$$\hat x=R^{-1}Q^Tb. \tag{12.10}$$
**Algorithm 12.1** (p. 232): (1) compute the QR factorization $A=QR$; (2) compute $Q^Tb$; (3) solve the triangular system $R\hat x=Q^Tb$ by back substitution.

**Comparison with square systems (p. 232).** For square invertible $A$, $x=R^{-1}Q^Tb$ (11.4) has the same form as (12.10). The only difference is that $A$ and $Q$ may be tall, and then $R^{-1}Q^Tb$ is not in general a solution of $Ax=b$. Algorithm 12.1 is formally algorithm 11.2. When $A$ is square the two problems coincide, so 12.1 generalizes 11.2.

**Backslash.** In several software packages, $A\backslash b$ means $A^{-1}b$ for square invertible $A$, and $A^\dagger b$ for tall $A$ with independent columns. The authors note this is not standard mathematical notation (p. 232).

**Complexity (p. 232).** Step 1 costs $2mn^2$ flops, step 2 costs $2mn$, step 3 costs $n^2$. Total $2mn^2+2mn+n^2\approx2mn^2$. The neglected terms are smaller than the first by factors of $n$ and $2m$. The order is $mn^2$: linear in $m$, quadratic in $n$.

**Sparse least squares.** For sparse $A$, a QR factorization tailored to sparse matrices can be used in algorithm 12.1 (p. 232). Another approach solves the $(m+n)$-equation system

$$\begin{bmatrix}0&A^T\\A&I\end{bmatrix}\begin{bmatrix}\hat x\\\hat y\end{bmatrix}=\begin{bmatrix}0\\b\end{bmatrix}, \tag{12.11}$$

whose coefficient matrix is sparse when $A$ is. Conversely, if $\hat x$ satisfies the normal equations, then $(\hat x,\hat y)$ solves (12.11) with $\hat y=b-A\hat x$ (p. 233).

**Matrix least squares (p. 233).** Choose the $n\times k$ matrix $X$ to minimize $\|AX-B\|^2$ ($A$ is $m\times n$, $B$ is $m\times k$, matrix norm). Because the squared matrix norm is the sum of squared column norms,
$$\|AX-B\|^2=\|Ax_1-b_1\|^2+\cdots+\|Ax_k-b_k\|^2,$$
and each term involves only one column $x_j$. So the columns can be chosen independently, and with independent columns of $A$, $\hat x_j=A^\dagger b_j$. Then
$$\hat X=[\hat x_1\ \cdots\ \hat x_k]=[A^\dagger b_1\ \cdots\ A^\dagger b_k]=A^\dagger[b_1\ \cdots\ b_k]=A^\dagger B. \tag{12.12}$$
For $k=1$ this is the ordinary solution. Factor once, solve $k$ times: one QR factorization, then steps 2–3 for each column of $B$. Cost is $2mn^2+k(2mn+n^2)$ flops, roughly $2mn^2$ when $k$ is small compared to $n$.

*Intuition note.* Several right-hand sides are just several separate fits. The expensive factorization is shared, and only the cheap steps repeat.

### 12.4 Examples (pp. 234–238)
**Advertising purchases (p. 234).** There are $m$ demographic groups and $n$ channels. $R_{ij}$ is the number of impressions in group $i$ per dollar spent in channel $j$. The spend vector $s$ gives views $v=Rs$, and the target is $v^{\rm des}$. Choose $s$ to minimize $\|Rs-v^{\rm des}\|^2$. Nonnegativity of $s$ is not guaranteed, and total cost is not considered (chapter 16 addresses it).
- Numbers: $n=3$, $m=10$, $R$ in units of 1000 views per dollar, entries within an 18:1 range. $v^{\rm des}=10^3\mathbf 1$, i.e. one million in each group.
- Result: $\hat s=(62,100,1443)$, with RMS error 132, or 13.2% of target (figures 12.3–12.4, p. 235).

**Illumination (pp. 236–238).** $n$ lamps light $m$ pixels; $l=Ap$, where column $j$ of $A$ is lamp $j$'s pattern at power 1. $A$ is assumed to have independent columns. For target $l^{\rm des}$ (e.g. $\alpha\mathbf 1$), $\hat p=A^\dagger l^{\rm des}=(A^TA)^{-1}A^Tl^{\rm des}$. Powers may come out negative or above the maximum; this is ignored.
- Setup: a $25\times25$ grid, $m=625$ pixels of 1 m². There are 10 lamps at heights 3 m to 6 m. $A_{ij}\propto d_{ij}^{-2}$ (inverse square law), scaled so all-ones power gives average illumination 1. Target is $\mathbf 1$.
- With $p=\mathbf 1$: RMS error 0.24, with dark corners and bright spots under the lamps.
- Least squares: $\hat p=(1.46,0.79,2.97,0.74,0.08,0.21,0.21,2.05,0.91,1.47)$, RMS error 0.14, about half. The pattern is more uniform (figures 12.5–12.6, pp. 237–238).

### Exercises (pp. 239–243)
Sixteen exercises, listed under "Exercises worth doing" below. No solutions are printed in these pages.

## Toy example (ours, not from the text)
Let $A=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$, $b=(1,1,0)$. The columns are independent.
1. $A^TA=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ (entries $1+1$, $0+1$, $0+1$, $1+1$). $A^Tb=(1+0,\ 0+1)=(1,1)$.
2. Normal equations: $2x_1+x_2=1$, $x_1+2x_2=1$. Subtract the second from the first: $x_1-x_2=0$. So $3x_1=1$ and $\hat x=(1/3,1/3)$.
3. $A\hat x=(1/3,1/3,2/3)$. $\hat r=A\hat x-b=(-2/3,-2/3,2/3)$. Then $\|\hat r\|^2=3\cdot4/9=4/3$.
4. Orthogonality: $A^T\hat r=(-2/3+0+2/3,\ 0-2/3+2/3)=(0,0)$ ✓.
5. Compare $x=(1/2,1/2)$: $Ax=(1/2,1/2,1)$, $r=(-1/2,-1/2,1)$, $\|r\|^2=1/4+1/4+1=3/2>4/3$ ✓.
6. Pythagoras (12.7 reduced): $x-\hat x=(1/6,1/6)$, $A(x-\hat x)=(1/6,1/6,1/3)$, norm squared $=(1+1+4)/36=1/6$. And $4/3+1/6=9/6=3/2$ ✓.

## Concepts
- [[least-squares]] — choose $x$ to minimize $\|Ax-b\|^2$ for tall $A$; the solution need not satisfy $Ax=b$ (p. 225)
- [[residual]] (new) — $r=Ax-b$; its norm is the quantity to be made small (p. 225)
- [[normal-equations]] (new) — $A^TA\hat x=A^Tb$, from setting $\nabla f=2A^T(Ax-b)$ to zero (p. 229)
- [[pseudoinverse]] — $A^\dagger=(A^TA)^{-1}A^T$ for independent columns; $\hat x=A^\dagger b$ (p. 229)
- [[orthogonality-principle]] (new) — optimal residual is orthogonal to every combination of the columns of $A$ (p. 231)
- [[projection]] — $A\hat x$ is the closest point to $b$ in the span of the columns (p. 231)
- [[gram-matrix]] (new) — $A^TA$, with inner products of columns as entries (p. 229)
- [[gram-schmidt-qr]] — QR factorization used to solve least squares: $\hat x=R^{-1}Q^Tb$ (p. 231)
- [[matrix-least-squares]] (new) — minimize $\|AX-B\|^2$; solved by $\hat X=A^\dagger B$ (p. 233)
- [[linear-independence]] — the assumption making the minimizer unique (p. 227)

## Canonical instances
- [[ls-three-equation-example]] (new) — $3\times2$ system with $\hat x=(1/3,-1/3)$, optimal squared residual $2/3$ (p. 227)
- [[advertising-purchases]] (new) — spend allocation to hit impression targets (p. 234)
- [[lamp-illumination]] (new) — lamp powers for near-uniform lighting (p. 236)

## Bridges (candidates)
- [structural-analogy] Normal equations, $\hat r\perp$ columns ↔ projection: $A\hat x$ is the closest point in the column space (the text uses the word "closest", not "projection", in the chapter; exercise 12.8 names it).
- [same-math] Matrix least squares $\hat X=A^\dagger B$ ↔ regression with several response variables: the same independent column-wise fits.
- [structural-analogy] Normal equations in row form (12.8) ↔ sequential updating of Gram sums (exercise 12.14 builds on it).

## Questions this raises
- What happens if the columns of $A$ are not linearly independent? The chapter assumes (12.2) throughout, so these pages do not say.
- How should we handle constraints such as nonnegative spend or maximum lamp power, which both examples ignore?
- Is $A^TA$ safe to form numerically, or is QR better? (The chapter presents QR as the algorithm but does not compare accuracy; see exercise 12.16 for cost.)
- Can residual components be weighted differently (exercise 12.4)?

## Exercises worth doing
- Ex. 12.1 (p. 239) — fitting $b$ by a multiple of $a$: optimal error is $\|b\|^2(\sin\theta)^2$; links least squares to the angle between vectors — easy
- Ex. 12.2 (p. 239) — with orthonormal columns, $\hat x=Q^Tb$; cheap special case — easy
- Ex. 12.3 (p. 239) — $\hat x$ also minimizes the angle between $Ax$ and $b$ — medium
- Ex. 12.8 (p. 240) — $A\hat x=QQ^Tb$ and $\|A\hat x-b\|^2=\|b\|^2-\|Q^Tb\|^2$ via QR — medium
- Ex. 12.14 (p. 242) — recursive least squares by updating $G^{(k)},h^{(k)}$ as rows arrive — medium
- Ex. 12.4 (p. 239) — weighted least squares reduces to ordinary least squares via a diagonal matrix — medium

## Reading notes
- Printed page = pdf page − 10. The last pdf page (254, printed 244) is blank.
- Exercise 12.12(c) (p. 241): the image shows "$p_8=(0,1)$, $p_8=(1,1)$". The second is presumably $p_9$, since the other fixed points are $p_7$ and $p_{10}$.
- p. 233: the text says that if $(\hat x,\hat y)$ solves (12.11), then "$\hat x$ satisfies (12.11)". From context, "the normal equations" is meant.
- Exercises appear with no printed solutions. Sections 12.1–12.4 are covered in L3; the exercises are only listed (six are selected below); the figures were read from the images.
