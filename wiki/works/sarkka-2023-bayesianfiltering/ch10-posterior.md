---
id: sarkka-2023-bayesianfiltering/ch10-posterior
work: sarkka-2023-bayesianfiltering
unit: "10 Posterior Linearization Filtering"
pages: 204-228
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Posterior Linearization Filtering

## L0 — One line
Linearize the measurement model with respect to the (iteratively improved) approximate posterior instead of the prior, then do an ordinary Kalman update; this gives the iterated posterior linearization filters.

## L1 — The gist (≤ 120 words)
Gaussian filters linearize the models and then apply Kalman equations. Statistical linear regression (SLR) normally averages over the prior or predicted distribution. This chapter asks whether another linearization distribution is better. The proposed answer: use the posterior, since that is where the state is expected to lie after measuring. The posterior is unknown, so iterated posterior linearization (IPL) re-linearizes around the latest posterior approximation. This gives iterated posterior linearization filters (IPLFs) for additive-noise, non-additive-noise and conditional-distribution models, with sigma-point and Monte Carlo versions. The chapter also states in what sense Taylor, statistical, SLR and posterior linearizations are optimal.

**Prerequisites:** Kalman filter update equations; Gaussian moments; statistical linear regression and sigma-point (cubature, Gauss–Hermite) integration from Chapters 8–9; Kullback–Leibler divergence.

## L2 — Key ideas (5–10 bullets)
- Generalized SLR (GSLR) lets the distribution used for linearization, $\pi(\mathbf x)$, differ from the distribution of $\mathbf x$ in the estimation problem. It then no longer reduces to moment matching (the linear model reproducing the true means and covariances of $(\mathbf x,\mathbf y)$) (pp. 204–206).
- Posterior linearization (PL) sets $\pi(\mathbf x)=p(\mathbf x\mid\mathbf y)$. The linearization is then accurate where the state is expected to be after measuring (pp. 206–208).
- The posterior is unknown, so IPL runs a loop: linearize at the current posterior approximation, update the *prior* with that linear model, repeat (Algorithm 10.6, pp. 209–210).
- In the scalar example $y=x^3+q$, the first IPL iteration equals prior SLR (moment matching). After two iterations the approximation is accurate, and after three it is hard to distinguish from the true posterior (pp. 210–211).
- IPLF = ordinary Gaussian-filter prediction + IPL measurement update. Between additive, non-additive, conditional-moment and conditional-distribution models, the update changes only in its moment integrals, while (10.14)–(10.15) stay the same; the prediction integrals also depend on the model (pp. 212–217).
- Sigma-point and Monte Carlo versions approximate the integrals. Monte Carlo needs care with convergence of the inner iteration (pp. 217–224).
- IPLF performs SLR where the iterated extended Kalman filter (IEKF) uses a first-order Taylor expansion (pp. 213–214). In the two examples shown, iteration appears not to improve on non-iterated Gaussian filters for the pendulum, and helps only at start-up from an inaccurate initial guess in the coordinated turn model (pp. 219–220).
- Optimality: Taylor is optimal infinitesimally close to a point. Statistical linearization (SL) and SLR minimize an average squared error under a distribution; SLR also minimizes an expected Kullback–Leibler (KL) divergence criterion. PL gives posterior moments that match the exact posterior up to the Gaussian approximations used on the way, so it is maximally accurate at the posterior (pp. 225–227).

## L3 — Walkthrough

**Intro (p. 204).** Chapter 9 showed that the Gaussian filters are "linearize, then Kalman". How we linearize matters, and any affine function with additive Gaussian noise may be used. Posterior and iterated posterior linearization come from García-Fernández et al. (2015) and Tronarp et al. (2018).

### 10.1 Generalized Statistical Linear Regression (pp. 204–206)
In the SLR filters, the prediction/update distributions of $\mathbf x_k$ were implicitly the linearization distribution, which gave moment matching. There is no inherent reason for this; the IEKF already decoupled linearization point from the distribution by iterating (p. 204).

**Definition 10.1 (GSLR).** Let $\pi(\mathbf x)$ be an arbitrary linearization distribution. Then $\mathbf y\simeq \mathbf A\mathbf x+\mathbf b+\tilde{\mathbf e}$, $\tilde{\mathbf e}\sim\mathrm N(\mathbf 0,\boldsymbol\Lambda)$, is a statistical linear regression with respect to $\pi$ if $\mathbf A,\mathbf b$ minimize
$$\mathrm{MSE}(\mathbf A,\mathbf b)=\mathrm E_\pi\!\left[(\mathbf y-\mathbf A\mathbf x-\mathbf b)^{\mathsf T}(\mathbf y-\mathbf A\mathbf x-\mathbf b)\right],\tag{10.1}$$
with $\mathbf A,\mathbf b$ deterministic, and the noise covariance is
$$\boldsymbol\Lambda=\mathrm E_\pi\!\left[(\mathbf y-\mathbf A\mathbf x-\mathbf b)(\mathbf y-\mathbf A\mathbf x-\mathbf b)^{\mathsf T}\right].\tag{10.2}$$
(p. 205)

**Theorem 10.2.** With $\mathbf m_\pi=\mathrm E_\pi[\mathbf x]$, $\mathbf P_\pi=\mathrm{Cov}_\pi[\mathbf x]$, $\boldsymbol\mu_G=\mathrm E_\pi[\mathbf y]$, $\mathbf S_G=\mathrm{Cov}_\pi[\mathbf y]$, $\mathbf C_G=\mathrm{Cov}_\pi[\mathbf x,\mathbf y]$:
$$\mathbf A=\mathbf C_G^{\mathsf T}\mathbf P_\pi^{-1},\quad \mathbf b=\boldsymbol\mu_G-\mathbf A\mathbf m_\pi,\quad \boldsymbol\Lambda=\mathbf S_G-\mathbf A\mathbf P_\pi\mathbf A^{\mathsf T}.\tag{10.3}$$
The proof is the same as for Theorem 9.12 (p. 205).

**Corollary 10.3.** For $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$, $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$, $\mathbf q\sim\mathrm N(\mathbf 0,\mathbf Q)$, the GSLR parameters are again (10.4) = (10.3), with
$$\mathbf m_\pi=\!\int\!\mathbf x\,\pi\,d\mathbf x,\ \ \mathbf P_\pi=\!\int\!(\mathbf x-\mathbf m_\pi)(\mathbf x-\mathbf m_\pi)^{\mathsf T}\pi\,d\mathbf x,\ \ \boldsymbol\mu_G=\!\int\!\mathbf g(\mathbf x)\pi\,d\mathbf x,$$
$$\mathbf C_G=\!\int\!(\mathbf x-\mathbf m_\pi)(\mathbf g(\mathbf x)-\boldsymbol\mu_G)^{\mathsf T}\pi\,d\mathbf x,\ \ \mathbf S_G=\!\int\!(\mathbf g(\mathbf x)-\boldsymbol\mu_G)(\mathbf g(\mathbf x)-\boldsymbol\mu_G)^{\mathsf T}\pi\,d\mathbf x+\mathbf Q.\tag{10.5}$$
The joint Gaussian approximation is
$$\begin{pmatrix}\mathbf x\\\mathbf y\end{pmatrix}\sim\mathrm N\!\left(\begin{pmatrix}\mathbf m\\\mathbf A\mathbf m+\mathbf b\end{pmatrix},\begin{pmatrix}\mathbf P&\mathbf P\mathbf A^{\mathsf T}\\\mathbf A\mathbf P&\mathbf A\mathbf P\mathbf A^{\mathsf T}+\mathbf Q\end{pmatrix}\right).\tag{10.6}$$
(pp. 205–206)

The key point: this no longer reduces to moment matching, because $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$ differs from $\pi$. The moments of the joint approximation then no longer exactly match the true ones when $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$. The authors turn this into an advantage: we want accuracy for the posterior of $\mathbf x$, not the prior (p. 206).

*Intuition note.* The regression line is fitted by averaging over some distribution of $\mathbf x$. Whoever picks that distribution decides where the line is most accurate. Choosing it equal to the true distribution gives moment matching; choosing something else buys accuracy elsewhere.

### 10.2 Posterior Linearization (pp. 206–208)
After measuring, belief about $\mathbf x$ changes, so the posterior is a more suitable linearization distribution than the prior (p. 206). The discussion is restricted to SLR, since SL is a deterministic version of SLR that ignores the approximation error (p. 207).

**Definition 10.4 (PL).** Given an observed $\mathbf y$ with posterior $p(\mathbf x\mid\mathbf y)$, put $\pi(\mathbf x)=p(\mathbf x\mid\mathbf y)$ and form $\mathbf y\simeq\mathbf A\mathbf x+\mathbf b+\tilde{\mathbf e}$ by GSLR. For $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$ this is Corollary 10.3 with $\pi=p(\mathbf x\mid\mathbf y)$ (p. 207).

The catch: forming PL needs the posterior, which linearization is meant to approximate. This is resolved in 10.3 (p. 207). The original is called *prior SLR*; PL is *posterior SLR* (p. 207).

With the linearized model and Gaussian prior $\mathrm N(\mathbf m,\mathbf P)$, the posterior moments are the Kalman update
$$\boldsymbol\mu=\mathbf A\mathbf m+\mathbf b,\ \ \mathbf S=\mathbf A\mathbf P\mathbf A^{\mathsf T}+\boldsymbol\Lambda,\ \ \mathbf K=\mathbf P\mathbf A^{\mathsf T}\mathbf S^{-1},\ \ \mathbf m^+=\mathbf m+\mathbf K(\mathbf y-\boldsymbol\mu),\ \ \mathbf P^+=\mathbf P-\mathbf K\mathbf S\mathbf K^{\mathsf T}.\tag{10.7}$$
Prior SLR and PL both use (10.7) but with different $\mathbf A,\mathbf b,\boldsymbol\Lambda$ (pp. 207–208). Prior SLR is moment matched only for the prior of $\mathbf x$; PL is maximally accurate when $\mathbf x$ follows the posterior. Both properties relate to KL-divergence optimality (Section 10.6) (p. 208).

**Example 10.5.** $x\sim\mathrm N(1,0.1)$, $g(x)=x^3$, $y=g(x)+q$, $q\sim\mathrm N(0,0.1)$, observed $y=5$. The posterior is centred near $x\simeq1.7$. PL fits $g$ near 1.7; prior SLR fits near the prior mean 1. The linearization-noise standard deviation $\sqrt\Lambda$ is about 0.45 (prior SLR) versus about 0.01 (posterior SLR), because the posterior variance is much smaller. The posterior from PL overlaps the true posterior; prior SLR gives larger variance and a different mean. "At least in this example" PL is more accurate (p. 208, Fig. 10.1).

*Intuition note.* A straight line cannot follow $x^3$ everywhere, so it is better to fit it where the answer will actually lie. After a strong measurement that region is narrow, so the fit can be tight.

### 10.3 Iterated Posterior Linearization (pp. 208–211)
Idea: always linearize with respect to the best available posterior approximation (p. 208).

**Algorithm 10.6 (IPL).** Given $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$, prior $\mathrm N(\mathbf m,\mathbf P)$, observation $\mathbf y$: start with $\mathbf m^{(0)}=\mathbf m$, $\mathbf P^{(0)}=\mathbf P$. For $i=1,2,\dots$:

1. Linearize:
$$\mathbf A^{(i)}=[\mathbf P^{xy,(i-1)}]^{\mathsf T}[\mathbf P^{(i-1)}]^{-1},\ \ \mathbf b^{(i)}=\boldsymbol\mu^{+,(i-1)}-\mathbf A^{(i)}\mathbf m^{(i-1)},\ \ \boldsymbol\Lambda^{(i)}=\mathbf P^{y,(i-1)}-\mathbf A^{(i)}\mathbf P^{(i-1)}[\mathbf A^{(i)}]^{\mathsf T}\tag{10.9}$$
with moments taken under $\mathrm N(\mathbf x\mid\mathbf m^{(i-1)},\mathbf P^{(i-1)})$:
$$\boldsymbol\mu^{+,(i-1)}=\!\int\!\mathbf g(\mathbf x)\,\mathrm N(\cdot)\,d\mathbf x,\ \ \mathbf P^{xy,(i-1)}=\!\int\!(\mathbf x-\mathbf m^{(i-1)})(\mathbf g(\mathbf x)-\boldsymbol\mu^{+,(i-1)})^{\mathsf T}\mathrm N(\cdot)\,d\mathbf x,$$
$$\mathbf P^{y,(i-1)}=\!\int\!(\mathbf g(\mathbf x)-\boldsymbol\mu^{+,(i-1)})(\mathbf g(\mathbf x)-\boldsymbol\mu^{+,(i-1)})^{\mathsf T}\mathrm N(\cdot)\,d\mathbf x+\mathbf Q.\tag{10.10}$$
2. Update (shapes: $\mathbf m,\mathbf m^{(i)}\in\mathbb R^n$, $\mathbf P\in\mathbb R^{n\times n}$, $\mathbf A^{(i)}\in\mathbb R^{d\times n}$ for $\mathbf y\in\mathbb R^d$; this is added bookkeeping):
$$\boldsymbol\mu^{(i)}=\mathbf A^{(i)}\mathbf m+\mathbf b^{(i)},\ \ \mathbf S^{(i)}=\mathbf A^{(i)}\mathbf P[\mathbf A^{(i)}]^{\mathsf T}+\boldsymbol\Lambda^{(i)},\ \ \mathbf K^{(i)}=\mathbf P[\mathbf A^{(i)}]^{\mathsf T}\mathbf S^{-1},$$
$$\mathbf m^{(i)}=\mathbf m+\mathbf K^{(i)}(\mathbf y-\boldsymbol\mu^{(i)}),\ \ \mathbf P^{(i)}=\mathbf P-\mathbf K^{(i)}\mathbf S^{(i)}[\mathbf K^{(i)}]^{\mathsf T}.\tag{10.11}$$
(pp. 209–210)

Important: the update step starts from the *prior* $\mathrm N(\mathbf m,\mathbf P)$. The latest posterior approximation is only used to linearize, not explicitly in the update (p. 210). The first iteration linearizes at the prior.

*Intuition note.* Each pass asks, "if the state were near my current guess, what straight-line-plus-noise model fits the sensor there?". It then redoes the Kalman update with that model. The hope is that a better guess gives a better model, and so a better guess again.

**Example 10.7.** Same model as Example 10.5. After iteration 1, IPL equals prior SLR (which equals moment matching in general Gaussian filters). After two iterations the approximation is accurate; after three it is hard to distinguish from the true posterior (pp. 210–211, Fig. 10.2).

**Remarks (p. 211).**
- The integrals can be computed with the strategies of Chapter 9, so IPL also applies to non-additive and conditional-distribution models.
- If the integrals are approximated by Taylor-series linearization at the current guess, we obtain a Gauss–Newton method, also the basis of the IEKF.
- If the posterior variance is small, moment matching and Taylor expansion coincide, and we again get Gauss–Newton.
- When measurement noise is large, the posterior resembles the prior, so prior and posterior SLR are likely to give similar results.

### 10.4 Iterated Posterior Linearization Filter (pp. 212–217)
Prediction is done as in the general Gaussian filters (Chapter 8); IPL is used in the measurement update (p. 212).

**Algorithm 10.8 (IPLF I, additive noise).**
Prediction:
$$\mathbf m_k^-=\!\int\!\mathbf f(\mathbf x)\mathrm N(\mathbf x\mid\mathbf m_{k-1},\mathbf P_{k-1})d\mathbf x,\ \ \mathbf P_k^-=\!\int\!(\mathbf f(\mathbf x)-\mathbf m_k^-)(\mathbf f(\mathbf x)-\mathbf m_k^-)^{\mathsf T}\mathrm N(\cdot)d\mathbf x+\mathbf Q_{k-1}.\tag{10.12}$$
Update: start from $\mathbf m_k^{(0)}=\mathbf m_k^-$, $\mathbf P_k^{(0)}=\mathbf P_k^-$. For $i=1,2,\dots$, with all integrals under $\mathbf x_k\sim\mathrm N(\mathbf m_k^{(i-1)},\mathbf P_k^{(i-1)})$:
$$\boldsymbol\mu_k^{+,(i-1)}=\!\int\!\mathbf h_k(\mathbf x)\mathrm N(\cdot)d\mathbf x,\ \ \mathbf P_k^{xy,(i-1)}=\!\int\!(\mathbf x-\mathbf m_k^{(i-1)})(\mathbf h_k(\mathbf x)-\boldsymbol\mu_k^{+,(i-1)})^{\mathsf T}\mathrm N(\cdot)d\mathbf x,$$
$$\mathbf P_k^{y,(i-1)}=\!\int\!(\mathbf h_k(\mathbf x)-\boldsymbol\mu_k^{+,(i-1)})(\mathbf h_k(\mathbf x)-\boldsymbol\mu_k^{+,(i-1)})^{\mathsf T}\mathrm N(\cdot)d\mathbf x+\mathbf R_k.\tag{10.13}$$
Linearize:
$$\mathbf H_k^{(i)}=[\mathbf P_k^{xy,(i-1)}]^{\mathsf T}[\mathbf P_k^{(i-1)}]^{-1},\ \ \mathbf b_k^{(i)}=\boldsymbol\mu_k^{+,(i-1)}-\mathbf H_k^{(i)}\mathbf m_k^{(i-1)},\ \ \boldsymbol\Omega_k^{(i)}=\mathbf P_k^{y,(i-1)}-\mathbf H_k^{(i)}\mathbf P_k^{(i-1)}(\mathbf H_k^{(i)})^{\mathsf T}.\tag{10.14}$$
Kalman update from the predicted moments:
$$\boldsymbol\mu_k^{(i)}=\mathbf H_k^{(i)}\mathbf m_k^-+\mathbf b_k^{(i)},\ \ \mathbf S_k^{(i)}=\mathbf H_k^{(i)}\mathbf P_k^-(\mathbf H_k^{(i)})^{\mathsf T}+\boldsymbol\Omega_k^{(i)},\ \ \mathbf K_k^{(i)}=\mathbf P_k^-(\mathbf H_k^{(i)})^{\mathsf T}(\mathbf S_k^{(i)})^{-1},$$
$$\mathbf m_k^{(i)}=\mathbf m_k^-+\mathbf K_k^{(i)}(\mathbf y_k-\boldsymbol\mu_k^{(i)}),\ \ \mathbf P_k^{(i)}=\mathbf P_k^--\mathbf K_k^{(i)}\mathbf S_k^{(i)}(\mathbf K_k^{(i)})^{\mathsf T}.\tag{10.15}$$
At convergence set $\mathbf m_k=\mathbf m_k^{(i)}$, $\mathbf P_k=\mathbf P_k^{(i)}$ (pp. 212–213).

Relation to other filters (pp. 213–214):
- The prediction equals that in Algorithms 8.3 and 9.21. Algorithm 9.20 gives the same prediction but the others use simplified expressions.
- The update is closely related to Algorithm 9.20, which linearizes with respect to $\mathrm N(\mathbf m_k^-,\mathbf P_k^-)$ and simplifies to 9.21. IPLF linearizes with respect to the iterated posterior approximation, which prevents that simplification.
- Compared with the IEKF (Algorithm 7.9): both linearize using the posterior. IEKF uses a first-order Taylor expansion about $\mathbf m_k^{(i-1)}$; IPLF uses SLR, which is accurate on average across the chosen distribution and has benefits over Taylor "in some contexts".

**Algorithm 10.9 (IPLF II, non-additive noise).** In the IPL-based update step only the moment integrals change; (10.14) and (10.15) stay as they are. Prediction (10.16) integrates $\mathbf f(\mathbf x_{k-1},\mathbf q_{k-1})$ over $\mathrm N(\mathbf x_{k-1}\mid\mathbf m_{k-1},\mathbf P_{k-1})\,\mathrm N(\mathbf q_{k-1}\mid\mathbf 0,\mathbf Q_{k-1})$ for mean and covariance (no added $\mathbf Q$). Update moments (10.17) use $\mathbf h(\mathbf x_k,\mathbf r_k)$ under $\mathrm N(\mathbf x_k\mid\mathbf m_k^{(i-1)},\mathbf P_k^{(i-1)})\,\mathrm N(\mathbf r_k\mid\mathbf 0,\mathbf R_k)$, with no added $\mathbf R_k$ (pp. 214–215).

**Algorithm 10.10 (IPLF III, conditional moments).** Assuming the conditional moments of (9.68) can be computed: prediction uses $\mathbf m_k^-=\int\boldsymbol\mu_k^-(\mathbf x)\mathrm N\,d\mathbf x$ and $\mathbf P_k^-=\int(\boldsymbol\mu_k^--\mathbf m_k^-)(\cdot)^{\mathsf T}\mathrm N\,d\mathbf x+\int\mathbf P_k^x(\mathbf x)\mathrm N\,d\mathbf x$ (10.18). Update moments (10.19) use $\boldsymbol\mu_k(\mathbf x)$ in place of $\mathbf h_k$, and $\mathbf P_k^{y,(i-1)}$ has the extra term $\int\mathbf P_k^y(\mathbf x)\mathrm N\,d\mathbf x$. It works for all model types if these moments are computable. For additive noise it simplifies to Algorithm 10.8. The conditional moments for the other types are in (A.55)/(A.63) and (A.56)/(A.64). A closed form also exists for models with state-dependent covariance, $p(\mathbf x_k\mid\mathbf x_{k-1})=\mathrm N(\mathbf f_{k-1}(\mathbf x_{k-1}),\mathbf Q_{k-1}(\mathbf x_{k-1}))$ (pp. 215–216).

**Algorithm 10.11 (IPLF IV, conditional distributions).** Moments are written as integrals over $\mathbf y_k\,p(\mathbf y_k\mid\mathbf x_k)\,\mathrm N(\mathbf x_k\mid\mathbf m_k^{(i-1)},\mathbf P_k^{(i-1)})$ (prediction: $\mathbf x_k\,p(\mathbf x_k\mid\mathbf x_{k-1})\,\mathrm N(\mathbf x_{k-1}\mid\cdot)$), eqs. (10.20)–(10.21). Steps 2–3 are (10.14) and (10.15) (pp. 216–217).

### 10.5 Practical Iterated Posterior Linearization Filters (pp. 217–225)
**Algorithm 10.12 (sigma-point IPLF I, additive noise).** Prediction: sigma points $\mathcal X_{k-1}^{(j)}=\mathbf m_{k-1}+\sqrt{\mathbf P_{k-1}}\boldsymbol\xi^{(j)}$ (10.22), $\mathcal X_k^{-(j)}=\mathbf f(\mathcal X_{k-1}^{(j)})$ (10.23), then
$$\mathbf m_k^-=\sum_{j=1}^mW_j\mathcal X_k^{-(j)},\ \ \mathbf P_k^-=\sum_{j=1}^mW_j(\mathcal X_k^{-(j)}-\mathbf m_k^-)(\mathcal X_k^{-(j)}-\mathbf m_k^-)^{\mathsf T}+\mathbf Q_{k-1}.\tag{10.24}$$
Update, per iteration: $\mathcal X_k^{(j)}=\mathbf m_k^{(i-1)}+\sqrt{\mathbf P_k^{(i-1)}}\boldsymbol\xi^{(j)}$ (10.25), $\mathcal Y_k^{(j)}=\mathbf h(\mathcal X_k^{(j)})$ (10.26), and
$$\boldsymbol\mu_k^{+,(i-1)}=\sum_jW_j\mathcal Y_k^{(j)},\ \ \mathbf P_k^{xy,(i-1)}=\sum_jW_j(\mathcal X_k^{(j)}-\mathbf m_k^{(i-1)})(\mathcal Y_k^{(j)}-\boldsymbol\mu_k^{+,(i-1)})^{\mathsf T},$$
$$\mathbf P_k^{y,(i-1)}=\sum_jW_j(\mathcal Y_k^{(j)}-\boldsymbol\mu_k^{+,(i-1)})(\cdot)^{\mathsf T}+\mathbf R_k.\tag{10.27}$$
Then (10.14) and (10.15). Depending on the sigma-point choice, the prediction is identical to that of the CKF, GHKF or UKF (pp. 218–219).

**Example 10.13 (pendulum, Gauss–Hermite IPLF).** RMSE 0.14, lower than EKF and IEKF (0.17) but higher than many non-iterated Gaussian filters. The authors say it appears that, in this model and data, the iteration does not improve the result over non-iterated Gaussian filters (pp. 219–220).

**Example 10.14 (coordinated turn, inaccurate initial guess).** GHKF RMSE 0.032, IPLF 0.031, explained by faster convergence at the start. The iteration helps initialize tracking, as IEKF versus EKF does, and afterwards the result is practically identical to the non-iterated filter (p. 220, Fig. 10.4).

**Algorithm 10.15 (sigma-point IPLF II, non-additive).** As in Algorithm 8.12, build sigma points on the augmented variable: $\tilde{\mathbf m}_{k-1}=(\mathbf m_{k-1};\mathbf 0)$, $\tilde{\mathbf P}_{k-1}=\mathrm{blockdiag}(\mathbf P_{k-1},\mathbf Q_{k-1})$ (10.28). Pass the first $n$ components to $\mathbf f$'s state argument and the last $n_q$ to its noise argument (10.29); mean and covariance as in (10.30). In the update the augmentation is $(\mathbf m_k^{(i-1)};\mathbf 0)$, $\mathrm{blockdiag}(\mathbf P_k^{(i-1)},\mathbf R_k)$ (10.31). Propagate through $\mathbf h$ (10.32) and compute moments by weighted sums without adding $\mathbf R_k$ (10.33) (pp. 221–222).

**Algorithm 10.16 (sigma-point IPLF III, conditional moments).** Sigma points are propagated through $\boldsymbol\mu_k^-(\cdot),\mathbf P_k^x(\cdot)$ and $\boldsymbol\mu_k(\cdot),\mathbf P_k^y(\cdot)$ (10.34–10.38). Covariances add $\sum_jW_j\mathbf P^{(\cdot),(j)}$ to the spread of the conditional means (10.36, 10.39) (pp. 222–223).

**Algorithm 10.17 (Monte Carlo IPLF, conditional distributions).** Prediction: draw $\mathbf x_{k-1}^{(j)}\sim\mathrm N(\mathbf m_{k-1},\mathbf P_{k-1})$, $j=1..N$, then $\mathbf x_k^{-(j)}\sim p(\mathbf x_k\mid\mathbf x_{k-1}^{(j)})$, and take the sample mean and covariance (10.40–10.42). Update: draw $\mathbf x_k^{(j)}\sim\mathrm N(\mathbf m_k^{(i-1)},\mathbf P_k^{(i-1)})$, draw $\mathbf y_k^{(j)}\sim p(\mathbf y_k\mid\mathbf x_k^{(j)})$, and form sample moments (10.43–10.45); then (10.14), (10.15). Convergence of the inner iteration needs care because it is stochastic (pp. 223–225).

### 10.6 Optimality Properties of Different Linearizations (pp. 225–227)
- **Taylor** $\mathbf g(\mathbf x)\simeq\mathbf g(\mathbf m)+\mathbf G_{\mathbf x}(\mathbf m)(\mathbf x-\mathbf m)$ (10.46): optimal for approximating $\mathbf g$ infinitesimally close to $\mathbf m$. It is exact there, and accuracy drops quickly away from it (p. 225).
- **SL** $\mathbf g(\mathbf x)\simeq\mathbf A\mathbf x+\mathbf b$ (10.47) minimizes $\mathrm{MSE}=\mathrm E[(\mathbf g-\mathbf A\mathbf x-\mathbf b)^{\mathsf T}(\cdot)]$ with $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$ (10.48). It is less local than Taylor. SL can be seen as Taylor with $\mathbf g(\mathbf m)$, $\mathbf G_{\mathbf x}(\mathbf m)$ replaced by expectations over $\mathrm N(\mathbf m,\mathbf P)$, so it becomes Taylor when $\mathbf P\to\mathbf 0$ (p. 225).
- **SLR** $\mathbf y\simeq\mathbf A\mathbf x+\mathbf b+\tilde{\mathbf e}$ (10.49) makes sense for a stochastic mapping. It matches moments of $(\mathbf x,\mathbf y)$ and also minimizes a KL-based criterion (pp. 225–226). With $p(\mathbf y\mid\mathbf x)=\mathrm N(\mathbf g(\mathbf x),\mathbf Q)$ and $q(\mathbf y\mid\mathbf x)=\mathrm N(\mathbf A\mathbf x+\mathbf b,\boldsymbol\Lambda)$ (10.50):
$$\mathrm{KL}(p\|q)=\tfrac12\Big[\mathrm{tr}\{\boldsymbol\Lambda^{-1}\mathbf Q\}-n+\log\tfrac{|\boldsymbol\Lambda|}{|\mathbf Q|}+(\mathbf g-\mathbf A\mathbf x-\mathbf b)^{\mathsf T}\boldsymbol\Lambda^{-1}(\mathbf g-\mathbf A\mathbf x-\mathbf b)\Big]\tag{10.51}$$
Taking $\mathrm E$ over $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$ gives the criterion $\mathrm{MKL}(\mathbf A,\mathbf b,\boldsymbol\Lambda)$ (10.52), which SLR minimizes (Exercise 10.7). GSLR minimizes the same criterion with $\pi$ in place of $\mathrm N(\mathbf m,\mathbf P)$ (p. 226).
- For general $p(\mathbf y\mid\mathbf x)$, plugging it directly into the KL is *not* the correct generalization. The correct one approximates $p(\mathbf y\mid\mathbf x)\simeq\mathrm N(\mathbf y\mid\boldsymbol\mu_R(\mathbf x),\mathbf S_R(\mathbf x))$ (10.53) with the conditional moments of (9.46) (pp. 226–227).
- **PL** ($\pi=p(\mathbf x\mid\mathbf y)$) needs iteration. Its optimality: the posterior mean and covariance computed with the linearized model match the exact posterior up to the Gaussian approximations used on the way. So it has maximal accuracy at the posterior. The IEKF linearization is a type of PL that linearizes at the MAP estimate (p. 227).
- In Chapter 14 these methods are applied to smoothing (p. 227).

## Toy example (our own, not from the text)
Scalar $y=x^2+q$, $q\sim\mathrm N(0,1)$, prior $x\sim\mathrm N(1,1)$, observed $y=4$. For $x\sim\mathrm N(m,P)$: $\mathrm E[x^2]=m^2+P$, $\mathrm{Cov}(x,x^2)=2mP$, $\mathrm{Var}(x^2)=2P^2+4m^2P$ (standard Gaussian moments).

*Iteration 1* (linearize at prior $m=1,P=1$): $\mu_G=2$, $C=2$, $S_G=2+4+1=7$. So $A=2/1=2$, $b=2-2\cdot1=0$, $\Lambda=7-4\cdot1=3$. Update of the prior: $\mu=2$, $S=4\cdot1+3=7$, $K=2/7$, $m^{(1)}=1+\tfrac27(4-2)=11/7\approx1.571$, $P^{(1)}=1-\tfrac{4}{49}\cdot7=3/7\approx0.429$. This equals prior SLR (moment matching).

*Iteration 2* (linearize at $m=11/7$, $P=3/7$): $\mu_G=121/49+21/49=142/49$; $C=2\cdot\tfrac{11}7\cdot\tfrac37=66/49$; $\mathrm{Var}=18/49+1452/343=1578/343$, so $S_G=1921/343$. Then $A=\tfrac{66/49}{3/7}=22/7\approx3.143$, $b=142/49-242/49=-100/49\approx-2.041$, $\Lambda=1921/343-1452/343=67/49\approx1.367$. Update of the *prior* $\mathrm N(1,1)$: $\mu=22/7-100/49=54/49$, $S=484/49+67/49=551/49$, $K=\tfrac{22/7}{551/49}=154/551\approx0.280$, $m^{(2)}=1+K(4-54/49)\approx1.810$, $P^{(2)}=1-K\cdot A\approx0.122$.

The slope grows from 2 to 3.14 as the linearization point moves toward the data-supported region, and the mean moves from 1.57 to 1.81. Both illustrate the IPL loop.

## Concepts
- [[linearization]] — here: any affine map plus additive Gaussian noise approximating the model; the choice of linearization distribution matters (p. 204)
- [[statistical-linear-regression]] (new) — affine fit $\mathbf A\mathbf x+\mathbf b+\tilde{\mathbf e}$ minimizing mean squared error under a distribution of $\mathbf x$ (p. 205)
- [[generalized-slr]] (new) — SLR with an arbitrary linearization distribution $\pi(\mathbf x)$; no longer moment matching (pp. 205–206)
- [[posterior-linearization]] (new) — GSLR with $\pi=p(\mathbf x\mid\mathbf y)$ (p. 207)
- [[iterated-posterior-linearization]] (new) — loop that linearizes at the latest posterior approximation, then updates the prior (p. 209)
- [[iterated-posterior-linearization-filter]] (new) — Gaussian filter with standard prediction and an IPL measurement update (p. 212)
- [[kalman-filter]] — the update (10.7)/(10.15) is applied to the linearized model (p. 207)
- [[kalman-gain]] — $\mathbf K=\mathbf P\mathbf A^{\mathsf T}\mathbf S^{-1}$ (p. 207)
- [[iterated-extended-kalman-filter]] (new) — Taylor-based relative; linearizes at the iterated posterior point (pp. 213–214, 227)
- [[kl-divergence-optimality-of-slr]] (new) — SLR minimizes expected KL between true and linearized conditional model (p. 226)

## Canonical instances
- [[cubic-measurement-example]] — $y=x^3+q$, prior vs posterior SLR and IPL convergence (pp. 208, 210)
- [[pendulum-tracking]] — IPLF RMSE 0.14 vs EKF/IEKF 0.17 (pp. 219–220)
- [[coordinated-turn-model]] — IPLF helps only at start-up (p. 220)

## Bridges (candidates)
- [structural-analogy] IPL with Taylor integrals ↔ optimization: Gauss–Newton iteration — the text says Taylor-based IPL gives Gauss–Newton (p. 211).
- [structural-analogy] IPLF measurement update ↔ control-theory observer: model corrected by measurement via gain $\mathbf K$ — a linear Kalman correction is run on a re-linearized model.
- [structural-analogy] Linearize-at-the-estimate loop ↔ gain scheduling/extended observers in nonlinear control: the linearization point is itself estimated.

## Questions this raises
- Does IPL converge, and to what? The text says only "at convergence" and notes stochastic inner loops in Monte Carlo (p. 223).
- When is the extra cost of iteration worth it, given the modest gains in Examples 10.13–10.14?
- How does PL change smoothing (Chapter 14, p. 227)?
- Why is plugging non-Gaussian $p(\mathbf y\mid\mathbf x)$ into the KL criterion the wrong generalization (p. 226)?

## Exercises worth doing
- Ex. 10.1 (p. 227) — GSLR reduces to moment matching only when $\pi$ is the true distribution — easy
- Ex. 10.2 (pp. 227–228) — prior vs posterior linearization of $y=x^3+r$ with Riemann sums; compare posteriors — medium
- Ex. 10.3 (p. 228) — run IPL on the Ex. 10.2 model and watch convergence — medium
- Ex. 10.4 (p. 228) — IPL with spherical cubature rule — medium
- Ex. 10.7 (p. 228) — SLR minimizes the KL-based criterion (10.52) — hard

## Reading notes
- Printed page = pdf − 30 (pdf 234 = printed 204).
- Text layer lost many symbols; all math was read from the page images.
- Eq. (10.6) as printed gives the $\mathbf y$-block as $\mathbf A\mathbf P\mathbf A^{\mathsf T}+\mathbf Q$, whereas $\boldsymbol\Lambda$ of (10.4) includes $\mathbf Q$ via $\mathbf S_G$. This may be a misprint; $\mathbf A\mathbf P\mathbf A^{\mathsf T}+\boldsymbol\Lambda$ would be the consistent form (my inference).
- In (10.17) the images show $\mathbf h(\mathbf x_k,\mathbf q_k)$ inside $\mathbf P^{xy}$ and $\boldsymbol\mu_k^+$ without index $(i-1)$ in $\mathbf P^y$; these look like typos for $\mathbf r_k$ and $(i-1)$.
- In (10.39) and (10.45) the index $i$ appears as the summation variable in the $\mathbf P^y$ line ($\sum_{i=1}$), apparently meaning $j$.
- Figures 10.1–10.4 were read only roughly; numeric values come from captions and text.
- The pages carry a pre-publication notice (Cambridge University Press, 2nd edition, © 2023).
