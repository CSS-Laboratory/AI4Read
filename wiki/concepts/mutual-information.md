---
id: mutual-information
type: concept
curated: 2026-10-15
fields: [information-theory, bayesian, political-science, llm, decision-game-theory, analytic-philosophy]
level: UG
grounding: digests
aliases: [mutual-information-ixy]
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch06-gambling, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch13-rate, mackay-2003-information/ch09-communication, mackay-2003-information/ch11-error, mackay-2003-information/ch44-supervised, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch35-entropic, stone-2022-information/ch06-mutual, stone-2022-information/ch09-transfer, gibson-2019-efficiency/main, tishby-2000-bottleneck/main, shannon-1948-mathematical/main-p1, pierce-1980-introduction/ch08-noisy, murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch34-decision, grimmer-2022-textasdata/ch11-discriminating, popper-1959-logic/appix-untitled]
links: [entropy, kl-divergence, channel-capacity, conditional-mutual-information, data-processing-inequality, information-bottleneck, rate-distortion-function, transfer-entropy]
generated_version: wiki/kg/hub-sources/mutual-information.md
---

# Mutual information

**Gist.** Mutual information $I(X;Y)$ is how much knowing one variable reduces your uncertainty about another, on average; it is symmetric and it is zero exactly when the two are independent.

Canon spine name: "mutual information I(X;Y)" (information theory). 58 digests use it (list in the generated version); almost all are information-theory texts, so this hub shows the few uses outside that field in full.

## How each field uses it

### Information theory (home field)
- “$D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)$; symmetric; $\ge0$, $=0$ iff independent” — [[cover-2006-elements/ch02-entropy]] (pp. 18–20, 27)
- “$I(X;Y)=H(Y)-H(Y|X)$, concave in $p(x)$, the quantity maximized” (for channel capacity) — [[cover-2006-elements/ch08-channel-p1]] (pp. 184, 191)
- “objective of the minimization; convex in $p(\hat x|x)$” (rate–distortion) — [[cover-2006-elements/ch13-rate]] (p. 350)
- “in a horse race equals the doubling-rate gain from side information” — [[cover-2006-elements/ch06-gambling]] (p. 131)
- “here defined as D(P_{X,Y}‖P_X P_Y), the general definition; equals H(X)−H(X|Y) for discrete X when H(X|Y)<∞” — [[polyanskiy-2025-information/ch04-mutual]] (p. 42, 44)
- “the one information measure with a well-behaved continuous limit, eq. (11.24)” — [[mackay-2003-information/ch11-error]] (p. 180)
- “$I[X:C]=H[X]-H[X\mid C]$, symmetric and non-negative” — [[gibson-2019-efficiency/main]] (p. 4)
- “$I(X;\tilde X)$ is the rate bound; $I(\tilde X;Y)$ is the relevant information” — [[tishby-2000-bottleneck/main]] (pp. 4, 9)

### Bayesian theory & modeling
- “KL divergence between joint and product of marginals; reduction in uncertainty about one variable from observing the other” — [[murphy-2023-pml2/ch05-information-p2]] (p. 238)
- “the Bayes KL risk is the conditional mutual information $I(\theta;X_{n+1}|X^n)$” — [[polyanskiy-2025-information/ch35-entropic]] (p. 605)

### Political science (text as data)
- “$H(k)-H(k|j)$: how much a word's presence reduces category uncertainty; unsigned” — [[grimmer-2022-textasdata/ch11-discriminating]] (pp. 190–191)

### Machine learning (llm field)
- “proposed classifier score $I(T;Y)$” — [[mackay-2003-information/ch44-supervised]] (p. 533)

## Bridges between fields

- **same-math** (information theory → Bayesian): “MI as expected posterior-vs-prior KL, E_y[D_KL(p(X|y)‖p(X))] ↔ Bayesian inference: expected information gain from an observation — same expression (Eq. 6.51).” — [[stone-2022-information/ch06-mutual]]. Justification: one expression, two readings (channel information vs expected learning).
- **same-math** (Bayesian → information theory): “Reference-prior objective (mutual information $\mathbb I(\theta,\mathcal D)$) ↔ information theory: expected KL between posterior and prior (p. 107).” — [[murphy-2023-pml2/ch03-statistics-p2]]. Justification: the prior is chosen to maximise the information the data carry about $\theta$.
- **same-math** (Bayesian/decision → information theory): “BALD's $\alpha(x)=\mathbb I(w;y|\mathcal D,x)$ ↔ information theory: mutual information, with the KL form (34.96).” — [[murphy-2023-pml2/ch34-decision]]. Justification: the active-learning score is a mutual information.
- **same-math** (analytic philosophy → information theory): “Hamblin's $C(x,y)=\log_2\frac{P(xy)}{P(x)P(y)}$ ↔ information theory: pointwise mutual information. Popper says it is related to the fundamental idea of information theory (p. 421); the formula itself is the standard log-ratio.” — [[popper-1959-logic/appix-untitled]]. Justification: the measure of confirmation is the pointwise version of the same log-ratio.

## Where definitions disagree

- **Name vs. quantity in Shannon and Pierce.** Shannon 1948 does not name it: “not named here; the rate $R=H(x)-H_y(x)=H(y)-H_x(y)=H(x)+H(y)-H(x,y)$ is, in a sense, the bits per second common to input and output” — [[shannon-1948-mathematical/main-p1]] (p. 22). Likewise “Pierce does not use this name. His rate $R$ in 8.8–8.10 is the same quantity” — [[pierce-1980-introduction/ch08-noisy]] (p. 155).
- **Discrete vs. general definition.** Most texts define $I=H(X)-H(X|Y)$; Polyanskiy takes the divergence form as the definition and the entropy difference as a special case (quote above, ch04).
- **Symmetric vs. directed.** Stone contrasts it with transfer entropy: “$I(y_t;y_{t-1})=H(y_t)-H(y_t|y_{t-1})$; symmetric, unlike transfer entropy” — [[stone-2022-information/ch09-transfer]] (pp. 198, 199). See [[transfer-entropy]].
- **Signed vs. unsigned use in text analysis.** Grimmer's digest notes the word-category score is “unsigned” — [[grimmer-2022-textasdata/ch11-discriminating]]: it says a word is informative, not which category it points to.

## Digests

Information theory: [[cover-2006-elements/ch01-introduction]], [[cover-2006-elements/ch02-entropy]], [[cover-2006-elements/ch06-gambling]], [[cover-2006-elements/ch08-channel-p1]], [[cover-2006-elements/ch13-rate]], [[mackay-2003-information/ch09-communication]], [[mackay-2003-information/ch11-error]], [[polyanskiy-2025-information/ch04-mutual]], [[stone-2022-information/ch06-mutual]], [[stone-2022-information/ch09-transfer]], [[gibson-2019-efficiency/main]], [[tishby-2000-bottleneck/main]], [[shannon-1948-mathematical/main-p1]], [[pierce-1980-introduction/ch08-noisy]] ·
Bayesian: [[murphy-2023-pml2/ch05-information-p2]], [[murphy-2023-pml2/ch03-statistics-p2]], [[polyanskiy-2025-information/ch35-entropic]] ·
Decision theory: [[murphy-2023-pml2/ch34-decision]] ·
Political science: [[grimmer-2022-textasdata/ch11-discriminating]] ·
ML: [[mackay-2003-information/ch44-supervised]] ·
Analytic philosophy: [[popper-1959-logic/appix-untitled]]
