---
id: mackay-2003-information/ch32-exact
work: mackay-2003-information
unit: "32 Exact Monte Carlo Sampling"
pages: 413-421
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Exact Monte Carlo Sampling

## L0 — One line
By running coupled Markov chains from further and further in the past with the same random numbers until they all coalesce, one gets, for suitable chains, exact samples from the equilibrium distribution (Propp–Wilson "coupling from the past").

## L1 — The gist (≤ 120 words)
Ordinary MCMC gives samples from the target only asymptotically, and it is hard to know how long to run the chain. Propp and Wilson's method gives exact samples for suitable chains. It rests on three ideas. Chains that share random numbers can coalesce. Starting from a time $T_0$ in the past, and moving $T_0$ further back while reusing the same random numbers, gives an exact sample once all trajectories have coalesced. For some chains, monotonicity lets you track only the extreme states. The chapter applies this to the Ising model and generalises it with "summary states" for non-attractive systems. It also mentions coupling as a way to improve MCMC estimates.

**Prerequisites:** Markov chains and equilibrium distributions; the Metropolis and Gibbs sampling methods (Ch. 29); Ising spin systems with couplings $J_{ij}$ (Ch. 31); partial orders.

## L2 — Key ideas (5–10 bullets)
- MCMC samples come from $P^{(T)}(\mathbf x)$, not $P(\mathbf x)$, if the chain is run too short. Exact sampling removes this uncertainty for certain chains (p. 413).
- Coalescence: chains started in different states but driven by one random-number generator can merge, and once merged they stay merged. Full coalescence means the initial condition is forgotten (p. 413).
- The state at the moment of full coalescence is not a valid sample. For example, in the chain of Fig. 32.1b final coalescence always happens at a wall. Sampling forward until coalescence is therefore invalid (p. 415).
- Coupling from the past: start at $T_0$ in the past, reuse the same random numbers, and push $T_0$ further back (e.g. double it) until coalescence occurs. Then $x(0)$ is an exact sample (p. 415).
- Naively this needs all states to be simulated. For some chains, monotonicity (ordered, non-crossing trajectories) means tracking only the extreme states is enough (pp. 415–418).
- It works for an attractive Ising model (all couplings positive, plus a few special negative cases) via all-up and all-down trajectories. Below the critical temperature this is slow. An improved Propp–Wilson method (random cluster model) gave an exact sample at critical temperature (p. 418).
- The summary-state method uses states in $\{-1,+1,?\}^N$ and works for any couplings. It may be slow to detect coalescence, and convergence is not guaranteed (p. 419).
- Coupling also helps ordinary MCMC estimates, by correcting them with a coupled chain on a simpler distribution $Q$ (p. 420).
- Coalescence time and equilibration time have no direct relationship (p. 421).

## L3 — Walkthrough

### 32.1 The problem with Monte Carlo methods
- MCMC methods (Metropolis, Gibbs, slice sampling) are the most widely used samplers in high dimensions (p. 413).
- A given algorithm can be guaranteed to sample from $P(\mathbf x)$ asymptotically, once the chain has converged to the equilibrium distribution. If the chain is run for too short a time $T$, the samples come from some other distribution $P^{(T)}(\mathbf x)$ (p. 413).
- How long the chain must run is usually very hard to answer. Propp and Wilson (1996) answer it for certain chains and show how to get "exact" samples (p. 413).

### 32.2 Exact sampling concepts
The method is also called "perfect simulation" or "coupling from the past". It uses three ideas (p. 413).

**Idea 1: coalescence of coupled chains.**
- Chains started from different initial conditions but sharing one random-number generator may coalesce. Having coalesced, they do not separate again (p. 413).
- If all initial conditions coalesce into one trajectory, the chain has "forgotten" its initial condition (p. 413).
- Test chain: 21 chains of the Metropolis sampler on $\{0,1,\dots,20\}$ from section 29.4, one chain per initial state. In Fig. 32.1a-i, with a single random-number stream, coalescence takes about 80 steps. With another seed, it takes 400 steps (p. 413).
- In Fig. 32.1b the proposal ('left' or 'right') is the same for all chains at each step, whatever their state. Neighbouring paths merge only when a rejection occurs, and rejections occur only at the walls (for this particular chain). So coalescence occurs only when all chains are in the leftmost state or all are in the rightmost state (p. 413).
- *Intuition note:* sharing random numbers ties the chains' moves together, so they may merge. The way each state uses the shared numbers decides how fast they merge, as the two couplings in Fig. 32.1 show.

**Idea 2: coupling from the past.**
- The state at the moment of full coalescence is not a valid equilibrium sample. In Fig. 32.1b, coalescence always happens at a wall. So sampling forward until coalescence is not valid (p. 415).
- Instead, sample from a time $T_0$ in the past up to the present. If coalescence has occurred, the present sample is an unbiased sample from the equilibrium distribution. If not, restart from a $T_0$ further back, reusing the same random numbers. Doubling $T_0$ is a convenient choice. When coalescence occurs before the present, record $x(0)$ as an exact sample (p. 415).
- Fig. 32.2a: start 21 chains at $T_0=-50$, with no coalescence. Restart at $T_0=-100$ with the same random numbers at each time $t$. The trajectories from $t=-50$ to $0$ are then a subset of the first run's. Still no coalescence. At $T_0=-200$ all trajectories coalesce, and this gives the exact sample (p. 415).
- An earlier $T_0$ such as $-500$ would end at the same point. Every trajectory passes through some state at $t=-200$, and all those states lead to the same final point (p. 415).
- As described, the method is of little practical use. One must simulate chains from all initial states, and a realistic problem has an enormous number of states (e.g. $2^{1000}$ for 1000 binary spins) (p. 415).
- *Intuition note:* a chain run for an infinite time in the past, from any initial condition, would end in the same state (p. 415). Reusing the same random numbers means the runs from $T_0=-100$ are, from $t=-50$ on, a subset of the runs from $T_0=-50$, so once coalescence has occurred, starting earlier does not change the final state.

**Idea 3: monotonicity.**
- For some chains, coalescence of all trajectories can be detected without simulating all of them. This holds for the chain of Fig. 32.1b, where two trajectories never cross (p. 415).
- It then suffices to track the trajectories started from the leftmost and rightmost states. When these two coalesce, all have coalesced (pp. 415–418).
- Fig. 32.3a shows only these two trajectories from Fig. 32.2b, run from $T_0=-50,-100,-200$. Two more exact samples (Fig. 32.3b,c) with other seeds needed $T_0=-50$ and $T_0=-1000$ (pp. 417–418).
- *Intuition note:* if every trajectory stays between the leftmost and rightmost ones, then when those two meet, everything between them has met too.

### 32.3 Exact sampling from interesting distributions
- Many interesting state spaces can be put into a partial order, with coupled chains that respect it. Example for two spins: $(+,+)>(+,-)>(-,-)$ and $(+,+)>(-,+)>(-,-)$, while $(+,-)$ and $(-,+)$ are not ordered (p. 418).
- For such systems, coalescence can be shown by checking only the histories started from "maximal" and "minimal" states (p. 418).
- **Ferromagnetic Ising model with Gibbs sampling.** Order: $\mathbf x \ge \mathbf y$ if $x_i \ge y_i$ for all $i$. The maximal and minimal states are all-up and all-down (p. 418).
- Coupling (Algorithm 32.4): all chains update the same spin $i$ at each step and share the same random numbers $u$ (p. 418).
  - Compute $a_i := \sum_j J_{ij}x_j$.
  - Draw $u$ from Uniform$(0,1)$.
  - If $u < 1/(1+e^{-2a_i})$, set $x_i := +1$; else $x_i := -1$.
- Propp and Wilson show exact samples can be generated this way. Below the critical temperature the time is large, because Gibbs sampling itself mixes slowly there (p. 418).
- They improved on this for the Ising model by using the single-bond heat bath algorithm on the random cluster model. Exact samples from the random cluster model can be obtained rapidly and converted into Ising samples. Their paper includes an exact sample from a 16-million-spin Ising model at its critical temperature (p. 418).
- **'Attractive' distributions.** In practical terms, the Propp–Wilson method applies to spin systems with all couplings positive (e.g. the ferromagnet) and to a few special systems with negative couplings (e.g. the rectangular ferromagnet and antiferromagnet, which are equivalent). It does not apply to general systems with some negative couplings, because the all-up and all-down trajectories are then not guaranteed to bound all trajectories (p. 418).
- **Summary-state generalisation.** The idea is again to keep bounds on all trajectories and detect when the bounds are equal. The bounds are not actual trajectories and are not necessarily tight (p. 419).
  - Simulate one trajectory envelope in the augmented space $\{-1,+1,?\}^N$, where '?' means 'either $-1$ or $+1$'. Example: the summary state ++-?+? stands for the four states ++-+++, ++-++-, ++--++, ++--+- (p. 419).
  - Update rule: take one spin. Enumerate all neighbour states compatible with the current summary state. For each, compute the new spin value by Gibbs sampling coupled to $u$ as in Algorithm 32.4. If all new values agree, set the spin to the unanimous value; otherwise set it to '?' (p. 419).
  - Initial condition at $T_0$: all spins '?', meaning all possible start configurations. Coalescence is detected when no '?' remains (p. 419).
  - With positive couplings this is identical to simulating the uppermost and lowermost states. It can be applied to spin systems with any couplings (p. 419).
  - Shortcoming: the envelope may describe an unnecessarily large set of states. There is no guarantee that the algorithm converges, and detection may take much longer than the underlying chain's actual coalescence (p. 419).
- *Intuition note:* '?' means "we cannot tell this spin across all possible histories". The sample is exact once every spin is known, whatever the history.
- Applications and names: belief networks (Harvey and Neal, 2000); the triangular antiferromagnetic Ising model (Childs et al., 2001). Summary-state methods were introduced by Huber (1998) and are also called sandwiching methods and bounding chains (p. 419). Fig. 32.6 shows a perfectly random lozenge tiling of a hexagon (p. 420).
- **Other uses for coupling.** Pinto and Neal (2001) showed that the estimator
$$\hat\Phi_P \equiv \frac1T\sum_t \phi(\mathbf x^{(t)})\tag{32.1}$$
can be improved by coupling the chain of interest (converging to $P$) to a second chain for a simpler distribution $Q$. The chains' states must be strongly correlated (pp. 419–420).
  - Estimate $\hat\Phi_Q$ and $\hat\Phi_P$ in the normal way. The true $\Phi_Q$ is assumed exactly computable. If $\hat\Phi_Q$ overestimates, then $\hat\Phi_P$ likely does too, so $(\hat\Phi_Q-\Phi_Q)$ can be used to correct $\hat\Phi_P$ (p. 420).

### 32.4 Exercises (listed, not solved here)
Exercises 32.1–32.6 are on pp. 420–421. They concern the relation between coalescence and equilibration, a faulty simulator that uses fresh random numbers, perfect sampling for linear regression, surname coalescence, a coin-made random ranking, and the partition function $Z$ (pp. 420–421).

### 32.5 Solutions
- Ex. 32.1: there is no direct relationship between equilibration time and coalescence time (p. 421).
- Example: the uniform distribution on $\{0,\dots,20\}$ with the chain that draws $s_{t+1}$ uniformly whatever $s_t$ is. It converges in exactly one iteration (p. 421).
- Coupling (a): set $s_{t+1}=u$. Coupling (b): set $s_{t+1}=(s_t+u)\bmod 21$. Both have equilibration time one. Coalescence times are one for (a) and infinity for (b), where trajectories stay locked together and never merge (p. 421).
- The author says it seems plausible that coalescence time gives some sort of upper bound on equilibration time (p. 421).

## Toy example (ours, not from the text)
Chain on states $\{0,1,2\}$. Each step uses one shared move: L means $x\to\max(x-1,0)$ and R means $x\to\min(x+1,2)$. Fix the move sequence by time: step at $t=-2$ is L, step at $t=-1$ is L. The state at $t=0$ is the result of the step at $t=-1$.
- Try $T_0=-1$ (only the step at $t=-1$): L maps $0,1,2\to 0,0,1$. Not coalesced, since 0 and 1 remain.
- Restart at $T_0=-2$, reusing the step at $t=-1$:
  - Step $t=-2$ (L): $0,1,2\to 0,0,1$.
  - Step $t=-1$ (L): $0,0,1\to 0,0,0$.
  - All coalesce, so $x(0)=0$ is the exact sample for these moves.
- Monotone shortcut: track only 0 and 2.
  - $T_0=-1$: $0\to0$, $2\to1$, which differ.
  - $T_0=-2$: $0\to0\to0$, $2\to1\to0$. They meet, so the same answer comes from two trajectories.
- Note that the step at $t=-1$ was reused in the second try. One sample proves nothing about the distribution; the point is the procedure.

## Concepts
- [[markov-chain-monte-carlo]] — Markov-chain sampler that can be guaranteed to produce samples from the target asymptotically. Run too short, it samples $P^{(T)}$, not $P$ (p. 413).
- [[gibbs-sampling]] — update one spin at a time from its conditional. Here it is coupled via shared $u$ and the same spin $i$ (Algorithm 32.4) (p. 418).
- [[metropolis-hastings]] — the 21-state Metropolis chain is the toy chain used throughout (p. 413).
- [[coalescence]] (new) — coupled chains meet in one trajectory and never separate (p. 413).
- [[coupling-from-the-past]] (new) — start at $T_0$ in the past, reuse random numbers, push $T_0$ back until coalescence; $x(0)$ is then an exact sample (p. 415).
- [[monotone-coupling]] (new) — a partial order on states respected by the coupled chains. Tracking maximal and minimal states then suffices to detect coalescence (pp. 415, 418).
- [[summary-state-method]] (new) — one envelope trajectory in $\{-1,+1,?\}^N$; works for general couplings but may be slow to detect coalescence (p. 419).
- [[convergence-diagnostics]] — here, an exact answer to "has the chain converged?" for suitable chains (p. 413).
- [[monte-carlo-integration]] — estimator (32.1); the coupling idea can improve it (p. 419).

## Canonical instances
- [[metropolis-21-state-chain]] — toy chain on $\{0,\dots,20\}$ used for coalescence, CFTP and monotonicity (p. 413).
- [[ising-exact-sample]] — exact samples from the ferromagnetic Ising model, including a 16-million-spin one at critical temperature (p. 418).
- [[uniform-coupling-counterexample]] — same chain, two couplings, coalescence time 1 versus infinity (p. 421).

## Bridges (candidates)
- [structural-analogy] Summary state '?' ↔ interval arithmetic: bounds that enclose all possibilities, possibly loosely (p. 419).
- [structural-analogy] Pinto–Neal correction using $Q$ ↔ control variates: correct an estimate with a correlated one whose true value is known (p. 420).
- [metaphor] Coalescence of trajectories ↔ population genetics: surnames or lineages merging to a common ancestor (Ex. 32.4, p. 420).

## Questions this raises
- Why does reusing the same random numbers for the earlier $T_0$ runs matter, and what goes wrong without it (Ex. 32.2)?
- Is coalescence time an upper bound on equilibration time?
- Can the summary-state envelope be kept tight enough to be useful for non-attractive systems?
- Can the time to coalescence carry information about the partition function $Z$ (Ex. 32.6)?

## Exercises worth doing
- Ex. 32.2 (p. 420) — why identical random bits across $T_0$ are required — difficulty: easy
- Ex. 32.4 (p. 420) — coalescence in surnames, with a forensic DNA question — difficulty: medium
- Ex. 32.5 (p. 421) — build a coin-based random ranking of 3 people with exact sampling — difficulty: easy
- Ex. 32.6 (p. 421) — whether coalescence time or random-bit use reveals $Z$ — difficulty: hard

## Reading notes
- Printed page = pdf page − 12 (pdf 425 = p. 413).
- Figures are images only. The text layer shows axis ticks, so figure details come from the captions and page images.
- The text says the 400-step coalescence for the second seed in Fig. 32.1a-ii is "not shown". The plotted axes stop at 250.
- Typos in the source: "occuring" (p. 419), "the the" (p. 418). They do not affect the content.
- On the pages given (to p. 421), Section 32.5 prints a solution to Ex. 32.1 only. No solutions to the other exercises appear on these pages.
