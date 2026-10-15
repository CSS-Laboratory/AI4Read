---
id: broadcast-channel
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch14-network-p1, cover-2006-elements/ch14-network-p3, mackay-2003-information/ch15-further]
generated_by: build_kg.py
---

# broadcast-channel

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch14-network-p1]] (p. 375): one sender, several receivers, with different messages [new]
- [[cover-2006-elements/ch14-network-p3]] (p. 418): one sender, several receivers, channel $p(y_1,y_2|x)$; question is the set of simultaneously achievable rates [new]
- [[mackay-2003-information/ch15-further]] (p. 237): one transmitter, several receivers; capacity region is a convex hull of $(R_0,R_A,R_B)$ [new; work fields: information-theory, bayesian]

## Instances that use it

- [[binary-symmetric-broadcast-channel]] — region from $1-H(\beta*p_2)$ and $H(\beta*p_1)-H(p_1)$ — from [[cover-2006-elements/ch14-network-p3]]
- [[gaussian-broadcast-channel]] — region $C(\alpha P/N_1)$, $C((1-\alpha)P/(\alpha P+N_2))$ — from [[cover-2006-elements/ch14-network-p3]]
- [[orthogonal-broadcast-channels]] — rectangular capacity region — from [[cover-2006-elements/ch14-network-p3]]
