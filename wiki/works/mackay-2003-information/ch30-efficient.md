---
id: mackay-2003-information/ch30-efficient
work: mackay-2003-information
unit: "30 Efficient Monte Carlo Methods"
pages: 387–398
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Efficient Monte Carlo Methods

## L0 — One line
Metropolis and Gibbs sampling move by slow random walks, and several tricks (gradients, biased updates, temperature, interacting populations) can cut this, while an information-theoretic view shows why a plain Metropolis chain gains at most about one bit per step.

## L1 — The gist (≤ 120 words)
Question: how can we get effectively independent samples faster than a random-walk Metropolis method does? MacKay reviews Hamiltonian Monte Carlo (gradient-driven, persistent motion), overrelaxation (Gibbs updates biased to the opposite side), simulated annealing (a temperature schedule), Skilling's multi-state leapfrog, and genetic or particle-style multi-state methods. He also views a dumb Metropolis method (one whose proposals ignore $P$) as a channel that carries at most $H_2(f)$ bits per step. This gives a simple justification for the "acceptance rate about ½" rule of thumb. Last, he warns that scattering initial points widely need not fix slow mixing in hierarchical models.

**Prerequisites:** Metropolis acceptance rule; Gibbs sampling; detailed balance; Gaussian distributions; binary entropy $H_2$.

## L2 — Key ideas
- **Hamiltonian Monte Carlo (HMC)** adds momentum variables and simulates dynamics. The state then tends to move a distance linear in computer time, rather than as a square root. The Metropolis rule corrects numerical error (pp. 387–389).
- **Overrelaxation** biases each Gibbs update to the opposite side of the conditional. Each coordinate move keeps detailed balance, but the fixed-order sweep does not. This asymmetry can give directed motion (instead of a random walk) in positively correlated variables, and may cut the time to independent samples (p. 391).
- **Simulated annealing** samples at high temperature $T$ and lowers $T$ to 1. It does not sample exactly. Simulated tempering (temperature as a random variable) and annealed importance sampling (importance weights) remove the bias (p. 392).
- **Skilling's leapfrog** keeps $S$ states and leapfrogs one over another. In a needle-like density the typical distance explored in the long direction grows exponentially with iterations. For a spherical Gaussian, acceptance scales as $e^{-2N}$ in $N$ dimensions at equilibrium (pp. 392–393, 398).
- **Channel view:** for a dumb Metropolis method, the information about $P$ gained in $T$ steps is at most $TH_2(f)$ bits; this bound is largest at $f=1/2$ (p. 394).
- **Multi-state methods** need both multiplication and death, at least one of them selective, to obtain a speed-up. Crossover with a Metropolis rule is valid but gives no $\sqrt G$ speed-up (pp. 395–396).
- **Widely scattered initial conditions can fail** in hierarchical models: the hyperparameter $\beta$ (which couples many parameters) still random-walks with steps $\propto 1/\sqrt N$ (p. 397).

## L3 — Walkthrough

**Intro (p. 387).** The aim is to reduce the time needed for "independent samples", meaning effectively independent ones. The method is to reduce random-walk behaviour in Metropolis methods.

### 30.1 Hamiltonian Monte Carlo (pp. 387–390)
HMC is a Metropolis method for continuous state spaces. It uses the gradient of $E(\mathbf x)$ to reduce random-walk behaviour (p. 387). The target is
$$P(\mathbf x)=\frac{e^{-E(\mathbf x)}}{Z}\tag{30.1}$$
Both $E$ and its gradient are assumed readily computable. Using a plain random-walk Metropolis method seems wasteful when the gradient is available, since the gradient indicates which direction leads to higher-probability states (p. 387).

**Overview.** The state is augmented with momentum variables $\mathbf p$. Two proposal types alternate. The first randomizes $\mathbf p$ and leaves $\mathbf x$ alone. The second changes both using simulated Hamiltonian dynamics, defined by a Hamiltonian with a 'kinetic energy' $K$ such as $K=\mathbf p^{\mathsf T}\mathbf p/2$ (p. 387):
$$H(\mathbf x,\mathbf p)=E(\mathbf x)+K(\mathbf p),\quad K(\mathbf p)=\mathbf p^{\mathsf T}\mathbf p/2 \tag{30.2}$$
Together they asymptotically give samples from
$$P_H(\mathbf x,\mathbf p)=\frac1{Z_H}\exp[-H(\mathbf x,\mathbf p)]=\frac1{Z_H}\exp[-E(\mathbf x)]\exp[-K(\mathbf p)]\tag{30.3}$$
This is separable, so the marginal of $\mathbf x$ is $e^{-E}/Z$. Discarding $\mathbf p$ leaves samples of $P(\mathbf x)$ (p. 387).

**Details.**
- The first proposal is a Gibbs-style update. It draws $\mathbf p$ from $\exp[-K(\mathbf p)]/Z_K$ and is always accepted (p. 389).
- The dynamical proposal follows (p. 389):
$$\dot{\mathbf x}=\mathbf p\tag{30.4}$$
$$\dot{\mathbf p}=-\frac{\partial E(\mathbf x)}{\partial \mathbf x}\tag{30.5}$$
- Because $\mathbf x$ keeps moving along $\mathbf p$, it tends to travel a distance linear in computer time, "rather than as the square root" (p. 389).
- The second proposal is accepted by the Metropolis rule. If the simulation is numerically perfect, $H$ is conserved, so $a$ in (29.31) equals one and every proposal is accepted. With finite step sizes some proposals are rejected. The rejection rule uses the change in $H$, which is zero for a perfect simulation. These occasional rejections ensure the asymptotic samples come from $P_H$ (p. 389).
- Algorithm 30.1 (Octave code, p. 388) does the following. For each of $L$ loops it draws $\mathbf p\sim$ Normal(0,1) and computes $H=\mathbf p^{\mathsf T}\mathbf p/2+E$. It then makes Tau leapfrog steps, each of which is:
  1. half-step in $\mathbf p$: $\mathbf p\leftarrow\mathbf p-\epsilon\,\mathbf g_{new}/2$;
  2. full step in $\mathbf x$: $\mathbf x_{new}\leftarrow\mathbf x_{new}+\epsilon\mathbf p$;
  3. recompute the gradient at $\mathbf x_{new}$;
  4. second half-step in $\mathbf p$.

  Finally it computes $dH=H_{new}-H$. It accepts if $dH<0$, or else if rand() $<\exp(-dH)$ (p. 388). (The text on p. 389 calls this code "figure 30.1"; the caption says Algorithm 30.1.)

**Experiment (Fig. 30.2, pp. 388–390).** The target is a bivariate Gaussian with $E=\tfrac12\mathbf x^{\mathsf T}\mathbf A\mathbf x$ (p. 389):
$$\mathbf A=\begin{bmatrix}250.25&-249.75\\-249.75&250.25\end{bmatrix}\tag{30.6}$$
Its covariance matrix is
$$\begin{bmatrix}1&0.998\\0.998&1\end{bmatrix}\tag{30.7}$$
- In panel (a), two successive trajectories each used Tau = 19 and epsilon = 0.055. Both were accepted, with Hamiltonian errors $+0.016$ and $-0.06$ (p. 389).
- In panel (b), four trajectories converged from a start far from the typical set. Tau and epsilon were randomized uniformly with means 19 and 0.055.
  - The second trajectory ended nearer the bottom of the energy landscape, where $E$ is lower. So $K$ was necessarily larger than at the start.
  - Randomizing the momentum before the third trajectory made $K$ much smaller.
  - After the fourth trajectory the state appeared typical (pp. 389–390).
- Panels (c) and (d) are random-walk Metropolis runs with similar computer time. In (c) the step size gave a 58% acceptance rate with 38 proposals. The distance moved was small because of random-walk behaviour (p. 390).

*Intuition note:* Momentum makes the state keep going in one direction for many steps. If the simulated dynamics are accurate, energy is nearly conserved along the path, so long moves are mostly accepted. A random walk, which keeps changing direction, tends to cover less distance in the same time.

### 30.2 Overrelaxation (pp. 390–391)
Overrelaxation reduces random-walk behaviour in Gibbs sampling. It was originally introduced for systems whose conditionals are all Gaussian (p. 390). An example that is not jointly Gaussian but has Gaussian conditionals is $P(x,y)=\exp(-x^2y^2-x^2-y^2)/Z$ (p. 390).

**Gaussian conditionals.** Ordinary Gibbs sampling ignores the old value $x_i^{(t)}$, and strongly correlated variables give lengthy random walks (p. 391). In Adler's (1981) method, if the conditional is Normal($\mu,\sigma^2$), then
$$x_i^{(t+1)}=\mu+\alpha\,(x_i^{(t)}-\mu)+(1-\alpha^2)^{1/2}\sigma\nu\tag{30.8}$$
Here $\nu\sim$ Normal(0,1) and $\alpha\in(-1,1)$, "usually set to a negative value". A positive $\alpha$ is called under-relaxation (p. 391).
- Exercise 30.1 asks the reader to show that (30.8) leaves Normal($\mu,\sigma^2$) invariant (p. 391).
- Exercise 30.2 asks the reader to investigate, for a toy two-dimensional Gaussian, the assertion that overrelaxation's advantages are lost if the updates are made in a random order (for which $T$ would be symmetric) (p. 391).
- Each single-coordinate transition satisfies detailed balance, so the chain is a valid sampler that converges to $P(\mathbf x)$. A complete fixed-order update does not satisfy detailed balance, so the overall chain is not reversible. MacKay says this temporal asymmetry is the key to the benefit. Positively correlated variables then evolve in a directed way on short timescales, which "may significantly reduce" the time to independent samples (p. 391).
- Fig. 30.3 uses $\rho=0.998$. Panel (a) uses $\alpha=-0.98$, chosen excessively large to make the effect visible. Panel (c) uses $\alpha=-0.89$ over 2000 iterations of $x_1$ (p. 390).

**Ordered overrelaxation (Neal 1995).** This applies wherever Gibbs sampling is used (p. 391).
1. Draw $K$ samples $x_i^{(1)},\dots,x_i^{(K)}$ from the conditional. $K$ might be about twenty. The extra samples often add negligible cost.
2. Sort them, insert the current value, and rank the $K+1$ points $0,\dots,K$. Let $\kappa$ be the current value's rank.
3. Set $x_i'$ to the value of rank $K-\kappa$.

$K$ plays the role of $\alpha$, and $K=1$ gives ordinary Gibbs sampling. Neal estimates that it may speed up a simulation by a factor of ten or twenty (p. 391).

*Intuition note:* Instead of forgetting where it was, the chain jumps to a spot biased toward the opposite side of the conditional (in ordered overrelaxation, the rank-mirrored value). Repeated sweeps can then carry it in a directed way along a correlated ridge instead of letting it wander back and forth.

### 30.3 Simulated annealing (p. 392)
A temperature parameter, when large, allows transitions improbable at $T=1$. $T$ starts large and is gradually reduced to 1. This is supposed to reduce the chance of getting stuck in an unrepresentative probability island. For target (30.9) $P(\mathbf x)=e^{-E(\mathbf x)}/Z$, one samples instead
$$P_T(\mathbf x)=\frac1{Z(T)}e^{-E(\mathbf x)/T}\tag{30.10}$$
If $E=E_0+E_1$ with $E_0$ "nice" and $E_1$ "nasty" (30.11), a better scheme might be
$$P'_T(\mathbf x)=\frac1{Z'(T)}e^{-E_0(\mathbf x)-E_1(\mathbf x)/T}\tag{30.12}$$
At high $T$ this reverts to a well-behaved distribution defined by $E_0$. For optimization, $T$ is decreased to zero instead (p. 392).

As a Monte Carlo method, simulated annealing as described does not sample exactly, because nothing guarantees that the chance of falling into a basin equals that basin's total probability. Simulated tempering (Marinari and Parisi 1992) makes temperature a random variable updated in Metropolis fashion. Annealed importance sampling (Neal 1998) removes the bias with importance weights (p. 392).

### 30.4 Skilling's multi-state leapfrog (pp. 392–393)
This method is similar in spirit to overrelaxation but works in more dimensions. It needs only an easy-to-evaluate $E(\mathbf x)$ (no gradient), applies to continuous spaces, and is meant to be used in sequence with other operators (p. 392).

- It maintains $S$ state vectors $\{\mathbf x^{(s)}\}$ ($S$ perhaps six or twelve), aiming for all to be independent samples of $P$ (pp. 392–393).
- It proposes leapfrogging $\mathbf x^{(s)}$ over a partner $\mathbf x^{(t)}$:
$$\mathbf x^{(s)\prime}=\mathbf x^{(t)}+(\mathbf x^{(t)}-\mathbf x^{(s)})=2\mathbf x^{(t)}-\mathbf x^{(s)}\tag{30.13}$$
- The proposal is accepted by the Metropolis rule. Other vectors do not move, so acceptance depends only on the energy change of $\mathbf x^{(s)\prime}$ (p. 393).
- The partner may be chosen at random. Nearest neighbours may be better, provided the acceptance rule checks that $t$ is still a nearest neighbour of the new point, which ensures detailed balance (p. 393).

**Why it helps.** Take a needle-like Gaussian of width $\epsilon$ and length $L\gg\epsilon$, and a cloud of points initially in a ball of size $\epsilon$ (p. 393).
- A typical first move takes a point a little outside the ball. If all moves are accepted the ball grows by about a factor of two in all dimensions.
- Rejections mean the ball probably elongates along the needle by about two per cycle.
- So the distance covered in the long direction grows exponentially with iterations. Even at a factor of 1.1 per iteration, exploring it takes a number of iterations proportional to $\log L/\log 1.1$ (p. 393).

MacKay says the method resembles Gilks et al.'s (1994) adaptive direction sampling, but is simpler and applicable to a greater variety of distributions (p. 393). Exercise 30.3 asks how it scales with dimension and correlation; the printed solution is below.

**Solution to Ex. 30.3 (p. 398).** Take a spherical Gaussian with zero mean and unit variance. In coordinate $n$, if $x^{(1)}_n$ leapfrogs over $x^{(2)}_n$:
$$(x_n^{(1)})'=2x_n^{(2)}-x_n^{(1)}\tag{30.16}$$
With both coordinates Normal(0,1), $(x_n^{(1)})'$ is Normal(0,$\sigma^2$) with $\sigma^2=2^2+(-1)^2=5$. The energy change in this dimension is
$$\tfrac12\big[(2x_n^{(2)}-x_n^{(1)})^2-(x_n^{(1)})^2\big]=2(x_n^{(2)})^2-2x_n^{(2)}x_n^{(1)}\tag{30.17}$$
The typical change is $2\langle (x_n^{(2)})^2\rangle=2$. In $N$ dimensions the typical change at equilibrium is $+2N$, and acceptance scales as
$$e^{-2N}\tag{30.18}$$
So the method as described is not effective in very high dimensions, at least once convergence has occurred. Its advantage is that its convergence is independent of the strength of correlations. MacKay says not even HMC or overrelaxation offers this (p. 398). The hint on p. 393 says the method is invariant under affine transformations, so the separable case suffices.

### 30.5 Monte Carlo algorithms as communication channels (pp. 394–395)
Two communications occur when a sample is generated (p. 394).
1. Selecting a particular $\mathbf x$ from $P(\mathbf x)$ needs at least $\log 1/P(\mathbf x)$ random bits.
2. Generating the sample conveys information about $P$ from the subroutine evaluating $P^*(\mathbf x)$.

In a **dumb Metropolis method** the proposals $Q$ have nothing to do with $P$. Properties of $P$ enter only at the acceptance step, via $P^*(\mathbf x')/P^*(\mathbf x)$. So all information about $P$ passes through the string of accept/reject decisions, a bottleneck. MacKay says he is not aware of much use of this viewpoint but finds it instructive (p. 394).

**Example 30.4 (rule of thumb).** Let $\mathbf a$ be the acceptance history and $f$ the acceptance rate. After $T$ steps, the information learned about $P$ is at most the information content of $\mathbf a$. That content is at most $TH_2(f)$, which is maximized at $f=1/2$. This justifies tuning a dumb Metropolis method to an acceptance rate of about one half (p. 394).

**Evolutionary analogy.** A proposal makes progeny $\mathbf x'$ of the current state $\mathbf x$. They compete under a noisy survival-of-the-fittest rule, and insights about the rate of evolution can be applied to Monte Carlo methods (p. 394).

Exercise 30.5 asks for analysis of a dumb Metropolis method that flips a fraction $m$ of $G$ bits, for $P(\mathbf x)=\prod_g p(x_g)$ (30.14) (pp. 394–395).

The fastest information-theoretic progress of a standard Metropolis method is "about one bit per iteration". MacKay says this motivates speed-ups (p. 395). Exercises ask whether Gibbs sampling (30.6), HMC (30.7), or importance sampling and adaptive hybrids (30.8) can do better (p. 395).

*Intuition note:* Each accept/reject is one yes/no answer from the target density. A yes/no answer carries at most one bit, and an answer that is almost always "yes" or almost always "no" carries less. So the bound on information is largest at an acceptance rate of one half.

### 30.6 Multi-state methods (pp. 395–396)
Multiple vectors evolve individually (Metropolis, Gibbs) and interact. Either all should eventually be samples from $P$ (as in Skilling's method), or their associated information should allow approximate expectations (as in importance sampling) (p. 395).

**Genetic methods.** MacKay's view is that genetic algorithms are best categorized as Monte Carlo algorithms, and an ideal one would be provably valid and convergent to a specified density (p. 395). With $R$ vectors, the target is $P^*(\{\mathbf x^{(r)}\}_1^R)=\prod_r P^*(\mathbf x^{(r)})$ (p. 396).
- **Individual moves** perturb one vector, using any method above.
- **Crossover** $\mathbf x,\mathbf y\to\mathbf x',\mathbf y'$ in a typical move gives the progeny $\mathbf x'$ half its state vector from one parent and half from the other. Success needs an encoding in which crossing two fit states has a fair chance of giving fit progeny. MacKay says this is hard to satisfy, so genetic algorithms are "mainly talked about and hyped up, and rarely used by serious experts" (his view, p. 396).
- A valid acceptance rule is the Metropolis rule on the ratio
$$\frac{P^*(\mathbf x')P^*(\mathbf y')}{P^*(\mathbf x)P^*(\mathbf y)}\tag{30.15}$$
If the crossover operator is reversible, there is an easy proof of detailed balance (p. 396).

Exercise 30.9 asks whether these two operators beat a single-state method (p. 396).

**Why no speed-up.** In Chapter 19, the sexual community learned faster because crossover produced diversity with standard deviation $\sqrt G$, and the Blind Watchmaker conveyed information by killing the less fit. The two operators here give no $\sqrt G$ speed-up because there is no killing. A speed-up needs multiplication and death, with at least one selective: kill the less fit, or let the fitter breed more. Defining a valid method is hard. Exercise 30.10 asks for a birth and death rule with chain converging to $P^*(\{\mathbf x^{(r)}\})$. MacKay believes this is still an open research problem (p. 396).

**Particle filters** are multi-state methods mixing importance sampling and MCMC, popular for temporal tracking. The text only cites references (p. 396).

### 30.7 Methods that do not necessarily help (p. 397)
**Question:** can many initial conditions "well distributed about the whole state space" ensure good coverage of the typical set? **Answer:** "unfortunately, no" (p. 397).

**Example (hierarchical model).** Parameters $\{x_n\}$ are coupled via a hyperparameter $\beta$ (an inverse noise variance). The joint is
$$P(\beta,\{x_n\})=P(\beta)\prod_{n=1}^N P(x_n\mid\beta)=P(\beta)\prod_{n=1}^N\frac1{Z(\beta)}e^{-\beta x_n^2/2}$$
with $Z(\beta)=\sqrt{2\pi/\beta}$ and $P(\beta)$ broad. The chain is Gibbs sampling, alternating $\beta$ given $\{x_n\}$ and all $x_n$ given $\beta$. The marginal of $\beta$ should asymptotically be $P(\beta)$ (p. 397).
- For large $N$, the conditional of $\beta$ given any $\{x_n\}$ is tightly concentrated, with width $\propto1/\sqrt N$.
- So moves along the $\beta$-axis are a slow random walk with steps $\propto1/\sqrt N$ (p. 397).
- Distributing the $x_n$ widely favours a large initial noise level $1/\beta$. After the first draw of $\beta$, the walk will tend "always" to start off from one end of the $\beta$-axis (p. 397).

*Intuition note:* Scattering the $x_n$ does not scatter $\beta$. The first $\beta$ draw immediately snaps to a value that depends on how spread out the $x_n$ are. Every run therefore tends to start at the same end of $\beta$'s range and then moves along it in tiny steps.

### Further reading and further exercises (p. 397–398)
HMC (Duane et al. 1987) is reviewed in Neal (1993b), which also covers simulated annealing and free-energy estimation (p. 397).
- Exercise 30.11 states that the HMC simulation, though inaccurate, must be perfectly reversible (if $(\mathbf x,\mathbf p)$ goes to $(\mathbf x',\mathbf p')$, the same simulator must take $(\mathbf x',-\mathbf p')$ to $(\mathbf x,-\mathbf p)$), and must conserve state-space volume. The leapfrog method satisfies these rules (p. 397).
- Exercise 30.12 proposes multi-state slice sampling. It updates $\mathbf x^{(s)}$ by 1-D slice sampling along $\mathbf y=\mathbf x^{(v)}-\mathbf x^{(w)}$ for two randomly chosen other states. If $S-1<N$, the method is not ergodic by itself (p. 398).

## Toy example (ours, not from the text)
Target $E(x)=x^2/2$ (standard Gaussian), so the gradient is $g=x$. Start at $x=1$ with momentum $p=0.5$, $\epsilon=0.5$, one leapfrog step.
1. Initial $H=p^2/2+E=0.125+0.5=0.625$.
2. Half-step in $p$: $p=0.5-0.25\times1=0.25$.
3. Full step in $x$: $x_{new}=1+0.5\times0.25=1.125$. New gradient: $1.125$.
4. Half-step in $p$: $p=0.25-0.25\times1.125=-0.03125$.
5. $H_{new}=(0.03125)^2/2+(1.125)^2/2=0.000488+0.632813=0.633301$.
6. $dH=0.633301-0.625=0.008301$, which is $>0$.
7. Accept with probability $e^{-0.0083}\approx0.9917$.

The state moved by 0.125 in one step with nearly no energy error. This is only one leapfrog step. The text's point is that, because $\mathbf x$ keeps moving along $\mathbf p$ during a trajectory, the state tends to cover a distance linear in computer time rather than as a square root (p. 389).

## Concepts
- [[hamiltonian-monte-carlo-hmc-nuts]] — Metropolis method using gradient dynamics with momentum variables $\mathbf p$; original name "hybrid Monte Carlo" (pp. 387–389)
- [[metropolis-hastings]] — accept/reject rule used to correct inexact dynamics and in crossover moves (pp. 389, 396)
- [[gibbs-sampling]] — draw each variable from its conditional; slow random walk when variables are strongly correlated (p. 391)
- [[markov-chain-monte-carlo-mcmc]] — chains whose long-run distribution is the target; here the aim is fewer steps per independent sample (p. 387)
- [[overrelaxation]] (new) — Gibbs-type update biased to the opposite side of the conditional, eq. (30.8) (p. 391)
- [[ordered-overrelaxation]] (new) — Neal's rank-reflection version using $K$ conditional samples; works for any Gibbs system (p. 391)
- [[detailed-balance]] (new) — reversibility condition; each coordinate update has it, the fixed-order sweep does not (p. 391)
- [[leapfrog-integrator]] (new) — half-step, full-step, half-step scheme to simulate Hamiltonian dynamics (p. 388)
- [[simulated-annealing]] (new) — sample $P_T\propto e^{-E/T}$ with $T$ lowered to 1 (or 0 for optimization) (p. 392)
- [[simulated-tempering]] (new) — temperature as a random variable updated in Metropolis fashion, correcting annealing bias (p. 392)
- [[annealed-importance-sampling]] (new) — removes annealing bias using importance weights (p. 392)
- [[skilling-leapfrog]] (new) — $S$-state method with proposal $2\mathbf x^{(t)}-\mathbf x^{(s)}$ (p. 393)
- [[multi-state-methods]] (new) — keep several interacting state vectors (genetic algorithms, particle filters) (p. 395)
- [[mcmc-as-communication-channel]] (new) — dumb Metropolis passes information about $P$ only through the accept/reject string (p. 394)
- [[hierarchical-multilevel-model]] — parameters coupled by a hyperparameter; here an example where widely spread starts do not help (p. 397)
- [[entropy-hx]] — $H_2(f)$ caps information per Metropolis step (p. 394)
- [[typical-set]] — states typical of the target; Fig. 30.2b shows a start far from it converging to it (pp. 389–390)

## Canonical instances
- [[correlated-bivariate-gaussian-rho-0998]] — benchmark target ($\rho=0.998$): HMC is compared with random-walk Metropolis (Fig. 30.2) and overrelaxation with Gibbs sampling (Fig. 30.3) (pp. 388–390)
- [[hierarchical-noise-hyperparameter-gibbs]] — $\beta$ and $\{x_n\}$ example of slow mixing despite scattered starts (p. 397)
- [[needle-gaussian-leapfrog]] — Gaussian needle showing exponential growth in explored length (p. 393)
- [[acceptance-rate-one-half-rule]] — the $f=1/2$ rule of thumb justified via $H_2(f)$ (p. 394)

## Bridges (candidates)
- [structural-analogy] MCMC acceptance string as a bottleneck channel ↔ information-theory: noisy channel with capacity limit — a binary decision stream caps information per use.
- [structural-analogy] Dumb Metropolis proposals and survival-of-the-fittest ↔ evolution: fitness-based selection (Ch. 19) — parent and progeny compete under a noisy rule.
- [structural-analogy] Simulated annealing temperature $T$ ↔ physics: Gibbs distribution at temperature $T$ — $e^{-E/T}$ flattens energy barriers.
- [same-math] HMC target $e^{-H}$ with separable $K(\mathbf p)$ ↔ information-theory: Gibbs/exponential-family distribution — the $\mathbf x$-marginal is exactly $e^{-E}/Z$.

## Questions this raises
- Does HMC, or Gibbs sampling, actually get more than one bit per iteration about $P$ (Ex. 30.6–30.7)?
- How should Tau and $\epsilon$ be chosen, and why does randomizing them help (p. 389)?
- Can multiplication-and-death be designed so that a population chain remains exactly valid (Ex. 30.10)?
- How do these methods behave in high dimensions, given Skilling's $e^{-2N}$ acceptance (p. 398)?

## Exercises worth doing
- Ex. 30.1 (p. 391) — verify that Adler's update (30.8) leaves the Gaussian conditional invariant — difficulty: easy
- Ex. 30.2 (p. 391) — test whether overrelaxation's advantage vanishes with random update order — difficulty: medium
- Ex. 30.5 (pp. 394–395) — analyze dumb Metropolis bit-flipping and the optimal $m$, then compare with Chapter 19 — difficulty: medium
- Ex. 30.6 (p. 395) — find toy cases where Gibbs sampling exceeds one bit per iteration — difficulty: hard
- Ex. 30.11 (p. 397) — why HMC dynamics must be reversible and volume-conserving — difficulty: hard

## Reading notes
- Printed page = pdf page − 12 (pdf 399 = printed 387).
- Page 389 says the code is "figure 30.1", while the caption on p. 388 says "Algorithm 30.1".
- Figure and panel details (axis values, trajectories) were read from page images; no equations were unreadable.
- Section 30.4 text on p. 393 refers to Exercise 30.3 with solution on p. 398. That solution is summarized in L3 and is not listed under exercises.
- Several claims are MacKay's opinions or references to others: Neal's speed-up estimate, Skilling's method being simpler than adaptive direction sampling, genetic algorithms being rarely used, and Exercise 30.10 being open.
