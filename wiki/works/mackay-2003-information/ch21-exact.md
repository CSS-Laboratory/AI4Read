---
id: mackay-2003-information/ch21-exact
work: mackay-2003-information
unit: "21 Exact Inference by Complete Enumeration"
pages: 293-299
fields: [information-theory, bayesian]
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
# Exact Inference by Complete Enumeration

## L0 — One line
Brute-force inference lists every hypothesis, computes its posterior probability and marginalizes. It is exact, but the cost grows exponentially with the number of parameters.

## L1 — The gist (≤ 120 words)
How do we compute posterior probabilities exactly when we simply list all hypotheses? In the burglar-alarm example, four (burglar, earthquake) hypotheses are enumerated. This gives about a 50% chance of a burglar after the phone call, which drops to 8% once an earthquake is known. That drop is "explaining away". For continuous parameters (one Gaussian, a mixture of two Gaussians) we discretize into a grid and sum, and the same sum gives a model's evidence. But if the data narrow each of K parameters about tenfold, brute force needs at least 10^K grid points, so enumeration is rarely feasible. This motivates the smarter methods in later chapters.

**Prerequisites:** Bayes' theorem; marginalization (summing out a variable); independence; the Gaussian density.

## L2 — Key ideas
- Complete enumeration means evaluating the posterior of every hypothesis, then marginalizing to answer a question. It is exact but brute force (p. 293, p. 295).
- In the alarm network, the posterior is computed from prior × likelihood over the four (b, e) pairs, then normalized (p. 294).
- Marginalizing gives P(b=1 | a=1) = 0.495, so nearly a 50% chance of a burglar (p. 295).
- Burglar and earthquake are independent a priori but dependent after observing the alarm (p. 295).
- Explaining away: learning e=1 lowers P(b=1) from 0.495 to 0.08, even though b and e were a priori independent. The author calls this a feature of correct inference (p. 295).
- Continuous spaces are discretized to a grid. The Gaussian (2 parameters) and the two-Gaussian mixture (5 parameters) show how enumeration looks (pp. 295–298).
- Model comparison uses the evidence, a sum of prior × likelihood over the grid (eq. 21.9) (p. 298).
- With K parameters whose uncertainty has each been reduced by, say, a factor of ten by the data, brute-force integration needs at least 10^K grid points, so enumeration is rarely feasible (pp. 298–299).

## L3 — Walkthrough

### 21.1 The burglar alarm (pp. 293–295)
The author notes that Bayesian probability is "sometimes called" "common sense, amplified" and asks the reader to consult intuition first (p. 293).

**Example 21.1 (after Pearl, 1988).** Fred is at work and gets a phone call from his neighbour saying his burglar alarm is ringing. What is P(burglar)? Driving home, he hears on the radio that a small earthquake happened near his home. **Fred says:** it was probably the earthquake. What is P(burglar) now? (p. 293)

Variables: b = burglar, a = alarm ringing, p = neighbour phones, e = earthquake, r = radio reports earthquake. The belief network (Figure 21.1) has arrows b→a, e→a, e→r, a→p. The joint factorizes as (p. 293):
$$P(b,e,a,p,r)=P(b)P(e)P(a\mid b,e)P(p\mid a)P(r\mid e)\tag{21.1}$$

Plausible numbers (pp. 293–294):
- $P(b{=}1)=\beta$, $P(b{=}0)=1-\beta$ (21.2), e.g. $\beta=0.001$, which the author describes as a burglary once every three years.
- $P(e{=}1)=\epsilon$, $P(e{=}0)=1-\epsilon$ (21.3), e.g. $\epsilon=0.001$. Independence $P(b,e)=P(b)P(e)$ seems reasonable unless opportunistic burglars strike right after earthquakes.
- Alarm, a "noisy-or": it rings if any of three events happens. A burglar triggers it with reliability $\alpha_b=0.99$. An earthquake triggers it with $\alpha_e=0.01$ (the author writes "perhaps αe = 1% of alarms are triggered by earthquakes?"). Some other cause gives a false alarm with rate $f=0.001$.
- Hence $P(a{=}0\mid b,e)=(1-f)(1-\alpha_b)^{b}(1-\alpha_e)^{e}$. The author writes the four cases out one by one (p. 294). (The exponent form is our compact restatement.)

Numbers for $P(a{=}1\mid b,e)$ (p. 294):

| (b, e) | P(a=1 \| b, e) |
|---|---|
| (0, 0) | 0.001 |
| (1, 0) | 0.99001 |
| (0, 1) | 0.01099 |
| (1, 1) | 0.9901099 |

Assumptions: the neighbour never phones if the alarm is silent, $P(p{=}1\mid a{=}0)=0$. The radio is trustworthy, $P(r{=}1\mid e{=}0)=0$. So p=1 gives certainty that a=1, and r=1 gives certainty that e=1. The probabilities $P(p{=}1\mid a{=}1)$ and $P(r{=}1\mid e{=}1)$ are not needed (p. 294).

**Step 1: after p=1, so a=1.** The posterior over the four (b, e) hypotheses is (p. 294):
$$P(b,e\mid a{=}1)=\frac{P(a{=}1\mid b,e)P(b)P(e)}{P(a{=}1)}\tag{21.4}$$
Numerators (p. 294):
- (0,0): $0.001\times0.999\times0.999=0.000998$
- (1,0): $0.99001\times0.001\times0.999=0.000989$
- (0,1): $0.01099\times0.999\times0.001=0.000010979$
- (1,1): $0.9901099\times0.001\times0.001=9.9\times10^{-7}$

Their sum is the normalizer, $P(a{=}1)=0.002$. The posteriors are (p. 294):
$$P(0,0\mid a{=}1)=0.4993,\ P(1,0\mid a{=}1)=0.4947,\ P(0,1\mid a{=}1)=0.0055,\ P(1,1\mid a{=}1)=0.0005\tag{21.5}$$

**Step 2: marginalize over e** (p. 295):
$$P(b{=}0\mid a{=}1)=0.4993+0.0055=0.505,\quad P(b{=}1\mid a{=}1)=0.4947+0.0005=0.495\tag{21.6}$$
So there is nearly a 50% chance of a burglar. The variables b and e, independent a priori, are now dependent: (21.5) is not a separable function of b and e (p. 295).

**Step 3: learn e=1.** Divide the bottom two rows of (21.5) by their sum $P(e{=}1\mid a{=}1)=0.0060$ (p. 295):
$$P(b{=}0\mid e{=}1,a{=}1)=0.92,\quad P(b{=}1\mid e{=}1,a{=}1)=0.08\tag{21.7}$$
The burglar probability falls to 8%, in line with everyday intuition (p. 295).

**Explaining away.** One possible cause (b=1) of the data (a=1) becomes less probable when another cause (e=1) becomes more probable, though the causes were independent a priori. The author calls this "an important feature of correct inferences" that any AI should replicate (p. 295). If the neighbour and radio are unreliable, the calculation is more complex but the effect persists: the report r makes it more probable that the alarm is ringing and less probable that there was a burglar (p. 295).

*Intuition note:* Once we know the alarm rang, the two causes compete to explain it. Evidence for one makes the other less needed. Prior independence does not survive conditioning on the effect.

Summary: enumerate the four (b, e) hypotheses, find their posteriors, marginalize to get the inference about b (p. 295). Exercise 21.2 asks for P(earthquake) after the phone call but before the radio (p. 295).

### 21.2 Exact inference for continuous hypothesis spaces (pp. 295–299)
Many hypothesis spaces are continuous. Examples are the decay length λ (one dimension) and a Gaussian's (μ, σ) (two dimensions). In a computer they are necessarily discretized, so in principle they can be enumerated on a grid (p. 295).

**A two-parameter model (pp. 296–297).** The Gaussian is
$$P(x\mid\mu,\sigma)=\frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big)\equiv\mathrm{Normal}(x;\mu,\sigma^2)\tag{21.8}$$
Figure 21.2 enumerates 100 hypotheses on a 10×10 grid of μ and σ, each drawn as the density it puts on x. Data $x_n$, n = 1..N, are assumed drawn independently. For the five points of Figure 21.3, the likelihood $P(\{x_n\}_{n=1}^5\mid\mu,\sigma)$ of each grid hypothesis is shown by line thickness in Figure 21.4. Hypotheses with likelihood below $e^{-8}$ times the maximum are deleted (p. 296). A finer grid gives surface and contour plots (Figure 21.5). The data there have mean $\bar x=1.0$ and $S=\sum(x-\bar x)^2=1.0$ (p. 297).

**A five-parameter mixture model (pp. 296–298).** The author suggests that, eyeballing the data, it seems more plausible that they come from a mixture of two Gaussians (p. 296). This has two means, two standard deviations and mixing coefficients $\pi_1+\pi_2=1$, $\pi_i\ge0$ (p. 298):
$$P(x\mid\mu_1,\sigma_1,\pi_1,\mu_2,\sigma_2,\pi_2)=\frac{\pi_1}{\sqrt{2\pi}\sigma_1}e^{-\frac{(x-\mu_1)^2}{2\sigma_1^2}}+\frac{\pi_2}{\sqrt{2\pi}\sigma_2}e^{-\frac{(x-\mu_2)^2}{2\sigma_2^2}}$$
Figure 21.6 enumerates 800 subhypotheses. The means take five values each, the standard deviations four values each, and $\pi_1$ two values (0.6/0.4 in the top half, 0.8/0.2 in the bottom half). (Added step: 5·5·4·4·2 = 800.) Figure 21.7 shows the likelihood on the same grid, with the same $e^{-8}$ cutoff. Blank regions are hypotheses the data have ruled out (pp. 298–299).

**Model comparison.** The posterior probability of each model $\mathcal H$ is found from its evidence (marginal likelihood). This is an integral over parameters $\boldsymbol\theta$, done numerically as a sum over the enumerated values, with $P(\boldsymbol\theta)$ the prior over the grid, taken uniform (p. 298):
$$P(\{x\}\mid\mathcal H)=\sum_{\boldsymbol\theta}P(\boldsymbol\theta)P(\{x\}\mid\boldsymbol\theta,\mathcal H)\tag{21.9}$$

**The cost.** For the mixture this is a five-dimensional integral. An accurate answer needs a grid much finer than in the figures. If the data narrow the uncertainty about each of K parameters by (say) a factor of ten, brute force needs at least $10^K$ grid points. This exponential growth with model size is why complete enumeration is rarely feasible (pp. 298–299). Exercise 21.3 asks for the cost for ten Gaussians in twenty dimensions (p. 299).

*Intuition note:* Enumeration treats a continuous model as a long list of cases. Every extra parameter multiplies the list length, so the list explodes quickly.

## Toy example (ours, not from the text)
Two independent causes b, e, each with prior 0.1. The effect is a deterministic OR: a=1 if b=1 or e=1. We observe a=1.
- Numerators P(a=1|b,e)P(b)P(e): (0,0): 0; (1,0): 0.1×0.9 = 0.09; (0,1): 0.9×0.1 = 0.09; (1,1): 0.1×0.1 = 0.01.
- Normalizer: 0 + 0.09 + 0.09 + 0.01 = 0.19.
- Marginal: P(b=1|a=1) = (0.09+0.01)/0.19 = 0.526.
- Now learn e=1: P(b=1|e=1,a=1) = 0.01/(0.09+0.01) = 0.1, the prior value.

The probability of b drops from 0.526 to 0.1 because e explains the alarm. This is explaining away. A grid with K=5 parameters, 10 values each, would have 10^5 = 100,000 points, versus 4 hypotheses here.

## Concepts
- [[complete-enumeration]] (new) — list every hypothesis, compute its posterior, marginalize; exact but brute force (p. 293)
- [[belief-network]] (new) — graph showing how the joint factorizes into local conditional probabilities (p. 293, Fig. 21.1)
- [[noisy-or]] (new) — an effect occurs if any of several causes, or a background cause, triggers it (p. 294)
- [[marginalization]] (new) — summing a joint posterior over unwanted variables (p. 295)
- [[explaining-away]] (new) — one cause becomes less probable when an alternative cause of the same data becomes more probable, though the causes were independent a priori (p. 295)
- [[bayes-theorem]] — posterior = likelihood × prior / normalizer, used in (21.4) (p. 294)
- [[prior-distribution]] — P(b), P(e), and the uniform P(θ) on the grid (pp. 293, 298)
- [[likelihood]] — P(data | μ, σ) evaluated at each grid point (p. 296)
- [[posterior-distribution]] — P(b,e | a=1) over four hypotheses (p. 294)
- [[marginal-likelihood]] — P({x}|H), a prior-weighted sum of likelihoods over θ (p. 298)
- [[mixture-of-gaussians]] (new) — density that is a weighted sum of Gaussians with weights summing to 1 (p. 298)
- [[curse-of-dimensionality]] (new) — grid of at least 10^K points for K parameters if the uncertainty about each has been reduced by, say, a factor of ten (p. 298)

## Canonical instances
- [[burglar-alarm]] — noisy-or network showing posterior enumeration and explaining away (pp. 293–295)
- [[gaussian-grid-enumeration]] — 10×10 grid over (μ, σ) for five data points (pp. 296–297)
- [[two-gaussian-mixture-grid]] — 800-point grid over five parameters, with model evidence (pp. 298–299)

## Bridges (candidates)
- [structural-analogy] explaining away ↔ bayesian: conditioning on a common effect (collider, b→a←e) makes independent causes dependent (canon link; not stated in this unit)
- [same-math] evidence as a prior-weighted grid sum (21.9) ↔ bayesian: marginal likelihood as the average of the likelihood over the prior
- [metaphor] 10^K grid cost ↔ bayesian: motivation for Monte Carlo and variational methods (canon link; the unit only says later chapters introduce "smarter" methods)

## Questions this raises
- How can the b, e posterior be computed without listing all hypotheses when there are hundreds of variables?
- How sensitive are the 50% and 8% answers to β, ε, α_e and f?
- Does the evidence P({x}|H) favour the mixture over one Gaussian on the five points of Figure 21.3? The unit sets up the comparison but gives no numbers.
- What approximations replace the grid sum when the grid would have 10^K points?

## Exercises worth doing
- Ex. 21.2 (p. 295) — compute P(earthquake) after the phone call but before the radio; checks understanding of (21.5) — difficulty: easy (rated [2] in the text)
- Ex. 21.3 (p. 299) — estimate the grid cost for ten Gaussians in twenty dimensions; shows the exponential blow-up — difficulty: easy (rated [1] in the text)

## Reading notes
- Printed page = pdf − 12 (pdf 305 = p. 293).
- The text layer drops the symbol ε (epsilon) in (21.3) and nearby text. The page image shows ε.
- The text layer garbles the mixture formula on p. 298. The image gives the two-term sum used above.
- Figures 21.2, 21.4, 21.6 and 21.7 are pictures of grids of small curves (in 21.4 and 21.7 line thickness encodes the likelihood); only their captions and the text about them are digested here.
- The source gives no solutions to exercises.
