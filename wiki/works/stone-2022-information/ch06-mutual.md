---
id: stone-2022-information/ch06-mutual
work: stone-2022-information
unit: "6 Mutual Information: Continuous"
pages: 135-152
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Mutual Information: Continuous

## L0 — One line
For continuous channel input X and output Y, mutual information is the average reduction in uncertainty about one variable from observing the other, and it can be written several equivalent ways without any infinities.

## L1 — The gist (≤ 120 words)
How much does the output Y of a noisy channel tell us about the input X when both are continuous? Mutual information: the average reduction in uncertainty (entropy) about X once Y is seen. It equals H(X)+H(Y)−H(X,Y) = H(Y)−H(Y|X), where H(Y|X), the conditional entropy, is the uncertainty left in Y once X is known. It is symmetric, and its definition contains no infinities, unlike the entropy of a continuous variable. Within limits, it is unchanged by reversible transformations of X or Y. It also equals the Kullback–Leibler divergence (a measure of difference between two distributions) between the joint distribution and the product of the marginals (the separate distributions of X and Y).

**Prerequisites:** discrete entropy and mutual information; probability density; integrals; product rule p(x,y)=p(y|x)p(x); log rules.

## L2 — Key ideas
- **Mutual information (MI)** is the logarithm of the number of input values that can be reliably told apart from the output. Noise limits that number, and Shannon's upper bound on it gives the channel capacity, C = log m_max (p. 135–136).
- **Marginalisation** (integrating out one variable) gives the marginal distributions of a joint distribution. If X and Y are independent, the joint distribution is the product of the marginals and MI is 0 (pp. 137–140).
- **Conditional entropy** H(Y|X) is the average, over X, of the entropy of each slice p(Y|x). Usually H(X|Y) ≠ H(Y|X) (pp. 143–145).
- MI has three equivalent forms: H(X)−H(X|Y), H(Y)−H(Y|X), and H(X)+H(Y)−H(X,Y) (pp. 146–148).
- The joint entropy splits into three disjoint parts: I(X,Y), H(X|Y) and H(Y|X). This gives the **chain rule** for entropy, e.g. H(X,Y)=H(X)+H(Y|X) (pp. 149–150).
- The infinite constant in continuous entropy cancels in MI. On average MI cannot be negative (pp. 146–147).
- Within formally defined limits, MI is invariant under invertible (reversible) transformations of X and Y, so it can measure association strength whatever the form of the relationship (pp. 150–151).
- MI is the KL divergence between the joint distribution and the product of the marginals, D_KL(joint ‖ product). It is also the average KL divergence between the posterior p(X|y) and the prior p(X), written D_KL(p(X|y)‖p(X)) (pp. 151–152).

## L3 — Walkthrough

### 6.1 Introduction (pp. 135–136)
- Figure 6.1: a signal s is encoded as x = g(s), noise η is added, and the output is y = x + η (p. 136).
- MI for continuous variables is defined as for discrete ones (p. 135):
$$I(X,Y)=H(X)+H(Y)-H(X,Y)\ \text{bits}\tag{6.1}$$
- MI is the logarithm of the number m of input values that can be reliably discriminated from the outputs (I = log m). Because MI is symmetric, m also counts output values discriminable from the inputs (pp. 135–136).
- Shannon proved m has an upper bound m_max, and C = log m_max is the channel capacity (p. 136).
- MI is sensitive to the strength of association but "blind" to its nature (linear or not) (p. 136). Section 6.5 returns to this.
- Eq. 6.1 will be derived from a formal definition. Most of the chapter develops the conditional-entropy form (p. 136).

**Intuition note.** Noise blurs neighbouring inputs together. MI counts, on a log scale, how many inputs stay distinguishable despite the blur.

### 6.2 Joint distributions (pp. 137–141)
- If X and Y are correlated, knowing X tells us something about Y, and vice versa. How much depends on the size of the correlation (p. 137).
- If they are independent, knowing X tells nothing about Y (Figs 6.3, 6.5) (p. 137).
- The joint density is p(x,y). The author notes that ignoring the distinction between density and probability makes the notation less rigorous but more readable (p. 137).
- Independent case: the joint distribution factorises, i.e. is the outer product of the marginals (p. 137):
$$p(X,Y)=p(X)\,p(Y)\tag{6.2}$$
- Marginalisation by integration (p. 138):
$$p(X)=\int_{y=-\infty}^{\infty}p(x,y)\,dy\tag{6.3}$$
$$p(Y)=\int_{x=-\infty}^{\infty}p(x,y)\,dx\tag{6.4}$$
- Figure 6.2 shows correlated Gaussian variables with σ_Y = 1, σ_X = 2 and ρ = 0.8 (p. 138).
- The joint differential entropy is (p. 138):
$$H_{dif}(X,Y)=\int_{x}\int_{y}p(x,y)\log\frac{1}{p(x,y)}\,dy\,dx\tag{6.5}$$
$$=\mathrm{E}\!\left[\log\frac{1}{p(x,y)}\right]\ \text{bits}\tag{6.6}$$
- The limits and the subscript "dif" are dropped from now on. The infinities problem of Section 5.3 also applies to joint distributions and is "solved" by ignoring the infinities. "Joint entropy" means joint differential entropy (p. 139).
- H(X,Y) can be seen as a measure of overall variability, or dispersion, of p(X,Y) (p. 139).
- If X and Y are independent, the joint entropy equals the sum of the marginal entropies (p. 139):
$$H(X)+H(Y)=\int_x\!\int_y p(x)p(y)\log\frac{1}{p(x)p(y)}\,dy\,dx\tag{6.7}$$
$$=\int_x p(x)\log\frac1{p(x)}dx+\int_y p(y)\log\frac1{p(y)}dy\tag{6.8}$$
$$=\mathrm{E}\!\left[\log\tfrac1{p(x)}\right]+\mathrm{E}\!\left[\log\tfrac1{p(y)}\right]\tag{6.9}$$
- Hence, for independent X and Y (p. 140):
$$H(X)+H(Y)-H(X,Y)=0\ \text{bits}\tag{6.10}$$
- MI for continuous variables (p. 140):
$$I(X,Y)=\int_x\!\int_y p(x,y)\log\frac{p(x,y)}{p(x)p(y)}\,dx\,dy\tag{6.11}$$
- Rewritten (p. 140):
$$I(X,Y)=\int_x p(x)\log\frac1{p(x)}dx+\int_y p(y)\log\frac1{p(y)}dy-\int_x\!\int_y p(x,y)\log\frac1{p(x,y)}dy\,dx\tag{6.12}$$
$$=\mathrm{E}\!\left[\log\tfrac1{p(x)}\right]+\mathrm{E}\!\left[\log\tfrac1{p(y)}\right]-\mathrm{E}\!\left[\log\tfrac1{p(x,y)}\right]\tag{6.13}$$
$$I(X,Y)=H(X)+H(Y)-H(X,Y)\ \text{bits}\tag{6.14}$$
- By analogy with the discrete case, I(X,Y) is the average information each input conveys about each output value, and (by symmetry) each output about each input. The author calls this form arguably less accessible than the conditional-entropy forms (p. 141).

### 6.3 Conditional distributions and entropy (pp. 141–145)
- A slice of the joint density at X = x₁ is p(x₁,Y). The product rule gives (p. 142):
$$p(x_1,Y)=p(Y|x_1)\,p(x_1)\tag{6.15}$$
$$p(Y|x_1)=p(x_1,Y)/p(x_1)\tag{6.16}$$
$$p(x_1)=\int_y p(x_1,y)\,dy\tag{6.17}$$
- So p(Y|x₁) is the slice rescaled by 1/p(x₁), which makes it have unit area. For our purposes the value of p(x₁) is immaterial: it simply serves as this scaling factor (p. 143). Slices at Y = y₁ give p(X|y₁) in the same way (p. 143).
- H(Y|X) is the average entropy of all slices at fixed X, averaged over X. H(X|Y) is defined likewise over slices at fixed Y (pp. 143–144).
- Derivation (p. 144):
$$H(Y|x_1)=\int_y p(y|x_1)\log\frac1{p(y|x_1)}dy\tag{6.18}$$
$$H(Y|X)=\int_x p(x)H(Y|x)\,dx\tag{6.19}$$
$$H(Y|X)=\int_x p(x)\Big[\int_y p(y|x)\log\frac1{p(y|x)}dy\Big]dx\tag{6.20}$$
- Using p(y|x)p(x) = p(x,y):
$$H(Y|X)=\int_y\!\int_x p(x,y)\log\frac1{p(y|x)}dx\,dy\tag{6.21}$$
$$=\mathrm{E}\!\left[\log\tfrac1{p(y|x)}\right]\ \text{bits}\tag{6.22}$$
- The expectation is over all X and Y. The equivocation (the other conditional entropy) is (p. 144):
$$H(X|Y)=\int_y\!\int_x p(x,y)\log\frac1{p(x|y)}dx\,dy\ \text{bits}\tag{6.23}$$
- Usually H(X|Y) ≠ H(Y|X). In Fig. 6.2 the conditionals p(Y|X) have large variance (Fig. 6.6) and p(X|Y) small variance (Fig. 6.7). These variances are reflected in the two conditional entropies (p. 145).

**Intuition note.** Cut the joint "hill" along one variable. Each slice has its own spread. Conditional entropy is the average spread of the slices, so it measures the uncertainty left after the other variable is known.

### 6.4 Mutual information and conditional entropy (pp. 145–150)
- Goal: show that I(X,Y) = H(Y) − H(Y|X) (Eq. 6.24) (p. 145).
- Start from Eq. 6.25, which is the same as 6.11:
$$I(X,Y)=\int_y\!\int_x p(x,y)\log\frac{p(x,y)}{p(x)p(y)}dx\,dy\tag{6.25}$$
- Substitute p(x,y) = p(y|x)p(x) (p. 145):
$$I(X,Y)=\int_y\!\int_x p(x,y)\log\frac{p(y|x)}{p(y)}dx\,dy\tag{6.26}$$
$$=\int_y\!\int_x p(x,y)\log\frac1{p(y)}dx\,dy-\int_y\!\int_x p(x,y)\log\frac1{p(y|x)}dx\,dy\tag{6.27}$$
- The second term is H(Y|X) by Eq. 6.21. The first is H(Y) (p. 145):
$$\int_y\!\int_x p(x,y)\log\frac1{p(y)}dx\,dy=\int_y p(y)\log\frac1{p(y)}dy=H(Y)\tag{6.28}$$
$$I(X,Y)=H(Y)-H(Y|X)\ \text{bits}\tag{6.29}$$
- Swapping X and Y, by symmetry (p. 146):
$$I(X,Y)=H(X)-H(X|Y)\ \text{bits}\tag{6.30}$$
- **No infinity.** H(X) and H(X|Y) both contain the infinite constant of Eq. 5.12. It has the same value in both and cancels in the subtraction. So the definitions of MI, discrete or continuous, contain no infinities (p. 146).
- **Information Y gives about X.** MI is the uncertainty about X before Y is observed, H(X), minus the uncertainty after, H(X|Y) (Eq. 6.31). It is the amount of output entropy exclusively related to the input entropy, and so not related to the noise in the input (pp. 146–147).
- **Non-negativity.** On average, observing an output reduces uncertainty about the input, though certain outputs may increase it. It can be shown (Reza, 1961) that
$$H(X|Y)\le H(X)\ \text{bits}\tag{6.32}$$
with equality only if X and Y are independent. By Eq. 6.30, MI is positive unless X and Y are independent, when it is zero (p. 147).
- **Information X gives about Y.** I(X,Y) = H(Y) − H(Y|X) (Eq. 6.33). It is the amount of input entropy exclusively related to the output entropy, and so not related to the noise in the output (p. 148). In Fig. 6.8, the output noise η has H(η) = H(Y|X) (p. 147).
- Three expressions (p. 148):
$$I(X,Y)=H(X)-H(X|Y)\tag{6.34}$$
$$I(X,Y)=H(Y)-H(Y|X)\tag{6.35}$$
$$I(X,Y)=H(X)+H(Y)-H(X,Y)\tag{6.36}$$
- "A little algebra" gives a fourth (p. 148):
$$I(X,Y)=H(X,Y)-[H(X|Y)+H(Y|X)]\tag{6.37}$$
- (added step) Adding 6.34 and 6.35: $2I=H(X)+H(Y)-H(X|Y)-H(Y|X)$. By 6.36, $H(X)+H(Y)=I+H(X,Y)$. So $2I=I+H(X,Y)-[H(X|Y)+H(Y|X)]$, which gives 6.37.
- Rearranged (p. 149):
$$H(X,Y)=I(X,Y)+H(X|Y)+H(Y|X)\tag{6.38}$$
- So H(X,Y) is an "entropy container" with three disjoint parts (Figs 6.9, 6.10) (p. 149):
  1. H(X|Y), due to noise in X: entropy in X not determined by Y.
  2. H(Y|X), due to noise in Y: entropy in Y not determined by X.
  3. I(X,Y), the entropy shared by X and Y, resulting from their co-dependence.
- Eqs 6.34–6.36 imply (p. 149):
$$H(X|Y)=H(X,Y)-H(Y)\tag{6.39}$$
$$H(Y|X)=H(X,Y)-H(X)\tag{6.40}$$
- These in turn give the chain rule for entropy (p. 150):
$$H(X,Y)=H(X)+H(Y|X)\tag{6.41}$$
$$H(X,Y)=H(Y)+H(X|Y)\tag{6.42}$$

**Intuition note.** Think of two overlapping circles, one for H(X) and one for H(Y). The overlap is MI. The non-overlapping crescents are the noise parts. MI is what is left of the total once the noise parts are removed.

### 6.5 Mutual information is invariant (pp. 150–151)
- Within formally defined limits, MI between two variables is invariant under transformations of them (p. 150). Invariant means the amount of MI is unaffected by the transformation (p. 150).
- With $X'=f(X)$ (6.43) and $Y'=g(Y)$ (6.44), $I(X',Y')=I(X,Y)$ provided f and g are invertible, i.e. X is recoverable from X′ and Y from Y′ (p. 150).
- Example: $X'=\log X$ is recoverable by $X=2^{X'}$. A map to a constant $X'=k$ is not invertible, because X cannot be recovered from X′ (p. 150).
- This ensures that no matter how complex the relationship between X and Y appears, MI measures the precise strength of association in bits (p. 150).
- Example: a study finds I(X,Y) = 2 bits between diabetes prevalence X and sugar intake Y in grams. Measuring sugar as Y′ = Y² (or log Y) still gives 2 bits (p. 151).
- The author says no such claim can be made for conventional measures such as correlation (see Section 7.6) (p. 151).

**Intuition note.** Re-scaling or re-labelling a variable without losing information does not change what it can tell you about the other variable. So, within the formally defined limits, MI is unchanged by such re-expression of a variable.

### 6.6 Kullback–Leibler divergence and Bayes (pp. 151–152)
- KL divergence (relative entropy) measures the difference between two distributions p(X) and q(X) of the same variable (p. 151):
$$D_{KL}(p(X)\|q(X))=\int_x p(x)\log\frac{p(x)}{q(x)}dx\tag{6.45}$$
- It is not a true distance because usually (p. 151)
$$D_{KL}(p(X)\|q(X))\neq D_{KL}(q(X)\|p(X)).\tag{6.46}$$
- D_KL is positive unless p = q, when it is zero (p. 151).
- With the joint p(X,Y) and the product of marginals (p. 151):
$$D_{KL}(p(X,Y)\|[p(X)p(Y)])=\int_x\!\int_y p(x,y)\log\frac{p(x,y)}{p(x)p(y)}dy\,dx\tag{6.47}$$
This is MI by Eq. 6.25. So MI is the KL divergence between the joint distribution and the outer product of the marginals (p. 151).
- **Bayes' rule.** Using p(x,y) = p(x|y)p(y) (p. 152):
$$I(X,Y)=\int_y p(y)\int_x p(x|y)\log\frac{p(x|y)}{p(x)}dx\,dy\tag{6.48}$$
- The inner integral is the KL divergence between p(X|y), the posterior (distribution after observing y), and p(X), the prior (distribution before observing) (p. 152):
$$D_{KL}(p(X|y)\|p(X))=\int_x p(x|y)\log\frac{p(x|y)}{p(x)}dx\tag{6.49}$$
$$I(X,Y)=\int_y p(y)\,D_{KL}(p(X|y)\|p(X))\,dy\tag{6.50}$$
$$I(X,Y)=\mathrm{E}_y\big[D_{KL}(p(X|y)\|p(X))\big]\tag{6.51}$$
So MI is the expected KL divergence between posterior and prior, taken over values of Y (p. 152).

**Intuition note.** Each observed y moves our belief about X from the prior to a posterior. KL divergence quantifies that move, though it is not a true distance and depends on direction. MI is the average size of the move.

### 6.7 Summary (p. 152)
Joint distributions define and visualise marginal and conditional distributions and their entropies. MI of continuous variables, unlike their entropy, has a sensible interpretation without infinities. Channel noise reduces what each input conveys about the output, and vice versa. MI is linked to KL divergence and Bayes' rule (p. 152).

## Toy example
Ours, not from the text. It is a discrete table, to keep the arithmetic exact. The text says the definitions are the same in form (p. 135). Joint table: p(0,0) = p(1,1) = 0.4 and p(0,1) = p(1,0) = 0.1.
- Marginals: p(x) = 0.5 and p(y) = 0.5 for each value. So H(X) = H(Y) = 1 bit.
- Joint entropy: $H(X,Y)=2(0.4)\log_2 2.5+2(0.1)\log_2 10=0.8(1.3219)+0.2(3.3219)=1.0575+0.6644=1.7219$ bits.
- Eq. 6.36: $I=1+1-1.7219=0.2781$ bits.
- Eq. 6.35: given x, Y has distribution (0.8, 0.2). $H(Y|x)=0.8\log_2 1.25+0.2\log_2 5=0.8(0.3219)+0.2(2.3219)=0.2575+0.4644=0.7219$. This is the same for both x, so $H(Y|X)=0.7219$ and $I=1-0.7219=0.2781$. ✓.
- Chain rule: $H(X)+H(Y|X)=1+0.7219=1.7219=H(X,Y)$ ✓.
- KL form (6.47): the ratio $p(x,y)/(p(x)p(y))$ is $0.4/0.25=1.6$ or $0.1/0.25=0.4$. $I=0.8\log_2 1.6+0.2\log_2 0.4=0.8(0.6781)+0.2(-1.3219)=0.5425-0.2644=0.2781$ ✓.
- Invariance: relabelling X → 1−X (invertible) only swaps rows of the table, so every sum above is unchanged.

## Concepts
- [[mutual information I(X;Y)]] — here I(X,Y) = H(X)+H(Y)−H(X,Y) = H(X)−H(X|Y) = H(Y)−H(Y|X); symmetric, zero if X, Y are independent (pp. 135, 148)
- [[joint and conditional entropy]] — H(X,Y) is the dispersion of the joint density; H(Y|X) is the average entropy of slices p(Y|x) (pp. 139, 143–144)
- [[chain rule]] — H(X,Y) = H(X)+H(Y|X) = H(Y)+H(X|Y) (p. 150)
- [[differential entropy]] — entropy of continuous variables; an infinite constant is ignored, and it cancels in MI (pp. 138–139, 146)
- [[relative entropy / KL divergence]] — D_KL(p‖q) is positive unless p = q, and usually asymmetric; MI is D_KL(joint ‖ product of marginals) (p. 151)
- [[noisy channel]] — output y = x + η with encoder x = g(s) (p. 136)
- [[channel capacity]] — C = log m_max, with m_max Shannon's upper bound on discriminable inputs (p. 136)
- [[marginalisation]] (new) — integrating a joint density over one variable to get a marginal (p. 138)
- [[invariance of mutual information]] (new) — I(f(X), g(Y)) = I(X,Y) for invertible f, g, within formally defined limits (p. 150)

## Canonical instances
- [[correlated Gaussians (Fig. 6.2)]] — σ_X = 2, σ_Y = 1, ρ = 0.8; shows marginals and slices (pp. 138, 142–143)
- [[diabetes and sugar intake]] — MI of 2 bits stays 2 bits under Y′ = Y² or log Y (p. 151)
- [[additive noise channel y = x + η]] — input, output and noise entropies (pp. 136, 147)

## Bridges (candidates)
- [same-math] MI as D_KL(joint ‖ product of marginals) ↔ information-theory canon: relative entropy — the same integral (Eq. 6.47).
- [same-math] MI as expected posterior-vs-prior KL, E_y[D_KL(p(X|y)‖p(X))] ↔ Bayesian inference: expected information gain from an observation — same expression (Eq. 6.51).
- [structural-analogy] The entropy container H(X,Y) = I + H(X|Y) + H(Y|X) ↔ set algebra: the Venn diagram of two overlapping sets (Fig. 6.9).
- [structural-analogy] MI's invariance under invertible transformations ↔ statistics: association measures such as correlation, which the author says lack this claim (p. 151).

## Questions this raises
- What exactly are the "formally defined limits" under which MI is invariant (p. 150)?
- For the channel y = x + η, how does I(X,Y) relate to the noise entropy H(η) and to the capacity C?
- Why is H(X|Y) ≤ H(X) true on average, though particular outputs can increase uncertainty (p. 147)?
- How does MI compare with correlation as a measure of association (Section 7.6, as referred to on p. 151)?

## Reading notes
- Printed page = pdf page − 16 (pdf 151 = printed 135).
- The text layer garbles some symbols (e.g. "6=" for ≠ on pp. 145 and 151, and the integral signs). The equations here were checked against the page images.
- The text layer of pdf 164 contains a stray "See p20 cover", which is not visible in the image.
- Notation is slightly inconsistent: Eq. 6.15 writes p(x₁,Y), while the Fig. 6.6 caption writes p(Y,x₁) for the same slice.
- Eq. 6.32 is cited to Reza (1961) and not proved here.
- On p. 150 the text writes that X′ = k 'cannot be recovered from X' (and, for the log example, that X′ can be recovered from X). The digest uses the direction that matches the preceding sentences, recovery of X from X′. Bayes' rule is referred to Stone (2013) and Appendix F, which are outside this unit.
