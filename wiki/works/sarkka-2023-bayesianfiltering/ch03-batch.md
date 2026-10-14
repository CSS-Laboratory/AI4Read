---
id: sarkka-2023-bayesianfiltering/ch03-batch
work: sarkka-2023-bayesianfiltering
unit: "3 Batch and Recursive Bayesian Estimation"
pages: 27-43
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Batch and Recursive Bayesian Estimation

## L0 — One line
Treating each posterior as the next prior gives recursive Bayesian estimation, which matches the batch answer and, once a dynamic model is added, leads to the Kalman filter.

## L1 — The gist (≤ 120 words)
The chapter asks how a batch Bayesian estimate relates to one computed measurement by measurement. For linear regression with Gaussian noise, the recursive update gives exactly the batch posterior. Letting the parameters drift as a Gaussian random walk adds a prediction step. The result is a special case of the Kalman filter (a recursive solution for linear Gaussian state models). A state-space rewrite then removes the explicit time covariate. The chapter also names smoothing (using later data) and prediction (iterating the prediction step), and it shows that static Bayesian models are special cases of the general dynamic model. Why it matters: it introduces the Kalman filter, smoothing and prediction in a simple regression setting, before the full theory (for smoothing, Chapter 12, p. 39).

**Prerequisites:** Bayes' rule; Gaussian densities and completing the square; matrix products and inverses; marginalization (integrating out a variable).

## L2 — Key ideas (5–10 bullets)
- With Gaussian prior and likelihood, the batch regression posterior is Gaussian with closed-form mean and covariance (p. 29).
- Using the previous posterior as the prior gives a recursive update that ends in exactly the batch posterior. Reordering the measurements does not change it (pp. 30, 33).
- The scalar-measurement recursive update $(S_k, K_k, m_k, P_k)$ is a special case of the Kalman filter update. It needs no matrix inversion (pp. 30–31).
- A Gaussian random walk on the parameters adds a prediction step (Chapman–Kolmogorov integral) that inflates the covariance by $\mathbf Q$ (p. 34).
- State-space notation uses $\mathbf x$ for the unknown state, not for a regressor. A locally linear model removes the explicit time covariate (pp. 35–37).
- The Kalman filter is stated as prediction plus update. Smoothing conditions on future data too, and prediction iterates the prediction step (pp. 37–39).
- The general model $\mathbf x_k\sim p(\mathbf x_k\mid\mathbf x_{k-1})$, $\mathbf y_k\sim p(\mathbf y_k\mid\mathbf x_k)$ contains static Bayesian models as a special case. Markovianity (the next state depends on the past only through the current state) is less restrictive than it sounds (pp. 39–41).

## L3 — Walkthrough

### Intro and 3.1 Batch linear regression (pp. 27–29)
The chapter solves a familiar regression recursively. It then adds a dynamic model to contrast dynamic and batch estimation (p. 27).

Model: $y_k=\theta_1+\theta_2 t_k+\varepsilon_k$ with $\varepsilon_k\sim N(0,\sigma^2)$ (3.1). The prior on $\boldsymbol\theta=(\theta_1\ \theta_2)^T$ is $N(\mathbf m_0,\mathbf P_0)$ (p. 27). In probabilistic form:
$$p(y_k\mid\boldsymbol\theta)=N(y_k\mid \mathbf H_k\boldsymbol\theta,\sigma^2),\qquad p(\boldsymbol\theta)=N(\boldsymbol\theta\mid\mathbf m_0,\mathbf P_0)\tag{3.2}$$
with row vector $\mathbf H_k=(1\ \ t_k)$. It is written as a matrix because it is generally a matrix for vector measurements (p. 27). The regressors $t_k$ are known, so the dependence on them is left implicit. The posterior is written conditional on $y_{1:T}$, so that the notation also works where there are no natural regressors (p. 28).

Batch solution by Bayes' rule (p. 28):
$$p(\boldsymbol\theta\mid y_{1:T})\propto p(\boldsymbol\theta)\prod_{k=1}^T p(y_k\mid\boldsymbol\theta)=N(\boldsymbol\theta\mid\mathbf m_0,\mathbf P_0)\prod_{k=1}^T N(y_k\mid\mathbf H_k\boldsymbol\theta,\sigma^2).$$
Prior and likelihood are Gaussian, so the posterior is Gaussian: $p(\boldsymbol\theta\mid y_{1:T})=N(\boldsymbol\theta\mid\mathbf m_T,\mathbf P_T)$ (3.3). Completing the quadratic form in the exponent gives (p. 29)
$$\mathbf m_T=\Big[\mathbf P_0^{-1}+\tfrac1{\sigma^2}\mathbf H^T\mathbf H\Big]^{-1}\Big[\tfrac1{\sigma^2}\mathbf H^T\mathbf y+\mathbf P_0^{-1}\mathbf m_0\Big],\quad \mathbf P_T=\Big[\mathbf P_0^{-1}+\tfrac1{\sigma^2}\mathbf H^T\mathbf H\Big]^{-1}\tag{3.4}$$
with $\mathbf H=(\mathbf H_1;\dots;\mathbf H_T)$ the $T\times2$ matrix with rows $(1\ t_k)$, and $\mathbf y=(y_1,\dots,y_T)^T$ of size $T\times1$ (3.5). Shapes: $\mathbf m_T$ is $2\times1$, $\mathbf P_T$ is $2\times2$. Figure 3.2 plots the posterior-mean line, using a slight regularization prior and known variance (p. 29).

*Intuition note:* The prior acts like extra data. Precision (inverse covariance) adds: prior precision plus data precision $\mathbf H^T\mathbf H/\sigma^2$.

### 3.2 Recursive linear regression (pp. 30–31)
Suppose $p(\boldsymbol\theta\mid y_{1:k-1})=N(\mathbf m_{k-1},\mathbf P_{k-1})$ is known and a new $y_k$ arrives with likelihood $N(y_k\mid\mathbf H_k\boldsymbol\theta,\sigma^2)$. Use the previous posterior as the prior (p. 30):
$$p(\boldsymbol\theta\mid y_{1:k})\propto p(y_k\mid\boldsymbol\theta)\,p(\boldsymbol\theta\mid y_{1:k-1})\propto N(\boldsymbol\theta\mid\mathbf m_k,\mathbf P_k)\tag{3.6}$$
$$\mathbf m_k=\Big[\mathbf P_{k-1}^{-1}+\tfrac1{\sigma^2}\mathbf H_k^T\mathbf H_k\Big]^{-1}\Big[\tfrac1{\sigma^2}\mathbf H_k^T y_k+\mathbf P_{k-1}^{-1}\mathbf m_{k-1}\Big],\quad \mathbf P_k=\Big[\mathbf P_{k-1}^{-1}+\tfrac1{\sigma^2}\mathbf H_k^T\mathbf H_k\Big]^{-1}\tag{3.7}$$
The matrix inversion lemma (Corollary A.5) gives $\mathbf P_k=\mathbf P_{k-1}-\mathbf P_{k-1}\mathbf H_k^T[\mathbf H_k\mathbf P_{k-1}\mathbf H_k^T+\sigma^2]^{-1}\mathbf H_k\mathbf P_{k-1}$. With temporary variables:
$$\begin{aligned}S_k&=\mathbf H_k\mathbf P_{k-1}\mathbf H_k^T+\sigma^2,\\ \mathbf K_k&=\mathbf P_{k-1}\mathbf H_k^T S_k^{-1},\\ \mathbf m_k&=\mathbf m_{k-1}+\mathbf K_k[y_k-\mathbf H_k\mathbf m_{k-1}],\\ \mathbf P_k&=\mathbf P_{k-1}-\mathbf K_k S_k\mathbf K_k^T.\end{aligned}\tag{3.8}$$
Shapes: $S_k$ is a scalar, so no matrix inversion is needed. $\mathbf K_k$ is $2\times1$. (p. 30)

These are special cases of the Kalman filter update equations. Only the update part is needed, because the parameters are assumed constant (no stochastic dynamics model) (pp. 30–31). Figures 3.3 and 3.4 show the means and variances converging. The final values equal the batch ones. The variances decrease monotonically (pp. 31–32).

*Intuition note:* The gain $\mathbf K_k$ weights the surprise $y_k-\mathbf H_k\mathbf m_{k-1}$ by how uncertain the current estimate is relative to the measurement noise.

### 3.3 Batch versus recursive estimation (pp. 31–33)
Batch Bayesian solution (pp. 31–32):
1. Specify the likelihood $p(\mathbf y_k\mid\boldsymbol\theta)$. Typically the measurements are conditionally independent: $p(\mathbf y_{1:T}\mid\boldsymbol\theta)=\prod_k p(\mathbf y_k\mid\boldsymbol\theta)$.
2. Encode prior information in $p(\boldsymbol\theta)$.
3. The data are $\mathcal D=\{(t_1,\mathbf y_1),\dots\}$, or $\mathbf y_{1:T}$ if the explicit conditioning on $t_k$ is dropped.
4. Apply Bayes' rule: $p(\boldsymbol\theta\mid\mathbf y_{1:T})=\frac1Z p(\boldsymbol\theta)\prod_k p(\mathbf y_k\mid\boldsymbol\theta)$, with normalization constant $Z=\int p(\boldsymbol\theta)\prod_k p(\mathbf y_k\mid\boldsymbol\theta)\,d\boldsymbol\theta$.

Recursive solution (p. 33): the likelihood and conditional independence are as before. At step 0 the prior is all the information. Measurements arrive one at a time, and each step uses the previous posterior as prior:
$$p(\boldsymbol\theta\mid\mathbf y_{1:k})=\tfrac1{Z_k}\,p(\mathbf y_k\mid\boldsymbol\theta)\,p(\boldsymbol\theta\mid\mathbf y_{1:k-1}),\quad k=1,\dots,T.$$
The authors state that it is easy to show the final posterior equals the batch posterior, and that reordering the measurements does not change it. They do not give the proof here (p. 33).

Listed properties of the recursive form (p. 33):
- It is on-line learning.
- Batch inference is a special case of recursive inference.
- Because estimation is sequential, one can model what happens to $\boldsymbol\theta$ between measurements. This is the basis of filtering theory, where $\boldsymbol\theta(t)$ is a stochastic process.

### 3.4 Drift model for linear regression (pp. 34–36)
Let the parameters follow a Gaussian random walk:
$$p(y_k\mid\boldsymbol\theta_k)=N(y_k\mid\mathbf H_k\boldsymbol\theta_k,\sigma^2),\ \ p(\boldsymbol\theta_k\mid\boldsymbol\theta_{k-1})=N(\boldsymbol\theta_k\mid\boldsymbol\theta_{k-1},\mathbf Q),\ \ p(\boldsymbol\theta_0)=N(\mathbf m_0,\mathbf P_0)\tag{3.9}$$
Given $p(\boldsymbol\theta_{k-1}\mid y_{1:k-1})=N(\mathbf m_{k-1},\mathbf P_{k-1})$, the joint is $p(\boldsymbol\theta_k,\boldsymbol\theta_{k-1}\mid y_{1:k-1})=p(\boldsymbol\theta_k\mid\boldsymbol\theta_{k-1})p(\boldsymbol\theta_{k-1}\mid y_{1:k-1})$. Footnote: this is correct only for Markovian models, where $p(\boldsymbol\theta_k\mid\boldsymbol\theta_{k-1},y_{1:k-1})=p(\boldsymbol\theta_k\mid\boldsymbol\theta_{k-1})$ (p. 34). Marginalizing gives the Chapman–Kolmogorov equation:
$$p(\boldsymbol\theta_k\mid y_{1:k-1})=\int p(\boldsymbol\theta_k\mid\boldsymbol\theta_{k-1})\,p(\boldsymbol\theta_{k-1}\mid y_{1:k-1})\,d\boldsymbol\theta_{k-1}.$$
Both factors are Gaussian, so the result is $N(\mathbf m_k^-,\mathbf P_k^-)$ with $\mathbf m_k^-=\mathbf m_{k-1}$ and $\mathbf P_k^-=\mathbf P_{k-1}+\mathbf Q$ (p. 34). Using this as the prior gives (3.8) with $\mathbf m_{k-1},\mathbf P_{k-1}$ replaced by $\mathbf m_k^-,\mathbf P_k^-$ (p. 35):
$$S_k=\mathbf H_k\mathbf P_k^-\mathbf H_k^T+\sigma^2,\ \ \mathbf K_k=\mathbf P_k^-\mathbf H_k^TS_k^{-1},\ \ \mathbf m_k=\mathbf m_k^-+\mathbf K_k[y_k-\mathbf H_k\mathbf m_k^-],\ \ \mathbf P_k=\mathbf P_k^--\mathbf K_kS_k\mathbf K_k^T\tag{3.10}$$
This is again a special case of the Kalman filter. Figure 3.5 tracks a sine signal with a small diagonal drift model (p. 35).

*Intuition note:* Adding $\mathbf Q$ before each update stops the covariance from shrinking to zero. The estimate can keep following a changing signal.

**Notation switch** (pp. 35–36): in state-space notation $\mathbf x$ is the unknown state, that is, the vector of unknown parameters. It is not the regressor or covariate. Model (3.9) becomes
$$p(y_k\mid\mathbf x_k)=N(y_k\mid\mathbf H_k\mathbf x_k,\sigma^2),\ p(\mathbf x_k\mid\mathbf x_{k-1})=N(\mathbf x_k\mid\mathbf x_{k-1},\mathbf Q),\ p(\mathbf x_0)=N(\mathbf m_0,\mathbf P_0)\tag{3.11}$$
From now on, $\boldsymbol\theta$ denotes the static parameters of the state-space model. The authors note that parameters can always be augmented into the state, but it is useful to treat them separately (p. 36).

### 3.5 State space model for linear regression with drift (pp. 36–39)
Problem with (3.9): $t_k$ grows without bound as measurements accumulate, so conditioning gets worse. A time-invariant model, depending only on relative times, is also desirable (p. 36). With $\Delta t_{k-1}=t_k-t_{k-1}$, an exactly linear signal satisfies
$$x_k-x_{k-1}=\dot x\,\Delta t_{k-1}\tag{3.12}$$
Deviations from linearity are modelled by noise on the right-hand side. The derivative can also be assumed to do a small random walk and so not be exactly constant (p. 36):
$$x_{1,k}=x_{1,k-1}+\Delta t_{k-1}x_{2,k-1}+q_{1,k-1},\quad x_{2,k}=x_{2,k-1}+q_{2,k-1},\quad y_k=x_{1,k}+r_k\tag{3.13}$$
Here $x_{1,k}$ is the signal and $x_{2,k}$ is its derivative. The noises are $r_k\sim N(0,\sigma^2)$ and $(q_{1,k-1},q_{2,k-1})\sim N(\mathbf 0,\mathbf Q)$ (p. 37). Equivalently
$$p(y_k\mid\mathbf x_k)=N(y_k\mid\mathbf Hx_k,\sigma^2),\ \ p(\mathbf x_k\mid\mathbf x_{k-1})=N(\mathbf x_k\mid\mathbf A_{k-1}\mathbf x_{k-1},\mathbf Q),\tag{3.14}$$
$$\mathbf A_{k-1}=\begin{pmatrix}1&\Delta t_{k-1}\\0&1\end{pmatrix},\ \ \mathbf H=(1\ \ 0).$$
Here $\mathbf A$ is $2\times2$ and $\mathbf H$ is $1\times2$. With a suitable $\mathbf Q$ this is equivalent to (3.9). It estimates the signal itself (a point on the line) rather than the regression parameters (p. 37).

**Kalman filter** for generic linear-Gaussian models $p(\mathbf y_k\mid\mathbf x_k)=N(\mathbf H_k\mathbf x_k,\mathbf R_k)$ and $p(\mathbf x_k\mid\mathbf x_{k-1})=N(\mathbf A_{k-1}\mathbf x_{k-1},\mathbf Q_{k-1})$ (p. 37):
- Prediction: $\mathbf m_k^-=\mathbf A_{k-1}\mathbf m_{k-1}$, $\ \mathbf P_k^-=\mathbf A_{k-1}\mathbf P_{k-1}\mathbf A_{k-1}^T+\mathbf Q_{k-1}$.
- Update: $\mathbf S_k=\mathbf H_k\mathbf P_k^-\mathbf H_k^T+\mathbf R_k$, $\ \mathbf K_k=\mathbf P_k^-\mathbf H_k^T\mathbf S_k^{-1}$, $\ \mathbf m_k=\mathbf m_k^-+\mathbf K_k[\mathbf y_k-\mathbf H_k\mathbf m_k^-]$, $\ \mathbf P_k=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^T$.

All mean and covariance equations in the book so far are special cases of these, including the one-step batch solution for scalar measurements (p. 38). Figure 3.6 shows the sine tracked with this filter. It differs slightly from Figure 3.5 because of a different process-noise choice (p. 38).

Filter estimates $p(\mathbf x_k\mid\mathbf y_{1:k})=N(\mathbf m_k,\mathbf P_k)$ are non-anticipative: they use only measurements up to step $k$. Estimates of $\mathbf x_{k-1},\mathbf x_{k-2},\dots$ that also use later measurements are called **Bayesian smoothing**. They can be expected to be more accurate, since more information is used (p. 38). For linear-Gaussian models the solution is the Rauch–Tung–Striebel (RTS) smoother (full theory in Chapter 12). Figure 3.7 shows it is smoother and more accurate than the filter (p. 39). **Optimal prediction** of unmeasured future states can always be done by iterating the filter's prediction step, so no special algorithm is needed. In Figure 3.8 the prediction is a straight line, as the model states (pp. 39–40).

### 3.6 Toward Bayesian filtering and smoothing (pp. 39–41)
All models so far are special cases of
$$\text{dynamics: }\mathbf x_k\sim p(\mathbf x_k\mid\mathbf x_{k-1}),\qquad\text{measurements: }\mathbf y_k\sim p(\mathbf y_k\mid\mathbf x_k)\tag{3.15}$$
Replacing Gaussians and linear functions with non-Gaussian and non-linear ones gives non-linear filtering, and the book's theory applies to such models (p. 40). Dropping time dependence from the state gives
$$\mathbf x\sim p(\mathbf x),\qquad \mathbf y_k\sim p(\mathbf y_k\mid\mathbf x)\tag{3.16}$$
which is a general static Bayesian model, with $\mathbf x$ the vector of all unknown (hyper-)parameters. So all static Bayesian models are special cases, and dynamic estimation adds a Markov model for how the parameters change in time (p. 40). Markovianity is less restrictive than it sounds. The process is vector-valued, and Markov processes of any order can be turned into first-order vector-valued ones, as with differential equations (p. 41).

*Intuition note:* Recursive Bayesian inference does the same job as batch inference. Its advantage is that it can model the state changing between measurements.

## Toy example (ours, not from the text)
Scalar parameter, $H_k=1$, $\sigma^2=1$, prior $N(0,1)$, data $y_1=2$, $y_2=1$.
- Step 1: $S_1=1\cdot1\cdot1+1=2$; $K_1=1/2$; $m_1=0+\tfrac12(2-0)=1$; $P_1=1-\tfrac12\cdot2\cdot\tfrac12=0.5$.
- Step 2: $S_2=0.5+1=1.5$; $K_2=0.5/1.5=1/3$; $m_2=1+\tfrac13(1-1)=1$; $P_2=0.5-\tfrac13\cdot1.5\cdot\tfrac13=0.5-\tfrac16=\tfrac13$.
- Batch check: $\mathbf H=(1,1)^T$, so $\mathbf H^T\mathbf H=2$, $P_T=[1+2]^{-1}=1/3$, $m_T=\tfrac13[(1\cdot2+1\cdot1)+0]=1$. ✓
- Reversed order ($y=1$ first, then $y=2$): $m_1=0.5$, $P_1=0.5$; then $S=1.5$, $K=1/3$, $m_2=0.5+\tfrac13(1.5)=1$, $P_2=1/3$. Same result. ✓
- With a random walk, $Q=0.5$, applied before step 2: $P_2^-=0.5+0.5=1$, $S_2=2$, $K_2=0.5$, $m_2=1+0.5(1-1)=1$, $P_2=1-0.5\cdot2\cdot0.5=0.5$. The variance stays at 0.5 instead of falling to 1/3.

## Concepts
- [[batch-bayesian-estimation]] (new) — apply Bayes' rule once to all data: prior times product of likelihoods, normalized (p. 32)
- [[recursive-bayesian-estimation]] (new) — each step's posterior becomes the next prior. The final posterior equals the batch one (p. 33)
- [[kalman-filter]] — recursive posterior mean and covariance for linear-Gaussian models, as prediction then update (p. 37)
- [[kalman-gain]] — $\mathbf K_k=\mathbf P_k^-\mathbf H_k^T\mathbf S_k^{-1}$, the weight on the prediction error $y_k-\mathbf H_k\mathbf m_k^-$ (p. 35; same form with $\mathbf m_{k-1},\mathbf P_{k-1}$ on p. 30)
- [[state-space-model]] — dynamics $p(\mathbf x_k\mid\mathbf x_{k-1})$ plus measurement $p(\mathbf y_k\mid\mathbf x_k)$ (p. 39)
- [[state]] — here the vector of unknown parameters of the system, not the regressor (p. 35)
- [[bayesian-smoothing]] (new) — estimating a state using past and future measurements; RTS smoother in the linear-Gaussian case (p. 38)
- [[optimal-prediction]] (new) — forecasting unmeasured states by iterating the filter's prediction step (p. 39)
- [[chapman-kolmogorov-equation]] (new) — predictive density by integrating the transition density against the previous posterior (p. 34)

## Canonical instances
- [[linear-regression-recursive]] — recursive Gaussian regression equals the batch solution (pp. 30–32)
- [[drift-regression-sine-tracking]] — tracking a sine with random-walk parameters (Fig. 3.5) and with a locally linear Kalman filter (Fig. 3.6) (pp. 35, 38)
- [[rts-smoother-example]] — sine tracked more accurately by smoothing than by filtering (p. 39)

## Bridges (candidates)
- [same-math] Recursive regression update (3.8) ↔ control-theory: Kalman filter update step — the text states these are special cases of the Kalman filter update, and that only the update part is needed because the parameters are assumed constant (pp. 30–31).
- [structural-analogy] Kalman correction $\mathbf m_k^-+\mathbf K_k[\,y_k-\mathbf H_k\mathbf m_k^-]$ ↔ control-theory: observer with output-error correction — a model run forward and corrected by the measurement residual.
- [structural-analogy] Prediction step $\mathbf P^-=\mathbf A\mathbf P\mathbf A^T+\mathbf Q$ ↔ control-theory: delay/disturbance makes uncertainty grow between measurements.
- [metaphor] On-line Bayesian learning ↔ control-theory: temporal-difference learning — both update beliefs from each new observation.

## Questions this raises
- How do the update equations change when the model is non-linear or non-Gaussian, where (3.15) still holds but Gaussian closed forms fail?
- How should $\mathbf Q$ be chosen, and what trade-off between tracking speed and noise does it set?
- How does the RTS smoother use future data, and when is it worth its extra cost?
- What does the footnote on Markovian models imply when the true dynamics have memory?

## Exercises worth doing
- Ex. 3.1 (p. 41) — convert the batch solution (3.4) into the form (3.8) with the matrix inversion lemma, and check numerically — difficulty: medium
- Ex. 3.2 (pp. 41–42) — prove by induction that the Kalman filter at step $T$ gives the batch posterior for a static regression model — difficulty: hard
- Ex. 3.3(a–b) (pp. 42–43) — derive the joint and marginal Gaussian for $\mathbf x,\mathbf y$ with $p(\mathbf y\mid\mathbf x)=N(\mathbf H\mathbf x,\mathbf R)$ — difficulty: medium
- Ex. 3.3(c) (p. 43) — derive the Gaussian conditioning formula via block inverses and Schur complement — difficulty: hard

## Reading notes
- Printed page = pdf − 30. Running header on each page marks this as the Cambridge pre-publication version (2023).
- The text layer drops many Greek symbols and the tilde and minus signs. I read all equations from the page images.
- Page 38 says "non-anticipative measurements"; the context shows "estimates" is meant.
- Exercise 3.2 refers to Exercise 2.4, which is outside this unit. The proof of batch = recursive posterior is only asserted ("easy to show", p. 33).
- Figure 3.4's caption states that the variances decrease monotonically. This is a statement about that example's plot.
