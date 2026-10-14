---
id: deisenroth-2020-mml/ch10-dimensionality
work: deisenroth-2020-mml
unit: "10 Dimensionality Reduction with Principal Component Analysis"
pages: 317–347
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 4
pipeline_version: 0.1
---
# Dimensionality Reduction with Principal Component Analysis

## L0 — One line
PCA compresses data by projecting it onto the eigenvectors of the data covariance matrix with the largest eigenvalues, and the variance lost (the average squared reconstruction error) equals the sum of the discarded eigenvalues.

## L1 — The gist (≤ 120 words)
How can we replace high-dimensional data by a few coordinates and lose as little as possible? The chapter derives principal component analysis (PCA) in two ways: maximizing the variance of the projected data, and minimizing the average squared reconstruction error. Both give the same answer. Project onto the eigenvectors of the data covariance matrix that belong to the M largest eigenvalues. The average squared reconstruction error is the sum of the discarded eigenvalues. The chapter also shows how to compute this with the singular value decomposition (SVD), a trick for N ≪ D (far fewer data points than dimensions), the practical steps, and a probabilistic latent-variable version (PPCA).

**Prerequisites:** orthonormal basis and orthogonal projection; eigenvalues, eigenvectors, spectral theorem; SVD and Eckart–Young; covariance and variance; Lagrange multipliers; trace; Gaussian conditioning (for §10.7).

## L2 — Key ideas (5–10 bullets)
- PCA assumes centered data, an orthonormal matrix $B\in\mathbb R^{D\times M}$, a code $z=B^\top x$ and a reconstruction $\tilde x=BB^\top x$; $B^\top$ is the encoder and $B$ the decoder (pp. 318–319).
- Maximum-variance view: the unit vector maximizing the projected variance $b^\top S b$ is an eigenvector of $S$ (the one with the largest eigenvalue), and the variance equals its eigenvalue. The $m$th component is found by removing the first $m-1$ components from the data (pp. 321–324).
- The variance captured by $M$ components is $V_M=\sum_{m\le M}\lambda_m$. The variance lost is $J_M=\sum_{j>M}\lambda_j$ (p. 325).
- Projection view: for a given orthonormal basis, the best coordinates are those of the orthogonal projection, $z_{in}=b_i^\top x_n$. The reconstruction error then becomes $\sum_{j>M}b_j^\top S b_j$, so the two views give the same solution (pp. 328–332).
- Computing PCA: eigendecompose $S$, or take the SVD of $X$ with $\lambda_d=\sigma_d^2/N$. The truncated SVD is the best rank-$M$ approximation (Eckart–Young). Iterative methods such as power iteration (repeatedly multiply by $S$ and normalize) are cheaper when only a few eigenvectors are needed (pp. 333–335).
- If $N\ll D$, work with the $N\times N$ matrix $\frac1N X^\top X$ and map its eigenvectors back by $X c_m$ (pp. 335–336).
- In practice: subtract the mean, divide by the standard deviation, eigendecompose, project; undo the standardization to return to the original space (pp. 336–338).
- Probabilistic PCA (PPCA) models $x=Bz+\mu+\epsilon$ with a Gaussian prior on $z$. It gives a likelihood, a Gaussian posterior over $z$, and the ML solution. PCA is the noise-free limit (pp. 339–345).

## L3 — Walkthrough

### Introduction (pp. 317–318)
- High-dimensional data (e.g. images) is hard to analyze, interpret, visualize and store. It is often overcomplete (many dimensions are redundant) and correlated, so it has an intrinsic lower-dimensional structure (p. 317).
- Dimensionality reduction exploits this and works like compression (jpeg, mp3) (p. 317).
- PCA is an algorithm for *linear* dimensionality reduction, proposed by Pearson (1901) and Hotelling (1933). In signal processing it is also called the Karhunen–Loève transform (pp. 317–318).
- Figure 10.1: 2-D data that barely vary along $x_2$ can be stored by $x_1$ alone with nearly no loss. The data then lie in a one-dimensional subspace of $\mathbb R^2$ (p. 318).

### 10.1 Problem Setting (pp. 318–320)
- **Setting.** An i.i.d. dataset $\mathcal X=\{x_1,\dots,x_N\}$, $x_n\in\mathbb R^D$, has mean $\mathbf 0$ and data covariance matrix (p. 318)
$$S=\frac1N\sum_{n=1}^N x_nx_n^\top .\tag{10.1}$$
- **Code.** Each $x_n$ has a compressed representation (code)
$$z_n=B^\top x_n\in\mathbb R^M,\tag{10.2}$$
$$B:=[b_1,\dots,b_M]\in\mathbb R^{D\times M}.\tag{10.3}$$
- The columns of $B$ are orthonormal: $b_i^\top b_j=0$ for $i\neq j$ and $b_i^\top b_i=1$ (p. 318).
- We seek an $M$-dimensional subspace $U\subseteq\mathbb R^D$, $\dim U=M<D$. The projected points are $\tilde x_n\in U$ and their coordinates with respect to $b_1,\dots,b_M$ are $z_n$. The aim is to make $\tilde x_n$ as similar as possible to $x_n$ and minimize the compression loss (p. 318).
- **Example 10.1.** In $\mathbb R^2$ with canonical basis, $[5,3]^\top=5e_1+3e_2$ (10.4). Vectors of the form $\tilde x=[0,z]^\top$ (10.5) are always $0e_1+ze_2$, so storing $z$ suffices. They form a subspace $U=\mathrm{span}[e_2]$ with $\dim U=1$ (p. 319).
- **Encoder/decoder.** Figure 10.2: $x\in\mathbb R^D\to z\in\mathbb R^M\to\tilde x\in\mathbb R^D$. The code $z$ is a bottleneck controlling how much information flows from $x$ to $\tilde x$. We use $z=B^\top x$ and $\tilde x=Bz$. $B^\top$ acts as encoder and $B$ as decoder (p. 319).
- Section 10.2 looks for representations retaining maximal information. Section 10.3 gives an alternative derivation by minimizing $\|x_n-\tilde x_n\|^2$ (p. 319).
- Running example: MNIST, 60,000 handwritten digits, each $28\times28=784$ pixels, i.e. $x\in\mathbb R^{784}$ (p. 320).

### 10.2 Maximum Variance Perspective (pp. 320–325)
- **Idea.** Information is interpreted as how "space filling" the data is, i.e. its spread. Variance measures spread, so PCA maximizes the variance of the low-dimensional code. The author states this is equivalent to retaining the most information (Hotelling, 1933) (p. 320).
- **Remark (centered data).** With $\mu$ the data mean, $\mathbb V_z[z]=\mathbb V_x[B^\top(x-\mu)]=\mathbb V_x[B^\top x-B^\top\mu]=\mathbb V_x[B^\top x]$ (10.6). The code's variance does not depend on the mean, so centering loses no generality. The code's mean is then $\mathbb E[z]=B^\top\mathbb E[x]=\mathbf 0$ (p. 320).

#### 10.2.1 Direction with Maximal Variance (pp. 321–322)
- The author maximizes variance sequentially. First find $b_1\in\mathbb R^D$ maximizing the variance of the first coordinate $z_1$ (p. 321):
$$V_1:=\mathbb V[z_1]=\frac1N\sum_{n=1}^N z_{1n}^2,\tag{10.7}$$
$$z_{1n}=b_1^\top x_n,\tag{10.8}$$
which is the coordinate of the orthogonal projection of $x_n$ onto $\mathrm{span}[b_1]$.
- Substituting (shape check: $b_1\in\mathbb R^D$, $S\in\mathbb R^{D\times D}$, $V_1$ scalar):
$$V_1=\frac1N\sum_n (b_1^\top x_n)^2=\frac1N\sum_n b_1^\top x_nx_n^\top b_1\tag{10.9a}$$
$$=b_1^\top\Big(\frac1N\sum_n x_nx_n^\top\Big)b_1=b_1^\top S b_1 .\tag{10.9b}$$
- Making $b_1$ longer increases $V_1$ (twice as long can give four times larger variance). So we restrict to $\|b_1\|^2=1$ (p. 321):
$$\max_{b_1} b_1^\top S b_1\quad\text{subject to }\|b_1\|^2=1.\tag{10.10}$$
- Lagrangian and its partial derivatives (p. 322):
$$\mathfrak L(b_1,\lambda)=b_1^\top Sb_1+\lambda_1(1-b_1^\top b_1)\tag{10.11}$$
$$\frac{\partial\mathfrak L}{\partial b_1}=2b_1^\top S-2\lambda_1b_1^\top,\qquad\frac{\partial\mathfrak L}{\partial\lambda_1}=1-b_1^\top b_1.\tag{10.12}$$
- Setting both to $\mathbf 0$:
$$Sb_1=\lambda_1b_1,\tag{10.13}$$
$$b_1^\top b_1=1.\tag{10.14}$$
- So $b_1$ is an eigenvector of $S$ and the multiplier $\lambda_1$ is the eigenvalue. Then
$$V_1=b_1^\top Sb_1=\lambda_1b_1^\top b_1=\lambda_1.\tag{10.15}$$
- The variance of the projected data equals the eigenvalue of $b_1$. To maximize it, choose the eigenvector with the largest eigenvalue; this is the **first principal component** (p. 322).
- Margin note: $\sqrt{\lambda_1}$ is called the loading of $b_1$ and is the standard deviation accounted for by $\mathrm{span}[b_1]$ (p. 322).
- Mapped back to data space: $\tilde x_n=b_1z_{1n}=b_1b_1^\top x_n\in\mathbb R^D$ (10.16). It needs a single coordinate $z_{1n}$ although it is $D$-dimensional (p. 322).

#### 10.2.2 $M$-dimensional Subspace with Maximal Variance (pp. 322–325)
- Assume the first $m-1$ components are the eigenvectors of $S$ for the $m-1$ largest eigenvalues. By the spectral theorem (Thm 4.15), since $S$ is symmetric, they form an orthonormal eigenbasis of an $(m-1)$-dimensional subspace (pp. 322–323).
- The $m$th component is found by subtracting the first $m-1$ components from the data (p. 323):
$$\hat X:=X-\sum_{i=1}^{m-1}b_ib_i^\top X=X-B_{m-1}X,\tag{10.17}$$
with $X=[x_1,\dots,x_N]\in\mathbb R^{D\times N}$ and $B_{m-1}:=\sum_{i<m}b_ib_i^\top$, a projection matrix onto $\mathrm{span}[b_1,\dots,b_{m-1}]$.
- **Notation remark.** Data points are the *columns* of $X$, so $X$ is $D\times N$ (not the conventional $N\times D$). This avoids transposes in the algebra (p. 323).
- The $m$th component maximizes
$$V_m=\mathbb V[z_m]=\frac1N\sum_n z_{mn}^2=\frac1N\sum_n(b_m^\top\hat x_n)^2=b_m^\top\hat Sb_m\tag{10.18}$$
subject to $\|b_m\|^2=1$, where $\hat S$ is the covariance matrix of $\hat X$. As before, the optimum is the eigenvector of $\hat S$ with the largest eigenvalue (p. 323).
- **Claim:** every eigenvector of $S$ is an eigenvector of $\hat S$. Take $Sb_i=\lambda_ib_i$ (p. 323):
$$\hat Sb_i=\tfrac1N\hat X\hat X^\top b_i=\tfrac1N(X-B_{m-1}X)(X-B_{m-1}X)^\top b_i\tag{10.19a}$$
$$=(S-SB_{m-1}-B_{m-1}S+B_{m-1}SB_{m-1})b_i.\tag{10.19b}$$
- Two cases (p. 324):
$$B_{m-1}b_i=b_i\ \ (i<m),\qquad B_{m-1}b_i=\mathbf 0\ \ (i\ge m).\tag{10.20}$$
 For $i\ge m$, $b_i$ is orthogonal to the first $m-1$ components. For $i<m$, $b_i$ lies in the principal subspace and $b_1,\dots,b_{m-1}$ are an ONB of it.
- **Case $i\ge m$.** $\hat Sb_i=(S-B_{m-1}S)b_i=Sb_i=\lambda_ib_i$ (the author's line; (added step): $B_{m-1}Sb_i=\lambda_iB_{m-1}b_i=\mathbf 0$). Hence
$$\hat Sb_m=Sb_m=\lambda_mb_m.\tag{10.21}$$
 So $b_m$ is an eigenvector of both. $\lambda_m$ is the largest eigenvalue of $\hat S$ and the $m$th largest of $S$ (p. 324).
- **Case $i<m$.** (added step: $SB_{m-1}b_i=\lambda_ib_i$, $B_{m-1}Sb_i=\lambda_ib_i$, $B_{m-1}SB_{m-1}b_i=\lambda_ib_i$, so the four terms give $\lambda_i-\lambda_i-\lambda_i+\lambda_i$.)
$$\hat Sb_i=(S-SB_{m-1}-B_{m-1}S+B_{m-1}SB_{m-1})b_i=\mathbf 0=0\,b_i.\tag{10.22}$$
 So $b_1,\dots,b_{m-1}$ are eigenvectors of $\hat S$ with eigenvalue 0 and span its null space (p. 324).
- Hence every eigenvector of $S$ is an eigenvector of $\hat S$. If it lies in the $(m-1)$-dimensional principal subspace, its eigenvalue for $\hat S$ is 0 (p. 324).
- Variance on the $m$th component:
$$V_m=b_m^\top Sb_m\overset{(10.21)}{=}\lambda_mb_m^\top b_m=\lambda_m.\tag{10.23}$$
 The variance of the data projected onto an $M$-dimensional subspace equals the sum of the eigenvalues of the corresponding eigenvectors (p. 324).
- **Intuition note.** Each new direction is the "biggest leftover spread" after the earlier directions are removed. Because the earlier directions are eigenvectors, removing them leaves all other eigenvectors untouched. So the whole procedure just sorts the eigenvectors of $S$ by eigenvalue.
- **Example 10.2 (eigenvalues of MNIST "8").** For all training digits "8", the 200 largest eigenvalues of the covariance matrix are plotted (Fig. 10.5a). Only a few differ significantly from 0. So a few principal components capture most of the variance (Fig. 10.5b) (pp. 324–325).
- **Summary.** Choose the columns of $B$ as the $M$ eigenvectors of $S$ with the largest eigenvalues (p. 325). The maximum captured variance and the variance lost are
$$V_M=\sum_{m=1}^M\lambda_m,\tag{10.24}$$
$$J_M:=\sum_{j=M+1}^D\lambda_j=V_D-V_M.\tag{10.25}$$
 Relative variance captured is $V_M/V_D$; relative variance lost is $1-V_M/V_D$ (p. 325).

### 10.3 Projection Perspective (pp. 325–332)
PCA is now derived as the algorithm that directly minimizes the average reconstruction error. This views PCA as an optimal linear auto-encoder (p. 325). Figure 10.6 shows the difference vectors between original and projected data (p. 325).

#### 10.3.1 Setting and Objective (pp. 326–327)
- Take an ordered ONB $(b_1,\dots,b_D)$ of $\mathbb R^D$. Any $x$ can be written (p. 326)
$$x=\sum_{d=1}^D\zeta_db_d=\sum_{m=1}^M\zeta_mb_m+\sum_{j=M+1}^D\zeta_jb_j.\tag{10.26}$$
- We want $\tilde x\in U$, $\dim U=M$, with (p. 326)
$$\tilde x=\sum_{m=1}^Mz_mb_m\in U\subseteq\mathbb R^D\tag{10.27}$$
as close to $x$ as possible in Euclidean distance. At this point the author says we need to assume the coordinates $z_m$ of $\tilde x$ and $\zeta_m$ of $x$ are not identical (p. 326). It is shown on p. 329 that they must be identical.
- The data are centered; the author says the solution is the same without this assumption, only the notation is more cluttered (pp. 326–327).
- The subspace $U$ is called the **principal subspace**. The projections are
$$\tilde x_n:=\sum_{m=1}^Mz_{mn}b_m=Bz_n\in\mathbb R^D,\quad z_n\in\mathbb R^M.\tag{10.28}$$
- Objective: the average squared Euclidean distance (reconstruction error, Pearson 1901) (p. 327)
$$J_M:=\frac1N\sum_{n=1}^N\|x_n-\tilde x_n\|^2.\tag{10.29}$$
- Two steps: optimize the coordinates $z_n$ for a given ONB, then find the best ONB (p. 327).

#### 10.3.2 Finding Optimal Coordinates (pp. 327–329)
- Chain rule (p. 327): $\frac{\partial J_M}{\partial z_{in}}=\frac{\partial J_M}{\partial\tilde x_n}\frac{\partial\tilde x_n}{\partial z_{in}}$ (10.30a), with $\frac{\partial J_M}{\partial\tilde x_n}=-\frac2N(x_n-\tilde x_n)^\top\in\mathbb R^{1\times D}$ (10.30b).
- (p. 328) $\frac{\partial\tilde x_n}{\partial z_{in}}=\frac{\partial}{\partial z_{in}}\big(\sum_mz_{mn}b_m\big)=b_i$ (10.30c). Therefore
$$\frac{\partial J_M}{\partial z_{in}}=-\frac2N(x_n-\tilde x_n)^\top b_i=-\frac2N\Big(x_n-\sum_mz_{mn}b_m\Big)^\top b_i\tag{10.31a}$$
$$\overset{\text{ONB}}{=}-\frac2N(x_n^\top b_i-z_{in}b_i^\top b_i)=-\frac2N(x_n^\top b_i-z_{in}),\tag{10.31b}$$
using $b_i^\top b_i=1$.
- Setting this to 0:
$$z_{in}=x_n^\top b_i=b_i^\top x_n,\quad i=1,\dots,M,\ n=1,\dots,N.\tag{10.32}$$
- Consequences stated by the author (pp. 328–329): the optimal linear projection of $x_n$ is an orthogonal projection. The optimal coordinates are those of the orthogonal projection onto the principal subspace. An orthogonal projection is the best linear mapping for objective (10.29). The coordinates $\zeta_m$ of $x$ and $z_m$ of $\tilde x$ must be identical for $m=1,\dots,M$, because $U^\perp=\mathrm{span}[b_{M+1},\dots,b_D]$ is the orthogonal complement of $U$.
- **Remark (recap of Section 3.8).** For one ONB vector, $\tilde x=b_j(b_j^\top b_j)^{-1}b_j^\top x=b_jb_j^\top x$ (10.33), with coordinate $z_j=b_j^\top x$. For $M$ vectors,
$$\tilde x=B(\underbrace{B^\top B}_{=I})^{-1}B^\top x=BB^\top x,\tag{10.34}$$
with coordinates $z=B^\top x$. Only $M$ coordinates are needed; the other $D-M$ coordinates (for $b_{M+1},\dots,b_D$) are always 0 (p. 329).
- **Intuition note.** Given the directions, the closest point of the subspace to $x$ is its foot of the perpendicular. That foot has coordinates $b_i^\top x$. Any other choice of coordinates only adds distance.

#### 10.3.3 Finding the Basis of the Principal Subspace (pp. 329–332)
- Rewrite $\tilde x_n$ (pp. 329–330):
$$\tilde x_n=\sum_mz_{mn}b_m\overset{(10.32)}=\sum_m(x_n^\top b_m)b_m=\Big(\sum_{m=1}^Mb_mb_m^\top\Big)x_n.\tag{10.35, 10.36}$$
- Since $x_n$ is a combination of all basis vectors (p. 330):
$$x_n=\sum_{d=1}^D z_{dn}b_d\overset{(10.32)}=\Big(\sum_{d=1}^Db_db_d^\top\Big)x_n\tag{10.37a}$$
$$=\Big(\sum_{m=1}^Mb_mb_m^\top\Big)x_n+\Big(\sum_{j=M+1}^Db_jb_j^\top\Big)x_n.\tag{10.37b}$$
- The displacement vector is therefore
$$x_n-\tilde x_n=\Big(\sum_{j=M+1}^Db_jb_j^\top\Big)x_n=\sum_{j=M+1}^D(x_n^\top b_j)b_j.\tag{10.38a, b}$$
 It is the projection of $x_n$ onto the orthogonal complement of the principal subspace and lies in that complement (Fig. 10.9) (p. 330).
- **Remark (low-rank approximation).** $BB^\top=\sum_{m\le M}b_mb_m^\top$ (10.39) is a sum of rank-one matrices, symmetric, of rank $M$. So (p. 331)
$$\frac1N\sum_n\|x_n-\tilde x_n\|^2=\frac1N\sum_n\|x_n-BB^\top x_n\|^2=\frac1N\sum_n\|(I-BB^\top)x_n\|^2.\tag{10.40a, b}$$
 Finding the best basis equals finding the best rank-$M$ approximation $BB^\top$ of the identity $I$ (Section 4.6).
- Loss reformulated (p. 331):
$$J_M\overset{(10.38b)}=\frac1N\sum_n\Big\|\sum_{j=M+1}^D(b_j^\top x_n)b_j\Big\|^2.\tag{10.41}$$
 Using that the $b_j$ are an ONB and $b_j^\top x_n=x_n^\top b_j$:
$$J_M=\frac1N\sum_n\sum_{j>M}(b_j^\top x_n)^2=\frac1N\sum_n\sum_{j>M}b_j^\top x_nx_n^\top b_j.\tag{10.42a, b}$$
 Swapping the sums:
$$J_M=\sum_{j=M+1}^Db_j^\top\underbrace{\Big(\frac1N\sum_nx_nx_n^\top\Big)}_{=:S}b_j=\sum_{j>M}b_j^\top Sb_j\tag{10.43a}$$
$$=\sum_{j>M}\mathrm{tr}(b_j^\top Sb_j)=\sum_{j>M}\mathrm{tr}(Sb_jb_j^\top)=\mathrm{tr}\Big(\Big(\sum_{j>M}b_jb_j^\top\Big)S\Big).\tag{10.43b}$$
 This uses that the trace is linear and invariant under cyclic permutations. The bracketed projection matrix has rank $D-M$ (p. 331).
- **Skip path:** carry forward $J_M=\sum_{j>M}b_j^\top Sb_j=\mathrm{tr}(P_{U^\perp}S)$ and its value $\sum_{j>M}\lambda_j$.
- Minimizing the average squared reconstruction error equals minimizing the variance of the data projected onto the ignored subspace $U^\perp$. Equivalently, it maximizes the retained variance, which links to Section 10.2. The solution is therefore the same, and the author omits the repeated derivation (p. 332).
- Result:
$$J_M=\sum_{j=M+1}^D\lambda_j,\tag{10.44}$$
 so we discard the $D-M$ smallest eigenvalues. Their eigenvectors span $U^\perp$. The principal subspace is spanned by the eigenvectors of the $M$ largest eigenvalues (p. 332).
- **Intuition note.** "Keep as much spread as possible" and "lose as little squared distance as possible" are the same goal. The total variance is fixed, so what you do not keep is exactly what you lose.
- **Example 10.3 (MNIST embedding).** MNIST "0" and "1" projected onto the first two principal components show a relatively clear separation. The variation within the "0"s is significantly greater than within the "1"s (Fig. 10.10) (pp. 332–333).

### 10.4 Eigenvector Computation and Low-Rank Approximations (pp. 333–335)
- **Setup.** $S=\frac1N\sum_nx_nx_n^\top=\frac1NXX^\top$ (10.45), $X=[x_1,\dots,x_N]\in\mathbb R^{D\times N}$ (10.46) (p. 333).
- Two ways to get eigenpairs of $S$: eigendecomposition of $S$, or the SVD of $X$, since $S$ factorizes into $XX^\top$ up to the factor $1/N$ (p. 333).
- SVD (with shapes): $X=U\Sigma V^\top$ with $U\in\mathbb R^{D\times D}$, $\Sigma\in\mathbb R^{D\times N}$, $V^\top\in\mathbb R^{N\times N}$ (10.47); $U,V$ orthogonal and $\Sigma$'s only nonzero entries are the singular values $\sigma_{ii}\ge0$. Then
$$S=\frac1NXX^\top=\frac1NU\Sigma\underbrace{V^\top V}_{=I_N}\Sigma^\top U^\top=\frac1NU\Sigma\Sigma^\top U^\top.\tag{10.48}$$
- The columns of $U$ are eigenvectors of $XX^\top$ (hence of $S$), and
$$\lambda_d=\frac{\sigma_d^2}{N}.\tag{10.49}$$
 This links the maximum-variance view with the SVD (p. 333).

#### 10.4.1 PCA Using Low-Rank Matrix Approximations (p. 334)
- PCA takes the columns of $U$ for the $M$ largest eigenvalues as the projection matrix $B$ (p. 334).
- Best rank-$M$ approximation of $X$ in spectral norm (4.93):
$$\tilde X_M:=\operatorname*{argmin}_{\mathrm{rk}(A)\le M}\|X-A\|_2\in\mathbb R^{D\times N}.\tag{10.50}$$
 By the Eckart–Young theorem (Thm 4.25) it is the SVD truncated at the top-$M$ singular values:
$$\tilde X_M=\underbrace{U_M}_{D\times M}\underbrace{\Sigma_M}_{M\times M}\underbrace{V_M^\top}_{M\times N}\in\mathbb R^{D\times N},\tag{10.51}$$
 with $U_M=[u_1,\dots,u_M]$, $V_M=[v_1,\dots,v_M]$ and $\Sigma_M$ diagonal with the $M$ largest singular values.

#### 10.4.2 Practical Aspects (pp. 334–335)
- Eigenvalues as roots of the characteristic polynomial cannot be found in closed form for matrices larger than $4\times4$. The Abel–Ruffini theorem says there is no algebraic solution for polynomials of degree 5 or more. So iterative methods are used (e.g. `np.linalg.eigh`, `np.linalg.svd`) (p. 334).
- If only a few leading eigenvectors are needed, iterative methods that optimize them directly are more efficient than a full decomposition (p. 334).
- **Power iteration.** Choose a random $x_0$ not in the null space of $S$ and iterate
$$x_{k+1}=\frac{Sx_k}{\|Sx_k\|},\quad k=0,1,\dots\tag{10.52}$$
 so that $\|x_k\|=1$. The sequence converges to the eigenvector of the largest eigenvalue. If $S$ is invertible, $x_0\ne0$ is enough. The original Google PageRank algorithm uses such an algorithm (p. 335).
- **Intuition note.** The SVD of the data matrix and the eigendecomposition of the covariance matrix hold the same information. Squared singular values divided by $N$ are the variances along the principal directions.

### 10.5 PCA in High Dimensions (pp. 335–336)
- Eigendecomposition of the $D\times D$ matrix $S$ scales cubically in $D$. For $100\times100$ images, that is a $10{,}000\times10{,}000$ matrix. The remedy is for $N\ll D$ (p. 335).
- With centered data, $S=\frac1NXX^\top\in\mathbb R^{D\times D}$ (10.53). The author states that if there are no duplicate data points, $S$ has rank $N$, so $D-N+1$ eigenvalues are 0 (p. 335).
- Start from $Sb_m=\lambda_mb_m$ (10.54), i.e. $\frac1NXX^\top b_m=\lambda_mb_m$ (10.55). Multiply from the left by $X^\top\in\mathbb R^{N\times D}$:
$$\frac1N\underbrace{X^\top X}_{N\times N}\underbrace{X^\top b_m}_{=:c_m}=\lambda_mX^\top b_m\iff\frac1NX^\top Xc_m=\lambda_mc_m.\tag{10.56}$$
- So $\lambda_m$ stays an eigenvalue, now of the $N\times N$ matrix $\frac1NX^\top X$ with eigenvector $c_m=X^\top b_m\in\mathbb R^N$. This confirms that nonzero eigenvalues of $XX^\top$ and $X^\top X$ coincide (Section 4.5.3). Without duplicate points the author says this matrix has rank $N$ and is invertible (p. 336).
- Recover the eigenvectors of $S$: left-multiply by $X$,
$$\frac1N XX^\top\,Xc_m=\lambda_m Xc_m,\tag{10.57}$$
 so $Xc_m$ is an eigenvector of $S$. It must be normalized to norm 1 before use in Section 10.6 (p. 336).

### 10.6 Key Steps of PCA in Practice (pp. 336–338)
Running example: 2-D data projected to 1-D (Fig. 10.11) (p. 336).
1. **Mean subtraction:** subtract the mean $\mu$ from each point. This is not strictly necessary but reduces the risk of numerical problems (p. 336).
2. **Standardization:** divide each dimension $d$ by its standard deviation $\sigma_d$. The data become unit-free with variance 1 along each axis (p. 336).
3. **Eigendecomposition of the covariance matrix:** compute $S$, its eigenvalues and eigenvectors. By the spectral theorem we get an ONB of eigenvectors. The longest eigenvector spans the principal subspace $U$ (Fig. 10.11d) (pp. 336–337).
4. **Projection:** standardize a new point $x_*$ with the *training* mean and standard deviation (p. 337):
$$x_*^{(d)}\leftarrow\frac{x_*^{(d)}-\mu_d}{\sigma_d},\quad d=1,\dots,D.\tag{10.58}$$
 Then
$$\tilde x_*=BB^\top x_*,\tag{10.59}$$
$$z_*=B^\top x_*.\tag{10.60}$$
 PCA returns the coordinates (10.60), not the projections (p. 337).
- To return to the original data space, undo the standardization (p. 338):
$$\tilde x_*^{(d)}\leftarrow\tilde x_*^{(d)}\sigma_d+\mu_d,\quad d=1,\dots,D.\tag{10.61}$$
- **Example 10.4 (MNIST reconstruction).** PCA was applied to 5,389 training images of the digit "8". The learned projection reconstructed test images (Fig. 10.12). With 1 PC the reconstruction is "halfway decent" but blurry and generic. With 10, 100, 500 PCs it becomes sharper. With 500 PCs it is near-perfect. With 784 PCs it is exact (pp. 338–339).
- Average squared reconstruction error as a function of $M$ (Fig. 10.13):
$$\frac1N\sum_n\|x_n-\tilde x_n\|^2=\sum_{i=M+1}^D\lambda_i.\tag{10.62}$$
 The importance of components drops off rapidly. With about 550 PCs the training data are essentially fully reconstructed; some boundary pixels never vary (they are always black) (p. 339).

### 10.7 Latent Variable Perspective (pp. 339–343)
- The earlier derivations use no probabilistic model. A probabilistic model would give a likelihood, handling of noisy observations, Bayesian model comparison, a generative model, handling of values missing at random, a notion of novelty of a new point, extensions such as mixtures, and a fully Bayesian treatment. The PCA solution would be a special case (pp. 339–340).
- Tipping and Bishop (1999) proposed **probabilistic PCA (PPCA)**. The ordinary PCA solution is the special case of maximum likelihood in a noise-free setting (p. 340).

#### 10.7.1 Generative Process and Probabilistic Model (pp. 340–341)
- Latent $z\in\mathbb R^M$ with prior $p(z)=\mathcal N(0,I)$, and
$$x=Bz+\mu+\epsilon\in\mathbb R^D,\tag{10.63}$$
 with $\epsilon\sim\mathcal N(0,\sigma^2I)$, $B\in\mathbb R^{D\times M}$, $\mu\in\mathbb R^D$ (p. 340). Hence
$$p(x\mid z,B,\mu,\sigma^2)=\mathcal N(x\mid Bz+\mu,\sigma^2I).\tag{10.64}$$
- Generative process:
$$z_n\sim\mathcal N(z\mid0,I)\tag{10.65}$$
$$x_n\mid z_n\sim\mathcal N(x\mid Bz_n+\mu,\sigma^2I)\tag{10.66}$$
 This is ancestral sampling: first sample $z_n$, then $x_n$ given $z_n$ (p. 340).
- Joint: $p(x,z\mid B,\mu,\sigma^2)=p(x\mid z,B,\mu,\sigma^2)p(z)$ (10.67), giving the graphical model of Fig. 10.14 (p. 340).
- **Remark.** The arrow runs from $z$ to $x$: a lower-dimensional latent cause for high-dimensional observations. To learn about $z$ from $x$, Bayesian inference "inverts" the arrow (p. 341).
- **Example 10.5.** Using the 2-D PCA latent coordinates of MNIST "8", any query $z_*$ gives an image $\tilde x_*=Bz_*$ resembling an "8". Shape, rotation and size vary with $z_*$. Far from the training data, more artifacts appear. The generated images have intrinsic dimensionality two (p. 341).

#### 10.7.2 Likelihood and Joint Distribution (p. 342)
- The likelihood integrates out $z$:
$$p(x\mid B,\mu,\sigma^2)=\int p(x\mid z,B,\mu,\sigma^2)p(z)\,dz=\int\mathcal N(x\mid Bz+\mu,\sigma^2I)\mathcal N(z\mid0,I)\,dz.\tag{10.68a, b}$$
- This is Gaussian (Section 6.5) with
$$\mathbb E_x[x]=\mathbb E_z[Bz+\mu]+\mathbb E_\epsilon[\epsilon]=\mu,\tag{10.69}$$
$$\mathbb V[x]=\mathbb V_z[Bz+\mu]+\mathbb V_\epsilon[\epsilon]=\mathbb V_z[Bz]+\sigma^2I=B\mathbb V_z[z]B^\top+\sigma^2I=BB^\top+\sigma^2I.\tag{10.70a, b}$$
- This likelihood can be used for maximum likelihood or MAP estimation. The conditional (10.64) cannot be used, because it still depends on the latent variables (p. 342).
- Cross-covariance $\mathrm{Cov}[x,z]=\mathrm{Cov}_z[Bz+\mu]=B\,\mathrm{Cov}_z[z,z]=B$ (10.71). So the joint is
$$p(x,z\mid B,\mu,\sigma^2)=\mathcal N\!\left(\begin{bmatrix}x\\z\end{bmatrix}\Big|\begin{bmatrix}\mu\\0\end{bmatrix},\begin{bmatrix}BB^\top+\sigma^2I&B\\B^\top&I\end{bmatrix}\right),\tag{10.72}$$
 with mean vector of length $D+M$ and covariance matrix of size $(D+M)\times(D+M)$.

#### 10.7.3 Posterior Distribution (p. 343)
- Gaussian conditioning (Section 6.5.1) gives
$$p(z\mid x)=\mathcal N(z\mid m,C),\tag{10.73}$$
$$m=B^\top(BB^\top+\sigma^2I)^{-1}(x-\mu),\tag{10.74}$$
$$C=I-B^\top(BB^\top+\sigma^2I)^{-1}B.\tag{10.75}$$
- The posterior covariance does not depend on the observed $x$. A small determinant of $C$ means the embedding $z_*$ is fairly certain. A posterior with much variance may indicate an outlier (p. 343).
- To explore the posterior: (1) sample $z_*\sim p(z\mid x_*)$; (2) sample $\tilde x_*\sim p(x\mid z_*,B,\mu,\sigma^2)$. Repeating this hypothesizes data plausible under the posterior (p. 343).
- **Intuition note.** PPCA says: draw a few hidden numbers $z$, mix them linearly with $B$, add equal noise in every direction. The observed covariance is then $BB^\top+\sigma^2I$.

### 10.8 Further Reading (pp. 343–347)
Only what the text states; most items are pointers to other work.
- **Recap.** $B$'s columns are eigenvectors of $S$ for the largest eigenvalues; $\tilde x=BB^\top x$ is a projection (p. 343).
- **Auto-encoder view.** With linear maps $z_n=B^\top x_n$ and $\tilde x_n=Bz_n$ (Fig. 10.16), the average squared error is
$$\frac1N\sum_n\|x_n-\tilde x_n\|^2=\frac1N\sum_n\|x_n-BB^\top x_n\|^2.\tag{10.76}$$
 This is the same objective as (10.29), so minimizing the squared auto-encoding loss gives the PCA solution. Replacing the linear maps by deep neural networks gives a deep auto-encoder. There the encoder is also called a recognition or inference network and the decoder a generator (p. 344).
- **Information theory.** Reconstruction is lossy. Maximizing the mutual information between data and code would, according to the author, give the same PCA solution as Section 10.3 (p. 344).
- **ML estimates in PPCA** (Tipping and Bishop, 1999, as reported by the author; the author notes a different notation here) (pp. 344–345):
$$\mu_{ML}=\frac1N\sum_nx_n,\tag{10.77}$$
$$B_{ML}=T(\Lambda-\sigma^2I)^{1/2}R,\tag{10.78}$$
$$\sigma^2_{ML}=\frac1{D-M}\sum_{j=M+1}^D\lambda_j.\tag{10.79}$$
 Here $T\in\mathbb R^{D\times M}$ holds $M$ eigenvectors of the data covariance matrix. $\Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_M)$ holds the corresponding eigenvalues. $R\in\mathbb R^{M\times M}$ is an arbitrary orthogonal matrix. $B_{ML}$ is unique only up to this orthogonal transformation. $\mu_{ML}$ is the sample mean. $\sigma^2_{ML}$ is the average variance in the orthogonal complement of the principal subspace, i.e. leftover variance treated as noise. The margin note says $\Lambda-\sigma^2I$ is positive semidefinite because the smallest eigenvalue of the data covariance is bounded below by $\sigma^2$ (p. 345).
- **Noise-free limit.** With $S=T\Lambda T^{-1}$ (10.80) and $\mathrm{Cov}[x]=BB^\top+\sigma^2I\to BB^\top$ as $\sigma\to0$,
$$\mathrm{Cov}[\mathcal X]=T\Lambda T^{-1}=BB^\top\iff B=T\Lambda^{1/2}R,\tag{10.81}$$
 which is (10.78) with $\sigma=0$. So (P)PCA decomposes the data covariance matrix (p. 345).
- **Other remarks.** For streaming data, the author recommends iterative EM (Roweis, 1998) (p. 345). To choose the dimension $M$, a heuristic of Gavish and Donoho (2014): if the noise variance $\sigma^2$ can be estimated, discard singular values smaller than $\frac{4\sigma\sqrt D}{\sqrt3}$. Alternatively use (nested) cross-validation or Bayesian model selection (pp. 345–346).
- **Bayesian PCA** (Bishop, 1999): a prior on $(\mu,B,\sigma^2)$ integrated out. This addresses overfitting and allows automatic choice of $M$. The integration is intractable, so approximate inference (MCMC, variational) is proposed (p. 346).
- **Factor analysis (FA):** let each observation dimension $d$ have its own noise variance $\sigma_d^2$. There is no closed-form ML solution, so use e.g. EM. In PPCA all stationary points are global optima; for FA this no longer holds. FA does not change under scaling of the data but gives different solutions under rotation (p. 346).
- **ICA:** keep the latent-variable model but use non-Gaussian priors on $z$. It can be used for blind-source separation. PCA is invariant to rotations, so it identifies the subspace but not the signals themselves (p. 346).
- **Extensions:** kernel PCA via the kernel trick (inner products of infinite-dimensional features). A deep auto-encoder with identity activations is equivalent to PCA. The GP-LVM replaces the linear map with a Gaussian process and marginalizes the parameters. The Bayesian GP-LVM also keeps a distribution over $z$ (p. 347).

## Toy example (ours, not from the text)
Four centered points in $\mathbb R^2$ ($D=2$, $N=4$): $x_1=(2,2)$, $x_2=(-2,-2)$, $x_3=(1,-1)$, $x_4=(-1,1)$. The sum is $(0,0)$.

1. Outer products: $x_1x_1^\top=x_2x_2^\top=\begin{bmatrix}4&4\\4&4\end{bmatrix}$ and $x_3x_3^\top=x_4x_4^\top=\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$. The sum is $\begin{bmatrix}10&6\\6&10\end{bmatrix}$, so $S=\frac14\cdot$ that $=\begin{bmatrix}2.5&1.5\\1.5&2.5\end{bmatrix}$.
2. Eigenpairs: $S(1,1)^\top=(4,4)^\top$, so $\lambda_1=4$ with $b_1=(1,1)/\sqrt2$. $S(1,-1)^\top=(1,-1)^\top$, so $\lambda_2=1$ with $b_2=(1,-1)/\sqrt2$.
3. Codes with $M=1$: $z_n=b_1^\top x_n$ gives $4/\sqrt2=2\sqrt2$, $-2\sqrt2$, $0$, $0$. Variance $=\frac14(8+8+0+0)=4=\lambda_1=V_1$ ✓ (10.15).
4. Reconstructions $\tilde x_n=z_nb_1$: $(2,2)$, $(-2,-2)$, $(0,0)$, $(0,0)$. Squared errors: $0,0,\|(1,-1)\|^2=2,2$. So $J_1=\frac14(0+0+2+2)=1=\lambda_2$ ✓ (10.44). Relative variance captured $V_1/V_2=4/5=0.8$.
5. Wrong direction $b_2$: $z_n=0,0,\sqrt2,-\sqrt2$, variance $\frac14(2+2)=1=\lambda_2$ and $J_1=\frac14(8+8+0+0)=4$. So the variance retained is smaller and the error larger, as the theory predicts.
6. SVD link (10.49): $\sigma_d^2=N\lambda_d$ gives $\sigma_1^2=16$ and $\sigma_2^2=4$.

## Concepts
- [[principal component analysis]] — linear dimensionality reduction by projecting centered data onto the top-$M$ eigenvectors of $S$ (p. 317)
- [[covariance matrix]] — here $S=\frac1N\sum x_nx_n^\top=\frac1NXX^\top$ for centered data, with data points as columns of $X$ (pp. 318, 323)
- [[eigenvector / eigenvalue]] — principal components are eigenvectors of $S$; the eigenvalue is the variance along them (p. 322)
- [[spectral theorem]] — used to get an orthonormal eigenbasis of the symmetric $S$ and $\hat S$ (pp. 322–323)
- [[orthonormal basis / orthogonal matrix]] — columns of $B$ are orthonormal, $B^\top B=I$ (p. 318)
- [[projection]] — $\tilde x=BB^\top x$, the optimal linear reconstruction (p. 329)
- [[rank-one matrix / outer product]] — $BB^\top=\sum b_mb_m^\top$ is a sum of rank-one matrices, rank $M$ (p. 330)
- [[singular value decomposition (SVD)]] — $X=U\Sigma V^\top$; columns of $U$ are principal directions, $\lambda_d=\sigma_d^2/N$ (p. 333)
- [[Eckart–Young theorem]] — the truncated SVD is the best rank-$M$ approximation of $X$ (p. 334)
- [[power iteration]] — $x_{k+1}=Sx_k/\|Sx_k\|$ converges to the top eigenvector (p. 335)
- [[norm]] — spectral norm in (10.50); squared Euclidean norm in the error (pp. 327, 334)
- [[maximum-variance view of PCA]] (new) — choose directions maximizing the variance of the code; the variance equals the eigenvalue (p. 320)
- [[reconstruction error]] (new) — $J_M=\frac1N\sum\|x_n-\tilde x_n\|^2=\sum_{j>M}\lambda_j$ (pp. 327, 332)
- [[principal subspace]] (new) — span of the top-$M$ eigenvectors of $S$, where the projected data live (p. 327)
- [[standardization]] (new) — subtract the mean and divide by the standard deviation per dimension (p. 336)
- [[N ≪ D covariance trick]] (new) — eigenvectors of $\frac1NX^\top X$ ($N\times N$) mapped back by $Xc_m$ (pp. 335–336)
- [[linear auto-encoder]] (new) — encoder $B^\top$, decoder $B$; minimizing the squared loss gives PCA (p. 344)
- [[probabilistic PCA]] (new) — latent-variable model $x=Bz+\mu+\epsilon$ with $z\sim\mathcal N(0,I)$; PCA is its noise-free ML limit (pp. 340, 345)
- [[latent variable]] (new) — an unobserved low-dimensional cause $z$ of the observed $x$ (p. 340)

## Canonical instances
- [[mnist-digit-8-eigenvalue-spectrum]] — only a few of the 200 largest eigenvalues are far from 0, so a few PCs capture most variance (p. 324)
- [[mnist-0-1-pca-embedding]] — a 2-D principal subspace roughly separates "0" and "1"; "0"s vary more (p. 332)
- [[mnist-reconstruction-vs-number-of-pcs]] — reconstruction sharpens with 1, 10, 100, 500 PCs; about 550 PCs give essentially full reconstruction of the training "8"s (pp. 338–339)
- [[ppca-generating-mnist-digits]] — decoding a latent point $z_*$ gives $\tilde x_*=Bz_*$ that looks like an "8" (p. 341)
- [[google-pagerank-power-iteration]] — the original PageRank algorithm uses power iteration on hyperlinks (p. 335)

## Bridges (candidates)
- [same-math] PCA's maximize $b^\top Sb$ s.t. $\|b\|=1$ ↔ linear algebra: Rayleigh quotient maximization — the maximum is the top eigenvalue, attained at its eigenvector.
- [same-math] PCA via SVD of centered $X$, $\lambda_d=\sigma_d^2/N$ ↔ linear algebra: SVD and Eckart–Young — the same factorization, read as variance.
- [same-math] Power iteration for the top eigenvector ↔ network analysis: PageRank / eigenvector centrality — the same iteration on a different matrix.
- [structural-analogy] PPCA covariance $BB^\top+\sigma^2I$ ↔ social-science latent factor models: a few shared factors plus noise explain the correlations among many observed variables.
- [structural-analogy] Linear auto-encoder (encoder $B^\top$, decoder $B$) ↔ deep learning: nonlinear auto-encoders, which generalize PCA.
- [metaphor] The code $z$ as a bottleneck ↔ information theory: lossy compression with limited channel capacity.

## Questions this raises
- The text standardizes by dividing by $\sigma_d$ but calls mean subtraction "not strictly necessary". When does standardization change which directions PCA finds, and does the variance argument still make sense?
- How should $M$ be chosen in practice (the $4\sigma\sqrt D/\sqrt3$ heuristic, cross-validation, Bayesian criteria), and how do these compare?
- PCA and PPCA give $B$ only up to an orthogonal matrix $R$. What does that rotational freedom mean for interpreting components as "factors", and how does ICA with non-Gaussian priors fix it?
- Why does the posterior covariance $C$ in PPCA not depend on $x$, and what does that imply about how confident we can be about an embedding?

## Reading notes
- Printed page = pdf − 6 (pdf 323 = printed 317). All page images show the printed numbers, which I used.
- All equations were checked against the page images; none were unreadable.
- The text layer is garbled in places (e.g. (10.43b), (10.78)) but the images are clear.
- Running footers: "Draft (2024-01-15) of 'Mathematics for Machine Learning'" and "©2024 M. P. Deisenroth, A. A. Faisal, C. S. Ong. Published by Cambridge University Press (2020)".
- p. 326 says we "need to assume" that $z_m$ and $\zeta_m$ are not identical; p. 329 concludes they must be identical. I report both as printed.
- p. 335 states that without duplicate points $S$ has rank $N$ and $D-N+1$ zero eigenvalues, for centered data, without discussing the effect of centering. I report this as the author's statement.
- The Figure 10.9 caption speaks of $U_1$, $U_2$, while the figure is labelled $U$ and $U^\perp$.
- "MMIST" on p. 332 is a typo for MNIST.
- On p. 345, $T$ is first an $M$-column matrix in (10.78) and then a full eigenvector matrix in (10.80); the notation is reused.
- The text writes "there exist $D$ distinct eigenvectors" (p. 323), where "orthonormal" is probably meant.
- The unit prints no exercises, so there is no Exercises section.
