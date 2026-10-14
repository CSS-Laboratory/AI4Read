---
id: boyd-2018-vmls/ch10-matrix
work: boyd-2018-vmls
unit: "Chapter 10 — Matrix multiplication"
pages: 177-198
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
# Matrix multiplication

## L0 — One line
Multiplying matrices means composing linear functions (do B, then A), and this one operation unifies inner and outer products, Gram matrices, powers, path counting, dynamics and QR factorization.

## L1 — The gist (≤ 120 words)
The chapter defines the product C = AB entry by entry. It then shows four equivalent views: columns, rows, inner products and sums of outer products. Because AB means "apply B, then A", order matters and AB ≠ BA in general. The same view gives a compact form of the chain rule and of closed-loop dynamics, and shows why powers Aˡ propagate a linear system ℓ steps. Powers of an adjacency matrix count paths. Gram matrices AᵀA collect all column inner products. Orthonormal columns (QᵀQ = I) preserve norms, inner products and angles, and Gram–Schmidt is written compactly as A = QR. The order in which a product is evaluated can change its cost sharply.

**Prerequisites:** vectors, inner product, transpose, matrix–vector product, block matrices, linear and affine functions, Gram–Schmidt (§5.4), flop counts, adjacency matrix, derivative matrix.

## L2 — Key ideas
- The product of an m×p matrix and a p×n matrix is the m×n matrix with entries $C_{ij}=\sum_k A_{ik}B_{kj}$. It includes inner, outer, matrix–vector and scalar–vector products as special cases (pp. 177–178).
- Multiplication is associative and distributive, and $(AB)^T=B^TA^T$. It is not commutative: the order of the factors matters (pp. 178–179).
- There are several equivalent readings of AB. These are columns $Ab_j$, rows $(B^Ta_i)^T$, mn inner products, and a sum of p outer products. Each gives extra insight into the product (pp. 180–181).
- The Gram matrix $G=A^TA$ holds all inner products of the columns of A. It is symmetric, and for a 0/1 membership matrix it counts shared members (p. 181).
- AB costs about 2mnp flops. The bracketing of a triple product changes the cost: $ab^Tc$ costs 3n flops if $b^Tc$ is formed first and 3n² otherwise (pp. 182–183).
- AB is the matrix of the composition f(g(x)). This gives the second difference matrix, composition of affine maps, the chain rule $Dh(z)=Df(g(z))Dg(z)$, and the closed-loop matrix A+BK (pp. 183–186).
- $(A^\ell)_{ij}$ counts paths of length ℓ from vertex j to vertex i, and $x_{t+\ell}=A^\ell x_t$ in a linear dynamical system (pp. 186–189).
- Orthonormal columns ($A^TA=I$) preserve norm, inner product and angle. Gram–Schmidt gives the QR factorization A = QR, with Q having orthonormal columns and R upper triangular with positive diagonal (pp. 189–190).

## L3 — Walkthrough

### 10.1 Matrix-matrix multiplication (pp. 177–183)

**Definition.** A and B are *compatible* if the number of columns of A equals the number of rows of B. If A is m×p and B is p×n, the product C = AB is m×n with
$$C_{ij}=\sum_{k=1}^{p}A_{ik}B_{kj}=A_{i1}B_{1j}+\cdots+A_{ip}B_{pj},\quad i=1,\dots,m,\ j=1,\dots,n. \tag{10.1}$$
Mnemonic: move left to right along row i of A and top to bottom down column j of B, keeping a running sum of products (p. 177).

Example (p. 177):
$$\begin{bmatrix}-1.5&3&2\\1&-1&0\end{bmatrix}\begin{bmatrix}-1&-1\\0&-2\\1&0\end{bmatrix}=\begin{bmatrix}3.5&-4.5\\-1&1\end{bmatrix}.$$
The 1,2 entry is $(-1.5)(-1)+(3)(-2)+(2)(0)=-4.5$ (p. 177).

**Special cases** (p. 178):
- *Scalar–vector.* Treat x as n×1 and a as 1×1. Then xa is a matrix product. The conventional ax cannot be read as a matrix product unless n = 1, because a has one column and x has n rows.
- *Inner product.* $a^Tb$ is the product of the 1×n matrix aᵀ and the n×1 matrix b. The result is 1×1, which we treat as a scalar.
- *Matrix–vector.* y = Ax is the product of A with the n×1 matrix x.
- *Outer product.* For an m-vector a and an n-vector b, abᵀ is the m×n matrix with entries $a_ib_j$. In general $ab^T\ne ba^T$. The equation does not even make sense unless m = n, and even then it is not true in general.
- *Identity.* AI = A and IA = A. The two identity matrices have different sizes.

**Order matters.** In general AB ≠ BA. BA may not exist, or may have a different size. If A is 2×3 and B is 3×4, then AB exists but BA does not. Even for square matrices, AB ≠ BA in general. Example (pp. 178–179): $A=\begin{bmatrix}1&6\\9&3\end{bmatrix}$, $B=\begin{bmatrix}0&-1\\-1&2\end{bmatrix}$ give $AB=\begin{bmatrix}-6&11\\-3&-3\end{bmatrix}$ and $BA=\begin{bmatrix}-9&-3\\17&0\end{bmatrix}$. If AB = BA, the matrices *commute*, and both must then be square (p. 179).

**Properties** (easy to verify from the definition; all products assumed defined; γ a scalar) (p. 179):
- Associativity: (AB)C = A(BC), so we may write ABC.
- γ(AB) = (γA)B = A(γB).
- Distributivity: A(B+C) = AB + AC and (A+B)C = AC + BC.
- Transpose of a product: $(AB)^T=B^TA^T$, in the opposite order.
- Consequence for square matrices of the same size: (A+B)(C+D) = AC + AD + BC + BD, with the order of factors preserved.
- For A m×n, x an n-vector and y an m-vector: $y^T(Ax)=(y^TA)x=(A^Ty)^Tx$. The inner product of y and Ax equals the inner product of x and Aᵀy.

**Block matrices.** If A has m×p block entries $A_{ij}$ and B has p×n block entries $B_{ij}$, and each $A_{ik}B_{kj}$ makes sense (the blocks *conform*), then AB has blocks given by (10.1). Example: $\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}E&F\\G&H\end{bmatrix}=\begin{bmatrix}AE+BG&AF+BH\\CE+DG&CF+DH\end{bmatrix}$. The order of the factors must be kept (pp. 179–180).

**Four readings of AB** (A is m×p, B is p×n):
1. *Columns* (p. 180). With columns $b_k$ of B, $AB=A[b_1\ \cdots\ b_n]=[Ab_1\ \cdots\ Ab_n]$. A is "applied" to each column of B. Consequence: k linear systems $Ax_i=b_i$ with the same coefficient matrix A are written compactly as AX = B, with $X=[x_1\cdots x_k]$ and $B=[b_1\cdots b_k]$. This is a "linear equation with matrix right-hand side".
2. *Rows* (p. 180). With rows $a_1^T,\dots,a_m^T$ of A, $AB$ has rows $a_i^TB=(B^Ta_i)^T$. So the rows of AB come from applying Bᵀ to the transposed rows of A and transposing the result.
3. *Inner products* (p. 181). $AB$ is the m×n matrix of the mn inner products $a_i^Tb_j$.
4. *Outer products* (p. 181). If $a_1,\dots,a_p$ are the columns of A and $b_1^T,\dots,b_p^T$ the rows of B, then $AB=a_1b_1^T+\cdots+a_pb_p^T$.

> **Intuition note.** The same sum $\sum_k A_{ik}B_{kj}$ can be grouped three ways. Group by entry and you get inner products. Group by column of B and you get "A applied to each column". Group by k and you get a sum of p rank-one pieces. Each grouping gives its own insight.

**Gram matrix** (p. 181). For an m×n matrix A with columns $a_1,\dots,a_n$, $G=A^TA$ is the Gram matrix of those vectors. Its entries are $G_{ij}=a_i^Ta_j$, so it contains all inner products of pairs of columns. It is symmetric because $a_i^Ta_j=a_j^Ta_i$. The transpose rule gives the same: $G^T=(A^TA)^T=(A^T)(A^T)^T=A^TA=G$. The author says the Gram matrix will play an important role later in the book.

Example (p. 181): let $A_{ij}=1$ if item i is in group j and 0 otherwise (m items, n groups). Then $G_{ij}$ is the number of items in both groups i and j, and $G_{ii}$ is the number of items in group i.

**Complexity** (pp. 182–183):
- *Dense product.* C = AB has mn entries. Each is an inner product of length-p vectors, which costs 2p − 1 flops. The total is mn(2p − 1), approximated by 2mnp flops. The order of the cost is mnp (p. 182).
- *Gram matrix.* For the n×n Gram matrix $G=B^TB$ one need only compute half of the entries, since G is symmetric. This saves about half, giving around pn² flops. The order is the same (p. 182).
- *Sparse times non-sparse.* Suppose A is m×p and sparse, and B is p×n. The product of row $a_i^T$ with a column of B costs at most $2\,\mathbf{nnz}(a_i^T)$ flops. Summing over i and j gives $2\,\mathbf{nnz}(A)\,n$ flops. If B is sparse the bound is $2\,\mathbf{nnz}(B)\,m$. These agree with 2mnp when all entries are nonzero. For two sparse matrices there is no simple formula, but the cost is at most $2\min\{\mathbf{nnz}(A)n,\mathbf{nnz}(B)m\}$ flops (p. 182).
- *Triple product* D = ABC, with A m×n, B n×p, C p×q (p. 182):
  - (AB)C costs 2mnp + 2mpq = 2mp(n+q) flops.
  - A(BC) costs 2npq + 2mnq = 2nq(m+p) flops.
  - The first is cheaper when $2mp(n+q)<2nq(m+p)$, i.e. when $\frac1n+\frac1q<\frac1m+\frac1p$.
  - Example: if m = p and n = q, the first costs proportional to m²n and the second to mn². The first is preferred when m ≪ n.
- *Example $ab^Tc$* with n-vectors (pp. 182–183). Forming the outer product abᵀ first costs n² flops and n² storage. Multiplying by c costs 2n², so the total is 3n². Forming the inner product bᵀc first costs 2n flops and stores one number. Scaling a by it costs n, so the total is 3n.

### 10.2 Composition of linear functions (pp. 183–186)

**Product = composition** (p. 183). Let A be m×p and B be p×n, with $f(x)=Ax$ ($\mathbf R^p\to\mathbf R^m$) and $g(x)=Bx$ ($\mathbf R^n\to\mathbf R^p$). The composition is
$$h(x)=f(g(x))=A(Bx)=(AB)x.$$
In the formula f is on the left of g, but g is applied first. h is linear with matrix C = AB. This explains why AB ≠ BA in general: ABx applies B first, and BAx applies A first.

Example (p. 183): $A=\begin{bmatrix}-1&0\\0&1\end{bmatrix}$ (changes the sign of $x_1$), $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ (swaps the two entries). Then $AB=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ and $BA=\begin{bmatrix}0&1\\-1&0\end{bmatrix}$. Also $ABx=(-x_2,x_1)$, while $BAx=(x_2,-x_1)$.

**Second difference matrix** (pp. 183–184). $D_n$ is the (n−1)×n difference matrix from (6.5), and $D_nx=(x_2-x_1,\dots,x_n-x_{n-1})$. The product $\Delta=D_{n-1}D_n$ is (n−2)×n and gives second differences:
$$D_{n-1}D_nx=(x_1-2x_2+x_3,\ x_2-2x_3+x_4,\ \dots,\ x_{n-2}-2x_{n-1}+x_n).$$
For n = 5:
$$\begin{bmatrix}1&-2&1&0&0\\0&1&-2&1&0\\0&0&1&-2&1\end{bmatrix}=\begin{bmatrix}-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{bmatrix}\begin{bmatrix}-1&1&0&0&0\\0&-1&1&0&0\\0&0&-1&1&0\\0&0&0&-1&1\end{bmatrix}.$$
Here $\Delta$ maps 5-vectors to 3-vectors, $D_4$ maps 4-vectors to 3-vectors, and $D_5$ maps 5-vectors to 4-vectors (p. 184).

**Composition of affine functions** (p. 184). Let $f(x)=Ax+b$ and $g(x)=Cx+d$. Then
$$h(x)=f(g(x))=A(Cx+d)+b=(AC)x+(Ad+b)=\tilde Ax+\tilde b,\quad \tilde A=AC,\ \tilde b=Ad+b.$$
So the composition is affine.

**Chain rule** (pp. 184–185). Let f: $\mathbf R^p\to\mathbf R^m$ and g: $\mathbf R^n\to\mathbf R^p$ be differentiable, and $h(x)=f(g(x))$. Then h is differentiable and
$$\frac{\partial h_i}{\partial x_j}(z)=\frac{\partial f_i}{\partial y_1}(g(z))\frac{\partial g_1}{\partial x_j}(z)+\cdots+\frac{\partial f_i}{\partial y_p}(g(z))\frac{\partial g_p}{\partial x_j}(z).$$
In matrix form, the derivative matrix is $Dh(z)=Df(g(z))\,Dg(z)$. This generalizes $h'(z)=f'(g(z))g'(z)$.

First-order Taylor approximation: $\hat h(x)=h(z)+Dh(z)(x-z)=f(g(z))+Df(g(z))Dg(z)(x-z)$. This equals the composition $\hat f(\hat g(x))$ of the two Taylor approximations $\hat f(y)=f(g(z))+Df(g(z))(y-g(z))$ and $\hat g(x)=g(z)+Dg(z)(x-z)$. The text checks this in three lines: substitute $\hat g(x)$ into $\hat f$, then cancel $g(z)-g(z)$ (p. 185).

For scalar-valued f (m = 1), $\nabla h(z)=Dg(z)^T\nabla f(g(z))$. If g(x) = Ax + b is affine, then $\nabla h(z)=A^T\nabla f(Az+b)$ (p. 185).

> **Intuition note.** Near a point, a smooth map looks like an affine map. Composing the maps then multiplies their derivative matrices, just as composing linear maps multiplies their matrices. The chain rule is matrix multiplication of local linear approximations.

**Linear dynamical system with state feedback** (pp. 185–186). Take $x_{t+1}=Ax_t+Bu_t$ with n-vector state and m-vector input. In state feedback control the input is a linear function of the measured state, $u_t=Kx_t$, where K is the m×n *state-feedback gain matrix*. The state affects the input and the input affects the next state, which forms a loop. Then
$$x_{t+1}=Ax_t+B(Kx_t)=(A+BK)x_t.$$
This is the *closed-loop system* with *closed-loop dynamics matrix* A + BK. The recursion $x_{t+1}=Ax_t$ (u = 0) is the *open-loop system* (p. 186).

### 10.3 Matrix power (pp. 186–189)

**Powers** (p. 186). For square A, $A^k$ is k copies of A multiplied. $A^kA^l=A^{k+l}$ and $(A^k)^l=A^{kl}$, with the convention $A^0=I$. Notation ambiguity: $A^T$ may mean the transpose or the Tth power. Usually the context, or an explicit statement by the author, shows which is meant; for non-square A it can only be the transpose. Negative powers are deferred to §11.2. Non-integer powers such as $A^{1/2}$ need not make sense, or can be ambiguous, unless conditions on A hold; the book does not pursue this (p. 186).

**Paths in a directed graph** (pp. 186–187). Let A be the adjacency matrix with $A_{ij}=1$ if there is an edge from vertex j to vertex i, and 0 otherwise. A path of length ℓ is a sequence of ℓ+1 vertices with an edge from each vertex to the next. By convention, each vertex has a path of length zero to itself.

Claim: $(A^\ell)_{ij}$ is the number of paths of length ℓ from vertex j to vertex i.
- *Case ℓ = 2.* $(A^2)_{ij}=\sum_kA_{ik}A_{kj}$. Each term is 1 only if there is an edge j→k and an edge k→i, i.e. a path of length exactly two via k. Summing over k counts all such paths (p. 187).
- *Induction.* Assume the claim for ℓ. Then $(A^{\ell+1})_{ij}=\sum_kA_{ik}(A^\ell)_{kj}$. The kth term is the number of paths of length ℓ from j to k if there is an edge k→i, and 0 otherwise. This counts the paths of length ℓ+1 from j to i whose last edge is (k, i). Summing over k gives all of them (p. 187).

Example (figure 10.1, five vertices) (pp. 187–188):
$$A=\begin{bmatrix}0&1&0&0&1\\1&0&1&0&0\\0&0&1&1&1\\1&0&0&0&0\\0&0&0&1&0\end{bmatrix},\quad A^2=\begin{bmatrix}1&0&1&1&0\\0&1&1&1&2\\1&0&1&2&1\\0&1&0&0&1\\1&0&0&0&0\end{bmatrix},\quad A^3=\begin{bmatrix}1&1&1&1&2\\2&0&2&3&1\\2&1&1&2&2\\1&0&1&1&0\\0&1&0&0&1\end{bmatrix}.$$
- There is one path of length two from vertex 1 to itself, (1,2,1), and one from vertex 3 to vertex 1, (3,2,1).
- $(A^2)_{34}=2$, from the paths (4,3,3) and (4,5,3).
- $(A^3)_{24}=3$, from the paths (4,3,3,2), (4,5,3,2) and (4,5,1,2).

**Linear dynamical system** (pp. 188–189). For $x_{t+1}=Ax_t$ we have $x_{t+2}=A(Ax_t)=A^2x_t$, and in general $x_{t+\ell}=A^\ell x_t$. So $A^\ell$ propagates the state ℓ steps forward.

In a population model, $A^\ell$ maps the current population distribution to the one ℓ periods ahead. The total population then is $\mathbf 1^T(A^\ell x_t)=(\mathbf 1^TA^\ell)x_t$. The ith entry of the row vector $\mathbf 1^TA^\ell$ is the contribution to the total population in ℓ periods from each person of current age i − 1. Figure 10.2 plots it for ℓ = 10 with the US data of §9.2. In the plot the factor is about 1 at age 0, peaks near 1.5 around age 25, and falls to 0 at about age 90 (p. 188).

With an input: $x_{t+2}=A(Ax_t+Bu_t)+Bu_{t+1}=A^2x_t+ABu_t+Bu_{t+1}$. Iterating,
$$x_{t+\ell}=A^\ell x_t+A^{\ell-1}Bu_t+A^{\ell-2}Bu_{t+1}+\cdots+Bu_{t+\ell-1}. \tag{10.2}$$
The first term is the no-input response. The term $A^{\ell-2}Bu_{t+1}$ is the contribution of the input at time t+1 to $x_{t+\ell}$ (p. 189).

> **Intuition note.** Each time step multiplies by A once. So $A^\ell$ is "wait ℓ steps". In the graph case the same multiplication adds one more edge to every path, which is why entries count paths.

### 10.4 QR factorization (pp. 189–190)

**Orthonormal columns** (p. 189). The n-vectors $a_1,\dots,a_k$ are orthonormal exactly when $A^TA=I$, where A is n×k with those columns. There is no standard name for such a matrix. A *square* matrix with $A^TA=I$ is called *orthogonal*, and its columns are an orthonormal basis. Examples already seen: identity matrices, 2-D reflections and rotations, and permutation matrices.

**Properties** (p. 189). Let the columns of the m×n matrix A be orthonormal, with x, y any n-vectors. Then:
- $\|Ax\|=\|x\|$ (norm preserving);
- $(Ax)^T(Ay)=x^Ty$ (inner product preserving);
- $\angle(Ax,Ay)=\angle(x,y)$ (angle preserving).

In each equation the vectors on the left have dimension m and on the right dimension n. Proof (pp. 189–190):
$$(Ax)^T(Ay)=(x^TA^T)(Ay)=x^T(A^TA)y=x^TIy=x^Ty.$$
The steps use the transpose-of-product rule, re-association of four matrices, $A^TA=I$, and $Iy=y$. Taking y = x gives $(Ax)^T(Ax)=x^Tx$, and the square root gives $\|Ax\|=\|x\|$. Angle preservation follows from the first two:
$$\angle(Ax,Ay)=\arccos\frac{(Ax)^T(Ay)}{\|Ax\|\|Ay\|}=\arccos\frac{x^Ty}{\|x\|\|y\|}=\angle(x,y).$$

**QR factorization** (p. 190). Let A be n×k with linearly independent columns $a_1,\dots,a_k$. By the independence-dimension inequality, A is tall or square. Let Q be the n×k matrix whose columns $q_1,\dots,q_k$ are the Gram–Schmidt outputs, so $Q^TQ=I$. Gram–Schmidt gives
$$a_i=(q_1^Ta_i)q_1+\cdots+(q_{i-1}^Ta_i)q_{i-1}+\|\tilde q_i\|q_i,$$
where $\tilde q_i$ is the vector from the first step of Gram–Schmidt. Writing $a_i=R_{1i}q_1+\cdots+R_{ii}q_i$, we have $R_{ij}=q_i^Ta_j$ for i < j and $R_{ii}=\|\tilde q_i\|$. Setting $R_{ij}=0$ for i > j gives
$$A=QR.$$
Shapes: A is n×k, Q is n×k with orthonormal columns, and R is k×k upper triangular with positive diagonal. If A is square with independent columns, Q is orthogonal. R is upper triangular because each $a_i$ is a combination of $q_1,\dots,q_i$ only.

Other QR algorithms exist that are more reliable under round-off errors, and they may change the order in which columns are processed. There are also sparse QR algorithms. They store Q in a special format that needs much less memory than the generic nk numbers, and their flop count is much smaller than 2nk² (p. 190).

> **Intuition note.** A = QR says: "express each column of A in the new orthonormal columns Q". R holds the coefficients. Column i only needs the first i of the q's, which is why R is triangular.

## Toy example (ours, not from the text)
Graph with three vertices and edges 1→2, 2→3, 1→3. Using the book's convention ($A_{ij}=1$ if there is an edge from j to i):
$$A=\begin{bmatrix}0&0&0\\1&0&0\\1&1&0\end{bmatrix}.$$
Compute $A^2=AA$ by rows. Row 1 of A is zero, so row 1 of $A^2$ is zero. Row 2 of A is $[1,0,0]$, so row 2 of $A^2$ is 1·(row 1 of A) = [0,0,0]. Row 3 of A is $[1,1,0]$, so row 3 of $A^2$ is (row 1) + (row 2) = [0,0,0] + [1,0,0] = [1,0,0]. Hence
$$A^2=\begin{bmatrix}0&0&0\\0&0&0\\1&0&0\end{bmatrix}.$$
So $(A^2)_{31}=1$: exactly one path of length two from vertex 1 to vertex 3, namely (1,2,3). All other entries are 0. The direct edge 1→3 has length one and is not counted in $A^2$.

Composition check: apply the map $x\mapsto Ax$ twice to $e_1=(1,0,0)$. First, $Ae_1$ is column 1 of A, which is (0,1,1). Then $A(0,1,1)=1\cdot\text{col}_2+1\cdot\text{col}_3=(0,0,1)+(0,0,0)=(0,0,1)$. This is column 1 of $A^2$, as the column reading predicts: $A^2e_1=A(Ae_1)$.

Order: with $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ and $A'=\begin{bmatrix}-1&0\\0&1\end{bmatrix}$ (the book's example, p. 183), $A'B\ne BA'$, since the sign flip and the swap do not commute.

## Concepts
- [[matrix multiplication as composition]] — AB is the matrix of "apply B, then A"; $h(x)=A(Bx)=(AB)x$ (p. 183)
- [[matrix-multiplication-definition]] (new) — $C_{ij}=\sum_kA_{ik}B_{kj}$ for compatible sizes; the book also gives column, row, inner-product and outer-product readings (pp. 177, 180–181)
- [[non-commutativity-of-matrix-product]] (new) — in general AB ≠ BA; BA may not exist, or may have a different size (pp. 178–179, 183)
- [[block-matrix-multiplication]] (new) — blocks multiply by the scalar rule, with factor order preserved when the blocks conform (pp. 179–180)
- [[dot (inner) product]] — $a^Tb$ as the product of a 1×n and an n×1 matrix (p. 178)
- [[rank-one matrix / outer product]] — $ab^T$ has entries $a_ib_j$; AB is a sum of p outer products of columns of A with rows of B (pp. 178, 181)
- [[gram-matrix]] (new) — $G=A^TA$, entries $a_i^Ta_j$, symmetric (p. 181)
- [[flop-count-matrix-product]] (new) — about 2mnp flops for dense AB; sparse and triple-product variants (pp. 182–183)
- [[matrix-power]] (new) — $A^k$ for square A, $A^0=I$; propagates a linear system k steps (pp. 186, 188)
- [[adjacency matrix]] — here $A_{ij}=1$ if there is an edge from j to i; $(A^\ell)_{ij}$ counts paths of length ℓ from j to i (pp. 186–187)
- [[chain-rule-derivative-matrix]] (new) — $Dh(z)=Df(g(z))Dg(z)$; for scalar f, $\nabla h(z)=Dg(z)^T\nabla f(g(z))$ (pp. 184–185)
- [[state-feedback-closed-loop]] (new) — with $u_t=Kx_t$, $x_{t+1}=(A+BK)x_t$ (pp. 185–186)
- [[orthonormal basis / orthogonal matrix]] — a square matrix with $A^TA=I$; columns orthonormal; preserves norm, inner product, angle (p. 189)
- [[Gram–Schmidt and QR]] — A = QR with $Q^TQ=I$ and R upper triangular with positive diagonal, from Gram–Schmidt (p. 190)

## Canonical instances
- [[swap-and-sign-flip-noncommuting]] — the 2×2 matrices that flip the sign of $x_1$ and swap entries do not commute (p. 183)
- [[second-difference-matrix]] — $\Delta=D_{n-1}D_n$, with the n = 5 case written out (p. 184)
- [[path-counting-5-vertex-graph]] — $A$, $A^2$, $A^3$ for figure 10.1 (pp. 187–188)
- [[population-dynamics-contribution-factor]] — $\mathbf 1^TA^{10}$ by age, figure 10.2 (p. 188)
- [[group-membership-gram-matrix]] — $G_{ij}$ = number of items in both groups i and j (p. 181)
- [[outer-product-cost-example]] — $ab^Tc$ costs 3n flops one way and 3n² the other (pp. 182–183)
- [[state-feedback-control]] — closed-loop matrix A + BK (pp. 185–186)

## Bridges (candidates)
- [same-math] Matrix powers of the adjacency matrix ↔ graph theory/network science: counting walks of length ℓ — the same entries $(A^\ell)_{ij}$.
- [same-math] Chain rule as $Dh=Df\cdot Dg$ ↔ calculus/optimization: gradient of f(Ax+b) is $A^T\nabla f$ — the same Jacobian product.
- [same-math] Gram matrix of a 0/1 membership matrix ↔ social network analysis: co-membership counts in two-mode (affiliation) networks — the same product $A^TA$ on an incidence-style matrix.
- [structural-analogy] State feedback $u=Kx$ giving $A+BK$ ↔ control and dynamical systems: changing the dynamics matrix by closing a loop.
- [same-math] Covariance-like Gram matrix $\tilde A^T\tilde A/n$ (exercise 10.16) ↔ statistics: covariance matrix of de-meaned data.
- [metaphor] Order of evaluation of ABC ↔ computer science: choosing the cheaper association is like choosing the cheaper query plan.

## Questions this raises
- When do two matrices commute, and is there a simple description of all matrices that commute with a given one?
- Associativity lets one choose the bracketing of a long product to minimise flops. How is the best order found for a product of many matrices?
- How do Gram matrices encode all the geometry (lengths, angles, distances) of a set of vectors?
- How can the state-feedback matrix K be chosen to make $A+BK$ behave well (the book points to §17.2.3)?

## Exercises worth doing
- Ex. 10.5 (p. 191) — when is $ab^T=ba^T$? Builds intuition for rank-one structure — difficulty: easy
- Ex. 10.15 (p. 192) — recover $\|a_i-a_j\|$ from Gram entries; shows the Gram matrix holds the geometry — difficulty: easy
- Ex. 10.13 (p. 192) — Laplacian $L=AA^T$ as a Gram matrix and its quadratic form — difficulty: medium
- Ex. 10.30 (p. 195) — count cycles of length 10 via matrix powers — difficulty: medium
- Ex. 10.37 (p. 197) — every 2×2 orthogonal matrix is a rotation or a reflection — difficulty: medium
- Ex. 10.42 (p. 198) — fast multiplication by $I+ab^T$ in time linear in n — difficulty: easy

## Reading notes
- Printed page = pdf page − 10 (pdf 187 = printed 177). Chapter text is pp. 177–190; exercises are pp. 191–198. Exercises were not digested beyond the list above.
- Minor typos seen in the images: "there is a edge" (p. 186); a stray extra ")" in "(1, 2, 1))" (p. 187); "no more that" (p. 182); exercise 10.40 (p. 197) prints $Q_i=A_{1:n,1:i}$ where $Q_{1:n,1:i}$ is evidently meant.
- On p. 182 the Gram matrix $G=B^TB$ is n×n, so B is p×n there, while on p. 181 the Gram matrix is $A^TA$ for m×n A.
- The adjacency convention here ($A_{ij}=1$ for an edge from j to i) makes $(A^\ell)_{ij}$ count paths from j to i, not i to j.
- The text refers to material outside this unit: (6.4), (6.5), §1.4, §5.4, §9.2, §11.2, §17.2.3, pages 112, 129, 132, 135, and (in the exercises) (7.1), §7.1, §7.3 and exercise 9.2.
