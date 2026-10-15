---
id: fano-inequality
type: concept
fields: [information-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch30-metric]
generated_by: build_kg.py
---

# fano-inequality

## Definitions in the sources

### information-theory

- [[polyanskiy-2025-information/ch19-error]] (p. 348): gives the same bound in one line
- [[polyanskiy-2025-information/ch30-metric]] (p. 542): used to lower-bound mutual information by $(1-2c)\log M-\log2$

## Candidate bridges

- [structural-analogy] Fano's inequality ↔ classification or prediction from noisy data: leftover uncertainty $H(X|Y)$ forces a minimum error rate. — from [[cover-2006-elements/ch02-entropy]] (information-theory → other)
- [same-math] Fano's inequality here ↔ Fano's inequality in estimation: the same bound $H(W|Y^n)\le1+P_e\log|\mathcal W|$ ties residual entropy to error. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → other)
- [same-math] Weak converse proof via DPI on $d(1-P_e\|1/M)$ ↔ Fano's inequality (p. 348) — from [[polyanskiy-2025-information/ch19-error]] (information-theory → unspecified)
