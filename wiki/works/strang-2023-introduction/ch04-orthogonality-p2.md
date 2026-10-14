---
id: strang-2023-introduction/ch04-orthogonality-p2
work: strang-2023-introduction
unit: "4 Orthogonality (part 2/2): §4.4 Orthonormal Bases and Gram-Schmidt; §4.5 The Pseudoinverse of a Matrix"
pages: 176-197
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Orthonormal Bases, Gram-Schmidt, QR, and the Pseudoinverse

## L0 — One line
Orthonormal columns make projection and least squares trivial ($\hat x = Q^{\mathsf T}b$), Gram-Schmidt builds such columns and gives $A=QR$, and the pseudoinverse $A^+$ extends "inverse" to every matrix.

## L1 — The gist (≤ 120 words)
Why are orthogonal columns good, and how do we make them? If $Q^{\mathsf T}Q=I$, least squares needs no matrix inversion, and lengths and dot products are preserved. Gram-Schmidt subtracts from each new vector its projections onto the earlier directions, then normalizes. In matrix form this is $A=QR$ with $R$ upper triangular, so least squares reduces to back substitution. §4.5 then defines the pseudoinverse $A^+$ for any matrix. It inverts $A$ from row space to column space and sends the left nullspace to zero. It can be computed from $A=CR$ as $R^{\mathsf T}(C^{\mathsf T}AR^{\mathsf T})^{-1}C^{\mathsf T}$, or from the SVD.

**Prerequisites:** dot product and projection onto a line; least squares $A^{\mathsf T}A\hat x=A^{\mathsf T}b$; four fundamental subspaces; rank; $A=CR$ (Ch. 1, 3); matrix transpose and inverse.

## L2 — Key ideas
- Orthonormal columns mean $Q^{\mathsf T}Q=I$. When $Q$ is square, $Q^{-1}=Q^{\mathsf T}$ and $Q$ is called orthogonal. Rotations, permutations and reflections are examples (pp. 176–178).
- $\|Qx\|=\|x\|$ and $(Qx)^{\mathsf T}(Qy)=x^{\mathsf T}y$, so orthogonal matrices keep numbers from growing (pp. 178–179).
- With orthonormal $q$'s: $\hat x=Q^{\mathsf T}b$, $P=QQ^{\mathsf T}$. Nothing is inverted, and $b$ splits into its components along the $q$'s (pp. 179–180).
- Gram-Schmidt: subtract from every new vector its projections onto the directions already set, then divide by lengths (p. 180).
- $A=QR$, with $R=Q^{\mathsf T}A$ upper triangular, turns least squares into back substitution. Modified Gram-Schmidt, which subtracts one projection at a time, is more stable in code (pp. 182–183).
- The pseudoinverse $A^+$ is the left inverse, right inverse or true inverse when one exists. Otherwise it gives the minimum-norm least-squares solution $x^+=A^+b$ (pp. 190–191).
- $A^+A$ and $AA^+$ are the symmetric projections onto the row space and column space, and four Penrose conditions characterize $A^+$ (pp. 191, 194).
- $A=CR$ gives $A^+=R^+C^+=R^{\mathsf T}(C^{\mathsf T}AR^{\mathsf T})^{-1}C^{\mathsf T}$, worked exactly for a graph incidence matrix (pp. 193–195).

## L3 — Walkthrough

### 4.4 Orthonormal Bases and Gram-Schmidt

**Goals.** The section asks why orthogonal columns are good and how to construct them. Dot products are zero, so $A^{\mathsf T}A$ becomes diagonal (p. 176).

**Definition (p. 176).** Vectors $q_1,\dots,q_n$ are *orthonormal* if
$$q_i^{\mathsf T}q_j=\begin{cases}0 & i\ne j\ \text{(orthogonal)}\\ 1 & i=j\ \text{(unit vectors, } \|q_i\|=1).\end{cases}$$
A matrix $Q$ with orthonormal columns has $Q^{\mathsf T}Q=I$. Typically $m>n$.

Row $i$ of $Q^{\mathsf T}$ times column $j$ of $Q$ is $q_i^{\mathsf T}q_j$, which gives
$$Q^{\mathsf T}Q=\begin{bmatrix}-q_1^{\mathsf T}-\\ \vdots\\ -q_n^{\mathsf T}-\end{bmatrix}\begin{bmatrix}|&&|\\ q_1&\cdots&q_n\\ |&&|\end{bmatrix}=I\tag{1}$$
(p. 177). If the columns are only orthogonal, $Q^{\mathsf T}Q$ is diagonal, "almost as good as $I$" (p. 177).

- For rectangular $Q$, $Q^{\mathsf T}$ is a one-sided (left) inverse, and $QQ^{\mathsf T}\ne I$ (pp. 176–177).
- For square $Q$, $Q^{\mathsf T}Q=I$ means $Q^{\mathsf T}=Q^{-1}$, a two-sided inverse. The rows are orthonormal too. Then $Q$ is an *orthogonal matrix* (p. 177).
- The author notes that "orthonormal matrix" would be a better name (footnote, p. 177).

**Example 1, rotation (p. 177).**
$$Q=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix},\quad Q^{\mathsf T}=Q^{-1}=\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix}.$$
The columns are orthogonal and unit because $\sin^2\theta+\cos^2\theta=1$. $Q^{-1}$ rotates back through $-\theta$, which agrees with $Q^{\mathsf T}$ since $\cos(-\theta)=\cos\theta$ and $\sin(-\theta)=-\sin\theta$.

**Example 2, permutation (pp. 177–178).** $\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}(x,y,z)^{\mathsf T}=(y,z,x)^{\mathsf T}$, and $\begin{bmatrix}0&1\\1&0\end{bmatrix}(x,y)^{\mathsf T}=(y,x)^{\mathsf T}$. The columns are unit and orthogonal because the 1's sit in different places. The inverse puts components back in order, so $Q^{-1}=Q^{\mathsf T}$. Every permutation matrix is an orthogonal matrix (p. 178).

**Example 3, reflection (p. 178).** For a unit vector $u$, $Q=I-2uu^{\mathsf T}$. Here $uu^{\mathsf T}$ is a matrix and $u^{\mathsf T}u=\|u\|^2=1$ is a number.
$$Q^{\mathsf T}=I-2uu^{\mathsf T}=Q\quad\text{and}\quad Q^{\mathsf T}Q=I-4uu^{\mathsf T}+4uu^{\mathsf T}uu^{\mathsf T}=I.\tag{2}$$
So reflections are symmetric and orthogonal, and $Q^2=Q^{\mathsf T}Q=I$ (reflecting twice returns the original). With $u=(-1/\sqrt2,\,1/\sqrt2)$:
$$Q=I-2\begin{bmatrix}.5&-.5\\-.5&.5\end{bmatrix}=\begin{bmatrix}0&1\\1&0\end{bmatrix},$$
which sends $(x,y)\mapsto(y,x)$. A vector like $(3,3)$ on the mirror line does not move (p. 178).

**Lengths and angles (p. 178).** $\|Qx\|^2=(Qx)^{\mathsf T}(Qx)=x^{\mathsf T}Q^{\mathsf T}Qx=x^{\mathsf T}Ix=x^{\mathsf T}x$. Hence
$$\|Qx\|=\|x\|\ \text{for every } x\tag{3}$$
whenever $Q^{\mathsf T}Q=I$. Dot products are preserved too: $(Qx)^{\mathsf T}(Qy)=x^{\mathsf T}Q^{\mathsf T}Qy=x^{\mathsf T}y$.

*Intuition note.* $Q^{\mathsf T}Q=I$ is just "the columns are orthonormal" written as one matrix product. Because $Q$ keeps all lengths and angles, it can rotate, flip or reorder vectors but never stretch them. That is why the author says stable codes use $Q$'s as much as possible (p. 179).

**Projections with $QQ^{\mathsf T}$ (p. 179).** All projection formulas involve $A^{\mathsf T}A$, whose entries are the dot products $a_i^{\mathsf T}a_j$. If the basis is orthonormal, $A^{\mathsf T}A$ becomes $Q^{\mathsf T}Q=I$ and
$$\hat x=Q^{\mathsf T}b,\qquad p=Q\hat x,\qquad P=QQ^{\mathsf T}.\tag{4}$$
There are no matrices to invert. $\hat x$ is just the dot products of $q_1,\dots,q_n$ with $b$, and the "coupling matrix" $A^{\mathsf T}A$ is now $I$. Then
$$p=QQ^{\mathsf T}b=\begin{bmatrix}|&&|\\q_1&\cdots&q_n\\|&&|\end{bmatrix}\begin{bmatrix}q_1^{\mathsf T}b\\ \vdots\\ q_n^{\mathsf T}b\end{bmatrix}=q_1(q_1^{\mathsf T}b)+\cdots+q_n(q_n^{\mathsf T}b).\tag{5}$$

**Square case (p. 179).** If $Q$ is square, the subspace is the whole space. Then $\hat x=Q^{\mathsf T}b=Q^{-1}b$ is exact, $p=b$, and $P=QQ^{\mathsf T}=I$. So
$$b=q_1(q_1^{\mathsf T}b)+\cdots+q_n(q_n^{\mathsf T}b).\tag{6}$$
The author says $QQ^{\mathsf T}=I$ is the foundation of Fourier series and the great "transforms" of applied mathematics. They break $b$ or $f(x)$ into perpendicular pieces, and the inverse transform adds the pieces back (p. 179).

**Example 4 (pp. 179–180).** $Q=\tfrac13\begin{bmatrix}-1&2&2\\2&-1&2\\2&2&-1\end{bmatrix}$ has $Q^{\mathsf T}Q=QQ^{\mathsf T}=I$. For $b=(0,0,1)$ the projections are $p_1=q_1(q_1^{\mathsf T}b)=\tfrac23q_1$, $p_2=\tfrac23q_2$, $p_3=-\tfrac13q_3$. Their sum reconstructs $b$:
$$\tfrac23q_1+\tfrac23q_2-\tfrac13q_3=\tfrac19\begin{bmatrix}-2+4-2\\4-2-2\\4+4+1\end{bmatrix}=\begin{bmatrix}0\\0\\1\end{bmatrix}=b.$$
$p_1+p_2$ is the projection onto the plane of $q_1,q_2$ (p. 180).

*Intuition note.* With perpendicular axes, the best coordinate along each axis does not depend on the other axes. So $n$ separate one-dimensional projections add up to the full projection.

**The Gram-Schmidt process (p. 180).** Start with independent $a,b,c$. Build orthogonal $A,B,C$, then divide by lengths: $q_1=A/\|A\|$, $q_2=B/\|B\|$, $q_3=C/\|C\|$.

- Take $A=a$.
- Subtract from $b$ its projection along $A$:
$$B=b-\frac{A^{\mathsf T}b}{A^{\mathsf T}A}A.\tag{7}$$
  Multiplying by $A^{\mathsf T}$ gives $A^{\mathsf T}B=A^{\mathsf T}b-A^{\mathsf T}b=0$. $B$ is the error vector $e$, and $B\ne0$ because otherwise $a,b$ would be dependent.
- For $c$, subtract components along both $A$ and $B$:
$$C=c-\frac{A^{\mathsf T}c}{A^{\mathsf T}A}A-\frac{B^{\mathsf T}c}{B^{\mathsf T}B}B.\tag{8}$$

The one idea is: subtract from every new vector its projections in the directions already set. A fourth vector $d$ would lose three projections (onto $A,B,C$) to give $D$ (p. 180). The author's footnote guesses Gram had the idea and says he does not know where Schmidt came in.

**Worked example (p. 181).** $a=(1,-1,0)$, $b=(2,0,-2)$, $c=(3,-3,3)$.

- $A=a$ has $A^{\mathsf T}A=2$ and $A^{\mathsf T}b=2$. So $B=b-\tfrac22A=(1,1,-2)$, and $A^{\mathsf T}B=0$.
- $C=c-\tfrac62A+\tfrac66B=(1,1,1)$. This is perpendicular to both $A$ and $B$.
- Lengths are $\sqrt2,\sqrt6,\sqrt3$, so $q_1=\tfrac1{\sqrt2}(1,-1,0)$, $q_2=\tfrac1{\sqrt6}(1,1,-2)$, $q_3=\tfrac1{\sqrt3}(1,1,1)$.

The author remarks that $A,B,C$ usually contain fractions and the $q$'s usually contain square roots: "the price we pay for unit vectors" (p. 181).

**The factorization $A=QR$ (p. 182).** Each $a_k$ is a combination of $q_1,\dots,q_k$ only, and later $q$'s are not involved. Reason: $a$, $A$, $q_1$ lie on one line; $a,b$ and $q_1,q_2$ lie in one plane; and so on. So the connecting matrix is triangular:
$$\begin{bmatrix}a&b&c\end{bmatrix}=\begin{bmatrix}q_1&q_2&q_3\end{bmatrix}\begin{bmatrix}q_1^{\mathsf T}a&q_1^{\mathsf T}b&q_1^{\mathsf T}c\\&q_2^{\mathsf T}b&q_2^{\mathsf T}c\\&&q_3^{\mathsf T}c\end{bmatrix}\quad\text{or}\quad A=QR.\tag{9}$$
Multiplying by $Q^{\mathsf T}$ gives $R=Q^{\mathsf T}A$. It is upper triangular because later $q$'s are orthogonal to earlier $a$'s. For the example,
$$A=\begin{bmatrix}1&2&3\\-1&0&-3\\0&-2&3\end{bmatrix}=\begin{bmatrix}1/\sqrt2&1/\sqrt6&1/\sqrt3\\-1/\sqrt2&1/\sqrt6&1/\sqrt3\\0&-2/\sqrt6&1/\sqrt3\end{bmatrix}\begin{bmatrix}\sqrt2&\sqrt2&\sqrt{18}\\0&\sqrt6&-\sqrt6\\0&0&\sqrt3\end{bmatrix}.$$
The diagonal of $R$ holds the lengths of $A,B,C$ (p. 182).

Any $m\times n$ $A$ with independent columns factors as $A=QR$. $Q$ ($m\times n$) has orthonormal columns and $R$ ($n\times n$) is upper triangular with positive diagonal (p. 182).

**Least squares via QR (pp. 182–183).** $A^{\mathsf T}A=R^{\mathsf T}Q^{\mathsf T}QR=R^{\mathsf T}R$. So $A^{\mathsf T}A\hat x=A^{\mathsf T}b$ becomes $R^{\mathsf T}R\hat x=R^{\mathsf T}Q^{\mathsf T}b$, then
$$R\hat x=Q^{\mathsf T}b,\qquad \hat x=R^{-1}Q^{\mathsf T}b,\tag{10}$$
solved by fast back substitution. The real cost is the $mn^2$ multiplications of Gram-Schmidt (p. 183).

**Code (p. 183).** For column $j$:
$$r_{kj}=\sum_{i=1}^m q_{ik}v_{ij},\quad v_{ij}=v_{ij}-q_{ik}r_{kj},\quad r_{jj}=\Big(\sum_{i=1}^m v_{ij}^2\Big)^{1/2},\quad q_{ij}=\frac{v_{ij}}{r_{jj}}.\tag{11}$$

- Start with $v=a_j$. For each $i<j$, set $R(i,j)=q_i^{\mathsf T}v$ and $v\leftarrow v-R(i,j)q_i$.
- Then $R(j,j)=\|v\|$ and $q_j=v/R(j,j)$.
- For $a,b,c=a_1,a_2,a_3$: $q_1=a_1/\|a_1\|$; $B=a_2-(q_1^{\mathsf T}a_2)q_1$; $C^*=a_3-(q_1^{\mathsf T}a_3)q_1$; $C=C^*-(q_2^{\mathsf T}C^*)q_2$.
- Subtracting one projection at a time is *modified Gram-Schmidt*. The author says it is numerically more stable than (8), which subtracts all projections at once.
- Undoing the steps gives column $j$ of $A$ (the $j$-th column of $QR=A$):
$$R(j,j)q_j=(\text{column } j \text{ of } A)-\sum_{i=1}^{j-1}R(i,j)q_i.\tag{12}$$

**"Confession" (p. 184).** Good software (LAPACK, in MATLAB, Julia, Python) may not use this code. Householder reflections produce the triangular $R$ one column at a time, as elimination produces $U$. For tridiagonal $A$, 2 by 2 rotations simplify it further. The result is always $A=QR$, and the MATLAB command is `[Q,R]=qr(A)`. Gram-Schmidt is still the process to understand (p. 184).

**Review and worked examples (pp. 184–185).**

- Key ideas: $Q^{\mathsf T}Q=I$; square gives $Q^{\mathsf T}=Q^{-1}$; $\|Qx\|=\|x\|$; $P=QQ^{\mathsf T}$; square gives $P=I$ and (6); Gram-Schmidt gives $A=QR$ (p. 184).
- **4.4 A.** Hadamard matrices have entries $\pm1$ and orthogonal columns. $H_4=\begin{bmatrix}H_2&H_2\\H_2&-H_2\end{bmatrix}$ with $H_2=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, and $Q=H_4/2$ has orthonormal columns. A $5\times5$ Hadamard matrix is impossible: the dot product of two columns would have five $\pm1$ terms and could not add to zero (p. 185).
- With $H_8=\begin{bmatrix}H_4&H_4\\H_4&-H_4\end{bmatrix}$ and $H_4^{\mathsf T}H_4=4I$:
$$H_8^{\mathsf T}H_8=\begin{bmatrix}H^{\mathsf T}&H^{\mathsf T}\\H^{\mathsf T}&-H^{\mathsf T}\end{bmatrix}\begin{bmatrix}H&H\\H&-H\end{bmatrix}=\begin{bmatrix}2H^{\mathsf T}H&0\\0&2H^{\mathsf T}H\end{bmatrix}=\begin{bmatrix}8I&0\\0&8I\end{bmatrix},$$
so $Q_8=H_8/\sqrt8$ (p. 185).
- **4.4 B.** Key point of orthogonal columns: $Q^{\mathsf T}Q$ is diagonal and easy to invert, so we can project onto lines and just add (p. 185).
- The table on p. 185 sets $A$ ($n$ independent columns) beside $Q$ ($n$ orthonormal columns):

| | $A$ | $Q$ |
|---|---|---|
| Gram matrix | $A^{\mathsf T}A$ symmetric, invertible | $Q^{\mathsf T}Q=I$ |
| Projection | $P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$ | $P=QQ^{\mathsf T}$ |
| Least squares | $A^{\mathsf T}A\hat x=A^{\mathsf T}b$ | $\hat x=Q^{\mathsf T}b$ |
| Pseudoinverse | $A^+=R^+Q^+=R^{-1}Q^{\mathsf T}$ for $A=QR$ | $Q^+=Q^{\mathsf T}$ |

### 4.5 The Pseudoinverse of a Matrix

**One-sided inverses (p. 190).** Of the three rank examples, only the first matrix $I$ is truly invertible (p. 190). More generally, a true inverse needs a square matrix with independent columns and independent rows (p. 192). Every matrix has a pseudoinverse $A^+$, which covers inverses, left inverses and right inverses. The author's summary:

| Left inverse: $A^+A=I$ | Right inverse: $AA^+=I$ |
|---|---|
| independent columns, rank $r=n$ | independent rows, rank $r=m$ |
| $Ax=b$ has 0 or 1 solution; $N(A)=\{0\}$ | $Ax=b$ has 1 or many solutions; $N(A^{\mathsf T})=\{0\}$ |
| $A^{\mathsf T}A$ is $n\times n$, invertible | $AA^{\mathsf T}$ is $m\times m$, invertible |
| $A^+=(A^{\mathsf T}A)^{-1}A^{\mathsf T}$ | $A^+=A^{\mathsf T}(AA^{\mathsf T})^{-1}$ |

Example: $I_L=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$ and $I_R=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}$ have $(I_L)(I_R)=I$ but $(I_R)(I_L)\ne I$ (p. 190).

- Left column: this is the least-squares chapter. $\hat x=A^+b$ solves $A^{\mathsf T}A\hat x=A^{\mathsf T}b$ and makes $e=b-A\hat x$ as small as possible.
- Right column: infinitely many solutions. $x^+=A^+b$ is the minimum-length one. It lies in the row space, and every other solution $x=x^++x_n$ has a nullspace part that increases the length.
- When $r<m$ and $r<n$ there is no one-sided inverse. $A^+$ still gives the best $x^+=A^+b$: it minimizes $\|Ax-b\|^2$ and, among all minimizers, has minimum length. This is the "minimum norm least squares solution".
- Key idea: $x^+$ has nullspace component 0. The section is called optional (p. 190).

**Definition through the four subspaces (p. 191).** $A^+$ is $n\times m$ for $A$ $m\times n$.

1. Every $y\in\mathbb R^m$ splits into perpendicular parts $y=b+z$.
2. $b$ is in the column space of $A$; $z$ is in the nullspace of $A^{\mathsf T}$, with $A^{\mathsf T}z=0$ and $A^+z=0$.
3. $Ax=b$ for exactly one $x$ in the row space. Invert this part: $A^+b=x$.

So $A^+y=A^+b+A^+z=x$. $A^+$ has the same four subspaces as $A^{\mathsf T}$. $A^+A$ is exactly the $n\times n$ projection onto the row space, and $AA^+$ is exactly the $m\times m$ projection onto the column space (p. 191). The author attributes $A^+$ to Moore and again to Penrose. It is the matrix that gives symmetric projections:
$$P_{\text{row}}=A^+A=(A^+A)^2=(A^+A)^{\mathsf T},\qquad P_{\text{column}}=AA^+=(AA^+)^2=(AA^+)^{\mathsf T}.$$

**Examples (p. 192).**
- $A=\begin{bmatrix}2&0\\0&0\end{bmatrix}$, $y=(y_1,y_2)=b+z$ with $b=(y_1,0)$ and $z=(0,y_2)$. Then $A^+=\begin{bmatrix}1/2&0\\0&0\end{bmatrix}$, $A^+y=(y_1/2,0)$, and $A^+A=\begin{bmatrix}1&0\\0&0\end{bmatrix}$.
- For a diagonal $D$ (square or rectangular), invert the nonzero diagonal entries and take $1/0$ as zero. For example $D=\mathrm{diag}(2,3,0)$ gives $D^+=\mathrm{diag}(1/2,1/3,0)$. Extra zero rows (columns) of $D$ give extra zero columns (rows) of $D^+$.
- The author states: for $A=BDC$ with $B,C$ invertible, $A^+$ "will be" $C^{-1}D^+B^{-1}$ (see Reading notes).
- $A=\begin{bmatrix}1\\1\end{bmatrix}$ has $A^+=\tfrac12\begin{bmatrix}1&1\end{bmatrix}$, a left inverse. $A=\begin{bmatrix}1&1\end{bmatrix}$ has $A^+=\tfrac12\begin{bmatrix}1\\1\end{bmatrix}$, a right inverse.
- Tall, independent columns: $A^+=(A^{\mathsf T}A)^{-1}A^{\mathsf T}$, so $A^+A=I$ but $AA^+\ne I$ (1). Short, independent rows: $A^+=A^{\mathsf T}(AA^{\mathsf T})^{-1}$, so $AA^+=I$ but $A^+A\ne I$ (2).

**Row space to column space (p. 193).** Two vectors $x\ne X$ in the row space cannot satisfy $Ax=AX$.

*Proof.* $A(x-X)=b-b=0$, so $x-X$ is in the nullspace. It is also in the row space. The nullspace is orthogonal to the row space, so $x-X$ is orthogonal to itself and must be zero.

So each $b=Ax$ in the column space comes from one and only one $x$ in the row space, and $A^+b=x$. A basis $x_1,\dots,x_r$ of the row space is sent to a basis $Ax_1,\dots,Ax_r$ of the column space (p. 193).

*Intuition note.* Restricted to the row space, $A$ is a one-to-one map onto the column space, so it can be undone there. $A^+$ undoes it there and sends everything perpendicular to the column space to zero. The nullspace of $A$ is destroyed by $A$ and is simply never produced by $A^+$.

**$A^+$ from $A=CR$ (p. 193).** $C$ is $m\times r$ with $r$ independent columns of $A$; $R$ is $r\times n$ with $r$ independent rows (from the reduced echelon form). Then $C^{\mathsf T}C$ and $RR^{\mathsf T}$ are invertible $r\times r$ matrices, and
$$C^+=(C^{\mathsf T}C)^{-1}C^{\mathsf T},\qquad R^+=R^{\mathsf T}(RR^{\mathsf T})^{-1},\tag{3}$$
with $C^+C=I$ and $RR^+=I$. The author says "by good fortune" they come in the order $R^+C^+$ (and adds "But see Problem 10."). Then
$$A^+=R^+C^+=R^{\mathsf T}(RR^{\mathsf T})^{-1}(C^{\mathsf T}C)^{-1}C^{\mathsf T}=R^{\mathsf T}(C^{\mathsf T}CRR^{\mathsf T})^{-1}C^{\mathsf T}=R^{\mathsf T}(C^{\mathsf T}AR^{\mathsf T})^{-1}C^{\mathsf T}.\tag{4}$$
(The last step uses $C^{\mathsf T}CRR^{\mathsf T}=C^{\mathsf T}AR^{\mathsf T}$, because $CR=A$; added step.) The key facts are that $C^{\mathsf T}C$ and $RR^{\mathsf T}$ are invertible when $C$ has independent columns and $R$ has independent rows (p. 193).

**Penrose conditions (p. 194).** Penrose required four conditions, which identify the same pseudoinverse:
$$AA^+A=A,\qquad A^+AA^+=A^+,\qquad (A^+A)^{\mathsf T}=A^+A,\qquad (AA^+)^{\mathsf T}=AA^+.\tag{5}$$
Then $A^+A$ and $AA^+$ are projections onto the row space and column space. The author adds that the same $A^+$ comes from $A=CR$, $A=QR$ and the SVD $A=U\Sigma V^{\mathsf T}$. Singular vectors (Chapter 7) are orthonormal $v_i$ in the row space with $Av_i$ orthogonal in the column space (p. 194).

**Incidence-matrix example (pp. 194–195).** The graph has 4 nodes and 5 edges $a$–$e$. Row $i$ of $A$ has $-1$ at the leaving node and $+1$ at the entering node of edge $i$:
$$A=\begin{bmatrix}-1&1&0&0\\-1&0&1&0\\0&-1&1&0\\-1&0&0&1\\0&-1&0&1\end{bmatrix}.$$
Here $m=5$, $n=4$, $r=3$. Column 4 is minus (columns 1 + 2 + 3), so
$$A=CR,\quad C=\text{first three columns},\quad R=\begin{bmatrix}1&0&0&-1\\0&1&0&-1\\0&0&1&-1\end{bmatrix}.\tag{6}$$
Shapes: $C$ is $5\times3$, $R$ is $3\times4$.

**Row space to column space again (p. 195).** The author recalls that $Ax=b$ has a solution when $b$ is a combination of the columns of $A$. The minimum norm solution $x_0$ is the only solution in the row space. Other solutions $x=x_0+x_n$ have larger norm, $\|x\|^2=\|x_0\|^2+\|x_n\|^2$, because of a nullspace part with $Ax_n=0$. Every $A$ is invertible from its row space to its column space, dimension $r$ to $r$: $Ax_0=b_0$ and $A^+b_0=x_0$, while $Ax_n=0$ and $A^+b_n=0$ for $b_n$ in the nullspace of $A^{\mathsf T}$.

**Computing $A^+$ (p. 195).**
- Recommended: from the SVD, $A^+=V\Sigma^+U^{\mathsf T}$, where $U$, $V$ are square orthogonal. The $n\times m$ matrix $\Sigma^+$ replaces each $\sigma_i>0$ by $1/\sigma_i$, and each diagonal zero stays zero.
- For small integer matrices, use $A=CR$. This gives fractions but not irrational numbers:
$$A^+=R^{\mathsf T}(C^{\mathsf T}AR^{\mathsf T})^{-1}C^{\mathsf T}.\tag{7}$$
- Checking $(A^+A)^2=A^+A$:
$$(A^+A)^2=R^{\mathsf T}(C^{\mathsf T}AR^{\mathsf T})^{-1}C^{\mathsf T}AR^{\mathsf T}(C^{\mathsf T}AR^{\mathsf T})^{-1}C^{\mathsf T}A=A^+A.\tag{8}$$
  Similarly $(AA^+)^2=AA^+$. If $A$ is invertible, $A^+=A^{-1}$.
- For the graph:
$$C^{\mathsf T}AR^{\mathsf T}=\begin{bmatrix}4&0&0\\0&4&0\\-1&-1&2\end{bmatrix},\quad A^+=\tfrac18\begin{bmatrix}-2&-2&0&-2&0\\2&0&-2&0&-2\\0&3&3&-1&-1\\0&-1&-1&3&3\end{bmatrix}.\tag{9}$$
- Each row of $A$ adds to zero, and each column of $A^+$ adds to zero. Row 2 of $A$ = Row 1 + Row 3, and Column 2 of $A^+$ = Column 1 + Column 3. Row 1 of $A$ = Row 4 − Row 5, and Column 1 of $A^+$ = Column 4 − Column 5.
- $A^{\mathsf T}y=0$ is Kirchhoff's Current Law (flow in = flow out at each node) (p. 195).

**Thoughts on the victory of orthogonality (p. 197).** The author lists wins of orthogonal matrices:
1. $\|Qx\|=\|x\|$.
2. $(Qx)^{\mathsf T}(Qy)=x^{\mathsf T}y$.
3. $P=QQ^{\mathsf T}=(QQ^{\mathsf T})^2$.
4. $\hat x=Q^{\mathsf T}b=Q^+b$ for $Qx=b$, $m>n$.
5. Powers $Q^N$ and products $Q_1\cdots Q_N$ are orthogonal, and $|\det|=1$.
6. Eigenvectors of a symmetric $S$ can be chosen orthonormal.
7. The singular vectors of every matrix are orthonormal.

The success is tied to the sum-of-squares definition $\|x\|^2=x^{\mathsf T}x$. In least squares, the derivative of $\|Ax-b\|^2$ leads to the symmetric $S=A^{\mathsf T}A$, which an orthogonal matrix diagonalizes. Every $A$ is diagonalized by two orthogonal matrices (Ch. 7). Two more facts:
8. Every invertible matrix equals orthogonal $Q$ times symmetric $S$. Example: $\begin{bmatrix}3&0\\4&5\end{bmatrix}=\tfrac1{\sqrt5}\begin{bmatrix}2&-1\\1&2\end{bmatrix}\sqrt5\begin{bmatrix}2&1\\1&2\end{bmatrix}$.
9. Every invertible matrix equals orthogonal $Q$ times upper triangular $R$. Example: $\begin{bmatrix}3&0\\4&5\end{bmatrix}=\tfrac15\begin{bmatrix}3&-4\\4&3\end{bmatrix}\begin{bmatrix}5&4\\0&3\end{bmatrix}$.

## Toy example (ours, not from the text)
Gram-Schmidt and QR for $a=(3,4)$, $b=(2,1)$, then solve $Ax=y$ with $A=[a\ b]$, $y=(7,1)$.

1. $A=a$ (here the book's letter $A$ is the first vector, so $A^{\mathsf T}A=25$) and $A^{\mathsf T}b=3\cdot2+4\cdot1=10$.
2. $B=b-\tfrac{10}{25}A=(2,1)-0.4(3,4)=(0.8,-0.6)$. Check: $A^{\mathsf T}B=2.4-2.4=0$.
3. $\|A\|=5$ and $\|B\|=\sqrt{0.64+0.36}=1$. So $q_1=(0.6,0.8)$, $q_2=(0.8,-0.6)$.
4. $R=Q^{\mathsf T}A$: $q_1^{\mathsf T}a=1.8+3.2=5$; $q_1^{\mathsf T}b=1.2+0.8=2$; $q_2^{\mathsf T}a=2.4-2.4=0$; $q_2^{\mathsf T}b=1.6-0.6=1$. So $R=\begin{bmatrix}5&2\\0&1\end{bmatrix}$.
5. Check $QR$ column 2: $2q_1+1q_2=(1.2+0.8,\ 1.6-0.6)=(2,1)=b$ ✓.
6. $Q^{\mathsf T}y=(0.6\cdot7+0.8\cdot1,\ 0.8\cdot7-0.6\cdot1)=(5,5)$. Solve $Rx=(5,5)$ by back substitution: $x_2=5$, then $5x_1+2\cdot5=5$ gives $x_1=-1$.
7. Check: $-1\cdot(3,4)+5\cdot(2,1)=(7,1)=y$ ✓.

## Concepts
- [[orthonormal-basis-orthogonal-matrix]] — columns with $q_i^{\mathsf T}q_j=\delta_{ij}$; $Q^{\mathsf T}Q=I$; called orthogonal if square, then $Q^{-1}=Q^{\mathsf T}$ (pp. 176–177)
- [[gram-schmidt-and-qr]] — subtract earlier projections from each new vector, then normalize; gives $A=QR$, $R=Q^{\mathsf T}A$ upper triangular (pp. 180, 182)
- [[projection]] — with orthonormal columns $P=QQ^{\mathsf T}$, $p=Q\hat x$ (p. 179)
- [[least-squares]] — $\hat x=Q^{\mathsf T}b$ for $Q$; $R\hat x=Q^{\mathsf T}b$ for $A=QR$ (pp. 179, 183)
- [[numerical-stability]] — modified Gram-Schmidt (one projection at a time) is more stable than (8); Householder reflections used in good software (pp. 183–184)
- [[pseudoinverse]] — $A^+$: inverts $A$ from row space to column space, zero on the left nullspace; minimum-norm least-squares solution (pp. 190–191)
- [[four-fundamental-subspaces]] — used to define $A^+$ (p. 191)
- [[rank]] — $r$ is the common dimension of row and column space, and equals the number of columns of $C$ (p. 193)
- [[one-sided-inverse]] (new) — left inverse $A^+A=I$ (independent columns) or right inverse $AA^+=I$ (independent rows) (p. 190)
- [[penrose-conditions]] (new) — four equations (5) that characterize $A^+$ (p. 194)
- [[reflection-matrix]] (new) — $I-2uu^{\mathsf T}$, symmetric and orthogonal, $Q^2=I$ (p. 178)
- [[rank-factorization-CR]] (new) — $A=CR$, giving $A^+=R^{\mathsf T}(C^{\mathsf T}AR^{\mathsf T})^{-1}C^{\mathsf T}$ (pp. 193–194)

## Canonical instances
- [[rotation-matrix]] — orthogonal $2\times2$ matrix with $Q^{-1}=Q^{\mathsf T}$ (p. 177)
- [[permutation-matrix]] — every permutation matrix is orthogonal (p. 178)
- [[hadamard-matrix]] — $\pm1$ entries, orthogonal columns, $H_8^{\mathsf T}H_8=8I$ (p. 185)
- [[incidence-matrix]] — graph example with $m=5,n=4,r=3$; $A^+$ computed exactly via $CR$; $A^{\mathsf T}y=0$ is Kirchhoff's law (pp. 194–195)
- [[gram-schmidt-3x3-example]] — $a,b,c\to q_1,q_2,q_3$ and $A=QR$ (pp. 181–182)

## Bridges (candidates)
- [same-math] $A=QR$ and $R\hat x=Q^{\mathsf T}b$ ↔ numerical linear algebra: QR-based least squares avoiding $A^{\mathsf T}A$ — same factorization, used for solving.
- [same-math] $A^+=V\Sigma^+U^{\mathsf T}$ ↔ SVD (Ch. 7): the same pseudoinverse (p. 195).
- [same-math] $\hat x=Q^{\mathsf T}b$, $b=\sum q_i(q_i^{\mathsf T}b)$ ↔ Fourier series / transforms: expansion in orthogonal pieces (author's own link, p. 179).
- [structural-analogy] Kirchhoff's law $A^{\mathsf T}y=0$ ↔ graph Laplacian and network flow: nullspace of the incidence transpose.
- [structural-analogy] Gram-Schmidt step ↔ elimination: both give a triangular factor, with $A^{\mathsf T}A$ pivots equal to squares of the diagonal of $R$ (Problem 19, p. 187).

## Questions this raises
- Why does the minimum-norm solution $x^+$ lie in the row space, and how does that connect to the SVD route to $A^+$ (Chapter 7)?
- When is $(AB)^+=B^+A^+$? Problem 10 shows it can fail, yet $(CR)^+=R^+C^+$ holds.
- How much better is modified Gram-Schmidt than classical in floating point, and why do Householder reflections beat both?
- Which matrices $BDC$ have $A^+=C^{-1}D^+B^{-1}$? (See Reading notes.)

## Exercises worth doing
- Ex. 10 (p. 186) — orthonormal vectors are automatically independent (vector proof and matrix proof) — easy
- Ex. 18 (p. 187, "Recommended") — Gram-Schmidt on $a,b,c$ with entries $\pm1$ — medium
- Ex. 19 (p. 187) — $A^{\mathsf T}A=R^{\mathsf T}R$; pivots of $A^{\mathsf T}A$ are squares of the diagonal of $R$ — medium
- Ex. 26 (p. 188) — modified Gram-Schmidt $C$ equals the $C$ of equation (8) — medium
- Ex. 34 (p. 189) — reflection: $Qu=-u$, and $Qv=v$ when $u^{\mathsf T}v=0$ — easy
- Ex. 2 (p. 196) — $A=cr^{\mathsf T}$ has $A^+=rc^{\mathsf T}/(r^{\mathsf T}r)(c^{\mathsf T}c)$; check the Penrose conditions — medium
- Ex. 10, §4.5 (p. 196) — $(AB)^+\ne B^+A^+$ but $(BA)^+=A^+B^+$ — hard

## Reading notes
- This part starts at §4.4 (printed p. 176) and ends with "Thoughts on the Victory of Orthogonality" (p. 197), the end of §4.5. It includes both problem sets. Printed = pdf − 10. The running header on these pages reads "Chapter 4. Orthogonality"; author and edition are not visible on these pages (they come from the unit metadata).
- The text layer of p. 176 and parts of other pages are badly garbled. All equations here were checked against the page images.
- The caption of the Gram-Schmidt figure on p. 181 reads "Figure 4.10", but the text on p. 180 refers to "Figure 4.11" for $A$ and $B$. The pseudoinverse figure on p. 191 is captioned 4.11. The text reference on p. 180 seems to be a numbering slip.
- On p. 192 the unit states that $A=BDC$ (with $B,C$ invertible) has $A^+=C^{-1}D^+B^{-1}$. No proof is given. Test: take $A=\begin{bmatrix}1&1\end{bmatrix}$, $B=1$, $D=\begin{bmatrix}1&0\end{bmatrix}$, $C=\begin{bmatrix}1&1\\0&1\end{bmatrix}$. The formula gives $(1,0)^{\mathsf T}$, but the unit's own $A^+$ for $\begin{bmatrix}1&1\end{bmatrix}$ is $\tfrac12(1,1)^{\mathsf T}$ (p. 192). Treat the claim with care and use the Penrose conditions (5) to check.
- Worked example 4.4 A asks for the projection $p_{1,2}$ of $b=(6,0,0,2)$ onto the first two columns of $H_4$. The printed solution (p. 185) does not state it.
- The "Confession" (p. 184) and Remarks (p. 194) mention Householder reflections, Chapter 7 and the SVD without developing them here.
