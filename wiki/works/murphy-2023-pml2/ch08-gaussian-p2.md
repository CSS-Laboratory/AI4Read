---
id: murphy-2023-pml2/ch08-gaussian-p2
work: murphy-2023-pml2
unit: "8 Gaussian filtering and smoothing (part 2/2): §8.3.2.3 (end) – §8.7"
pages: 379-400
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Gaussian filtering and smoothing, part 2: unscented, general Gaussian, ensemble and assumed-density filters

## L0 — One line
When the dynamics or observation model is nonlinear or non-Gaussian, one can still filter with Gaussians by approximating the needed joint distribution (or the posterior) with a Gaussian chosen by moment matching.

## L1 — The gist (≤ 120 words)
Linearizing a nonlinear model (the extended Kalman filter, EKF) is only one way to keep Kalman-style updates. Section 8.4 replaces linearization by numerical Gaussian moment calculation. The unscented transform uses 2n+1 weighted "sigma points". General Gaussian filtering covers quadrature, Monte Carlo and conditional-moment variants. Related methods are iterated filters, the ensemble Kalman filter, and assumed density filtering (ADF), which projects the exact posterior onto a tractable family after each step. ADF gives, for example, online Bayesian logistic regression. The unit ends with grid, expectation propagation (EP), variational inference (VI), MCMC and particle alternatives. It matters because it shows which approximation (joint vs posterior, linearization vs moments) each named filter makes.

**Prerequisites:** Kalman filter equations (gain, predict/update); Gaussian conditioning; KL divergence and moment matching; Jacobians; law of iterated expectation and total variance.

## L2 — Key ideas (5–10 bullets)
- The unscented transform (UT) propagates 2n+1 sigma points through a nonlinear $g$ and fits a Gaussian from weighted sample moments. It needs no Jacobians; its mean is exact for polynomials up to order 3, its covariance only for linear $g$ (p. 381–382).
- The UKF applies the UT twice (dynamics and measurement) and then does Gaussian conditioning; the UKS reuses the RTS equations with UT-estimated covariances (p. 382).
- General Gaussian filtering (GGF) fits a Gaussian to the joint $p(z,y)$ by moment matching. Linearization recovers the EKF, the UT recovers the UKF, and other quadrature or Monte Carlo rules give other filters (p. 383–385).
- Statistical linear regression views the same fit as the best linear likelihood on average over the Gaussian prior, not just at the mean (p. 383–384).
- Conditional-moment Gaussian filtering (CMGF) needs only $E[y|z]$ and $\mathrm{Cov}[y|z]$, so it handles Poisson and categorical likelihoods (p. 386–387).
- The ensemble Kalman filter represents the belief by samples updated Kalman-style. In the cost comparison (assuming $N_z>N_s>N_y$) it is cheaper than the EKF, but its posterior does not converge to the true posterior as $N_s\to\infty$ except in the linear-Gaussian case (p. 388–390).
- ADF = predict, update, project, where project means moment matching (minimizing $D_{KL}(p\|q)$). ADF approximates the posterior; GF approximates the joint (p. 391–393).
- ADF with diagonal Gaussians gives online logistic regression in $O(D)$ per step, with no step size, and it converges to near the offline Laplace answer in the example (p. 394–397).

## L3 — Walkthrough

### 8.3.2.3–8.3.3 Ends of the EKF section (p. 379)
- Tracking example: $f(z) = (z_1 + \Delta\sin z_2,\ z_2 + \Delta\cos z_1)$ (8.147), with step size $\Delta$ and fully visible state, $h(z)=z$. Exact inference is intractable; the EKF is applied easily (Fig. 8.4b) (p. 379).
- The EKF is also used for online neural-network parameter inference (pointer to §17.5.2) (p. 379).
- **EKS** (extended RTS smoother): linearize the dynamics around the filtered mean to get $F_t$, then run the standard Kalman smoother (p. 379).
- **Iterated EKS** relinearizes at the previous MAP estimate. [Bel94] shows it is equivalent to Gauss–Newton for the MAP of the smoothing posterior. It can diverge; a robust version with line search and Levenberg–Marquardt is in [SS20a] (p. 379).

### 8.4 Inference based on the unscented transform (p. 379)
- Idea: instead of passing a Gaussian through a linearized function, approximate $p(z_{t-1},z_t|y_{1:t-1})$ and $p(z_t,y_t|y_{1:t-1})$ by Gaussians whose moments come from numerical integration. Then take marginals and conditionals for the time and measurement updates (p. 379).
- The UT version is the **UKF** (also "sigma point filter"). Claimed advantages: can be more accurate and stable, and needs no Jacobians, so it works for non-differentiable or hard-constrained models. Disadvantages: it can be slower (the text says it needs $N_z$ model evaluations; §8.4.1 uses $2n+1$ points) and has 3 hyperparameters (p. 379).

### 8.4.1 The unscented transform (p. 381–382)
Let $x\sim\mathcal N(\mu,\Sigma)$, $y=g(x)$, $g:\mathbb R^n\to\mathbb R^m$.

**Sigma points (Alg. 8.5)** with $\lambda=\alpha^2(n+\kappa)-n$ (p. 381). Here $[\sqrt\Sigma]_{:i}$ is column $i$ of the matrix square root, $\sqrt\Sigma\sqrt\Sigma^\top=\Sigma$:
$$\mathcal X_0=\mu,\quad \mathcal X_i=\mu+\sqrt{n+\lambda}\,[\sqrt\Sigma]_{:i},\quad \mathcal X_{i+n}=\mu-\sqrt{n+\lambda}\,[\sqrt\Sigma]_{:i}$$
$$w_0^m=\tfrac{\lambda}{n+\lambda},\quad w_0^c=\tfrac{\lambda}{n+\lambda}+(1-\alpha^2+\beta),\quad w_i^m=w_i^c=\tfrac{1}{2(n+\lambda)}\ (i\ge1)$$

**Transform:**
$$\mathcal Y_i=g(\mathcal X_i),\ i=0{:}2n \tag{8.148}$$
$$E[g(x)]\approx\hat y=\sum_{i=0}^{2n}w_i^m\mathcal Y_i \tag{8.149}$$
$$\mathrm{Cov}[g(x)]\approx S'=\sum_{i=0}^{2n}w_i^c(\mathcal Y_i-\hat y)(\mathcal Y_i-\hat y)^\top \tag{8.150}$$

**Joint with noise:** for $y=g(x)+e$, $e\sim\mathcal N(0,\Omega)$, apply the same procedure to $\tilde g(x)=(x,g(x))$ and add noise (p. 381–382):
$$\begin{pmatrix}x\\y\end{pmatrix}\sim\mathcal N\left(\begin{pmatrix}\mu\\\hat y\end{pmatrix},\begin{pmatrix}\Sigma&C\\C^\top&S\end{pmatrix}\right)\tag{8.151}$$
Alg. 8.6 returns $(\hat y,S,C)$, with $S=\sum_i w_i^c(\mathcal Y_i-\hat y)(\mathcal Y_i-\hat y)^\top+\Omega$ and $C=\sum_i w_i^c(\mathcal X_i-\mu)(\mathcal Y_i-\hat y)^\top$. (The printed algorithm writes $\mu_U$ where $\hat y$ is meant; see Reading notes.)

**Hyperparameters** $\alpha,\beta,\kappa$ set the spread of the points. A typical setting is $\alpha=1,\beta=0,\kappa=n/2$ [Bit16] (p. 382).

**Accuracy** (p. 382): the UT is more accurate than the Taylor transform in Fig. 8.5. With $2n+1$ points the mean of $y$ is exact for polynomials up to order 3. The covariance is exact only for linear functions, because the square of a second-order polynomial is already order 4. An order-5 extension with $2n^2+1$ points [MS67] captures covariance terms exactly for quadratic functions (p. 382).

*Intuition note:* Instead of approximating the function by a line, the UT approximates the Gaussian by a few well-chosen points and pushes the points through the true function. Moments of the output points then estimate the output moments.

### 8.4.2 UKF (p. 382)
By analogy with §8.2.2.5:
$$(\mu_{t|t-1},\Sigma_{t|t-1},-)=\text{UnscentedGaussJoint}(\mu_{t-1|t-1},\Sigma_{t-1|t-1},f(\cdot,u_t),Q_t)\tag{8.152}$$
$$(\hat y_t,S_t,C_t)=\text{UnscentedGaussJoint}(\mu_{t|t-1},\Sigma_{t|t-1},h(\cdot,u_t),R_t)\tag{8.153}$$
$$(\mu_{t|t},\Sigma_{t|t},\ell_t)=\text{GaussCondition}(\mu_{t|t-1},\Sigma_{t|t-1},\hat y_t,S_t,C_t,y_t)\tag{8.154}$$
Fig. 8.4c shows the UKF ($\alpha=1,\beta=0,\kappa=2$) on the tracking problem (p. 382).

### 8.4.3 UKS (p. 382)
The reverse gain $J_t$ of Eq. (8.80) can be written with the predicted covariance and cross-covariance. Both can be estimated by the UT, after which the RTS equations are used as usual. The UK government's COVID-19 contact-tracing app used the UKS to estimate distance between anonymized phones from bluetooth signal strength. The distance was combined with other signals to estimate transmission risk (p. 382).

### 8.5.1 General Gaussian filtering (GGF) (p. 383)
Let $p(z)=\mathcal N(\mu,\Sigma)$ and $p(y|z)=\mathcal N(h_\mu(z),\Omega)$. The best Gaussian approximation to the exact joint is
$$q(z,y)=\arg\min_{q\in\mathcal N}D_{KL}(p(z,y)\|q(z,y))\tag{8.155}$$
It is obtained by moment matching: $q=\mathcal N\!\left(\begin{pmatrix}\mu\\\hat y\end{pmatrix},\begin{pmatrix}\Sigma&C\\C^\top&S\end{pmatrix}\right)$ (8.156), with
$$\hat y=\int h_\mu(z)\mathcal N(z|\mu,\Sigma)dz\tag{8.157}$$
$$S=\Omega+\int (h_\mu(z)-\hat y)(h_\mu(z)-\hat y)^\top\mathcal N(z|\mu,\Sigma)dz\tag{8.158}$$
$$C=\int (z-\mu)(h_\mu(z)-\hat y)^\top\mathcal N(z|\mu,\Sigma)dz\tag{8.159}$$
This can be used for the time update or the measurement update. For the measurement update with prior $\mathcal N(\mu_{t|t-1},\Sigma_{t|t-1})$:
$$K_t=C_tS_t^{-1}\tag{8.160}$$
$$\mu_{t|t}=\mu_{t|t-1}+K_t(y_t-\hat y_t)\tag{8.161}$$
$$\Sigma_{t|t}=\Sigma_{t|t-1}-K_tS_tK_t^\top\tag{8.162}$$

**8.5.1.1 Statistical linear regression (SLR)** (p. 383–384). Equivalently, the likelihood is approximated by $q(y|z)=\mathcal N(y|Az+b,\Omega)$ with
$$A=C^\top\Sigma^{-1},\quad b=\hat y-A\mu,\quad \Omega=S-A\Sigma A^\top\tag{8.163}$$
This minimizes $\mathcal L(A,b,\Omega)=E_{\mathcal N(z|\mu,\Sigma)}[D_{KL}(p(y|z)\|q(y|z;A,b,\Omega))]$ (8.164) (proof in [GF+15; Kam+22]). Equivalently, $A,b$ minimize the mean squared error $E[(y-Ax-b)^\top(y-Ax-b)]$ (8.165), with $\Omega$ the residual noise $E[(y-Ax-b)(y-Ax-b)^\top]$ (8.166). SLR differs from a Taylor expansion because the linearization is optimal on average over $\mathcal N(z|\mu,\Sigma)$, not only at the point $\mu$ (p. 384).

**8.5.1.2 Moment functions** (p. 384):
$$g_e(f,\mu,\Sigma)\triangleq\int f(z)\mathcal N(z|\mu,\Sigma)dz\tag{8.167}$$
$$g_c(f,g,\mu,\Sigma)\triangleq\int (f(z)-\bar f)(g(z)-\bar g)^\top\mathcal N(z|\mu,\Sigma)dz\tag{8.168}$$
with $\bar f=g_e(f,\mu,\Sigma)$ and $\bar g=g_e(g,\mu,\Sigma)$.

**8.5.1.3 Linearization** (p. 384–385). With $\hat f(z)=\mu+F(z-\mu)$ and $\hat g(z)=\mu+G(z-\mu)$ ($F,G$ Jacobians; 8.169–8.170), $g_e(\hat f,\mu,\Sigma)=E[\mu+F(z-\mu)]=\mu$ (8.171). (added step) Using $\bar f=\bar g=\mu$ in (8.173)–(8.175), the terms in $\mu\mu^\top$ and the terms linear in $(z-\mu)$ vanish (their expectation is zero), leaving
$$g_c(\hat f,\hat g,\mu,\Sigma)=F\,E[(z-\mu)(z-\mu)^\top]\,G^\top=F\Sigma G^\top\tag{8.176}$$
GGF with this rule is equivalent to the EKF, but it can have large errors and sometimes diverges [IX00; VDMW03] (p. 385).

**8.5.1.4 Gaussian quadrature (sigma points)** (p. 385). Use $\int h(z)\mathcal N(z|\mu,\Sigma)dz\approx\sum_{k=1}^Kw^kh(z^k)$ (8.177). (1-d integrals are "quadratures", multi-d ones "cubatures".) Using the UT for the points gives the UKF. Spherical cubature gives the **cubature Kalman filter (CKF)** [AH09], which is a special case of the UKF with $2n_z+1$ points, $\alpha=1$, $\beta=0$ and $\kappa$ free. Gauss–Hermite integration of order $p$ is exact for polynomials up to order $2p-1$, but needs $p^n$ points. It gives the **GHKF/QKF** (p. 385).

**8.5.1.5 Monte Carlo** (p. 385). The integrals can also be done by Monte Carlo. This is not particle filtering, which approximates the conditional $p(z_t|y_{1:t})$ rather than the joint $p(z_t,y_t|y_{1:t-1})$.

*Intuition note:* GGF is one template with a pluggable integrator. The choice of integrator (Jacobian, sigma points, quadrature, Monte Carlo) gives the EKF, UKF, CKF, GHKF and so on.

### 8.5.2 Conditional moment Gaussian filtering (CMGF) (p. 386–387)
The only requirement is computing the conditional moments
$$h_\mu(z)=E[y|z],\qquad h_\Sigma(z)=\mathrm{Cov}[y|z]\tag{8.178, 8.179}$$
The likelihood may be non-Gaussian, and $y$ may be discrete (sums replace integrals). By iterated expectation (p. 386):
$$\hat y=g_e(h_\mu(z),\mu,\Sigma)\tag{8.180}$$
$$C=E[(z-\mu)(h_\mu(z)-\hat y)]=g_c(z,h_\mu(z),\mu,\Sigma)\tag{8.181–8.182}$$
$$S=E[V[y|z]]+V[E[y|z]]=g_e(h_\Sigma(z),\mu,\Sigma)+g_c(h_\mu(z),h_\mu(z),\mu,\Sigma)\tag{8.183–8.185}$$
These match GGF's $\hat y$ and $C$; $S$ matches if $h_\Sigma(z)=\Omega$. The moments can be approximated by linearization or numerical integration and plugged into GGF (p. 386).

Examples: Poisson likelihood $p(y|z)=\mathrm{Poisson}(y|ce^z)$ gives $h_\mu(z)=h_\Sigma(z)=ce^z$ (8.186). Categorical likelihood $\mathrm{Cat}(y_t|\mathrm{softmax}(h(z_t)))$ (8.187) gives
$$h_\mu(z_t)=p_t=\mathrm{softmax}(h(z_t)),\qquad h_\Sigma(z_t)=\mathrm{diag}(p_t)-p_tp_t^\top\tag{8.188}$$
One class can be dropped to make the covariance full rank. Uses cited: online inference in neural-network classifiers, GP classifiers, recommender systems, and proposals inside particle filters (p. 387).

*Intuition note:* To make a Gaussian summary of $y$, one only needs its mean and variance given $z$. The total-variance split in (8.183) then adds the average conditional noise to the spread of the conditional mean.

### 8.5.3 Iterated filters and smoothers (p. 387–388)
GGF and CMGF take moments under the predictive distribution. The **IPLF** does one GGF step to get a posterior $\mathcal N(\mu_{t|t},\Sigma_{t|t})$ and then recomputes the moments under that posterior, repeating $J$ times (Alg. 8.7). The prior used in conditioning stays $(\mu_{t|t-1},\Sigma_{t|t-1})$. It is similar to the iterated EKF. The **IPLS** is the smoother analogue. Both can diverge; more robust versions use line search/damping [Rai+18b] and line search with Levenberg–Marquardt [Lin+21c] (p. 387).

Extensions (p. 388): [HPR19] extends IPLS to belief propagation on Forney factor graphs, with Jacobian-based, statistical or other linearizations. [Kam+22] gives an approximate expectation-propagation method that uses the "cavity" distribution (current posterior minus the last incoming message). Its advantage is that the outgoing message does not double count the evidence; its disadvantage is possible numerical instability. [WSS21] "Bayes-Newton" methods generalize all of the above, for SSMs and GPs.

### 8.5.4 Ensemble Kalman filter (EnKF) (p. 388–390)
Developed in meteorology for large nonlinear systems, mainly where the hidden state is a physical field on a spatial grid and measurements are sparse. Combining such information over space and time is called **data assimilation** (p. 388).

- **Belief state:** $N_s$ samples $z^s_{t|t}\in\mathbb R^{N_z}$, stacked as an $N_z\times N_s$ matrix $Z_{t|t}$. Unlike particle filtering, there is no importance sampling or resampling. The posterior does not converge to the true Bayesian posterior as $N_s\to\infty$ except in the linear-Gaussian case [LGMT11]. EnKF may sometimes do better for small $N_s$ (depending on the PF proposal) (p. 388).
- **Moments:** $\tilde z_{t|t}=\frac1{N_s}Z_{t|t}\mathbf 1$ (8.189), $\tilde\Sigma_{t|t}=\frac1{N_s-1}\tilde Z_{t|t}\tilde Z_{t|t}^\top$ (8.190), where $\tilde Z_{t|t}=Z_{t|t}(I_{N_s}-\frac1{N_s}\mathbf 1\mathbf 1^\top)$ are the centered columns (p. 388).
- **Time update:** draw $q^s_t\sim\mathcal N(0,Q_t)$ and set $z^s_{t|t-1}=f(z^s_{t-1|t-1},q^s_t)$. Draw $r^s_t\sim\mathcal N(0,R_t)$ and set $y^s_{t|t-1}=h(z^s_{t|t-1},r^s_t)$; $Y_{t|t-1}$ is $N_y\times N_s$ (p. 389).
- **Measurement update:** $Z_{t|t}=Z_{t|t-1}+\tilde K_t(y_t\mathbf 1^\top-Y_{t|t-1})$ (8.191), analog of (8.29). The exact linear-Gaussian gain is $K_t=\Sigma_{t|t-1}H^\top S_t^{-1}=C_tS_t^{-1}$. EnKF estimates it from anomalies $\tilde Z_{t|t-1}=Z_{t|t-1}-\tilde z_{t|t-1}\mathbf 1^\top$ and $\tilde Y_{t|t-1}=Y_{t|t-1}-\tilde y_{t|t-1}\mathbf 1^\top$ (8.192):
$$\tilde C_t=\tfrac1{N_s-1}\tilde Z_{t|t-1}\tilde Y_{t|t-1}^\top,\ \ \tilde S_t=\tfrac1{N_s-1}\tilde Y_{t|t-1}\tilde Y_{t|t-1}^\top\ (8.193),\qquad \tilde K_t=\tilde C_t\tilde S_t^{-1}\ (8.194)$$
This has the form of a multivariate least-squares problem (p. 389).
- **Variance reduction (additive noise):** replace $\tilde Y$ by $\tilde O_{t|t-1}=H\tilde Z_{t|t-1}$ (linear $h$), with $\tilde C_t=\frac1{N_s-1}\tilde Z\tilde O^\top$ and $\tilde S_t=\frac1{N_s-1}\tilde O\tilde O^\top+R_t$. The ensemble square root filter [Tip+03] removes latent sampling but may be less robust (p. 389).
- **Cost** (assuming $N_z>N_s>N_y$): for a sparse $F$, EnKF is $O(N_zN_s+N_zN_sN_y)$ and EKF is $O(N_z^2+N_z^2N_y)$. For a dense $F$, EnKF is $O(N_z^2N_s+N_zN_sN_y)$ and EKF is $O(N_z^3+N_z^2N_y)$ (p. 389).
- **Failure and fix:** if $N_s$ is too small, EnKF can be overconfident and diverge. Covariance inflation replaces the anomalies by $\beta(Z_{t|t-1}-\tilde z_{t|t-1}\mathbf 1^\top)$ with $\beta>1$. Hybrid PF/EnKF methods have better theory (p. 390).

*Intuition note:* The EnKF keeps the Kalman update formula but replaces the covariance matrices by sample covariances of an ensemble. That makes it cheaper than the EKF in the paper's cost comparison, which assumes $N_z>N_s>N_y$. The price is a Gaussian-style update with no guarantee of reaching the exact posterior.

### 8.5.5–8.5.7 Robust, dual and normalizing-flow variants (p. 390)
- **Robust KFs:** for outliers or sudden changes, use Laplace or Student-$t$ noise. [Hua+17b] uses variational Bayes with Student-distributed dynamics and observations, a Gaussian posterior conditional on the noise scale matrix, and an inverse-Wishart model for that matrix. Robustness to approximation error (e.g., step-size adaptation) is also useful (p. 390).
- **Dual EKF:** for online parameter estimation, add $\theta_t$ to the state with artificial dynamics $p(\theta_t|\theta_{t-1})=\mathcal N(\theta_t|\theta_{t-1},\epsilon I)$. One EKF estimates states and another estimates parameters [WN01] (p. 390).
- **Normalizing-flow KF** [Béz+20]: observe $y_t=f_t(h_t)$ with $h_t=H_tz_t+r_t$ and $f_t$ invertible with tractable Jacobian. Then the exact posterior $p(z_t|y_{1:t})$ is the usual KF posterior $p_{\text{LGSSM}}(z_t|h_{1:t})$ with $h_t=f_t^{-1}(y_t)$. Proof by induction (p. 390–391): by change of variables, $p(y_t|z_t)=p(h_t|z_t)\,Df_t^{-1}(y_t)$ with $Dg(a)=|\det\mathrm{Jac}(g)(a)|$. Assume $p(z_{t-1}|y_{1:t-1})=p_{\text{LGSSM}}(z_{t-1}|h_{1:t-1})$; then, by the linear-Gaussian dynamics, $p(z_t|y_{1:t-1})=p_{\text{LGSSM}}(z_t|h_{1:t-1})$. In Bayes' rule the factor $Df_t^{-1}(y_t)$ does not depend on $z_t$ and cancels, leaving $p_{\text{LGSSM}}(z_t|h_{1:t})$. Similar reasoning applies to smoothing (p. 391).

### 8.6 Assumed density filtering (ADF) (p. 391–392)
Assume the posterior lies in a tractable family $\mathcal Q$ (e.g., Gaussian). Given $q_{t-1}\in\mathcal Q$ with $q_{t-1}\approx p(z_{t-1}|y_{1:t-1})$:
$$p_{t|t-1}(z_t|y_{1:t-1})=\int p(z_t|z_{t-1})q_{t-1}(z_{t-1})dz_{t-1}\tag{8.195}$$
$$p_t(z_t|y_{1:t})=\tfrac1{Z_t}p(y_t|z_t)p_{t|t-1}(z_t),\quad Z_t=\int p(y_t|z_t)p_{t|t-1}(z_t)dz_t\tag{8.196, 8.197}$$
The result is often not in $\mathcal Q$, so we project:
$$q_t(z_t|y_{1:t})=\arg\min_{q\in\mathcal Q}D_{KL}(p_t(z_t|y_{1:t})\|q(z_t))\tag{8.198}$$
The three steps are predict, update, project (Fig. 8.6). Minimizing $D_{KL}(p\|q)$ is **moment projection**: for a Gaussian, set the mean and covariance of $q_t$ equal to those of $p_t$. Minimizing $D_{KL}(q\|p)$, as in variational inference, is **information projection** and gives mode-seeking behaviour (p. 392).

**8.6.1 Link to GF** (p. 392–393). GF solves $q_{t|t-1}(z_t,\tilde y_t)=\arg\min_{q\in\mathcal Q}D_{KL}(p(z_t,\tilde y_t|y_{1:t-1})\|q(z_t,\tilde y_t|y_{1:t-1}))$ (8.199) by moment matching, then conditions on $\tilde y_t=y_t$ (easy because of the Gaussian assumption). ADF first computes the locally exact posterior and then projects it. So ADF approximates the conditional $p_t(z_t|y_{1:t})$ and GF approximates the joint. ADF is more accurate since it approximates the posterior directly, but more computationally demanding, for reasons explained in [Wüt+16]. [Kam+22] give an EP-style method (EP generalizes ADF) whose messages use GF's local joint approximation. Fig. 8.7 is a taxonomy of the filters (p. 393).

**8.6.2 ADF for switching linear dynamical systems (Gaussian sum filter)** (p. 393–394). A Gaussian sum filter keeps a mixture of $K$ Gaussians, one per discrete state $m$ (runs $K$ Kalman filters in parallel). In GPB2 [BSF88] the prior belief is
$$b^i_{t-1}\triangleq p(z_{t-1},m_{t-1}=i|y_{1:t-1})=\pi^i_{t-1|t-1}\mathcal N(z_{t-1}|\mu^i_{t-1|t-1},\Sigma^i_{t-1|t-1})\tag{8.200}$$
Pass it through the $K$ linear models:
$$b^{ij}_t\triangleq p(z_t,m_{t-1}=i,m_t=j|y_{1:t})=\pi^{ij}_{t|t}\mathcal N(z_t|\mu^{ij}_{t|t},\Sigma^{ij}_{t|t})\tag{8.201}$$
with $\pi^{ij}_{t|t}=\pi^i_{t-1|t-1}A_{ij}$ and $A_{ij}=p(m_t=j|m_{t-1}=i)$. Then collapse over $i$ for each $j$: $b^j_t\triangleq p(z_t,m_t=j|y_{1:t})=\pi^j_{t|t}\mathcal N(z_t|\mu^j_{t|t},\Sigma^j_{t|t})$ (8.202). Collapsing a mixture $\sum_k\pi^k\mathcal N(\mu^k,\Sigma^k)$ to one Gaussian is done by moment matching ("weak marginalization", since it preserves the first two moments):
$$\mu=\sum_k\pi^k\mu^k,\qquad \Sigma=\sum_k\pi^k\big(\Sigma^k+(\mu^k-\mu)(\mu^k-\mu)^\top\big)\tag{8.203, 8.204}$$
Applied here (8.205–8.208):
$$\pi^j=\sum_i\pi^{ij},\quad \pi^{j|i}=\frac{\pi^{ij}}{\sum_{j'}\pi^{ij'}},\quad \mu^j=\sum_i\pi^{j|i}\mu^{ij},\quad \Sigma^j=\sum_i\pi^{j|i}\big(\Sigma^{ij}+(\mu^{ij}-\mu^j)(\mu^{ij}-\mu^j)^\top\big)$$
GPB2 runs $K^2$ filters per step. The cheaper **IMM** first collapses the prior to one Gaussian, then updates it with $K$ Kalman filters, one per $m_t$ (Fig. 8.8) (p. 394).

**8.6.3 ADF for online logistic regression** (based on [Zoe07]) (p. 394–396). Model: $p(y_t|x_t,w_t)=\mathrm{Ber}(y_t|\sigma(x_t^\top w_t))$ (8.209), $p(w_t|w_{t-1})=\mathcal N(w_t|w_{t-1},Q)$ (8.210), with $Q=\epsilon I$ (or $\epsilon=0$, as in recursive least squares, if the weights do not change). ADF is needed because the likelihood is not conjugate to the prior (p. 394). The approximating family is diagonal Gaussians: $p_{t-1}(w_{t-1})=\prod_j\mathcal N(w^j_{t-1}|\mu^j_{t-1|t-1},\tau^j_{t-1|t-1})$ (8.211) (p. 395).

1. Predict: $\mu_{t|t-1}=\mu_{t-1|t-1}$, $\tau_{t|t-1}=\tau_{t-1|t-1}+Q$ (p. 395).
2. Logit $\eta_t=w_t^\top x_t$ has prior predictive $\mathcal N(m_{t|t-1},v_{t|t-1})$ (8.212) with $m_{t|t-1}=\sum_jx_{t,j}\mu^j_{t|t-1}$ (8.213) and $v_{t|t-1}=\sum_jx_{t,j}^2\tau^j_{t|t-1}$ (8.214) (p. 395).
3. Posterior of $\eta_t$: $\mathcal N(m_t,v_t)$ (8.215), with $m_t=\int\eta_t\tfrac1{Z_t}p(y_t|\eta_t)p_{t|t-1}(\eta_t)d\eta_t$, $v_t=\int\eta_t^2\tfrac1{Z_t}p(y_t|\eta_t)p_{t|t-1}(\eta_t)d\eta_t-m_t^2$, $Z_t=\int p(y_t|\eta_t)p_{t|t-1}(\eta_t)d\eta_t$ (8.216–8.218). These are 1-d integrals, computed by Gaussian quadrature [Zoe07; KB00] (p. 396).
4. With $m_t=m_{t|t-1}+\delta_m$ and $v_t=v_{t|t-1}+\delta_v$ (8.219), treat $p(\eta_t)=\mathcal N(m_t,v_t)$ as "soft evidence" in a linear Gaussian system:
$$\mu^i_{t|t}=\mu^i_{t|t-1}+a_i\delta_m,\quad \tau^i_{t|t}=\tau^i_{t|t-1}+a_i^2\delta_v,\quad a_i\triangleq\frac{x^i_t\tau^i_{t|t-1}}{\sum_j(x^j_t)^2+\tau^j_{t|t-1}}\tag{8.220–8.223}$$
Parameters with inputs of larger magnitude or larger uncertainty get updated most, because $a_i$ is larger (p. 396).

Experiment: a 2-d binary classification problem with 3 weights. ADF converges toward the offline Laplace/MAP estimate (Fig. 8.10), also with a different data order (Fig. 8.11), and the final predictive distributions are similar (Fig. 8.12) (p. 396–397). Cost is $O(D)$ time and space per step, like SGD, but with no step-size parameter (the diagonal covariance implicitly sets the update size), and it returns a posterior approximation, not only a point estimate. It is very similar to the posterior linearization filter of §8.5.3, except that ADF approximates the posterior rather than the joint (p. 396).

**8.6.4** ADF for online deep networks is deferred to §17.5.3 (p. 398).

### 8.7 Other inference methods for SSMs (p. 398–400)
- **8.7.1 Grid-based:** discretize the state and use the HMM filter and smoother, which costs $O(K^2)$ per step for $K$ states. With $N_z$ dimensions and $B$ bins, $K=B^{N_z}$, so it is intractable in high dimension but useful in 1-d or 2-d (p. 398). Example: $z_t=z_{t-1}+\mathcal T_2(0,1)$, $y_t=z_t+\mathcal T_2(0,1)$ (8.224, 8.225), with an outlier at $t=20$. The filtering posterior at $t=20$ is bimodal with a mean far from the true state, and a fine grid can represent this (Figs. 8.13–8.14) (p. 398–399).
- **8.7.2 Expectation propagation:** an iterative version of ADF. Each exact local likelihood factor is combined with approximate factors from the past filtering and the future smoothed posterior, projected back to the tractable family, and iterated. Intractable local updates can use a local Gaussian approximation as in GGF [Kam+22] (p. 398).
- **8.7.3 Variational inference:** EP locally minimizes inclusive KL $D_{KL}(p(z_t|y_{1:T})\|q(z_t|y_{1:T}))$. VI globally minimizes exclusive KL $D_{KL}(q(z_{1:T}|y_{1:T})\|p(z_{1:T}|y_{1:T}))$. VI has a tractable lower bound that can be optimized stochastically and is guaranteed to converge, unlike EP (p. 399).
- **8.7.4 MCMC:** for HMMs or linear-Gaussian SSMs, blocked Gibbs sampling uses forward filtering backward sampling for $p(z_{1:T}|y_{1:T},\theta)$ and then samples $p(\theta|z_{1:T},y_{1:T})$. Alternatively marginalize out the states. When state inference is intractable and states are continuous, HMC can be used, but it does not scale well to long sequences (p. 399–400).
- **8.7.5 Particle filtering:** weighted samples ("particles") replace the Gaussian assumption. It is essentially importance sampling plus steps to prevent particle impoverishment. It may need many samples, but EKF or UKF can serve as proposals to improve efficiency. Offline: particle smoothing and SMC samplers (p. 400).

## Toy example (ours, not from the text)
One-dimensional UT: $x\sim\mathcal N(0,1)$, $g(x)=x^2$, so $n=1$, $\mu=0$, $\Sigma=1$. Use the recommended $\alpha=1,\beta=0,\kappa=n/2=0.5$.
- $\lambda=\alpha^2(n+\kappa)-n=1.5-1=0.5$; $n+\lambda=1.5$; $\sqrt{1.5}\approx1.2247$.
- Sigma points: $\mathcal X_0=0$, $\mathcal X_1=+1.2247$, $\mathcal X_2=-1.2247$.
- Weights: $w_0^m=0.5/1.5=1/3$; $w_0^c=1/3+(1-1+0)=1/3$; $w_{1,2}^m=w_{1,2}^c=1/(2\cdot1.5)=1/3$.
- Outputs: $\mathcal Y=(0,\ 1.5,\ 1.5)$ since $1.2247^2=1.5$.
- Mean: $\hat y=\tfrac13(0+1.5+1.5)=1$. True $E[x^2]=1$: exact, as expected for a polynomial of order $\le3$.
- Covariance: $S'=\tfrac13(1+0.25+0.25)=0.5$. True $\mathrm{Var}(x^2)=E[x^4]-1=3-1=2$. Not exact, since $g$ is not linear.
- Cross-covariance: $C=\tfrac13\big(0+1.2247\cdot0.5+(-1.2247)\cdot0.5\big)=0$, which equals the true $\mathrm{Cov}(x,x^2)=0$.
- Contrast: linearizing at $\mu=0$ gives $g'(0)=0$, hence mean $0$ and variance $0$; the UT mean is correct.

## Concepts
- [[unscented-transform]] (new) — Gaussian approximation of $p(g(x))$ from $2n+1$ weighted sigma points pushed through $g$ (p. 381)
- [[sigma-points-quadrature]] (new) — evaluation points $z^k$ and weights $w^k$ for $\int h\,\mathcal N\approx\sum w^kh(z^k)$ (p. 385)
- [[extended-kalman-filter]] (new) — Kalman filtering with the model linearized at the mean; equals GGF with linearized moments (p. 379, 385)
- [[general-gaussian-filtering]] (new) — filter that moment-matches a Gaussian to the joint of state and observation (p. 383)
- [[statistical-linear-regression]] (new) — linear model fitted optimally on average over the Gaussian, not at a single point (p. 383–384)
- [[conditional-moment-gaussian-filter]] (new) — Gaussian filter that needs only $E[y|z]$ and $\mathrm{Cov}[y|z]$ (p. 386)
- [[ensemble-kalman-filter]] (new) — sample-based Kalman-style filter with empirical $\tilde C,\tilde S$; posterior does not converge to the true one as $N_s\to\infty$ except in the linear-Gaussian case (p. 388)
- [[assumed-density-filtering]] (new) — predict, update, then project the posterior onto a tractable family (p. 391)
- [[moment-projection]] (new) — minimizing $D_{KL}(p\|q)$; for a Gaussian $q$, matches mean and covariance (p. 392)
- [[weak-marginalization]] (new) — collapsing a Gaussian mixture to one Gaussian by matching first two moments (p. 394)
- [[gaussian-sum-filter]] (new) — SLDS filter keeping a mixture of $K$ Gaussians (GPB2, IMM) (p. 393–394)
- [[grid-based-filter]] (new) — discretize state space and apply the HMM filter; fails in high dimension (p. 398)
- [[kl-divergence]] — the projection objective; direction decides moment-matching vs mode-seeking (p. 392)
- [[monte-carlo-integration]] — one way to compute GGF moments (p. 385)
- [[variational-inference-elbo]] — globally minimizes exclusive KL with a tractable bound (p. 399)

## Canonical instances
- [[nonlinear-tracking-2d]] — $f$ from (8.147) with $h(z)=z$; EKF and UKF compared (p. 379, 382)
- [[ukf-covid-contact-tracing]] — UKS for bluetooth-based distance estimation (p. 382)
- [[poisson-categorical-cmgf]] — Poisson and softmax likelihood moments for CMGF (p. 386–387)
- [[adf-online-logistic-regression]] — diagonal-Gaussian ADF vs Laplace on a 2-d problem (p. 394–397)
- [[student-noise-1d-grid-filter]] — bimodal filtering posterior at an outlier, handled on a grid (p. 398–399)

## Bridges (candidates)
- [same-math] Moment matching of a Gaussian mixture (8.204) ↔ law of total variance (8.183): both are $E[\mathrm{Cov}]+\mathrm{Cov}[E]$.
- [same-math] SLR (8.165) ↔ least-squares regression: the same MSE objective, averaged over a Gaussian input.
- [structural-analogy] ADF moment projection ↔ expectation propagation: EP iterates ADF-style projections with past and future factors.
- [structural-analogy] ADF online logistic regression ↔ SGD: same $O(D)$ cost per step, but the posterior variance replaces the step size.
- [metaphor] Sigma points ↔ a small survey sample chosen deterministically to reproduce known moments of a population.

## Questions this raises
- How should $\alpha,\beta,\kappa$ be chosen for a given problem, and when does the choice change the filter's stability?
- When the exact posterior is strongly non-Gaussian, how much error accumulates from projecting at every ADF step?
- Why does EnKF fail to converge to the Bayesian posterior as $N_s\to\infty$, and when is that acceptable in practice?
- How does ADF (posterior) vs GF (joint) approximation differ in cost and accuracy for the same model?

## Reading notes
- Printed page = pdf page − 34. The unit begins mid-§8.3.2.3 (printed p. 379, the end of the tracking example), continues through §§8.3.2.4–8.3.3, and ends at the end of §8.7.5 on p. 400. The metadata describes the split as at a section boundary, but the first page begins mid-sentence in §8.3.2.3; the earlier material is presumably in part 1.
- Running footer: "Probabilistic Machine Learning: Advanced Topics", online version, December 10, 2025.
- Printed p. 393: the text layer is garbled, and the text layer also contains overlaid text from another document (Figures 39/40, particle-filtering text), which is not visible in the page image. Content was read from the page image (Fig. 8.8 and §8.6.1–8.6.2).
- Algorithm 8.6 (p. 381) uses $\mu_U$ in lines 5–6; it is not defined on these pages. The context (8.149–8.150) suggests $\hat y$; I wrote it that way.
- §8.6.2 (p. 394) says the optimal single-Gaussian fit is $\arg\min_q D_{KL}(q\|p)$, but it then solves it by moment matching, which §8.6 (p. 392) associates with $D_{KL}(p\|q)$. The direction as printed looks inconsistent. I used moment matching as printed.
- Smaller notation slips as printed: (8.165)–(8.166) use $x$ where $z$ is meant; (8.208) has $\mu_j$ in the last factor where $\mu^j$ is meant; (8.169)–(8.170) write $\mu$ where $f(\mu)$ and $g(\mu)$ are meant; (8.216)–(8.218) write $p(y_t|\eta_t)=\mathrm{Ber}(y_t|\eta_t)$ (probably $\sigma(\eta_t)$); the sentence after (8.219) writes $p(\eta_t|w)=\mathcal N(\eta_t|w^\top\eta_t,0)$ (probably $w^\top x_t$). In (8.223) the denominator bracketing is ambiguous in print; I copied it.
- Near Alg. 8.7 (p. 387), the predict step calls MomentsGaussJoint with $(f,Q,g_e,g_c)$, while the function is defined with $(h_\mu,h_\Sigma,g_e,g_c)$.
- §8.4 (p. 379) says the UKF needs $N_z$ model evaluations; §8.4.1 uses $2n+1$ points. Both are reported as printed.
- The unit contains no exercises.
