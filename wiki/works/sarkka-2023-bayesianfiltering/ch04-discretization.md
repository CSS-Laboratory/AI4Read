---
id: sarkka-2023-bayesianfiltering/ch04-discretization
work: sarkka-2023-bayesianfiltering
unit: "4 Discretization of Continuous-Time Dynamic Models"
pages: 44-72
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
# Discretization of Continuous-Time Dynamic Models

## L0 — One line
Physical tracking models are written as white-noise-driven differential equations in continuous time; to use them in discrete-time filters, they are discretized exactly if linear and time-invariant, and approximately (Euler–Maruyama, linearization, fast sampling) if non-linear.

## L1 — The gist (≤ 120 words)
Filters need a transition model $p(\mathbf x_k\mid\mathbf x_{k-1})$, but physics gives a continuous-time stochastic differential equation (SDE). For linear time-invariant SDEs the exact transition is Gaussian, with a matrix exponential for the mean map and an integral for the noise covariance. For non-linear SDEs the exact transition is usually intractable, so the chapter builds Gaussian approximations. Euler–Maruyama (freezing the drift over each step) is simple but often gives a singular, non-invertible noise covariance. Linearizing around the mean gives a good mean but a usually intractable covariance; around the initial point, a tractable covariance but a rougher mean. Fixed-point linearization gives a state-independent covariance. Sampling faster than the measurements makes Euler–Maruyama more accurate.

**Prerequisites:** matrix exponential; Gaussian distributions and covariance; Jacobian and first-order Taylor expansion; ordinary differential equations; basic idea of white noise.

## L2 — Key ideas
- Dynamic models are built in continuous time as SDEs $\dot{\mathbf x}=\mathbf a(\mathbf x)+\mathbf L\mathbf w$ and then discretized; the sampled sequence stays Markovian (p. 46).
- Linear time-invariant SDEs discretize exactly: $\mathbf A=\exp(\mathbf F\Delta t)$ and $\mathbf Q=\int_0^{\Delta t}e^{\mathbf Fs}\mathbf L\mathbf Q^c\mathbf L^\top e^{\mathbf F^\top s}\,ds$ (Thm 4.3, p. 49). The Wiener process becomes a random walk and the Wiener velocity model gets closed-form $\mathbf A,\mathbf Q$ (pp. 49–51).
- Euler–Maruyama: $\mathbf f=\mathbf x+\mathbf a\Delta t$, $\mathbf Q=\mathbf L\mathbf Q^c\mathbf L^\top\Delta t$ (Thm 4.8, p. 54). Its covariance is singular when $\mathbf L\mathbf Q^c\mathbf L^\top$ is not invertible (p. 55).
- Linearizing around the mean gives an ODE for $\mathbf m(t)$ and a Lyapunov ODE for $\mathbf P(t)$ (Thm 4.13, p. 59). The mean is often solvable in closed form (CT and bicycle models); the covariance usually is not (pp. 60–64).
- Linearizing at the initial point (Thm 4.18, p. 65) gives a tractable but state-dependent covariance. The constant-gradient variant (Thm 4.19, p. 66) combines it with the mean-linearization mean.
- To remove state dependence, evaluate the Jacobian at a fixed point (Alg. 4.20, p. 67); the result is usually non-singular (p. 67).
- Fast sampling inserts extra sampling times between measurements, so each step is shorter; the text shows that this makes the Euler–Maruyama approximation more accurate (pp. 69–70).

## L3 — Walkthrough

**Intro (p. 44).** A state space model needs a measurement model $p(\mathbf y_k\mid\mathbf x_k)$ and a dynamic model $p(\mathbf x_k\mid\mathbf x_{k-1})$. The dynamic model lets measurements at other times inform $\mathbf x_k$. Models are built in continuous time as SDEs, then discretized, because the later filters work in discrete time. The authors deliberately use the white-noise-driven approach. They note that driving the SDE with piecewise-constant or impulse noise is an alternative (p. 44).

### 4.1 Discrete-time and continuous-time models (pp. 45–46)
- Discrete-time model: $\mathbf x_k=\mathbf f_{k-1}(\mathbf x_{k-1})+\mathbf q_{k-1}$, $\mathbf q_{k-1}\sim\mathrm N(\mathbf 0,\mathbf Q_{k-1})$ \tag{4.1}, equivalently $p(\mathbf x_k\mid\mathbf x_{k-1})=\mathrm N(\mathbf x_k\mid \mathbf f_{k-1}(\mathbf x_{k-1}),\mathbf Q_{k-1})$ \tag{4.2} (p. 45).
- Samples are $\mathbf x_k=\mathbf x(t_k)$ with sampling period $\Delta t_{k-1}=t_k-t_{k-1}$ (p. 45).
- Continuous-time analogue (SDE): $\dfrac{d\mathbf x}{dt}=\mathbf a(\mathbf x(t))+\mathbf L\mathbf w(t)$ \tag{4.3}.
- The noise has zero mean and covariance
$$\mathrm E[\mathbf w(t)]=\mathbf 0,\quad \mathrm{Cov}[\mathbf w(\tau_1),\mathbf w(\tau_2)]=\delta(\tau_1-\tau_2)\mathbf Q^c \tag{4.4}$$
($\delta$ = Dirac delta, $\mathbf Q^c$ = spectral density matrix, a continuous-time analogue of a covariance) (p. 46).
- The noise enters causally: $\mathbf w(t')$ and $\mathbf x(t)$ are uncorrelated for $t'\ge t$. Together with whiteness this makes $\mathbf x(t)$ Markovian (p. 46).
- White-noise notation avoids Itô calculus (p. 46).
- Discretization = obtaining the model for the step $\mathbf x_{k-1}\to\mathbf x_k$. The sampled sequence is Markovian. An exact transition density always exists, but is often intractable; non-linear models therefore need approximate discretization (p. 46).

### 4.2 Discretizing linear dynamic models (pp. 47–52)
Model: $\dfrac{d\mathbf x}{dt}=\mathbf F\mathbf x+\mathbf L\mathbf w$ \tag{4.5}, with $\mathbf w$ as in (4.4) (p. 47). (Shapes, added: $\mathbf x\in\mathbb R^n$, $\mathbf F$ is $n\times n$, $\mathbf L$ is $n\times s$, $\mathbf Q^c$ is $s\times s$.)

**Example 4.1 (car, p. 47–48).** The car is a point mass at $(x_1,x_2)$, pushed by unknown forces. Newton's law is $\mathbf g=m\mathbf a$ \tag{4.6}. Model $\mathbf g/m$ as two independent white noises:
$$\frac{d^2x_1}{dt^2}=w_1(t),\quad \frac{d^2x_2}{dt^2}=w_2(t)\tag{4.7}$$
With $x_3=dx_1/dt$, $x_4=dx_2/dt$:
$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}=\underbrace{\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&0&0&0\\0&0&0&0\end{pmatrix}}_{\mathbf F}\mathbf x+\underbrace{\begin{pmatrix}0&0\\0&0\\1&0\\0&1\end{pmatrix}}_{\mathbf L}\begin{pmatrix}w_1\\w_2\end{pmatrix}\tag{4.8}$$
with $\mathbf Q^c=\mathrm{diag}(q^c_1,q^c_2)$ (p. 48).

**Example 4.2 (CV / Wiener velocity model, p. 48).** For a $d$-dimensional model with positions then velocities in $\mathbf x$:
$$\frac{d\mathbf x}{dt}=\begin{pmatrix}\mathbf 0&\mathbf I\\\mathbf 0&\mathbf 0\end{pmatrix}\mathbf x+\begin{pmatrix}\mathbf 0\\\mathbf I\end{pmatrix}\mathbf w\tag{4.9}$$
The position derivative is the velocity; the velocity derivative is the noise.

**Theorem 4.3 (p. 49).** The solution of (4.5) is Gaussian, so the transition is linear-Gaussian:
$$p(\mathbf x(t_k)\mid\mathbf x(t_{k-1}))=\mathrm N\big(\mathbf x(t_k)\mid \exp(\mathbf F\Delta t_{k-1})\mathbf x(t_{k-1}),\mathbf Q_{k-1}\big)\tag{4.10}$$
$$\mathbf Q_{k-1}=\int_0^{\Delta t_{k-1}}\exp(\mathbf Fs)\,\mathbf L\mathbf Q^c\mathbf L^\top\exp(\mathbf Fs)^\top ds\tag{4.11}$$
Here $\exp$ is the matrix exponential. The discrete model is $\mathbf x_k=\mathbf A_{k-1}\mathbf x_{k-1}+\mathbf q_{k-1}$, with $\mathbf A_{k-1}=\exp(\mathbf F\Delta t_{k-1})$ and $\mathbf q_{k-1}\sim\mathrm N(\mathbf 0,\mathbf Q_{k-1})$ \tag{4.12}. The proof follows from Lemma A.9 (appendix, not in this unit) with $\mathbf b=\mathbf 0$, $\tau=\Delta t_{k-1}$ (p. 49).

*Intuition note.* Without noise, the state simply follows the matrix exponential from the old state to the new one. The noise added over the step is the sum of all its effects over the step, each propagated to the end by $\exp(\mathbf F s)$, and this sum is Gaussian.

**Example 4.4 (Wiener process, p. 49).** For $d\mathbf x/dt=\mathbf w$ we have $\mathbf F=\mathbf 0$ and $\exp(\mathbf 0)=\mathbf I$. Then $\mathbf Q_{k-1}=\int_0^{\Delta t_{k-1}}\mathbf Q^c ds=\mathbf Q^c\Delta t_{k-1}$, and the discretized model is the random walk $\mathbf x_k=\mathbf x_{k-1}+\mathbf q_{k-1}$ \tag{4.15}. Figure 4.3: a scalar Wiener process with $Q^c=2$ sampled at $\Delta t=0.5$ gives $Q_k=1$ (p. 50).

**Example 4.5 (discrete CV model, pp. 50–51).** With $\mathbf F=\begin{pmatrix}\mathbf 0&\mathbf I\\\mathbf 0&\mathbf 0\end{pmatrix}$, $\mathbf L=\begin{pmatrix}\mathbf 0\\\mathbf I\end{pmatrix}$ \tag{4.16}, $\mathbf F^n=\mathbf 0$ for $n\ge2$ (nilpotent of index 2), so
$$\mathbf A_{k-1}=\sum_{n=0}^\infty\frac{(\mathbf F\Delta t_{k-1})^n}{n!}=\mathbf I+\mathbf F\Delta t_{k-1}=\begin{pmatrix}\mathbf I&\mathbf I\Delta t_{k-1}\\\mathbf 0&\mathbf I\end{pmatrix}\tag{4.17}$$
(velocity constant; new position = old position + $\Delta t\cdot$ velocity, ignoring noise). Then
$$\mathbf Q_{k-1}=\int_0^{\Delta t_{k-1}}\begin{pmatrix}\mathbf I&s\mathbf I\\\mathbf 0&\mathbf I\end{pmatrix}\begin{pmatrix}\mathbf 0\\\mathbf I\end{pmatrix}\mathbf Q^c\begin{pmatrix}\mathbf 0&\mathbf I\end{pmatrix}\begin{pmatrix}\mathbf I&\mathbf 0\\s\mathbf I&\mathbf I\end{pmatrix}ds=\int_0^{\Delta t_{k-1}}\begin{pmatrix}s^2\mathbf Q^c&s\mathbf Q^c\\s\mathbf Q^c&\mathbf Q^c\end{pmatrix}ds=\begin{pmatrix}\frac{\Delta t_{k-1}^3}{3}\mathbf Q^c&\frac{\Delta t_{k-1}^2}{2}\mathbf Q^c\\\frac{\Delta t_{k-1}^2}{2}\mathbf Q^c&\Delta t_{k-1}\mathbf Q^c\end{pmatrix}\tag{4.18}$$
The author says: for $\Delta t_{k-1}\ll1$ the noise is small and dominated by the velocity state; for $\Delta t_{k-1}\gg1$ it is large and dominated by the position state (p. 51).

**Example 4.6 (discretized car, p. 51).** Using step $\Delta t$ and $\mathbf Q^c=\mathrm{diag}(q_1^c,q_2^c)$: $\mathbf x_k=\mathbf A\mathbf x_{k-1}+\mathbf q_{k-1}$ with $\mathbf A=\begin{pmatrix}1&0&\Delta t&0\\0&1&0&\Delta t\\0&0&1&0\\0&0&0&1\end{pmatrix}$ \tag{4.19}, and
$$\mathbf Q=\begin{pmatrix}\frac{q_1^c\Delta t^3}{3}&0&\frac{q_1^c\Delta t^2}{2}&0\\0&\frac{q_2^c\Delta t^3}{3}&0&\frac{q_2^c\Delta t^2}{2}\\\frac{q_1^c\Delta t^2}{2}&0&q_1^c\Delta t&0\\0&\frac{q_2^c\Delta t^2}{2}&0&q_2^c\Delta t\end{pmatrix}\tag{4.20}$$
When (4.11) has no convenient analytical form, it can be evaluated numerically by matrix fraction decomposition (pp. 51–52).

### 4.3 The Euler–Maruyama method (pp. 52–58)
For non-linear $\dfrac{d\mathbf x}{dt}=\mathbf a(\mathbf x)+\mathbf L\mathbf w$ \tag{4.21}, the transition density is in general not Gaussian and has no closed form. We nevertheless seek $\mathbf x_k=\mathbf f_{k-1}(\mathbf x_{k-1})+\mathbf q_{k-1}$ with Gaussian $\mathbf q_{k-1}$ \tag{4.22} (p. 52).

**Example 4.7 (noisy pendulum, pp. 52–53).** Unit length and mass: $\dfrac{d^2\alpha}{dt^2}=-g\sin\alpha+w(t)$ \tag{4.23}, with $w$ of spectral density $q^c$. With $x_1=\alpha$, $x_2=d\alpha/dt$:
$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}x_2\\-g\sin x_1\end{pmatrix}+\begin{pmatrix}0\\1\end{pmatrix}w(t)\tag{4.24}$$
a case of $d\mathbf x/dt=\mathbf a(\mathbf x)+\mathbf L\mathbf w$ \tag{4.25}.

The method approximates $\mathbf a(\mathbf x(t))\approx\mathbf a(\mathbf x(t_{k-1}))$ on $[t_{k-1},t_k)$:
$$\frac{d\mathbf x}{dt}\approx\mathbf a(\mathbf x(t_{k-1}))+\mathbf L\mathbf w(t)\tag{4.26}$$

**Theorem 4.8 (p. 53–54).** The method gives $\mathbf x_k=\mathbf f_{k-1}(\mathbf x_{k-1})+\mathbf q_{k-1}$, $\mathbf q_{k-1}\sim\mathrm N(\mathbf 0,\mathbf Q_{k-1})$ \tag{4.28}, with
$$\mathbf f_{k-1}(\mathbf x_{k-1})=\mathbf x_{k-1}+\mathbf a(\mathbf x_{k-1})\Delta t_{k-1},\quad \mathbf Q_{k-1}=\mathbf L\mathbf Q^c\mathbf L^\top\Delta t_{k-1}\tag{4.29}$$
Equivalent form: $\mathbf x_k=\mathbf f_{k-1}(\mathbf x_{k-1})+\mathbf L\tilde{\mathbf q}_{k-1}$, $\tilde{\mathbf q}_{k-1}\sim\mathrm N(\mathbf 0,\tilde{\mathbf Q}_{k-1})$ \tag{4.30}, $\tilde{\mathbf Q}_{k-1}=\mathbf Q^c\Delta t_{k-1}$ \tag{4.31}. The authors call this form often more convenient because $\tilde{\mathbf Q}_{k-1}$ is usually strictly positive definite even though $\mathbf Q_{k-1}$ is not (p. 54).

*Proof (p. 54).* Integrate (4.32), $d\mathbf x/dt\approx\mathbf a(\mathbf x(t_{k-1}))+\mathbf L\mathbf w$, from $t_{k-1}$ to $t_k$:
$$\mathbf x(t_k)-\mathbf x(t_{k-1})=\mathbf a(\mathbf x(t_{k-1}))\Delta t_{k-1}+\mathbf L\int_{t_{k-1}}^{t_k}\mathbf w\,dt\tag{4.33}$$
By Example 4.4, $\int_{t_{k-1}}^{t_k}\mathbf w\,dt\sim\mathrm N(\mathbf 0,\mathbf Q^c\Delta t_{k-1})$ \tag{4.34}, hence $\mathbf L\int\mathbf w\,dt\sim\mathrm N(\mathbf 0,\mathbf L\mathbf Q^c\mathbf L^\top\Delta t_{k-1})$. Rearranging gives the result.

*Intuition note.* Freeze the drift at the start of the step, then add the noise accumulated over the step. The noise only reaches the directions that $\mathbf L$ can reach, so $\mathbf Q$ has zero rows wherever $\mathbf L$ does.

**Example 4.9 (pendulum, pp. 54–55).** Here $\mathbf a(\mathbf x)=(x_2,-g\sin x_1)^\top$, $\mathbf L=(0,1)^\top$. First form (4.28):
$$\mathbf f_{k-1}=\begin{pmatrix}x_{1,k-1}+x_{2,k-1}\Delta t_{k-1}\\x_{2,k-1}-g\sin(x_{1,k-1})\Delta t_{k-1}\end{pmatrix}\tag{4.37}$$
$$\mathbf Q_{k-1}=\mathbf L q^c\mathbf L^\top\Delta t_{k-1}=\begin{pmatrix}0&0\\0&q^c\Delta t_{k-1}\end{pmatrix}\tag{4.38}$$
which is singular. The second form (4.39) uses the same $\mathbf f_{k-1}$ with scalar noise $\tilde q_{k-1}\sim\mathrm N(0,q^c\Delta t_{k-1})$ entering only the second component (p. 55).

**Singularity (p. 55).** The second form does not remove the general problem: the Euler–Maruyama transition is singular whenever $\mathbf L\mathbf Q^c\mathbf L^\top$ is not invertible. This is not a problem for most filters in the book, but iterated filters and smoothers get numerical problems.

**Example 4.10 (polar coordinated turn, CT, pp. 55–57).** Heading $\varphi(t)$ is measured counterclockwise from east, $s$ is speed, $\omega$ is turn rate:
$$\dot x_1=s\cos\varphi,\ \dot x_2=s\sin\varphi\ \ (4.40),\qquad \dot\varphi=\omega\tag{4.41}$$
$$\dot s=w_1(t),\quad\dot\omega=w_2(t)\tag{4.42}$$
Form (4.44), $d\mathbf x/dt=\mathbf a(\mathbf x)+\mathbf L\mathbf w$, with state $(x_1,x_2,s,\varphi,\omega)$ and
$$\mathbf a=(s\cos\varphi,\ s\sin\varphi,\ 0,\ \omega,\ 0)^\top,\quad \mathbf L=\begin{pmatrix}0&0\\0&0\\1&0\\0&0\\0&1\end{pmatrix}\tag{4.43}$$

**Example 4.11 (p. 57).** The second Euler–Maruyama form gives $\mathbf x_k=\mathbf x_{k-1}+(s_{k-1}\cos\varphi_{k-1},\,s_{k-1}\sin\varphi_{k-1},\,0,\,\omega_{k-1},\,0)^\top\Delta t_{k-1}+\mathbf L\tilde{\mathbf q}_{k-1}$ \tag{4.45}, with $\tilde{\mathbf Q}_{k-1}=\mathrm{diag}(q_1^c,q_2^c)\Delta t_{k-1}$ \tag{4.46}. The model function is
$$\mathbf f_{k-1}=\begin{pmatrix}x_{1,k-1}+s_{k-1}\cos(\varphi_{k-1})\Delta t_{k-1}\\x_{2,k-1}+s_{k-1}\sin(\varphi_{k-1})\Delta t_{k-1}\\s_{k-1}\\\varphi_{k-1}+\omega_{k-1}\Delta t_{k-1}\\\omega_{k-1}\end{pmatrix}\tag{4.47}$$
However, $\mathrm N(\mathbf x_k\mid\mathbf f(\mathbf x_{k-1}),\mathbf Q_{k-1})$ is not a proper density, since $\mathbf Q_{k-1}=\mathbf L\mathbf Q^c\mathbf L^\top\Delta t_{k-1}$ is not invertible.

**Algorithm 4.12 (simulating an SDE, p. 58).** Split $[t_{k-1},t_k]$ into $n$ steps of length $\Delta\tau=(t_k-t_{k-1})/n$. Start from $\hat{\mathbf x}_0=\mathbf x(t_{k-1})$. For $j=1,\dots,n$:
$$\hat{\mathbf x}_j=\hat{\mathbf x}_{j-1}+\mathbf a(\hat{\mathbf x}_{j-1})\Delta\tau+\mathbf L\hat{\mathbf q}_{j-1},\quad\hat{\mathbf q}_{j-1}\sim\mathrm N(\mathbf 0,\mathbf Q^c\Delta\tau)\tag{4.48}$$
The path is the piecewise-constant trajectory through $\{\hat{\mathbf x}_0,\dots,\hat{\mathbf x}_n\}$. Simulated trajectories converge to true SDE sample paths as $\Delta\tau\to0$ (Kloeden and Platen, cited). With multiple steps, the singularity of the effective multi-step transition vanishes (p. 58). This is useful for the prediction (importance-sampling) step of particle filters and for generating simulated data. Linearization, which is very useful for discretization, is not as useful for simulation, because its theoretical convergence rate is no better than that of Euler–Maruyama (p. 58).

### 4.4 Discretization via continuous-time linearization (pp. 58–65)
Euler–Maruyama uses a zeroth-order approximation of $\mathbf a$; it often yields rough approximations for long sampling periods and often gives singular covariances. Alternative: first-order Taylor expansion around a nominal trajectory $\bar{\mathbf x}(t)$:
$$\mathbf a(\mathbf x(t))\approx\mathbf a(\bar{\mathbf x}(t))+\mathbf A_{\mathbf x}(\bar{\mathbf x}(t))(\mathbf x(t)-\bar{\mathbf x}(t))\tag{4.49}$$
where $\mathbf A_{\mathbf x}$ is the Jacobian (row $i$ = gradient of $a_i$) (p. 59). Choosing $\bar{\mathbf x}=\mathbf m(t)=\mathrm E[\mathbf x(t)]$ gives (4.50). Using the unknown $\mathbf m(t)$ may look counterintuitive, but the approximation helps to find $\mathbf m(t)$ (p. 59). The same approximation is used in the continuous-discrete extended Kalman filter.

**Theorem 4.13 (p. 59).** If $\dfrac{d\mathbf x}{dt}\approx\mathbf a(\mathbf m)+\mathbf A_{\mathbf x}(\mathbf m)(\mathbf x-\mathbf m)+\mathbf L\mathbf w$ \tag{4.51}, then given $\mathbf x(t_{k-1})=\mathbf x_{k-1}$, $\mathbf x(t)$ is Gaussian for $t\ge t_{k-1}$ with
$$\frac{d\mathbf m}{dt}=\mathbf a(\mathbf m)\tag{4.52}$$
$$\frac{d\mathbf P}{dt}=\mathbf A_{\mathbf x}(\mathbf m)\mathbf P+\mathbf P\mathbf A_{\mathbf x}^\top(\mathbf m)+\mathbf L\mathbf Q^c\mathbf L^\top\tag{4.53}$$
and $\mathbf m(t_{k-1})=\mathbf x_{k-1}$, $\mathbf P(t_{k-1})=\mathbf 0$. *Proof:* take expectations, using $\mathrm E[\mathbf A_{\mathbf x}(\mathbf m)(\mathbf x-\mathbf m)]=\mathbf 0$ and $\mathrm E[\mathbf L\mathbf w]=\mathbf 0$, to get (4.52). The derivation of (4.53) is in Appendix A.5 (not in this unit).

The mean equation is the noise-free deterministic dynamics. It can be solved in closed form in several important examples. Equation (4.53) is the Lyapunov differential equation; it generally lacks an analytical solution unless $\mathbf A_{\mathbf x}(\mathbf m(t))$ is constant. Either equation can be solved with Runge–Kutta solvers (p. 60).

**Algorithm 4.14 (mean linearization, p. 60).** Let $\mathbf f_{k-1}(\mathbf x_{k-1})=\mathbf m(t_k)$ and $\mathbf Q_{k-1}(\mathbf x_{k-1})=\mathbf P(t_k)$, both depending on $\mathbf x_{k-1}$ through the initial condition. Then $\mathbf x_k=\mathbf f_{k-1}(\mathbf x_{k-1})+\mathbf q_{k-1}$, $\mathbf q_{k-1}\sim\mathrm N(\mathbf 0,\mathbf Q_{k-1}(\mathbf x_{k-1}))$ \tag{4.55}. The covariance is state-dependent and more complicated than Euler–Maruyama's; it is often further approximated (p. 60).

*Intuition note.* The mean follows the noise-free dynamics. The covariance grows through the local sensitivity $\mathbf A_{\mathbf x}$ plus the noise injected at every instant.

**Example 4.15 (polar CT mean, pp. 60–61).** The mean ODE is the deterministic part (4.56). Solving it analytically (Appendix A.7) gives
$$\mathbf f_{k-1}=\begin{pmatrix}x_{1,k-1}+\frac{2s_{k-1}}{\omega_{k-1}}\sin\!\big(\frac{\Delta t_{k-1}\omega_{k-1}}{2}\big)\cos\!\big(\varphi_{k-1}+\frac{\Delta t_{k-1}\omega_{k-1}}{2}\big)\\x_{2,k-1}+\frac{2s_{k-1}}{\omega_{k-1}}\sin\!\big(\frac{\Delta t_{k-1}\omega_{k-1}}{2}\big)\sin\!\big(\varphi_{k-1}+\frac{\Delta t_{k-1}\omega_{k-1}}{2}\big)\\s_{k-1}\\\varphi_{k-1}+\omega_{k-1}\Delta t_{k-1}\\\omega_{k-1}\end{pmatrix}\tag{4.57}$$
For $\omega_{k-1}\approx0$, $\frac{2s}{\omega}\sin(\Delta t\,\omega/2)\approx s\Delta t$, giving the numerically stable approximations $f_1\approx x_{1,k-1}+s_{k-1}\Delta t_{k-1}\cos\varphi_{k-1}$ and $f_2\approx x_{2,k-1}+s_{k-1}\Delta t_{k-1}\sin\varphi_{k-1}$ \tag{4.58}. The covariance ODE (4.53) is intractable here; the Euler–Maruyama covariance is possible but singular (p. 61).

**Example 4.16 (Cartesian CT, pp. 61–62).** Differentiate (4.40) and use (4.41)–(4.42):
$$\ddot x_1=w_1\cos\varphi-\omega\dot x_2,\quad\ddot x_2=w_1\sin\varphi+\omega\dot x_1\tag{4.59}$$
The derivation is heuristic; a rigorous one needs the Itô formula (p. 61). Rename the turn-rate noise $w_3$ and replace $w_1\cos\varphi\to w_1$, $w_1\sin\varphi\to w_2$ (independent noises). With state $(x_1,x_2,\dot x_1,\dot x_2,\omega)$:
$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\\\dot x_1\\\dot x_2\\\omega\end{pmatrix}=\begin{pmatrix}\dot x_1\\\dot x_2\\-\omega\dot x_2\\\omega\dot x_1\\0\end{pmatrix}+\begin{pmatrix}0&0&0\\0&0&0\\1&0&0\\0&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}w_1\\w_2\\w_3\end{pmatrix}\tag{4.60}$$
This is conceptually simpler than the polar CT model, but the noise no longer acts directly in the tangential (speed) direction, only additively on the velocity vector (p. 62). The mean solution is
$$\mathbf f_{k-1}=\begin{pmatrix}1&0&\frac{\sin(\Delta t\,\omega)}{\omega}&-\frac{1-\cos(\Delta t\,\omega)}{\omega}&0\\0&1&\frac{1-\cos(\Delta t\,\omega)}{\omega}&\frac{\sin(\Delta t\,\omega)}{\omega}&0\\0&0&\cos(\Delta t\,\omega)&-\sin(\Delta t\,\omega)&0\\0&0&\sin(\Delta t\,\omega)&\cos(\Delta t\,\omega)&0\\0&0&0&0&1\end{pmatrix}\mathbf x_{k-1}\tag{4.61}$$
(with $\Delta t=\Delta t_{k-1}$, $\omega=\omega_{k-1}$; derivation left to Exercise 4.5). For $\omega_{k-1}\to0$, for numerical stability, use the limit
$$\lim_{\omega_{k-1}\to0}\mathbf f_{k-1}=\begin{pmatrix}1&0&\Delta t_{k-1}&0&0\\0&1&0&\Delta t_{k-1}&0\\0&0&1&0&0\\0&0&0&1&0\\0&0&0&0&1\end{pmatrix}\mathbf x_{k-1}\tag{4.62}$$
The covariance is again intractable (p. 63).

**Example 4.17 (bicycle model, pp. 63–64).** The rear-wheel position is $(x_1,x_2)$, heading $\theta$, speed $s$, front steering angle $\delta$, wheelbase $L$, signed distance to the centre of rotation $r$. From the figure, $\tan\delta=L/r$, so
$$\frac{d\theta}{dt}=\frac{s}{r}=\frac{s\tan\delta}{L}\tag{4.63}$$
Speed and steering are driven by independent white noises: $d\mathbf x/dt=(s\cos\theta,\ s\sin\theta,\ 0,\ s/r,\ 0)^\top+\mathbf L\mathbf w$ \tag{4.64}, with $\mathbf L=\begin{pmatrix}0&0\\0&0\\1&0\\0&0\\0&1\end{pmatrix}$, $\mathbf Q^c=\mathrm{diag}(q_s^c,q_\delta^c)$ \tag{4.65}. The mean has a closed form (Appendix A.6):
$$\mathbf f(\mathbf x_{k-1})=\begin{pmatrix}x_{1,k-1}+r_{k-1}(\sin(\theta_{k-1}+\beta_{k-1})-\sin\theta_{k-1})\\x_{2,k-1}+r_{k-1}(\cos\theta_{k-1}-\cos(\theta_{k-1}+\beta_{k-1}))\\s_{k-1}\\\theta_{k-1}+\beta_{k-1}\\\delta_{k-1}\end{pmatrix}\tag{4.66}$$
with $r_{k-1}=L/\tan\delta_{k-1}$, $\beta_{k-1}=\Delta t_{k-1}s_{k-1}/r_{k-1}$. The covariance is intractable; use Euler–Maruyama or the approximations of Section 4.5 (p. 64).

**Linearizing at the initial point.** If the deterministic model cannot be solved quickly, use $\mathbf a(\mathbf x(t))\approx\mathbf a(\mathbf x(t_{k-1}))+\mathbf A_{\mathbf x}(\mathbf x(t_{k-1}))(\mathbf x(t)-\mathbf x(t_{k-1}))$ \tag{4.67} (p. 64).

**Theorem 4.18 (p. 65).** Under the approximation $d\mathbf x/dt\approx\mathbf a(\mathbf x_{k-1})+\mathbf A_{\mathbf x}(\mathbf x_{k-1})(\mathbf x-\mathbf x_{k-1})+\mathbf L\mathbf w$ \tag{4.69}, the discretized model is
$$\mathbf x_k=\mathbf x_{k-1}+\Big(\int_0^{\Delta t_{k-1}}\exp(\mathbf A_{\mathbf x}(\mathbf x_{k-1})s)ds\Big)\mathbf a(\mathbf x_{k-1})+\mathbf q_{k-1}=\mathbf x_{k-1}+\Big(\sum_{i=1}^\infty\frac{\Delta t_{k-1}^i\,\mathbf A_{\mathbf x}(\mathbf x_{k-1})^{i-1}}{i!}\Big)\mathbf a(\mathbf x_{k-1})+\mathbf q_{k-1}\tag{4.70}$$
with $\mathbf q_{k-1}\sim\mathrm N(\mathbf 0,\mathbf Q_{k-1}(\mathbf x_{k-1}))$ and
$$\mathbf Q_{k-1}(\mathbf x_{k-1})=\int_0^{\Delta t_{k-1}}\exp(\mathbf A_{\mathbf x}(\mathbf x_{k-1})s)\mathbf L\mathbf Q^c\mathbf L^\top\exp(\mathbf A_{\mathbf x}(\mathbf x_{k-1})s)^\top ds\tag{4.71}$$
Proof: Exercise 4.7. *Sanity check (p. 65):* if $\mathbf a(\mathbf x)=\mathbf F\mathbf x$, then $\mathbf A_{\mathbf x}=\mathbf F$ and the deterministic part becomes $\exp(\mathbf F\Delta t_{k-1})\mathbf x_{k-1}$ \tag{4.72}, so Theorem 4.3 is recovered. The covariance is tractable, but the deterministic part can be rough (linearization at the start only) and cumbersome to compute (p. 65).

### 4.5 Covariance approximation via constant gradients (pp. 65–68)
The aim is $\mathbf f_{k-1}$ and $\mathbf Q_{k-1}$ both accurate, with $\mathbf Q_{k-1}$ preferably non-singular and independent of $\mathbf x_{k-1}$ (pp. 65–66). Mean linearization gives a good $\mathbf f_{k-1}$. Initial-point linearization gives a slightly inferior $\mathbf f_{k-1}$ but a tractable covariance. Combine them using the constant matrix $\mathbf A_{\mathbf x}(\mathbf x_{k-1})$ with the mean $\mathbf m(t)$:
$$\mathbf a(\mathbf x(t))\approx\mathbf a(\mathbf m(t))+\mathbf A_{\mathbf x}(\mathbf x_{k-1})(\mathbf x(t)-\mathbf m(t))\tag{4.76}$$
This gives the same $\mathbf m(t)$ and thus the same $\mathbf f_{k-1}$ as mean linearization (p. 66).

**Theorem 4.19 (p. 66).** Under (4.77), with $\mathbf x(t_{k-1})=\mathbf x_{k-1}$, the mean solves $d\mathbf m/dt=\mathbf a(\mathbf m)$, $\mathbf m(t_{k-1})=\mathbf x_{k-1}$ \tag{4.78}, and
$$\mathbf P(t_k)=\int_0^{\Delta t_{k-1}}\exp(\mathbf A_{\mathbf x}(\mathbf x_{k-1})s)\mathbf L\mathbf Q^c\mathbf L^\top\exp(\mathbf A_{\mathbf x}(\mathbf x_{k-1})s)^\top ds\tag{4.79}$$
Put $\mathbf f_{k-1}(\mathbf x_{k-1})=\mathbf m(t_k)$ and $\mathbf Q_{k-1}(\mathbf x_{k-1})=\mathbf P(t_k)$. Proof: Exercise 4.9.

The covariance still depends on $\mathbf x_{k-1}$, i.e. $p(\mathbf x_k\mid\mathbf x_{k-1})=\mathrm N(\mathbf x_k\mid\mathbf f_{k-1},\mathbf Q_{k-1}(\mathbf x_{k-1}))$. Some later filters handle this: Gaussian filters in conditional-moments form (Alg. 9.22) and particle filters (Alg. 11.8). For simpler filters, evaluate the Jacobian at a fixed point instead (p. 67).

**Algorithm 4.20 (additive noise approximation, p. 67).** Form $\mathbf f_{k-1}$ by, for example, Euler–Maruyama or continuous-time linearization. Then linearize at a fixed point $\hat{\mathbf x}$ and take the noise covariance of $d\mathbf x/dt=\mathbf A_{\mathbf x}(\hat{\mathbf x})\mathbf x+\mathbf L\mathbf w$ \tag{4.80}:
$$\mathbf Q_{k-1}\approx\int_0^{\Delta t_{k-1}}\exp(\mathbf A_{\mathbf x}(\hat{\mathbf x})s)\mathbf L\mathbf Q^c\mathbf L^\top\exp(\mathbf A_{\mathbf x}(\hat{\mathbf x})s)^\top ds\tag{4.81}$$
This is usually non-singular even when Euler–Maruyama's is singular, and independent of $\mathbf x_{k-1}$. Any $\hat{\mathbf x}$ can be chosen (e.g. the origin); it may be better to choose it close to the true state, for instance the filter's posterior mean $\hat{\mathbf x}=\mathbf m_k$ (p. 67).

*Intuition note.* The mean is obtained from the noise-free ODE, which gives a good $\mathbf f_{k-1}$ when it can be solved. For the covariance, simpler filters are easier with a state-independent $\mathbf Q$, so the Jacobian is frozen at one fixed point.

**Example 4.21 (pendulum, pp. 67–68).** Linearizing at $\hat{\mathbf x}=(0,0)$: $\mathbf a(\mathbf x)\approx\begin{pmatrix}0&1\\-g&0\end{pmatrix}\mathbf x$ \tag{4.82}, giving a constant noise covariance. Linearizing only in $x_2$ with $x_1$ fixed at the origin gives $\mathbf a(\mathbf x)\approx\begin{pmatrix}0&1\\0&0\end{pmatrix}\mathbf x$ \tag{4.83}. Then (4.18) yields
$$\mathbf Q_{k-1}=q^c\begin{pmatrix}\frac{\Delta t_{k-1}^3}{3}&\frac{\Delta t_{k-1}^2}{2}\\\frac{\Delta t_{k-1}^2}{2}&\Delta t_{k-1}\end{pmatrix}\tag{4.84}$$

**Example 4.22 (polar CT covariance, p. 68).** The constant-gradient covariance at $\mathbf x_{k-1}$ is given in Appendix A.8. Set the speed to zero, set cross-terms with sines and cosines to zero, and dominate squares of sines and cosines by 1. The result is
$$\mathbf Q_{k-1}=\begin{pmatrix}q_s^c\frac{\Delta t^3}{3}&0&0&0&0\\0&q_s^c\frac{\Delta t^3}{3}&0&0&0\\0&0&q_s^c\Delta t&0&0\\0&0&0&q_\omega^c\frac{\Delta t^3}{3}&q_\omega^c\frac{\Delta t^2}{2}\\0&0&0&q_\omega^c\frac{\Delta t^2}{2}&q_\omega^c\Delta t\end{pmatrix}\tag{4.85}$$
($\Delta t=\Delta t_{k-1}$; $q_s^c,q_\omega^c$ drive speed and angular velocity).

### 4.6 Fast sampling (pp. 69–70)
For small $\Delta t_{k-1}$ even Euler–Maruyama is accurate. The single-step Gaussian approximation may be poor for large periods. Higher-order SDE expansions (Itô–Taylor) often give overly complicated solutions. The alternative is to sample the continuous-time state more often. This gives an accurate Gaussian model but possibly more costly filters (p. 69).

Formally, insert $n_k-1$ extra times $\tau_i$ between $t_{k-1}$ and $t_k$, with $\tau_i=t_k$ when $i=\sum_{j=1}^kn_j$, and define $\mathbf x_k=\mathbf x(\tau_k)$ (Figure 4.7). Measurements are still collected only at the $t_k$; the filters and smoothers apply directly, skipping the update step when there is no measurement. The posterior at the original times is obtained as part of the result (pp. 69–70).

This is closely related to Algorithm 4.12. With Euler–Maruyama the assumption becomes $\mathbf a(\mathbf x(t))\approx\mathbf a(\mathbf x(\tau_{k-1}))$ on $[\tau_{k-1},\tau_k)$ \tag{4.86}, over a shorter interval. If $\Delta t_k=\Delta t$ and $\Delta\tau=\Delta t/n$, the approximation is used on $1/n$ of the original period, "which leads to more accurate approximations" (p. 70).

## Toy example (ours, not from the text)
Scalar Wiener velocity model ($d=1$): state $(x,v)$, $\dot x=v$, $\dot v=w$, $q^c=2$, $\Delta t=0.5$.

*Exact (Theorem 4.3 / (4.17)–(4.18)):* $\mathbf A=\begin{pmatrix}1&0.5\\0&1\end{pmatrix}$. $\mathbf Q=2\begin{pmatrix}0.125/3&0.25/2\\0.25/2&0.5\end{pmatrix}=\begin{pmatrix}0.08333&0.25\\0.25&1\end{pmatrix}$. $\det\mathbf Q=0.08333\cdot1-0.25^2=0.02083>0$.

*Euler–Maruyama (Thm 4.8):* $\mathbf f=\mathbf x+\mathbf a\Delta t=(x+0.5v,\ v)$, the same $\mathbf A$ because $\mathbf F$ is nilpotent. But $\mathbf Q=\mathbf L q^c\mathbf L^\top\Delta t=\begin{pmatrix}0&0\\0&1\end{pmatrix}$, with $\det=0$: singular. Position gets no noise in one step.

*Two substeps, $\Delta\tau=0.25$ (Section 4.6):* $\mathbf A_s=\begin{pmatrix}1&0.25\\0&1\end{pmatrix}$, $\mathbf Q_s=\mathrm{diag}(0,\ 2\cdot0.25)=\mathrm{diag}(0,0.5)$. The two-step noise is $\mathbf A_s\mathbf q_1+\mathbf q_2$, with covariance $\mathbf A_s\mathbf Q_s\mathbf A_s^\top+\mathbf Q_s$. First, $\mathbf A_s\mathbf Q_s=\begin{pmatrix}0&0.125\\0&0.5\end{pmatrix}$. Multiplying by $\mathbf A_s^\top=\begin{pmatrix}1&0\\0.25&1\end{pmatrix}$ gives $\begin{pmatrix}0.03125&0.125\\0.125&0.5\end{pmatrix}$. Adding $\mathbf Q_s$ gives $\begin{pmatrix}0.03125&0.125\\0.125&1\end{pmatrix}$, $\det=0.03125-0.015625=0.015625>0$. The singularity is gone and the matrix is closer in shape to the exact $\mathbf Q$.

Mean from $(x,v)=(0,1)$: $(0.5,\ 1)$ in all three cases.

## Concepts
- [[state-space-model]] — dynamic model plus measurement model; here the dynamic part is built from physics, then discretized (p. 44).
- [[linearization]] — first-order Taylor expansion of $\mathbf a$ around a nominal point (mean, initial point, or fixed point) to get tractable moments (p. 59).
- [[disturbance-and-noise]] — here, process noise as continuous-time white noise $\mathbf w(t)$ with spectral density $\mathbf Q^c$ (p. 46).
- [[discretization]] (new) — obtaining $p(\mathbf x_k\mid\mathbf x_{k-1})$ from the SDE (p. 46).
- [[spectral-density-white-noise]] (new) — $\mathrm{Cov}[\mathbf w(\tau_1),\mathbf w(\tau_2)]=\delta(\tau_1-\tau_2)\mathbf Q^c$ (p. 46).
- [[matrix-exponential-discretization]] (new) — exact linear discretization: $\mathbf A=\exp(\mathbf F\Delta t)$ and the $\mathbf Q$ integral (p. 49).
- [[wiener-velocity-model]] (new) — constant velocity model, velocity driven by white noise (p. 48).
- [[euler-maruyama-method]] (new) — freezes drift at the interval start; $\mathbf Q=\mathbf L\mathbf Q^c\mathbf L^\top\Delta t$ (p. 54).
- [[singular-process-noise]] (new) — Euler–Maruyama transition is singular when $\mathbf L\mathbf Q^c\mathbf L^\top$ is not invertible (p. 55).
- [[lyapunov-differential-equation]] (new) — the covariance ODE (4.53) (p. 60).
- [[additive-noise-approximation]] (new) — state-independent $\mathbf Q$ from linearization at a fixed point (p. 67).
- [[fast-sampling]] (new) — extra sampling times between measurements; update skipped without data (p. 69).

## Canonical instances
- [[constant-velocity-car-model]] — Wiener velocity model of a 2D car with closed-form $\mathbf A,\mathbf Q$ (pp. 47–51).
- [[noisy-pendulum]] — non-linear model used to show Euler–Maruyama and additive noise approximation (pp. 52–55, 67–68).
- [[coordinated-turn-model]] — polar and Cartesian versions; closed-form mean, intractable covariance (pp. 55–62).
- [[bicycle-model]] — vehicle model with closed-form mean (pp. 63–64).

## Bridges (candidates)
- [same-math] $\mathbf A=\exp(\mathbf F\Delta t)$ in Thm 4.3 ↔ control-theory: state transition of a linear time-invariant system between sampling instants — same matrix exponential.
- [structural-analogy] Lyapunov ODE (4.53) for $\mathbf P(t)$ ↔ control-theory: covariance propagation in the continuous-discrete extended Kalman filter (the text notes the same approximation is used there, p. 59).
- [structural-analogy] Fast sampling ↔ control-theory: finer-grained sample-and-hold model — shorter step, better short-step approximation.
- [metaphor] Linearizing around $\mathbf m(t)$ before knowing $\mathbf m(t)$ ↔ control-theory: self-consistent estimate, state estimate used to linearize its own dynamics.

## Questions this raises
- How large can $\Delta t$ be before the one-step Gaussian approximation of the non-linear transition fails, and how would one measure the error?
- Does the dependence of $\mathbf Q_{k-1}(\mathbf x_{k-1})$ on the state change the performance of the filters that assume additive state-independent noise?
- How good is the replacement of $\mathbf Q$ in Example 4.22 (speed set to zero, cross-terms dropped) compared with the exact constant-gradient covariance in Appendix A.8?
- How many substeps $n$ are needed in fast sampling to trade accuracy against filter cost?

## Exercises worth doing
- Ex. 4.1 (p. 70) — simulate scalar Wiener process samples with Algorithm 4.12 — difficulty: easy.
- Ex. 4.2 (p. 70) — exact discretization of the constant acceleration model via Theorem 4.3 — difficulty: medium.
- Ex. 4.3 (p. 70) — Euler–Maruyama for the CA model, compared with the exact result of 4.2 — difficulty: medium.
- Ex. 4.4 (p. 70–71) — sample RW, CV and CA models and compare roughness — difficulty: easy.
- Ex. 4.8 (p. 71) — check that the linear moments satisfy Theorem 4.13 in the scalar case — difficulty: medium.
- Ex. 4.10 (p. 71) — covariance $\mathbf Q_{k-1}(\mathbf x_{k-1})$ from Theorem 4.19 for the bicycle model, plus simulation — difficulty: hard.

## Reading notes
- Printed page = pdf − 30. Pages used: pdf 74–102 (printed 44–72).
- The text layer is heavily garbled (missing minus signs, Greek letters, hats). I checked every equation against the page images. Some images show the pdf's "Δ" and "−" rendering clearly where the text layer drops them.
- Misprints in the source text: "continous" (p. 46), "becase" (p. 50), "Euler–Maryuama" (pp. 58, 64).
- Proofs of Theorem 4.3 (Lemma A.9), the $\mathbf P$ equation in Theorem 4.13 (App. A.5), and the closed forms in Examples 4.15, 4.17, 4.22 (App. A.6–A.8) are in the appendix and are not in this unit. Proofs of Theorems 4.18 and 4.19 are left as exercises.
- Exercise 4.11 (p. 71) states the covariance (4.90) for the Cartesian CT model at the origin: $\mathbf Q_{k-1}=\begin{pmatrix}q_1^c\frac{\Delta t^3}{3}&0&q_1^c\frac{\Delta t^2}{2}&0&0\\0&q_2^c\frac{\Delta t^3}{3}&0&q_2^c\frac{\Delta t^2}{2}&0\\q_1^c\frac{\Delta t^2}{2}&0&q_1^c\Delta t&0&0\\0&q_2^c\frac{\Delta t^2}{2}&0&q_2^c\Delta t&0\\0&0&0&0&q_3^c\Delta t\end{pmatrix}$ with $\Delta t=\Delta t_{k-1}$, where $q_1^c,q_2^c,q_3^c$ are the spectral densities of $w_1,w_2,w_3$.
- Statements about "dominated by velocity/position noise" (p. 51) and "usually strictly positive definite" (p. 54) are reported as the author gives them, without proof.
