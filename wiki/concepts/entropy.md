---
id: entropy
type: concept
curated: 2026-10-15
fields: [information-theory, bayesian, complex-systems, control-theory, communication-theory]
level: UG
grounding: digests
aliases: [entropy-hx, entropy-h-x, entropy-h, information-entropy, shannon-entropy, entropy-communication-sense]
sources: [shannon-1948-mathematical/main-p1, cover-2006-elements/ch02-entropy, cover-2006-elements/ch05-data-p1, mackay-2003-information/ch02-probability, mackay-2003-information/ch04-source, gibson-2019-efficiency/main, polyanskiy-2025-information/ch01-introduction, stone-2022-information/ch02-entropy, stone-2022-information/ch05-entropy, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch13-information, jaynes-1957-information/main, jaynes-2003-probability/ch11-discrete, jaynes-2003-probability/ch22-introduction, mcelreath-2020-rethinking/ch06-overfitting-p1, mcelreath-2020-rethinking/ch09-big, murphy-2023-pml2/ch05-information-p1, mitchell-2009-guidedtour/ch03-information, mitchell-2009-guidedtour/ch07-defining, mackay-2003-information/ch31-ising, ashby-1956-cybernetics/ch09-incessant, ashby-1956-cybernetics/ch11-requisite, carey-1989-cultural/ch01-cultural, polyanskiy-2025-information/ch02-entropy, polyanskiy-2025-information/ch15-universal, stone-2022-information/ch10-thermodynamic, ouyang-2022-instructgpt/main-p3]
links: [kl-divergence, mutual-information, cross-entropy, self-information, thermodynamic-entropy, differential-entropy, maximum-entropy-principle, perplexity]
generated_version: wiki/kg/hub-sources/entropy.md
---

# Entropy

**Gist.** Entropy is the average surprise of a random outcome: about how many yes/no answers (bits) you need, on average, to say which outcome happened.

The canon spine name is "entropy H(X)" (information theory). Every quote below is copied from a digest; the digest gives the page reference. The full list of all 55 digests that use this id is in the generated version (`generated_version` above).

## How each field uses it

### Information theory (home field)
- “$H=-\sum p_i\log p_i$ (Shannon: choice/uncertainty); $K$ only sets the unit” — [[shannon-1948-mathematical/main-p1]] (p. 11)
- “$H(X)=-\sum p\log p=E\log\frac1{p(X)}$; depends only on probabilities; $0\le H\le\log|\mathcal X|$” — [[cover-2006-elements/ch02-entropy]] (pp. 13–14, 27)
- “the lower bound $H_D(X)$ on expected length of instantaneous codes” — [[cover-2006-elements/ch05-data-p1]] (p. 86)
- “$H(X)=\sum P(x)\log\frac1{P(x)}$, the average information content, also called uncertainty” — [[mackay-2003-information/ch02-probability]] (p. 32)
- “average surprisal of a random variable, as uncertainty about its value” — [[gibson-2019-efficiency/main]] (p. 4)
- “average, over outcomes, of the KL dissimilarity between prior and the posterior that puts all mass on the observed outcome” — [[polyanskiy-2025-information/ch01-introduction]] (p. xviii)

### Bayesian theory & modeling
- “$-K\sum p_i\ln p_i$, read as the amount of uncertainty in a distribution” — [[jaynes-1957-information/main]] (p. 622)
- “$H=-\sum p_i\log p_i$, here called information entropy, derived from the Shannon conditions” — [[jaynes-2003-probability/ch11-discrete]] (p. 350)
- “$H(p)=-\sum p_i\log p_i$; uncertainty in a distribution” — [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 178)
- “$H(p)=-\sum p_i\log p_i$; here treated as approximately log number of ways per observation” — [[mcelreath-2020-rethinking/ch09-big]] (pp. 268, 270)
- “$-\sum p\log p$; $\log K$ minus KL to the uniform” — [[murphy-2023-pml2/ch05-information-p1]] (p. 235)

### Complex systems
- “in physics, energy unavailable for more work; in Boltzmann's sense, a function of the number of microstates behind a macrostate” — [[mitchell-2009-guidedtour/ch03-information]] (pdf 65, 75)
- “average information or surprise of a message source; maximal for random sequences” — [[mitchell-2009-guidedtour/ch07-defining]] (pdf 128)
- “here called $S=\sum p\ln(1/p)$ and tied to $\ln Z$ and free energy (Ex. 31.1)” — [[mackay-2003-information/ch31-ising]] (p. 402)

### Control theory & cybernetics
- “Shannon's $H=-\sum p\log p$; Ashby uses the word only in this sense” — [[ashby-1956-cybernetics/ch09-incessant]] (pp. 174–175)

### Communication theory
- “Carey's own gloss: the world is not strictly ordered, so the mind imposes order (p. 20) (differs from canon: Carey means only that the world is loosely ordered, not Shannon entropy)” — [[carey-1989-cultural/ch01-cultural]] (p. 20)

## Bridges between fields

- **same-math** (information theory → complex systems): “Shannon entropy H ↔ statistical mechanics: Gibbs entropy k_B Σp_i ln(1/p_i), equal to H up to the factor k_B (p. 87).” — [[mackay-2003-information/ch04-source]]. Justification: the two formulas are the same sum; only the constant $k_B$ differs.
- **same-math** (information theory → complex systems): “Boltzmann–Gibbs entropy $S=kn\sum p_j\log\frac1{p_j}$ ↔ statistical physics: the same sum as $nH(P)$, times $k$ (p. 15)” — [[polyanskiy-2025-information/ch02-entropy]]. Justification: the digest states it is the same sum.
- **same-math** (Bayesian → information theory): “Wallis multiplicity and Stirling's approximation ↔ information theory: Shannon entropy as the rate of growth of log counts — the derivation is literally this.” — [[mcelreath-2020-rethinking/ch09-big]]. Justification: counting the ways to get a distribution gives $H$.
- **same-math** (control theory → information theory): “Ashby's entropy form ($H(E)\ge H(D)-H(R)$ when $H_D(R)=0$) ↔ information theory: limit on noise removable by a correction channel (Shannon's Theorem 10, as stated on p. 211).” — [[ashby-1956-cybernetics/ch11-requisite]]. Justification: the law of requisite variety written with entropies is Shannon's bound.
- **same-math** (information theory → LLMs): “Log-loss on next-token prediction ↔ LLM cross-entropy training: the text states they solve the same task.” — [[polyanskiy-2025-information/ch15-universal]]. Justification: the same loss is minimised.
- **same-math** (information theory → LLMs): “"Entropy $n$ bits ≈ $2^n$ equiprobable states" ↔ language modelling: perplexity $=2^{\text{entropy}}$ — the effective number of choices.” — [[stone-2022-information/ch10-thermodynamic]]. Justification: perplexity is entropy on an exponential scale.
- **same-math** (LLMs → information theory): “Entropy bias metric ↔ information theory: Shannon entropy of a normalized binary distribution — literally $-\sum P\log_2P$.” — [[ouyang-2022-instructgpt/main-p3]]. Justification: the metric is the formula itself.
- **structural-analogy** (Bayesian → complex systems): “Entropy as "most ways" ↔ statistical mechanics: many microstates produce the observed macrostate, as with the knotted cords (p. 267).” — [[mcelreath-2020-rethinking/ch09-big]]. Justification: same counting argument, used for priors instead of gases.
- **metaphor** (Bayesian → information theory): “Flat minima as "large volume" regions ↔ entropy in statistical mechanics: volume weighting favours wide basins.” — [[murphy-2023-pml2/ch17-bayesian]]. Justification: inspiring picture only; no formula is shared.

## Where definitions disagree

- **Whose uncertainty?** Shannon's digest glosses $H$ as choice or uncertainty (quote above), while Jaynes says it is “the engineer's ignorance about messages, not the sender's information” — [[jaynes-2003-probability/ch22-introduction]] (pp. 634–635).
- **Information entropy vs. physical entropy.** Mitchell's digest gives the physics meaning: “energy unavailable for more work” — [[mitchell-2009-guidedtour/ch03-information]]. The Shannon quantity and the thermodynamic quantity have their own ids here: [[thermodynamic-entropy]] (Boltzmann's and Gibbs' formulas, in joules per degree) is kept separate and linked by the same-math bridges above, not merged.
- **Discrete vs. continuous.** Stone's digest notes the histogram entropy is “infinite for a continuous variable as bin width → 0” — [[stone-2022-information/ch05-entropy]] (p. 114, p. 116). The continuous version is a different id: [[differential-entropy]].
- **Loose, non-technical uses.** Carey's "entropy" is not Shannon entropy (quote above). Pierce's chapter on the arts uses the id for “here "variety/information rate" of a work, which must stay within human limits to be distinctive” — [[pierce-1980-introduction/ch13-information]] (p. 252).
- **Naming of nearby quantities.** "Relative entropy" means $D(p\|q)$ in Cover and later texts but $H/H_{\max}$ in Shannon 1948; "cross entropy" also has two meanings. See [[kl-divergence]].

## Digests

Information theory: [[shannon-1948-mathematical/main-p1]], [[cover-2006-elements/ch02-entropy]], [[cover-2006-elements/ch05-data-p1]], [[mackay-2003-information/ch02-probability]], [[mackay-2003-information/ch04-source]], [[gibson-2019-efficiency/main]], [[polyanskiy-2025-information/ch01-introduction]], [[polyanskiy-2025-information/ch02-entropy]], [[polyanskiy-2025-information/ch15-universal]], [[stone-2022-information/ch02-entropy]], [[stone-2022-information/ch05-entropy]], [[stone-2022-information/ch10-thermodynamic]], [[pierce-1980-introduction/ch05-entropy]], [[pierce-1980-introduction/ch13-information]], [[jaynes-1957-information/main]] ·
Bayesian: [[jaynes-2003-probability/ch11-discrete]], [[jaynes-2003-probability/ch22-introduction]], [[mcelreath-2020-rethinking/ch06-overfitting-p1]], [[mcelreath-2020-rethinking/ch09-big]], [[murphy-2023-pml2/ch05-information-p1]], [[murphy-2023-pml2/ch17-bayesian]] ·
Complex systems: [[mitchell-2009-guidedtour/ch03-information]], [[mitchell-2009-guidedtour/ch07-defining]], [[mackay-2003-information/ch31-ising]] ·
Control theory: [[ashby-1956-cybernetics/ch09-incessant]], [[ashby-1956-cybernetics/ch11-requisite]] ·
Communication theory: [[carey-1989-cultural/ch01-cultural]] ·
LLMs: [[ouyang-2022-instructgpt/main-p3]]
