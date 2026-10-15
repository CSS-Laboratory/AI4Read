---
id: typical-set
type: concept
fields: [information-theory, bayesian, llm]
fields_strong: [information-theory, bayesian, llm]
n_sources: 41
n_works: 9
tiers: [core, reference, deep]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, betancourt-2017-hmc/main-p2, betancourt-2017-hmc/main-p3, cover-2006-elements/ch01-introduction, cover-2006-elements/ch03-asymptotic, cover-2006-elements/ch04-entropy, cover-2006-elements/ch06-gambling, cover-2006-elements/ch07-kolmogorov, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch09-differential, cover-2006-elements/ch10-gaussian, cover-2006-elements/ch12-information-p1, cover-2006-elements/ch13-rate, cover-2006-elements/ch14-network-p1, cover-2006-elements/ch14-network-p2, cover-2006-elements/ch14-network-p3, cover-2006-elements/ch15-information, gelman-2020-workflow/main-p1, mackay-2003-information/ch04-source, mackay-2003-information/ch06-stream, mackay-2003-information/ch09-communication, mackay-2003-information/ch10-noisy, mackay-2003-information/ch14-very, mackay-2003-information/ch15-further, mackay-2003-information/ch18-crosswords, mackay-2003-information/ch22-maximum, mackay-2003-information/ch29-monte, mackay-2003-information/ch30-efficient, mackay-2003-information/ch41-learning, mackay-2003-information/ch51-appendices, murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch05-information-p1, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch09-many, polyanskiy-2025-information/ch13-fixed, polyanskiy-2025-information/ch14-entropy, polyanskiy-2025-information/ch28-rate, shannon-1948-mathematical/main-p1, shannon-1948-mathematical/main-p2, stone-2022-information/ch03-source]
aliases: [typical-set-aep]
canon_spine: [bayesian, information-theory]
generated_by: build_kg.py
---

# typical-set

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `typical-set-aep` — 30 digest(s)

## Canon spine entry

- **Typical set** (bayesian): the thin region of high-dimensional space where most probability mass actually lives, away from the mode (grad)

## Canon spine entry

- **typical set / AEP** (information-theory): long sequences almost always fall in a set of about 2^{nH} roughly equiprobable sequences (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 6): about $2^{nH}$ sequences, each of probability about $2^{-nH}$ [as `typical set / AEP`; alias `typical-set-aep`]
- [[cover-2006-elements/ch03-asymptotic]] (pp. 51–52): AEP: −(1/n)log p(X¹ⁿ) → H in probability. Typical set A_ε^(n): sequences with probability in [2^{−n(H+ε)}, 2^{−n(H−ε)}] [alias `typical-set-aep`]
- [[cover-2006-elements/ch04-entropy]] (p. 65): for stationary ergodic processes $-\frac1n\log p\to H(\mathscr X)$ a.s.; about $2^{nH}$ typical sequences [alias `typical-set-aep`]
- [[cover-2006-elements/ch06-gambling]] (p. 133): only an analogy here: red-and-black return is the same for all sequences [alias `typical-set-aep`]
- [[cover-2006-elements/ch07-kolmogorov]] (p. 159–160): used in the lower bound of Theorem 7.5.3 [alias `typical-set-aep`]
- [[cover-2006-elements/ch08-channel-p1]] (p. 195): here the joint AEP: jointly typical set $A_\epsilon^{(n)}$ with about $2^{nH(X,Y)}$ members [alias `typical-set-aep`]
- [[cover-2006-elements/ch08-channel-p2]] (pp. 216, 219): typical set of size $\le2^{n(H+\epsilon)}$ used for source coding; joint typicality in the summary [alias `typical-set-aep`]
- [[cover-2006-elements/ch09-differential]] (p. 226): continuous AEP: $-\frac1n\log f(X^n)\to h$; typical set has volume about $2^{nh}$ [alias `typical-set-aep`]
- [[cover-2006-elements/ch10-gaussian]] (pp. 244–245): joint AEP used in decoding and in the error bound [alias `typical-set-aep`]
- [[cover-2006-elements/ch12-information-p1]] (pp. 287–288): here, $\{x:D(P_x\|Q)\le\epsilon\}$ and the strongly typical set with component-wise closeness $\epsilon/|\mathcal X|$ [alias `typical-set-aep`]
- [[cover-2006-elements/ch13-rate]] (p. 351–356): used for random-coding achievability [alias `typical-set-aep`]
- [[cover-2006-elements/ch14-network-p1]] (p. 384): here extended to joint typicality over all subsets of $k$ variables [alias `typical-set-aep`]
- [[cover-2006-elements/ch14-network-p2]] (p. 393–394): joint typicality decoding and the AEP bound on $P(E_{11}^c)$ [alias `typical-set-aep`]
- [[cover-2006-elements/ch14-network-p3]] (p. 417): jointly typical sequences used for every error bound here [alias `typical-set-aep`]
- [[cover-2006-elements/ch15-information]] (p. 475): here the Shannon–McMillan–Breiman theorem: $-\frac1n\log p(X_0^{n-1})\to H$ a.s. for stationary ergodic finite-valued sources [alias `typical-set-aep`]
- [[mackay-2003-information/ch04-source]] (p. 84): T_{Nβ}: strings with (1/N)log₂(1/P) within β of H; holds almost all probability; about 2^{NH} members (p. 80). Unlike the canon's "roughly equiprobable", MacKay says equipartition holds "only in a weak sense" [as `typical set / AEP`; alias `typical-set-aep`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch06-stream]] (pp. 125, 131): a Gaussian's mass lies in a thin shell of radius $\sqrt N\sigma$, not at the density peak [alias `typical-set-aep`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch09-communication]] (p. 154): used for counting: ≈ 2^{NH(Y)} typical outputs, ≈ 2^{NH(Y|X)} per typical input [alias `typical-set-aep`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch10-noisy]] (pp. 162–163): here extended to jointly-typical pairs, with $|J_{N\beta}|\le2^{N(H(X,Y)+\beta)}$ [alias `typical-set-aep`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch14-very]] (p. 230): noise vectors with $\log 1/P\simeq NH(X)$; about $2^{NH(X)}$ of them [alias `typical-set-aep`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch15-further]] (p. 234): set $T_{N\beta}$ of likely sequences, to be counted in Ex. 15.8 [alias `typical-set-aep`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch18-crosswords]] (p. 261): used to count the $2^{f_1SH_0}$ typical fillings [as `typical set / AEP`; alias `typical-set-aep`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch22-maximum]] (p. 306): in high dimensions most mass lies in a set unlike the max-density points [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch29-monte]] (p. 360): region holding most probability, size about 2^H; uniform sampling needs about 2^(N−H) draws to hit it [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch30-efficient]] (pp. 389–390): states typical of the target; Fig. 30.2b shows a start far from it converging to it [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch41-learning]] (p. 500): here: the typical set of $\mathbf w$ has different properties from the most probable state $\mathbf w_{\rm MP}$ [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch51-appendices]] (p. 604): typicality, as used here, fails near a critical point; information content and energy fluctuations are linked [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch05-entropy]] (p. 88): about $2^{MH}$ probable $M$-symbol messages carry almost all probability [alias `typical-set-aep`]
- [[pierce-1980-introduction/ch09-many]] (pp. 172–174): here, for ergodic sources and Gaussian noise, long sequences have energy nearly constant, so they lie near a sphere surface (pp. 172–174); used qualitatively, not stated as AEP [alias `typical-set-aep`]
- [[polyanskiy-2025-information/ch13-fixed]] (p. 217): $T^n_\delta$: sequences with $|\frac1n\log\frac1{P}-H|\le\delta$; probability $\to1$, size $\le e^{(H+\delta)n}$ [alias `typical-set-aep`]
- [[polyanskiy-2025-information/ch14-entropy]] (p. 234): $T_n^\delta$ holds almost all probability and has about $e^{n\mathcal H}$ elements [alias `typical-set-aep`]
- [[polyanskiy-2025-information/ch28-rate]] (p. 499): types and joint typicality used for covering; "jointly typical" means $\mathrm{TV}(\hat P,P)=o(1)$ [alias `typical-set-aep`]
- [[shannon-1948-mathematical/main-p1]] (pp. 13–14): Theorems 3–4: about $2^{HN}$ sequences of probability about $2^{-HN}$ (pp. 13–14) (canon link; not stated in this unit) [alias `typical-set-aep`; weak: not really used in this unit]
- [[shannon-1948-mathematical/main-p2]] (pp. 38–39): continuous version: $\frac{\log p}n$ within $\epsilon$ of $H'$ as printed (see Reading notes) and $\lim\frac{\log V_n(q)}n=H'$ [alias `typical-set-aep`]
- [[stone-2022-information/ch03-source]] (pp. 71–76): not named by the author; his counting argument says most long messages fall in a set of about $2^H$ roughly equiprobable messages [alias `typical-set-aep`]

### bayesian

- [[betancourt-2017-hmc/main-p1]] (p. 7): region between mode and tails, where density × volume is significant; invariant under reparameterization
- [[betancourt-2017-hmc/main-p2]] (p. 23): region where target mass concentrates; trajectories must stay in it
- [[betancourt-2017-hmc/main-p3]] (p. 44): where mass concentrates; heavy tails push it into extremes
- [[gelman-2020-workflow/main-p1]] (p. 13): region of parameter space where log posterior density is near its expected value, which the paper relates to the typical set; warmup moves the chain toward it
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 23): here, the thin shell of radius about $\sigma\sqrt D$ holding most Gaussian mass
- [[murphy-2023-pml2/ch05-information-p1]] (p. 236): length-$N$ sequences whose per-sample negative log-probability is within $\epsilon$ of the entropy [work fields: bayesian, information-theory]

## Instances that use it

- [[grid-quadrature-curse]] — $N^D$ evaluations; grid misses the typical set — from [[betancourt-2017-hmc/main-p1]]
- [[satellite-orbit-analogy]] — planet = mode, gravity = gradient, orbit = typical set — from [[betancourt-2017-hmc/main-p1]]
- [[typical-set-flag-bit-code]] — two-part code with flag bit 0/1 — from [[cover-2006-elements/ch03-asymptotic]]
- [[ber-p-typical-set]] — typical sequences have Hamming weight fraction near $p$ — from [[polyanskiy-2025-information/ch13-fixed]]

## Candidate bridges

- [structural-analogy] Typical set ↔ statistical mechanics/information theory: mass concentrates away from the peak in a thin shell — the pattern looks the same, but this unit does not state the link. — from [[betancourt-2017-hmc/main-p1]] (bayesian → complex-systems)
- [metaphor] Gradient crashing into the mode ↔ optimization: gradient ascent/MAP finds the mode, which the typical set avoids. — from [[betancourt-2017-hmc/main-p1]] (bayesian → other:optimization)
- [structural-analogy] typical set ↔ statistical mechanics: a small set of near-equiprobable microstates carries almost all probability — from [[cover-2006-elements/ch03-asymptotic]] (information-theory → complex-systems)
- [metaphor] Most-probable macrostate = most microstates ↔ typical-set counting (AEP). — from [[cover-2006-elements/ch11-maximum]] (information-theory → unspecified)
- [structural-analogy] Gaussian as maximum-entropy attractor under variance-conserving operations ↔ information theory: maximum entropy principle and the typical set — repeated information-losing steps approach a maximum-entropy law. — from [[jaynes-2003-probability/ch07-central-p2]] (bayesian → information-theory)
- [same-math] Multiplicity $M\sim e^{nH}$ ↔ information-theory: number of sequences of a given type is $\approx 2^{nH}$ (method of types / typical set) — same counting by Stirling, in natural logs. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (bayesian → information-theory)
- [structural-analogy] Coarse-grained probability over ribbon-like H/T domains ↔ bayesian: Typical set — probability is assigned at a resolution coarser than the fine structure of the space. — from [[jaynes-2003-probability/ch10-physics]] (bayesian → bayesian)
- [structural-analogy] Wallis counting, $\tfrac1n\log W\to H$ and (11.95) ↔ information-theory: typical set / AEP — counting sequences by their empirical distribution — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → information-theory)
- [metaphor] Orthodox "averaging over unobserved data sets" ↔ information theory: ignoring the actual sequence's configuration, as in the typical-set picture (pp. 533, 551). — from [[jaynes-2003-probability/ch17-principles-p2]] (bayesian → information-theory)
- [structural-analogy] $W\approx V(\Omega')\,p(\hat\theta)$ ↔ information-theory: typical-set volume — the fraction of prior mass in the region the data single out. — from [[jaynes-2003-probability/ch20-model]] (bayesian → information-theory)
- [structural-analogy] Volume in a thin shell for large $N$ ↔ information-theory: typical-set concentration — both say mass sits away from the centre or mode (canon link; not stated in this unit). — from [[mackay-2003-information/ch02-probability]] (information-theory → information-theory)
- [structural-analogy] Typical set of X^N (high-probability strings are not the single most probable ones) ↔ Bayesian: typical set in high-dimensional posteriors, where mass lies away from the mode. — from [[mackay-2003-information/ch04-source]] (information-theory → bayesian)
- [structural-analogy] Gaussian thin shell ↔ bayesian: typical set in high-dimensional posteriors — similar concentration of mass away from the mode, though the text treats only the Gaussian (p. 131). — from [[mackay-2003-information/ch06-stream]] (information-theory → bayesian)
- [structural-analogy] Counting 2^{NH(Y)}/2^{NH(Y|X)} typical-set balls ↔ information-theory: sphere-packing bounds on code size. — from [[mackay-2003-information/ch09-communication]] (information-theory → information-theory)
- [structural-analogy] Typical-set decoding ↔ Bayesian hypothesis choice among codewords (decoder weighs "which $s$ explains $\mathbf y$"); the chapter itself uses typicality, not posteriors. — from [[mackay-2003-information/ch10-noisy]] (information-theory → unspecified)
- [structural-analogy] Sphere overlap "not disastrous" in high dimensions ↔ typical set: probability sits in tiny-volume regions, not where volume intuition suggests. — from [[mackay-2003-information/ch13-binary]] (information-theory → information-theory)
- [structural-analogy] Typical-set decoding ↔ Chapter 10's random-code proof: the unit says both use typical sets (p. 228) and contrasts this linear-code proof with Chapter 10's random-code proof. — from [[mackay-2003-information/ch14-very]] (information-theory → other:chapter-10s-random-code)
- [structural-analogy] Counting valid crosswords by $|T|\beta^{f_wS}$ ↔ information-theory: typical-set counting for constrained channels. — from [[mackay-2003-information/ch18-crosswords]] (information-theory → information-theory)
- [structural-analogy] Optimized $\mathbf w_{\rm MP}$ unrepresentative of samples ↔ information-theory: typical set versus the single most probable sequence. — from [[mackay-2003-information/ch41-learning]] (information-theory → information-theory)
- [structural-analogy] Energy fluctuations and the failure of typicality at criticality ↔ information-theory: typical set / AEP — the AEP's concentration needs fluctuations to be small. — from [[mackay-2003-information/ch51-appendices]] (information-theory → information-theory)
- [structural-analogy] Adversarial examples via $\|\delta\|\approx\sigma\sqrt d$ ↔ Typical set: in high dimensions mass sits in a thin shell far from the center, so ordinary and worst-case distances differ greatly. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → information-theory)
- [structural-analogy] Block coding saving ↔ information-theory: typical set / source coding theorem — long blocks let the code use only the likely sequences. — from [[pierce-1980-introduction/ch04-encoding]] (information-theory → information-theory)
- [same-math] Probable $M$-symbol messages ($2^{MH}$) ↔ information-theory canon "typical set / AEP": same counting claim, informally stated. — from [[pierce-1980-introduction/ch05-entropy]] (information-theory → information-theory)
- [structural-analogy] Nearly all volume near the surface, so energy of long signals is nearly constant ↔ information-theory: typical set/AEP — both say long sequences concentrate on a "thin" high-probability region. — from [[pierce-1980-introduction/ch09-many]] (information-theory → information-theory)
- [metaphor] Random pattern: maximum entropy yet perceptually uniform ↔ typical set: the details are information-rich but irrelevant to the observer. — from [[pierce-1980-introduction/ch13-information]] (information-theory → information-theory)
- [structural-analogy] counting argument ($\log_2 C_{n,nP}\approx nH$) ↔ information-theory: typical set / AEP — both say about $2^{nH}$ sequences carry nearly all probability — from [[stone-2022-information/ch03-source]] (information-theory → information-theory)
- [structural-analogy] Macrostate/microstate counting ↔ typical set: most outcomes fall in a huge set of roughly equiprobable states. — from [[stone-2022-information/ch10-thermodynamic]] (information-theory → information-theory)
