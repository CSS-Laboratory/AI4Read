---
id: conditional-mutual-information
type: concept
fields: [information-theory]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch02-entropy, mackay-2003-information/ch08-dependent, polyanskiy-2025-information/ch04-mutual, stone-2022-information/ch09-transfer]
generated_by: build_kg.py
---

# conditional-mutual-information

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch02-entropy]] (pp. 22, 33): $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)$; $\ge0$; can exceed $I(X;Y)$ without a Markov chain [new]
- [[mackay-2003-information/ch08-dependent]] (pp. 139, 144): $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)$; may exceed $I(X;Y)$ [new]
- [[polyanskiy-2025-information/ch04-mutual]] (p. 50): $I(X;Y|Z)=\mathbb E_z I(X;Y|Z=z)$ [new]
- [[stone-2022-information/ch09-transfer]] (p. 197): information one variable gives about another given a third; equals transfer entropy here [new]

## Candidate bridges

- [structural-analogy] Prior making data irrelevant ($AA=A$) ↔ information-theory: conditional mutual information is zero when the prior already contains the information. — from [[jaynes-2003-probability/ch08-sufficiency]] (information-theory → information-theory)
- [structural-analogy] directed information $\vec I(X^n;Y^n)$ ↔ information-theory: transfer entropy — both are sums of conditional mutual informations measuring causally directed flow, though the conditioning sets differ. — from [[polyanskiy-2025-information/ch25-channel]] (information-theory → information-theory)
- [structural-analogy] Conditioning on $y_{\text{past}}$ ↔ information theory: chain rule / conditional mutual information — only information not already supplied by $y$'s own history counts. — from [[stone-2022-information/ch09-transfer]] (information-theory → information-theory)
