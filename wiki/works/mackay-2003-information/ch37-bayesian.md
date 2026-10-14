---
id: mackay-2003-information/ch37-bayesian
work: mackay-2003-information
unit: 37 Bayesian Inference and Sampling Theory
pages: 457-466
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Bayesian Inference and Sampling Theory

## L0 — One line
MacKay argues that sampling-theory tools (p-values, confidence levels) do not answer the question we care about and can depend on irrelevant facts, whereas Bayesian posteriors answer it directly.

## L1 — The gist (≤ 120 words)
The chapter compares two schools of statistics on small problems. Sampling theory judges a procedure by how it behaves over many repeated experiments. Bayesian inference computes the probability of the hypotheses of interest, given the actual data (the posterior probability). On a vaccine trial, a χ² significance test gives p = 0.07, while the Bayesian posterior gives about 99% that A beats B. A coin experiment shows p-values changing with the stopping rule (the plan for when to stop). An integer-parameter example shows a "75% confidence interval" whose posterior probability is 50% in one case and 100% in another. MacKay ends with compromises: Bayesian methods can be judged by sampling properties, and p-values may help with model criticism.

**Prerequisites:** Binomial probabilities; integrating a probability density; Bayes' theorem (posterior ∝ likelihood × prior); the idea of a null hypothesis.

## L2 — Key ideas
- A p-value is the probability, under a null hypothesis, of an outcome as extreme as or more extreme than the one seen. It is not the probability that the null is true, though many readers treat it so (p. 457, p. 460).
- A sampling-theory test usually compares a null with a general alternative such as "different effectiveness". It focuses only on how surprising the data are under the null, not on how well the alternative predicts them (p. 458).
- In the vaccine example the χ² test gives p ≈ 0.07. The Bayesian posterior gives P(pA+ < pB+ | Data) = 0.990, and it can answer other questions such as "is A ten times better?" (pp. 459–461).
- For the toy 1-and-1 data set, the Bayesian evidence ratio is 1/4 : 1/6 = 0.6 : 0.4. It quantifies how weak the evidence is, where the significance test just says "not significant" (p. 462).
- Sampling-theory p-values change with the experimenter's stopping rule (fixed n versus stop at the third b: 7% versus 3%). The Bayesian inference about the coin's bias does not depend on the stopping rule (pp. 463–464).
- A confidence level is a property of a procedure over imagined repeated experiments. In the integer example it is not the probability that θ lies in the reported interval, so reading it that way is incorrect (p. 464, p. 465).
- Compromises: Bayesian methods often have good sampling properties. Sampling-theory tests can help criticise a model when no alternative is specified (p. 466).

## L3 — Walkthrough

### Introduction (p. 457)
- **Sampling theorists** want methods guaranteed to work most of the time under minimal assumptions. **Bayesians** want inferences that use all available information and answer the question for the particular data set (p. 457).
- A p-value is the probability, given a null hypothesis for the data's distribution, of an outcome as or more extreme than the observed one. Untrained readers, and perhaps many authors, read it as a Bayesian posterior probability of the null. Both schools agree that this reading is wrong (p. 457).
- Sampling theory can be "trigger-happy". It may reject a null when the data weakly support it (exercise 3.15, p. 59, and p. 64, cited). It can also miss strong evidence. Its "significance" can change with irrelevant features of the experimental design (p. 457).
- MacKay says the chapter is optional and suggests readers who find it hard should skip it and use Bayesian methods (p. 457).

### 37.1 A medical example (pp. 458–462)
**Data.** 40 volunteers. 30 get vaccine A and 10 get placebo B. In group A, 1 of 30 gets microsoftus. In group B, 3 of 10 do. Is A better than B? (p. 458)

**Sampling theory.**
- Hypotheses: $\mathcal H_1$: "A and B have different effectivenesses". $\mathcal H_0$: "exactly the same". After they are defined, attention focuses only on $\mathcal H_0$. It is accepted or rejected on how unexpected the data were under $\mathcal H_0$, not on how much better $\mathcal H_1$ predicted them (p. 458).
- The statistic χ² measures deviation of counts $F_i$ from their expectations under $\mathcal H_0$ (p. 458):
$$\chi^2=\sum_i\frac{(F_i-\langle F_i\rangle)^2}{\langle F_i\rangle}\tag{37.1}$$
- With Yates's correction (p. 458):
$$\chi^2=\sum_i\frac{(|F_i-\langle F_i\rangle|-0.5)^2}{\langle F_i\rangle}\tag{37.2}$$
- Under $\mathcal H_0$ with common rates $f_\pm$ (p. 458):
$$\langle F_{A+}\rangle=f_+N_A,\ \langle F_{A-}\rangle=f_-N_A,\ \langle F_{B+}\rangle=f_+N_B,\ \langle F_{B-}\rangle=f_-N_B\tag{37.3}$$
- The sampling distribution of a statistic is its distribution over repetitions of the experiment, assuming $\mathcal H_0$ (p. 459). The four counts obey two constraints ($F_{A+}+F_{A-}=N_A$, $F_{B+}+F_{B-}=N_B$) and $f_\pm$ are unknown. Together these reduce the degrees of freedom from four to one (p. 459). Tabulated χ² distributions are accurate only if the expected counts are about 5 or more (p. 459).
- The parameters are estimated from the data (p. 459):
$$\hat f_+=\frac{F_{A+}+F_{B+}}{N_A+N_B},\quad \hat f_-=\frac{F_{A-}+F_{B-}}{N_A+N_B}\tag{37.4}$$
- **Camp one** fixes the significance level (e.g. 5%) before seeing the data and finds the critical value ($\chi^2_{0.05}=3.84$ for one degree of freedom). **Camp two** computes χ² and reports the p for which the observed value would be critical (p. 459).
- Here $f_+=1/10$, $f_-=9/10$ (37.5). The expected counts are $\langle F_{A+}\rangle=3$, $\langle F_{A-}\rangle=27$, $\langle F_{B+}\rangle=1$, $\langle F_{B-}\rangle=9$ (37.6–37.9). Then $\chi^2=5.93$ (37.10) (p. 459).
- Camp one rejects $\mathcal H_0$ at 0.05, since 5.93 > 3.84. With Yates's correction χ² = 3.33, and camp one accepts $\mathcal H_0$ (p. 459).
- Camp two interpolates between $\chi^2_{.10}=2.71$ and $\chi^2_{.05}$ and reports p = 0.07 (p. 460).
- The result says A differs "significantly" from B. It does not say by how much, and "significant" means only statistically significant (p. 460). A layperson might read p = 0.07 as "93% chance the treatments differ". It actually means that, if the treatments were equal, 7% of repetitions would give a more extreme χ². That has almost nothing to do with how likely A is better than B (p. 460).

*Intuition note.* A p-value answers "how odd are these data if nothing is going on?". It does not answer "how likely is it that A is better?". These are different questions, and the second is the one we want.

**Bayesian analysis.**
- MacKay scraps the exact-equality hypothesis because we do not believe it. The unknowns are $p_{A+}$ and $p_{B+}$, the disease probabilities under each treatment (p. 460).
$$P(p_{A+},p_{B+}\mid\{F_i\})=\frac{P(\{F_i\}\mid p_{A+},p_{B+})\,P(p_{A+},p_{B+})}{P(\{F_i\})}\tag{37.11}$$
$$P(\{F_i\}\mid p_{A+},p_{B+})=\binom{N_A}{F_{A+}}p_{A+}^{F_{A+}}p_{A-}^{F_{A-}}\binom{N_B}{F_{B+}}p_{B+}^{F_{B+}}p_{B-}^{F_{B-}}\tag{37.12}$$
$$=\binom{30}{1}p_{A+}^1p_{A-}^{29}\binom{10}{3}p_{B+}^3p_{B-}^7\tag{37.13}$$
- The prior is uniform: $P(p_{A+},p_{B+})=1$ (37.14). It is separable, so the posterior is too (p. 460):
$$P(p_{A+},p_{B+}\mid\{F_i\})=P(p_{A+}\mid F_{A+},F_{A-})\,P(p_{B+}\mid F_{B+},F_{B-})\tag{37.15}$$
- The question "how probable is it that $p_{A+}$ is smaller than $p_{B+}$?" is answered by $P(p_{A+}<p_{B+}\mid\text{Data})$ (37.16). This is the joint posterior integrated over the triangle $p_{A+}<p_{B+}$ (fig. 37.3), found by numerical integration of the likelihood (37.13): **0.990** (p. 461).
- Conclusion: given the data and the prior assumptions, there is a 99% chance that A is superior, about 99 to one (p. 461).
- Other questions can be answered by integrating over other regions. MacKay says "ten times more effective" uses the region $p_{A+}<10\,p_{B+}$ (fig. 37.4) (p. 461). (See Reading notes: the figure's shaded triangle looks narrow.)

*Intuition note.* In the Bayesian view, questions about the two rates can be answered by integrating the same posterior over different regions, as the two examples show. No new test is needed for each question.

**Model comparison (p. 461–462).** Suppose we do want to compare $\mathcal H_0:p_{A+}=p_{B+}$ with $\mathcal H_1:p_{A+}\ne p_{B+}$. Data $D$: one subject given A contracted the disease, and one given B did not.
- Uniform priors: $P(p\mid\mathcal H_0)=1$ on (0,1) (37.17), and $P(p_{A+},p_{B+}\mid\mathcal H_1)=1$ on the unit square (37.18) (p. 462).
- The probability of the data under a model is the normalizing constant of the posterior (p. 462):
$$P(D\mid\mathcal H_0)=\int dp\,P(D\mid p)P(p\mid\mathcal H_0)=\int dp\,p(1-p)\times1=1/6\tag{37.19–37.21}$$
$$P(D\mid\mathcal H_1)=\iint dp_{A+}dp_{B+}P(D\mid p_{A+},p_{B+})P(p_{A+},p_{B+}\mid\mathcal H_1)=\int dp_{A+}\,p_{A+}\int dp_{B+}(1-p_{B+})=\tfrac12\times\tfrac12=\tfrac14\tag{37.22–37.25}$$
$$\frac{P(D\mid\mathcal H_1)}{P(D\mid\mathcal H_0)}=\frac{1/4}{1/6}=\frac{0.6}{0.4}\tag{37.26}$$
- With 50:50 prior odds, the posterior is 60:40 in favour of $\mathcal H_1$ (p. 462).
- MacKay says the sampling-theory answer would be the same significance test, giving "not significant". He thinks it better to admit the data give weak evidence for $\mathcal H_1$, and Bayesian methods say how weak (p. 462).

### 37.2 Dependence of p-values on irrelevant information (pp. 462–464)
- Dr. Bloggs tosses a coin 12 times and gets `aaabaaaabaab`: 3 bs and 9 as. Is the coin biased towards a? (p. 462)
- **Sampling-theory friend (r random, n = 12 fixed):** the p-value is
$$P(r\le3\mid n=12,\mathcal H_0)=\sum_{r=0}^{3}\binom{n}{r}\tfrac1{2^n}=\Big(\tbinom{12}{0}+\tbinom{12}{1}+\tbinom{12}{2}+\tbinom{12}{3}\Big)\tfrac1{2^{12}}=0.07\tag{37.27}$$
This is "not significant" at 5%. A two-tailed p would be about 15% (p. 463).
- **Bloggs replies:** he had decided to keep tossing until three bs appeared, so $n$ is the random variable (p. 463). The friend recomputes:
$$P(n\mid\mathcal H_0,r)=\binom{n-1}{r-1}\tfrac1{2^n}\tag{37.28}$$
$$P(n\ge12\mid r=3,\mathcal H_0)=0.03\tag{37.29}$$
Now the friend says there *is* significant evidence of bias (p. 463).
- Exercise 37.1 asks for the Bayesian inference and whether it depends on the stopping rule (p. 463). MacKay states the answer: the inferences about $p_a$ do not depend on the stopping rule (p. 463). This is consistent with the likelihood principle, that the stopping rule is not relevant to what we have learned about $p_a$ (p. 464).
- MacKay says the audience divides in two. Half intuitively feel the stopping rule is irrelevant. The other half, perhaps because of sampling-theory training, feel that stopping at the third b may have biased the experiment. He encourages the second group to reflect and hopes they will come round to the likelihood-principle view (pp. 463–464).
- Thought experiment: spies update $r$ and $n$ after each toss. Should their beliefs depend on Bloggs's intentions? MacKay poses this as a question and does not answer it on this page (p. 464).
- It seems to MacKay that the stopping-rule dependence of p-values (and whole volumes of literature on complicated stopping rules, e.g. sequential probability ratio tests) is a compelling argument for having nothing to do with p-values at all. He points to a Bayesian solution in sections 3.2–3.3 and exercise 3.15 (p. 464).
- Janitor's scene: the coin was destroyed right after $n=12$, so he asks whether Bloggs must "recompute your p-value?". MacKay introduces the scene by asking whether it would help clarify the issue; the page gives no explicit answer (p. 464).

*Intuition note.* The data string is the same in both designs. Only the experimenter's private plan differs. On MacKay's view, a method whose verdict changes with the plan is reacting to something other than the evidence.

### 37.3 Confidence intervals (pp. 464–465)
- A confidence interval $(\theta_{\min}(D),\theta_{\max}(D))$ is a function of the data. Its **confidence level** $f$ is a property computable before the data arrive. Generate many data sets from a true $\theta$ and check how often the interval contains it. If that fraction is $f$ for all true $\theta$, the level is $f$ (p. 464).
- Example: if $\theta$ is a Gaussian mean with known standard deviation 1 and $D$ is one sample, $(D-2,D+2)$ is a 95% confidence interval (p. 464).
- **Integer example.** $\theta$ is an integer, and $x_1,x_2$ are drawn independently with (p. 464):
$$P(x\mid\theta)=\begin{cases}1/2&x=\theta\\1/2&x=\theta+1\\0&\text{otherwise}\end{cases}\tag{37.30}$$
For $\theta=39$ the four data sets (39,39), (39,40), (40,39), (40,40) each have probability 1/4 (37.31) (p. 465).
- Interval: $[\theta_{\min},\theta_{\max}]=[\min(x_1,x_2),\min(x_1,x_2)]$ (37.32). It contains $\theta$ in 3 of 4 cases, so its confidence level is 75% (p. 465).
- Data (29,29): the interval is [29,29], with level 75%. By Bayes' theorem, $\theta$ is 29 or 28, equally likely if the priors on 28 and 29 are equal. So the posterior is 50% on each (p. 465).
- Data (29,30): the interval is still [29,29] at 75%, but by Bayes' theorem or common sense we are 100% sure $\theta=29$ (p. 465).
- In neither case is the probability that θ lies in the "75% interval" equal to 75% (p. 465). MacKay concludes that (1) many people interpret confidence levels incorrectly, and (2) what people usually want is a Bayesian posterior (p. 465).
- MacKay invites sceptics to try both methods on simulated data in exercise 35.4 and Kepler and Oprea (2001). He challenges readers to let him know if they do not find the Bayesian answer always better, and often much, much better (p. 465). This is his opinion, not something derived here.

*Intuition note.* "75%" describes how the interval-making recipe performs averaged over all possible data. Once you see a particular data set, you may know much more or much less than 75%.

### 37.4 Some compromise positions (p. 466)
- Many sampling theorists are pragmatic: they are happy to choose whichever method has the "best" long-run properties. MacKay proposes offering them Bayesian estimators and Bayesian confidence intervals and asking them to evaluate the sampling properties. Many Bayesian methods turn out to have good ones (p. 466).
- Not all problems are well posed. Model criticism ("am I using an appropriate model?") may be aided by sampling-theory tests with a well-defined null ("the current model is correct") but no specified alternative. P-values could guide the search for the aspects most in need of scrutiny (p. 466).
- Further reading is listed (Jaynes, Gull, Loredo, Berger, Box and Tiao, O'Hagan) (p. 466).

### 37.5 Further exercises (p. 466)
Exercise 37.2 is a Poisson traffic comparison. Exercise 37.3 asks for a program for the vaccine comparison.

## Toy example (ours, not from the text)
Coin tosses give the string `aab`: 2 as and 1 b. We test $\mathcal H_0$: $p_a=1/2$.
- **Design 1: fixed n = 3.** The random variable is $r$, the number of bs. $P(r\le1)=\big(\binom30+\binom31\big)/2^3=(1+3)/8=0.50$.
- **Design 2: stop at the first b.** The random variable is $n$. $P(n\ge3)$ is the probability that the first two tosses are both a, which is $(1/2)^2=0.25$.
- So the p-value is 0.50 or 0.25 for the same string.
- **Likelihood.** The string's probability is $p_a^2(1-p_a)$ under both designs. At $p_a=2/3$ it is $(4/9)(1/3)=4/27$. At $p_a=1/2$ it is $1/8$. The ratio is $(4/27)/(1/8)=32/27\approx1.19$ under both designs. A Bayesian inference built from this likelihood is the same under both.

## Concepts
- [[frequentist-vs-bayesian]] — here "sampling theory" judges methods by long-run behaviour over repeated experiments, and "Bayesian" computes probabilities of hypotheses given the data (p. 457)
- [[p-value]] (new) — the probability, under the null, of an outcome as or more extreme than the observed one; not the posterior probability of the null (p. 457)
- [[null-hypothesis-test]] (new) — a test that focuses only on how unexpected the data are under $\mathcal H_0$ (p. 458)
- [[chi-squared-statistic]] (new) — the sum over the counts of (observed − expected)² divided by the expected count, with expectations taken under the null (p. 458)
- [[sampling-distribution]] (new) — the distribution of a statistic over repetitions of the experiment, assuming the null (p. 459)
- [[confidence-interval]] (new) — an interval computed from data. Its level is the fraction of repeated experiments in which it contains the true θ, for every θ (p. 464)
- [[stopping-rule]] (new) — the experimenter's rule for when to stop collecting data; it changes sampling-theory p-values (p. 463)
- [[likelihood-principle]] (new) — as MacKay uses it, the stopping rule is not relevant to what the data tell us about the parameter (p. 464)
- [[likelihood]] — the probability of the data as a function of the parameters, e.g. (37.12) (p. 460)
- [[prior-distribution]] — here a uniform prior on each probability (p. 460)
- [[posterior-distribution]] — gives P(pA+<pB+|Data) by integration over a region (p. 461)
- [[marginal-likelihood]] — the probability of the data under a model, used as the evidence for model comparison (p. 462)

## Canonical instances
- [[microsoftus-vaccine-trial]] — χ² p ≈ 0.07 versus Bayesian P(pA+<pB+) = 0.990 (pp. 458–461)
- [[bloggs-coin-stopping-rule]] — same data, p = 0.07 or 0.03 depending on stopping rule (pp. 462–464)
- [[integer-theta-confidence-interval]] — a 75% interval with posterior probability 50% or 100% (pp. 464–465)

## Bridges (candidates)
- [structural-analogy] Confidence interval ↔ bayesian: credible interval — both give an interval, but one has coverage over repeated data and the other has posterior probability for this data set.
- [structural-analogy] Stopping-rule irrelevance ↔ bayesian: sequential updating — the spies update after each toss, and only the data seen matter.
- [same-math] Each term P(D|H0), P(D|H1) in the ratio (37.26) ↔ bayesian: marginal likelihood (evidence) — each is the data probability averaged over the prior (37.19, 37.22).

## Questions this raises
- How would the vaccine posterior change with a prior that expects pA+ and pB+ to be similar (p. 460)?
- If p-values depend on the stopping rule, which sampling-theory properties do Bayesian methods keep, and how are they evaluated (p. 466)?
- How can p-value-based model criticism be done without specifying an alternative model (p. 466)?
- What would the sampling properties of a Bayesian interval look like on the integer example?

## Exercises worth doing
- Ex. 37.1 (p. 463) — Bayesian inference about $p_a$ for the coin, and whether it depends on the stopping rule — difficulty: easy
- Ex. 37.2 (p. 466) — Poisson rates from 12 vehicles/hour versus 9 vehicles/half-hour; compare $\lambda_S$ and $\lambda_F$ — difficulty: medium
- Ex. 37.3 (p. 466) — program the vaccine comparison and compute the three probabilities — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 469 = printed 457). The pages are the chapter in full.
- The text layer is garbled for some equations. I checked (37.27) and the others against the page images.
- Eq. (37.5) is written $f_+=1/10$, $f_-=9/10$ without hats, though these are the estimates of (37.4).
- Possible misprint: p. 461 and the caption of fig. 37.4 say "$p_{A+}<10\,p_{B+}$" for "A is ten times more effective than B". The image shows a narrow shaded triangle near $p_{A+}=0$. That looks like $p_{A+}<p_{B+}/10$, not the larger region $p_{A+}<10\,p_{B+}$. Exercise 37.3 uses the same notation.
- Figures 37.1–37.2 are plots; only the axis ticks are labelled, so no values can be read off them. The values 0.990 and 0.03 are as printed.
- The page does not say which χ² value camp two uses. The p-value 0.07 lies between the 0.10 and 0.05 critical values (2.71 and 3.84), which fits the Yates value 3.33 but not 5.93 (above 3.84).
- Sections 3.2–3.3, exercises 3.15 and 35.4 and Kepler and Oprea (2001) are cited but not included in these pages.
