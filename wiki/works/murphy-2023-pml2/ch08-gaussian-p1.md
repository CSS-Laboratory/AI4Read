---
id: murphy-2023-pml2/ch08-gaussian-p1
work: murphy-2023-pml2
unit: "8 Gaussian filtering and smoothing (part 1/2): §8.1 to start of §8.3.2.3"
pages: 359-378
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Gaussian filtering and smoothing (part 1/2)

## L0 — One line
In state-space models, filtering and smoothing are recursions of predict, update and backward-correct steps. They are exact in closed form when everything is linear-Gaussian (Kalman filter and RTS smoother), and approximate after linearizing a nonlinear model (extended Kalman filter).

## L1 — The gist (≤ 120 words)
How can we infer hidden states $z_t$ from noisy observations $y_t$ in a sequence model? The Bayes filter computes $p(z_t|y_{1:t})$ recursively, and a backward pass computes $p(z_t|y_{1:T})$. These integrals are generally intractable. If the model is linear-Gaussian, belief states (posteriors over $z_t$) stay Gaussian, so the Kalman filter and the Rauch–Tung–Striebel (RTS) smoother give exact answers in $O(TN_z^3)$ time. An information-form version swaps means and covariances for natural parameters (precision and precision-weighted mean). For nonlinear dynamics, the extended Kalman filter (EKF) linearizes with a first-order Taylor expansion. It is simple but can be inaccurate. Smoothing reduces uncertainty relative to filtering; in the book's example it also lowers error (MSE 3.13 to 1.71).

**Prerequisites:** conditioning and marginalizing multivariate Gaussians; Bayes' rule; Jacobians and first-order Taylor expansion; matrix inversion lemma.

## L2 — Key ideas (5–10 bullets)
- Filtering gives $p(z_t|y_{1:t})$, smoothing gives $p(z_t|y_{1:T})$, and prediction looks $h$ steps ahead; fixed-lag smoothing trades accuracy for delay (pp. 359–361).
- The Bayes filter is a predict step (Chapman–Kolmogorov: push the old posterior through the dynamics) followed by an update step (Bayes' rule). Its normalizers give the data log-likelihood (pp. 361–362).
- Smoothing runs backwards from $T$. It takes the two-slice filtered joint (of $z_t,z_{t+1}$ given $y_{1:t}$), divides out $p(z_{t+1}|y_{1:t})$, multiplies in $p(z_{t+1}|y_{1:T})$ and marginalizes (pp. 362–363).
- For linear-Gaussian models, Kalman gain $K_t=\Sigma_{t|t-1}H_t^\top S_t^{-1}$ weighs prior against measurement, and the update is mean plus gain times innovation (observation minus predicted observation) (pp. 365–366).
- The derivation reduces to two generic functions, joint and conditioning, for linear-Gaussian systems (Alg. 8.1–8.2). The EKF reuses the conditioning function and replaces the joint function by a linearized version (Alg. 8.3) (pp. 368–369, 376–377).
- The RTS smoother needs only the filtered moments, not the observations. It is preferred to two-filter smoothing for stability and for nonlinear extension (pp. 370–372).
- Information form is the "dual" of moment form: marginals are hard and conditionals easy (p. 372), so its predict step (marginalization) is the involved one and its update step (conditioning) is a simple addition (pp. 373–375).
- The EKF linearizes $f$ and $h$ around the latest mean estimates. It works poorly with large prior covariance or when the function is highly nonlinear near the current mean. The iterated EKF re-linearizes at the posterior and can be read as a Gauss–Newton search for the MAP (most probable) state (pp. 375–378).

## L3 — Walkthrough

### 8.1 Introduction
**State-space model (SSM).** The joint is
$$p(y_{1:T},z_{1:T}|u_{1:T})=p(z_1|u_1)\prod_{t=2}^T p(z_t|z_{t-1},u_t)\prod_{t=1}^T p(y_t|z_t,u_t)\tag{8.1}$$
Here $z_t$ is hidden, $y_t$ is observed and $u_t$ is an optional input. The factors are the transition (dynamics) model, the observation model and the initial-state distribution (p. 359). Fig. 8.1 shows the chain graph (p. 360).

**8.1.1 Goals.** State estimation means posterior inference on hidden states. Example: an airplane in 2d, with $z_t\in\mathbb R^4$ (location and velocity) and $y_t\in\mathbb R^2$ (noisy location) (p. 359).
- *Filtering* computes the belief state $p(z_t|y_{1:t})$. The filtered path is less noisy than the raw data because it uses prior knowledge about how the data were generated (p. 359).
- *Smoothing* computes $p(z_t|y_{1:T})$ offline. In Fig. 8.2, trajectory MSE is 3.13 for filtering and 1.71 for smoothing, and the smoothed ellipses are smaller (pp. 359–360).
- The author's detective analogy: once the key clue is found, earlier confusing observations are easy to explain in hindsight (p. 360).
- Smoothing cannot run online. *Fixed-lag smoothing* computes $p(z_{t-\ell}|y_{1:t})$ with lag $\ell>0$. It beats filtering at the cost of a slight delay (p. 360; Fig. 8.3, p. 361).
- Prediction $h$ steps ahead (sums become integrals for continuous states):
$$p(y_{t+h}|y_{1:t})=\sum_{z_{t+h}}p(y_{t+h}|z_{t+h})p(z_{t+h}|y_{1:t})\tag{8.2}$$
$$p(z_{t+h}|y_{1:t})=\sum_{z_{t:t+h-1}}p(z_t|y_{1:t})p(z_{t+1}|z_t)\cdots p(z_{t+h}|z_{t+h-1})\tag{8.3}$$
(p. 361)

**8.1.2 Bayes filter.** It computes the belief state recursively from $p(z_{t-1}|y_{1:t-1})$, $y_t$ and the model, with constant computation per step (p. 361).
$$p(z_t|y_{1:t-1})=\int p(z_t|z_{t-1})p(z_{t-1}|y_{1:t-1})\,dz_{t-1}\tag{8.4}$$
This is the prediction step (Chapman–Kolmogorov). It turns the previous posterior into the current prior. The update step is Bayes' rule (p. 362):
$$p(z_t|y_{1:t})=\tfrac1{Z_t}p(y_t|z_t)p(z_t|y_{1:t-1}),\quad Z_t=\int p(y_t|z_t)p(z_t|y_{1:t-1})dz_t=p(y_t|y_{1:t-1})\tag{8.5, 8.6}$$
$$\log p(y_{1:T})=\sum_{t=1}^T\log p(y_t|y_{1:t-1})=\sum_{t=1}^T\log Z_t\tag{8.7}$$
with $p(y_1|y_0)=p(y_1)$. This is useful for the MLE of parameters (p. 362).

**8.1.3 Smoothing (FFBS).** First run the forward filtering pass, then go backwards from $t=T$ to $1$. By induction, assume $p(z_{t+1}|y_{1:T})$ is known (p. 362).
$$p(z_t,z_{t+1}|y_{1:T})=p(z_t|z_{t+1},y_{1:T})\,p(z_{t+1}|y_{1:T})\tag{8.8}$$
By the Markov property, $y_{t+1:T}$ drops out once $z_{t+1}$ is given:
$$p(z_t|z_{t+1},y_{1:T})=p(z_t|z_{t+1},y_{1:t})=\frac{p(z_t,z_{t+1}|y_{1:t})}{p(z_{t+1}|y_{1:t})}=\frac{p(z_{t+1}|z_t)p(z_t|y_{1:t})}{p(z_{t+1}|y_{1:t})}\tag{8.9–8.11}$$
$$p(z_t,z_{t+1}|y_{1:T})=\frac{p(z_{t+1}|z_t)p(z_t|y_{1:t})p(z_{t+1}|y_{1:T})}{p(z_{t+1}|y_{1:t})}\tag{8.12}$$
$$p(z_t|y_{1:T})=\int p(z_t,z_{t+1}|y_{1:t})\frac{p(z_{t+1}|y_{1:T})}{p(z_{t+1}|y_{1:t})}dz_{t+1}\tag{8.13, 8.14}$$
(pp. 362–363). Reading: take the two-slice filtered distribution, divide out the old $p(z_{t+1}|y_{1:t})$, multiply in the new $p(z_{t+1}|y_{1:T})$, then marginalize out $z_{t+1}$ (p. 363).

*Intuition note.* Filtering moves forward and never revisits a belief. Smoothing goes back and corrects each belief using what happened later. Only the "future" part of the correction is new information.

**8.1.4 Gaussian ansatz.** In general the integrals are intractable. Two exceptions are discrete states (HMM, forwards–backwards, §9.2) and linear-Gaussian SSMs (Kalman filter and smoother). For nonlinear or non-Gaussian models, a Gaussian can still represent an approximate belief state (p. 363). Most of the chapter assumes
$$z_t=f(z_{t-1},u_t)+\mathcal N(0,Q_t),\qquad y_t=h(z_t,u_t)+\mathcal N(0,R_t)\tag{8.15}$$
(p. 363).

### 8.2 Inference for linear-Gaussian SSMs
An LG-SSM (also called an LDS) has (p. 363)
$$p(z_t|z_{t-1},u_t)=\mathcal N(z_t|F_tz_{t-1}+B_tu_t+b_t,Q_t),\quad p(y_t|z_t,u_t)=\mathcal N(y_t|H_tz_t+D_tu_t+d_t,R_t)\tag{8.16, 8.17}$$
with $z_t\in\mathbb R^{N_z}$, $y_t\in\mathbb R^{N_y}$, $u_t\in\mathbb R^{N_u}$. Often $b_t=d_t=0$ and $B_t=D_t=0$, giving $p(z_t|z_{t-1})=\mathcal N(z_t|F_tz_{t-1},Q_t)$ and $p(y_t|z_t)=\mathcal N(y_t|H_tz_t,R_t)$ (8.18, 8.19) (p. 364). The whole joint is one big Gaussian of dimension $N_yN_zT$ (as printed). Its structure lets the Kalman filter and smoother be exact in $O(TN_z^3)$ time (p. 364).

**8.2.1 Examples.**
- *Tracking.* State $=$ 2d location and velocity; sampling period $\Delta$ (p. 364):
$$z_t=\begin{pmatrix}1&0&\Delta&0\\0&1&0&\Delta\\0&0&1&0\\0&0&0&1\end{pmatrix}z_{t-1}+q_t,\qquad y_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix}z_t+r_t\tag{8.20, 8.21}$$
with $q_t\sim\mathcal N(0,Q_t)$, $r_t\sim\mathcal N(0,R_t)$. Velocity is not observed but can be inferred from location changes (p. 364). Figs. 8.2(b,c) show the results (p. 365).
- *Recursive least squares.* Set the latent state to the regression weights, $z_t=w$. Use $p(y_t|z_t)=\mathcal N(y_t|x_t^\top z_t,\sigma^2)$ and $p(z_t|z_{t-1})=\mathcal N(z_t|z_{t-1},0\mathbf I)$. The Kalman filter then gives the exact online posterior (p. 365).
- Time-series forecasting is deferred to §29.12 (p. 365).

**8.2.2 Kalman filter (KF).** The belief state is $p(z_t|y_{1:t})=\mathcal N(z_t|\mu_{t|t},\Sigma_{t|t})$. It is the Gaussian analogue of the HMM filter (p. 365).

*Predict (time update):*
$$p(z_t|y_{1:t-1},u_{1:t})=\mathcal N(z_t|\mu_{t|t-1},\Sigma_{t|t-1}),\quad \mu_{t|t-1}=F_t\mu_{t-1|t-1}+B_tu_t+b_t,\quad \Sigma_{t|t-1}=F_t\Sigma_{t-1|t-1}F_t^\top+Q_t\tag{8.22–8.24}$$
(p. 365)

*Update (measurement update):*
$$\hat y_t=H_t\mu_{t|t-1}+D_tu_t+d_t\tag{8.26}$$
$$S_t=H_t\Sigma_{t|t-1}H_t^\top+R_t\tag{8.27}$$
$$K_t=\Sigma_{t|t-1}H_t^\top S_t^{-1}\tag{8.28}$$
$$\mu_{t|t}=\mu_{t|t-1}+K_t(y_t-\hat y_t)\tag{8.29}$$
$$\Sigma_{t|t}=\Sigma_{t|t-1}-K_tH_t\Sigma_{t|t-1}=\Sigma_{t|t-1}-K_tS_tK_t^\top\tag{8.30, 8.31}$$
(p. 366). (added step) Shapes follow from the dimensions above: $K_t$ and $C_t$ are $N_z\times N_y$, $S_t$ and $R_t$ are $N_y\times N_y$.
- $K_t$ is the Kalman gain. $e_t=y_t-\hat y_t$ is the residual (innovation). $S_t$ is the observation covariance. $C_t=\Sigma_{t|t-1}H_t^\top$ is the state–observation cross-covariance (p. 366).
- In practice, solve $K_tS_t=C_t$ rather than inverting $S_t$ (p. 366).
- If $H_t=I$ in the scalar case, $k_t=\Sigma_{t|t-1}/S_t$, which the author reads as an inverse signal-to-noise ratio. A strong prior and/or noisy sensors give small $|K_t|$, so little weight on the correction. A weak prior and/or precise sensors give large $|K_t|$. The covariance shrinks by a positive definite matrix that depends on how informative the measurement is (p. 366).
- By the matrix inversion lemma, $K_t=\Sigma_{t|t-1}H_t^\top(H_t\Sigma_{t|t-1}H_t^\top+R_t)^{-1}=(\Sigma_{t|t-1}^{-1}+H_t^\top R_t^{-1}H_t)^{-1}H_t^\top R_t^{-1}$ (8.32). This is useful if $R_t^{-1}$ is precomputed and $N_y\gg N_z$. Via (8.97), also $K_t=\Sigma_tH_t^\top R_t^{-1}$ (p. 366).

*Intuition note.* The filter corrects its forecast by a fraction of the surprise. In the scalar case with $H_t=I$, the fraction is how much of the total predicted variance in the measurement comes from the state rather than from sensor noise.

*Posterior predictive (8.2.2.3).* Marginalizing $z_t$ gives $p(y_t|y_{1:t-1})=\mathcal N(y_t|\hat y_t,S_t)$ (8.35) (pp. 366–367). So $\log p(y_{1:T})=\sum_t\log p(y_t|y_{1:t-1})=\sum_t\log Z_t$ (8.36). This sums how "surprised" the model is at each step (p. 367). Forecasting $K$ steps means forecasting in latent space and then "grounding" the final state into observations. This contrasts with an RNN, which must generate observations at every step (p. 367).

*Derivation (8.2.2.4),* using the linear-Gaussian rules of §2.3.2 (p. 367).
1. Predict: $p(z_{t-1},z_t|y_{1:t-1})=\mathcal N(z_t|F_tz_{t-1},Q_t)\mathcal N(z_{t-1}|\mu_{t-1|t-1},\Sigma_{t-1|t-1})=\mathcal N\big((z_{t-1};z_t)|\mu',\Sigma'\big)$ with
$$\mu'=\begin{pmatrix}\mu_{t-1|t-1}\\F_t\mu_{t-1|t-1}\end{pmatrix},\ \Sigma'=\begin{pmatrix}\Sigma_{t-1|t-1}&\Sigma_{t-1|t-1}F_t^\top\\F_t\Sigma_{t-1|t-1}&F_t\Sigma_{t-1|t-1}F_t^\top+Q_t\end{pmatrix}\tag{8.37–8.40}$$
Marginalizing $z_{t-1}$ gives (8.41), equal to (8.22–8.24) (p. 367).
2. Update: $p(z_t,y_t|y_{1:t-1})=\mathcal N(y_t|H_tz_t,R_t)\mathcal N(z_t|\mu_{t|t-1},\Sigma_{t|t-1})=\mathcal N\big((z_t;y_t)|\mu'',\Sigma''\big)$, with $\mu''=(\mu_{t|t-1};H_t\mu_{t|t-1})$. The covariance blocks are $\Sigma_{t|t-1}$, $\Sigma_{t|t-1}H_t^\top$, $H_t\Sigma_{t|t-1}$ and $H_t\Sigma_{t|t-1}H_t^\top+R_t$ (8.42–8.45). The lower-right block is printed with a stray $^{-1}$ (see Reading notes) (pp. 367–368).
3. Conditioning on $y_t$ (Eq. 2.78) gives $\mu_{t|t}=\mu_{t|t-1}+\Sigma_{t|t-1}H_t^\top(H_t\Sigma_{t|t-1}H_t^\top+R_t)^{-1}[y_t-H_t\mu_{t|t-1}]$ and $\Sigma_{t|t}=\Sigma_{t|t-1}-\Sigma_{t|t-1}H_t^\top(\cdot)^{-1}H_t\Sigma_{t|t-1}$. With $S_t$, $K_t$ as above these are (8.46–8.52) (p. 368).

*Abstract formulation (8.2.2.5).* Let $p(z)=\mathcal N(\breve\mu,\breve\Sigma)$ and $p(y|z)=\mathcal N(Az+b,\Omega)$. Then
$$p(z,y)=\mathcal N\left(\begin{pmatrix}\breve\mu\\ \bar\mu\end{pmatrix},\begin{pmatrix}\breve\Sigma&C\\C^\top&S\end{pmatrix}\right),\ \bar\mu=A\breve\mu+b,\ S=A\breve\Sigma A^\top+\Omega,\ C=\breve\Sigma A^\top\tag{8.53–8.55}$$
$$p(z|y)=\mathcal N\big(z|\breve\mu+K(y-\bar\mu),\ \breve\Sigma-KSK^\top\big),\quad K=CS^{-1}\tag{8.56}$$
Algorithm 8.1 packages these as `LinGaussJoint` (returns $\bar\mu,S,C$) and `GaussCondition` (returns $\hat\mu,\hat\Sigma$ and $\ell=\log\mathcal N(y|\bar\mu,S)$). Predict is `LinGaussJoint`$(\mu_{t-1|t-1},\Sigma_{t-1|t-1},F_t,B_tu_t+b_t,Q_t)$ (8.58). Update is `LinGaussJoint`$(\mu_{t|t-1},\Sigma_{t|t-1},H_t,D_tu_t+d_t,R_t)$ then `GaussCondition` (8.61, 8.63). Algorithm 8.2 loops over $t$ and returns the filtered moments and $\sum_t\ell_t$ (pp. 368–369).

*Numerical issues (8.2.2.6).* Alternatives are the information filter (updates $\Lambda_{t|t}=\Sigma_{t|t}^{-1}$ and $\eta_{t|t}=\Lambda_t\mu_{t|t}$), the square-root filter (works with the Cholesky or QR factor of $\Sigma_{t|t}$) and their combination, the SRIF. A QR-based approach avoiding matrix inversions is also cited (p. 370). *Continuous time (8.2.2.7):* the Kalman–Bucy filter (p. 370).

**8.2.3 Kalman (RTS) smoother.** Named after Rauch, Tung and Striebel. It is the linear-Gaussian analogue of HMM forwards-filtering backwards-smoothing. Conditioning on past and future data reduces uncertainty, as seen in Fig. 8.2(c) (p. 370).

*Algorithm (8.2.3.1):* $p(z_t|y_{1:T})=\mathcal N(z_t|\mu_{t|T},\Sigma_{t|T})$ with
$$\mu_{t+1|t}=F_t\mu_{t|t},\ \Sigma_{t+1|t}=F_t\Sigma_{t|t}F_t^\top+Q_{t+1},\ J_t=\Sigma_{t|t}F_t^\top\Sigma_{t+1|t}^{-1}\tag{8.65–8.67}$$
$$\mu_{t|T}=\mu_{t|t}+J_t(\mu_{t+1|T}-\mu_{t+1|t})\tag{8.68}$$
$$\Sigma_{t|T}=\Sigma_{t|t}+J_t(\Sigma_{t+1|T}-\Sigma_{t+1|t})J_t^\top\tag{8.69}$$
(p. 370)

*Derivation (8.2.3.2),* using §2.3.2 rules (pp. 370–371):
1. Filtered two-slice joint: $p(z_t,z_{t+1}|y_{1:t})=\mathcal N(z_{t+1}|F_tz_t,Q_{t+1})\mathcal N(z_t|\mu_{t|t},\Sigma_{t|t})=\mathcal N(\cdot|m_1,V_1)$, with $m_1=(\mu_{t|t};F_t\mu_{t|t})$. The blocks of $V_1$ are $\Sigma_{t|t}$, $\Sigma_{t|t}F_t^\top$, $F_t\Sigma_{t|t}$ and $F_t\Sigma_{t|t}F_t^\top+Q_{t+1}$ (8.70–8.72).
2. Markov property: $p(z_t|z_{t+1},y_{1:T})=p(z_t|z_{t+1},y_{1:t})$ (8.73). Conditioning the joint on $z_{t+1}$ gives $\mathcal N(z_t|m_2,V_2)$ with $m_2=\mu_{t|t}+J_t(z_{t+1}-\mu_{t+1|t})$ and $V_2=\Sigma_{t|t}-J_t\Sigma_{t+1|t}J_t^\top$ (8.74–8.79). $J_t=\Sigma_{t,t+1|t}\Sigma_{t+1|t}^{-1}$ is the backwards Kalman gain, with $\Sigma_{t,t+1|t}=\Sigma_{t|t}F_t^\top$ (8.80).
3. Joint given all data: $p(z_{t+1},z_t|y_{1:T})=\mathcal N(z_t|m_2(z_{t+1}),V_2)\mathcal N(z_{t+1}|\mu_{t+1|T},\Sigma_{t+1|T})=\mathcal N(\cdot|m_3,V_3)$, with
$$m_3=\begin{pmatrix}\mu_{t+1|T}\\ \mu_{t|t}+J_t(\mu_{t+1|T}-\mu_{t+1|t})\end{pmatrix},\ V_3=\begin{pmatrix}\Sigma_{t+1|T}&\Sigma_{t+1|T}J_t^\top\\J_t\Sigma_{t+1|T}&J_t\Sigma_{t+1|T}J_t^\top+V_2\end{pmatrix}\tag{8.81–8.84}$$
The $z_t$ marginal of this joint gives (8.68) and (8.69) (p. 371).

*Intuition note.* The smoothed mean at $t$ is the filtered mean plus a gain $J_t$ times how much the future-informed belief about $t+1$ differs from the forecast made at time $t$.

*Two-filter smoothing (8.2.3.3).* The backwards pass of RTS needs only the filtered moments, not $y_{1:T}$. In two-filter smoothing, one computes backwards messages $p(y_{t+1:T}|z_t)\propto\mathcal N(z_t|\mu^b_{t|t},\Sigma^b_{t|t})$. These are likelihoods, not posteriors, which can cause numerical problems. At $t=T$ one needs $\Sigma^b_T=\infty I$. Information form, or multiplying by artificial distributions, resolves this. The author states RTS is generally preferred: it is more stable and easier to generalize to the nonlinear case (p. 372).

*Complexity (8.2.3.4).* Per step $O(N_y^3+N_z^2+N_yN_z)$ as printed, over $T$ steps. A parallel prefix scan operator reduces the number of sequential steps to $O(\log T)$ on GPUs. Space can go from $O(T)$ to $O(\log T)$ using the §9.2.5 algorithm (p. 372).

*Forwards filtering backwards sampling (8.2.3.5).* To sample the posterior, use
$$p(z_t|z_{t+1},y_{1:T})=\mathcal N(z_t|\tilde\mu_t,\tilde\Sigma_t),\ \tilde\mu_t=\mu_{t|t}+J_t(z_{t+1}-F_t\mu_{t|t}),\ \tilde\Sigma_t=\Sigma_{t|t}-J_t\Sigma_{t+1|t}J_t^\top=\Sigma_{t|t}(I-F_t^\top J_t^\top)\tag{8.85–8.88}$$
(p. 372).

**8.2.4 Information form** (section written by Giles Harper-Donnelly). This is the "dual" of moment form. In moment form, marginals are easy and conditionals need a matrix inverse. In information form, marginals are hard and conditionals are easy (p. 372). Notation: $\mathcal N_c(z|\eta,\Lambda)$ with $\Lambda=\Sigma^{-1}$, $\eta=\Lambda\mu$ (p. 370).

*Filtering (8.2.4.1).* Predict, starting from $\mathcal N_c(z_{t-1}|\eta_{t-1|t-1},\Lambda_{t-1|t-1})$ (p. 373):
$$M_t=\Lambda_{t-1|t-1}+F_t^\top Q_t^{-1}F_t,\quad J_t=Q_t^{-1}F_tM_t^{-1}\tag{8.90, 8.91}$$
$$\Lambda_{t|t-1}=Q_t^{-1}-Q_t^{-1}F_tM_t^{-1}F_t^\top Q_t^{-1}=Q_t^{-1}-J_tF_t^\top Q_t^{-1}=Q_t^{-1}-J_tM_tJ_t^\top\tag{8.92–8.94}$$
$$\eta_{t|t-1}=J_t\eta_{t-1|t-1}+\Lambda_{t|t-1}(B_tu_t+b_t)\tag{8.95}$$
Equation (8.92) is the inverse of $\Sigma_{t|t-1}$ in (8.24), by the matrix inversion lemma. Update:
$$\Lambda_{t|t}=\Lambda_{t|t-1}+H_t^\top R_t^{-1}H_t,\quad \eta_{t|t}=\eta_{t|t-1}+H_t^\top R_t^{-1}(y_t-D_tu_t-d_t)\tag{8.97, 8.98}$$
(p. 373)

*Derivation (8.2.4.2).* Predict: the joint over $(z_{t-1},z_t)$ is $\mathcal N_c(\eta_{t-1,t|t-1},\Lambda_{t-1,t|t-1})$ with
$$\eta=\begin{pmatrix}\eta_{t-1|t-1}-F_t^\top Q_t^{-1}(B_tu_t+b_t)\\Q_t^{-1}(B_tu_t+b_t)\end{pmatrix},\ \Lambda=\begin{pmatrix}\Lambda_{t-1|t-1}+F_t^\top Q_t^{-1}F_t&-F_t^\top Q_t^{-1}\\-Q_t^{-1}F_t&Q_t^{-1}\end{pmatrix}\tag{8.103, 8.104}$$
Marginalizing gives (8.89–8.95). Update: the joint over $(z_t,y_t)$ has
$$\eta_{z,y|t}=\begin{pmatrix}\eta_{t|t-1}-H_t^\top R_t^{-1}(D_tu_t+d_t)\\R_t^{-1}(D_tu_t+d_t)\end{pmatrix},\ \Lambda_{z,y|t}=\begin{pmatrix}\Lambda_{t|t-1}+H_t^\top R_t^{-1}H_t&-H_t^\top R_t^{-1}\\-R_t^{-1}H_t&R_t^{-1}\end{pmatrix}\tag{8.108, 8.109}$$
Conditioning gives (8.97, 8.98) (pp. 373–374).

*Smoothing (8.2.4.3).* $p(z_t|y_{1:T})=\mathcal N_c(z_t|\eta_{t|T},\Lambda_{t|T})$ with
$$U_t=Q_t^{-1}+\Lambda_{t+1|T}-\Lambda_{t+1|t},\quad L_t=F_t^\top Q_t^{-1}U_t^{-1}\tag{8.111, 8.112}$$
$$\Lambda_{t|T}=\Lambda_{t|t}+F_t^\top Q_t^{-1}F_t-L_tU_tL_t^\top\tag{8.113, 8.114}$$
$$\eta_{t|T}=\eta_{t|t}+L_t(\eta_{t+1|T}-\eta_{t+1|t})\tag{8.115}$$
$L_t$ is the information-form analogue of the backwards gain. $\eta_{t|t},\Lambda_{t|t}$ are the filtered values and $\eta_{t+1|t},\Lambda_{t+1|t}$ the predicted ones (p. 374).

*Derivation (8.2.4.4).* Start from the generic smoothing equation (8.14) in $\mathcal N_c$ form (8.116–8.119). The two-slice predictive joint has
$$\eta_{t,t+1|t}=\begin{pmatrix}\eta_{t|t}\\0\end{pmatrix},\ \Lambda_{t,t+1|t}=\begin{pmatrix}\Lambda_{t|t}+F_{t+1}^\top Q_{t+1}^{-1}F_{t+1}&-F_{t+1}^\top Q_{t+1}^{-1}\\-Q_{t+1}^{-1}F_{t+1}&Q_{t+1}^{-1}\end{pmatrix}\tag{8.120}$$
Dividing by the old and multiplying by the new $z_{t+1}$ potential means subtracting and adding information (§2.3.3):
$$\eta_{t,t+1|T}=\eta_{t,t+1|t}+\begin{pmatrix}0\\ \eta_{t+1|T}\end{pmatrix}-\begin{pmatrix}0\\ \eta_{t+1|t}\end{pmatrix}=\begin{pmatrix}\eta_{t|t}\\ \eta_{t+1|T}-\eta_{t+1|t}\end{pmatrix}\tag{8.121}$$
$$\Lambda_{t,t+1|T}=\Lambda_{t,t+1|t}+\begin{pmatrix}0&0\\0&\Lambda_{t+1|T}\end{pmatrix}-\begin{pmatrix}0&0\\0&\Lambda_{t+1|t}\end{pmatrix}\tag{8.122}$$
which has lower-right block $Q_{t+1}^{-1}+\Lambda_{t+1|T}-\Lambda_{t+1|t}$ (8.123). Information-form marginalization (Eq. 2.85) then gives (8.115) and (8.113) (p. 375).

*Intuition note.* In information form, "multiply in new evidence, divide out old evidence" is just adding and subtracting precision terms. In the derivation the smoothing step is done exactly this way (8.121–8.123).

### 8.3 Inference based on local linearization
Idea: for nonlinear $f$ and/or $h$ with additive Gaussian noise, linearize around the previous state estimate with a first-order Taylor expansion, then apply the Kalman equations. This approximates a stationary nonlinear system by a non-stationary linear one. It is the extended Kalman filter (EKF) (p. 375).

**8.3.1 Taylor expansion.** If $x\sim\mathcal N(\mu,\Sigma)$ and $y=g(x)$ with $g$ differentiable and invertible, then $p(y)=|\det\mathrm{Jac}(g^{-1})(y)|\,\mathcal N(g^{-1}(y)|\mu,\Sigma)$ (8.124). This is generally intractable (p. 375). Write $x=\mu+\delta$, $\delta\sim\mathcal N(0,\Sigma)$. Then
$$g(\mu+\delta)\approx g(\mu)+G(\mu)\delta,\quad [G(\mu)]_{jj'}=\partial g_j/\partial x_{j'}|_{x=\mu}\tag{8.125, 8.126}$$
(p. 375). Moments (p. 376):
$$\mathbb E[y]\approx g(\mu)+G(\mu)\mathbb E[\delta]=g(\mu)\tag{8.127}$$
$$\mathrm{Cov}[y]\approx\mathbb E[(g(x)-g(\mu))(g(x)-g(\mu))^\top]\approx\mathbb E[(G\delta)(G\delta)^\top]=G\,\mathbb E[\delta\delta^\top]G^\top=G(\mu)\Sigma G(\mu)^\top\tag{8.128–8.133}$$
For $y=g(x)+q$ with $q\sim\mathcal N(0,\Omega)$ independent of $x$, apply this to $\tilde g(x)=[x,g(x)]$:
$$\begin{pmatrix}x\\y\end{pmatrix}\sim\mathcal N\left(\begin{pmatrix}\mu\\g(\mu)\end{pmatrix},\begin{pmatrix}\Sigma&\Sigma G^\top\\G\Sigma&G\Sigma G^\top+\Omega\end{pmatrix}\right)\tag{8.134, 8.135}$$
Algorithm 8.3 (`LinearizedGaussJoint`) returns $\hat y=g(\mu)$, $S=G\Sigma G^\top+\Omega$, $C=\Sigma G^\top$. Conditioning on $y$ gives the posterior. Non-additive noise is covered in [SS23, §7.1] (p. 376).

*Intuition note.* Replacing $g$ by its tangent line at the mean turns the problem back into the linear-Gaussian one, with the Jacobian $G$ playing the role of $A$.

**8.3.2 EKF.** Linearize $f$ around $\mu_{t-1|t-1}$ for prediction, then $h$ around $\mu_{t|t-1}$, then do a Gaussian update (p. 376):
$$(\mu_{t|t-1},\Sigma_{t|t-1},-)=\text{LinearizedGaussJoint}(\mu_{t-1|t-1},\Sigma_{t-1|t-1},f(\cdot,u_t),Q_t)\tag{8.136}$$
$$(\hat y_t,S_t,C_t)=\text{LinearizedGaussJoint}(\mu_{t|t-1},\Sigma_{t|t-1},h(\cdot,u_t),R_t)\tag{8.137}$$
$$(\mu_{t|t},\Sigma_{t|t},\ell_t)=\text{GaussCondition}(\mu_{t|t-1},\Sigma_{t|t-1},\hat y_t,S_t,C_t,y_t)\tag{8.138}$$
Explicitly: $\mu_{t|t-1}=f(\mu_{t-1},u_t)$, $\Sigma_{t|t-1}=F_t\Sigma_{t-1}F_t^\top+Q_t$ (8.139, 8.140). Update: $\hat y_t=h(\mu_{t|t-1},u_t)$, $S_t=H_t\Sigma_{t|t-1}H_t^\top+R_t$, $K_t=\Sigma_{t|t-1}H_t^\top S_t^{-1}$, $\mu_{t|t}=\mu_{t|t-1}+K_t(y_t-\hat y_t)$, $\Sigma_{t|t}=\Sigma_{t|t-1}-K_tH_t\Sigma_{t|t-1}=\Sigma_{t|t-1}-K_tS_tK_t^\top$ (8.141–8.145). Here $F_t$ is $N_z\times N_z$, $H_t$ is $N_y\times N_z$ and $K_t$ is $N_z\times N_y$ (p. 377).

*Accuracy (8.3.2.1).* The EKF is simple and relatively efficient. It works poorly in two cases (p. 377):
- When the prior covariance is large, because probability mass passes through parts of the function far from the linearization point.
- When the function is highly nonlinear near the current mean.

Improvements: the second-order EKF (still closed form), the iterated EKF, and the unscented KF (more accurate, no Jacobians; §8.4.2) (p. 377).

*Iterated EKF (8.3.2.2).* Repeatedly re-linearize the measurement model around the current posterior mean $\mu_{t|t}$ instead of $\mu_{t|t-1}$. In Algorithm 8.4, each of $J$ inner iterations calls `LinearizedGaussJoint` at $(\mu_{t|t},\Sigma_{t|t})$ and then `GaussCondition` using the original prior $(\mu_{t|t-1},\Sigma_{t|t-1})$. $J=1$ recovers the EKF (pp. 377–378). The IEKF can be read as Gauss–Newton for the per-step MAP estimate, minimizing
$$\mathcal L(z_t)=\tfrac12(y_t-h(z_t))^\top R_t^{-1}(y_t-h(z_t))+\tfrac12(z_t-\mu_{t|t-1})^\top\Sigma_{t|t-1}^{-1}(z_t-\mu_{t|t-1})\tag{8.146}$$
Gauss–Newton can sometimes diverge. Levenberg–Marquardt, line-search and quasi-Newton extensions are cited (p. 378).

*Intuition note.* Re-linearizing at a better estimate means the tangent line is taken closer to where the posterior actually lies. The source says only that this improves accuracy; the reason given here is our reading.

*8.3.2.3 Spiral example.* The section begins by motivating nonlinear tracking of an object on a curved trajectory. Fig. 8.4 compares EKF and UKF estimates. The text continues in the next part (p. 378).

## Toy example (ours, not from the text)
Scalar LG-SSM with $F=1$, $Q=1$, $H=1$, $R=2$, $\mu_{0|0}=0$, $\Sigma_{0|0}=1$; observations $y_1=3$, $y_2=1$.

*Filter, $t=1$.* Predict: $\mu_{1|0}=0$, $\Sigma_{1|0}=1\cdot1\cdot1+1=2$. Update: $\hat y=0$, $S=2+2=4$, $K=2/4=0.5$, $\mu_{1|1}=0+0.5(3-0)=1.5$, $\Sigma_{1|1}=2-0.5\cdot4\cdot0.5=1$. Check with (8.30): $2-0.5\cdot1\cdot2=1$. ✓. Log-likelihood term: $\log\mathcal N(3|0,4)=-\tfrac12\log(8\pi)-9/8\approx-1.612-1.125=-2.737$.

*Filter, $t=2$.* Predict: $\mu_{2|1}=1.5$, $\Sigma_{2|1}=1+1=2$. Update: $\hat y=1.5$, $S=4$, $K=0.5$, $\mu_{2|2}=1.5+0.5(1-1.5)=1.25$, $\Sigma_{2|2}=2-0.5\cdot4\cdot0.5=1$.

*Smoother, $t=1$ ($T=2$).* $J_1=\Sigma_{1|1}F/\Sigma_{2|1}=1/2=0.5$. $\mu_{1|2}=1.5+0.5(1.25-1.5)=1.375$. $\Sigma_{1|2}=1+0.5^2(1-2)=0.75$.

The smoothed variance $0.75$ is below the filtered variance $1$, and the mean moved toward the later, lower observation.

## Concepts
- [[state-space-model]] (new) — latent Markov chain $z_t$ with observations $y_t$ and optional inputs $u_t$ (p. 359)
- [[bayes-filter]] (new) — recursive predict (Chapman–Kolmogorov) plus update (Bayes) for $p(z_t|y_{1:t})$ (p. 361)
- [[sequential-updating]] — each posterior becomes the next step's prior; constant work per step (p. 361)
- [[marginal-likelihood]] — $\log p(y_{1:T})=\sum_t\log Z_t$ from filter normalizers (p. 362)
- [[smoothing-ffbs]] (new) — forward filter then backward pass for $p(z_t|y_{1:T})$; fixed-lag is a compromise (pp. 360, 362)
- [[kalman-filter]] (new) — exact Bayes filter for linear-Gaussian SSMs (p. 365)
- [[kalman-gain]] (new) — matrix weighting the innovation: $K_t=\Sigma_{t|t-1}H_t^\top S_t^{-1}$ (p. 366)
- [[rts-smoother]] (new) — Kalman smoother using the backwards gain $J_t$ (p. 370)
- [[information-form]] (new) — Gaussian filtering with precision $\Lambda$ and $\eta=\Lambda\mu$ (pp. 370, 372)
- [[extended-kalman-filter]] (new) — Kalman filter on a first-order Taylor linearization (p. 375)
- [[iterated-ekf]] (new) — EKF with repeated re-linearization at the posterior; Gauss–Newton MAP (pp. 377–378)

## Canonical instances
- [[tracking-2d-lgssm]] — constant-velocity 2d tracking; filter vs smoother MSE 3.13 vs 1.71 (pp. 359–360, 364)
- [[recursive-least-squares]] — Kalman filter with latent state = regression weights (p. 365)
- [[spiral-tracking-ekf-ukf]] — nonlinear 2d tracking, EKF vs UKF (Fig. 8.4; begins p. 378)

## Bridges (candidates)
- [same-math] Bayes filter predict/update ↔ bayesian: sequential updating — yesterday's posterior is prior, then multiply by the likelihood.
- [same-math] Kalman update (8.56) ↔ bayesian: conjugate Gaussian linear regression posterior — same conditioning formula.
- [structural-analogy] Kalman filter ↔ hmm-inference (§9.2 as cited): the Gaussian analogue of the HMM forward filter; RTS ↔ HMM forwards-backwards smoothing (pp. 365, 370).
- [structural-analogy] Iterated EKF ↔ optimization: Gauss–Newton for MAP, with the prior as a quadratic penalty (p. 378).
- [metaphor] Smoothing "hindsight" ↔ the detective's key clue (p. 360).

## Questions this raises
- When is the Gaussian belief approximation accurate for nonlinear models, and what do the UKF and other methods (later sections) do differently from linearization?
- How do filter normalizers $Z_t$ enable parameter learning (MLE or Bayesian) in SSMs?
- Why is the backward Kalman gain $J_t$ the same as the regression of $z_t$ on $z_{t+1}$ under the filtered joint?
- How badly does the EKF's covariance estimate fail under strong nonlinearity, in terms of overconfidence?

## Reading notes
- This part starts at §8.1 (printed p. 359; pdf 393) and ends partway through §8.3.2.3 (printed p. 378; pdf 412), where the spiral example's text is cut off. Printed = pdf − 34.
- Eq. 8.45: the image shows $H_t\Sigma_{t|t-1}^{-1}H_t^\top+R_t$ in the lower-right block of $\Sigma''$. The stray $^{-1}$ is a misprint, since (8.27) and (8.51) give $S_t=H_t\Sigma_{t|t-1}H_t^\top+R_t$.
- Eq. 8.58 lists the output $\Sigma_{t-1,t|t}$, while (8.57) uses $\Sigma_{t-1,t|t-1}$. The text after 8.20 writes velocity as $(\dot x_{t1},\dot x_{t1})$, with the second index presumably intended as 2.
- Footnote 4 (p. 364) says $G_t$ is "$N_y\times N_q$". Since $Q_t$ is $N_z\times N_z$, $N_z\times N_q$ looks intended.
- Under (8.139–8.140), $F_t\equiv\mathrm{Jac}(f(\cdot,u_t))(\mu_{t|t-1})$ is printed, while the surrounding text says linearization is around $\mu_{t-1|t-1}$. The two statements are inconsistent as printed.
- Eq. 8.113 prints "$L_tQ_t^{-1}F$" without the subscript on $F$. The symbol $J_t$ is used both for the backward Kalman gain (8.67) and for the information-form predict matrix (8.91). Complexity in §8.2.3.4 is quoted as printed.
- Algorithm 8.2's line 7 in the image calls `GaussCondition(..., µ̄, S, C, y)` with unsubscripted names. §8.2.4 is attributed to Giles Harper-Donnelly. Footer: online version, December 10, 2025.
