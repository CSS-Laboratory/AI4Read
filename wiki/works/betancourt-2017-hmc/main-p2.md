---
id: betancourt-2017-hmc/main-p2
work: betancourt-2017-hmc
unit: "paper (part 2/3): Sections 3.1 (end) – 5.2 (start)"
pages: 22-40
fields: [bayesian]
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
# Hamiltonian phase space, tuning, and symplectic integration (part 2 of Betancourt's HMC introduction)

## L0 — One line
Adding momentum as a dual variable makes the target's gradient generate trajectories along the typical set. How well these trajectories explore then depends on three choices: the kinetic energy, the integration time and the numerical integrator.

## L1 — The gist (≤ 120 words)
The question is how to turn the target's gradient into efficient exploration of its typical set. The answer is to add auxiliary momentum with a conditional distribution, which gives a Hamiltonian $H=K+V$ and trajectories that stay on energy level sets. A transition is: resample momentum, follow a trajectory, drop the momentum. The unit then says how to tune the kinetic energy and the integration time. In practice, symplectic integrators (volume-preserving numerical solvers) such as leapfrog avoid drift, and a Metropolis–Hastings correction with a momentum flip removes their small bias. This matters because, as the author notes, well-chosen settings let HMC perform well even on challenging high-dimensional problems (p. 26).

**Prerequisites:** typical set; Markov chains and Metropolis–Hastings acceptance ratio; gradients; covariance matrices; ordinary differential equations (basic).

## L2 — Key ideas (5–10 bullets)
- The gradient alone is not aligned with the typical set. Momentum parameters, endowed with a suitable probabilistic structure, twist it into conservative dynamics along the typical set (pp. 22–23).
- The canonical distribution is $\pi(q,p)=\pi(p\mid q)\pi(q)=e^{-H}$ with $H=K+V$. Hamilton's equations turn $\partial V/\partial q$ into trajectories confined to the typical set (p. 25).
- One HMC transition is a random lift (sample $p$), a deterministic trajectory, and a projection back to $q$ (p. 26).
- Phase space foliates (splits) into energy level sets (sets of constant $H$). A chain alternates between deterministic motion within a level set and a random walk across energies (pp. 27–28).
- The kinetic energy (defined by a mass matrix, i.e. a Euclidean or Riemannian metric) is tuned so level sets are as uniform as possible and the energy transition distribution (the distribution of energies after momentum resampling at a fixed $q$) matches the marginal energy distribution (the distribution of energies across level sets) as well as possible. Setting $M^{-1}$ to the target covariance is optimal within the Euclidean-Gaussian family (pp. 30–32).
- The optimal integration time varies across phase space, so static times fail on heavy tails. It should be found dynamically, e.g. with the No-U-Turn criterion (a heuristic stopping rule for trajectory length) (pp. 33–35).
- Most generic ODE solvers drift. Symplectic integrators (numerical solvers that preserve phase-space volume) oscillate near the exact level set; their failures (divergences, where the numerical trajectory flies off toward infinite energy) are easy to detect (pp. 36–38).
- A momentum flip makes the proposal reversible, so a Metropolis–Hastings correction with $\min(1,e^{-\Delta H})$, where $\Delta H=H(q_L,-p_L)-H(q_0,p_0)$, becomes possible (pp. 38–40).

## L3 — Walkthrough

### 3.1 (end) Momentum balances gravity — the satellite analogy
- A satellite with too little transverse momentum crashes into the planet. With too much, it escapes into space (Fig. 16, p. 22).
- With exactly the right momentum the dynamics are conservative: falling in raises momentum and pushes the satellite out; drifting out lowers momentum and gravity pulls it back. The resulting vector field follows the orbit (Fig. 17, pp. 22–23).
- Probabilistic translation: expand the system with auxiliary momentum. It cannot be added arbitrarily; it needs a probabilistic structure that ensures conservative dynamics. The author states that only one procedure does this, HMC (p. 22).

### 3.2 Phase space and Hamilton's equations
- Conservative dynamics preserve volumes in **phase space** (position–momentum space). Compression in position space is balanced by expansion in momentum space (Fig. 18, pp. 22–24).
- Add a momentum $p_n$ to each parameter $q_n$, $q_n\to(q_n,p_n)$. This turns the $D$-dimensional space into a $2D$-dimensional phase space. Momenta must be dual to the parameters, i.e. transform oppositely under reparameterization, so that phase-space volume is invariant (p. 23).
- Lift the target via the **canonical distribution**: $\pi(q,p)=\pi(p\mid q)\,\pi(q)$. Marginalizing out $p$ recovers the target. Trajectories exploring the joint typical set project to trajectories exploring the target typical set (p. 23, Fig. 19, p. 24).
- Because densities also transform oppositely, the canonical density is parameterization-independent and can be written with the **Hamiltonian** (energy at each point):
$$\pi(q,p)=e^{-H(q,p)},\qquad H(q,p)\equiv-\log\pi(q,p).$$
- It decomposes as
$$H(q,p)=-\log\pi(p\mid q)-\log\pi(q)\equiv K(p,q)+V(q).$$
  $K$ is the kinetic energy and $V$ the potential energy. $V$ is fixed by the target. $K$ is unconstrained and must be chosen by the implementation (p. 25).
- Hamilton's equations generate the desired vector field (p. 25):
$$\frac{dq}{dt}=+\frac{\partial H}{\partial p}=\frac{\partial K}{\partial p},\qquad \frac{dp}{dt}=-\frac{\partial H}{\partial q}=-\frac{\partial K}{\partial q}-\frac{\partial V}{\partial q}.$$
- $\partial V/\partial q$ is the gradient of the log target density (as the author describes it). Channeling it through the momentum aligns it with the typical set. Following the field for time $t$ gives trajectories $\phi_t(q,p)$ that move quickly while staying in the typical set (p. 25).

*Intuition note:* Hamilton's equations feed the gradient into the momentum instead of using it to move the parameters directly (p. 25). The author says this fulfils the satellite intuition: the gradient is twisted to align with the typical set. This is the "orbit" of the satellite picture.

### 3.3 The idealized Hamiltonian Markov transition
1. **Lift:** sample $p\sim\pi(p\mid q)$. If $q$ was in the typical set, the lifted point lies in the phase-space typical set.
2. **Flow:** $(q,p)\to\phi_t(q,p)$, which pushes away from the initial point while staying in the joint typical set.
3. **Project:** $(q,p)\to q$ (p. 26).
- Fig. 20 (p. 27) shows these steps. In the tails, momentum resampling and projection let the chain fall toward the typical set. Once there, the trajectories explore efficiently (p. 26).

### 4. Efficient HMC
- The construction gives infinitely many transitions, one per choice of kinetic energy and integration time. Well-chosen settings perform well even on challenging high-dimensional problems; poor choices can degrade performance dramatically (p. 26). The analysis is easier in a different view of phase space (p. 27).

### 4.1 Natural geometry of phase space
- Hamilton's equations conserve $H$. Each trajectory stays on a level set $H^{-1}(E)=\{q,p\mid H(q,p)=E\}$. Apart from ignorable exceptions these are $(2D-1)$-dimensional compact surfaces (p. 27).
- Phase space foliates into concentric level sets. A point is given by its energy $E$ and its position $\theta_E$ on the level set (Fig. 21, p. 28).
- **Microcanonical decomposition:** $\pi(q,p)=\pi(\theta_E\mid E)\,\pi(E)$. The first factor is the microcanonical distribution and the second the marginal energy distribution (p. 27).
- A chain therefore has two phases: deterministic motion along level sets (trajectory) and a random walk between level sets (momentum resampling) (Fig. 22, pp. 28–29).
- *Deterministic phase:* its cost is proportional to total integration time. The time needed depends on level-set geometry: the more uniform and regular the level sets, the faster the exploration (p. 28).
- *Stochastic phase:* let $\pi(E\mid q)$ be the energy transition distribution induced by resampling at $q$. Diffusion speed depends on how heavy-tailed $\pi(E)$ is relative to $\pi(E\mid q)$. If $\pi(E\mid q)$ is narrow relative to $\pi(E)$, the walk is slow. If they are similar, samples from $\pi(E)$ are nearly independent at every transition (Fig. 23, pp. 28–29).

*Intuition note:* A transition splits into "how far along the contour" and "which contour". Each has its own tuning knob: integration time for the first, kinetic energy for the second (and for contour shape).

### 4.2 Optimizing the kinetic energy
- The kinetic energy completes the phase-space structure and determines the microcanonical geometry. The ideal choice makes level sets as uniform as possible and matches $\pi(E\mid q)$ to $\pi(E)$ as well as possible. Searching all kinetic energies is impossible, so one searches a restricted family built from the problem's structure (p. 30).

**4.2.1 Euclidean-Gaussian.**
- A Euclidean metric $g$ ($D\times D$ matrix) gives distances $\Delta(q,q')=(q-q')^T g\,(q-q')$ (p. 30).
- Modified metrics: $M=R\,S\,g\,S^T R^T$, with $S$ a diagonal scaling and $R$ an orthogonal rotation (p. 30).
- On momentum space this induces $\Delta(p,p')=(p-p')^T M^{-1}(p-p')$. A Gaussian momentum $\pi(p\mid q)=\mathcal N(p\mid 0,M)$ defines
$$K(q,p)=\tfrac12 p^T M^{-1}p+\log|M|+\text{const.}$$
  The page image prints $\log|M|$ without the factor $\tfrac12$ (see Reading notes). $M$ is called the mass matrix (pp. 30–31).
- Transforming $p'=\sqrt{M^{-1}}\,p$ simplifies $K$, but the opposite transformation $q'=\sqrt M\,q$ must be applied to the parameters. So $M^{-1}$ effectively rotates and rescales parameter space and can correlate or de-correlate the target (p. 31).
- As $M^{-1}$ better resembles the target covariance, the target is de-correlated and level sets become more uniform. The optimum in this family is
$$M^{-1}=\mathbb E_\pi\big[(q-\mu)(q-\mu)^T\big].$$
- In practice, estimate the covariance from the chain in an extended warm-up. First converge to the typical set. Then run with a default metric, estimate the covariance, update the metric and repeat. A few iterations typically give a near-optimal metric (p. 31).

**4.2.2 Riemannian-Gaussian.**
- Unless the target is exactly Gaussian, no global rotation and rescaling gives completely uniform level sets. A Riemannian metric varies with position, giving $\pi(p\mid q)=\mathcal N(p\mid0,\Sigma(q))$ and
$$K(q,p)=\tfrac12 p^T\Sigma^{-1}(q)\,p+\tfrac12\log|\Sigma(q)|+\text{const.}$$
  This is Riemannian HMC (Girolami and Calderhead, 2011) (p. 31).
- If the metric resembles the Hessian of the target, local corrections give very uniform level sets. The inverse metric must stay well-behaved; the SoftAbs metric does this heuristically, and formalizing it is an active research topic (p. 32).
- The $\tfrac12\log|\Sigma(q)|$ term modifies the marginal energy distribution. With a well-chosen metric this can bring it closer to the energy transition distribution (p. 32).

**4.2.3 Non-Gaussian.**
- In theory, any distribution with quadratic sufficient statistics is possible. **Rhetorical question:** why not use heavier or lighter tails? The implied answer: empirically such kinetic energies tend to perform poorly, especially in high dimensions, though there is little supporting theory (p. 32).
- A possible intuition: in high dimensions the marginal energy distribution tends, under relatively weak conditions, to a Gaussian (central limit theorem). When it converges to a Gaussian, only a Gaussian momentum distribution gives the optimal energy transition (p. 32).

### 4.3 Optimizing the integration time
- Short integration wastes coherent exploration. Because level sets are compact in well-behaved problems, long integration revisits explored regions with diminishing returns (p. 32).
- **Dynamic ergodicity:** the *orbit* is everything a trajectory reaches as time goes to infinity. A uniform sample from the trajectory increasingly resembles a sample from the microcanonical distribution restricted to the orbit. The temporal expectation converges to the spatial expectation over the orbit (pp. 32–33).
- Typically, convergence is first rapid and superlinear, then enters an asymptotic regime (Fig. 24, p. 33). The caption says convergence then continues only with the square of the integration time. The optimal time lies at the transition between the regimes, since cost scales with integration time (p. 33).
- Geometrically, the superlinear regime is the first sojourn around the orbit, where each step reaches new neighborhoods. Later passes only refine slowly (Fig. 25, p. 34).
- The optimal time varies across trajectories. In one dimension, for $\pi_\beta(q)\propto e^{-|q|^\beta}$ with $\pi(p\mid q)=\mathcal N(0,1)$:
$$T_{\text{optimal}}(q,p)\propto \big(H(q,p)\big)^{\frac{2-\beta}{2\beta}}.$$
  For heavy tails, $\beta<2$, it grows quickly toward the tails. Only for $\beta=2$ is it constant (Fig. 26, p. 35). Any static time then gives trajectories too short in the tails, and the chain slows to a crawl (pp. 34–35).
- The time should therefore be set dynamically. One heuristic is the No-U-Turn criterion (Hoffman and Gelman, 2014), which uses a Euclidean or Riemannian structure (form in Appendix A.4.2, not in this part). Its near-optimality can be shown rigorously in some simple cases, and it has proven an empirical success on a very diverse set of targets. Exhaustive termination criteria use the microcanonical geometry. They can be more robust but need careful tuning, which is an open topic (p. 35).

*Intuition note:* The first lap around an orbit is where exploration is extremely efficient; later laps refine only slowly. For heavy-tailed targets ($\beta<2$) the optimal time grows toward the tails, so the "one lap" time is longer there.

### 5. Implementing HMC in practice
- Almost no Hamiltonian transitions are immediately applicable. Hamilton's equations cannot be solved exactly except in trivial cases, so they are solved numerically as ODEs on phase space (p. 36).
- Most generic solvers drift: errors add coherently and push the numerical trajectory off the typical set. The drift grows rapidly with the dimension of phase space, so generic solvers suit only short trajectories (Fig. 27, p. 36).

### 5.1 Symplectic integrators
- Symplectic integrators exactly preserve phase-space volume like the true flow. This limits how far the numerical energy can deviate. Trajectories oscillate near the exact level set even for long times (Fig. 28, p. 37).
- If the momentum distribution is independent of position (e.g. Euclidean-Gaussian), the **leapfrog** integrator applies. With step size $\epsilon$ and $q_0\leftarrow q$, $p_0\leftarrow p$, for $0\le n<\lfloor T/\epsilon\rfloor$:
$$p_{n+\frac12}\leftarrow p_n-\tfrac{\epsilon}{2}\tfrac{\partial V}{\partial q}(q_n),\quad q_{n+1}\leftarrow q_n+\epsilon\,p_{n+\frac12},\quad p_{n+1}\leftarrow p_{n+\frac12}-\tfrac{\epsilon}{2}\tfrac{\partial V}{\partial q}(q_{n+1}).$$
  This interleaving ensures exact volume preservation (pp. 37–38).
- Exception: high-curvature neighborhoods of level sets that the step cannot resolve cause a divergence, with the numerical trajectory shooting toward infinite energy (Fig. 29). This makes failures easy to identify (p. 38).
- Two obstructions remain: small integrator errors bias the transition unless corrected, and a suitable integrator must be chosen (p. 38).

### 5.2 Correcting integrator error (part covered here)
- Treat the transition as a Metropolis–Hastings proposal on phase space. With an analytic acceptance probability this gives exact samples from the canonical distribution, hence from the target (p. 38).
- **Naive proposal:** integrate $L$ steps and propose the final state, $\mathbb Q(q',p'\mid q_0,p_0)=\delta(q'-q_L)\,\delta(p'-p_L)$. Backward proposals are impossible (Fig. 30), so
$$\frac{\mathbb Q(q_0,p_0\mid q_L,p_L)}{\mathbb Q(q_L,p_L\mid q_0,p_0)}=\frac01,$$
  and the acceptance probability is always zero (p. 39).
- **Reversible fix:** add a momentum flip $(q,p)\to(q,-p)$, giving $\mathbb Q(q',p'\mid q_0,p_0)=\delta(q'-q_L)\,\delta(p'+p_L)$ (Fig. 31). The acceptance probability is (p. 39)
$$\begin{aligned}a(q_L,-p_L\mid q_0,p_0)&=\min\!\Big(1,\frac{\mathbb Q(q_0,p_0\mid q_L,-p_L)\,\pi(q_L,-p_L)}{\mathbb Q(q_L,-p_L\mid q_0,p_0)\,\pi(q_0,p_0)}\Big)\\&=\min\!\Big(1,\frac{\delta(q_L-q_L)\delta(-p_L+p_L)\,\pi(q_L,-p_L)}{\delta(q_0-q_0)\delta(p_0-p_0)\,\pi(q_0,p_0)}\Big)\\&=\min\!\Big(1,\frac{\pi(q_L,-p_L)}{\pi(q_0,p_0)}\Big)=\min\!\Big(1,\frac{e^{-H(q_L,-p_L)}}{e^{-H(q_0,p_0)}}\Big)\\&=\min\!\big(1,\exp(-H(q_L,-p_L)+H(q_0,p_0))\big).\end{aligned}$$
- $H$ can always be evaluated. Because symplectic integrators oscillate near the exact level set, the acceptance probability deteriorates only negligibly in higher dimensions (p. 40).
- **Uniform proposal over the trajectory** (motivated by Section 4.3): $\mathbb Q(q',p'\mid q_0,p_0)=\frac1L\sum_{l=0}^{L}\delta(q'-q_l)\,\delta(p'+p_l)$. It is still reversible, with $a(q_l,-p_l\mid q_0,p_0)=\min(1,\exp(-H(q_l,-p_l)+H(q_0,p_0)))$ for $0\le l\le L$ and zero otherwise (p. 40).
- Weakness: it proposes states independently of their acceptance probability. A high-error state may be proposed and rejected even though other states on the trajectory have higher acceptance probability. Optimal performance needs the proposals averaged into one efficient proposal. This requires integrating both forwards and backwards, and the transition is easier to see as a two-stage process (p. 40). The text of this part breaks off here.

## Toy example (ours)
Target $\pi(q)=\mathcal N(0,1)$, so $V=q^2/2$, $\partial V/\partial q=q$. Take $M=1$, so $K=p^2/2$.
- Start at $q_0=1$ and sample $p_0=0.5$. Then $H_0=0.5+0.125=0.625$.
- One leapfrog step with $\epsilon=0.5$: $p_{1/2}=0.5-0.25\cdot1=0.25$. Then $q_1=1+0.5\cdot0.25=1.125$. Then $p_1=0.25-0.25\cdot1.125=-0.03125$.
- Energy after the step: $H_1=1.125^2/2+0.03125^2/2=0.6328125+0.00048828=0.63330078$. The exact flow would keep $0.625$. The numerical energy differs by only $0.0083$, so it stays near the level set.
- Flip: $H(q_1,-p_1)=H_1$, since $K$ is even in $p$. Acceptance probability $=\min(1,e^{-0.00830078})\approx0.9917$. The step is nearly always accepted, and the rare rejection removes the integrator bias.

## Concepts
- [[hamiltonian-monte-carlo]] — MCMC that lifts $q$ to phase space, runs Hamiltonian trajectories, and projects back (p. 26). Canon id: Hamiltonian Monte Carlo (HMC/NUTS).
- [[typical-set]] — region where target mass concentrates; trajectories must stay in it (p. 23).
- [[metropolis-hastings]] — used here to correct integrator error, with a reversible proposal (p. 38).
- [[phase-space]] (new) — $2D$-dimensional space of positions and dual momenta, where volume is preserved (p. 23).
- [[canonical-distribution]] (new) — $\pi(q,p)=\pi(p\mid q)\pi(q)=e^{-H}$ on phase space (pp. 23, 25).
- [[hamiltonian-function]] (new) — $H=-\log\pi(q,p)=K+V$, the "energy"; conserved by the flow (pp. 25, 27).
- [[kinetic-energy-mass-matrix]] (new) — $K=-\log\pi(p\mid q)$; Euclidean-Gaussian uses mass matrix $M$ (p. 30).
- [[microcanonical-decomposition]] (new) — $\pi(q,p)=\pi(\theta_E\mid E)\pi(E)$ across energy level sets (p. 27).
- [[dynamic-ergodicity]] (new) — a uniform trajectory sample approaches the orbit's microcanonical distribution as time grows (p. 32).
- [[no-u-turn-criterion]] (new) — heuristic dynamic stopping rule for trajectory length (p. 35).
- [[symplectic-integrator]] (new) — volume-preserving numerical solver whose error oscillates near the true level set; leapfrog is an example (p. 37).
- [[momentum-flip-reversibility]] (new) — $(q,p)\to(q,-p)$ makes the proposal reversible, so the acceptance ratio is nonzero (p. 39).

## Canonical instances
- [[satellite-orbit-analogy]] — momentum balances gravity to give orbits, motivating the construction (pp. 22–23).
- [[generalized-exponential-1d-target]] — $\pi_\beta\propto e^{-|q|^\beta}$, whose optimal integration time scales as $H^{(2-\beta)/(2\beta)}$ (p. 34).
- [[leapfrog-integrator]] — three-line half-step/full-step algorithm (p. 37).
- [[forward-only-proposal-rejection]] — non-reversible proposal with acceptance probability zero (p. 39).

## Bridges (candidates)
- [structural-analogy] Level-set foliation of phase space ↔ bayesian: marginal energy distribution as a one-dimensional summary of the joint, with trajectories moving within and resampling moving across.
- [same-math] Mass matrix $M^{-1}$ = target covariance ↔ bayesian: preconditioning/reparameterization of $q$ by $\sqrt M q$ (the unit gives the transformation).
- [same-math] Acceptance $\min(1,e^{-\Delta H})$ ↔ bayesian: Metropolis–Hastings ratio with a symmetric deterministic proposal.
- [metaphor] Satellite orbit ↔ gradient flow around a mode: momentum prevents falling in.

## Questions this raises
- How do the No-U-Turn criterion and the proposal-averaging schemes that need both-direction integration work in detail (Appendix A)?
- What does the energy transition distribution $\pi(E\mid q)$ look like for common models, and when are heavy tails in $\pi(E)$ a problem?
- How should the step size $\epsilon$ be chosen, given divergences and acceptance probability?
- Why does a Gaussian momentum remain best when the marginal energy distribution is not asymptotically Gaussian?

## Reading notes
- This part starts mid-Section 3.1 (satellite-orbit paragraph, printed p. 22) and ends mid-Section 5.2 (printed p. 40), with the sentence "First we uniformly sample a" cut off. Sections 1–3.1 and 5.2 onward are in other parts.
- Printed page = pdf page (22–40).
- In the page image (p. 30) the Euclidean-Gaussian kinetic energy reads $\tfrac12p^TM^{-1}p+\log|M|$, with no $\tfrac12$ on the log term. The Riemannian version (p. 31) has $\tfrac12\log|\Sigma(q)|$. I report the Euclidean formula as printed. The $\tfrac12$ is probably missing, but this is my inference, not stated in the pages.
- The text layer has typos ("it should we should", "the the", "is make"); they do not change the meaning. The text layer of the leapfrog algorithm and of $\Delta(q,q')$ was garbled; the images were used.
- Fig. 24 has no numerical axis values. Fig. 26 shows an optimal-integration-time axis (0–10) and curves for $\beta=0.5,1,2$, but no constant of proportionality is given. Fig. 24's caption says "square of the integration time", which I report without interpreting.
