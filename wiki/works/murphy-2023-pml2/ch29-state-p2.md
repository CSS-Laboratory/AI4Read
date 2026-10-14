---
id: murphy-2023-pml2/ch29-state-p2
work: murphy-2023-pml2
unit: "29 State-space models (part 2/3): §29.4 end, §29.5–§29.10.1"
pages: 997–1020
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# State-space models, part 2: HMM generalizations, linear dynamical systems, switching and nonlinear models

## L0 — One line
Starting from the HMM, one can add durations, hierarchy, several chains or run lengths; making everything linear-Gaussian gives the LDS, with exact filtering, EM learning and tracking uses, while switching or nonlinear versions need approximate inference.

## L1 — The gist (≤ 120 words)
The unit asks how to extend the plain hidden Markov model (HMM, with a discrete hidden state) and what changes when the hidden state is continuous. HMM extensions model non-geometric state durations, nested structure, distributed state, coupled streams, and changepoints through run lengths. The LDS (linear dynamical system, a linear-Gaussian state-space model) supports exact inference and covers tracking, online linear regression and adaptive filtering. Its parameters can be learned by EM, subspace methods or Bayesian sampling. Adding a discrete switch (SLDS) makes exact inference intractable, because the number of Gaussian modes explodes; this is why tracking with unknown assignments needs approximations. Nonlinear observation models, such as bearings-only tracking, rule out the Kalman filter.

**Prerequisites:** HMMs and forward-backward; Gaussian conditioning and the Kalman filter/smoother (Ch. 8); EM; Dirichlet and MNIW conjugacy; matrix calculus; negative binomial and geometric distributions.

## L2 — Key ideas
- A plain HMM has geometric state durations. Replacing each state by $n$ chained copies gives a negative-binomial duration. A hidden semi-Markov model (HSMM) models durations explicitly and can generate whole segments at once (pp. 997–999).
- Hierarchical HMMs (nested chains), factorial HMMs (several binary chains explaining one observation), coupled HMMs (chains influencing neighbours) and dynamic Bayes nets (DBNs, directed-graph models of a process over time) extend the HMM. Costs the source names include intractable exact inference for factorial HMMs and $O(MK^4)$ parameters for coupled HMMs (pp. 999–1003).
- Bayesian online changepoint detection (BOCPD) tracks a posterior over the current run length (time since the last changepoint), using a hazard function (the chance that a segment of the current length ends now). It is exact but $O(T^2)$, and conjugacy is needed for $O(1)$ updates per run length (pp. 1003–1006).
- The LDS has linear-Gaussian transition and observation models. Object tracking, recursive least squares and adaptive filtering are all LDS inference problems (pp. 1006–1010).
- LDS parameters can be learned by EM with Kalman-smoother statistics (closed-form M step), by SVD-based subspace identification, or by Bayesian blocked Gibbs sampling. It is useful to constrain the eigenvalues of $\mathbf F$ to be below 1 for stability (pp. 1011–1015).
- In a switching LDS (SLDS), exact filtering is intractable because the belief state grows to $2^t$ Gaussians for binary $m_t$. Approximations include pruning, particle filtering, ADF (replacing the big mixture by a smaller one) and structured variational inference (pp. 1015–1016).
- Multitarget tracking is an SLDS with data-association variables. Approximations: Hungarian matching (a hard one-to-one assignment), loopy belief propagation (the SPADA method), sequential Monte Carlo, and birth/death heuristics for an unknown number of targets (pp. 1017–1019).
- With nonlinear $h$ (bearings-only tracking), the Kalman filter no longer applies and approximate inference is used (p. 1020).

## L3 — Walkthrough

### End of §29.4: posterior of a Bayesian HMM (p. 997)
Given $\mathbf z_{1:T}$, the log prior plus log complete-data likelihood shows that the posteriors of $\boldsymbol\pi$ and each row $\mathbf A_{j\cdot}$ are Dirichlet. The posterior of the emission parameters $\{\mathbf E_j,\boldsymbol\Sigma_j\}$ is matrix normal inverse Wishart (MNIW). The hyperparameters come from replacing $\mathbf Y,\mathbf A,\mathbf X$ in Eq. (15.105) with $\hat{\mathbf Y}_j,\mathbf E_j,\tilde{\mathbf Y}_j$ (p. 997).

$$\boldsymbol\pi|\mathbf z_{1:T}\sim \mathrm{Dir}(\hat{\boldsymbol\alpha}_\pi),\quad \hat\alpha_{\pi,k}=\breve\alpha_\pi/K+\mathbb I(z_1=k)\tag{29.47}$$
$$\mathbf A_{j\cdot}|\mathbf z_{1:T}\sim \mathrm{Dir}(\hat{\boldsymbol\alpha}_A),\quad \hat\alpha_{A_j,k}=\breve\alpha_A/K+N_{jk}\tag{29.48}$$
$$\boldsymbol\Sigma_j|\mathbf z_{1:T},\mathbf y_{1:T}\sim \mathrm{IW}(\hat\nu_j,\hat{\boldsymbol\Psi}_j),\quad \mathbf E_j|\boldsymbol\Sigma_j,\mathbf z_{1:T},\mathbf y_{1:T}\sim\mathcal{MN}(\hat{\mathbf M}_j,\boldsymbol\Sigma_j,\hat{\mathbf V}_j)\tag{29.49}$$

*Intuition note.* Given the hidden states, each count-based quantity just adds counts to the Dirichlet prior. This is the conjugate update.

### 29.5 HMMs: generalizations

**29.5.1 Hidden semi-Markov model (HSMM).** In an HMM the time spent in state $i$ is geometric (p. 997):
$$p(d_i=d)=(1-A_{ii})A_{ii}^d\propto\exp(d\log A_{ii})\tag{29.50}$$
This exponential decay is "sometimes unrealistic". Fix 1: replace each state by $n$ copies with the same emissions, chained with self-loops $p$ and forward move $1-p$ (Fig. 29.15a). A path of length $d$ has probability $p^{d-n}(1-p)^n$. Multiplying by the number of paths gives (p. 997):
$$p(d)=\binom{d-1}{n-1}p^{d-n}(1-p)^n\tag{29.51}$$
This is a negative binomial. Varying $n$ and $p$ gives many waiting-time shapes (Fig. 29.15b, $p=0.99$) (p. 998).

Fix 2, the semi-Markov model: the next state depends on the previous state and on the time already spent in it. If the state is hidden, this is an HSMM (also called variable-duration or explicit-duration HMM) (p. 998). Graphical model (Fig. 29.16a): a duration counter $d_t\in\{1,\dots,D\}$, with $D$ the maximum duration. On entering state $j$, sample $d_t\sim p_j(\cdot)$, then count down to 1:
$$p(d_t=d'|d_{t-1}=d,z_t=j)=\begin{cases}D_j(d')&d=1\\1&d'=d-1,\ d>1\\0&\text{otherwise}\end{cases}\tag{29.52}$$
$D_j$ can be a table or a parametric law (e.g. gamma). A truncated geometric $D_j$ emulates a standard HMM. While $d>1$ the state stays; at $d=1$ it jumps (assuming $A_{jj}=0$) (p. 998):
$$p(z_t=k|z_{t-1}=j,d_{t-1}=d)=\begin{cases}1&d>1,\ j=k\\A_{jk}&d=1\\0&\text{otherwise}\end{cases}\tag{29.53}$$
An HSMM can also model a whole subsequence at once, with likelihood $p(\mathbf y_{t:t+l-1}|z_t=k,d_t=l)$ giving $l$ correlated observations. This is a segmental HMM, useful for piecewise-linear data or local trends. An RNN per segment gives an RNN-HSMM (p. 998). The segmental HMM is
$$p(\mathbf y,\mathbf z,\mathbf d)=\Big[p(z_1)p(d_1|z_1)\prod_{t=2}^T p(z_t|z_{t-1},d_{t-1})p(d_t|z_t,d_{t-1})\Big]p(\mathbf y|\mathbf z,\mathbf d)\tag{29.54}$$
A standard HSMM uses $p(\mathbf y|\mathbf z,\mathbf d)=\prod_t p(y_t|z_t)$ (29.55), so durations affect only the hidden dynamics. For a segmental HMM, segment starts and ends follow from $\mathbf d$: $s_1=1$, $s_i=s_{i-1}+d_{s_{i-1}}$, $e_i=s_i+d_{s_i}-1$ (p. 999):
$$p(\mathbf y|\mathbf z,\mathbf d)=\prod_{i=1}^{|\mathbf s|}p(\mathbf y_{s_i:e_i}|z_{s_i},d_{s_i})\tag{29.56}$$
With an RNN per segment (hidden state $h_t$ updated deterministically from earlier observations in the segment):
$$p(\mathbf y_{s_i:e_i}|z_{s_i},d_{s_i})=\prod_{t=s_i}^{e_i}p(y_t|\mathbf y_{s_i:t-1},z_{s_i})=\prod_{t=s_i}^{e_i}p(y_t|h_t,z_{s_i})\tag{29.57}$$
Cited results: [Chi14] computes $p(z_t,d_t|\mathbf y_{1:T})$ in $O(TK^2+TKD)$ time; [Dai+17] trains an approximate mean-field posterior $q(\mathbf z,\mathbf d|\mathbf y)=\prod_t q(z_t|\mathbf y)q(d_t|\mathbf y)$, computing the posterior in $O(TK+TD)$ (p. 999).

*Intuition note.* Chaining $n$ sticky states makes a state "last" a sum of $n$ geometric times, so very short stays become unlikely. The HSMM instead keeps an explicit countdown.

**29.5.2 Hierarchical HMMs (HHMM).** These model hierarchical structure, e.g. in speech recognition words → phones → subphones (Fig. 29.17). An HHMM can always be flattened to a regular HMM, but the factored form is often easier to interpret and allows more efficient inference and fitting (p. 999). Applications listed include speech, gene finding, plan recognition, transportation monitoring and robot localization. HHMMs are less expressive than stochastic context-free grammars (bounded hierarchy depth only), but inference is $O(T)$ rather than $O(T^3)$ for SCFGs (inside-outside) (p. 1001). In the DPGM (Fig. 29.18), $Z_t^\ell$ is the state at level $\ell$ and $F_t^\ell=1$ if the level-$\ell$ HMM has finished. A transition at level $\ell$ is allowed only if the chain below has finished, per the node $F_t^{\ell-1}$. So higher levels evolve more slowly and lower levels are nested within higher ones. A variable-duration HMM is a special case: the top level is a deterministic counter and the bottom level a regular HMM that can change state only after the counter times out (p. 1001).

**29.5.3 Factorial HMMs (FHMM).** A single $z_t\in\{1..K\}$ needs $K=2^{10}=1024$ states for 10 bits. A distributed representation uses 10 binary variables $z_{t,m}$ (p. 1001):
$$p(\mathbf z,\mathbf y)=\prod_t\Big[\prod_m p(z_{tm}|z_{t-1,m})\Big]p(\mathbf y_t|\mathbf z_t)\tag{29.58}$$
Here $p(z_{tm}=k|z_{t-1,m}=j)=A_{mjk}$ and $p(z_{1m}=k)=\pi_{mk}$ are per-chain. The observation model is
$$p(\mathbf y_t|\mathbf z_t)=\mathcal N\Big(\mathbf y_t\Big|\sum_{m=1}^M\mathbf W_m\mathbf z_{tm},\boldsymbol\Sigma\Big)\tag{29.59}$$
where $\mathbf z_{tm}$ is the 1-of-$K$ encoding and $\mathbf W_m$ is $D\times K$ for $\mathbf y_t\in\mathbb R^D$ (Fig. 29.19a). Application, energy disaggregation: observe total household energy,
$$p(y_t|\mathbf z_t)=\mathcal N\Big(y_t\Big|\sum_m w_m z_{tm},\sigma^2\Big)\tag{29.60}$$
with $w_m$ the power of device $m$ and $z_{tm}=1$ if it is on. Transitions: $p(z_{t,m}=1|z_{t-1,m})=A_{01}$ if $z_{t-1,m}=0$, $A_{11}$ if $z_{t-1,m}=1$ (29.61) (p. 1001). Inference over time separates the total into per-device parts (p. 1002). Given $\mathbf y_t$, all hidden variables become correlated ("explaining away" of the common observed child), so exact state estimation is intractable. Approximate algorithms exist (Supplementary §10.3.2) (p. 1002).

**29.5.4 Coupled HMMs.** For related data streams, each chain's transition depends on neighbouring chains (p. 1002):
$$p(\mathbf z_t,\mathbf y_t|\mathbf z_{t-1})=\prod_m p(\mathbf y_{tm}|z_{tm})\,p(z_{tm}|\mathbf z_{t-1,m-1:m+1})\tag{29.62}$$
Drawbacks: exact inference costs $O(T(K^M)^2)$ (not usually a problem in practice since $M$ is often small), and $O(MK^4)$ parameters are needed. The influence model uses fewer parameters through a convex combination of pairwise transition matrices (p. 1002).

**29.5.5 Dynamic Bayes nets (DBN).** A DBN represents a stochastic process with a directed graphical model. The network itself is not dynamic: structure and parameters are fixed. It is a natural generalization of the HMM. To define one, specify the first time-slice structure, the inter-slice structure and the CPD forms. Example: the BATnet for a simulated autonomous car (Fig. 29.20) (p. 1003).

**29.5.6 Changepoint detection.** The task is detecting abrupt changes in the distribution of a time series, here the online case (p. 1003). Instead of an HSMM down-counter, use a run length $r_t\in\{0,1,\dots\}$ that resets to 0 at a new segment and counts up (Fig. 29.21):
$$p(r_t|r_{t-1})=\begin{cases}H(r_{t-1}+1)&r_t=0\\1-H(r_{t-1}+1)&r_t=r_{t-1}+1\\0&\text{otherwise}\end{cases}\tag{29.63}$$
$$H(\tau)=\frac{p_g(\tau)}{\sum_{t=\tau}^\infty p_g(t)}\tag{29.64}$$
$H$ is the hazard function, and $p_g(t)$ is the probability of a segment of length $t$. If $p_g$ is geometric with parameter $\lambda$, then $H(\tau)=1/\lambda$ is constant (p. 1004).

The advantage of run lengths is that the within-segment observation model is causal (uses only past data):
$$p(\mathbf y_t|\mathbf y_{1:t-1},r_t=r,z_t=k)=p(\mathbf y_t|\mathbf y_{t-r:t-1},z_t=k)=\int p(\mathbf y_t|\boldsymbol\eta)p(\boldsymbol\eta|\mathbf y_{t-r:t-1},z_t=k)d\boldsymbol\eta\tag{29.65}$$
Here $\boldsymbol\eta$ are the segment-local parameters; this is the underlying predictive model (UPM). Its posterior is
$$p(\boldsymbol\eta|\mathbf y_{t-r:t-1},z_t=k)\propto p(\boldsymbol\eta|z_t=k)\prod_{i=t-r}^{t-1}p(\mathbf y_i|\boldsymbol\eta)\tag{29.66}$$
The prior hyperparameters are chosen by state $k$. If the model is conjugate exponential, this is closed form:
$$\pi_t^{r,k}=p(\mathbf y_t|\mathbf y_{t-r:t-1},z_t=k)=p(\mathbf y_t|\boldsymbol\psi_t^{r,k})\tag{29.67}$$
where $\boldsymbol\psi_t^{r,k}$ are the posterior-predictive parameters based on the last $r$ observations (p. 1004). For $K=1$, segments are independent, giving a product partition model, so there is no information sharing between segments (pp. 1004–1005):
$$p(\mathbf y|\mathbf r)=p(\mathbf y_{s_1:e_1})\cdots p(\mathbf y_{s_N:e_N})\tag{29.68}$$

*BOCPD.* An exact online algorithm was proposed in [FL07] and independently in [AM07], where it is named Bayesian online changepoint detection. The run-length posterior is computed recursively, with $p(r_0=0)=1$ (p. 1005):
$$p(r_t|\mathbf y_{1:t})\propto p(\mathbf y_t|\mathbf y_{1:t-1},r_t)\,p(r_t|\mathbf y_{1:t-1})\tag{29.69}$$
$$p(r_t|\mathbf y_{1:t-1})=\sum_{r_{t-1}}p(r_t|r_{t-1})p(r_{t-1}|\mathbf y_{1:t-1})\tag{29.70}$$
$$p(\mathbf y_{t+1}|\mathbf y_{1:t})=\sum_{r_t}p(\mathbf y_{t+1}|\mathbf y_{1:t},r_t)p(r_t|\mathbf y_{1:t})\tag{29.71}$$
The likelihood in (29.69) is (29.65) with $z_t$ dropped. Example (Fig. 29.22): synthetic 1d data from a 4-state GMM, likelihood $\mathcal N(y_t|\mu,\sigma^2)$ with $\sigma^2=1$ fixed and a Gaussian prior on $\mu$. The hazard is geometric with rate $N/T$, where $N=4$ is the true number of changepoints and $T=200$ (p. 1005).

*Extensions (pp. 1005–1006).* Each update is $O(t)$, so the total is $O(T^2)$. Particle filtering with $N$ particles and stratified optimal resampling gives $O(TN)$ [FL07]. The $O(1)$ per-$r$ update relies on conjugate exponential models. For more complex models: variational Bayes [TBS13] or particle filtering [Mav16] (more general but much slower). Other extensions: Markov dependence between neighbouring segments' parameters [FL11]; a Gaussian-process UPM [STR10]; generalized Bayesian inference for robustness to misspecification [KJD18]; modelling a sequence of observations rather than a single-step likelihood ratio [Gol+17]. [AE+20] allow multiple discrete states and put both $r_t$ and $d_t$ in the state, so the end of a segment can be predicted and the UPM can depend on duration:
$$p(y_t|r_t,d_t,\boldsymbol\eta)=\mathcal N(y_t|\boldsymbol\phi(r_t/d_t)^\top\boldsymbol\eta,\sigma^2),\quad 0\le r_t/d_t\le1\tag{29.72}$$
with $\boldsymbol\phi$ learned basis functions. Sequences from the same hidden state then share a functional shape even when durations differ (p. 1006).

*Intuition note.* BOCPD keeps a distribution over "how long since the last change". Each step, either the run grows by one (no change) or resets to 0, weighted by the hazard and by how well the segment's own predictive model explains the new point.

### 29.6 Linear dynamical systems (LDS)
The LDS, or linear-Gaussian SSM (LG-SSM), is an SSM with linear transition and observation functions and Gaussian process and observation noise (p. 1006). Its graphical model is Fig. 29.1(a): Markov hidden states, observations iid given the states (p. 1006).
$$p(\mathbf z_t|\mathbf z_{t-1},\mathbf u_t)=\mathcal N(\mathbf z_t|\mathbf F_t\mathbf z_{t-1}+\mathbf B_t\mathbf u_t+\mathbf b_t,\mathbf Q_t)\tag{29.73}$$
$$p(\mathbf y_t|\mathbf z_t,\mathbf u_t)=\mathcal N(\mathbf y_t|\mathbf H_t\mathbf z_t+\mathbf D_t\mathbf u_t+\mathbf d_t,\mathbf R_t)\tag{29.74}$$
With zero biases this becomes (29.75)–(29.76) (drop $\mathbf b_t,\mathbf d_t$). With no inputs: $p(\mathbf z_t|\mathbf z_{t-1})=\mathcal N(\mathbf z_t|\mathbf F_t\mathbf z_{t-1},\mathbf Q_t)$ and $p(\mathbf y_t|\mathbf z_t)=\mathcal N(\mathbf y_t|\mathbf H_t\mathbf z_t,\mathbf R_t)$ (29.77–29.78). Equivalent structural form (p. 1007):
$$\mathbf z_t=\mathbf F_t\mathbf z_{t-1}+\mathbf q_t,\quad \mathbf y_t=\mathbf H_t\mathbf z_t+\mathbf r_t\tag{29.79–29.80}$$
with $\mathbf q_t\sim\mathcal N(\mathbf 0,\mathbf Q_t)$ the process noise and $\mathbf r_t\sim\mathcal N(\mathbf 0,\mathbf R_t)$ the observation noise. Parameters are typically time-independent (stationary). Online inference uses the Kalman filter (§8.2.2) and offline inference the Kalman smoother (§8.2.3) (p. 1007).

### 29.7 LDS: applications

**29.7.1 Object tracking.** State $\mathbf z_t=(u_t,v_t,\dot u_t,\dot v_t)$ is the 2d position and velocity. Newton's law with white-noise random acceleration is a linear SDE. It is evaluated at discrete observation times (a continuous-discrete SSM) (p. 1007). With step $\Delta$ and noise $\mathbf q_t\sim\mathcal N(\mathbf 0,\mathbf Q)$:
$$\begin{pmatrix}u_t\\v_t\\\dot u_t\\\dot v_t\end{pmatrix}=\underbrace{\begin{pmatrix}1&0&\Delta&0\\0&1&0&\Delta\\0&0&1&0\\0&0&0&1\end{pmatrix}}_{\mathbf F\ (4\times4)}\begin{pmatrix}u_{t-1}\\v_{t-1}\\\dot u_{t-1}\\\dot v_{t-1}\end{pmatrix}+\mathbf q_t\tag{29.81}$$
$$\mathbf Q=\begin{pmatrix}\frac{q_1\Delta^3}{3}&0&\frac{q_1\Delta^2}{2}&0\\0&\frac{q_2\Delta^3}{3}&0&\frac{q_2\Delta^2}{2}\\\frac{q_1\Delta^2}{2}&0&q_1\Delta&0\\0&\frac{q_2\Delta^2}{2}&0&q_2\Delta\end{pmatrix}$$
where $q_i$ are the diffusion coefficients of the white noise in dimension $i$ (p. 1008). The location is observed with noise:
$$\begin{pmatrix}y_{1,t}\\y_{2,t}\end{pmatrix}=\underbrace{\begin{pmatrix}1&0&0&0\\0&0&1&0\end{pmatrix}}_{\mathbf H\ (2\times4)}\begin{pmatrix}u_t\\\dot u_t\\v_t\\\dot v_t\end{pmatrix}+\mathbf r_t\tag{29.82}$$
$\mathbf H$ "extracts" the relevant state entries. (See Reading notes on the state ordering printed here.) Simulation (Fig. 29.23): $\mathbf R=\mathrm{diag}(\sigma_1^2,\sigma_2^2)$; the Kalman filter is initialized with the vague prior $p(\mathbf z_0)=\mathcal N(\mathbf 0,10^5\mathbf I)$. The filtered mean is close to the truth with considerable uncertainty. The smoother (conditioning on past and future) gives a smoother estimate with less uncertainty, larger at the edges. MSE: filtering 3.13, smoothing 1.71 (p. 1009, caption).

**29.7.2 Online Bayesian linear regression (recursive least squares, RLS).** Sequential Bayesian updating (p. 1008):
$$p(\mathbf w|\mathcal D_{1:t})\propto p(\mathcal D_t|\mathbf w)p(\mathbf w|\mathcal D_{1:t-1})\propto p(\mathcal D_t|\mathbf w)p(\mathcal D_{t-1}|\mathbf w)\cdots p(\mathcal D_1|\mathbf w)p(\mathbf w)\tag{29.83–29.84}$$
Implement it as an LG-SSM: the hidden state holds the regression weights, and the time-varying observation matrix $\mathbf H_t$ is the current feature vector (p. 1010):
$$p(y_t|\mathbf w_t)=\mathcal N(y_t|\mathbf H_t\mathbf z_t,\mathbf R_t)=\mathcal N(y_t|\mathbf x_t^\top\mathbf w_t,\sigma^2)\tag{29.85}$$
$$p(\mathbf w_t|\mathbf w_{t-1})=\mathcal N(\mathbf w_t|\mathbf w_{t-1},0)=\delta(\mathbf w_t-\mathbf w_{t-1})\tag{29.86}$$
If the weights may drift, one gets a dynamic linear model. Footnote 3: one cannot set $\mathbf u_t=\mathbf x_t$, since then features multiply the constant parameter $\mathbf D_t$ rather than the hidden weights. Fig. 29.24b: online inference converges to the batch posterior in a single pass. Approximating the Kalman gain by $\mathbf K_t\approx\eta_t\mathbf 1$ recovers least mean squares (LMS) with learning rate $\eta_t$. LMS needs its rate adapted and may need multiple passes. RLS adapts step size automatically and reaches the optimal posterior in one pass (p. 1010).

**29.7.3 Adaptive filtering.** For the AR($D$) model $y_t=w_1y_{t-1}+\dots+w_Dy_{t-D}+\epsilon_t$, $\epsilon_t\sim\mathcal N(0,1)$ (29.87), estimate $\mathbf w_{1:D}$ from $\mathbf y_{1:t}$. Cast as an LG-SSM with $\mathbf H_t=(y_{t-1}\dots y_{t-D})$ and $\mathbf z_t=\mathbf w$; the parameters may also evolve (p. 1010). **29.7.4** Forecasting is deferred to §29.12 (p. 1010).

*Intuition note.* In RLS the "state" is the unknown weight vector, which is assumed not to change over time here. Each data point is a noisy linear measurement of it, so Kalman filtering is the same as sequential Bayesian updating of the weights.

### 29.8 LDS: parameter learning (called systems identification in control theory; p. 1011)

**29.8.1 EM for LDS.** Conceptually similar to Baum-Welch (§29.4.1), but the E step uses Kalman smoothing and the M step has different formulas [SS82; GH96a]. The text extends this to the case with inputs $\mathbf u_{1:T}$ (the text says "the HMM may have an optional input sequence", presumably meaning the LDS). Maximize (p. 1011)
$$\mathcal Q(\boldsymbol\theta,\boldsymbol\theta_{k-1})=\mathbb E[\log p(\mathbf z_{1:T},\mathbf y_{1:T}|\boldsymbol\theta)|\mathbf y_{1:T},\mathbf u_{1:T},\boldsymbol\theta_{k-1}]\tag{29.88}$$
Initialize randomly or from a simpler model such as factor analysis. Biases are absorbed into $\mathbf D,\mathbf B$ (last entry of $\mathbf u_t$ is 1). The log joint, with $p(\mathbf z_1)=\mathcal N(\mathbf m_1,\mathbf V_1)$:
$$\log p=-\sum_{t=1}^T\tfrac12(\mathbf y_t-\mathbf H\mathbf z_t-\mathbf D\mathbf u_t)^\top\mathbf R^{-1}(\cdot)-\tfrac T2\log|\mathbf R|\tag{29.89}$$
$$\quad-\sum_{t=2}^T\tfrac12(\mathbf z_t-\mathbf F\mathbf z_{t-1}-\mathbf B\mathbf u_t)^\top\mathbf Q^{-1}(\cdot)-\tfrac{T-1}2\log|\mathbf Q|\tag{29.90}$$
$$\quad-\tfrac12(\mathbf z_1-\mathbf m_1)^\top\mathbf V_1^{-1}(\mathbf z_1-\mathbf m_1)-\tfrac12\log|\mathbf V_1|+\text{const}\tag{29.91}$$
*E step.* The Kalman smoother gives $\boldsymbol\mu_{t|T}=\mathbb E[\mathbf z_t|\mathbf y_{1:T}]$ and $\boldsymbol\Sigma_{t|T}$; set $\hat{\mathbf z}_t=\boldsymbol\mu_{t|T}$ (p. 1011):
$$\mathbf P_t=\mathbb E[\mathbf z_t\mathbf z_t^\top|\mathbf y_{1:T}]=\boldsymbol\Sigma_{t|T}+\boldsymbol\mu_{t|T}\boldsymbol\mu_{t|T}^\top\tag{29.92}$$
$$\mathbf P_{t,t-1}=\mathbb E[\mathbf z_t\mathbf z_{t-1}^\top|\mathbf y_{1:T}]=\boldsymbol\Sigma_{t,t-1|T}+\boldsymbol\mu_{t|T}\boldsymbol\mu_{t-1|T}^\top\tag{29.93}$$
$$\boldsymbol\Sigma_{t-1,t-2|T}=\boldsymbol\Sigma_{t-1|t-1}\mathbf J_{t-2}^\top+\mathbf J_{t-1}(\boldsymbol\Sigma_{t,t-1|T}-\mathbf F\boldsymbol\Sigma_{t-1|t-1})\mathbf J_{t-2}^\top\tag{29.94}$$
with $\mathbf J_t$ the backwards Kalman gain (Eq. 8.67), initialized by $\boldsymbol\Sigma_{T,T-1|T}=(\mathbf I-\mathbf K_T\mathbf H)\mathbf F\boldsymbol\Sigma_{T-1|T-1}$ ($\mathbf K_T$ forwards Kalman gain, Eq. 8.28) (p. 1012).

*M step* (matrix calculus; p. 1012). Notation: $\mathbf A_{\rm out}=[\mathbf H,\mathbf D]$ (shape $N_y\times(N_z+N_u)$, added), $\hat{\mathbf x}_{{\rm out},t}=[\hat{\mathbf z}_t^\top,\mathbf u_t^\top]^\top$, $\mathbf A_{\rm dyn}=[\mathbf F,\mathbf B]$, $\hat{\mathbf x}_{{\rm dyn},t}=[\hat{\mathbf z}_{t-1}^\top,\mathbf u_t^\top]^\top$,
$$\mathbf P_{{\rm out},t}=\begin{pmatrix}\mathbf P_t&\hat{\mathbf z}_t\mathbf u_t^\top\\\mathbf u_t\hat{\mathbf z}_t^\top&\mathbf u_t\mathbf u_t^\top\end{pmatrix},\quad\mathbf P_{{\rm dyn},t}=\begin{pmatrix}\mathbf P_{t-1}&\hat{\mathbf z}_{t-1}\mathbf u_t^\top\\\mathbf u_t\hat{\mathbf z}_{t-1}^\top&\mathbf u_t\mathbf u_t^\top\end{pmatrix}\tag{29.95}$$
- Output matrices: $\frac{\partial\mathcal Q}{\partial\mathbf A_{\rm out}}=\sum_t\mathbf R^{-1}\mathbf y_t\hat{\mathbf x}_{{\rm out},t}^\top-\sum_t\mathbf R^{-1}\mathbf A_{\rm out}\mathbf P_{{\rm out},t}=\mathbf 0$ (29.96), so $\mathbf A_{\rm out}^{\rm new}=\big(\sum_t\mathbf y_t\hat{\mathbf x}_{{\rm out},t}^\top\big)\big(\sum_t\mathbf P_{{\rm out},t}\big)^{-1}$ (29.97).
- Output noise: $\frac{\partial\mathcal Q}{\partial\mathbf R^{-1}}=\frac T2\mathbf R-\frac12\sum_t(\mathbf y_t\mathbf y_t^\top-2\mathbf A_{\rm out}^{\rm new}\hat{\mathbf x}_{{\rm out},t}\mathbf y_t^\top+\mathbf A_{\rm out}^{\rm new}\mathbf P_{{\rm out},t}\mathbf A_{\rm out}^{{\rm new},\top})=\mathbf 0$ (29.98), so $\mathbf R^{\rm new}=\frac1T\sum_t(\mathbf y_t\mathbf y_t^\top-\mathbf A_{\rm out}^{\rm new}\hat{\mathbf x}_{{\rm out},t}\mathbf y_t^\top)$ (29.99).
- Dynamics matrices: $\frac{\partial\mathcal Q}{\partial\mathbf A_{\rm dyn}}=-\sum_{t=2}^T\mathbf Q^{-1}[\mathbf P_{t,t-1},\hat{\mathbf z}_t\mathbf u_t^\top]+\sum_{t=2}^T\mathbf Q^{-1}\mathbf A_{\rm dyn}\mathbf P_{{\rm dyn},t}=\mathbf 0$ (29.100), so $\mathbf A_{\rm dyn}^{\rm new}=\big(\sum_{t=2}^T[\mathbf P_{t,t-1},\hat{\mathbf z}_t\mathbf u_t^\top]\big)\big(\sum_{t=2}^T\mathbf P_{{\rm dyn},t}\big)^{-1}$ (29.101).
- State noise: the derivative (29.102) simplifies to (29.103), $\frac{T-1}2\mathbf Q-\frac12\sum_{t=2}^T(\mathbf P_t-\mathbf A_{\rm dyn}^{\rm new}[\mathbf P_{t-1,t},\mathbf u_t\hat{\mathbf z}_t^\top])=\mathbf 0$, giving $\mathbf Q^{\rm new}=\frac1{T-1}\sum_{t=2}^T(\mathbf P_t-\mathbf A_{\rm dyn}^{\rm new}[\mathbf P_{t-1,t},\mathbf u_t\hat{\mathbf z}_t^\top])$ (29.104).
- Initial state (p. 1013): $\frac{\partial\mathcal Q}{\partial\mathbf m}=(\hat{\mathbf z}_1-\mathbf m)\mathbf V_1^{-1}=\mathbf 0$ (29.105), so $\mathbf m^{\rm new}=\hat{\mathbf z}_1$ (29.106). $\frac{\partial\mathcal Q}{\partial\mathbf V_1^{-1}}=\frac{\mathbf V_1}2-\frac12(\mathbf P_1-\hat{\mathbf z}_1\mathbf m_1^\top-\mathbf m_1\hat{\mathbf z}_1^\top+\mathbf m_1\mathbf m_1^\top)=\mathbf 0$ (29.107), so $\mathbf V_1^{\rm new}=\mathbf P_1-\hat{\mathbf z}_1\hat{\mathbf z}_1^\top$ (29.108).

Computing these statistics costs $O(T)$ per EM iteration. ASOS [Mar10b] precomputes statistics in one pass so later iterations are constant time. With multiple processors, Kalman smoothing takes $O(\log T)$ by parallel scan (§8.2.3.4) (p. 1013).

*Skip path (our gloss, not stated in the source):* the M-step formulas have the shape of least-squares normal equations built from the smoother's expected sufficient statistics $\mathbf P$.

**29.8.2 Subspace identification (SSID).** EM is sensitive to initialization. In the noise-free case, $\mathbf z_t=\mathbf F\mathbf z_{t-1}$ and $\mathbf y_t=\mathbf H\mathbf z_t$, so $\mathbf y_t=\mathbf H\mathbf F^{t-1}\mathbf z_1$. All observations then lie in a $\dim(\mathbf z_t)$-dimensional subspace, which PCA can identify. Estimate the $\mathbf z_t$, then fit the model as if fully observed, and use this directly or to initialize EM. Several papers [Smi+00; BK15] show that EM initialized this way gives much better results than random initialization or SSID without EM. The theory covers only noise-free data, but one can try to estimate $\mathbf Q$ and $\mathbf R$ from prediction residuals. The method uses an SVD, so it is a spectral method (p. 1013).

**29.8.3 Stability.** With no system noise, $\mathbf z_t=\mathbf F^t\mathbf z_1=\mathbf U\boldsymbol\Lambda^t\mathbf U^{-1}\mathbf z_1$ (29.109). If any $\lambda_i>1$, $\mathbf z_t$ blows up for large $t$, so it is useful to require all eigenvalues below 1 [SBG07]. Then $\mathbb E[\mathbf z_t]=\mathbf 0$ for large $t$, but with noise the state stays non-zero, so the model does not degenerate (pp. 1013–1014).

**29.8.4 Bayesian LDS.** SSMs can be quite sensitive to parameter values, which matters for forecasting and for scientific interpretation, so representing parameter uncertainty is wise. Options: variational Bayes EM, blocked Gibbs, or collapsed MCMC (marginalize $\mathbf z_{1:T}$, sample $p(\boldsymbol\theta|\mathbf y_{1:T})$ with HMC). Since $\boldsymbol\theta$ and $\mathbf z$ are highly correlated, mean field can be inaccurate and blocked Gibbs can mix slowly (p. 1014).

*29.8.4.1 Blocked Gibbs.* Alternate (i) sampling $\mathbf z_{1:T}\sim p(\cdot|\mathbf y_{1:T},\boldsymbol\theta)$ by forwards-filter backwards-sampling (§8.2.3.5), and (ii) sampling $\boldsymbol\theta|\mathbf z_{1:T},\mathbf y_{1:T}$, easy with conjugate priors. Model: homogeneous parameters (29.110–29.111), $\boldsymbol\theta=\{\mathbf F,\mathbf H,\mathbf B,\mathbf D,\mathbf Q,\mathbf R\}$. Priors:
$$p(\mathbf Q,[\mathbf F,\mathbf B])=\mathrm{MNIW}(\mathbf M_{z0},\mathbf V_{z0},\nu_{q0},\boldsymbol\Psi_{q0}),\quad p(\mathbf R,[\mathbf H,\mathbf D])=\mathrm{MNIW}(\mathbf M_{y0},\mathbf V_{y0},\nu_{r0},\boldsymbol\Psi_{r0})\tag{29.112–29.113}$$
Posteriors are MNIW: $\mathbf Q|\mathbf z,\mathbf u\sim\mathrm{IW}(\nu_{q1},\boldsymbol\Psi_{q1})$, $[\mathbf F,\mathbf B]|\mathbf Q,\mathbf z,\mathbf u\sim\mathcal{MN}(\mathbf M_{z1},\mathbf Q,\mathbf V_{z1})$ (29.114–29.115). The hyperparameters follow by replacing $\mathbf Y,\mathbf A,\mathbf X$ in (15.105) with $\mathbf z_{2:T}$, $[\mathbf F,\mathbf B]$, $[\mathbf z_{t-1}^\top,\mathbf u_t^\top]^\top_{t=2:T}$. Likewise $\mathbf R\sim\mathrm{IW}(\nu_{r1},\boldsymbol\Psi_{r1})$ and $[\mathbf H,\mathbf D]|\mathbf R,\dots\sim\mathcal{MN}(\mathbf M_{y1},\mathbf R,\mathbf V_{y1})$ (29.116–29.117), using $\mathbf y_{1:T}$, $[\mathbf H,\mathbf D]$, $[\mathbf y_t^\top,\mathbf u_t^\top]^\top$ (pp. 1014–1015; the last replacement is printed with the index "$1;T$").

**29.8.5 Online parameter learning.** Estimating e.g. $\mathbf Q,\mathbf R$ online (to track non-stationary environments) is also called adaptive filtering. Cited approaches: moment-matching methods [JB67; Meh72], recursive MLE from the particle-filter derivative [ADT12], online variational Bayes [Cam+21; Hua+18c; VW21] (p. 1015).

### 29.9 Switching LDS (SLDS)
The latent state has a discrete $m_t\in\{1..K\}$ (a hybrid system in control theory) and a continuous $\mathbf z_t\in\mathbb R^{N_z}$; $\mathbf y_t\in\mathbb R^{N_y}$, optional $\mathbf u_t\in\mathbb R^{N_u}$. $m_t$ can represent operating regimes (normal/abnormal) or observation models (e.g. outliers from sensor failure). Other names: regime switching Markov model, jump Markov linear system (p. 1015).
$$p(m_t=k|m_{t-1}=j)=A_{jk},\quad p(\mathbf z_t|\mathbf z_{t-1},m_t=k,\mathbf u_t)=\mathcal N(\mathbf F_k\mathbf z_{t-1}+\mathbf B_k\mathbf u_t+\mathbf b_k,\mathbf Q_k)\tag{29.118–29.119}$$
$$p(\mathbf y_t|\mathbf z_t,m_t=k,\mathbf u_t)=\mathcal N(\mathbf H_k\mathbf z_t+\mathbf D_k\mathbf u_t+\mathbf d_k,\mathbf R_k)\tag{29.120}$$
**Posterior inference.** Exact inference is intractable even in the linear Gaussian case. Take binary $m_t$, with only $\mathbf F$ depending on $m_t$. The belief after $\mathbf y_1$ is a mixture of 2 Gaussians. The one-step predictive is a mixture of 4, and the belief at step 2 is again 4 (each updated by $\mathbf y_2$). At step 3 it is 8, and so on: an exponential explosion of modes (p. 1015). Each discrete sequence is a hypothesis ("track"), a tree (Fig. 29.25b) (p. 1016). Approximations listed (p. 1016): prune low-probability branches (multiple hypothesis tracking); particle filtering over discrete trajectories with Kalman filtering for the continuous part (§13.4.1); ADF, approximating the mixture by a smaller one (§8.6.2); structured variational inference with chain-structured factors for discrete and continuous variables plus coupling terms.

*Intuition note.* Every possible regime history gives its own Gaussian belief, so the number of beliefs doubles each step with two regimes. Several approximations keep only part of this tree or replace it by a smaller mixture.

**29.9.3 Multitarget tracking** (p. 1016). Warm-up (§29.9.3.1): if $N$ objects are known and each yields its own uniquely identified observation, and objects are independent, run Kalman filtering/smoothing in parallel (Fig. 29.26) (p. 1017). *Data association* (§29.9.3.2): at each step $M$ measurements may arrive, with $M<N$ (occlusion, missed detection), $M>N$ (clutter, false alarms) or $M=N$. The correspondence between detections and objects is unknown. Model it with discrete variables $m_t$ encoding the association (Fig. 29.27); inference is intractable, again due to the exponential number of modes (pp. 1017–1018).
- *Nearest neighbour + Hungarian algorithm* (§29.9.3.3): build an $N\times M$ compatibility matrix $W_{im}$ (closeness of measurement $m$ to the predicted position of object $i$). Pad with dummy background objects (explain false alarms) and dummy observations (explain missed detections) to get a square matrix. Maximal-weight bipartite matching by the Hungarian algorithm costs $O(\max(N,M)^3)$. Given the assignment, do the usual Kalman update. Objects assigned to dummies get no measurement update, only forward prediction (p. 1018).
- *Other schemes* (§29.9.3.4): the Hungarian method can be slow (cubic in the number of measurements) and can give poor results because it relies on hard assignment. Loopy belief propagation (SPADA) approximately marginalizes the assignments instead of taking a MAP estimate. Each iteration costs $O(NM)$; [WL14b] proved convergence in finitely many steps, [Von13] showed the solution is the global optimum. The text says SPADA is more efficient and accurate than earlier heuristics such as JPDA. SMC methods are also possible (p. 1018).
- *Unknown number of targets* (§29.9.3.5): an open-world model (§4.6.5), not the closed-world assumption. Fig. 29.28(b–c) shows two hypotheses about the tracks behind the data; the text asks whether there could be more targets (some undetected) or fewer (some observations false alarms), and (d) shows a more complex hypothesis with track termination, track initiation, a detection failure and a false alarm. This is multiple hypothesis tracking. A common approximation creates a new object when an observation is not well explained by existing ones, and prunes objects not detected for a while. Sets of random size and content are random finite sets (pp. 1018–1019).

### 29.10 Nonlinear SSMs (beginning)
$$\mathbf z_t=\mathbf f(\mathbf z_{t-1},\mathbf u_t)+\mathbf q_t,\ \mathbf q_t\sim\mathcal N(\mathbf 0,\mathbf Q_t);\quad\mathbf y_t=\mathbf h(\mathbf z_t,\mathbf u_t)+\mathbf r_t,\ \mathbf r_t\sim\mathcal N(\mathbf 0,\mathbf R_t)\tag{29.121–29.124}$$
This is a nonlinear dynamical system (NLDS) or NLG-SSM (p. 1020). Example (§29.10.1): linear 2d dynamics as in §29.7.1, but a bearings-only observation of the angle to the target from a sensor at $(s_x,s_y)$:
$$y_t=\tan^{-1}\!\Big(\frac{v_t-s_y}{u_t-s_x}\Big)+r_t\tag{29.125}$$
This nonlinear observation model prevents the Kalman filter, but approximate inference methods still apply (p. 1020). The part ends here.

## Toy example (ours)
Noise-free tracking step, with $\Delta=1$ and the ordering of (29.81): $\mathbf z_{t-1}=(u,v,\dot u,\dot v)=(0,0,1,2)$.
- $\mathbf F\mathbf z_{t-1}$: row 1 $=1\cdot0+0\cdot0+1\cdot1+0\cdot2=1$; row 2 $=0+1\cdot0+0+1\cdot2=2$; row 3 $=1$; row 4 $=2$. So $\mathbf z_t=(1,2,1,2)$ (position moved by velocity).
- Observation of the location with this ordering takes entries 1 and 2: $\mathbf y_t=(1,2)$ plus noise.
- Switching: with binary $m_t$, the number of Gaussian modes after steps $1,2,3$ is $2,4,8$, i.e. $2^t$. For $t=10$ that is $1024$.
- Duration check (29.51) with $n=2$, $p=0.5$: $p(d)=(d-1)\,0.5^{d}$, so $p(2)=0.25$, $p(3)=0.25$, $p(4)=0.1875$. The geometric law always has its mode at the shortest stay, but here $d=2$ and $d=3$ tie as most likely.

## Concepts
- [[hidden-semi-markov-model]] (new) — HMM with explicit state-duration distribution; segments may emit correlated blocks (p. 998)
- [[hazard-function]] (new) — $H(\tau)=p_g(\tau)/\sum_{t\ge\tau}p_g(t)$, probability a segment of length $\tau$ ends now (p. 1004)
- [[bayesian-online-changepoint-detection]] (new) — exact recursive posterior over run length $r_t$ (p. 1005)
- [[factorial-hmm]] (new) — several binary chains jointly explaining one observation; distributed hidden state (p. 1001)
- [[linear-gaussian-ssm]] (new) — LDS: linear transition/observation, Gaussian noise (p. 1006)
- [[kalman-filter-smoother]] (new) — exact online/offline inference in an LDS (cited from Ch. 8) (p. 1007)
- [[recursive-least-squares]] (new) — online Bayesian linear regression as Kalman filtering with weights as state (p. 1008)
- [[em-for-lds]] (new) — EM with Kalman smoother E step and closed-form M step (p. 1011)
- [[subspace-identification]] (new) — SVD/PCA-based spectral initialization of LDS parameters (p. 1013)
- [[switching-lds]] (new) — LDS with discrete regime variable; exact inference has exponentially many modes (p. 1015)
- [[data-association]] (new) — unknown matching of detections to objects (p. 1017)
- [[sequential-updating]] — today's posterior becomes tomorrow's prior (used for RLS) (p. 1008)
- [[conjugate-prior]] — Dirichlet/MNIW posteriors; conjugate UPM gives closed-form BOCPD likelihood (pp. 997, 1004)
- [[gibbs-sampling]] — blocked Gibbs alternating $\mathbf z_{1:T}$ and $\boldsymbol\theta$ (p. 1014)
- [[posterior-predictive-distribution]] — UPM predictive of $\mathbf y_t$ given the segment (p. 1004)

## Canonical instances
- [[energy-disaggregation-fhmm]] — total power split into devices (p. 1001)
- [[constant-velocity-tracking-lds]] — 2d position/velocity Kalman tracking; filter MSE 3.13 vs smoother 1.71 (pp. 1007–1009)
- [[bearings-only-tracking]] — nonlinear angle observation (p. 1020)
- [[multitarget-tracking-slds]] — data association, birth/death of tracks (pp. 1016–1019)
- [[hhmm-speech-recognition]] — words/phones/subphones (p. 1000)

## Bridges (candidates)
- [same-math] RLS ↔ Bayesian: sequential updating of a Gaussian posterior for linear-regression weights; both are the same conjugate update.
- [structural-analogy] BOCPD run-length posterior ↔ HMM forward algorithm: both recursively propagate a posterior over a latent counter/state with predict and update steps.
- [structural-analogy] SLDS mode explosion ↔ hierarchical/mixture models: growth of mixture components under conditioning, controlled by pruning or merging.
- [structural-analogy] Blocked Gibbs for LDS ↔ Gibbs sampling in hierarchical models: alternate latent variables and parameters.

## Questions this raises
- How exactly do the Kalman filter and smoother formulas (Ch. 8) produce $\mathbf P_t$ and $\mathbf P_{t,t-1}$ used in EM?
- Which approximate filters (EKF, UKF, particle) work best for bearings-only tracking, and when do they fail?
- When does the constraint on eigenvalues of $\mathbf F$ hurt, e.g. for oscillatory or marginally stable systems?
- How should the hazard rate be chosen or learned in BOCPD when changepoint frequency is unknown?

## Reading notes
- This part starts at the end of §29.4 (Eqs. 29.47–29.49, p. 997, mid-section) and ends at the start of §29.10, after Eq. 29.125 (p. 1020). Printed page = pdf − 34.
- Eq. 29.82 orders the state as $(u_t,\dot u_t,v_t,\dot v_t)$, while 29.81 and the text use $(u,v,\dot u,\dot v)$. With the 29.81 ordering, $\mathbf H$ would pick entries 1 and 2. The toy example uses the 29.81 ordering.
- Eq. 29.62 refers to "Section 29.5.4" for the illustration; the figure is 29.19b.
- §29.8.1 mentions an "HMM" with an input sequence; presumably LDS is meant.
- §29.8.3 says eigenvalues "$\lambda_i>1$" blow up; the source does not say explicitly that magnitudes are meant.
- Eq. 29.105 uses $\mathbf m$ and $\mathbf m_1$ interchangeably for the initial mean.
- Figure 29.18's extracted text layer contains an overlapping caption fragment (a "Figure 1" using $Q_t^d$, $F_t^d$) that differs from the book's $Z$, $F^\ell$ notation; the page image shows only the book's caption.
- No exercises appear in this unit.
