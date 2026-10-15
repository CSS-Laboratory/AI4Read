---
id: transfer-function
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 6
n_works: 1
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch12-frequency]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# transfer-function

## Canon spine entry

- **transfer function** (control-theory): input-to-output relation of a linear system in the frequency (Laplace) domain (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-7): $G(s)=b(s)/a(s)$, the factor multiplying $e^{st}$ in the particular solution
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-9): describes the frequency response of an input/output system; only mentioned
- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-23): here $G(s)=C(sI-A)^{-1}B+D$, appearing as the steady-state factor for input $e^{st}$
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-4, 9-8): coefficient of $e^{st}$ in the pure exponential response; $C(sI-A)^{-1}B+D$ for state space, $b(s)/a(s)$ for ODEs
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-24): input-to-output relation $G(s)=b(s)/a(s)$, equal to $C(sI-A)^{-1}B+D$ for state-space systems
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-3): used to relate every signal pair in Table 12.1

## Instances that use it

- [[vehicle-steering]] — observer-based controller as transfer functions; $G_{yr}$ independent of $l_1,l_2$ — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]]
- [[atomic-force-microscope]] — fitted high-order transfer function with delay — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]]
- [[bode-ideal-loop-transfer-function]] — $L=ks^{-n}$ gives phase margin independent of gain — from [[astrom-2021-feedbacksystems/ch13-robust]]

## Candidate bridges

- [same-math] Mechanical spring–wheel–friction system, RLC circuit and $a\ddot z + b\dot z + cz = w$ (pp. 95–96) ↔ control-theory: systems sharing one second-order transfer function — the same differential equation with matched parameters. — from [[ashby-1956-cybernetics/ch06-black]] (control-theory → control-theory)
- [structural-analogy] Reachable canonical form (polynomial coefficients as feedback paths) ↔ signal processing / transfer functions: direct-form realisation of a denominator polynomial — coefficients appear one-to-one in a chain of integrators. — from [[astrom-2021-feedbacksystems/ch07-state]] (control-theory → control-theory)
- [structural-analogy] Hidden cancelled mode ↔ observability/reachability: an unobservable or unreachable mode does not show in the transfer function. — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (control-theory → control-theory)
- [structural-analogy] $\delta_\nu$ via the Riemann sphere ↔ geometry: chordal distance on the sphere — a metric on transfer functions. — from [[astrom-2021-feedbacksystems/ch13-robust]] (control-theory → other:mathematics)
- [structural-analogy] Renewal equation transform $\hat u=\hat f/(1-\hat\varphi)$ ↔ control-theory: a closed-loop transfer function $1/(1-L)$ with a convolution kernel in the loop. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
