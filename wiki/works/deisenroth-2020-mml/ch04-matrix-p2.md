---
id: deisenroth-2020-mml/ch04-matrix-p2
work: deisenroth-2020-mml
unit: "4 Matrix Decompositions (part 2/2): 4.5 Singular Value Decomposition to 4.8 Further Reading, plus Exercises"
pages: 119-138
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Singular Value Decomposition, Low-Rank Approximation and the Matrix Phylogeny

## L0 — One line
Every real matrix factors as $A=U\Sigma V^\top$ (rotate, scale, rotate), and writing it as a sum of rank-1 pieces and cutting the sum after $k$ terms gives the best rank-$k$ approximation in the spectral norm.

## L1 — The gist (≤ 120 words)
Eigendecomposition needs square matrices and may not exist. This unit asks for a decomposition that works for any $m\times n$ matrix. The answer is the SVD, $A=U\Sigma V^\top$. $V$ holds the eigenvectors of $A^\top A$, $U$ holds the normalised images $Av_i/\sigma_i$, and the singular values are $\sigma_i=\sqrt{\lambda_i}$. Writing $A$ as a sum of rank-1 matrices $\sigma_i u_i v_i^\top$ lets us truncate it. The Eckart–Young theorem says the truncation is the best rank-$k$ approximation in the spectral norm (the largest factor by which a matrix can stretch a vector), with error $\sigma_{k+1}$. Examples cover a hand-computed SVD, movie ratings and image compression. A "phylogeny" figure and further reading close the part.

**Prerequisites:** eigenvalues/eigenvectors, spectral theorem for symmetric matrices, orthogonal matrices, rank and null space, basis change, vector norms.

## L2 — Key ideas (5–10 bullets)
- The SVD exists for every real matrix $A\in\mathbb R^{m\times n}$. It has the form $U\Sigma V^\top$ with $U$, $V$ orthogonal and $\Sigma$ rectangular, diagonal and non-negative (p. 119).
- Geometrically, $V^\top$ changes basis in the domain, $\Sigma$ scales and changes dimension, and $U$ changes basis in the codomain. Eigendecomposition instead applies one basis change and then undoes it (pp. 120–121).
- Construction: diagonalise $A^\top A$ to get $V$ and $\sigma_i^2=\lambda_i$. Then the images $Av_i$ are orthogonal, and dividing by $\sigma_i$ gives orthonormal $u_i=Av_i/\sigma_i$ (pp. 123–125).
- Compared with eigendecomposition, the SVD always exists, uses orthonormal $U,V$ and has non-negative real $\Sigma$. For symmetric matrices the two coincide (p. 127).
- $A=\sum_i\sigma_i u_iv_i^\top$ is a sum of rank-1 matrices. Keeping the first $k$ terms gives a rank-$k$ approximation; in the Stonehenge example, rank 5 needs about 0.6% of the original numbers (p. 130).
- The spectral norm of $A$ is $\sigma_1$ (Theorem 4.24). Eckart–Young (Theorem 4.25): the truncated SVD minimises $\|A-B\|_2$ over rank-$k$ matrices $B$, and the minimum is $\sigma_{k+1}$ (p. 131).
- In the movie-ratings example, the author reads $u_i$ as "stereotypical movies" and $v_j$ as "stereotypical viewers" (under stated assumptions), and the rank-2 approximation is close to the data (pp. 127–133).
- Matrix types form a tree (Fig. 4.13). Diagonalisable is not the same as invertible (pp. 134–135).

## L3 — Walkthrough

### End of 4.4 (fragment)
The page opens with the end of a chain $\dots=\det(D)=\prod_i d_{ii}$ (4.63b). The author says this allows efficient computation of $\det A$. Eigendecomposition needs square matrices, so a more general tool is wanted (p. 119).

### 4.5 Singular Value Decomposition
The SVD is a central decomposition, called "fundamental theorem of linear algebra" by Strang (1993), because it applies to all matrices and always exists (p. 119).

**Theorem 4.22 (SVD).** Let $A\in\mathbb R^{m\times n}$ have rank $r\in[0,\min(m,n)]$. Then
$$A = U\,\Sigma\,V^\top \tag{4.64}$$
- $U\in\mathbb R^{m\times m}$ is orthogonal, with columns $u_i$ (left-singular vectors).
- $V\in\mathbb R^{n\times n}$ is orthogonal, with columns $v_j$ (right-singular vectors).
- $\Sigma\in\mathbb R^{m\times n}$ has $\Sigma_{ii}=\sigma_i\ge0$ and $\Sigma_{ij}=0$ for $i\ne j$ (p. 119).

The $\sigma_i$ are the singular values, ordered $\sigma_1\ge\sigma_2\ge\dots\ge\sigma_r\ge0$ (p. 119). $\Sigma$ is unique. It has the same size as $A$, so it needs zero padding (p. 119).
- If $m>n$, $\Sigma$ is diagonal up to row $n$, followed by zero rows $0^\top$ for rows $n+1$ to $m$ (4.65).
- If $m<n$, $\Sigma$ is diagonal up to column $m$, followed by zero columns for $m+1$ to $n$ (4.66) (pp. 119–120).

The SVD exists for any $A\in\mathbb R^{m\times n}$ (p. 120).

*Intuition note.* Every matrix, even a non-square one, can be written as "rotate, stretch along axes, rotate" (the text calls orthonormal $U,V$ rotations). The zero padding in $\Sigma$ just records that the input and output spaces can have different dimensions.

### 4.5.1 Geometric intuitions
The SVD splits the map $\Phi:\mathbb R^n\to\mathbb R^m$ into three operations (Fig. 4.8, p. 120). Assume $A$ is given in the standard bases, with second bases $\tilde B$ of $\mathbb R^n$ and $\tilde C$ of $\mathbb R^m$:
1. $V$ changes basis in the domain from $\tilde B$ to the standard basis, so $V^\top=V^{-1}$ goes from $B$ to $\tilde B$.
2. $\Sigma$ scales the new coordinates by $\sigma_i$ and adds or deletes dimensions. It is the matrix of $\Phi$ with respect to $\tilde B,\tilde C$.
3. $U$ changes basis in the codomain from $\tilde C$ to the canonical basis (p. 121).

The SVD changes basis in both domain and codomain. Eigendecomposition works in one space, applies a basis change and then undoes it. The two bases in the SVD are linked at the same time by $\Sigma$ (p. 121).

**Example 4.12.** Map a square grid of vectors in a $2\times2$ box using
$$A=\begin{bmatrix}1&-0.8\\0&1\\1&0\end{bmatrix}=U\Sigma V^\top,\quad U=\begin{bmatrix}-0.79&0&-0.62\\0.38&-0.78&-0.49\\-0.48&-0.62&0.62\end{bmatrix},\ \Sigma=\begin{bmatrix}1.62&0\\0&1.0\\0&0\end{bmatrix},\ V^\top=\begin{bmatrix}-0.78&0.62\\-0.62&-0.78\end{bmatrix}\tag{4.67}$$
$V^\top$ rotates the grid. $\Sigma$ stretches it by the singular values and embeds it in $\mathbb R^3$ with third coordinate 0. $U$ rotates it within $\mathbb R^3$, so the image is still a plane but no longer the $x_1$-$x_2$ plane (pp. 121–122, Fig. 4.9).

### 4.5.2 Construction of the SVD
*Remark.* For a symmetric positive definite $S=S^\top=PDP^\top$ (4.68) with SVD $S=U\Sigma V^\top$ (4.69), setting $U=P=V$, $D=\Sigma$ (4.70) shows that the SVD of an SPD matrix is its eigendecomposition (pp. 122–123).

Computing the SVD means finding orthonormal bases $U=(u_1,\dots,u_m)$ of $\mathbb R^m$ and $V=(v_1,\dots,v_n)$ of $\mathbb R^n$. The plan is: build $V$, build $U$, then link them by requiring that the images $Av_i$ stay orthogonal (p. 123).

**Right-singular vectors.** For any $A$, the matrix $A^\top A\in\mathbb R^{n\times n}$ is symmetric positive semidefinite (Thm 4.14). By the spectral theorem (Thm 4.15) it is diagonalisable with an orthonormal eigenbasis:
$$A^\top A=PDP^\top=P\begin{bmatrix}\lambda_1&&0\\&\ddots&\\0&&\lambda_n\end{bmatrix}P^\top,\quad\lambda_i\ge0\tag{4.71}$$
Now assume an SVD exists and insert (4.64):
$$A^\top A=(U\Sigma V^\top)^\top(U\Sigma V^\top)=V\Sigma^\top U^\top U\Sigma V^\top\tag{4.72}$$
With $U^\top U=I$:
$$A^\top A=V\Sigma^\top\Sigma V^\top=V\,\mathrm{diag}(\sigma_1^2,\dots,\sigma_n^2)\,V^\top\tag{4.73}$$
Comparing (4.71) and (4.73):
$$V^\top=P^\top\tag{4.74}$$
$$\sigma_i^2=\lambda_i\tag{4.75}$$
So the eigenvectors of $A^\top A$ are the right-singular vectors, and its eigenvalues are the squared singular values (p. 123–124).

**Left-singular vectors.** Use the symmetric $AA^\top\in\mathbb R^{m\times m}$:
$$AA^\top=(U\Sigma V^\top)(U\Sigma V^\top)^\top=U\Sigma V^\top V\Sigma^\top U^\top=U\,\mathrm{diag}(\sigma_1^2,\dots,\sigma_m^2)\,U^\top\tag{4.76}$$
Its orthonormal eigenvectors are the left-singular vectors $U$. $AA^\top$ and $A^\top A$ have the same nonzero eigenvalues (see page 106 of the book), so the nonzero entries of $\Sigma$ agree in both cases (p. 124).

**Linking.** For orthogonal eigenvectors $v_i,v_j$, $i\neq j$:
$$(Av_i)^\top(Av_j)=v_i^\top(A^\top A)v_j=v_i^\top(\lambda_jv_j)=\lambda_jv_i^\top v_j=0\tag{4.77}$$
So the images are orthogonal. For $m\ge r$, $\{Av_1,\dots,Av_r\}$ is a basis of an $r$-dimensional subspace of $\mathbb R^m$. Normalising gives
$$u_i:=\frac{Av_i}{\|Av_i\|}=\frac1{\sqrt{\lambda_i}}Av_i=\frac1{\sigma_i}Av_i\tag{4.78}$$
The author says the last equality uses (4.75) and (4.76b) (p. 124). Rearranging gives the **singular value equation**
$$Av_i=\sigma_iu_i,\quad i=1,\dots,r\tag{4.79}$$
It resembles the eigenvalue equation, but the vectors on the two sides differ (pp. 124–125).
- For $n<m$, (4.79) holds only for $i\le n$. Nothing is said about $u_i$ for $i>n$, but they are orthonormal by construction.
- For $m<n$, (4.79) holds only for $i\le m$. For $i>m$, $Av_i=0$. So the SVD also gives an orthonormal basis of the kernel (null space) of $A$ (p. 125).

Stacking the vectors as columns gives $AV=U\Sigma$ (4.80). Right-multiplying by $V^\top$ gives $A=U\Sigma V^\top$ (p. 125).

*Intuition note.* $V$ is found from the symmetric matrix $A^\top A$. $A$ then maps these perpendicular directions to perpendicular directions, whose lengths are the singular values. Dividing by those lengths gives $U$.

**Example 4.13.** $A=\begin{bmatrix}1&0&1\\-2&1&0\end{bmatrix}$ (4.81) (p. 125).
- *Step 1.* $A^\top A=\begin{bmatrix}5&-2&1\\-2&1&0\\1&0&1\end{bmatrix}$ (4.82). Its decomposition $PDP^\top$ has $D=\mathrm{diag}(6,1,0)$ and
$$V=P=\begin{bmatrix}\frac5{\sqrt{30}}&0&\frac{-1}{\sqrt6}\\\frac{-2}{\sqrt{30}}&\frac1{\sqrt5}&\frac{-2}{\sqrt6}\\\frac1{\sqrt{30}}&\frac2{\sqrt5}&\frac1{\sqrt6}\end{bmatrix}\tag{4.83–4.84}$$
- *Step 2.* Since $\mathrm{rk}(A)=2$, only two singular values are nonzero: $\sigma_1=\sqrt6$, $\sigma_2=1$. So $\Sigma=\begin{bmatrix}\sqrt6&0&0\\0&1&0\end{bmatrix}$ (4.85) (p. 126).
- *Step 3.* $u_1=\frac1{\sqrt6}Av_1=\begin{bmatrix}1/\sqrt5\\-2/\sqrt5\end{bmatrix}$ (4.86), $u_2=\frac11Av_2=\begin{bmatrix}2/\sqrt5\\1/\sqrt5\end{bmatrix}$ (4.87), so $U=\frac1{\sqrt5}\begin{bmatrix}1&2\\-2&1\end{bmatrix}$ (4.88) (p. 126).

The author warns that on a computer this route has poor numerical behaviour, and the SVD is normally computed without the eigendecomposition of $A^\top A$ (p. 126).

### 4.5.3 Eigenvalue decomposition vs. SVD
Comparison for $A=PDP^{-1}$ and $A=U\Sigma V^\top$ (pp. 126–127):
- The SVD always exists. Eigendecomposition is defined only for square matrices, and exists only if there is a basis of eigenvectors.
- The columns of $P$ need not be orthogonal. $U$ and $V$ are orthonormal, so they represent rotations (reflections are not mentioned here).
- Both are compositions of three maps: basis change in the domain, independent scaling plus map to the codomain, basis change in the codomain.
- In the SVD, domain and codomain can have different dimensions.
- $U$ and $V$ are generally not inverses of each other. $P$ and $P^{-1}$ are.
- $\Sigma$ is real and non-negative. The eigenvalue diagonal matrix need not be.
- Links: left-singular vectors of $A$ are eigenvectors of $AA^\top$. Right-singular vectors are eigenvectors of $A^\top A$. The nonzero singular values are the square roots of the nonzero eigenvalues of both.
- For symmetric $A\in\mathbb R^{n\times n}$, the two decompositions coincide (spectral theorem 4.15) (p. 127).

**Example 4.14 (movie ratings).** $A\in\mathbb R^{4\times3}$: rows are movies (Star Wars, Blade Runner, Amelie, Delicatessen), columns are Ali, Beatrix, Chandra. Ratings run from 0 to 5 (p. 127):
$$A=\begin{bmatrix}5&4&1\\5&5&0\\0&0&5\\1&0&4\end{bmatrix}$$
Its SVD (Fig. 4.10) has $\sigma_1=9.6438$, $\sigma_2=6.3639$, $\sigma_3=0.7056$ (p. 127). The author lists three assumptions: viewers rate consistently via the same linear mapping, there is no noise, and $u_i$ are read as stereotypical movies and $v_j$ as stereotypical viewers (p. 128).
- $u_1$ has large absolute values for the two science-fiction movies, and $\sigma_1$ is large. $v_1$ is large for Ali and Beatrix. The author takes this to suggest that $v_1$ reflects the notion of a "science fiction lover".
- $u_2$ seems to capture a French art-house theme, and $v_2$ indicates Chandra is close to an idealised lover of such movies (p. 128).
- The author further assumes any viewer's preferences are a linear combination of the $v_j$, and any movie's like-ability a linear combination of the $u_i$ (p. 128).
- A margin note says the two "spaces" are meaningfully spanned only if the data cover enough diversity of viewers and movies (p. 128).

*Intuition note.* In this example the SVD can be read as grouping movies and viewers that go together; the author points to large entries in $u_1$ and $v_1$ together with a large first singular value. This reading holds only under the stated assumptions.

**Conventions** (p. 128–129). The mathematics is the same in all versions:
- The book's (4.64) is the *full SVD*.
- *Reduced SVD*, for $m\ge n$: $A_{m\times n}=U_{m\times n}\Sigma_{n\times n}V^\top_{n\times n}$ (4.89). Here $\Sigma$ is diagonal, as in eigendecomposition.
- The *truncated SVD* is what Section 4.6 uses for approximation.
- For rank $r$: $U$ is $m\times r$, $\Sigma$ is $r\times r$ diagonal with only nonzero diagonal entries, and the third factor is described as "an $r\times n$ matrix" (printed as $V$).
- Restricting the SVD to $m>n$ is unnecessary. For $m<n$, $\Sigma$ has more zero columns than rows and $\sigma_{m+1},\dots,\sigma_n$ are 0.

The SVD is used in least squares and in solving linear systems. Using it can make calculations more robust to rounding errors, and the author says its ability to approximate matrices opens up applications from dimensionality reduction and topic modelling to data compression and clustering (p. 129).

### 4.6 Matrix Approximation
Define a rank-1 matrix from the outer product of the $i$th columns of $U$ and $V$:
$$A_i:=u_iv_i^\top\in\mathbb R^{m\times n}\tag{4.90}$$
Fig. 4.11 shows a grayscale Stonehenge image, $A\in\mathbb R^{1432\times1910}$, and $A_1,\dots,A_5$ with $\sigma_1\approx228{,}052$, $\sigma_2\approx40{,}647$, $\sigma_3\approx26{,}125$, $\sigma_4\approx20{,}232$, $\sigma_5\approx15{,}436$ (pp. 129–130).

A rank-$r$ matrix is a weighted sum of rank-1 matrices:
$$A=\sum_{i=1}^r\sigma_iu_iv_i^\top=\sum_{i=1}^r\sigma_iA_i\tag{4.91}$$
Why: the diagonal $\Sigma$ multiplies only matching pairs $u_iv_i^\top$. Terms $\Sigma_{ij}u_iv_j^\top$ with $i\ne j$ vanish. Terms with $i>r$ vanish because those $\sigma_i=0$ (p. 130).

Summing only up to $k<r$ gives the **rank-$k$ approximation**
$$\widehat A(k):=\sum_{i=1}^k\sigma_iu_iv_i^\top=\sum_{i=1}^k\sigma_iA_i,\quad \mathrm{rk}(\widehat A(k))=k\tag{4.92}$$
Storage in the Stonehenge example: the original needs $1432\cdot1910=2{,}735{,}120$ numbers. Rank 5 needs $5\cdot(1432+1910+1)=16{,}715$ numbers, just above 0.6% (p. 130). Rocks are clearly recognisable at rank 5 (Fig. 4.12, p. 131).

**Definition 4.23 (spectral norm).** For $x\in\mathbb R^n\setminus\{0\}$,
$$\|A\|_2:=\max_x\frac{\|Ax\|_2}{\|x\|_2}\tag{4.93}$$
It is the most that $A$ can lengthen any vector (p. 131).

**Theorem 4.24.** $\|A\|_2=\sigma_1$. The proof is left as an exercise (p. 131).

**Theorem 4.25 (Eckart–Young).** Let $A\in\mathbb R^{m\times n}$ have rank $r$, and let $B\in\mathbb R^{m\times n}$ have rank $k$. For any $k\le r$ with $\widehat A(k)=\sum_{i=1}^k\sigma_iu_iv_i^\top$:
$$\widehat A(k)=\operatorname*{argmin}_{\mathrm{rk}(B)=k}\|A-B\|_2,\tag{4.94}$$
$$\big\|A-\widehat A(k)\big\|_2=\sigma_{k+1}.\tag{4.95}$$
The author reads $\widehat A(k)$ as a projection of $A$ onto rank-at-most-$k$ matrices. Of all such approximations, the SVD one minimises the spectral-norm error (p. 131).

*Why it holds (author's sketch, p. 132).*
1. $A-\widehat A(k)=\sum_{i=k+1}^r\sigma_iu_iv_i^\top$ (4.96). By Thm 4.24 its spectral norm is $\sigma_{k+1}$, which gives (4.95).
2. For (4.94), suppose some $B$ with $\mathrm{rk}(B)\le k$ has $\|A-B\|_2<\|A-\widehat A(k)\|_2$ (4.97).
3. Then $B$ has a null space $Z\subseteq\mathbb R^n$ of dimension at least $n-k$, and $x\in Z\Rightarrow Bx=0$. So $\|Ax\|_2=\|(A-B)x\|_2$ (4.98).
4. A matrix-norm version of Cauchy–Schwarz (3.17) gives $\|Ax\|_2\le\|A-B\|_2\|x\|_2<\sigma_{k+1}\|x\|_2$ (4.99).
5. But on the $(k+1)$-dimensional span of $v_1,\dots,v_{k+1}$, $\|Ax\|_2\ge\sigma_{k+1}\|x\|_2$.
6. The dimensions of the two spaces add to more than $n$, so a nonzero vector lies in both. The author calls this a contradiction of rank–nullity (Thm 2.24).

The author interprets the rank-$k$ approximation as lossy compression. Uses named: image processing, noise filtering, regularisation of ill-posed problems, dimensionality reduction and PCA (Chapter 10) (p. 132).

*Intuition note.* Each term $\sigma_iu_iv_i^\top$ adds one simple "pattern", ordered from strongest to weakest. Dropping the weak ones leaves an error of exactly $\sigma_{k+1}$ in the spectral norm, and no rank-$k$ matrix does better.

**Example 4.15 (movies, continued).** With $u_1=(-0.6710,-0.7197,-0.0939,-0.1515)^\top$ and $v_1^\top=[-0.7367,-0.6515,-0.1811]$,
$$A_1=u_1v_1^\top=\begin{bmatrix}0.4943&0.4372&0.1215\\0.5302&0.4689&0.1303\\0.0692&0.0612&0.0170\\0.1116&0.0987&0.0274\end{bmatrix}\tag{4.100}$$
$A_1$ shows that Ali and Beatrix like the sci-fi films (entries $>0.4$) but fails to capture the ratings of the other movies by Chandra (p. 133). Next, $u_2=(0.0236,0.2054,-0.7705,-0.6030)^\top$ and $v_2^\top=[0.0852,0.1762,-0.9807]$ give
$$A_2=u_2v_2^\top=\begin{bmatrix}0.0020&0.0042&-0.0231\\0.0175&0.0362&-0.2014\\-0.0656&-0.1358&0.7556\\-0.0514&-0.1063&0.5914\end{bmatrix}\tag{4.101}$$
It captures Chandra but not the sci-fi films. Then
$$\widehat A(2)=\sigma_1A_1+\sigma_2A_2=\begin{bmatrix}4.7801&4.2419&1.0244\\5.2252&4.7522&-0.0250\\0.2493&-0.2743&4.9724\\0.7495&0.2756&4.0278\end{bmatrix}\tag{4.102}$$
This is close to the original $A$ (4.103). The author concludes that $A_3$ can be ignored, that the data show no evidence of a third theme/lover category, and that the theme space is two-dimensional (sci-fi and French art house) (p. 133).

### 4.7 Matrix Phylogeny
Fig. 4.13 is a tree of matrix types. Black arrows mean "is a subset of". Blue marks the operations available on each type. A margin note explains that "phylogenetic" refers to relationships among groups (p. 134).
- All real matrices have a pseudo-inverse and an SVD. Square matrices also have a determinant and trace.
- The determinant says whether a square matrix is regular (invertible).
- A square $n\times n$ matrix with $n$ linearly independent eigenvectors is non-defective, so an eigendecomposition exists (Thm 4.12). Repeated eigenvalues may give defective matrices, which cannot be diagonalised.
- Non-singular and non-defective are different. A rotation matrix is invertible but not diagonalisable over the reals, because its eigenvalues need not be real (p. 134).

Within non-defective matrices (p. 135):
- $A$ is *normal* if $A^\top A=AA^\top$. If moreover $A^\top A=AA^\top=I$, it is orthogonal (Def. 3.8). Orthogonal matrices are a subset of the regular matrices, with $A^\top=A^{-1}$.
- Symmetric matrices ($S=S^\top$) are a subset of normal matrices and have only real eigenvalues.
- Positive definite matrices ($x^\top Px>0$ for all $x\ne0$) are a subset of symmetric ones. They have a unique Cholesky decomposition (Thm 4.18), only positive eigenvalues, and are always invertible.
- Diagonal matrices are another subset of symmetric ones. They are closed under multiplication and addition. They form a group only if all diagonal entries are nonzero. The identity is a special diagonal matrix.

### 4.8 Further Reading
(All claims by the author, p. 135–136.)
- Determinants help invert matrices and compute eigenvalues by hand. For almost all but the smallest instances, numerical computation by Gaussian elimination outperforms determinants (the author cites Press et al., 2007). They remain useful in theory, e.g., the sign of the determinant gives the orientation of a basis.
- The Cholesky decomposition is used to simulate random events and to compute the reparametrisation trick (e.g., in variational autoencoders).
- Eigendecomposition underlies *spectral methods* that eigendecompose a positive-definite kernel. Examples are PCA, Fisher discriminant analysis, multidimensional scaling, Isomap, Laplacian eigenmaps, Hessian eigenmaps and spectral clustering. Their core computations are generally underpinned by low-rank approximation techniques.
- The SVD finds similar information but applies to non-square matrices. Uses: finding heterogeneity, compression (storing $(n+m)k$ values instead of $n\times m$), and decorrelating predictors of a design matrix.
- The SVD is a special case of tensor decompositions such as the Tucker and CP decompositions.
- Low-rank approximation saves memory and nonzero multiplications. It is also used for matrices with missing values, lossy compression and dimensionality reduction.

### Exercises (listed, pp. 137–138)
Exercises 4.1–4.7 cover determinants, eigenspaces and diagonalisability. Exercises 4.8–4.12 cover the SVD, rank-1 approximation and two facts used in this unit (Ex. 4.11 on $A^\top A$ and $AA^\top$; Ex. 4.12 on Theorem 4.24). No solutions are printed.

## Toy example (ours, not from the text)
Take $A=\begin{bmatrix}3&0\\4&5\end{bmatrix}$.
1. $A^\top A=\begin{bmatrix}3&4\\0&5\end{bmatrix}\begin{bmatrix}3&0\\4&5\end{bmatrix}=\begin{bmatrix}25&20\\20&25\end{bmatrix}$.
2. Its eigenvalues are $45$ (eigenvector $(1,1)/\sqrt2$) and $5$ (eigenvector $(1,-1)/\sqrt2$). Check: $\begin{bmatrix}25&20\\20&25\end{bmatrix}(1,1)^\top=(45,45)^\top$ and $\begin{bmatrix}25&20\\20&25\end{bmatrix}(1,-1)^\top=(5,-5)^\top$.
3. So $\sigma_1=\sqrt{45}=3\sqrt5\approx6.708$ and $\sigma_2=\sqrt5\approx2.236$, with $v_1=(1,1)/\sqrt2$, $v_2=(1,-1)/\sqrt2$.
4. $Av_1=(3,9)/\sqrt2$, so $u_1=Av_1/\sigma_1=(3,9)/(\sqrt2\cdot3\sqrt5)=(1,3)/\sqrt{10}$. $Av_2=(3,-1)/\sqrt2$, so $u_2=(3,-1)/\sqrt{10}$. Check: $u_1\cdot u_2=(3-3)/10=0$.
5. Rank-1 approximation: $\sigma_1u_1v_1^\top=\frac{3\sqrt5}{\sqrt{10}\sqrt2}\begin{bmatrix}1&1\\3&3\end{bmatrix}=\frac32\begin{bmatrix}1&1\\3&3\end{bmatrix}=\begin{bmatrix}1.5&1.5\\4.5&4.5\end{bmatrix}$.
6. The residual is $A-\widehat A(1)=\begin{bmatrix}1.5&-1.5\\-0.5&0.5\end{bmatrix}=\sigma_2u_2v_2^\top=\frac12\begin{bmatrix}3&-3\\-1&1\end{bmatrix}$. This is rank 1 with spectral norm $\frac12\|(3,-1)\|\,\|(1,-1)\|=\frac12\sqrt{10}\sqrt2=\sqrt5=\sigma_2$, as Eckart–Young predicts.

## Concepts
- [[singular value decomposition (SVD)]] — $A=U\Sigma V^\top$ for any real $m\times n$ matrix, with $U,V$ orthogonal and $\Sigma$ diagonal, non-negative (p. 119)
- [[eckart-young theorem]] — the truncated SVD is the best rank-$k$ approximation in spectral norm, with error $\sigma_{k+1}$ (p. 131)
- [[rank-one matrix / outer product]] — $A_i=u_iv_i^\top$; $A$ is the sum $\sum\sigma_iA_i$ (pp. 129–130)
- [[norm]] — here the spectral norm $\|A\|_2=\max_x\|Ax\|_2/\|x\|_2=\sigma_1$ (p. 131)
- [[orthogonal matrix]] — $U,V$ in the SVD; $A^\top=A^{-1}$ (pp. 119, 135)
- [[eigenvector / eigenvalue]] — right-singular vectors are eigenvectors of $A^\top A$, with $\sigma_i^2=\lambda_i$ (pp. 123–124)
- [[spectral theorem]] — used to diagonalise $A^\top A$ and $AA^\top$ (pp. 123–124)
- [[positive (semi)definite matrix]] — $A^\top A$ is symmetric PSD, so $\lambda_i\ge0$ (p. 123)
- [[change of basis]] — $V^\top$ and $U$ are basis changes in domain and codomain (p. 121)
- [[null space (kernel)]] — $v_i$ with $i>m$ (case $m<n$) span a null-space basis (p. 125)
- [[rank]] — number of nonzero singular values in the construction; $\mathrm{rk}(\widehat A(k))=k$ (pp. 126, 130)
- [[low-rank approximation]] (new) — $\widehat A(k)=\sum_{i\le k}\sigma_iu_iv_i^\top$, "lossy compression" (p. 130, 132)
- [[full vs reduced vs truncated SVD]] (new) — full and reduced SVD are notation variants with unchanged mathematics; truncated SVD is the approximation technique of Sect. 4.6 (pp. 128–129)
- [[singular value equation]] (new) — $Av_i=\sigma_iu_i$ (p. 124)
- [[matrix phylogeny]] (new) — subset tree of matrix types: normal, symmetric, positive definite, orthogonal, etc. (p. 134)
- [[principal component analysis]] — named as an application of low-rank approximation (Chapter 10) (pp. 132, 136)

## Canonical instances
- [[svd-computation-example-4.13]] — hand SVD of a $2\times3$ matrix via $A^\top A$ (p. 125)
- [[movie-ratings-svd]] — $u_i$ as stereotypical movies, $v_j$ as stereotypical viewers; rank-2 approximation is close to the ratings (pp. 127–133)
- [[stonehenge-image-compression]] — rank-5 uses about 0.6% of the numbers (pp. 130–131)
- [[svd-grid-mapping-example-4.12]] — rotate, stretch, embed in $\mathbb R^3$ (pp. 121–122)

## Bridges (candidates)
- [structural-analogy] Rank-$k$ SVD of a user×item rating matrix ↔ social science: a few latent "types" of respondents and items summarising survey or rating data.
- [structural-analogy] $A^\top A$ and its eigenvectors ↔ statistics: the covariance-matrix route to principal components. The unit only says the SVD plays a key role in PCA.
- [same-math] Truncated SVD as best rank-$k$ approximation ↔ data compression and noise filtering: the same factor-and-truncate procedure.
- [metaphor] Domain basis change, scaling, codomain basis change ↔ "rotate, stretch, rotate" as a general picture of any linear map.

## Questions this raises
- What happens to the construction when singular values repeat? The text does not discuss this case.
- How should one pick $k$ in practice? The movie example drops $A_3$ because $\widehat A(2)$ looks similar to $A$. Is there a principled rule?
- What is the best approximation under other norms, such as the Frobenius norm? The unit states optimality only for the spectral norm.
- If the SVD is not computed via $A^\top A$ on a computer, how is it computed (p. 126 gives no method)?

## Exercises worth doing
- Ex. 4.8 (p. 138) — full SVD of a $2\times3$ matrix; repeats the Example 4.13 procedure — difficulty: medium
- Ex. 4.9 (p. 138) — SVD of a square $2\times2$ non-symmetric matrix — difficulty: easy
- Ex. 4.10 (p. 138) — rank-1 approximation of the Ex. 4.8 matrix; practises (4.92) — difficulty: easy
- Ex. 4.11 (p. 138) — $A^\top A$ and $AA^\top$ have the same nonzero eigenvalues (used in the construction on p. 124) — difficulty: medium
- Ex. 4.12 (p. 138) — prove $\max_x\|Ax\|_2/\|x\|_2=\sigma_1$ (Theorem 4.24, used in Eckart–Young) — difficulty: hard
- Ex. 4.5 (p. 137) — diagonalisability versus invertibility, as in Sect. 4.7 — difficulty: easy

## Reading notes
- **Where this part starts and ends:** it starts mid-Section 4.4, at the end of eq. (4.63b) on printed p. 119. It ends with the Exercises on printed p. 138, the last page given (this is part 2 of 2). The first page (119) begins with the last lines of Section 4.4, before the 4.5 heading.
- **Page offset:** printed = pdf − 6.
- **Source:** the footer reads "©2024 M. P. Deisenroth, A. A. Faisal, C. S. Ong. Published by Cambridge University Press (2020)." Even pages carry "Draft (2024-01-15) of 'Mathematics for Machine Learning'".
- **Misprint:** the ordering line on p. 119 reads $\sigma_1\ge\sigma_2\ge\sigma_r\ge0$. The page image shows "σ₁ ⩾ σ₂ ⩾ σ_r ⩾ 0" with the dots missing.
- **Notation, p. 129:** the rank-$r$ SVD variant says "$V$ an $r\times n$ matrix", as printed. I kept it, since it presumably means $V^\top$ (the text does not say).
- **Proof gap:** Theorem 4.24 is stated without proof (left as an exercise). The Eckart–Young argument on p. 132 is a sketch.
- **Text layer:** matrices in the text layer were garbled. I checked Examples 4.12–4.15 against the page images.
