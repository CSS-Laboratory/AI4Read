---
id: joint-and-conditional-entropy
type: concept
fields: [information-theory]
n_sources: 23
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch04-entropy, cover-2006-elements/ch14-network-p1, cover-2006-elements/ch16-inequalities, gibson-2019-efficiency/main, mackay-2003-information/ch08-dependent, mackay-2003-information/ch09-communication, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch08-noisy, pierce-1980-introduction/ch14-back, polyanskiy-2025-information/ch02-entropy, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch09-entropy, shannon-1948-mathematical/main-p1, shannon-1951-prediction/main, stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/appf-rules, stone-2022-information/ch04-noisy, stone-2022-information/ch06-mutual, stone-2022-information/ch08-rate, stone-2022-information/ch09-transfer]
raw_ids: [joint and conditional entropy]
canon_spine: information-theory
generated_by: build_kg.py
---

# joint-and-conditional-entropy

## Canon spine entry

- **joint and conditional entropy** (information-theory): uncertainty of a pair, and what remains about X once Y is known (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 6): here only conditional entropy $H(X|Y)$ is named, as uncertainty of $X$ given $Y$ [as `joint and conditional entropy`]
- [[cover-2006-elements/ch02-entropy]] (pp. 15–16): $H(X,Y)$ is the entropy of the pair; $H(Y|X)=\sum_xp(x)H(Y|X=x)$
- [[cover-2006-elements/ch04-entropy]] (p. 64): $H(X_n|X_{n-1},\dots,X_1)$ decreases to $H'(\mathscr X)$
- [[cover-2006-elements/ch14-network-p1]] (p. 386): used for conditional typical sets
- [[cover-2006-elements/ch16-inequalities]] (p. 483): conditioning reduces entropy; used in every proof of Sec. 16.5, 16.8–16.9
- [[gibson-2019-efficiency/main]] (p. 4): $H[X\mid C]$, uncertainty left about $X$ given $C$; between 0 and $H[X]$
- [[mackay-2003-information/ch08-dependent]] (p. 138): $H(X,Y)$; $H(X|y)$ is entropy of one conditional distribution; $H(X|Y)$ averages over $y$
- [[mackay-2003-information/ch09-communication]] (p. 147): H(X|Y) averages H(X|y) over y; can exceed H(X) for a particular y
- [[pierce-1980-introduction/ch05-entropy]] (pp. 91–93): (5.4) averages the entropy of the next symbol given the preceding block, weighted by block probability
- [[pierce-1980-introduction/ch08-noisy]] (pp. 153–154): $H(x,y)$, $H_x(y)$, $H_y(x)$: pair uncertainty and uncertainty given the other symbol [as `joint and conditional entropy`]
- [[pierce-1980-introduction/ch14-back]] (p. 272): here the equivocation $H_y(x)$: uncertainty about the message given the cipher text [as `joint and conditional entropy`]
- [[polyanskiy-2025-information/ch02-entropy]] (p. 9–10): $H(X^n)$ and $H(X|Y)=\mathbb E_y[H(P_{X|Y=y})]$
- [[polyanskiy-2025-information/ch04-mutual]] (p. 44): $I+H(X|Y)=H(X)$ (3.2) [as `joint and conditional entropy`]
- [[polyanskiy-2025-information/ch09-entropy]] (p. 164): conditioning reduces entropy, used for $h(X_S)$ bounds
- [[shannon-1948-mathematical/main-p1]] (p. 12): $H(x,y)$, $H_x(y)$ (conditional entropy of $y$ given $x$)
- [[shannon-1951-prediction/main]] (p. 51): $F_N$ is the average uncertainty of the next letter given the preceding $N-1$ letters
- [[stone-2022-information/appa-glossary]] (p. 242): $H(Y|X)=\mathrm E[\log(1/p(y|x))]$
- [[stone-2022-information/appb-mathematical]] (pp. 248–249): $H(X,Y)$ is the entropy of the joint distribution. $H(X|Y)$ is the average uncertainty in $X$ after $Y$ is observed.
- [[stone-2022-information/appf-rules]] (p. 265): H.3–H.11 [as `joint and conditional entropy`]
- [[stone-2022-information/ch04-noisy]] (pp. 84, 91): $H(X,Y)$ is average surprisal per pair; $H(Y|X)$ is residual uncertainty about $Y$ after $X$
- [[stone-2022-information/ch06-mutual]] (pp. 139, 143–144): H(X,Y) is the dispersion of the joint density; H(Y|X) is the average entropy of slices p(Y|x) [as `joint and conditional entropy`]
- [[stone-2022-information/ch08-rate]] (p. 174): equivocation $E=H(X|\hat X)$ used as the uncertainty measure [as `joint and conditional entropy`]
- [[stone-2022-information/ch09-transfer]] (p. 196): $H(y_t|y_{\text{past}})$ is the uncertainty about $y_t$ left once the past is known
