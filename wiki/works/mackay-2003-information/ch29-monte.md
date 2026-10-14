---
id: mackay-2003-information/ch29-monte
work: mackay-2003-information
unit: "29 Monte Carlo Methods"
pages: 356-386
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Monte Carlo Methods (MacKay, ch. 29)

## L0 — One line
When a high-dimensional density can only be evaluated up to a constant, importance and rejection sampling are expected to degrade exponentially with dimension, so one uses Markov chain methods (Metropolis, Gibbs, slice), which scale well with dimension but move by slow random walks.

## L1 — The gist (≤ 120 words)
How can we draw samples from, or compute averages under, a complicated high-dimensional distribution P(x) = P*(x)/Z when we can only evaluate P*? The chapter shows that uniform sampling, importance sampling and rejection sampling tend to break down in high dimensions, because the typical set is tiny and the weights or bounding constants grow exponentially. Markov chain methods (Metropolis, Gibbs, slice sampling) avoid that catastrophe, but they explore by slow random walks and need at least about (L/ε)² steps per independent sample. The accuracy of a Monte Carlo average depends on σ²/R, not on dimension, so about a dozen independent samples may suffice.

**Prerequisites:** probability densities and expectations; variance; Gaussian distributions; typical sets (Part I); Markov chains and transition matrices as eigenvector problems; basic Bayesian posteriors.

## L2 — Key ideas
- Monte Carlo has two aims: generate samples from P(x), and estimate expectations Φ = ⟨φ⟩. The estimator's variance is σ²/R whatever the dimension, so a dozen independent samples may suffice (p. 357–358).
- The hard part is sampling. We usually do not know Z, and enumerating states costs exponentially much (e.g. 2^1000 for 1000 spins). Uniform sampling needs about 2^(N−H) samples to hit the typical set once (p. 358–361).
- Importance sampling estimates Φ with weights w = P*/Q*. It is hard to know its reliability, the sampler should have heavy tails (slowly decaying, e.g. Cauchy rather than Gaussian), and in the N-dimensional sphere–Gaussian case study the largest weight among 100 samples is about exp(√(2N)) times the median (p. 362–364).
- Rejection sampling gives independent samples but needs c with cQ* > P*. In the N-dimensional Gaussian case study c grows exponentially, so the acceptance rate is expected to be exponentially small (p. 364–365).
- Metropolis accepts a proposed move with probability min(1, a), where a is the ratio of target values P*(x')/P*(x) times a proposal-density correction (29.31). It has no catastrophic dependence on N, but needs at least about (L/ε)² iterations per independent sample because it is a random walk (p. 366–370).
- Gibbs sampling is Metropolis with conditional proposals that are always accepted. It has no tunable parameters but is also a slow random walk unless the parameterization makes P separable (p. 370–371).
- MCMC theory: a chain needs P as an invariant distribution (one the chain leaves unchanged) and must be ergodic (the state distribution converges to P from any start). Detailed balance, $T(a;b)P(b)=T(b;a)P(a)$, implies invariance (p. 372–374).
- Slice sampling self-tunes its step size: too-small w costs linear in f, too-large costs logarithmic in F, and it has no rejections (p. 374–377).
- Practical points: Z is hard to get from MCMC; proposal widths must not adapt to history; run strategies trade convergence against independence; dependent samples can be averaged without bias (p. 379–381).

## L3 — Walkthrough

### Preface to the chapter (p. 356)
Laplace's method (Gaussian fit at the posterior maximum) can fail, e.g. in clustering, where the likelihood is multimodal with unbounded spikes. Monte Carlo methods are the general-purpose alternative (p. 356).

The chapter covers importance, rejection, Metropolis, Gibbs and slice sampling, and asks of each whether it suits high dimensions (p. 356). Conventions:
- A "sample" is a single realization x from P(x), not a collection (p. 356).
- Matrices act to the right: $u = Mv$ (29.1), not $u^T = v^T M^T$ (29.2).
- $T_{ij} = T_{i|j}$ is the probability of going from state j to state i, so columns are probability vectors. $T(x';x)$ is the density of going from x to x'. The sequence xyz has probability $T(z;y)T(y;x)\pi(x)$ (p. 356).

### 29.1 The problems to be solved (p. 357–361)
**Problem 1:** generate samples $\{x^{(r)}\}_{r=1}^R$ from the target density P(x). **Problem 2:** estimate
$$\Phi = \langle\phi(x)\rangle \equiv \int d^N x\, P(x)\phi(x). \tag{29.3}$$
Means and variances come from first and second moments:
$$\Phi_1 \equiv \mathcal E[\phi_1(x)],\ \Phi_2 \equiv \mathcal E[\phi_2(x)] \tag{29.4}$$
$$\bar t = \Phi_1,\qquad \mathrm{var}(t) = \Phi_2 - \Phi_1^2 \tag{29.5}$$
with $\phi_1 = t(x)$ and $\phi_2 = (t(x))^2$ (p. 357).

If problem 1 is solved, problem 2 follows from
$$\hat\Phi \equiv \frac1R\sum_r \phi(x^{(r)}). \tag{29.6}$$
If the $x^{(r)}$ come from P, then $\mathbb E[\hat\Phi]=\Phi$, and the variance of $\hat\Phi$ decreases as $\sigma^2/R$ with
$$\sigma^2 = \int d^N x\, P(x)(\phi(x)-\Phi)^2. \tag{29.7}$$
The accuracy depends only on the variance of φ, not on dimension. As few as a dozen independent samples may suffice (p. 357–358).

*Intuition note.* Averaging R independent draws shrinks error like $1/\sqrt R$, however many coordinates x has. The catch is the word "independent". Getting independent draws from P is the hard part (p. 358).

**Why sampling is hard.** We assume we can evaluate $P^*$ with
$$P(x)=P^*(x)/Z,\qquad Z=\int d^N x\,P^*(x). \tag{29.8, 29.9}$$
There are two difficulties. First, Z is typically unknown. Second, even if Z were known, there is no obvious way to find where P is big without evaluating it everywhere. Few high-dimensional densities, e.g. the Gaussian, are easy to sample (p. 358).

The running 1-D example is $P^*(x)=\exp[0.4(x-0.4)^2-0.08x^4]$ (29.10), plotted in figure 29.1 (p. 358).

**Discretizing.** On a grid, compute $Z=\sum_i p_i^*$ (29.11) and $p_i=p_i^*/Z$ (29.12). The cost is a visit to every point. With 50 grid points per dimension and N = 1000 this is 50^1000 evaluations. With two values per component it is still 2^1000. Take 2^266 electrons, each a computer doing 2^40 evaluations per second for 2^58 seconds (the age of the universe). They would visit only 2^364 states, so one would wait about 2^636 ≃ 10^190 universe ages (p. 359).

Such systems are common. An example is a 30×30 Ising model with
$$P^*(x)=\exp[-\beta E(x)],\quad x_n\in\{\pm1\},\quad E(x)=-\Big[\tfrac12\sum_{m,n}J_{mn}x_mx_n+\sum_nH_nx_n\Big]. \tag{29.13, 29.14}$$
E is easy to evaluate for one state, but evaluating all states costs 2^1000 evaluations. Generating exact samples was achieved by Propp and Wilson (1996), to be described in Chapter 32 (p. 359).

**Lake analogy.** The depth of a lake at x is $P^*(x)$ and the plankton concentration is φ(x). Then $\Phi=\frac1Z\int d^N x\,P^*(x)\phi(x)$ (29.15), and Z is the lake's volume. With a boat, a navigation system and a plumbline, we can measure $P^*$ and φ at any chosen point. Problem 1 is to draw water samples equally likely from any point of the lake. Problem 2 is to find the average concentration. If much volume lies in narrow deep canyons (figure 29.3), the method must implicitly find them (p. 359–360).

**Uniform sampling.** Draw $x^{(r)}$ uniformly and set
$$Z_R=\sum_{r=1}^R P^*(x^{(r)}),\qquad \hat\Phi=\sum_{r=1}^R\phi(x^{(r)})\frac{P^*(x^{(r)})}{Z_R}. \tag{29.16, 29.17}$$
For benign φ, Φ is determined mainly by φ on the typical set T, with $|T|\simeq 2^{H(X)}$. So we need enough samples to hit T at least once or twice (p. 360).

Caveat from the author: an Ising model near a phase transition may not strictly have a typical set, since the energy variance (heat capacity) may diverge (p. 360). Each sample falls in T with chance $2^H/2^N$, so
$$R_{\min}\simeq 2^{N-H}. \tag{29.18}$$
At high temperature H → N bits and $R_{\min}$ is of order 1, so uniform sampling may be fine. At the critical temperature of the infinite Ising model, $\theta_c=2.27$, the entropy is roughly N/2 bits (figure 29.4), so
$$R_{\min}\simeq 2^{N-N/2}=2^{N/2}, \tag{29.19}$$
which for N = 1000 is about 10^150, roughly the square of the number of particles in the universe. Uniform sampling is "utterly useless" for Ising models of modest size, and in most high-dimensional problems with non-uniform P it is unlikely to help (p. 361).

*Intuition note.* In many high-dimensional problems almost all states are irrelevant, since the probability sits in a thin typical set. Throwing darts uniformly then almost never hits it.

### 29.2 Importance sampling (p. 361–364)
Importance sampling estimates expectations (problem 2). It does not generate samples from P. It can be viewed as a generalization of uniform sampling (p. 361).

**Setup.** P = P*/Z cannot be sampled directly. A simpler sampler density $Q=Q^*/Z_Q$ can be sampled and evaluated up to its constant. Draw $x^{(r)}\sim Q$. Where Q > P, points are over-represented, and where Q < P, under-represented. Correct this with weights
$$w_r\equiv \frac{P^*(x^{(r)})}{Q^*(x^{(r)})},\qquad \hat\Phi\equiv\frac{\sum_r w_r\phi(x^{(r)})}{\sum_r w_r}. \tag{29.21, 29.22}$$
Exercise 29.1 asks for a proof of convergence if Q(x) is non-zero wherever P(x) is (p. 362). The printed solution (p. 384–385) is as follows.
- $\langle w_r\rangle = Z_P/Z_Q$ and $\langle w_r\phi\rangle = (Z_P/Z_Q)\Phi$, so numerator/R and denominator/R converge to $(Z_P/Z_Q)\Phi$ and $Z_P/Z_Q$.
- The denominator converges if var(w) is finite. It also converges if the variance is infinite, as long as the expectation is well defined.
- Numerator and denominator are unbiased for $RZ_P\Phi/Z_Q$ and $RZ_P/Z_Q$, but their ratio is not necessarily unbiased for finite R (p. 385).

**Reliability.** The estimator's variance is unknown beforehand. The empirical variances of $w_r$ and $w_r\phi$ are not necessarily a good guide. If Q is small where $|\phi P^*|$ is large, no sample may land there. The estimate is then badly wrong with no warning in the empirical variance (p. 362).

**Cautionary illustration (p. 362–363).** In a toy amino-acid problem, a Gaussian sampler's estimate looked settled after about 500 samples but was wrong. After a million samples it still had not settled. A Cauchy sampler converged after about 5000 samples (figure 29.6). Lesson: an importance sampler should have heavy tails (p. 363).

Exercise 29.2 (multimodal P, unimodal Q fitted to one peak). The printed solution says it is unwise. Points landing in other modes get enormous weights, so the variance is huge but may stay invisible if no such point has been seen (p. 385).

**Many dimensions (p. 363–364).** Case study: P* uniform inside a sphere of radius $R_P$ (29.23), and Q a spherical Gaussian with variance σ² per axis (29.24). Using typical-set facts from Part I, the squared radius of a sample from Q satisfies
$$\rho^2\sim N\sigma^2\pm\sqrt{2N}\,\sigma^2. \tag{29.25}$$
So almost all samples lie near distance $\sqrt N\sigma$. Assume σ is chosen so that this typical set lies inside the sphere. If it does not, almost all samples have weight zero (p. 363). Then Q typically lies in
$$\frac{1}{(2\pi\sigma^2)^{N/2}}\exp\Big(-\frac N2\pm\frac{\sqrt{2N}}{2}\Big) \tag{29.26}$$
and the weights $P^*/Q$ typically lie in
$$(2\pi\sigma^2)^{N/2}\exp\Big(\frac N2\pm\frac{\sqrt{2N}}{2}\Big). \tag{29.27}$$
Doubling the standard deviation roughly estimates the largest-to-median ratio:
$$\frac{w^{\max}_r}{w^{\mathrm{med}}_r}=\exp(\sqrt{2N}). \tag{29.28}$$
For N = 1000 and 100 samples, the largest weight is roughly 10^19 times the median, so the estimate is likely dominated by a few samples (p. 364).

In conclusion, importance sampling in high dimensions often suffers from two difficulties. First, we must get samples into the typical set of P, which may take long unless Q is a good approximation. Second, even inside the typical set, the weights vary by factors of order $\exp(\sqrt N)$ unless Q is near-perfect (p. 364).

*Intuition note.* Points in a typical set have similar but not identical probabilities. With N coordinates, the log-probabilities scatter by about $\sqrt N$, so the ratios of weights scatter exponentially. A few samples are then likely to dominate the estimate.

### 29.3 Rejection sampling (p. 364–365)
Assume a proposal Q (sampleable, evaluable up to $Z_Q$) and a known constant c with
$$cQ^*(x)>P^*(x)\ \text{ for all }x. \tag{29.29}$$
Procedure:
1. Draw $x\sim Q$.
2. Draw $u\sim\mathrm{Uniform}[0,cQ^*(x)]$.
3. Accept x if $u\le P^*(x)$, otherwise reject. Rejected points are discarded, and u is discarded either way.

Why it works: (x, u) is uniform under the curve $cQ^*$, and the rule keeps those under $P^*$. These are uniform under $P^*$, so the x-coordinates have density ∝ P* and are independent samples (p. 364–365). It works best if Q approximates P, otherwise c must be large and rejections frequent (p. 365).

**Many dimensions.** Take two N-dimensional zero-mean Gaussians. Here P has standard deviation σ_P, and Q has σ_Q, which must be larger than σ_P for any c to exist. The required c is
$$c=\frac{(2\pi\sigma_Q^2)^{N/2}}{(2\pi\sigma_P^2)^{N/2}}=\exp\Big(N\ln\frac{\sigma_Q}{\sigma_P}\Big). \tag{29.30}$$
With N = 1000 and σ_Q/σ_P = 1.01, c = exp(10) ≃ 20,000. Both densities are normalized, so the acceptance rate is 1/c, here about 1/20,000. In general c grows exponentially with N, and the acceptance rate is expected to be exponentially small. Finding c can also be hard if we do not know where the modes are or how high (p. 365).

### 29.4 The Metropolis–Hastings method (p. 365–370)
**Algorithm.** The proposal $Q(x';x^{(t)})$ depends on the current state, e.g. a Gaussian centred on $x^{(t)}$. It can be any fixed density we can sample, and need not resemble P (p. 365). Compute
$$a=\frac{P^*(x')}{P^*(x^{(t)})}\frac{Q(x^{(t)};x')}{Q(x';x^{(t)})}. \tag{29.31}$$
If a ≥ 1, accept. Otherwise accept with probability a. If accepted, $x^{(t+1)}=x'$. If rejected, $x^{(t+1)}=x^{(t)}$ (p. 366).

Unlike rejection sampling, a rejection writes the current state onto the list again. T iterations give T *dependent* states, not T independent samples. The index t labels chain states and r labels independent samples (p. 366). For symmetric Q the Q-ratio is 1. The author calls even the asymmetric general case "the Metropolis method" for short (p. 366).

**Convergence.** For any positive Q (Q(x';x) > 0 for all x, x'), the distribution of $x^{(t)}$ tends to P as t → ∞. This does not require Q to be positive everywhere in every use, and says nothing about speed. Convergence and independence are hard to assess, as with importance-sampling variance (p. 366).

**Step size.** Typically ε, the proposal length scale, is short relative to the longest scale L of the probable region (figure 29.11, acceptance about 0.5). Large steps from a typical point usually land on very low probability and are rejected. Small steps give a random walk (p. 367). Exercise 29.3 asks to show that after T steps of size ε the state is likely to have moved only about $\sqrt T\epsilon$ (p. 367).

**Rule of thumb** (a lower bound): to get a roughly independent sample you need at least
$$T\simeq (L/\epsilon)^2 \tag{29.32}$$
iterations. If only a fraction f of steps are accepted, this time grows by a factor 1/f. It may be much worse if the distribution has several islands of high probability separated by low-probability regions (p. 367).

**Toy demonstration (p. 369).** Target: uniform on {0, …, 20}, so $P(x)=1/21$ (29.33). Proposal: $Q(x';x)=1/2$ for $x'=x\pm1$ (29.34). Rejections occur only when x' = −1 or 21. Starting at $x_0=10$, the rule predicts about 100 iterations to reach an end state, and the first end-state visit was at iteration 178. The rule predicts about 400 to traverse the space, and the other end was first reached at iteration 540. So about 400 iterations are needed per independent sample. A systematic sweep would take about 20 steps (p. 369).

**High dimensions (p. 369–370).** Take an N-dimensional axis-aligned Gaussian target with standard deviations σ_n and a spherical Gaussian proposal of width ε. Suppose ε is tuned so the acceptance frequency is near 1. Each coordinate then does its own random walk, and the time is controlled by σ^max: $T\simeq(\sigma^{\max}/\epsilon)^2$. If ε > σ^min the acceptance rate falls sharply, so the optimal ε is plausibly similar to σ^min. The author notes this may fail in special cases, where the optimum may be nearer the second-smallest σ_n. The rough conclusion:
$$T\gtrsim(\sigma^{\max}/\sigma^{\min})^2$$
iterations per independent sample with simple spherical proposals (p. 369). There is no catastrophic dependence on N, unlike importance and rejection sampling, but the quadratic dependence on the length-scale ratio can still force long runs (p. 370).

*Intuition note.* The method pays in time, not in an exponential factor of dimension. The price is that the walk must creep across the distribution in small steps, so time grows as distance squared.

### 29.5 Gibbs sampling (p. 370–371)
Gibbs sampling ("heat bath", "Glauber dynamics") needs at least two dimensions. It is a Metropolis method whose proposals come from the conditionals $P(x_i\mid\{x_j\}_{j\ne i})$. These are assumed tractable, which holds for many but not all graphical models. Non-standard conditionals may be sampled by adaptive rejection sampling if they satisfy convexity properties (p. 370). One iteration for K variables:
$$x_1^{(t+1)}\sim P(x_1\mid x_2^{(t)},\dots,x_K^{(t)}) \tag{29.35}$$
$$x_2^{(t+1)}\sim P(x_2\mid x_1^{(t+1)},x_3^{(t)},\dots,x_K^{(t)}) \tag{29.36}$$
$$x_3^{(t+1)}\sim P(x_3\mid x_1^{(t+1)},x_2^{(t+1)},\dots,x_K^{(t)}),\ \text{etc.} \tag{29.37}$$
Exercise 29.4 asks to show that a single-variable update is a Metropolis method in which every proposal is always accepted (p. 371). Because it is a Metropolis method, the distribution of $x^{(t)}$ tends to P as long as P has no pathological properties (p. 371).

Exercise 29.5 (syndrome decoding, posterior 29.38, with the factor $\mathbb 1[Hn=z]$). The printed solution says the posterior is pathological for Gibbs sampling:
- Only the 2^K codeword-compatible vectors have non-zero probability, and no two are adjacent.
- So one bit flip leads to zero probability and the chain never moves. The solution says a general code has the same problem, since valid codewords are few and not adjacent (at least for any useful code).
- Using the message bits s as variables avoids lock-up, but for a good code any single flip changes the codeword substantially, so escaping a good state takes impractically long (p. 385).

**High dimensions.** Gibbs sampling is also a slow random walk unless the parameterization makes P separable. For strongly correlated $x_1, x_2$ with marginal width L and conditional width ε, it needs at least about $(L/\epsilon)^2$ iterations. It has no adjustable parameters, which is attractive for quick model building. The package BUGS sets up models and simulates them by Gibbs sampling (p. 371).

### 29.6 Terminology for MCMC (p. 372–374)
Let $p^{(t)}(x)$ be the state distribution of the chain (imagine infinitely many parallel simulators). A chain is specified by an initial $p^{(0)}$ and a transition probability T:
$$p^{(t+1)}(x')=\int d^Nx\,T(x';x)\,p^{(t)}(x). \tag{29.39}$$
Example 29.6 is the 21-state chain of section 29.4. Its T has entries 1/2 on the two off-diagonals, plus 1/2 at the two corners (1/2 1/2 at the first and last rows). Starting from $p^{(0)}$ concentrated on x = 10 (29.40), figures 29.14–29.15 show $p^{(t)}$ converging to the uniform density, also from $x_0=17$ (p. 372–373).

**Required properties.**
1. P must be an *invariant distribution*:
$$\pi(x')=\int d^Nx\,T(x';x)\pi(x). \tag{29.41}$$
It is an eigenvector of T with eigenvalue 1 (p. 372).
2. The chain must be *ergodic*:
$$p^{(t)}(x)\to\pi(x)\ \text{as }t\to\infty,\text{ for any }p^{(0)}. \tag{29.42}$$

Two ways ergodicity can fail (p. 373):
- (a) *Reducible*: the space has subsets that cannot be reached from each other. There are then many invariant distributions, and the limit depends on $p^{(0)}$. T has more than one eigenvalue equal to 1.
- (b) *Periodic*: the distribution tends to a limit cycle. Example: the random walk on the N-dimensional hypercube. Its unique invariant distribution is uniform over 2^N states, but the chain has period two (odd and even parity alternate). T then has eigenvalues +1 and −1, so more than one eigenvalue has magnitude 1.

**Construction.** Use base transitions B that all satisfy
$$P(x')=\int d^Nx\,B(x';x)P(x). \tag{29.43}$$
They need not be individually ergodic. A *mixture* picks a base transition at random: $T(x',x)=\sum_b p_bB_b(x',x)$ (29.44). A *concatenation* applies B₁ then B₂: $T(x',x)=\int d^Nx''\,B_2(x',x'')B_1(x'',x)$ (29.45) (p. 373).

**Detailed balance.**
$$T(x_a;x_b)P(x_b)=T(x_b;x_a)P(x_a)\ \ \text{for all }x_a,x_b. \tag{29.46}$$
If a state is drawn from P and moved by T, going b→a is as likely as a→b. Such chains are called reversible. Detailed balance implies invariance of P, which is a necessary condition for convergence to P (Exercise 29.7: prove it). Metropolis satisfies detailed balance. It is not essential: irreversible chains can be useful, because they may have different random-walk properties (p. 374).

Exercise 29.8 asks to show that concatenating two base transitions that satisfy detailed balance does not necessarily give T satisfying it. Exercise 29.9 asks whether Gibbs sampling with a deterministic update sequence satisfies it (p. 374).

### 29.7 Slice sampling (p. 374–378)
Slice sampling (Neal) can be used wherever Metropolis can, i.e. wherever $P^*$ can be evaluated. It is more robust to step-size parameters. It resembles Gibbs sampling (one-dimensional transitions, but no need for easy or convex conditionals) and rejection sampling (it asymptotically samples the area under $P^*$, but needs no upper-bounding function) (p. 374).

**Skeleton (1-D).** A transition $(x,u)\to(x',u')$ between points under the curve:
1. Evaluate $P^*(x)$.
2. Draw $u'\sim\mathrm{Uniform}(0,P^*(x))$.
3. Create an interval $(x_l,x_r)$ enclosing x.
4. Loop: draw $x'\sim\mathrm{Uniform}(x_l,x_r)$ and evaluate $P^*(x')$. If $P^*(x')>u'$, stop. Otherwise modify the interval (step 8).

The overall method must satisfy detailed balance, so that the uniform distribution under the curve is invariant (p. 375).

**Stepping out (step 3).** Draw $r\sim U(0,1)$. Set $x_l:=x-rw$ and $x_r:=x+(1-r)w$. While $P^*(x_l)>u'$, set $x_l:=x_l-w$. While $P^*(x_r)>u'$, set $x_r:=x_r+w$ (p. 375).

**Shrinking (step 8).** If $x'>x$ set $x_r:=x'$, else set $x_l:=x'$. The original x stays in the interval (p. 375).

**Properties.** Slice sampling is also a random walk, but its step size self-tunes (p. 376–377).
- If w is too small by a factor f, stepping out expands the interval at cost linear in f. Metropolis costs time scaling as f².
- If w is too large by a factor F, shrinking takes time proportional to log F, since the interval typically shrinks by a factor of about 0.6 per rejected point. Metropolis responds with almost all proposals rejected, which is exponentially bad in F.
- There are no rejections in slice sampling, and staying in exactly the same place has very small probability (p. 377).

Exercise 29.10 uses the density of figure 29.17 (p. 377).

**Real problems.** For N dimensions, pick directions $y^{(t)}$ and slice-sample along $x=x^{(t)}+xy^{(t)}$ using $P^*(x^{(t)}+xy^{(t)})$. Directions may be coordinate axes or random, as long as detailed balance holds (p. 377).

**Computer-friendly version (Skilling, p. 377–378).** Represent x by a b-bit integer X with B = 2^b values, which removes floating-point rounding errors in detailed balance. For a nonlinear map the density becomes $P^{**}(X)\propto P^*(x)|dx/dX|$. Operators available: addition and subtraction mod B, bitwise XOR ⊕, and `randbits(l)`. Given X and a height $Y=P^*(X)\times U(0,1)$:
1. $U:=\mathrm{randbits}(b)$ (random translation of the coordinate system).
2. Set l ≤ b.
3. Repeat: $N:=\mathrm{randbits}(l)$; $X':=((X-U)\oplus N)+U$; $l:=l-1$. Stop when $X'=X$ or $P^*(X')\ge Y$.

Termination at or before l = 0 is assured. U avoids permanent sharp edges, e.g. between 0111111111 and 1000000000. The interval is halved each time while keeping the previous point (figure 29.18). If stepping out is needed, step 2 is replaced by a loop that sets l < b, repeats the randomization with $l:=l+1$, and stops when l = b or $P^*(X')<Y$. Variants change l by Δl > 1 (any assigned distribution, possibly including 0). Exercise 29.11 (difficulty [4]) asks you to prove that choosing Δl depending on Y − P*(X') does not spoil validity. A single integer can encode several real parameters through a space-filling (Peano) curve, so the same code does multi-dimensional slice sampling (p. 378).

### 29.8 Practicalities (p. 379)
Lower bounds on convergence time come from random-walk arguments. Precise prediction is hard, and most theoretical upper bounds are of little practical use. The exact sampling of Chapter 32 solves this for certain chains. Diagnosing convergence is also hard, and available tools are imperfect (Cowles and Carlin, 1996). Speed-ups (Hamiltonian Monte Carlo, overrelaxation, simulated annealing) come in the next chapter (p. 379).

### 29.9 Further practical issues (p. 379–381)
**Normalizing constant.** Monte Carlo does not readily give Z; it is an active research area. Techniques listed: importance sampling and annealed importance sampling, thermodynamic integration / acceptance ratio / umbrella sampling, reversible jump MCMC. One may sometimes avoid Z, e.g. by one hierarchical model with continuous hyperparameters instead of several models. The author says he is not endorsing this: Z is often the single most important number, and he thinks every effort should go into computing it (p. 379).

**Metropolis for big models.** Use several proposals $Q^{(b)}$, each updating some components, each accepted or rejected individually, run in sequence (p. 379). Exercise 29.12 asks why this moves faster than one concatenated proposal when each has acceptance rate f < 1/2. The printed solution argues that, if f is small, the mean energy change per move is some ΔE > 0, so the concatenated acceptance scales roughly as f^B and the mean-square distance moved is of order f^B Bε², against f Bε² when moves are considered individually (p. 386).

Widths are set by trial and error, aiming for a rejection frequency of about 0.5. It is *not* valid to adapt widths dynamically depending on the simulation history, because this would violate detailed balance (p. 380).

**Gibbs in big models.** Sample groups of variables jointly:
$$x_1^{(t+1)},\dots,x_a^{(t+1)}\sim P(x_1,\dots,x_a\mid x_{a+1}^{(t)},\dots,x_K^{(t)}) \tag{29.47}$$
and so on for the next groups (p. 380).

**How many samples?** The variance of $\hat\Phi$ depends on the number of independent samples R and on σ² (29.48). In the pipeline example, x is the corrosion in each of 10,000 pipes and φ the repair cost. The author suggests there is little point knowing Φ to better than about σ/3, because the true cost likely differs by ±σ. With R = 12 independent samples the precision is $\sigma/\sqrt{12}$, smaller than σ/3, so twelve samples suffice (p. 380).

**Allocation of resources.** An experiment has an adjustment period, a burn-in, and then recording. Three strategies (figure 29.19):
1. One long run.
2. A few medium runs from different starts.
3. R short runs, recording only each final state.

Strategy 1 has the best chance of convergence. Strategy 3 may give less correlated samples. The middle path is popular with MCMC experts because it avoids repeated burn-in waste and can still reveal non-convergence. Samples need not be nearly independent: averaging dependent points does not bias the estimate, though estimating its accuracy is harder (p. 381).

### 29.10 Summary (p. 381–382)
- Monte Carlo can sample any P(x) = P*(x)/Z and answer queries as $\int\phi P\simeq\frac1R\sum_r\phi(x^{(r)})$ (29.49).
- In high dimensions the only satisfactory methods are Markov-chain based: Metropolis, Gibbs, slice.
- Gibbs has no adjustable parameters but needs samplable conditionals. Slice sampling has step-length parameters, but its performance is not very sensitive to them.
- Simple Metropolis and Gibbs explore by slow random walks. Slice sampling does not avoid the random walk, but chooses the largest appropriate step size automatically (p. 382).

### 29.11–29.12 Exercises and solutions (p. 382–386)
Exercise 29.13: importance sampling can fail even in 1-D with Gaussians P (std σ_p) and Q (std σ_q). The printed solution (p. 386):
- The mean weight is 1.
- The variance of the weights is finite only if $\sigma_q^2>\tfrac12\sigma_p^2$ (29.61).
- When that holds,
$$\mathrm{var}(w)=\frac{\sigma_q^2}{\sigma_p\,(2\sigma_q^2-\sigma_p^2)^{1/2}}-1. \tag{29.62}$$
- The variance becomes infinite as σ_q approaches about 0.7σ_p. The empirical standard deviation of the weights can look small (e.g. σ_q ≃ 0.3) even though the true one is infinite (figure 29.20).

The other exercises ask for implementations (29.15–29.17), step-size and scaling analyses (29.18–29.20), a variant of the toy chain (29.14), and a philosophical question about a Bayesian Monte Carlo method (29.21). Exercise 29.21 notes that Monte Carlo estimators depend on the proposal distributions and the random numbers used, whereas a Bayesian approach would depend only on the computed $P^*$ values (p. 382–384).

## Toy example (ours, not from the text)
Target on states {1, 2, 3} with unnormalized $P^*=(1,2,1)$. Z is never needed. Use the symmetric proposal "pick one of the other two states with probability 1/2 each". Then $a=P^*(x')/P^*(x)$.

Transition probabilities $T(\text{to};\text{from})$:
- From 1: to 2: ½·min(1, 2/1) = ½. To 3: ½·min(1, 1/1) = ½. Stay: 0.
- From 2: to 1: ½·(1/2) = ¼. To 3: ¼. Stay: 1 − ¼ − ¼ = ½.
- From 3: to 1: ½. To 2: ½. Stay: 0.

Check that $\pi=(\tfrac14,\tfrac12,\tfrac14)$ (that is, P*/4) is invariant:
- $\pi'(1)=0\cdot\tfrac14+\tfrac14\cdot\tfrac12+\tfrac12\cdot\tfrac14=\tfrac18+\tfrac18=\tfrac14$.
- $\pi'(2)=\tfrac12\cdot\tfrac14+\tfrac12\cdot\tfrac12+\tfrac12\cdot\tfrac14=\tfrac18+\tfrac14+\tfrac18=\tfrac12$.
- $\pi'(3)=\tfrac14$ by symmetry.

Detailed balance for 1↔2: $T(2;1)\pi(1)=\tfrac12\cdot\tfrac14=\tfrac18$ and $T(1;2)\pi(2)=\tfrac14\cdot\tfrac12=\tfrac18$. ✓.

One step by hand: at state 2, proposing 1 gives a = 1/2. If the uniform draw is 0.7 > 0.5, reject and write state 2 again. At state 1, proposing 2 gives a = 2 ≥ 1, so always accept.

## Concepts
- [[monte-carlo-integration]] — approximate ⟨φ⟩ by averaging φ over samples; error variance σ²/R, independent of dimension (p. 357)
- [[typical-set]] — region holding most probability, size about 2^H; uniform sampling needs about 2^(N−H) draws to hit it (p. 360)
- [[importance-sampling]] (new) — estimate Φ from Q-samples using weights P*/Q* and a ratio estimator; needs heavy-tailed Q; not a sampler (p. 361–362)
- [[rejection-sampling]] (new) — accept (x, u) under P* within the envelope cQ*; gives independent samples, acceptance rate 1/c for normalized densities (p. 364–365)
- [[metropolis-hastings]] — propose from Q(x'; x), accept with min(1, a), a from (29.31); a rejection repeats the state (p. 365–366)
- [[markov-chain-monte-carlo-mcmc]] — generate dependent states from a chain whose long-run distribution is P (p. 366)
- [[gibbs-sampling]] — update one variable (or group) at a time from its conditional; a Metropolis method with all proposals accepted (p. 370–371)
- [[slice-sampling]] (new) — sample uniformly under the curve P* via interval stepping-out and shrinking; self-tuning step size (p. 374–375)
- [[random-walk-rule-of-thumb]] (new) — an MCMC with step ε in a region of scale L needs at least about (L/ε)² iterations per independent sample (p. 367)
- [[invariant-distribution-ergodicity]] (new) — π is invariant if it is an eigenvector of T with eigenvalue 1; ergodic means p^(t) → π from any start (p. 372–373)
- [[detailed-balance]] (new) — T(a;b)P(b) = T(b;a)P(a); implies invariance; defines reversible chains (p. 374)
- [[marginal-likelihood-evidence]] — the normalizing constant Z, which MCMC does not readily give; author considers it often the most important number (p. 379)
- [[convergence-diagnostics]] — detecting convergence and independence of an MCMC run is hard; the author lists no perfect tool (p. 366, 379)

## Canonical instances
- [[ising-model-sampling]] — 2^1000 states; uniform sampling needs about 10^150 samples at criticality (p. 359–361)
- [[lake-plankton-analogy]] — depth = P*, plankton = φ, canyons = hidden volume (p. 359–360)
- [[importance-sampling-sphere-gaussian]] — weight spread exp(√(2N)); about 10^19 for N = 1000 (p. 363–364)
- [[rejection-gaussian-1000d]] — c = exp(10) ≃ 20,000 for σ_Q/σ_P = 1.01 (p. 365)
- [[metropolis-21-state-chain]] — random walk takes about 400 iterations per independent sample (p. 369, 372)
- [[hypercube-random-walk]] — periodic, non-ergodic chain with eigenvalues +1 and −1 (p. 373)
- [[syndrome-decoding-gibbs-failure]] — Gibbs sampling gets stuck on codeword-constrained posteriors (p. 371, 385)
- [[corrosion-pipelines-twelve-samples]] — twelve independent samples suffice (p. 380)

## Bridges (candidates)
- [same-math] Invariant distribution of an MCMC chain (eigenvalue 1 of T) ↔ linear algebra: Perron–Frobenius-style stationary vector of a column-stochastic matrix — the text states the eigenvector fact (p. 372).
- [structural-analogy] Weight spread exp(√N) in importance sampling ↔ information-theory: fluctuation of −ln P(x) around entropy (AEP), which the text invokes via typical sequences (p. 363–364, 384).
- [structural-analogy] Gibbs sampling for mixtures ↔ soft K-means: alternate sampling labels and updating parameters, as noted in Ex. 29.16 (p. 383).
- [structural-analogy] Sampling under a curve (rejection and slice sampling) ↔ geometry: x-marginal of a uniform distribution under P* is P (p. 364–365, 375).
- [metaphor] Random-walk (L/ε)² exploration ↔ diffusion: distance grows like √T (p. 367).

## Questions this raises
- How can random-walk behaviour be suppressed, so that time scales as L/ε rather than (L/ε)²? (The next chapter is cited, p. 370.)
- Since MCMC does not give Z, how can ratios of Z, or Bayesian model evidence, be estimated reliably (p. 379, Ex. 29.20)?
- How can one detect that a chain has not mixed (e.g. several separated modes) when empirical variances may mislead (p. 366, 379)?
- Is a genuinely Bayesian Monte Carlo method possible, whose answers depend only on computed P* values (Ex. 29.21, p. 384)?

## Exercises worth doing
- Ex. 29.3 (p. 367) — random walk RMS distance ≈ √T·ε, the root of the (L/ε)² rule — difficulty: easy
- Ex. 29.4 (p. 371) — Gibbs update as a Metropolis step with acceptance always 1 — difficulty: medium
- Ex. 29.7 (p. 374) — detailed balance implies invariance — difficulty: medium
- Ex. 29.10 (p. 377) — slice sampling on a peak-plus-tail density: transition times and correctness — difficulty: medium
- Ex. 29.14 (p. 382–383) — a modified proposal at the end states changes the stationary distribution; find the correct acceptance rule — difficulty: medium
- Ex. 29.18 (p. 383) — step size, traversal time and ln P changes in a 1000-D Gaussian — difficulty: medium

## Reading notes
- Printed page = pdf page − 12 (pdf 368 = p. 356). The unit includes the "About Chapter 29" page (p. 356) and the solutions to exercises 29.1, 29.2, 29.5, 29.12 and 29.13 (p. 384–386). They are summarised in L3, not listed as exercises.
- Figure 29.1's formula (29.10) reads $\exp[0.4(x-0.4)^2-0.08x^4]$ in the image.
- The prose on p. 375 says stepping out finds endpoints where P* is smaller than "u", while the algorithm uses u'. The algorithm and the figure 29.16 caption use u', so "u" in the prose is evidently a misprint for u'.
- p. 366 first says "Metropolis method" for the symmetric case, then adopts the name for the general asymmetric algorithm. Section 29.9 (p. 380) uses "rejection frequency of about 0.5" and the figure 29.11 caption (p. 367) "acceptance frequency will be about 0.5". These are consistent.
- Equations (29.44–29.45) use T(x', x) with a comma, while most other equations use a semicolon, T(x'; x).
- Several exercises (29.15–29.17) refer to earlier chapters (22, 24) not included here.
