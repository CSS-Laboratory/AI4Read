---
id: murphy-2023-pml2/ch29-state-p3
work: murphy-2023-pml2
unit: "29 State-space models (part 3/3): §29.10.2–29.13 (non-Gaussian SSMs, structural time series, deep SSMs)"
pages: 1021-1041
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
# Non-Gaussian SSMs, structural time series models, and deep SSMs

## L0 — One line
A forecasting model can be built by adding simple linear-Gaussian latent components (trend, season, regressors); the same state-space idea then extends to count data, to counterfactual causal-impact estimation, and to neural-network dynamics trained with an ELBO.

## L1 — The gist (≤ 120 words)
The unit asks how to use state-space models (SSMs) when data are not linear-Gaussian, and how to forecast. For counts, it keeps Gaussian latent dynamics and uses a Poisson likelihood. For forecasting, structural time series (STS) models sum components (level, trend, season, covariates) into one linear-Gaussian SSM, so the Kalman filter gives forecasts. Fitting a model to the pre-intervention period and forecasting forward gives counterfactuals for causal impact. The unit then surveys neural forecasters. It ends with deep SSMs (deep Markov models, recurrent SSMs, variational RNNs), trained by maximizing an ELBO. This matters because the same state-space framework is applied here to forecasting, anomaly detection, causal impact and generative models of sequences.

**Prerequisites:** Kalman filter/smoother; Laplace approximation; EM; ELBO and KL divergence; reparameterization trick; basic structural causal models (counterfactuals).

## L2 — Key ideas (5–10 bullets)
- A non-Gaussian SSM allows non-Gaussian transition and/or observation noise (the functions may be linear or nonlinear); in the spike-train example the latent dynamics stay linear-Gaussian and the likelihood is Poisson. That example is fit by EM, using a Laplace approximation (a local Gaussian fit) in the E step (p. 1021–1022).
- An STS model writes the series as a sum of components, each a linear-Gaussian SSM. The sum is one linear-Gaussian SSM (LG-SSM) with sparse block matrices $\mathbf F,\mathbf H$, so only variances and regression weights are learned (p. 1023–1024).
- Building blocks: local level, local linear trend, semilocal trend, covariates and seasonality. Stacking the seasonal offsets makes the season first-order Markov (p. 1024–1026).
- Forecasting = Kalman-filter posterior over $\mathbf z_t$, then roll forward in latent space. Uncertain parameters are handled by Monte Carlo over posterior samples. Anomalies are flagged by one-step-ahead predictive z-scores (p. 1027–1029).
- Count data (sales) can use a Poisson likelihood on a latent demand. Out-of-stock zeros can be handled by a zero-inflated Poisson, but ZIP and negative binomial likelihoods are not log-concave (for $d_t=0$), so the Laplace approximation is a poor choice; a log-concave multi-stage likelihood is one remedy (p. 1028–1030).
- Causal impact: an STS model, copied into a "twin network" (a counterfactual copy of the post-intervention part of the model), predicts the counterfactual series, i.e. what would have happened without the intervention. This needs predictability, unaffectedness and stability (p. 1031–1033).
- Neural forecasters (ES-RNN, DeepSSM, Deep Factors, N-BEATS, DeepAR, quantile methods trained with the CRPS loss, a score for predicted quantile functions) become attractive when data are plentiful (p. 1035–1036).
- Deep SSMs (DMM, RSSM, VRNN) put neural networks into the dynamics or observation model. They are trained by stochastic variational inference (SVI) on an ELBO (evidence lower bound). Overshooting terms are proposed to improve multistep prediction (p. 1037–1041).

## L3 — Walkthrough

### 29.10.2 Posterior inference in nonlinear dynamical systems (p. 1021)
Inferring states of a nonlinear LDS is in general hard. Approximate schemes such as the extended and unscented Kalman filters can be used (p. 1021). Figure 29.30 shows samples from a 2-d LDS with 5 Poisson observation terms (p. 1021).

### 29.11 Non-Gaussian SSMs (p. 1021)
Transition and observation noise are non-Gaussian; the functions $f,h$ may be linear or nonlinear:
$$p(\mathbf z_t|\mathbf z_{t-1},\mathbf u_t)=p(\mathbf z_t|f(\mathbf z_{t-1},\mathbf u_t))\tag{29.126}$$
$$p(\mathbf y_t|\mathbf z_t,\mathbf u_t)=p(\mathbf y_t|h(\mathbf z_t,\mathbf u_t))\tag{29.127}$$
This is a non-Gaussian SSM (NSSM) (p. 1021).

**29.11.1 Spike-train example.** Latent dynamics are linear-Gaussian. The likelihood is Poisson, an exponential-family SSM used in neuroscience (p. 1021). The model has 2 latent dimensions, $\mathbf A$ is a random rotation matrix, and there are $D=5$ observations per step (p. 1022):
$$p(\mathbf y_t|\mathbf z_t)=\prod_{d=1}^{D}\mathrm{Poi}\big(y_{td}\,|\,\exp(\mathbf w_d^{\mathsf T}\mathbf z_t)\big)\tag{29.128}$$
with $\mathbf w_d$ random. Fitting uses EM. In the E step, $p(\mathbf y_t|\mathbf z_t)$ is approximated by a Laplace approximation, then the Kalman smoother gives $p(\mathbf z_{1:T}|\mathbf y_{1:T})$. In the M step the expected complete-data log likelihood is optimized, as in §29.8.1. Figure 29.31 shows good agreement between true and estimated $\mathbf A$ and posterior trajectory $\mathbb E[\mathbf z_t|\mathbf y_{1:T}]$ (p. 1022).

**29.11.2 Stochastic volatility.** The log-return is $y_t=\log(p_t/p_{t-1})$ for asset price $p_t$ (p. 1022):
$$y_t=\mathbf u_t^{\mathsf T}\boldsymbol\beta+\exp(z_t/2)\,r_t\tag{29.129}$$
$$z_t=\mu+\rho(z_{t-1}-\mu)+\sigma q_t\tag{29.130}$$
$$r_t\sim\mathcal N(0,1),\quad q_t\sim\mathcal N(0,1)\tag{29.131–29.132}$$
The dynamics are a first-order autoregressive (AR) process. Stationarity typically requires $|\rho|<1$. The Gaussian observation noise can be replaced by a heavy-tailed one such as a Student (p. 1022). A higher-order AR process is obtained by stacking past values into the state. For $K=2$:
$$\begin{pmatrix}z_t-\mu\\ z_{t-1}-\mu\end{pmatrix}=\begin{pmatrix}\rho_1&\rho_2\\1&0\end{pmatrix}\begin{pmatrix}z_{t-1}-\mu\\ z_{t-2}-\mu\end{pmatrix}+\begin{pmatrix}q_t\\0\end{pmatrix}\tag{29.133}$$
with $q_t\sim\mathcal N(0,\sigma_z^2)$, i.e. $z_t=\mu+\rho_1(z_{t-1}-\mu)+\rho_2(z_{t-2}-\mu)+q_t$ (29.134) (p. 1023).

**29.11.3 Inference.** Exact inference is in general hard. Approximations are Gaussian approximations (Chapter 8) and sequential Monte Carlo (Chapter 13) (p. 1023).

*Intuition note:* Keep the hidden state's linear-Gaussian structure but let the emission be a count or heavy-tailed distribution. Then exact Kalman inference no longer applies and approximations are needed, e.g. a local Gaussian (Laplace) fit of the likelihood, after which the Kalman smoother can be used (as in the spike example).

### 29.12 Structural time series models
**Goal.** Forecasting means computing $p(\mathbf y_{t+h}|\mathbf y_{1:t})$, optionally given known future inputs $\mathbf u_{1:t+h}$. STS models are defined through linear-Gaussian SSMs. Many classical methods, such as ARMA, can be represented as STS models, and STS allows nonlinear, non-Gaussian and hierarchical extensions (p. 1023).

**29.12.1 Introduction.** The scalar series is a sum of $C$ components (p. 1023):
$$f(t)=f_1(t)+\dots+f_C(t)+\epsilon_t,\quad \epsilon_t\sim\mathcal N(0,\sigma^2)\tag{29.135}$$
Each $f_c$ is a linear-Gaussian SSM, here called a dynamic linear model (DLM). They combine into one LG-SSM (p. 1023):
$$p(\mathbf z_t|\mathbf z_{t-1},\boldsymbol\theta)=\mathcal N(\mathbf z_t|\mathbf F\mathbf z_{t-1},\mathbf Q)\tag{29.136}$$
$$p(y_t|\mathbf z_t,\boldsymbol\theta)=\mathcal N(y_t|\mathbf H\mathbf z_t+\boldsymbol\beta^{\mathsf T}\mathbf u_t,\sigma_y^2)\tag{29.137}$$
$\mathbf F,\mathbf Q$ are block structured, one block per component. $\mathbf H$ sums the components' contributions. $\mathbf F,\mathbf H$ are fixed sparse matrices derived from the components, so the free parameters are $\mathbf Q$, $\sigma_y^2$ and optional $\boldsymbol\beta$ (p. 1023–1024). Vector-valued version (p. 1024):
$$p(\mathbf z_t|\mathbf z_{t-1},\boldsymbol\theta)=\mathcal N(\mathbf z_t|\mathbf F\mathbf z_{t-1},\mathbf Q),\quad p(\mathbf y_t|\mathbf z_t,\boldsymbol\theta)=\mathcal N(\mathbf y_t|\mathbf H\mathbf z_t+\mathbf D\mathbf u_t,\mathbf R)\tag{29.138–29.139}$$

**29.12.2 Building blocks.**
- *Local level* (p. 1024): $y_t=\mu_t+\epsilon_{y,t}$, $\epsilon_{y,t}\sim\mathcal N(0,\sigma_y^2)$ (29.140); $\mu_t=\mu_{t-1}+\epsilon_{\mu,t}$, $\epsilon_{\mu,t}\sim\mathcal N(0,\sigma_\mu^2)$ (29.141). With $\mu_1\sim\mathcal N(0,\sigma_\mu^2)$, the latent mean has $\mu_t\sim\mathcal N(0,t\sigma_\mu^2)$, so the variance grows with time. An AR version $\mu_t=\rho\mu_{t-1}+\epsilon_{\mu,t}$ with $|\rho|<1$ has stationary distribution $\mathcal N\big(0,\sigma_\mu^2/(1-\rho^2)\big)$, so uncertainty reaches a finite asymptote (p. 1024).
- *Local linear trend* (p. 1024): the level moves by slope $\delta_{t-1}$ (per $\Delta t=1$): $\mu_t=\mu_{t-1}+\delta_{t-1}+\epsilon_{\mu,t}$ (29.142). The slope is a random walk: $\delta_t=\delta_{t-1}+\epsilon_{\delta,t}$, $\epsilon_{\delta,t}\sim\mathcal N(0,\sigma_\delta^2)$ (29.143). Combined:
$$\begin{pmatrix}\mu_t\\ \delta_t\end{pmatrix}=\underbrace{\begin{pmatrix}1&1\\0&1\end{pmatrix}}_{\mathbf F}\begin{pmatrix}\mu_{t-1}\\ \delta_{t-1}\end{pmatrix}+\begin{pmatrix}\epsilon_{\mu,t}\\ \epsilon_{\delta,t}\end{pmatrix}\tag{29.144}$$
$$y_t=\underbrace{(1\;\;0)}_{\mathbf H}\begin{pmatrix}\mu_t\\ \delta_t\end{pmatrix}+\epsilon_{y,t}\tag{29.145}$$
 An AR slope, $\delta_t=D+\rho(\delta_{t-1}-D)+\epsilon_{\delta,t}$ (29.146), reverts to a long-run slope $D$. It is called a "semilocal linear trend" and is useful for longer-term forecasts (p. 1025).
- *Covariates* (p. 1025): $y_t=\mu_t+\boldsymbol\beta^{\mathsf T}\mathbf u_t+\epsilon_{y,t}$ (29.147). For forecasting one needs future inputs $\mathbf u_{t+h}$. A simple approach is $\mathbf u_{t+h}=\mathbf u_t$ (p. 1025). Figure 29.32a shows the graphical model of a BSTS with local linear trend and linear regression on inputs (the text calls it the local level model with covariates).
- *Seasonality* (p. 1026): offsets $s_t$ sum to zero (on average) over a cycle of $S$ steps:
$$s_t=-\sum_{k=1}^{S-1}s_{t-k}+\epsilon_{s,t},\quad\epsilon_{s,t}\sim\mathcal N(0,\sigma_s^2)\tag{29.148}$$
 For $S=4$, $s_t=-(s_{t-1}+s_{t-2}+s_{t-3})+\epsilon_{s,t}$. Stacking the last $S-1$ seasons into the state makes it first-order (Fig. 29.32b).
- *Adding it up* (S=4 case, state $\mathbf z_t=(s_t,s_{t-1},s_{t-2},\mu_t,\delta_t)^{\mathsf T}$, shape $5\times1$; $\mathbf F$ is $5\times5$) (p. 1026):
$$\mathbf z_t=\underbrace{\begin{pmatrix}-1&-1&-1&0&0\\1&0&0&0&0\\0&1&0&0&0\\0&0&0&1&1\\0&0&0&0&1\end{pmatrix}}_{\mathbf F}\mathbf z_{t-1}+\mathcal N\big(\mathbf 0,\mathrm{diag}([\sigma_s^2,0,0,\sigma_\mu^2,\sigma_\delta^2])\big)\tag{29.149}$$
 The Kalman filter gives $p(\mathbf z_t|\mathbf y_{1:t})$. Prediction rolls forward in latent space, then predicts the output:
$$p(\mathbf y_{t+1}|\mathbf y_{1:t})=\int p(\mathbf y_{t+1}|\mathbf z_{t+1})p(\mathbf z_{t+1}|\mathbf z_t)p(\mathbf z_t|\mathbf y_{1:t})\,d\mathbf z_t\tag{29.150}$$
 This is closed form, as in §8.2.2 (p. 1026).

*Intuition note:* Each component is a small hidden process with its own few lines of the $\mathbf F$ matrix. Stacking them into one big sparse matrix lets the ordinary Kalman filter handle trend, season and level together.

**29.12.3 Model fitting.** The parameters to learn are $\boldsymbol\theta=(\mathbf D,\mathbf R,\mathbf Q)$, since $\mathbf F,\mathbf H$ are fixed by the blocks and $\mathbf B=\mathbf 0$ (as printed). Methods: maximum likelihood (§29.8) or Bayesian inference (§29.8.4). The Bayesian version is Bayesian structural time series (BSTS), often with the conjugate prior $p(\boldsymbol\theta)=\mathrm{MNIW}(\mathbf R,\mathbf D)\,\mathrm{IW}(\mathbf Q)$ (29.151). With many covariates, a sparsity-promoting prior such as spike-and-slab can be used for the regression coefficients (p. 1026).

**29.12.4 Forecasting.** Estimate $\boldsymbol\theta$ on history. Use the Kalman filter to get $p(\mathbf z_t|\mathbf y_{1:t},\mathbf u_{1:t},\boldsymbol\theta)$. Roll forward to get $p(\mathbf y_{t+h}|\mathbf y_{1:t},\mathbf u_{1:t+h},\boldsymbol\theta)$. If parameters are uncertain, sample from $p(\boldsymbol\theta|\mathbf y_{1:t},\mathbf u_{1:t})$ and average the forecasts by Monte Carlo (p. 1027).

**29.12.5 Examples.**
- *Mauna Loa CO$_2$* (p. 1027): monthly data, Jan 1966–Feb 2019. The model is a local linear trend plus a seasonal part with $S=12$. It is fit by variational Bayes to all but the last 10 years. Posterior mean ± sd: $\sigma_y=0.169\pm0.008$, $\sigma_\mu=0.159\pm0.017$, $\sigma_\delta=0.009\pm0.003$, $\sigma_s=0.038\pm0.008$. Ten sampled parameter vectors give a distribution over forecasts. The two latent components (trend, current seasonal value) show the signal decomposed into two simpler signals.
- *Electricity demand, Victoria* (p. 1028–1029): hourly data, first six weeks of 2014. Four components: hourly seasonal effect (period 24), daily seasonal effect (period 7, 24 steps per season), linear regression on temperature, and an AR term on the observations. Fit by variational inference (about a minute on a GPU), with 10 posterior samples. Forecasts are reasonable but quite uncertain. Temperature regression is the most important effect. The hour-of-day effect is also quite significant after accounting for temperature. The AR term is the most uncertain, since it absorbs all residual variation beyond observation noise. *Anomaly detection*: compute the one-step-ahead predictive $p(y_t|\mathbf y_{1:t-1},\mathbf u_{1:t})=\mathcal N(\mu_t,\sigma_t^2)$ and flag points where the z-score $(y_t-\mu_t)/\sigma_t$ exceeds 3 (Fig. 29.36, p. 1029).
- *Integer sales* (p. 1028–1030): for counts, Poisson likelihood with latent demand: $y_t\sim\mathrm{Poi}(g(d_t^y))$ [SSF16; See+17], where $d_t=z_t+\mathbf u_t^{\mathsf T}\mathbf w$, $\mathbf u_t$ are seasonal/holiday covariates, and $g(d)=e^d$ or $\log(1+e^d)$. The dynamics are a random walk $z_t=z_{t-1}+\alpha\mathcal N(0,1)$. A zero count may mean "out of stock", not "no demand". If this is ignored, one may infer $z_t=0$ and underestimate demand. One remedy is the zero-inflated Poisson: $p(y_t|d_t)=p_0\mathbb I(y_t=0)+(1-p_0)\mathrm{Poi}(y_t|e^{d_t})$, where $p_0$ is the probability of the first mixture component. Negative binomial likelihoods (possibly zero-inflated) are also common. Their disadvantage: they are not log-concave (for $d_t=0$, as printed), which complicates inference. The Laplace approximation is then a poor choice since it may find a saddle point. [SSF16] use a log-concave multi-stage likelihood. $y_t=0$ is emitted with probability $\sigma(d_t^0)$; otherwise $y_t=1$ with probability $\sigma(d_t^1)$; otherwise the count is emitted with probability $\mathrm{Poi}(d_t^2)$ (p. 1030).
- *Hierarchical SSM for electoral panel data* (p. 1030–1031): $N_t^j$ voters in state $j$ at time $t$, of which $y_t^j$ vote Democrat. A national chain $\mathbf z_t^0$ models national trends. State chains $\mathbf z_t^j$ model local "random effects" (Fig. 29.38):
$$y_t^j\sim\mathrm{Bin}(y_t^j|\pi_t^j,N_t^j),\quad \pi_t^j=\sigma\big[(\mathbf z_t^0)^{\mathsf T}\mathbf u_t^0+(\mathbf z_t^j)^{\mathsf T}\mathbf u_t^j\big]\tag{29.152–29.153}$$
$$\mathbf z_t^0=\mathbf z_{t-1}^0+\mathcal N(\mathbf 0,\sigma^2\mathbf I),\quad \mathbf z_t^j=\mathbf z_{t-1}^j+\mathcal N(\mathbf 0,\tau^2\mathbf I)\tag{29.154–29.155}$$

**29.12.6 Causal impact of a time series intervention.** The data are "quasi-experimental": collected under an intervention but without random assignment. Example: click-through rate $y_t$; an ad campaign launches at time $n$; $\mathbf y_{1:n}$ is observed before and $\mathbf y_{n+1:m}$ after (an interrupted time series). The counterfactual question is what the CTR would have been without the campaign. If the counterfactual series $\tilde{\mathbf y}_{n+1:m}$ can be predicted, comparing it with the actual $y_t$ estimates the causal impact (p. 1031). Following [Bro+15], an STS model is an LG-SSM whose arrows follow the arrow of time, so it is a structural causal model. One infers the noise variables from the data, "rolls back time" to the intervention, and rolls forward in a new copy (twin network, §4.7.4) (p. 1031).

*29.12.6.1 Computing the counterfactual (p. 1032–1033).* In Figure 29.39, $n=2$, $m=4$. Observations $\mathbf y_{1:2}$ come before and $\mathbf y_{3:4}$ after. The states have exogenous noise (unmodeled factors) and there are exogenous covariates $\mathbf x_{1:m}$. In the real world, incoming arcs to $\mathbf z_3$ are cut. In the counterfactual world ($\tilde a=0$), the distributions stay as in the past. The goal is
$$p(\tilde{\mathbf y}_{n+1:m}|\mathbf y_{1:n},\mathbf x_{1:m})=\int p(\tilde{\mathbf y}_{n+1:m}|\tilde{\mathbf z}_{n+1:m},\mathbf x_{n+1:m},\boldsymbol\theta)\,p(\tilde{\mathbf z}_{n+1:m}|\mathbf z_n,\boldsymbol\theta)\,p(\mathbf z_n,\boldsymbol\theta|\mathbf x_{1:n},\mathbf y_{1:n})\,d\boldsymbol\theta\,d\mathbf z_n\,d\tilde{\mathbf z}_{n+1:m}\tag{29.156–29.157}$$
$$p(\mathbf z_n,\boldsymbol\theta|\mathbf x_{1:n},\mathbf y_{1:n})=p(\mathbf z_n|\mathbf x_{1:n},\mathbf y_{1:n},\boldsymbol\theta)\,p(\boldsymbol\theta|\mathbf x_{1:n},\mathbf y_{1:n})\tag{29.158}$$
For LG-SSMs the first factor comes from Kalman filtering. The second comes from MCMC or variational inference (p. 1032). With posterior samples $i$, the per-step treatment effect is $\tau_t^i=y_t-\tilde y_t^i$ and the cumulative impact is $\sigma_t^i=\sum_{s=n+1}^{t}\tau_s^i$. Uncertainty includes epistemic (parameters) and aleatoric (system and observation noise) parts (p. 1033).

*29.12.6.2 Assumptions (p. 1033).* (1) Predictability: the model predicts the outcome adequately (check by backcasting on historical data). (2) Unaffectedness: the intervention does not change future covariates $\mathbf x_{n+1:m}$ (can potentially be checked by running the method with each covariate as outcome). (3) Stability: without intervention, the pre-treatment model would have continued after treatment (check whether an effect is predicted if the treatment is shifted earlier).

*29.12.6.3 Example (p. 1034).* Local level with a linear covariate term:
$$y_t=\mu_t+\boldsymbol\beta^{\mathsf T}\mathbf x_t+\mathcal N(0,\sigma_y^2),\quad \mu_t=\mu_{t-1}+\delta_{t-1}+\mathcal N(0,\sigma_\mu^2),\quad \delta_t=\delta_{t-1}+\mathcal N(0,\sigma_\delta^2)\tag{29.159–29.161}$$
Static parameters: $\boldsymbol\theta=(\boldsymbol\beta,\sigma_y^2,\sigma_\mu^2,\sigma_\delta^2)$. Synthetic data: $x_t$ from an AR process, $y_t=1.2x_t+\epsilon_t$; at $t=70$ the $y_t$ values are increased by 10. The forecast $\tilde y_t$ for $t\ge70$ follows the pre-intervention trend, and the posterior pointwise impact $\tau_t=y_t-\tilde y_t$ is about 10 for $t\ge70$ (Fig. 29.41).

*29.12.6.4 Synthetic control (p. 1034).* $\boldsymbol\beta^{\mathsf T}\mathbf x_t$ over "donor" series resembles synthetic control, but it is not restricted to convex combinations. With many covariates, spike-and-slab or horseshoe priors select relevant ones. STS also works if only $y_t$ is observed.

*Intuition note:* Fit the model only on "before" data, then forecast "after" as if nothing happened. The gap between that forecast and reality is the estimated effect. The method's validity is based on the three assumptions.

**29.12.7 Prophet (p. 1035).** Prophet is a generalized additive model:
$$y(t)=g(t)+s(t)+h(t)+\mathbf w^{\mathsf T}\mathbf x(t)+\epsilon_t\tag{29.162}$$
$g$ = trend, $s$ = seasonal (linear regression on a sinusoidal basis), $h$ = optional sparse holiday effects, $\mathbf x(t)$ = optional covariates, $\epsilon$ = iid Gaussian. It is a regression model, not autoregressive: it predicts from the time stamp and covariates, not past $y$. The trend is piecewise linear with $S$ uniformly spaced changepoints:
$$g(t)=(k+\mathbf a(t)^{\mathsf T}\boldsymbol\delta)\,t+(m+\mathbf a(t)^{\mathsf T}\boldsymbol\gamma)\tag{29.163}$$
$k$ = growth rate, $m$ = offset, $a_j(t)=\mathbb I(t\ge s_j)$, $\gamma_j=-s_j\delta_j$ for continuity, and $\delta$ has a Laplace($\tau$) prior, so the MAP estimate is sparse (the change across a changepoint is usually 0).

**29.12.8 Neural forecasting (p. 1035–1036).** Classical methods work well with little data. With much data (one long sequence, or many related sequences) neural nets are natural. They were until recently not competitive with classical methods, but this has started to change.
- *ES-RNN*: a hybrid that won the 2019 M4 competition. Exponential smoothing adapts to the local series. The RNN learns nonlinear components across related series ("local+global") (p. 1035).
- *DeepSSM* [Ran+18]: one RNN with shared parameters $\boldsymbol\phi$ predicts SSM parameters, $\boldsymbol\theta_t^n=f(\mathbf c_{1:T}^n;\boldsymbol\phi)$. The Kalman filter gives $L_n=\log p(\mathbf x_{1:T}^n|\mathbf c_{1:T}^n,\boldsymbol\theta_{1:T}^n)$. Training maximizes $\sum_n L_n$ end to end (p. 1035–1036).
- *Deep Factors*: weighted sum of a global neural series and a local stochastic model (SSM or GP). *DeepGLO*: matrix-factorization global model plus temporal convolutional networks (p. 1036).
- *N-BEATS*: residual network predicting weights of basis functions (polynomial trend, periodic signal). *DeepAR*: one RNN over many series; the original used a negative binomial likelihood, which is unimodal. Mixtures of Gaussians have also been proposed (p. 1036).
- *Quantile regression* with the pinball loss. *SQF-RNN* represents the quantile function by splines and trains with CRPS:
$$\mathrm{CRPS}(F^{-1},y)=\int_0^1 2\,\ell_\alpha\big(y,F^{-1}(\alpha)\big)\,d\alpha$$
 where $\ell_\alpha$ is the pinball loss (Eq. 14.53). CRPS is a proper scoring rule, less sensitive to outliers and more "distance aware" than log loss. For deterministic predictions it reduces to absolute error (p. 1036).
- For multiple simultaneous observations, copulas model dependence (low-rank Gaussian; nonparametric). *MQ-CNN* predicts quantiles for several steps ahead with dilated causal convolutions (or an RNN). [WT19] extend it to take the quantile level $\alpha$ as input (p. 1036).

### 29.13 Deep SSMs (p. 1036–1041)
Deep SSMs (dynamical variational autoencoders) allow nonlinear and/or non-Markovian neural dynamics and/or observation models. Observations are written $\mathbf x_t$ (p. 1036–1037).

**29.13.1 Deep Markov models (DMM)** (stochastic RNN): neural dynamics and/or observation model, fit by SVI (p. 1037). The exact posterior, using $\mathbf z_t\perp\mathbf x_{1:t-1}\,|\,\mathbf z_{t-1}$ (with $p(\mathbf z_1|\mathbf z_0,\mathbf x_{1:T})=p(\mathbf z_1|\mathbf x_{1:T})$):
$$p(\mathbf z_{1:T}|\mathbf x_{1:T})=\prod_{t=1}^T p(\mathbf z_t|\mathbf z_{t-1},\mathbf x_{1:T})=\prod_{t=1}^T p(\mathbf z_t|\mathbf z_{t-1},\mathbf x_{t:T})\tag{29.164}$$
It is intractable, so an inference network $q$ is used. Option 1: fully factorized causal $q(\mathbf z_{1:T}|\mathbf x_{1:T})=\prod_t q(\mathbf z_t|\mathbf x_{1:t})$, with $\mathbf x_{1:t}$ summarized in an RNN state $\mathbf h_t$ (Fig. 29.42a). It works online. Option 2 (offline training, more accurate), where $\mathbf x_{1:t-1}$ is already captured by $\mathbf z_{t-1}$ and future $\mathbf x_{t:T}$ is summarized by a backwards RNN (Fig. 29.42b):
$$q(\mathbf z_{1:T}|\mathbf x_{1:T})=\prod_t q(\mathbf z_t|\mathbf z_{t-1},\mathbf x_{t:T})\tag{29.165}$$
$$q(\mathbf z_{1:T},\mathbf h_{1:T}|\mathbf x_{1:T})=\prod_{t=T}^{1}\mathbb I(\mathbf h_t=f(\mathbf h_{t+1},\mathbf x_t))\prod_{t=1}^T q(\mathbf z_t|\mathbf z_{t-1},\mathbf h_t)\tag{29.166}$$
ELBO for fully factored $q$ (p. 1038):
$$\log p(\mathbf x_{1:T})=\log\Big[\sum_{\mathbf z_{1:T}}p(\mathbf x_{1:T}|\mathbf z_{1:T})p(\mathbf z_{1:T})\Big]\tag{29.167}$$
$$=\log\mathbb E_{q(\mathbf z_{1:T})}\Big[p(\mathbf x_{1:T}|\mathbf z_{1:T})\frac{p(\mathbf z_{1:T})}{q(\mathbf z_{1:T})}\Big]\tag{29.168}$$
$$=\log\mathbb E_{q(\mathbf z_{1:T})}\Big[\prod_{t=1}^T\frac{p(\mathbf x_t|\mathbf z_t)p(\mathbf z_t|\mathbf z_{t-1})}{q(\mathbf z_t)}\Big]\tag{29.169}$$
$$\ge\mathbb E_{q(\mathbf z_{1:T})}\Big[\sum_{t=1}^T\log p(\mathbf x_t|\mathbf z_t)+\log p(\mathbf z_t|\mathbf z_{t-1})-\log q(\mathbf z_t)\Big]\tag{29.170}$$
$$=\sum_{t=1}^T\mathbb E_{q(\mathbf z_t)}[\log p(\mathbf x_t|\mathbf z_t)]-\mathbb E_{q(\mathbf z_{t-1})}\big[D_{\mathrm{KL}}(q(\mathbf z_t)\,\|\,p(\mathbf z_t|\mathbf z_{t-1}))\big]\tag{29.171}$$
(added step) The step to (29.170) is an inequality that moves the log inside the expectation (Jensen's inequality); the author gives no comment on it. If the variational posteriors are jointly Gaussian, the reparameterization trick gives stochastic ELBO gradients, and the KL term (Gaussian prior) is analytic (p. 1038).

*Intuition note:* The ELBO has two kinds of terms per step: reconstruct $\mathbf x_t$ from $\mathbf z_t$, and keep the posterior over $\mathbf z_t$ close to what the dynamics predict from $\mathbf z_{t-1}$.

**29.13.2 Recurrent SSM (RSSM).** Long-range dependence is added through a deterministic state $\mathbf h_t=f(\mathbf h_{t-1},\mathbf z_t)$, which records all stochastic choices. First, $p(\mathbf x_t|\mathbf h_t)$ makes the observation depend on $\mathbf z_{1:t}$ (Fig. 29.43a). Second, replacing $p(\mathbf z_t|\mathbf z_{t-1})$ by $p(\mathbf z_t|\mathbf h_{t-1})$ makes the prior depend on $\mathbf z_{1:t-1}$ (Fig. 29.43b). This is the recurrent SSM. Its inference network is like the DMM's, with a standard forwards RNN (p. 1038).

**29.13.3 Improving multistep predictions.** In the ELBO (Fig. 29.44a), the dynamics model $p(\mathbf z_t|\mathbf z_{t-1})$ is only penalized by its difference from the one-step-ahead posterior $q(\mathbf z_t)$. This can hurt long-term prediction (p. 1039). *Observation overshooting* [Amo+18] predicts several steps forward with the dynamics and adds reconstruction errors on future observations (Fig. 29.44b). Faster, *latent overshooting* [Haf+19] works in latent space. Repeated transitions give $p(\mathbf z_t|\mathbf z_{t-d})$, and (p. 1039–1040)
$$\log p_d(\mathbf x_{1:T})\triangleq\log\int\prod_{t=1}^T p(\mathbf z_t|\mathbf z_{t-d})p(\mathbf x_t|\mathbf z_t)\,d\mathbf z_{1:T}\tag{29.172}$$
$$\ge\sum_{t=1}^T\mathbb E_{q(\mathbf z_t)}[\log p(\mathbf x_t|\mathbf z_t)]-\mathbb E_{p(\mathbf z_{t-1}|\mathbf z_{t-d})q(\mathbf z_{t-d})}\big[D_{\mathrm{KL}}(q(\mathbf z_t)\,\|\,p(\mathbf z_t|\mathbf z_{t-1}))\big]\tag{29.173}$$
Averaging over horizons $1\le d\le D$, and for computational reasons averaging only the KL terms with weights $\beta_d$:
$$\frac1D\sum_{d=1}^D\log p_d(\mathbf x_{1:T})\ge\sum_{t=1}^T\mathbb E_{q(\mathbf z_t)}[\log p(\mathbf x_t|\mathbf z_t)]-\frac1D\sum_{d=1}^D\beta_d\,\mathbb E_{p(\mathbf z_{t-1}|\mathbf z_{t-d})q(\mathbf z_{t-d})}\big[D_{\mathrm{KL}}(q(\mathbf z_t)\|p(\mathbf z_t|\mathbf z_{t-1}))\big]\tag{29.174–29.175}$$

**29.13.4 Variational RNNs (VRNN)** [Chu15]. Hidden states depend on all past hidden states and all past observations. The model is more expressive but slower for forecasting, since unrolling needs generated $\mathbf x_{t+1},\mathbf x_{t+2},\dots$ to feed the hidden states. This makes it less useful for forecasting and model-based RL (p. 1040). Generative model:
$$p(\mathbf x_{1:T},\mathbf z_{1:T},\mathbf h_{1:T})=\prod_{t=1}^T p(\mathbf z_t|\mathbf h_{t-1},\mathbf x_{t-1})\,\mathbb I\big(\mathbf h_t=f(\mathbf h_{t-1},\mathbf x_{t-1},\mathbf z_t)\big)\,p(\mathbf x_t|\mathbf h_t)\tag{29.176}$$
with $p(\mathbf z_1|\mathbf h_0,\mathbf x_0)=p(\mathbf z_0)$ and $\mathbf h_1=f(\mathbf z_1)$ (as printed). So $\mathbf h_t=(\mathbf z_{1:t},\mathbf x_{1:t-1})$. The latent prior is $p(\mathbf z_t|\mathbf z_{1:t-1},\mathbf x_{1:t-1})$, versus $p(\mathbf z_t|\mathbf z_{t-1})$ in a DMM and $p(\mathbf z_t|\mathbf z_{1:t-1})$ in an RSSM (p. 1041). Training uses SVI with
$$q(\mathbf z_{1:T},\mathbf h_{1:T}|\mathbf x_{1:T})=\prod_t\mathbb I\big(\mathbf h_t=f(\mathbf h_{t-1},\mathbf z_{t-1},\mathbf x_t)\big)\,q(\mathbf z_t|\mathbf h_t)\tag{29.177}$$
Here $\mathbf h_t=(\mathbf z_{1:t-1},\mathbf x_{1:t})$, giving the filtered posterior $\prod_t q(\mathbf z_t|\mathbf z_{1:t-1},\mathbf x_{1:t})$. Replacing $\mathbf x_t$ by a bidirectional-RNN output gives a smoothed posterior $\prod_t q(\mathbf z_t|\mathbf z_{1:t-1},\mathbf x_{1:T})$. [DF18] used this for simple videos (stochastic video generation, SVG). [Vil+19] scaled it up with simpler but larger architectures (p. 1041).

## Toy example (ours, not from the text)
Counterfactual impact with a local-level model. Assume $\sigma_\mu^2=1$, $\sigma_y^2=1$, no covariates. At the intervention time $n$ the filtered posterior is $\mu_n\sim\mathcal N(10,1)$, from pre-intervention data.
- Forecast $h=1$: $\tilde\mu_{n+1}$ has mean 10 and variance $1+1=2$. The predictive for $\tilde y_{n+1}$ has mean 10 and variance $2+1=3$ (sd $\sqrt3\approx1.732$).
- Forecast $h=2$: $\tilde\mu_{n+2}$ has variance $2+1=3$; $\tilde y_{n+2}$ has mean 10 and variance 4 (sd 2). (Here we ignore any observations after $n$, as the counterfactual does.)
- Suppose actual $y_{n+1}=15$, $y_{n+2}=16$. Pointwise effect at the mean forecast: $\tau_{n+1}=15-10=5$, $\tau_{n+2}=16-10=6$. Cumulative effect at the mean forecast: $5+6=11$.
- Z-scores: $5/1.732\approx2.89$ and $6/2=3.0$. Neither exceeds 3, so these are not "improbable" under a rough analogue of the Fig. 29.36 rule (which actually uses one-step-ahead predictives given past data), even though the cumulative effect is large. Predictive sd grows with horizon (1.73, then 2), so the evidence per step is modest.
- The estimate is valid only under predictability, unaffectedness and stability (p. 1033).

## Concepts
- [[structural-time-series]] (new) — observed series as a sum of linear-Gaussian latent components; one LG-SSM with sparse $\mathbf F,\mathbf H$ (p. 1023)
- [[local-level-model]] (new) — latent mean follows a random walk (or AR); observation = mean + noise (p. 1024)
- [[local-linear-trend]] (new) — level plus slope, both random walks; $\mathbf F=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ (p. 1024)
- [[seasonal-component]] (new) — offsets constrained to sum to zero over $S$ steps; stacked into state (p. 1026)
- [[bayesian-structural-time-series]] (new) — STS with Bayesian parameter inference, e.g. MNIW/IW prior (p. 1026)
- [[non-gaussian-ssm]] (new) — SSM with non-Gaussian transition/observation noise (p. 1021)
- [[zero-inflated-poisson]] (new) — mixture of point mass at 0 and Poisson; for out-of-stock zeros (p. 1030)
- [[causal-impact-sts]] (new) — counterfactual forecast from a twin-network STS; effect = actual − predicted (p. 1031–1033)
- [[crps]] (new) — integral of pinball loss over quantile levels; proper scoring rule (p. 1036)
- [[deep-markov-model]] (new) — SSM with neural dynamics/observation, fit by SVI (p. 1037)
- [[recurrent-ssm]] (new) — deterministic $\mathbf h_t$ added so $\mathbf x_t$ depends on $\mathbf z_{1:t}$ and the prior on $\mathbf z_t$ depends on $\mathbf z_{1:t-1}$ (p. 1038)
- [[latent-overshooting]] (new) — averaging multistep KL terms with weights $\beta_d$ to improve long-horizon prediction (p. 1040)
- [[variational-rnn]] (new) — hidden state depends on past $\mathbf x$ and $\mathbf z$ (p. 1040)
- [[variational-inference-elbo]] — ELBO used to train deep SSMs (p. 1038)
- [[kl-divergence]] — penalizes mismatch of $q(\mathbf z_t)$ and the predicted prior (p. 1038)
- [[hierarchical-multilevel-model]] — national chain plus state chains (p. 1030)
- [[posterior-predictive-distribution]] — forecasts $p(\mathbf y_{t+h}|\mathbf y_{1:t})$ (p. 1027)
- [[structural-causal-model]] — STS read as an SCM (p. 1031)

## Canonical instances
- [[poisson-lds-spike-trains]] — 2-d rotation dynamics with 5 Poisson emissions; EM + Laplace + Kalman smoother (p. 1022)
- [[stochastic-volatility-model]] — AR(1) log-volatility driving return noise (p. 1022)
- [[mauna-loa-co2-sts]] — local linear trend + $S=12$ seasonality (p. 1027)
- [[victoria-electricity-sts]] — four-component STS; anomaly detection (p. 1028)
- [[demand-forecasting-zip]] — sales counts with out-of-stock zeros (p. 1030)
- [[electoral-panel-hierarchical-ssm]] — binomial survey data, national and state chains (p. 1030)
- [[causal-impact-simulation]] — +10 shift at $t=70$ recovered (p. 1034)

## Bridges (candidates)
- [same-math] STS as one LG-SSM ↔ Kalman filtering: forecasts via filter then roll-forward (29.150).
- [same-math] DMM/RSSM ELBO (29.171) ↔ variational inference: standard ELBO with reconstruction and KL terms.
- [structural-analogy] Causal-impact counterfactual forecast ↔ potential outcomes: treated unit's untreated outcome is the missing quantity, here predicted by a model.
- [structural-analogy] Local-level shrinkage of noisy observations ↔ partial pooling: estimate balances prior dynamics and data.
- [metaphor] Latent overshooting ↔ model-based RL planning horizons: training for multi-step rollouts.

## Questions this raises
- How reliable are the stability and unaffectedness assumptions in real interventions, and how well do the proposed checks detect violations?
- When is a Laplace approximation to a non-log-concave count likelihood unreliable, and what do multi-stage likelihoods trade away?
- Does latent overshooting with weights $\beta_d$ change the meaning of the ELBO as a bound on $\log p(\mathbf x_{1:T})$?
- When do neural forecasters beat STS on short series, and how should the hybrid local+global methods be compared with classical ones?

## Reading notes
- This is part 3/3 of Chapter 29. It starts at the end of §29.10 (Fig. 29.30, §29.10.2, printed p. 1021) and ends with §29.13.4 (printed p. 1041). pdf 1076 (printed 1042) is blank. Offset: printed = pdf − 34. Split at a section boundary.
- Notation clashes in the source: $\mathbf D$ is the input matrix in (29.139), the regression coefficients in §29.12.3, and the long-run slope in (29.146). $\boldsymbol\theta=(\mathbf D,\mathbf R,\mathbf Q)$ with "$\mathbf B=\mathbf 0$" differs from $\boldsymbol\theta$ in (29.137) and from $\boldsymbol\beta$ in (29.147).
- Probable misprints: "$\delta_t\sim$ Laplace($\tau$)" in Prophet (index likely $j$); "$y_t=$ is emitted with probability Poi($d_t^2$)" has a missing value; Fig. 29.44 caption "but does need to care about future observations" likely means "does not"; "$q(\mathbf z_t|\mathbf x_{1:t-1},\mathbf x_{1:t})$" in §29.13.2 as printed; "determiistic" and "Calro" typos; "yt∼Poi(yt|g(dyt))" printed with $d_t^y$ though $d_t$ is defined. (29.177) lacks a closing parenthesis after $\mathbf x_t$ in the printed indicator (both in the text layer and in the image).
- Equation (29.171) is printed with $q(\mathbf z_t)$ in a fully factored form. The text layer was readable; all equations were checked against the images.
- Many methods (Prophet, M4 winners, DeepAR etc.) are only described briefly with citations; details are not in these pages.
