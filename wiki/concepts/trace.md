---
id: trace
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch08-operators, axler-2024-ladr/ch09-multilinear-p2, deisenroth-2020-mml/ch04-matrix-p1]
generated_by: build_kg.py
---

# trace

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch08-operators]] (pp. 326–328): sum of diagonal entries; basis-independent; equals the sum of eigenvalues with multiplicity over $\mathbf C$ [new]
- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 364): appears as minus the coefficient of $z^{n-1}$ in the characteristic polynomial [new]
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 103–104, 113): sum of diagonal entries; cyclic invariance; basis-independent for a linear map; equals the sum of eigenvalues [new]

## Instances that use it

- [[two-water-baths-a-b]] — Fig. 10/6/1: the better regulator's record shows no trace of D — from [[ashby-1956-cybernetics/ch10-regulation]]
- [[ex-trace-3x3-complex-eigenvalues]] — trace 5 equals $1+(2+3i)+(2-3i)$ — from [[axler-2024-ladr/ch08-operators]]
- [[trace-form-tr-st]] — $\rho(S,T)=\operatorname{tr}(ST)$ is a symmetric bilinear form on $\mathcal L(V)$ — from [[axler-2024-ladr/ch09-multilinear-p1]]
- [[trace-product-m-linear-form]] — $\operatorname{tr}(T_1\cdots T_m)$ is $m$-linear but is not claimed alternating — from [[axler-2024-ladr/ch09-multilinear-p1]]
- [[cramer-discontinuity-anomaly]] — estimators of "abnormally high" precision which Jaynes traces to ignoring the delta term in $\partial\log f/\partial\theta$ — from [[jaynes-2003-probability/appb-mathematical]]
- [[univariate-gaussian-two-points-diffuse-prior]] — diffuse prior gives traces that barely overlap and many HMC divergences; a sensible prior fixes it — from [[murphy-2023-pml2/ch12-markov-p2]]
- [[neural-ode-ffjord]] — continuous-time flows with adjoint method; Hutchinson trace — from [[murphy-2023-pml2/ch23-normalizing]]
- [[imdb-controlled-sentiment]] — a controlled setting with a known reward classifier, used to trace the reward–KL frontier — from [[rafailov-2023-dpo/main]]
- [[sum-of-leverage-scores-is-n-minus-1]] — trace proof $\mathrm{Tr}(\Pi)=n-1$ — from [[spielman-2025-sagt/ch32-sparsification]]
- [[gridworld-trace-credit]] — Example 12.1: one-step, n-step and trace updates after reaching a goal — from [[sutton-2018-rl/ch12-eligibility]]
- [[linear-mc-lms]] — Section 12.6: LMS/MC rewritten with a dutch trace — from [[sutton-2018-rl/ch12-eligibility]]

## Candidate bridges

- [same-math] trace $=$ sum of eigenvalues with multiplicity (8.52) ↔ linear-algebra: total variance in PCA equals the sum of covariance eigenvalues (covariance is symmetric, so it is a special case). — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [same-math] Over $\mathbf C$, $\det T$ is the product of eigenvalues ↔ characteristic polynomial and the trace as sum of eigenvalues, since the coefficients are $\operatorname{tr}T$ and $\det T$. — from [[axler-2024-ladr/ch09-multilinear-p2]] (linear-algebra → unspecified)
- [metaphor] Trace and determinant as "sum and product of stretches" ↔ geometry: perimeter and area of the image of a unit square (valid only for the orthonormal-eigenvector picture on p. 113). — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → other:mathematics)
- [structural-analogy] vertical flow of opinion via opinion leaders (p. 213) ↔ communication-theory: two-step flow. Habermas cites Katz and Lazarsfeld as a trace of the liberal public sphere, then notes that the opinion leaders are the least inclined to submit their views seriously to discussion. — from [[habermas-1989-publicsphere/ch06-transformation-p2]] (communication-theory → communication-theory)
- [metaphor] CA boundaries as "particles" ↔ physics: bubble-chamber traces of elementary particles — a visual and naming analogy (p. 19) — from [[mitchell-2009-guidedtour/ch11-computing]] (complex-systems → other:physics)
- [structural-analogy] Pro-innovation bias via retrospective success selection ↔ statistics: survivorship/selection bias — failed cases leave no trace, as in the toy example. — from [[rogers-2003-diffusion/ch03-contributions]] (communication-theory → other:statistics)
- [same-math] $x^TLx=\sum_j\lambda_j(\psi_j^Tx)^2$ minimized over orthonormal frames ↔ linear-algebra: Rayleigh quotient / Courant–Fischer — Theorem 3.2.1 is the multi-vector (trace) version. — from [[spielman-2025-sagt/ch03-laplacian]] (linear-algebra → linear-algebra)
- [structural-analogy] Trace method: $\mathrm{Tr}\,R^l$ as a sum over closed walks ↔ adjacency matrix: $(A^k)_{ij}$ counts walks of length $k$ — same expansion, but weighted by random entries here. — from [[spielman-2025-sagt/ch08-eigenvalues]] (linear-algebra → linear-algebra)
- [structural-analogy] choosing $v_i$ by trace averaging ↔ probabilistic method: if the average satisfies the inequality, some element does. — from [[spielman-2025-sagt/ch33-linear]] (linear-algebra → other:mathematics)
- [structural-analogy] eligibility trace ↔ control-theory: fading-memory (exponentially weighted) filter of past inputs — both keep a decaying sum of past signals, with decay set by one parameter. — from [[sutton-2018-rl/ch12-eligibility]] (control-theory → control-theory)
- [same-math] dutch-trace derivation with forgetting matrices $\mathbf F_t=\mathbf I-\alpha\mathbf x_t\mathbf x_t^\top$ ↔ LMS adaptive filtering: the LMS update itself (stated in the text as the same rule), unrolled as a matrix product. — from [[sutton-2018-rl/ch12-eligibility]] (control-theory → other:lms-adaptive-filtering)
- [same-math] eligibility trace $z_t=\gamma\lambda z_{t-1}+g_t$ ↔ signal processing: a first-order exponentially decaying (low-pass) sum of past inputs. — from [[sutton-2018-rl/ch15-neuroscience-p2]] (control-theory → other:signal-processing)
- [same-math] Trace minimization $\min\mathrm{Tr}(H'LH)$ s.t. $H'H=I$ ↔ linear-algebra spine: Rayleigh quotient / Courant–Fischer extreme eigenvalues — same optimization, bottom-$k$ eigenvectors. — from [[vonluxburg-2007-spectralclustering/main]] (linear-algebra → linear-algebra)
