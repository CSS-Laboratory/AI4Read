---
id: markov-chain
type: concept
fields: [information-theory, bayesian, control-theory]
fields_strong: [information-theory, bayesian, control-theory]
n_sources: 4
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [ashby-1956-cybernetics/ch09-incessant, cover-2006-elements/ch02-entropy, cover-2006-elements/ch04-entropy, murphy-2023-pml2/ch02-probability-p3]
aliases: [markov-chain-xyz]
generated_by: build_kg.py
---

# markov-chain

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `markov-chain-xyz` — 1 digest(s)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch02-entropy]] (p. 32): $X\to Y\to Z$ iff $p(x,y,z)=p(x)p(y|x)p(z|y)$, iff $X\perp Z\mid Y$ [alias `markov-chain-xyz`; new]
- [[cover-2006-elements/ch04-entropy]] (p. 61): next symbol depends on the past only through the current symbol [new]

### bayesian

- [[murphy-2023-pml2/ch02-probability-p3]] (pp. 46–48): sequence with $p(x_t|x_{1:t-1})=p(x_t|x_{t-1})$; transition matrix $\mathbf A$, $n$-step matrix $\mathbf A^n$ [new]

### control-theory

- [[ashby-1956-cybernetics/ch09-incessant]] (pp. 166, 170): a sequence (or the system producing it) whose transition probabilities depend only on the present state and are constant [new; work fields: control-theory, information-theory]

## Instances that use it

- [[insect-in-pool]] — three-state Markov chain (B, W, P); equilibrium (44.9, 42.9, 12.2); entropy 0.842 bits per step — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[sequence-selection-experiment]] — random Markov chains, percentage recovery of greedy's loss — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]]
- [[two-state-markov-chain]] — rate $\frac{\beta}{\alpha+\beta}H(\alpha)+\frac{\alpha}{\alpha+\beta}H(\beta)$ — from [[cover-2006-elements/ch04-entropy]]
- [[correlated-urn-markov-chain]] — forward correlations $\epsilon,\delta$, solved exactly; shows failure of the binomial for long runs — from [[jaynes-2003-probability/ch03-elementary]]
- [[alternating-markov-chain]] — $0101\dots$ vs $1010\dots$: ergodic in the process sense — from [[polyanskiy-2025-information/ch14-entropy]]
- [[markov-chain-mixing-sdpi]] — $D_f(qP^n\|\pi)\le\eta_f(\pi,K)^nD_f(q\|\pi)$ — from [[polyanskiy-2025-information/ch36-strong-p1]]

## Candidate bridges

- [structural-analogy] Matrix of + and 0 with composition by row-into-column multiplication (Ex. 2/16/3) ↔ Markov-chain transition matrices: the same layout, but 0/+ entries rather than probabilities. — from [[ashby-1956-cybernetics/ch02-change]] (control-theory → linear-algebra)
- [same-math] Markovian machine with absorbing state; mean time to absorption ↔ Markov chains: absorbing-state expected hitting time (p. 230 average equals a geometric-series mean). — from [[ashby-1956-cybernetics/ch12-error]] (control-theory → other:probability)
- [structural-analogy] random surfer with restarts ↔ linear-algebra: Markov chain, steady-state eigenvector — the paper ties PageRank to a principal eigenvector but gives no derivation. — from [[brin-1998-anatomy/main]] (linear-algebra → linear-algebra)
- [same-math] Column-stochastic $A$, eigenvalue 1 ↔ Markov chains: stationary distribution — the paper mentions Markov chains and gives the surfer reading (p. 1, 3, 10) — from [[bryan-2006-eigenvector/main]] (linear-algebra → other:probability)
- [structural-analogy] Monotone fall of $D(\mu_n\|\mu)$ under a Markov transition ↔ convergence of Markov-chain simulation toward its stationary distribution: both are about a distribution approaching a fixed point. — from [[cover-2006-elements/ch02-entropy]] (information-theory → other:convergence-of-markov-chain)
- [structural-analogy] Kolmogorov sufficient statistic ↔ statistics: sufficient statistics, $\theta\to T(X)\to X$ — the text draws the parallel via a Markov chain. — from [[cover-2006-elements/ch07-kolmogorov]] (information-theory → other:statistics)
- [same-math] $I(X;W)-I(Y;W)$ under the Markov chain $W\to X\to Y$ ↔ information-theory: the Slepian–Wolf rate (the case $W=X$) — at D = 0 it equals H(X|Y). — from [[cover-2006-elements/ch14-network-p4]] (information-theory → information-theory)
- [same-math] Gibbs and Metropolis acceptance logic here ↔ Markov chain Monte Carlo (canon): the same algorithms, in code form. — from [[gelman-2013-bda3/appc-computation]] (bayesian → bayesian)
- [same-math] Two-state transition matrix, $V_k=\mathsf M^{k-1}V_1$ ↔ stochastic processes: two-state Markov chain with eigenvalues $1$ and $\epsilon+\delta$ — the same linear-algebra computation. — from [[jaynes-2003-probability/ch03-elementary]] (bayesian → other:probability)
- [same-math] Invariant distribution as principal right-eigenvector of $\mathbf{Q}$ ↔ bayesian: MCMC stationary distribution — the same linear-algebra fact about Markov chains. — from [[mackay-2003-information/ch51-appendices]] (information-theory → bayesian)
- [same-math] finite-state machine with coin-flip transitions ↔ probability: Markov chain with given transition probabilities (here, 1/2 per arrow) — from [[pierce-1980-introduction/ch03-mathematical]] (information-theory → other:probability)
- [structural-analogy] $I(X;Z|Y)$ as distance to Markov chains ↔ graphical models: information flow through a deleted edge (p. 69). — from [[polyanskiy-2025-information/ch05-variational]] (information-theory → bayesian)
- [structural-analogy] Mixing bound $D_f(qP^n\|\pi)\le\eta^nD_f(q\|\pi)$ ↔ Markov chain theory: spectral gap contraction of χ² — (33.18) with $\gamma_*^2$. — from [[polyanskiy-2025-information/ch36-strong-p1]] (information-theory → other:markov-chain-theory)
- [structural-analogy] $n$-freedom (insensitivity to the last $n$ elements) ↔ stochastic processes: Markov-chain order — both ask how many past elements matter for the next one. — from [[popper-1959-logic/ch08-probability-p1]] (analytic-philosophy → other:probability)
- [same-math] Metropolis–Hastings acceptance ↔ Markov-chain reversibility: acceptance probability makes $\pi$ invariant (detailed balance). — from [[robert-2011-mcmc/main]] (bayesian → other:markov-chain-reversibility)
- [same-math] Walk matrix $W_G=M_GD_G^{-1}$ ↔ probability/Markov chains: the author names "probability that a random walk is at that vertex"; each non-isolated vertex's column sums to 1. — from [[spielman-2025-sagt/ch01-introduction]] (linear-algebra → other:probability)
- [structural-analogy] Equitable-partition quotient ↔ lumping a Markov chain by symmetry. — from [[spielman-2025-sagt/ch05-fundamental]] (linear-algebra → unspecified)
- [structural-analogy] Escape probability $\le t\phi(S)/2$ ↔ Markov chains: bottleneck ratio slows mixing. — from [[spielman-2025-sagt/ch22-local]] (linear-algebra → other:probability)
- [same-math] Aᵏ = XΛᵏX⁻¹ with λ = 1, .5 ↔ Markov chains: powers converge to a steady-state eigenvector. — from [[strang-2023-introduction/ch06-eigenvalues-p2]] (linear-algebra → other:probability)
- [same-math] stationary distribution $\mu_\pi$ in (10.8) ↔ Markov chains: a fixed point of the transition operator. — from [[sutton-2018-rl/ch10-policy]] (control-theory → other:probability)
- [structural-analogy] Appendix A's $\text{Lib}_{(t+1)}=X\,\text{Lib}_{(t)}+P_{\to L}$ with an equilibrium independent of starting values ↔ Markov chains: steady state of fixed transition probabilities — similar convergence logic, not stated as a Markov chain in the text. — from [[zaller-1992-massopinion/ch09-two]] (political-science → other:probability)
