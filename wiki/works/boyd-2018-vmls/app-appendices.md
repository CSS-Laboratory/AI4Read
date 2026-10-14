---
id: boyd-2018-vmls/app-appendices
work: boyd-2018-vmls
unit: "Appendices (A Notation, B Complexity, C Derivatives and optimization, D Further study), plus the end of Exercise 19.3"
pages: 435–453
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
# Appendices: notation, flop counts, derivatives and Lagrange multipliers, further study

## L0 — One line
The appendices give the book's notation, the flop counts of its algorithms, the small calculus toolkit (gradient, Jacobian, Taylor approximation, KKT conditions) behind nonlinear least squares, and pointers to further study.

## L1 — The gist (≤ 120 words)
These pages support the book's main text. Appendix A lists notation. Appendix B tabulates approximate flop counts and gives a "big × small²" rule of thumb. Appendix C reviews the calculus needed for nonlinear and constrained nonlinear least squares: derivatives, gradients, Jacobians, first-order Taylor approximations, the optimality conditions ∇h = 0 and the KKT conditions for equality constraints. In each case a satisfied condition does not guarantee a minimizer. Appendix D names topics for further study. The unit also contains the end of Exercise 19.3, on Boolean least squares solved by the augmented Lagrangian method.

**Prerequisites:** matrices and vectors, matrix–vector product, transpose, norm, least squares; limits and derivatives of one variable.

## L2 — Key ideas (5–10 bullets)
- Sets use braces and are unordered without repeats; vectors use parentheses. Σ over i∈S sums over a set of indices (p. 440).
- Flop counts drop lower-order terms; for sparse operands and an algorithm modified to exploit sparsity they can be dramatically lower. Examples: Ax costs 2mn, QR costs 2mn², A⁻¹b costs 2n³ (pp. 441–442).
- Many two-dimension costs are of order (big) × (small)² flops, e.g. least squares 2mn² and least norm 2np² (p. 442).
- The first-order Taylor approximation is affine: f̂(x) = f(z) + Df(z)(x−z). It agrees with f at z and is a good approximation near z, but can be poor far away (pp. 443–446).
- The Jacobian Df(z) has entries ∂fᵢ/∂xⱼ. It gives ∇‖f(x)‖² = 2Df(z)ᵀf(z) (C.1) and the chain rule Df = Dg(h(z))Dh(z) (pp. 446–447).
- If x̂ minimizes h, then ∇h(x̂) = 0. The converse can fail, so candidate points must be checked (pp. 447–448).
- With equality constraints g(x) = 0, a solution x̂ has a multiplier vector ẑ with ∇h(x̂) + Dg(x̂)ᵀẑ = 0 and g(x̂) = 0, provided the rows of Dg(x̂) are linearly independent (p. 449).
- Exercise 19.3 casts Boolean least squares as a constrained nonlinear least squares problem with 2ⁿ feasible points, so brute force is not practical for n larger than about 30 (p. 435).

## L3 — Walkthrough

### End of Exercise 19.3: Boolean least squares (p. 435)
- The problem: minimize $\|Ax-b\|^2$ subject to $x_i^2 = 1$, $i=1,\dots,n$. The $m\times n$ matrix $A$ and $m$-vector $b$ are given. It is a special case of constrained nonlinear least squares (19.1) (p. 435).
- The constraints force each $x_i \in \{-1,+1\}$, so there are $2^n$ feasible vectors (p. 435).
- Brute force evaluates the objective at all $2^n$ points. It is "not practical for $n$ larger than 30 or so" (p. 435).
- Heuristics are much faster and find an $x$ with small, not necessarily smallest, objective. One is the augmented Lagrangian algorithm 19.2 (p. 435).
- Task (a): work out the Levenberg–Marquardt update step used in each iteration for this problem. Task (b): implement the algorithm. Start at the minimizer of $\|Ax-b\|^2$. Round each iterate with $\tilde x^{(k)}=\mathbf{sign}(x^{(k)})$, plot $\|A\tilde x^{(k)}-b\|^2$ and return the best rounded point. Test with $n=m=10$ against brute force, then with $n=m=500$ (p. 435).

### Appendix A: Notation (pp. 439–440)
- Vectors: $(x_1,\dots,x_n)$ is an $n$-vector; $x_{r:s}$ a subvector; $\mathbf 0$, $\mathbf 1$, $e_i$ the zero, all-ones and $i$th unit vector; $x^Ty$ the inner product; $\|x\|$ the norm; $\mathbf{rms}$, $\mathbf{avg}$, $\mathbf{std}$, $\mathbf{dist}$; $\angle(x,y)$ the angle; $x\perp y$ orthogonality (p. 439).
- Matrices: $X_{ij}$ entry; $X_{r:s,p:q}$ submatrix; $I$ identity; $X^T$ transpose; $\|X\|$ norm; $X^k$ power; $X^{-1}$ inverse; $X^{-T}$ inverse of transpose; $X^\dagger$ pseudo-inverse; $\mathbf{diag}(x)$ diagonal matrix (pp. 439–440).
- Functions: $f:A\to B$ is a function on set $A$ into set $B$. $\nabla f(z)$ is the gradient of $f:\mathbf R^n\to\mathbf R$ at $z$. $Df(z)$ is the Jacobian of $f:\mathbf R^n\to\mathbf R^m$ at $z$ (p. 440).
- Ellipsis: $k,\dots,l$ lists the integers from $k$ to $l$. $\sum_{i=1,\dots,n}a_i$ means $a_1+\cdots+a_n$ (p. 440).
- Sets: $\{a_1,\dots,a_n\}$ is a set, not the vector $(a_1,\dots,a_n)$. Order does not matter, e.g. $\{1,2,6\}=\{6,1,2\}$. A set has no repeated elements (p. 440).
  - $\{x\mid \text{condition}(x)\}$ is the set of $x$ satisfying the condition. $\in$ means "in" and $\notin$ means "not in".
  - $\sum_{i\in S}x_i$ sums over indices in $S$; e.g. $\sum_{i\in\{1,2,6\}}a_i=a_1+a_2+a_6$.
  - $\mathbf R$ is the set of real numbers (scalars). $\mathbf R^n$ is the set of $n$-vectors.

*Intuition note:* This is a lookup table. Note the difference between braces and parentheses: for a set, order does not matter and repeats are not allowed; a vector is written with parentheses.

### Appendix B: Complexity (pp. 441–442)
Counts are approximate flops (floating-point operations), with lower-order terms dropped. Sparse operands with a sparsity-aware algorithm can give dramatically lower counts (p. 441).

**Vector operations** ($x,y$ are $n$-vectors, $a$ a scalar) (p. 441):

| operation | flops |
|---|---|
| $ax$, $x+y$ | $n$ |
| $x^Ty$, $\|x\|$, $\mathbf{rms}(x)$ | $2n$ |
| $\|x-y\|$ | $3n$ |
| $\mathbf{std}(x)$ | $4n$ |
| $\angle(x,y)$ | $6n$ |

Convolution of an $n$-vector and an $m$-vector, by a special algorithm, takes $5(m+n)\log_2(m+n)$ flops (p. 441).

**Matrix operations** ($A,B$ are $m\times n$; $C$ is $n\times p$) (p. 441):

| operation | flops |
|---|---|
| $aA$, $A+B$ | $mn$ |
| $Ax$, $\|A\|$ | $2mn$ |
| $AC$ | $2mnp$ |
| $A^TA$ | $mn^2$ |

**Factorizations and inverses** ($A$ tall or square $m\times n$, $R$ triangular $n\times n$; the objects are assumed to exist, and $A$ must be square wherever $A^{-1}$ appears) (p. 442):

| operation | flops |
|---|---|
| QR factorization of $A$ | $2mn^2$ |
| $R^{-1}b$ | $n^2$ |
| $A^{-1}b$ | $2n^3$ |
| $A^{-1}$ | $3n^3$ |
| $A^\dagger$ | $3mn^2$ |

For a wide $A$ with linearly independent rows, $A^\dagger$ takes $3m^2n$ flops (p. 442).

**Least squares problems** ($C$ wide $p\times n$; independence conditions assumed) (p. 442):

| problem | flops |
|---|---|
| minimize $\|Ax-b\|^2$ | $2mn^2$ |
| minimize $\|Ax-b\|^2$ s.t. $Cx=d$ | $2(m+p)n^2+2np^2$ |
| minimize $\|x\|^2$ s.t. $Cx=d$ | $2np^2$ |

**Big-times-small-squared mnemonic.** Many costs with two dimensions are of order (big) × (small)² flops (p. 442). Examples:
- The Gram matrix of a tall $m\times n$ matrix costs $mn^2$ ($m$ big, $n$ small).
- QR costs $2mn^2$ ($m\ge n$).
- $A^\dagger$ costs $3mn^2$ for tall $A$ and $3nm^2$ for wide $A$.
- Least squares costs $2mn^2$ ($m\ge n$).
- The least norm problem costs $2np^2$ ($p\le n$, so $n$ is big).
- Constrained least squares involves the stacked matrix $\begin{bmatrix}A\\C\end{bmatrix}$, with big dimension $m+p$ and small dimension $n$ ($m+p\ge n$). The cost $2(m+p)n^2+2np^2$ lies between $2(m+p)n^2$ and $4(m+p)n^2$ (p. 442).

*Intuition note:* For many of the two-dimension costs, the cost is of order the big dimension times the square of the small dimension, so knowing which dimension is small helps you estimate what a method costs.

### Appendix C: Derivatives and optimization (pp. 443–449)
Calculus does not play a big role in the book, except in chapters 18–19, where derivatives, Taylor approximations and Lagrange multipliers are used (p. 443).

**C.1.1 Scalar function of a scalar (pp. 443–444).**
- The derivative of $f:\mathbf R\to\mathbf R$ at $z$, if the limit exists, is
$$f'(z)=\lim_{t\to 0}\frac{f(z+t)-f(z)}{t}.$$
It is the slope of the graph at $(z,f(z))$ (p. 443).
- First-order Taylor approximation at $z$: $\hat f(x)=f(z)+f'(z)(x-z)$. Here $x-z$ is the deviation, and $f'(z)(x-z)$ approximates the resulting change in $f$ (p. 443).
- Notation $\hat f(x;z)$ shows the point $z$. $\hat f$ is called the "linearized" approximation but is affine, a linear function plus a constant. It satisfies $\hat f(z;z)=f(z)$. For $x$ near $z$ it is a very good approximation; for $x$ not close enough to $z$ it can be poor (p. 444).
- Rules: $f(x)=x^2$ gives $f'(z)=2z$; $f(x)=e^x$ gives $f'(z)=e^z$. Chain rule: if $f(x)=g(h(x))$ then $f'(z)=g'(h(z))h'(z)$. Product rule: $f=gh$ gives $f'(z)=g'(z)h(z)+g(z)h'(z)$. Linearity: $f=ag+bh$ gives $f'(z)=ag'(z)+bh'(z)$ (p. 444).

**C.1.2 Scalar function of a vector (pp. 444–445).**
- Partial derivative of $f:\mathbf R^n\to\mathbf R$ at $z$ in argument $i$, if the limit exists:
$$\frac{\partial f}{\partial x_i}(z)=\lim_{t\to0}\frac{f(z+te_i)-f(z)}{t}.$$
Roughly, it is the derivative in argument $i$ with the others fixed (p. 444).
- Gradient: the $n$-vector $\nabla f(z)$ with entries $\frac{\partial f}{\partial x_i}(z)$ (p. 445).
- Taylor approximation: $\hat f(x)=f(z)+\frac{\partial f}{\partial x_1}(z)(x_1-z_1)+\cdots+\frac{\partial f}{\partial x_n}(z)(x_n-z_n)$, in compact form
$$\hat f(x;z)=f(z)+\nabla f(z)^T(x-z).$$
It is affine in $x$, agrees with $f$ at $z$, and is very good when all $x_i$ are near $z_i$ (p. 445).
- Example: $f(x)=\|x\|^2=x_1^2+\cdots+x_n^2$ has $\frac{\partial f}{\partial x_i}(z)=2z_i$, so $\nabla f(z)=2z$. This resembles the scalar derivative of $x^2$ (p. 445).
- Linearity holds for gradients: $f=ag+bh$ gives $\nabla f(z)=a\nabla g(z)+b\nabla h(z)$ (p. 445).

**C.1.3 Vector function of a vector (pp. 446–447).**
- $f:\mathbf R^n\to\mathbf R^m$ has components $f_1(x),\dots,f_m(x)$ (p. 446).
- Jacobian (derivative matrix), shape $m\times n$:
$$Df(z)_{ij}=\frac{\partial f_i}{\partial x_j}(z),\quad i=1,\dots,m,\; j=1,\dots,n.$$
"$Df$" is one symbol, not a product. Its rows are $\nabla f_i(z)^T$. For $m=1$ it is the row vector $\nabla f(z)^T$ (p. 446).
- Taylor approximation: $\hat f(x)_i=f_i(z)+\nabla f_i(z)^T(x-z)$, i.e.
$$\hat f(x)=f(z)+Df(z)(x-z).$$
It is affine, not in general linear, and very good for $x$ near $z$ (p. 446).
- Worked derivation. Let $h(x)=\|f(x)\|^2=f_1(x)^2+\cdots+f_m(x)^2$ (p. 446). Then
$$\frac{\partial h}{\partial x_j}(z)=2f_1(z)\frac{\partial f_1}{\partial x_j}(z)+\cdots+2f_m(z)\frac{\partial f_m}{\partial x_j}(z).$$
Arranged as a row vector, $Dh(z)=2f(z)^TDf(z)$. Transposing,
$$\nabla h(z)=2Df(z)^Tf(z).\tag{C.1}$$
This parallels $h'(z)=2f'(z)f(z)$ for $h=f^2$ in the scalar case (p. 447).
- Chain rule: if $f(x)=g(h(x))$ with $h:\mathbf R^n\to\mathbf R^k$ and $g:\mathbf R^k\to\mathbf R^m$, then
$$Df(z)=Dg(h(z))\,Dh(z),$$
a matrix product. Order matters (p. 447).

*Intuition note:* Near $z$, a function is well approximated by an affine map whose matrix is the Jacobian. Many scalar derivative formulas, such as the chain rule, carry over with products replaced by matrix products in the right order.

**C.2 Optimization (pp. 447–448).**
- Scalar case: if $\hat x$ minimizes $h$, then $h'(\hat x)=0$. Reason: if $h'(\hat x)\ne0$, a point slightly to the left (if $h'(\hat x)>0$) or slightly to the right (if $h'(\hat x)<0$) gives a smaller value. Points with $h'(\hat x)=0$ need not be minimizers, so they must be checked (p. 447).
- Vector case: if $\hat x$ minimizes $h:\mathbf R^n\to\mathbf R$, then $\frac{\partial h}{\partial x_i}(\hat x)=0$ for all $i$, i.e. $\nabla h(\hat x)=0$. Again the converse can fail (pp. 447–448).
- Nonlinear least squares: with $h(x)=\|f(x)\|^2$, the condition is $2Df(\hat x)^Tf(\hat x)=0$, using (C.1). A minimizer satisfies it, but points satisfying it need not solve the problem (p. 448).

**C.3 Lagrange multipliers (pp. 448–449).**
- Problem: minimize $h:\mathbf R^n\to\mathbf R$ subject to $g(x)=0$, where $g=(g_1,\dots,g_p)$. A solution $\hat x$ is feasible ($g(\hat x)=0$) and $h(x)\ge h(\hat x)$ for every other feasible $x$ (p. 448).
- Lagrangian, with multiplier vector $z\in\mathbf R^p$:
$$L(x,z)=h(x)+z_1g_1(x)+\cdots+z_pg_p(x)=h(x)+g(x)^Tz.$$
One term is added per constraint (p. 448).
- KKT conditions (Karush, Kuhn, Tucker): if $\hat x$ solves the problem, then there is $\hat z$ with $\frac{\partial L}{\partial x_i}(\hat x,\hat z)=0$ for $i=1,\dots,n$ and $\frac{\partial L}{\partial z_i}(\hat x,\hat z)=0$ for $i=1,\dots,p$. This holds provided the rows of $Dg(\hat x)$ are linearly independent, a technical condition the author ignores. Pairs satisfying KKT may have $\hat x$ not a solution. The method is to solve the KKT equations, then check the solutions found (p. 449).
- Compact form. The last $p$ equations say $g_i(\hat x)=0$. The first $n$ say $\nabla_xL(\hat x,\hat z)=0$, i.e.
$$\nabla h(\hat x)+\hat z_1\nabla g_1(\hat x)+\cdots+\hat z_p\nabla g_p(\hat x)=\nabla h(\hat x)+Dg(\hat x)^T\hat z=0.$$
So the KKT conditions are $\nabla h(\hat x)+Dg(\hat x)^T\hat z=0$ and $g(\hat x)=0$ (p. 449).
- Constrained nonlinear least squares: minimize $\|f(x)\|^2$ subject to $g(x)=0$. With $h=\|f\|^2$ and $\nabla h(\hat x)=2Df(\hat x)^Tf(\hat x)$, the KKT conditions are
$$2Df(\hat x)^Tf(\hat x)+Dg(\hat x)^T\hat z=0,\qquad g(\hat x)=0.$$
They hold for a solution if the rows of $Dg(\hat x)$ are linearly independent, but other points may satisfy them (p. 449).

*Intuition note:* At a constrained minimum, provided the rows of $Dg$ are linearly independent, the objective's gradient is cancelled by a combination of the constraint gradients, with multipliers as weights. This extends the unconstrained condition $\nabla h=0$. For both conditions, points satisfying them need not be minimizers.

### Appendix D: Further study (pp. 451–453)
Topics are grouped, but the groups overlap (p. 451).
- **Mathematics.**
  - Probability and statistics: not used in the book. The author "strongly encourage[s]" learning them, while noting that topics like data fitting can be discussed without them (p. 451).
  - Abstract linear algebra: vector spaces, subspaces, nullspace, range, eigenvalues, singular values and the matrix exponential. These let one handle least squares when the columns are not linearly independent (p. 451).
  - Optimization: inequality constraints; convex optimization, which can be solved efficiently and non-heuristically; non-convex methods (pp. 451–452).
- **Computer science.**
  - Languages and packages for linear algebra, to carry out numerical calculations (p. 452).
  - Computational linear algebra: floating point and round-off error, sparse matrices, iterative methods for huge problems (p. 452).
- **Applications** (pp. 452–453).
  - Machine learning: unsupervised methods (PCA, nonnegative matrix factorization), logistic regression, support vector machines, large-scale methods; deep neural networks are mentioned as a possible additional topic.
  - Linear dynamical systems, control and estimation: continuous-time systems and the matrix exponential.
  - Finance: factor models, transaction costs, leverage limits, long-only portfolios.
  - Signal and image processing: convolution, Fourier transform, convex optimization, neural networks.
  - Time series analysis: prediction, finance, supply chain.

## Toy example (ours, not from the text)
Let $f:\mathbf R^2\to\mathbf R^2$, $f(x)=(x_1^2,\;x_1+x_2)$, and $z=(1,2)$. Let $h(x)=\|f(x)\|^2=x_1^4+(x_1+x_2)^2$.

*Direct gradient:* $\partial h/\partial x_1=4x_1^3+2(x_1+x_2)=4+2\cdot3=10$ and $\partial h/\partial x_2=2(x_1+x_2)=6$. So $\nabla h(z)=(10,6)$.

*Via (C.1):* $f(z)=(1,3)$ and $Df(z)=\begin{bmatrix}2x_1&0\\1&1\end{bmatrix}=\begin{bmatrix}2&0\\1&1\end{bmatrix}$, so $Df(z)^T=\begin{bmatrix}2&1\\0&1\end{bmatrix}$.
$Df(z)^Tf(z)=(2\cdot1+1\cdot3,\;0\cdot1+1\cdot3)=(5,3)$. Doubling gives $(10,6)$. ✓.

*Taylor check:* take $x=(1.1,2)$, so $x-z=(0.1,0)$. $\hat f(x)=f(z)+Df(z)(x-z)=(1,3)+(0.2,0.1)=(1.2,3.1)$. The true value is $f(x)=(1.21,3.1)$, so the approximation is close.

*KKT:* minimize $h(x)=x_1^2+x_2^2$ subject to $g(x)=x_1+x_2-2=0$. Then $\nabla h=2x$ and $Dg=[1\;1]$, so the conditions are $2x_1+\hat z=0$, $2x_2+\hat z=0$, $x_1+x_2=2$. The first two give $x_1=x_2=-\hat z/2$. The third gives $-\hat z=2$, so $\hat z=-2$ and $\hat x=(1,1)$. The single row of $Dg$ is nonzero, hence linearly independent.

## Concepts
- [[gradient]] (new) — vector of partial derivatives of a scalar function of a vector; $\nabla\|x\|^2=2x$ (p. 445)
- [[jacobian-derivative-matrix]] (new) — $m\times n$ matrix $Df(z)_{ij}=\partial f_i/\partial x_j$; rows are $\nabla f_i^T$ (p. 446)
- [[taylor-approximation]] (new) — affine approximation $f(z)+Df(z)(x-z)$, good near $z$, possibly poor far away (pp. 443–446)
- [[chain-rule]] (new) — $Df(z)=Dg(h(z))Dh(z)$ for $f=g\circ h$ (p. 447)
- [[matrix multiplication as composition]] — the matrix chain rule uses matrix products for composed functions (p. 447)
- [[gradient-condition-for-minimization]] (new) — a minimizer of $h$ has $\nabla h=0$; the converse can fail (pp. 447–448)
- [[nonlinear-least-squares]] (new) — minimize $\|f(x)\|^2$; condition $2Df(\hat x)^Tf(\hat x)=0$ (p. 448)
- [[lagrange-multipliers]] (new) — Lagrangian $L(x,z)=h(x)+g(x)^Tz$ for equality constraints (p. 448)
- [[kkt-conditions]] (new) — $\nabla h+Dg^T\hat z=0$, $g=0$; necessary under a linear-independence condition (p. 449)
- [[flop-count]] (new) — approximate number of arithmetic operations, lower-order terms dropped (p. 441)
- [[big-times-small-squared]] (new) — cost mnemonic (big)×(small)² (p. 442)
- [[least squares]] — cost $2mn^2$ flops (p. 442)
- [[Gram–Schmidt and QR]] — QR factorization costs $2mn^2$ flops (p. 442)
- [[pseudoinverse]] — $3mn^2$ flops (tall), $3m^2n$ (wide) (p. 442)
- [[boolean-least-squares]] (new) — least squares with entries restricted to $\pm1$; $2^n$ feasible points (p. 435)

## Canonical instances
- [[boolean-least-squares]] — a constrained nonlinear least squares special case whose brute force method is not practical for $n$ larger than about 30 (p. 435)
- [[gradient-of-sum-of-squares]] — $\nabla\|x\|^2=2z$ at $z$ (p. 445)
- [[gradient-of-squared-norm-of-vector-function]] — $\nabla h(z)=2Df(z)^Tf(z)$ (p. 447)
- [[constrained-nonlinear-least-squares-kkt]] — KKT system $2Df^Tf+Dg^T\hat z=0$, $g=0$ (p. 449)

## Bridges (candidates)
- [same-math] chain rule $Df=Dg\,Dh$ ↔ linear-algebra: matrix multiplication as composition — the Jacobian of a composition is the product of Jacobians.
- [same-math] condition $2Df(\hat x)^Tf(\hat x)=0$ ↔ least squares normal equations — the condition reduces to $A^T(Ax-b)=0$ when $f(x)=Ax-b$, since then $Df=A$ (our step; the text does not state this).
- [structural-analogy] KKT conditions ↔ the KKT linear system of constrained least squares — in the linear case, $\nabla h+Dg^T\hat z=0$ and $g=0$ become linear equations (this unit does not state it).
- [metaphor] Taylor approximation ↔ local linear model of a nonlinear system — an affine map that is accurate only near the expansion point.

## Questions this raises
- When does a point with $\nabla h(\hat x)=0$ actually minimize $h$? The appendix says only that it must be checked.
- How is $\|Ax-b\|^2$ with $x_i^2=1$ solved by Levenberg–Marquardt inside the augmented Lagrangian method, and how good is the rounded solution?
- What happens to the KKT conditions if the rows of $Dg(\hat x)$ are not linearly independent?
- How do the flop counts change for sparse matrices, and by how much?

## Exercises worth doing
- Ex. 19.3(a) (p. 435) — derive the Levenberg–Marquardt update step for Boolean least squares inside the augmented Lagrangian method — difficulty: medium
- Ex. 19.3(b) (p. 435) — implement it, round with sign, compare to brute force at $n=m=10$, and run at $n=m=500$ — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 10 (pdf 445 = p. 435). Pages 436, 438, 450 and 454 are blank. Page 437 is the "Appendices" divider. Page 453 has a number but no running header.
- The unit opens with the end of Exercise 19.3, which belongs to chapter 19. The appendix text itself starts at p. 439.
- The red numbers in the Notation tables are page references into the main text, which is outside this unit. The chain rule is also said to be "described on page 184" (p. 447); that page is not in this unit.
- On p. 448 the sentence on non-minimizers writes $\nabla h(z)=0$ with $z$ where the context uses $\hat x$. The context suggests $\hat x$ is meant.
- Only Exercise 19.3 appears here. No solutions are printed.
