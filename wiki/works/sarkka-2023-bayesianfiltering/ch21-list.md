---
id: sarkka-2023-bayesianfiltering/ch21-list
work: sarkka-2023-bayesianfiltering
unit: "List of Theorems, Corollaries, and Algorithms"
pages: 397–400
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# List of Theorems, Corollaries, and Algorithms

## L0 — One line
This unit is a page-numbered index of the book's numbered theorems, corollaries and algorithms, from Chapter 4 to Appendix A, and, judging from the titles, it can serve as a partial map of the book's methods.

## L1 — The gist (≤ 120 words)
This unit makes no argument. It lists numbered results with their printed page numbers. Judging from the item titles, the entries move from discretizing dynamic models (Ch. 4), to Bayesian and Kalman filtering (Ch. 6), to non-linear Gaussian filters (Ch. 7–10), to particle filters (Ch. 11), to smoothers (Ch. 12–15), and to parameter estimation (Ch. 16), with matrix and derivative results in Appendix A. Use it to find where a named method is stated, and to see which methods are variants of each other (for example "Extended Kalman filter I" and "II"). The chapter topics here are my reading of the titles, not statements by the authors.

**Prerequisites:** none for the list itself. To use the entries you need the idea of recursive state estimation (predict, then update).

## L2 — Key ideas (5–10 bullets)
- The list covers Chapters 4, 6–16 and Appendix A; no entries carry chapter numbers 1–3, 5 or 17 and above (p. 397–400).
- The Kalman filter (p. 97) and the "Bayesian filtering equations" (p. 94) are the earliest filtering entries (p. 397).
- Chapters 7–10 contain many "I/II/III/IV" variants of non-linear filters: Taylor-based, Gauss–Hermite, cubature, unscented, statistical-linearization and iterated-posterior-linearization (p. 397–398).
- Chapter 11 collects the sampling-based methods: importance sampling, several resampling schemes, the bootstrap filter, the auxiliary and Rao–Blackwellized particle filters (p. 398–399).
- Smoothers form a second family. Judging from the titles, many filters from Ch. 6–10 have a matching RTS smoother in Ch. 12–14 (p. 399).
- Particle smoothers (Ch. 15) and parameter-estimation methods such as Metropolis–Hastings and EM (Ch. 16) come last before the appendix (p. 399–400).
- Appendix A lists matrix and derivative results: block inverses, inversion lemmas, Cholesky factorization and energy-function derivatives (p. 400).

## L3 — Walkthrough
The list is grouped by chapter. Item numbers are chapter.item, and they skip values (for example 4.3, 4.8, 4.12). Each entry gives a title and a printed page. The page offset is printed = pdf − 30.

**Ch. 4, discretization and SDEs (8 entries, my count).** Discretization of linear dynamic models (4.3, p. 49), Euler–Maruyama method (4.8, p. 53), simulating an SDE solution (4.12, p. 58), and several linearization-based discretizations (4.13–4.20, p. 59–67) (p. 397).

**Ch. 6, filtering basics (5 entries).** Bayesian filtering equations (6.5, p. 94), Kalman filter (6.6, p. 97), affine Kalman filter (6.9, p. 102), and filtering equations for discrete state spaces and discrete HMMs (6.10, 6.11, p. 103–104) (p. 397).

**Ch. 7, Taylor-series filters (7 entries).** Linear and quadratic approximations of transforms (7.1–7.3, p. 110–112), Extended Kalman filter I and II (7.4 p. 113, 7.5 p. 115), second order EKF (7.8, p. 119), iterated EKF (7.9, p. 124) (p. 397).

**Ch. 8, Gaussian filters (16 entries).** Gaussian moment matching (8.1, 8.2), Gaussian filters I and II (8.3, 8.4), Gauss–Hermite quadrature, cubature and Kalman filter (8.5–8.7), spherical cubature and cubature Kalman filters (8.10–8.12) (p. 397). Unscented transforms and filters (8.15–8.18) and fifth order cubature/unscented integration and filter (8.21, 8.22) follow (p. 398).

**Ch. 9, statistical linearization and regression (21 entries).** Gaussian filtering with enabling linearizations (9.1, p. 169), statistical linearization I–III and the statistically linearized filters (9.3–9.10), statistical linear regression (SLR) and conditional-moment forms (9.12–9.18), SLR filters I–IV, a sigma-point conditional moment Kalman filter, a Monte Carlo Kalman filter and a sigma-point non-additive conditional moment filter (9.20–9.27, p. 187–198) (p. 398).

**Ch. 10, iterated posterior linearization (11 entries).** Generalized SLR (10.2, 10.3), iterated posterior linearization (10.6), filters I–IV (10.8–10.11), sigma-point versions (10.12, 10.15, 10.16) and a Monte Carlo version (10.17, p. 224) (p. 398).

**Ch. 11, particle filtering (11 entries).** Importance sampling (11.1, p. 233) and sequential importance sampling (11.2, p. 235) (p. 398). Then resampling and its variants: inverse transform, multinomial, stratified, systematic (11.3–11.7, p. 237–239). Then sequential importance resampling (11.8), bootstrap filter (11.9, p. 242), auxiliary particle filter (11.12, p. 246) and Rao–Blackwellized particle filter (11.13, p. 248) (p. 399).

**Ch. 12, smoothing basics (7 entries).** Bayesian smoothing equations (12.1, p. 253), RTS smoother (12.2, p. 255), affine RTS smoother (12.5), discrete smoothing equations and HMM smoother (12.6, 12.7), Viterbi algorithm for the MAP path and for discrete HMMs (12.9, 12.10, p. 263–265) (p. 399).

**Ch. 13, extended smoothers (3 entries).** Extended RTS smoother (13.1, p. 267), second order (13.4), iterated (13.5) (p. 399).

**Ch. 14, non-linear smoothers (17 entries).** Gaussian RTS smoothers I–III, Gauss–Hermite, cubature, unscented and fifth order smoothers (14.1–14.12), statistical linear regression smoother, Monte Carlo RTS smoother, generalized SLR smoother, and iterated posterior linearization smoothers (14.15–14.22, p. 292–302) (p. 399).

**Ch. 15, particle smoothing (6 entries).** SIR particle smoother (15.1, p. 308), backward-simulation smoother (15.2), rejection sampling (15.5), backward simulation with rejection sampling (15.6), reweighting smoother (15.7), Rao–Blackwellized SIR smoother (15.8, p. 316) (p. 399–400).

**Ch. 16, parameter estimation (15 entries).** Recursions for the marginal likelihood and the energy function (16.1, 16.4), Metropolis–Hastings (16.5), RAM algorithm (16.6), abstract EM and EM (16.7, 16.8), linear Gaussian energy function, evaluation and maximization of Q, and EM for linear state space models (16.9–16.13), Gaussian-filtering-based energy function and Q via Gaussian smoothing (16.14, 16.15), SIR-based energy approximation and Q via particle smoothers (16.16–16.19, p. 341–344) (p. 400).

**Appendix A (8 entries).** Block matrix inverses (A.4, p. 356), matrix inversion lemmas (A.5), Cholesky factorization and its partial derivatives (A.6–A.8, p. 357–358), energy-function derivatives for the linear Gaussian model and for Gaussian filtering (A.10–A.12, p. 372–375) (p. 400).

*Intuition note:* Judging from the titles only, the list suggests a plan: linear-model results come first, and many variants for non-linear models follow. Filters then seem to have smoother counterparts, and filters and smoothers both appear in the parameter-estimation entries.

## Toy example (ours)
Task: locate the exact Kalman filter and its extended and smoothing relatives.
1. Kalman filter: entry 6.6, p. 97 (p. 397).
2. Extended Kalman filter I: entry 7.4, p. 113 (p. 397).
3. RTS smoother: entry 12.2, p. 255. Extended RTS smoother: 13.1, p. 267 (p. 399).
4. Page gap between filter and smoother: 255 − 97 = 158 pages.
5. Chapter numbers pair up: 7 (extended filter) ↔ 13 (extended smoother). By the titles, filter chapter 8 matches smoother chapter 14.

## Concepts
- [[kalman-filter]] — named entries 6.6, 6.9 and many "Kalman filter" variants (p. 397)
- [[linearization]] — by their titles, the Ch. 7 and 9–10 entries concern linear approximations of non-linear transforms (p. 397–398)
- [[bayesian-filtering]] (new) — entry "Bayesian filtering equations" (p. 397)
- [[bayesian-smoothing]] (new) — "Bayesian smoothing equations" and RTS smoother entries (p. 399)
- [[particle-filter]] (new) — Ch. 11 entries (p. 398–399)
- [[sigma-point-methods]] (new) — unscented, cubature and Gauss–Hermite entries (p. 397–398)
- [[state-space-model]] — "linear state space models" appear in 16.13 (p. 400)

## Canonical instances
- [[kalman-filter-6.6]] — Kalman filter, entry 6.6 (p. 397)
- [[extended-kalman-filter]] — entries 7.4, 7.5 (p. 397)
- [[rts-smoother]] — entry 12.2 (p. 399)
- [[bootstrap-filter]] — entry 11.9 (p. 399)
- [[viterbi-algorithm]] — entries 12.9, 12.10 (p. 399)

## Bridges (candidates)
- [structural-analogy] Kalman filter (6.6) ↔ control theory: observer / state estimator — both correct a model prediction with measurements.
- [structural-analogy] Viterbi algorithm (12.9) ↔ control theory: principle of optimality — both build a best path recursively.
- [metaphor] Smoother entries (Ch. 12–14) ↔ filtering plus hindsight: using later data to revise earlier estimates.

## Questions this raises
- Which of the many "I/II/III" variants are special cases of others?
- Why do several filters (Ch. 7–10) have smoother counterparts (Ch. 13–14), and what does a smoother add?
- What do the gaps in item numbering stand for?
- How do the EM and energy-function entries (Ch. 16) reuse the filters and smoothers?

## Reading notes
- Page offset: printed = pdf − 30 (pdf 427 = printed 397).
- Every page carries a pre-publication notice: Cambridge University Press, second edition, © Särkkä and Svensson 2023, not for re-distribution.
- The text layer matches the layout; no OCR problems were noticed.
- The unit has no equations. Entry counts per chapter are my own tallies (135 in total). Chapter topics are inferred from titles only.
- Item numbers skip values (for example 4.3 → 4.8). The pages do not say why.
- No entry is numbered with chapters 1–3, 5 or 17 and above. These pages do not show what those chapters contain.
- A bare "p. N" next to an item number is the book page where that item is stated; the closing (p. 397–400) tag is the page of this list.
