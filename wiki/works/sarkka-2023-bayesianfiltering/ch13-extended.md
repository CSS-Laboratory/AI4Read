---
id: sarkka-2023-bayesianfiltering/ch13-extended
work: sarkka-2023-bayesianfiltering
unit: 13 Extended Rauch–Tung–Striebel Smoothing
pages: 267-277
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Extended Rauch–Tung–Striebel Smoothing

## L0 — One line
Replacing the prediction step of the RTS smoother by a Taylor-series approximation gives a smoother for nonlinear models, and relinearizing the whole trajectory repeatedly turns it into a Gauss–Newton method for the MAP trajectory.

## L1 — The gist (≤ 120 words)
How do we smooth (use all data $\mathbf y_{1:T}$ to estimate every state) when the dynamic or measurement model is nonlinear? The extended Rauch–Tung–Striebel (RTS) smoother (ERTSS) uses the RTS equations with a first-order (linearized) or second-order prediction. The iterated version (IERTSS) relinearizes dynamics and measurements at every time step along the current smoother estimate, and reruns an affine (linear plus constant) Kalman filter and smoother. It is a Gauss–Newton (iterative least-squares) method for the maximum a posteriori (MAP) estimate of the whole trajectory. In the pendulum example the root-mean-square error (RMSE) falls from 0.17 (extended Kalman filter, EKF) to 0.06 (ERTSS) to 0.03 (IERTSS). Levenberg–Marquardt and line-search variants exist.

**Prerequisites:** Gaussian conditioning; the linear Kalman filter and RTS smoother (Ch. 6, 12); the EKF and Jacobians (Ch. 7); Gauss–Newton least squares; MAP estimation.

## L2 — Key ideas (5–10 bullets)
- The ERTSS is the RTS smoother with the prediction replaced by a first-order Taylor approximation, evaluated at the filter mean $\mathbf m_k$ (p. 267–268).
- Derivation: build a Gaussian joint of $(\mathbf x_k,\mathbf x_{k+1})$ given $\mathbf y_{1:k}$, condition on $\mathbf x_{k+1}$, then marginalize with the smoothing law of $\mathbf x_{k+1}$ (p. 268–269).
- Non-additive models need only the non-additive prediction equations of Algorithm 7.5. A second-order smoother uses the Hessian-based prediction of Algorithm 7.8 (p. 269–270).
- The IERTSS minimizes the negative log posterior of the whole trajectory, a sum of weighted squares that Gauss–Newton can handle (p. 271–272).
- Each iteration linearizes $\mathbf f$ and $\mathbf h$ at all steps around the previous trajectory. This gives an affine Gaussian model, whose MAP estimate is the affine Kalman filter plus RTS smoother mean (p. 273–274).
- The iterated EKF (IEKF) relinearizes only the measurement model, at the previous estimate. The IERTSS relinearizes dynamic and measurement models at all steps and aims at the MAP of the whole trajectory (p. 271, 275).
- The initial guess affects only convergence speed; the point of convergence (if the algorithm converges) is the MAP estimate regardless of the guess (author's claim, p. 275).
- In the examples, the iteration lowers the error (pendulum 0.06 → 0.03) (p. 269, 275, 276).
- Levenberg–Marquardt (pseudo-measurements) and line search (step size $\gamma$) can improve convergence (p. 276–277).

## L3 — Walkthrough

### 13.1 Extended RTS smoother
The ERTSS assumes a Gaussian smoothing distribution $p(\mathbf x_k\mid\mathbf y_{1:T})\simeq \mathrm N(\mathbf x_k\mid \mathbf m_k^s,\mathbf P_k^s)$ (13.1, p. 267). It is built from the basic RTS equations by first-order approximation of the prediction (p. 267). Shapes (added): $\mathbf x_k\in\mathbb R^n$, so $\mathbf F_x,\mathbf P,\mathbf G,\mathbf Q$ are $n\times n$.

**Algorithm 13.1** (additive model (7.24)); $\mathbf F_x(\mathbf m_k)$ is the Jacobian of $\mathbf f$ at $\mathbf m_k$ (p. 268):
$$\begin{aligned}
\mathbf m_{k+1}^-&=\mathbf f(\mathbf m_k),\\
\mathbf P_{k+1}^-&=\mathbf F_x(\mathbf m_k)\mathbf P_k\mathbf F_x^\top(\mathbf m_k)+\mathbf Q_k,\\
\mathbf G_k&=\mathbf P_k\mathbf F_x^\top(\mathbf m_k)[\mathbf P_{k+1}^-]^{-1},\\
\mathbf m_k^s&=\mathbf m_k+\mathbf G_k[\mathbf m_{k+1}^s-\mathbf m_{k+1}^-],\\
\mathbf P_k^s&=\mathbf P_k+\mathbf G_k[\mathbf P_{k+1}^s-\mathbf P_{k+1}^-]\mathbf G_k^\top.
\end{aligned}\tag{13.2}$$
Start at $k=T$ with $\mathbf m_T^s=\mathbf m_T$, $\mathbf P_T^s=\mathbf P_T$ (p. 268). The filter means and covariances come from the EKF or a similar method (p. 268).

**Derivation.** Assume $p(\mathbf x_k\mid\mathbf y_{1:k})\simeq\mathrm N(\mathbf m_k,\mathbf P_k)$ and $p(\mathbf x_{k+1}\mid\mathbf y_{1:T})\simeq\mathrm N(\mathbf m^s_{k+1},\mathbf P^s_{k+1})$ (p. 268).
1. As in the EKF prediction, $p(\mathbf x_k,\mathbf x_{k+1}\mid\mathbf y_{1:k})=\mathrm N(\tilde{\mathbf m}_1,\tilde{\mathbf P}_1)$ (13.3), with
$$\tilde{\mathbf m}_1=\begin{pmatrix}\mathbf m_k\\ \mathbf f(\mathbf m_k)\end{pmatrix},\quad
\tilde{\mathbf P}_1=\begin{pmatrix}\mathbf P_k&\mathbf P_k\mathbf F_x^\top\\ \mathbf F_x\mathbf P_k&\mathbf F_x\mathbf P_k\mathbf F_x^\top+\mathbf Q_k\end{pmatrix}\tag{13.4}$$
($\mathbf F_x$ at $\mathbf m_k$) (p. 268).
2. Conditioning on $\mathbf x_{k+1}$ as in Section 12.2: $p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:T})=p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:k})=\mathrm N(\tilde{\mathbf m}_2,\tilde{\mathbf P}_2)$ (13.5), with (p. 269)
$$\begin{aligned}\mathbf G_k&=\mathbf P_k\mathbf F_x^\top(\mathbf F_x\mathbf P_k\mathbf F_x^\top+\mathbf Q_k)^{-1},\\
\tilde{\mathbf m}_2&=\mathbf m_k+\mathbf G_k(\mathbf x_{k+1}-\mathbf f(\mathbf m_k)),\\
\tilde{\mathbf P}_2&=\mathbf P_k-\mathbf G_k(\mathbf F_x\mathbf P_k\mathbf F_x^\top+\mathbf Q_k)\mathbf G_k^\top.\end{aligned}\tag{13.6}$$
3. Joint given all data: $p(\mathbf x_{k+1},\mathbf x_k\mid\mathbf y_{1:T})=p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:T})\,p(\mathbf x_{k+1}\mid\mathbf y_{1:T})=\mathrm N(\tilde{\mathbf m}_3,\tilde{\mathbf P}_3)$ (13.7), with (p. 269)
$$\tilde{\mathbf m}_3=\begin{pmatrix}\mathbf m^s_{k+1}\\ \mathbf m_k+\mathbf G_k(\mathbf m^s_{k+1}-\mathbf f(\mathbf m_k))\end{pmatrix},\quad
\tilde{\mathbf P}_3=\begin{pmatrix}\mathbf P^s_{k+1}&\mathbf P^s_{k+1}\mathbf G_k^\top\\ \mathbf G_k\mathbf P^s_{k+1}&\mathbf G_k\mathbf P^s_{k+1}\mathbf G_k^\top+\tilde{\mathbf P}_2\end{pmatrix}\tag{13.8}$$
4. The marginal of $\mathbf x_k$ is $\mathrm N(\mathbf m_k^s,\mathbf P_k^s)$ (13.9), with
$$\mathbf m_k^s=\mathbf m_k+\mathbf G_k(\mathbf m^s_{k+1}-\mathbf f(\mathbf m_k)),\quad
\mathbf P^s_k=\mathbf P_k+\mathbf G_k(\mathbf P^s_{k+1}-\mathbf F_x\mathbf P_k\mathbf F_x^\top-\mathbf Q_k)\mathbf G_k^\top\tag{13.10}$$
(added step) this equals the last two lines of (13.2), since $\mathbf m^-_{k+1}=\mathbf f(\mathbf m_k)$ and $\mathbf P^-_{k+1}=\mathbf F_x\mathbf P_k\mathbf F_x^\top+\mathbf Q_k$ (p. 269).

*Intuition note.* The smoother pulls the filter estimate at $k$ toward what the later data say about $\mathbf x_{k+1}$. The gain $\mathbf G_k$ says how strongly $\mathbf x_k$ and $\mathbf x_{k+1}$ are linked through the linearized dynamics.

Non-additive model (7.39): replace the first two equations of (13.2) by their versions in Algorithm 7.5 (p. 269).

**Examples.** Pendulum (Example 7.6): ERTSS RMSE 0.06 vs EKF 0.17; other filters 0.10–0.17 (Ex. 13.2, p. 269). Coordinated turn (Example 7.7): ERTSS error 0.016 vs EKF 0.31 (Ex. 13.3, p. 269).

### 13.2 Higher order ERTSS
**Algorithm 13.4** replaces the prediction by the second-order version of Algorithm 7.8 (p. 270). $\mathbf F^{(i)}_{xx}(\mathbf m_k)$ is the Hessian of $\mathbf f$ as defined in (7.54); the index $i$ and the vectors $\mathbf e_i$ are not defined on these pages (see Ch. 7).
$$\begin{aligned}\mathbf m_{k+1}^-&=\mathbf f(\mathbf m_k)+\tfrac12\sum_i\mathbf e_i\,\mathrm{tr}\{\mathbf F^{(i)}_{xx}(\mathbf m_k)\mathbf P_k\},\\
\mathbf P_{k+1}^-&=\mathbf F_x\mathbf P_k\mathbf F_x^\top+\tfrac12\sum_{i,i'}\mathbf e_i\mathbf e_{i'}^\top\mathrm{tr}\{\mathbf F^{(i)}_{xx}\mathbf P_k\mathbf F^{(i')}_{xx}\mathbf P_k\}+\mathbf Q_k,\end{aligned}\tag{13.11}$$
and $\mathbf G_k,\mathbf m^s_k,\mathbf P^s_k$ are as in (13.2) (p. 270).

### 13.3 Iterated ERTSS
The IERTSS (also called IEKS or IKS, Bell 1994) is a Gauss–Newton method for the MAP estimate of $\mathbf x_{0:T}$ (p. 271). Idea: relinearize the model at all steps along the current smoother estimate and rerun the smoother (p. 271). The IEKF relinearized only the measurement model at the previous estimate; the IERTSS relinearizes both dynamic and measurement models at all steps (p. 271).

**MAP problem.** $p(\mathbf x_{0:T}\mid\mathbf y_{1:T})\propto p(\mathbf x_0)\prod_k p(\mathbf y_k\mid\mathbf x_k)p(\mathbf x_k\mid\mathbf x_{k-1})$ (13.12). Then $\mathbf x^{\rm MAP}_{0:T}=\arg\max$ of this (13.13), or $\arg\min L$ (13.15) with (p. 272)
$$L(\mathbf x_{0:T})=-\log p(\mathbf x_0)-\sum_k\log p(\mathbf y_k\mid\mathbf x_k)-\sum_k\log p(\mathbf x_k\mid\mathbf x_{k-1}).\tag{13.14}$$
For $p(\mathbf x_k\mid\mathbf x_{k-1})=\mathrm N(\mathbf f(\mathbf x_{k-1}),\mathbf Q_{k-1})$, $p(\mathbf y_k\mid\mathbf x_k)=\mathrm N(\mathbf h(\mathbf x_k),\mathbf R_k)$ (13.16) and $p(\mathbf x_0)=\mathrm N(\mathbf m_0,\mathbf P_0)$ (p. 272):
$$\begin{aligned}L=C&+\tfrac12(\mathbf x_0-\mathbf m_0)^\top\mathbf P_0^{-1}(\mathbf x_0-\mathbf m_0)+\tfrac12\sum_k(\mathbf y_k-\mathbf h(\mathbf x_k))^\top\mathbf R_k^{-1}(\mathbf y_k-\mathbf h(\mathbf x_k))\\&+\tfrac12\sum_k(\mathbf x_k-\mathbf f(\mathbf x_{k-1}))^\top\mathbf Q_{k-1}^{-1}(\mathbf x_k-\mathbf f(\mathbf x_{k-1})),\end{aligned}\tag{13.17}$$
with $C$ independent of the states. This is a special case of the Gauss–Newton cost form (7.63), so Gauss–Newton can minimize it (p. 272).

**Linearization.** Start from $\mathbf x^{(0)}_{0:T}$ (e.g. from a non-iterated ERTSS). Given $\mathbf x^{(i-1)}_{0:T}$, for all $k=1,\dots,T$ (p. 273):
$$\mathbf f(\mathbf x_{k-1})\simeq\mathbf f(\mathbf x^{(i-1)}_{k-1})+\mathbf F_x(\mathbf x^{(i-1)}_{k-1})(\mathbf x_{k-1}-\mathbf x^{(i-1)}_{k-1}),\quad
\mathbf h(\mathbf x_k)\simeq\mathbf h(\mathbf x^{(i-1)}_k)+\mathbf H_x(\mathbf x^{(i-1)}_k)(\mathbf x_k-\mathbf x^{(i-1)}_k)\tag{13.18}$$
Define $\mathbf u_{k-1}=\mathbf f(\mathbf x^{(i-1)}_{k-1})-\mathbf F_x\mathbf x^{(i-1)}_{k-1}$, $\mathbf A_{k-1}=\mathbf F_x(\mathbf x^{(i-1)}_{k-1})$, $\mathbf d_k=\mathbf h(\mathbf x^{(i-1)}_k)-\mathbf H_x\mathbf x^{(i-1)}_k$, $\mathbf H_k=\mathbf H_x(\mathbf x^{(i-1)}_k)$ (13.19). Then $\mathbf f(\mathbf x_{k-1})\simeq\mathbf A_{k-1}\mathbf x_{k-1}+\mathbf u_{k-1}$, $\mathbf h(\mathbf x_k)\simeq\mathbf H_k\mathbf x_k+\mathbf d_k$ (13.20). Substituting into (13.17) gives (13.21), the cost of the affine Gaussian model
$$p(\mathbf x_k\mid\mathbf x_{k-1})\simeq\mathrm N(\mathbf A_{k-1}\mathbf x_{k-1}+\mathbf u_{k-1},\mathbf Q_{k-1}),\quad p(\mathbf y_k\mid\mathbf x_k)\simeq\mathrm N(\mathbf H_k\mathbf x_k+\mathbf d_k,\mathbf R_k)\tag{13.22}$$
For a Gaussian, the mean equals the MAP estimate. So the minimizer of (13.21) is the smoother mean from the affine Kalman filter (Thm 6.9) and affine RTS smoother (Thm 12.5). It becomes the next iterate $\mathbf x^{(i)}_{0:T}=\mathbf m^s_{0:T}$ (p. 273–274).

**Algorithm 13.5** (for $i=1,\dots,I_{\max}$; shapes (added): $\mathbf H_x$ is $d\times n$, $\mathbf S$ is $d\times d$, $\mathbf K$ is $n\times d$) (p. 274).
1. Filter from $\mathbf m^{(i)}_0=\mathbf m_0$, $\mathbf P^{(i)}_0=\mathbf P_0$, for $k=1,\dots,T$:
$$\begin{aligned}\mathbf m_k^{-(i)}&=\mathbf f(\mathbf x^{(i-1)}_{k-1})+\mathbf F_x(\mathbf x^{(i-1)}_{k-1})(\mathbf m^{(i)}_{k-1}-\mathbf x^{(i-1)}_{k-1}),\\
\mathbf P_k^{-(i)}&=\mathbf F_x\mathbf P^{(i)}_{k-1}\mathbf F_x^\top+\mathbf Q_{k-1},\\
\mathbf v_k^{(i)}&=\mathbf y_k-\mathbf h(\mathbf x^{(i-1)}_k)-\mathbf H_x(\mathbf x^{(i-1)}_k)(\mathbf m_k^{-(i)}-\mathbf x^{(i-1)}_k),\\
\mathbf S^{(i)}_k&=\mathbf H_x\mathbf P_k^{-(i)}\mathbf H_x^\top+\mathbf R_k,\quad \mathbf K^{(i)}_k=\mathbf P_k^{-(i)}\mathbf H_x^\top[\mathbf S^{(i)}_k]^{-1},\\
\mathbf m^{(i)}_k&=\mathbf m_k^{-(i)}+\mathbf K^{(i)}_k\mathbf v^{(i)}_k,\quad \mathbf P^{(i)}_k=\mathbf P_k^{-(i)}-\mathbf K^{(i)}_k\mathbf S^{(i)}_k[\mathbf K^{(i)}_k]^\top.\end{aligned}\tag{13.23}$$
2. Smoother from $\mathbf m^{s,(i)}_T=\mathbf m_T$, $\mathbf P^{s,(i)}_T=\mathbf P_T$, for $k=T-1,\dots,0$ (Jacobians at $\mathbf x^{(i-1)}_k$):
$$\begin{aligned}\mathbf m^{-(i)}_{k+1}&=\mathbf f(\mathbf x^{(i-1)}_k)+\mathbf F_x(\mathbf m^{(i)}_k-\mathbf x^{(i-1)}_k),\quad \mathbf P^{-(i)}_{k+1}=\mathbf F_x\mathbf P^{(i)}_k\mathbf F_x^\top+\mathbf Q_k,\\
\mathbf G^{(i)}_k&=\mathbf P^{(i)}_k\mathbf F_x^\top[\mathbf P^{-(i)}_{k+1}]^{-1},\\
\mathbf m^{s,(i)}_k&=\mathbf m^{(i)}_k+\mathbf G^{(i)}_k[\mathbf m^{s,(i)}_{k+1}-\mathbf m^{-(i)}_{k+1}],\\
\mathbf P^{s,(i)}_k&=\mathbf P^{(i)}_k+\mathbf G^{(i)}_k[\mathbf P^{s,(i)}_{k+1}-\mathbf P^{-(i)}_{k+1}][\mathbf G^{(i)}_k]^\top.\end{aligned}\tag{13.24}$$
3. Set $\mathbf x^{(i)}_{0:T}=\mathbf m^{s,(i)}_{0:T}$. Final output: $\mathbf m^s_{0:T}=\mathbf m^{s,(I_{\max})}_{0:T}$, $\mathbf P^s_{0:T}=\mathbf P^{s,(I_{\max})}_{0:T}$ (13.25) (p. 274).

*Intuition note.* Each sweep solves exactly a linear-Gaussian problem that approximates the true trajectory cost near the current guess. Repeating it is a Gauss–Newton iteration: under the convergence conditions the author cites (and if it converges), it ends at the trajectory with the highest posterior density (p. 275).

**Convergence.** Being Gauss–Newton, the IERTSS can be shown to converge in well-defined conditions (Bell 1994), and the convergence is to the trajectory MAP. The IEKF does only a local iteration at the update step, so it does not converge to the global MAP (p. 275). The initial guess affects only speed; the point of convergence (if the algorithm converges) is the MAP estimate regardless of the guess (author's claim, p. 275).

**Examples.** Pendulum: IERTSS RMSE 0.03 (ERTSS 0.06, EKF 0.17, other filters 0.10–0.17) (Ex. 13.6, p. 275). Coordinated turn (Example 7.11, inaccurate initial guess): 0.015 vs ERTSS 0.017. With the more accurate initial guess data of Example 13.3 the error is also 0.015 (Ex. 13.7, p. 275–276).

### 13.4 Levenberg–Marquardt and line-search IERTSS
Details are not given; see Särkkä and Svensson (2020) (p. 276).
- Levenberg–Marquardt: add to the filter a (pseudo-)measurement of the previous iterate $\mathbf x^{(i-1)}_k$ at each step $k$, with a suitably defined covariance (p. 276).
- Line search: $\mathbf x^{(i)}_{0:T}=\mathbf x^{(i-1)}_{0:T}+\gamma(\mathbf m^{s,(i)}_{0:T}-\mathbf x^{(i-1)}_{0:T})$ (13.26), where the step size $\gamma$ is chosen to minimize $L$ (13.17) at the new point $\mathbf x^{(i-1)}_{0:T}+\gamma(\mathbf m^{s,(i)}_{0:T}-\mathbf x^{(i-1)}_{0:T})$; this minimization need not be exact (p. 276–277).

## Toy example (ours)
Scalar model $f(x)=x^2$, $Q=1$. Filter results: $m_k=2$, $P_k=1$ at step $k$; at the last step $T=k+1$, $m_T=3.5$, $P_T=0.5$, so $m^s_T=3.5$, $P^s_T=0.5$.
- $F_x=2x=4$ at $m_k=2$.
- $m^-_{k+1}=f(2)=4$; $P^-_{k+1}=4\cdot1\cdot4+1=17$.
- $G_k=1\cdot4/17=4/17$.
- $m^s_k=2+\tfrac4{17}(3.5-4)=2-\tfrac2{17}=\tfrac{32}{17}\approx1.882$.
- $P^s_k=1+\tfrac{16}{289}(0.5-17)=1-\tfrac{264}{289}=\tfrac{25}{289}\approx0.087$.

The late data are lower than predicted (3.5 vs 4), so the smoother lowers $m_k$ and shrinks the variance from 1. For one relinearization step of (13.19) at $\bar x=1.5$: $A=3$, $u=2.25-4.5=-2.25$, so $f(x)\simeq3x-2.25$ (at $x=2$: 3.75 vs true 4).

## Concepts
- [[extended-rts-smoother]] (new) — RTS smoother with linearized (or second-order) prediction around the filter mean (p. 267–268)
- [[iterated-extended-rts-smoother]] (new) — relinearize all steps along the smoother estimate and repeat; Gauss–Newton for the trajectory MAP (p. 271)
- [[gauss-newton-method]] (new) — iterative minimizer for sums of weighted squared nonlinear residuals, using linearization (p. 272)
- [[map-trajectory-estimate]] (new) — argmax of $p(\mathbf x_{0:T}\mid\mathbf y_{1:T})$ over the whole path (p. 272)
- [[levenberg-marquardt-and-line-search]] (new) — damped or step-length-controlled variants of the iteration (p. 276)
- [[linearization]] — first-order Taylor approximation of $\mathbf f,\mathbf h$ at a point (p. 273)
- [[kalman-filter]] — affine Kalman filter plus RTS smoother solves each linearized problem (p. 273–274)

## Canonical instances
- [[pendulum-tracking]] — RMSE 0.17 (EKF) → 0.06 (ERTSS) → 0.03 (IERTSS) (p. 269, 275)
- [[coordinated-turn-model]] — ERTSS 0.016 vs EKF 0.31; IERTSS 0.015 vs ERTSS 0.017 on an inaccurate initial guess (p. 269, 276)

## Bridges (candidates)
- [same-math] IERTSS iteration ↔ nonlinear least squares: Gauss–Newton on the cost (13.17), solved by Kalman filter and smoother.
- [structural-analogy] Smoothing ↔ state estimation in control (observer using future data): offline refinement of filter estimates.
- [metaphor] Relinearizing around a better guess ↔ re-planning a path from the current best trajectory.

## Questions this raises
- When does Gauss–Newton fail on (13.17), and how do Levenberg–Marquardt or line search help?
- How good is the Gaussian covariance $\mathbf P^s$ returned at the final iterate as an uncertainty estimate?
- Can the iterated smoother cope with non-Gaussian noise?

## Exercises worth doing
- Ex. 13.1 (p. 277) — implement the ERTSS and compare filter and smoother errors — difficulty: easy
- Ex. 13.3 (p. 277) — bearings-only tracking; linear dynamics make the smoother linear — difficulty: medium
- Ex. 13.5 (p. 277) — one IERTSS iteration from the EKF result equals the ERTSS — difficulty: medium
- Ex. 13.6 (p. 277) — derive and implement the IERTSS and compare errors — difficulty: hard

## Reading notes
- Printed page = pdf − 30. Text-layer math was garbled; equations were checked against the page images.
- Figure 13.4's caption and Example 13.7 cite Example 7.11, while Example 13.3 cites Example 7.7. Both are as printed.
- The text states convergence to the MAP "if the algorithm convergences" (typo as printed) and does not discuss local minima on these pages (p. 275).
- Section 13.4 gives only ideas, no algorithms. Section 13.5 gives exercises only, with no solutions.
