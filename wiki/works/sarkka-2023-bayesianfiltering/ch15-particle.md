---
id: sarkka-2023-bayesianfiltering/ch15-particle
work: sarkka-2023-bayesianfiltering
unit: 15 Particle Smoothing
pages: 308-318
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Particle Smoothing

## L0 — One line
Particle smoothers approximate smoothing distributions by Monte Carlo; because the plain SIR smoother tends to be degenerate, other smoothers (backward simulation, reweighting) reuse the stored filter particles, and backward simulation is stated to be much less degenerate.

## L1 — The gist (≤ 120 words)
When Gaussian smoothers are too inaccurate, Monte Carlo (particle) smoothers can approximate smoothing distributions. Keeping the full state histories in SIR gives a smoother, but it degenerates when T is much larger than k. The chapter presents alternative smoothers developed because of this problem; backward simulation is stated to be much less degenerate. Backward simulation (FFBS) draws trajectories backward from stored filter particles. A rejection-sampling version aims to avoid quadratic cost in N. The reweighting (marginal) smoother gives new weights to the filter particles. Rao–Blackwellized variants handle conditionally Gaussian models. Pendulum examples show a clear gain over a Gaussian smoother (GHRTSS, without a clutter model) with cluttered measurements, but no real benefit in the plain model.

**Prerequisites:** Bayesian filtering and smoothing equations (RTS form), SIR/bootstrap particle filter, importance weights, rejection sampling, Rao–Blackwellized particle filter; RMSE (root mean square error); FFBS = forward-filtering backward-sampling.

## L2 — Key ideas (5–10 bullets)
- SIR with resampled full histories approximates the smoothing distribution, but degenerates when $T \gg k$ (p. 309).
- Backward simulation draws each $\tilde{\mathbf{x}}_k$ from the filter particles, reweighted by the transition density to the already drawn $\tilde{\mathbf{x}}_{k+1}$ (p. 310).
- Backward simulation costs $O(STN)$ and is much less degenerate than the SIR smoother (p. 311).
- In cluttered pendulum tracking, the particle smoother (RMSE 0.05) clearly beats a GHRTSS Gaussian smoother without a clutter model (0.83). In the plain pendulum the particles bring no real benefit (pp. 311–312).
- Rejection sampling can avoid the quadratic cost in $N$ (complexity close to $O(TN)$ when trajectories are sampled jointly), given a bound $C(\mathbf{x}_k)$ on the transition density. Low acceptance rates are a practical risk (pp. 312–314).
- The reweighting smoother gives the filter particles new weights, at cost $O(TN^2)$ (pp. 314–316).
- For conditionally Gaussian models, run RTS smoothers on stored RBPF histories. The smoothed $\mathbf{u}_k$ can still degenerate (pp. 316–317).
- Kim's approximation gives an approximate Rao–Blackwellized backward simulation, not a true Rao–Blackwellized representation (pp. 317–318).

## L3 — Walkthrough

**Chapter intro (p. 308).** Gaussian approximations may be too inaccurate for non-linear/non-Gaussian smoothing. SIR gives a smoothing approximation as a by-product, but it tends to be degenerate. Hence the FFBS and reweighting smoothers.

### 15.1 SIR particle smoother (pp. 308–309)
Idea (Kitagawa, 1996): in sequential importance sampling (SIS) keep the full histories $\mathbf{x}_{0:k}^{(i)}$. In SIR also resample the *histories*, so that resampling does not break them (p. 308).

**Algorithm 15.1.** Draw $\mathbf{x}_0^{(i)}\sim p(\mathbf{x}_0)$, set $w_0^{(i)}=1/N$ (p. 309). For $k=1,\dots,T$:
1. Draw $\mathbf{x}_k^{(i)}\sim\pi(\mathbf{x}_k\mid\mathbf{x}_{k-1}^{(i)},\mathbf{y}_{1:k})$, where $\mathbf{x}_{k-1}^{(i)}$ is the last element of the history (15.2).
2. Weights, then normalize (p. 309):
$$w_k^{(i)}\propto w_{k-1}^{(i)}\frac{p(\mathbf{y}_k\mid\mathbf{x}_k^{(i)})\,p(\mathbf{x}_k^{(i)}\mid\mathbf{x}_{k-1}^{(i)})}{\pi(\mathbf{x}_k^{(i)}\mid\mathbf{x}_{k-1}^{(i)},\mathbf{y}_{1:k})}\tag{15.3}$$
3. Append: $\mathbf{x}_{0:k}^{(i)}=(\mathbf{x}_{0:k-1}^{(i)},\mathbf{x}_k^{(i)})$ (15.4).
4. If the effective number of particles (11.31) is too low, resample the histories.

Outputs (p. 309):
$$p(\mathbf{x}_{0:T}\mid\mathbf{y}_{1:T})\approx\sum_i w_T^{(i)}\delta(\mathbf{x}_{0:T}-\mathbf{x}_{0:T}^{(i)})\tag{15.5}$$
$$p(\mathbf{x}_k\mid\mathbf{y}_{1:T})\approx\sum_i w_T^{(i)}\delta(\mathbf{x}_k-\mathbf{x}_k^{(i)}),\quad T>k\tag{15.6}$$
Here $\mathbf{x}_k^{(i)}$ is the $k$th component of $\mathbf{x}_{0:T}^{(i)}$. If $T\gg k$, this is known to be degenerate (p. 309).

*Intuition note (our gloss, not stated in the text):* the book only says that the direct SIR smoother is known to give degenerate approximations when $T\gg k$, that is, when an early state $\mathbf{x}_k$ is smoothed using many later measurements. A plausible reason is that resampling the stored histories repeatedly copies some histories, so the early parts of the histories may share few distinct ancestors.

### 15.2 Backward-simulation particle smoother (pp. 310–311)
Also called FFBS (BS-PS). It reuses the filtering particles $\{w_k^{(i)},\mathbf{x}_k^{(i)}\}$ and simulates trajectories backward (p. 310).

**Algorithm 15.2.** Choose $\tilde{\mathbf{x}}_T=\mathbf{x}_T^{(i)}$ with probability $w_T^{(i)}$. For $k=T-1,\dots,0$:
1. $w_{k|k+1}^{(i)}\propto w_k^{(i)}\,p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(i)})$ (15.7)
2. Choose $\tilde{\mathbf{x}}_k=\mathbf{x}_k^{(i)}$ with probability $w_{k|k+1}^{(i)}$.

**Derivation (p. 310).** Assume $\tilde{\mathbf{x}}_{k+1:T}$ is already simulated from the smoothing distribution. By (12.3),
$$p(\mathbf{x}_k\mid\tilde{\mathbf{x}}_{k+1},\mathbf{y}_{1:T})=\frac{p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k)\,p(\mathbf{x}_k\mid\mathbf{y}_{1:k})}{p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{y}_{1:k})}=Z\,p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k)\,p(\mathbf{x}_k\mid\mathbf{y}_{1:k})\tag{15.8}$$
with $Z$ a normalization constant. Inserting the SIR filter approximation (11.35):
$$p(\mathbf{x}_k\mid\tilde{\mathbf{x}}_{k+1},\mathbf{y}_{1:T})\approx Z\sum_i w_k^{(i)}p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k)\,\delta(\mathbf{x}_k-\mathbf{x}_k^{(i)})\tag{15.9}$$
Sampling $\mathbf{x}_k^{(i)}$ with probability $\propto w_k^{(i)}p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(i)})$ draws from this (p. 310).

With $S$ trajectories $\tilde{\mathbf{x}}_{0:T}^{(j)}$ (p. 310):
$$p(\mathbf{x}_{0:T}\mid\mathbf{y}_{1:T})\approx\frac1S\sum_j\delta(\mathbf{x}_{0:T}-\tilde{\mathbf{x}}_{0:T}^{(j)})\tag{15.10}$$
Marginals come from the $k$th components. Cost is $O(STN)$. The result is much less degenerate than the SIR smoother (p. 311).

*Intuition note:* Going backward, each filter particle is favoured if it could plausibly lead to the already chosen future state. This reuses the filtering results instead of simply storing full SIR histories (p. 310).

**Example 15.3 (pendulum, p. 311).** BS-PS with 100 samples on a bootstrap filter with 10,000 samples. RMSE 0.04, against ERTSS 0.06 and IERTSS 0.03, and similar to Gaussian smoothers. The bootstrap filter had RMSE 0.10 (Fig. 15.1). The authors conclude that particle approximations are not really beneficial in this model.

**Example 15.4 (cluttered pendulum, p. 312).** Same setup. Particle smoother RMSE 0.05, particle filter 0.20, GHRTSS without a clutter model 0.83. The particle smoother is a significant improvement here.

### 15.3 Backward simulation with rejection sampling (pp. 312–314)
Drawing $S=N$ trajectories costs $O(TN^2)$, because the weights $\propto w_k^{(i)}p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(i)})$ must be normalized. Rejection sampling can avoid this (Douc et al., 2011; Chopin and Papaspiliopoulos, 2020) (p. 312).

**Algorithm 15.5 (rejection sampling, p. 313).** Needs $p(\mathbf{x})\le M q(\mathbf{x})$. Repeat: draw $\mathbf{x}'\sim q$, $u\sim U(0,1)$. Accept $\mathbf{x}'$ if
$$u\le\frac{p(\mathbf{x}')}{M q(\mathbf{x}')}\tag{15.11}$$
Target over particle indices, with $Z_p=\sum_j w_k^{(j)}p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(j)})$:
$$p(i)=\frac{w_k^{(i)}p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(i)})}{\sum_j w_k^{(j)}p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(j)})}=\frac1{Z_p}w_k^{(i)}p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(i)})\tag{15.12}$$
Assume a function $C$ with
$$p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k)\le C(\mathbf{x}_k)\tag{15.13}$$
Proposal, with $Z_q=\sum_j w_k^{(j)}C(\mathbf{x}_k^{(j)})$:
$$q(i)=\frac{w_k^{(i)}C(\mathbf{x}_k^{(i)})}{\sum_j w_k^{(j)}C(\mathbf{x}_k^{(j)})}=\frac1{Z_q}w_k^{(i)}C(\mathbf{x}_k^{(i)})\tag{15.14}$$
Then
$$p(i)=\frac1{Z_p}w_k^{(i)}p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(i)})\le\frac1{Z_p}w_k^{(i)}C(\mathbf{x}_k^{(i)})=\frac{Z_q}{Z_p}q(i)\tag{15.15}$$
so $M=Z_q/Z_p$. The acceptance ratio simplifies to
$$\frac{p(i)}{(Z_q/Z_p)\,q(i)}=\frac{p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(i)})}{C(\mathbf{x}_k^{(i)})}\tag{15.16}$$
(added step: the weights $w_k^{(i)}$ and constants $Z_p$, $Z_q$ cancel in this ratio.)

**Algorithm 15.6 (p. 314).** Choose $\tilde{\mathbf{x}}_T$ by the weights $w_T^{(i)}$. For $k=T-1,\dots,0$: while not accepted, (a) draw index $i$ from $q(i)\propto w_k^{(i)}C(\mathbf{x}_k^{(i)})$; (b) draw $u\sim U(0,1)$ and accept if $u\le p(\tilde{\mathbf{x}}_{k+1}\mid\mathbf{x}_k^{(i)})/C(\mathbf{x}_k^{(i)})$. Then set $\tilde{\mathbf{x}}_k=\mathbf{x}_k^{(i)}$.

Complexity close to $O(TN)$ for $N$ trajectories requires sampling them jointly, not one by one (p. 314). Practical problem: acceptance probabilities for some particles can be very low, so run-time can be extremely long. Taghavi et al. (2013) propose a hybrid that falls back to BS-PS when rejection takes too long (p. 314).

### 15.4 Reweighting particle smoother (pp. 314–316)
Also called the marginal particle smoother (Hürzeler and Kunsch, 1998; Doucet et al., 2000). It gives new weights to the SIR filter particles (p. 314).

**Algorithm 15.7.** Set $w_{T|T}^{(i)}=w_T^{(i)}$. For $k=T-1,\dots,0$ (p. 315):
$$w_{k|T}^{(i)}=\sum_j w_{k+1|T}^{(j)}\frac{w_k^{(i)}p(\mathbf{x}_{k+1}^{(j)}\mid\mathbf{x}_k^{(i)})}{\left[\sum_l w_k^{(l)}p(\mathbf{x}_{k+1}^{(j)}\mid\mathbf{x}_k^{(l)})\right]}\tag{15.17}$$
$$p(\mathbf{x}_k\mid\mathbf{y}_{1:T})\approx\sum_i w_{k|T}^{(i)}\delta(\mathbf{x}_k-\mathbf{x}_k^{(i)})\tag{15.18}$$

**Derivation (pp. 315–316).** Assume
$$p(\mathbf{x}_{k+1}\mid\mathbf{y}_{1:T})\approx\sum_i w_{k+1|T}^{(i)}\delta(\mathbf{x}_{k+1}-\mathbf{x}_{k+1}^{(i)})\tag{15.19}$$
The integral in the second of Eqs. (12.2) becomes
$$\int\frac{p(\mathbf{x}_{k+1}\mid\mathbf{x}_k)\,p(\mathbf{x}_{k+1}\mid\mathbf{y}_{1:T})}{p(\mathbf{x}_{k+1}\mid\mathbf{y}_{1:k})}d\mathbf{x}_{k+1}\approx\sum_i w_{k+1|T}^{(i)}\frac{p(\mathbf{x}_{k+1}^{(i)}\mid\mathbf{x}_k)}{p(\mathbf{x}_{k+1}^{(i)}\mid\mathbf{y}_{1:k})}\tag{15.20}$$
The SIR filter approximation (11.35) gives the predicted density
$$p(\mathbf{x}_{k+1}\mid\mathbf{y}_{1:k})\approx\sum_j w_k^{(j)}p(\mathbf{x}_{k+1}\mid\mathbf{x}_k^{(j)})\tag{15.21}$$
so the integral is approximately
$$\sum_i w_{k+1|T}^{(i)}\frac{p(\mathbf{x}_{k+1}^{(i)}\mid\mathbf{x}_k)}{\left[\sum_j w_k^{(j)}p(\mathbf{x}_{k+1}^{(i)}\mid\mathbf{x}_k^{(j)})\right]}\tag{15.22}$$
Insert this and the filter approximation into the smoothing equation, using $p(\mathbf{x}_k\mid\mathbf{y}_{1:T})=p(\mathbf{x}_k\mid\mathbf{y}_{1:k})\int[\cdots]d\mathbf{x}_{k+1}$:
$$p(\mathbf{x}_k\mid\mathbf{y}_{1:T})\approx\sum_l w_k^{(l)}\delta(\mathbf{x}_k-\mathbf{x}_k^{(l)})\sum_i w_{k+1|T}^{(i)}\frac{p(\mathbf{x}_{k+1}^{(i)}\mid\mathbf{x}_k^{(l)})}{\left[\sum_j w_k^{(j)}p(\mathbf{x}_{k+1}^{(i)}\mid\mathbf{x}_k^{(j)})\right]}\tag{15.23}$$
Reading off the weight of $\mathbf{x}_k^{(l)}$:
$$w_{k|T}^{(l)}=\sum_i w_{k+1|T}^{(i)}\frac{w_k^{(l)}p(\mathbf{x}_{k+1}^{(i)}\mid\mathbf{x}_k^{(l)})}{\left[\sum_j w_k^{(j)}p(\mathbf{x}_{k+1}^{(i)}\mid\mathbf{x}_k^{(j)})\right]}\tag{15.24}$$
Complexity is $O(TN^2)$, the same as BS-PS with $S=N$ (p. 316).

*Intuition note:* Particle positions stay fixed and only the weights change. Each later particle $i$ passes its smoothed weight back to the earlier particles that could have produced it, in proportion to how well they explain it.

### 15.5 Rao–Blackwellized particle smoothers (pp. 316–318)
For the conditionally Gaussian models of Eq. (11.50) (p. 316). Simple approach: store histories in the RBPF, as in Algorithm 15.1. The stored means and covariances are conditional on the latent histories $\mathbf{u}_{0:T}$, but only on measurements up to $k$. So RTS smoothers must be applied to each history (p. 316).

**Algorithm 15.8 (p. 316–317).** (1) Compute the weighted RB histories $\{w_T^{(i)},\mathbf{u}_{0:T}^{(i)},\mathbf{m}_{0:T}^{(i)},\mathbf{P}_{0:T}^{(i)}\}$ (15.25). (2) Set $w_T^{s,(i)}=w_T^{(i)}$, $\mathbf{u}_{0:T}^{s,(i)}=\mathbf{u}_{0:T}^{(i)}$ (15.26). (3) Apply the RTS smoother to each $(\mathbf{m}_{0:T}^{(i)},\mathbf{P}_{0:T}^{(i)})$ to get $\mathbf{m}_{0:T}^{s,(i)},\mathbf{P}_{0:T}^{s,(i)}$.

Like the SIR smoother, the smoothed $\mathbf{u}_k$ can be quite degenerate if $T\gg k$. The smoothed $\mathbf{x}_k$ can still be relatively good, because Rao–Blackwellization avoids their degeneracy (p. 317).

Alternatives (p. 317):
- The backward-simulation RB smoother draws trajectories from the marginal posterior of $\mathbf{u}_k$. The Gaussian part then comes from Kalman filtering and RTS smoothing.
- Backward simulation from the joint $(\mathbf{x}_k,\mathbf{u}_k)$ does not give RB estimates, because the Gaussian part is sampled too.
- The reweighting smoother in RB form seems quite problematic to implement.
- Kim's approximation:
$$\int p(\mathbf{u}_k\mid\mathbf{u}_{k+1},\mathbf{x}_{k+1},\mathbf{y}_{1:k})\,p(\mathbf{x}_{k+1}\mid\mathbf{u}_{k+1},\mathbf{y}_{1:T})d\mathbf{x}_{k+1}\simeq p(\mathbf{u}_k\mid\mathbf{u}_{k+1},\mathbf{y}_{1:k})\tag{15.27}$$
Apply Algorithm 15.2 to the $\mathbf{u}_k$ samples alone, using $p(\mathbf{u}_{k+1}\mid\mathbf{u}_k)$ in place of $p(\mathbf{x}_{k+1}\mid\mathbf{x}_k)$. The Gaussian part may then be recovered with a Kalman filter and RTS smoother. This is only an approximation, not a true RB Monte Carlo representation (pp. 317–318).

## Toy example (ours)
One backward-simulation step (Algorithm 15.2), scalar state, $N=2$. Filter particles at step $k$: $x_k^{(1)}=0$, $x_k^{(2)}=1$, with $w_k^{(1)}=w_k^{(2)}=0.5$. Suppose $\tilde x_{k+1}=1$ was already drawn, and the model is $p(x_{k+1}\mid x_k)=\mathcal N(x_{k+1};x_k,1)$.
- Unnormalized transition values (the factor $1/\sqrt{2\pi}$ cancels): $e^{-(1-0)^2/2}=e^{-0.5}=0.6065$; $e^{-(1-1)^2/2}=1$.
- Products with the weights: $0.5\cdot0.6065=0.3033$; $0.5\cdot1=0.5$. Sum $=0.8033$.
- Normalize (15.7): $w_{k|k+1}^{(1)}=0.3033/0.8033=0.378$; $w_{k|k+1}^{(2)}=0.5/0.8033=0.622$.
So particle 2 is chosen as $\tilde x_k$ with probability 0.622, although the filter weights were equal. The future draw has shifted weight toward the particle that explains it better.

## Concepts
- [[particle-smoother]] (new) — Monte Carlo approximation of $p(\mathbf{x}_k\mid\mathbf{y}_{1:T})$ or $p(\mathbf{x}_{0:T}\mid\mathbf{y}_{1:T})$ by weighted samples (p. 308)
- [[sir-particle-smoother]] (new) — SIR with resampled full state histories, Algorithm 15.1; degenerate if $T\gg k$ (p. 308)
- [[particle-degeneracy]] (new) — the poor ('degenerate') approximation that the text says the direct SIR smoother produces when $T\gg k$; the text does not define it further (pp. 308–309)
- [[backward-simulation-smoother]] (new) — FFBS/BS-PS: sample backward from filter particles reweighted by transition density (p. 310)
- [[reweighting-particle-smoother]] (new) — marginal smoother: new weights on filter particles, $O(TN^2)$ (p. 314)
- [[rejection-sampling]] (new) — draw from $p$ using proposals $q$ with $p\le Mq$ (p. 313)
- [[rao-blackwellized-particle-smoother]] (new) — RBPF histories plus RTS smoothing of the Gaussian part (p. 316)
- [[kims-approximation]] (new) — Eq. (15.27); approximate backward simulation over $\mathbf{u}_k$ only (p. 317)
- [[state-estimation-smoothing]] (new) — estimating past states from data up to later time $T$ (p. 308)

## Canonical instances
- [[pendulum-tracking]] — BS-PS RMSE 0.04, about the same as Gaussian smoothers; no real benefit from particles (p. 311)
- [[cluttered-pendulum-tracking]] — BS-PS RMSE 0.05 versus GHRTSS 0.83 without a clutter model (p. 312)

## Bridges (candidates)
- [structural-analogy] Backward simulation ↔ control-theory: RTS backward pass, using the future state to correct filter estimates — same filter-then-backward-pass structure, but sampled rather than Gaussian.
- [same-math] Rejection sampling with bound $C(\mathbf{x}_k)$ ↔ general Monte Carlo: Algorithm 15.5 applied to a discrete index distribution.
- [structural-analogy] Reweighting smoother ↔ RTS smoother: both fold future information into the filter estimate, here as weights instead of Gaussian moments.

## Questions this raises
- How large must $N$ be before the quadratic cost of BS-PS and the reweighting smoother matters in practice?
- When is a bound $C(\mathbf{x}_k)$ on the transition density available and tight enough for good acceptance rates?
- Why is the reweighting smoother hard to Rao–Blackwellize, while backward simulation generalizes?
- How much does Kim's approximation distort the smoothing distribution of $\mathbf{u}_k$?

## Exercises worth doing
- Ex. 15.1 (p. 318) — implement BS-PS for the Exercise 7.1 model and compare it to Gaussian smoothers — difficulty: medium
- Ex. 15.2 (p. 318) — BS-PS with rejection sampling; compare to the other smoothers — difficulty: medium
- Ex. 15.3 (p. 318) — implement the reweighting smoother and compare — difficulty: medium
- Ex. 15.4 (p. 318) — show that $p(\mathbf{u}_k\mid\mathbf{u}_{k+1},\mathbf{y}_{1:T})\neq p(\mathbf{u}_k\mid\mathbf{u}_{k+1},\mathbf{y}_{1:k})$ in general (15.28) — difficulty: hard
- Ex. 15.6 (p. 318) — write Kim-approximation backward simulation for the clutter model, and find its peculiar property — difficulty: hard

## Reading notes
- Printed = pdf − 30. Source is the pre-publication version, with a copyright header on every page.
- The text layer is garbled for equations and symbols. Equations (15.1)–(15.26) were checked against the page images (pdf 339–346); (15.27) and (15.28) on pdf 347–348 were read from the text layer only. The text uses "degenerate" without defining it on these pages.
- Eq. (15.16) prints the denominator as $C(\mathbf{x}_k^{(i)})$. The text layer garbles the index placement, but the image reads as above.
- Page 311 says "(see next section)" for rejection sampling. The text does not state the "suitable conditions" beyond the existence of $C(\mathbf{x}_k)$ in Section 15.3.
- Exercise 15.5 is not listed above. Its model (Exercise 11.9) is not given in this unit.
