---
id: innovation
type: concept
fields: [control-theory, bayesian, communication-theory]
fields_strong: [control-theory, bayesian, communication-theory]
n_sources: 3
n_works: 3
tiers: [core, deep]
grounding: digests
sources: [kalman-1960-filtering/main, rogers-2003-diffusion/ch01-elements-p1, sarkka-2023-bayesianfiltering/ch01-symbols]
generated_by: build_kg.py
---

# innovation

## Definitions in the sources

### control-theory

- [[kalman-1960-filtering/main]] (p. 40): the part $\tilde y(t|t-1)$ of the new measurement orthogonal to the past; the paper does not use this word [new]
- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (p. xxv): $\mathbf v_k$ with covariance $\mathbf S_k$ in a Kalman/Gaussian filter [new; work fields: control-theory, bayesian]

### communication-theory

- [[rogers-2003-diffusion/ch01-elements-p1]] (pdf 50): idea, practice or object perceived as new by the adopting unit [new]

## Instances that use it

- [[los-molinas-water-boiling]] — innovation failed by incompatibility, wrong early adopters and a change agent oriented to the innovation — from [[rogers-2003-diffusion/ch01-elements-p1]]
- [[son-preference-ultrasound]] — a diffusing innovation with disastrous social consequences — from [[rogers-2003-diffusion/ch03-contributions]]
- [[ryan-gross-hybrid-corn]] — founding study: profitable innovation, individual unit, no network data — from [[rogers-2003-diffusion/ch03-contributions]]
- [[rap-music-diffusion]] — a radical innovation that succeeded among white youths seeking rebellion — from [[rogers-2003-diffusion/ch06-attributes-p1]]
- [[vcr-price-decline]] — a falling price changed an innovation's relative advantage mid-diffusion — from [[rogers-2003-diffusion/ch06-attributes-p1]]
- [[seat-belts]] — preventive innovation with 73 percent adoption in 2002 — from [[rogers-2003-diffusion/ch06-attributes-p1]]
- [[old-order-amish]] — rejection of most consumer and many agricultural innovations, but adoption of values-consistent ones — from [[rogers-2003-diffusion/ch07-innovativeness]]
- [[meyer-goes-hospitals]] — 300 innovation-decisions as the unit; attributes explained more variance than organization — from [[rogers-2003-diffusion/ch10-innovation]]
- [[mcc-rd-consortium]] — a once-radical innovation becoming less radical and more routine — from [[rogers-2003-diffusion/ch10-innovation]]
- [[ddt-malaria-eradication]] — effective innovation with perverse consequences — from [[rogers-2003-diffusion/ch11-consequences-p2]]

## Candidate bridges

- [structural-analogy] "Nervous system in reverse" (the same lines carry unity or contagion) ↔ diffusion research: the same ties spread innovations and also unwanted influence. — from [[carey-1989-cultural/ch00-introduction]] (communication-theory → communication-theory)
- [metaphor] "Electrical sublime" ↔ diffusion research: pro-innovation bias — both are over-optimism about a technology's effects. — from [[carey-1989-cultural/ch05-mythos]] (communication-theory → communication-theory)
- [metaphor] White "innovation" after the first summer ↔ any residual-whiteness diagnostic in time-series model checking. — from [[kalman-1960-filtering/main]] (control-theory → unspecified)
- [metaphor] Entrepreneur finding selective incentives ↔ innovation in markets: a Schumpeterian actor organizing a new supply. — from [[olson-1965-collectiveaction/app-untitled]] (political-science → economics-finance)
- [structural-analogy] Elias' scheme (send the innovation, orthogonal to past outputs) ↔ estimation theory: recursive linear MMSE/innovations estimation. — from [[polyanskiy-2025-information/ch25-channel]] (information-theory → other:statistics)
- [structural-analogy] Pro-innovation bias via retrospective success selection ↔ statistics: survivorship/selection bias — failed cases leave no trace, as in the toy example. — from [[rogers-2003-diffusion/ch03-contributions]] (communication-theory → other:statistics)
- [metaphor] Skunkworks protecting innovation from bureaucracy ↔ organizational slack/niche protection — only a loose resemblance. — from [[rogers-2003-diffusion/ch04-generation]] (communication-theory → unspecified)
- [structural-analogy] EKF ↔ observer (state estimator): a model run in parallel, corrected by gain times innovation, with the gain from the covariance. — from [[sarkka-2023-bayesianfiltering/ch07-extended]] (control-theory → control-theory)
- [same-math] Kalman innovations $v_k,S_k$ in the energy (16.38) ↔ control-theory: Kalman filter innovation and its covariance — same quantities, here used to score θ. — from [[sarkka-2023-bayesianfiltering/ch16-parameter]] (control-theory → control-theory)
