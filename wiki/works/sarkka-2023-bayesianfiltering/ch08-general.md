---
id: sarkka-2023-bayesianfiltering/ch08-general
work: sarkka-2023-bayesianfiltering
unit: "8 General Gaussian Filtering"
pages: 131-167
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# General Gaussian Filtering

## L0 — One line
Gaussian filters assume the filtering density is Gaussian and compute its mean and covariance as Gaussian integrals. The Gauss–Hermite, cubature and unscented Kalman filters (GHKF, CKF, UKF) are obtained by computing those integrals with different numerical rules.

## L1 — The gist (≤ 120 words)
Chapter 7 handled non-linear models by linearizing them (the extended Kalman filter, EKF). This chapter asks for a different approximation: match the true mean and covariance of the transformed variable. Those moments are Gaussian integrals of the model functions. The resulting general Gaussian filter is a theoretical construction. It becomes practical when a numerical rule replaces the integrals: Gauss–Hermite (exact to high order but $p^n$ points), spherical cubature ($2n$ points, third order), the unscented transform ($2n+1$ points, tunable) or a fifth-order rule. The unscented and cubature rules are closely related. In the examples, all of these filters give lower error than the EKF on the pendulum model. No derivatives are needed.

**Prerequisites:** Gaussian distributions, mean and covariance; Kalman filter and EKF (Ch. 7); Gaussian conditioning; matrix square root (Cholesky); polynomial degree; multi-dimensional integrals.

## L2 — Key ideas (5–10 bullets)
- **Moment matching instead of linearization.** The mean and covariance of $(\mathbf x,\mathbf y)$ are written as Gaussian integrals and the Gaussian with those moments is used. Linearizing $\mathbf g$ inside these integrals gives back the EKF transform (pp. 132–133).
- **The Gaussian filter** assumes $p(\mathbf x_k\mid\mathbf y_{1:k})\simeq \mathrm N(\mathbf m_k,\mathbf P_k)$. Prediction and update are the Kalman equations with the moment integrals in place of the linear terms (pp. 133–135).
- **The integrals must be computed.** The filter is a theoretical construction until the integrals are computed in closed form or numerically (p. 136).
- **Gauss–Hermite cubature** is a product of 1-D rules. It is exact for monomials (products of powers of the coordinates) with each degree $\le 2p-1$, but needs $p^n$ points (the evaluation points, called sigma points), which is infeasible in high dimension (pp. 137–140).
- **Third-order spherical cubature** uses $2n$ points with weights $1/(2n)$ at distance $\sqrt n$ along the axes. Its weights are always positive (pp. 143–145).
- **The unscented transform** adds the mean point and parameters $\kappa,\alpha,\beta$. It equals the cubature rule when $\kappa=0$. In the sigma-point forming step, the UKF differs from the other numerical-integration filters (GHKF, CKF) only superficially (pp. 150–161).
- **"Third order" is only for the mean.** The covariance is exact only for first-order polynomials, so the CKF and UKF are first-order methods for the covariance (pp. 145, 155, 159).
- **Higher-order rules** exist. The fifth-order rule shown ($O(n^2)$ points) has negative weights for $n\ge5$, a typical challenge of higher-order symmetric rules, which can lead to non-positive-definite covariances (pp. 162–163).

## L3 — Walkthrough

### Introduction (p. 131)
Chapter 7 linearized the model (EKF); iterating gives the IEKF, a Gauss–Newton special case. This chapter instead postulates the form of the filtering density and matches its mean and covariance to the true filtering density, at least approximately (p. 131). The authors say the EKF-based filters can be seen as approximations to the general Gaussian filter (p. 131).

### 8.1 Gaussian moment matching (pp. 131–133)
Setting: $\mathbf x\sim \mathrm N(\mathbf m,\mathbf P)$, $\mathbf q\sim\mathrm N(\mathbf 0,\mathbf Q)$, $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$ (8.1) (p. 132). The moments cannot be found in closed form but are Gaussian integrals:

$$\mathrm E[\mathbf y]=\int \mathbf g(\mathbf x)\,\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)\,d\mathbf x,\quad
\mathrm{Cov}[\mathbf y]=\int(\mathbf g(\mathbf x)-\mathrm E[\mathbf y])(\mathbf g(\mathbf x)-\mathrm E[\mathbf y])^{\mathsf T}\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)\,d\mathbf x+\mathbf Q \tag{8.2}$$

Everything reduces to approximating $\int \mathbf g(\mathbf x)\,\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)d\mathbf x$ (p. 132).

**Algorithm 8.1 (additive transform).**
$$\begin{pmatrix}\mathbf x\\ \mathbf y\end{pmatrix}\sim\mathrm N\!\left(\begin{pmatrix}\mathbf m\\ \boldsymbol\mu_M\end{pmatrix},\begin{pmatrix}\mathbf P&\mathbf C_M\\ \mathbf C_M^{\mathsf T}&\mathbf S_M\end{pmatrix}\right)\tag{8.3}$$
$$\boldsymbol\mu_M=\int\mathbf g(\mathbf x)\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)d\mathbf x,\;
\mathbf S_M=\int(\mathbf g-\boldsymbol\mu_M)(\mathbf g-\boldsymbol\mu_M)^{\mathsf T}\mathrm N\,d\mathbf x+\mathbf Q,\;
\mathbf C_M=\int(\mathbf x-\mathbf m)(\mathbf g-\boldsymbol\mu_M)^{\mathsf T}\mathrm N\,d\mathbf x\tag{8.4}$$
Substituting the linear approximation $\mathbf g(\mathbf x)\simeq\mathbf g(\mathbf m)+\mathbf G_{\mathbf x}(\mathbf m)(\mathbf x-\mathbf m)$ reduces these to the linear transform of Algorithm 7.1 (p. 133).

**Algorithm 8.2 (non-additive, $\mathbf y=\mathbf g(\mathbf x,\mathbf q)$).** Same joint Gaussian (8.5), with the same three integrals taken over $\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)\,\mathrm N(\mathbf q\mid\mathbf 0,\mathbf Q)\,d\mathbf x\,d\mathbf q$ and with no added $\mathbf Q$ in $\mathbf S_M$ (8.6) (p. 133).

*Intuition note.* The Gaussian approximation is chosen so that its first two moments are the true ones, computed through integrals. The EKF instead approximates the function and then computes moments exactly.

### 8.2 Gaussian filter (pp. 133–136)
Key assumption: $p(\mathbf x_k\mid\mathbf y_{1:k})\simeq\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)$ (8.7). It applies to the same models as the EKF, (7.24) and (7.39) (p. 133).

**Algorithm 8.3 (additive noise).**
- Prediction (8.8):
$$\mathbf m_k^-=\int\mathbf f(\mathbf x_{k-1})\mathrm N(\mathbf x_{k-1}\mid\mathbf m_{k-1},\mathbf P_{k-1})d\mathbf x_{k-1},$$
$$\mathbf P_k^-=\int(\mathbf f(\mathbf x_{k-1})-\mathbf m_k^-)(\mathbf f(\mathbf x_{k-1})-\mathbf m_k^-)^{\mathsf T}\mathrm N(\mathbf x_{k-1}\mid\mathbf m_{k-1},\mathbf P_{k-1})d\mathbf x_{k-1}+\mathbf Q_{k-1}.$$
- Update (8.9), with all integrals over $\mathrm N(\mathbf x_k\mid\mathbf m_k^-,\mathbf P_k^-)$:
$$\boldsymbol\mu_k=\int\mathbf h(\mathbf x_k)\mathrm N\,d\mathbf x_k,\quad
\mathbf S_k=\int(\mathbf h-\boldsymbol\mu_k)(\mathbf h-\boldsymbol\mu_k)^{\mathsf T}\mathrm N\,d\mathbf x_k+\mathbf R_k,\quad
\mathbf C_k=\int(\mathbf x_k-\mathbf m_k^-)(\mathbf h-\boldsymbol\mu_k)^{\mathsf T}\mathrm N\,d\mathbf x_k,$$
$$\mathbf K_k=\mathbf C_k\mathbf S_k^{-1},\quad \mathbf m_k=\mathbf m_k^-+\mathbf K_k(\mathbf y_k-\boldsymbol\mu_k),\quad \mathbf P_k=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}.$$

**Derivation (p. 134–135).**
1. Apply Algorithm 8.1 to $\mathbf x_k=\mathbf f(\mathbf x_{k-1})+\mathbf q_{k-1}$. This gives a joint Gaussian for $(\mathbf x_{k-1},\mathbf x_k)$ with means $(\mathbf m_{k-1},\mathbf m_k^-)$ and covariance blocks $\mathbf P_{k-1},\mathbf D_k,\mathbf P_k^-$ (8.10), where $\mathbf D_k=\int(\mathbf x_{k-1}-\mathbf m_{k-1})(\mathbf f(\mathbf x_{k-1})-\mathbf m_k^-)^{\mathsf T}\mathrm N\,d\mathbf x_{k-1}$ (8.11). By Lemma A.3 the marginal of $\mathbf x_k$ has mean $\mathbf m_k^-$ and covariance $\mathbf P_k^-$.
2. Apply it to $\mathbf y_k=\mathbf h(\mathbf x_k)+\mathbf r_k$. This gives a joint Gaussian of $(\mathbf x_k,\mathbf y_k)$ with blocks $\mathbf P_k^-,\mathbf C_k,\mathbf S_k$ (8.12). Gaussian conditioning (Lemma A.3) gives
$$\mathbf m_k=\mathbf m_k^-+\mathbf C_k\mathbf S_k^{-1}(\mathbf y_k-\boldsymbol\mu_k),\quad \mathbf P_k=\mathbf P_k^--\mathbf C_k\mathbf S_k^{-1}\mathbf C_k^{\mathsf T}\tag{8.13}$$
which is rewritten as (8.9) (p. 135).

The advantage of the moment-matching form is that it admits many numerical integration methods: Gauss–Hermite, cubature rules, Bayes–Hermite/Gaussian-process quadrature and Monte Carlo (p. 135).

**Algorithm 8.4 (non-additive, models (7.39)).** Prediction and update are the same as above, except that each integral is over the joint Gaussian of the state and the noise. For example $\mathbf m_k^-=\int\mathbf f(\mathbf x_{k-1},\mathbf q_{k-1})\mathrm N(\mathbf x_{k-1}\mid\mathbf m_{k-1},\mathbf P_{k-1})\mathrm N(\mathbf q_{k-1}\mid\mathbf 0,\mathbf Q_{k-1})d\mathbf x_{k-1}d\mathbf q_{k-1}$. There is no additive $\mathbf Q_{k-1}$ or $\mathbf R_k$ term, and the gain and update equations are unchanged (8.14–8.15) (pp. 135–136).

The authors state that these general Gaussian filters are theoretical constructions rather than practical algorithms. Closed-form integrals exist for many models, but numerical computation is more practical (p. 136).

*Intuition note.* The Gaussian filter is the Kalman filter with the "linear" parts $\mathbf F\mathbf m$, $\mathbf H\mathbf P\mathbf H^{\mathsf T}$, etc. replaced by Gaussian integrals of the true non-linear functions.

### 8.3 Gauss–Hermite integration (pp. 136–140)
Goal: approximate $\int\mathbf g(\mathbf x)\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)d\mathbf x$ (8.16) (p. 136). Plan: generalize the 1-D rule by Cartesian product. Disadvantage: the number of evaluation points is exponential in the dimension (pp. 136–137).

**1-D rule.** With the unit Gaussian weight function, the rule is $\int g(x)\mathrm N(x\mid0,1)dx\approx\sum_i W_i g(x^{(i)})$ (8.17), where the $x^{(i)}$ are "sigma points". The probabilists' convention is used (p. 137). Weights and points are chosen so that polynomial integrands are integrated exactly. The polynomial order is maximized by taking the points as roots of the Hermite polynomial $H_p$. The rule is then exact for polynomials up to order $2p-1$ (p. 137).

$$H_p(x)=(-1)^p\exp(x^2/2)\frac{d^p}{dx^p}\exp(-x^2/2)\tag{8.18}$$
$H_0=1$, $H_1=x$, $H_2=x^2-1$, $H_3=x^3-3x$, $H_4=x^4-6x^2+3$ (8.19), with recursion $H_{p+1}(x)=xH_p(x)-pH_{p-1}(x)$ (8.20) (p. 137).

Change of variables: $\int g(x)\mathrm N(x\mid m,P)dx=\int g(P^{1/2}\xi+m)\mathrm N(\xi\mid0,1)d\xi$ (8.21) (pp. 137–138).

**Algorithm 8.5.** (1) Unit sigma points $\xi^{(i)}$ = roots of $H_p$. The authors say it is numerically more stable to get them as eigenvalues of a tridiagonal matrix (Golub–Welsch). (2) Weights
$$W_i=\frac{p!}{p^2[H_{p-1}(\xi^{(i)})]^2}\tag{8.23}$$
(3) $\int g(x)\mathrm N(x\mid m,P)dx\approx\sum_{i=1}^pW_ig(P^{1/2}\xi^{(i)}+m)$ (8.24) (p. 138).

**Multi-dimensional.** Let $\mathbf P=\sqrt{\mathbf P}\sqrt{\mathbf P}^{\mathsf T}$ (Cholesky or similar square root) and $\mathbf x=\mathbf m+\sqrt{\mathbf P}\boldsymbol\xi$ (8.25). Then $\int\mathbf g(\mathbf x)\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)d\mathbf x=\int\mathbf g(\mathbf m+\sqrt{\mathbf P}\boldsymbol\xi)\mathrm N(\boldsymbol\xi\mid\mathbf 0,\mathbf I)d\boldsymbol\xi$ (8.26). The unit Gaussian integral is an iterated product of 1-D integrals, each approximated by quadrature (8.27) (pp. 138–139).

**Algorithm 8.6.** Weights $W_{i_1,\dots,i_n}=W_{i_1}\cdots W_{i_n}$ (8.29), with each $i_k=1,\dots,p$. Unit sigma points $\boldsymbol\xi^{(i_1,\dots,i_n)}=(\xi^{(i_1)},\dots,\xi^{(i_n)})^{\mathsf T}$ (8.30). Approximation:
$$\int\mathbf g(\mathbf x)\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)d\mathbf x\approx\sum_{i_1,\dots,i_n}W_{i_1,\dots,i_n}\mathbf g(\mathbf m+\sqrt{\mathbf P}\boldsymbol\xi^{(i_1,\dots,i_n)})\tag{8.31}$$
The $p$th order rule is exact for monomials $x_1^{d_1}\cdots x_n^{d_n}$ and their linear combinations with each $d_i\le2p-1$. It needs $p^n$ sigma points (pp. 139–140).

*Intuition note.* Gauss–Hermite picks the few points and weights that make the sum exact for the most polynomials. Using all combinations of 1-D points in $n$ dimensions costs $p^n$ evaluations.

### 8.4 Gauss–Hermite Kalman filter (pp. 140–143)
The GHKF (also called the quadrature Kalman filter, QKF) is obtained by replacing the integrals in Algorithm 8.3 with Algorithm 8.6 (p. 140).

**Algorithm 8.7 (additive).**
- Prediction: sigma points $\mathcal X_{k-1}^{(i_1,\dots,i_n)}=\mathbf m_{k-1}+\sqrt{\mathbf P_{k-1}}\boldsymbol\xi^{(i_1,\dots,i_n)}$ (8.32); propagate $\hat{\mathcal X}_k^{(\cdot)}=\mathbf f(\mathcal X_{k-1}^{(\cdot)})$ (8.33); then $\mathbf m_k^-=\sum W\hat{\mathcal X}_k$, $\mathbf P_k^-=\sum W(\hat{\mathcal X}_k-\mathbf m_k^-)(\hat{\mathcal X}_k-\mathbf m_k^-)^{\mathsf T}+\mathbf Q_{k-1}$ (8.34).
- Update: sigma points $\mathcal X_k^{-(\cdot)}=\mathbf m_k^-+\sqrt{\mathbf P_k^-}\boldsymbol\xi^{(\cdot)}$ (8.35); $\hat{\mathcal Y}_k=\mathbf h(\mathcal X_k^{-})$ (8.36); $\boldsymbol\mu_k=\sum W\hat{\mathcal Y}_k$, $\mathbf S_k=\sum W(\hat{\mathcal Y}_k-\boldsymbol\mu_k)(\cdot)^{\mathsf T}+\mathbf R_k$, $\mathbf C_k=\sum W(\mathcal X_k^--\mathbf m_k^-)(\hat{\mathcal Y}_k-\boldsymbol\mu_k)^{\mathsf T}$ (8.37); then $\mathbf K_k=\mathbf C_k\mathbf S_k^{-1}$, $\mathbf m_k=\mathbf m_k^-+\mathbf K_k[\mathbf y_k-\boldsymbol\mu_k]$, $\mathbf P_k=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}$ (8.38) (pp. 140–141).

The non-additive version follows by applying the quadrature to Algorithm 8.4. The augmented form is computationally heavy because it needs roughly double the integration dimension (p. 141).

**Examples.** Pendulum (Ex. 8.8): the GHKF needs no analytic derivatives or automatic differentiation. RMSE 0.10, versus 0.17 for both EKF and IEKF (pp. 141–142). Coordinated turn (Ex. 8.9): position RMSE 0.030 is slightly lower than the EKF but "still practically the same" (p. 142).

### 8.5 Spherical cubature integration (pp. 142–145)
The third-order spherical cubature rule was popularized by Arasaratnam and Haykin (2009). The authors say it can be seen in hindsight as a special case of the unscented transform. They use the simpler derivation of Wu et al. (2006), which is equivalent (p. 142). Because of (8.25)–(8.26) it suffices to treat $\int\mathbf g(\boldsymbol\xi)\mathrm N(\boldsymbol\xi\mid\mathbf 0,\mathbf I)d\boldsymbol\xi$ (8.39). Seek a $2n$-point rule
$$\int\mathbf g(\boldsymbol\xi)\mathrm N(\boldsymbol\xi\mid\mathbf 0,\mathbf I)d\boldsymbol\xi\approx W\sum_i\mathbf g(c\,\mathbf u^{(i)})\tag{8.40}$$
with points in the symmetric set $[1]=\{\pm\mathbf e_1,\dots,\pm\mathbf e_n\}$, i.e. $(1,0,\dots,0)$, $(0,1,0,\dots)$, $(-1,0,\dots)$, … (8.41) (pp. 143–144).

**Derivation (p. 144).**
1. By symmetry the rule is exact for every monomial with at least one odd exponent.
2. To be exact up to third degree it is enough to fix $W,c$ so that $g_j=1$ and $g_j=\xi_j^2$ are integrated exactly. The true values are both 1 (8.42).
3. This gives $W\sum_i1=W\,2n=1$ and $W\sum_i[c\,u_j^{(i)}]^2=W\,2c^2=1$ (8.43). (Added step: only two of the $2n$ points have a non-zero $j$th coordinate, $\pm1$.)
4. Solution: $W=\frac1{2n}$, $c=\sqrt n$ (8.44). The rule is $\int\mathbf g(\boldsymbol\xi)\mathrm N\,d\boldsymbol\xi\approx\frac1{2n}\sum_i\mathbf g(\sqrt n\,\mathbf u^{(i)})$ (8.45).

**Algorithm 8.10.** Unit sigma points $\boldsymbol\xi^{(i)}=\sqrt n\,\mathbf e_i$ for $i=1,\dots,n$ and $-\sqrt n\,\mathbf e_{i-n}$ for $i=n+1,\dots,2n$ (8.47). Then $\int\mathbf g(\mathbf x)\mathrm N(\mathbf x\mid\mathbf m,\mathbf P)d\mathbf x\approx\frac1{2n}\sum_{i=1}^{2n}\mathbf g(\mathbf m+\sqrt{\mathbf P}\boldsymbol\xi^{(i)})$ (8.48) (pp. 144–145).

Remarks (p. 145):
- Arasaratnam and Haykin's derivation is more complicated (spherical coordinates, even-order monomials). Wu et al. presented the more general generators $[u]$; Algorithm 8.10 is the special case with the useful property that its weights are always positive, which the more general methods do not always have.
- "Third order" means something different here. The $p$th order GHKF is exact up to order $2p-1$, so the third-order GHKF is exact up to fifth order. The third-order cubature rule is exact only up to third order.
- Higher-order symmetric rules exist, but not with $O(n)$ sigma points. The fifth-order rule needs a number proportional to $n^2$ (Sect. 8.9).
- Exactness to order three ensures only that the mean of $\mathbf g(\boldsymbol\xi)$ is exact for polynomials of order three. The covariance is exact only up to order one. So it is a first-order rule for the covariance.

### 8.6 Cubature Kalman filter (pp. 145–149)
Applying Algorithm 8.10 to Algorithm 8.3 gives the CKF (p. 145).

**Algorithm 8.11 (additive CKF).** It has the same structure as the GHKF template: sigma points $\mathbf m+\sqrt{\mathbf P}\boldsymbol\xi^{(i)}$, $i=1,\dots,2n$, with $\boldsymbol\xi^{(i)}$ from (8.50) $=$ (8.47). Equal weights $1/(2n)$ are used in all sums: (8.49)–(8.52) for prediction, (8.53)–(8.56) for update (pp. 146–147).

**Algorithm 8.12 (augmented, non-additive CKF).** Augment the state with the noise: $\tilde{\mathbf m}_{k-1}=(\mathbf m_{k-1};\mathbf 0)$, $\tilde{\mathbf P}_{k-1}=\mathrm{blockdiag}(\mathbf P_{k-1},\mathbf Q_{k-1})$, with $n'=n+n_q$ and $2n'$ sigma points (8.57–8.58). Propagate $\hat{\mathcal X}_k=\mathbf f(\tilde{\mathcal X}^{x},\tilde{\mathcal X}^{q})$ (8.59). Moments use weights $1/(2n')$ (8.60). The update step is analogous with $n''=n+n_r$, $\tilde{\mathbf P}_k^-=\mathrm{blockdiag}(\mathbf P_k^-,\mathbf R_k)$ and $\hat{\mathcal Y}_k=\mathbf h(\tilde{\mathcal X}^{x},\tilde{\mathcal X}^{r})$ (8.61–8.64) (pp. 147–149). No $\mathbf Q$ or $\mathbf R$ is added to the covariances.

The authors stress that the covariance computation is exact only for first-order polynomials, so the CKF is "a first order method" in that sense (p. 149).

**Examples.** Pendulum (Ex. 8.13): RMSE 0.11, between GHKF (0.10) and EKF (0.17), practically the same as GHKF (p. 149). Coordinated turn (Ex. 8.14): RMSE 0.30, the same as GHKF (p. 149). (Ex. 8.9 printed 0.030 for the GHKF; see Reading notes.)

### 8.7 Unscented transform (pp. 149–155)
Historically the UKF was the first general filtering framework to use this approach. The UT is a numerical-integration approximation to the moment-matching transform of Algorithm 8.1 (pp. 149–150).

**Derivation.** Add the origin to the cubature rule: $\int\mathbf g(\boldsymbol\xi)\mathrm N\,d\boldsymbol\xi\approx W_0\mathbf g(\mathbf 0)+W\sum_i\mathbf g(c\,\mathbf u^{(i)})$ (8.65). Requiring exactness for $g_j=1$ and $g_j=\xi_j^2$ gives, with free parameter $\kappa$,
$$W_0=\frac{\kappa}{n+\kappa},\quad W=\frac1{2(n+\kappa)},\quad c=\sqrt{n+\kappa}\tag{8.66}$$
(Added check: $W_0+2nW=\frac{\kappa+n}{n+\kappa}=1$ and $2Wc^2=1$.) Using $\sqrt{\mathbf P}\,\mathbf e_i=[\sqrt{\mathbf P}]_i$ (the $i$th column), the rule is
$$\int\mathbf g\,\mathrm N\,d\mathbf x\approx\frac{\kappa}{n+\kappa}\mathbf g(\mathcal X^{(0)})+\frac1{2(n+\kappa)}\sum_{i=1}^{2n}\mathbf g(\mathcal X^{(i)})\tag{8.69}$$
with $\mathcal X^{(0)}=\mathbf m$, $\mathcal X^{(i)}=\mathbf m+\sqrt{n+\kappa}[\sqrt{\mathbf P}]_i$, $\mathcal X^{(i+n)}=\mathbf m-\sqrt{n+\kappa}[\sqrt{\mathbf P}]_i$ (8.70) (p. 152). This rule appears in the original UT article and equals the cubature rule of Algorithm 8.10 when $\kappa=0$ (p. 152). Equivalently, propagate $\mathcal Y^{(i)}=\mathbf g(\mathcal X^{(i)})$ and use (8.71) (p. 152).

**Scaled UT (Julier, 2002).** Evaluate at $\mathcal X'^{(i)}=\mathcal X^{(0)}+\alpha(\mathcal X^{(i)}-\mathcal X^{(0)})$, $\alpha>0$ (8.72). This replaces $\sqrt{n+\kappa}$ by $\alpha\sqrt{n+\kappa}$. To keep third-order exactness one needs a modified $\lambda$ with $\alpha\sqrt{n+\kappa}=\sqrt{n+\lambda}$ (8.73), i.e. $\lambda=\alpha^2(n+\kappa)-n$ (8.74) (p. 152). The mean and covariance need not share weights. A further parameter $\beta>0$ enters only the covariance weights, to account for higher-order moments. The choice $\beta=2$ is "in a certain sense optimal for a Gaussian distribution" (pp. 152–153):
$$W_0^{(m)}=\frac{\lambda}{n+\lambda},\;W_0^{(c)}=\frac{\lambda}{n+\lambda}+(1-\alpha^2+\beta),\;W_i^{(m)}=W_i^{(c)}=\frac1{2(n+\lambda)},\ i=1,\dots,2n\tag{8.75}$$

**Algorithm 8.15 (additive UT).** Sigma points as (8.70) with $\lambda$ in place of $\kappa$ (8.77); $\mathcal Y^{(i)}=\mathbf g(\mathcal X^{(i)})$, $i=0,\dots,2n$. Then
$$\boldsymbol\mu_U=\sum_{i=0}^{2n}W_i^{(m)}\mathcal Y^{(i)},\;\mathbf S_U=\sum_{i=0}^{2n}W_i^{(c)}(\mathcal Y^{(i)}-\boldsymbol\mu_U)(\mathcal Y^{(i)}-\boldsymbol\mu_U)^{\mathsf T}+\mathbf Q,\;\mathbf C_U=\sum_{i=0}^{2n}W_i^{(c)}(\mathcal X^{(i)}-\mathbf m)(\mathcal Y^{(i)}-\boldsymbol\mu_U)^{\mathsf T}\tag{8.78}$$
with joint Gaussian (8.76) (pp. 153–154).

**Algorithm 8.16 (non-additive UT).** Augment $\tilde{\mathbf x}=(\mathbf x,\mathbf q)$ with $n'=n+n_q$, $\tilde{\mathbf m}=(\mathbf m;\mathbf 0)$, $\tilde{\mathbf P}=\mathrm{blockdiag}(\mathbf P,\mathbf Q)$, $\lambda'$ from (8.74) with $n\to n'$ (8.80). Propagate $\tilde{\mathcal Y}^{(i)}=\mathbf g(\tilde{\mathcal X}^{(i),x},\tilde{\mathcal X}^{(i),q})$. Sums are as in (8.78) over $2n'+1$ points, with weights from (8.75) using $n',\lambda'$ and with no added $\mathbf Q$ (pp. 154–155).

**Accuracy (p. 155).** The mean estimate is exact for polynomials up to order three. The covariance is exact only for first-order polynomials: the square of a second-order polynomial is already order four, which the UT does not integrate exactly. So the UT is "only a first order method". With $\kappa=3-n$ some, but not all, fourth-order terms in the covariance are correct for quadratic functions.

*Intuition note.* The UT is a cubature rule with an optional centre point and a tunable spread. Moving points toward or away from the mean ($\alpha$) and re-weighting ($\kappa,\beta$) changes how higher moments enter. All of these rules are still exact only to a limited polynomial degree.

### 8.8 Unscented Kalman filter (pp. 155–161)
The UKF uses the UT to approximate the general Gaussian filters 8.3 and 8.4 (p. 155).

**Algorithm 8.17 (additive UKF).** Prediction: sigma points $\mathcal X_{k-1}^{(0)}=\mathbf m_{k-1}$, $\mathcal X_{k-1}^{(i)}=\mathbf m_{k-1}\pm\sqrt{n+\lambda}[\sqrt{\mathbf P_{k-1}}]_i$ (8.82); propagate through $\mathbf f$ for $i=0,\dots,2n$ (8.83); $\mathbf m_k^-=\sum W_i^{(m)}\hat{\mathcal X}_k^{(i)}$, $\mathbf P_k^-=\sum W_i^{(c)}(\hat{\mathcal X}_k^{(i)}-\mathbf m_k^-)(\cdot)^{\mathsf T}+\mathbf Q_{k-1}$ (8.84). Update: the same pattern with $\mathbf P_k^-$ and $\mathbf h$ (8.85–8.87), then $\mathbf K_k,\mathbf m_k,\mathbf P_k$ exactly as in (8.9) (8.88) (pp. 156–157). The authors say the derivation parallels the EKF and Gaussian filter, with the UT used in place of linearization or moment matching (p. 157).

**Algorithm 8.18 (augmented UKF).** Augment state with process noise (prediction) and state with measurement noise (update), as in Alg. 8.12 but with $2n'+1$ and $2n''+1$ points, centre point, and weights (8.75) with $n',\lambda'$ resp. $n'',\lambda''$ (8.89–8.95) (pp. 157–159). The authors note that augmenting both noises at once and applying the UT in one step differs from the moment-matching Gaussian filter, whereas augmenting the process noise for prediction and the measurement noise for update corresponds to it (p. 157).

**Discussion (pp. 159–160).** The UKF was proposed as an improvement over the EKF. It does not rely on a linearization at a single point. The authors say, following Julier and Uhlmann (2004), that the UT captures higher-order moments caused by the non-linearity better than Taylor-series approximations. The mean is exact up to order three, but the covariance only up to order one. The model functions need not be differentiable and no Jacobians are needed. The disadvantage is that the UKF often needs slightly more operations than the EKF (p. 160).

**Examples.** Pendulum (Ex. 8.19): RMSE 0.10, same as GHKF, better than EKF (0.17) and CKF (0.11) (p. 160). Coordinated turn (Ex. 8.20): RMSE 0.30, same as CKF and GHKF (p. 160).

**Unification (p. 161).** The UKF's sigma-point step differs from the GHKF/CKF only superficially. Using columns of the Cholesky factor is equivalent to using unit sigma points $\boldsymbol\xi^{(i)}=\sqrt{n+\lambda}\,\mathbf e_i$ ($i\le n$), $-\sqrt{n+\lambda}\,\mathbf e_{i-n}$ (8.96), because $\sqrt{\mathbf P}(c\,\mathbf e_i)=c[\sqrt{\mathbf P}]_i$. Different weights for mean and covariance are not unique to the UKF: any numerical-integration filter could use different rules for different integrals, but the authors did not discuss this for the other filters.

### 8.9 Higher-order cubature/unscented Kalman filters (pp. 162–166)
Higher-order rules use symmetric sets: $[0]=\{\mathbf 0\}$ and $[u]=\{(u,0,\dots,0),(-u,0,\dots),(0,u,\dots),\dots\}$. The unscented rule is $\int\mathbf g\,\mathrm N\,d\boldsymbol\xi\approx W_0\sum_{[0]}\mathbf g+W\sum_{[c]}\mathbf g$ (8.97), and the cubature rule is the case $\kappa=0$ (8.98) (p. 162).

A fifth-order symmetric rule has the form
$$\int\mathbf g(\boldsymbol\xi)\mathrm N(\boldsymbol\xi\mid\mathbf 0,\mathbf I)d\boldsymbol\xi\approx W_0\sum_{[0]}\mathbf g+W^{(1)}\sum_{[u]}\mathbf g+W^{(2)}\sum_{[u,u]}\mathbf g\tag{8.99}$$
where $[u,u]$ contains all vectors with exactly two non-zero entries equal to $\pm u$. In 3-D, $[1,1]$ has 12 vectors (8.100) (p. 162). Per McNamee–Stenger and Wu et al., it integrates monomials up to fifth order if $u=\sqrt3$, $W_0=1+(n^2-7n)/18$, $W_1=(4-n)/18$, $W_2=1/36$ (pp. 162–163).

**Algorithm 8.21.** $\boldsymbol\xi^{(0)}=\mathbf 0$; $\boldsymbol\xi^{(i)}$, $i=1,\dots,2n$: the $i$th vector in $[\sqrt3]$; $\boldsymbol\xi^{(i+2n)}$: the $i$th vector in $[\sqrt3,\sqrt3]$ (8.102). Weights (8.103): $W_0=1+(n^2-7n)/18$, $W_i=(4-n)/18$ ($i=1,\dots,2n$), $W_{i+2n}=1/36$. Approximation $\sum_iW_i\mathbf g(\mathbf m+\sqrt{\mathbf P}\boldsymbol\xi^{(i)})$ (8.104) (p. 163).

Disadvantage: negative weights when $n\ge5$, typical of higher-order symmetric rules; this can give non-positive-definite covariances and hence unstable filters (p. 163).

**Algorithm 8.22 (UKF5, additive).** Same template as the other filters with the sigma points (8.102) and weights (8.103), using index $i=0,1,2,\dots$ (8.105–8.111) (pp. 163–164). The non-additive version could be derived like the CKF. By changing weights and unit sigma points, the algorithm serves as a prototype for filters based on any rule of this form (p. 165).

**Examples.** Pendulum (Ex. 8.23): RMSE 0.10, practically the same as GHKF and UKF. Coordinated turn (Ex. 8.24): RMSE 0.30, similar to GHKF, CKF and UKF (p. 165).

### 8.10 Exercises (pp. 166–167)
Twelve exercises (listed below).

## Toy example (ours, not from the text)
Take $n=1$, $g(x)=x^2$, $x\sim\mathrm N(m=1,P=4)$, so $\sqrt P=2$. Exact values: $\mathrm E[x^2]=m^2+P=5$; $\mathrm{Var}[x^2]=2P^2+4m^2P=32+16=48$; $\mathrm{Cov}(x,x^2)=2mP=8$.

*Cubature rule (8.48), $n=1$:* points $m\pm\sqrt n\sqrt P=1\pm2=3,-1$; weights $\tfrac12$ each. $y=9,1$.
- Mean $=\tfrac12(9+1)=5$ (exact).
- Variance $=\tfrac12[(9-5)^2+(1-5)^2]=\tfrac12(16+16)=16$ (true 48: wrong).
- Cross-covariance $=\tfrac12[(3-1)(9-5)+(-1-1)(1-5)]=\tfrac12(8+8)=8$ (exact).

The mean is exact (degree 2 $\le3$) but the covariance involves a degree-4 integrand, which is not integrated exactly.

*Gauss–Hermite $p=3$:* roots of $H_3=x^3-3x$ are $0,\pm\sqrt3$. By (8.23): $W=3!/(9\cdot[H_2(0)]^2)=6/9=\tfrac23$ at 0, and $6/(9\cdot2^2)=\tfrac16$ at $\pm\sqrt3$. Points $x=1+2\xi$: $1,\ 1+2\sqrt3,\ 1-2\sqrt3$; $y=1,\ 13+4\sqrt3,\ 13-4\sqrt3$.
- Mean $=\tfrac23\cdot1+\tfrac16\cdot26=\tfrac23+\tfrac{13}3=5$.
- $y-5=-4,\ 8+4\sqrt3,\ 8-4\sqrt3$; squares $16,\ 112+64\sqrt3,\ 112-64\sqrt3$. Variance $=\tfrac23\cdot16+\tfrac16\cdot224=\tfrac{32}3+\tfrac{112}3=48$. Exact, as the rule is exact to degree $2p-1=5\ge4$.

## Concepts
- [[moment-matching]] (new) — approximating a distribution by a Gaussian with its true mean and covariance, computed via integrals (p. 131)
- [[gaussian-filter-adf]] (new) — Gaussian assumed-density filter: Kalman-form recursion with moment integrals (p. 133)
- [[kalman-filter]] — here the gain/conditioning step $\mathbf K=\mathbf C\mathbf S^{-1}$ reused with integral-based $\boldsymbol\mu,\mathbf S,\mathbf C$ (p. 134)
- [[kalman-gain]] — $\mathbf K_k=\mathbf C_k\mathbf S_k^{-1}$ (p. 134)
- [[linearization]] — the EKF alternative this chapter replaces by integration (p. 133)
- [[sigma-points]] (new) — evaluation points of a numerical integration rule, used to propagate a Gaussian (p. 137)
- [[gauss-hermite-cubature]] (new) — product of 1-D Gauss–Hermite rules; exact for degrees $\le2p-1$; $p^n$ points (p. 139)
- [[spherical-cubature-rule]] (new) — $2n$ points at $\pm\sqrt n\,\mathbf e_i$, weights $1/(2n)$, third order (p. 144)
- [[unscented-transform]] (new) — $2n+1$ point rule with parameters $\kappa,\alpha,\beta$ and separate mean/covariance weights (pp. 150–153)
- [[curse-of-dimensionality-quadrature]] (new) — the $p^n$ growth of tensor-product rules (p. 137)

## Canonical instances
- [[pendulum-tracking]] — RMSE: EKF/IEKF 0.17, GHKF 0.10, CKF 0.11, UKF 0.10, UKF5 0.10 (pp. 141, 149, 160, 165)
- [[coordinated-turn-model]] — RMSE 0.30 for CKF, UKF, UKF5 (and GHKF in Ex. 8.14/8.20, but 0.030 in Ex. 8.9); the GHKF result is called practically the same as the EKF (pp. 142, 149, 160, 165)

## Bridges (candidates)
- [structural-analogy] Sigma-point propagation (UKF) ↔ control-theory: Kalman filter prediction/correction with non-linear dynamics; the Kalman filter is replaced by $\mathbf K=\mathbf C\mathbf S^{-1}$ built from integral-based moments.
- [same-math] Gauss–Hermite quadrature rule (8.17) ↔ numerical analysis: Gauss quadrature with Gaussian weight; points are Hermite roots.
- [structural-analogy] Moment matching to an assumed density ↔ approximate inference: fitting a Gaussian to match mean and covariance of an intractable posterior.

## Questions this raises
- How large can the moment-matching error become when the true filtering density is strongly non-Gaussian (e.g. multimodal)? The chapter only reports RMSEs on two examples.
- How should $\kappa$, $\alpha$, $\beta$ be chosen in practice, and what exactly does "optimal for a Gaussian" mean for $\beta=2$?
- Can negative-weight rules (n ≥ 5 for the fifth-order rule) be used safely, e.g. with covariance corrections?
- Exercise 8.7 asks whether UKF, GHKF and CKF can be made identical by parameter choice. How general is that?

## Exercises worth doing
- Ex. 8.1 (p. 166) — shows $\kappa=3-n$ integrates $\xi_i^4$ exactly and what happens to the weights for $n>3$ — difficulty: medium
- Ex. 8.2 (p. 166) — UT and cubature are exact for linear functions — difficulty: easy
- Ex. 8.3 (p. 166) — orthogonality of 1-D Hermite polynomials under the Gaussian inner product (8.112) — difficulty: medium
- Ex. 8.7 (p. 167) — implement CKF/UKF vs EKF/GHKF; find parameters that make them identical — difficulty: medium
- Ex. 8.10 (p. 167) — numerically check exactness orders (third for 8.5/8.7, fifth for 8.9) — difficulty: medium
- Ex. 8.6 (p. 167) — write the cubature transform from Algorithm 8.1 plus Algorithm 8.10 — difficulty: easy

## Reading notes
- Printed pages 131–167 (pdf 161–197); printed = pdf − 30.
- Inconsistency in RMSE reporting: Example 8.9 and Figure 8.2 give GHKF position RMSE as 0.030 (p. 142–143), while Example 8.14 says CKF's 0.30 is the same as GHKF's, and Figure 8.4 caption says 0.30 "matches that of GHKF" (pp. 149, 151). The images show 0.030 and 0.30 as printed. Probably one is a misprint; I did not resolve it.
- Misprint in (8.94) (p. 159): the image shows $W_{i-1}^{(c)''}$ in the $\mathbf S_k$ sum, where $W_i^{(c)''}$ is expected, as in (8.78) and (8.87).
- "Chokesly" misspelling for Cholesky on p. 161.
- Pages 152 and 161: the text's notation $\sqrt{\mathbf P}\,\mathbf e_i=[\sqrt{\mathbf P}]_i$ is as printed.
- In Alg. 8.12 and Alg. 8.16 the covariance formulas do not add $\mathbf Q$ or $\mathbf R$ (the noise enters through the augmented vector).
- Header on every page: pre-publication version of the Cambridge University Press second edition. Text-layer equations are garbled; all equations here were read from page images.
