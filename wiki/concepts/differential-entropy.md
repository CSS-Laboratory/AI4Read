---
id: differential-entropy
type: concept
fields: [information-theory, bayesian]
n_sources: 21
tiers: [core, reference, deep]
grounding: digests
sources: [cover-2006-elements/ch09-differential, cover-2006-elements/ch10-gaussian, cover-2006-elements/ch11-maximum, cover-2006-elements/ch13-rate, cover-2006-elements/ch14-network-p2, cover-2006-elements/ch16-inequalities, jaynes-2003-probability/ch12-ignorance, mackay-2003-information/ch11-error, murphy-2023-pml2/ch05-information-p1, nielsen-2020-elementary/main-p2, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch09-entropy, polyanskiy-2025-information/ch27-rate, polyanskiy-2025-information/ch29-evaluating, shannon-1948-mathematical/main-p2, stone-2022-information/appa-glossary, stone-2022-information/appd-probability, stone-2022-information/ch05-entropy, stone-2022-information/ch06-mutual, stone-2022-information/ch07-channel]
raw_ids: [differential entropy]
canon_spine: information-theory
generated_by: build_kg.py
---

# differential-entropy

## Canon spine entry

- **differential entropy** (information-theory): entropy for continuous variables; it can be negative and depends on coordinates (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch09-differential]] (pp. 224, 227): $h(X)=-\int_Sf\log f$; can be negative; log of the effective side length of the smallest set holding most of the probability
- [[cover-2006-elements/ch10-gaussian]] (p. 241): used with $h(Z)=\frac12\log2\pi eN$; the normal maximizes it for given variance
- [[cover-2006-elements/ch11-maximum]] (p. 266): $h(f)=-\int f\ln f$, concave in $f$; used throughout
- [[cover-2006-elements/ch13-rate]] (p. 345): used in the Gaussian lower bound
- [[cover-2006-elements/ch14-network-p2]] (p. 404–405): used to evaluate Gaussian MAC bounds
- [[cover-2006-elements/ch16-inequalities]] (pp. 485, 488): $-\int f\log f$; may be negative; Gaussian maximises it at given covariance
- [[jaynes-2003-probability/ch12-ignorance]] (p. 375): $-\int p\log p$ is not derived and not the correct measure (it also lacks invariance); $-\int p\log(p/m)$ is the continuous measure
- [[mackay-2003-information/ch11-error]] (p. 180): the problem MacKay points out: replacing sums by integrals is not well defined; entropy depends on grain size
- [[nielsen-2020-elementary/main-p2]] (pp. 29, 31, 39): $h(p)=-\int p\log p$; negative entropy of a mixture is not closed-form
- [[polyanskiy-2025-information/ch03-divergence]] (p. 27): $h(X)=-D(P_X\|\mathrm{Leb})$; can be negative, $\pm\infty$ or undefined [as `differential entropy`]
- [[polyanskiy-2025-information/ch04-mutual]] (pp. 44, 47, 64): used for Gaussian examples and the EPI [as `differential entropy`]
- [[polyanskiy-2025-information/ch09-entropy]] (p. 164): $h(X^n)=\log\mathrm{Leb}(K)$ for $X^n$ uniform on $K$
- [[polyanskiy-2025-information/ch27-rate]] (p. 483): $h(X)=-\int p\log p$; appears in the entropy of a uniform quantizer's output [as `differential entropy`]
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 509–510): used in the Gaussian error-geometry argument; may be undefined for discrete $\hat S$
- [[shannon-1948-mathematical/main-p2]] (pp. 35, 37–38): $H=-\int p\log p\,dx$; relative to coordinates, can be negative, changes by $-E[\log J]$ under a change of variables
- [[stone-2022-information/appa-glossary]] (p. 242): expected value $\mathrm E[\log(1/p(x))]$ for a continuous variable
- [[stone-2022-information/appd-probability]] (p. 258): the same expectation for continuous X, as an integral [as `differential entropy`]
- [[stone-2022-information/ch05-entropy]] (p. 117, p. 126): $E[\log 1/p(X)]$, the entropy of a continuous variable with the infinite term dropped; can be negative
- [[stone-2022-information/ch06-mutual]] (pp. 138–139, 146): entropy of continuous variables; an infinite constant is ignored, and it cancels in MI [as `differential entropy`]
- [[stone-2022-information/ch07-channel]] (p. 155): Gaussian entropy $\tfrac12\log2\pi ev$, used for noise, input and output [as `differential entropy`]

### bayesian

- [[murphy-2023-pml2/ch05-information-p1]] (p. 235): continuous analogue; can be negative; unit-dependent [new]
