---
id: fanos-inequality
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 18
n_works: 2
tiers: [reference, core]
grounding: digests
sources: [cover-2006-elements/ch02-entropy, cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch10-gaussian, cover-2006-elements/ch14-network-p2, cover-2006-elements/ch14-network-p3, cover-2006-elements/ch14-network-p4, cover-2006-elements/ch16-inequalities, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch07-tensorization, polyanskiy-2025-information/ch13-fixed, polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch23-capacity, polyanskiy-2025-information/ch24-strong, polyanskiy-2025-information/ch25-channel, polyanskiy-2025-information/ch30-metric, polyanskiy-2025-information/ch34-lower, polyanskiy-2025-information/ch35-entropic]
aliases: [fano-inequality]
raw_ids: ["Fano's inequality"]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# fanos-inequality

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `fano-inequality` — 2 digest(s)

## Canon spine entry

- **Fano's inequality** (information-theory): a lower bound on error probability from the residual conditional entropy (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch02-entropy]] (p. 39): $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$
- [[cover-2006-elements/ch08-channel-p2]] (pp. 204–205): $H(W|Y^n)\le1+P_e^{(n)}nR$ for uniform $W$ on $2^{nR}$ messages
- [[cover-2006-elements/ch10-gaussian]] (pp. 246, 259): gives $H(W|Y^n)\le n\epsilon_n$ in both converses
- [[cover-2006-elements/ch14-network-p2]] (p. 399, 413): used in all converses
- [[cover-2006-elements/ch14-network-p3]] (p. 433): gives $H(X^n|S,T)\le n\epsilon_n$ in the converse
- [[cover-2006-elements/ch14-network-p4]] (p. 447): used in step (d) of the cut-set proof
- [[cover-2006-elements/ch16-inequalities]] (p. 488): $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$
- [[polyanskiy-2025-information/ch04-mutual]] (p. 57): $H(X|Y)\le P_e\log(M-1)+h(P_e)$ and the version (3.19) [as `Fano's inequality`]
- [[polyanskiy-2025-information/ch07-tensorization]] (p. 112): here tensorized to vectors
- [[polyanskiy-2025-information/ch13-fixed]] (p. 227): used in the converse of Theorem 11.17
- [[polyanskiy-2025-information/ch19-error]] (p. 348): gives the same bound in one line [alias `fano-inequality`]
- [[polyanskiy-2025-information/ch21-channel]] (p. 391, 393): used for the BER converse and the separation converse [as `Fano's inequality`]
- [[polyanskiy-2025-information/ch23-capacity]] (p. 415): opens the converse of Theorem 21.2 (p. 411); the same inequality (21.10) starts the converse of Theorem 21.4
- [[polyanskiy-2025-information/ch24-strong]] (p. 423, 426): gives the weak converse (Thm 17.3); the proof here instead analyzes hypothesis testing explicitly
- [[polyanskiy-2025-information/ch25-channel]] (p. 446): used as $-h(\epsilon)+\bar\epsilon\log M\le I(W;\hat W)$
- [[polyanskiy-2025-information/ch30-metric]] (p. 542): used to lower-bound mutual information by $(1-2c)\log M-\log2$ [alias `fano-inequality`]
- [[polyanskiy-2025-information/ch34-lower]] (p. 600): bounds the testing error from I(θ;X) and log M [as `Fano's inequality`]
- [[polyanskiy-2025-information/ch35-entropic]] (pp. 619, 620, 623): used for the minimax lower bounds in this chapter (Thm 32.14, Cor 32.15, §32.4), in the form of Thm 31.3

## Candidate bridges

- [structural-analogy] Fano's inequality ↔ classification or prediction from noisy data: leftover uncertainty $H(X|Y)$ forces a minimum error rate. — from [[cover-2006-elements/ch02-entropy]] (information-theory → other:classification-or-prediction-from)
- [same-math] Fano's inequality here ↔ Fano's inequality in estimation: the same bound $H(W|Y^n)\le1+P_e\log|\mathcal W|$ ties residual entropy to error. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → other:fanos-inequality-in-estimation)
- [same-math] Weak converse proof via DPI on $d(1-P_e\|1/M)$ ↔ Fano's inequality (p. 348) — from [[polyanskiy-2025-information/ch19-error]] (information-theory → unspecified)
