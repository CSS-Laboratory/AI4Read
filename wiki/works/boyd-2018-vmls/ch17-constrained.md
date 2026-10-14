---
id: boyd-2018-vmls/ch17-constrained
work: boyd-2018-vmls
unit: "Chapter 17 — Constrained least squares applications"
pages: 357-380
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Constrained least squares applications

## L0 — One line
Portfolio selection, optimal control and state estimation can each be written as a linearly constrained least squares problem; in control and estimation this is done by stacking the states and inputs (or noises) into one big vector.

## L1 — The gist (≤ 120 words)
Chapter 17 asks how real decision and estimation problems fit the constrained least squares form of chapter 16. Three applications are shown. (1) Portfolio optimization: minimize risk for a required return. (2) Linear quadratic control: choose inputs so the output and inputs stay small, with a given start state and sometimes a required final state. (3) Linear quadratic state estimation: guess hidden states from noisy measurements. In control and estimation the states and inputs (or noises) are stacked into one vector. Trade-off parameters weight objectives; $\lambda$ (portfolio regularization, estimation) is chosen by back-testing or validation. Sparsity makes the control and estimation problems cost only linear time in the horizon $T$.

**Prerequisites:** least squares and the KKT system of constrained least squares (ch. 16); stacking and block matrices; mean, standard deviation, RMS; linear dynamical systems $x_{t+1}=Ax_t+Bu_t$; train/test validation.

## L2 — Key ideas
- **Portfolio return and risk are matrix-vector quantities.** With return matrix $R$ ($T\times n$) and weights $w$, the return series is $r=Rw$. Return is $\mathbf{avg}(r)$ and risk is $\mathbf{std}(r)$ (p. 358–359).
- **Minimum risk for fixed return is a constrained least squares problem (17.2).** The two linear constraints are $\mathbf 1^Tw=1$ and $\mu^Tw=\rho$. The solution is the KKT system (17.3) (p. 360).
- **The usefulness of the weights rests on "future returns are similar to past returns" (17.4).** It need not hold. So weights are validated by back-testing on a different period, and results can disagree more than in ordinary data fitting (p. 361–363).
- **Two-fund theorem.** Pareto optimal weights are $w=w^0+\rho v$, a line in weight space. Pareto optimal means the best risk–return trade-off. Every Pareto optimal portfolio is an affine combination (weights summing to 1) of any two different ones (p. 365–366).
- **Linear quadratic control stacks states and inputs into $z$.** Dynamics and initial/final conditions become $\tilde Cz=\tilde d$, and the objective becomes $\|\tilde Az-\tilde b\|^2$. Sparsity (most matrix entries are zero) gives cost linear in the number of time steps $T$ (p. 367–368).
- **State feedback gain $K$ comes from the control problem.** with $x^{\rm des}=0$, $u_1$ is linear in $x_1$, so $K$ is found from $n$ solves with $x^{\rm init}=e_1,\dots,e_n$ (p. 371–372).
- **State estimation has the same structure with a different meaning.** The inputs become unknown process noise (we must guess them), and $\lambda$ trades measurement fit against small noise. Control and estimation are closely related ("duality") (p. 373–374).
- **Held-out measurements validate $\lambda$ in estimation.** Treat some measurements as missing and compare predictions with them (p. 375–377).

## L3 — Walkthrough

Page offset: printed = pdf − 10.

### 17.1 Portfolio optimization (p. 357–366)

**17.1.1 Portfolio risk and return.**

*Weights.* An allocation $n$-vector $w$ satisfies $\mathbf 1^Tw=1$. With total amount $V$, the amount in asset $j$ is $Vw_j$. A negative entry is a short position of $|Vw_j|$ dollars on asset $j$ (p. 357). $w=e_j$ puts everything in asset $j$. For $w=(-0.2,0,1.2)$ we short asset 1 by one fifth of the total and invest the proceeds in asset 3 (p. 357–358).

*Leverage.* $L=|w_1|+\dots+|w_n|$ (p. 358).
- For a long-only portfolio (all $w_j\ge0$), $L=1$. If some entries are negative, $L>1$.
- Leverage 5 means \$3 long and \$2 short per \$1 of portfolio value (p. 358).

*Returns.* $R$ is $T\times n$. $R_{tj}$ is the fractional return of asset $j$ in period $t$. Column $j$ is the time series of asset $j$. Row $t$ is written $\tilde r_t^T$.
- Example: $R_{61}=0.02$ means asset 1 gained 2% in period 6.
- A risk-free asset $n$ has constant return $\mu^{\rm rf}$, so the last column of $R$ is $\mu^{\rm rf}\mathbf 1$ (p. 358).

*Value of the portfolio.* Invest $V_t$ at the start of period $t$. At the end,
$$V_{t+1}=\sum_{j=1}^n V_tw_j(1+R_{tj})=V_t(1+\tilde r_t^Tw).$$
Portfolio value is assumed positive; otherwise the portfolio has "gone bust" (p. 358).
- The fractional return in period $t$ is $(V_{t+1}-V_t)/V_t=\tilde r_t^Tw$.
- Re-balancing means buying and selling each period so the dollar fractions are again $w$ (p. 358).
- In matrix form, $r=Rw$ is the $T$-vector of portfolio returns. With $w=e_n$ and asset $n$ risk-free, $r=\mu^{\rm rf}\mathbf 1$ (p. 358).

*Compounding.*
$$V_t=V_1(1+r_1)(1+r_2)\cdots(1+r_{t-1}).\tag{17.1}$$
- For $w=e_n$ with a risk-free last asset, $V_t=V_1(1+\mu^{\rm rf})^{t-1}$ (compounded interest) (p. 359).
- If returns are small and $T$ is not too big, expand the product. Terms with two or more returns are neglected. This gives $V_t\approx V_1+V_1(r_1+\dots+r_{t-1})$, and for $t=T+1$,
$$V_{T+1}\approx V_1+T\,\mathbf{avg}(r)V_1.$$
- So high $\mathbf{avg}(r)$ is sought (p. 359).

*Return and risk.* Mean return is $\mathbf{avg}(r)$. Risk is $\mathbf{std}(r)$. With $P$ periods per year, the annualized return and risk are $P\,\mathbf{avg}(r)$ and $\sqrt P\,\mathbf{std}(r)$.
- Daily data: $P\approx250$, so the factors are $250$ and $15.81$.
- Example: daily return 0.0005 and risk 0.005 give 12.5% and 7.9% per year.
- The $\sqrt P$ comes from assuming period-to-period fluctuations are random and independent (p. 359).

**17.1.2 Portfolio optimization (p. 360–361).**

There are two objectives, return and risk, so there is a family of trade-offs.
- Weights that minimize risk for a given return (or maximize return for a given risk) are **Pareto optimal**.
- $w=e_n$ (risk-free) has zero risk, the smallest possible, and return $\mu^{\rm rf}$. Other choices can give higher return with higher risk (p. 360).

*Fix the return at $\rho$.* Let $\mu=R^T\mathbf 1/T$ be the vector of average asset returns. Then $\mathbf{avg}(r)=(1/T)\mathbf 1^T(Rw)=\mu^Tw=\rho$, one linear equation in $w$. Given this,
$$\mathbf{std}(r)^2=(1/T)\|r-\mathbf{avg}(r)\mathbf 1\|^2=(1/T)\|r-\rho\mathbf 1\|^2.$$
So we solve
$$\text{minimize }\|Rw-\rho\mathbf 1\|^2\quad\text{subject to}\quad \begin{bmatrix}\mathbf 1^T\\ \mu^T\end{bmatrix}w=\begin{bmatrix}1\\ \rho\end{bmatrix}.\tag{17.2}$$
The factor $1/T$ is dropped; it does not change the solution (p. 360).

*Solution* (KKT system, with Lagrange multipliers $z_1,z_2$ for the two constraints):
$$\begin{bmatrix}w\\z_1\\z_2\end{bmatrix}=\begin{bmatrix}2R^TR&\mathbf 1&\mu\\ \mathbf 1^T&0&0\\ \mu^T&0&0\end{bmatrix}^{-1}\begin{bmatrix}2\rho T\mu\\1\\ \rho\end{bmatrix}.\tag{17.3}$$
(added step: the top block of the right-hand side is $2\rho R^T\mathbf 1=2\rho T\mu$, because $R^T\mathbf 1=T\mu$.)

Historical note: Markowitz used a statistical model of returns. Here realized returns are used; exercise 17.2 gives a closer formulation (p. 360).

*Intuition note.* Once the return is fixed at $\rho$, squared risk is $1/T$ times the squared distance of $r$ from the constant series $\rho\mathbf 1$. So "least risk for a given return" is least squares with two linear equality constraints. The weights that come out are an ordinary KKT solve.

**The big assumption (p. 361).** Problem (17.2) uses the returns of the very periods it is applied to. If future returns were known, huge positions on the winners would give any return. We do not know them. So $w$ is computed from realized returns in $t=1,\dots,T$ and used later under the assumption:
$$\text{Future asset returns are similar to past returns.}\tag{17.4}$$
- This need not hold, e.g. in a "market shift"; past performance is no guarantee (p. 361).
- As in model fitting (ch. 13–14), the weights can be validated: compute them on a training period and check a testing period. In investing this is called **back-testing**.
- Assumption (17.4) holds less well than "future data looks like past data" in data fitting. So less agreement between train and test performance is expected, especially for short test periods such as 100 (p. 361).

**17.1.3 Example (p. 362–364).** Data: 19 stocks, 2000 daily returns (8 years), plus a risk-free asset with 1% annual return. So $R$ is $2000\times20$. The asset points in figure 17.1 are $(\sqrt{250}\,\mathbf{std}(Re_i),\,250\,\mathbf{avg}(Re_i))$ (p. 362). Table 17.1 (annualized):

| Portfolio | Return train | Return test | Risk train | Risk test | Leverage |
|---|---|---|---|---|---|
| Risk-free | 0.01 | 0.01 | 0.00 | 0.00 | 1.00 |
| 10% | 0.10 | 0.08 | 0.09 | 0.07 | 1.96 |
| 20% | 0.20 | 0.15 | 0.18 | 0.15 | 3.03 |
| 40% | 0.40 | 0.30 | 0.38 | 0.31 | 5.48 |
| $1/n$ | 0.10 | 0.21 | 0.23 | 0.13 | 1.00 |

(p. 363.)
- Higher required return means higher leverage.
- For the three Pareto portfolios, test returns are lower than training returns. The $1/n$ portfolio has test return 0.21 against 0.10 in training.
- Figure 17.2 shows total value over the 2000 training days. Figure 17.3 shows value over a 500-day test period (p. 363–364).

**17.1.4 Variations (p. 364–365).**
- *Regularization.* The weights can over-fit: very good on past returns, poor on new ones. Add $\lambda(\sigma_1^2w_1^2+\dots+\sigma_{n-1}^2w_{n-1}^2)$ to the objective, with $\sigma_i=\mathbf{std}(Re_i)$ and $\lambda>0$. The risk-free weight $w_n$ is not penalized, so risky assets are penalized more than less risky ones. $\lambda$ is chosen by back-testing (p. 364).
- *Time-varying weights.* Markets shift, so weights may be updated. In the extreme version, the weights for each period come from solving the problem over the preceding $M$ periods; $M$ is chosen by back-testing (p. 365).
- *Turnover term.* Add $\kappa\|w^{\rm curr}-w\|^2$ with $\kappa>0$ to keep the new allocation near the current one. This limits turnover, i.e. excessive buying and selling, which brings trading costs not in the simple model. $\kappa$ is chosen by back-testing (p. 365).

**17.1.5 Two-fund theorem (p. 365–366).** Split the right-hand side of (17.3) into a part not involving $\rho$ and a part multiplying $\rho$:
$$\begin{bmatrix}w\\z_1\\z_2\end{bmatrix}=K^{-1}\begin{bmatrix}0\\1\\0\end{bmatrix}+\rho\,K^{-1}\begin{bmatrix}2T\mu\\0\\1\end{bmatrix},\qquad K=\begin{bmatrix}2R^TR&\mathbf 1&\mu\\ \mathbf 1^T&0&0\\ \mu^T&0&0\end{bmatrix}.$$
(I write $K$ for the matrix only here; the book writes it out.) Taking the first $n$ components,
$$w=w^0+\rho v,\tag{17.5}$$
where $w^0$ and $v$ are the first $n$ components of the two $(n+2)$-vectors above. Consequences:
- Pareto optimal portfolios form a **line** in weight space, parametrized by $\rho$. $w^0$ is a point on it, and $v$ is its direction, with $\mathbf 1^Tv=0$.
- We do not solve (17.3) for each $\rho$. Factor the matrix once, do two solves to get $w^0$ and $v$, then form $w^0+\rho v$.
- Any point on a line is an affine combination of two different points on it. So every Pareto optimal portfolio is an affine combination of any two different Pareto optimal portfolios: the **two-fund theorem** ("fund" means portfolio) (p. 365).

With a risk-free last asset, $w=e_n$ is Pareto optimal. Take $w^2$, the one with return $2\mu^{\rm rf}$ (any return other than $\mu^{\rm rf}$ would do). Then
$$w=(1-\theta)e_n+\theta w^2,\qquad \theta=\rho/\mu^{\rm rf}-1.$$
(added step: the return is $(1-\theta)\mu^{\rm rf}+2\theta\mu^{\rm rf}=(1+\theta)\mu^{\rm rf}=\rho$.) (p. 366)

*Intuition note.* The right-hand side of the KKT system is affine in $\rho$ (a constant part plus $\rho$ times a fixed part), so the solution is too. Hence the Pareto optimal portfolios sit on a straight line, and two of them are enough to generate all the others.

### 17.2 Linear quadratic control (p. 366–372)

**Setup.** A time-varying linear system has state $n$-vector $x_t$, input $m$-vector $u_t$, and output $p$-vector $y_t$:
$$x_{t+1}=A_tx_t+B_tu_t,\qquad y_t=C_tx_t,\quad t=1,2,\dots\tag{17.6, 17.7}$$
Usually $m\le n$ and $p\le n$ (p. 366).
- The input is what we can manipulate (e.g. control surface deflection or engine thrust). State, input and output typically represent deviations from a desired operating condition, so we want them small (p. 366).
- *Linear quadratic control* chooses the input and state sequences over $t=1,\dots,T$ to minimize a sum of squares, subject to the dynamics and further linear equality constraints. "Linear" refers to the dynamics, "quadratic" to the objective (p. 366).
- Constraints: an initial state $x_1=x^{\rm init}$ (most problems) and sometimes a final state $x_T=x^{\rm des}$.

**Objective:** $J=J_{\rm output}+\rho J_{\rm input}$, with
$$J_{\rm output}=\|y_1\|^2+\dots+\|y_T\|^2=\|C_1x_1\|^2+\dots+\|C_Tx_T\|^2,\qquad J_{\rm input}=\|u_1\|^2+\dots+\|u_{T-1}\|^2,$$
where $\rho>0$ weights the input objective against the output objective (p. 366).

The problem is
$$\begin{array}{ll}\text{minimize}& J_{\rm output}+\rho J_{\rm input}\\ \text{subject to}& x_{t+1}=A_tx_t+B_tu_t,\ t=1,\dots,T-1\\ & x_1=x^{\rm init},\ x_T=x^{\rm des},\end{array}\tag{17.8}$$
with variables $x_1,\dots,x_T,u_1,\dots,u_{T-1}$ (p. 367).

**Stacking.** $z=(x_1,\dots,x_T,u_1,\dots,u_{T-1})$ has dimension $Tn+(T-1)m$ (p. 367).
- Objective: $\|\tilde Az-\tilde b\|^2$ with $\tilde b=0$. $\tilde A$ is block diagonal on the state part, with blocks $C_1,\dots,C_T$, followed by $\sqrt\rho I$ blocks of size $m$ on the input part.
- Constraints: $\tilde Cz=\tilde d$. The first $T-1$ block rows are $[A_t\ \ -I]$ in the columns of $x_t,x_{t+1}$, plus $B_t$ in the column of $u_t$, with right-hand side $0$. Two more rows give $I\cdot x_1=x^{\rm init}$ and $I\cdot x_T=x^{\rm des}$.
- So $\tilde d=(0,\dots,0,x^{\rm init},x^{\rm des})$.

$$\text{minimize }\|\tilde Az-\tilde b\|^2\quad\text{subject to}\quad\tilde Cz=\tilde d.\tag{17.9}$$
The solution $\hat z$ is linear in $\tilde b$ and $\tilde d$. Since $\tilde b=0$ here, it is linear in $x^{\rm init}$ and $x^{\rm des}$ (p. 367).

**Complexity (p. 368).** Dimensions: $\tilde n=Tn+(T-1)m$, $\tilde m=Tp+(T-1)m$, $\tilde p=(T-1)n+2n$.
- Standard methods (§16.2) cost about $(\tilde p+\tilde m)\tilde n^2\approx T^3(m+p+n)(m+n)^2$ flops.
- $\tilde A$ and $\tilde C$ are very sparse. Exploiting this gives order $T(m+p+n)(m+n)^2$ flops, linear in $T$.

**17.2.1 Example (p. 368–370).** A time-invariant system with
$$A=\begin{bmatrix}0.855&1.161&0.667\\0.015&1.073&0.053\\-0.084&0.059&1.022\end{bmatrix},\ B=\begin{bmatrix}-0.076\\-0.139\\0.342\end{bmatrix},\ C=\begin{bmatrix}0.218&-3.597&-1.683\end{bmatrix},$$
$x^{\rm init}=(0.496,-0.745,1.394)$, $x^{\rm des}=0$, $T=100$. Input and output are scalars (p. 368).
- Open-loop output (zero input): $y_t=CA^{t-1}x^{\rm init}$ (figure 17.4).
- Varying $\rho$ and solving (17.9) traces the trade-off curve of $J_{\rm input}$ against $J_{\rm output}$ (figure 17.5), with $\rho=0.05,0.2,1$ marked.
- Increasing $\rho$ decreases $J_{\rm input}$ at the cost of increasing $J_{\rm output}$. In figure 17.6, larger $\rho$ gives a smaller input and a larger output (p. 368–370).

**17.2.2 Variations (p. 368, 371).**
- *Tracking.* Replace $y_t$ by $y_t-y_t^{\rm des}$. Then $J_{\rm output}$ is the tracking error. Decreasing $\rho$ gives better tracking at the cost of a larger input. This uses the same $\tilde A,\tilde C,\tilde d$, and a nonzero $\tilde b$ that contains $y_t^{\rm des}$ (p. 368).
- *Time-weighted objective.* $J_{\rm output}=w_1\|y_1\|^2+\dots+w_T\|y_T\|^2$ with positive $w_t$. Exponential weighting is $w_t=\theta^t$: for $\theta>1$ later outputs count more, for $\theta<1$ earlier ones do ($\theta$ is then a discount or forgetting factor) (p. 371).
- *Way-point constraints.* $y_\tau=y^{\rm wp}$ at a given time $\tau$. This is a linear equality constraint on $z$ (p. 371).

**17.2.3 Linear state feedback control (p. 371–372).** Instead of planning inputs for a fixed horizon, apply $u_t=Kx_t$ with a state feedback gain matrix $K$ ($m\times n$). This is very widely used in practice, especially when there is no fixed time at which the state must reach a target; we want $x_t,u_t$ small and converging to zero. $K$ can be found ahead of time, and operation needs only one matrix-vector multiply per step (p. 371).

*Finding $K$ from (17.8).* Let $\hat z$ solve (17.8) with $x^{\rm des}=0$.
1. $\hat z$ is linear in $x^{\rm init}=x_1$.
2. $\hat u_1$ is a subvector of $\hat z$, so $\hat u_1=Kx_1$ for some $m\times n$ matrix $K$.
3. The columns of $K$ come from solving (17.8) with $x^{\rm init}=e_1,\dots,e_n$: factor once, then do $n$ solves (p. 371).

This generally gives a good gain. Under it the first input equals the LQ input; for $t>1$ they differ. The author notes, without proof, that $K$ found this way does not depend much on $T$ once $T$ is large enough (p. 372).

*Example.* For §17.2.1 with $\rho=1$: $K=[\,0.308\ \ -2.659\ \ -1.446\,]$. In figure 17.7, LQ control achieves $y_T=0$ exactly. State feedback makes $y_T$ small but not zero (p. 372).

*Intuition note.* When the target is $x^{\rm des}=0$, the first input of the optimal plan depends linearly on the initial state. Reading off that linear map gives a fixed rule $u=Kx$, which the book says generally is a good gain (the later inputs differ from the LQ inputs).

### 17.3 Linear quadratic state estimation (p. 372–377)

**Model.**
$$x_{t+1}=A_tx_t+B_tw_t,\qquad y_t=C_tx_t+v_t,\quad t=1,2,\dots\tag{17.10}$$
$x_t$ is the state ($n$-vector). $y_t$ is the measurement ($p$-vector). $w_t$ is the input or process noise ($m$-vector). $v_t$ is the measurement noise or residual ($p$-vector) (p. 372).
- We know $A_t,B_t,C_t$ and $y_1,\dots,y_T$, but not the noises. We want to estimate $x_1,\dots,x_T$. Applications include guidance and navigation such as GPS (p. 372–373).
- We estimate states and process noises that satisfy the dynamics. A guessed state sequence implies $v_t=y_t-C_tx_t$.
- Fundamental assumption: process and measurement noises are small, or at least not too large (p. 373).

**Objectives.**
$$J_{\rm meas}=\|v_1\|^2+\dots+\|v_T\|^2=\|C_1x_1-y_1\|^2+\dots+\|C_Tx_T-y_T\|^2,\qquad J_{\rm proc}=\|w_1\|^2+\dots+\|w_{T-1}\|^2.$$
Small $J_{\rm meas}$ means the guess is consistent with the data. Small $J_{\rm proc}$ matches the prior that process noise is small (p. 373).

**Estimation problem.**
$$\text{minimize }J_{\rm meas}+\lambda J_{\rm proc}\quad\text{subject to}\quad x_{t+1}=A_tx_t+B_tw_t,\ t=1,\dots,T-1,\tag{17.11}$$
with $\lambda>0$. Roughly, small $\lambda$ means we trust the measurements more; large $\lambda$ means we trust them less and prefer a trajectory consistent with the dynamics with small process noise (p. 373).

**Estimation versus control (p. 373).** The math is very close but the meaning differs.
- In control we choose the inputs and thereby affect the state.
- In estimation the "inputs" (process noise) are unknown. We passively observe outputs and try to deduce the state.
- The close connection is sometimes called control/estimation duality.

**Constrained least squares form (p. 374).** Stack $z=(x_1,\dots,x_T,w_1,\dots,w_{T-1})$.
- Objective $\|\tilde Az-\tilde b\|^2$: $\tilde A$ has blocks $C_1,\dots,C_T$ on the state part and $\sqrt\lambda I$ blocks on the noise part.
- $\tilde b=(y_1,\dots,y_T,0,\dots,0)$.
- Constraints $\tilde Cz=\tilde d$ with $\tilde d=0$ and rows $[A_t\ \ -I \,|\, B_t]$, as in control but without the initial/final rows.
- Dimensions: $\tilde n=Tn+(T-1)m$, $\tilde m=Tp+(T-1)m$, $\tilde p=(T-1)n$.
- Cost: order $T^3(m+p+n)(m+n)^2$ naively, and $T(m+p+n)(m+n)^2$ with sparsity.

The problem was formulated around 1960 by Rudolf Kalman and others in a statistical framework. A particular recursive algorithm for it became known as Kalman filtering; Kalman received the Kyoto Prize in 1985 (p. 374).

**17.3.1 Example (p. 374–375).** Here $n=4$, $p=2$, $m=2$, $T=100$, with
$$A=\begin{bmatrix}1&0&1&0\\0&1&0&1\\0&0&1&0\\0&0&0&1\end{bmatrix},\ B=\begin{bmatrix}0&0\\0&0\\1&0\\0&1\end{bmatrix},\ C=\begin{bmatrix}1&0&0&0\\0&1&0&0\end{bmatrix}.$$
- This models a mass moving in 2-D. Components 1–2 of $x_t$ are position; 3–4 are velocity. $w_t$ acts like a force by adding to the velocity.
- $Cx_t$ is the true position. $y_t=Cx_t+v_t$ is a noisy measurement (p. 375).
- In figure 17.8, $\lambda=1$ is too small: the estimate follows the measurement noise. $\lambda=10^5$ is too large: the estimate is very smooth but its imputed measurement noise is too high. $\lambda=10^3$ is plotted too. Here the true trajectory is known, so choosing $\lambda$ is easy (p. 375).

**17.3.2 Variations (p. 375).**
- *Known initial state:* add the constraint $x_1=x_1^{\rm known}$.
- *Missing measurements:* $y_t$ is known only for $t\in\mathcal T$. Either replace $\sum_{t=1}^T\|v_t\|^2$ by $\sum_{t\in\mathcal T}\|v_t\|^2$, or treat missing $y_t$ as extra variables. The author says both lead to the same state estimate. The missing values can be estimated by $\hat y_t=C_t\hat x_t$ for $t\notin\mathcal T$ (assuming $v_t=0$).

**17.3.3 Validation (p. 375–377).** Hold back some measurements (say 20%), run the estimation as if they were missing, and compare predictions $\hat y_t$ with the actual values. Choose $\lambda$ that approximately minimizes this test prediction error (p. 375).

*Example.* Remove 20 of the 100 points at random, with $J_{\rm meas}=\sum_{t\in\mathcal T}\|Cx_t-y_t\|^2$. The RMS errors are
$$E_{\rm train}=\frac1{\sqrt{80p}}\Big(\sum_{t\in\mathcal T}\|C\hat x_t-y_t\|^2\Big)^{1/2},\qquad E_{\rm test}=\frac1{\sqrt{20p}}\Big(\sum_{t\notin\mathcal T}\|C\hat x_t-y_t\|^2\Big)^{1/2}.$$
In figure 17.9, for $\lambda<100$ or so the test error substantially exceeds the train error (over-fit). A $\lambda$ around $10^3$ is a good choice (p. 377).

*Intuition note.* Hidden data are what an estimator must predict, so withholding some measurements gives an honest test. Too small a $\lambda$ follows the measurement noise (over-fit); too large a $\lambda$ gives a very smooth estimate that trusts the measurements too little.

## Toy example (our own)
Scalar control: $x_{t+1}=x_t+u_t$ ($A=B=C=1$), $T=3$, $x_1=1$, $x_3=0$, parameter $\rho$.

*Stacking.* $z=(x_1,x_2,x_3,u_1,u_2)$, so $\tilde n=Tn+(T-1)m=3+2=5$. Rows of $\tilde A z$: $(x_1,x_2,x_3,\sqrt\rho u_1,\sqrt\rho u_2)$, with $\tilde b=0$. Constraints (form $A_tx_t-x_{t+1}+B_tu_t=0$):
- $x_1-x_2+u_1=0$
- $x_2-x_3+u_2=0$
- $x_1=1$
- $x_3=0$

That is $\tilde p=(T-1)n+2n=4$ rows.

*Solve by hand.* Let $a=x_2$. Then $u_1=a-1$, and $u_2=-a$ because $x_3=a+u_2=0$.
$$J=1+a^2+0+\rho\big((a-1)^2+a^2\big).$$
Set the derivative to zero: $2a+\rho(2(a-1)+2a)=0$, so $a(1+2\rho)=\rho$, i.e. $a=\rho/(1+2\rho)$.

For $\rho=1$: $a=1/3$, $u=(-2/3,-1/3)$, $J_{\rm input}=4/9+1/9=5/9$, $J_{\rm output}=1+1/9+0=10/9$.

| $\rho$ | $a$ | $J_{\rm input}$ | $J_{\rm output}$ |
|---|---|---|---|
| $\to0$ | 0 | 1 | 1 |
| 1 | 1/3 | 5/9 ≈ 0.556 | 10/9 ≈ 1.111 |
| large | $\to 1/2$ | $\to 1/2$ | $\to 5/4$ |

As in the chapter, raising $\rho$ lowers $J_{\rm input}$ and raises $J_{\rm output}$.

## Concepts
- [[least-squares]] — minimize $\|Ax-b\|^2$; here it is the base of every application (p. 360, 367, 373)
- [[constrained-least-squares]] (new) — least squares with linear equality constraints, solved via a KKT system; every problem in this chapter is of this form (p. 360, 367)
- [[portfolio-optimization]] (new) — choose weights $w$ with $\mathbf 1^Tw=1$ to minimize risk for a required return (p. 357, 360)
- [[pareto-optimal]] (new) — weights that minimize risk for a given return, or maximize return for a given risk (p. 360)
- [[leverage-portfolio]] (new) — $L=\sum|w_i|$; $L=1$ for long-only portfolios (p. 358)
- [[two-fund-theorem]] (new) — all Pareto optimal portfolios are affine combinations of any two of them (p. 365)
- [[back-testing-validation]] (new) — checking weights or $\lambda$ on held-out realized data (p. 361, 375)
- [[regularization]] (new) — here a penalty added to the objective: on risky-asset weights or on turnover $\kappa\|w^{\rm curr}-w\|^2$ (p. 364–365). The estimation term $\lambda J_{\rm proc}$ is a similar penalty, but these pages do not use the word for it (p. 373)
- [[linear-quadratic-control]] (new) — choose inputs and states to minimize a sum of squares subject to linear dynamics (p. 366–367)
- [[state-feedback-control]] (new) — $u_t=Kx_t$; $K$ found from $n$ solves of the LQ problem with $x^{\rm init}=e_i$ (p. 371)
- [[state-estimation]] (new) — guess states and process noise from noisy measurements, minimizing $J_{\rm meas}+\lambda J_{\rm proc}$ (p. 372–373)
- [[stacking-block-matrices]] (new) — stack all variables into one vector $z$ and build block matrices $\tilde A,\tilde C$ (p. 367, 374)
- [[sparse-structure-cost]] (new) — exploiting sparsity makes the cost linear in $T$ (p. 368, 374)

## Canonical instances
- [[markowitz-portfolio]] — min-risk-for-return problem (17.2) and its KKT solution (17.3); the book notes it is not exactly Markowitz's original statistical formulation (p. 360)
- [[risk-return-example-19-stocks]] — 2000×20 return matrix, Pareto curve, Table 17.1 (p. 362–363)
- [[lq-control-3-state-example]] — $T=100$ example with trade-off curve in $\rho$ (p. 368–370)
- [[mass-in-2d-state-estimation]] — position/velocity model with noisy position measurements (p. 374–377)
- [[boeing-747-longitudinal-control]] — exercise 17.6 (p. 379)

## Bridges (candidates)
- [structural-analogy] control/estimation duality ↔ optimization: both are the same stacked constrained least squares, with inputs chosen (control) or inputs unknown (estimation) — the text itself calls this duality (p. 373).
- [structural-analogy] $\lambda J_{\rm proc}$, $\rho J_{\rm input}$ and the weighted portfolio penalty ↔ regularization in ch. 13–14 model fitting: each trades fit against a "size" penalty (p. 364).
- [structural-analogy] choosing $\lambda$ by withholding measurements ↔ train/test validation in data fitting (p. 375, 377).
- [same-math] Pareto line $w=w^0+\rho v$ ↔ affine combinations: the solution of a linear KKT system with a right-hand side affine in a parameter is an affine function of that parameter (p. 365).

## Questions this raises
- How reliably does assumption (17.4) hold, and how short can a test period be before back-testing becomes uninformative (p. 361)?
- Why does $K$ depend little on $T$ when $T$ is large enough (p. 372)? The book calls this beyond its scope.
- How exactly does the recursive Kalman filter solve (17.11), and how does it relate to the sparse stacked solve (p. 374)?
- How should one choose among $\lambda$, $\kappa$, $M$ and $\rho$ jointly in practice (p. 364–365)?

## Exercises worth doing
- Ex. 17.1 (p. 378) — dropping $\rho\mathbf 1$ from the objective of (17.2) gives an equivalent problem; shows that a constant term in the objective can be dropped when the constraints fix the return — difficulty: easy
- Ex. 17.2 (p. 378) — covariance-matrix form (17.13) of portfolio optimization is equivalent to (17.2) — difficulty: medium
- Ex. 17.3 (p. 378) — two-asset portfolio solved analytically; when are positions long or short — difficulty: easy
- Ex. 17.4–17.5 (p. 378–379) — index tracking and market-neutral constraints as constrained least squares — difficulty: medium
- Ex. 17.6 (p. 379–380) — LQ control and state feedback for a Boeing 747; $K$ for $T=100$ vs $T=50$ — difficulty: hard
- Ex. 17.7 (p. 380) — bio-mass estimation as a state estimation problem; effect of $\lambda$ — difficulty: medium

## Reading notes
- Printed page = pdf page − 10 (pdf 367 = printed 357).
- The extracted text garbles matrices (17.3), (17.5) and the block matrices of §17.2 and §17.3. I checked them against the page images and followed the images.
- The text at p. 361 refers to "the discussion on page 268", and the text at p. 368 and p. 374 refers to "page 349" (sparsity). Those pages are not in this unit.
- The unit also mentions "page 185" (state feedback) and §16.2 (standard methods); these are outside the pages provided.
- In the p. 377 text, the test region is described as "for $\lambda<100$ or so"; in figure 17.9 the train and test curves cross at roughly a few hundred, between $10^2$ and $10^3$ (read from the plot).
- One small typo: "which is a called a long-only portfolio" (p. 358). No other misprints found.
