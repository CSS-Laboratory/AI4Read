---
id: jaynes-2003-probability/ch09-repetitive-p2
work: jaynes-2003-probability
unit: "9 Repetitive experiments: probability and frequency (part 2/2: end of §9.9 through §9.16.2)"
pages: 292-313
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Repetitive experiments: probability and frequency (part 2/2)

## L0 — One line
A goodness-of-fit test is only meaningful relative to a stated class of alternatives; Bayes' theorem gives an exact version (ψ) for the Bernoulli class of alternatives; Pearson's χ² approximates it when frequencies are close to the expected ones, and it grossly over-penalises very unlikely events.

## L1 — The gist (≤ 120 words)
Jaynes separates probability (a state of knowledge) from frequency (a fact about the world). He then asks how a significance test can work when it names no alternative. Answer: it implicitly uses a class of alternatives. For the Bernoulli class (independent trials with fixed probabilities), Bayes' theorem gives an exact measure, ψ (in decibels), of the best support any alternative can get. Pearson's χ² (a standard fit statistic) is nearly proportional to ψ when observed frequencies are close to expected ones, and it can badly over-penalise rare events. The unit then covers the χ² test in practice, Halley's 1693 mortality table, a defence of induction against Hume and Popper, and a note on superstition.

**Prerequisites:** Bayes' theorem in odds/evidence form (decibels, Ch. 4); binomial and Poisson distributions; Taylor series of log; the idea of a Gibbs/maximum-entropy distribution (§9.9).

## L2 — Key ideas (5–10 bullets)
- Probabilities are assigned to represent knowledge; frequencies are measured facts. They coincide only for particular states of knowledge. Many probability–frequency links follow as theorems, so no frequency definition of probability is needed (p. 292–293).
- No alternative can be supported against H by more than ψ∞ = −10 log₁₀ p(D|H) dB. A "sure-thing" hypothesis always reaches that bound, so raw p(D|H) cannot be the fit criterion (p. 296).
- Within the Bernoulli class $B_m$, ψ_B = 10 Σ n_k log₁₀(n_k/np_k) is the exact maximum support any alternative can get against H. Jaynes calls −ψ_B/n an entropy per symbol, which arises from Bayes' theorem alone, independently of Shannon (p. 297–298).
- χ² is nearly proportional to ψ_B when frequencies are near the expected values (condition A: deviations grow only like √n). Its 1/p_k weighting grossly over-penalises small discrepancies on very unlikely events (p. 298–301).
- In the 3-outcome coin example, χ² prefers the Martian's uniform hypothesis over the better-informed one, while ψ does not (p. 300).
- The χ² test is the "tail area" test using a universal large-n distribution; reporting P-values is better than a fixed 5% verdict, and ψ needs no tables (p. 302–304).
- The ψ construction generalises to any well-defined class C of alternatives. χ² tests only relative to the Bernoulli class (p. 305).
- Halley (1693) used observed frequencies as probabilities and spoke of odds. Jaynes complains that he did not show his raw data (p. 305–309).
- Induction yields the predictions most strongly indicated by given information, not guaranteed truths. Bayesian inference is relative to a definite set of alternatives (p. 310–311).

## L3 — Walkthrough

### End of §9.9 — Gibbs canonical ensemble (p. 292)
A condition from the previous part (not shown) holds if and only if $f_j=u_j$. The remaining step is to choose λ so that the required average $\overline G$ is realised. From (9.75), where Z is defined (outside this part):
$$\overline{G}=-\frac{\partial \log Z}{\partial\lambda}\tag{9.78}$$
This is solved for λ. Its right side is continuous and strictly decreasing in λ on the real axis, so there is only one real root and the solution is unique (p. 292). This is the "Gibbs canonical ensemble" formalism of quantum statistics for a closed system. Jaynes says its generality far beyond that application is now evident (p. 292).

### 9.10 Probability and frequency (p. 292–293)
- **Jaynes' definitions.** A probability is assigned to represent a state of knowledge, or calculated from assigned probabilities by the rules. A frequency is a factual property of the world that we measure or estimate. "Estimating a probability" is a logical incongruity, like "assigning a frequency" (p. 292).
- **Relativity principle.** Probabilities change when knowledge changes; frequencies do not. So p(E) can equal f(E) only for particular states of knowledge, for example when the only information about E is its observed frequency (p. 292).
- **Two familiar links.** Under exchangeability plus other prior information, an observed frequency in a binary experiment becomes an assigned probability by Laplace's rule of succession (Chapters 6 and 18). Under independence, an assigned probability becomes an estimated frequency by Bernoulli's weak law of large numbers, with de Moivre–Laplace for error estimates (p. 292).
- **Other links** are contained in maximum entropy (Ch. 11), transformation groups (Ch. 12) and the theory of fluctuations in exchangeable sequences. Jaynes thinks a researcher could find about a dozen logically distinct connections. They appear automatically as consequences of probability as logic, so a probability never needs to be defined as a frequency (p. 292–293).
- **Jaynes' view of the dispute.** Fisher, Neyman, von Mises, Feller and Savage denied that probability is an extension of logic (p. 293). Mr A (frequencies) and Mr B (logical inference) each have the right to work. Jaynes cannot see why A does not simply say "frequency". Substituting "frequency" for their "probability" would, he says, go a long way toward clearing up the confusion. He thinks most real scientific problems are Mr B's (p. 293).

*Intuition note.* "Probability" here means what you know. "Frequency" means what happened. They can match only for particular states of knowledge, for example when all you know about the event is its observed frequency.

### 9.11 Significance tests (p. 293–296)
**Setup.** Orthodox tests purport to reject hypotheses without alternatives (p. 293). With two hypotheses H, H′ we must have P(H|DI)+P(H′|DI)=1. Bayes' theorem in decibel evidence (Chapter 4) is
$$e(H|DI)=e(H|I)+10\log_{10}\!\left[\frac{P(D|H)}{P(D|H')}\right]\tag{9.79}$$
In words, the data support H relative to H′ by that many dB. The phrase "relative to H′" is essential. Against another alternative H″ the change might be entirely different. Asking how much data support H "in themselves" makes no sense, except when D is impossible on H (p. 294).

**Poisson example (particle counter, Ch. 6).** With known source strength and efficiency, counts per second are Poisson with mean λ=sφ:
$$p(c|s\phi)=e^{-\lambda}\frac{\lambda^c}{c!},\quad 0\le c\le\infty\tag{9.80}$$
If the event c=12 has independent probability
$$p=e^{-\lambda}\frac{\lambda^{12}}{12!}\tag{9.81}$$
at each trial, the number r of occurrences in n trials is binomial:
$$b(r|n,p)=\binom nr p^r(1-p)^{n-r}\tag{9.82}$$
(p. 294).

**Moments, by the operator $p\,d/dp$ (p. 295).** With q=1−p set at the end:
$$\langle r\rangle=\sum_{r=0}^n r\,b(r|n,p)=\Big[p\frac{d}{dp}\sum_r\binom nr p^r q^{n-r}\Big]_{q=1-p}=\Big(p\frac{d}{dp}\Big)(p+q)^n=np\tag{9.83}$$
$$\langle r^2\rangle=\Big(p\frac d{dp}\Big)^2(p+q)^n=np+n(n-1)p^2,$$
$$\langle r^3\rangle=\Big(p\frac d{dp}\Big)^3(p+q)^n=np+2n(n-1)p^2+n(n-1)(n-2)p^3\ \text{[as printed; see Reading notes]}\tag{9.84}$$
Each higher moment applies $p\,d/dp$ once more, then sets p+q=1. The estimates are
$$(r)_{\rm est}=\langle r\rangle\pm\sqrt{\langle r^2\rangle-\langle r\rangle^2}=np\pm\sqrt{np(1-p)}\tag{9.85}$$
$$(f)_{\rm est}=p\pm\sqrt{p(1-p)/n},\quad f=r/n\tag{9.86}$$
This is Bernoulli's original link between probability and frequency (p. 295).

**The puzzle.** If after a few thousand counts the observed frequencies are far outside the limits (9.86), intuition says the Poisson form or the independence assumption is wrong. Yet no alternative was named. Jaynes says this is a question about psychology, i.e. what intuition is doing, not about probability theory (p. 295–296).

### 9.11.1 Implied alternatives (p. 296–299)
Since $p(D|H')\le1$ for any H′, from (9.79):
$$e(H|DI)\ge e(H|I)+10\log_{10}p(D|H)=e(H|I)-\psi_\infty\tag{9.87}$$
$$\psi_\infty\equiv-10\log_{10}p(D|H)\ge0\tag{9.88}$$
So no alternative can be supported relative to H by more than ψ∞ dB (p. 296). The proper question is therefore whether any alternative is supported by D relative to H, and by how much. Asking how well D supports H, with no alternative named, is not well posed (p. 296).

**ψ∞ is not a good fit criterion.** After D is seen one can invent a "sure thing" hypothesis H_S with p(D|H_S)=1, supported relative to H by exactly ψ∞. For a die tossed n=10 000 times with H="honest", each outcome has probability 6⁻ⁿ, so
$$\psi_\infty=10\log_{10}(6^n)=77\,815\ \text{dB}\tag{9.89}$$
Continuing to believe the die honest requires that H_S had prior probability below −77 815 dB. This is consistent: there were 6ⁿ equally likely "sure thing" hypotheses before D. In practice we compare H only with a restricted class Ω of "reasonable" alternatives (p. 296–297).

**Bernoulli class $B_m$.** There are m results $A_1,\dots,A_m$ per trial. Define
$$x_i\equiv k\ \text{ if }A_k\text{ is true at trial }i\tag{9.90}$$
In $B_m$ the trials are independent and stationary, so
$$p(x_1\dots x_n|H)=p_1^{n_1}\cdots p_m^{n_m}\tag{9.91}$$
with $n_k$ the number of occurrences of $A_k$. Each H in $B_m$ corresponds to $\{p_k\}$ with $p_k\ge0$, $\sum p_k=1$, and conversely (p. 297).

**Gibbs' lemma.** Put $x=n_k/np_k$ and use $\log x\ge1-x^{-1}$ on the positive reals, with equality iff x=1. Then
$$\sum_{k=1}^m n_k\log\!\Big(\frac{n_k}{np_k}\Big)\ge0\tag{9.92}$$
with equality iff $p_k=n_k/n$ for all k. (Added step: multiplying by $n_k$ and summing gives $\ge \sum_k (n_k-np_k)=n-n=0$.) Equivalently, with $f_k=n_k/n$,
$$\log p(x_1\dots x_n|H)\le n\sum_k f_k\log f_k\tag{9.93}$$
(Added step: $\sum n_k\log p_k\le\sum n_k\log f_k$.) The right side depends only on the sample, so how close the bound is to equality measures the fit. In decibels:
$$\psi_B\equiv10\sum_{k=1}^m n_k\log_{10}\!\Big(\frac{n_k}{np_k}\Big)\tag{9.94}$$
(p. 297; the page refers to these equations as "(9.88)", see Reading notes).

**Meaning of ψ_B.** Take two hypotheses H={p_k}, H′={p′_k} in $B_m$ with values ψ_B, ψ′_B. Then
$$e(H|x_1\dots x_n)=e(H|I)+10\log_{10}\!\Big[\frac{p(x_1\dots x_n|H)}{p(x_1\dots x_n|H')}\Big]=e(H|I)+\psi'_B-\psi_B\tag{9.95}$$
Some H′ in $B_m$ has $p'_k=n_k/n$, so ψ′_B=0. Result: given H and D, for any ψ with 0≤ψ≤ψ_B there is an H′ in $B_m$ supported relative to H by ψ dB. No H′ in $B_m$ is supported by more than ψ_B dB (p. 298). So ψ_B names no alternative yet is the exact goodness-of-fit measure relative to $B_m$. Jaynes says the ψ-test is the quantitative version of what intuition does unconsciously; he recalls (§5.4) that natural selection would tend to evolve creatures that reason in a Bayesian way (p. 298).

**Entropy reading.** Rewrite
$$\psi_B=10n\sum_k f_k\log_{10}(f_k/p_k)\tag{9.96}$$
Jaynes calls $-\psi_B/n$ the entropy per symbol $H(f;p)$ of the observed message distribution $\{f_k\}$ relative to the expected $\{p_k\}$. He concludes that entropy, or a monotonic function of it, appears automatically for anyone using Bayes' theorem for hypothesis testing, independently of Shannon (p. 298).

*Intuition note.* Take the best-fitting hypothesis with probabilities equal to the observed frequencies. ψ_B is how many decibels better than H it explains the data. If ψ_B is small, no tidy alternative of that kind does much better. Per trial, ψ_B/(10n)=Σ f_k log₁₀(f_k/p_k) by (9.96); Jaynes calls −ψ_B/n an entropy per symbol (p. 298).

**Pearson's χ².** Condition A: $|n_k-np_k|$ grows only like √n. Under A, using $\log x=(x-1)-(x-1)^2/2+\cdots$,
$$\sum_k n_k\log\!\Big[\frac{n_k}{np_k}\Big]=\frac12\sum_k\frac{(n_k-np_k)^2}{np_k}+O\!\Big(\frac1{\sqrt n}\Big)\tag{9.97}$$
with the remainder tending to zero provided the sample satisfies A. Define
$$\chi^2\equiv\sum_k\frac{(n_k-np_k)^2}{np_k}=n\sum_k\frac{(f_k-p_k)^2}{p_k}\tag{9.98}$$
Then
$$\psi_B=[10\log_{10}e]\times\tfrac12\chi^2+O(1/\sqrt n)=4.343\,\chi^2+O(1/\sqrt n)\tag{9.99}$$
as printed (see Reading notes on the constant). χ²≥0 with equality iff the observed frequencies equal the expected ones; but ψ_B shares these qualitative properties (p. 299).

**Why χ²?** In the orthodox textbooks he scanned, Jaynes finds χ² usually introduced as a deus ex machina, with no connected theoretical argument for it. He quotes **Cramér (1946)**, who says it fits the general principle of least squares to use $\sum c_i(n_i/n-p_i)^2$, with coefficients $c_i$ chosen more or less arbitrarily. Pearson showed $c_i=n/p_i$ "particularly simple properties" (p. 299). Jaynes' comment: χ² is adopted for simple properties, not shown good by any criterion (p. 299). He proposes testing the two criteria by **magnification** (borrowed from Galileo, Jaynes 1976): find an extreme case where a small quantitative difference becomes visible to common sense (p. 299).

### 9.12 Comparison of psi and chi-squared (p. 300–302)
**Setup.** A coin has three outcomes: heads, tails, edge. Mr A assigns $p=(0.499,0.499,0.002)$. Mr B on Mars knows only "three outcomes" and assigns $p'=(1/3,1/3,1/3)$. In 29 tosses we see $(n_1,n_2,n_3)=(14,14,1)$ (p. 300).

**ψ criterion:**
$$\psi_A=10\Big[28\log_{10}\frac{14}{29\times0.499}+\log_{10}\frac{1}{29\times0.002}\Big]=8.34\ \text{dB}$$
$$\psi_B=10\Big[28\log_{10}\frac{14\times3}{29}+\log_{10}\frac{3}{29}\Big]=35.19\ \text{dB}\tag{9.100}$$
Mr B learns that:
- (a) some hypothesis is 35.2 dB better than his (odds over 3 300:1);
- (b) A's hypothesis is 26.8 dB better than his, and within about 8 dB of the best in $B_3$.

This matches common sense (p. 300).

**χ² criterion:**
$$\chi_A^2=2\frac{(14-29\times0.499)^2}{29\times0.499}+\frac{(1-29\times0.002)^2}{29\times0.002}=15.33,$$
$$\chi_B^2=2\frac{(14-29\times0.333)^2}{29\times0.333}+\frac{(1-29\times0.333)^2}{29\times0.333}=11.66\tag{9.101}$$
So a Martian trusting χ² would claim his hypothesis is slightly preferable (p. 300).

**Diagnosis (p. 301).** Jaynes says the ψ criterion is exactly derivable, so any approximation to it must show an inconsistency or a violation of common sense in special cases. Under A, np₁=14.471, so 14 is the nearest possible integer. The trouble is the last term of χ²_A, the single edge landing. Under A, the probability of at least one edge in 29 tosses is $1-0.998^{29}=1/17.73$, mildly surprising (like fog on one day in 18). Yet that term contributes 15.30 of the 15.33. The $1/p_i$ weight makes χ² focus on extremely unlikely outcomes, so slight discrepancies there grotesquely over-penalise the hypothesis. ψ has this effect too but only inside a logarithm, so much more mildly (p. 301).

**Second data set (14, 15, 0):**
$$\psi_A=0.30\ \text{dB},\ \chi_A^2=0.0925;\qquad\psi_B=51.2\ \text{dB},\ \chi_B^2=14.55\tag{9.102}$$
The largest relative change is in χ²_A. Both criteria now say A is far better (p. 301).

**Professor Q (ESP) story and Moral (p. 301–302).** Q plays card games, erases the disappointing tapes, and records one run where an extremely improbable event occurs. χ² is enormous, and the null hypothesis is "decisively rejected" by the accepted test, though the data came from selection. Moral: for moderately large probabilities that agree moderately with observation, ψ and χ² differ little. For testing hypotheses with extremely unlikely events, use ψ (p. 302).

*Intuition note.* Dividing by p_k in χ² makes a rare event count enormously, even when its observed count is off by one. ψ only takes a log of the ratio, so it is gentle.

### 9.13 The chi-squared test (p. 302–304)
**Procedure (orthodox reasoning).** A null hypothesis H, with no alternative stated, predicts $n_k=nf_k$ (p. 302).
- Small categories are grouped so each $n_k\ge$ about 5. Example: m=6, observed {6,11,14,7,3,2}; the last two are grouped, giving {6,11,14,7,5} with $p_5+p_6$ (p. 302).
- Compute
$$\chi^2_{\rm obs}=\sum_{k=1}^m\frac{(n_k-np_k)^2}{np_k}\tag{9.103}$$
- Reject H if the tail probability $P(\chi^2_{\rm obs})$ of a deviation at least that large is small, usually below 5% (p. 302).

**Distribution.** The exact χ² distribution is discrete, with at most $(n+m-1)!/(n!(m-1)!)$ values (if the $p_k$ are all different and incommensurable). For large n it is approximated by the universal law
$$g(\chi^2)\,d(\chi^2)=\frac{\chi^{f-2}}{2^{f/2}(f/2-1)!}\exp\!\Big\{-\tfrac12\chi^2\Big\}d(\chi^2)\tag{9.104}$$
Here f = degrees of freedom: f=m−1 if H has no free parameters, f=m−1−r if r parameters are estimated from the data (p. 303). Footnote 5: the young Fisher saw the need for this correction and Pearson did not; this began their first fierce controversy (Ch. 16). Mean and variance are ⟨χ²⟩=f and var(χ²)=2f, so
$$(\chi^2)_{\rm est}=f\pm\sqrt{2f}\tag{9.105}$$
The reason usually given for grouping is that (9.104) would otherwise be a bad approximation. But grouping discards information, and with exact ψ there is never a reason to group (p. 303).

**P-values.** With $q\equiv\tfrac12\chi^2$, $k\equiv(f-2)/2$:
$$P(\chi^2_{\rm obs})=\int_{\chi^2_{\rm obs}}^\infty d(\chi^2)\,g(\chi^2)=\int_{q_{\rm obs}}^\infty dq\,\frac{q^k}{k!}e^{-q}\tag{9.106}$$
Jaynes criticises reporting only reject/not-reject at a fixed level. Reporting the P-value, where H is just barely rejected, is "a major improvement". But standard tables list only widely spaced levels, so interpolation is impossible (p. 303–304). Writing $q=q_0+t$ (the page uses k for both the fixed exponent and the sum index; read the exponent as $m=k$):
$$P=\int_0^\infty dt\frac{(q_0+t)^k}{k!}e^{-(q_0+t)}=\frac1{k!}\sum_{j=0}^m\binom mj\int_0^\infty dt\,q_0^{\,j}t^{m-j}e^{-(q_0+t)}=\sum_{j=0}^m e^{-q_0}\frac{q_0^{\,j}}{j!}\tag{9.107}$$
(last step: added step, using $\int_0^\infty t^{m-j}e^{-t}dt=(m-j)!$). This is a cumulative Poisson sum, easily computed (p. 304).

**Bayesian view.** ψ needs no tables and its numerical value describes the evidence. From the Bayesian view, rejecting a hypothesis is useless unless a definite better alternative exists. That depends on ψ, the alternative's prior and the costs of errors, so it is a decision-theory problem (p. 304). In practice the conclusions may be similar. As f grows the orthodox statistician accepts χ² roughly ∝ f (9.105). The Bayesian must accept proportionally higher ψ because the number of reasonable alternatives grows exponentially with f, lowering each one's prior. Jaynes sees an enormous philosophical difference but not necessarily a big difference in where the limit lies (p. 304). He refers to Lancaster (1969) and Box & Tiao (1973) (p. 304).

### 9.14 Generalization (p. 304–305)
χ² measures fit only relative to alternatives in the same Bernoulli class; until this is recognised, Jaynes says, one does not really know what the χ²-test is testing (p. 305). For any well-defined class C, write Bayes' theorem for two hypotheses H₁, H₂ in C as
$$e(H_1|DI)-e(H_2|DI)=\psi_2-\psi_1\tag{9.108}$$
(as printed; no prior terms shown). Here ψ_i depends only on the data and H_i, is non-negative over C, and vanishes for some H_i in C. Choose H₂ with ψ₂=0; then ψ₁ is the maximum support any hypothesis in C can get relative to H₁ from D (p. 305). Jaynes adds:
- Jaynes says Chapter 17 will show that the format of such tests can be replaced by parameter estimation, as Laplace already did.
- Anscombe (1963) called the need for a class of alternatives a weakness; Jaynes calls it a merit.
- Jaynes suggests that where an orthodox method is usable, Bayesian inference supplies its missing theoretical basis and usually improves it (p. 305).

### 9.15 Halley's mortality table (p. 305–310)
**Background.** London's weekly Bills of Mortality (intermittent from 1591, continuous from 1604) were compiled by the Searchers (p. 305–306). John Graunt (1662), a shopkeeper, aggregated the 1632 data and noted that large birth samples have slightly more boys than girls. Charles II had him admitted to the Royal Society (p. 306). Footnote 6: Jaynes draws a parallel with credit-card companies' unused data.

**Halley's data (p. 306).** Edmund Halley (1693) found London and Dublin data unusable: age at death was often missing and in-migration biased them. So he used 5 years (1687–91) from Breslau, which had a stable population. Jaynes calls the result surely valid for Breslau and presumably not badly in error for England (p. 306).

**Tables.** Halley gave d(x), the annual deaths (total/5) at each age (Table 9.1), and n(x), the population by age (Table 9.2) (p. 307–308). The first table omits ages under 7 and the second omits ages above 84, the regions of strong curvature (p. 308). He does not describe his procedure. Jaynes infers the following (p. 308):
- Under a stable population, n(25)−n(26)=d(25).
- So presumably n(0)=1238 (births per year) and $n(x)=n(x-1)-\bar d(x)$ with $\bar d$ the smoothed d.
- The total population is $\sum_x n(x)=34\,000$.
- The later entries fit this; the first six entries (0<x<7) do not, and no conjecture was found (p. 308).

**Our reading of the tables (Jaynes, p. 309).**
- "Age current" is the age in the current year of life. "Eight years current" means 7<x≤8. Jaynes therefore shifts ages down one year in Fig. 9.1: Halley's (25, 567) becomes n(24)=567, persons aged in (24,25).
- Beyond 84 he extrapolates, using the 19 deaths in (85,100) (three at age current 100) and Halley's estimate of 107 people in that range.
- Features of the graph: an appalling infant mortality; Halley states that 56% survive to age 6 (disagreeing with Table 9.2) and 50% to 17 (agreeing); and the graph is almost perfectly linear from 35 to 80.

**Use as probability/odds.** The probability that a person of age y lives to age z is reasonably p=n(z)/n(y). Halley speaks of "odds", exactly as we do: $O(m|y)=n(y+m)/[n(y)-n(y+m)]=p/(1-p)$ (p. 309). Further complaints: sexes pooled, raw data not shown. Jaynes' proposed first commandment for publishing data analyses: reveal the full original data unprocessed, since future readers will bring different prior knowledge (p. 309–310).

*Intuition note.* Counting survivors gives a reasonable probability: the fraction still alive at age z among those alive at age y. Halley's odds are the same fraction written as a ratio.

### 9.16 Comments (p. 310–313)
**9.16.1 The irrationalists (p. 310–311).**
- Jaynes lists Hume to Popper as having tried to deny the possibility of induction. D. Stove calls them "the irrationalists" (p. 310).
- Popper holds that theories can never attain high probability. Jaynes replies that this presupposes testing against an infinite number of alternatives. Bayesian inference gives plausibility relative to a definite set of alternatives. Within that set a hypothesis can reach very high or very low probability. Over "all conceivable theories" the probability is undefined (p. 310).
- **Objection:** without a high absolute probability there is no proof that induction will be right. **Jaynes:** this misses the point. Induction tells us which predictions are most strongly indicated by the information put into the calculation. It is legitimate to induct from hypotheses we do not believe, to learn their consequences (p. 310–311).
- Confirmed predictions raise confidence, and eventually such hypotheses are called "physical laws". Failed predictions are where induction most helps, since we learn the hypotheses are wrong or incomplete, as Jeffreys explained (p. 311).
- Examples: pandemic influenza from China (the cause appears to have been traced to ducks and pigs raised together; pigs can pass modified duck viruses to humans); the gooseberry as host of white pine blister rust; Pasteur's work; modern gene hunting. Jaynes says all were found by qualitative plausible reasoning in Pólya's format, and that Bayesian analysis is the unique quantitative expression of that reasoning format. It does not guarantee conclusions, but direct tests can confirm or refute them (p. 311).

**9.16.2 Superstitions (p. 312–313).**
- Jaynes says the untrained mind uses mostly unjustified induction: it reads correlation as causation and predicts recurrence, with no demand for a physical mechanism (p. 312).
- He criticises nature documentaries that read purpose into mutations. The Darwinian order is mutation first, then the animal finds a niche where it survives. We see only the successes (p. 312). Footnote 10 notes the Burgess shale as an exception where non-surviving forms were found.
- Counter-example: Andean woodpeckers where there are no trees. Arrivals in a niche are seldom perfectly adapted; stress eliminates bad mutations faster, so selection acts faster (p. 312–313).

## Toy example (ours, not from the text)
Coin test, m=2 outcomes. H: fair, $p=(0.5,0.5)$. Data: n=10 tosses, $n_1=8$ heads, $n_2=2$ tails.

1. $np_k=5$ for each k.
2. ψ_B from (9.94):
 - $8\log_{10}(8/5)=8\times0.20412=1.6330$
 - $2\log_{10}(2/5)=2\times(-0.39794)=-0.7959$
 - Sum $=0.8371$; ×10 gives ψ_B ≈ 8.37 dB.
3. Check with the best alternative $H'=(0.8,0.2)$ (frequencies as probabilities): the likelihood ratio is $\dfrac{0.8^8\,0.2^2}{0.5^{10}}=\dfrac{0.016777\times0.04}{0.00097656}=6.87$, and $10\log_{10}6.87=8.37$ dB. This is the maximum support in $B_2$.
4. A weaker alternative $H''=(0.6,0.4)$: $\psi_{H''}=10[8\log_{10}(8/6)+2\log_{10}(2/4)]=10[0.9995-0.6021]=3.97$, so by (9.95) H″ is supported relative to H by $8.37-3.97=4.40$ dB. Direct check: $0.6^8\,0.4^2/0.5^{10}=2.75$, and $10\log_{10}2.75=4.40$.

So "ψ_B = 8.37 dB" means: some hypothesis in the class does 8.37 dB (odds ≈ 6.9:1) better than "fair", and none does more.

## Concepts
- [[probability-vs-frequency]] (new) — probability is an assigned state of knowledge; frequency is a measured fact; they are equal only for particular knowledge states (p. 292)
- [[frequentist-vs-bayesian-inference]] — Jaynes' stance: probability as logic; frequency links arise as theorems (p. 293)
- [[bayes-theorem]] — written as decibel evidence update (9.79), always relative to a named alternative (p. 294)
- [[likelihood]] — p(D|H); the likelihood ratio sets the evidence shift between two hypotheses (p. 294)
- [[probability-as-extended-logic]] — the view Jaynes defends against Fisher, Neyman and others (p. 293)
- [[implied-alternatives]] (new) — any fit judgment is relative to a class of alternatives; ψ∞ bounds support by any alternative (p. 296)
- [[sure-thing-hypothesis]] (new) — post-hoc H_S with p(D|H_S)=1; supported by exactly ψ∞ dB, but with minuscule prior (p. 296)
- [[bernoulli-class]] (new) — hypotheses with independent, stationary trial probabilities $\{p_k\}$ (p. 297)
- [[psi-test]] (new) — ψ_B, the exact max decibel support for any alternative in the Bernoulli class (p. 297–298)
- [[relative-entropy-kl]] — ψ_B/(10n)=Σ f log₁₀(f/p); Jaynes calls −ψ_B/n an "entropy per symbol" relative to the expected distribution (p. 298)
- [[chi-squared-test]] (new) — Pearson's Σ(n−np)²/np with tail-area rejection; is nearly proportional to ψ_B when condition A holds (p. 298–299, 302–303)
- [[p-value]] (new) — tail probability P(χ²_obs); better reported than a fixed-level verdict (p. 303–304)
- [[maximum-entropy-principle]] — in §9.9, the Gibbs distribution solves the constrained extremum; unique λ from (9.78) (p. 292)
- [[exponential-family-gibbs]] — "Gibbs canonical ensemble"; the function Z (from (9.75), not shown here) and $\overline G=-\partial\log Z/\partial\lambda$ (p. 292)
- [[magnification-technique]] (new) — find an extreme case that exposes a small quantitative difference between methods (p. 299)
- [[induction-as-plausible-reasoning]] (new) — induction gives the predictions most strongly indicated by the information, not guaranteed truths (p. 310–311)

## Canonical instances
- [[poisson-particle-counter]] — Poisson counts with binomial frequency of c=12; Bernoulli's probability–frequency link (p. 294–295)
- [[honest-die-10000]] — ψ∞=77 815 dB; sure-thing hypothesis problem (p. 296)
- [[thick-coin-three-outcomes]] — ψ and χ² disagree on A vs the Martian's hypothesis (p. 300–301)
- [[professor-q-esp]] — χ² "decisively rejects" the null after selecting a lucky run (p. 301–302)
- [[halley-mortality-table]] — frequencies used as probabilities and odds from Breslau data (p. 305–309)
- [[influenza-duck-pig]] — induction identifying a causal chain (p. 311)

## Bridges (candidates)
- [same-math] ψ_B = 10n Σ f_k log₁₀(f_k/p_k) ↔ information-theory: n × KL divergence D(f‖p) in log₁₀ units, scaled by 10 — literally the same sum.
- [same-math] χ² as the second-order expansion (9.97) ↔ information-theory: the local quadratic (Fisher-information) form of KL divergence.
- [same-math] §9.9 Gibbs distribution with $\overline G=-\partial\log Z/\partial\lambda$ ↔ information-theory: exponential family from MaxEnt under an expectation constraint.
- [structural-analogy] Class Ω of alternatives in the ψ-test ↔ bayesian: model-class choice behind Bayesian Occam's razor; "undefined over all conceivable theories".
- [structural-analogy] Reporting P-values/ψ rather than a reject/accept verdict ↔ bayesian: reporting full posterior evidence and leaving the decision to decision theory.

## Questions this raises
- How should one choose the class of alternatives Ω when no natural class exists, and how sensitive is ψ to that choice?
- Can the "number of alternatives grows exponentially with f" argument (p. 304) be made quantitative so that ψ and χ² critical values can be compared?
- Chapter 17 is said to replace such tests by parameter estimation: what extra information does that give?
- With modern computing and Halley-type raw data, how would one estimate a mortality table with full uncertainty (Ex. 9.3)?

## Exercises worth doing
- Ex. 9.3 (p. 310) — reprocess Halley-type raw data with modern probability theory and compare conclusions — difficulty: hard

## Reading notes
- **Where this part starts and ends.** It begins at printed p. 292, in the last lines of §9.9 (the Gibbs ensemble derivation); the previous part is not given, so (9.75), which defines Z, is referenced but not shown. It ends at the end of p. 313, in the middle of §9.16.2; the next page was not given.
- **Page offset.** Printed = pdf − 30.
- **Equation-number misprints.** Around (9.93)–(9.94), the text says "the right-hand side of (9.88)" and "express (9.88) in decibel units". The image shows "(9.88)" there; the inequality is (9.93) and the decibel form is (9.94).
- **(9.84).** The page shows $np+2n(n-1)p^2+n(n-1)(n-2)p^3$ for ⟨r³⟩. Applying $p\,d/dp$ three times gives the middle coefficient 3, not 2. I copied the printed form and flagged it.
- **(9.99).** The printed middle form $[10\log_{10}e]\times\frac12\chi^2$ equals about 2.171χ², but the printed value is "4.343χ²". The two are inconsistent as shown on the page; 4.343 would match the unhalved version.
- **(9.107).** The page uses k both for the fixed exponent and for the sum index. I read the exponent as m (with $m\equiv k=(f-2)/2$) and gave the sum index j, which is my notation.
- **(9.108).** The printed form has no prior terms $e(H_i|I)$; I reproduced it as printed.
- **Tables 9.1–9.2 and Fig. 9.1** are not reproduced here beyond the figures quoted in the text. Table 9.1 is garbled in the text layer; its image is readable.
- The fog probability appears as "0.99829" in the text layer but as $0.998^{29}$ in the image.
- Footnotes 5, 6 and 10 are summarised above; footnotes 7, 8 and 9 are not.
