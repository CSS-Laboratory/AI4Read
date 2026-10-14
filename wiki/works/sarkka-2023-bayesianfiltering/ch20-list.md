---
id: sarkka-2023-bayesianfiltering/ch20-list
work: sarkka-2023-bayesianfiltering
unit: "List of Examples (back matter)"
pages: 393–396
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# List of Examples

## L0 — One line
This is an index of 73 numbered worked examples across chapters 4–16, giving each title and its page in the book.

## L1 — The gist (≤ 120 words)
The unit has no argument or equations. It is a lookup table: example number, title, page. The numbers show which chapters hold examples (4–16). The titles show that a few test problems return again and again. These are a noisy pendulum, a coordinated turn (CT) model, a car, a Gaussian random walk and a Gilbert–Elliot channel. Each is treated with different filtering or smoothing methods. Use it to find the same problem under different methods. The list spells out only a few abbreviations (CT, AR, TVAR). The meaning of the other method names (EKF, GHKF, BS-PS and so on) must come from the chapters.

**Prerequisites:** none; later chapters are needed to understand the method names.

## L2 — Key ideas (5–10 bullets)
- The list covers examples numbered 4.x to 16.x, 73 entries in all (pp. 393–396).
- Chapters 4–5 hold the most model-building examples: 14 each (p. 393).
- Chapters 6 and 12 have random-walk and car-tracking examples: filters in chapter 6, smoothers in chapter 12 (pp. 393–394).
- The pendulum and CT examples recur in chapters 7, 8, 10, 13, 14 (and the pendulum also in 11, 15, 16). Chapters 7, 8, 10, 13 and 14 use both problems (pp. 394–395).
- Cluttered pendulum tracking appears in chapters 11 and 15 (pp. 394–395).
- Chapter 16 has two examples: a parameter posterior and noise-variance estimation (p. 395).
- Page 396 has no entries (p. 396).

## L3 — Walkthrough
Each item gives example number, title and book page. "(p. 393)" etc. is the list page.

**Chapters 4–5: models** (p. 393).
- Ch. 4 (14 entries): car, constant-velocity and Wiener-process models, pendulum, polar and Cartesian CT models, bicycle model. Also discretizations, analytical means and noise approximations (4.1–4.22; book pp. 47–68).
- Ch. 5 (14 entries): measurement models (position, pendulum, radar, range, robust, clutter, gyroscope). Also regression and generalized linear models, bias in the state, AR and TVAR models, and the Gilbert–Elliot channel (5.1–5.14; pp. 74–87).

**Chapters 6–7** (pp. 393–394).
- Ch. 6: Gaussian random walk (6.4), Kalman filter for it (6.7), for car tracking (6.8), and a Gilbert–Elliot filter (6.12).
- Ch. 7: pendulum and CT examples with EKF (7.6, 7.7) and IEKF (7.10, 7.11).

**Chapters 8–11** (p. 394).
- Ch. 8: pendulum and CT with GHKF, CKF, UKF and UKF5 (8.8–8.24).
- Ch. 9: statistical linearization, statistical linear regression, SLR with Poisson observations, and Gaussian filtering with Poisson observations (9.7, 9.15, 9.19, 9.26).
- Ch. 10: posterior statistical linear regression, iterated posterior linearization, and pendulum and CT with posterior-linearization filters (10.5, 10.7, 10.13, 10.14).
- Ch. 11: pendulum and cluttered pendulum with a particle filter (11.10, 11.11).

**Chapters 12–14: smoothers** (pp. 394–395).
- Ch. 12: RTS smoother for the random walk and for car tracking, Gilbert–Elliot smoother, and a Viterbi algorithm (12.3, 12.4, 12.8, 12.11).
- Ch. 13: pendulum and CT with ERTSS and IERTSS (13.2, 13.3, 13.6, 13.7).
- Ch. 14: pendulum with GHRTSS, CRTSS, URTSS, URTSS5 and IPLS. CT with "Gaussian smoothers" (14.14, 14.24). These two titles are identical in the list.

**Chapters 15–16** (p. 395).
- Ch. 15: pendulum and cluttered pendulum with BS-PS (15.3, 15.4).
- Ch. 16: parameter posterior for the random walk (16.10) and noise-variance estimation in the pendulum model (16.17).

**Intuition note:** The titles suggest that a few test problems are reused under many methods. This would let a reader compare methods on the same problem (our reading; the list does not state the authors' intent).

## Toy example (ours)
Find "7.6 Pendulum tracking with EKF … 117". The prefix 7 gives chapter 7. The list says the example is on book page 117 (p. 394). The same pendulum problem with another filter is 8.8 (GHKF, p. 141), 8.13 (CKF, p. 149) or 10.13 (IPLF, p. 220). Subtracting page numbers is not meaningful here.

## Concepts
- [[kalman-filter]] — named only in 6.7, 6.8 (Kalman filter for random walk and car); no definition here (p. 393–394)
- [[rts-smoother]] (new) — named in 12.3, 12.4; no definition here (p. 394)
- [[particle-filter]] (new) — named in 11.10, 11.11; no definition here (p. 394)

## Canonical instances
- [[gaussian-random-walk]] — filtering (6.7), smoothing (12.3), parameter posterior (16.10) (pp. 393–395)
- [[noisy-pendulum]] — most reused test problem (pp. 393–395)
- [[coordinated-turn-model]] — second recurring test problem (pp. 393–395)
- [[car-tracking]] — model, filter, smoother (pp. 393–394)
- [[gilbert-elliot-channel]] — model, filter, smoother, Viterbi (pp. 393–394)

## Bridges (candidates)
- [structural-analogy] Same test problem under many estimators ↔ control-theory: one plant tested with several observers.

## Questions this raises
- Which methods give the best accuracy on the pendulum and CT problems?
- Why does chapter 9 include Poisson-observation examples (9.19, 9.26)?
- What do the abbreviations (ERTSS, GHRTSS, BS-PS, …) stand for?

## Reading notes
- Printed = pdf − 30. Page 396 has only the copyright header.
- Page numbers beside each title are book pages of the examples, not this list's pages.
- No equations. Example numbers skip (e.g. 4.3), so numbering is probably shared with other items; the list does not say.
