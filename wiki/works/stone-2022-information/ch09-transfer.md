---
id: stone-2022-information/ch09-transfer
work: stone-2022-information
unit: 9 Transfer Entropy
pages: 195-202
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Transfer Entropy

## L0 — One line
Transfer entropy measures how much the past of X reduces uncertainty about the present of Y beyond what Y's own past already does, so it is a directed (time-asymmetric) measure of dependence.

## L1 — The gist (≤ 120 words)
Mutual information is symmetric, so by itself it does not distinguish the two directions. This chapter asks how information theory can capture time-ordered influence. Stone's answer is transfer entropy: the conditional mutual information $I(y_t; x_{\text{past}} \mid y_{\text{past}})$ (what $x$'s past adds about $y_t$ beyond $y$'s past). It is not symmetric, and it can detect nonlinear dependence. In a linear Gaussian example, transfer entropy from X to Y is about 0.33 bits, while the reverse direction is about 0. Correlation-based mutual information captures only about 10% of the transfer entropy there. The author notes that precedence, the idea behind transfer entropy, is necessary but not sufficient for establishing causality, since a hidden third variable can mimic it.

**Prerequisites:** entropy, conditional entropy, mutual information; Gaussian noise; autoregressive-style recurrences.

## L2 — Key ideas
- Causes must precede effects. This is the basis of transfer entropy (p. 195). The author calls this precedence condition necessary but not sufficient for establishing causality (p. 198).
- Transfer entropy is the drop in uncertainty about $y_t$ when $x_{\text{past}}$ is added to $y_{\text{past}}$: $H(y_t|y_{\text{past}}) - H(y_t|y_{\text{past}},x_{\text{past}})$ (p. 196).
- It equals the conditional mutual information $I(y_t;x_{\text{past}}|y_{\text{past}})$, which is the extra information beyond $y_{\text{past}}$ (p. 197).
- Unlike mutual information it is asymmetric. If X affects Y but not the reverse, $T_{x\to y}>0$ and $T_{y\to x}=0$ (p. 199).
- The author says it can detect dependence whatever its form, including nonlinear. Granger causality detects only linear dependence (p. 195). The Summary repeats the nonlinear point (p. 202).
- A hidden common cause $Z$ with different delays to X and Y can create a false apparent link from X to Y (p. 198).
- In the linear example, $T_{x\to y}\approx0.331$ bits (estimated) against 0.327 bits (analytic), and the reverse is about 0.001 bits (pp. 200–201).

## L3 — Walkthrough

### 9.1 Introduction (p. 195)
- Author's claim: transfer entropy is one of the few theoretical advances since Shannon's 1948 paper. It was devised to measure causal relations between variables.
- Starting observation: if changes in a causal $X$ induce changes in $Y$, each change in $X$ must precede the matching change in $Y$.
- It can detect the influence of the current $X$ on future $Y$ whatever the dependence, even nonlinear. Granger causality detects only linear dependence.
- Applications listed include bacteria, climate, ecohydrology, earthquakes, neuroscience, EEG and biomedical time series.

### 9.2 Transfer entropy (pp. 196–197)
Uncertainty about $y_t$ given only $y_{\text{past}}$, and given both pasts:
$$H(y_t|y_{\text{past}}) \tag{9.1}$$
$$H(y_t|y_{\text{past}},x_{\text{past}}) \tag{9.2}$$
Adding $x_{\text{past}}$ usually lowers uncertainty. The difference is the transfer entropy (p. 196):
$$T_{x_{\text{past}}\to y_t}=H(y_t|y_{\text{past}})-H(y_t|y_{\text{past}},x_{\text{past}}) \tag{9.3}$$
Equivalently, it is the extra information $x_{\text{past}}$ gives about $y_t$ (p. 197):
$$T_{x_{\text{past}}\to y_t}=I(y_t;x_{\text{past}}|y_{\text{past}}) \tag{9.4}$$
$$=I(y_t;y_{\text{past}},x_{\text{past}})-I(y_t;y_{\text{past}}) \tag{9.5}$$
Key point (p. 197): $T_{x_{\text{past}}\to y_t}$ is the average information that $x_{\text{past}}$ provides about $y_t$, over and above what $y_{\text{past}}$ provides.
Figures 9.1 and 9.2 show this as a Venn region. It can be read as $H(y_t|y_{\text{past}})-H(y_t|x_{\text{past}},y_{\text{past}})$ or as $H(x_{\text{past}},y_{\text{past}})-H(x_{\text{past}},y_{\text{past}}|y_t)$ (p. 196).

With explicit lags $k$ and $n$ (p. 197):
$$T_{x_{\text{past}}\to y_t}(k,n)=I\big(y_t;(x_{t-n},\dots,x_{t-1})\,\big|\,(y_{t-k},\dots,y_{t-1})\big) \tag{9.6}$$
The author says setting $n=k=0$ is common practice (see Reading notes).

*Intuition note.* Ask how well you can guess $y_t$ from $y$'s own history. Then ask how much better you guess after also seeing $x$'s history. The improvement, in bits, is the transfer entropy.

**Transfer entropy and causation (p. 198).** Precedence is necessary but not sufficient for causality. A third variable $Z$ may affect $X$ before it affects $Y$. In Fig. 9.3, $z_{t-2}$ reaches $x_{t-1}$ after 1 s and $y_t$ after 2 s, which falsely suggests $x_{t-1}\to y_t$ if only X and Y are observed. The author proceeds by defining transfer entropy as how far past $X$ is related to current $Y$.

### 9.3 The pendulum (pp. 198–199)
The pendulum's height $y_t$ is predictable from its momentum except for air noise. Using only consecutive steps:
$$I(y_t;y_{t-1})=H(y_t)-H(y_t|y_{t-1}) \tag{9.7}$$
Here $H(y_t|y_{t-1})=H(\eta_y)$, the noise entropy. If an external force $X$ nudges the pendulum, $y_t$ depends on both $x_{t-1}$ and $y_{t-1}$:
$$I(y_t;y_{t-1},x_{t-1})=H(y_t)-H(y_t|y_{t-1},x_{t-1}) \tag{9.8}$$
$$I(y_t;x_{t-1},y_{t-1})>I(y_t;y_{t-1}) \tag{9.9}$$
Transfer entropy is the gain:
$$T_{x_{t-1}\to y_t}=I(y_t;x_{t-1}|y_{t-1}) \tag{9.10}$$
$$=I(y_t;y_{t-1},x_{t-1})-I(y_t,y_{t-1}) \tag{9.11}$$
Substituting 9.7 and 9.8 into 9.11 (the $H(y_t)$ terms cancel; added step: $[H(y_t)-H(y_t|y_{t-1},x_{t-1})]-[H(y_t)-H(y_t|y_{t-1})]$):
$$T_{x_{t-1}\to y_t}=H(y_t|y_{t-1})-H(y_t|x_{t-1},y_{t-1}) \tag{9.12}$$
$$T_{y_{t-1}\to x_t}=H(x_t|x_{t-1})-H(x_t|x_{t-1},y_{t-1}) \tag{9.13}$$
Asymmetry: if the past $x_{t-1}$ affects $y_t$ but not vice versa, then $T_{x_{t-1}\to y_t}>0$ and $T_{y_t\to x_{t-1}}=0$. Mutual information is always symmetric: $I(x_{t-1};y_t)=I(y_t;x_{t-1})$ (p. 199).

### 9.4 Numerical example (pp. 200–201)
The process follows Edinburgh et al. (2021), with $\eta_x\sim\mathcal N(0,\sigma_x^2)$ and $\eta_y\sim\mathcal N(0,\sigma_y^2)$ (p. 200):
$$x_t=b_x x_{t-1}+\eta_{x,t-1} \tag{9.14}$$
$$y_t=b_y y_{t-1}+\lambda x_{t-1}+\eta_{y,t-1} \tag{9.15}$$
Parameters are $b_x=0.8$, $b_y=0.4$, $\sigma_x=\sigma_y=0.2^{1/2}$, and $\lambda$ in $[0,1]$. Fig. 9.4 uses $\lambda=0.9$. $Y$ has no effect on $X$.

- From $n=10^5$ samples: $T_{x_{t-1}\to y_t}=0.331$ bits (9.16). The analytic value is 0.327 bits (9.17) (p. 201).
- Since $x_t$ does not depend on $y_{t-1}$, $H(x_t|x_{t-1})=H(x_t|x_{t-1},y_{t-1})$ (9.18). So $T_{y_{t-1}\to x_t}=0$ from 9.13. The estimate was 0.001 bits.
- X and Y are approximately Gaussian. The measured correlation $\rho=0.212$ implies mutual information 0.032 bits (via Eq. 7.45, not in this unit). That is about 10% of 0.331, so correlation ignores about 90% of the dependence.
- A fairer comparison uses the correlation between $x_{t-1}$ and $y_t$: $\rho=0.514$, giving 0.221 bits. This still ignores about 33%.
- For Gaussian variables, transfer entropy is equivalent to Granger causality.

*Intuition note.* In this example the plain correlation between X and Y gives a mutual information of only about 10% of the transfer entropy. Even the lagged correlation still ignores about 33% (p. 201).

### 9.5 Summary (pp. 201–202)
The author argues that "correlation does not imply causation" should read "general statistical dependence does not imply causation". Transfer entropy measures time-asymmetric dependence, even for nonlinear relations. It is not an infallible test of causality, but is "arguably" less likely than other methods to mistake such dependence for causality (p. 202).

## Toy example (ours)
Let $x_t$ be independent fair coin flips (bits), and let $y_t=x_{t-1}$ exactly. Then $y_{t-1}=x_{t-2}$ is independent of $x_{t-1}$.

- $H(y_t|y_{t-1})=H(x_{t-1}|x_{t-2})=1$ bit, since the flips are independent.
- $H(y_t|y_{t-1},x_{t-1})=0$, since $x_{t-1}$ fixes $y_t$.
- $T_{x_{t-1}\to y_t}=1-0=1$ bit.
- Reverse: $H(x_t|x_{t-1})=1$ and $H(x_t|x_{t-1},y_{t-1})=1$, because $x_t$ is independent of everything earlier. So $T_{y_{t-1}\to x_t}=1-1=0$.
- Same-time mutual information $I(x_t;y_t)=I(x_t;x_{t-1})=0$, so the same-time relation shows no dependence, yet the lagged influence is a full bit.

## Concepts
- [[transfer-entropy]] — $I(y_t;x_{\text{past}}|y_{\text{past}})$: extra information $x$'s past gives about $y_t$ beyond $y$'s past (p. 196)
- [[joint-and-conditional-entropy]] — $H(y_t|y_{\text{past}})$ is the uncertainty about $y_t$ left once the past is known (p. 196)
- [[mutual-information]] — $I(y_t;y_{t-1})=H(y_t)-H(y_t|y_{t-1})$; symmetric, unlike transfer entropy (pp. 198, 199)
- [[conditional-mutual-information]] (new) — information one variable gives about another given a third; equals transfer entropy here (p. 197)
- [[granger-causality]] (new) — a measure detecting only linear dependence; the author says it equals transfer entropy for Gaussian variables (pp. 195, 201)
- [[confounding-common-cause]] (new) — a third variable $Z$ drives X and Y with different delays and fakes an $X\to Y$ link (p. 198)

## Canonical instances
- [[pendulum-nudge-example]] (new) — noise-limited pendulum with an external nudge $x_{t-1}$ (pp. 198–199)
- [[linear-gaussian-two-variable-process]] (new) — Eqs. 9.14–9.15; $T=0.331$ bits forward, about 0 reverse (p. 200)
- [[delayed-common-cause-fig-9-3]] (new) — $z_{t-2}$ reaching X in 1 s and Y in 2 s (p. 198)

## Bridges (candidates)
- [same-math] Transfer entropy for Gaussian variables ↔ econometrics: Granger causality — the author states the two are equivalent in the Gaussian case (p. 201).
- [structural-analogy] Hidden common cause with delays (Fig. 9.3) ↔ causal inference: confounding — both produce an apparent link that is not a direct effect.
- [structural-analogy] Conditioning on $y_{\text{past}}$ ↔ information theory: chain rule / conditional mutual information — only information not already supplied by $y$'s own history counts.

## Questions this raises
- How can transfer entropy be estimated from finite data when the processes are nonlinear and the histories are long?
- Can a hidden common cause be ruled out, and what extra variables or conditions would be needed?
- How should the lags $k$ and $n$ be chosen in practice?
- What does "arguably less likely than other methods" to mislead mean in concrete comparisons?

## Reading notes
- Printed page = pdf − 16.
- Eq. 9.6 sets $n=k=0$ as common practice, but with $n=k=0$ the history windows $(x_{t-n},\dots,x_{t-1})$ are empty. The one-step examples use a lag of one step. This looks like a misprint (or an unexplained indexing convention).
- Eq. 9.11 writes $I(y_t,y_{t-1})$ with a comma. Context (9.5, 9.7) implies $I(y_t;y_{t-1})$.
- p. 201 writes $I(x_t;y_{t-1})=0.221$ for the correlation between $x_{t-1}$ and $y_t$. The indices look swapped relative to the text.
- Which $\lambda$ gave 0.331 bits is not stated explicitly. Fig. 9.4 uses $\lambda=0.9$.
- Eq. 7.45 (Gaussian correlation to mutual information) is in an earlier chapter, not these pages.
- The page images agreed with the text layer on all equations used here.
