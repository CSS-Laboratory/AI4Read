---
id: kl-divergence
type: concept
curated: 2026-10-15
fields: [information-theory, bayesian, llm, control-theory, decision-game-theory]
level: UG
grounding: digests
aliases: [relative-entropy-kl-divergence, relative-entropy-kl, relative-entropy]
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch05-data-p1, cover-2006-elements/ch05-data-p2, cover-2006-elements/ch06-gambling, cover-2006-elements/ch12-information-p1, cover-2006-elements/ch12-information-p2, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch08-f-p1, stone-2022-information/ch06-mutual, nielsen-2020-elementary/main-p2, tishby-2000-bottleneck/main, shannon-1948-mathematical/main-p1, mcelreath-2020-rethinking/ch06-overfitting-p1, blei-2017-variational/main-p1, murphy-2023-pml2/ch05-information-p1, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch10-variational-p2, murphy-2023-pml2/ch20-generative, murphy-2023-pml2/ch24-energy, murphy-2023-pml2/ch35-reinforcement, murphy-2023-pml2/ch34-decision, jaynes-2003-probability/ch05-queer, prince-2023-udl/ch05-loss, prince-2023-udl/ch23-probability, ouyang-2022-instructgpt/main-p1, rafailov-2023-dpo/main, vosoughi-2018-spread/main]
links: [entropy, cross-entropy, mutual-information, relative-entropy-shannon, kl-penalty, f-divergence, variational-inference-elbo, forwards-vs-reverse-kl]
generated_version: wiki/kg/hub-sources/kl-divergence.md
---

# KL divergence (relative entropy)

**Gist.** The KL divergence $D(p\|q)$ measures how much worse it is, on average, to use a model $q$ when the truth is $p$; it is never negative, it is zero only when $p=q$, and it is not symmetric.

Canon spine name: "relative entropy / KL divergence" (information theory). The digests used four ids for it (see `aliases`); they are merged here. Shannon's 1948 "relative entropy" is a **different** concept and is not merged (see below). All 93 digests are listed in the generated version.

## How each field uses it

### Information theory (home field)
- “$D(p\|q)=E_p\log\frac{p}{q}$; $\ge0$; not symmetric; no triangle inequality (p. 18)” — [[cover-2006-elements/ch02-entropy]]
- “$D(p\|q)$, the extra expected length when coding $p$ with a code for $q$” — [[cover-2006-elements/ch05-data-p1]] (pp. 89–90)
- “the loss from betting $\mathbf b$ instead of $\mathbf p$ is $D(\mathbf p\|\mathbf b)$” — [[cover-2006-elements/ch06-gambling]] (p. 128)
- “controls type-class probability $2^{-nD(P\|Q)}$ and the cost of a mismatched Huffman code” — [[cover-2006-elements/ch12-information-p1]] (pp. 285, 288)
- “$D(Q\|P)$, the dissimilarity between posterior $Q$ and prior $P$ in Shannon's case” — [[polyanskiy-2025-information/ch01-introduction]] (p. xviii)
- “the f-divergence with $f=x\log x$” — [[polyanskiy-2025-information/ch08-f-p1]] (p. 116)
- “D_KL(p‖q) is positive unless p = q, and usually asymmetric; MI is D_KL(joint ‖ product of marginals)” — [[stone-2022-information/ch06-mutual]] (p. 151)
- “emerges as the effective distortion $d(x,\tilde x)$” — [[tishby-2000-bottleneck/main]] (p. 12)

### Bayesian theory & modeling
- “extra uncertainty from using $q$ to describe $p$; $\sum p_i\log(p_i/q_i)$; asymmetric” — [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 179)
- “asymmetric, nonnegative measure of proximity between densities; VI minimizes KL(q‖p), here with q first” — [[blei-2017-variational/main-p1]] (pp. 3, 6)
- “expected log ratio $\sum p\log(p/q)$; size of an update from $q$ to $p$; unique under the five desiderata” — [[murphy-2023-pml2/ch05-information-p1]] (p. 221)
- “the reference prior maximizes expected KL between posterior and prior” — [[murphy-2023-pml2/ch03-statistics-p2]] (p. 107)
- “$D_{\mathbb{KL}}(q\|p)$ is zero-forcing, $D_{\mathbb{KL}}(p\|q)$ zero-avoiding” — [[murphy-2023-pml2/ch10-variational-p2]] (p. 478)
- “Jaynes's $H(f,p)$, the entropy of the observed distribution relative to the expected one, in the likelihood $e^{nH}$ (p. 121). Under the canon, $-H$ is KL.” — [[jaynes-2003-probability/ch05-queer]]

### Large language models / machine learning
- “measure of distance between two distributions, eq. 5.27” — [[prince-2023-udl/ch05-loss]] (p. 71)
- “MLE equals minimising $D_{KL}(p_D\|p_\theta)$ (p. 851)” — [[murphy-2023-pml2/ch24-energy]]
- “KL divergence; equals $-\mathbb H(p)+\mathbb H_{ce}(p,q)$” — [[murphy-2023-pml2/ch20-generative]] (p. 783)

### Control theory (reinforcement learning)
- “policy proximity and the MERL objective” — [[murphy-2023-pml2/ch35-reinforcement]] (pp. 1161, 1179)

### Decision theory
- “appears in the expected posterior change (34.96) and the regret lower bound (34.73)” — [[murphy-2023-pml2/ch34-decision]] (pp. 1128, 1141)

## Bridges between fields

- **same-math** (information theory → Bayesian): “MI as expected posterior-vs-prior KL, E_y[D_KL(p(X|y)‖p(X))] ↔ Bayesian inference: expected information gain from an observation — same expression (Eq. 6.51).” — [[stone-2022-information/ch06-mutual]]. Justification: the digest says the two expressions are identical.
- **same-math** (Bayesian → information theory): “Reference-prior objective (mutual information $\mathbb I(\theta,\mathcal D)$) ↔ information theory: expected KL between posterior and prior (p. 107).” — [[murphy-2023-pml2/ch03-statistics-p2]]. Justification: the reference prior is chosen by an information-theoretic quantity.
- **same-math** (Bayesian → information theory): “entropy $-\sum p_i\log p_i$ and $D_{KL}$ ↔ information theory/machine learning: entropy and cross-entropy loss.” — [[mcelreath-2020-rethinking/ch06-overfitting-p1]]. Justification: McElreath's model-comparison measures are the information-theory quantities.
- **structural-analogy** (information theory → LLMs/ML): “Decision boundary D(P‖P₂)−D(P‖P₁)=const ↔ classification: a nearest-prototype rule with relative entropy as distance.” — [[cover-2006-elements/ch12-information-p2]]. Justification: same shape of rule (pick the closest prototype), here with KL as the distance.
- **structural-analogy** (communication theory → information theory): “Novelty measured as KL or Bhattacharyya distance between topic distributions ↔ Information (Shannon): information as surprise relative to what the receiver expects — both tie value to departure from expectation.” — [[vosoughi-2018-spread/main]]. Justification: the paper uses KL as a novelty score; the link to Shannon information is an analogy of argument.

## Where definitions disagree

- **Two meanings of "relative entropy".** In Cover and later texts it is $D(p\|q)$ (quotes above). Shannon 1948 uses the same words for something else: “author's meaning: $H/H_{\max}$ for the same symbols. **Not** the KL divergence of the canon list” — [[shannon-1948-mathematical/main-p1]] (p. 14). That record has its own id, [[relative-entropy-shannon]], and is **not** merged.
- **"Cross entropy" as a name.** The Cover chapter-2 digest records that “The author also lists "cross entropy" as another name for it (p. 49), unlike the canon's $H(p)+D(p\|q)$.” — [[cover-2006-elements/ch02-entropy]]. Elsewhere cross entropy is the sum, e.g. “cost of a wrong code, $H(p)+D(p\|q)$, only in the summary” — [[cover-2006-elements/ch05-data-p2]] (p. 117), and in Murphy “KL divergence; equals $-\mathbb H(p)+\mathbb H_{ce}(p,q)$” — [[murphy-2023-pml2/ch20-generative]]. See [[cross-entropy]].
- **Which direction?** Variational inference minimises $D(q\|p)$ (“VI minimizes KL(q‖p), here with q first” — [[blei-2017-variational/main-p1]]); maximum likelihood minimises $D(p_D\|p_\theta)$ (Murphy ch24, above). Murphy names the behaviours: “$D_{\mathbb{KL}}(q\|p)$ is zero-forcing, $D_{\mathbb{KL}}(p\|q)$ zero-avoiding” — [[murphy-2023-pml2/ch10-variational-p2]].
- **Sign convention.** Jaynes writes an entropy "relative to the expected" distribution whose negative is KL (Jaynes ch05 quote above).
- **The RLHF "KL penalty" is a use, not a new quantity.** Prince's digest notes “$\int p\log(p/q)$; $\ge0$, asymmetric (p. 461). Not the same as the canon's "KL penalty".” — [[prince-2023-udl/ch23-probability]]. The penalty is its own id, [[kl-penalty]]: “per-token penalty from the SFT model to curb RM over-optimisation, coefficient $\beta$” — [[ouyang-2022-instructgpt/main-p1]]; “the β-weighted KL term in Eq. 3 that keeps $\pi_\theta$ near $\pi_{\text{ref}}$ and preserves diversity” — [[rafailov-2023-dpo/main]].

## Digests

Information theory: [[cover-2006-elements/ch01-introduction]], [[cover-2006-elements/ch02-entropy]], [[cover-2006-elements/ch05-data-p1]], [[cover-2006-elements/ch05-data-p2]], [[cover-2006-elements/ch06-gambling]], [[cover-2006-elements/ch12-information-p1]], [[cover-2006-elements/ch12-information-p2]], [[polyanskiy-2025-information/ch01-introduction]], [[polyanskiy-2025-information/ch08-f-p1]], [[stone-2022-information/ch06-mutual]], [[nielsen-2020-elementary/main-p2]], [[tishby-2000-bottleneck/main]], [[shannon-1948-mathematical/main-p1]] (different concept) ·
Bayesian: [[mcelreath-2020-rethinking/ch06-overfitting-p1]], [[blei-2017-variational/main-p1]], [[murphy-2023-pml2/ch05-information-p1]], [[murphy-2023-pml2/ch03-statistics-p2]], [[murphy-2023-pml2/ch10-variational-p2]], [[jaynes-2003-probability/ch05-queer]] ·
LLMs / ML: [[prince-2023-udl/ch05-loss]], [[prince-2023-udl/ch23-probability]], [[murphy-2023-pml2/ch20-generative]], [[murphy-2023-pml2/ch24-energy]], [[ouyang-2022-instructgpt/main-p1]], [[rafailov-2023-dpo/main]] ·
Control / decision: [[murphy-2023-pml2/ch35-reinforcement]], [[murphy-2023-pml2/ch34-decision]] ·
Communication theory: [[vosoughi-2018-spread/main]]
