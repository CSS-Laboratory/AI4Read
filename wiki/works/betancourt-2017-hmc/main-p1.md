---
id: betancourt-2017-hmc/main-p1
work: betancourt-2017-hmc
unit: paper (part 1/3) — Introduction, §1 Computing expectations, §2 Markov chain Monte Carlo, start of §3 (to §3.1)
pages: 1-21
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# A Conceptual Introduction to Hamiltonian Monte Carlo — Part 1 (pp. 1–21)

## L0 — One line
In high dimensions, expectations are dominated by a thin "typical set" away from the mode, so a sampler must glide coherently through that set, and the gradient of the density alone cannot guide it there.

## L1 — The gist (≤ 120 words)
How can we compute expectations under a high-dimensional target distribution? Probability mass sits in the typical set, a thin region between the mode (the point of highest density, with little volume) and the tails (much volume, tiny density). Markov chain Monte Carlo explores this set with a chain whose transitions preserve the target. Ideal chains give estimators with a central limit theorem. Chains typically have trouble exploring regions of high curvature. Random Walk Metropolis scales poorly with dimension: large proposals land in the tails and are rejected, while small ones move slowly. Better transitions need geometric information. The density gradient alone points toward the mode, so it must be "twisted". A physics analogy (satellite in orbit) motivates how.

**Prerequisites:** probability densities and expectations as integrals; gradient; basic idea of a Markov chain and autocorrelation; the normal distribution.

## L2 — Key ideas
- Expectations are integrals of density × function over volume. They are invariant under reparameterization (a change of coordinates), but the density's shape is not (p. 4).
- Density is largest at the mode, but volume there is tiny. The product π(q) dq concentrates in the typical set, which is parameterization-invariant and narrows with dimension (pp. 5–8).
- Grid quadrature needs $N^D$ evaluations and, unless $N$ is incredibly large, is unlikely to hit the narrow typical set (p. 8).
- In Markov chain Monte Carlo (MCMC), if the transition preserves the target, the chain drifts into and across the typical set and, up to some technicalities, its estimators converge. Ideal chains pass through three phases, then satisfy a central limit theorem (CLT) with standard error governed by the effective sample size (pp. 9–11).
- In pathological regions (e.g. high curvature) chains typically get stuck. Estimators then oscillate around the truth, and stopping after a finite time almost always gives substantial bias. Split $\hat R$ (a statistic comparing several chains) is an empirical diagnostic for this failure (pp. 13–15).
- Random Walk Metropolis (RWM): large proposals are rejected, small ones move slowly. Either way exploration of the typical set is very slow in all but the lowest dimensions (p. 16).
- We need transitions that follow the typical set. A vector field aligned with it would do this. The density gradient is never aligned with it; following it pulls toward the mode (pp. 17–19).
- A physical analogy (planet, gravity, orbit) suggests that momentum is the missing ingredient (pp. 20–21).

## L3 — Walkthrough

### Introduction (p. 3)
Hamiltonian Monte Carlo (HMC) began in the late 1980s as Hybrid Monte Carlo for lattice quantum chromodynamics. Neal later saw its use for applied statistics, and software such as Stan made it widespread (p. 3). The author says its success rests on a theory built in differential geometry. This paper gives the intuition, assuming only basic probability and calculus, and sacrifices rigor (p. 3). The plan is: geometry of high-dimensional distributions → MCMC from that view → the features a scalable method needs → HMC, tuning and diagnostics (p. 3).

### 1. Computing expectations by exploring distributions (pp. 3–4)
The goal is expectations $\mathbb E_\pi[f]$ of functions under a target $\pi$ on a $D$-dimensional sample space $Q$ (p. 4).

### 1.1 Computing expectations in practice (p. 4)
With a smooth parameterization $q\in\mathcal Q$ and density $\pi(q)$:
$$\mathbb E_\pi[f]=\int_{\mathcal Q}\mathrm dq\,\pi(q)\,f(q).$$
A different parameterization $\mathcal Q'$ has density $\pi'(q')$. The expectation value is invariant, so
$$\mathbb E_\pi[f]=\int_{\mathcal Q}\mathrm dq\,\pi(q)f(q)=\int_{\mathcal Q'}\mathrm dq'\,\pi'(q')f(q').$$
Computations must not depend on irrelevant details of the parameterization, such as the shape of the density (p. 4). For nontrivial targets the integrals are not analytic, so numerical methods are needed. Their accuracy is limited by finite computation (p. 4).

### 1.2 Parsimonious expectation computation (p. 5)
Computation is wasted where the integrand contributes negligibly (p. 5). A common intuition is to focus where the integrand is largest. The author assumes $f$ varies little compared with the density, since a method tuned to one function would need re-tuning for each new function (p. 5). (If only one expectation matters, exploiting $f$ can help a lot.) Under the assumption that $f$ varies little, the integrand's variation is dominated by the density, so one is led to consider the neighbourhood of the mode. This intuition is "fatally naive": expectations accumulate over volume, and there is little volume near the mode (p. 5). In high dimensions volume and density are in tension, so the important region lies away from both extremes (p. 5).

*Intuition note:* An integral adds up "height × width". The tallest point has almost no width, so it contributes little.

### 1.3 Geometry of high-dimensional spaces (pp. 6–7)
- **Box view (Fig. 1):** split each axis into 3 cells. The centre cell has weight $1/3,\ 1/9,\ 1/27$ in $D=1,2,3$. There are $3^D-1$ neighbouring cells, so the neighbours dominate quickly (p. 6).
- **Shell view (Fig. 2):** in 1-D the volumes a distance $\delta$ inside and outside a shell are equal. In 2-D and 3-D more volume lies outside (p. 6).
- **Conclusion:** volume is largest in the tails, and the disparity grows exponentially with dimension. This volume can compensate for the lower density, so the density and the volume must be balanced (pp. 6–7).

### 1.4 Geometry of high-dimensional distributions (pp. 7–8)
The **typical set** is the neighbourhood between the mode and the far tails. It is where density × volume gives significant contributions (p. 7).
- Densities and volumes transform oppositely under reparameterization, so the typical set is invariant (p. 7).
- With rising dimension the typical set becomes more singular, a manifestation of **concentration of measure**. Only the typical set contributes significantly to expectations, so we should average over it and focus computation there (pp. 7–8; Figs. 3–4).
- **Grid quadrature:** a grid of length $N$ in $D$ dimensions needs $N^D$ evaluations. Unless $N$ is incredibly large, it is unlikely that any point hits the narrow typical set (p. 8).
- Judging an algorithm by how it quantifies the typical set is a quick way to predict its performance (p. 8).

*Intuition note:* In high dimensions the significant probability mass sits in a narrow region away from the peak. A sampler that cannot find this region wastes its work.

### 2. Markov chain Monte Carlo (pp. 8–16)
MCMC uses a Markov chain to explore the typical set stochastically, giving a random grid across high-probability regions (pp. 8–9). A properly designed chain eventually explores any typical set. The practical question is whether it does so in finite time (p. 9).

### 2.1 Estimating expectations with Markov chains (pp. 9–11)
A **Markov transition** is a random map, or equivalently a conditional density $T(q'\mid q)$. A chain applies it repeatedly (p. 9). An arbitrary chain is useless for expectations. The special case is a transition that **preserves the target**:
$$\pi(q)=\int_{\mathcal Q}\mathrm dq'\,\pi(q')\,T(q\mid q').$$
Samples from $\pi$ pushed through $T$ remain distributed as $\pi$ (p. 9). Then, from any start, the chain drifts into and across the typical set (p. 10; Fig. 6). The chain history $\{q_0,\dots,q_N\}$ gives the estimator
$$\hat f_N=\frac1N\sum_{n=0}^N f(q_n),$$
and, "up to some technicalities", $\lim_{N\to\infty}\hat f_N=\mathbb E_\pi[f]$ (pp. 10–11). This asymptotic result has limited practical use, so finite-time behaviour matters (p. 11).

### 2.2 Ideal behavior (pp. 11–13)
Under ideal conditions there are three phases (p. 11; Fig. 7):
1. The chain converges to the typical set, and estimators have strong bias.
2. It finds the typical set and makes the first sojourn through it, and bias is rapidly removed.
3. It refines its exploration, and precision improves more slowly.

Once in phase 3, a central limit theorem holds:
$$\hat f_N^{\rm MCMC}\sim\mathcal N\big(\mathbb E_\pi[f],\ \text{MCMC-SE}\big),\qquad \text{MCMC-SE}\equiv\sqrt{\frac{\mathrm{Var}_\pi[f]}{\mathrm{ESS}}},$$
$$\mathrm{ESS}=\frac{N}{1+2\sum_{l=1}^\infty\rho_l},$$
where $\rho_l$ is the lag-$l$ autocorrelation of $f$ over the chain's history (p. 11). ESS is the number of exact samples with equivalent estimator precision. It can also be read as the number of sojourns across the typical set. It is estimated from the chain, with care to avoid bias (p. 11). **Warm-up** means discarding the initial converging samples. It can also be used to tune the transition's free parameters without biasing later estimators (p. 13).

*Intuition note:* Correlated samples carry less information than independent ones. ESS counts how many independent samples the chain is "worth".

### 2.3 Pathological behavior (pp. 13–15)
The ideal behaviour requires that the transition is compatible with the target's structure (p. 13).
- **Mechanism:** where the typical set pinches into a high-curvature region (Fig. 8), most transitions cannot resolve it. The chain ignores the region, so estimators are biased (p. 13).
- **Compensation:** because the chain must recover exact expectations asymptotically, it typically gets stuck near the boundary. Estimators are drawn toward the truth, then overcorrect, and the chain escapes (p. 13; Fig. 9).
- **Result:** estimators oscillate around the truth. Terminating after finite time almost always breaks the balance and gives substantial bias (pp. 13–15).
- Whether a feature is pathological depends on how the transition interacts with it. Some transitions are more robust, and some can be tuned to be (p. 15).
- **Geometric ergodicity** is the sufficient condition guaranteeing the ideal behaviour, notably a CLT. It is very hard to verify theoretically for all but the simplest problems (p. 15).
- **Split $\hat R$** is an empirical diagnostic. It measures variation across chains started from different points. If it is not near 1, we should be suspicious that geometric ergodicity holds (p. 15).

### 2.4 The Metropolis–Hastings algorithm (pp. 15–16)
Metropolis–Hastings builds transitions automatically in two steps: a **proposal** (any stochastic perturbation) and a **correction** (rejecting proposals that stray from the typical set). With proposal density $Q(q'\mid q)$, the acceptance probability is
$$a(q'\mid q)=\min\!\left(1,\ \frac{Q(q\mid q')\,\pi(q')}{Q(q'\mid q)\,\pi(q)}\right).$$
**Random Walk Metropolis** uses $Q(q'\mid q)=\mathcal N(q'\mid q,\Sigma)$. The proposal is symmetric, so $Q$ cancels:
$$a(q'\mid q)=\min\!\left(1,\ \frac{\pi(q')}{\pi(q)}\right)$$
(pp. 15–16). Intuition: proposals favour large volume (the tails), and the correction rejects those landing at too-small density (p. 16).

**Failure in high dimension:** the volume outside the typical set overwhelms the volume inside, so almost every proposal lands in the tails and the acceptance probability is negligible (p. 16; Fig. 10a). Shrinking the proposal keeps points inside the typical set but moves the chain extremely slowly (Fig. 10b). Whatever the tuning of $\Sigma$, exploration is extremely slow in all but the lowest dimensions. In the worst case not even one sojourn is completed, and in milder cases autocorrelations are large (p. 16). We need to exploit the geometry of the typical set (p. 16).

*Intuition note:* RWM guesses a direction at random. In high dimensions almost all directions leave the typical set, so guesses are rejected or tiny.

### 3. Foundations of Hamiltonian Monte Carlo (pp. 16–21, partial)
Guess-and-check fails because there are exponentially many directions to guess but only a "singular" number that stay in the typical set (p. 16). We need transitions that follow contours of high probability mass and glide coherently (p. 17; Fig. 11). The author states that HMC is the unique procedure for generating this exploration automatically, for sufficiently well-behaved targets (p. 17).

### 3.1 Informing effective Markov transitions (pp. 17–21, to the end of this part)
- A **vector field** (a direction at every point) aligned with the typical set could guide us. Following it a small step gives a new point and a new direction, which traces a coherent trajectory (p. 17; Fig. 12).
- The extra information in the target is the **gradient** of the density, which gives a vector field sensitive to the target's structure (p. 19).
- **Problem:** the gradient is never aligned with the typical set. It pulls toward the mode (p. 19). The density and its gradient depend on the parameterization, so the gradient directs us to parameterization-sensitive places like the mode, not to the invariant typical set (p. 19).
- We must add geometric constraints that remove the parameterization dependence and twist the directions into alignment. Differential geometry gives such a procedure, but it is hard to learn (p. 19).
- **Physical equivalence:** the same mathematics describes classical physics. Mode ↔ planet, gradient ↔ gravitational field, typical set ↔ orbit; exploring means putting a satellite in stable orbit (p. 20; Fig. 14).
- A satellite at rest crashes into the planet, as gradient-following crashes into the mode (p. 20; Fig. 15). The fix is to give it momentum against gravity. Too little transverse momentum and it still crashes (Fig. 16a). The text on this page ends mid-sentence, with "if we add too much momentum…" (p. 20).

*Intuition note:* Following the gradient pulls the motion uphill into the mode. In the satellite picture, giving the object momentum lets it stay in orbit instead of crashing. The text of this part breaks off before saying how much momentum is needed.

## Toy example (ours, not from the source)
**Setup:** split every axis into 3 equal cells, so there are $3^D$ cells of equal volume. Suppose the density is constant within a cell, and the centre cell has density 20 times that of every other cell (say 20 vs. 1, in arbitrary units). The centre cell then has mass ∝ $20\times$ volume. The other $3^D-1$ cells have mass ∝ $1\times$ volume each.

Share of mass in the centre $=\dfrac{20}{20+(3^D-1)}$:
- $D=1$: $20/(20+2)=20/22\approx0.91$
- $D=2$: $20/(20+8)=20/28\approx0.71$
- $D=3$: $20/(20+26)=20/46\approx0.43$
- $D=5$: $3^5-1=242$, so $20/262\approx0.076$
- $D=10$: $3^{10}-1=59048$, so $20/59068\approx0.00034$

Even a 20-fold density advantage is overwhelmed by volume. The mode region's share of expectations collapses as $D$ grows, as in §1.3 (p. 6).

**ESS check:** if $\rho_1=0.5$ and $\rho_l=0$ for $l\ge2$, with $N=1000$, then $\mathrm{ESS}=1000/(1+2\cdot0.5)=500$. The chain is worth 500 exact samples (formula p. 11).

## Concepts
- [[typical-set]] — region between mode and tails, where density × volume is significant; invariant under reparameterization (p. 7)
- [[markov-chain-monte-carlo]] — a chain whose transition preserves the target; its history estimates expectations (pp. 9–10)
- [[metropolis-hastings]] — proposal plus accept/reject correction with the ratio above (p. 15)
- [[convergence-diagnostics]] — here: split $\hat R$ as the empirical diagnostic, with geometric ergodicity as the formal sufficient condition (p. 15); ESS measures estimator precision (p. 11)
- [[monte-carlo-integration]] — averaging $f$ over the chain history to estimate $\mathbb E_\pi[f]$ (p. 10)
- [[concentration-of-measure]] (new) — typical set becomes more singular as dimension grows (p. 7)
- [[effective-sample-size]] (new) — $N/(1+2\sum\rho_l)$; exact-sample equivalent of a chain (p. 11)
- [[warm-up]] (new) — discarding initial converging samples; can also tune the transition (p. 13)
- [[geometric-ergodicity]] (new) — sufficient condition for ideal behaviour, including a CLT; hard to verify (p. 15)
- [[random-walk-metropolis]] (new) — Metropolis–Hastings with a Gaussian proposal; scales poorly with dimension (pp. 15–16)

## Canonical instances
- [[grid-quadrature-curse]] — $N^D$ evaluations; grid misses the typical set (p. 8)
- [[box-partition-volume]] — $3^D-1$ neighbours of the centre cell (p. 6)
- [[curvature-stuck-chain]] — chain stuck at a high-curvature neck; oscillating estimators (pp. 13–14)
- [[rwm-high-dimension-failure]] — large proposals rejected, small proposals slow (p. 16)
- [[satellite-orbit-analogy]] — planet = mode, gravity = gradient, orbit = typical set (pp. 20–21)

## Bridges (candidates)
- [structural-analogy] Typical set ↔ statistical mechanics/information theory: mass concentrates away from the peak in a thin shell — the pattern looks the same, but this unit does not state the link.
- [same-math] ESS formula ↔ time-series analysis: integrated autocorrelation time $1+2\sum\rho_l$ (canon link; not stated in this unit).
- [metaphor] Gradient crashing into the mode ↔ optimization: gradient ascent/MAP finds the mode, which the typical set avoids.

## Questions this raises
- How exactly is momentum added so that motion stays on the typical set, and what makes the construction parameterization-invariant?
- How fast does the typical set narrow with dimension for a concrete distribution such as a Gaussian?
- How well does split $\hat R$ detect a pathology if all chains miss the same hidden region?
- Is "unique" in the claim about HMC (p. 17) a precise theorem, and under what conditions?

## Reading notes
- Part 1 of 3: starts at the title/abstract (p. 1) and ends on p. 21, inside §3.1. The text breaks off mid-sentence at the bottom of p. 20, in the argument about momentum; p. 21 has only Figs. 14–15 (Fig. 16 and the rest of §3.1 are not in this part). Sections 3.2 onwards are not covered. Split at a section boundary, per the source note; printed = pdf page numbers.
- Page images for pp. 4, 7, 8, 11 were checked. Other pages were taken from the text layer; figures were not inspected beyond their captions.
- Misprint on p. 4: the second integral over $\mathcal Q'$ in the displayed pair shows $\pi(q')$ without a prime. The next display has $\pi'(q')$, the intended form.
- The caption of Fig. 7c (p. 12) says estimator precision is "reducing … towards zero". The text on p. 11 says precision improves; read the caption as the error shrinking.
- In §1.4 (p. 7) "complimentary neighborhood" is a misspelling of "complementary". Several other typos (e.g. "motiving", p. 3) are harmless.
