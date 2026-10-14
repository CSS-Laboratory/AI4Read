---
id: boyd-2018-vmls/ch15-multi
work: boyd-2018-vmls
unit: Chapter 15 — Multi-objective least squares
pages: 309–338
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
# Multi-objective least squares

## L0 — One line
To make several squared-norm objectives small at once, minimize their weighted sum, which is an ordinary least squares problem on a stacked matrix. Adding secondary terms such as $\lambda\|x\|^2$ is sometimes called regularization.

## L1 — The gist (≤ 120 words)
Often we want several quantities $\|A_ix-b_i\|^2$ small at once, and they conflict. The chapter's method minimizes a weighted sum. Stacking $\sqrt{\lambda_i}A_i$ turns this into one least squares problem, solved by QR. Varying the weights traces an optimal trade-off curve of Pareto optimal points. Applications: control, estimation (Tikhonov regularization, periodic series, de-blurring, tomography) and regularized data fitting (ridge regression). In Tikhonov regularization the extra term also guarantees independent columns of the stacked matrix. Gram caching and the kernel trick make solving for many weights, or for wide $A$, cheap.

**Prerequisites:** least squares and the normal equations, QR factorization, Gram matrix $A^TA$, linear independence of columns, matrix–vector block notation, flop counts.

## L2 — Key ideas
- Several objectives $J_i=\|A_ix-b_i\|^2$ are combined by a weighted sum with positive weights. Only the relative weights matter, so it is common to set $\lambda_1=1$ (pp. 309–310).
- Stacking $\sqrt{\lambda_i}A_i$ and $\sqrt{\lambda_i}b_i$ gives an ordinary least squares problem. The stacked matrix can have independent columns even if no $A_i$ does (pp. 310–311).
- Every weighted-sum solution is Pareto optimal (no other point is at least as good on every objective and strictly better on one). Plotting $(J_1,J_2)$ against each other as $\lambda$ varies gives the optimal trade-off curve. Weights are "knobs", typically tried on a log grid (pp. 311–314).
- Control and estimation use a primary objective plus secondary ones ($\|x\|^2$, $\|x-x^{\rm nom}\|^2$, $\|Dx\|^2$, Dirichlet energy $\|A^Tx\|^2$ of a graph, which penalizes differences between neighbouring entries). Examples: heating, demand shaping, periodic series, de-blurring, tomography (pp. 314–325).
- Tikhonov regularization $\|Ax-y\|^2+\lambda\|x\|^2$ always has a unique solution $(A^TA+\lambda I)^{-1}A^Ty$, whatever the shape of $A$ (p. 318).
- Regularized data fitting (ridge regression) trades a worse training fit for smaller parameters. $\lambda$ is chosen by validation, and a model may then have more features than data points (pp. 328–330).
- Gram caching reuses $G_i=A_i^TA_i$ across many weights. For wide $A$, the kernel trick via $(A^TA+\lambda I)^{-1}A^T=A^T(AA^T+\lambda I)^{-1}$ reduces cost from order $n^3$ to order $m^2n$ (pp. 332–333).

## L3 — Walkthrough

### 15.1 Multi-objective least squares (pp. 309–314)

**Setup.** We have $k$ objectives $J_i=\|A_ix-b_i\|^2$, with $A_i$ of size $m_i\times n$ and $b_i$ an $m_i$-vector (p. 309). Ordinary least squares can minimize any single $J_i$ (if $A_i$ has independent columns), which gives $k$ different solutions. We want one compromise $\hat x$ (p. 309).

**Weighted sum.** Minimize
$$J=\lambda_1J_1+\dots+\lambda_kJ_k=\lambda_1\|A_1x-b_1\|^2+\dots+\lambda_k\|A_kx-b_k\|^2,\tag{15.1}$$
with positive weights $\lambda_i$ that express our relative desire for each term to be small (p. 309). Scaling all weights by a positive number scales $J$ and does not change the minimizers. So it is common to set $\lambda_1=1$, making $J_1$ the *primary objective* (p. 310).

**Stacking.** Use $\|(a_1,\dots,a_k)\|^2=\|a_1\|^2+\dots+\|a_k\|^2$. Then (p. 310)
$$J=\left\|\begin{bmatrix}\sqrt{\lambda_1}(A_1x-b_1)\\ \vdots\\ \sqrt{\lambda_k}(A_kx-b_k)\end{bmatrix}\right\|^2=\|\tilde Ax-\tilde b\|^2,\qquad
\tilde A=\begin{bmatrix}\sqrt{\lambda_1}A_1\\ \vdots\\ \sqrt{\lambda_k}A_k\end{bmatrix},\ 
\tilde b=\begin{bmatrix}\sqrt{\lambda_1}b_1\\ \vdots\\ \sqrt{\lambda_k}b_k\end{bmatrix}.\tag{15.2}$$
Shapes: $\tilde A$ is $m\times n$, $\tilde b$ has length $m$, with $m=m_1+\dots+m_k$ (p. 310). If the columns of $\tilde A$ are linearly independent, the minimizer is unique and equals
$$\hat x=(\tilde A^T\tilde A)^{-1}\tilde A^T\tilde b=(\lambda_1A_1^TA_1+\dots+\lambda_kA_k^TA_k)^{-1}(\lambda_1A_1^Tb_1+\dots+\lambda_kA_k^Tb_k).\tag{15.3}$$
For $k=1$ this is the standard formula, and then $\lambda_1$ does not matter. $\hat x$ can be computed by QR of $\tilde A$ (p. 310).

> **Intuition note.** Weighting a squared norm by $\lambda$ is the same as scaling its vector by $\sqrt\lambda$ before taking the norm. Once all pieces are stacked in one tall vector, the problem is plain least squares.

**Independent columns of the stacked matrix.** $\tilde A$ has independent columns exactly when no nonzero $x$ satisfies $A_ix=0$ for all $i=1,\dots,k$ (pp. 310–311). Hence if just one $A_i$ has independent columns, $\tilde A$ does. $\tilde A$ can have independent columns even when no $A_i$ does, for example when every $A_i$ is wide ($m_i<n$). Still we need $m_1+\dots+m_k\ge n$, since $\tilde A$ must be tall or square (p. 311).

**Optimal trade-off curve (two objectives).** Write $J=J_1+\lambda J_2$ with $\lambda>0$, and let $\hat x(\lambda)$ be the minimizer, assuming independent columns of the stacked matrix. For small $\lambda$ we care mostly about $J_1$, for large $\lambda$ mostly about $J_2$ (p. 311).

The points $\hat x(\lambda)$ are *Pareto optimal*. This means no $z$ satisfies
$$\|A_1z-b_1\|^2\le\|A_1\hat x(\lambda)-b_1\|^2,\qquad\|A_2z-b_2\|^2\le\|A_2\hat x(\lambda)-b_2\|^2$$
with one of the inequalities strict. Reason: such a $z$ would give a smaller value of $J$ than $\hat x(\lambda)$, which minimizes $J$ — a contradiction (p. 311).

Plot $J_1$ against $J_2$ at $\hat x(\lambda)$ for $\lambda\in(0,\infty)$. This is the *optimal trade-off curve*. No point $z$ has $(J_1,J_2)$ below and to the left of it (p. 311).

> **Intuition note.** If a point beat $\hat x(\lambda)$ on one objective without losing on the other, it would also win on the weighted sum. That is impossible, so the minimizer cannot be improved on one goal without hurting the other.

**Simple example (pp. 311–313).** $A_1,A_2$ are both $10\times5$. Small $\lambda$ gives $\hat x(\lambda)$ close to the least squares solution for $(A_1,b_1)$, and large $\lambda$ gives one close to that for $(A_2,b_2)$. In between, $\hat x(\lambda)_3$ first increases and then decreases (fig. 15.1). As $\lambda$ increases, $J_1$ increases and $J_2$ decreases ("It can be shown that this always holds"), fig. 15.2 (p. 311). On the curve (fig. 15.3) the left end-point minimizes $\|A_1x-b_1\|^2$ and the right end-point minimizes $\|A_2x-b_2\|^2$. For example, no $z$ achieves $\|A_1z-b_1\|^2\le 8$ and $\|A_2z-b_2\|^2\le5$ (p. 311).

The curve is steep near the left end-point. There a substantial decrease in $J_2$ costs only a small increase in $J_1$. Near the right end-point the reverse holds. The author calls this "quite typical" and says it is why multi-criterion least squares is useful (p. 313).

**Trade-off surface.** For $k=3$ there are two weights $\lambda_2,\lambda_3$ relative to $J_1$. Each $\hat x(\lambda)$ is Pareto optimal: no point has $J_1,J_2,J_3$ all less than or equal, with at least one strict. As $\lambda_2,\lambda_3$ vary, $(J_1,J_2,J_3)$ sweeps out the *optimal trade-off surface* (p. 313).

**Using the method in practice (pp. 313–314).**
- $J_1$ is the primary objective, typically what ordinary least squares would minimize (e.g. training mean square error or deviation from a target).
- Secondary objectives $J_2,\dots,J_k$ are typically generic: parameters 'small', 'smooth', or close to a prior value. In estimation they encode prior knowledge about $x$. We accept a larger $J_1$ if the secondary objectives fall enough.
- Weights are 'knobs' tuned until the trade-off is acceptable. For example, if $J_2$ is too large but $J_3$ can grow, increase $\lambda_2$ and decrease $\lambda_3$ and recompute. In data fitting, validation can guide the choice. Elsewhere it is judgment or taste.
- The added terms $\lambda_2J_2,\dots,\lambda_kJ_k$ are called *regularization (terms)*.
- Weights are explored on a logarithmic grid. For $N$ values between $\lambda^{\min}$ and $\lambda^{\max}$: $\lambda^{\min},\theta\lambda^{\min},\dots,\theta^{N-1}\lambda^{\min}=\lambda^{\max}$ with $\theta=(\lambda^{\max}/\lambda^{\min})^{1/(N-1)}$ (p. 314).

### 15.2 Control (pp. 314–316)

The input (action) is an $n$-vector $x$ and the output an $m$-vector $y$. They are related by an affine model $y=Ax+b$. Here $b$ is the output when $x=0$, and often $x,y$ are deviations from standard values (p. 314). With a target output $y^{\rm des}$, the primary objective is $J_1=\|Ax+b-y^{\rm des}\|^2$ (p. 315).

Secondary objectives:
- $J_2=\|x\|^2$: trade missing the target against keeping the input small (p. 315).
- $J_2=\|x-x^{\rm nom}\|^2$: keep the input near a nominal value, e.g. the current one (p. 315).

**Heating and cooling (p. 315).** $x_i>0$ is heating and $x_i<0$ cooling for $n$ air-handling units. $y$ holds temperatures at $m$ locations, and $y^{\rm des}=T^{\rm des}\mathbf 1$. $\|x\|^2$ is "at least roughly" related to energy cost. Minimize $J_1+\lambda_2J_2$ and increase $\lambda_2$ if the powers are too large.

**Demand shaping (pp. 315–316).** Price changes $\delta^{\rm price}$ are the action, and the model is $\delta^{\rm dem}=E^{\rm d}\delta^{\rm price}$. Take $J_1=\|E^{\rm d}\delta^{\rm price}-\delta^{\rm tar}\|^2$ and $J_2=\|\delta^{\rm price}\|^2$. Minimize $J_1+\lambda J_2$ over several $\lambda$.

**Dynamics (p. 316).** For time series, a common model is the convolution $y=h*x$. Then $A$ is Toeplitz and $b$ is the output with $x=0$. Besides $\|x\|^2$, a smoothness objective $\|Dx\|^2$ is common, with the $(n-1)\times n$ first difference matrix
$$D=\begin{bmatrix}-1&1&0&\cdots&0&0&0\\0&-1&1&\cdots&0&0&0\\ \vdots&&&&&&\vdots\\0&0&0&\cdots&-1&1&0\\0&0&0&\cdots&0&-1&1\end{bmatrix}.\tag{15.4}$$

### 15.3 Estimation and inversion (pp. 316–325)

**Model.** $y=Ax+v$, with $A$ known $m\times n$, and $v$ an unknown measurement noise presumed small. We want a sensible guess of $x$ given $y$, $A$ and prior knowledge. With no noise and independent columns, $x=A^\dagger y$ (*exact inversion*). Otherwise we do *approximate inversion* (p. 316). $A$ may be wide, square or tall, and the same methods are used. When $A$ is wide, prior information is needed. Even for square or tall $A$, multi-objective least squares can use prior knowledge and "yield far better results" (p. 317).

#### 15.3.1 Regularized inversion (pp. 317–318)
Guessing $\hat x$ implicitly guesses $v=y-A\hat x$. If smaller $\|v\|$ is more plausible, the primary objective is $\|Ax-y\|^2$ (p. 317). Secondary objectives encode priors (p. 317):
- $\|x\|^2$: $x$ should be small.
- $\|x-x^{\rm prior}\|^2$: $x$ should be near a known $x^{\rm prior}$.
- $\|Dx\|^2$: $x$ should be smooth, with $x_{i+1}$ near $x_i$ (often for time series).
- Dirichlet energy $\mathcal D(x)=\|A^Tx\|^2$ with $A$ the incidence matrix of a graph: $x_i$ near $x_j$ when $i,j$ are joined by an edge. Used as a regularizer it is called *Laplacian regularization*. $\|Dx\|^2$ is the special case for the chain graph.

Estimate: minimize $\|Ax-y\|^2+\lambda_2J_2(x)+\dots+\lambda_pJ_p(x)$, called *regularized inversion* (p. 317).

**Tikhonov regularized inversion.** Minimize $\|Ax-y\|^2+\lambda\|x\|^2$, $\lambda>0$ (p. 317). The stacked matrix $\tilde A=\begin{bmatrix}A\\\sqrt\lambda I\end{bmatrix}$, of size $(m+n)\times n$ (added step: shape), always has independent columns, for any shape of $A$. Reason: $\tilde Ax=(Ax,\sqrt\lambda x)=0$ implies $\sqrt\lambda x=0$, so $x=0$ (p. 318). The Gram matrix $\tilde A^T\tilde A=A^TA+\lambda I$ is therefore always invertible (for $\lambda>0$), and
$$\hat x=(A^TA+\lambda I)^{-1}A^Ty.$$

> **Intuition note.** The $\sqrt\lambda I$ block makes every direction of $x$ cost something. So no nonzero $x$ can be invisible to the stacked system.

**Equalization.** If $x$ is a transmitted signal and $A$ the channel, $y=Ax+v$ includes noise. Estimating $x$ undoes the channel, and is called *equalization* (p. 318).

#### 15.3.2 Estimating a periodic time series (pp. 318–321)
Suppose the $T$-vector $y$ is believed to be a noisy version of a series that repeats every $P$ periods and may be smooth. Examples: hourly temperature (period 24), monthly snowfall (12), daily restaurant sales (weekly) (p. 318).

The periodic series is a $P$-vector $x$. The full series is $\hat y=(x,x,\dots,x)=Ax$ with $A$ the $T\times P$ selector matrix $A=\begin{bmatrix}I\\\vdots\\I\end{bmatrix}$ (assuming $T$ is a multiple of $P$) (p. 318). The error is $\|Ax-y\|^2$. Its minimizer $\hat x$ is found by averaging the entries of $y$ belonging to each entry of $x$ (e.g. all Tuesdays); see exercise 15.10. This works well if $T/P$ is large (p. 319).

For a smoother estimate, assume $x_1\approx x_2,\dots,x_{P-1}\approx x_P$ and also $x_P\approx x_1$ (wrap-around). Non-smoothness is $\|D^{\rm circ}x\|^2$, with the $P\times P$ circular difference matrix $D^{\rm circ}$: the matrix (15.4) shape with $-1$ on the diagonal and $+1$ on the superdiagonal, plus a final row $(1,0,\dots,0,-1)$ (p. 319). Minimize
$$\|Ax-y\|^2+\lambda\|D^{\rm circ}x\|^2 .$$
For $\lambda=0$ we recover simple averaging. As $\lambda$ grows, the estimate becomes smoother and ultimately converges to a constant, the mean of the data (p. 319).

$A\hat x$ is the *extracted seasonal component* and $y-A\hat x$ the *seasonally adjusted* series. $\lambda$ can be chosen by validation, e.g. training on 3 of 4 years and testing on the last (p. 319).

**Ozone example (pp. 319–321).** Hourly ozone for July 1–14, 2014 is a 336-vector $c$ with $c_{24(j-1)+i}$ the value for hour index $i$ on day $j$. Only 275 of 336 values are available. $M_j\subseteq\{1,\dots,24\}$ is the set of available indices on day $j$; e.g. $M_8=\{1,2,3,4,6,7,8,23,24\}$ (p. 319). The 24-vector $x$ is repeated 14 times and estimated by minimizing
$$\sum_{j=1}^{14}\sum_{i\in M_j}\big(x_i-\log(c_{24(j-1)+i})\big)^2+\lambda\Big(\sum_{i=1}^{23}(x_{i+1}-x_i)^2+(x_1-x_{24})^2\Big)$$
for $\lambda=1$ and $\lambda=100$ (fig. 15.4) (p. 321).

#### 15.3.3 Image de-blurring (pp. 321–323)
$x$ is an image and $y=Ax+v$ a blurred, noisy image, with $A$ the blurring. The prior is that neighboring pixel values are similar. Minimize
$$\|Ax-y\|^2+\lambda(\|D_{\rm h}x\|^2+\|D_{\rm v}x\|^2).\tag{15.5}$$
For an $M\times N$ image $X$ stored column-wise ($x$ of length $MN$): $D_{\rm h}$ is $M(N-1)\times MN$, built from $M\times M$ blocks with $-I,\,I$ on the block diagonal and block superdiagonal. $D_{\rm v}$ is $(M-1)N\times MN$, block diagonal with $N$ copies of the $(M-1)\times M$ difference matrix $D$ (p. 321). The penalty is
$$\|D_{\rm h}x\|^2+\|D_{\rm v}x\|^2=\sum_{i=1}^M\sum_{j=1}^{N-1}(X_{i,j+1}-X_{ij})^2+\sum_{i=1}^{M-1}\sum_{j=1}^N(X_{i+1,j}-X_{ij})^2,$$
the Dirichlet energy of the graph joining each pixel to its left/right and up/down neighbors (p. 322). Example: a $512\times512$ image, deblurred for $\lambda=10^{-6},10^{-4},10^{-2},1$ (fig. 15.6). The best result by eye is at $\lambda$ around $0.007$ (p. 322).

#### 15.3.4 Tomography (pp. 322–325)
$x$ holds a quantity (e.g. density) in $n$ voxels (pixels in 2-D). Each measurement $y_i$ is the intensity of a beam after passing through the region, related to the integral of absorption along the beam (CAT scan, weld inspection) (p. 322).

*Line integrals (2-D).* With density $d(x,y)=0$ outside the region, a line is $p(t)=(x_0,y_0)+t(\cos\theta,\sin\theta)$. Its line integral is $\int_{-\infty}^{\infty}d(p(t))\,dt$. Measurement $y_i$ is this integral plus small noise (p. 324).

*Pixel model.* Density is constant, $x_j$, in pixel $j$. The line integral is the sum of $x_j$ times the length of the line inside pixel $j$. In figure 15.7 (25 pixels numbered row-wise from the top left, unit size) the printed result is $1.06x_{16}+0.80x_{17}+0.27x_{12}+1.06x_{13}+1.06x_{14}+0.53x_{15}+0.54x_{10}$ (p. 324).

*Measurement model.* Without noise the measurements are $Ax$, with $A_{ij}=$ length of line $i$ in pixel $j$ ($0$ if no intersection), $A$ being $m\times n$ (p. 324).

*Reconstruction.* Minimize $\|Ax-y\|^2$ plus regularizers for smoothness. A common one is the Dirichlet energy of the graph joining each voxel to its 6 (3-D) or 4 (2-D) neighbors, also called Laplacian regularization (p. 324).

*Example (pp. 325–327).* $m=4000$ lines (100 points around the square, 40 beams from each point), on $100\times100$ pixels so $n=10000$. The true density is 0 or 1 per pixel (fig. 15.9). Solve: minimize $\|Ax-y\|^2+\lambda\|Dx\|^2$, with $\|Dx\|^2$ the sum of squared differences of pixel values from their neighbors. Figure 15.10 uses $\lambda=10^{-2},10^{-1},1,5,10,100$. For small $\lambda$ the reconstruction is relatively sharp but noisy. For large $\lambda$ it has less noise but is too smooth (p. 325).

### 15.4 Regularized data fitting (pp. 325–330)

Regularization is another way to avoid over-fitting, different from choosing a simpler model with fewer basis functions. It is also called *de-tuning*, *shrinkage* or *ridge regression* (p. 325).

**Motivation.** Model $\hat f(x)=\theta_1f_1(x)+\dots+\theta_pf_p(x)$ (15.6). A large $\theta_i$ makes predictions sensitive to variation in $f_i(x)$ in new data, so we prefer small $\theta_i$. Exception: if $f_i$ is constant, its size does not matter (p. 328). With $f_1=1$, minimize
$$\|y-A\theta\|^2+\lambda\|\theta_{2:p}\|^2,\tag{15.7}$$
where $\lambda>0$ is the *regularization parameter*. For a regression model this is $\|y-X^T\beta-v\mathbf 1\|^2+\lambda\|\beta\|^2$, which penalizes $\beta$ but not the offset $v$. Choosing $\beta$ this way is *ridge regression* (p. 328).

**Effect.** We accept a worse fit $\|y-A\theta\|^2$ for smaller parameters (except $\theta_1$). Parameters are *shrunk*. The model is not excessively "tuned" to the training data (p. 328).

**Regularization path.** The way parameters change with $\lambda$ is the *regularization path*. Usually 30 or 50 values of $\lambda$ are used, log-spaced (p. 328). Choose $\lambda$ by out-of-sample or cross-validation. As $\lambda$ increases, training RMS error increases. Test RMS error typically decreases and then, for too large $\lambda$, increases. A good $\lambda$ approximately minimizes test RMS error. If several values do, common practice is to take the largest, i.e. the model of minimum sensitivity $\|\beta\|^2$ among those predicting well (p. 328).

**Example (pp. 329–330).** The signal is $s(t)=c+\sum_{k=1}^4\alpha_k\sin(\omega_kt+\phi_k)$ with
$$c=1.54,\ \alpha_1=0.66,\ \alpha_2=-0.90,\ \alpha_3=-0.66,\ \alpha_4=0.89,\tag{15.8}$$
$\omega=(13.69,3.55,23.25,6.03)$, $\phi=(0.21,0.02,-1.87,1.72)$. The model has $p=5$, $f_1=1$, $f_{k+1}(x)=\sin(\omega_kx+\phi_k)$. It is exact for $\theta_1=c$, $\theta_k=\alpha_{k-1}$, which "rarely occurs in practice". Fit on 10 noisy samples, test on 20 (fig. 15.11). As $\lambda$ grows, $\theta_2,\dots,\theta_5$ shrink toward zero and training error increases. Test error first decreases to a minimum around $\lambda=0.079$, then increases. Any $\lambda$ between about $0.065$ and $0.100$ is reasonable, and near $0.079$ the estimates are close to the true values (fig. 15.12) (pp. 329–330).

**Independent columns.** The stacked matrix $\begin{bmatrix}A\\\sqrt\lambda B\end{bmatrix}$, with $B=[e_2\ \cdots\ e_p]^T$ the $(p-1)\times p$ selector so $B\theta=\theta_{2:p}$, always has independent columns, even if $A$ does not (the proof uses that the first column of $A$ is $\mathbf1$). Suppose $\begin{bmatrix}A\\\sqrt\lambda B\end{bmatrix}x=0$. The last $p-1$ rows give $\sqrt\lambda x_i=0$, so $x_2=\dots=x_p=0$. The first column of $A$ is $\mathbf1$, so the top equations become $\mathbf1x_1=0$, hence $x_1=0$ (p. 330).

**Feature engineering.** A rough rule keeps the number of features small relative to data points (say at most 10–20%). Regularization lets us use more features than appropriate otherwise, even more features than data points ($A$ wide). It is "often the key to success in feature engineering" (p. 330).

### 15.5 Complexity (pp. 330–333)

Forming $\tilde A,\tilde b$ and using QR costs order $mn^2$ flops, $m=m_1+\dots+m_k$. For $L$ weight choices the total is order $Lmn^2$ (p. 330).

#### 15.5.1 Gram caching (p. 332)
From (15.3), $\hat x$ solves $G\hat x=h$, where $G=\lambda_1G_1+\dots+\lambda_kG_k$ with $G_i=A_i^TA_i$, and $h=\lambda_1h_1+\dots+\lambda_kh_k$ with $h_i=A_i^Tb_i$. Costs: forming $G_i,h_i$ is $m_in^2$ and $2m_in$ flops (a factor two saved for the Gram matrix); summed, about $mn^2$. Forming $G,h$ costs $2kn^2$. Solving $G\hat x=h$ costs order $2n^3$.

*Gram caching* computes $G_i,h_i$ once and reuses them for $L$ weight choices. Total complexity as printed: $mn^2+L(k+2n)n^2$ flops. When $m$ is much larger than $k+n$ (common) this is smaller than $Lmn^2$.

*Tikhonov example.* Compute $\hat x^{(i)}=(A^TA+\lambda^{(i)}I)^{-1}A^Tb$ for $i=1,\dots,L$. The simple method costs $2Lmn^2$. Gram caching costs $mn^2+2Ln^3=(m+2Ln)n^2$ (the $Lkn^2$ term is dropped since $k=2$). With $m=100n$, $L=100$, caching reduces cost by more than a factor of 50. (Added step: $2\cdot100\cdot100n\cdot n^2=20000n^3$ versus $(100n+200n)n^2=300n^3$, ratio about 67.) The whole regularization path costs not much more than a single solution (p. 332).

> **Intuition note.** The expensive part, touching all $m$ rows of each $A_i$, is the same for every weight. Only small $n\times n$ work depends on the weights, so do the big part once.

#### 15.5.2 The kernel trick (pp. 332–333)
Special case:
$$J=\|Ax-b\|^2+\lambda\|x-x^{\rm des}\|^2,\qquad A\ m\times n\ \text{wide } (m<n),\ \lambda>0.\tag{15.9}$$
The stacked matrix $\begin{bmatrix}A\\\sqrt\lambda I\end{bmatrix}$ is $(m+n)\times n$ with independent columns. QR costs $2(m+n)n^2$, growing like $n^3$ (p. 332). From (15.3):
$$\hat x=(A^TA+\lambda I)^{-1}(A^Tb+\lambda x^{\rm des})=(A^TA+\lambda I)^{-1}\big(A^Tb+(\lambda I+A^TA)x^{\rm des}-A^TAx^{\rm des}\big)=(A^TA+\lambda I)^{-1}A^T(b-Ax^{\rm des})+x^{\rm des}.$$
This inverse is $n\times n$ (p. 333). The key identity, valid for any matrix $A$ and any $\lambda>0$, is
$$(A^TA+\lambda I)^{-1}A^T=A^T(AA^T+\lambda I)^{-1}.\tag{15.10}$$
The right side inverts a smaller $m\times m$ matrix. (This is a variation on the push-through identity of exercise 11.9.) *Proof:* both $A^TA+\lambda I$ and $AA^T+\lambda I$ are invertible. Start from $A^T(AA^T+\lambda I)=(A^TA+\lambda I)A^T$, multiply by $(A^TA+\lambda I)^{-1}$ on the left and $(AA^T+\lambda I)^{-1}$ on the right (p. 333).

Hence $\hat x=A^T(AA^T+\lambda I)^{-1}(b-Ax^{\rm des})+x^{\rm des}$. Compute $(AA^T+\lambda I)^{-1}(b-Ax^{\rm des})$ via QR of the $(m+n)\times m$ matrix $\bar A=\begin{bmatrix}A^T\\\sqrt\lambda I\end{bmatrix}$ at cost $2(m+n)m^2$. The remaining operations are matrix–vector products of order at most $mn$ flops. So $\hat x$ costs about $2(m+n)m^2$, linear in $n$ (p. 333).

Summary: the direct way costs $2(m+n)n^2$ and the kernel-trick way costs $2(m+n)m^2$. Use the kernel trick when $m<n$. The complexity is $(m+n)\min\{m^2,n^2\}\approx\min\{mn^2,nm^2\}=\max\{m,n\}\,(\min\{m,n\})^2$ (p. 333). This is an instance of the *big-times-small-squared* rule: many operations on a matrix cost order (big) × (small)$^2$ flops. More examples are in appendix B (p. 333).

> **Intuition note.** The same answer can be reached by inverting a matrix whose size is the number of unknowns ($n$) or the number of equations ($m$). For wide $A$ the second is much smaller.

## Toy example (ours)
Two scalar objectives, $x\in\mathbb R$: $J_1=(x-0)^2$ (so $A_1=1,b_1=0$) and $J_2=(x-1)^2$ ($A_2=1,b_2=1$). Minimize $J_1+\lambda J_2$.

Stacked form: $\tilde A=\begin{bmatrix}1\\\sqrt\lambda\end{bmatrix}$, $\tilde b=\begin{bmatrix}0\\\sqrt\lambda\end{bmatrix}$. By (15.3), $\hat x=(1+\lambda)^{-1}(0+\lambda)=\lambda/(1+\lambda)$. Then $J_1=\lambda^2/(1+\lambda)^2$ and $J_2=\big(\tfrac{\lambda}{1+\lambda}-1\big)^2=1/(1+\lambda)^2$.

| $\lambda$ | $\hat x$ | $J_1$ | $J_2$ |
|---|---|---|---|
| 1/3 | $\frac{1/3}{4/3}=0.25$ | $0.0625$ | $(0.75)^2=0.5625$ |
| 1 | $0.5$ | $0.25$ | $0.25$ |
| 3 | $\frac34=0.75$ | $0.5625$ | $0.0625$ |

As $\lambda$ rises, $J_1$ rises and $J_2$ falls, as the chapter says. Here $\sqrt{J_1}+\sqrt{J_2}=\frac{\lambda}{1+\lambda}+\frac1{1+\lambda}=1$, so the trade-off curve is the arc $\sqrt{J_1}+\sqrt{J_2}=1$ (added step; this is specific to this example).

Kernel-trick check, wide case: $A=[1\ 1]$ ($m=1,n=2$), $y=2$, $\lambda=1$ (Tikhonov, $x^{\rm des}=0$). Direct: $A^TA+I=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ with inverse $\frac13\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$ and $A^Ty=(2,2)$, so $\hat x=\frac13(4-2,\,-2+4)=(\tfrac23,\tfrac23)$. Kernel form: $AA^T+\lambda=2+1=3$, so $\hat x=A^T\cdot\frac13\cdot2=(\tfrac23,\tfrac23)$. Same, with a $1\times1$ inverse instead of a $2\times2$.

## Concepts
- [[multi-objective-least-squares]] (new) — choose one $x$ making several $\|A_ix-b_i\|^2$ small; solved by a weighted sum (p. 309)
- [[weighted-sum-objective]] (new) — $J=\sum\lambda_iJ_i$ with positive weights; only relative weights matter (pp. 309–310)
- [[stacked-least-squares]] (new) — stack $\sqrt{\lambda_i}A_i$ and $\sqrt{\lambda_i}b_i$ to get a standard least squares problem (p. 310)
- [[least-squares]] — reused; the stacked problem is solved by $(\tilde A^T\tilde A)^{-1}\tilde A^T\tilde b$, via QR (p. 310)
- [[linear-independence]] — reused; stacked columns are independent iff no nonzero $x$ has all $A_ix=0$ (p. 310)
- [[pareto-optimality]] (new) — no point beats a solution on one objective without losing on another; holds for every weighted-sum minimizer (p. 311)
- [[optimal-trade-off-curve]] (new) — plot of $(J_1,J_2)$ at $\hat x(\lambda)$ over $\lambda>0$; the surface for $k=3$ (pp. 311, 313)
- [[regularization]] (new) — secondary terms $\lambda_iJ_i$ added to the primary objective, encoding prior knowledge (p. 314)
- [[tikhonov-regularization]] (new) — minimize $\|Ax-y\|^2+\lambda\|x\|^2$; solution $(A^TA+\lambda I)^{-1}A^Ty$ (p. 317)
- [[ridge-regression]] (new) — Tikhonov regularization in data fitting, penalizing $\beta$ but not the offset (p. 328)
- [[regularization-path]] (new) — how fitted parameters change with $\lambda$; $\lambda$ chosen by validation (p. 328)
- [[first-difference-matrix]] (new) — $D$ with rows $(e_{i+1}-e_i)^T$; $\|Dx\|^2$ penalizes roughness (p. 316)
- [[graph-laplacian]] — canon link: Dirichlet energy $\|A^Tx\|^2$ for an incidence matrix, used as "Laplacian regularization" (p. 317)
- [[incidence-matrix]] — reused; defines the Dirichlet energy (p. 317)
- [[gram-caching]] (new) — precompute $A_i^TA_i,A_i^Tb_i$ once, reuse for many weights (p. 332)
- [[kernel-trick]] (new) — use $(A^TA+\lambda I)^{-1}A^T=A^T(AA^T+\lambda I)^{-1}$ to invert a small $m\times m$ matrix (p. 333)
- [[big-times-small-squared]] (new) — many matrix operations cost order (big)×(small)$^2$ flops (p. 333)
- [[pseudoinverse]] — reused; exact inversion $x=A^\dagger y$ (p. 316); defined as a Tikhonov limit in exercise 15.11 (p. 337)

## Canonical instances
- [[simple-bicriterion-10x5]] — $\hat x(\lambda)$, $J_1,J_2$ and the trade-off curve for two $10\times5$ objectives (p. 311)
- [[heating-cooling-control]] — track target temperature while penalizing power $\|x\|^2$ (p. 315)
- [[demand-shaping]] — choose price changes to reach a target demand change, with $\|\delta^{\rm price}\|^2$ penalty (pp. 315–316)
- [[periodic-time-series-ozone]] — smooth periodic fit to log hourly ozone, $\lambda=1,100$ (pp. 319–321)
- [[image-deblurring]] — $\|Ax-y\|^2+\lambda(\|D_hx\|^2+\|D_vx\|^2)$, best $\lambda\approx0.007$ (p. 322)
- [[tomography-reconstruction]] — line-integral model $A_{ij}$, $n=10000$, $m=4000$, Laplacian regularization (p. 325)
- [[sinusoid-ridge-example]] — five-parameter ridge fit, minimum test error near $\lambda=0.079$ (p. 329)

## Bridges (candidates)
- [same-math] Dirichlet energy $\|A^Tx\|^2$ (incidence matrix) ↔ linear-algebra canon: graph Laplacian quadratic form $\sum(x_i-x_j)^2$ — both are $x^T(AA^T)x$ for the incidence matrix $A$.
- [same-math] Tikhonov limit $\lim_{\lambda\to0}(A^TA+\lambda I)^{-1}A^T$ ↔ pseudoinverse: exercise 15.11 defines $A^\dagger$ this way for any matrix.
- [structural-analogy] Pareto optimal trade-off curve ↔ economics: efficient frontier of competing goals; the text names Pareto as the economist behind the term.
- [structural-analogy] Choosing the largest $\lambda$ among near-minimizers of test error ↔ model selection: prefer the least sensitive model among those that predict equally well.
- [metaphor] Weights as 'knobs' ↔ engineering control panels: tune until the trade-off is acceptable.

## Questions this raises
- Is there a principled way to pick $\lambda$ beyond validation, for instance when only a trade-off curve is available?
- Does the weighted-sum approach reach every Pareto optimal point, or only some when the objectives are not quadratic?
- How does the shrinkage of $\theta$ as $\lambda$ grows relate to the singular values of $A$?
- How accurate is the "(big)×(small)²" rule once sparsity or structure (Toeplitz, difference matrices) is used?

## Exercises worth doing
- Ex. 15.1 (p. 334) — scalar case: the weighted-sum minimizer is a convex combination of the $b_i$; find the weights — difficulty: easy
- Ex. 15.2 (p. 334) — if columns $2..p$ of $A$ have mean zero, penalizing $\theta_1$ or not gives the same $\theta_2..\theta_p$ — difficulty: medium
- Ex. 15.3 (p. 334) — weighted Gram matrix is invertible provided no nonzero $x$ has all $A_ix=0$ — difficulty: easy
- Ex. 15.5 (b),(c) (p. 335) — trade-off curve slopes downward, and its slope at $\hat x(\lambda)$ is $-1/\lambda$ — difficulty: hard
- Ex. 15.6 (p. 335) — smoothness-regularized stacked matrix has independent columns iff $A\mathbf1\neq0$ — difficulty: medium
- Ex. 15.10 (p. 337) — unregularized periodic fit equals averaging over periods — difficulty: easy

## Reading notes
- Printed page = pdf page − 10 (pdf 319 = printed 309). The unit ends at printed 337; printed 338 is blank.
- The text layer garbles matrices. I checked the matrices ($D$, $D^{\rm circ}$, $D_h$, $D_v$) against the page images.
- Figures 15.5, 15.6, 15.8–15.10 are images. I described them only as the text does (and the stated $\lambda$ values read from panel labels).
- Complexity in §15.5.1: the text prices forming $G,h$ at $2kn^2$ and solving at about $2n^3$, which sum to $2(k+n)n^2$ per weight choice. The printed total is $mn^2+L(k+2n)n^2$, and it then says "$m$ much larger than $k+n$". I copied the printed formula. The two expressions do not match exactly (the printed total has $k$ where my sum has $2k$ in the $n^2$ term).
- Exercise 15.10 as printed says "for $i=1,\dots,P-1$"; the formula seems intended for all $P$ entries (my reading).
- Exercise 15.5(c) hint (p. 335): "S ≥ −1/λ" and "S ≤ −1/λ" are as printed.
