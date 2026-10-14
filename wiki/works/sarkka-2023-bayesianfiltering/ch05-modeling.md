---
id: sarkka-2023-bayesianfiltering/ch05-modeling
work: sarkka-2023-bayesianfiltering
unit: "5 Modeling with State Space Models"
pages: 73-90
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
# Modeling with State Space Models

## L0 — One line
A probabilistic state space model needs a measurement model $p(\mathbf{y}_k \mid \mathbf{x}_k)$ as well as dynamics, and many estimation problems (outliers, biases, regression, AR models, discrete HMMs) can be written in this form.

## L1 — The gist (≤ 120 words)
Chapter 4 gave dynamic models $p(\mathbf{x}_k\mid\mathbf{x}_{k-1})$. This chapter asks how to build the other half, the measurement model $p(\mathbf{y}_k\mid\mathbf{x}_k)$. It gives linear and non-linear Gaussian sensor models (position, radar range and bearing), heavy-tailed and clutter models for outliers (readings far from what the state predicts), Poisson and Bernoulli models, and the idea of treating a measurement as a known input. It then shows that regression, sensor bias, autoregressive models and finite-state HMMs can be recast as state space models. The model type guides the choice of estimator: Kalman filter, extended/unscented Kalman filters (EKF/UKF), generalized Gaussian filters or particle filters.

**Prerequisites:** Gaussian density and conditional probability; matrix–vector products; Chapter 4 dynamic models (constant velocity, coordinated turn, pendulum); Markov chains.

## L2 — Key ideas (5–10 bullets)
- A measurement model is a conditional density. The common form is $\mathbf{y}_k=\mathbf{h}(\mathbf{x}_k)+\mathbf{r}_k$ with Gaussian noise; a linear $\mathbf{h}$ together with linear Gaussian dynamics gives a Kalman-filter problem (pp. 74–75); with non-linear dynamics the book names EKF, UKF or particle filters (p. 76).
- Non-linear $\mathbf{h}$ arises when the sensor measures a non-linear function of the state, e.g. radar range and bearing. Several sensors are stacked into one vector (pp. 76–77).
- Student's t noise has heavier tails than Gaussian noise, so it is more robust to outliers. It can be written as a Gaussian with a gamma-scaled covariance (pp. 78–79).
- A mixture of a Gaussian and a uniform "clutter" density models outliers with a detection probability $\rho$. Poisson and Bernoulli models cover counts and binary data (pp. 79–82).
- The estimator depends on the model: for the Student's t car model the Kalman filter is no longer applicable (p. 78), and for the clutter model an EKF-based method cannot be used (p. 81); generalized Gaussian or particle filters can be used for these models and for the Poisson and Bernoulli models (pp. 78–82).
- A measurement can be fed in as a known input, which can reduce the number of states; this may cost performance (pp. 82–83).
- Unknown parameters or biases can be put into the state. Regression and AR models then become state space models with $\mathbf{x}_k=\mathbf{x}_{k-1}$ or a random walk (pp. 83–87).
- A finite-state hidden Markov model (HMM) is a state space model with a transition matrix $\boldsymbol{\Pi}$ and an emission matrix $\mathbf{O}$ (pp. 87–88).

## L3 — Walkthrough

### 5.1 Linear and non-linear Gaussian models
The dynamic model is $\mathbf{x}_k=\mathbf{f}(\mathbf{x}_{k-1})+\mathbf{q}_{k-1}$, $\mathbf{q}_{k-1}\sim\mathrm{N}(\mathbf{0},\mathbf{Q}_{k-1})$ (5.1), i.e. $p(\mathbf{x}_k\mid\mathbf{x}_{k-1})=\mathrm{N}(\mathbf{x}_k\mid\mathbf{f}(\mathbf{x}_{k-1}),\mathbf{Q}_{k-1})$ (5.2). The authors omit possible dependence of $\mathbf{f}$ on $k$ and of $\mathbf{Q}$ on the state (p. 73). We often cannot observe the states directly and only get indirect, noisy observations; estimating the states from them can be done with Bayesian filters and smoothers (pp. 73–74). The standard measurement model is
$$\mathbf{y}_k=\mathbf{h}(\mathbf{x}_k)+\mathbf{r}_k,\quad \mathbf{r}_k\sim\mathrm{N}(\mathbf{0},\mathbf{R}_k)\tag{5.3}$$
$$p(\mathbf{y}_k\mid\mathbf{x}_k)=\mathrm{N}(\mathbf{y}_k\mid\mathbf{h}(\mathbf{x}_k),\mathbf{R}_k)\tag{5.4}$$
More generally $\mathbf{y}_k=\mathbf{h}(\mathbf{x}_k,\mathbf{r}_k)$ with possibly non-Gaussian noise, but (5.3) is the most common case (p. 74). Linear models are common when we measure state variables with noise. Non-linear models may appear, for example, if the state variables need to be converted into a different coordinate system to enable a simple relation to the measurements (p. 74).

**Example 5.1 (car position).** The state is $\mathbf{x}=(x_1,x_2,x_3,x_4)$ with position $(x_1,x_2)$ and velocity $(x_3,x_4)$. The measurement noises are independent, $r_{1,k}\sim\mathrm{N}(0,\sigma_1^2)$ and $r_{2,k}\sim\mathrm{N}(0,\sigma_2^2)$. Then $y_{1,k}=x_{1,k}+r_{1,k}$ and $y_{2,k}=x_{2,k}+r_{2,k}$ (5.5), and
$$\mathbf{y}_k=\mathbf{H}\mathbf{x}_k+\mathbf{r}_k,\quad \mathbf{H}=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix}\tag{5.6}$$
($\mathbf{H}$ is $2\times4$) (p. 74). With $\mathbf{x}_k=\mathbf{A}\mathbf{x}_{k-1}+\mathbf{q}_{k-1}$ this is a linear Gaussian model, $\mathbf{R}=\mathrm{diag}(\sigma_1^2,\sigma_2^2)$. The Kalman filter can estimate the state (p. 75). If the polar coordinated turn model with state $(x_1,x_2,s,\varphi,\omega)$ is used (speed $s$, direction $\varphi$, angular velocity $\omega$), the measurement matrix becomes $2\times5$, (5.7). The dynamics are then non-linear and the measurement model is linear. Suitable estimators include the EKF, UKF or a particle filter (pp. 75–76).

**Example 5.2 (pendulum).** The state is $(\alpha, d\alpha/dt)$. Measuring the angle gives a linear Gaussian model (5.8). Measuring only the horizontal position gives $y_k=\sin(\alpha(t_k))+r_k$ (5.9), which is non-linear. Combined, this is $\mathbf{x}_k=\mathbf{f}(\mathbf{x}_{k-1})+\mathbf{q}_{k-1}$, $\mathbf{y}_k=\mathbf{h}(\mathbf{x}_k)+\mathbf{r}_k$ (5.10), solvable by EKF, UKF or particle filter (p. 76).

**Example 5.3 (radar).** A radar at the origin gives range and bearing:
$$\mathbf{y}_k=\begin{pmatrix}\sqrt{x_{1,k}^2+x_{2,k}^2}\\ \arctan\!\left(x_{2,k}/x_{1,k}\right)\end{pmatrix}+\mathbf{r}_k\tag{5.11}$$
The same measurement model would apply if the dynamics were the constant velocity model (p. 77).

**Example 5.4 (multiple ranges).** For several sensors, stack the measurements into one larger vector. With four radars at $(s_{i,x},s_{i,y})$, $i=1,\dots,4$, the $i$-th entry of $\mathbf{h}(\mathbf{x}_k)$ is $\sqrt{(x_{1,k}-s_{i,x})^2+(x_{2,k}-s_{i,y})^2}$, and $\mathbf{r}_k=(r_{1,k},\dots,r_{4,k})$ (5.12). Range and bearing measurements can be stacked in the same way. Combined with a dynamic model we get $\mathbf{x}_k=\mathbf{f}(\mathbf{x}_{k-1})+\mathbf{q}_{k-1}$, $\mathbf{y}_k=\mathbf{h}(\mathbf{x}_k)+\mathbf{r}_k$ (5.13), processed e.g. by the EKF (p. 77).

*Intuition note:* The measurement model only says how the state shows up in the sensor, plus noise. If the dynamics and $\mathbf{h}$ are linear and the noise is Gaussian, the Kalman filter fits (p. 75); if $\mathbf{h}$ (or the dynamics) is non-linear, the book points to EKF, UKF or particle filters (pp. 76–77).

### 5.2 Non-Gaussian measurement models
Gaussian noise cannot always be modeled accurately (p. 78).

**Student's t.** The $n$-dimensional Student's t density with $\nu$ degrees of freedom is
$$\mathrm{St}(\mathbf{y}\mid\boldsymbol\mu,\mathbf{R},\nu)=\frac{\Gamma((\nu+n)/2)}{\Gamma(\nu/2)\,\nu^{n/2}\pi^{n/2}|\mathbf{R}|^{1/2}}\left(1+\frac1\nu(\mathbf{y}-\boldsymbol\mu)^{\mathsf T}\mathbf{R}^{-1}(\mathbf{y}-\boldsymbol\mu)\right)^{-(\nu+n)/2}\tag{5.15}$$
with $\Gamma(z)=\int_0^\infty x^{z-1}e^{-x}\,dx$. It has heavier tails than the Gaussian, so the model expects some larger errors (outliers) and is more robust to them (p. 78). The measurement model is $p(\mathbf{y}_k\mid\mathbf{x}_k)=\mathrm{St}(\mathbf{y}_k\mid\mathbf{h}(\mathbf{x}_k),\mathbf{R},\nu)$ (5.16). Here $\mathbf{R}$ and $\nu$ control covariance and tail weight. The covariance is $\frac{\nu}{\nu-2}\mathbf{R}$, finite only when $\nu>2$ (p. 78). Figure 5.2 compares a Gaussian and Student's t with $\nu=1$ and $\nu=4$ ($\mu=1$, $R=1$) (p. 79).

**Example 5.5.** For the car, $p(\mathbf{y}_k\mid\mathbf{x}_k)=\mathrm{St}(\mathbf{y}_k\mid\mathbf{H}\mathbf{x}_k,\mathbf{R},\nu)$ (5.17). The Kalman filter is no longer applicable. Student's t extensions of it, generalized Gaussian filters (Chapters 9, 10) and particle filters (Chapter 11) are applicable (pp. 78–79).

**Gaussian scale mixture.** If $u\sim\mathrm{Ga}(\nu/2,\nu/2)$ and $\mathbf{y}\mid u\sim\mathrm{N}(\boldsymbol\mu,\mathbf{R}/u)$ (5.18), then the marginal of $\mathbf{y}$ is $\mathrm{St}(\boldsymbol\mu,\mathbf{R},\nu)$. So it is a Gaussian whose covariance is scaled by an unobserved gamma variable $u$ (p. 79).

**Clutter (Gaussian + uniform).** With probability $\rho\in[0,1]$ (the detection probability) we get a regular measurement, and with probability $1-\rho$ an outlier from a uniform density
$$\mathrm{U}(\mathbf{y}_k\mid\mathbb{V})=\begin{cases}1/V,&\mathbf{y}_k\in\mathbb{V}\\0,&\text{otherwise}\end{cases}\tag{5.19}$$
where $V$ is the volume of $\mathbb{V}$ (the outlier model could also be a Gaussian with larger covariance). The model is (5.20), equivalently the mixture
$$p(\mathbf{y}_k\mid\mathbf{x}_k)=(1-\rho)\,\mathrm{U}(\mathbf{y}_k\mid\mathbb{V})+\rho\,\mathrm{N}(\mathbf{y}_k\mid\mathbf{h}(\mathbf{x}_k),\mathbf{R}_k)\tag{5.21}$$
(Figure 5.3: $\mathbb{V}=[-7,9]$, $\rho=0.9$) (pp. 79–80). Equivalently, add an unobserved indicator $c_k\sim\mathrm{Be}(\rho)$:
$$p(c_k)=\mathrm{Be}(c_k\mid\rho),\quad p(\mathbf{y}_k\mid\mathbf{x}_k,c_k)=\begin{cases}\mathrm{N}(\mathbf{y}_k\mid\mathbf{h}(\mathbf{x}_k),\mathbf{R}_k),&c_k=1\\\mathrm{U}(\mathbf{y}_k\mid\mathbb{V}),&c_k=0\end{cases}\tag{5.22}$$
(pp. 80–81).

**Example 5.6 (pendulum clutter).** $p(y_k\mid\mathbf{x}_k)$ is $\mathrm{N}(y_k\mid\sin\alpha_k,R_k)$ with probability $\rho$ and $\mathrm{U}(y_k\mid[-L,L])$ with probability $1-\rho$ (5.23). An EKF-based method can no longer be used, but a general Gaussian filter or a particle filter can (p. 81).

**Poisson counts.** $\mathrm{Po}(y\mid\lambda)=\exp(-\lambda)\lambda^y/y!$ (5.24) for counts $y=0,1,2,\dots$. Since $\lambda>0$, use $\lambda=\lambda_0\exp(u)$, giving $p(y_k\mid\mathbf{x}_k)=\mathrm{Po}(y_k\mid\lambda_0\exp(h(\mathbf{x}_k)))$ (5.25). Here $h$ maps the state to the log-intensity relative to $\lambda_0$. Particle filters or generalized Gaussian filters can be used (p. 81).

**Bernoulli (binary).** $\mathrm{Be}(y\mid\rho)=\rho^y(1-\rho)^{1-y}$ (5.26), $y\in\{0,1\}$. To keep $\rho\in[0,1]$, transform a real-valued variable:
$$p(y_k=1\mid\mathbf{x}_k)=\Phi(h(\mathbf{x}_k))\ \text{ or }\ \frac{1}{1+\exp(-h(\mathbf{x}_k))}\tag{5.27}$$
where $\Phi(z)=\int_{-\infty}^z\mathrm{N}(x\mid0,1)\,dx$. Particle filters or generalized Gaussian filters apply (pp. 81–82).

*Intuition note (our paraphrase of the book's "more robust", p. 78):* A Gaussian gives a far-off reading very little probability. The t and clutter models reserve some probability for such readings, so one outlier should dominate the estimate less.

### 5.3 Measurements as inputs
Sometimes an observation is treated as a known input $\mathbf{u}_{k-1}$: $\mathbf{x}_k=\mathbf{f}(\mathbf{x}_{k-1},\mathbf{u}_{k-1})+\mathbf{q}_{k-1}$ (5.28). The aim is to simplify the problem and reduce the number of states. This often gives good performance when the measurement noise is small (p. 82).

**Example 5.7 (gyroscope).** The coordinated-turn function (5.29) is
$$\mathbf{f}(\mathbf{x}_{k-1})=\begin{pmatrix}x_{1,k-1}+\frac{2s_{k-1}}{\omega_{k-1}}\sin\!\left(\frac{\Delta t_{k-1}\omega_{k-1}}2\right)\cos\!\left(\varphi_{k-1}+\frac{\Delta t_{k-1}\omega_{k-1}}2\right)\\x_{2,k-1}+\frac{2s_{k-1}}{\omega_{k-1}}\sin\!\left(\frac{\Delta t_{k-1}\omega_{k-1}}2\right)\sin\!\left(\varphi_{k-1}+\frac{\Delta t_{k-1}\omega_{k-1}}2\right)\\s_{k-1}\\\varphi_{k-1}+\omega_{k-1}\Delta t_{k-1}\\\omega_{k-1}\end{pmatrix}$$
Option 1: model the gyro reading as a noisy measurement, $\omega_k^{\text{gyro}}=\omega_k+r_k=(0\ 0\ 0\ 0\ 1)\mathbf{x}_k+r_k$ (5.30). Option 2: set $u_{k-1}=\omega^{\text{gyro}}_{k-1}$ and replace $\omega_{k-1}$ by $u_{k-1}$ in the first four rows, giving $\mathbf{f}(\mathbf{x}_{k-1},u_{k-1})$ (5.31). The state is now only $(x_1,x_2,s,\varphi)$ (p. 83). The same can be done for a speedometer (Exercise 5.4). The simplification may come at the price of reduced performance (p. 83).

### 5.4 Linear-in-parameters models in state space form
**Example 5.8.** The model $y_k=w_0+w_1g_1(t_k)+\dots+w_dg_d(t_k)+\varepsilon_k$ (5.32) has given functions $g_i$ and Gaussian noise $\varepsilon_k$. Let $\mathbf{H}_k=(1\ g_1(t_k)\ \cdots\ g_d(t_k))$ ($1\times(d+1)$) and $\mathbf{x}_k=\mathbf{x}=(w_0,\dots,w_d)$. Then
$$\mathbf{x}_k=\mathbf{x}_{k-1},\qquad y_k=\mathbf{H}_k\mathbf{x}_k+\varepsilon_k\tag{5.33}$$
is a linear Gaussian state space model, so a linear Kalman filter estimates the weights (pp. 83–84).

**Example 5.9.** The same works for regressors $\mathbf{s}_k\in\mathbb{R}^n$: $y_k=w_0+w_1g_1(\mathbf{s}_k)+\dots+w_dg_d(\mathbf{s}_k)+\varepsilon_k$ (5.34), with $\mathbf{H}_k=(1\ g_1(\mathbf{s}_k)\cdots g_d(\mathbf{s}_k))$ (p. 84).

**Example 5.10 (generalized linear model).** $y_k=g(w_0+\mathbf{w}^{\mathsf T}\mathbf{s}_k)+\varepsilon_k$ (5.35), with non-linear link $g$. With $\mathbf{x}=(w_0,\mathbf{w})$ and $\mathbf{h}_k(\mathbf{x})=g(w_0+\mathbf{w}^{\mathsf T}\mathbf{s}_k)$ we get $\mathbf{x}_k=\mathbf{x}_{k-1}$, $y_k=\mathbf{h}_k(\mathbf{x}_k)+\varepsilon_k$ (5.36). This is non-linear, so a non-linear Kalman filter such as the EKF or UKF is needed instead of the linear one (p. 84). Multi-layer perceptrons can be converted similarly. Non-linear Kalman filtering is one way to train them, though unconventional (pp. 84–85).

**Sensor bias.** If $\mathbf{y}_k=\mathbf{h}(\mathbf{x}_k)+\mathbf{b}+\mathbf{r}_k$ (5.37), augment the state: $\tilde{\mathbf{x}}_k=(\mathbf{x}_k,\mathbf{b}_k)$ with $\mathbf{b}_k=\mathbf{b}_{k-1}$, and $\tilde{\mathbf{h}}(\tilde{\mathbf{x}}_k)=\mathbf{h}(\mathbf{x}_k)+\mathbf{b}_k$ (5.38). Adding a small noise, $\mathbf{b}_k=\mathbf{b}_{k-1}+\mathbf{q}^{\mathbf{b}}_{k-1}$, allows slow drift (p. 85).

**Example 5.11.** For a constant velocity model with state $(x_{1,k},x_{2,k})$ (position, velocity), the velocity measurement has a drifting bias: $\mathbf{y}_k=(x_{1,k},x_{2,k})+(0,b_k)+\mathbf{r}_k$ (5.39). With $\tilde{\mathbf{x}}_k=(x_{1,k},x_{2,k},b_k)$ the dynamics are
$$\begin{pmatrix}x_{1,k}\\x_{2,k}\\b_k\end{pmatrix}=\begin{pmatrix}1&\Delta t_{k-1}&0\\0&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}x_{1,k-1}\\x_{2,k-1}\\b_{k-1}\end{pmatrix}+\begin{pmatrix}q_{1,k-1}\\q_{2,k-1}\\q_{3,k-1}\end{pmatrix}\tag{5.40}$$
with $\mathbf{q}_{k-1}\sim\mathrm{N}(\mathbf{0},\mathbf{Q}_{k-1})$. This is a constant velocity model for $(x_1,x_2)$ and a random walk for $b_k$ (p. 85).

*Intuition note:* A fixed unknown parameter is treated as a state that never moves. Adding small noise lets it drift slowly.

### 5.5 Autoregressive models
In adaptive filtering the signal-model parameters are estimated from data (p. 86).

**Example 5.12 (AR).** $y_k=w_1y_{k-1}+\dots+w_dy_{k-d}+\varepsilon_k$ (5.41), with white Gaussian $\varepsilon_k$. Let $\mathbf{H}_k=(y_{k-1}\cdots y_{k-d})$ and $\mathbf{x}_k=(w_1,\dots,w_d)$. Then $\mathbf{x}_k=\mathbf{x}_{k-1}$, $y_k=\mathbf{H}_k\mathbf{x}_k+\varepsilon_k$ (5.42), solvable with a linear Kalman filter. The classical LMS algorithm can be interpreted as an approximate version of this filter (p. 86).

**Example 5.13 (TVAR).** Weights depend on time: $y_k=w_{1,k}y_{k-1}+\dots+w_{d,k}y_{k-d}+\varepsilon_k$ (5.43), with random walks $w_{i,k}=w_{i,k-1}+q_{i,k-1}$, $q_{i,k-1}\sim\mathrm{N}(0,Q_i)$ (5.44). With $\mathbf{x}_k=(w_{1,k},\dots,w_{d,k})$: $\mathbf{x}_k=\mathbf{x}_{k-1}+\mathbf{q}_{k-1}$, $y_k=\mathbf{H}_k\mathbf{x}_k+\varepsilon_k$ (5.45). More general (TV)ARMA models can be handled similarly (pp. 86–87).

### 5.6 Discrete-state hidden Markov models
In a finite-state HMM, $\mathbf{x}_k\in\mathbb{X}$ (finite), and often $\mathbf{y}_k\in\mathbb{Y}$ (finite). Without loss of generality use scalars $x_k\in\{1,\dots,X\}$, $y_k\in\{1,\dots,Y\}$. The states form a Markov chain with transition matrix
$$\Pi_{i,j}=p(x_k=j\mid x_{k-1}=i)\tag{5.46}$$
and measurements are described by the emission matrix
$$O_{i,j}=p(y_k=j\mid x_k=i)\tag{5.47}$$
Either matrix may depend on $k$ (p. 87).

**Example 5.14 (Gilbert–Elliot channel).** A binary input $b_k$ is sent; a binary regime $s_k$ sets the error probability. The measurement is $b_k\oplus v_k$ (xor), with $v_k$ a Bernoulli sequence. It is coded $y_k=1$ if $b_k\oplus v_k=0$ and $y_k=2$ if it equals 1. The error probability $p(v_k=1)$ is $q_0$ when $s_k=0$ and $q_1$ (larger) when $s_k=1$. $s_k$ is a Markov chain with $0\to1$ probability $p_0$ and $1\to0$ probability $p_1$. $b_k$ is a Markov chain with switching probability $p_2$. The pair $(b_k,s_k)$ is a four-state chain, states $(0,0),(0,1),(1,0),(1,1)$ coded $1,\dots,4$ (pp. 87–88). Matrices (rows = current state; $\boldsymbol\Pi$ is $4\times4$, $\mathbf{O}$ is $4\times2$):
$$\boldsymbol\Pi=\begin{pmatrix}(1-p_0)(1-p_2)&p_0(1-p_2)&(1-p_0)p_2&p_0p_2\\p_1(1-p_2)&(1-p_1)(1-p_2)&p_1p_2&(1-p_1)p_2\\(1-p_0)p_2&p_0p_2&(1-p_0)(1-p_2)&p_0(1-p_2)\\p_1p_2&(1-p_1)p_2&p_1(1-p_2)&(1-p_1)(1-p_2)\end{pmatrix},\quad \mathbf{O}=\begin{pmatrix}1-q_0&q_0\\1-q_1&q_1\\q_0&1-q_0\\q_1&1-q_1\end{pmatrix}$$
Figure 5.4 shows simulated trajectories (p. 88). HMMs can also model indicator variables inside continuous-state tracking models (Exercise 5.8) (p. 89).

## Toy example (ours): outlier under a Gaussian vs a clutter mixture
Scalar sensor with $h(x)=0$, $R=1$, $\rho=0.9$, $\mathbb{V}=[-7,9]$, so $V=16$ (the setting of Figure 5.3). Mixture (5.21): $p(y)=0.1/16+0.9\,\mathrm{N}(y\mid0,1)$.
- $y=0$: $\mathrm{N}=1/\sqrt{2\pi}\approx0.3989$. $p=0.00625+0.9(0.3989)=0.00625+0.35904\approx0.3653$. Pure Gaussian: $0.3989$.
- $y=5$ (an outlier): $\mathrm{N}=e^{-12.5}/\sqrt{2\pi}\approx3.73\times10^{-6}/2.507\approx1.49\times10^{-6}$. Mixture: $0.00625+0.9(1.49\times10^{-6})\approx0.006251$.

The mixture gives the outlier about $4\,200$ times more likelihood than the Gaussian ($0.006251/1.49\times10^{-6}\approx4200$), while near the mean it is only about 8% lower ($0.3653/0.3989\approx0.92$). So a single outlier reading cannot rule out the true state.

## Concepts
- [[measurement-model]] (new) — conditional density $p(\mathbf{y}_k\mid\mathbf{x}_k)$ linking sensor output to the state, completing the state space model (p. 73)
- [[state-space-model]] — dynamics $p(\mathbf{x}_k\mid\mathbf{x}_{k-1})$ plus measurement model; here also linear regression, AR and HMM forms (pp. 73, 83–87)
- [[disturbance-and-noise]] — measurement noise $\mathbf{r}_k$, Gaussian or heavy-tailed, additive or not (p. 74)
- [[kalman-filter]] — estimator used for linear Gaussian models (p. 75); not applicable to the Student's t model (p. 78)
- [[robustness]] — here: tolerance to outlier measurements via heavy-tailed or clutter noise (p. 78)
- [[heavy-tailed-noise]] (new) — Student's t noise, with a Gaussian scale-mixture form (5.18) (pp. 78–79)
- [[clutter-mixture-model]] (new) — Gaussian + uniform mixture with detection probability $\rho$ (p. 80)
- [[state-augmentation]] (new) — adding unknown parameters or bias to the state (p. 85)
- [[measurements-as-inputs]] (new) — treating a measured signal as known input $\mathbf{u}$ (p. 82)
- [[hidden-markov-model]] (new) — finite-state chain with matrices $\boldsymbol\Pi$ and $\mathbf{O}$ (p. 87)
- [[autoregressive-model]] (new) — $y_k$ as weighted past values plus noise; weights as state (p. 86)

## Canonical instances
- [[car-position-measurement]] — linear $\mathbf{H}$ picking out position (p. 74)
- [[radar-range-bearing]] — non-linear $\mathbf{h}$, stackable over several radars (p. 77)
- [[pendulum-horizontal-position]] — $y=\sin\alpha+r$ (p. 76)
- [[gilbert-elliot-channel]] — four-state HMM example (p. 87)
- [[bias-in-state-vector]] — drifting velocity-sensor bias (p. 85)

## Bridges (candidates)
- [same-math] Linear-in-parameters regression as $\mathbf{x}_k=\mathbf{x}_{k-1}$, $y_k=\mathbf{H}_k\mathbf{x}_k+\varepsilon_k$ ↔ control-theory: observer for a constant unknown parameter — the same linear Gaussian state space model.
- [structural-analogy] Sensor bias as an extra state ↔ control-theory: disturbance estimation by augmenting the observer's state — both augment the state with the unknown quantity.
- [structural-analogy] Finite-state HMM ($\boldsymbol\Pi$, $\mathbf{O}$) ↔ control-theory: discrete-state stochastic systems with noisy outputs.

## Questions this raises
- How do the Kalman filter and its non-linear versions use $\mathbf{H}$ and $\mathbf{h}$ to update the state estimate?
- When does treating a measurement as an input (Section 5.3) lose too much compared with keeping it as a measurement?
- How do filters cope with the unobserved indicator $c_k$ or scale $u$ in the clutter and Student's t models?
- How does the filtering problem for an HMM differ from the Gaussian case?

## Exercises worth doing
- Ex. 5.2 (p. 89) — show Student's t tends to a Gaussian as $\nu\to\infty$; links the two noise families — difficulty: medium
- Ex. 5.5 (p. 89) — write a regression with Gaussian priors on $a_1,a_2,b$ as a linear Gaussian state space model — difficulty: medium
- Ex. 5.6 (p. 89) — find $\mathbf{H}$ for the bias-augmented model (5.39) — difficulty: easy
- Ex. 5.7 (p. 89) — rewrite an AR latent signal observed in noise as a linear Gaussian state space model — difficulty: medium
- Ex. 5.8 (p. 90) — clutter model for the car, a Markov clutter indicator and an augmented joint model — difficulty: hard

## Reading notes
- Printed page = pdf − 30. The text layer lost many Greek symbols and hats; all equations were checked against the page images.
- Header on each page: pre-publication version of *Bayesian Filtering and Smoothing*, 2nd ed., © Särkkä and Svensson 2023.
- Minor misprints in the source: "radars" appears twice in the sensor list (p. 74); "various others contexts" (p. 85).
- Many examples refer to Chapter 4 models (e.g. Example 5.7 recalls Example 4.15) and Example 5.8 builds on the Chapter 3 regression problem; those chapters are not part of this unit.
