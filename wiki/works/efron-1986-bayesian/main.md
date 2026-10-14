---
id: efron-1986-bayesian/main
work: efron-1986-bayesian
unit: paper
pages: 1-5
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Why Isn't Everyone a Bayesian? (Efron 1986)

## L0 — One line
Efron argues that Fisherian and frequentist methods have so far outweighed Bayesian ones in practice, mainly because they are easy to use, attend to model building, let a problem be split into pieces, and hold the high ground of objectivity, even though the Bayesian argument is cogent.

## L1 — The gist (≤ 120 words)
Efron asks why most scientific data analysis is non-Bayesian, although the Bayesian argument is cogent. He answers mainly with practical examples in which a Bayesian approach is difficult but a Fisherian or frequentist solution is relatively easy: a median interval, a ".05 level" test, and a heart-attack classification tree. He then discusses objectivity: intuitively "fair" frequentist ideas are very popular, while objectivity inside Bayesian theory turns out to be hard. He lists four reasons: ease of use, model building, division of labor, and objectivity. In his opinion none is insurmountable, but a lot more Bayesian effort will be needed.

**Prerequisites:** prior, posterior, likelihood; confidence interval; maximum likelihood; normal distribution; order statistics (the sorted sample values); "frequentist" (judging a method by averages taken with the true parameter fixed); "flat prior" (spreads probability evenly over all parameter values); "coverage" (how often an interval contains the true value); bootstrap (a resampling check).

## L2 — Key ideas (5–10 bullets)
- Everyone used to be a Bayesian (Laplace; most 19th-century scientists, including Gauss), and modern theory (Savage, de Finetti) gives powerful reasons to prefer Bayes. Yet 20th-century statistics is mainly non-Bayesian, and this is the puzzle (p. 1).
- Fisher's theory (R. A. Fisher's likelihood-based approach) works by reduction to "archetypes" such as $x\sim N(\theta,1)$. Maximum likelihood is automatic and, in experienced hands, rarely goes far wrong, while Bayes needs a great deal of thought about each situation (p. 1).
- The NPW (Neyman–Pearson–Wald) school, also called the frequentists, solves a narrow piece of a problem that is judged most relevant. Bayesians criticize this as incoherent. Efron replies that the accusation cuts both ways: to be coherent, Bayesians have to solve all problems at once, an often impossible exercise (p. 2).
- The .05-level test is popular because, Efron says, it is often easier to compare quantities than to assign them absolute values. A Bayesian "7 to 1" odds statement is more satisfactory but needs more input: it tacitly implies an absolute scale of evidence (p. 2).
- In the heart-attack tree, the apparent 96.7% success rate becomes about 70% in a bootstrap analysis. The way the tree was built has no effect on the likelihood, so it makes no difference to a Bayesian, but it makes a great difference to a frequentist. Efron then writes that "This is incoherent behavior" (pp. 2–3).
- In Efron's opinion, objectivity is the linchpin of non-Bayesian success with practitioners. Subjective Bayesianism has failed to make much of a dent in scientific practice (p. 3).
- Objective Bayes is hard: the flat prior does well for one normal mean but gives poor frequentist coverage for $\theta_1\theta_2$, and the right objective prior seems to depend on the parameter of interest. This is not hopeless (p. 4).
- Four reasons for Fisherian and NPW dominance: ease of use, model building, division of labor, objectivity. Some Bayesian efforts exist on all four; in Efron's opinion a lot more will be needed (p. 4).

## L3 — Walkthrough

### Abstract and 1. Introduction (p. 1)
- The paper began as a talk at a conference on Bayesian statistics. The abstract says the argument consists mainly of practical examples where the Bayesian approach is difficult but Fisherian/frequentist solutions are relatively easy. A brief discussion of objectivity follows, and a closing list of practical advantages that, so far, seem to have outweighed the philosophical superiority of Bayesianism (p. 1).
- Why the title is a fair question (p. 1):
  - Everyone used to be a Bayesian. Laplace endorsed Bayes's formulation and most 19th-century scientists followed, including Gauss.
  - The Bayesian argument is cogent. Following Savage and de Finetti, modern statisticians have advanced powerful reasons for preferring Bayes, and a byproduct is a disturbing catalogue of inconsistencies in the frequentist view.
  - Still, the current era is the first century in which statistics has been widely used for scientific reporting, and 20th-century statistics is mainly non-Bayesian. Lindley (1975) predicts a change for the 21st. Efron asks: what has happened?

### 2. Two powerful competitors (p. 1)
- The competitors are Fisherian theory and what Jack Kiefer called the Neyman–Pearson–Wald (NPW) school of decision theory, whose constituents are also known as the frequentists.
- Fisher invented his theory, and to a remarkable degree completed it, between 1920 and 1935. NPW began with the famous lemma of 1933 and was "asymptoting" in the 1950s, though significant advances have continued (Stein estimation, empirical Bayes, robustness theory).
- Working together in rather uneasy alliance, Fisher and NPW dominate current theory and practice, with Fisherian ideas particularly prevalent in applied statistics. Efron says he will try to explain why.

### 3. Fisherian statistics (p. 1)
- In its inferential aspects, Fisherian statistics lies closer to Bayes than to NPW in one crucial way: the assumption that there is a *correct* inference in any given situation.
- Example: a sample $x_1,\dots,x_{20}$ from a Cauchy distribution with unknown center $\theta$. In the absence of prior knowledge, the correct 95% central confidence interval is, to a good approximation, $\hat\theta \pm 1.96/\sqrt{-\ddot\ell_{\hat\theta}}$. Here $\hat\theta$ is the maximum likelihood estimator (MLE) and $\ddot\ell_{\hat\theta}$ is the second derivative of the log-likelihood at $\hat\theta$ (see Reading notes).
- The (mathematically) equally good approximation $\hat\theta\pm 1.96/\sqrt{I_0}$, with $I_0$ the *expected* Fisher information, is not correct (Efron and Hinkley 1978).
- Fisher's theory is a theory of archetypes: the correct inference is divined by reducing a problem to an archetypal form where the correct inference is obvious. The first and simplest archetype is inference about $\theta$ from one observation in the normal model
$$x\sim N(\theta,1).\tag{1}$$
  Sufficiency, ancillarity, permutation distributions and asymptotic optimality theory are among Fisher's inventions, all intended to reduce complicated problems to something like (1). Fisher's work superseded an earlier archetypal system, Karl Pearson's method of moments and families of frequency curves.
- Why so much applied statistics is Fisherian: one big reason is the theory's automatic nature. Maximum likelihood is the original jackknife, in Tukey's sense of a widely applicable and dependable tool. Faced with a new situation, the working statistician can apply it automatically, with little chance (in experienced hands) of going far wrong and considerable chance of a nearly optimal inference. He does not need to think much about the specific situation to get on toward a solution.
- Bayesian theory requires a great deal of thought about the situation to apply sensibly. Efron sees this in the efforts of Novick, Kadane and colleagues, and many others to at least partially automate Bayesian inference. All this thinking is admirable in principle, but not necessarily in day-to-day practice. The same objection applies to some aspects of NPW theory, for instance minimax estimation procedures, with the same result: they are not used very much (pp. 1–2).

> **Intuition note.** Maximum likelihood can be applied to a new situation almost mechanically, and Efron says that in experienced hands it rarely goes far wrong. A Bayesian analysis, he says, needs much thought about the specific situation. He grants this thinking is admirable in principle but not necessarily in day-to-day practice.

**Figure 1 and what statistics is (p. 2).** Efron reprints a diagram of four basic operations. Enumeration (collecting and listing individual data) is at the bottom. Above it, the raw data are reduced to a more understandable form through summary and comparison. This is the part where, usually, the statistician decides on a reasonable probabilistic model. Inference is at the top, with estimation and hypothesis testing drawn beside it. Inference takes us from the data actually seen to data that might be expected in future.
- Bayesian theory concentrates on inference, the most glamorous part of statistics, but not necessarily the most important.
- Fisher paid a lot of attention to the earlier steps. Randomization and experimental design concern how data should be collected. Maximum likelihood is a provably efficient way to summarize data, whatever estimation problems are involved in the final inference (Efron 1982b). The NPW school also contributed to enumeration (survey sampling, efficient experimental design).
- Fisher's theory culminated in fiducial inference. To Efron and most current observers it looks like a form of objective (as opposed to subjective) Bayesianism. It is alone among Fisher's major efforts in failing to enter common use. In its place, the NPW theory of confidence intervals dominates practice, despite some serious logical problems in its foundations (p. 2).

### 4. The NPW school (pp. 2–3)
- Unlike Bayes and Fisher, NPW does not insist on a correct solution for a given situation. A part judged most relevant to the investigator is split off, stated in narrow mathematical form and, it is hoped, solved.
- Under model (1), the correct Bayesian or Fisherian inference for $\theta$ leads directly to the correct inference for $\gamma=1/(1+\theta)$. This is not necessarily so in the NPW formulation. Efron asks: what is the uniform minimum variance unbiased estimate of $\gamma$? (p. 2).
- The NPW piecewise approach has been justly criticized by Bayesians (Efron's word) as self-contradictory, inconsistent and incoherent. The work of Savage, de Finetti and their successors shows, Efron says, that no logically consistent inference maker can behave in such a non-Bayesian way. **NPW reply:** there is no reason to believe inference should be logically consistent in the Bayesians' sense, and there are good practical reasons for treating specific problems individually (p. 2).

**Example 1: median interval (p. 2).**
- Setting: a random sample $x_1,\dots,x_{15}$ from a continuous distribution $F$ on the real line. We want an interval estimate for $\theta$, the median of $F$. The experiment is a new one, so very little is known about $F$.
- A genuine Bayesian solution "seems difficult" here, since it requires a prior on the space of all distributions. Frequentist theory gives a simple confidence interval based on order statistics:
$$\theta\in[x_{(3)},x_{(12)}]$$
  with probability .963, whatever $F$ may be.
- Unlike a Bayesian solution, this one does not also solve the corresponding problem for, say, $\phi=$ the 50% trimmed mean of $F$. This does not dismay the frequentist, particularly if a satisfactory Bayesian solution is not available.
- Efron's reply on coherence: the Bayesian accusation of incoherency "cuts both ways". In order to be coherent, Bayesians have to solve all problems at once, an often impossible mental exercise (p. 2).

**Example 2: "rejecting at the .05 level" (p. 2).**
- Its inconsistencies are well documented in the Bayesian literature (Lindley 1982), yet it is one of the most widely used statistical ideas.
- Efron says its popularity is founded on a crucial practical observation: it is often easier to compare quantities than to assign them absolute values. Here the comparison is between the amount of evidence against the null hypothesis provided by different possible outcomes.
- For $H_0: x\sim N(0,1)$ versus $H_1: x\sim N(2,1)$, we know that a larger observed $x$ gives more evidence against $H_0$ and in favor of $H_1$, even if "evidence" cannot be quantified absolutely.
- A Bayes statement of the form "the a posteriori odds ratio is 7 to 1 in favor of $H_1$" is more satisfactory than "the data are significant at the .05 level", but it also requires more input. It tacitly implies that we have assigned an *absolute* measure of evidence to every possible outcome. Absolute here means that "7 to 1" has the same meaning no matter what experiment it came from.
- Good's (1965) Bayes–non-Bayes compromise suggests using Bayesian ideas in a comparative mode. Efron says it is the only example he knows.

> **Intuition note.** A significance test rests on comparing how much evidence against $H_0$ different possible outcomes provide. A posterior-odds statement needs more input: it implies one absolute scale of evidence that means the same across experiments.

**Example 3: heart-attack decision tree (pp. 2–3, Fig. 2).**
- The tree purports to predict coronary patients at high risk of dying (population 2) from variables observed at hospital admission. A series of dichotomous observations is made, for example high or low kinase level, giving a final prediction. Of the 389 patients classified, only 1 of 30 deaths was predicted to live. Efron asks: can we believe the tree has a 96.7% probability of successfully predicting deaths? (pp. 2–3)
- Because the medical investigators had little prior knowledge, the tree was built by an elaborate data-fitting procedure designed to maximize the *apparent* success rate. At each stage, the variable and the splitting point were chosen to give the maximum apparent difference between populations 1 and 2.
- A bootstrap analysis, much like a cross-validation, gave an unbiased estimate of successful prediction of death of about 70% instead of 96.7% (details in sec. 7.6 of Efron 1982a) (p. 3).
- To a Bayesian, the fact that the data were used to construct the tree, and how they were used, makes no difference, since it has no effect on the likelihood function. This is similar in spirit to the fact that a sequential stopping rule has no Bayesian consequence. To the frequentist it makes a great difference. If exactly the same tree had been constructed by a less flexible rule, the unbiased estimate would move closer to the observed 96.7%. Efron then writes "This is incoherent behavior." He adds that the Bayesian estimate, whatever it is, would not change (p. 3). The referent of "this" is not spelled out (see Reading notes).
- "Ad hoc" is a pejorative adjective in Bayesian descriptions of frequentist statistics. Yet ad hoc reasoning produces a reasonable answer here, in a problem that seems far too complicated for a full Bayesian solution. The right to split off the simple part of a complicated inference problem should not be the exclusive property of the frequentists. Efron is not aware of much Bayesian activity along these lines, and the coherency approach of Savage and de Finetti seems to have discouraged it. He cites Boos and Monahan (in press) as a counterexample (p. 3).
- The NPW school invented decision theory, but decision theory is not what separates them from the Bayesians; Bayesians have made good use of it. The parting of the ways is $\theta$ averages: expectations taken with the state of nature $\theta$ fixed, i.e. frequentist calculations. Controlling, or at least computing, them is central to the NPW approach and irrelevant to the Bayesians. This brings Efron to objectivity, in his opinion the linchpin of non-Bayesian success with statistical practitioners (p. 3).

> **Intuition note.** In Efron's account the tree was chosen to maximize its apparent success rate, and the bootstrap estimate is about 70% rather than 96.7%. He says that how the tree was built has no effect on the likelihood, so for a Bayesian the estimate would not change, while for a frequentist it matters a great deal.

### 5. Objectivity (pp. 3–4)
- The dominant Bayesian school, with the legitimate claim to philosophic coherency, is the subjective Bayesianism of de Finetti and Savage. Efron says that, by definition, one cannot argue with a subjectivist, so he simply states what he calls the obvious fact: subjectivism is undoubtedly useful in personal decision making (business, legal decisions) but has failed to make much of a dent in scientific statistical practice. The nature of scientific communication makes him doubt that it ever will (p. 3).
- Scientific objectivity is more than a catch-phrase. Strict objectivity is one of the crucial factors separating scientific thinking from wishful thinking. Complete objectivity about one's own work is a little much to expect from a human being, even a scientist, but it is not too much to expect from one's colleagues. A prime requirement of any statistical theory intended for scientific use is that it reassures oneself and others that the data have been interpreted fairly (pp. 3–4).
- With this in mind, Efron finds it not surprising that intuitively "fair" ideas (unbiasedness, confidence intervals, .05 significance) are immensely popular with the statistical public. Ideas that do not pass the test of objectivity are not much used. This includes NPW ideas as well as Bayesian ones, for example James–Stein estimation. Robust estimation is an interesting borderline case that could go either way depending on how it develops (p. 4).
- Of course, there is no scientific law that says objectivity must be interpreted in a frequentist sense. Another line of Bayesian thought attempts to deal directly with fairness. Efron calls it "objective Bayes theory", to differentiate it from the Savage–de Finetti approach. Bayes and Laplace were objective Bayesians, and in this century Jeffreys (1961) wrote a famous book on the subject. The goal is to produce prior distributions that capture the idea of objectivity (p. 4).

**Situation (1) again (p. 4).** The obvious prior is the improper one (its total mass is infinite) that spreads probability mass for $\theta$ uniformly from $-\infty$ to $+\infty$, often written $d\theta$. A Bayesian using it obtains good frequentist results: the central 90% a posteriori interval for $\theta$ agrees exactly with the standard 90% confidence interval.

**Situation (2) (p. 4).** Observe two independent copies of (1):
$$\begin{pmatrix}x_1\\x_2\end{pmatrix}\sim N_2\!\left(\begin{pmatrix}\theta_1\\\theta_2\end{pmatrix},I\right).\tag{2}$$
- In some recent work, Efron needed inferences about $\lambda=\theta_1\theta_2$. It seemed intuitively reasonable, and objective, to use the improper prior $d\theta_1\,d\theta_2$, which spreads mass uniformly over the entire plane.
- Table 1 shows the central 90% posterior interval for $\lambda$ from this prior has poor frequentist properties. For $(\theta_1,\theta_2)$ in the first quadrant, it gives overly low probabilities of missing $\lambda$ on the left and overly high ones on the right. From a frequentist viewpoint the interval estimates have been biased toward the origin.
- Charles Stein has recently given a method of constructing priors with better frequentist properties (Stein 1982). For $\lambda$, it suggests the improper prior $(\theta_1^2+\theta_2^2)^{1/2}d\theta_1\,d\theta_2$, and Table 1 shows this does give better frequentist coverage probabilities.

Table 1: theoretical versus actual probability of not covering $\lambda$ with the central 90% interval from the flat prior. Each cell gives the flat-prior value, then in parentheses the value with Stein's prior. The theoretical value is .050 on each side. The printed table omits the decimal points (p. 4).

| $(\theta_1,\theta_2)$ | left | right |
|---|---|---|
| (0,0) | .002 (.006) | .002 (.006) |
| (2,2) | .023 (.036) | .087 (.065) |
| (3,3) | .029 (.041) | .074 (.053) |
| (4,4) | .031 (.046) | .070 (.047) |
| (5,5) | .036 (.048) | .064 (.043) |
| (1,10) | .045 (.053) | .051 (.053) |

- The parenthesized figures are essentially the same probabilities computed with Stein's improper prior. Efron says they were derived for the bias-corrected percentile intervals (sec. 10.7 of Efron 1982a), and it was then verified that these intervals were almost the same as Stein's.
- The point of the example, Efron says, is that the theory of Bayesian objectivity cannot be a simple one. The correct objective prior seems to depend on which parameter we want to estimate. With several parameters rather than just two, the problems become acute (Efron 1982b).
- This does not mean the situation is hopeless. Even a partial solution to the problem of Bayesian objectivity would likely be a valuable contribution. As a hopeful prototype, the Bayesian explanation of the James–Stein estimator has deepened our understanding of this potentially wonderful tool. The whole subject of empirical Bayes can be thought of as an exercise in Bayesian objectivity: trying not to put more information into the prior than necessary. More progress in this area can be expected (p. 4).

> **Intuition note.** Efron's example shows that a flat prior on $(\theta_1,\theta_2)$, which seemed objective, gave poor frequentist coverage for $\lambda=\theta_1\theta_2$, while Stein's prior did better. His conclusion: the correct objective prior seems to depend on the parameter we want to estimate.

### 6. Summary (p. 4)
Efron summarizes the major reasons why Fisherian and NPW ideas have pushed Bayesian theory aside in statistical practice:
1. **Ease of use:** Fisher's theory in particular is well set up to yield answers on an easy and almost automatic basis.
2. **Model building:** Both Fisherian and NPW theory pay more attention to the preinferential aspects of statistics.
3. **Division of labor:** The NPW school in particular allows interesting parts of a complicated problem to be broken off and solved separately. These partial solutions often use aspects of the situation, such as the sampling plan, that do not seem to help the Bayesian.
4. **Objectivity:** the frequentists have seized the high ground of scientific objectivity.

None of these points is insurmountable, and there have been some Bayesian efforts on all four. In Efron's opinion, a lot more such effort will be needed to fulfil Lindley's prediction of a Bayesian 21st century (p. 4).

### Start of Chernoff's Comment (p. 5; not Efron's text)
Page 5 begins a Comment by Herman Chernoff. He says he wishes to add some reasons why not everyone is a Bayesian, to explain why everyone is, should be, or will soon be a Bayesian, and to claim that (objective) Bayesianism is wrong. On these pages he argues:
- **Teaching:** practice changes slowly because the teaching of elementary statistics changes slowly. Bayes's theorem is relatively abstract and less intuitive than proportions, means and standard deviations. Guttman (1978) attributes the "stargazing" habits tied to .01 and .05 levels to poor teaching by the statistical profession.
- **Practice versus theory:** the popularity of Fisherian theory stems in part from the byproducts of the analysis it suggests, such as analysis of variance. Theory should serve as a guide and enhance intuition, not be used as a prescription requiring optimal behavior.
- **How he is a Bayesian:** he feels ease and freedom in applied work only after he has formulated some decision-theoretic and Bayesian view of the problem. He asks whether most statisticians are closet Bayesians in this sense.
- **When Bayesianism is the only way:** he lists public-policy issues (acid rain, ozone depletion, nuclear power safety, diesel fumes) where the scientific foundations are unclear and fundamental data are lacking. He says scientific analysis of nuclear safety may, for lack of any real alternative, require a Bayesian fault tree analysis with priors based more on imagination than on real data. He hopes numbers derived this way will not have undue influence on a public impressed by quantification. The supplied pages end here.

## Toy example (ours, not from the text)
Two small checks of results quoted in the paper.

**(a) Median interval, small case.** Take $n=3$ and the interval $[x_{(1)},x_{(3)}]$ (sample minimum and maximum) for the median $\theta$ of a continuous $F$. Let $B$ be the number of observations below $\theta$. Each observation is below $\theta$ with probability $1/2$, so $B\sim\text{Bin}(3,\tfrac12)$.
- The interval covers $\theta$ exactly when at least one observation is below it and at least one is above it, i.e. $1\le B\le2$.
- $P(B=0)=1/8$ and $P(B=3)=1/8$. So coverage $=1-1/8-1/8=6/8=.75$, for every continuous $F$.
- No prior on $F$ was needed. This is the same style of argument as for Efron's $[x_{(3)},x_{(12)}]$ example.

**(b) Flat prior, situation (1).** Let $x=1.2$ in $x\sim N(\theta,1)$ with prior $d\theta$. The posterior is $N(1.2,1)$. The central 90% interval is $1.2\pm1.645=(-0.445,\,2.845)$. The standard 90% confidence interval is the same: $x\pm1.645$.

## Concepts
- [[frequentist-vs-bayesian-inference]] — the contrast the whole paper is about; per Efron, the parting of the ways is $\theta$ averages (expectations with the state of nature $\theta$ fixed): central for frequentists, irrelevant to Bayesians (p. 3)
- [[subjective-personal-probability]] — de Finetti–Savage subjective Bayes, which has the legitimate claim to philosophic coherency but, per Efron, has failed to make much of a dent in scientific statistical practice (p. 3)
- [[objective-bayes]] (new) — the line of Bayesian thought that tries to build priors capturing fairness; Bayes and Laplace were objective Bayesians, Jeffreys (1961) wrote a famous book on it; the flat prior does well in situation (1) but poorly for $\lambda=\theta_1\theta_2$ (p. 4)
- [[prior-distribution]] — here improper priors: $d\theta$, $d\theta_1d\theta_2$, and Stein's $(\theta_1^2+\theta_2^2)^{1/2}d\theta_1d\theta_2$ (p. 4)
- [[likelihood]] — Efron says tree-building has no effect on the likelihood function, so it makes no difference to the Bayesian (p. 3)
- [[fisherian-archetypes]] (new) — Fisher's strategy of reducing problems to a simple form such as $x\sim N(\theta,1)$ (p. 1)
- [[npw-school]] (new) — Neyman–Pearson–Wald decision theory: split off a narrow piece of the problem; $\theta$ averages are central (pp. 1–3)
- [[maximum-likelihood]] (new) — the automatic Fisherian tool, the original jackknife in Tukey's sense of a widely applicable and dependable tool (p. 1)
- [[bayesian-vs-frequentist-coherence]] (new) — the Bayesian charge that frequentist practice is incoherent, versus Efron's reply that coherent Bayesians have to solve all problems at once, an often impossible exercise (pp. 2–3)
- [[partial-pooling-shrinkage]] — James–Stein estimation, cited as an idea that fails the objectivity test and, via its Bayesian explanation, as a hopeful prototype (p. 4)
- [[cross-validation-loo-waic]] — the nearest spine concept; Efron's bootstrap analysis for the tree is described as much like a cross-validation, correcting the apparent success rate (p. 3)

## Canonical instances
- [[cauchy-location-interval]] — the correct 95% interval uses the observed (second-derivative) information, not the expected information (p. 1)
- [[median-order-statistic-interval]] — distribution-free interval $[x_{(3)},x_{(12)}]$ for $n=15$; a genuine Bayesian solution needs a prior on all distributions (p. 2)
- [[significance-test-n01-vs-n21]] — $N(0,1)$ vs $N(2,1)$: comparative evidence versus absolute "7 to 1" odds (p. 2)
- [[heart-attack-decision-tree]] — apparent 96.7% versus bootstrap about 70%; the likelihood is unaffected by how the tree was built (p. 3)
- [[theta1-theta2-product-prior]] — flat prior gives poor coverage for $\lambda=\theta_1\theta_2$; Stein's prior is better (Table 1) (p. 4)

## Bridges (candidates)
- [structural-analogy] Efron's tree: apparent vs bootstrap success rate ↔ machine learning: training error vs held-out error — both correct optimism from fitting and testing on the same data.
- [structural-analogy] A stopping rule or data-dependent model building has no Bayesian consequence ↔ Bayesian workflow: likelihood principle versus data-adaptive modelling and the need for predictive checks.
- [metaphor] Objective prior choice depending on the parameter of interest ↔ Bayesian statistics: the parameterization-dependence of "uninformative" priors.
- [structural-analogy] Empirical Bayes as keeping the prior from carrying extra information ↔ hierarchical models: priors learned from data.

## Questions this raises
- Efron says the flat prior $d\theta$ gives intervals that match confidence intervals in situation (1). Which other models have this property, and what prior does it need?
- For $\lambda=\theta_1\theta_2$, why does the flat prior bias intervals toward the origin, and why does Stein's prior help?
- Is the bootstrap/cross-validation correction for the tree something a Bayesian could build into a model (e.g., through a prior on tree-fitting procedures), or is it outside Bayes?
- If objectivity means good frequentist coverage, what does a Bayesian gain from calling a method "Bayesian"?

## Reading notes
- The first PDF page is the publisher's download cover sheet. Printed page 1 is pdf 2, so printed = pdf − 1. The paper runs to printed p. 4. References are on pp. 4–5. The start of Chernoff's Comment is on p. 5 and is not Efron's text (the page ends mid-comment).
- The text layer is heavily garbled (columns, formulas, Table 1). Figure 2 and Table 1 were checked against their page images (pdf 4 and pdf 5). No image was supplied for printed p. 1, so the Cauchy interval formulas in sec. 3 are reconstructed from the garbled text. My notation ($\ddot\ell$, $I_0$) may differ from the original symbols; the text layer shows the expected information as "10".
- In sec. 4 the interval printed is $[x_{(3)},x_{(12)}]$ with probability .963 for $n=15$. By my own calculation (not in the source), under the standard coverage count (the interval covers iff between 3 and 11 observations lie below $\theta$), I get about .979, not .963. I have reported the printed values and could not reconcile them.
- Table 1 is labelled "Theoretical .050 .050" for the two tail columns. Which column is which side is inferred from the text (left too low, right too high in the first quadrant). The printed table omits decimal points; I read "002" as .002, and so on.
- The note under Table 1 is partly garbled in the text layer. I read it from the image as: figures in parentheses are essentially the same probabilities using the improper prior $(\theta_1^2+\theta_2^2)^{1/2}d\theta_1d\theta_2$.
- In sec. 4 (p. 3), "This is incoherent behavior" comes after the sentences about the frequentist estimate moving with the construction rule and before the sentence about the Bayesian estimate. The page does not state explicitly what "this" refers to, and the digest does not resolve it.
