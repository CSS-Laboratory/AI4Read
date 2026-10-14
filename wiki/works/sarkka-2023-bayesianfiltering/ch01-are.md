---
id: sarkka-2023-bayesianfiltering/ch01-are
work: sarkka-2023-bayesianfiltering
unit: "1 What Are Bayesian Filtering and Smoothing?"
pages: 1-16
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
# What Are Bayesian Filtering and Smoothing?

## L0 — One line
Bayesian filtering and smoothing estimate a hidden, time-varying state from noisy measurements. They do this by computing marginal posterior distributions, with a constant amount of work per time step, instead of the intractable full joint posterior.

## L1 — The gist (≤ 120 words)
The chapter asks how to estimate a hidden state that evolves in time and is seen only through noisy measurements. Writing the problem as Bayes' rule over all states gives the full joint posterior. That posterior must be recomputed with every new measurement, and its dimension grows with the number of time steps. The authors restrict the model to a Markov sequence and compute only marginals: filtering, prediction and smoothing distributions. Each costs a constant amount of work per time step. The chapter also surveys applications, the history from the Wiener filter to the Kalman filter, families of algorithms, and how unknown parameters are handled. The full joint posterior of states and parameters cannot be computed; the authors call this the price of constant work per time step.

**Prerequisites:** Bayes' rule; conditional and marginal distributions; Markov property; Gaussian distribution; the idea of a dynamic system with a state vector.

## L2 — Key ideas (5–10 bullets)
- Optimal filtering means estimating a system's state from indirect noisy measurements. "Optimal" means statistically optimal, and the authors use "Bayesian filtering" for the same thing. Smoothing also reconstructs earlier states (p. 1).
- Process noise usually models uncertainty in the dynamics; the system is usually not truly random (p. 1). Applications run from GPS and tracking to robotics, brain imaging, epidemics, telecommunications and stochastic optimal control (pp. 2–7).
- Optimal recursive estimation began with least squares for linear systems. Wiener's filter works only for stationary signals; Kalman's recursive filter was then found to be a Bayesian filter (pp. 7–8).
- The full joint posterior $p(\mathbf x_{0:T}\mid \mathbf y_{1:T})$ must be recomputed at each new measurement. Its dimension grows, so it becomes intractable (p. 10).
- The fix is a Markov state space model, eq. (1.3), plus marginals only: filtering (1.4), prediction (1.5), smoothing (1.6). These need a constant number of computations per time step (pp. 10–11).
- Closed-form solutions exist for linear Gaussian and finite-state problems. Otherwise one uses approximations: extended and unscented Kalman filters (EKF, UKF), particle, grid-based and others (pp. 13–14).
- Unknown parameters get a prior. The filter's by-products give $p(\boldsymbol\theta\mid\mathbf y_{1:T})$ (1.8), but the full joint of states and parameters stays intractable (p. 15).

## L3 — Walkthrough

### Introduction (p. 1)
- **Optimal filtering** estimates the state of a time-varying system observed indirectly through noisy measurements. "Optimal" means statistically optimal. "Bayesian filtering" is the Bayesian formulation, and the book uses the terms interchangeably (p. 1).
- The **state** is the collection of dynamic variables (position, velocity, orientation, angular velocity) that fully describe the system. Measurement noise means measurements are not deterministic functions of the state, even if the true state were known (p. 1).
- The state evolves as a dynamic system perturbed by **process noise**, which models uncertainty in the dynamics. In most cases the system is not truly stochastic; stochasticity represents model uncertainty (p. 1).
- Basic filters estimate the current state from the measurement history. **Smoothers** also reconstruct states from before the current time (p. 1).

### 1.1 Applications (pp. 2–7)
The authors list time-varying systems of this type, each with a short description.
- **GPS:** the receiver measures signal arrival times and typically uses an EKF or another optimal filter for position and velocity. Footnote: the EKF is strictly only approximate, since it uses a Taylor-series Gaussian approximation to the non-Gaussian optimal solution (p. 2).
- **Target tracking** with radars and other sensors. **Multiple target tracking** adds data association (which measurement came from which target?) and estimation of the number of targets (p. 3).
- **Inertial navigation** uses accelerometers and gyroscopes (p. 3).
- **Integrated inertial navigation** combines unbiased but inaccurate sensors with biased but locally accurate inertial sensors. It was used, for example, in the Apollo 11 lunar module guidance (p. 4).
- **GPS/INS** lets inertial sensors compensate short-term GPS fluctuations, and GPS compensates inertial biases. It can also switch temporarily to pure inertial navigation when there is no GPS fix (pp. 4–5).
- **Robotics** uses simultaneous localization and mapping (SLAM): the environment is typically unknown, so its map also needs to be generated during localization. Methods include EKFs and particle filters (p. 5).
- **Brain imaging** (EEG, MEG, fMRI, DOT) uses minimum norm estimates, which can be read in the Bayesian sense as estimating the field with a certain prior structure from Gaussian observations. This is equivalent to statistical inversion or generalized Gaussian process regression. Adding dynamical priors gives spatio-temporal problems solvable with Kalman filters and smoothers (p. 5).
- **Infectious diseases** and **biological processes** are modeled as differential equations. Adding uncertainty and imperfect measurements gives filtering problems (pp. 5–6).
- **Telecommunications:** the Viterbi algorithm can be seen as computing the maximum a posteriori (MAP) smoothing solution of a hidden Markov model (HMM). **Audio** restoration uses time-varying autoregressive models (p. 6).
- **Stochastic optimal control:** besides statistical optimality, "optimal" means the control minimizes a performance cost (e.g. fuel). Because the state is usually observed through sensors, filters are needed to reconstruct it (pp. 6–7).
- **Learning systems** relate to Bayesian non-parametrics and Gaussian process regression. **Physical systems** give time-varying inverse problems, for which filters and smoothers are the Bayesian solutions (p. 7).

### 1.2 Origins (pp. 7–8)
- Optimal recursive estimators were first built for linear systems because of their simplicity, with least squares as the natural criterion. For linear systems the MMSE Bayesian solution coincides with least squares: the optimal least squares solution is exactly the posterior mean (p. 7).
- The **Wiener filter** (1950) is a frequency-domain least squares solution for stationary Gaussian signals. Its disadvantage is that it applies only to stationary signals (p. 7).
- **Kalman (1960b)** gave a recursive solution for discrete-time linear filtering. One reason for its success is that it needs much lighter mathematics than the Wiener filter. The Kalman–Bucy filter contains the Wiener filter as a limiting special case (p. 8).
- Soon afterwards the Kalman filter was found to be a Bayesian filter, and Bayesian smoothers (Rauch and others) followed. Stratonovich worked on the probabilistic approach in Russia in parallel (p. 8).
- Kalman filtering and dynamic linear models (DLM) are equivalent, though derived from different starting points. The book takes the Kalman filtering viewpoint because of its link to stochastic optimal control. Kalman also contributed to linear quadratic Gaussian (LQG) regulators (p. 8).
- The same equations follow from pure Bayesian analysis, not only from least squares (p. 8).

### 1.3 Optimal filtering and smoothing as Bayesian inference (pp. 9–11)
**Setting.** The unknown is a vector time series $\{\mathbf x_0,\mathbf x_1,\dots\}$ observed through noisy $\{\mathbf y_1,\mathbf y_2,\dots\}$ (Fig. 1.5, p. 9).
- **Example (Figs 1.6–1.9):** a noisy resonator with known angular velocity. The state is $\mathbf x_k=(x_k\ \dot x_k)^{\mathsf T}$, 2D (position and its time derivative). The measurement $y_k$ is a scalar noisy observation of position (p. 9).

**Full posterior.** The goal is $\mathbf x_{0:T}$ from $\mathbf y_{1:T}$, via Bayes' rule (p. 10):
$$p(\mathbf x_{0:T}\mid \mathbf y_{1:T})=\frac{p(\mathbf y_{1:T}\mid \mathbf x_{0:T})\,p(\mathbf x_{0:T})}{p(\mathbf y_{1:T})}\tag{1.1}$$
- $p(\mathbf x_{0:T})$ is the prior defined by the dynamic model.
- $p(\mathbf y_{1:T}\mid \mathbf x_{0:T})$ is the likelihood.
- $p(\mathbf y_{1:T})$ is the normalization constant:
$$p(\mathbf y_{1:T})=\int p(\mathbf y_{1:T}\mid \mathbf x_{0:T})\,p(\mathbf x_{0:T})\,\mathrm d\mathbf x_{0:T}\tag{1.2}$$

**Problem.** Each new measurement requires recomputing the full posterior. As steps accumulate, its dimension and the cost of one step grow, so computation eventually becomes intractable however much computing power exists. Without extra information or restrictive approximations there is no way around this (p. 10).

**Remedy.** Settle for selected marginals (this makes computation "an order of magnitude lighter") and restrict to probabilistic Markov sequences (p. 10). The model has three parts (pp. 10–11):
- an initial distribution $p(\mathbf x_0)$;
- a dynamic model, the transition distribution $p(\mathbf x_k\mid\mathbf x_{k-1})$;
- a measurement model $p(\mathbf y_k\mid\mathbf x_k)$.

$$\mathbf x_0\sim p(\mathbf x_0),\quad \mathbf x_k\sim p(\mathbf x_k\mid\mathbf x_{k-1}),\quad \mathbf y_k\sim p(\mathbf y_k\mid\mathbf x_k)\tag{1.3}$$

**Marginals considered** (Fig. 1.7, p. 12; p. 11):
- Filtering: $p(\mathbf x_k\mid\mathbf y_{1:k}),\ k=1,\dots,T$ (1.4).
- Prediction: $p(\mathbf x_{k+n}\mid\mathbf y_{1:k}),\ n=1,2,\dots$ (1.5). It is computed with the prediction step of the Bayesian filter.
- Smoothing: $p(\mathbf x_k\mid\mathbf y_{1:T})$, with $T>k$ (1.6).

All three need only a constant number of computations per time step, so arbitrarily long series can be processed (p. 11). In Figs 1.8–1.9 the estimates are means of the filtering and smoothing distributions, with 95% quantiles (pp. 12–13).

*Intuition note:* Asking for the whole trajectory's posterior forces you to redo everything as data grow. Asking only "where is the state now (or at step $k$)?" needs only a constant number of computations per time step. You give up the joint distribution of all times.

### 1.4 Algorithms (pp. 12–14)
- **Closed form:** the Kalman filter (KF) for linear Gaussian filtering, where the posterior is exactly Gaussian. The Rauch–Tung–Striebel smoother (RTSS) is its smoother. Finite-state filters and smoothers solve HMMs with finite state spaces (p. 13).
- The exact equations are generally intractable, so approximations were developed (pp. 13–14):
  - EKF: linearization by Taylor series, giving a Gaussian approximation to the filtering distribution; ERTSS is its smoother.
  - UKF: unscented transform, also Gaussian; URTSS is its smoother.
  - Particle filters and smoothers (sequential Monte Carlo): a weighted set of samples. The unscented particle filter and local linearization methods use UKFs and EKFs to approximate the optimal importance distributions.
  - Rao–Blackwellized particle filters: closed-form integration for some state variables, Monte Carlo for others.
  - Grid-based methods: discrete distributions on a finite grid.
  - Others: Gaussian mixtures, series expansions, variational Bayes, batch Monte Carlo (MCMC), and more.

### 1.5 Parameter estimation (pp. 14–15)
- Models often contain unknown parameters $\boldsymbol\theta$ (e.g. the resonator frequency, noise variances). Formally they can be added to the state, but in practice it is often useful to treat them separately (p. 14).
- In the Bayesian setting they get a prior and become random variables (p. 14):
$$\boldsymbol\theta\sim p(\boldsymbol\theta),\quad \mathbf x_0\sim p(\mathbf x_0\mid\boldsymbol\theta),\quad \mathbf x_k\sim p(\mathbf x_k\mid\mathbf x_{k-1},\boldsymbol\theta),\quad \mathbf y_k\sim p(\mathbf y_k\mid\mathbf x_k,\boldsymbol\theta)\tag{1.7}$$
- The full joint posterior $p(\mathbf x_{0:T},\boldsymbol\theta\mid\mathbf y_{1:T})$ is even harder than the states-only joint, so it is intractable (p. 15).
- A filter run with fixed $\boldsymbol\theta$ yields $p(\mathbf y_k\mid\mathbf y_{1:k-1},\boldsymbol\theta)$ as side products. With $p(\mathbf y_1\mid\mathbf y_{1:0},\boldsymbol\theta)\triangleq p(\mathbf y_1\mid\boldsymbol\theta)$ (p. 15):
$$p(\boldsymbol\theta\mid\mathbf y_{1:T})\propto p(\boldsymbol\theta)\prod_{k=1}^{T}p(\mathbf y_k\mid\mathbf y_{1:k-1},\boldsymbol\theta)\tag{1.8}$$
- Combined with smoothing distributions, the marginal joints are (p. 15):
$$p(\mathbf x_k,\boldsymbol\theta\mid\mathbf y_{1:T})=p(\mathbf x_k\mid\mathbf y_{1:T},\boldsymbol\theta)\,p(\boldsymbol\theta\mid\mathbf y_{1:T})\tag{1.9}$$
- The full joint of states and parameters cannot be computed. This is "the price" of constant computation per time step (p. 15).
- If the parameter values themselves are not of interest, the proper Bayesian approach is to integrate them out (p. 15):
$$p(\mathbf x_k\mid\mathbf y_{1:T})=\int p(\mathbf x_k,\boldsymbol\theta\mid\mathbf y_{1:T})\,\mathrm d\boldsymbol\theta=\int p(\mathbf x_k\mid\mathbf y_{1:T},\boldsymbol\theta)\,p(\boldsymbol\theta\mid\mathbf y_{1:T})\,\mathrm d\boldsymbol\theta\tag{1.10}$$
  Many Bayesian parameter methods allow this approximately. For example, MCMC parameter samples give a Monte Carlo approximation of the integral (p. 15).

*Intuition note:* Running the filter at a trial parameter value tells you how well the model predicted each new measurement. Multiplying those prediction scores together with the prior gives that parameter value's posterior weight (up to a constant). Averaging smoothers over the parameter's posterior removes dependence on the unknown value.

### 1.6 Exercises (p. 16)
Three exercises on Kalman's article, maximum likelihood estimation and a package-choosing puzzle. They are listed below.

## Toy example (ours, not from the text)
A hidden two-state chain with states A, B. Assumed numbers: $p(x_0{=}A)=0.5$; the state stays the same with probability 0.9 and switches with 0.1; the sensor reports the true state with probability 0.8. We observe $y_1=A$, $y_2=B$.

**Filter at $k=1$.** Prediction: $p(x_1{=}A)=0.5(0.9)+0.5(0.1)=0.5$. Unnormalized posterior: A: $0.5\times0.8=0.4$; B: $0.5\times0.2=0.1$. Sum $=0.5=p(y_1)$. Filter: $(0.8,\,0.2)$.

**Filter at $k=2$.** Prediction: $p(x_2{=}A)=0.8(0.9)+0.2(0.1)=0.74$, so B is 0.26. Unnormalized for $y_2=B$: A: $0.74\times0.2=0.148$; B: $0.26\times0.8=0.208$. Sum $=0.356=p(y_2\mid y_1)$. Filter: $(0.148/0.356,\ 0.208/0.356)\approx(0.416,\,0.584)$.

**Smoother at $k=1$** (added step, Bayes' rule with the Markov property): $p(x_1\mid y_{1:2})\propto p(x_1\mid y_1)\,p(y_2{=}B\mid x_1)$.
- $p(y_2{=}B\mid x_1{=}A)=0.9(0.2)+0.1(0.8)=0.26$.
- $p(y_2{=}B\mid x_1{=}B)=0.1(0.2)+0.9(0.8)=0.74$.
- Unnormalized: A: $0.8\times0.26=0.208$; B: $0.2\times0.74=0.148$. Sum $=0.356$ (same constant).
- Smoothed: $(0.584,\,0.416)$.

The later measurement $y_2=B$ moves the belief about $x_1$ from 0.8 to 0.584 for A. This is the difference between filtering and smoothing.

**Parameter score (eq. 1.8 idea).** With $\theta=0.9$ (stay probability), $p(y_{1:2}\mid\theta)=0.5\times0.356=0.178$. A competing value of $\theta$ would be compared by recomputing this product.

## Concepts
- [[state]] — the dynamic variables that fully describe the system, e.g. $(x_k,\dot x_k)$ (p. 1, p. 9)
- [[bayesian-filtering]] (new) — computing the distribution of the current state given measurements up to now; "optimal filtering" in the Bayesian way (p. 1, p. 11)
- [[bayesian-smoothing]] (new) — computing the state's distribution given measurements including later ones, $p(\mathbf x_k\mid\mathbf y_{1:T})$ with $T>k$ (p. 1, p. 11)
- [[prediction-distribution]] (new) — $p(\mathbf x_{k+n}\mid\mathbf y_{1:k})$, the distribution of a future state (p. 11)
- [[probabilistic-state-space-model]] (new) — initial, dynamic and measurement distributions, eq. (1.3). The text calls it a general probabilistic state space model (p. 11)
- [[markov-sequence]] (new) — a state sequence defined by the transition distribution $p(\mathbf x_k\mid\mathbf x_{k-1})$ (p. 11)
- [[disturbance and noise]] — here process noise (uncertainty in the dynamics) and measurement noise (p. 1)
- [[full-joint-posterior]] (new) — $p(\mathbf x_{0:T}\mid\mathbf y_{1:T})$; intractable because it is recomputed and grows with every step (p. 10)
- [[Kalman filter]] — closed-form solution of the linear Gaussian filtering problem (p. 13)
- [[rts-smoother]] (new) — closed-form smoother for linear Gaussian models (p. 13)
- [[parameter-marginal-posterior]] (new) — $p(\boldsymbol\theta\mid\mathbf y_{1:T})$ built from filter by-products, eq. (1.8) (p. 15)
- [[data-association]] (new) — deciding which measurement came from which target (p. 3)

## Canonical instances
- [[noisy-resonator]] — a 2D state, scalar noisy position, used for filter and smoother plots (pp. 9, 12–13)
- [[gps-ekf]] — position from satellite signal delays via an EKF (p. 2)
- [[gps-ins-navigation]] — inertial sensors and GPS compensate each other (pp. 4–5)
- [[apollo-11-guidance]] — integrated inertial navigation for the lunar module (p. 4)
- [[slam]] — joint localization and mapping (p. 5)
- [[viterbi-as-map-smoothing]] — Viterbi as MAP smoothing for an HMM (p. 6)

## Bridges (candidates)
- [structural-analogy] Bayesian filter (state from noisy outputs) ↔ control-theory: observer/state estimator — both reconstruct hidden state from measurements; the unit ties the Kalman filter to LQG control (p. 8).
- [same-math] Viterbi algorithm ↔ HMM MAP smoothing — the text states this identification (p. 6).
- [structural-analogy] Minimum norm brain imaging ↔ Gaussian process regression — the text says the Bayesian reading is equivalent to statistical inversion/GP regression (p. 5).
- [same-math] Exercise 1.3 (package choice) ↔ Bayes' rule on a discrete hypothesis — a posterior update after evidence.

## Questions this raises
- How exactly do the prediction and update steps of the Bayes filter give $p(\mathbf x_k\mid\mathbf y_{1:k})$ recursively, and how does the Kalman filter specialize them?
- How much accuracy is lost by the Gaussian approximations of the EKF and UKF compared with particle filters?
- Because the full posterior over states and parameters is not computed, what information about their correlation is lost?
- What does separating estimation from control (the LQG link) require in stochastic optimal control?

## Exercises worth doing
- Ex. 1.1 (p. 16) — read Kalman's orthogonal-projection derivation; ask whether it extends to non-linear/non-Gaussian cases — difficulty: medium
- Ex. 1.2 (p. 16) — a maximum likelihood state estimate (1.11) leaves out the dynamic model; find the problem — difficulty: easy
- Ex. 1.3 (p. 16) — a three-package choice puzzle on whether switching helps; a Bayes' rule exercise — difficulty: easy

## Reading notes
- Printed page = pdf page − 30. Running notice: pre-publication version of Cambridge University Press, 2nd edition, © Särkkä and Svensson 2023.
- The text layer lost many symbols (tildes, subscripts, bold and Greek letters, ranges like $1{:}k$). I checked equations against page images where available (pdf 39, 41, 45).
- No page image was provided for pdf 40 (printed 10) or pdf 44 (printed 14). Eqs. (1.1)–(1.2) were read from the garbled text layer, whose structure is clear. Eq. (1.7) was reconstructed from the text layer and the parallel structure of (1.3); its form matches the narrative on p. 14.
- Fig. 1.7 is a bar diagram of measurement spans for prediction, filtering and smoothing. I described it from the image.
