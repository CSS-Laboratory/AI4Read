---
id: feedforward
type: concept
fields: [control-theory]
n_sources: 9
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch11-pid, astrom-2021-feedbacksystems/ch12-frequency, astrom-2021-feedbacksystems/ch15-architecture-p1]
canon_spine: control-theory
generated_by: build_kg.py
---

# feedforward

## Canon spine entry

- **feedforward** (control-theory): acting on a measured disturbance before it affects the output (UG)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch12-error]] (p. 238): control from D before E changes, e.g. shivering on seeing cold things. Ashby calls it "control from D"
- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-4): measure a disturbance (or the reference) and act before it affects the output; needs a good model
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-6): using a model to precompute inputs that make the system respond in a certain way
- [[astrom-2021-feedbacksystems/ch07-state]] (pp. 7-10, 7-14): the term $k_fr$ from reference to input; fixes steady state but needs exact calibration
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-23): here $u_{ff}$ from a trajectory generator
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-18, 9-20): $F$ in Figure 9.6 and $G_{ur}$
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-4): term $u_{ff}=k_fr$ that gives the desired steady state but needs exact $P(0)$
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-18): blocks $F_r$, $F_v$ act on reference and measured disturbance, ideally by inverse models
- [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (p. 15-12): here, the trajectory generator's command $u_d$ in a two-degree-of-freedom design

## Instances that use it

- [[server-farm-control]] — feedforward logic plus PID for temperature — from [[astrom-2021-feedbacksystems/ch01-introduction]]
- [[vehicle-steering]] — feedforward lane change with $F_r=F_m/P$ — from [[astrom-2021-feedbacksystems/ch12-frequency]]
- [[rhp-zero-inverse-response]] — right half-plane zero causes initial undershoot in feedforward response — from [[astrom-2021-feedbacksystems/ch12-frequency]]

## Candidate bridges

- [structural-analogy] thermostat as stored design against repeating disturbances ↔ feedforward: fixed design used against recurrent disturbance. — from [[ashby-1956-cybernetics/ch14-amplifying]] (control-theory → other)
- [structural-analogy] Feedback vs feedforward ↔ economics: market-based vs planned economy — the text itself draws the analogy (p. 1-4). — from [[astrom-2021-feedbacksystems/ch01-introduction]] (control-theory → economics-finance)
- [structural-analogy] Feedforward + feedback split (two degrees of freedom) ↔ motor control: Ito's hypothesis that human motion control combines feedforward and feedback (p. 8-32). — from [[astrom-2021-feedbacksystems/ch08-output]] (control-theory → control-theory)
- [structural-analogy] Feedforward $F_r=F_m/P$ as model inversion ↔ model-based control in neuroscience: an internal inverse model produces the command. — from [[astrom-2021-feedbacksystems/ch12-frequency]] (control-theory → control-theory)
- [structural-analogy] GLM composition $\sigma_k(A_kx_k+b_k)$ ↔ layers of a feedforward neural network. — from [[deisenroth-2020-mml/ch09-linear]] (linear-algebra → unspecified)
- [metaphor] Foresight under long delays ↔ control-theory: feedforward or predictive control — acting before the problem is obvious. — from [[meadows-2008-thinking/ch04-systems]] (control-theory → control-theory)
