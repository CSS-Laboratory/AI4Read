---
id: kalman-1960-filtering/main
work: kalman-1960-filtering
unit: paper
pages: 35-45
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# A New Approach to Linear Filtering and Prediction Problems (Kalman, 1960)

## L0 — One line
If a random signal is modelled as a linear state system driven by white gaussian noise, the optimal linear estimate is a recursive filter whose gain follows from a nonlinear difference equation for the error covariance, and this problem is the dual of the noise-free optimal regulator.

## L1 — The gist (≤ 120 words)
Wiener's solution to estimating a random signal from noisy data was specified by an impulse response. It was hard to synthesize or compute, and awkward for nonstationary or growing data. Kalman models the signal as a linear state system driven by white gaussian noise (independent random shocks). He then projects the unknown state orthogonally onto the observations. This gives a recursive linear filter. Its gain comes from a nonlinear difference equation for the error covariance (Theorem 3). The same equations, with time reversed and matrices transposed, solve the noise-free optimal regulator, a control problem with no randomness (Theorem 4). One derivation covers stationary, nonstationary, growing-memory and infinite-memory cases. It also ties estimation to control.

**Prerequisites:** matrix algebra (transpose, inverse, positive definite); expectation, covariance, conditional expectation; vector spaces with an inner product (orthogonality, projection); difference equations; the gaussian distribution.

## L2 — Key ideas (5–10 bullets)
- **Problem and contribution.** Wiener's method (impulse response, spectral factorization) is hard to use. The paper recasts estimation with "state" and "state transition", so one derivation covers many cases, e.g. growing-memory filters (which use all data since the start) (pp. 35–36).
- **Optimal estimate = conditional expectation.** For symmetric, convex-type conditional distributions and any loss of type (2), the optimal estimate is the conditional mean. For squared loss no extra assumptions are needed (Theorem 1, 1-a; p. 37).
- **Projection.** The conditional mean equals the orthogonal projection onto the span of the observations if the processes are gaussian. The projection is also the best *linear* estimate under squared loss (Theorem 2; p. 38).
- **Model.** Random phenomena are treated as linear dynamics driven by independent gaussian noise, $x(t+1)=\Phi x(t)+u(t)$, $y=Mx$. The paper gives reasons for this choice and sets aside how to identify the model (pp. 39–40).
- **Theorem 3.** The optimal estimate is a linear dynamic system $x^*(t+1|t)=\Phi^* x^*(t|t-1)+\Delta^* y(t)$. Its gain $\Delta^*$ comes from the error covariance $P^*$, which obeys the nonlinear recursion (32) (pp. 40–41).
- **The filter is a feedback system.** The innovation $\tilde y(t|t-1)$ (our label: the part of the new measurement orthogonal to the past ones) is a white (orthogonal) sequence. The author says this is apparently the first rigorous proof that every Wiener filter is realizable by feedback (Remark (m), p. 42).
- **Duality (Theorem 4).** Substituting $X(t_0+\tau)\to \hat X'(T-\tau)$ turns the filter recursions (28–30) into the regulator recursions (35–37) (p. 42).
- **Worked cases.** Two examples are solved in closed form: signal plus white noise, and a constant-velocity particle with correlated noise. For $t\gg1$ and $\phi_{33}=0$ the second gives a result the author says is identical to those of Shinbrot and Solodovnikov (pp. 43–44).
- **Open items.** Stability, convergence, continuous-time form and the joint identification of model and filter are deferred or not studied (Remarks (i), (j), p. 41–42; p. 40).

## L3 — Walkthrough

### Abstract and Introduction (pp. 35–36)
The paper re-examines the classical filtering and prediction problem. It uses the Bode–Shannon representation of random processes and the state-transition method for dynamic systems (p. 35). The author claims three new results (p. 35):
1. The method applies unchanged to stationary and nonstationary statistics, and to growing-memory and infinite-memory filters.
2. A nonlinear difference (or differential) equation is derived for the covariance matrix of the optimal estimation error. The filter coefficients follow from its solution without further calculation.
3. The filtering problem is the dual of the noise-free regulator problem.

**Background.** Wiener showed that prediction and signal–noise separation lead to the Wiener–Hopf integral equation. He solved it by spectral factorization for stationary statistics and rational spectra. Others extended this (Zadeh–Ragazzini, Booton, Darlington, Davis and others; p. 35).

**Four limitations of Wiener's method** (p. 35):
1. The filter is specified by an impulse response, which is hard to synthesize.
2. Numerical computation is awkward and gets worse with complexity.
3. Generalizations need new derivations.
4. The mathematics is not transparent.

**Highlights (5)–(9)** (pp. 35–36):
- (5) The problem is approached through conditional distributions and expectations. All results need only first- and second-order averages.
- (6) Random signals are represented, up to second-order statistics, as outputs of linear dynamic systems excited by white noise. These systems are described by first-order difference or differential equations (state and state transition).
- (7) A nonlinear difference equation for the covariance of the optimal error is "vaguely analogous" to the Wiener–Hopf equation. Its solution starts at $t_0$, the time of the first observation. It gives at once the (generally time-varying) filter coefficients.
- (8) The Wiener problem is the dual of the noise-free optimal regulator problem. The author says the identical mathematics "has been suspected all along", but the analogy had not been made explicit.
- (9) The method is most powerful for theory and for machine computation. Two nonstationary prediction examples are solved in closed form.

Only Theorems 3 and 4 are original. The rest reviews known material (p. 36).

### Notation conventions (p. 36)
- Time is discrete, with sampling period chosen as 1, so $t, t_0, \tau, T$ are integers. The author says the restriction is not essential from the engineering viewpoint.
- Vectors are lowercase bold, matrices uppercase bold, and the prime means transpose.
- $x'y=\sum x_iy_i$ is the scalar product. $xy'$ is the $m\times n$ matrix with elements $x_iy_j$.
- $x'Qx=\sum_{i,j}x_iq_{ij}x_j$ is the quadratic form.
- $Ex$ is the expected value. $Exy'$ has elements $E(x_iy_j)$.
- Principal symbols: $y(t)$ observed variable, $x^*(t_1|t)$ optimal estimate, $\mathcal Y(t)$ span of $y(t_0),\dots,y(t)$, $\bar x(t_1|t)$ orthogonal projection, $\tilde x(t_1|t)$ component orthogonal to $\mathcal Y(t)$ (p. 36).

### Optimal Estimates (pp. 36–37)
**Setting.** Signal $x_1(t)$ and noise $x_2(t)$; only $y(t)=x_1(t)+x_2(t)$ is observed. Given $y(t_0),\dots,y(t)$, estimate $x_1(t_1)$. If $t_1<t$ this is data smoothing (interpolation). If $t_1=t$ it is filtering. If $t_1>t$ it is prediction. The collective term is *estimation* (p. 36).

**Conditional distribution** (p. 37):
$$Pr[x_1(t_1)\le \xi_1\,|\,y(t_0)=\eta(t_0),\dots,y(t)=\eta(t)]=F(\xi_1)\tag{1}$$
$F$ carries all the information the measurements give about $x_1(t_1)$. Any estimate $X_1(t_1|t)$ is a function of the observed variables.

**Loss function** (p. 37): the error is $\epsilon=x_1(t_1)-X_1(t_1)$. The loss must be positive and nondecreasing in $|\epsilon|$:
$$L(0)=0;\quad L(\epsilon_2)\ge L(\epsilon_1)\ge0\ \text{ when }\epsilon_2\ge\epsilon_1\ge0;\quad L(\epsilon)=L(-\epsilon)\tag{2}$$
Examples: $a\epsilon^2,\ a\epsilon^4,\ a|\epsilon|,\ a[1-\exp(-\epsilon^2)]$.

**Risk:**
$$E\{L[x_1(t_1)-X_1(t_1)]\}=E\big[E\{L[x_1(t_1)-X_1(t_1)]\,|\,y(t_0),\dots,y(t)\}\big]\tag{3}$$
The outer expectation does not depend on the choice of $X_1$. So minimizing (3) is equivalent to minimizing the inner conditional expectation:
$$E\{L[x_1(t_1)-X_1(t_1)]\,|\,y(t_0),\dots,y(t)\}\tag{4}$$

**Theorem 1.** Assume $L$ is of type (2) and the conditional distribution $F(\xi)$ is
- (A) symmetric about its mean $\bar\xi$: $F(\xi-\bar\xi)=1-F(\bar\xi-\xi)$;
- (B) convex for $\xi\le\bar\xi$: $F(\lambda\xi_1+(1-\lambda)\xi_2)\le\lambda F(\xi_1)+(1-\lambda)F(\xi_2)$ for all $\xi_1,\xi_2\le\bar\xi$, $0\le\lambda\le1$.

Then the estimate minimizing the average loss (3) is the conditional expectation
$$x_1^*(t_1|t)=E[x_1(t_1)\,|\,y(t_0),\dots,y(t)]\tag{5}$$
The proof (credited to Sherman [25]) says this follows from a well-known lemma in probability theory (p. 37).

- **Corollary.** If $\{x_1\},\{x_2\},\{y\}$ are gaussian, Theorem 1 holds. Conditional distributions of gaussian processes are gaussian (Theorem 5(A)), so the requirements are met (p. 37).
- **Theorem 1-a.** If $L(\epsilon)=\epsilon^2$, Theorem 1 holds without (A) and (B). Expand (4): $E[x_1^2|\cdot]-2X_1E[x_1|\cdot]+X_1^2$. Differentiate in $X_1$. The author calls this not fully rigorous and points to Doob [15] for a rigorous proof (p. 37).
- **Remarks.** (a) It is not known what the most general class of processes is for which the conditional distribution meets Theorem 1's requirements. (b) The author says many sources state that general loss functions like (2) cannot be handled conveniently. (c) For vector-valued $x$ with $y=Mx$ ($M$ singular), Theorem 1 holds if $F(\xi_1,\dots,\xi_n)$ is symmetric about the mean in the $n$ variables and convex where all $\xi_i-\bar\xi_i$ are negative (p. 37).

*Intuition note.* Under squared loss, the best guess of the hidden signal given the data is its conditional average. For other losses the same holds when the posterior is symmetric and suitably shaped (Theorem 1 gives these as sufficient conditions, not as necessary ones). Gaussian posteriors always qualify.

### Orthogonal Projections (pp. 37–38)
**Motivation.** The explicit calculation of the optimal estimate is in general impossible. The exception is when the processes are gaussian. Requiring a *linear* estimate with $L=\epsilon^2$ gives the same estimate as the gaussian optimum. So nonlinear estimation can beat linear estimation only if (i) the processes are nongaussian, and (ii) even then only by using at least third-order distributions (p. 37).

**Construction** (pp. 37–38):
- All linear combinations $\sum_{i=t_0}^t a_iy(i)$ form a vector space $\mathcal Y(t)$ (6). Here "vector" means a point of this space, not a vector-valued variable.
- $u,v\in\mathcal Y(t)$ are orthogonal if $Euv=0$. By Schmidt orthogonalization there is an orthonormal basis $e_{t_0},\dots,e_t$:
$$Ee_ie_j=\delta_{ij}\quad(i,j=t_0,\dots,t)\tag{7}$$
- Any $\bar x=\sum a_ie_i$ in $\mathcal Y(t)$ has coefficients
$$E\bar xe_j=E\Big(\sum_i a_ie_i\Big)e_j=\sum_i a_iEe_ie_j=\sum_i a_i\delta_{ij}=a_j\tag{8}$$
- Any random variable $x$ decomposes uniquely as
$$x=\bar x+\tilde x=\sum_{i=t_0}^t(Exe_i)e_i+\tilde x\tag{9}$$
  with $\bar x\in\mathcal Y(t)$. To check $\tilde x\perp\mathcal Y(t)$: $E\tilde xe_i=E(x-\bar x)e_i=Exe_i-E\bar xe_i$. Coordinates are unique, so $Exe_i=E\bar xe_i$. Hence $E\tilde xe_i=0$.
- $\bar x$ is the *orthogonal projection* of $x$ on $\mathcal Y(t)$. It is also the linear function of the observations that minimizes the quadratic loss. For any other $\bar w\in\mathcal Y(t)$, since $\tilde x\perp \bar x-\bar w$:
$$E(x-\bar w)^2=E(x-\bar x)^2+E(\bar x-\bar w)^2\ge E(x-\bar x)^2\tag{10}$$
  So any other minimizer equals $\bar x$ except on a set of probability zero.

**Theorem 2.** Let $\{x(t)\},\{y(t)\}$ have zero mean. We observe $y(t_0),\dots,y(t)$. If either (A) the processes are gaussian, or (B) the optimal estimate is restricted to be a linear function of the observations and $L(\epsilon)=\epsilon^2$, then
$$x^*(t_1|t)=\text{optimal estimate of }x(t_1)\text{ given }y(t_0),\dots,y(t)=\text{orthogonal projection }\bar x(t_1|t)\text{ of }x(t_1)\text{ on }\mathcal Y(t)\tag{11}$$
Notation: $\bar x(t_1|t)=\hat E[x(t_1)|\mathcal Y(t)]$; $\hat E$ is "motivated" by the fact that for gaussian processes projection equals conditional expectation (p. 38).

*Proof outline* (p. 38): the case of linear estimation with quadratic loss follows from (10). For the gaussian case, $\tilde x(t_1|t)$ has zero mean and is orthogonal to the observations. Orthogonal zero-mean gaussian variables are independent (Theorem 5(B)). So
$$0=E\tilde x(t_1|t)=E[\tilde x(t_1|t)|y(t_0),\dots,y(t)]=E[x(t_1)|y(t_0),\dots,y(t)]-\bar x(t_1|t)$$
Hence the conditional expectation equals the projection. (The labels (A)/(B) in the printed proof are swapped relative to the theorem; see Reading notes.)

**Remarks (d)–(g)** (p. 38):
- (d) A rigorous version as $t\to\infty$ needs Hilbert-space theory.
- (e) If one trusts gaussianity, the projection is optimal for all reasonable loss functions. If one doubts it and only considers linear estimates, projections are *not* optimal for many reasonable losses. The author says it is hard to decide how broad Theorem 2 is, because the degree of gaussianness of physical processes is hard to establish.
- (f) The vector-valued case follows by taking all linear combinations $\sum_i\sum_{j=1}^m a_{ij}y_j(i)$.
- (g) Theorem 2 says that under condition (A) or (B) the optimal estimate is a linear combination of all past observations, i.e. the output of a linear filter. It gives a way to compute the impulse response, but the author does not give explicit formulas because the impulse response is not a complete solution.

*Intuition note.* Think of random variables as arrows. Zero correlation (for zero-mean variables) plays the role of a right angle. The best linear guess is the shadow of the unknown arrow on the plane spanned by the data. What is left over is perpendicular to every datum, so no linear combination of the data explains it any further.

### Models for Random Processes (pp. 38–40)
**Assumptions.**
- Useful results need a separation of causes and effects (causality) (p. 38).
- The author says it is "fairly generally accepted" that primary macroscopic sources of randomness are independent gaussian processes. Footnote 5 gives the reasons: macroscopic effects are superpositions of many microscopic ones, and microscopic events are fast, so the sources look independent on a macroscopic time scale. The example is resistor thermal noise (p. 39).
- Observed correlation in time is explained by a dynamic system between source and observer. Gaussian signals stay gaussian through a linear system (Theorem 5(A)). If the source is independent gaussian and the observed signal is gaussian, the system between them may be assumed linear (p. 39).
- Given any process with known first and second-order averages, a gaussian process with the same averages exists (Theorem 5(C)). So gaussian distributions and linear dynamics are "natural, mutually plausible" assumptions when data are scant (p. 39).

**State.** The *state* is the least amount of data about the past needed to predict the future behavior. Dynamics are described by state transitions (p. 39).

**Linear system** (p. 39):
$$\frac{dx}{dt}=F(t)x+D(t)u(t),\qquad y(t)=M(t)x(t)\tag{12}$$
Shapes: $x$ is an $n$-vector (the state); $u$ an $m$-vector ($m\le n$); $F$ is $n\times n$; $D$ is $n\times m$; $y$ a $p$-vector; $M$ is $p\times n$ ($p\le n$). If all coefficients are constant, the system is stationary (time-invariant). Fig. 1 is the matrix block diagram.

**Discretization.** If (12) is stationary and $u$ is constant within each sampling period, $u(t+\tau)=u(t)$ for $0\le\tau<1$ (13), then
$$x(t+1)=\Phi(1)x(t)+\Delta(1)u(t),\quad \Phi(1)=\exp F=\sum_{i=0}^\infty F^i/i!\ (F^0=I),\quad \Delta(1)=\Big(\int_0^1\exp F\tau\,d\tau\Big)D$$
For the nonstationary case:
$$x(t+1)=\Phi(t+1;t)x(t)+\Delta(t)u(t),\quad y(t)=M(t)x(t)\tag{14}$$
Here $\Phi(t+1;t)$ and $\Delta(t)$ cannot in general be given in closed form.

**Transition matrix** $\Phi(t_2;t_1)$ takes the state from time $t_1$ to $t_2$ (p. 39):
- $\Phi(t;t)=I$.
- Stationary case: $\Phi(t+1;t)=\Phi(1)$ is constant, and $\Phi(t;\tau)=\exp F(t-\tau)$.
- Product rule: $\Phi(t;s)\Phi(s;r)=\Phi(t;r)$.
- Inverse rule: $\Phi^{-1}(t;s)=\Phi(s;t)$.

**Model used throughout:**
$$x(t+1)=\Phi(t+1;t)x(t)+u(t)\tag{15}$$
$\{u(t)\}$ is an independent gaussian vector process with $Eu(t)=0$, $Eu(t)u'(s)=0$ for $t\ne s$, and $Eu(t)u'(t)=Q(t)$. Then $x(t)$ is a zero-mean gaussian process, but no longer independent (p. 39). In the steady state (stable system, initial state neglected),
$$x(t)=\sum_{r=-\infty}^{t-1}\Phi(t;r+1)u(r)$$
and for $t\ge s$:
$$Ex(t)x'(s)=\sum_{r=-\infty}^{s-1}\Phi(t;r+1)Q(r)\Phi'(s;r+1)$$
(p. 40).

**Scope limit.** Real life is usually reversed: one has estimates of the covariance $Ex(t)x'(s)$ and must obtain (15) and $Q$. The author calls this "a subtle and presently largely unsolved problem". He starts from the model and treats obtaining it as a separate question. He says model and filter should ideally be optimized jointly, but he knows of no study of that (p. 40).

### Solution of the Wiener Problem (pp. 40–42)
**Problem I** (p. 40). Dynamic model:
$$x(t+1)=\Phi(t+1;t)x(t)+u(t)\tag{16}$$
$$y(t)=M(t)x(t)\tag{17}$$
$u(t)$ is independent gaussian ($n$-vectors, zero mean); $x$ is an $n$-vector; $y$ a $p$-vector ($p\le n$). $\Phi$ ($n\times n$) and $M$ ($p\times n$) are nonrandom functions of time. Given $y(t_0),\dots,y(t)$, find $x^*(t_1|t)$ minimizing the expected loss.

Problem I covers filtering, prediction and smoothing. It also covers reconstructing all state variables of a linear system from observations of only some of them ($p<n$) (p. 40).

By Theorem 2 (the source writes "Theorem 2-a"), the solution is the orthogonal projection of $x(t_1)$ on $\mathcal Y(t)$. It is to be computed by a linear, not necessarily stationary, dynamic system of the form (14) (p. 40).

**Derivation** (pp. 40–41). *Skip path:* carry forward the result (21)–(22) and the covariance recursion (24), then (25).

1. *Innovation.* Suppose $\mathcal Y(t-1)$ is known and $y(t)$ is now measured. Let $\tilde y(t|t-1)$ be the component of $y(t)$ orthogonal to $\mathcal Y(t-1)$. It generates a manifold $\mathcal Z(t)$, and $\mathcal Y(t-1)$ and $\mathcal Z(t)$ together span $\mathcal Y(t)$, with $\mathcal Z(t)\perp\mathcal Y(t-1)$. If $\tilde y(t|t-1)=0$ the measurement carries no new information. The author says this is unlikely in a physically meaningful case (p. 40).
2. *Induction* (p. 40). Assume $x^*(t_1-1|t-1)$ is known. Then
$$x^*(t_1|t)=\hat E[x(t_1)|\mathcal Y(t)]=\hat E[x(t_1)|\mathcal Y(t-1)]+\hat E[x(t_1)|\mathcal Z(t)]$$
$$=\Phi(t+1;t)x^*(t_1-1|t-1)+\hat E[u(t_1-1)|\mathcal Y(t-1)]+\hat E[x(t_1)|\mathcal Z(t)]\tag{18}$$
(written as printed; the transition matrix expected here is $\Phi(t_1;t_1-1)$, see Reading notes).
3. *Reduction to $t_1=t+1$.* Let $t_1=t+s$. If $s\ge0$, $u(t_1-1)$ is independent of $\mathcal Y(t-1)$ and has zero mean, so the middle term of (18) vanishes. If $s<0$ there are "considerable complications". The author treats only $t_1\ge t$, and it suffices to treat $t_1=t+1$, since other cases reduce to it (p. 40).
4. The last term is a linear operation on $\tilde y(t|t-1)$:
$$\hat E[x(t+1)|\mathcal Z(t)]=\Delta^*(t)\tilde y(t|t-1)\tag{19}$$
   $\Delta^*(t)$ is $n\times p$; the star means "optimal filtering".
5. The component of $y(t)$ in $\mathcal Y(t-1)$ is $\bar y(t|t-1)=M(t)x^*(t|t-1)$. Hence
$$\tilde y(t|t-1)=y(t)-\bar y(t|t-1)=y(t)-M(t)x^*(t|t-1)\tag{20}$$
6. Combining (18)–(20) (Fig. 3):
$$x^*(t+1|t)=\Phi^*(t+1;t)x^*(t|t-1)+\Delta^*(t)y(t)\tag{21}$$
$$\Phi^*(t+1;t)=\Phi(t+1;t)-\Delta^*(t)M(t)\tag{22}$$
   The optimal estimator is a linear dynamic system of form (14). Its state is the previous estimate, its input is the last measurement, and its transition matrix is (22). Building it needs only the model of the random process and the operator $\Delta^*$.
7. *Error dynamics.* $\tilde x(t+1|t)=x(t+1)-x^*(t+1|t)=\Phi x(t)+u(t)-\Phi^*x^*(t|t-1)-\Delta^*Mx(t)$. This equals $\Phi^*(t+1;t)\tilde x(t|t-1)+u(t)$ (23) (the last step uses $\Phi-\Delta^*M=\Phi^*$ from (22) and $x-x^*=\tilde x$, so $\Phi x-\Delta^*Mx-\Phi^*x^*=\Phi^*(x-x^*)$; added step).
8. *Covariance recursion.* $u(t)$ is independent of $\tilde x(t|t-1)$, so with $P^*(t)=E\tilde x(t|t-1)\tilde x'(t|t-1)$ and $Q(t)=Eu(t)u'(t)$:
$$P^*(t+1)=E\tilde x(t+1|t)\tilde x'(t+1|t)=\Phi^*P^*(t)\Phi^{*\prime}+Q(t)=\Phi^*(t+1;t)P^*(t)\Phi'(t+1;t)+Q(t)\tag{24}$$
   The source passes from $\Phi^{*\prime}$ to $\Phi'$ without comment. (Added step: the two are equal because (28) below gives $\Phi^*PM'=\Phi PM'-\Delta^*MPM'=0$, so $\Phi^*P\Phi^{*\prime}=\Phi^*P\Phi'-\Phi^*PM'\Delta^{*\prime}=\Phi^*P\Phi'$.)
9. *Finding $\Delta^*$.* The error $x(t+1)-\hat E[x(t+1)|\mathcal Z(t)]$ is orthogonal to $\tilde y(t|t-1)$. By (19):
$$0=E[x(t+1)-\Delta^*(t)\tilde y(t|t-1)]\tilde y'(t|t-1)=Ex(t+1)\tilde y'(t|t-1)-\Delta^*(t)E\tilde y(t|t-1)\tilde y'(t|t-1)$$
   The source then rewrites this, using orthogonality, the definition of $P^*$ and (17), as
$$0=E\tilde x(t+1|t-1)\tilde y'(t|t-1)-\Delta^*(t)M(t)P^*(t)M'(t)$$
   Substitute $\tilde x(t+1|t-1)=\Phi(t+1;t)\tilde x(t|t-1)+u(t|t-1)$ and use the independence of $u(t)$ from $x(t)$:
$$0=\Phi(t+1;t)P^*(t)M'(t)-\Delta^*(t)M(t)P^*(t)M'(t)$$
10. $M P^* M'$ ($p\times p$) is positive definite, hence invertible, whenever $P^*$ is positive definite and no row of $M(t)$ is linearly dependent on the others. In other words, no observed scalar $y_i$ is a linear combination of the others. Then
$$\Delta^*(t)=\Phi(t+1;t)P^*(t)M'(t)[M(t)P^*(t)M'(t)]^{-1}\tag{25}$$
11. *Start.* Observations begin at $t_0$, so $\tilde x(t_0|t_0-1)=x(t_0)$, and one must specify $P^*(t_0)=Ex(t_0)x'(t_0)$. If it is positive definite, (25) gives $\Delta^*(t_0)$, then (22) gives $\Phi^*(t_0+1;t_0)$, and (24) gives $P^*(t_0+1)$. If $Q(t)$ is positive definite, all $P^*(t)$ are positive definite, so the requirement in (25) holds at each step (p. 41).
12. *Removing $t_1=t+1$.* Since $u(t)$ is orthogonal to $\mathcal Y(t)$, $x^*(t+1|t)=\Phi(t+1;t)x^*(t|t)$. If $\Phi$ has an inverse (always so for the transition matrix of a differential-equation system), $x^*(t|t)=\Phi(t;t+1)x^*(t+1|t)$. For $s\ge1$, repeated use of (16) writes $x(t+s)$ as $\Phi(t+s;t+1)x(t+1)$ plus terms in $u(t+1),\dots,u(t+s-1)$. Those are orthogonal to $\mathcal Y(t)$, so $x^*(t+s|t)=\Phi(t+s;t+1)x^*(t+1|t)$ for $s\ge1$. For $s<0$ the results are "similar", but the estimate has $(1-s)(n-p)$ coordinates, as printed (p. 41).

**Theorem 3 (Solution of the Wiener Problem)** (p. 41). Consider Problem I.
- The optimal estimate $x^*(t+1|t)$ of $x(t+1)$ given $y(t_0),\dots,y(t)$ is generated by the linear dynamic system (21).
- The estimation error obeys (23).
- Error covariance and expected quadratic loss:
$$\operatorname{cov}\tilde x(t|t-1)=E\tilde x(t|t-1)\tilde x'(t|t-1)=P^*(t)\tag{26}$$
$$\sum_{i=1}^nE\tilde x_i^2(t|t-1)=\operatorname{trace}P^*(t)\tag{27}$$
- For $t\ge t_0$ the matrices are generated by:
$$\Delta^*(t)=\Phi(t+1;t)P^*(t)M'(t)[M(t)P^*(t)M'(t)]^{-1}\tag{28}$$
$$\Phi^*(t+1;t)=\Phi(t+1;t)-\Delta^*(t)M(t)\tag{29}$$
$$P^*(t+1)=\Phi^*(t+1;t)P^*(t)\Phi'(t+1;t)+Q(t)\tag{30}$$
- One must specify $P^*(t_0)$ and $Q(t)$. For $s\ge0$, if $\Phi$ is invertible:
$$x^*(t+s|t)=\Phi(t+s;t+1)x^*(t+1|t)=\Phi(t+s;t+1)\Phi^*(t+1;t)\Phi(t;t+s-1)x^*(t+s-1|t-1)+\Phi(t+s;t+1)\Delta^*(t)y(t)\tag{31}$$
  so the estimate is again given by a linear dynamic system of type (21).

*Shapes:* $\Phi,\Phi^*,P^*,Q$ are $n\times n$; $M$ is $p\times n$; $\Delta^*$ is $n\times p$; $MP^*M'$ is $p\times p$.

*Intuition note.* At each step the filter predicts the next measurement from its current estimate and compares it with the real one. It corrects its estimate by $\Delta^*$ times the surprise. By (28), $\Delta^*$ grows with $P^*M'$, i.e. with the prior error as seen through the measurement. The covariance recursion does not depend on the data, so $\Delta^*$ can be computed in advance.

**Remarks (h)–(m)** (pp. 41–42):
- (h) Eliminating $\Delta^*$ and $\Phi^*$ gives a nonlinear difference equation for $P^*$:
$$P^*(t+1)=\Phi(t+1;t)\{P^*(t)-P^*(t)M'(t)[M(t)P^*(t)M'(t)]^{-1}M(t)P^*(t)\}\Phi'(t+1;t)+Q(t)\quad(t\ge t_0)\tag{32}$$
  (Added step: substitute (28) and (29) into (30).) It is linear only if $M$ is invertible. Then all of $x$ is observed and $P^*(t+1)=Q(t)$, so the problem is trivial. Equation (32) plays a role analogous to the Wiener–Hopf equation, and solving it is "a much simpler task". Once $P^*$ is computed from $t_0$, the filter follows from (29)–(30).
- (i) Theorem 3 does not settle everything. The physical meaning of the assumptions behind (25), the convergence and stability of (32), and the stability of filter (21) are not treated. The author says these can be done "in a completely satisfactory way" but leaves them to a future paper [29], where duality is the main tool.
- (j) Letting the sampling period go to zero would give a differential equation for the filter. This requires the logarithm of $\Phi^*$, which exists only if $\Phi^*$ is nonsingular. It is not, because the optimal filter needs only $n-p$ state variables. By modifications, (22) can be reduced to $n-p$ equations with a nonsingular transition matrix. Details are promised for later publications.
- (k) Filter (21) is in general nonstationary, because $\Phi$ and $M$ may depend on time and because estimation improves as data accumulate. If $\Phi,M$ are constants, it "can be shown" that (21) becomes stationary as $t\to\infty$. This is the classical Wiener case.
- (l) The derivation is unaffected by nonstationarity or finite data. The only earlier explicit recursions for the growing-memory filter are Blum's [12], which the author says are much more complicated.
- (m) By Fig. 3 the optimal filter is a feedback system. The signal after the first summer is white noise, since $\tilde y(t|t-1)$ is an orthogonal process. The author says this is apparently the first rigorous proof that every Wiener filter is realizable by a feedback system. He adds that another paper will show such a filter is always stable under very mild assumptions on (16–17).

### The Dual Problem (pp. 42–43)
**Problem II (noise-free regulator)** (p. 42). Dynamic system
$$x(t+1)=\hat\Phi(t+1;t)x(t)+\hat M(t)u(t)\tag{33}$$
$x$ is an $n$-vector; $u$ an $m$-vector ($m\le n$); $\hat\Phi,\hat M$ are $n\times n$, $n\times m$ and nonrandom. Given $x(t)$, find $u(t),\dots,u(T)$ minimizing
$$V[x(t)]=\sum_{\tau=t}^{T+1}x'(\tau)\hat Q(\tau)x(\tau)$$
with $\hat Q$ positive definite. No probability enters. It is implicitly assumed that every state variable can be measured exactly at each instant. $T\ge t$ is the terminal time (possibly infinity).

**Known solution** (the author's earlier work [18], after a change of notation): the optimal controls are nonstationary linear functions of the state,
$$u^*(t)=-\hat\Delta^*(t)x(t)\tag{34}$$
Closed loop (Fig. 4): $x(t+1)=\hat\Phi^*(t+1;t)x(t)$, and the minimum index is $V^*[x(t)]=x'(t)\hat P^*(t-1)x(t)$. With $t\le T$:
$$\hat\Delta^*(t)=[\hat M'(t)\hat P^*(t)\hat M(t)]^{-1}\hat M'(t)\hat P^*(t)\hat\Phi(t+1;t)\tag{35}$$
$$\hat\Phi^*(t+1;t)=\hat\Phi(t+1;t)-\hat M(t)\hat\Delta^*(t)\tag{36}$$
$$\hat P^*(t-1)=\hat\Phi^{*\prime}(t+1;t)\hat P^*(t)\hat\Phi^*(t+1;t)+\hat Q(t)\tag{37}$$
with the initial condition $\hat P^*(T)=\hat Q(T+1)$.

**Theorem 4 (Duality Theorem).** Problems I and II are duals in this sense. Let $\tau\ge0$. Replace every matrix $X(t)=X(t_0+\tau)$ in (28–30) by $\hat X'(t)=\hat X'(T-\tau)$; then one has (35–37). Conversely, replace every $\hat X(T-\tau)$ in (35–37) by $X'(t_0+\tau)$; then one has (28–30). The proof is to carry out the substitutions (p. 42).

**Table 1 (dictionary)** (p. 42):

| Problem I | Problem II |
|---|---|
| $x(t)$ unobservable state variables of the random process | $x(t)$ observable state variables of the plant |
| $y(t)$ observed random variables | $u(t)$ control variables |
| $t_0$ first observation | $T$ last control action |
| $\Phi(t_0+\tau+1;t_0+\tau)$ transition matrix | $\hat\Phi(T-\tau+1;T-\tau)$ transition matrix |
| $P^*(t_0+\tau)$ covariance of optimized estimation error | $\hat P^*(T-\tau)$ matrix of the quadratic form for the performance index under optimal regulation |
| $\Delta^*(t_0+\tau)$ weighting of observation | $\hat\Delta^*(T-\tau)$ weighting of state for optimal control |
| $\Phi^*$ transition matrix for the optimal estimation error | $\hat\Phi^*$ transition matrix under optimal regulation |
| $M(t_0+\tau)$ effect of state on observation | $\hat M(T-\tau)$ effect of control vectors on state |
| $Q(t_0+\tau)$ covariance of random excitation | $\hat Q(T-\tau)$ matrix of the quadratic form defining the error criterion |

**Remarks (n)–(q)** (pp. 42–43):
- (n) Mathematically, both problems reduce to the Wiener–Hopf-like equation (32).
- (o) The physical meaning is "intriguing": the text asks why observations and control are dual quantities. The author says recent research [29] has shown that the essence lies in the duality of constraints at the output (matrix $M$ in Problem I) and at the input ($\hat M$ in Problem II).
- (p) Wiener's methods have long been applied to the noise-free regulator (Newton, Gould, Kaiser [27]). The connection and the duality had apparently not been stated precisely before.
- (q) Duality is a powerful tool for deepening the *theory* of Wiener filters (as opposed to computation), to be published elsewhere.

*Intuition note.* Estimating hidden states from outputs and steering states with inputs use the same matrix recursion. One runs forward in time, the other backward. Swap $\Phi\to\hat\Phi'$ and $M\to\hat M'$ and the algebra is identical.

### Applications (pp. 43–44)
For numerical data one simply iterates (28–30). Closed forms are hard in general, so two examples are given (p. 43).

**Example 1 (signal plus white noise)** (p. 43). Model (written with $x_2$ as noise):
$$x_1(t+1)=\phi_{11}(t+1;t)x_1(t)+u_1(t),\quad x_2(t+1)=u_2(t),\quad y_1(t)=x_1(t)+x_2(t)$$
Data: $t_1=t+1$, $t_0=0$; $Ex_1^2(0)=0$ (so $x_1(0)=0$); $Eu_1^2=a^2$, $Eu_2^2=b^2$, $Eu_1u_2=0$; $\phi_{11}$ constant. The following satisfy (28–30) for all $t\ge t_0$:
$$\Delta^*(t)=\begin{bmatrix}\phi_{11}C(t)\\0\end{bmatrix},\quad \Phi^*(t+1;t)=\begin{bmatrix}\phi_{11}[1-C(t)]&0\\0&0\end{bmatrix},\quad P^*(t+1)=\begin{bmatrix}a^2+\phi_{11}^2b^2C(t)&0\\0&b^2\end{bmatrix}$$
$$C(t+1)=1-\frac{b^2}{a^2+b^2+\phi_{11}^2b^2C(t)},\quad t\ge0\tag{38}$$
- *Check (added):* with $p=P^*_{11}(t)$, $C(t)=p/(p+b^2)$, and (30) gives $p(t+1)=a^2+\phi_{11}^2b^2C(t)$. Then $C(t+1)=p(t+1)/(p(t+1)+b^2)$ reproduces (38).
- $x_1(0)=0$ is known, so neither $x_1(1)$ nor $\tilde x_1(1)$ can be predicted from $y_1(0)$. The measurement at $t=0$ is useless, so $C(0)=0$. This and (38) determine $C(t)$. Equation (38) "plays the role of the Wiener–Hopf equation".
- If $b^2/a^2\ll1$, then $C\cong1$, "essentially pure prediction". If $b^2/a^2\gg1$, then $C\cong0$: the filter relies mainly on $x_1^*(t|t-1)$ and gives the measurement very small weight, as expected for very noisy data (p. 43).
- $x_2^*(t|t-1)=0$ always, since one cannot predict independent noise. So $\phi^*_{12}$ can be set to zero, and the optimal predictor is first-order. For the stationary Wiener filter, put $t=\infty$ in (38) and solve the resulting quadratic (p. 43).

**Example 2 (particles with constant unknown velocity)** (p. 43). Particles leave the origin at $t_0=0$ with random velocities. Then each moves at constant velocity. One particle's position is measured with stationary additive correlated noise. Estimate position and velocity at the time of the last measurement. Let $x_1$ be position, $x_2$ velocity, $x_3$ noise:
$$x_1(t+1)=x_1(t)+x_2(t),\quad x_2(t+1)=x_2(t),\quad x_3(t+1)=\phi_{33}(t+1;t)x_3(t)+u_3(t),\quad y_1(t)=x_1(t)+x_3(t)$$
Conditions: $t_1=t$, $t_0=0$; $Ex_1^2(0)=Ex_2(0)=0$, $Ex_2^2(0)=a^2>0$; $Eu_3=0$, $Eu_3^2=b^2$; $\phi_{33}$ constant (see Reading notes on condition 2).
- One-step prediction. With $a^2$ the initial velocity variance and $b^2$:
$$P^*(1)=\begin{bmatrix}a^2&a^2&0\\a^2&a^2&0\\0&0&b^2\end{bmatrix},\quad\Delta^*(0)=\begin{bmatrix}0\\0\\1\end{bmatrix}$$
- Substitution into (28–30) verifies that, for all $t\ge1$,
$$P^*(t)=\frac{b^2}{C_1(t-1)}\begin{bmatrix}t^2&t&-\phi_{33}t(t-1)\\t&1&-\phi_{33}(t-1)\\-\phi_{33}t(t-1)&-\phi_{33}(t-1)&\phi_{33}^2(t-1)^2+C_1(t-1)\end{bmatrix}$$
  with $C_1(0)=b^2/a^2$ and $C_1(t)=C_1(t-1)+[t-\phi_{33}(t-1)]^2$ for $t\ge1$. (Check, added: at $t=1$ this gives the $P^*(1)$ above.) The results hold also when $\phi_{33}$ depends on $t$. The author says the stationary/nonstationary-noise difference in conventional treatments is a misleading impression created by the special methods used there.
- With $C_2(0)=0$ and $C_2(t)=t-\phi_{33}(t-1)$, $t\ge1$, one finds for $t\ge0$ (filtering):
$$\Phi(t;t+1)\Delta^*(t)=\frac1{C_1(t)}\begin{bmatrix}tC_2(t)\\C_2(t)\\C_1(t)-tC_2(t)\end{bmatrix},\qquad \operatorname{cov}\tilde x(t|t)=E\tilde x(t|t)\tilde x'(t|t)=\frac{b^2}{C_1(t)}\begin{bmatrix}t^2&t&-t^2\\t&1&-t\\-t^2&-t&t^2\end{bmatrix}$$
  The author also gives (p. 44), with $C_1,C_2$ evaluated at $t$:
$$\Phi(t;t+1)\Phi^*(t+1;t)\Phi(t+1;t)=\frac1{C_1}\begin{bmatrix}C_1-tC_2&C_1-tC_2&-\phi_{33}tC_2\\-C_2&C_1-C_2&-\phi_{33}C_2\\-C_1+tC_2&-C_1+tC_2&\phi_{33}tC_2\end{bmatrix}$$
- *Large $t$.* $C_1$ obeys approximately $dC_1/dt\cong C_2^2$, hence
$$C_1(t)\cong(1-\phi_{33})^2t^3/3+\phi_{33}(1-\phi_{33})t^2+\phi_{33}^2t+b^2/a^2\quad(t\gg1)\tag{39}$$
  (Check, added: integrate $C_2^2=(1-\phi_{33})^2t^2+2\phi_{33}(1-\phi_{33})t+\phi_{33}^2$.) Then, for $t\gg1$,
$$\Phi^{-1}\Phi^*\Phi\cong\begin{bmatrix}1&1&0\\0&1&0\\-1&-1&0\end{bmatrix},\qquad\Phi^{-1}\Delta^*\cong\begin{bmatrix}0\\0\\1\end{bmatrix}$$
- *Interpretation.* With many observations the filter relies almost exclusively on $x_1^*(t|t),x_2^*(t|t)$ to estimate the next state. Current observations are used almost exclusively to estimate the noise, $x_3^*(t|t)\cong y_1(t)-x_1^*(t|t)$. The author compares this with fitting a straight line to an increasing number of points.
- *Check against literature.* For $t\gg1$ and $\phi_{33}=0$,
$$E\tilde x_1^2(t|t)\cong\frac{a^2b^2t^2}{b^2+a^2t^3/3}$$
  This is identical, says the author, to Shinbrot [11] (Example 1) and Solodovnikov [14] (Example 2), who used an entirely different approach for finite-length continuous data (p. 44). (Check, added: $b^2t^2/C_1$ with $C_1\cong t^3/3+b^2/a^2$.)

### Conclusions (p. 44)
The paper formulates and solves the Wiener problem from the "state" point of view. This gives a very general treatment, including cases that are difficult for other methods. It also shows the Wiener problem to be closely connected with other problems in control theory. The author says much remains to be done to exploit these connections.

### Appendix: Random processes, basic concepts (p. 45)
A review of standard definitions:
- **Random variable** $x$ with distribution function $F_x(\xi)=Pr(x\le\xi)$ and density $f_x=dF_x/d\xi$. Expected value $Eg(x)=\int g(\xi)\,dF_x(\xi)$ (40).
- **Discrete random process** $\{x(t)\}$ (41). A realization is one set of observed values.
- **Uncorrelated:** $Ex(t)x(s)=Ex(t)Ex(s)$ for $t\ne s$. **Orthogonal:** in addition $Ex(t)x(s)=0$. Replacing $x$ by $x-Ex$ makes an uncorrelated process orthogonal. For an orthogonal process, the expected square of a sum is the sum of the expected squares.
- **Covariance matrix** $\operatorname{cov}x=E(x-Ex)(x'-Ex')$ (42).
- **Joint distribution** (43). **Independent** process: joint distribution is the product of the first-order ones. Independent implies uncorrelated, but not conversely. For more than two variables, pairwise independence is not sufficient for independence.
- **Conditional distribution** (44), and the fact that $E[E\{g(x(t_{n+1}))|x(t_1),\dots,x(t_n)\}]=E\{g(x(t_{n+1}))\}$. The integrals need never be evaluated here; only the concept of expectation is used.
- **Gaussian:** $f_x(\xi)=[2\pi E(x-Ex)^2]^{-1/2}\exp[-\tfrac12(\xi-Ex)^2/E(x-Ex)^2]$. For a vector, $f_x(\xi)=(2\pi)^{-n/2}(\det C)^{-1/2}\exp[-\tfrac12(\xi-Ex)'C^{-1}(\xi-Ex)]$.
- **Theorem 5.** (A) Linear functions (hence conditional expectations) on a gaussian process are gaussian. (B) Orthogonal gaussian random variables are independent. (C) Given means and covariances, a unique gaussian process with the same means and covariances exists.

## Toy example (ours, not from the paper)
Position–velocity tracking with $n=2$, $p=1$. Take
$\Phi=\begin{bmatrix}1&1\\0&1\end{bmatrix}$, $M=[1\ \ 0]$, $Q=I$, $P^*(t_0)=I$.
Position is observed; velocity is hidden.

**Step 1.** $P=I$.
- $MPM'=1$ (1×1). $PM'=[1;0]$.
- $\Phi PM'=[1;0]$, so by (28) $\Delta^*=[1;0]/1=[1;0]$ (2×1).
- (29): $\Phi^*=\Phi-\Delta^*M=\begin{bmatrix}1&1\\0&1\end{bmatrix}-\begin{bmatrix}1&0\\0&0\end{bmatrix}=\begin{bmatrix}0&1\\0&1\end{bmatrix}$.
- (30): $\Phi^*P=\begin{bmatrix}0&1\\0&1\end{bmatrix}$ and $\Phi'=\begin{bmatrix}1&0\\1&1\end{bmatrix}$. So $\Phi^*P\Phi'=\begin{bmatrix}1&1\\1&1\end{bmatrix}$, and $P^*(t_0+1)=\begin{bmatrix}1&1\\1&1\end{bmatrix}+I=\begin{bmatrix}2&1\\1&2\end{bmatrix}$.
- Check by (32): $P-PM'(MPM')^{-1}MP=\begin{bmatrix}0&0\\0&1\end{bmatrix}$. Then $\Phi\begin{bmatrix}0&0\\0&1\end{bmatrix}\Phi'=\begin{bmatrix}1&1\\1&1\end{bmatrix}$, giving the same result.

**Step 2.** $P=\begin{bmatrix}2&1\\1&2\end{bmatrix}$.
- $MPM'=2$, $PM'=[2;1]$, $\Phi PM'=[3;1]$, so $\Delta^*=[1.5;0.5]$.
- $\Phi^*=\begin{bmatrix}1-1.5&1\\-0.5&1\end{bmatrix}=\begin{bmatrix}-0.5&1\\-0.5&1\end{bmatrix}$. Check: $\Phi^*PM'=[-1+1;-1+1]=0$.
- $\Phi^*P=\begin{bmatrix}0&1.5\\0&1.5\end{bmatrix}$, so $\Phi^*P\Phi'=\begin{bmatrix}1.5&1.5\\1.5&1.5\end{bmatrix}$ and $P^*(t_0+2)=\begin{bmatrix}2.5&1.5\\1.5&2.5\end{bmatrix}$.
- Trace of $P^*$ (expected squared error, (27)): 2, 4, 5.

**Data update.** Let $x^*(t_0|t_0-1)=[0;0]$ and $y(t_0)=2$. By (21) (with $x^*=0$): $x^*(t_0+1|t_0)=\Delta^*y=[1;0]\cdot2=[2;0]$. Next let $y(t_0+1)=3$. By (21):
$\Phi^*[2;0]+\Delta^*\cdot3=[-1;-1]+[4.5;1.5]=[3.5;0.5]$.
Check with the innovation form: predicted measurement $Mx^*=2$, innovation $\tilde y=3-2=1$, and $\Phi x^*+\Delta^*\tilde y=[2;0]+[1.5;0.5]=[3.5;0.5]$ ✓.

The surprise of +1 in position raises the position estimate by 1.5 and the velocity estimate by 0.5. The velocity is never measured, only inferred through the correlation $P^*_{12}$.

## Concepts
- [[kalman-filter]] — the recursive optimal linear estimator (21)+(28)–(30); the paper does not use this name (p. 41)
- [[kalman-gain]] — $\Delta^*(t)=\Phi P^*M'[MP^*M']^{-1}$, the weight on the innovation in (19); in (21) it multiplies $y(t)$ (p. 41)
- [[state]] — least data about the past needed to predict the future (p. 39)
- [[state-space-model]] — first-order difference or differential equations $x(t+1)=\Phi x+\dots$, $y=Mx$ (p. 39)
- [[observer-state-estimator]] — the filter (21) is a model run in feedback with measurements; the author describes it as a feedback system (Remark (m), p. 42)
- [[duality]] — Theorem 4: filtering Problem I and noise-free regulator Problem II share the same recursions under the Table 1 substitutions (p. 42)
- [[lqr]] — Problem II (noise-free regulator with quadratic index) with solution (34)–(37); not named LQR in the paper (p. 42)
- [[feedback]] — the optimal filter is a feedback system, from inspection of Fig. 3 (p. 42)
- [[transition-matrix]] (new) — $\Phi(t_2;t_1)$ carries the state from $t_1$ to $t_2$; product and inverse rules (p. 39)
- [[orthogonal-projection-estimation]] (new) — the best linear squared-loss estimate is the projection onto the span of the observations (p. 38)
- [[conditional-expectation-optimal-estimate]] (new) — under loss type (2) with symmetric/convex $F$, or squared loss, the optimum is $E[x|y]$ (p. 37)
- [[innovation]] (new) — the part $\tilde y(t|t-1)$ of the new measurement orthogonal to the past; the paper does not use this word (p. 40)
- [[error-covariance-recursion]] (new) — nonlinear difference equation (32) for $P^*(t)$, "analogous" to the Wiener–Hopf equation (p. 41)
- [[random-process-model]] (new) — random signals as outputs of linear dynamic systems driven by independent gaussian noise, model (15) (p. 39)
- [[wiener-filter]] (new) — the classical optimal linear filter, specified by impulse response / Wiener–Hopf equation (p. 35)

## Canonical instances
- [[signal-plus-noise-estimation]] — Example 1: signal $x_1$ plus white noise $x_2$, with recursion (38) for the gain (p. 43)
- [[constant-velocity-particle]] — Example 2: position measurement with correlated noise; closed-form $P^*(t)$ (p. 43)
- [[line-fitting-analogy]] — the large-$t$ behavior is likened to fitting a straight line to more and more points (p. 44)
- [[thermal-noise-resistor]] — noise voltage of a resistor as the example of a primary gaussian random source (p. 39)

## Bridges (candidates)
- [same-math] Theorem 4 duality (filter ↔ noise-free regulator) ↔ control-theory: the LQR design equations — the paper itself gives the substitution $X\to\hat X'(T-\tau)$ between (28–30) and (35–37).
- [structural-analogy] $\Delta^*$ weighting the surprise $y-Mx^*$ ↔ reinforcement learning: a learning rate times a prediction error in temporal-difference updates — both correct an estimate in proportion to the error.
- [structural-analogy] Orthogonal-projection estimate ↔ statistics: least-squares regression as projection onto a span — both minimize squared error by making the residual orthogonal to the regressors.
- [structural-analogy] Hidden state observed through $y=Mx$, with updates over time ↔ computational social science: tracking a latent trait (e.g. opinion) from noisy survey or behavioral series.
- [metaphor] White "innovation" after the first summer ↔ any residual-whiteness diagnostic in time-series model checking.

## Questions this raises
- Under what conditions do $P^*(t)$ converge and the filter stay stable? The author defers both to [29] (Remark (i)).
- How good is the linear filter when the processes are nongaussian? The text says gains require at least third-order distributions (p. 37).
- Where do $\Phi$, $M$ and $Q$ come from in practice? The author says identification is largely unsolved and joint optimization with the filter has not been studied (p. 40).
- Why are observation and control dual? The author calls it "intriguing" and points to constraints at output vs. input (Remark (o)).

## Reading notes
- **Page numbers.** The page labels give no printed number, but the page images show them: printed = pdf + 34 (pdf 1 = p. 35, pdf 11 = p. 45). All references here use printed pages, although the metadata suggested using (pdf N).
- **Edition facts.** R. E. Kalman, *Journal of Basic Engineering*, March 1960 (running header; Transactions of the ASME). Contributed by the Instruments and Regulators Division, presented March 29–April 2, 1959, Paper 59-IRD-11 (p. 35).
- **Theorem 2 proof labels.** The theorem's (A) is "gaussian" and (B) is "linear + quadratic loss". The printed proof says "(A)… consequence of the remarks in connection with (10)" (which is the linear case) and "(B)…" gives the gaussian argument. The labels appear swapped. Remark (e) uses (A) for the gaussian case.
- **"Theorem 2-a."** Cited on p. 40, but no Theorem 2-a appears on these pages (only Theorem 1-a and Theorem 2). Here it is read as Theorem 2.
- **Equation (18).** The printed first term is $\Phi(t+1;t)x^*(t_1-1|t-1)$. For $t_1=t+s$ one would expect $\Phi(t_1;t_1-1)$. Kept as printed.
- **Equation (24).** The printed lines switch from $\Phi^{*\prime}$ to $\Phi'$ without comment; the added step in L3 shows they are equal.
- **Sum before Theorem 3 (p. 41).** The printed coefficient in the sum for $x(t+s)$ appears as $\Phi(t+s;t+r)$. By (16) one would expect $\Phi(t+s;t+r+1)$. Not reproduced in L3; only its conclusion is used.
- **Example 2, condition 2 (p. 43).** The page image reads $Ex_1^2(0)=Ex_2(0)=0$, $Ex_2^2(0)=a^2>0$ (the text layer is garbled here, as "ExS(0)"). The $P^*(1)$ printed on the same page, with $a^2$ in the (1,1), (1,2), (2,2) entries and $b^2$ in (3,3), agrees with $a^2$ being the variance of the velocity $x_2(0)$. The page also says particles have "random velocities". Taken as printed: $a^2$ is the initial velocity variance.
- **OCR.** The text layer is garbled in many equations and in the two $3\times3$ matrices on p. 44. Equations were checked against the images. The $3\times3$ matrix $\Phi^{-1}\Phi^*\Phi$ on p. 44 is legible in the image and is transcribed in L3 (checked against $\Phi-(\Phi^{-1}\Delta^*)M\Phi$ with $M=[1\ 0\ 1]$). Its large-$t$ limit is also given.
- **Terminology.** The paper does not use the words "Kalman filter", "innovation", "Riccati" or "LQR", and uses "observer" only for the person who observes the signal (p. 39), not for a state estimator. These ids are our labels for the paper's constructs.
- **Shape of $M$ in (12) (p. 39).** The text says "$M(t)$ is an $n\times p$ matrix", but $y=Mx$ with $x$ an $n$-vector and $y$ a $p$-vector needs $p\times n$, as Problem I states (p. 40). L3 uses $p\times n$.
