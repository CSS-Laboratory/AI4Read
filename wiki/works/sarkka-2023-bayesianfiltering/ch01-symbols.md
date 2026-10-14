---
id: sarkka-2023-bayesianfiltering/ch01-symbols
work: sarkka-2023-bayesianfiltering
unit: "Symbols and Abbreviations (front matter)"
pages: xv–xxx
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Symbols and Abbreviations

## L0 — One line
This front-matter reference fixes the book's typography, matrix and probability conventions, a long symbol list in which many letters carry several context-dependent meanings, and a list of abbreviations covering filters, smoothers, sampling methods, models and general terms.

## L1 — The gist (≤ 120 words)
The unit has no argument. It is a lookup table with four parts: general typography (scalars, vectors, matrices, sets), notational conventions (transpose, Jacobian, covariance, matrix square root, ∝, ≜, ≈, ≃, x_{0:k}), a long list of symbols, and abbreviations. A reader can look up here the meaning of a symbol or abbreviation. The symbol list shows two habits. One letter often has several meanings, depending on context. Subscripts and superscripts mark which approximation, time step, iteration or particle a quantity belongs to. The list also contains state-space symbols (state, dynamic and measurement functions, Kalman gain, process and measurement noise).

**Prerequisites:** vectors and matrices (transpose, inverse, determinant, trace); expectation and variance; partial derivatives and the Jacobian.

## L2 — Key ideas
- Typography carries meaning: italic = scalar, bold lowercase = vector, bold uppercase = matrix, blackboard bold = space or set (p. xv).
- Covariance and cross-covariance are defined by expectations of outer products of centred variables (p. xv).
- The matrix square root satisfies $\mathbf P=\sqrt{\mathbf P}\sqrt{\mathbf P}^{\mathsf T}$, and $\mathbf P^{-1/2}$ means $[\sqrt{\mathbf P}]^{-1}$ (p. xvi).
- Four relation symbols express different degrees of equality or proportionality: $\triangleq$ (definition), $\approx$ (is approximately), $\simeq$ (is assumed approximately), and $\propto$ (equal up to a constant factor) (p. xvi).
- Many letters are overloaded (for example $m$, $\mathbf A$, $\mathbf P$, $\Phi$, $\pi$). The list gives several meanings for such letters, so the intended one has to be chosen from the context (pp. xvii–xxvii).
- Recurring decorations include $k$ (time step), $-$ (predicted), s (smoother), $(i)$ (iteration, particle or sigma point), tilde (augmented) and letters G, L, M, Q, R, S, U (the approximation used) (pp. xvii–xxvii).
- Control-flavoured symbols appear: feedback matrix $\mathbf F$, noise coefficient matrix $\mathbf L$, spectral density $\mathbf Q^{\rm c}$, deterministic input $\mathbf u_k$, action, cost and utility (pp. xviii–xxv).
- The abbreviations list includes KF (Kalman filter), EKF (extended Kalman filter), UKF (unscented Kalman filter), CKF (cubature Kalman filter), PF (particle filter), RTS smoothers (Rauch–Tung–Striebel), HMM (hidden Markov model), MCMC (Markov chain Monte Carlo), EM (expectation-maximization) and LQG (linear quadratic Gaussian regulator) (pp. xxvii–xxx).

## L3 — Walkthrough

### General Notation (p. xv)
- Italic letters $a,b,c,x,t,\alpha,\beta$ are scalars (p. xv).
- Bold lowercase letters $\mathbf a,\mathbf f,\mathbf s,\mathbf x,\mathbf y,\boldsymbol\alpha,\boldsymbol\beta$ are vectors (p. xv).
- Bold uppercase letters $\mathbf A,\mathbf F,\mathbf S,\mathbf X,\mathbf Y$ are matrices (p. xv).
- Blackboard-bold letters $\mathbb A,\mathbb F,\mathbb S,\mathbb X,\mathbb Y$ are spaces or sets (p. xv).

*Intuition note:* The font tells you what kind of object a symbol is. Without this rule, $\mathbf x$ (a vector) and $x$ (a scalar) could be confused.

### Notational Conventions (pp. xv–xvi)
Matrix and calculus notation (p. xv):
- $\mathbf A^{\mathsf T}$ is the transpose, $\mathbf A^{-1}$ the inverse, and $\mathbf A^{-\mathsf T}$ the inverse of the transpose.
- $[\mathbf A]_i$ is the $i$th column of $\mathbf A$. $[\mathbf A]_{ij}$ is the element in row $i$, column $j$.
- $|a|$ is the absolute value of a scalar. $|\mathbf A|$ is the determinant of a matrix.
- $\mathrm d\mathbf x/\mathrm dt$ is the time derivative of $\mathbf x(t)$. $\partial g_i(\mathbf x)/\partial x_j$ is the partial derivative of $g_i$ with respect to $x_j$.
- $(a_1,\dots,a_n)$ is a column vector. $(a_1\ \cdots\ a_n)$ is a row vector. $(a_1\ \cdots\ a_n)^{\mathsf T}$ is a column vector.
- The same fraction $\partial g(\mathbf x)/\partial\mathbf x$ is used twice. For a scalar function $g$ it is the gradient (a column vector). For a vector-valued function $\mathbf x\mapsto\mathbf g(\mathbf x)$ it is the Jacobian matrix.
- $\operatorname{diag}(a_1,\dots,a_n)$ is the diagonal matrix with diagonal values $a_1,\dots,a_n$.

Covariance (p. xv):
$$\mathrm{Cov}[\mathbf x]=\mathrm E[(\mathbf x-\mathrm E[\mathbf x])(\mathbf x-\mathrm E[\mathbf x])^{\mathsf T}]$$
$$\mathrm{Cov}[\mathbf x,\mathbf y]=\mathrm E[(\mathbf x-\mathrm E[\mathbf x])(\mathbf y-\mathrm E[\mathbf y])^{\mathsf T}]$$
The second is the cross-covariance of $\mathbf x$ and $\mathbf y$ (p. xv).

Matrix square root and expectation (p. xvi):
$$\mathbf P=\sqrt{\mathbf P}\,\sqrt{\mathbf P}^{\mathsf T}$$
$\mathbf P^{-1/2}$ is the alternative notation for $[\sqrt{\mathbf P}]^{-1}$ (p. xvi). $\mathrm E[\mathbf x]$ is the expectation and $\mathrm E[\mathbf x\mid\mathbf y]$ the conditional expectation.

Integrals and probability (p. xvi):
- $\int f(\mathbf x)\,\mathrm d\mathbf x$ integrates over $\mathbb R^n$. $\int_a^b g(t)\,\mathrm dt$ integrates over $t\in[a,b]$.
- $p(\mathbf x)$ is a density for continuous $\mathbf x$, or a probability for discrete $\mathbf x$. $p(\mathbf x\mid\mathbf y)$ is the conditional version.
- $p(\mathbf x)\propto q(\mathbf x)$ means that a constant $c$ exists with $p(\mathbf x)=c\,q(\mathbf x)$ for all values of $\mathbf x$.
- $\operatorname{tr}\mathbf A$ is the trace. $\mathrm{Var}[x]=\mathrm E[(x-\mathrm E[x])^2]$ is defined for scalar $x$.
- $\mathbf x\sim p(\mathbf x)$ means $\mathbf x$ has density or distribution $p(\mathbf x)$.

Relation symbols and indexing (p. xvi):
- $x\gg y$: $x$ is much greater than $y$.
- $\mathbf x\triangleq\mathbf y$: $\mathbf x$ is defined to be equal to $\mathbf y$.
- $\mathbf x\approx\mathbf y$: approximately equal.
- $\mathbf x\simeq\mathbf y$: *assumed* to be approximately equal.
- $x_{i,k}$ is the $i$th component of $\mathbf x_k$. $\mathbf x_{0:k}$ is the set or sequence $\{\mathbf x_0,\dots,\mathbf x_k\}$. $\dot{\mathbf x}$ is the time derivative of $\mathbf x(t)$.

*Intuition note:* Covariance is the average outer product of deviations from the mean. Cross-covariance uses deviations of two different variables. $\sqrt{\mathbf P}$ is any matrix whose product with its own transpose gives $\mathbf P$. The text does not say here that it is unique.

### Symbols (pp. xvi–xxvii)
The list runs through Greek letters, then Latin letters (scalar, bold, matrix, calligraphic forms). I report the structure and a selection. Pages xix, xx, xxiv, xxviii–xxx had no page image, so symbols there were read from the text layer only.

**Several meanings for one letter.** The source gives these multiple meanings explicitly:
- $\alpha$: unscented-transform parameter *or* a pendulum angle (p. xvi). $\theta$: a parameter *or* a heading angle (p. xvii).
- $\lambda$: unscented-transform parameter, Poisson-distribution parameter, *or* regularization parameter (p. xvii).
- $\Phi(\cdot)$: a function returning the lower triangular part of its argument, *or* the standard Gaussian cumulative density (p. xviii).
- $\pi$: the constant 3.14159265358979323846… (p. xviii), while $\pi(\cdot)$ is an importance or linearization distribution (p. xviii).
- $m$: measurement dimension, univariate Gaussian mean, a mass, number of sigma points, *or* a loop counter (p. xxi).
- $\mathbf A$ has five meanings. They include the dynamic model matrix of a linear time-invariant model and the lower triangular Cholesky factor of a covariance matrix (p. xix).
- $P$ is the variance of a univariate Gaussian, and $\mathbf P$ is a Gaussian covariance (p. xxii). $Q$ is the scalar process-noise variance and $\mathbf Q$ the covariance in a time-invariant model (p. xxiv). $R$ and $\mathbf R$ play the same role for measurement noise (p. xxiv).

*Intuition note:* The same letter can name different objects. For example, $P$ is a variance and $\mathbf P$ a covariance matrix, and $m$ has five listed meanings. The list gives the meanings; it does not say how to choose between them.

**State-space symbols (the filtering core).**
- $\mathbf x_k$ is the state at step $k$, and $\mathbf x(t)$ the state at continuous time $t$. $\mathbf y_k$ is the measurement at step $k$. $\mathbf y_{1:k}$ is the set $\{\mathbf y_1,\dots,\mathbf y_k\}$ (pp. xxvi–xxvii).
- $\mathbf f(\cdot)$ is the dynamic transition function. $\mathbf h(\cdot)$ is the measurement model function (p. xx).
- $\mathbf q_k$ is Gaussian process noise, with covariance $\mathbf Q_k$ for the jump from step $k$ to $k+1$. $\mathbf r_k$ is the vector of Gaussian measurement noises (the scalar version is $r_k$), and $\mathbf R_k$ is the covariance matrix of the measurement at step $k$ (p. xxiv).
- $\mathbf m_k,\mathbf P_k$ are the mean and covariance of a Kalman/Gaussian filter at step $k$ (pp. xxi–xxii). $\mathbf m_k^-,\mathbf P_k^-$ are the predicted mean and covariance, "just before the measurement $\mathbf y_k$" (pp. xxi, xxiii).
- $\mathbf v_k$ and $\mathbf S_k$ are the innovation vector and innovation covariance of a Kalman/Gaussian filter (p. xxv). $\mathbf K_k$ is its gain matrix (p. xxi). $\mathbf G_k$ is the gain matrix in an RTS smoother (p. xx).
- $\mathbf m^{\rm s}_k,\mathbf P^{\rm s}_k$ are the smoother mean and covariance at step $k$ (pp. xxii–xxiii).
- $\mathbf H_x(\cdot)$ and $\mathbf F_x(\cdot)$ are Jacobian matrices of $\mathbf h$ and $\mathbf f$. $\mathbf H^{(i)}_{xx}(\cdot)$ is the Hessian of $h_i$ (pp. xx–xxi).
- $\mathbf A_k$ is the transition matrix from step $k$ to $k+1$ (p. xix); the source also lists an approximate transition matrix in a statistical linear regression approximation. $\mathbf H_k$ is the measurement model matrix at step $k$ in a linear Gaussian or affine model (p. xx).

**Continuous-time and control-flavoured symbols.**
- $\mathbf F$ is the feedback matrix of a continuous-time linear state space model (p. xx). $\mathbf L$ is its noise coefficient (dispersion) matrix (p. xxi).
- $\mathbf w(t)$ is a Gaussian white noise process, with spectral density $q^{\rm c}$ (scalar) or $\mathbf Q^{\rm c}$ (matrix) (pp. xxiv, xxvi).
- $\mathbf a(\cdot)$ is a non-linear drift function in a stochastic differential equation, or acceleration (p. xviii).
- $\mathbf u_k$ is a latent variable in a Rao–Blackwellized particle filter or smoother, *or* a deterministic input to a dynamic model (p. xxv).
- Decision theory: $\mathbf a$ is an action, $\mathbf a_{\rm o}$ the optimal action (p. xviii). $C(\cdot)$ is a cost or loss function (p. xix). $U(\cdot)$ is a utility function (p. xxv).

**Approximation labels.** Subscripts mark the approximation behind a mean, cross-covariance or covariance. The pattern is $\boldsymbol\mu$, $\mathbf C$, $\mathbf S$ with label G (generalized statistical linear regression), L (linear, Taylor series), M (Gaussian moment matching), Q (quadratic), R (statistical linear regression), S (statistical linearization), U (unscented) (pp. xvii–xviii, xix–xx, xxv).

**Other decorations.**
- $\hat{\mathbf x}$ is an estimate or nominal $\mathbf x$. $\mathbf x^*_k$ is the optimal state at step $k$. $\tilde{\mathbf x}_k$ is the augmented state (p. xxvi).
- A superscript $(i)$ marks the $i$th particle, sigma point, iteration or Monte Carlo sample, depending on context (pp. xvii, xxi, xxvi).
- $\boldsymbol\theta^{(n)}$ marks EM iteration $n$, and $\boldsymbol\theta^{(i)}$ marks MCMC iteration $i$ (p. xvii).
- $n$ is usually the state dimension, $N$ usually the number of Monte Carlo samples (p. xxii). $k$ is the time step number, $T$ the last step or final time, $t_k$ the time of step $k$ (pp. xxi, xxv).

### Abbreviations (pp. xxvii–xxx)
The list covers general terms (2D, CPU, GPU, GPS, GNSS), model names, filters and smoothers, and sampling and estimation methods. Selected entries:
- Models: AR, ARMA, CV (constant velocity), CA (constant acceleration), CT (coordinated turn), RW (random walk), DLM (dynamic linear model), HMM (hidden Markov model), SDE, SLDS (p. xxviii–xxx).
- Filters and smoothers: KF, EKF, IEKF, UKF, CKF, GHKF, QKF, ADF, PL/PLF/IPLF, MKF, RBPF, PF, RTSS and its variants (pp. xxviii–xxx).
- Estimation and sampling: MAP, ML, MMSE, EM, EP, IS, SIR, MC, MCMC, MH, HMC, PMCMC (pp. xxviii–xxx).
- Other: LQG (linear quadratic Gaussian regulator), CRLB (Cramér–Rao lower bound), INS (inertial navigation system), SLAM (simultaneous localization and mapping) (pp. xxviii–xxx).

## Toy example (ours, not from the text)
**Cholesky-type factor.** Take $\mathbf A=\begin{pmatrix}2&0\\1&2\end{pmatrix}$, lower triangular. Then
$\mathbf A\mathbf A^{\mathsf T}=\begin{pmatrix}2\cdot2+0&2\cdot1+0\\1\cdot2+0&1\cdot1+2\cdot2\end{pmatrix}=\begin{pmatrix}4&2\\2&5\end{pmatrix}=:\mathbf P$.
So $\mathbf A$ is a valid $\sqrt{\mathbf P}$ in the sense $\mathbf P=\sqrt{\mathbf P}\sqrt{\mathbf P}^{\mathsf T}$.
Its inverse is $\begin{pmatrix}1/2&0\\-1/4&1/2\end{pmatrix}$. Check, row 2 times column 1: $1\cdot\tfrac12+2\cdot(-\tfrac14)=0$. Row 2 times column 2: $0+2\cdot\tfrac12=1$. So $\mathbf P^{-1/2}=[\sqrt{\mathbf P}]^{-1}=\begin{pmatrix}1/2&0\\-1/4&1/2\end{pmatrix}$.

**Covariance.** Let $(x,y)$ be $(1,2)$ or $(3,6)$, each with probability $1/2$. Then $\mathrm E[x]=2$ and $\mathrm E[y]=4$. $\mathrm{Var}[x]=\tfrac12[(1-2)^2+(3-2)^2]=1$. $\mathrm{Cov}[x,y]=\tfrac12[(1-2)(2-4)+(3-2)(6-4)]=\tfrac12(2+2)=2$.

## Concepts
- [[covariance]] (new) — $\mathrm{Cov}[\mathbf x]=\mathrm E[(\mathbf x-\mathrm E\mathbf x)(\mathbf x-\mathrm E\mathbf x)^{\mathsf T}]$ (p. xv)
- [[cross-covariance]] (new) — same with $\mathbf y$ in the second factor (p. xv)
- [[matrix-square-root]] (new) — $\sqrt{\mathbf P}$ with $\mathbf P=\sqrt{\mathbf P}\sqrt{\mathbf P}^{\mathsf T}$ (p. xvi)
- [[proportionality-notation]] (new) — $p\propto q$: $p=cq$ for some constant $c$ and all $\mathbf x$ (p. xvi)
- [[state]] — $\mathbf x_k$ at step $k$, $\mathbf x(t)$ at continuous time (p. xxvi)
- [[state-space-model]] — dynamic function $\mathbf f$, measurement function $\mathbf h$; continuous-time linear form uses $\mathbf F$, $\mathbf L$ (pp. xx–xxi)
- [[kalman-filter]] — mean $\mathbf m_k$, covariance $\mathbf P_k$, gain $\mathbf K_k$ (pp. xxi–xxii)
- [[kalman-gain]] — $\mathbf K_k$, "gain matrix of a Kalman/Gaussian filter" (p. xxi)
- [[innovation]] (new) — $\mathbf v_k$ with covariance $\mathbf S_k$ in a Kalman/Gaussian filter (p. xxv)
- [[disturbance-and-noise]] — process noise $\mathbf q_k$, measurement noise $\mathbf r_k$, white noise $\mathbf w(t)$ (pp. xxiv, xxvi)
- [[sigma-point]] (new) — points such as $\mathcal X^{(i)}$, with weights $W_i$ (pp. xxvi–xxvii)

## Canonical instances
- [[gilbert-elliot-channel-model]] — symbols $b_k$, $p_0,p_1,p_2$, $q_0,q_1$, $s_k$, $v_k$ belong to this model (pp. xix, xxii, xxiv, xxv)
- [[coordinated-turn-model]] — abbreviation CT, next to CV and CA (p. xxviii)

## Bridges (candidates)
- [structural-analogy] $\mathbf F$, $\mathbf L$, spectral density $\mathbf Q^{\rm c}$ ↔ control-theory: continuous-time state-space matrices with white-noise disturbance — same symbols as a linear plant model driven by noise.
- [metaphor] Source's LQG entry (p. xxix) ↔ control-theory: separate estimation and control — the unit only expands the abbreviation.

## Questions this raises
- How do the several uses of $\mathbf A$ and $\mathbf u_k$ get separated inside a single derivation?
- Is the matrix square root meant to be a Cholesky factor in every case? The unit only lists a lower triangular Cholesky factor as one meaning of $\mathbf A$ (p. xix) and does not link it to $\sqrt{\mathbf P}$.
- What exactly distinguishes statistical linearization (S) from statistical linear regression (R)?

## Reading notes
- Printed page numbers are roman numerals. The numeral's value equals the pdf number (xv = pdf 15, … xxx = pdf 30).
- Every page carries a pre-publication notice from Cambridge University Press. It marks the text as the pre-publication version for personal use.
- The text layer drops Greek letters, hats, tildes, bold and sub/superscripts. I read pages xv–xviii, xxi–xxiii, xxv–xxvii from the images.
- No images were provided for pages xix, xx, xxiv, xxviii, xxix, xxx. For these pages I relied on the text layer, so some symbols there are unverified. Descriptions were legible.
- I summarised the symbol list and did not reproduce every entry.
