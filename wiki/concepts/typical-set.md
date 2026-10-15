---
id: typical-set
type: concept
fields: [bayesian, information-theory]
n_sources: 11
tiers: [core, deep, reference]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, betancourt-2017-hmc/main-p2, betancourt-2017-hmc/main-p3, gelman-2020-workflow/main-p1, mackay-2003-information/ch22-maximum, mackay-2003-information/ch29-monte, mackay-2003-information/ch30-efficient, mackay-2003-information/ch41-learning, mackay-2003-information/ch51-appendices, murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch05-information-p1]
canon_spine: bayesian
generated_by: build_kg.py
---

# typical-set

## Canon spine entry

- **Typical set** (bayesian): the thin region of high-dimensional space where most probability mass actually lives, away from the mode (grad)

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p1]] (p. 7): region between mode and tails, where density × volume is significant; invariant under reparameterization
- [[betancourt-2017-hmc/main-p2]] (p. 23): region where target mass concentrates; trajectories must stay in it
- [[betancourt-2017-hmc/main-p3]] (p. 44): where mass concentrates; heavy tails push it into extremes
- [[gelman-2020-workflow/main-p1]] (p. 13): region of parameter space where log posterior density is near its expected value, which the paper relates to the typical set; warmup moves the chain toward it
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 23): here, the thin shell of radius about $\sigma\sqrt D$ holding most Gaussian mass
- [[murphy-2023-pml2/ch05-information-p1]] (p. 236): length-$N$ sequences whose per-sample negative log-probability is within $\epsilon$ of the entropy

### information-theory

- [[mackay-2003-information/ch22-maximum]] (p. 306): in high dimensions most mass lies in a set unlike the max-density points
- [[mackay-2003-information/ch29-monte]] (p. 360): region holding most probability, size about 2^H; uniform sampling needs about 2^(N−H) draws to hit it
- [[mackay-2003-information/ch30-efficient]] (pp. 389–390): states typical of the target; Fig. 30.2b shows a start far from it converging to it
- [[mackay-2003-information/ch41-learning]] (p. 500): here: the typical set of $\mathbf w$ has different properties from the most probable state $\mathbf w_{\rm MP}$
- [[mackay-2003-information/ch51-appendices]] (p. 604): typicality, as used here, fails near a critical point; information content and energy fluctuations are linked

## Instances that use it

- [[grid-quadrature-curse]] — $N^D$ evaluations; grid misses the typical set — from [[betancourt-2017-hmc/main-p1]]
- [[satellite-orbit-analogy]] — planet = mode, gravity = gradient, orbit = typical set — from [[betancourt-2017-hmc/main-p1]]
- [[typical-set-flag-bit-code]] — two-part code with flag bit 0/1 — from [[cover-2006-elements/ch03-asymptotic]]
- [[ber-p-typical-set]] — typical sequences have Hamming weight fraction near $p$ — from [[polyanskiy-2025-information/ch13-fixed]]

## Candidate bridges

- [structural-analogy] Typical set ↔ statistical mechanics/information theory: mass concentrates away from the peak in a thin shell — the pattern looks the same, but this unit does not state the link. — from [[betancourt-2017-hmc/main-p1]] (bayesian → complex-systems)
- [metaphor] Gradient crashing into the mode ↔ optimization: gradient ascent/MAP finds the mode, which the typical set avoids. — from [[betancourt-2017-hmc/main-p1]] (bayesian → other)
- [structural-analogy] typical set ↔ statistical mechanics: a small set of near-equiprobable microstates carries almost all probability — from [[cover-2006-elements/ch03-asymptotic]] (information-theory → complex-systems)
- [metaphor] Most-probable macrostate = most microstates ↔ typical-set counting (AEP). — from [[cover-2006-elements/ch11-maximum]] (information-theory → unspecified)
- [structural-analogy] Gaussian as maximum-entropy attractor under variance-conserving operations ↔ information theory: maximum entropy principle and the typical set — repeated information-losing steps approach a maximum-entropy law. — from [[jaynes-2003-probability/ch07-central-p2]] (information-theory → information-theory)
- [same-math] Multiplicity $M\sim e^{nH}$ ↔ information-theory: number of sequences of a given type is $\approx 2^{nH}$ (method of types / typical set) — same counting by Stirling, in natural logs. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (information-theory → information-theory)
- [structural-analogy] Coarse-grained probability over ribbon-like H/T domains ↔ bayesian: Typical set — probability is assigned at a resolution coarser than the fine structure of the space. — from [[jaynes-2003-probability/ch10-physics]] (information-theory → bayesian)
- [structural-analogy] Wallis counting, $\tfrac1n\log W\to H$ and (11.95) ↔ information-theory: typical set / AEP — counting sequences by their empirical distribution — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → information-theory)
- [metaphor] Orthodox "averaging over unobserved data sets" ↔ information theory: ignoring the actual sequence's configuration, as in the typical-set picture (pp. 533, 551). — from [[jaynes-2003-probability/ch17-principles-p2]] (information-theory → information-theory)
- [structural-analogy] $W\approx V(\Omega')\,p(\hat\theta)$ ↔ information-theory: typical-set volume — the fraction of prior mass in the region the data single out. — from [[jaynes-2003-probability/ch20-model]] (information-theory → information-theory)
- [structural-analogy] Volume in a thin shell for large $N$ ↔ information-theory: typical-set concentration — both say mass sits away from the centre or mode (canon link; not stated in this unit). — from [[mackay-2003-information/ch02-probability]] (information-theory → information-theory)
- [structural-analogy] Typical set of X^N (high-probability strings are not the single most probable ones) ↔ Bayesian: typical set in high-dimensional posteriors, where mass lies away from the mode. — from [[mackay-2003-information/ch04-source]] (information-theory → bayesian)
- [structural-analogy] Gaussian thin shell ↔ bayesian: typical set in high-dimensional posteriors — similar concentration of mass away from the mode, though the text treats only the Gaussian (p. 131). — from [[mackay-2003-information/ch06-stream]] (information-theory → bayesian)
- [structural-analogy] Counting 2^{NH(Y)}/2^{NH(Y|X)} typical-set balls ↔ information-theory: sphere-packing bounds on code size. — from [[mackay-2003-information/ch09-communication]] (information-theory → information-theory)
- [structural-analogy] Typical-set decoding ↔ Bayesian hypothesis choice among codewords (decoder weighs "which $s$ explains $\mathbf y$"); the chapter itself uses typicality, not posteriors. — from [[mackay-2003-information/ch10-noisy]] (information-theory → unspecified)
- [structural-analogy] Sphere overlap "not disastrous" in high dimensions ↔ typical set: probability sits in tiny-volume regions, not where volume intuition suggests. — from [[mackay-2003-information/ch13-binary]] (information-theory → other)
- [structural-analogy] Typical-set decoding ↔ Chapter 10's random-code proof: the unit says both use typical sets (p. 228) and contrasts this linear-code proof with Chapter 10's random-code proof. — from [[mackay-2003-information/ch14-very]] (information-theory → other)
- [structural-analogy] Counting valid crosswords by $|T|\beta^{f_wS}$ ↔ information-theory: typical-set counting for constrained channels. — from [[mackay-2003-information/ch18-crosswords]] (information-theory → information-theory)
- [structural-analogy] Optimized $\mathbf w_{\rm MP}$ unrepresentative of samples ↔ information-theory: typical set versus the single most probable sequence. — from [[mackay-2003-information/ch41-learning]] (information-theory → information-theory)
- [structural-analogy] Energy fluctuations and the failure of typicality at criticality ↔ information-theory: typical set / AEP — the AEP's concentration needs fluctuations to be small. — from [[mackay-2003-information/ch51-appendices]] (information-theory → information-theory)
- [structural-analogy] Adversarial examples via $\|\delta\|\approx\sigma\sqrt d$ ↔ Typical set: in high dimensions mass sits in a thin shell far from the center, so ordinary and worst-case distances differ greatly. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → other)
- [structural-analogy] Block coding saving ↔ information-theory: typical set / source coding theorem — long blocks let the code use only the likely sequences. — from [[pierce-1980-introduction/ch04-encoding]] (information-theory → information-theory)
- [same-math] Probable $M$-symbol messages ($2^{MH}$) ↔ information-theory canon "typical set / AEP": same counting claim, informally stated. — from [[pierce-1980-introduction/ch05-entropy]] (information-theory → information-theory)
- [structural-analogy] Nearly all volume near the surface, so energy of long signals is nearly constant ↔ information-theory: typical set/AEP — both say long sequences concentrate on a "thin" high-probability region. — from [[pierce-1980-introduction/ch09-many]] (information-theory → information-theory)
- [metaphor] Random pattern: maximum entropy yet perceptually uniform ↔ typical set: the details are information-rich but irrelevant to the observer. — from [[pierce-1980-introduction/ch13-information]] (information-theory → other)
- [structural-analogy] counting argument ($\log_2 C_{n,nP}\approx nH$) ↔ information-theory: typical set / AEP — both say about $2^{nH}$ sequences carry nearly all probability — from [[stone-2022-information/ch03-source]] (information-theory → information-theory)
- [structural-analogy] Macrostate/microstate counting ↔ typical set: most outcomes fall in a huge set of roughly equiprobable states. — from [[stone-2022-information/ch10-thermodynamic]] (information-theory → other)
