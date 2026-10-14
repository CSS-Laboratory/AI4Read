---
id: mackay-2003-information/ch35-random
work: mackay-2003-information
unit: "35 Random Inference Topics"
pages: 445-450
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Random Inference Topics

## L0 — One line
For someone truly ignorant of a quantity's units, beliefs about its first digit should not change under rescaling (they are uniform on a log scale), which gives Benford's law; and Bayesian inference, with priors that state one's real assumptions, can be applied to problems such as mutation rates and the direction of arrows.

## L1 — The gist (≤ 120 words)
The chapter collects short inference problems. It first asks what someone who knows nothing should believe about the first digit of a measured number. For someone truly ignorant of the units, the belief should not change when the number is rescaled. This gives Benford's law, not a uniform distribution. It then works two exercises: the mutation rate from heavy-tailed Luria–Delbrück counts, and the direction of an arrow between two binary variables, decided by comparing the posterior probabilities of the two models. MacKay argues that priors should state real assumptions, so data can sometimes separate likelihood-equivalent models (models that can give identical joint distributions of the data). Several further exercises are posed without printed solutions.

**Prerequisites:** logarithms; Poisson distribution; convolution of distributions; Bayes' theorem and marginal likelihood; beta/Dirichlet distributions (Gamma function).

## L2 — Key ideas
- Ignorance of units means invariance under multiplying $x$ by any number. The first-digit probability is then proportional to log-scale length (p. 445).
- This gives $P(d)=\log_{10}(1+1/d)$, Benford's law. Ignorance is not a uniform distribution over digits (p. 446).
- Luria–Delbrück: the mutant count is a sum of a roughly Poisson number of clone sizes, whose distribution is heavy-tailed (a few very large values occur). The likelihood of the rate $a$ can be computed numerically by summing over $r$ (pp. 449–450).
- A smoothed clone-size law $P(n_i)=1/(Zn_i^2)$ keeps the likelihood accurate even though its moments are wrong (p. 449).
- For data with many zeros, keeping only the zero/non-zero counts loses very little (p. 450).
- Likelihood-equivalent graph models (models that can give the same joint distribution of the data; e.g. $A\to B$, $B\to A$) can still get different posterior probabilities if the priors are not "prior-equivalent", i.e. not chosen so that likelihood-equivalent models get identical posteriors (p. 447).
- In the worked example the posterior odds are about 3.8 : 1 for $A\to B$ (the printed value), i.e. modest evidence (p. 450).

## L3 — Walkthrough

### 35.1 What do you know if you are ignorant?
**Example 35.1** (p. 445). A real variable $x$ is measured accurately (half-life of the neutron, depth of Lake Vostok, and so on). What is the probability that its first digit is 1, as in $e=1.602\ldots\times10^{-19}$ C, or 9, as in $\mathcal F=9.648\ldots\times10^4$ C mol$^{-1}$? The text also asks about the second digit ("1.1…" versus "9.9…"). The printed solution works out only the first digit.

**Solution (p. 445).**
- An expert may predict $x$. What about someone who knows nothing about the topic?
- The units of $x$ were not specified. Changing units divides $x$ by a number, e.g. 1 209 600 for fortnights instead of seconds, or about $3\times10^7$ for years.
- For the expert, changing units changes predictions. For someone *truly ignorant*, predictions about the first digit are independent of units. So the distribution is invariant when $x$ is multiplied by any number.
- On a logarithmic scale, different unit scales are translations of one another (Fig. 35.1). So the probability of a first digit is proportional to the length of its piece of log scale:
$$p_1=\frac{\log 2-\log 1}{\log 10-\log 1}=\frac{\log 2}{\log 10}.\tag{35.1}$$
- Since $2^{10}=1024\simeq10^3=1000$, we get $10\log2\simeq3\log10$, hence (p. 446)
$$p_1\simeq\frac{3}{10}.\tag{35.2}$$
- For digit $d$ (p. 446):
$$\frac{\log(d+1)-\log d}{\log10-\log1}=\log_{10}(1+1/d).\tag{35.3}$$
This is **Benford's law**. The author concludes: ignorance does not correspond to a uniform distribution over $d$ (p. 446).

*Intuition note.* If you truly cannot tell whether a length is in metres or inches, you cannot prefer any decade-position. Equal *ratios* are equally likely, not equal differences. Small first digits then take more log-scale length than big ones.

**Exercise 35.2** (p. 446): a tumbling pin, with the angle to the vertical in the air versus in a photograph. Posed only; no solution is printed.

**Exercise 35.3** (p. 446), record breaking. Records are attempted at a steady rate; the distribution $P(x)$ does not change (the author thinks this unlikely for sports); nothing is known about $P(x)$. What can be predicted about the intervals between successive record dates? Posed only.

### 35.2 The Luria–Delbrück distribution
**Exercise 35.4 setup** (pp. 446–447).
- Luria and Delbrück wanted the mutation rate from the number of mutants at the end of an experiment. The count is heavy-tailed, because an early mutation can give a huge number of mutants (p. 446).
- The author's view: they did not know Bayes' theorem, and their coping involved arbitrary hacks giving two estimators. One estimator (based on the mean count) has "appallingly large variance", yet sampling theorists still use it (p. 446).
- One non-resistant bacterium grows for $g$ generations into $N=2^g$ clones. The mutation rate per cell per generation, $a$, is about one in a hundred million. There are $\sum_{i=0}^{g-1}2^i\simeq2^g=N$ opportunities to mutate. A mutation at generation $i$ yields $2^{g-i}$ resistant descendants (p. 446).
- Given $M$ experiments with counts $\{n_m\}$, infer $a$. Data, with $N=2.4\times10^8$: $\{1,0,3,0,0,5,0,5,0,6,107,0,0,0,1,0,0,64,0,35\}$ (p. 447).

**Solution (pp. 449–450).**
1. The number of mutations $r$ is roughly Poisson (slightly inaccurate, because descendants of a mutant cannot undergo the same mutation again):
$$P(r\mid a,N)=e^{-aN}\frac{(aN)^r}{r!}.\tag{35.7}$$
2. With perfect clockwork division, $P(n_i)=1/(2n_i)$ for powers of two (1/2, 1/4, 1/8, …). Real division is not synchronous, so a smoothed law allowing all integers is used (p. 449):
$$P(n_i)=\frac1Z\frac1{n_i^2},\qquad Z=\pi^2/6=1.645.\tag{35.8}$$
Its moments are all wrong, because $n_i\le N$. The author asks who cares about moments and answers: only sampling-theory statisticians, whom he calls "barking up the wrong tree", who build "unbiased estimators" such as $\hat a=(\bar n/N)/\log N$. The error this approximation introduces into the likelihood is negligible, in his view (p. 449).
3. The observed count is a sum (p. 449):
$$n=\sum_{i=1}^{r}n_i.\tag{35.9}$$
$P(n\mid r)$ is the $r$-fold convolution of (35.8). For example
$$P(n\mid r=2)=\sum_{n_1=1}^{n-1}\frac1{Z^2}\frac1{n_1^2}\frac1{(n-n_1)^2}\quad(n\ge2).\tag{35.10}$$
4. The likelihood of $a$ is obtained by summing over $r$:
$$P(n\mid a)=\sum_{r=0}^{N}P(n\mid r)\,P(r\mid a,N).\tag{35.11}$$
There is no analytic form. For small $a$ it is evaluated numerically by summing $r=0$ to $r_{\max}$, with $P(n\mid r)$ found by explicit convolutions. It is exact if $r_{\max}=n_{\max}$. Here $r_{\max}=9$ is plenty; the author used $r_{\max}=74$ for Fig. 35.3, which plots the likelihood of $a$ for these data on linear and log vertical scales (p. 450).
5. With many zero counts, little is lost by Luria and Delbrück's second approximation: keep only how many counts are zero (11) and non-zero (9):
$$L(a)=(e^{-aN})^{11}(1-e^{-aN})^{9}.\tag{35.12}$$
This is scarcely distinguishable from the full-information likelihood (p. 450).

*Intuition note.* The hard part is the heavy tail: a few huge counts (107, 64, 35) are presumably the result of early mutations, which the author says can give a huge number of mutants. Instead of averaging counts, the Bayesian model uses the probability of each observed count under each $a$ (35.11) to build a likelihood for $a$. This avoids the mean-based estimator that the author says has appallingly large variance.

### 35.3 Inferring causation
**Exercise 35.5 setup** (p. 447).
- Two graphical models are **likelihood-equivalent** if for any parameter setting of either there is a setting of the other giving the same joint distribution of observables. Example: $A\to B$ and $B\to A$.
- The author uses "B is a parent of A" for causation, since "R causes D" (rain, dry pavement) would be confusing.
- Some statistical methods that use the likelihood alone are unable to use data to distinguish such models. A Bayesian may separate them somewhat, because likelihood-equivalence does not force priors assigning equivalent densities over the two parameter spaces (p. 447).
- MacKay's criticism: many Bayesian graphical modellers deliberately use "prior-equivalent" priors, namely specially constructed Dirichlet distributions. These give likelihood-equivalent models identical posterior probabilities. In his view it is a philosophical error to use only those priors for which causation cannot be inferred. Priors should describe one's assumptions, and then interesting causal inferences are likely to be possible (p. 447).
- Toy problem: $A,B$ binary. $\mathcal H_{A\to B}$ has a Beta(1,1) (uniform) prior on the marginal probability of $A$ and independent Beta(1,1) priors on $P(b\mid a=0)$ and $P(b\mid a=1)$. $\mathcal H_{B\to A}$ is analogous (p. 447). Data, $F=1000$ (p. 448):

| | $a=0$ | $a=1$ | |
|---|---|---|---|
| $b=0$ | 760 | 5 | 765 |
| $b=1$ | 190 | 45 | 235 |
| | 950 | 50 | |

Find the posterior probabilities of the two hypotheses. The hint is to work symbolically. It gives $\Psi(x)=\frac{d}{dx}\ln\Gamma(x)\simeq\ln x-\frac1{2x}+O(1/x^2)$ (35.5) (p. 448).

**Solution (p. 450).**
- Each of the six terms has the Dirichlet-multinomial form
$$P(\mathbf F\mid\alpha\mathbf m)=\frac{\prod_i\Gamma(F_i+\alpha m_i)}{\Gamma(\sum_iF_i+\alpha)}\frac{\Gamma(\alpha)}{\prod_i\Gamma(\alpha m_i)}.\tag{35.13}$$
- Most factors cancel, leaving
$$\frac{P(\mathcal H_{A\to B}\mid\text{Data})}{P(\mathcal H_{B\to A}\mid\text{Data})}=\frac{(765+1)(235+1)}{(950+1)(50+1)}=\frac{3.8}{1}.\tag{35.14}$$
- This is modest evidence for $\mathcal H_{A\to B}$. The three probabilities inferred under it (roughly 0.95, 0.8, 0.1) are more typical of the prior than those under the other (0.24, 0.008, 0.19).
- That sounds absurd under a "uniform" prior. But in the natural, logit basis the prior is proportional to $p(1-p)$, and the ratio can be estimated by
$$\frac{0.95\times0.05\times0.8\times0.2\times0.1\times0.9}{0.24\times0.76\times0.008\times0.992\times0.19\times0.81}\simeq\frac31,\tag{35.15}$$
"not exactly right", but it shows where the preference comes from.

The author adds that causation is a complex topic. Bayesian inference of arrow directions seems to be a neglected view, "certainly not the whole story". He points to Pearl (2000) (p. 448).

*Intuition note.* Both models fit the table equally well at their best parameters. They differ in how plausible those best parameters are under each model's prior. The data table happens to need less "unusual" parameters under $A\to B$.

### 35.4 Further exercises (pp. 448–449; no solutions printed)
- **35.6:** photons from a Poisson process with rate $\lambda(t)=\exp(a+b\sin(\omega t+\phi))$ (35.6). Discuss inference of $a,b,\omega,\phi$ from arrival times (p. 448).
- **35.7:** two-column data printed without a boundary, e.g. "891.10.0". Compare parsing (a) "891. 10.0" with (b) "891.1 0.0" (p. 448).
- **35.8:** four points $\{0,0.9,2,6\}$ from the biexponential $P(x\mid\mu)=\frac1Z\exp(-|x-\mu|)$ with $Z=2$ (p. 449). What do they say about $\mu$? Sketches and a plausible range are requested.

## Toy example (ours)
Benford's law from scale invariance, with digits 1–9 for numbers in $[1,10)$ and base-10 logs.
- $p_1=\log_{10}2=0.3010$.
- $p_2=\log_{10}(3/2)=0.1761$ and $p_3=\log_{10}(4/3)=0.1249$.
- Check of invariance: doubling maps numbers starting with 1 (range $[1,2)$) to $[2,4)$, i.e. first digit 2 or 3. Then $p_2+p_3=0.1761+0.1249=0.3010=p_1$. Belief is unchanged by the unit change "×2".
- Also $p_9=\log_{10}(10/9)=0.0458$. The sum telescopes: $\sum_{d=1}^9\log_{10}\frac{d+1}{d}=\log_{10}10=1$.
- A uniform digit distribution would give $1/9=0.111$ for every digit. It would not be preserved by "×2". For example, the mass of $[2,4)$ would be $2/9$, but $[1,2)$ has mass $1/9$.

## Concepts
- [[principle-of-indifference-maximum-entropy]] — here ignorance is expressed as invariance under rescaling, not as a uniform distribution (p. 445)
- [[scale-invariant-prior]] (new) — a distribution unchanged when $x$ is multiplied by any number, so uniform on a log scale (p. 445)
- [[benford-law]] (new) — first digit $d$ has probability $\log_{10}(1+1/d)$ (p. 446)
- [[likelihood]] — probability of data as a function of the parameter, e.g. $L(a)$ (p. 450)
- [[marginal-likelihood-evidence]] — probability of the data averaged over the prior; used to compare $\mathcal H_{A\to B}$ and $\mathcal H_{B\to A}$ (p. 450)
- [[likelihood-equivalence]] (new) — models that can express exactly the same joint distributions of the observables (p. 447)
- [[prior-equivalence]] (new) — priors giving likelihood-equivalent models identical posteriors. MacKay opposes making it mandatory (p. 447)
- [[conjugate-prior]] — the Beta/Dirichlet priors give the closed-form Dirichlet-multinomial evidence (35.13) (p. 450)
- [[causal-dag]] — here, arrows read as "is a parent of" (p. 447)
- [[frequentist-vs-bayesian-inference]] — the author contrasts Bayesian likelihood-based inference with sampling-theory estimators (pp. 446, 449)

## Canonical instances
- [[benford-first-digit]] (new) — first-digit probabilities under unit ignorance (pp. 445–446)
- [[luria-delbruck-experiment]] (new) — inferring a mutation rate from heavy-tailed mutant counts (pp. 446, 449–450)
- [[binary-causal-direction-toy]] (new) — $A\to B$ vs $B\to A$ with Beta(1,1) priors and a 2×2 table (pp. 447–448, 450)

## Bridges (candidates)
- [structural-analogy] Scale-invariant (log-uniform) ignorance ↔ information-theory: description length grows like a logarithm of magnitude, so log scale is the natural measure of "size" — a loose parallel, not stated in this unit.
- [same-math] Dirichlet-multinomial evidence (35.13) ↔ bayesian: marginal likelihood with conjugate priors — the same integral over the prior.
- [structural-analogy] Likelihood-equivalence of $A\to B$ and $B\to A$ ↔ bayesian: causal DAGs, where observational data alone cannot fix arrow direction (canon link; not stated in this unit).

## Questions this raises
- Does Benford-style invariance hold for quantities whose range is limited, or for a non-expert who knows an approximate size?
- How sensitive is the 3.8 : 1 ratio to the choice of Beta(1,1) priors? What do other priors give?
- Why does the smoothed $1/n^2$ clone-size law give nearly the same likelihood as the true one?
- How would the results for $\mathcal H_{A\to B}$ vs $\mathcal H_{B\to A}$ change with a much larger $F$?

## Exercises worth doing
- Ex. 35.2 (p. 446) — invariance reasoning applied to angles in 3D versus a 2D photograph — difficulty: medium
- Ex. 35.3 (p. 446) — what a no-knowledge assumption predicts for record intervals — difficulty: medium
- Ex. 35.7 (p. 448) — comparing two parsings as two hypotheses; Bayesian model comparison on text — difficulty: medium
- Ex. 35.8 (p. 449) — posterior over a location parameter with a non-Gaussian likelihood; sketch it — difficulty: medium

Exercises 35.4 and 35.5 are the main worked examples. Their printed solutions are summarised in L3.

## Reading notes
- Printed page = pdf − 12 (pdf 457 = printed 445).
- Eq. (35.14): $(766\times236)/(951\times51)=180776/48501\approx3.73$, but the page prints 3.8. The page gives no explanation of the difference (my calculation, not a source statement); 3.73 would round to 3.7.
- Exercise 35.6 says the parameters $a,b,\omega,\phi$ "are known" and then asks to discuss their inference. This is how the image reads (my guess: "unknown" was meant).
- Exercise 35.2 sits beside a figure of log-scale segments labelled $P(1)$, $P(3)$, $P(9)$; the exercise text does not refer to it.
- The text layer is garbled for the side-figure labels and Fig. 35.3 axes; the images were used. In Fig. 35.3 the vertical axis is likelihood/$10^{-23}$ and the horizontal axis is $a$.
