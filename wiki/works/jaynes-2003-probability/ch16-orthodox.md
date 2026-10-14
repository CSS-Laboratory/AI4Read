---
id: jaynes-2003-probability/ch16-orthodox
work: jaynes-2003-probability
unit: "16 Orthodox methods: historical background"
pages: 490-508
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Orthodox methods: historical background

## L0 — One line
Jaynes argues that the "orthodox" statistics of about 1900–1970 answered pre-data (sampling-distribution) questions while claiming to answer post-data ones, and he links its course partly to the problems it faced and partly to personalities and ideology.

## L1 — The gist (≤ 120 words)
Jaynes asks why 'orthodox' statistics dominated about 1900–1970 and what is wrong with it. In his account, it grew from problems like Fisher's biological ones, offered unconnected recipes, and rested on a frequency-only view of probability. He argues this confines it to pre-data questions, while scientists need post-data ones. He says its answers match Bayesian ones mostly through mathematical accidents such as symmetry, as with Gaussian sampling, and diverge for Cauchy sampling. He also argues it is biased against real effects. He thinks personalities (Fisher, Jeffreys, Neyman) played a part. This chapter is history and opinion; the technical comparison comes in Chapter 17.

**Prerequisites:** *Estimator*: a function of the data used to guess a parameter. *Sampling distribution*: its distribution over repeated data sets. *Pre-data*: reasoning before seeing the data. *Post-data*: reasoning given the data in hand. *Posterior*: probability of a parameter given the data (Bayes' theorem). *Gaussian*: bell-curve model; *Cauchy*: heavy-tailed model (16.10). *Nuisance parameter*: unknown parameter not of interest. Taylor expansion; Gaussian integrals.

## L2 — Key ideas
- Jaynes dates "orthodox statistics" from about 1900 (non-physicists take over) to about 1970 (Bayesian revolution); before that, inference was Laplace's Bayesian theory (pp. 490–491).
- Orthodoxy was a set of ad hoc recipes (Fisher's cookbook; Neyman–Pearson methods) without unifying principles, and Jaynes says its defenders offered slogans rather than arguments against probability as logic (pp. 492–493).
- In Jaynes's telling, the Fisher–Jeffreys conflict came partly from different problems (biology with no prior information; geophysics with much) and, he thinks, partly from personalities (pp. 493, 496–498).
- Jaynes says orthodoxy is limited to pre-data questions, and rests on attributing "randomness" to Nature (his "mind projection fallacy"); virtually all real problems are post-data (pp. 499–500).
- Jaynes says Gaussian sampling with no cogent prior information makes pre- and post-data answers coincide; for Cauchy sampling they differ and orthodoxy has found no satisfactory estimator (pp. 501–503).
- Jaynes argues orthodox methods are biased against real effects; he grants the historical need for skepticism (pp. 503–505).
- Jaynes calls belief in "stochastic processes" with no causes another mind projection fallacy (pp. 505–506).
- Jaynes argues that with unified principles and computers each scientist can be his own statistician; loaded terms like "unbiased" hindered progress (pp. 506–508).

## L3 — Walkthrough

### 16.1 The early problems (pp. 490–491)
- Inference began in the 18th–19th centuries from astronomy and geodesy, with Daniel Bernoulli, Laplace, Gauss, Legendre and Poisson, described as mathematical physicists. Its peak under Laplace was a 'Bayesian' theory (p. 490).
- About 1900 non-physicists "moved in". Jaynes says they treated probability as a physical theory of 'chance' with no link to logic, and statistical inference as a separate field. It seemed they could not agree on the new principles, or on whether inference was deductive or inductive (p. 491).
- Early problems: estimate location parameters $\theta$ from $D=\{x_1,\dots,x_n\}$ with $p(x|\theta)=f(x-\theta)$ (p. 491).
- A scale problem is approximately a location problem if $x,\sigma$ are already known to be about $x_0,\sigma_0$. Put $q\equiv x-x_0$, $\delta\equiv\sigma-\sigma_0$ and keep only the linear term in $\delta$:
$$\frac{x}{\sigma}=\frac{x_0+q}{\sigma_0+\delta}=\frac{1}{\sigma_0}\,(x-\theta+\cdots),\qquad \theta\equiv x_0\delta/\sigma_0 \tag{16.1}$$
(added step: $(x_0+q)(1-\delta/\sigma_0)\approx x_0+q-x_0\delta/\sigma_0$, and $x_0+q=x$.) Then define
$$h(x-\theta)\propto f(x/\sigma) \tag{16.2}$$
so "almost any problem" can be linearized this way when the quantities are known fairly well (p. 491).
- Only late in the 19th century did practice reach joint location and scale estimation,
$$p(x|\theta\sigma)=f\!\left(\frac{x-\theta}{\sigma}\right)\frac{1}{\sigma} \tag{16.3}$$
and Galton's bivariate Gaussian work. Virtually all orthodox development concerned these three problems or their hypothesis-testing versions, most of it only the first (p. 491).

*Intuition note:* When a quantity is already roughly known, only a small correction remains. A small change in a scale then acts like a shift, so location methods cover many problems.

### 16.2 Sociology of orthodox statistics (pp. 492–493)
- Without unifying principles, scientists got "cookbook" recipes. Fisher's *Statistical Methods for Research Workers* (1925; 13 editions to 1960) became so authoritative that in some fields, such as medical testing, work failing to follow it was hard to publish (p. 492).
- Fisher's recipes: maximum likelihood, ANOVA, fiducial distributions, randomized design, significance tests. The Neyman–Pearson school: unbiased estimators, confidence intervals, hypothesis testing. Together these are "orthodox statistics". Jaynes says the absence of a shared criterion perpetuated the split (p. 492).
- Jaynes compares the statistician–client relation to doctor–patient. He says it was workable for simple problems. He would not criticize it had its proponents behaved like good doctors, admitting the true causes are unknown. Instead they were militant (p. 492).
- Jaynes says Fisher (1956) and Kendall attacked Neyman and Wald for seeking unifying principles in decision theory. He says Fisher, Cramér, Feller, Neyman, von Mises and even the putative Bayesian Savage accused Laplace and Jeffreys of "metaphysical nonsense" for treating probability theory as an extension of logic. He says they did not examine Cox's consistency work, Pólya's qualitative correspondence with common sense, or Jeffreys' practice, and gave only slogans about 'subjectivity' and 'objectivity' (p. 493).
- Jaynes cannot explain why James Bernoulli and Keynes escaped scorn. He concludes that personalities "must have had something to do with" events (p. 493).

### 16.3 Fisher, Jeffreys, Neyman (pp. 493–499)
- **Logic vs orthodox view of estimation.** Jaynes: probability as logic computes $p(\theta|DI)$. **Orthodox view (as Jaynes reports it):** this is meaningless because $\theta$ is an unknown constant, not a frequency. Instead pick an estimator $f(D)$ and judge it only by its sampling distribution $p(f|\theta)$, a limiting frequency over repeated draws (p. 493).
- With no general principle, orthodoxy guesses estimators and tests them by sampling distributions, so computing these is central (p. 494). Fisher was very good at it. Jaynes notes that Fisher spent 1912–1913 with James Jeans, who was working with high-dimensional Gaussian (Maxwellian) distributions (p. 494).
- Jaynes says Jeffreys bypassed these calculations in a few lines. With no cogent and detailed prior information, the best estimators come from the likelihood function, written down by inspection of $p(D|\theta)$. Jaynes calls Fisher's calculations unnecessary for conducting inference (p. 494).
- Fisher's later dominance, Jaynes says, came less from technical work than from personal style and institutional power. Jeffreys worked modestly as a geophysicist, with one doctoral student in probability (pp. 494–495).
- Jaynes says Fisher held that 'probability' means only limiting frequency, usually stated as a ratio of two infinite numbers. Jaynes says this "conceivably" came from Venn. In his last book (1956) Fisher defended Laplace against Venn, and his criticisms of Jeffreys were toned down. Some have opined he would be a Bayesian today (p. 495).
- Footnote 2: in 1962 Fisher published an article examining possibilities of Bayesian methods with priors "determined experimentally". Jaynes says this shows he never accepted, and probably never comprehended, Jeffreys' view of priors (p. 495).
- Jaynes describes the pattern of Fisher's inference papers: polemic against inverse probability, then an intuitive correct solution, ending abruptly just before the step that would show he was rediscovering Bayes' theorem (p. 495).
- Footnote 1: Jaynes judges Fisher's technical criticisms of Pearson and of Neyman justified. He thinks Fisher was wrong in his disputes with Gosset over randomization and with Jeffreys over the meaning of inference (p. 495).
- Jeffreys (1939) derived Fisher's results more easily, with their range of validity and generalizations. Jaynes says he was met with attacks on ideology: his "sin" was not requiring probability to be a frequency. Nobody saw that this broader conception gave his computational advantages (p. 496). Neyman rejected Jeffreys on the same grounds. Jaynes says a five-balls-in-two-urns dispute (Neyman 1952, p. 11 of his paper) is one where Jeffreys is clearly right (p. 496).
- **Different problems.** Fisher's biology had no prior information or guiding theory and resembled urn draws. Jeffreys' geophysics had much prior information and no population (p. 496). Neyman said that modern statistics was developed under pressure from biologists, so almost nothing in it applies directly to astronomy (pp. 496–497).
- Jaynes says Jeffreys saw Fisher's problems as trivial, the simplest applications of Bayes' theorem. Fisher would have been nearly helpless, and Neyman completely helpless, with many nuisance parameters and no sufficient or ancillary statistics. Neither treated linear regression with both variables in error; Jaynes says Bayesian methods handle nuisance parameters as minor details (p. 497).
- Footnote 3: Jaynes calls Fisher's randomized planting "not actually wrong" but hopelessly inefficient. He says it appears to be a quite general principle that any randomized method has a nonrandomized one with better performance that requires more thought (p. 497).
- Jaynes thinks that had Fisher tried harder problems he would have seen Jeffreys' power "rather quickly". He says Fisher never exhibited a problem where his methods worked and Jeffreys' did not, since Fisher's methods are special cases of Jeffreys' (pp. 497–498).
- Personalities. Jaynes cites Fisher's rages and a remark by one of his disciples (Kendall is given as an example) that "Whenever he paints a portrait, he paints a self-portrait" (p. 497). He contrasts Jeffreys' composure and humor, which he says Maxwell and Einstein shared (pp. 497–498).
- **The one-third argument.** Jeffreys (1932) derived the $d\sigma/\sigma$ prior from the predictive density for a third Gaussian observation:
$$p(x_3|x_1x_2I)=\int d\mu\int d\sigma\; p(x_3|\mu\sigma I)\,p(\mu\sigma|x_1x_2I). \tag{16.4}$$
If $\sigma$ is initially completely unknown, estimates of $\sigma$ ought to follow $|x_2-x_1|$. Then the probability that $x_3$ lies between $x_1$ and $x_2$ ought to be $1/3$, independently of $x_1,x_2$. With independent sampling every permutation of the three observations is equally probable. Jeffreys shows this holds only for the $d\sigma/\sigma$ prior (p. 498).
- Jaynes says Fisher (1933) took this to be a claim about the sampling distribution $p(x_3|\mu\sigma I)$, a different thing, and wrote seven pages of attack. Jaynes says Jeffreys saw the issue as the incompleteness of Fisher's methods and his unjustified premises: a hypothetical infinite population and an objectively "true" probability independent of human information. Jeffreys' aim was to use probability to represent human information (p. 498).
- Jeffreys complained that Fisher had "reduced his work to nonsense"; Fisher replied, "I am not inclined to deny it" (pp. 498–499). Geisser thinks Jeffreys came off second best. Jaynes sees Jeffreys smiling at a trap (p. 499).
- **Induction.** Neyman claimed his reasoning was entirely deductive (1952), though he spoke of "inductive behavior" in 1950. Fisher and Jeffreys denied that inference avoids induction, and denied Popper's claim that induction is impossible (p. 499).
- Fisher (1956), Stigler (1983) and Zabell (1989) give evidence that Bayes had his result by 1748 and was motivated by annoyance at Hume's claim that induction is impossible. Jaynes says this evidence is "just short of proof" (p. 499). Jaynes's own conjecture: Bayes sought a counter-example, found it harder than expected, and delayed publishing (p. 499).

*Intuition note:* Jaynes says orthodoxy's mathematical effort on estimator sampling distributions was a detour: if you can write down the likelihood, you can get the estimate directly. The 1/3 exchange shows the confusion between a predictive distribution (about the next observation, given the data) and a sampling distribution (about data, given parameters).

### 16.4 Pre-data and post-data considerations (pp. 499–500)
- Orthodox practice is limited at the outset to pre-data questions: (A) what data do you expect before seeing them? (B) if an algorithm will estimate parameters from not-yet-seen data, how accurate do you expect it to be? (C) if the hypothesis is true, what is the probability of data indicating it is true? (p. 499).
- Probability as logic includes all sampling-distribution calculations, so the numbers agree where these questions are the ones wanted (p. 500).
- Jaynes says virtually all real problems of scientific inference are post-data: (A′) any reason to be surprised by the data now? (B′) what estimates and accuracy now? (C′) probability, given the data, that the hypothesis is true? (p. 500).
- Jaynes says orthodoxy's basic tenet attributes the need for inference to 'randomness' in Nature rather than human ignorance, which he calls the "mind projection fallacy". This leads to the belief (orthodoxy's, as Jaynes reports it) that probability statements can be made only about 'random variables', not unknown fixed parameters (p. 500).
- Jaynes says orthodoxy has never given a usable definition of "random variable" (e.g. beans in a can). Data are always treated as random and almost everything else as not; to the best of his knowledge, no principle of orthodox statistics would let one predict this choice. He says the opposite choice would seem far more natural, since in a real situation the data are usually the only things that are definite and known. So orthodoxy admits no prior or posterior probability for a parameter or hypothesis. It passes off pre-data answers as post-data ones mostly through mathematical accidents, such as symmetry in parameter and estimator (p. 500).

### 16.5 The sampling distribution for an estimator (pp. 500–503)
- Jaynes says orthodoxy has no other criterion for estimators. In Bayesian analysis, an estimator derived from Bayes' theorem and a specified loss function is optimal for the problem as defined, whatever its sampling distribution. The sampling pdf plays no functional role post-data. It matters for pre-data tasks such as planning an experiment or deciding when to stop (p. 501).
- (Q1) If the sampling pdf equals long-run frequencies, its width tells how much the estimate varies over all data sets we might get. (Q2) The scientist wants to know how accurately the one data set $D$ determines $\alpha$. Jaynes says the answer to Q2 is the width of the posterior pdf (p. 501).
- **Gaussian case**, $\sigma$ known (p. 501):
$$p(D|\mu\sigma I)\propto\exp\Big\{-\sum_i\frac{(y_i-\mu)^2}{2\sigma^2}\Big\}\tag{16.5}$$
$$p(\mu|D\sigma I)\propto\exp\Big\{-\frac{n(\mu-\bar y)^2}{2\sigma^2}\Big\}\quad\text{(uniform prior)}\tag{16.6}$$
$$(\mu)_{\rm est}=\bar y\pm\frac{\sigma}{\sqrt n}\tag{16.7}$$
(added step: $\sum_i(y_i-\mu)^2=\sum_i(y_i-\bar y)^2+n(\mu-\bar y)^2$.) The mean $\bar y\equiv n^{-1}\sum y_i$ is a sufficient statistic. An orthodoxian using $\bar y$ finds
$$p(\bar y|\mu\sigma I)\propto\exp\Big\{-\frac{n(\bar y-\mu)^2}{2\sigma^2}\Big\}\tag{16.8}$$
$$(\bar y)_{\rm est}=\mu\pm\frac{\sigma}{\sqrt n}\tag{16.9}$$
(p. 502). The meanings differ, but they are mathematically so nearly identical that both make the same numerical estimate and accuracy claim. Where there are sufficient statistics but no nuisance parameters, a mathematical symmetry (approximate or exact) can make pre- and post-data answers closely related, if there is no cogent prior information to break it. With no prior information the Gaussian symmetry is exact (p. 502).
- Jaynes says this accident gave a distorted picture and let orthodoxy claim general validity on limited evidence (p. 502).
- **Cauchy case:**
$$p(y|\mu)=\frac1\pi\left[\frac{1}{1+(y-\mu)^2}\right]\tag{16.10}$$
With an uninformative prior the posterior is
$$p(\mu|DI)\propto\prod_{i=1}^n\frac{1}{1+(\mu-y_i)^2}\tag{16.11}$$
Posterior mean ± s.d. or median ± interquartile range are easily found by computer. There is no sufficient statistic and no good analytical solution (p. 502). Jaynes says orthodoxy has never found a satisfactory estimator here. The sampling pdf of the sample mean is
$$p(\bar y|\mu I)\propto\frac{1}{1+(\bar y-\mu)^2}\tag{16.12}$$
identical with (16.10), so by orthodox criteria the mean of any number of observations is no better than one (pp. 502–503).
- Fisher noted that for large samples the median tends to be more strongly concentrated near $\mu$ than the mean. Jaynes says this does not show it is best, and the question is open. He expects the Bayesian posterior mean and median would prove considerably better, by orthodox criteria, than any known orthodox estimator. Computer experiments could test this, but he doubts they will be done (p. 503).
- Footnote 4: Jaynes's analysis of Bayesian Cauchy estimation was twice rejected (a referee called Cauchy "pathological"). It appeared after 13 years (Jaynes 1976). He says that to his knowledge Bayesian analysis has no pathological cases (p. 503).

*Intuition note:* Gaussian: the spread of $\bar y$ around $\mu$ and the uncertainty of $\mu$ around $\bar y$ have the same size, so the two questions get the same number. Cauchy: averaging does not narrow the sampling distribution, but the posterior still depends on the actual data.

### 16.6 Pro-causal and anti-causal bias (pp. 503–505)
- Jaynes says orthodox methods have technical shortcomings (wasted information) that in practice all tend to bias inference in the same direction (to be shown in Chapter 17). Testing for a new phenomenon, orthodoxy in effect treats accepting an unreal one as a calamity but is unconcerned about missing a real one (p. 503).
- Historical context: the untrained mind sees causes in coincidence. Jaynes cites Kepler's horoscopes, Laplace's and Helmholtz's warnings, Pasteur and spontaneous generation, hundreds of "miraculous" plants, poison ivy "effluvium" (still reported in 1910), rice cooking, climate scares, and 1991 fears about 60 Hz fields and cancer (pp. 503–504). So he sympathizes with orthodox conservatism (p. 504).
- But skepticism can go too far. Jaynes says an orthodox significance test would have dismissed as random error the small surprises behind Rayleigh's argon and Hess's cosmic rays. These discoverers then investigated carefully (pp. 504–505). Footnote 5 (Jeffreys): a significance test that ignores alternatives would always have rejected Newton's law, and rejection was rational only once Einstein's alternative made precise predictions (p. 504).
- Jaynes says editorial policies may block first evidence that misses a significance level, though three or four data sets together might be overwhelming. How editors can allow many-step discovery without publicity-seeking is "genuinely difficult"; he does not claim a full answer. He says Bayesian analysis of all the evidence would give more defensible conclusions, and Bayesian editorial standards "would go a long way" toward solving the publication problem (p. 505).
- Jaynes says Feller and others ridicule "cycle hunters" without documented examples. Fisher, Feller and Tukey (orthodox methods) do not find business cycles; Burns sees them by eye; Bretthorst's probability-as-logic analysis may or may not. Jaynes says some orthodox skeptics miss real effects because their methods ignore prior information and violate the likelihood principle (p. 505).

### 16.7 What is real, the probability or the phenomenon? (pp. 505–506)
- Jaynes says orthodox reluctance to see causes becomes belief in 'stochastic processes' with no causes. Treating "stochastic" as a real physical property independent of human information is another mind projection fallacy (p. 506).
- "Gaussian random process fully determined by first and second moments" is harmless as a definition of an abstract model. Jaynes objects to its being presented as a fact about real processes, which would discourage looking for causes (p. 506).
- He says every disease and machine failure has a specific cause, as Pasteur understood. Medicine and crash investigators seek individual causes, not only statistics (p. 506).

### 16.8 Comments (pp. 506–508)
- Jaynes sees the scientist–statistician relation changing, because of better theory and computers. A scientist who knows the unified principles can do his own analysis (pp. 506–507).
- Scientists must compromise between seeing too little and too much. Jaynes says only methods using all relevant prior information, all previously obtained data and the whole likelihood function can do this. Probability as logic cannot mislead unless fed false information or denied true relevant information (p. 507).
- He says orthodox methods have often missed obvious effects and, more rarely, "hallucinated" nonexistent ones (p. 507).

**16.8.1 Communication difficulties.**
- Theorem: the posterior expectation minimizes expected squared error. Footnote 6 proof, with $\theta^*(x_1,\dots,x_n)$ any estimator and averages over the posterior of $\theta$:
$$\langle(\theta^*-\theta)^2\rangle=(\theta^*-\langle\theta\rangle)^2+(\langle\theta^2\rangle-\langle\theta\rangle^2),$$
minimized at $\theta^*=\langle\theta\rangle$ (p. 507).
- **Objection (a sampling theorist):** an estimator is a function of the data, an expectation is an average over all possible data and a function of the parameter, so "apples are oranges". Jaynes says he denied any posterior distribution, so "posterior expectation" meant nothing to him. Jaynes leaves open how to reply without losing contact (p. 507).
- Savage compared such breakdown to the Tower of Babel; Jaynes says computation lets us settle issues by demonstrating performance (p. 508).
- Jaynes says 1930s–40s frequentists used virtuous-sounding terms (unbiased, efficient, admissible, robust), almost forcing others to use "sinful" antonyms. He says these methods were ad hoc, with defects Bayesian methods overcome. A biased estimate may be much closer to the truth than an unbiased one, and an inadmissible procedure far better than an admissible one (shown in Chapter 17) (p. 508).

## Toy example (ours, not from the text)
**Gaussian.** $\sigma=2$ known, data $3,5,4,6$, $n=4$. $\bar y=18/4=4.5$; $\sigma/\sqrt n=2/2=1$. Bayesian (16.7): $\mu=4.5\pm1$. Orthodox (16.9): $\bar y$ has spread 1 around $\mu$, so with $\bar y=4.5$ one reports $4.5\pm1$. Same numbers, different meanings.

**Cauchy.** $n=2$, data $0$ and $10$, so $\bar y=5$. By (16.12), $\bar y$ is spread like a single observation. The second observation did not narrow it. Posterior (16.11), unnormalized:
- $\mu=0$: $1/[(1+0)(1+100)]=1/101\approx0.00990$;
- $\mu=5$: $1/[(1+25)(1+25)]=1/676\approx0.00148$;
- $\mu=10$: $1/[(1+100)(1+0)]\approx0.00990$.

The posterior is about $0.00990/0.00148\approx6.7$ times lower at the midpoint 5 than at 0 or 10. It reflects the two far-apart data values, which the pre-data statement about $\bar y$ cannot show.

## Concepts
- [[orthodox-statistics]] (new) — Jaynes's name for the Fisher and Neyman–Pearson recipes, c. 1900–1970 (p. 492)
- [[frequentist-vs-bayesian-inference]] — orthodoxy: probability only as frequency of random variables; Jaynes: probability represents information (pp. 493, 498)
- [[probability-as-extended-logic]] — Laplace–Jeffreys view that orthodox critics attacked (p. 493)
- [[cox-theorem]] — consistency work Jaynes says critics did not examine (p. 493)
- [[estimator]] (new) — orthodox: a function $f(D)$ of the data, judged by its sampling distribution (p. 493)
- [[sampling-distribution]] (new) — $p(f|\theta)$, a limiting frequency over repeated draws (p. 493)
- [[pre-data-vs-post-data]] (new) — questions A–C versus A′–C′ (pp. 499–500)
- [[posterior-distribution]] — $p(\theta|DI)$; its width answers Q2 (p. 501)
- [[likelihood]] — per Jaynes, with no cogent and detailed prior information, the likelihood determines Jeffreys' best estimators (p. 494)
- [[posterior-predictive-distribution]] — (16.4), the density of a new observation given the data (p. 498)
- [[mind-projection-fallacy]] (new) — Jaynes: attributing one's ignorance to Nature, e.g. "randomness" or "stochastic" processes (pp. 500, 506)
- [[sufficient-statistic]] (new) — not defined here; $\bar y$ is called one in the Gaussian case (p. 501)
- [[nuisance-parameter]] (new) — unknown parameter not of interest; named as orthodoxy's difficulty (p. 497)
- [[likelihood-principle]] (new) — named as violated by orthodox methods; shown in Ch. 17 (p. 505)

## Canonical instances
- [[gaussian-pre-post-coincidence]] (new) — (16.7) and (16.9) give the same numbers with no cogent prior information (p. 502)
- [[cauchy-sample-mean]] (new) — $\bar y$ no better than one observation (pp. 502–503)
- [[jeffreys-one-third-argument]] (new) — the 1/3 predictive argument for $d\sigma/\sigma$ (p. 498)
- [[argon-cosmic-rays]] (new) — discoveries Jaynes says a significance test would have dismissed as random error (p. 504)
- [[posterior-mean-minimizes-squared-error]] (new) — footnote 6 (p. 507)

## Bridges (candidates)
- [same-math] Footnote 6: $\langle(\theta^*-\theta)^2\rangle=(\theta^*-\langle\theta\rangle)^2+\text{variance}$ ↔ statistics: the bias–variance split of mean squared error.
- [structural-analogy] Pre-data vs post-data ↔ information theory: average code quality over all sources vs code length of the message actually sent.
- [same-math] (16.12) ↔ probability: the Cauchy density is unchanged under averaging.

## Questions this raises
- When is "symmetry in parameter and estimator" exact, and what breaks it?
- Would the computer experiment Jaynes proposes (posterior mean and median vs orthodox estimators under Cauchy sampling) support his conjecture?
- How should journals treat a first data set that is suggestive but misses a significance level?
- Is the one-third argument enough to single out $d\sigma/\sigma$?

## Reading notes
- Printed = pdf − 30 (pdf 520 = p. 490). Page labels give printed numbers.
- Equations (16.1)–(16.12) and footnote 6 were checked against page images. Bracket and sign details are as printed.
- "Feinberg and Hinkley (1980)" is as printed (p. 494). "Orthodoxian" is Jaynes's term.
- The unit has no exercises. Several claims are Jaynes's opinion or conjecture (the median/mean experiment, Bayes and Hume, Fisher "would be a Bayesian"); I have tagged them as his.
