---
id: cut-set-bound
type: concept
fields: [information-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch14-network-p1, cover-2006-elements/ch14-network-p4]
generated_by: build_kg.py
---

# cut-set-bound

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch14-network-p1]] (p. 377): information flow across any cut is bounded; generally not achievable [new]
- [[cover-2006-elements/ch14-network-p4]] (p. 445): $\sum R^{(ij)}\le I(X^{(S)};Y^{(S^c)}|X^{(S^c)})$ across a cut S [new]

## Instances that use it

- [[relay-channel]] — cut-set bound with $C\le\sup\min\{I(X,X_1;Y),I(X;Y,Y_1|X_1)\}$ — from [[cover-2006-elements/ch14-network-p4]]

## Candidate bridges

- [structural-analogy] Cut-set bound on information flow ↔ graph theory: max-flow min-cut — the same cut idea, but equality fails for information in general. — from [[cover-2006-elements/ch14-network-p1]] (information-theory → other)
- [structural-analogy] cut-set bound ↔ graph theory: max-flow–min-cut — the text itself offers this reading, with mutual information in place of edge capacity. — from [[cover-2006-elements/ch14-network-p4]] (information-theory → other)
