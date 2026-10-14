---
id: boyd-2018-vmls/ch18-nonlinear
work: boyd-2018-vmls
unit: Chapter 18 — Nonlinear least squares
pages: 381–418
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Nonlinear least squares

## L0 — One line
To solve f(x)=0 or minimize ‖f(x)‖² for a non-affine f, repeatedly replace f by its affine approximation at the current point and solve a linear least squares problem, with a penalty on step length (Levenberg–Marquardt) to keep the approximation trustworthy.

## L1 — The gist (≤ 120 words)
How can we solve f(x)=0, or minimize ‖f(x)‖², when f is not affine (linear plus a constant)? Exact methods exist but are rarely used. The chapter therefore offers heuristics (algorithms that often work, but not always). Gauss–Newton replaces f by its affine approximation at the current iterate and solves a linear least squares problem. It can diverge, and it needs linearly independent Jacobian columns. Levenberg–Marquardt adds a penalty on the step length, weighted by a trust parameter, and addresses both problems. Applications: equilibrium prices, locating an object from distances, nonlinear model fitting, and a classifier that smooths sign with a sigmoid (smooth S-shaped curve). On MNIST digits this classifier gives clearly lower error than the linear least squares classifier.

**Prerequisites:** least squares and the normal equations; QR factorization; regularized (multi-objective) least squares; Jacobian/derivative matrix and Taylor approximation; linear independence of columns; gradient of a scalar function.

## L2 — Key ideas (5–10 bullets)
- **Problem and optimality condition.** Minimizing ‖f(x)‖² generalizes linear least squares. A minimizer must satisfy 2Df(x̂)ᵀf(x̂)=0. This condition is necessary but not sufficient (p. 383).
- **Hardness forces heuristics.** For nonlinear equations there may be no solution, one, or many. There is no analog of QR factorization for this problem. We can only hope for an algorithm that often works (p. 383).
- **Gauss–Newton idea.** Alternate between an affine (Taylor) approximation of f at x⁽ᵏ⁾ and a linear least squares solve. The next iterate minimizes ‖f̂(x;x⁽ᵏ⁾)‖² (p. 387).
- **Why it can fail.** The approximate residual always goes down, but the true residual can go up if the step is large. Also, Df must have independent columns (p. 388).
- **Newton's method** is the case m=n. It solves f(x)=0 by f̂=0. On the sigmoid function it converges from 0.95 and diverges from 1.15 (pp. 388–390).
- **Levenberg–Marquardt (LM).** Minimize ‖f̂‖²+λ‖x−x⁽ᵏ⁾‖². The step formula (18.12) always exists, since the matrix is invertible for λ>0 (pp. 391–392).
- **Trust parameter and practice.** Accept the step and shrink λ if the true residual decreases. Otherwise reject it and grow λ. LM is still a heuristic. Warm starts and multiple runs are common (pp. 392–393).
- **Examples.** Equilibrium prices and location from ranges. For ranges, one of three starts ends at a non-optimal point (pp. 394–396).
- **Model fitting.** Nonlinear parametrized models, and orthogonal distance regression, which also moves the feature vectors, are both nonlinear least squares problems (pp. 399–400).
- **Classification.** Replacing sign by a sigmoid gives a differentiable surrogate for the error count. On MNIST, the error drops from 1.6% to about 0.7% (digit zero) and from 13.9% to 7.6% (ten digits, test set) (pp. 401–409).

## L3 — Walkthrough

### 18.1 Nonlinear equations and least squares

**18.1.1 Nonlinear equations (pp. 381–382).**
- Consider $m$ equations in $n$ unknowns $x=(x_1,\dots,x_n)$: $f_i(x)=0$, $i=1,\dots,m$, with $f_i:\mathbf R^n\to\mathbf R$. The value $f_i(x)$ is the $i$th *residual* (p. 381).
- A system $f_i(x)=b_i$ is converted by setting $\tilde f_i(x)=f_i(x)-b_i$ (p. 381).
- Vector form: $f(x)=0$ \tag{18.1}, with $f:\mathbf R^n\to\mathbf R^m$. The $m$-vector $f(x)$ is the residual vector (pp. 381–382).
- If $f$ is affine this is a set of linear equations. These are solved, or approximately solved by least squares when $m>n$, with earlier tools. The chapter treats non-affine $f$ (p. 382).
- Terms: $m<n$ is *under-determined*, $m=n$ is *square*, $m>n$ is *over-determined* (p. 382).

**18.1.2 Nonlinear least squares (p. 382).**
- If no solution exists, minimize $f_1(x)^2+\dots+f_m(x)^2=\|f(x)\|^2$. A point $\hat x$ with $\|f(x)\|^2\ge\|f(\hat x)\|^2$ for all $x$ is a least squares approximate solution. It solves the *nonlinear least squares problem*
$$\text{minimize}\quad \|f(x)\|^2 .\tag{18.2}$$
- For affine $f$ this is the linear least squares problem of chapter 12. Any solution of $f(x)=0$ also solves (18.2). Approximate solutions are often useful even when $f(x)\neq 0$, so the chapter focuses on (18.2) (p. 382).

**18.1.3 Optimality condition (pp. 382–383).**
- A necessary condition: every partial derivative of $\|f(x)\|^2$ must vanish at $\hat x$, i.e. $\nabla\|f(\hat x)\|^2=0$.
- The gradient is
$$\nabla\|f(x)\|^2=\nabla\Big(\sum_{i=1}^m f_i(x)^2\Big)=2\sum_{i=1}^m f_i(x)\nabla f_i(x)=2Df(x)^Tf(x).$$
- Here $Df(x)$ is the $m\times n$ Jacobian (derivative) matrix, the matrix of partial derivatives. So a minimizer must satisfy
$$2Df(\hat x)^Tf(\hat x)=0 .\tag{18.3}$$
- (18.3) is *necessary*: every solution satisfies it. It is not *sufficient*: other points may satisfy it without being solutions (p. 383).
- For affine $f$, (18.3) reduces to the normal equations (12.4) (p. 383).

> **Intuition note.** Setting the slope of the cost to zero is the first thing calculus demands of a minimizer. But other points can satisfy the condition without being solutions, so reaching it does not guarantee the best point.

**18.1.4 Difficulty (p. 383).**
- Nonlinear equations can have no solution, any number, or infinitely many. Deciding which case holds is very hard computationally. There is no analog of QR factorization for this problem.
- Exact (non-heuristic) algorithms exist but are complicated, very demanding, and rarely used.
- So we lower our expectations. We hope for an algorithm that often finds a solution, or at least a point with small residual norm. Such algorithms are *heuristics*. The k-means algorithm is one. QR-based linear least squares is not a heuristic, since it always works.
- Many heuristics, including those below, compute a point satisfying (18.3). Unless $f(\hat x)=0$, such a point need not solve (18.2).

**18.1.5 Examples (pp. 384–386).**
*Equilibrium points (typically square, $m=n$):*
- *Equilibrium prices.* Demand $D(p)$ and supply $S(p)$ are $n$-vector functions of the price vector $p$. Equilibrium means $S(p)=D(p)$, i.e. $f(p)=S(p)-D(p)=0$. The vector $f(p)$ is the *excess supply*. Figure 18.1 shows the case $n=1$ (p. 384).
- *Chemical equilibrium.* With concentration vector $c$, consumption $C(c)$ and generation $G(c)$: solve $f(c)=C(c)-G(c)=0$ (p. 384).
- *Mechanical equilibrium.* A system of $N$ nodes in 3-D has a stacked position $3N$-vector $q$ and a net-force $3N$-vector $F(q)$. Equilibrium is $F(q)=0$, which is $3N$ equations in $3N$ unknowns (p. 385).
- *Nash equilibrium.* Agent $i$ chooses $x_i$ and has payoff $R_i(x)$. At a Nash equilibrium no agent can increase her reward by changing her own choice. Hence $x_i$ maximizes $R_i$, so $\partial R_i/\partial x_i(x)=0$ for all $i$. This is a *necessary* condition and is a square set of nonlinear equations (p. 385).

*Nonlinear least squares:*
- *Location from range measurements.* The unknown location $x$ (2-D or 3-D) and known points $a_1,\dots,a_m$ give $\rho_i=\|x-a_i\|+v_i$, with small unknown errors $v_i$. Minimize $\sum_{i=1}^m(\|x-a_i\|-\rho_i)^2$. GPS uses a similar method (p. 386).
- *Nonlinear model fitting.* Fit $y\approx\hat f(x;\theta)$ by minimizing
$$\sum_{i=1}^N\big(\hat f(x^{(i)};\theta)-y^{(i)}\big)^2 .\tag{18.4}$$
Unlike chapter 13, $\hat f$ need not be affine in $\theta$. A regularization term may be added (p. 386).

### 18.2 Gauss–Newton algorithm

Setup (p. 386): iterative algorithms generate $x^{(1)},x^{(2)},\dots$. $x^{(1)}$ is the *starting point* and $x^{(k)}$ the $k$th *iterate*. Going from $x^{(k)}$ to $x^{(k+1)}$ is an *iteration*. Iterates are judged by $\|f(x^{(k)})\|$. Stop when this is small enough, when $x^{(k+1)}$ is very near $x^{(k)}$, or after a maximum number of iterations.

**18.2.1 Basic Gauss–Newton (pp. 387–388).**
- Idea: alternate between (i) an affine approximation of $f$ at the current iterate (calculus) and (ii) a linear least squares solve for the next iterate (p. 387).
- The Taylor approximation at $x^{(k)}$ ($Df(x^{(k)})$ is $m\times n$):
$$\hat f(x;x^{(k)})=f(x^{(k)})+Df(x^{(k)})(x-x^{(k)}) .\tag{18.5}$$
It is a very good approximation of $f(x)$ when $\|x-x^{(k)}\|$ is small.
- $x^{(k+1)}$ is the minimizer of $\|\hat f(x;x^{(k)})\|^2$. If $Df(x^{(k)})$ has linearly independent columns (which requires $m\ge n$):
$$x^{(k+1)}=x^{(k)}-\big(Df(x^{(k)})^TDf(x^{(k)})\big)^{-1}Df(x^{(k)})^Tf(x^{(k)}).\tag{18.6}$$
- (added step) Write $A=Df(x^{(k)})$ and $b=Ax^{(k)}-f(x^{(k)})$, so $\hat f(x)=Ax-b$. The least squares minimizer is $(A^TA)^{-1}A^Tb=x^{(k)}-(A^TA)^{-1}A^Tf(x^{(k)})$, which is (18.6).
- **Algorithm 18.1** (given differentiable $f$, start $x^{(1)}$; for $k=1,\dots,k^{\max}$): (1) evaluate $Df(x^{(k)})$ and form $\hat f$; (2) set $x^{(k+1)}$ as the minimizer of $\|\hat f(x;x^{(k)})\|^2$, given by (18.6) (p. 387).
- It stops early if $f(x)$ is very small or $x^{(k+1)}\approx x^{(k)}$. It stops with an error if the columns of $Df(x^{(k)})$ are linearly dependent (p. 387).
- $x^{(k+1)}=x^{(k)}$ holds when $(Df^TDf)^{-1}Df^Tf=0$. Given independent columns, this happens iff $Df(x^{(k)})^Tf(x^{(k)})=0$. So the algorithm stops only when (18.3) holds (p. 387).
- Two facts to separate (p. 388):
$$\|\hat f(x^{(k+1)};x^{(k)})\|^2\le\|\hat f(x^{(k)};x^{(k)})\|^2=\|f(x^{(k)})\|^2\tag{18.7}$$
This holds because $x^{(k+1)}$ minimizes $\|\hat f\|^2$ and $\hat f(x^{(k)};x^{(k)})=f(x^{(k)})$. It says the *approximation's* residual norm goes down. It is **not** the same as
$$\|f(x^{(k+1)})\|^2\le\|f(x^{(k)})\|^2,\tag{18.8}$$
the *true* residual decreasing, which is what we want.

*Shortcomings (p. 388).* Gauss–Newton can converge very quickly to a point with small residual, but it has two serious shortcomings:
1. It can *diverge*: $\|f(x^{(k)})\|$ increases to large values. The approximation $\|f(x)\|^2\approx\|\hat f(x;x^{(k)})\|^2$ is guaranteed only for $x$ near $x^{(k)}$. If $x^{(k+1)}$ is far from $x^{(k)}$, the true residual at $x^{(k+1)}$ can be larger than at $x^{(k)}$.
2. It assumes independent columns of $Df(x^{(k)})$. In some applications this never holds. In others it fails at some iterate, and then $x^{(k+1)}$ is undefined and the algorithm stops.

> **Intuition note.** The affine approximation is guaranteed to be accurate only near the point where it was formed. Gauss–Newton jumps to the bottom of the approximation, which may be far away, where the approximation need not match the real function.

**18.2.2 Newton algorithm (pp. 388–390).**
- For $m=n$, $Df(x^{(k)})$ is square, so (18.6) simplifies:
$$x^{(k+1)}=x^{(k)}-(Df)^{-1}(Df^T)^{-1}Df^Tf=x^{(k)}-\big(Df(x^{(k)})\big)^{-1}f(x^{(k)}),$$
which is the Newton algorithm. It is sometimes called Newton–Raphson: Newton developed it only for $n=1$ and Raphson extended it to $n>1$ (p. 388).
- **Algorithm 18.2:** form $\hat f$ as in (18.5). Set $x^{(k+1)}$ as the solution of $\hat f(x;x^{(k)})=0$, which is the update above (p. 389).
- It has the same shortcomings: it can diverge, and it stops if the derivative matrix is not invertible (p. 389).
- For $n=1$:
$$x^{(k+1)}=x^{(k)}-f(x^{(k)})/f'(x^{(k)}) .\tag{18.9}$$
Set $f(x^{(k)})+f'(x^{(k)})(x-x^{(k)})=0$. If $f'(x^{(k)})\ne0$ the solution is (18.9). If $f'(x^{(k)})=0$ the algorithm stops with an error (p. 389; figure 18.2).
- **Example (p. 390).** The sigmoid function
$$f(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}\tag{18.10}$$
has the unique zero $x=0$. Newton started at $x^{(1)}=0.95$ converges quickly to 0. Started at $x^{(1)}=1.15$, the iterates diverge (figures 18.3, 18.4).

> **Intuition note.** Newton's method follows the tangent line down to the axis. Near a zero this can work very well (it did from 0.95). On a curve that flattens out, like the sigmoid, a tangent from a slightly worse start can shoot far away.

### 18.3 Levenberg–Marquardt algorithm

LM is a variation that addresses both shortcomings (p. 391). The text says it is also sometimes called Gauss–Newton, since it naturally extends the basic algorithm (p. 391).

**Multi-objective update (pp. 391–392).**
- The trouble is that the minimizer of $\|\hat f\|^2$ may be far from $x^{(k)}$, where $\hat f\approx f$ need not hold. So there are two objectives: $\|\hat f(x;x^{(k)})\|^2$ small, and $\|x-x^{(k)}\|^2$ small. Choose $x^{(k+1)}$ as the minimizer of
$$\|\hat f(x;x^{(k)})\|^2+\lambda^{(k)}\|x-x^{(k)}\|^2,\tag{18.11}$$
with $\lambda^{(k)}>0$ (p. 391).
- Small $\lambda^{(k)}$ mainly minimizes the first term. Large $\lambda^{(k)}$ keeps $x^{(k+1)}$ near $x^{(k)}$. For $\lambda^{(k)}=0$ it is the Gauss–Newton iterate. The second term is the *trust penalty*, and $\lambda^{(k)}$ is the *trust parameter* ("distrust parameter" would be more accurate) (p. 391).
- This is a regularized least squares problem, equivalent to minimizing
$$\left\|\begin{bmatrix}Df(x^{(k)})\\ \sqrt{\lambda^{(k)}}\,I\end{bmatrix}x-\begin{bmatrix}Df(x^{(k)})x^{(k)}-f(x^{(k)})\\ \sqrt{\lambda^{(k)}}\,x^{(k)}\end{bmatrix}\right\|^2 .$$
- Shapes: the stacked matrix is $(m+n)\times n$, and the right-hand side is an $(m+n)$-vector (added step).
- Because $\lambda^{(k)}>0$, the stacked matrix has linearly independent columns even when $Df(x^{(k)})$ does not. So the solution exists and is unique (p. 391).
- Normal equations (p. 391):
$$\big(Df^TDf+\lambda^{(k)}I\big)x^{(k+1)}=Df^T\big(Dfx^{(k)}-f\big)+\lambda^{(k)}x^{(k)}=\big(Df^TDf+\lambda^{(k)}I\big)x^{(k)}-Df^Tf,$$
with $Df,f$ evaluated at $x^{(k)}$. Hence
$$x^{(k+1)}=x^{(k)}-\big(Df(x^{(k)})^TDf(x^{(k)})+\lambda^{(k)}I\big)^{-1}Df(x^{(k)})^Tf(x^{(k)}).\tag{18.12}$$
The inverse always exists (p. 392).
- From (18.12), $x^{(k+1)}=x^{(k)}$ only if $2Df^Tf=0$. So LM repeats itself only when (18.3) holds (p. 392).

> **Intuition note.** The penalty acts like a leash on the step. A short leash keeps us where the straight-line approximation is accurate. It also makes the linear problem always solvable, because the extra block $\sqrt{\lambda}\,I$ supplies independent columns.

**Updating the trust parameter (p. 392).**
- If $\lambda^{(k)}$ is too small, $x^{(k+1)}$ can be far enough away that $\|f(x^{(k+1)})\|^2>\|f(x^{(k)})\|^2$. If it is too large, the step is small, the objective decreases only slightly, and many iterations are needed. We want $\lambda$ in between.
- A simple method: form $x^{(k+1)}$. If the objective decreased, accept and decrease $\lambda$ a bit. Otherwise do not update $x$ and increase $\lambda$ substantially.

**Algorithm 18.3 (LM)** (given $f$, $x^{(1)}$, $\lambda^{(1)}>0$; for $k=1,\dots,k^{\max}$) (p. 392):
1. Form $\hat f(x;x^{(k)})$ as in (18.5).
2. Tentative iterate: minimizer of $\|\hat f(x;x^{(k)})\|^2+\lambda^{(k)}\|x-x^{(k)}\|^2$.
3. If $\|f(x^{(k+1)})\|^2<\|f(x^{(k)})\|^2$, accept and set $\lambda^{(k+1)}=0.8\lambda^{(k)}$. Otherwise set $\lambda^{(k+1)}=2\lambda^{(k)}$ and $x^{(k+1)}=x^{(k)}$.

**Practical points (p. 393).**
- *Stopping criteria:* stop before $k^{\max}$ if the residual $\|f(x^{(k+1)})\|^2$ is small enough, or if the optimality-condition residual $\|2Df(\hat x)^Tf(\hat x)\|$ is small enough. In the second case we can say very little for sure. The point may or may not minimize $\|f(x)\|^2$. So LM is a heuristic, like k-means, and is still widely used.
- *Warm start:* when a sequence of related problems is solved, start at the previous solution. This can greatly reduce iterations. It is common in nonlinear model fitting when a regularization parameter is varied.
- *Multiple runs:* run from several starting points. If the final points agree, our confidence rises, but we cannot be sure. If they differ, use the point with the smallest $\|f(x)\|^2$.
- *Complexity:* step 1 depends on $f$. Step 2 via QR of the stacked matrix costs $2(m+n)n^2$ flops (§15.5). This is of order $mn^2$ when $m$ is of order $n$ or larger. When $m\ll n$, the kernel trick (§15.5) gives $2nm^2$ flops.
- *LM for $n=1$* (minimizing $f(x)^2$):
$$x^{(k+1)}=x^{(k)}-\frac{f'(x^{(k)})}{\lambda^{(k)}+(f'(x^{(k)}))^2}f(x^{(k)}).\tag{18.13}$$
For $\lambda^{(k)}=0$ it equals Newton (18.9). When $f'(x^{(k)})=0$, (18.13) is still defined but Newton is not.

**18.3.1 Examples (pp. 394–396).**
- *Sigmoid.* LM started at $x^{(1)}=1.15$, $\lambda^{(1)}=1$ converges to $x=0$ in around 10 iterations (figure 18.5). Gauss–Newton (Newton) diverged from the same start (p. 394).
- *Equilibrium prices* (p. 394). Demand and supply:
$$D(p)=\exp\big(E^d(\log p-\log p^{nom})+d^{nom}\big),\quad S(p)=\exp\big(E^s(\log p-\log p^{nom})+s^{nom}\big),$$
with $\log,\exp$ applied elementwise. Data: $p^{nom}=(1,1)$, $d^{nom}=(3,1)$, $s^{nom}=(2,2)$,
$$E^d=\begin{bmatrix}-0.5&0.2\\0&-0.5\end{bmatrix},\quad E^s=\begin{bmatrix}0.5&-0.3\\-0.15&0.8\end{bmatrix}.$$
The residual is $f(p)=S(p)-D(p)$. Algorithm 18.3 is started at $p=(3,9)$, $\lambda^{(1)}=1$. Figures 18.6–18.8 show contours, iterates, and $\|f(p^{(k)})\|^2$ with $\lambda^{(k)}$ versus $k$ (pp. 394–396).
- *Location from range measurements* (p. 396). Five points $a_i$ in the plane. The ranges are the distances to the 'true' point $(1,1)$ plus errors. The minimizer of $\|f(x)\|^2$ is $(1.18,0.82)$, close to but not equal to $(1,1)$ because of the noise. Runs use $\lambda^{(1)}=0.1$ from three starts:
  - From $(1.8,3.5)$ and from $(3.0,1.5)$, LM converges to $(1.18,0.82)$.
  - From $(2.2,3.5)$ it converges to the non-optimal point $(2.98,2.12)$, a poor estimate of $(1,1)$.
  - In the first run $\lambda^{(k)}$ increases in iteration 3. In the second run it decreases monotonically. In the third run it increases in iterations 2 and 4.

> **Intuition note.** The range example shows concretely why multiple runs are recommended. The cost surface has more than one dip (figures 18.9, 18.10), and LM can settle in a dip that is not the lowest.

### 18.4 Nonlinear model fitting (pp. 399–400)
- Data: feature $n$-vectors $x^{(i)}$ and scalar outcomes $y^{(i)}$, $i=1,\dots,N$. Here the superscript indexes data, not iterations (p. 399).
- Model: $y\approx\hat f(x;\theta)$, $\theta$ a $p$-vector. In *linear* fitting $\hat f=\theta_1f_1(x)+\dots+\theta_pf_p(x)$ with *basis functions* $f_j$. In nonlinear fitting the dependence on $\theta$ is not linear or affine.
- Choose $\theta$ by minimizing the sum of squared prediction residuals (as in (18.4)). Regularization may be added.
- *Example (figure 18.13).* An exponentially decaying sinusoid $\hat f(x;\theta)=\theta_1e^{\theta_2x}\cos(\theta_3x+\theta_4)$ is fit to $N=60$ points. It is affine in $\theta_1$ but not in $\theta_2,\theta_3,\theta_4$ (pp. 399–400).
- *Orthogonal distance regression.* Take a model linear in the parameters, $\hat f=\theta_1f_1(x)+\dots+\theta_pf_p(x)$. Instead of squared differences between $\hat f(x^{(i)})$ and $y^{(i)}$, use the squared distances from the points $(x^{(i)},y^{(i)})$ to the graph of $\hat f$. This is found by solving
$$\text{minimize}\ \sum_{i=1}^N\big(\hat f(u^{(i)};\theta)-y^{(i)}\big)^2+\sum_{i=1}^N\|u^{(i)}-x^{(i)}\|^2$$
over $\theta_1,\dots,\theta_p$ and $u^{(1)},\dots,u^{(N)}$ (p. 400).
  - So the feature vectors may be modified from $x^{(i)}$ to $u^{(i)}$. This is an *error-in-variables* model, since it allows errors in the regressors.
  - Figure 18.14 shows a cubic polynomial fit to 25 points. Ordinary least squares minimizes the squared *vertical* errors instead.

### 18.5 Nonlinear least squares classification (pp. 401–409)
- *Setup (p. 401).* The Boolean classifier of chapter 14 fits $\tilde f(x)=\theta_1f_1(x)+\dots+\theta_pf_p(x)$ to data with $y^{(i)}\in\{-1,1\}$, by minimizing
$$\sum_{i=1}^N\big(\tilde f(x^{(i)})-y^{(i)}\big)^2\tag{18.14}$$
(plus optional regularization). $\tilde f$ is the *continuous prediction*. The classifier is $\hat f(x)=\mathbf{sign}(\tilde f(x))$, the *Boolean prediction*.
- The sum square error of the Boolean prediction is
$$\sum_{i=1}^N(\hat f(x^{(i)})-y^{(i)})^2=\sum_{i=1}^N\big(\mathbf{sign}(\tilde f(x^{(i)}))-y^{(i)}\big)^2\tag{18.15}$$
It is 4 times the number of training errors. A correct prediction contributes 0. A wrong one has values $+1$ and $-1$, so it contributes $(\pm2)^2=4$ (p. 401).
- (18.15) is what we really want, and (18.14) is a *surrogate*. But LM cannot minimize (18.15), because sign is not differentiable. So replace sign by the sigmoid
$$\phi(u)=\frac{e^u-e^{-u}}{e^u+e^{-u}}\tag{18.16}$$
(figure 18.15), and minimize
$$\sum_{i=1}^N\big(\phi(\tilde f(x^{(i)}))-y^{(i)}\big)^2\tag{18.17}$$
with LM (regularization optional). This is a good approximation for choosing $\theta$ to minimize the number of training errors (p. 401).
- *Loss functions (p. 402).* Each objective has the form $\sum_i\ell(\tilde f(x^{(i)}),y^{(i)})$, with $\ell(u,y)=(u-y)^2$ for (18.14), $(\mathbf{sign}(u)-y)^2$ for (18.15), and $(\phi(u)-y)^2$ for (18.17). All three discourage prediction errors, since their values are higher for $\mathbf{sign}(u)\ne y$. The sign version costs 0 or 4, and the sigmoid version is a smooth approximation of it (figure 18.16, p. 403).

> **Intuition note.** What we care about is the number of mistakes, but that count is a step function with no slope to follow. The sigmoid is a smooth ramp that imitates the step. Then the standard least squares machinery can be used.

**18.5.1 Handwritten digits (MNIST) (pp. 404–411).**
- *Digit zero, linear features.* $\tilde f(x)=x^T\beta+v$, with $x$ the 493-vector of pixel intensities. Solve
$$\text{minimize}\ \sum_{i=1}^N\big(\phi((x^{(i)})^T\beta+v)-y^{(i)}\big)^2+\lambda\|\beta\|^2.\tag{18.18}$$
This $\lambda$ is the regularization parameter, unrelated to the trust parameter $\lambda^{(k)}$ (p. 404).
- At $\lambda=100$, train and test errors are about 0.7%. This is less than half the 1.6% of the chapter 14 least squares classifier with the same features. The explanation given: the objective is closer to what we want (number of errors) than the surrogate (p. 404; figure 18.17).
- Test confusion matrix (Table 18.1, p. 405): 945 true zeros correctly predicted, 35 missed. Of 9020 non-zeros, 40 are predicted zero and 8980 correct. Training: 296 missed zeros and 148 false zeros out of 60000.
- *Convergence (p. 406).* LM takes several tens of iterations to meet its stopping criterion. But the classification errors reach their final values (0.7%) after just a few iterations (figure 18.19). The text calls this very typical in nonlinear data fitting: well before convergence the parameters are as good, judged by test error, as at convergence.
- *Feature engineering (p. 406).* Adding the 5000 random features of chapter 14 gives zero training error for small $\lambda$. At $\lambda=1000$ the test error is 0.24% (Table 18.2: 13 + 11 errors in 10000; p. 407). Starting LM from $\beta=0$, $v=0$ makes the first iteration's coefficients those of the linear least squares classifier. Training error is exactly zero at iteration 5, and test error is almost at its final value after one iteration (figure 18.22).
- *Multi-class (p. 409).* For each digit $k$ compute a Boolean classifier $\tilde f_k(x)=x^T\beta_k+v_k$ by solving (18.18), with the same $\lambda$ for all ten. Combine:
$$\hat f(x)=\operatorname*{argmax}_{k=1,\dots,10}\,(x^T\beta_k+v_k).$$
At $\lambda=1$ the test error is 7.6%, down from 13.9% for the least squares method with the same features (Table 18.3, p. 410).
- With the 5000 random features, train and test errors are 0.02% and 2% (λ=1000; Table 18.4, p. 411). The text says this matches human performance, and that further or more sophisticated feature engineering can bring test performance well below human level (p. 409).

### Exercises (pp. 412–417)
Eight exercises ask for LM updates and implementations for specific problems. They are listed under "Exercises worth doing" below.

## Toy example (ours, not from the text)
Take $n=m=1$ and $f(x)=x^2-4$, so $f'(x)=2x$. The zeros are $x=\pm2$. Start at $x^{(1)}=4$: $f=12$, $f'=8$.
- **Gauss–Newton = Newton (18.9):** $x^{(2)}=4-12/8=2.5$. Check: $\|f(2.5)\|^2=(6.25-4)^2=5.0625<144=\|f(4)\|^2$.
- **LM (18.13) with $\lambda^{(1)}=8$:** step $=\dfrac{8\cdot12}{8+64}=\dfrac{96}{72}=\dfrac43$, so $x^{(2)}=4-\tfrac43=\tfrac83\approx2.667$. Check: $f(8/3)=\tfrac{64}{9}-4=\tfrac{28}{9}$, so $\|f\|^2=\tfrac{784}{81}\approx9.68<144$. Accept, and set $\lambda^{(2)}=0.8\cdot8=6.4$. The LM step is shorter than the Newton step because $\lambda>0$ shrinks it.
- **Optimality condition at a non-solution:** at $x=0$, $f=-4$ and $Df=0$, so $2Df^Tf=0$ and (18.3) holds. But $\|f(0)\|^2=16$, while $\|f(1)\|^2=(1-4)^2=9<16$. So (18.3) holds at a point that is not a minimizer. Newton (18.9) is undefined there, since $f'(0)=0$. For LM, (18.13) gives step $0$: it stays at $0$, consistent with "stops only when (18.3) holds".

## Concepts
- [[nonlinear-least-squares]] (new) — minimize $\|f(x)\|^2$ for a possibly non-affine $f:\mathbf R^n\to\mathbf R^m$ (p. 382)
- [[least-squares]] — the linear special case, solved at each Gauss–Newton/LM step (p. 382)
- [[jacobian-matrix]] (new) — the $m\times n$ matrix $Df(x)$ of partial derivatives of $f$; gradient of $\|f\|^2$ is $2Df^Tf$ (p. 383)
- [[optimality-condition-nls]] (new) — $2Df(\hat x)^Tf(\hat x)=0$, necessary but not sufficient (p. 383)
- [[heuristic-algorithm]] (new) — an algorithm that often works but does not always find the best point; k-means and LM are examples (p. 383)
- [[gauss-newton-algorithm]] (new) — iterate by minimizing the affine approximation's squared norm, (18.6) (p. 387)
- [[newton-algorithm]] (new) — the case $m=n$: $x^{(k+1)}=x^{(k)}-Df^{-1}f$ (p. 388)
- [[levenberg-marquardt]] (new) — Gauss–Newton with a trust penalty $\lambda\|x-x^{(k)}\|^2$; update (18.12) (p. 391)
- [[trust-parameter]] (new) — $\lambda^{(k)}$: large means small steps; raised if the step fails, lowered if it succeeds (p. 391)
- [[linear-independence]] — needed for the Gauss–Newton step; always achieved in LM by the $\sqrt\lambda I$ block (p. 391)
- [[gram-schmidt-and-qr]] — used to cost an LM step at $2(m+n)n^2$ flops (p. 393)
- [[warm-start]] (new) — start at the solution of a related earlier problem (p. 393)
- [[sigmoid-function]] (new) — $\phi(u)=(e^u-e^{-u})/(e^u+e^{-u})$; smooth replacement for sign (p. 401)
- [[loss-function]] (new) — $\ell(u,y)$ rating the continuous prediction $u$ against outcome $y$ (p. 402)
- [[orthogonal-distance-regression]] (new) — fit by minimizing distances from points to the graph, also moving the features (p. 400)

## Canonical instances
- [[equilibrium-prices]] — $f(p)=S(p)-D(p)=0$; solved by LM in a two-commodity example (pp. 384, 394)
- [[nash-equilibrium]] — necessary condition $\partial R_i/\partial x_i=0$ is a square nonlinear system (p. 385)
- [[location-from-ranges]] — least squares on range residuals; one of three LM starts ends at a non-optimal point (p. 386, p. 396)
- [[sigmoid-newton-divergence]] — Newton converges from 0.95 and diverges from 1.15; LM converges from 1.15 (pp. 390, 394)
- [[exponentially-decaying-sinusoid-fit]] — nonlinear model fit with four parameters, $N=60$ (p. 399)
- [[mnist-nonlinear-ls-classifier]] — sigmoid-surrogate classifier: digit zero 0.7% (λ=100, linear features), ten digits 7.6% (p. 404, p. 409)

## Bridges (candidates)
- [same-math] LM step as regularized least squares ↔ linear-algebra: ridge/Tikhonov-type regularized least squares — each step solves $\min\|Ax-b\|^2+\lambda\|x-x^{(k)}\|^2$ literally.
- [structural-analogy] Newton/Gauss–Newton iteration ↔ linear-algebra: repeated linearization — nonlinear problem solved as a sequence of linear least squares problems.
- [structural-analogy] sigmoid surrogate for the sign/0–1 loss ↔ machine learning: replacing a non-differentiable error count by a smooth loss.
- [structural-analogy] Nash equilibrium conditions ↔ game theory: stable choices are zeros of a residual system, solvable with Newton-type methods.
- [metaphor] Trust parameter ↔ cautious steps in an uncertain terrain: take smaller steps when the local map has proved unreliable.

## Questions this raises
- When does $2Df^Tf=0$ at a non-solution correspond to a local minimum, a maximum, or a saddle, and can an algorithm tell the difference?
- Is the 0.8/2 rule for $\lambda$ the best choice, and how do other trust-region update rules compare?
- If a classifier's error stabilizes after a few LM iterations, how should one decide when to stop?
- How do we choose the number of random features and $\lambda$ without overfitting (training error zero but test error 0.24%)?

## Exercises worth doing
- Ex. 18.1 (p. 412) — derive the LM update (18.13) for $f(x)=xe^x-u$ and implement it to compute the Lambert W function — difficulty: easy
- Ex. 18.3 (p. 412) — show $Df(x)=\mathbf{diag}(d)A$ for residuals $\phi_i(a_i^Tx-b_i)$, so each step is a weighted least squares problem — difficulty: medium
- Ex. 18.5 (p. 413) — find the equilibrium position of a mass held by two cables with LM, using the starting-point caveat in the text — difficulty: medium
- Ex. 18.6 (p. 413) — derive gradient and derivative matrix for a 13-parameter two-layer neural network and fit $x_1x_2$; compare with linear regression — difficulty: hard
- Ex. 18.7 (p. 415) — robot arm joint angles by LM; explain what happens when the target is out of reach — difficulty: medium
- Ex. 18.8 (p. 416) — fit an ellipse by minimizing squared distances, with extra variables $t^{(i)}$ — difficulty: hard

## Reading notes
- Printed page = pdf page − 10 (pdf 391 is printed 381). The unit runs through printed p. 417; printed p. 418 (pdf 428) is blank.
- Possible slip, p. 396: the text says "$x^{(3)}=x^{(4)}$ in figure 18.12", but figure 18.12 plots cost and $\lambda^{(k)}$ against $k$. The iterates themselves appear in figure 18.11; figure 18.12 shows equal cost values at $k=3$ and $k=4$ for the blue run, which the sentence presumably refers to.
- p. 393: the stopping criterion is written with $\hat x$ ($\|2Df(\hat x)^Tf(\hat x)\|$). Presumably the current iterate is meant. Also, on p. 392, the expression "$\|f(x^{(k)}\|^2$" is missing a parenthesis.
- p. 383: "It is a not a sufficient condition" (a typo for "It is not a sufficient condition"). On p. 410, Table 18.3's caption has a stray period.
- p. 406: the text says LM takes "several tens of iterations" to converge. Figures 18.19 and 18.22 show only iterations up to 10.
- p. 408 (figure 18.22): the training-error curve ends at iteration 4. The text says training error is exactly zero at iteration 5. Zero cannot be shown on a log axis.
- The figures give only approximate values (e.g., the equilibrium price location, $\lambda$ curves); I did not read exact coordinates from them.
- Exercise 18.2 (not listed above) uses $r^{(0)}$ for the starting value, unlike the $x^{(1)}$ convention in the text.
