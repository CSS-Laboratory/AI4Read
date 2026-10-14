---
id: sarkka-2023-bayesianfiltering/ch09-gaussian
work: sarkka-2023-bayesianfiltering
unit: "9 Gaussian Filtering by Enabling Approximations"
pages: 168–203
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Gaussian Filtering by Enabling Approximations

## L0 — One line
The Gaussian filters of the book (EKF, IEKF, UKF, CKF, GHKF, …) can arguably all be seen as an affine, additive-Gaussian-noise approximation of the models followed by the exact Kalman filter, so the main difference between them is how that "enabling" linearization is chosen.

## L1 — The gist (≤ 120 words)
The EKF (Chapter 7) and the moment-matching filters (Chapter 8) look different. This chapter shows that they share two steps: approximate the models as affine with additive Gaussian noise, then run the closed-form Kalman filter. Statistical linearization (SL) is a noise-free affine fit, and its covariance is generally smaller than the one moment matching gives. Statistical linear regression (SLR) adds noise equal to the fit error. It reproduces the Chapter 8 moment-matching filters exactly. SLR also extends to non-additive and conditional-distribution models. This gives new filters: a sigma-point conditional-moment filter and a Monte Carlo Kalman filter. The result is a unified view of the Gaussian filter family.

**Prerequisites:** Kalman filter prediction/update equations (affine form); Gaussian joint/conditional moments; Jacobians; expectations and covariances; law of iterated expectations; sigma-point/cubature integration (Chapter 8). Acronyms used in L0–L2: EKF/IEKF = (iterated) extended Kalman filter, UKF = unscented Kalman filter, CKF = cubature Kalman filter, GHKF = Gauss–Hermite Kalman filter (all Chapters 7–8); EKF2 = second-order EKF, FHKF = Fourier–Hermite Kalman filter, GPQF = Gaussian process quadrature filter, MCKF = Monte Carlo Kalman filter.

## L2 — Key ideas
- Algorithm 9.1: any Gaussian filter that approximates models as affine plus Gaussian noise, then applies the Kalman equations, is covered. The EKF and IEKF are special cases with Taylor expansions at different linearization points (p. 169–170).
- The enabling approximation is flexible. It need not be a Taylor expansion, and the noise covariances may be set larger than $\mathbf Q$, $\mathbf R$ to absorb linearization error (p. 170).
- Statistical linearization (SL) picks $\mathbf A,\mathbf b$ to minimize the mean squared error over a distribution. It differs from a Taylor expansion because it uses $\mathrm E[\mathbf G_{\mathbf x}(\mathbf x)]$ and $\mathrm E[\mathbf g(\mathbf x)]$ instead of values at the mean (p. 171–174).
- For an additive transform, SL gives the same mean and cross-covariance as moment matching but a covariance that is generally smaller (the author's stated cause is the deterministic, noise-free approximation). It is therefore likely to underestimate uncertainty (p. 173).
- SLR keeps the SL values of $\mathbf A,\mathbf b$ and adds noise $\boldsymbol\Lambda=\mathbf S_R-\mathbf A\mathbf P\mathbf A^{\mathsf T}$. For $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$ it reproduces moment matching exactly (p. 179–181).
- SLR can be written with conditional moments $\mathrm E[\mathbf y\mid\mathbf x]$ and $\mathrm{Cov}[\mathbf y\mid\mathbf x]$. This covers additive, non-additive and conditional-distribution models (p. 183–185).
- The additive-noise SLR filter Alg. 9.21 is identical to Alg. 8.3, and its non-additive version gives Alg. 8.4 after simplification. The general Gaussian filters of Chapter 8 (e.g. UKF, CKF, GHKF) therefore implicitly use SLR (p. 188–189). Alg. 9.22–9.23 extend SLR filtering to conditional-moment and conditional-distribution models (p. 190–192).
- Practical outcomes are the sigma-point conditional-moment filter (Alg. 9.24, 9.27) and the Monte Carlo Kalman filter (Alg. 9.25). In one Poisson example MCKF beat CKF slightly, at higher cost (p. 193–200).
- Higher-order filters (EKF2, FHKF, GPQF) can be argued to be SLR filters. The series expansions only help approximate integrals, and SLR remains the enabling approximation (p. 201).

## L3 — Walkthrough

### Chapter introduction (p. 168)
The EKF linearizes the models and then applies a Kalman filter. The Chapter 8 moment-matching filters use numerical integration, but can also be viewed as ways to linearize the models. These linearizations are called *enabling approximations*, because they enable the closed-form Kalman prediction and update (p. 168). Most filters that approximate the posterior recursively as Gaussian combine two steps (p. 168):
1. Approximate the measurement and dynamic models as linear (affine) with additive Gaussian noise.
2. Use the Kalman filter equations for prediction and update.

Step 2 is identical for all filters. The difference lies in how the models are linearized. This view also allows new filters, such as the posterior linearization filters of Chapter 10 (p. 168).

### 9.1 Enabling Linearization (p. 169–171)
Model with additive noise (p. 169):
$$\mathbf x_k=\mathbf f(\mathbf x_{k-1})+\mathbf q_{k-1},\ \mathbf q_{k-1}\sim\mathrm N(\mathbf 0,\mathbf Q_{k-1});\qquad \mathbf y_k=\mathbf h(\mathbf x_k)+\mathbf r_k,\ \mathbf r_k\sim\mathrm N(\mathbf 0,\mathbf R_k)\tag{9.1}$$
Assumed affine Gaussian approximation, with constant matrices $\mathbf A_{k-1},\mathbf H_k$ and constant vectors $\mathbf a_{k-1},\mathbf b_k$ (p. 169):
$$\mathbf x_k\simeq\mathbf A_{k-1}\mathbf x_{k-1}+\mathbf a_{k-1}+\tilde{\mathbf e}_{k-1},\quad \mathbf y_k\simeq\mathbf H_k\mathbf x_k+\mathbf b_k+\tilde{\mathbf v}_k,\tag{9.2}$$
with $\tilde{\mathbf e}_{k-1}\sim\mathrm N(\mathbf 0,\boldsymbol\Lambda_{k-1})$ and $\tilde{\mathbf v}_k\sim\mathrm N(\mathbf 0,\boldsymbol\Omega_k)$. If $\boldsymbol\Lambda,\boldsymbol\Omega$ are full rank, this is equivalent to the densities
$$p(\mathbf x_k\mid\mathbf x_{k-1})\simeq\mathrm N(\mathbf x_k\mid\mathbf A_{k-1}\mathbf x_{k-1}+\mathbf a_{k-1},\boldsymbol\Lambda_{k-1}),\quad p(\mathbf y_k\mid\mathbf x_k)\simeq\mathrm N(\mathbf y_k\mid\mathbf H_k\mathbf x_k+\mathbf b_k,\boldsymbol\Omega_k).\tag{9.3}$$
A function $\mathbf A\mathbf x+\mathbf a$ is *affine* for all $\mathbf a$, and *linear* only if $\mathbf a=\mathbf 0$ (p. 169, footnote). The affine Kalman filter (Theorem 6.9) then gives closed-form steps (p. 169).

**Algorithm 9.1 (Gaussian filtering with enabling linearizations)** (p. 169–170).
- *Prediction:* find $\mathbf A_{k-1},\mathbf a_{k-1},\boldsymbol\Lambda_{k-1}$ with $\mathbf x_k\simeq\mathbf A_{k-1}\mathbf x_{k-1}+\mathbf a_{k-1}+\tilde{\mathbf e}_{k-1}$ (9.4). Then
$$\mathbf m_k^-=\mathbf A_{k-1}\mathbf m_{k-1}+\mathbf a_{k-1},\qquad \mathbf P_k^-=\mathbf A_{k-1}\mathbf P_{k-1}\mathbf A_{k-1}^{\mathsf T}+\boldsymbol\Lambda_{k-1}.\tag{9.5}$$
- *Update:* find $\mathbf H_k,\mathbf b_k,\boldsymbol\Omega_k$ with $\mathbf y_k\simeq\mathbf H_k\mathbf x_k+\mathbf b_k+\tilde{\mathbf v}_k$ (9.6). Then
$$\begin{aligned}\boldsymbol\mu_k&=\mathbf H_k\mathbf m_k^-+\mathbf b_k,\\ \mathbf S_k&=\mathbf H_k\mathbf P_k^-\mathbf H_k^{\mathsf T}+\boldsymbol\Omega_k,\\ \mathbf K_k&=\mathbf P_k^-\mathbf H_k^{\mathsf T}\mathbf S_k^{-1},\\ \mathbf m_k&=\mathbf m_k^-+\mathbf K_k(\mathbf y_k-\boldsymbol\mu_k),\\ \mathbf P_k&=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}.\end{aligned}\tag{9.7}$$

**EKF and IEKF as special cases** (additive-noise case verified, p. 170). Both use for the prediction $\mathbf A_{k-1}=\mathbf F_{\mathbf x}(\mathbf m_{k-1})$, $\mathbf a_{k-1}=\mathbf f(\mathbf m_{k-1})-\mathbf F_{\mathbf x}(\mathbf m_{k-1})\mathbf m_{k-1}$ and $\boldsymbol\Lambda_{k-1}=\mathbf Q_{k-1}$. This is the first-order Taylor expansion
$$\mathbf f(\mathbf x_{k-1})\simeq\mathbf f(\mathbf m_{k-1})+\mathbf F_{\mathbf x}(\mathbf m_{k-1})(\mathbf x_{k-1}-\mathbf m_{k-1}).\tag{9.8}$$
For the update, with linearization point $\bar{\mathbf m}_k$: $\mathbf H_k=\mathbf H_{\mathbf x}(\bar{\mathbf m}_k)$, $\mathbf b_k=\mathbf h(\bar{\mathbf m}_k)-\mathbf H_{\mathbf x}(\bar{\mathbf m}_k)\bar{\mathbf m}_k$, $\boldsymbol\Omega_k=\mathbf R_k$. The EKF uses $\bar{\mathbf m}_k=\mathbf m_k^-$. The IEKF seeks to set $\bar{\mathbf m}_k$ to the maximum a posteriori estimate of $\mathbf x_k$ (p. 170).

Enabling approximations are more flexible than Taylor expansions. We may want accuracy over a range of values, and we may choose $\boldsymbol\Lambda_{k-1},\boldsymbol\Omega_k$ larger than $\mathbf Q_{k-1},\mathbf R_k$ to acknowledge linearization error (p. 170).

Three model families are considered (p. 170–171): additive (9.1); non-additive, $\mathbf x_k=\mathbf f(\mathbf x_{k-1},\mathbf q_{k-1})$, $\mathbf y_k=\mathbf h(\mathbf x_k,\mathbf r_k)$ with Gaussian noises (9.9); and conditional distributions $\mathbf x_k\sim p(\mathbf x_k\mid\mathbf x_{k-1})$, $\mathbf y_k\sim p(\mathbf y_k\mid\mathbf x_k)$ (9.10). Some principles give filters identical to Chapter 8, others give new filters (p. 171).

### 9.2 Statistical Linearization (p. 171–176)
**Definition 9.2.** $\mathbf y\simeq\mathbf A\mathbf x+\mathbf b$ is a statistical linearization (SL) if deterministic $\mathbf A,\mathbf b$ minimize
$$\mathrm{MSE}(\mathbf A,\mathbf b)=\mathrm E\big[(\mathbf y-\mathbf A\mathbf x-\mathbf b)^{\mathsf T}(\mathbf y-\mathbf A\mathbf x-\mathbf b)\big].\tag{9.11}$$
The approximation is affine and noise free (p. 171).

**Theorem 9.3.** Let $\mathbf m=\mathrm E[\mathbf x]$, $\mathbf P=\mathrm{Cov}[\mathbf x]$, $\boldsymbol\mu_S=\mathrm E[\mathbf y]$, $\mathbf C_S=\mathrm{Cov}[\mathbf x,\mathbf y]$. The MSE is minimized by
$$\mathbf A=\mathbf C_S^{\mathsf T}\mathbf P^{-1},\qquad \mathbf b=\boldsymbol\mu_S-\mathbf A\mathbf m.\tag{9.13}$$
Proof: set the derivatives of the MSE with respect to $\mathbf A$ and $\mathbf b$ to zero (p. 171).

*Intuition note:* SL is the best affine predictor of $\mathbf y$ from $\mathbf x$ in the average-squared-error sense. It depends on the whole distribution of $\mathbf x$, not just on its mean.

**Corollary 9.4.** If $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$, SL gives the Gaussian approximation
$$\begin{pmatrix}\mathbf x\\\mathbf y\end{pmatrix}\sim\mathrm N\left(\begin{pmatrix}\mathbf m\\\boldsymbol\mu_S\end{pmatrix},\begin{pmatrix}\mathbf P&\mathbf C_S\\\mathbf C_S^{\mathsf T}&\mathbf S_S\end{pmatrix}\right),\quad \mathbf S_S=\mathbf A\mathbf P\mathbf A^{\mathsf T}.\tag{9.14}$$
Proof: insert $\mathbf A,\mathbf b$ into $\mathbf A\mathbf x+\mathbf b$; e.g. $\mathrm{Cov}[\mathbf x,\mathbf A\mathbf x+\mathbf b]=\mathrm{Cov}[\mathbf x,\mathbf x]\mathbf A^{\mathsf T}=\mathbf C_S$ (p. 172).

**Corollary 9.5 (SL of a transformation).** For $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$ and $\mathbf y=\mathbf g(\mathbf x)$ (9.15), MSE (9.16) is minimized by
$$\mathbf A=\mathrm E[(\mathbf x-\mathbf m)\mathbf g(\mathbf x)^{\mathsf T}]^{\mathsf T}\mathbf P^{-1},\qquad \mathbf b=\mathrm E[\mathbf g(\mathbf x)]-\mathbf A\mathbf m.\tag{9.17}$$
Proof: special case of Theorem 9.3 with $\boldsymbol\mu_S=\mathrm E[\mathbf g(\mathbf x)]$ and
$$\mathbf C_S=\mathrm E[(\mathbf x-\mathbf m)(\mathbf g-\mathrm E[\mathbf g])^{\mathsf T}]=\mathrm E[(\mathbf x-\mathbf m)\mathbf g^{\mathsf T}]+\underbrace{\mathrm E[\mathbf x-\mathbf m]}_{=0}\mathrm E[\mathbf g]^{\mathsf T}=\mathrm E[(\mathbf x-\mathbf m)\mathbf g^{\mathsf T}].\tag{9.18}$$
(p. 172). Also $\mathrm E[(\mathbf x-\mathbf m)\mathbf g^{\mathsf T}]^{\mathsf T}=\mathrm E[\mathbf g(\mathbf x-\mathbf m)^{\mathsf T}]$ (p. 173).

**Corollary 9.6 (additive transform).** For $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$, $\mathbf q\sim\mathrm N(\mathbf 0,\mathbf Q)$, SL gives (9.19) with
$$\boldsymbol\mu_S=\mathrm E[\mathbf g],\quad \mathbf S_S=\mathrm E[\mathbf g(\mathbf x-\mathbf m)^{\mathsf T}]\mathbf P^{-1}\mathrm E[(\mathbf x-\mathbf m)\mathbf g^{\mathsf T}]+\mathbf Q,\quad \mathbf C_S=\mathrm E[(\mathbf x-\mathbf m)\mathbf g^{\mathsf T}],\tag{9.20}$$
with expectations over $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$ (p. 173).

**Comparison with moment matching** (p. 173). Written as integrals (9.21), $\boldsymbol\mu_S=\boldsymbol\mu_M$ and $\mathbf C_S=\mathbf C_M$ (compare (8.4)), but $\mathbf S_S\ne\mathbf S_M$. In fact $\mathbf S_S\le\mathbf S_M$, so the SL covariance is generally smaller and likely to underestimate the uncertainty in $\mathbf y$. The cause is the deterministic approximation, and SLR (Section 9.4) is the remedy (p. 173).

**Relation to Taylor expansion** (p. 174). For differentiable $\mathbf g$ and $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$ there is a Gaussian property, with $\mathbf G_{\mathbf x}$ the Jacobian:
$$\mathrm E[\mathbf g(\mathbf x)(\mathbf x-\mathbf m)^{\mathsf T}]=\mathrm E[\mathbf G_{\mathbf x}(\mathbf x)]\,\mathbf P.\tag{9.22}$$
Hence $\mathbf A=\mathrm E[\mathbf g(\mathbf x)(\mathbf x-\mathbf m)^{\mathsf T}]\mathbf P^{-1}=\mathrm E[\mathbf G_{\mathbf x}(\mathbf x)]$ (9.23). Compare
$$\text{Taylor: }\mathbf g(\mathbf x)\simeq\mathbf G_{\mathbf x}(\mathbf m)(\mathbf x-\mathbf m)+\mathbf g(\mathbf m)\tag{9.24}$$
$$\text{SL: }\mathbf g(\mathbf x)\simeq\mathrm E[\mathbf G_{\mathbf x}(\mathbf x)](\mathbf x-\mathbf m)+\mathrm E[\mathbf g(\mathbf x)]\tag{9.25}$$
Taylor uses $\mathbf G_{\mathbf x}(\mathrm E[\mathbf x])$ and $\mathbf g(\mathrm E[\mathbf x])$. SL uses $\mathrm E[\mathbf G_{\mathbf x}(\mathbf x)]$ and $\mathrm E[\mathbf g(\mathbf x)]$ (p. 174).

*Intuition note:* Taylor looks at the function only at the mean. SL averages the slope and the value over the whole input distribution, so it is a more "global" fit.

**Example 9.7** (p. 174–175). Take $g(x)=x^3$ and $x\sim\mathrm N(m,P)$ with $m=1$. Compare a Taylor expansion about $x=1$ with SL at $P=0.1$ and at $P=1$. The SL is $g(x)\simeq A(x-m)+\mu$ with $A=\mathrm E[G_x(x)]=\int 3x^2\mathrm N(x\mid m,P)\,\mathrm dx$ and $\mu=\int x^3\mathrm N(x\mid m,P)\,\mathrm dx$ (9.26). The SL with $P=0.1$ is similar to the Taylor expansion, and both are accurate near $x=1$. The SL with $P=1$ approximates $x^3$ over a larger range. All three lines differ even though all are made around $x=1$ (p. 174–175, Fig. 9.1).

**Non-additive noise** (p. 175–176). Applying SL directly to $\mathbf g(\mathbf x,\mathbf q)$ gives a deterministic $\mathbf A\mathbf x+\mathbf b$, which is generally undesirable. Instead, use $\mathbf z=(\mathbf x;\mathbf q)$ (9.27) and
$$\mathbf y\simeq\mathbf A^z\mathbf z+\mathbf b=(\mathbf A\ \ \mathbf A^q)\begin{pmatrix}\mathbf x\\\mathbf q\end{pmatrix}+\mathbf b=\mathbf A\mathbf x+\mathbf A^q\mathbf q+\mathbf b.\tag{9.28}$$
The term $\mathbf A^q\mathbf q$ acts as additive noise. For the dynamic model, $\mathbf f(\mathbf x_{k-1},\mathbf q_{k-1})\simeq\mathbf A\mathbf x_{k-1}+\mathbf A^q\mathbf q_{k-1}+\mathbf a_{k-1}$ (9.29). Setting $\tilde{\mathbf e}_{k-1}=\mathbf A^q\mathbf q_{k-1}$ gives $\boldsymbol\Lambda_{k-1}=\mathbf A^q\mathbf Q_{k-1}(\mathbf A^q)^{\mathsf T}$ (p. 176).

**Corollary 9.8 (SL III).** With independent $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$ and $\mathbf q\sim\mathrm N(\mathbf 0,\mathbf Q)$, the MSE (9.30) of $\mathbf g(\mathbf x,\mathbf q)\simeq\mathbf A\mathbf x+\mathbf A^q\mathbf q+\mathbf b$ is minimized by
$$\mathbf A=\mathrm{Cov}[\mathbf y,\mathbf x]\mathbf P^{-1}=\mathrm E[\mathbf g(\mathbf x-\mathbf m)^{\mathsf T}]\mathbf P^{-1},\ \ \mathbf A^q=\mathrm{Cov}[\mathbf y,\mathbf q]\mathbf Q^{-1}=\mathrm E[\mathbf g\mathbf q^{\mathsf T}]\mathbf Q^{-1},\ \ \mathbf b=\mathrm E[\mathbf g]-\mathbf A\mathbf m.\tag{9.31}$$
Proof: Theorem 9.3 applied to $\mathbf y$ and $\mathbf z$ (Exercise 9.10) (p. 176). SL can also be seen as the first-order Fourier–Hermite series expansion of the function with respect to the Gaussian. This allows quadratic and higher extensions, which are not discussed here (p. 176).

### 9.3 Statistically Linearized Filter (p. 176–178)
A statistically linearized filter (SLF, also called quasi-linear filter) is Algorithm 9.1 with SL as enabling approximation. It is like the EKF but with SL instead of Taylor series (p. 176).

**Algorithm 9.9 (SLF I, additive noise)** (p. 177), with $\delta\mathbf x_{k-1}=\mathbf x_{k-1}-\mathbf m_{k-1}$ and $\mathbf x_{k-1}\sim\mathrm N(\mathbf m_{k-1},\mathbf P_{k-1})$:
$$\mathbf m_k^-=\mathrm E[\mathbf f(\mathbf x_{k-1})],\quad \mathbf P_k^-=\mathrm E[\mathbf f\,\delta\mathbf x_{k-1}^{\mathsf T}]\mathbf P_{k-1}^{-1}\mathrm E[\mathbf f\,\delta\mathbf x_{k-1}^{\mathsf T}]^{\mathsf T}+\mathbf Q_{k-1}.\tag{9.32}$$
Update, with $\delta\tilde{\mathbf x}_k=\mathbf x_k-\mathbf m_k^-$ and $\mathbf x_k\sim\mathrm N(\mathbf m_k^-,\mathbf P_k^-)$:
$$\begin{aligned}\boldsymbol\mu_k&=\mathrm E[\mathbf h(\mathbf x_k)],\\ \mathbf S_k&=\mathrm E[\mathbf h\,\delta\tilde{\mathbf x}_k^{\mathsf T}](\mathbf P_k^-)^{-1}\mathrm E[\mathbf h\,\delta\tilde{\mathbf x}_k^{\mathsf T}]^{\mathsf T}+\mathbf R_k,\\ \mathbf K_k&=\mathrm E[\mathbf h\,\delta\tilde{\mathbf x}_k^{\mathsf T}]^{\mathsf T}\mathbf S_k^{-1},\end{aligned}\tag{9.33}$$
followed by $\mathbf m_k=\mathbf m_k^-+\mathbf K_k(\mathbf y_k-\boldsymbol\mu_k)$ and $\mathbf P_k=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}$ (p. 177).

**Algorithm 9.10 (SLF II, non-additive noise)** uses Corollary 9.8 (p. 177–178). Prediction:
$$\mathbf m_k^-=\mathrm E[\mathbf f(\mathbf x_{k-1},\mathbf q_{k-1})],$$
$$\mathbf P_k^-=\mathrm E[\mathbf f\,\delta\mathbf x_{k-1}^{\mathsf T}]\mathbf P_{k-1}^{-1}\mathrm E[\mathbf f\,\delta\mathbf x_{k-1}^{\mathsf T}]^{\mathsf T}+\mathrm E[\mathbf f\mathbf q_{k-1}^{\mathsf T}]\mathbf Q_{k-1}^{-1}\mathrm E[\mathbf f\mathbf q_{k-1}^{\mathsf T}]^{\mathsf T}.\tag{9.34}$$
The update is the same with $\mathbf h(\mathbf x_k,\mathbf r_k)$, $\delta\tilde{\mathbf x}_k$, $\mathbf R_k$ in place of $\mathbf f$, $\delta\mathbf x_{k-1}$, $\mathbf Q_{k-1}$. It has $\mathbf S_k=\mathrm E[\mathbf h\,\delta\tilde{\mathbf x}_k^{\mathsf T}](\mathbf P_k^-)^{-1}\mathrm E[\cdot]^{\mathsf T}+\mathrm E[\mathbf h\mathbf r_k^{\mathsf T}]\mathbf R_k^{-1}\mathrm E[\cdot]^{\mathsf T}$ (9.35). The gain and the $\mathbf m_k,\mathbf P_k$ equations are as in (9.33) (p. 178).

*Advantages* (p. 178): the SLF is a more global approximation than the EKF. The nonlinearities need not be differentiable, since no Jacobians appear. If they are differentiable, (9.22)–(9.23) give an EKF-like form.
*Disadvantage* (p. 178): the expectations must be known in closed form. Many are tabulated in older physics and control books. Otherwise Gaussian quadrature (Chapter 8) can be used (Exercise 9.3). But if expectations are computed numerically anyway, the author says SLR is better (p. 178).

### 9.4 Statistical Linear Regression (p. 178–186)
Motivation: even for $\mathbf y=\mathbf g(\mathbf x)$ it can be valuable to add Gaussian noise that reflects the affine approximation error. SL also failed to match the covariance of moment matching (p. 178–179). SLR includes a rule for the noise covariance (Arasaratnam et al., 2007), and is not deterministic, so it fits all three model families (p. 179).

**Definition 9.11.** $\mathbf y\simeq\mathbf A\mathbf x+\mathbf b+\tilde{\mathbf e}$, $\tilde{\mathbf e}\sim\mathrm N(\mathbf 0,\boldsymbol\Lambda)$ is an SLR if $\mathbf A,\mathbf b$ minimize the MSE
$$\mathrm{MSE}(\mathbf A,\mathbf b)=\mathrm E[(\mathbf y-\mathbf A\mathbf x-\mathbf b)^{\mathsf T}(\mathbf y-\mathbf A\mathbf x-\mathbf b)]\tag{9.36}$$
and the noise covariance is
$$\boldsymbol\Lambda=\mathrm E[(\mathbf y-\mathbf A\mathbf x-\mathbf b)(\mathbf y-\mathbf A\mathbf x-\mathbf b)^{\mathsf T}].\tag{9.37}$$
(p. 179).

**Theorem 9.12.** Let $\mathbf m=\mathrm E[\mathbf x]$, $\mathbf P=\mathrm{Cov}[\mathbf x]$, $\boldsymbol\mu_R=\mathrm E[\mathbf y]$, $\mathbf S_R=\mathrm{Cov}[\mathbf y]$, $\mathbf C_R=\mathrm{Cov}[\mathbf x,\mathbf y]$. Then
$$\mathbf A=\mathbf C_R^{\mathsf T}\mathbf P^{-1},\quad \mathbf b=\boldsymbol\mu_R-\mathbf A\mathbf m,\quad \boldsymbol\Lambda=\mathbf S_R-\mathbf A\mathbf P\mathbf A^{\mathsf T}.\tag{9.38}$$
Proof: $\mathbf A,\mathbf b$ follow from Theorem 9.3. For $\boldsymbol\Lambda$:
$$\boldsymbol\Lambda=\mathrm{Cov}[\mathbf y-\mathbf A\mathbf x-\mathbf b]=\mathrm E\big[(\mathbf y-\boldsymbol\mu_R-\mathbf A(\mathbf x-\mathbf m))(\mathbf y-\boldsymbol\mu_R-\mathbf A(\mathbf x-\mathbf m))^{\mathsf T}\big]=\mathrm{Cov}[\mathbf y]+\mathbf A\mathbf P\mathbf A^{\mathsf T}-\mathbf A\mathbf C_R-\mathbf C_R^{\mathsf T}\mathbf A^{\mathsf T}=\mathbf S_R-\mathbf A\mathbf P\mathbf A^{\mathsf T},\tag{9.39}$$
where the last equality uses $\mathbf C_R=\mathbf P\mathbf A^{\mathsf T}$, so both cross terms equal $\mathbf A\mathbf P\mathbf A^{\mathsf T}$ (added step) (p. 179–180).

**Corollary 9.13.** For $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$, SLR gives
$$\begin{pmatrix}\mathbf x\\\mathbf y\end{pmatrix}\sim\mathrm N\left(\begin{pmatrix}\mathbf m\\\boldsymbol\mu_R\end{pmatrix},\begin{pmatrix}\mathbf P&\mathbf C_R\\\mathbf C_R^{\mathsf T}&\mathbf S_R\end{pmatrix}\right).\tag{9.40}$$
Proof: $\mathbf A\mathbf x+\mathbf b+\tilde{\mathbf e}$ is Gaussian, with mean $(\mathbf m;\mathbf A\mathbf m+\mathbf b)=(\mathbf m;\boldsymbol\mu_R)$ and covariance $\begin{pmatrix}\mathbf P&\mathbf P\mathbf A^{\mathsf T}\\\mathbf A\mathbf P&\mathbf A\mathbf P\mathbf A^{\mathsf T}+\boldsymbol\Lambda\end{pmatrix}=\begin{pmatrix}\mathbf P&\mathbf C_R\\\mathbf C_R^{\mathsf T}&\mathbf S_R\end{pmatrix}$ (9.41) (p. 180).

So SLR matches the first two moments of the joint distribution (p. 180).

**Corollary 9.14 (SLR of an additive transform).** For $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$, the SLR has $\mathbf A,\mathbf b,\boldsymbol\Lambda$ as in (9.42) (= (9.38)), with
$$\boldsymbol\mu_R=\int\mathbf g\,\mathrm N\,\mathrm d\mathbf x,\quad \mathbf C_R=\int(\mathbf x-\mathbf m)(\mathbf g-\boldsymbol\mu_R)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x,\quad \mathbf S_R=\int(\mathbf g-\boldsymbol\mu_R)(\mathbf g-\boldsymbol\mu_R)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x+\mathbf Q,\tag{9.43}$$
where $\mathrm N=\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)$. The joint Gaussian is (9.44) (p. 180–181).

These integrals equal $\boldsymbol\mu_M,\mathbf C_M,\mathbf S_M$ of (8.4). SLR therefore gives the same approximation as Chapter 8 moment matching, and all numerical integration methods (Gauss–Hermite, cubature) apply (p. 181).

*Intuition note:* SLR fits the same line as SL, then adds noise sized to the leftover fit error. That keeps the covariance of $\mathbf y$ correct, which moment matching also does.

**SL vs SLR** (p. 181–182). They have the same $\mathbf A,\mathbf b$, $\boldsymbol\mu_R=\boldsymbol\mu_S$ and $\mathbf C_R=\mathbf C_S$. Since $\mathbf S_S=\mathbf A\mathbf P\mathbf A^{\mathsf T}$ and $\mathbf S_R=\mathbf A\mathbf P\mathbf A^{\mathsf T}+\boldsymbol\Lambda$ with $\boldsymbol\Lambda$ positive semi-definite, $\mathbf S_R\ge\mathbf S_S$. For $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$, SL takes $\boldsymbol\Lambda_{SL}=\mathbf Q$. SLR gives, since $\mathbf q$ has zero mean and is independent of $\mathbf x$,
$$\boldsymbol\Lambda=\mathrm E[(\mathbf g+\mathbf q-\mathbf A\mathbf x-\mathbf b)(\cdot)^{\mathsf T}]=\mathrm E[(\mathbf g-\mathbf A\mathbf x-\mathbf b)(\mathbf g-\mathbf A\mathbf x-\mathbf b)^{\mathsf T}]+\mathbf Q.\tag{9.45}$$
So SLR adds $\mathrm E[(\mathbf g-\mathbf A\mathbf x-\mathbf b)(\cdot)^{\mathsf T}]$ to the SL noise, representing the affine approximation error (p. 181–182).

Why SLR is still useful (p. 182): it unifies all Gaussian filters as linearizations of state space models, and it gives insights for new filters (Chapter 10).

**Example 9.15** (p. 182). Same setting as Example 9.7 with noise-free $y=x^3\simeq Ax+b+e$. $A,b$ are as in SL. The noise has $\sqrt\Lambda\approx4.86$ for $P=1$ and $\approx0.43$ for $P=0.1$. The error is smaller for small $P$, because $\Lambda$ is the variance of $g(x)-Ax-b$ and that error is generally smaller near $m$. As $P\to0$, both SL and SLR converge to the noise-free Taylor expansion $y\approx g(m)+G_x(m)(x-m)$ (p. 182).

**Conditional moments** (p. 182–183). If only $p(\mathbf y\mid\mathbf x)$ is given (possibly non-Gaussian), often we can compute
$$\boldsymbol\mu_R(\mathbf x)=\mathrm E[\mathbf y\mid\mathbf x]=\int\mathbf y\,p(\mathbf y\mid\mathbf x)\,\mathrm d\mathbf y,\qquad \mathbf S_R(\mathbf x)=\mathrm{Cov}[\mathbf y\mid\mathbf x].\tag{9.46}$$
For $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$: $\boldsymbol\mu_R(\mathbf x)=\mathbf g(\mathbf x)$ and $\mathbf S_R(\mathbf x)=\mathbf Q$ (p. 182–183).

**Theorem 9.16.** The SLR moments in terms of conditional moments are
$$\boldsymbol\mu_R=\mathrm E[\boldsymbol\mu_R(\mathbf x)],\quad \mathbf C_R=\mathrm E[(\mathbf x-\mathbf m)(\boldsymbol\mu_R(\mathbf x)-\boldsymbol\mu_R)^{\mathsf T}],\quad \mathbf S_R=\mathrm{Cov}[\boldsymbol\mu_R(\mathbf x)]+\mathrm E[\mathbf S_R(\mathbf x)].\tag{9.47}$$
Proof (law of iterated expectations, LIE): $\mathrm E[\mathbf y]=\mathrm E[\mathrm E[\mathbf y\mid\mathbf x]]$ gives $\boldsymbol\mu_R$. Then $\mathbf C_R=\mathrm E[\mathrm E[(\mathbf x-\mathbf m)(\mathbf y-\boldsymbol\mu_R)^{\mathsf T}\mid\mathbf x]]=\mathrm E[(\mathbf x-\mathbf m)(\boldsymbol\mu_R(\mathbf x)-\boldsymbol\mu_R)^{\mathsf T}]$ (9.48). Finally, add and subtract $\boldsymbol\mu_R(\mathbf x)$ in $\mathbf S_R=\mathrm E[\mathrm E[(\mathbf y-\boldsymbol\mu_R)(\mathbf y-\boldsymbol\mu_R)^{\mathsf T}\mid\mathbf x]]$:
$$\mathbf S_R=\mathrm E\,\mathrm E[(\mathbf y-\boldsymbol\mu_R(\mathbf x))(\cdot)^{\mathsf T}\mid\mathbf x]+\mathrm E\,\mathrm E[(\boldsymbol\mu_R(\mathbf x)-\boldsymbol\mu_R)(\cdot)^{\mathsf T}\mid\mathbf x]=\mathrm E[\mathbf S_R(\mathbf x)]+\mathrm{Cov}[\boldsymbol\mu_R(\mathbf x)].\tag{9.49}$$
(The cross terms vanish; this step is not written out in the text — added.) (p. 183).

**Corollary 9.17 (non-additive transform).** For $\mathbf y=\mathbf g(\mathbf x,\mathbf q)$ with independent $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$, $\mathbf q\sim\mathrm N(\mathbf 0,\mathbf Q)$, the SLR is (9.38) with moments in two forms (p. 183–184).
- Joint integrals over $(\mathbf x,\mathbf q)$ with $\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)\mathrm N(\mathbf q\mid\mathbf 0,\mathbf Q)$: $\boldsymbol\mu_R=\int\mathbf g$, $\mathbf C_R=\int(\mathbf x-\mathbf m)(\mathbf g-\boldsymbol\mu_R)^{\mathsf T}$, $\mathbf S_R=\int(\mathbf g-\boldsymbol\mu_R)(\mathbf g-\boldsymbol\mu_R)^{\mathsf T}$ (9.50).
- Conditional moments $\boldsymbol\mu_R(\mathbf x)=\int\mathbf g\,\mathrm N(\mathbf q\mid\mathbf 0,\mathbf Q)\mathrm d\mathbf q$ and $\mathbf S_R(\mathbf x)=\int(\mathbf g-\boldsymbol\mu_R(\mathbf x))(\cdot)^{\mathsf T}\mathrm N(\mathbf q\mid\mathbf 0,\mathbf Q)\mathrm d\mathbf q$ (9.51), inserted in
$$\boldsymbol\mu_R=\int\boldsymbol\mu_R(\mathbf x)\mathrm N\,\mathrm d\mathbf x,\ \ \mathbf C_R=\int(\mathbf x-\mathbf m)(\boldsymbol\mu_R(\mathbf x)-\boldsymbol\mu_R)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x,\ \ \mathbf S_R=\int\big[(\boldsymbol\mu_R(\mathbf x)-\boldsymbol\mu_R)(\cdot)^{\mathsf T}+\mathbf S_R(\mathbf x)\big]\mathrm N\,\mathrm d\mathbf x.\tag{9.52}$$

The integrals can be approximated with, e.g., sigma-point methods. A potential disadvantage of (9.51)–(9.52) is that the integrals are nested ((9.51) must be evaluated for every $\mathbf x$), whereas (9.50) integrates jointly (p. 184).

**Corollary 9.18 (conditional distribution models).** For $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$, $\mathbf y\sim p(\mathbf y\mid\mathbf x)$: $\mathbf A,\mathbf b,\boldsymbol\Lambda$ are as in (9.38) with
$$\boldsymbol\mu_R=\int\mathbf y\,p(\mathbf y\mid\mathbf x)\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)\,\mathrm d\mathbf y\,\mathrm d\mathbf x,\ \ \mathbf C_R=\int(\mathbf x-\mathbf m)(\mathbf y-\boldsymbol\mu_R)^{\mathsf T}(\cdots),\ \ \mathbf S_R=\int(\mathbf y-\boldsymbol\mu_R)(\mathbf y-\boldsymbol\mu_R)^{\mathsf T}(\cdots).\tag{9.53}$$
Equivalently use (9.52) with conditional moments (9.54), the integrals (9.46) (p. 184–185). If $\mathbf y$ is discrete, $\mathbf y$-integrals become sums. The $\mathbf x$-integrals can use Gaussian quadrature, but $\mathbf y$-integrals may need other approximations unless $p(\mathbf y\mid\mathbf x)$ is Gaussian (p. 185). Equation (9.52) holds for all three model families, and only the conditional moments change (p. 185).

**Example 9.19 (Poisson observations)** (p. 185–186). Let $x\sim\mathrm N(m,P)$, with $\exp(x)$ the population size and $y\sim\mathrm{Po}(\alpha\exp(x))$ (9.55). The Poisson pmf is $\exp(-\lambda(x))\lambda(x)^y/y!$ (9.56), with mean and variance both $\lambda(x)=\alpha\exp(x)$. So $\mu(x)=\mathrm E[y\mid x]$ and $P_y(x)$ both equal $\alpha\exp(x)$. By (9.52),
$$\mu=\int\alpha e^{x}\mathrm N\,\mathrm dx,\quad P_{xy}=\int(x-m)(\alpha e^{x}-\mu)\mathrm N\,\mathrm dx,\quad P_y=\int\big(\alpha e^{x}+(\alpha e^{x}-\mu)^2\big)\mathrm N\,\mathrm dx.\tag{9.57}$$
These can be computed numerically or analytically (Exercise 9.5). Then $A=P_{xy}/P$, $b=\mu-Am$, $\Lambda=P_y-A^2P$. Figure 9.2 shows the result for $m=10$, $P=0.3$ (p. 186).

### 9.5 Statistical Linear Regression Filters (p. 187–192)
Background: the UKF was re-derived with SLR (Lefebvre et al., 2002), and later the GHKF (Arasaratnam et al., 2007). SLR has also been used for models given by conditional moments (Tronarp et al., 2018) (p. 187).

**Algorithm 9.20 (SLRF I, additive noise)** combines Corollary 9.14 with Algorithm 9.1, without simplification (p. 187–188). Prediction:
$$\mathbf A_{k-1}=(\mathbf P_k^{xx})^{\mathsf T}\mathbf P_{k-1}^{-1},\quad \mathbf a_{k-1}=\boldsymbol\mu_k^--\mathbf A_{k-1}\mathbf m_{k-1},\quad \boldsymbol\Lambda_{k-1}=\mathbf P_k^x-\mathbf A_{k-1}\mathbf P_{k-1}\mathbf A_{k-1}^{\mathsf T},\tag{9.58}$$
with ($\mathrm N=\mathrm N(\mathbf x\mid\mathbf m_{k-1},\mathbf P_{k-1})$)
$$\boldsymbol\mu_k^-=\int\mathbf f\,\mathrm N\,\mathrm d\mathbf x,\ \ \mathbf P_k^{xx}=\int(\mathbf x-\mathbf m_{k-1})(\mathbf f-\boldsymbol\mu_k^-)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x,\ \ \mathbf P_k^x=\int(\mathbf f-\boldsymbol\mu_k^-)(\cdot)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x+\mathbf Q_{k-1}.\tag{9.59}$$
Then (9.60) is (9.5). Update:
$$\mathbf H_k=(\mathbf P_k^{xy})^{\mathsf T}(\mathbf P_k^-)^{-1},\quad \mathbf b_k=\boldsymbol\mu_k^+-\mathbf H_k\mathbf m_k^-,\quad \boldsymbol\Omega_k=\mathbf P_k^y-\mathbf H_k\mathbf P_k^-\mathbf H_k^{\mathsf T},\tag{9.61}$$
with $\boldsymbol\mu_k^+,\mathbf P_k^{xy},\mathbf P_k^y$ the analogous integrals of $\mathbf h$ against $\mathrm N(\mathbf x\mid\mathbf m_k^-,\mathbf P_k^-)$, plus $\mathbf R_k$ in $\mathbf P_k^y$ (9.62). Then (9.63) is (9.7) (p. 187–188).

**Redundancies** (p. 188): $\mathbf m_k^-=\boldsymbol\mu_k^-$, $\mathbf P_k^-=\mathbf P_k^x$, $\boldsymbol\mu_k=\boldsymbol\mu_k^+$ and $\mathbf S_k=\mathbf P_k^y$. With $\mathbf C_k=\mathbf P_k^{xy}$ this gives Algorithm 9.21.

**Algorithm 9.21 (SLRF II)** (p. 188–189).
- Prediction (9.64): $\mathbf m_k^-=\int\mathbf f\,\mathrm N\,\mathrm d\mathbf x$ and $\mathbf P_k^-=\int(\mathbf f-\mathbf m_k^-)(\mathbf f-\mathbf m_k^-)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x+\mathbf Q_{k-1}$.
- Update (9.65): $\boldsymbol\mu_k=\int\mathbf h\,\mathrm N\,\mathrm d\mathbf x$, $\mathbf C_k=\int(\mathbf x-\mathbf m_k^-)(\mathbf h-\boldsymbol\mu_k)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x$, $\mathbf S_k=\int(\mathbf h-\boldsymbol\mu_k)(\cdot)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x+\mathbf R_k$. The expectations here are over $\mathrm N(\mathbf x\mid\mathbf m_k^-,\mathbf P_k^-)$ and the first $\mathbf m_k^-$ is also the prediction.
- Then (9.66): $\mathbf K_k=\mathbf C_k\mathbf S_k^{-1}$, $\mathbf m_k=\mathbf m_k^-+\mathbf K_k(\mathbf y_k-\boldsymbol\mu_k)$, $\mathbf P_k=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}$.

Algorithm 9.21 is identical to Algorithm 8.3. So the general Gaussian filters for additive noise (UKF, CKF, GHKF) implicitly use SLR as enabling approximation (p. 189).

*Intuition note:* The "linearize then Kalman" route and the "match moments then update" route give the same equations. The SLR noise term makes the covariance of $\mathbf y$ match the moment-matching value, so the Kalman step uses the same $\mathbf S_k$ (shown for the additive and non-additive models of Alg. 8.3 and 8.4).

For non-additive or conditional models only the moments in (9.59) and (9.62) change. Plugging (9.50) into Algorithm 9.21 gives Algorithm 8.4 after simplification (Exercise 9.8). So Algorithms 8.3 and 8.4 are SLR filters (p. 189).

**Conditional moment filters** (p. 189–192). For models (9.67)=(9.10), assume the conditional moments (9.68) can be computed: $\boldsymbol\mu_k^-(\mathbf x_{k-1})=\mathrm E[\mathbf x_k\mid\mathbf x_{k-1}]$, $\mathbf P_k^x(\mathbf x_{k-1})=\mathrm{Cov}[\mathbf x_k\mid\mathbf x_{k-1}]$, $\boldsymbol\mu_k(\mathbf x_k)=\mathrm E[\mathbf y_k\mid\mathbf x_k]$, $\mathbf P_k^y(\mathbf x_k)=\mathrm{Cov}[\mathbf y_k\mid\mathbf x_k]$ (p. 190).

**Algorithm 9.22 (SLRF III)** (p. 190–191). Using (9.52) with these moments and $\mathrm N_{k-1}=\mathrm N(\mathbf x_{k-1}\mid\mathbf m_{k-1},\mathbf P_{k-1})$:
$$\mathbf m_k^-=\int\boldsymbol\mu_k^-(\mathbf x_{k-1})\mathrm N_{k-1}\mathrm d\mathbf x_{k-1},\quad \mathbf P_k^-=\int(\boldsymbol\mu_k^--\mathbf m_k^-)(\boldsymbol\mu_k^--\mathbf m_k^-)^{\mathsf T}\mathrm N_{k-1}\mathrm d\mathbf x_{k-1}+\int\mathbf P_k^x(\mathbf x_{k-1})\mathrm N_{k-1}\mathrm d\mathbf x_{k-1}.\tag{9.69}$$
Update (with $\mathrm N=\mathrm N(\mathbf x_k\mid\mathbf m_k^-,\mathbf P_k^-)$):
$$\boldsymbol\mu_k=\int\boldsymbol\mu_k(\mathbf x_k)\mathrm N\,\mathrm d\mathbf x_k,\ \ \mathbf C_k=\int(\mathbf x_k-\mathbf m_k^-)(\boldsymbol\mu_k(\mathbf x_k)-\boldsymbol\mu_k)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x_k,\ \ \mathbf S_k=\int(\boldsymbol\mu_k(\mathbf x_k)-\boldsymbol\mu_k)(\cdot)^{\mathsf T}\mathrm N\,\mathrm d\mathbf x_k+\int\mathbf P_k^y(\mathbf x_k)\mathrm N\,\mathrm d\mathbf x_k.\tag{9.70}$$
Then $\mathbf K_k=\mathbf C_k\mathbf S_k^{-1}$, $\mathbf m_k=\mathbf m_k^-+\mathbf K_k(\mathbf y_k-\boldsymbol\mu_k)$, $\mathbf P_k=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}$ (9.71).

For the non-additive model (9.9), the conditional moments are (9.72)–(9.73): $\boldsymbol\mu_k^-(\mathbf x_{k-1})=\int\mathbf f(\mathbf x_{k-1},\mathbf q_{k-1})\mathrm N(\mathbf q_{k-1}\mid\mathbf 0,\mathbf Q_{k-1})\mathrm d\mathbf q_{k-1}$, $\mathbf P_k^x(\mathbf x_{k-1})$ the corresponding covariance integral, and analogously $\boldsymbol\mu_k(\mathbf x_k),\mathbf P_k^y(\mathbf x_k)$ with $\mathbf h$ and $\mathbf r_k$. The author says these formulations arguably give more involved expressions, but to handle other model types only (9.72)–(9.73) must change, which is useful from a software engineering view (p. 191).

**Algorithm 9.23 (SLRF IV, conditional distributions)** uses Corollary 9.18 directly when the conditional moments are inconvenient (p. 191–192).
- Prediction (9.74): $\mathbf m_k^-=\int\mathbf x_k\,p(\mathbf x_k\mid\mathbf x_{k-1})\mathrm N(\mathbf x_{k-1}\mid\mathbf m_{k-1},\mathbf P_{k-1})\mathrm d\mathbf x_k\mathrm d\mathbf x_{k-1}$ and $\mathbf P_k^-=\int(\mathbf x_k-\mathbf m_k^-)(\mathbf x_k-\mathbf m_k^-)^{\mathsf T}(\cdots)$.
- Update (9.75): $\boldsymbol\mu_k=\int\mathbf y_k(\cdots)$, $\mathbf C_k=\int(\mathbf x_k-\mathbf m_k^-)(\mathbf y_k-\boldsymbol\mu_k)^{\mathsf T}(\cdots)$, $\mathbf S_k=\int(\mathbf y_k-\boldsymbol\mu_k)(\mathbf y_k-\boldsymbol\mu_k)^{\mathsf T}(\cdots)$, with $(\cdots)=p(\mathbf y_k\mid\mathbf x_k)\mathrm N(\mathbf x_k\mid\mathbf m_k^-,\mathbf P_k^-)\mathrm d\mathbf y_k\mathrm d\mathbf x_k$.
- Gain and update as (9.76).

### 9.6 Practical SLR Filters (p. 192–200)
For SLR filters the key issue is to compute the moments $\boldsymbol\mu_k,\mathbf C_k,\mathbf S_k$ (the author calls this final conclusion a bit dull). Forming the SLR and applying an affine Kalman filter is equivalent to using these moments in a Gaussian filter. Sigma-point methods therefore recover the earlier filters. SLR's gain is a wider class of models, notably conditional distribution models (p. 192–193).

**Conditional moments in practice** (p. 193). For additive models, $\boldsymbol\mu_k^-(\mathbf x_{k-1})=\mathbf f(\mathbf x_{k-1})$, $\mathbf P_k^x=\mathbf Q_{k-1}$, $\boldsymbol\mu_k(\mathbf x_k)=\mathbf h(\mathbf x_k)$, $\mathbf P_k^y=\mathbf R_k$. For non-additive models, approximate (9.72)–(9.73) numerically. For many non-Gaussian-noise models (Section 5.2) there are closed forms or accurate approximations (p. 193).

**Algorithm 9.24 (sigma-point conditional moment Kalman filter, SPCMKF)** (p. 193–194). Unit sigma points $\boldsymbol\xi^{(i)}$ and weights $W_i$, $i=1,\dots,m$, come from the integration method of Chapter 8.
- Prediction: $\mathcal X_{k-1}^{(i)}=\mathbf m_{k-1}+\sqrt{\mathbf P_{k-1}}\,\boldsymbol\xi^{(i)}$ (9.78); $\boldsymbol\mu_k^{-(i)}=\boldsymbol\mu_k^-(\mathcal X_{k-1}^{(i)})$, $\mathbf P_k^{x,(i)}=\mathbf P_k^x(\mathcal X_{k-1}^{(i)})$ (9.79); then
$$\mathbf m_k^-=\sum_{i=1}^mW_i\boldsymbol\mu_k^{-(i)},\qquad \mathbf P_k^-=\sum_{i=1}^mW_i\Big(\mathbf P_k^{x,(i)}+(\boldsymbol\mu_k^{-(i)}-\mathbf m_k^-)(\boldsymbol\mu_k^{-(i)}-\mathbf m_k^-)^{\mathsf T}\Big).\tag{9.80}$$
- Update: $\mathcal X_k^{-(i)}=\mathbf m_k^-+\sqrt{\mathbf P_k^-}\,\boldsymbol\xi^{(i)}$ (9.81); $\boldsymbol\mu_k^{(i)}=\boldsymbol\mu_k(\mathcal X_k^{-(i)})$, $\mathbf P_k^{y,(i)}=\mathbf P_k^y(\mathcal X_k^{-(i)})$ (9.82); then
$$\boldsymbol\mu_k=\sum_iW_i\boldsymbol\mu_k^{(i)},\quad \mathbf S_k=\sum_iW_i\Big(\mathbf P_k^{y,(i)}+(\boldsymbol\mu_k^{(i)}-\boldsymbol\mu_k)(\boldsymbol\mu_k^{(i)}-\boldsymbol\mu_k)^{\mathsf T}\Big),\quad \mathbf C_k=\sum_iW_i(\mathcal X_k^{-(i)}-\mathbf m_k^-)(\boldsymbol\mu_k^{(i)}-\boldsymbol\mu_k)^{\mathsf T}.\tag{9.83}$$
Finally $\mathbf K_k=\mathbf C_k\mathbf S_k^{-1}$, $\mathbf m_k=\mathbf m_k^-+\mathbf K_k[\mathbf y_k-\boldsymbol\mu_k]$, $\mathbf P_k=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}$ (9.84).

**Algorithm 9.25 (Monte Carlo Kalman filter, MCKF)** (p. 195–196). It still approximates the filtering distribution as Gaussian. Particle filtering (Chapter 11) drops that approximation (p. 195).
- Prediction: draw $\mathbf x_{k-1}^{(i)}\sim\mathrm N(\mathbf m_{k-1},\mathbf P_{k-1})$, then $\hat{\mathbf x}_k^{(i)}\sim p(\mathbf x_k\mid\mathbf x_{k-1}^{(i)})$, $i=1,\dots,N$ (9.85–9.86). Sample moments: $\mathbf m_k^-=\frac1N\sum_i\hat{\mathbf x}_k^{(i)}$ and $\mathbf P_k^-=\frac1N\sum_i(\hat{\mathbf x}_k^{(i)}-\mathbf m_k^-)(\hat{\mathbf x}_k^{(i)}-\mathbf m_k^-)^{\mathsf T}$ (9.87).
- Update: draw $\mathbf x_k^{-(i)}\sim\mathrm N(\mathbf m_k^-,\mathbf P_k^-)$, then $\mathbf y_k^{(i)}\sim p(\mathbf y_k\mid\mathbf x_k^{-(i)})$ (9.88–9.89). Sample moments (9.90): $\boldsymbol\mu_k=\frac1N\sum_i\mathbf y_k^{(i)}$, $\mathbf S_k=\frac1N\sum_i(\mathbf y_k^{(i)}-\boldsymbol\mu_k)(\cdot)^{\mathsf T}$, $\mathbf C_k=\frac1N\sum_i(\mathbf x_k^{-(i)}-\mathbf m_k^-)(\mathbf y_k^{(i)}-\boldsymbol\mu_k)^{\mathsf T}$. Gain and update as (9.91).

The MCKF is theoretically appealing because it can approximate the SLR moments arbitrarily well and handles conditional-distribution models (p. 196).

**Example 9.26 (Poisson observations)** (p. 196–197). Random walk $x_k=x_{k-1}+q_{k-1}$, $q_{k-1}\sim\mathrm N(0,Q)$ (9.92), with $y_k\sim\mathrm{Po}(\lambda\exp(x_k))$ (9.93). Here $\lambda$ is the probability that an event occurs to one individual in a step. Parameters: $\lambda=0.1$, $Q=0.1$, $m_0=10$, $P_0=0.1$. MCKF used 10,000 samples. SPCMKF used the cubature rule, so it is a CKF. Over 500 sequences of length 25, the RMSE was 0.084 for MCKF and 0.091 for CKF. MCKF is more computationally demanding but gave slightly better estimates (p. 196–197, Fig. 9.3).

**Algorithm 9.27 (sigma-point non-additive conditional moment filter)** (p. 197–200). The conditional moments (9.72)–(9.73) are approximated by sigma points over the noises, with separate unit points $\boldsymbol\xi^{(j)'},\boldsymbol\xi^{(j)''}$ and weights $W'_j,W''_j$ ($m'$ and $m''$ points) (9.94–9.95).
- Prediction: sigma points $\mathcal X_{k-1}^{(i)}=\mathbf m_{k-1}+\sqrt{\mathbf P_{k-1}}\boldsymbol\xi^{(i)}$ and $\mathcal Q_{k-1}^{(j)}=\sqrt{\mathbf Q_{k-1}}\boldsymbol\xi^{(j)'}$ (9.96); propagate $\hat{\mathcal X}_k^{(i,j)}=\mathbf f(\mathcal X_{k-1}^{(i)},\mathcal Q_{k-1}^{(j)})$ (9.97); inner sums over $j$ give $\boldsymbol\mu_k^{-(i)}=\sum_jW'_j\hat{\mathcal X}_k^{(i,j)}$ and $\mathbf P_k^{x,(i)}=\sum_jW'_j(\hat{\mathcal X}_k^{(i,j)}-\boldsymbol\mu_k^{-(i)})(\cdot)^{\mathsf T}$ (9.98); outer sums over $i$ as (9.99) = (9.80).
- Update: analogous, with $\mathcal R_k^{(j)}=\sqrt{\mathbf R_k}\boldsymbol\xi^{(j)''}$ (9.100), $\mathcal Y_k^{(i,j)}=\mathbf h(\mathcal X_k^{-(i)},\mathcal R_k^{(j)})$ (9.101), inner sums (9.102), outer sums (9.103) = (9.83), and gain/update (9.104).

Difference from Chapter 8 non-additive filters: those integrated jointly over $\mathbf x_{k-1},\mathbf q_{k-1}$ (or $\mathbf x_k,\mathbf r_k$) with sigma points of dimension $n+n_r$ for the augmented variable. Algorithm 9.27 uses separate sigma points for state and noise in a nested integration (p. 200).

### 9.7 Relation to Other Gaussian Filters (p. 200–201)
EKF and IEKF use analytic linearization with different linearization points. The Chapter 8 filters implicitly use SLR (p. 200). The reason is that SLR writes $p(\mathbf y\mid\mathbf x)\simeq\mathrm N(\mathbf y\mid\mathbf A\mathbf x+\mathbf b,\boldsymbol\Lambda)$ (9.105). It still chooses the parameters so the joint $p(\mathbf x,\mathbf y)$ matches the original moments (9.41). For Gaussian $\mathbf x$, the joint approximation is therefore exactly that of the general Gaussian filters. For additive noise, (9.43) and (8.4) are identical integrals (p. 200–201).

Chapter 8 filters approximate $(\mathbf x_k,\mathbf x_{k-1})$ and $(\mathbf x_k,\mathbf y_k)$ as Gaussian. SLR filters linearize in both steps. Identical filters follow (p. 201).

Higher-order filters: EKF2, the Fourier–Hermite Kalman filter (FHKF) and the Gaussian process quadrature filter (GPQF) use series expansions of $\mathbf f$ and $\mathbf h$. The author argues it is possible to see them as SLR filters. The expansions serve to approximate the integrals of the Chapter 8 filters. A higher-order expansion does not enable closed-form posteriors, so SLR remains the enabling approximation (p. 201).

### 9.8 Exercises (p. 202–203)
See "Exercises worth doing".

## Toy example (ours, not from the text)
Let $x\sim\mathrm N(0,1)$ ($m=0$, $P=1$), $g(x)=x+x^2$, so no noise first. Use $\mathrm E[x]=0$, $\mathrm E[x^2]=1$, $\mathrm E[x^3]=0$, $\mathrm E[x^4]=3$.
- Mean: $\mu=\mathrm E[g]=0+1=1$.
- Cross-covariance: $C=\mathrm E[x\,g]=\mathrm E[x^2]+\mathrm E[x^3]=1$.
- Variance of $g$: $\mathrm{Var}[x]+\mathrm{Var}[x^2]+2\mathrm{Cov}(x,x^2)=1+(3-1)+0=3$.
- SL/SLR line (9.13): $A=C/P=1$, $b=\mu-Am=1$.
- SL covariance: $S_S=APA=1$. SLR covariance: $S_R=3$, so $\Lambda=S_R-APA=3-1=2$.
- Check: residual $g-Ax-b=x^2-1$ has variance $3-1=2$ ✓.

Now add a measurement $y=g(x)+r$, $r\sim\mathrm N(0,0.5)$, and observe $y=2$.
- SLR: $S=3+0.5=3.5$, $K=C/S=1/3.5\approx0.286$, $m=0+0.286\,(2-1)\approx0.286$, $P=1-C^2/S=1-1/3.5\approx0.714$.
- SL: $S=1+0.5=1.5$, $K=1/1.5\approx0.667$, $m\approx0.667$, $P=1-1/1.5\approx0.333$.

SL's smaller $S$ makes it overconfident: posterior variance 0.333 vs 0.714. The SLR value matches moment matching (used by UKF, CKF, GHKF).

## Concepts
- [[enabling-approximation]] (new) — affine-plus-Gaussian-noise approximation of models that makes the Kalman equations usable (p. 168)
- [[kalman-filter]] — closed-form prediction/update used as step 2 for all these filters, in affine form (p. 169)
- [[linearization]] — here a family: Taylor expansion (EKF/IEKF), SL, SLR; they differ in how $\mathbf A,\mathbf b,\boldsymbol\Lambda$ are chosen (p. 170)
- [[state-space-model]] — the three families: additive (9.1), non-additive (9.9), conditional distributions (9.10) (p. 169–171)
- [[kalman-gain]] — $\mathbf K_k=\mathbf C_k\mathbf S_k^{-1}$ in the SLR filters (p. 188)
- [[statistical-linearization]] (new) — noise-free affine fit minimizing MSE over the input distribution (p. 171)
- [[statistical-linear-regression]] (new) — SL's affine fit plus noise with covariance equal to the fit error (p. 179)
- [[moment-matching-gaussian-filter]] (new) — Chapter 8 filter family; shown equal to SLR filters (p. 181, 189)
- [[sigma-point-method]] (new) — numerical integration with unit points $\boldsymbol\xi^{(i)}$, weights $W_i$ (p. 193)
- [[conditional-moments-slr]] (new) — SLR moments via $\mathrm E[\mathbf y\mid\mathbf x]$ and $\mathrm{Cov}[\mathbf y\mid\mathbf x]$ (p. 182–183)
- [[monte-carlo-kalman-filter]] (new) — SLR filter whose moments come from random samples (p. 195)

## Canonical instances
- [[cubic-function-sl-example]] — $g(x)=x^3$: Taylor, SL and SLR lines differ; SLR noise $\sqrt\Lambda\approx4.86$ ($P=1$), $0.43$ ($P=0.1$) (p. 174, 182)
- [[poisson-observation-slr]] — $y\sim\mathrm{Po}(\alpha e^x)$; closed-form conditional moments, SLR with $m=10$, $P=0.3$ (p. 185–186)
- [[population-random-walk-mckf-vs-ckf]] — Poisson-observed random walk; RMSE 0.084 (MCKF) vs 0.091 (CKF) (p. 196)
- [[ekf-iekf-as-enabling-linearization]] — EKF/IEKF are Algorithm 9.1 with Taylor expansion at different points (p. 170)

## Bridges (candidates)
- [same-math] SL/SLR coefficients $\mathbf A=\mathbf C^{\mathsf T}\mathbf P^{-1}$ ↔ statistics: best linear (least-squares) predictor and its residual covariance — same formulas as linear regression, taken with respect to a Gaussian input.
- [same-math] SLR conditional-moment formula $\mathbf S_R=\mathrm{Cov}[\boldsymbol\mu_R(\mathbf x)]+\mathrm E[\mathbf S_R(\mathbf x)]$ ↔ probability: law of total variance.
- [structural-analogy] Enabling approximation (linearize, then exact Kalman) ↔ control theory: linearization about an operating point for linear design.
- [structural-analogy] Noise added to cover linearization error ↔ robustness: model uncertainty treated as extra disturbance.

## Questions this raises
- How should the linearization be chosen when the posterior is not near-Gaussian or the model is strongly non-linear? (The author points to posterior linearization, Chapter 10, p. 168.)
- When is the extra cost of MCKF over a sigma-point filter worth the small accuracy gain seen in Example 9.26?
- Do higher-order expansions (EKF2, FHKF, GPQF) ever change the enabling approximation itself, or only the integrals (p. 201)?
- What does SL/SLR lose when the Gaussian assumption on $\mathbf x$ fails, given that the identities use $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$?

## Exercises worth doing
- Ex. 9.1 (p. 202) — derive the SLF expectations for a scalar sine model (hint: Fourier transform of Gaussian), implement, compare with EKF — difficulty: medium
- Ex. 9.2 (p. 202) — prove $\mathrm E[\mathbf g(\mathbf x)(\mathbf x-\mathbf m)^{\mathsf T}]=\mathrm E[\mathbf G_{\mathbf x}]\mathbf P$ by integration by parts and derive the derivative form of the SLF — difficulty: hard
- Ex. 9.5 (p. 203) — closed-form integrals of the Poisson SLR example (9.57) — difficulty: medium
- Ex. 9.6 (p. 203) — implement the Gauss–Hermite SLR filter and check it equals the GHKF — difficulty: medium
- Ex. 9.8 (p. 203) — build the non-additive SLR filter and show it simplifies to Algorithm 8.4 — difficulty: hard
- Ex. 9.10 (p. 203) — verify Corollary 9.8 via Theorem 9.3 applied to $\mathbf z=(\mathbf x;\mathbf q)$ — difficulty: medium

## Reading notes
- Printed page = pdf − 30 (pdf 198 = printed 168; the unit runs printed pp. 168–203).
- The text layer drops minus signs, hats, bars, plus signs and many symbols. All equations were checked against the page images.
- All page references are the printed page numbers visible on the pages.
- Wording quirk: Corollary 9.13 says "the statistical linearization $\mathbf y\simeq\mathbf A\mathbf x+\mathbf b+\tilde{\mathbf e}$" where it means SLR (p. 180).
- Example 9.26 uses $n=10{,}000$ for the number of MCKF samples, while Algorithm 9.25 uses $N$ (p. 196).
- The proof of Theorem 9.3 is only sketched (set the derivatives to zero). The proof of Corollary 9.8 and the equivalence of the non-additive version of Algorithm 9.21 with Algorithm 8.4 are only referred to (Exercises 9.10, 9.8), not given.
- The Toy example, the "(added step)" in (9.39) and the added note in (9.49) are not from the source.
