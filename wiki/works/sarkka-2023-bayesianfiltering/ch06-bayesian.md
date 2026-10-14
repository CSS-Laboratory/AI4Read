---
id: sarkka-2023-bayesianfiltering/ch06-bayesian
work: sarkka-2023-bayesianfiltering
unit: 6 Bayesian Filtering Equations and Exact Solutions
pages: 91-107
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
# Bayesian Filtering Equations and Exact Solutions

## L0 — One line
In a Markovian state space model, the filtering distribution follows from a predict step (Chapman–Kolmogorov) and an update step (Bayes' rule), and these steps are solvable in closed form for linear Gaussian models (the Kalman filter) and for discrete-state hidden Markov models (HMMs).

## L1 — The gist (≤ 120 words)
The question: how can we compute the distribution of a hidden state given all measurements so far, using a constant amount of work per time step? The answer is a two-step recursion. Prediction pushes the previous filtering distribution through the dynamic model. Update multiplies by the measurement likelihood and renormalizes. For general models the recursion is written as integral equations. For linear Gaussian models every distribution stays Gaussian, so only a mean and a covariance are tracked: this is the Kalman filter. For finite state spaces the integrals become sums, giving the HMM filter. This matters because real-time sensing needs bounded computation per step.

**Prerequisites:** Bayes' rule; conditional independence; multivariate Gaussians (joint, marginal, conditional); matrix multiplication and inverse; Markov chains.

## L2 — Key ideas
- A probabilistic state space model is a dynamic model $p(\mathbf x_k\mid\mathbf x_{k-1})$ plus a measurement model $p(\mathbf y_k\mid\mathbf x_k)$, with Markov and conditional-independence properties (p. 91–92).
- Computing the full posterior by Bayes' rule needs ever more computation as data arrive, so it is infeasible in real time. Filtering is done recursively instead (p. 93–94).
- The Bayesian filter is a prediction step (Chapman–Kolmogorov) followed by an update step (Bayes' rule with normalizer $Z_k$). It starts from the prior $p(\mathbf x_0)$ (p. 94).
- For linear Gaussian models the Bayesian filter has a closed-form solution, the Kalman filter, which tracks mean and covariance (p. 97).
- The proof builds joint Gaussian distributions (Lemma A.2), then uses marginalization (predict) and conditioning (update) (Lemma A.3) (p. 97–98).
- The affine Kalman filter adds known offsets $\mathbf a_{k-1}$, $\mathbf b_k$ and changes only the mean prediction and the residual (measurement minus predicted measurement) (p. 102–103).
- For a time-invariant model, as $k\to\infty$ the Kalman filter approaches a constant-gain stationary filter (p. 102).
- For discrete states, integrals become sums; for finite HMMs the filter is a matrix-vector prediction followed by a normalized elementwise update (p. 103–104).

## L3 — Walkthrough

### 6.1 Probabilistic state space models (pp. 91–94)
**Definition 6.1.** The model is $\mathbf x_k\sim p(\mathbf x_k\mid\mathbf x_{k-1})$, $\mathbf y_k\sim p(\mathbf y_k\mid\mathbf x_k)$ for $k=1,2,\dots$ (6.1). Here $\mathbf x_k\in\mathbb R^n$ is the state and $\mathbf y_k\in\mathbb R^m$ the measurement. The first density is the dynamic model and the second the measurement model. The dynamic model may be a density, a counting measure, or a mix, depending on whether the state is continuous, discrete or hybrid (p. 91).

**Property 6.2 (Markov property).** The states form a Markov sequence. The state $\mathbf x_k$ given $\mathbf x_{k-1}$ is independent of everything before $k-1$ (p. 92):
$$p(\mathbf x_k\mid\mathbf x_{0:k-1},\mathbf y_{1:k-1})=p(\mathbf x_k\mid\mathbf x_{k-1}).\tag{6.2}$$
The past is independent of the future given the present:
$$p(\mathbf x_{k-1}\mid\mathbf x_{k:T},\mathbf y_{k:T})=p(\mathbf x_{k-1}\mid\mathbf x_k).\tag{6.3}$$

**Property 6.3.** $\mathbf y_k$ given $\mathbf x_k$ is conditionally independent of the state and measurement histories (p. 92):
$$p(\mathbf y_k\mid\mathbf x_{0:k},\mathbf y_{1:k-1})=p(\mathbf y_k\mid\mathbf x_k).\tag{6.4}$$

**Example 6.4 (Gaussian random walk).** (p. 92)
$$x_k=x_{k-1}+q_{k-1},\ q_{k-1}\sim \mathrm N(0,Q);\qquad y_k=x_k+r_k,\ r_k\sim \mathrm N(0,R).\tag{6.5}$$
Equivalently $p(x_k\mid x_{k-1})=\mathrm N(x_k\mid x_{k-1},Q)=\frac1{\sqrt{2\pi Q}}\exp\!\big(-\frac1{2Q}(x_k-x_{k-1})^2\big)$ and $p(y_k\mid x_k)=\mathrm N(y_k\mid x_k,R)=\frac1{\sqrt{2\pi R}}\exp\!\big(-\frac1{2R}(y_k-x_k)^2\big)$ (6.6). Figure 6.1 shows a simulation with $Q=R=1$ over 100 steps (p. 93).

**Joint prior and likelihood** (p. 93):
$$p(\mathbf x_{0:T})=p(\mathbf x_0)\prod_{k=1}^T p(\mathbf x_k\mid\mathbf x_{k-1}),\tag{6.7}$$
$$p(\mathbf y_{1:T}\mid\mathbf x_{0:T})=\prod_{k=1}^T p(\mathbf y_k\mid\mathbf x_k).\tag{6.8}$$
The full posterior is
$$p(\mathbf x_{0:T}\mid\mathbf y_{1:T})=\frac{p(\mathbf y_{1:T}\mid\mathbf x_{0:T})p(\mathbf x_{0:T})}{p(\mathbf y_{1:T})}\propto p(\mathbf y_{1:T}\mid\mathbf x_{0:T})p(\mathbf x_{0:T}).\tag{6.9}$$
This is not feasible in real time. The computation per step grows as observations arrive, and with unbounded data it eventually becomes intractable. A real-time algorithm needs a constant number of computations per step (p. 93). Filtering, prediction and smoothing distributions can be computed recursively with constant work per step. This chapter and the next few treat filtering and prediction; smoothing comes later (p. 94).

*Intuition note:* The full posterior over all states keeps growing as data arrive. Filtering keeps only the distribution of the current state, which is enough to continue the recursion because of the Markov structure.

### 6.2 Bayesian filtering equations (pp. 94–96)
The aim is the filtering distribution $p(\mathbf x_k\mid\mathbf y_{1:k})$ (6.10) (p. 94).

**Theorem 6.5 (Bayesian filtering equations).** (p. 94)
- Initialization: start from the prior $p(\mathbf x_0)$.
- Prediction (Chapman–Kolmogorov):
$$p(\mathbf x_k\mid\mathbf y_{1:k-1})=\int p(\mathbf x_k\mid\mathbf x_{k-1})\,p(\mathbf x_{k-1}\mid\mathbf y_{1:k-1})\,d\mathbf x_{k-1}.\tag{6.11}$$
- Update (Bayes' rule):
$$p(\mathbf x_k\mid\mathbf y_{1:k})=\frac1{Z_k}p(\mathbf y_k\mid\mathbf x_k)p(\mathbf x_k\mid\mathbf y_{1:k-1}),\tag{6.12}$$
$$Z_k=\int p(\mathbf y_k\mid\mathbf x_k)p(\mathbf x_k\mid\mathbf y_{1:k-1})\,d\mathbf x_k.\tag{6.13}$$
For discrete state components the integrals become sums (p. 95). Figures 6.2 and 6.3 illustrate prediction (propagating the previous distribution through the dynamic model) and update (prior times likelihood gives posterior) (p. 95).

**Proof.** (p. 96)
1. The joint is $p(\mathbf x_k,\mathbf x_{k-1}\mid\mathbf y_{1:k-1})=p(\mathbf x_k\mid\mathbf x_{k-1},\mathbf y_{1:k-1})p(\mathbf x_{k-1}\mid\mathbf y_{1:k-1})=p(\mathbf x_k\mid\mathbf x_{k-1})p(\mathbf x_{k-1}\mid\mathbf y_{1:k-1})$ (6.14). The measurement history drops out by the Markov property.
2. Integrating over $\mathbf x_{k-1}$ gives (6.15), which is (6.11). If $\mathbf x_{k-1}$ is discrete, sum instead.
3. Bayes' rule gives $p(\mathbf x_k\mid\mathbf y_{1:k})=\frac1{Z_k}p(\mathbf y_k\mid\mathbf x_k,\mathbf y_{1:k-1})p(\mathbf x_k\mid\mathbf y_{1:k-1})=\frac1{Z_k}p(\mathbf y_k\mid\mathbf x_k)p(\mathbf x_k\mid\mathbf y_{1:k-1})$ (6.16). The history drops out by conditional independence of $\mathbf y_k$ given $\mathbf x_k$.

*Intuition note:* Predict blurs yesterday's belief by the dynamics. Update sharpens it with today's measurement. Dividing by $Z_k$ just makes the result integrate to one.

### 6.3 Kalman filter (pp. 96–102)
**Model.** The linear Gaussian model is (p. 96)
$$\mathbf x_k=\mathbf A_{k-1}\mathbf x_{k-1}+\mathbf q_{k-1},\qquad \mathbf y_k=\mathbf H_k\mathbf x_k+\mathbf r_k,\tag{6.17}$$
with $\mathbf q_{k-1}\sim\mathrm N(\mathbf 0,\mathbf Q_{k-1})$, $\mathbf r_k\sim\mathrm N(\mathbf 0,\mathbf R_k)$ and prior $\mathbf x_0\sim\mathrm N(\mathbf m_0,\mathbf P_0)$. Equivalently $p(\mathbf x_k\mid\mathbf x_{k-1})=\mathrm N(\mathbf x_k\mid\mathbf A_{k-1}\mathbf x_{k-1},\mathbf Q_{k-1})$ and $p(\mathbf y_k\mid\mathbf x_k)=\mathrm N(\mathbf y_k\mid\mathbf H_k\mathbf x_k,\mathbf R_k)$ (6.18).

**Theorem 6.6 (Kalman filter).** The filtering equations can be evaluated in closed form, and all distributions are Gaussian (p. 97):
$$p(\mathbf x_k\mid\mathbf y_{1:k-1})=\mathrm N(\mathbf x_k\mid\mathbf m_k^-,\mathbf P_k^-),\ p(\mathbf x_k\mid\mathbf y_{1:k})=\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k),\ p(\mathbf y_k\mid\mathbf y_{1:k-1})=\mathrm N(\mathbf y_k\mid\mathbf H_k\mathbf m_k^-,\mathbf S_k).\tag{6.19}$$
Prediction:
$$\mathbf m_k^-=\mathbf A_{k-1}\mathbf m_{k-1},\qquad \mathbf P_k^-=\mathbf A_{k-1}\mathbf P_{k-1}\mathbf A_{k-1}^{\mathsf T}+\mathbf Q_{k-1}.\tag{6.20}$$
Update:
$$\begin{aligned}\mathbf v_k&=\mathbf y_k-\mathbf H_k\mathbf m_k^-,\\ \mathbf S_k&=\mathbf H_k\mathbf P_k^-\mathbf H_k^{\mathsf T}+\mathbf R_k,\\ \mathbf K_k&=\mathbf P_k^-\mathbf H_k^{\mathsf T}\mathbf S_k^{-1},\\ \mathbf m_k&=\mathbf m_k^-+\mathbf K_k\mathbf v_k,\\ \mathbf P_k&=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^{\mathsf T}.\end{aligned}\tag{6.21}$$
The recursion starts from $\mathbf m_0,\mathbf P_0$. (added step) Shapes follow from the dimensions: $\mathbf A,\mathbf P,\mathbf Q$ are $n\times n$; $\mathbf H$ is $m\times n$; $\mathbf R,\mathbf S$ are $m\times m$; $\mathbf K$ is $n\times m$.

**Proof.** (pp. 97–98)
1. By Lemma A.2 the joint of $\mathbf x_{k-1},\mathbf x_k$ given $\mathbf y_{1:k-1}$ is Gaussian (6.22):
$$p(\mathbf x_{k-1},\mathbf x_k\mid\mathbf y_{1:k-1})=\mathrm N(\mathbf x_k\mid\mathbf A_{k-1}\mathbf x_{k-1},\mathbf Q_{k-1})\mathrm N(\mathbf x_{k-1}\mid\mathbf m_{k-1},\mathbf P_{k-1})=\mathrm N\!\Big(\begin{pmatrix}\mathbf x_{k-1}\\ \mathbf x_k\end{pmatrix}\Big|\,\mathbf m',\mathbf P'\Big),$$
$$\mathbf m'=\begin{pmatrix}\mathbf m_{k-1}\\ \mathbf A_{k-1}\mathbf m_{k-1}\end{pmatrix},\quad \mathbf P'=\begin{pmatrix}\mathbf P_{k-1}&\mathbf P_{k-1}\mathbf A_{k-1}^{\mathsf T}\\ \mathbf A_{k-1}\mathbf P_{k-1}&\mathbf A_{k-1}\mathbf P_{k-1}\mathbf A_{k-1}^{\mathsf T}+\mathbf Q_{k-1}\end{pmatrix}.\tag{6.23}$$
By Lemma A.3 the marginal of $\mathbf x_k$ is $\mathrm N(\mathbf m_k^-,\mathbf P_k^-)$ with $\mathbf m_k^-,\mathbf P_k^-$ as in (6.20) (6.24–6.25).
2. By Lemma A.2 the joint of $\mathbf x_k,\mathbf y_k$ given $\mathbf y_{1:k-1}$ is (6.26)
$$\mathrm N(\mathbf y_k\mid\mathbf H_k\mathbf x_k,\mathbf R_k)\mathrm N(\mathbf x_k\mid\mathbf m_k^-,\mathbf P_k^-)=\mathrm N\!\Big(\begin{pmatrix}\mathbf x_k\\ \mathbf y_k\end{pmatrix}\Big|\,\mathbf m'',\mathbf P''\Big),$$
$$\mathbf m''=\begin{pmatrix}\mathbf m_k^-\\ \mathbf H_k\mathbf m_k^-\end{pmatrix},\quad \mathbf P''=\begin{pmatrix}\mathbf P_k^-&\mathbf P_k^-\mathbf H_k^{\mathsf T}\\ \mathbf H_k\mathbf P_k^-&\mathbf H_k\mathbf P_k^-\mathbf H_k^{\mathsf T}+\mathbf R_k\end{pmatrix}.\tag{6.27}$$
3. By Lemma A.3 the conditional $p(\mathbf x_k\mid\mathbf y_k,\mathbf y_{1:k-1})=p(\mathbf x_k\mid\mathbf y_{1:k})=\mathrm N(\mathbf m_k,\mathbf P_k)$ (6.28), where
$$\mathbf m_k=\mathbf m_k^-+\mathbf P_k^-\mathbf H_k^{\mathsf T}(\mathbf H_k\mathbf P_k^-\mathbf H_k^{\mathsf T}+\mathbf R_k)^{-1}[\mathbf y_k-\mathbf H_k\mathbf m_k^-],$$
$$\mathbf P_k=\mathbf P_k^--\mathbf P_k^-\mathbf H_k^{\mathsf T}(\mathbf H_k\mathbf P_k^-\mathbf H_k^{\mathsf T}+\mathbf R_k)^{-1}\mathbf H_k\mathbf P_k^-,\tag{6.29}$$
which can also be written in the form (6.21). (Lemmas A.2 and A.3 are cited here but are not included in this unit.)

*Intuition note:* Gaussians stay Gaussian under linear maps and conditioning, so the whole belief is described by $(\mathbf m,\mathbf P)$. The gain $\mathbf K_k$ weights the surprise $\mathbf v_k$ by how uncertain the prediction is compared with the sensor.

The authors note that this functional form is not the only possible one. For numerical stability, matrix square roots of covariances would be better than plain covariances (p. 98).

**Example 6.7 (scalar random walk).** For model (6.5) the equations are (p. 99)
$$m_k^-=m_{k-1},\quad P_k^-=P_{k-1}+Q,\quad m_k=m_k^-+\frac{P_k^-}{P_k^-+R}(y_k-m_k^-),\quad P_k=P_k^--\frac{(P_k^-)^2}{P_k^-+R}.\tag{6.31}$$
Figure 6.4 shows the result on the data of Figure 6.1.

**Example 6.8 (car tracking).** The state is $\mathbf x=(x_1,x_2,x_3,x_4)$: position $(x_1,x_2)$ and velocity $(x_3,x_4)$ (p. 99). The matrices are (p. 100)
$$\mathbf A=\begin{pmatrix}1&0&\Delta t&0\\0&1&0&\Delta t\\0&0&1&0\\0&0&0&1\end{pmatrix},\ \mathbf Q=\begin{pmatrix}\frac{q_1^c\Delta t^3}{3}&0&\frac{q_1^c\Delta t^2}{2}&0\\0&\frac{q_2^c\Delta t^3}{3}&0&\frac{q_2^c\Delta t^2}{2}\\\frac{q_1^c\Delta t^2}{2}&0&q_1^c\Delta t&0\\0&\frac{q_2^c\Delta t^2}{2}&0&q_2^c\Delta t\end{pmatrix},$$
$$\mathbf H=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix},\quad \mathbf R=\begin{pmatrix}\sigma_1^2&0\\0&\sigma_2^2\end{pmatrix}.$$
Here $q_1^c,q_2^c$ are the spectral densities (continuous-time variances) of the process noises. The prediction and update steps are (6.20) and (6.21) with these matrices (pp. 100–101). The simulation used $\sigma_1=\sigma_2=1/2$, $q_1^c=q_2^c=1$, $\Delta t=1/10$. The position RMSE is 0.77 from measurements alone and 0.43 for the Kalman filter (Figure 6.5, p. 101).

**Remarks.**
- Kalman (1960b) derived the filter differently, using orthogonal projections on the linear manifold spanned by the measurements (p. 101).
- That approach avoids explicit Gaussian noise assumptions, since the Kalman filter can then be seen as a more general best linear unbiased estimator. Its disadvantage is that the route to non-linear models is much less straightforward than in the Bayesian approach (p. 102).
- If the model matrices do not explicitly depend on $k$, then as $k\to\infty$ the filter approaches a time-invariant stationary (steady-state) Kalman filter. $\mathbf P_k\to\mathbf P$ and $\mathbf P_k^-\to\mathbf P^-$, the gain becomes a constant $\mathbf K$, and the filter is a time-invariant linear filter (p. 102).

### 6.4 Affine Kalman filter (pp. 102–103)
The model is $\mathbf x_k=\mathbf A_{k-1}\mathbf x_{k-1}+\mathbf a_{k-1}+\mathbf q_{k-1}$, $\mathbf y_k=\mathbf H_k\mathbf x_k+\mathbf b_k+\mathbf r_k$ (6.34), with known deterministic offsets $\mathbf a_{k-1},\mathbf b_k$.

**Theorem 6.9.** The distributions are Gaussian as in (6.35), with $p(\mathbf y_k\mid\mathbf y_{1:k-1})=\mathrm N(\mathbf H_k\mathbf m_k^-+\mathbf b_k,\mathbf S_k)$. Prediction: $\mathbf m_k^-=\mathbf A_{k-1}\mathbf m_{k-1}+\mathbf a_{k-1}$, $\mathbf P_k^-=\mathbf A_{k-1}\mathbf P_{k-1}\mathbf A_{k-1}^{\mathsf T}+\mathbf Q_{k-1}$ (6.36). Update (6.37): same as (6.21) except $\mathbf v_k=\mathbf y_k-\mathbf H_k\mathbf m_k^--\mathbf b_k$ (p. 103). The proof is analogous to Theorem 6.6, and with $\mathbf b_k=0$ the distributions equal (6.19) (p. 103).

### 6.5 Bayesian filter for discrete state space (pp. 103–105)
For $\mathbf x_k\in\mathbb X$ with $\mathbb X$ discrete, the integrals in (6.11) and (6.13) become sums. These models are often called hidden Markov models (HMMs) (p. 103).

**Corollary 6.10.** The prediction is $p(\mathbf x_k\mid\mathbf y_{1:k-1})=\sum_{\mathbf x_{k-1}\in\mathbb X}p(\mathbf x_k\mid\mathbf x_{k-1})p(\mathbf x_{k-1}\mid\mathbf y_{1:k-1})$ (6.38). The update is (6.39) with $Z_k=\sum_{\mathbf x_k\in\mathbb X}p(\mathbf y_k\mid\mathbf x_k)p(\mathbf x_k\mid\mathbf y_{1:k-1})$ (6.40) (p. 104).

**Finite case.** Take $\mathbb X=\{1,\dots,X\}$ and $\mathbb Y=\{1,\dots,Y\}$. Define $\Pi_{i,j}=p(x_k=j\mid x_{k-1}=i)$ and $O_{i,j}=p(y_k=j\mid x_k=i)$ (6.41), and $p^-_{j,k}=p(x_k=j\mid y_{1:k-1})$, $p_{j,k}=p(x_k=j\mid y_{1:k})$ (6.42).

**Corollary 6.11.** (p. 104)
$$p^-_{j,k}=\sum_i\Pi_{i,j}\,p_{i,k-1},\qquad p_{i,k}=\frac{O_{i,y_k}\,p^-_{i,k}}{\sum_j O_{j,y_k}\,p^-_{j,k}}.\tag{6.43}$$
This is closely related to the forward part of the forward–backward algorithm for HMMs. The smoother and the Viterbi algorithm (MAP trajectory) come in Sections 12.4 and 12.5 (p. 105).

**Example 6.12 (Gilbert–Elliot channel).** The filter (6.43) is applied to the model of Example 5.14. The filter estimate is the most probable state. Figure 6.6: error rate 11% for the filter, versus 14% for the baseline guess described in the caption as "no errors, $v_k=1$" (p. 105).

*Intuition note:* In the HMM case the predict step is a vector times the matrix $\Pi$. The update multiplies by one column of $O$ and renormalizes. It is the same two-step recipe as in the continuous case.

## Toy example (ours)
Scalar random walk (6.5) with $Q=R=1$, prior $m_0=0$, $P_0=1$. Use (6.31) with $y_1=2$, $y_2=1$.
- Step 1 predict: $m_1^-=0$, $P_1^-=1+1=2$. Update: $S_1=P_1^-+R=3$, gain $K_1=2/3$, $m_1=0+\tfrac23(2-0)=4/3$, $P_1=2-4/3=2/3$.
- Step 2 predict: $m_2^-=4/3$, $P_2^-=2/3+1=5/3$. Update: $S_2=5/3+1=8/3$, $K_2=(5/3)/(8/3)=5/8$, $v_2=1-4/3=-1/3$, $m_2=4/3+\tfrac58(-\tfrac13)=32/24-5/24=9/8$, $P_2=5/3-(25/9)/(8/3)=40/24-25/24=5/8$.
- Check: $P_k=K_kR$ in the scalar case, and $K_2R=5/8$. The posterior variance goes from the prior value 1 to 2/3 to 5/8 as two noisy measurements arrive. Each step costs the same number of operations.

## Concepts
- [[bayesian-filtering-equations]] (new) — recursion of Chapman–Kolmogorov prediction and Bayes update giving $p(\mathbf x_k\mid\mathbf y_{1:k})$ (p. 94)
- [[chapman-kolmogorov-equation]] (new) — predictive density as the integral of dynamic model times previous filtering density (p. 94)
- [[markov-property]] (new) — future state depends on the past only through the present state (p. 92)
- [[state-space-model]] — here a probabilistic one: dynamic model and measurement model as conditional distributions (p. 91)
- [[state]] — the hidden variable $\mathbf x_k$ whose distribution is estimated (p. 91)
- [[kalman-filter]] — closed-form Bayesian filter for linear Gaussian models, tracking mean and covariance (p. 97)
- [[kalman-gain]] — $\mathbf K_k=\mathbf P_k^-\mathbf H_k^{\mathsf T}\mathbf S_k^{-1}$, weight on the measurement residual (p. 97)
- [[observer]] — canon concept (state estimator); this unit does not mention observers (canon link only, not stated in this unit)
- [[stationary-kalman-filter]] (new) — constant-gain limit of the filter for time-invariant models (p. 102)
- [[affine-kalman-filter]] (new) — Kalman filter with known offsets in dynamics and measurement (p. 102)
- [[hidden-markov-model]] (new) — discrete-state Markov model with measurements; filtered by (6.43) (p. 103)

## Canonical instances
- [[gaussian-random-walk]] — scalar linear Gaussian model used to illustrate the filter (p. 92, 99)
- [[car-tracking-kalman]] — 4-dimensional position/velocity model with position measurements (p. 99–101)
- [[gilbert-elliot-channel]] — discrete-state filtering example (p. 105)

## Bridges (candidates)
- [structural-analogy] Kalman update $\mathbf m_k=\mathbf m_k^-+\mathbf K_k\mathbf v_k$ ↔ control theory: observer correcting a model prediction by a gain times output error — both run a model and correct it with measurement residuals.
- [same-math] Corollary 6.11 HMM filter ↔ forward pass of the forward–backward algorithm — the text says they are closely related (p. 105).
- [metaphor] Predict–update cycle ↔ feedback: measurement corrects the running estimate each step.
- [structural-analogy] Constant-gain stationary Kalman filter ↔ time-invariant linear (digital) filter (Ex. 6.3 asks which type).

## Questions this raises
- How do the equations change when the dynamic or measurement model is non-linear or non-Gaussian, so that the integrals have no closed form?
- When does the stationary gain exist for a time-invariant model, and how is it computed?
- How can the filter be implemented in a numerically stable way, for example with square-root covariances?
- How do smoothing equations reuse the filtering distributions to estimate past states?

## Exercises worth doing
- Ex. 6.1 (p. 106) — derive the Kalman filter for non-zero-mean noises; shows how offsets enter the mean — difficulty: medium
- Ex. 6.2 (p. 106) — implement and simulate the scalar random-walk filter — difficulty: easy
- Ex. 6.3 (p. 106) — stationary Kalman filter for the random walk and its frequency response — difficulty: medium
- Ex. 6.4 (p. 106) — Kalman filter for a discretized noisy resonator versus a baseline in RMSE — difficulty: medium
- Ex. 6.5 (p. 106–107) — binary HMM: verify $\Pi,\mathbf O$, simulate, compare filter with guessing $y_k$ — difficulty: easy
- Ex. 6.6 (p. 107) — grid approximation of the Bayesian filter, compared with the Kalman filter — difficulty: hard

## Reading notes
- Printed page = pdf − 30. The text layer lost minus signs, hats and bars. Equations were checked against the page images.
- The Figure 6.6 caption says "guessing by no errors, that is, $v_k=1$" gives 14%. The caption does not define $v_k$ on these pages, and $v_k$ is also the residual of (6.21), so treat the caption's meaning as unclear (Example 5.14, cited by Example 6.12, is not in this unit).
- Lemmas A.2 and A.3 are cited in the proof but are not in these pages.
- Pre-publication version of the 2nd edition (running notice on every page).
