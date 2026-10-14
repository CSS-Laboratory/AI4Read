---
id: strang-2023-introduction/ch07-singular
work: strang-2023-introduction
unit: "7 The Singular Value Decomposition (SVD)"
pages: 286-307
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The Singular Value Decomposition (SVD)

## L0 — One line
Every matrix factors as (orthogonal) × (diagonal) × (orthogonal), $A=U\Sigma V^T$, and cutting that sum of rank-one pieces after $k$ terms gives the closest rank-$k$ matrix, which is used in image compression and in principal component analysis (PCA).

## L1 — The gist (≤ 120 words)
Eigenvectors of symmetric matrices are orthogonal, but general or rectangular matrices need something more. The chapter asks how to keep orthogonality for every $m\times n$ matrix. The answer is two orthonormal bases, $v$'s for inputs and $u$'s for outputs, with $Av_i=\sigma_iu_i$. The $v$'s and $u$'s are eigenvectors of $A^TA$ and $AA^T$, and the $\sigma_i^2$ are their shared nonzero eigenvalues. Keeping only the $k$ largest $\sigma$'s gives the best rank-$k$ approximation (Eckart–Young). This is used to compress images (7.2) and to find the directions of greatest variance in centred data (PCA, 7.3).

**Prerequisites:** eigenvalues/eigenvectors of symmetric matrices; orthogonal matrices; the four fundamental subspaces; rank, trace, determinant; vector length and dot product.

## L2 — Key ideas
- Every $m\times n$ matrix has $A=U\Sigma V^T=\sigma_1u_1v_1^T+\dots+\sigma_ru_rv_r^T$ with orthonormal $u$'s and $v$'s and $\sigma_1\ge\dots\ge\sigma_r>0$ (p. 286, p. 287).
- Geometrically, $V^T$ rotates (possibly reflects), $\Sigma$ stretches along the axes, $U$ rotates; the unit circle becomes an ellipse (p. 288).
- Proof: choose orthonormal eigenvectors $v_k$ of $A^TA$, set $\sigma_k=\sqrt{\lambda_k}$ and $u_k=Av_k/\sigma_k$. Then the $u_k$ are orthonormal eigenvectors of $AA^T$ (pp. 290–291).
- $AB$ and $BA$ have the same nonzero eigenvalues, so $A^TA$ and $AA^T$ share their nonzero eigenvalues (p. 292).
- $\sigma_1=\max\|Ax\|/\|x\|$; each later $\sigma_{k+1}$ is the same maximum over vectors perpendicular to $v_1,\dots,v_k$. Every eigenvalue of a square matrix satisfies $|\lambda|\le\sigma_1$ (p. 293).
- Eckart–Young: for rank-$k$ $B$, $\|A-A_k\|\le\|A-B\|$ in the spectral, Frobenius and nuclear norms (three ways to measure the size of a matrix, defined in L3) (pp. 302–303).
- Image compression keeps $k$ rank-one pieces. Stripe flags are rank 1; the triangle of 1's is hard to compress, the Hilbert matrix easy (pp. 297–299).
- PCA (principal component analysis): centre the data rows (subtract each row's mean). The left singular vectors of $A$ are the eigenvectors of $S=AA^T/(n-1)$. $u_1$ gives the closest line (perpendicular least squares) and $u_1,u_2$ the closest plane (pp. 304–306).

## L3 — Walkthrough

### Chapter introduction (p. 286)
The SVD extends eigenvectors to every matrix. It uses input vectors $v_1,\dots,v_n$ and output vectors $u_1,\dots,u_m$, both orthonormal. $v_1..v_r$ is a basis for the row space and $u_1..u_r$ for the column space, with $r=\operatorname{rank}(A)$. The right singular vectors $v_i$ are eigenvectors of $A^TA$ (bases for row space and nullspace). The left singular vectors $u_i$ are eigenvectors of $AA^T$ (bases for column space and left nullspace). Also $Av_i=\sigma_iu_i$ for $i\le r$, and $AV=U\Sigma$.

If $A=S$ is symmetric positive definite, then $u_i=v_i=q_i$ and $\sigma_i=\lambda_i$. For centred data, $AA^T$ (divided by $n-1$) is the sample covariance matrix, and PCA is based on the singular vectors of the data matrix.

### 7.1 Singular Values and Singular Vectors

**Setup and first example (p. 287).** For all $m\times n$ matrices we want orthonormal $v_1..v_n\in\mathbb R^n$ and $u_1..u_m\in\mathbb R^m$ with $Av=\sigma u$ instead of $Sx=\lambda x$. Example $A=\begin{bmatrix}5&4\\0&3\end{bmatrix}$ has orthogonal inputs and orthogonal outputs:
$$A\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}9\\3\end{bmatrix},\qquad A\begin{bmatrix}-1\\1\end{bmatrix}=\begin{bmatrix}-1\\3\end{bmatrix}.\tag{1}$$
Divide $(1,1),(-1,1)$ by $\sqrt2$ and $(3,1),(-1,3)$ by $\sqrt{10}$. Then
$$Av_1=3\sqrt5\,u_1,\qquad Av_2=\sqrt5\,u_2,\tag{2}$$
so $\sigma_1=3\sqrt5$ and $\sigma_2=\sqrt5$. In matrix form $AV=U\Sigma$:
$$AV=\begin{bmatrix}5&4\\0&3\end{bmatrix}\tfrac1{\sqrt2}\begin{bmatrix}1&-1\\1&1\end{bmatrix}=\tfrac1{\sqrt{10}}\begin{bmatrix}3&-1\\1&3\end{bmatrix}\begin{bmatrix}3\sqrt5&0\\0&\sqrt5\end{bmatrix}=U\Sigma.\tag{3}$$
Multiplying by $V^T$ gives $A=U\Sigma V^T$, which splits as
$$A=\sigma_1u_1v_1^T+\sigma_2u_2v_2^T.\tag{4}$$
The first piece is more important because $\sigma_1>\sigma_2$. Check: $\tfrac32\begin{bmatrix}3&3\\1&1\end{bmatrix}+\tfrac12\begin{bmatrix}1&-1\\-3&3\end{bmatrix}=\begin{bmatrix}5&4\\0&3\end{bmatrix}$. Each matrix is diagonalized by two sets of singular vectors, not one set of eigenvectors.

*Intuition note.* An eigenvector problem uses one basis for input and output. The SVD lets the input basis and output basis differ, and it still keeps both orthonormal. Each rank-one piece $\sigma_iu_iv_i^T$ is a "layer" of $A$, ordered by size.

**The geometry (p. 288).** $A=U\Sigma V^T$ is (orthogonal)×(diagonal)×(orthogonal). $U$ and $V$ are rotations and possible reflections; $\Sigma$ stretches along the axes. Vectors $v$ on the unit circle go to $Av=\sigma u$ on an ellipse (Figure 7.1; there $A/\sqrt5$ has $\sigma_1=3,\sigma_2=1$). In 2D with positive determinants (no reflections):
$$A=\begin{bmatrix}a&b\\c&d\end{bmatrix}=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}\begin{bmatrix}\sigma_1&\\&\sigma_2\end{bmatrix}\begin{bmatrix}\cos\phi&\sin\phi\\-\sin\phi&\cos\phi\end{bmatrix}.\tag{5}$$
The author's five questions:
- Q1: a symmetric matrix has $b=c$, so 3 parameters instead of 4. The text asks how $\theta,\phi,\sigma_1,\sigma_2$ reduce to 3 numbers and gives no answer.
- Q2: $\theta=30^\circ$, $\sigma_1=2$, $\sigma_2=1$, $\phi=60^\circ$ gives $A=\tfrac14\begin{bmatrix}3\sqrt3&5\\-1&3\sqrt3\end{bmatrix}$, with determinant 2 (eq. 6).
- Q3: a 3×3 matrix has 9 parameters: 3 singular values plus 3 rotations each in $U$ and $V$. For a pilot these are pitch, roll and yaw.
- Q4: if $S=Q\Lambda Q^T$ is symmetric positive definite, its SVD is exactly $U=V=Q$, $\Sigma=\Lambda$.
- Q5: if $S$ has an eigenvalue $-a$ with $Sx=-ax$, then $\sigma=+a$. One singular vector ($u$ or $v$) must be $-x$, and the two sign changes cancel.

**Full-size form (p. 289).** Add basis vectors $v_{r+1}..v_n$ (nullspace of $A$) and $u_{r+1}..u_m$ (left nullspace) so that $V$ is $n\times n$ and $U$ is $m\times m$. Then $\Sigma$ is $m\times n$, zero except for $\sigma_1\ge\dots\ge\sigma_r>0$ on its diagonal:
$$AV=U\Sigma\quad (m\times n)(n\times n)=(m\times m)(m\times n),\qquad V^T=V^{-1},\ U^T=U^{-1}.\tag{6}$$
Multiplying on the right by $V^T$ gives $A=U\Sigma V^T$.

**Reduced form (p. 289).** Dropping the parts that only produce zeros gives $AV_r=U_r\Sigma_r$ with $\Sigma_r$ square ($r\times r$) and shapes $(m\times n)(n\times r)=(m\times r)(r\times r)$:
$$AV_r=U_r\Sigma_r,\qquad Av_i=\sigma_iu_i.\tag{7}$$
Still $V_r^TV_r=I_r$ and $U_r^TU_r=I_r$. But $V_rV_r^T\ne I$ and $U_rU_r^T\ne I$ when these are not square. $A=U_r\Sigma_rV_r^T=u_1\sigma_1v_1^T+\dots+u_r\sigma_rv_r^T$ is still true. The author prefers the reduced form. Example 1: the 2×2 matrix has $r=m=n$, so reduced = full. Example 2: $A=[1\ 2\ 2]=[1][3][1\ 2\ 2]/3$ has $r=1$, $\sigma_1=3$.

**Proof of the SVD (p. 290).** Form the symmetric matrices
$$A^TA=(V\Sigma^TU^T)(U\Sigma V^T)=V\Sigma^T\Sigma V^T\quad(U^TU=I),\tag{8}$$
$$AA^T=(U\Sigma V^T)(V\Sigma^TU^T)=U\Sigma\Sigma^TU^T\quad(V^TV=I).\tag{9}$$
Both have the form $Q\Lambda Q^T$. So $V$ holds orthonormal eigenvectors of $A^TA$, $U$ holds orthonormal eigenvectors of $AA^T$, and $\sigma_1^2..\sigma_r^2$ are the nonzero eigenvalues of both.

The choice of the $v$'s decides the signs of the $u$'s, because the SVD needs $Av_k=\sigma_ku_k$. If $\lambda$ is a double eigenvalue there is a whole plane of eigenvectors. So start with the $v$'s: choose orthonormal eigenvectors $v_1..v_r$ of $A^TA$, set $\sigma_k=\sqrt{\lambda_k}$, and define
$$A^TAv_k=\sigma_k^2v_k,\qquad u_k=\frac{Av_k}{\sigma_k}\ (k=1..r).\tag{10}$$
Check that the $u_k$ are eigenvectors of $AA^T$:
$$AA^Tu_k=AA^T\Big(\frac{Av_k}{\sigma_k}\Big)=A\Big(\frac{A^TAv_k}{\sigma_k}\Big)=A\frac{\sigma_k^2v_k}{\sigma_k}=\sigma_k^2u_k.\tag{11}$$
Check orthonormality:
$$u_j^Tu_k=\Big(\frac{Av_j}{\sigma_j}\Big)^T\Big(\frac{Av_k}{\sigma_k}\Big)=\frac{v_j^T(A^TAv_k)}{\sigma_j\sigma_k}=\frac{\sigma_k}{\sigma_j}v_j^Tv_k=\begin{cases}1&j=k\\0&j\neq k\end{cases}\tag{12}$$
The key was moving parentheses, $(AA^T)A=A(A^TA)$, by the associative law.

**Example 1 completed (p. 291).** $A=\begin{bmatrix}5&4\\0&3\end{bmatrix}$ has $A^TA=\begin{bmatrix}25&20\\20&25\end{bmatrix}$ and $AA^T=\begin{bmatrix}41&12\\12&9\end{bmatrix}$. Both have trace 50 and eigenvalues $45$ and $5$. So $\sigma_1=\sqrt{45}=3\sqrt5$, $\sigma_2=\sqrt5$, and $\sigma_1\sigma_2=15=\det A$. The author notes $\sigma_1$ is larger than $\lambda_{\max}(A)=5$ and $\sigma_2$ is smaller than $\lambda_{\min}(A)=3$. Eigenvectors of $A^TA$ are $(1,1)$ for 45 and $(-1,1)$ for 5, so $v_1=\frac1{\sqrt2}(1,1)$ and $v_2=\frac1{\sqrt2}(-1,1)$. Then, as printed on p. 291, $Av_1=\sqrt{45}\frac1{\sqrt{10}}(1,3)$ and $Av_2=\sqrt5\frac1{\sqrt{10}}(-3,1)$. These coordinates look swapped: direct multiplication gives $Av_1=\frac3{\sqrt2}(3,1)$ and $Av_2=\frac1{\sqrt2}(-1,3)$, matching $u_1,u_2$ on p. 287 (added remark; see Reading notes). The printed result is:
$$U=\tfrac1{\sqrt{10}}\begin{bmatrix}1&-3\\3&1\end{bmatrix},\quad\Sigma=\begin{bmatrix}\sqrt{45}&\\&\sqrt5\end{bmatrix},\quad V^T=\tfrac1{\sqrt2}\begin{bmatrix}1&1\\-1&1\end{bmatrix}.\tag{13}$$
The last $n-r$ $v$'s and $m-r$ $u$'s are any orthonormal bases of $N(A)$ and $N(A^T)$. They are automatically orthogonal to the earlier vectors because $N(A)\perp C(A^T)$ and $N(A^T)\perp C(A)$. The author adds that good codes do not start with $A^TA$ and $AA^T$ (see "Computing" below).

*Intuition note.* $A^TA$ and $AA^T$ are symmetric, so they have orthonormal eigenvectors. Defining $u_k=Av_k/\sigma_k$ links the two sets so that $A$ sends each $v_k$ to its own $u_k$.

**$AB$ and $BA$: equal nonzero eigenvalues (p. 292).** If $A$ is $m\times n$ and $B$ is $n\times m$, then $AB$ and $BA$ have the same nonzero eigenvalues. Proof: from $ABx=\lambda x$ with $\lambda\ne0$, multiply by $B$ to get $BA(Bx)=\lambda(Bx)$. Here $\lambda\neq0$ ensures $Bx\ne0$, so $Bx$ is a nonzero eigenvector of $BA$. If $B$ is square and invertible, $B^{-1}(BA)B=AB$ (similar). The first proof also covers $B=A^T$. If $m>n$, $AB$ has $m-n$ extra zero eigenvalues compared with $BA$.

**Singular vectors for 2×2 (picture proof, p. 292).** We look for perpendicular $v,w$ with $Av\perp Aw$. Start with $V=(1,0)$, $W=(0,1)$. If the angle $\theta$ from $AV$ to $AW$ is below $90^\circ$, then the angle from $AW$ to $-AV$ is $180-\theta$, above $90^\circ$. So somewhere as $v$ moves from $V$ toward $W$, the angle is exactly $90^\circ$ (Figure 7.2).

**The first singular vector $v_1$ (p. 293).**
$$\text{Maximize }\frac{\|Ax\|}{\|x\|};\ \text{the maximum is }\sigma_1\text{ at }x=v_1.\tag{14}$$
This does not assume $U,\Sigma,V$ are known. Square it and write $S=A^TA$:
$$\frac{\|Ax\|^2}{\|x\|^2}=\frac{x^TA^TAx}{x^Tx}=\frac{x^TSx}{x^Tx}\quad\text{(the Rayleigh quotient)}.\tag{15}$$
Write $x=c_1x_1+\dots+c_nx_n$ with $Sx_i=\lambda_ix_i$ (taking the eigenvectors orthonormal, as the formula needs; added):
$$\frac{x^TSx}{x^Tx}=\frac{c_1^2\lambda_1+\dots+c_n^2\lambda_n}{c_1^2+\dots+c_n^2}\le\lambda_1=\text{largest eigenvalue of }S.\tag{16}$$
So the best $x$ is an eigenvector of $S$, and the maximum is $\lambda_1(S)=\sigma_1^2(A)$. For $v_2$, maximize $\|Ax\|/\|x\|$ under $v_1^Tx=0$; the maximum is $\sigma_2$ at $x=v_2$. Generally $v_{k+1}$ gives the maximum ratio over all $x\perp v_1..v_k$. (The text mentions Lagrange multipliers and Problem 9 as a direct way to handle the constraint; the Problem 9 in the printed list is a different question, see Reading notes.)

*Question and answer (p. 293).* Why are all eigenvalues of a square $A$ at most $\sigma_1$ in size? Because orthogonal matrices keep lengths:
$$\|Ax\|=\|U\Sigma V^Tx\|=\|\Sigma V^Tx\|\le\sigma_1\|V^Tx\|=\sigma_1\|x\|.\tag{17}$$
An eigenvector has $\|Ax\|=|\lambda|\|x\|$, so $|\lambda|\le\sigma_1$.

*Intuition note.* $\sigma_1$ is the biggest stretch $A$ can apply to any unit vector. The direction of that stretch is $v_1$. The next singular vector is the biggest stretch among directions that remain.

**Rank-one example (p. 294).** For $A=xy^T$: $u_1=x/\|x\|$, $v_1=y/\|y\|$, $\sigma_1=\|x\|\|y\|$ is the only nonzero singular value:
$$A=xy^T=\frac{x}{\|x\|}\big(\|x\|\|y\|\big)\frac{y^T}{\|y\|}=u_1\sigma_1v_1^T.\tag{18}$$
Its only nonzero eigenvalue is $\lambda_1=y^Tx$ with eigenvector $x$. So $|\lambda_1|\le\sigma_1$ becomes exactly the Schwarz inequality $|y^Tx|\le\|x\|\|y\|$.

**Computing eigenvalues and singular values (p. 294).** A symmetric $S$ can be reduced by an orthogonal $Q$ to tridiagonal form $Q^{-1}SQ$ (limited freedom to create zeros). For singular values, $Q_1^{-1}AQ_2$ has the same $\sigma$'s even when $Q_1\ne Q_2$. There is more freedom, so it can be made bidiagonal:
$$Q^{-1}SQ=\text{tridiagonal }(a_i\text{ on diagonal},\ b_i\text{ beside it})\ \text{[for }\lambda\text{'s]},\qquad Q_1^{-1}AQ_2=\text{bidiagonal }(c_i,\ d_i)\ \text{[for }\sigma\text{'s]}.\tag{19}$$
The author says not to multiply out $A^TA$ and find its eigenvalues: that is unnecessary work and squares the condition of the problem. The Golub–Kahan algorithm works on $A$ directly. Step 1 makes $A$ bidiagonal, costing $O(mn^2)$ multiplications. Step 2 adjusts the shifted QR algorithm to preserve the singular values, normally $O(n^2)$ multiplications. For truly large $A$, randomized sampling gives accurate results with very high probability.

### 7.2 Image Processing by Linear Algebra

**Flags (pp. 297–298).** An image is a matrix of grayscale values (one per pixel and colour). If nearby pixels are correlated, the image can be compressed (p. 297). The SVD approach replaces $A=\sum_1^r\sigma_iu_iv_i^T$ by the first $k$ terms $A_k$. A three-stripe flag has rank 1: France is the column $(1,..,1)^T$ times the row $(b\,b\,w\,w\,r\,r)$, and Germany is nearly its transpose. The text says each flag matrix reduces to two vectors, so to transmit it "we can replace $N$ pixels by $2N$ pixels" (wording as printed; see Reading notes). Curved badges (Japan, Maldives) give infinite rank, so compression is possible but not to rank one. Greece: the author first thought rank 4 but now thinks row 2 + row 3 = row 1, so rank 3. Tonga appears to have rank 4 (the left half has four independent-looking rows), the "champion flag of finite rank" (p. 298).

**Singular values of the triangle of 1's (pp. 298–299).** Take the lower-triangular matrix $A$ of 1's with $A^{-1}$ having $1$ on the diagonal and $-1$ below it. $A$ has full rank $N$ and all eigenvalues 1, so there are $N$ positive singular values; the text says none equals 1 (but see Reading notes: its own formula gives $\sigma=1$ for $n=4$). For $n=4$,
$$AA^T=\begin{bmatrix}1&1&1&1\\1&2&2&2\\1&2&3&3\\1&2&3&4\end{bmatrix},\qquad (AA^T)^{-1}=(A^{-1})^TA^{-1}=\begin{bmatrix}2&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{bmatrix}.\tag{1}$$
The author says the eigenvalues of this $-1,2,-1$ matrix have the form $2-2\cos\theta$, so
$$\lambda(AA^T)=\frac1{2-2\cos\theta}=\frac1{4\sin^2(\theta/2)},\qquad \sigma(A)=\sqrt\lambda=\frac1{2\sin(\theta/2)},\tag{2}$$
with the $n$ angles $\theta=\frac{\pi}{2n+1},\frac{3\pi}{2n+1},\dots,\frac{(2n-1)\pi}{2n+1}$. For $n=4$ this includes $\theta=3\pi/9$, where $2\sin(\theta/2)=1$. The singular values drop off, but not steeply, so the SVD gives only moderate compression for this triangle (Figure 7.3: all $\sigma$'s of `tril(ones(40))` exceed 1/2). The Hilbert matrix $H(i,j)=(i+j-1)^{-1}$ has a very steep dropoff and low effective rank. The author states the "never below ½" behaviour, seen with Alex Townsend for other 0–1 shapes, "has not yet been explained" (p. 299).

**Image compression (pp. 299–301).** Keeping more terms $\sigma uv^T$ improves the picture. Tim Baumann's website demonstrates this. For a 600×600 image (360000 pixels), compressed size is about $600\times k+k+k\times600$. With $k=300$ this is $360300$ (ratio 1.00); with $k=20$ it is $24020$ (ratio $360000/24020=14.99$). The best ratio depends on image complexity: the girl and the Mondrian painting allow higher compression than the city, tree or cats (p. 301). $k=80$ uses $600\times80+80+80\times600$.

### 7.3 Principal Component Analysis (PCA by the SVD)

**Low-rank approximation (p. 302).** The principal components of $A$ are its singular vectors. PCA uses the largest $\sigma$'s with their $u$'s and $v$'s. Define $A_k=\sigma_1u_1v_1^T+\dots+\sigma_ku_kv_k^T$, which has rank $k$.

**Eckart–Young.** $A_k$ is the closest rank-$k$ matrix:
$$\text{If }B\text{ has rank }k\text{ then }\|A-A_k\|\le\|A-B\|.\tag{1}$$
Schmidt (1907) began the proof (for operators). Eckart and Young used the Frobenius norm. Mirsky allowed any norm depending only on the singular values. Three norms:
$$\|A\|_2=\max\frac{\|Ax\|}{\|x\|}=\sigma_1,\tag{2}$$
$$\|A\|_F=\sqrt{\sigma_1^2+\dots+\sigma_r^2},\tag{3}$$
$$\|A\|_N=\sigma_1+\dots+\sigma_r\ \text{(nuclear or trace norm)}.\tag{4}$$
For the $n\times n$ identity, and equally for any orthogonal $Q$ (all $\sigma_i=1$):
$$\|I\|_2=1,\quad\|I\|_F=\sqrt n,\quad\|I\|_N=n.\tag{5, 6}$$
All three norms are unchanged when $A$ is multiplied on either side by an orthogonal matrix, so $\|A\|=\|\Sigma\|$.

**Norm of a matrix (p. 303).** The Frobenius norm (also called Hilbert–Schmidt) sums squares of all entries:
$$\|v\|^2=v_1^2+\dots+v_n^2,\qquad\|A\|_F^2=a_{11}^2+\dots+a_{1n}^2+\dots+a_{m1}^2+\dots+a_{mn}^2.\tag{7}$$
Triangle inequalities: $\|v+w\|\le\|v\|+\|w\|$ and $\|A+B\|_F\le\|A\|_F+\|B\|_F$ (8). Schwarz inequalities: $|v^Tw|\le\|v\|\|w\|$ and $\|AB\|_F\le\|A\|_F\|B\|_F$ (9). The matrix version follows from the vector one: $|(AB)_{ij}|^2\le\|\text{row }i\text{ of }A\|^2\|\text{column }j\text{ of }B\|^2$; add over all $i,j$. A matrix dot product is $A\cdot B=\operatorname{trace}(A^TB)$. The largest $|\lambda|$ is not a norm: a nonzero matrix can have all eigenvalues zero. But $\sigma_1=\|A\|_2$ works.

**Example.** The closest rank-2 matrix to $A=\operatorname{diag}(4,3,2,1)$ is $A_2=\operatorname{diag}(4,3,0,0)$. Then $\|A-A_2\|_F=\sqrt{2^2+1^2}$. This diagonal case covers all matrices $Q_1AQ_2$, hence all matrices with singular values $4,3,2,1$. Chi-Kwong Li simplified Mirsky's proof for all norms depending only on the $\sigma$'s.

*Intuition note.* Orthogonal factors do not change sizes, so the size of $A$ is the size of its $\Sigma$. The Eckart–Young theorem then says that cutting off the smallest $\sigma$'s gives the closest matrix of rank $k$.

**PCA setup (p. 304).** The data matrix $A_0$ has $m$ rows (variables) and $n$ columns (samples). Subtract each row's mean to get centred $A$. Its columns sum to zero, so the average column is zero. The $n$ points often cluster near a line or low-dimensional subspace of $\mathbb R^m$. The closest line through $(0,0)$ is in the direction of $u_1$. (Figure 7.4: $A$ is $2\times n$, $AA^T$ is $2\times2$, $A^TA$ is $n\times n$.)

**Geometry behind PCA (p. 304).** The best line solves *perpendicular least squares* (orthogonal regression). Ordinary least squares (Section 4.3) minimizes $\|Ax-b\|^2$ (vertical distances) and leads to $A^TA\hat x=A^Tb$. PCA minimizes perpendicular distances and leads to eigenvectors of $AA^T$. Split each column $a_j$ along $u_1,u_2$:
$$\sum_1^n\|a_j\|^2=\sum_1^n|a_j^Tu_1|^2+\sum_1^n|a_j^Tu_2|^2.\tag{10}$$
The left side is fixed by the data. The first sum on the right equals $u_1^T(AA^T)u_1$. Maximizing it with the top eigenvector $u_1$ minimizes the second sum, the squared distance to the line.

**Geometric meaning of Eckart–Young (p. 305).** For a 3×$n$ centred $A$, the closest line is again $u_1$. If the points fan out, the closest plane is spanned by $u_1$ and $u_2$, and "the best plane contains the best line".

**Statistics behind PCA (p. 305).** Variances are the diagonal entries of $AA^T$; covariances are the off-diagonal entries (dot products of rows). The sample covariance matrix is $S=AA^T/(n-1)$ (the factor $n-1$ because one degree of freedom was used by mean $=0$). Example (six children, centred):
$$A=\begin{bmatrix}3&-4&7&1&-4&-3\\7&-6&8&-1&-1&-7\end{bmatrix},\qquad S=\tfrac1{6-1}AA^T=\begin{bmatrix}20&25\\25&40\end{bmatrix}.$$
$S$ is positive definite.

**Results for the example (p. 306).** The orthogonal eigenvectors of $S$ are the left singular vectors $u_1,u_2$ (the principal components). By Eckart–Young, $u_1$ points along the closest line and $u_2$ is perpendicular to it. $S$ has eigenvalues near 57 and 3, summing to $20+40=60=\operatorname{trace}S$. The leading eigenvector is $u_1\approx(0.6,0.8)$, so the line has slope near $8/6$. Important note: computing $S$ from $A$ can be a computational mistake. For large matrices, a direct SVD of $A$ is faster and more accurate. Going to $AA^T$ squares $\sigma_1$, $\sigma_r$ and the condition number $\sigma_1/\sigma_r$.

**Linear algebra behind PCA (p. 306).**
$$\text{Total variance }T=\|A\|_F^2/(n-1)=(\|a_1\|^2+\dots+\|a_n\|^2)/(n-1)=\operatorname{trace}(S).\tag{11}$$
The trace equals the sum of the eigenvalues of $S$. The author writes
$$T=\sigma_1^2+\dots+\sigma_r^2.\tag{12}$$
The first principal component explains a fraction $\sigma_1^2/T$ of total variance, the next $\sigma_2^2/T$, and so on. The $u_i$ separate the data into uncorrelated pieces in order of decreasing variance. Eckart–Young implies that $k$ singular vectors acting together explain more of the data than any other set of $k$ vectors. So $u_1..u_k$ is a justified basis for the $k$-dimensional subspace closest to the points. The "effective rank" is the number of singular values above the point where noise drowns the signal. Often this is visible as an "elbow" in a scree plot of the $\sigma$'s or $\sigma^2$'s.

*Intuition note.* PCA asks which direction the centred points spread out most along. Since that direction maximizes the sum of squared projections, it also minimizes the sum of squared perpendicular distances. The SVD supplies all such directions at once, ordered by variance.

## Toy example (ours, not from the text)
Take $A=\begin{bmatrix}0&2\\1&0\end{bmatrix}$.
- $A^TA=\begin{bmatrix}0&1\\2&0\end{bmatrix}\begin{bmatrix}0&2\\1&0\end{bmatrix}=\begin{bmatrix}1&0\\0&4\end{bmatrix}$. The eigenvalues are $4$ and $1$, so $\sigma_1=2$, $\sigma_2=1$.
- Eigenvectors: $v_1=(0,1)$ for 4, $v_2=(1,0)$ for 1.
- $u_1=Av_1/\sigma_1=(2,0)/2=(1,0)$ and $u_2=Av_2/\sigma_2=(0,1)/1=(0,1)$.
- Pieces: $\sigma_1u_1v_1^T=2\begin{bmatrix}1\\0\end{bmatrix}[0\ 1]=\begin{bmatrix}0&2\\0&0\end{bmatrix}$ and $\sigma_2u_2v_2^T=\begin{bmatrix}0\\1\end{bmatrix}[1\ 0]=\begin{bmatrix}0&0\\1&0\end{bmatrix}$. The sum is $A$.
- Checks: $\sigma_1\sigma_2=2=|\det A|$ (here $\det A=-2$). $\sum a_{ij}^2=0+4+1+0=5=\sigma_1^2+\sigma_2^2$.
- The eigenvalues of $A$ satisfy $\lambda^2=2$, so $|\lambda|=\sqrt2\le\sigma_1=2$.
- The best rank-1 matrix is $A_1=\begin{bmatrix}0&2\\0&0\end{bmatrix}$. The error $A-A_1=\begin{bmatrix}0&0\\1&0\end{bmatrix}$ has $\|\cdot\|_F=1=\sigma_2$.

## Concepts
- [[singular-value-decomposition]] — $A=U\Sigma V^T$ with orthonormal $U,V$ and $\sigma_1\ge\dots\ge\sigma_r>0$; works for every $m\times n$ matrix (p. 287)
- [[reduced-svd]] (new) — $A=U_r\Sigma_rV_r^T$ keeping only the $r$ nonzero $\sigma$'s; $\Sigma_r$ square (p. 289)
- [[rank-one-matrix-outer-product]] — $A$ is a sum of $r$ pieces $\sigma_iu_iv_i^T$ (p. 286, p. 294)
- [[orthonormal-basis-orthogonal-matrix]] — $U$, $V$ with $U^TU=I$, $V^TV=I$; rotations/reflections that keep length (p. 288)
- [[four-fundamental-subspaces]] — $v$'s span row space and nullspace; $u$'s span column space and left nullspace (p. 286, p. 289)
- [[eigenvector-eigenvalue]] — $\sigma_i^2$ are eigenvalues of $A^TA$ and $AA^T$; for SPD $S$, $\sigma_i=\lambda_i$ (p. 290; SPD case p. 286, p. 288)
- [[ab-ba-equal-nonzero-eigenvalues]] (new) — $AB$ and $BA$ share nonzero eigenvalues (p. 292)
- [[rayleigh-quotient]] — $x^TSx/x^Tx\le\lambda_1$; for $S=A^TA$ its max is $\sigma_1^2$ (p. 293)
- [[norm]] — spectral $\|A\|_2=\sigma_1$, Frobenius $\sqrt{\sum\sigma_i^2}$, nuclear $\sum\sigma_i$ (p. 302)
- [[eckart-young-theorem]] — truncated SVD $A_k$ is closest rank-$k$ matrix in these norms (p. 302, p. 303)
- [[principal-component-analysis]] — SVD of centred data; $u_1$ gives the closest line, $u_1,u_2$ the closest plane (p. 302, p. 304)
- [[covariance-matrix]] — $S=AA^T/(n-1)$ for centred $A$; diagonal = variances, off-diagonal = covariances (p. 305)
- [[condition-number]] — $\sigma_1/\sigma_r$; squared when forming $AA^T$ (p. 306)
- [[perpendicular-least-squares]] (new) — minimizes perpendicular distances (orthogonal regression); differs from ordinary least squares (p. 304)
- [[effective-rank-scree-plot]] (new) — number of $\sigma$'s above the noise level, read at the "elbow" (p. 306)
- [[golub-kahan-bidiagonalization]] (new) — compute $\sigma$'s by bidiagonalizing $A$ then shifted QR, not via $A^TA$ (p. 294)

## Canonical instances
- [[svd-5-4-0-3-matrix]] (new) — $\begin{bmatrix}5&4\\0&3\end{bmatrix}$: $\sigma=3\sqrt5,\sqrt5$, worked in full (p. 287, p. 291)
- [[triangle-of-ones-matrix]] (new) — lower-triangular 1's; singular values $1/(2\sin(\theta/2))$, not very compressible (p. 299)
- [[hilbert-matrix]] — $H(i,j)=(i+j-1)^{-1}$; steep dropoff, low effective rank (p. 299)
- [[flag-matrices]] (new) — stripe flags rank 1; Greece rank 3, Tonga rank 4 (pp. 297–298)
- [[age-height-covariance-example]] (new) — six children; $S=\begin{bmatrix}20&25\\25&40\end{bmatrix}$, $u_1\approx(0.6,0.8)$ (p. 305, p. 306)
- [[image-compression-demo]] (new) — 600×600 image, $k=20$ gives ratio 14.99 (p. 300)

## Bridges (candidates)
- [same-math] PCA via SVD of centred $A$ ↔ eigendecomposition of covariance $S=AA^T/(n-1)$: $u_i$ and $\sigma_i^2$ are eigenvectors and eigenvalues of $AA^T$.
- [same-math] $\sigma_1=\max\|Ax\|/\|x\|$ ↔ Rayleigh quotient of $A^TA$ (variational characterization of top eigenvalue).
- [structural-analogy] Eckart–Young truncation ↔ latent-factor / dimension-reduction models for survey or ratings matrices: keep few strong components, treat the rest as noise.
- [same-math] Forming $AA^T$ squares $\sigma_1/\sigma_r$ ↔ numerical analysis: squaring the condition number when solving via normal equations.

## Questions this raises
- Why are the singular values of the triangle of 1's bounded below by about ½? The author says this is not yet explained (p. 299).
- How should one choose $k$ in practice, i.e. where is the "elbow" when the scree plot has no clear break?
- Why does centring matter for PCA? What would the SVD of an uncentred data matrix find instead?
- The proof of Eckart–Young is only cited (Schmidt, Eckart–Young, Mirsky, Li). What is the key step for the Frobenius norm?

## Exercises worth doing
- Ex. 2, Problem Set 7.1 (p. 295) — compares eigenvalue and singular-value changes after a tiny perturbation of $A$ — difficulty: easy
- Ex. 4, Problem Set 7.1 (p. 295) — shows $\begin{bmatrix}0&A\\A^T&0\end{bmatrix}$ has eigenvalues $\pm\sigma_k$, linking symmetric eigenproblems to the SVD — difficulty: medium
- Ex. 1, Problem Set 7.2 (p. 301) — why the identity is hard to compress, and a rank-2 cross flag — difficulty: easy
- Ex. 1, Problem Set 7.3 (p. 307) — full PCA pipeline: centre, covariance, eigenvalues, closest line — difficulty: easy
- Ex. 5, Problem Set 7.3 (p. 307) — ordinary least squares versus perpendicular least squares on the same data — difficulty: medium
- Ex. 7, Problem Set 7.3 (p. 307) — singular values of $A-A_3$ (Eckart–Young, error structure) — difficulty: easy

## Reading notes
- Printed page = pdf page − 10 (pdf 296 = printed 286).
- Section 7.1 equation numbers restart in 7.2 and 7.3; L3 uses the author's numbers within each section.
- Misprints and inconsistencies seen in the images:
  - p. 304 text says "Figure 7.3 shows a typical set of data points", but the figure is captioned Figure 7.4.
  - p. 306 refers to a scree plot as "Figure 7.2"; no scree plot appears in these pages.
  - p. 306: S has eigenvalues $\lambda_i=\sigma_i^2$ and eq. (12) states $T=\sigma_1^2+\dots+\sigma_r^2$. Since $S=AA^T/(n-1)$, this is consistent with (11) only if the $\sigma$'s are those of $A/\sqrt{n-1}$ (the example's "$\sqrt{57}u_1v_1^T$" uses the same scaling). For the singular values of $A$ itself, $T=(\sigma_1^2+\dots+\sigma_r^2)/(n-1)$ (added remark).
  - p. 293 refers to "Problem 9" for the constraint $v_1^Tx=0$, but printed Problem 9 (p. 296) asks about orthogonal matrices; Problems 10–11 are the closest match.
- Q1 on p. 288 is posed without an answer.
- p. 291 prints $Av_1=\frac3{\sqrt2}(1,3)$, $Av_2=\frac1{\sqrt2}(-3,1)$ and $U=\frac1{\sqrt{10}}\begin{bmatrix}1&-3\\3&1\end{bmatrix}$ in (13). These conflict with $A(1,1)^T=(9,3)^T$ and with $u_1,u_2$ on p. 287. Direct multiplication gives $Av_1=\frac3{\sqrt2}(3,1)$, $Av_2=\frac1{\sqrt2}(-1,3)$ and $U=\frac1{\sqrt{10}}\begin{bmatrix}3&-1\\1&3\end{bmatrix}$ (added remark; $U\Sigma V^T=A$ checked). $\Sigma$ and $V^T$ in (13) are correct as printed.
- p. 297 says "replace $N$ pixels by $2N$ pixels"; this wording is kept as printed and is presumably loose.
- p. 298 says all $N$ singular values of the triangle matrix differ from 1, but p. 299 notes that for $n=4$ the angle $\theta=3\pi/9$ gives $2\sin(\theta/2)=1$, i.e. $\sigma=1$. The text contradicts itself here.
- The text layer of pp. 287–291 was heavily garbled; all matrices above were checked against the page images.
- Pages 295–296 and 307 are problem sets, as is the lower part of p. 301 (Problem Set 7.2); solutions are not printed.
