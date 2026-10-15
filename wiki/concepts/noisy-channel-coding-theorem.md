---
id: noisy-channel-coding-theorem
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 24
n_works: 6
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch10-gaussian, cover-2006-elements/ch14-network-p2, mackay-2003-information/ch01-introduction, mackay-2003-information/ch09-communication, mackay-2003-information/ch10-noisy, mackay-2003-information/ch11-error, mackay-2003-information/ch13-binary, mackay-2003-information/ch14-very, mackay-2003-information/ch15-further, pierce-1980-introduction/ch08-noisy, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch22-channels, polyanskiy-2025-information/ch24-strong, polyanskiy-2025-information/ch25-channel, shannon-1948-mathematical/main-p1, shannon-1948-mathematical/main-p2, stone-2022-information/ch04-noisy, stone-2022-information/ch07-channel, stone-2022-information/ch08-rate]
raw_ids: [noisy-channel coding theorem]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# noisy-channel-coding-theorem

## Canon spine entry

- **noisy-channel coding theorem** (information-theory): below capacity the error probability can be made arbitrarily small; above it, it cannot (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (pp. 7–8): stated informally: capacity is achievable with long block length codes [as `noisy-channel coding theorem`]
- [[cover-2006-elements/ch08-channel-p1]] (p. 198): Thm 8.7.1: rates below $C$ achievable; converse proved later
- [[cover-2006-elements/ch08-channel-p2]] (pp. 206, 219): rates $R<C$ achievable; converse $\lambda^{(n)}\to0\Rightarrow R\le C$
- [[cover-2006-elements/ch10-gaussian]] (pp. 242–247): Theorem 10.1.1: rates below $\frac12\log(1+P/N)$ are achievable; rates above are not
- [[cover-2006-elements/ch14-network-p2]] (p. 393): its random-coding proof is extended here to two senders
- [[mackay-2003-information/ch01-introduction]] (pp. 14–16): rates up to C are achievable with arbitrarily small error, and rates beyond C are not [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch09-communication]] (p. 152): part one: any R < C is achievable with arbitrarily small maximal block error for large N [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch10-noisy]] (pp. 162, 167–168): for rates $R<C$, codes with arbitrarily small (maximal) block error exist; above $R(p_b)$ they do not [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch11-error]] (p. 181): here extended to the Gaussian channel via derived discrete channels or sphere-packing intuition [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch13-binary]] (p. 212): used as in the canon; here for the BSC with $C=1-H_2(f)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch14-very]] (p. 231): here proved for the binary symmetric channel: good linear codes exist for $R<1-H(X)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch15-further]] (pp. 234, 238): Ex. 15.9 forbids invoking it; Ex. 15.20 refers to expectations from "Shannon's theories" [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch08-noisy]] (p. 156): Shannon's fundamental theorem for the noisy channel
- [[polyanskiy-2025-information/ch01-introduction]] (p. xviii): named as a classical coding theorem (Theorem 19.9)
- [[polyanskiy-2025-information/ch19-error]] (p. 345): for a memoryless channel, $\log M^*=nC+o(n)$
- [[polyanskiy-2025-information/ch21-channel]] (p. 377): $C=C^{(I)}=\sup_{P_X}I(X;Y)$ for stationary memoryless channels [as `noisy-channel coding theorem`]
- [[polyanskiy-2025-information/ch22-channels]] (pp. 397–399): here, $C(P)=C^{(I)}(P)$ via the weak converse and extended Feinstein
- [[polyanskiy-2025-information/ch24-strong]] (p. 422): below $C$, $\epsilon^*\to0$; the chapter refines it
- [[polyanskiy-2025-information/ch25-channel]] (p. 443): Theorem 23.3 extends the converse side to feedback
- [[shannon-1948-mathematical/main-p1]] (pp. 22, 25): Theorem 11 (and Theorem 12)
- [[shannon-1948-mathematical/main-p2]] (p. 42, p. 43): continuous version: rate $C$ achievable under general conditions; higher rates not
- [[stone-2022-information/ch04-noisy]] (p. 105): near-zero error up to capacity; equivocation at least $H(X)-C$ above it
- [[stone-2022-information/ch07-channel]] (pp. 155, 161): here the informal Gaussian proof and the error formula [as `noisy-channel coding theorem`]
- [[stone-2022-information/ch08-rate]] (p. 174): gives the bound $H(X|\hat X)\ge H(X)-C$ [as `noisy-channel coding theorem`]
