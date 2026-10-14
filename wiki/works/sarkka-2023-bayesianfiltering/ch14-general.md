---
id: sarkka-2023-bayesianfiltering/ch14-general
work: sarkka-2023-bayesianfiltering
unit: "14 General Gaussian Smoothing"
pages: 278-307
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# General Gaussian Smoothing

## L0 — One line
Gaussian smoothers keep the RTS backward recursion and compute the moments it needs by moment matching or sigma-point integration. They are equivalent to statistically linearizing the dynamic model around the filtering density, and relinearizing iteratively around the smoothing density gives the iterated posterior linearization smoother (IPLS).

## L1 — The gist (≤ 120 words)
The unit asks how to smooth (estimate states using all measurements, past and future) when the dynamic and measurement models are non-linear. The answer: reuse the RTS (Rauch–Tung–Striebel, the smoother for linear Gaussian models) backward recursion, but compute the needed moments by Gaussian moment matching, evaluated with sigma-point rules (Gauss–Hermite, cubature, unscented, fifth order). These smoothers equal statistical linear regression (SLR: an affine fit over a distribution) of the dynamic model around the filtering density (given past data only). Relinearizing around the smoothing density (given all data), iteratively, gives the iterated posterior linearization smoother (IPLS). In the reported pendulum and coordinated-turn examples the iterated versions have slightly lower error (0.03 vs 0.04; 0.015 vs 0.016).

**Prerequisites:** Kalman filter and affine RTS smoother (Ch. 12); Gaussian conditioning rules; moment matching, sigma-point/cubature integration and statistical linear regression (Ch. 8–10); EKF/extended RTS smoother (Ch. 13); matrix inverse and covariance.

## L2 — Key ideas
- A general Gaussian RTS smoother needs three moments from the filtering density $\mathrm N(\mathbf m_k,\mathbf P_k)$: predicted mean, predicted covariance and cross-covariance. The backward recursion then has the same form as the affine RTS smoother (pp. 279, 292).
- The moment integrals are mostly not closed-form, so they are replaced by sigma-point rules. Gauss–Hermite, spherical cubature, unscented and fifth-order rules give GHRTSS, CRTSS, URTSS and URTSS5. Only the points and weights change (pp. 280–289).
- Gauss–Hermite scales exponentially in dimension, so its non-additive version is not very useful. The cubature and unscented rules have augmented non-additive versions (pp. 281, 283, 286).
- Gaussian smoothers equal RTS smoothing of a statistically linearized dynamic model, where the regression is taken over the filtering density. The measurement model is not needed in the smoothing pass (pp. 291–293).
- Conditional-distribution models give the same smoother structure (Alg. 14.16), and the moments can be estimated by Monte Carlo (Alg. 14.17) (pp. 293–294).
- Posterior linearization smoothers may linearize over any chosen distribution. Linearizing over the smoothing density needs an iteration, which is the IPLS (pp. 295–297).
- The IPLS differs from the IPLF: it uses all measurements, and it updates both models at all time steps. It differs from the IERTSS only in using SLR instead of a Taylor expansion at the smoothed mean (pp. 298–299).
- In the reported examples the non-iterated smoothers have RMSE 0.04 (pendulum) and 0.016 (coordinated turn). The iterated ones have 0.03 and 0.015 (pp. 281, 290, 304).

## L3 — Walkthrough

### Opening (p. 278)
The chapter reuses the principles of Gaussian filters (moment matching, Ch. 8; statistical linear regression, Ch. 9; posterior linearization, Ch. 10). They are applied through the RTS equations to get Gaussian forward-backward smoothers. Chapter 13's Taylor-based smoothers are the starting point (p. 278).

### 14.1 General Gaussian RTS smoother (pp. 278–280)
**Setting.** State $\mathbf x_k\in\mathbb R^n$ with additive model $\mathbf x_{k+1}=\mathbf f(\mathbf x_k)+\mathbf q_k$. Filtering results $\mathbf m_k,\mathbf P_k$ are available. (added step, dimension check, not stated in the text) All of $\mathbf P^-_{k+1},\mathbf D_{k+1},\mathbf G_k$ are $n\times n$.

**Algorithm 14.1 (additive Gaussian RTS smoother I)** (p. 279):
$$
\begin{aligned}
\mathbf m^-_{k+1}&=\int \mathbf f(\mathbf x_k)\,\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)\,d\mathbf x_k,\\
\mathbf P^-_{k+1}&=\int[\mathbf f(\mathbf x_k)-\mathbf m^-_{k+1}][\mathbf f(\mathbf x_k)-\mathbf m^-_{k+1}]^{\mathsf T}\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)\,d\mathbf x_k+\mathbf Q_k,\\
\mathbf D_{k+1}&=\int[\mathbf x_k-\mathbf m_k][\mathbf f(\mathbf x_k)-\mathbf m^-_{k+1}]^{\mathsf T}\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)\,d\mathbf x_k,\\
\mathbf G_k&=\mathbf D_{k+1}[\mathbf P^-_{k+1}]^{-1},\\
\mathbf m^s_k&=\mathbf m_k+\mathbf G_k(\mathbf m^s_{k+1}-\mathbf m^-_{k+1}),\\
\mathbf P^s_k&=\mathbf P_k+\mathbf G_k(\mathbf P^s_{k+1}-\mathbf P^-_{k+1})\mathbf G_k^{\mathsf T}.
\end{aligned}\tag{14.1}
$$
Here $\mathbf D_{k+1}$ is the cross-covariance of $\mathbf x_k,\mathbf x_{k+1}$ given $\mathbf y_{1:k}$. $\mathbf G_k$ is the smoother gain.

**Derivation** (p. 279). Assume $p(\mathbf x_k\mid\mathbf y_{1:k})\simeq\mathrm N(\mathbf m_k,\mathbf P_k)$ and $p(\mathbf x_{k+1}\mid\mathbf y_{1:T})\simeq\mathrm N(\mathbf m^s_{k+1},\mathbf P^s_{k+1})$.
1. Moment matching (Alg. 8.1) applied to $\mathbf x_{k+1}=\mathbf f(\mathbf x_k)+\mathbf q_k$ gives the joint
$$p(\mathbf x_k,\mathbf x_{k+1}\mid\mathbf y_{1:k})\simeq\mathrm N\!\left(\begin{pmatrix}\mathbf x_k\\\mathbf x_{k+1}\end{pmatrix}\Big|\begin{pmatrix}\mathbf m_k\\\mathbf m^-_{k+1}\end{pmatrix},\begin{pmatrix}\mathbf P_k&\mathbf D_{k+1}\\\mathbf D_{k+1}^{\mathsf T}&\mathbf P^-_{k+1}\end{pmatrix}\right),\tag{14.2}$$
with the quantities defined in (14.1).
2. By Gaussian conditioning, $p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:T})\simeq\mathrm N(\tilde{\mathbf m}_2,\tilde{\mathbf P}_2)$ with $\mathbf G_k=\mathbf D_{k+1}[\mathbf P^-_{k+1}]^{-1}$, $\tilde{\mathbf m}_2=\mathbf m_k+\mathbf G_k(\mathbf x_{k+1}-\mathbf m^-_{k+1})$, $\tilde{\mathbf P}_2=\mathbf P_k-\mathbf G_k\mathbf P^-_{k+1}\mathbf G_k^{\mathsf T}$.
3. The rest is analogous to the ERTSS derivation in Section 13.1 (p. 280). That derivation is not repeated in this unit.

**Algorithm 14.2 (non-additive, $\mathbf x_{k+1}=\mathbf f(\mathbf x_k,\mathbf q_k)$)** (p. 280). The last three lines are as in (14.1). The three moments are integrated jointly over $\mathbf x_k$ and $\mathbf q_k\sim\mathrm N(\mathbf 0,\mathbf Q_k)$ (14.3):
$$\mathbf m^-_{k+1}=\int\mathbf f(\mathbf x_k,\mathbf q_k)\,\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)\mathrm N(\mathbf q_k\mid\mathbf 0,\mathbf Q_k)\,d\mathbf x_k d\mathbf q_k,$$
$\mathbf P^-_{k+1}$ is the covariance of $\mathbf f(\mathbf x_k,\mathbf q_k)$ under the same weight (no extra $\mathbf Q_k$), and $\mathbf D_{k+1}=\int[\mathbf x_k-\mathbf m_k][\mathbf f(\mathbf x_k,\mathbf q_k)-\mathbf m^-_{k+1}]^{\mathsf T}(\cdots)$.

The integrals can be approximated by Gauss–Hermite, spherical cubature or other schemes. The algorithms are mainly theoretical, because the integrals can be solved in closed form only in special cases. Fixed-point and fixed-lag versions exist in Särkkä and Hartikainen (2010a) (p. 280).

*Intuition note.* The RTS backward step is built from a Gaussian joint of $(\mathbf x_k,\mathbf x_{k+1})$ given the measurements up to $k$, together with the smoothing distribution at step $k+1$. Moment matching builds that joint for a non-linear model. The conditional of $\mathbf x_k$ then follows from Gaussian conditioning rules (p. 279).

### 14.2 Gauss–Hermite RTS smoother (pp. 280–282)
**Algorithm 14.3 (GHRTSS, additive)** (p. 281). Sigma points with $\sqrt{\mathbf P_k}$ a matrix square root, $\boldsymbol\xi^{(i_1,\dots,i_n)}$ the unit points of (8.30) and $W_{i_1,\dots,i_n}$ the weights of (8.29):
$$\mathcal X_k^{(i_1,\dots,i_n)}=\mathbf m_k+\sqrt{\mathbf P_k}\,\boldsymbol\xi^{(i_1,\dots,i_n)},\quad i_1,\dots,i_n=1,\dots,p,\tag{14.4}$$
$$\hat{\mathcal X}_{k+1}^{(i_1,\dots,i_n)}=\mathbf f(\mathcal X_k^{(i_1,\dots,i_n)}),\tag{14.5}$$
$$\begin{aligned}\mathbf m^-_{k+1}&=\sum W_{i_1,\dots,i_n}\hat{\mathcal X}^{(i_1,\dots,i_n)}_{k+1},\\
\mathbf P^-_{k+1}&=\sum W_{i_1,\dots,i_n}(\hat{\mathcal X}^{(i_1,\dots,i_n)}_{k+1}-\mathbf m^-_{k+1})(\hat{\mathcal X}^{(i_1,\dots,i_n)}_{k+1}-\mathbf m^-_{k+1})^{\mathsf T}+\mathbf Q_k,\\
\mathbf D_{k+1}&=\sum W_{i_1,\dots,i_n}(\mathcal X^{(i_1,\dots,i_n)}_k-\mathbf m_k)(\hat{\mathcal X}^{(i_1,\dots,i_n)}_{k+1}-\mathbf m^-_{k+1})^{\mathsf T}.\end{aligned}\tag{14.6}$$
Step 4 is the gain and smoothing recursion, identical to the last three lines of (14.1), as (14.7).

A non-additive version is possible, but Gauss–Hermite scales exponentially in the state dimension, and that dimension doubles with the non-additive transform (state and process noise are integrated jointly). So the extension is not very useful in practice (p. 281).

**Example 14.4** (pendulum, Example 7.6). GHRTSS RMSE is 0.04. This lies between ERTSS (0.06) and IERTSS (0.03) and is clearly below GHKF (0.10) (pp. 281–282, Fig. 14.1).

### 14.3 Cubature RTS smoother (pp. 282–284)
**Algorithm 14.5 (CRTSS, additive)** uses the third-order spherical cubature rule (Section 8.5), with $\mathbf e_i$ the unit vector along axis $i$:
$$\mathcal X_k^{(i)}=\mathbf m_k+\sqrt{\mathbf P_k}\,\boldsymbol\xi^{(i)},\ i=1,\dots,2n;\qquad\boldsymbol\xi^{(i)}=\begin{cases}\sqrt n\,\mathbf e_i,&i=1,\dots,n\\-\sqrt n\,\mathbf e_{i-n},&i=n+1,\dots,2n\end{cases}\tag{14.8–14.9}$$
Propagate $\hat{\mathcal X}^{(i)}_{k+1}=\mathbf f(\mathcal X^{(i)}_k)$. Then, with equal weights $1/(2n)$,
$$\mathbf m^-_{k+1}=\tfrac1{2n}\sum_{i=1}^{2n}\hat{\mathcal X}^{(i)}_{k+1},\quad \mathbf P^-_{k+1}=\tfrac1{2n}\sum_{i=1}^{2n}(\hat{\mathcal X}^{(i)}_{k+1}-\mathbf m^-_{k+1})(\cdot)^{\mathsf T}+\mathbf Q_k,\quad\mathbf D_{k+1}=\tfrac1{2n}\sum_{i=1}^{2n}(\mathcal X^{(i)}_k-\mathbf m_k)(\hat{\mathcal X}^{(i)}_{k+1}-\mathbf m^-_{k+1})^{\mathsf T}\tag{14.10}$$
Step 4 is as in (14.1), given as (14.11) (pp. 282–283).

**Algorithm 14.6 (non-additive, augmented)** (pp. 283–284). Use $n'=n+n_q$, $\tilde{\mathbf m}_k=\begin{pmatrix}\mathbf m_k\\\mathbf 0\end{pmatrix}$, $\tilde{\mathbf P}_k=\begin{pmatrix}\mathbf P_k&\mathbf 0\\\mathbf 0&\mathbf Q_k\end{pmatrix}$, and $2n'$ points $\tilde{\mathcal X}^{(i)}_k=\tilde{\mathbf m}_k+\sqrt{\tilde{\mathbf P}_k}\boldsymbol\xi^{(i)\prime}$ (14.12). Propagate $\hat{\mathcal X}^{(i)}_{k+1}=\mathbf f(\tilde{\mathcal X}^{(i),x}_k,\tilde{\mathcal X}^{(i),q}_k)$, where the superscripts $x$ and $q$ denote the parts of the augmented point for $\mathbf x_k$ and $\mathbf q_k$. The sums (14.13) use weights $1/(2n')$. $\mathbf P^-_{k+1}$ has no added $\mathbf Q_k$, and $\mathbf D_{k+1}=\frac1{2n'}\sum(\tilde{\mathcal X}^{(i),x}_k-\mathbf m_k)(\hat{\mathcal X}^{(i)}_{k+1}-\mathbf m^-_{k+1})^{\mathsf T}$. Step 4 is (14.14).

**Example 14.7.** CRTSS has RMSE 0.04, similar to GHRTSS (p. 284).

### 14.4 Unscented RTS smoother (pp. 285–287)
The URTSS uses the unscented transform as the numerical solution of the moment-matching integrals (p. 285).

**Algorithm 14.8 (additive).** With $\lambda$ from (8.74) and $[\sqrt{\mathbf P_k}]_i$ the $i$-th column of the square root:
$$\mathcal X_k^{(0)}=\mathbf m_k,\quad\mathcal X_k^{(i)}=\mathbf m_k+\sqrt{n+\lambda}\,[\sqrt{\mathbf P_k}]_i,\quad\mathcal X_k^{(i+n)}=\mathbf m_k-\sqrt{n+\lambda}\,[\sqrt{\mathbf P_k}]_i,\ i=1,\dots,n\tag{14.15}$$
Propagate $\hat{\mathcal X}^{(i)}_{k+1}=\mathbf f(\mathcal X_k^{(i)})$, $i=0,\dots,2n$. With the weights $W^{(m)}_i,W^{(c)}_i$ of (8.75):
$$\mathbf m^-_{k+1}=\sum_{i=0}^{2n}W^{(m)}_i\hat{\mathcal X}^{(i)}_{k+1},\ \ \mathbf P^-_{k+1}=\sum_{i=0}^{2n}W^{(c)}_i(\hat{\mathcal X}^{(i)}_{k+1}-\mathbf m^-_{k+1})(\cdot)^{\mathsf T}+\mathbf Q_k,\ \ \mathbf D_{k+1}=\sum_{i=0}^{2n}W^{(c)}_i(\mathcal X^{(i)}_k-\mathbf m_k)(\hat{\mathcal X}^{(i)}_{k+1}-\mathbf m^-_{k+1})^{\mathsf T}\tag{14.16}$$
Step 4 is as in (14.1) (14.17). The recursion starts from $\mathbf m^s_T=\mathbf m_T$, $\mathbf P^s_T=\mathbf P_T$ and runs backward for $k=T-1,\dots,0$ (p. 286). The derivation is that of Algorithm 14.1 with the unscented transform replacing moment matching (p. 286).

The CRTSS is a special case of the URTSS with $\alpha=1,\beta=0,\kappa=0$. This choice tends to work well, and the sigma-point and weight rules are simple (p. 286).

**Algorithm 14.9 (non-additive, augmented UT).** Same augmented variable as in 14.3, with $\lambda'$ and $2n'+1$ points $\tilde{\mathcal X}_k^{(0)}=\tilde{\mathbf m}_k$, $\tilde{\mathcal X}_k^{(i)}=\tilde{\mathbf m}_k\pm\sqrt{n'+\lambda'}[\sqrt{\tilde{\mathbf P}_k}]_i$ (14.18). The sums use $W_i^{(m)\prime},W_i^{(c)\prime}$ from Section 8.7 (14.19). Step 4 is (14.20) (pp. 286–287).

**Example 14.10.** URTSS RMSE is 0.04, the same as GHRTSS and CRTSS. The UKF had 0.10 (p. 287, Fig. 14.3 caption on p. 288).

### 14.5 Higher-order cubature/unscented smoothers (pp. 287–290)
Any higher-order rule can be used in the same way. With the fifth-order rule of Alg. 8.22, the unit points $\boldsymbol\xi^{(i)}$ are those of (8.102) and the weights $W_i$ those of (8.103), for $i=0,1,2,\dots$:

**Algorithm 14.11 (URTSS5, additive)** (pp. 287–288): $\mathcal X^{(i)}_k=\mathbf m_k+\sqrt{\mathbf P_k}\boldsymbol\xi^{(i)}$ (14.21). Sigma-point propagation, the sums $\sum_iW_i(\cdot)$ with $+\mathbf Q_k$ in $\mathbf P^-_{k+1}$ (14.22), and step 4 (14.23) have the same form as in (14.16)–(14.17).

**Algorithm 14.12 (non-additive).** Augmented variable with $n\leftarrow n+n_q$, as in 14.3 and 14.4. The sums are (14.25) and the smoother step is (14.26) (p. 289). Both algorithms can use any sigma-point integration method by changing only the unit points and weights (pp. 289–290).

**Example 14.13.** URTSS5 on the pendulum has RMSE 0.04, similar to the other smoothers (p. 290).

**Example 14.14** (coordinated turn model, Example 7.7). GH, spherical cubature, unscented and fifth-order smoothers all give RMSE 0.016. ERTSS gives 0.017 (p. 290, Fig. 14.5).

### 14.6 Statistical linear regression smoothers (pp. 290–294)
**Idea.** Gaussian smoothers are enabling-approximation algorithms. They first linearize the models, then use the closed-form RTS smoother. The extended RTS smoother (Alg. 13.1) linearizes the dynamic model with a first-order Taylor expansion at the filtering mean $\mathbf m_k$. The iterated ERTSS (Alg. 13.5) expands around the current smoothed mean estimate $\mathbf m^{s,(i-1)}_k$ (p. 291).

The affine RTS smoother (Theorem 12.5) does not use the measurement model. It suffices to do SLR on the dynamic model,
$$\mathbf x_{k+1}=\mathbf A_k\mathbf x_k+\mathbf a_k+\tilde{\boldsymbol\epsilon}_k,\quad\tilde{\boldsymbol\epsilon}_k\sim\mathrm N(\mathbf 0,\boldsymbol\Lambda_k).\tag{14.27}$$
SLR can be done with respect to different distributions, which gives different smoothers (Def. 10.1, Thm. 10.2). If the filtering density $\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)$ is used, the resulting smoothers give the same result as Algorithms 14.1 and 14.2 (p. 291).

**Algorithm 14.15 (SLRRTSS, additive)** (p. 292). Linearize:
$$\mathbf A_k=(\mathbf P^{xx}_{k+1})^{\mathsf T}\mathbf P_k^{-1},\quad\mathbf a_k=\boldsymbol\mu^-_{k+1}-\mathbf A_k\mathbf m_k,\quad\boldsymbol\Lambda_k=\mathbf P^x_{k+1}-\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}\tag{14.28}$$
with $\boldsymbol\mu^-_{k+1}=\int\mathbf f(\mathbf x)\mathrm N(\mathbf x\mid\mathbf m_k,\mathbf P_k)d\mathbf x$, $\mathbf P^{xx}_{k+1}=\int(\mathbf x-\mathbf m_k)(\mathbf f(\mathbf x)-\boldsymbol\mu^-_{k+1})^{\mathsf T}\mathrm N\,d\mathbf x$, $\mathbf P^x_{k+1}=\int(\mathbf f(\mathbf x)-\boldsymbol\mu^-_{k+1})(\cdot)^{\mathsf T}\mathrm N\,d\mathbf x+\mathbf Q_k$ (14.29). Then RTS smoothing of the affine model:
$$\mathbf m^-_{k+1}=\mathbf A_k\mathbf m_k+\mathbf a_k,\ \ \mathbf P^-_{k+1}=\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}+\boldsymbol\Lambda_k,\ \ \mathbf G_k=\mathbf P_k\mathbf A_k^{\mathsf T}[\mathbf P^-_{k+1}]^{-1},$$
and $\mathbf m^s_k,\mathbf P^s_k$ as in (14.1) (14.30).

**Equivalence.** Comparing (14.28) with (14.30): $\mathbf m^-_{k+1}=\boldsymbol\mu^-_{k+1}$ and $\mathbf P^-_{k+1}=\mathbf P^x_{k+1}$. With $\mathbf D_{k+1}=\mathbf P_k\mathbf A_k^{\mathsf T}$ one gets the relation of $\mathbf D_{k+1}$ to the cross-moment (the page prints $\mathbf P^x_{k+1}$; by (14.28) this is $\mathbf P^{xx}_{k+1}$, see Reading notes). Then (14.29) matches the first three lines of (14.1), so the redundant equations drop out and Algorithm 14.15 reduces to Algorithm 14.1 (p. 292). The same holds for non-additive models and Algorithm 14.2. In general, linearizing the dynamic model with respect to the filtering density gives the same result as the corresponding Gaussian RTS smoother (p. 293).

*Intuition note.* A Gaussian smoother can be read as "fit an affine model to $\mathbf f$ by regression over the filtering density, then run the exact linear smoother". This view makes it possible to choose other densities to fit over, as in 14.7.

**Five moment expressions.** A Gaussian smoother needs $\mathbf m^-_{k+1}=\mathbb E[\mathbf x_{k+1}\mid\mathbf y_{1:k}]$, $\mathbf P^-_{k+1}=\mathrm{Cov}[\mathbf x_{k+1}\mid\mathbf y_{1:k}]$ and $\mathbf D_{k+1}=\mathrm{Cov}[\mathbf x_k,\mathbf x_{k+1}\mid\mathbf y_{1:k}]$. Chapter 9 gives five expressions: one for additive models (9.1), and two each for non-additive (9.9) and conditional-distribution (9.10) models. Two were used in Algs. 8.3 and 8.4. A third is used below. The other two are the conditional-moment forms, left to Exercise 14.3 (p. 293).

**Algorithm 14.16 (Gaussian RTS smoother III, $p(\mathbf x_{k+1}\mid\mathbf x_k)$ given)** (p. 293):
$$\mathbf m^-_{k+1}=\int\mathbf x_{k+1}p(\mathbf x_{k+1}\mid\mathbf x_k)\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)d\mathbf x_{k+1}d\mathbf x_k,$$
$\mathbf P^-_{k+1}=\int(\mathbf x_{k+1}-\mathbf m^-_{k+1})(\cdot)^{\mathsf T}p\,\mathrm N\,d\mathbf x_{k+1}d\mathbf x_k$, $\mathbf D_{k+1}=\int(\mathbf x_k-\mathbf m_k)(\mathbf x_{k+1}-\mathbf m^-_{k+1})^{\mathsf T}p\,\mathrm N\,d\mathbf x_{k+1}d\mathbf x_k$ (14.31), then $\mathbf G_k,\mathbf m^s_k,\mathbf P^s_k$ as in (14.1).

**Algorithm 14.17 (Monte Carlo RTS smoother).** The integrals in (14.31) might not have closed form, so approximate them by sampling (p. 294):
$$\mathbf x_k^{(i)}\sim\mathrm N(\mathbf m_k,\mathbf P_k),\quad\mathbf x_{k+1}^{(i)}\sim p(\mathbf x_{k+1}\mid\mathbf x_k^{(i)}),\quad i=1,\dots,N\tag{14.32–14.33}$$
$$\mathbf m^-_{k+1}=\tfrac1N\sum\mathbf x^{(i)}_{k+1},\ \ \mathbf P^-_{k+1}=\tfrac1N\sum(\mathbf x^{(i)}_{k+1}-\mathbf m^-_{k+1})(\cdot)^{\mathsf T},\ \ \mathbf D_{k+1}=\tfrac1N\sum(\mathbf x^{(i)}_k-\mathbf m_k)(\mathbf x^{(i)}_{k+1}-\mathbf m^-_{k+1})^{\mathsf T}\tag{14.34}$$
followed by the RTS backward recursion (14.35).

**Remark** (p. 294). The Gaussian smoothers so far use the same linearizations as the Gaussian filters, since both do SLR over the filtering distribution. So if Alg. 9.20 is used for filtering, with explicit linearizations, those linearizations can be used directly in RTS smoothing (Thm. 12.5). This gives the same result as Alg. 8.3 followed by Alg. 14.1.

### 14.7 Posterior linearization smoothers (pp. 294–304)
**Generalized SLR.** Nothing forces linearization over the filtering distribution. Let $\pi^{\mathbf f}_k(\mathbf x_k)$ and $\pi^{\mathbf h}_k(\mathbf x_k)$ be linearization distributions for the dynamic and measurement models, with means $\mathbf m^{\mathbf f}_k,\mathbf m^{\mathbf h}_k$ and covariances $\mathbf P^{\mathbf f}_k,\mathbf P^{\mathbf h}_k$. Given the linearized models, affine Kalman filtering and RTS smoothing give the smoothing distributions (pp. 294–295).

**Algorithm 14.18 (generalized SLR smoother, additive noise)** (pp. 295–296).
1. For $k=0,\dots,T-1$, with $\mathbf x_k\sim\pi^{\mathbf f}_k$: $\boldsymbol\mu^-_{k+1}=\int\mathbf f\,\pi^{\mathbf f}_k$, $\mathbf P^{xx}_{k+1}=\int(\mathbf x-\mathbf m^{\mathbf f}_k)(\mathbf f(\mathbf x)-\boldsymbol\mu^-_{k+1})^{\mathsf T}\pi^{\mathbf f}_k$, $\mathbf P^x_{k+1}=\int(\mathbf f-\boldsymbol\mu^-_{k+1})(\cdot)^{\mathsf T}\pi^{\mathbf f}_k+\mathbf Q_k$ (14.36). Then
$$\mathbf A_k=(\mathbf P^{xx}_{k+1})^{\mathsf T}(\mathbf P^{\mathbf f}_k)^{-1},\ \ \mathbf a_k=\boldsymbol\mu^-_{k+1}-\mathbf A_k\mathbf m^{\mathbf f}_k,\ \ \boldsymbol\Lambda_k=\mathbf P^x_{k+1}-\mathbf A_k\mathbf P^{\mathbf f}_k\mathbf A_k^{\mathsf T}\tag{14.37}$$
2. For $k=1,\dots,T$, with $\mathbf x_k\sim\pi^{\mathbf h}_k$: $\boldsymbol\mu^+_k=\int\mathbf h\,\pi^{\mathbf h}_k$, $\mathbf P^{xy}_k=\int(\mathbf x-\mathbf m^{\mathbf h}_k)(\mathbf h-\boldsymbol\mu^+_k)^{\mathsf T}\pi^{\mathbf h}_k$, $\mathbf P^y_k=\int(\mathbf h-\boldsymbol\mu^+_k)(\cdot)^{\mathsf T}\pi^{\mathbf h}_k+\mathbf R_k$ (14.38). Then
$$\mathbf H_k=(\mathbf P^{xy}_k)^{\mathsf T}(\mathbf P^{\mathbf h}_k)^{-1},\ \ \mathbf b_k=\boldsymbol\mu^+_k-\mathbf H_k\mathbf m^{\mathbf h}_k,\ \ \boldsymbol\Omega_k=\mathbf P^y_k-\mathbf H_k\mathbf P^{\mathbf h}_k\mathbf H_k^{\mathsf T}\tag{14.39}$$
3. Affine Kalman filter, $k=1,\dots,T$:
$\mathbf m^-_k=\mathbf A_{k-1}\mathbf m_{k-1}+\mathbf a_{k-1}$, $\mathbf P^-_k=\mathbf A_{k-1}\mathbf P_{k-1}\mathbf A_{k-1}^{\mathsf T}+\boldsymbol\Lambda_{k-1}$ (14.40); and
$$\boldsymbol\mu_k=\mathbf H_k\mathbf m^-_k+\mathbf b_k,\ \mathbf S_k=\mathbf H_k\mathbf P^-_k\mathbf H_k^{\mathsf T}+\boldsymbol\Omega_k,\ \mathbf K_k=\mathbf P^-_k\mathbf H_k^{\mathsf T}\mathbf S_k^{-1},\ \mathbf m_k=\mathbf m^-_k+\mathbf K_k(\mathbf y_k-\boldsymbol\mu_k),\ \mathbf P_k=\mathbf P^-_k-\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}\tag{14.41}$$
4. Affine RTS smoother with $\mathbf m^s_T=\mathbf m_T$, $\mathbf P^s_T=\mathbf P_T$; for $k=T-1,\dots,0$: $\mathbf m^-_{k+1}=\mathbf A_k\mathbf m_k+\mathbf a_k$, $\mathbf P^-_{k+1}=\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}+\boldsymbol\Lambda_k$, $\mathbf G_k=\mathbf P_k\mathbf A_k^{\mathsf T}(\mathbf P^-_{k+1})^{-1}$, then $\mathbf m^s_k,\mathbf P^s_k$ as in (14.1) (14.42).

**Posterior linearization idea** (p. 296). Linearizations should be accurate on average over the posterior of $\mathbf x_k$. For smoothing this suggests $\pi^{\mathbf f}_k=\pi^{\mathbf h}_k=p(\mathbf x_k\mid\mathbf y_{1:T})\simeq\mathrm N(\mathbf m^s_k,\mathbf P^s_k)$. These moments are the end product, so as in the posterior linearization filters one iterates with the current best moments. This gives the **iterated posterior linearization smoother** (IPLS; García-Fernández et al., 2017; Tronarp et al., 2018).

**Algorithm 14.19 (IPLS I, additive)** (pp. 297–298). Start from an initial guess $\mathbf m^{s,(0)}_{0:T},\mathbf P^{s,(0)}_{0:T}$. For $i=1,2,\dots$: repeat steps 1–4 of Algorithm 14.18, with $\pi^{\mathbf f}_k=\pi^{\mathbf h}_k=\mathrm N(\mathbf m^{s,(i-1)}_k,\mathbf P^{s,(i-1)}_k)$. The moments (14.43) and (14.45) are those of (14.36) and (14.38) with this density, and the linearizations $\mathbf A^{(i)}_k,\mathbf a^{(i)}_k,\boldsymbol\Lambda^{(i)}_k$ and $\mathbf H^{(i)}_k,\mathbf b^{(i)}_k,\boldsymbol\Omega^{(i)}_k$ are (14.44) and (14.46). The Kalman filter starts from $\mathbf m^{(i)}_0=\mathbf m_0$, $\mathbf P^{(i)}_0=\mathbf P_0$ (14.47–14.48). The RTS smoother (14.49) starts from $\mathbf m^{s,(i)}_T=\mathbf m^{(i)}_T$, $\mathbf P^{s,(i)}_T=\mathbf P^{(i)}_T$. At convergence the final iterate is the result.

**IPLS vs IPLF** (pp. 298–299).
- The IPLF does SLR with respect to the filtering density. The IPLS uses the smoothing density, so it uses all of $\mathbf y_{1:T}$ and may give much more accurate linearizations in the relevant regions.
- The IPLF only improves the measurement-model linearization, one time step at a time. The IPLS iteratively updates both models at all time steps.

**IPLS vs IERTSS** (p. 299). Both linearize around the current smoothed approximation and then run an RTS smoother. The difference is that the IEKS (the text's name here) uses first-order Taylor expansions about the smoothed mean, while the IPLS uses SLR with respect to the smoothed posterior.

**Algorithm 14.20 (IPLS II, conditional moments)** (pp. 299–300). Assume one can compute $\boldsymbol\mu^-_k(\mathbf x_{k-1})=\mathbb E[\mathbf x_k\mid\mathbf x_{k-1}]$, $\mathbf P^x_k(\mathbf x_{k-1})=\mathrm{Cov}[\mathbf x_k\mid\mathbf x_{k-1}]$, $\boldsymbol\mu_k(\mathbf x_k)=\mathbb E[\mathbf y_k\mid\mathbf x_k]$, $\mathbf P^y_k(\mathbf x_k)=\mathrm{Cov}[\mathbf y_k\mid\mathbf x_k]$. Then it covers additive, non-additive and conditional-distribution models. Compared with 14.19, only the moments change. For the dynamic model (14.50):
$$\boldsymbol\mu^{-,(i-1)}_{k+1}=\int\boldsymbol\mu^-_k(\mathbf x)\,\mathrm N(\mathbf x\mid\mathbf m^{s,(i-1)}_k,\mathbf P^{s,(i-1)}_k)d\mathbf x,\quad\mathbf P^{xx,(i-1)}_{k+1}=\int(\mathbf x-\mathbf m^{s,(i-1)}_k)(\boldsymbol\mu^-_k(\mathbf x)-\boldsymbol\mu^{-,(i-1)}_{k+1})^{\mathsf T}\mathrm N\,d\mathbf x,$$
$$\mathbf P^{x,(i-1)}_{k+1}=\int(\boldsymbol\mu^-_k(\mathbf x)-\boldsymbol\mu^{-,(i-1)}_{k+1})(\cdot)^{\mathsf T}\mathrm N\,d\mathbf x+\int\mathbf P^x_k(\mathbf x)\mathrm N\,d\mathbf x.$$
The measurement moments (14.51) are analogous, with $\boldsymbol\mu_k(\mathbf x)$ and $\int\mathbf P^y_k(\mathbf x)\mathrm N\,d\mathbf x$. Linearization uses (14.44) and (14.46), and steps 3–4 use (14.47)–(14.49).

**Algorithm 14.21 (sigma-point IPLS I, additive)** (pp. 301–302). To approximate the integrals of (14.43), (14.45): for $j=1,\dots,m$ form points $\mathcal X^{(j)}_k=\mathbf m^{s,(i-1)}_k+\sqrt{\mathbf P^{s,(i-1)}_k}\boldsymbol\xi^{(j)}$ with weights $W_j$ (14.52, 14.55). Propagate $\mathcal X^{-(j)}_{k+1}=\mathbf f(\mathcal X^{(j)}_k)$ (14.53) and $\mathcal Y^{(j)}_k=\mathbf h(\mathcal X^{(j)}_k)$ (14.56). Then
$$\boldsymbol\mu^{-,(i-1)}_{k+1}=\sum_jW_j\mathcal X^{-(j)}_{k+1},\ \mathbf P^{xx,(i-1)}_{k+1}=\sum_jW_j(\mathcal X^{(j)}_k-\mathbf m^{s,(i-1)}_k)(\mathcal X^{-(j)}_{k+1}-\boldsymbol\mu^{-,(i-1)}_{k+1})^{\mathsf T},$$
$$\mathbf P^{x,(i-1)}_{k+1}=\sum_jW_j(\mathcal X^{-(j)}_{k+1}-\boldsymbol\mu^{-,(i-1)}_{k+1})(\cdot)^{\mathsf T}+\mathbf Q_k\tag{14.54}$$
and the same for $\boldsymbol\mu^{+}_k,\mathbf P^{xy}_k,\mathbf P^y_k$ with $\mathcal Y^{(j)}_k$ and $+\mathbf R_k$ (14.57). Steps (iv), 3 and 4 use (14.44), (14.46), (14.47)–(14.49). The initial trajectory guess is commonly made with a sigma-point RTS smoother (p. 302).

**Algorithm 14.22 (sigma-point IPLS II, conditional moments).** Same points as in 14.21. Propagate through the conditional mean and covariance functions: $\boldsymbol\mu^{-,(j)}_{k+1}=\boldsymbol\mu^-_k(\mathcal X^{(j)}_k)$, $\mathbf P^{x,(j)}_{k+1}=\mathbf P^x_k(\mathcal X^{(j)}_k)$ (14.59), and likewise for the measurement model (14.62). The moments are weighted sums as in (14.54), (14.57), but with the extra term $\sum_jW_j\mathbf P^{x,(j)}_{k+1}$ in $\mathbf P^x_{k+1}$ (14.60) and $\sum_jW_j\mathbf P^{y,(j)}_k$ in $\mathbf P^y_k$ (14.63) (pp. 302–304). Any integration method from Ch. 8 or earlier in this chapter may be used (p. 304).

**Example 14.23.** IPLS with Gauss–Hermite integration on the pendulum has RMSE 0.03, matching IERTSS (p. 304, Fig. 14.6).
**Example 14.24.** Iterated posterior linearization smoothers on the coordinated turn model (the text cites Example 7.11) with GH, spherical cubature, unscented and fifth-order cubature integration all give RMSE 0.015. IERTSS also gives 0.015 (p. 304, Fig. 14.7).

*Intuition note.* Each IPLS iteration asks "where do I think the state is, given all data?" and linearizes the models around that region. The new smoothed estimate then moves the region. The IPLS repeats this until the estimates stop changing.

### 14.8 Exercises (pp. 305–307)
Implementation and derivation exercises on the algorithms above (listed below).

## Toy example (ours, not from the text)
Scalar model $x_{k+1}=x_k^2+q_k$, $q_k\sim\mathrm N(0,Q)$ with $Q=1$. Filter result $m_k=1$, $P_k=1$. Smoothed result at $k+1$: $m^s_{k+1}=3$, $P^s_{k+1}=2$. Use the cubature rule with $n=1$: points $\xi=\pm1$, weights $\tfrac12$ each.
- Sigma points: $\mathcal X=1\pm1=\{2,0\}$. Propagated: $\{4,0\}$.
- $m^-=\tfrac12(4+0)=2$. $P^-=\tfrac12[(4-2)^2+(0-2)^2]+1=4+1=5$.
- $D=\tfrac12[(2-1)(4-2)+(0-1)(0-2)]=\tfrac12(2+2)=2$.
- $G=D/P^-=2/5=0.4$.
- $m^s_k=1+0.4(3-2)=1.4$. $P^s_k=1+0.4^2(2-5)=1-0.48=0.52$.

SLR check (as in 14.6): $A=D/P_k=2$, $a=m^--Am_k=2-2=0$, $\Lambda=P^--AP_kA=5-4=1$. The affine model $x_{k+1}=2x_k+\epsilon$ gives $A m_k+a=2$ and $AP_kA+\Lambda=5$, the same $m^-,P^-$. Also $G=P_kA/P^-=2/5$, the same gain. The cubature rule is approximate. For this $f$ the exact variance of $x^2$ under $\mathrm N(1,1)$ is $6$, not $4$.

## Concepts
- [[gaussian-rts-smoother]] (new) — Backward recursion $\mathbf m^s_k=\mathbf m_k+\mathbf G_k(\mathbf m^s_{k+1}-\mathbf m^-_{k+1})$ with moments from Gaussian moment matching (p. 279).
- [[cross-covariance-D]] (new) — $\mathbf D_{k+1}$, covariance of $(\mathbf x_k,\mathbf x_{k+1})$ given $\mathbf y_{1:k}$. It gives the smoother gain $\mathbf G_k=\mathbf D_{k+1}[\mathbf P^-_{k+1}]^{-1}$ (p. 279).
- [[sigma-points]] (new) — Deterministic points and weights approximating Gaussian integrals: GH, cubature, UT, fifth order (pp. 281–289).
- [[statistical-linear-regression]] (new) — Affine approximation of a function obtained by regression over a chosen distribution. It is used here to linearize the dynamic (and measurement) models (p. 291).
- [[posterior-linearization]] (new) — Linearizing over the posterior, here the smoothing density $\mathrm N(\mathbf m^s_k,\mathbf P^s_k)$, found iteratively (p. 296).
- [[iterated-posterior-linearization-smoother]] (new) — IPLS: repeats SLR, Kalman filter and RTS smoother until convergence (p. 297).
- [[linearization]] — Approximating non-linear models by affine ones. Taylor (extended) or SLR (Gaussian) here (p. 291).
- [[kalman-filter]] — The affine filter run on the linearized model in the IPLS (p. 296).
- [[observer]] — Smoothers likewise reconstruct hidden state from measurements, here using all of $\mathbf y_{1:T}$ (p. 279).

## Canonical instances
- [[pendulum-tracking]] — Example 7.6 reused to compare filters and smoothers (RMSE 0.10, 0.06, 0.03, 0.04) (pp. 281, 304).
- [[coordinated-turn-model]] — Tracking with RMSEs 0.016 (non-iterated) and 0.015 (iterated) (pp. 290, 304).

## Bridges (candidates)
- [structural-analogy] RTS backward recursion ↔ control: the backward pass of dynamic programming/Bellman recursion — both run backward from the final time $T$ using a one-step relation.
- [structural-analogy] Smoother gain $\mathbf G_k$ ↔ control: Kalman gain — both weight a correction by relative uncertainty.
- [structural-analogy] SLR as an affine fit averaged over a density ↔ Jacobian linearization: SLR replaces the Taylor expansion at a point (p. 291) by a fit over a density. Not the same math in general.
- [structural-analogy] IPLS iteration (relinearize, resolve, repeat) ↔ control: iterative linearization for non-linear trajectory optimization — plausible, not stated in the text.

## Questions this raises
- When the smoothing density is far from Gaussian (e.g. multimodal), what do the SLR and IPLS approximations lose?
- Does the IPLS always converge, and does the limit depend on the initial guess $\mathbf m^{s,(0)}_{0:T}$?
- How should one choose between cubature, unscented parameters ($\alpha,\beta,\kappa$) and Gauss–Hermite for a given state dimension?
- Is there a control-theoretic dual in which the smoother gain plays the role of a feedback gain?

## Exercises worth doing
- Ex. 14.2 (p. 305) — Non-additive Gaussian smoother using conditional moments (modify Alg. 14.2) — difficulty: medium
- Ex. 14.3 (p. 305) — Smoother with conditional moments analogous to Alg. 14.16 — difficulty: medium
- Ex. 14.4 (p. 305) — Derive the statistically linearized RTS smoother, following the ERTSS derivation — difficulty: hard
- Ex. 14.7 (p. 305) — Cubature-based smoother for bearings-only tracking; compare with filters — difficulty: medium
- Ex. 14.11 (p. 306) — IPLS for the non-additive model (9.9); only the moment expressions change — difficulty: medium
- Ex. 14.12 (p. 306) — Cubature IPLS for bearings-only tracking, compared with other smoothers — difficulty: medium

## Reading notes
- Printed page = pdf page − 30 (pdf 308 = p. 278). Pages are from a Cambridge University Press pre-publication version, with copyright 2023 printed in the header.
- The text layer drops minus signs and some symbols; equations here were checked against the images.
- Misprint, p. 292: the sentence after Alg. 14.15 says "$\mathbf D_{k+1}=\mathbf P^x_{k+1}$". From (14.28), $\mathbf D_{k+1}=\mathbf P_k\mathbf A_k^{\mathsf T}=\mathbf P^{xx}_{k+1}$ (added step: $\mathbf P_k\mathbf P_k^{-1}\mathbf P^{xx}_{k+1}$). I have read it that way.
- Misprint, p. 292, (14.30): the image shows $\mathbf m^-_{k+1}=\mathbf A_k\mathbf m_k+\mathbf a_{k-1}$. By (14.28) and (14.42) this should be $\mathbf a_k$.
- Example 14.24 (p. 304) cites Example 7.11 for the coordinated turn model, while Example 14.14 (p. 290) cites Example 7.7. I do not know whether these are the same model.
- On p. 299 the IERTSS is called "IEKS" in one sentence. The sentence on p. 304 "…in Chapter 8 are then later in the start of this chapter" is garbled. The algorithm end-lines show a typo "$\mathbf m^{s,}_{1:T}$" (p. 298).
- Algorithms 14.19, 14.20, 14.21, 14.22 repeat the same equations with different moment formulas. I wrote them once and listed the differences.
