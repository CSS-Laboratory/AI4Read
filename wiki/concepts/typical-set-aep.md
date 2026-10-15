---
id: typical-set-aep
type: concept
fields: [information-theory]
n_sources: 30
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch03-asymptotic, cover-2006-elements/ch04-entropy, cover-2006-elements/ch06-gambling, cover-2006-elements/ch07-kolmogorov, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch09-differential, cover-2006-elements/ch10-gaussian, cover-2006-elements/ch12-information-p1, cover-2006-elements/ch13-rate, cover-2006-elements/ch14-network-p1, cover-2006-elements/ch14-network-p2, cover-2006-elements/ch14-network-p3, cover-2006-elements/ch15-information, mackay-2003-information/ch04-source, mackay-2003-information/ch06-stream, mackay-2003-information/ch09-communication, mackay-2003-information/ch10-noisy, mackay-2003-information/ch14-very, mackay-2003-information/ch15-further, mackay-2003-information/ch18-crosswords, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch09-many, polyanskiy-2025-information/ch13-fixed, polyanskiy-2025-information/ch14-entropy, polyanskiy-2025-information/ch28-rate, shannon-1948-mathematical/main-p1, shannon-1948-mathematical/main-p2, stone-2022-information/ch03-source]
raw_ids: [typical set / AEP]
canon_spine: information-theory
generated_by: build_kg.py
---

# typical-set-aep

## Canon spine entry

- **typical set / AEP** (information-theory): long sequences almost always fall in a set of about 2^{nH} roughly equiprobable sequences (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 6): about $2^{nH}$ sequences, each of probability about $2^{-nH}$ [as `typical set / AEP`]
- [[cover-2006-elements/ch03-asymptotic]] (pp. 51–52): AEP: −(1/n)log p(X¹ⁿ) → H in probability. Typical set A_ε^(n): sequences with probability in [2^{−n(H+ε)}, 2^{−n(H−ε)}]
- [[cover-2006-elements/ch04-entropy]] (p. 65): for stationary ergodic processes $-\frac1n\log p\to H(\mathscr X)$ a.s.; about $2^{nH}$ typical sequences
- [[cover-2006-elements/ch06-gambling]] (p. 133): only an analogy here: red-and-black return is the same for all sequences
- [[cover-2006-elements/ch07-kolmogorov]] (p. 159–160): used in the lower bound of Theorem 7.5.3
- [[cover-2006-elements/ch08-channel-p1]] (p. 195): here the joint AEP: jointly typical set $A_\epsilon^{(n)}$ with about $2^{nH(X,Y)}$ members
- [[cover-2006-elements/ch08-channel-p2]] (pp. 216, 219): typical set of size $\le2^{n(H+\epsilon)}$ used for source coding; joint typicality in the summary
- [[cover-2006-elements/ch09-differential]] (p. 226): continuous AEP: $-\frac1n\log f(X^n)\to h$; typical set has volume about $2^{nh}$
- [[cover-2006-elements/ch10-gaussian]] (pp. 244–245): joint AEP used in decoding and in the error bound
- [[cover-2006-elements/ch12-information-p1]] (pp. 287–288): here, $\{x:D(P_x\|Q)\le\epsilon\}$ and the strongly typical set with component-wise closeness $\epsilon/|\mathcal X|$
- [[cover-2006-elements/ch13-rate]] (p. 351–356): used for random-coding achievability
- [[cover-2006-elements/ch14-network-p1]] (p. 384): here extended to joint typicality over all subsets of $k$ variables
- [[cover-2006-elements/ch14-network-p2]] (p. 393–394): joint typicality decoding and the AEP bound on $P(E_{11}^c)$
- [[cover-2006-elements/ch14-network-p3]] (p. 417): jointly typical sequences used for every error bound here
- [[cover-2006-elements/ch15-information]] (p. 475): here the Shannon–McMillan–Breiman theorem: $-\frac1n\log p(X_0^{n-1})\to H$ a.s. for stationary ergodic finite-valued sources
- [[mackay-2003-information/ch04-source]] (p. 84): T_{Nβ}: strings with (1/N)log₂(1/P) within β of H; holds almost all probability; about 2^{NH} members (p. 80). Unlike the canon's "roughly equiprobable", MacKay says equipartition holds "only in a weak sense" [as `typical set / AEP`]
- [[mackay-2003-information/ch06-stream]] (pp. 125, 131): a Gaussian's mass lies in a thin shell of radius $\sqrt N\sigma$, not at the density peak
- [[mackay-2003-information/ch09-communication]] (p. 154): used for counting: ≈ 2^{NH(Y)} typical outputs, ≈ 2^{NH(Y|X)} per typical input
- [[mackay-2003-information/ch10-noisy]] (pp. 162–163): here extended to jointly-typical pairs, with $|J_{N\beta}|\le2^{N(H(X,Y)+\beta)}$
- [[mackay-2003-information/ch14-very]] (p. 230): noise vectors with $\log 1/P\simeq NH(X)$; about $2^{NH(X)}$ of them
- [[mackay-2003-information/ch15-further]] (p. 234): set $T_{N\beta}$ of likely sequences, to be counted in Ex. 15.8
- [[mackay-2003-information/ch18-crosswords]] (p. 261): used to count the $2^{f_1SH_0}$ typical fillings [as `typical set / AEP`]
- [[pierce-1980-introduction/ch05-entropy]] (p. 88): about $2^{MH}$ probable $M$-symbol messages carry almost all probability
- [[pierce-1980-introduction/ch09-many]] (pp. 172–174): here, for ergodic sources and Gaussian noise, long sequences have energy nearly constant, so they lie near a sphere surface (pp. 172–174); used qualitatively, not stated as AEP
- [[polyanskiy-2025-information/ch13-fixed]] (p. 217): $T^n_\delta$: sequences with $|\frac1n\log\frac1{P}-H|\le\delta$; probability $\to1$, size $\le e^{(H+\delta)n}$
- [[polyanskiy-2025-information/ch14-entropy]] (p. 234): $T_n^\delta$ holds almost all probability and has about $e^{n\mathcal H}$ elements
- [[polyanskiy-2025-information/ch28-rate]] (p. 499): types and joint typicality used for covering; "jointly typical" means $\mathrm{TV}(\hat P,P)=o(1)$
- [[shannon-1948-mathematical/main-p1]] (pp. 13–14): Theorems 3–4: about $2^{HN}$ sequences of probability about $2^{-HN}$ (pp. 13–14) (canon link; not stated in this unit)
- [[shannon-1948-mathematical/main-p2]] (pp. 38–39): continuous version: $\frac{\log p}n$ within $\epsilon$ of $H'$ as printed (see Reading notes) and $\lim\frac{\log V_n(q)}n=H'$
- [[stone-2022-information/ch03-source]] (pp. 71–76): not named by the author; his counting argument says most long messages fall in a set of about $2^H$ roughly equiprobable messages

## Candidate bridges

- [structural-analogy] Wallis counting, $\tfrac1n\log W\to H$ and (11.95) ↔ information-theory: typical set / AEP — counting sequences by their empirical distribution — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → information-theory)
- [structural-analogy] Energy fluctuations and the failure of typicality at criticality ↔ information-theory: typical set / AEP — the AEP's concentration needs fluctuations to be small. — from [[mackay-2003-information/ch51-appendices]] (information-theory → information-theory)
- [same-math] Probable $M$-symbol messages ($2^{MH}$) ↔ information-theory canon "typical set / AEP": same counting claim, informally stated. — from [[pierce-1980-introduction/ch05-entropy]] (information-theory → information-theory)
- [structural-analogy] Nearly all volume near the surface, so energy of long signals is nearly constant ↔ information-theory: typical set/AEP — both say long sequences concentrate on a "thin" high-probability region. — from [[pierce-1980-introduction/ch09-many]] (information-theory → information-theory)
- [structural-analogy] counting argument ($\log_2 C_{n,nP}\approx nH$) ↔ information-theory: typical set / AEP — both say about $2^{nH}$ sequences carry nearly all probability — from [[stone-2022-information/ch03-source]] (information-theory → information-theory)
