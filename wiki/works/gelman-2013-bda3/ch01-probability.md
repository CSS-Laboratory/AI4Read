---
id: gelman-2013-bda3/ch01-probability
work: gelman-2013-bda3
unit: "1 Probability and inference"
pages: 3–28
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Probability and inference (BDA3, Chapter 1)

## L0 — One line
Bayesian data analysis means building a full probability model for unknowns and data, conditioning on the observed data to get a posterior distribution, and then checking and revising the model.

## L1 — The gist (≤ 120 words)
Bayesian data analysis asks how to draw conclusions about unobserved quantities from data using probability. The chapter's answer has three steps: build a full joint probability model, condition on the observed data to get a posterior distribution (the probability of the unknowns given the data), then check the model and revise it. It introduces Bayes' rule, predictive distributions and the likelihood, with genetics and spelling examples. The authors give reasons for using probability as a measure of uncertainty, without arguing the foundations in depth, and show that probabilities can be estimated empirically (football, record linkage). The chapter also reviews probability identities and simulation as working tools, and sets notation used in the rest of the book.

**Prerequisites:** conditional probability and densities; expectation and variance; integrals; the normal distribution and its cdf; determinant of a matrix (for the Jacobian).

## L2 — Key ideas (5–10 bullets)
- **Three-step workflow.** (1) Set up a full probability model for all observables and unobservables; (2) condition on the data to get the posterior; (3) check fit and sensitivity, then revise and repeat. Step 3 partly relieves the need to get the model right at the first attempt (p. 3).
- **Bayes' rule is the technical core.** $p(\theta|y)\propto p(\theta)p(y|\theta)$. The primary task of any specific application is to develop the model and compute and summarise the posterior (p. 7).
- **Prediction averages over the posterior.** The prior predictive distribution is $p(y)$, the distribution of the observable before seeing data. The posterior predictive distribution is $p(\tilde y|y)=\int p(\tilde y|\theta)p(\theta|y)d\theta$ (pp. 7–8).
- **Odds form and sequential updating.** Posterior odds (ratio of posterior densities at two parameter values) equal prior odds times the likelihood ratio (the ratio of $p(y|\theta)$ at those two values). Yesterday's posterior serves as today's prior, as in the hemophilia example (pp. 8–9).
- **Disputing a posterior signals misfit or missing information.** A dispute means the model does not fit or there is information not yet in the model. In the 'radom' example lack of fit is not the issue, so it points to extra information in the prior or likelihood; context can be added to the prior (p. 11).
- **Probability as a yardstick of uncertainty.** Analogy, normative axioms and betting coherence are offered as reasons for using probability. The authors say these considerations suggest probability may be a reasonable approach, call the normative rationale "suggestive but not compelling", and say the real test is success in applications. Symmetry and frequency are the usual justifications for a coin's ½ (pp. 11–13).
- **Probabilities can be assigned empirically.** Football point spreads (a normal model for outcome − spread) and record-linkage calibration (a mixture model) estimate probabilities from data (pp. 13–19).
- **Core identities.** $E(u)=E(E(u|v))$; $\operatorname{var}(u)=E(\operatorname{var}(u|v))+\operatorname{var}(E(u|v))$; the Jacobian change-of-variables rule for densities; logit and probit transformations that map $(0,1)$ to the whole real line (pp. 21–22).
- **Simulation summarises inference.** Draws from the posterior can be used to estimate any summary of interest. The inverse-cdf method (draw $U$ uniform on $[0,1]$, return $F^{-1}(U)$) is one way to generate draws (pp. 22–24).

## L3 — Walkthrough

### 1.1 The three steps of Bayesian data analysis (pp. 3–4)
- **Inference** here means making statements about unobserved quantities from data, using probability models for both observed quantities and quantities we want to learn about. Explicit use of probability to quantify uncertainty is the essential characteristic of Bayesian methods (p. 3).
- The process is idealised in three steps (p. 3):
  1. Set up a **full probability model**: a joint distribution for all observable and unobservable quantities. It should be consistent with the science and with how the data were collected.
  2. **Condition on observed data**: calculate and interpret the **posterior distribution**, the conditional distribution of the unobserved quantities of interest given the data.
  3. **Evaluate fit**: does the model fit, are conclusions reasonable, how sensitive are results to step 1? One may then alter or expand the model and repeat.
- Step 2 involves computational methods; step 3 balances technique and judgment, guided by the applied context. Step 1 remains a major stumbling block: where do models come from? (p. 3)
- Better computation and model checking ease, to some degree, the need to assume the correct model at the first attempt. The much-feared dependence on 'subjective' priors can be examined and explored (p. 3).
- **Interpretation.** A Bayesian interval can be directly regarded as having high probability of containing the unknown quantity. A frequentist confidence interval may strictly be interpreted only relative to a sequence of similar inferences. The authors also note the recent emphasis on interval estimation rather than hypothesis testing, which they see as an impetus to the Bayesian viewpoint, and say one aim is to show how far Bayesian readings of common simple procedures are justified (pp. 3–4). The authors suspect most users of confidence intervals give them a Bayesian reading (p. 3).
- The authors choose to stress pragmatic advantages rather than argue foundations. Direct quantification of uncertainty means no impediment in principle to models with many parameters and multilayered specifications. The practical problems are setting up and computing with them (p. 4).

### 1.2 General notation for statistical inference (pp. 4–6)
- **Estimands** are unobserved quantities about which we make inferences. There are two kinds: potentially observable quantities (future observations, or the outcome under the treatment not received) and non-observable parameters. The distinction is not always precise (p. 4).
- The clinical-trial example: even if the whole population could be exposed to one treatment, nobody can be exposed to both. So inference is still needed for the causal comparison between observed and unobserved outcome (p. 4).
- **Notation** (p. 4; explanatory variables are introduced on p. 5):

| Symbol | Meaning |
|---|---|
| $\theta$ | unobservable vector quantities or population parameters |
| $y$ | observed data |
| $\tilde y$ | unknown but potentially observable quantities |
| $x$, $X$ | explanatory variables (covariates) |

  Greek letters are parameters. Lower-case Roman letters are observed or observable scalars and vectors. Upper-case Roman letters are matrices. Vectors are columns, so $u^Tu$ is a scalar and $uu^T$ is $n\times n$.
- **Units.** Data on $n$ units are $y=(y_1,\dots,y_n)$. If several variables are measured per unit, $y$ is a matrix with $n$ rows. The $y$'s are 'random' in the sense that they could have turned out otherwise (p. 5).
- **Exchangeability.** The usual starting point is the often tacit assumption that the $y_i$ are exchangeable. This means uncertainty is expressed as a joint density $p(y_1,\dots,y_n)$ invariant to permutations of the indexes. A nonexchangeable model would be appropriate if relevant information were conveyed in the unit indexes rather than by explanatory variables (p. 5).
- Exchangeable data are commonly modelled as **iid given $\theta$**, with $\theta\sim p(\theta)$ (p. 5).
- **Explanatory variables** $x$ are observed on each unit but not modelled as random. $X$ is $n\times k$ for $k$ variables. Treating $X$ as random, exchangeability extends to the pairs $(x,y)_i$. It is always appropriate to assume an exchangeable model after including enough relevant information in $X$ that the indexes could be thought of as randomly assigned. Units with equal $x$ then have the same distribution of $y$. Any $x$ can be moved into $y$ if we wish to model it (p. 5).
- **Hierarchical (multilevel) models** (from Chapter 5 on) apply when information exists at several levels. Exchangeability can then be considered at each level. Example: patients within each city exchangeable, and cities exchangeable. Include city-level covariates, and the conditional distributions given them would be exchangeable (pp. 5–6).

*Intuition note.* Assuming exchangeability means the order or labels of the units are not treated as carrying information. Data of this kind are commonly modelled as iid draws from one common process with an unknown parameter.

### 1.3 Bayesian inference (pp. 6–8)
- Conclusions about $\theta$ or $\tilde y$ are probability statements conditional on observed $y$ (and covariates): $p(\theta|y)$, $p(\tilde y|y)$. Many textbooks instead evaluate retrospectively the estimation procedure over possible $y$ given the true $\theta$. In many simple analyses the two approaches give superficially similar conclusions, but Bayesian analyses extend easily to complex problems (p. 6).
- **Notation** (p. 6). $p(\cdot|\cdot)$ and $p(\cdot)$ denote conditional and marginal densities, with arguments fixed by context. The same symbol covers densities and mass functions. $\Pr(\cdot)$ may be used for events, for example $\Pr(\theta>2)=\int_{\theta>2}p(\theta)d\theta$. $\theta\sim N(\mu,\sigma^2)$ denotes a random variable and $N(\theta|\mu,\sigma^2)$ a density. The coefficient of variation is $\mathrm{sd}(\theta)/E(\theta)$, the geometric mean is $\exp(E[\log\theta])$, and the geometric sd is $\exp(\mathrm{sd}[\log\theta])$.
- **Bayes' rule.** A model gives the joint density as prior times sampling (data) distribution: $p(\theta,y)=p(\theta)p(y|\theta)$ (p. 6). Conditioning on known $y$ gives the posterior (p. 7):
$$p(\theta|y)=\frac{p(\theta,y)}{p(y)}=\frac{p(\theta)p(y|\theta)}{p(y)}\tag{1.1}$$
  with $p(y)=\sum_\theta p(\theta)p(y|\theta)$, or $\int p(\theta)p(y|\theta)d\theta$ for continuous $\theta$. Since $p(y)$ does not depend on $\theta$, for fixed $y$ it is a constant. This gives the **unnormalized posterior density**:
$$p(\theta|y)\propto p(\theta)p(y|\theta)\tag{1.2}$$
  Here $p(y|\theta)$ is taken as a function of $\theta$, not of $y$. The authors say these formulas hold the technical core of Bayesian inference: develop $p(\theta,y)$ and compute to summarise $p(\theta|y)$ (p. 7).
- **Prior predictive distribution.** Before data are seen, the distribution of the unknown observable $y$ is
$$p(y)=\int p(y,\theta)d\theta=\int p(\theta)p(y|\theta)d\theta\tag{1.3}$$
  It is "prior" because it is not conditional on a previous observation, and "predictive" because it is for an observable (p. 7).
- **Posterior predictive distribution.** After observing $y$, predict $\tilde y$ from the same process. The text's example is $n$ weighings of an object, with $\theta=(\mu,\sigma^2)$ the true weight and the scale's measurement variance (p. 7):
$$p(\tilde y|y)=\int p(\tilde y,\theta|y)d\theta=\int p(\tilde y|\theta,y)p(\theta|y)d\theta=\int p(\tilde y|\theta)p(\theta|y)d\theta\tag{1.4}$$
  The second and third lines show it as an average of conditional predictions over the posterior of $\theta$. The last step uses the assumed conditional independence of $y$ and $\tilde y$ given $\theta$ (p. 7).
- **Likelihood.** With a chosen model, the data affect the posterior (1.2) only through $p(y|\theta)$, regarded as a function of $\theta$ for fixed $y$: the likelihood function. Bayesian inference thereby obeys the **likelihood principle** (p. 7). The principle is reasonable only within the adopted model or family of models. One can rarely be confident the model is correct, so sampling distributions (imagined repeated data) can help check assumptions (Chapter 6). In the authors' view, an applied Bayesian statistician is willing to apply Bayes' rule under a variety of possible models (p. 8).
- **Odds.** The ratio of posterior densities at $\theta_1$ and $\theta_2$ is the posterior odds. The usual case is discrete $\theta$ with $\theta_2$ the complement of $\theta_1$. Bayes' rule becomes (p. 8):
$$\frac{p(\theta_1|y)}{p(\theta_2|y)}=\frac{p(\theta_1)p(y|\theta_1)/p(y)}{p(\theta_2)p(y|\theta_2)/p(y)}=\frac{p(\theta_1)}{p(\theta_2)}\,\frac{p(y|\theta_1)}{p(y|\theta_2)}\tag{1.5}$$
  In words, posterior odds equal prior odds times the likelihood ratio $p(y|\theta_1)/p(y|\theta_2)$ (p. 8).

*Intuition note.* The posterior is the prior reweighted by how well each parameter value predicted the data, then rescaled to sum to 1. In odds form for two parameter values, the data act only through one number, the likelihood ratio.

### 1.4 Discrete examples: genetics and spell checking (pp. 8–11)
**Inference about genetic status (hemophilia)** (pp. 8–9)
- Hemophilia is X-linked recessive. A male with the gene on his X-chromosome is affected. A female with the gene on only one of her two X-chromosomes is not affected (p. 8).
- **Prior.** The woman has an affected brother, so her mother is a carrier. Her father is unaffected. So she has a fifty-fifty chance of carrying the gene: $\theta=1$ (carrier) or $0$, with $\Pr(\theta=1)=\Pr(\theta=0)=\tfrac12$ (p. 8).
- **Likelihood.** She has two sons, neither affected ($y_i=1$ affected, $0$ not). The sons are exchangeable and, given $\theta$, independent (not identical twins). If she is a carrier, each son has a 50% chance of being affected. If not, the chance is close to 1 that a son is unaffected. The mutation rate is ignored (pp. 8–9):
$$\Pr(y_1=0,y_2=0|\theta=1)=(0.5)(0.5)=0.25,\qquad \Pr(y_1=0,y_2=0|\theta=0)=(1)(1)=1.$$
- **Posterior** (p. 9):
$$\Pr(\theta=1|y)=\frac{(0.25)(0.5)}{(0.25)(0.5)+(1.0)(0.5)}=\frac{0.125}{0.625}=0.20.$$
  In odds: prior odds $0.5/0.5=1$; likelihood ratio $0.25/1=0.25$; posterior odds $0.25$; probability $0.25/(1+0.25)=0.2$ (p. 9).
- **Adding data.** Use the previous posterior as the new prior. A third unaffected son gives (p. 9)
$$\Pr(\theta=1|y_1,y_2,y_3)=\frac{(0.5)(0.20)}{(0.5)(0.20)+(1)(0.8)}=0.111.$$
  If the third son were affected, the posterior probability of being a carrier becomes 1 (again ignoring mutation) (p. 9).

*Intuition note.* Each unaffected son makes carrier status less likely, because carriers would often have affected sons. The update can be done one observation at a time and gives the same answer as doing all the data at once.

**Spelling correction** (pp. 9–11)
- Someone types 'radom'. Let $y$ be the typed data and $\theta$ the intended word. Then
$$\Pr(\theta|y=\text{'radom'})\propto p(\theta)\Pr(y=\text{'radom'}|\theta)\tag{1.6}$$
  Consider only three intended words: $\theta_1$ = random, $\theta_2$ = radon, $\theta_3$ = radom. Then $p(\text{random}|\text{'radom'})=p(\theta_1)p(\text{'radom'}|\theta_1)/\sum_{j=1}^3 p(\theta_j)p(\text{'radom'}|\theta_j)$ (p. 9).
- Priors can come from word frequencies in a large database, ideally one adapted to the problem. Likelihoods can come from a model of spelling and typing errors (pp. 9–10).
- Google values given in the text (p. 10):

| $\theta$ | $p(\theta)$ | $p(\text{'radom'}\mid\theta)$ | $p(\theta)p(\text{'radom'}\mid\theta)$ | $p(\theta\mid\text{'radom'})$ |
|---|---|---|---|---|
| random | $7.60\times10^{-5}$ | 0.00193 | $1.47\times10^{-7}$ | 0.325 |
| radon | $6.05\times10^{-6}$ | 0.000143 | $8.65\times10^{-10}$ | 0.002 |
| radom | $3.12\times10^{-7}$ | 0.975 | $3.04\times10^{-7}$ | 0.673 |

- Renormalising the priors to sum to 1 is unnecessary, since it is absorbed into the proportionality constant (p. 10).
- The likelihood column is not a probability distribution; it gives the probability of one outcome ('radom') under three different parameter values (p. 10).
- Conclusion, conditional on the model: 'radom' is about twice as likely to be correct as to be a typo for 'random', and very unlikely to be a mistyped 'radon'. A fuller analysis would include more words (p. 10).
- **Decision, checking, improvement.** One may accept the roughly two-thirds probability, or dispute it. Disputing a posterior means the model does not fit or there is extra prior information. With a single word, lack of fit is not the issue, so the dispute is a claim of additional information in the prior or likelihood (p. 11).
- The authors have no grounds to criticise the likelihood. Priors are highly context dependent: 'random' is frequent in their statistics writing, 'radon' occasional, and 'radom' was new to them. Their surprise at the high probability of 'radom' is extra knowledge (pp. 10–11).
- Elaborating the model with context $x$: $p(\theta|x,y)\propto p(\theta|x)\,p(y|\theta,x)$. To a first approximation, the last term can be simplified to $p(y|\theta)$, so that the error probability does not depend on context. The authors say this is not perfect but could reduce modelling and computing burden (p. 11).

### 1.5 Probability as a measure of uncertainty (pp. 11–13)
- Mathematical definition is assumed known: probabilities are nonnegative, additive over mutually exclusive outcomes, and sum to 1 (p. 11).
- In Bayesian statistics probability is used as the fundamental measure, or yardstick, of uncertainty. Probabilities of 'rain tomorrow' or a Brazilian World Cup win are as legitimate as that of a coin landing heads. The probability that an estimand lies in a range is of more interest after data, while a sample-mean probability from a known population is more relevant beforehand (p. 11).
- The guiding principle: "The state of knowledge about anything unknown is described by a probability distribution." (p. 11)
- **Why is a coin's probability of heads ½?** Two justifications are commonly given (p. 12):
  1. *Symmetry or exchangeability*: probability = favourable cases / possibilities, assuming equally likely possibilities. For a coin this is a physical argument about forces and initial conditions.
  2. *Frequency*: relative frequency in a long sequence of identical, physically independent tosses.
- Both are in a sense subjective (they need judgments about the coin and procedure, and about 'equally likely', 'identical', 'independent'). Taken strictly, the frequency view does not allow a probability for a single toss not embedded in a long sequence of identical events (p. 12).
- **Increasingly subjective cases** (p. 12). A coin stated to be either double-headed or double-tailed: many would still say ½, perhaps by exchangeability of the labels. Other examples: Colombia vs. Brazil, rain tomorrow, a rocket launch failing. These resist strong frequency interpretations, but frequency interpretations can usually be constructed (for example, past launches as a reference set). That brings us back to treating outcomes as exchangeable and equally likely.
- **Why quantify uncertainty by probability?** Reasons "often advanced", with the authors' assessments (pp. 12–13):
  1. *Analogy*: physical randomness induces uncertainty, and common speech uses 'probably', 'unlikely'.
  2. *Axiomatic or normative*: related to decision theory, which places inference in the context of decision-making with gains and losses; reasonable axioms (ordering, transitivity, and so on) imply that uncertainty must be represented by probability. The authors view this normative rationale as "suggestive but not compelling" (p. 12).
  3. *Coherence of bets*: your probability $p$ for event $E$ is the fraction at which you would exchange $\$p$ for $\$1$ if $E$ occurs. If $E$ occurs you gain $\$(1-p)$, otherwise you lose $\$p$. Examples: a fair coin gives $p=\tfrac12$. Willing to bet 1 to win 10 on team A means your 'probability' for A is at least $\tfrac1{11}$ (p. 13). The *principle of coherence*: your probabilities should be such that nobody can make a definite gain betting with you. It "can be proved" that probabilities constructed this way must satisfy the basic axioms (p. 13).
- **Difficulties of the betting rationale** (p. 13): exact odds are needed, for betting either way on all events, and it is hard to assign them if unsure. Also, an informed counterparty may make a bet unwise, so probability is an incomplete guide to betting: necessary but not sufficient.
- The authors say these considerations suggest that probabilities may be a reasonable approach to summarising uncertainty in applied statistics, but that the real test is the success of the applications (p. 13).

**Subjectivity and objectivity** (p. 13)
- All statistical methods using probability are subjective in relying on mathematical idealisations. Bayesian methods are sometimes said to be especially subjective because of priors, but scientific judgment is needed for both likelihood and prior. Linear regression models are generally at least as suspect as any prior on the coefficients.
- Whenever there is replication (many exchangeable units), features of a distribution can be estimated from data, making analysis more 'objective'. If a whole experiment is replicated, prior parameters can themselves be estimated (Chapter 5).
- Elements of judgment remain: the choice of data included, the parametric forms, and how the model is checked.

### 1.6 Example: probabilities from football point spreads (pp. 13–16)
- The authors say this is an example of probability *assignment*, not Bayesian inference (p. 13).
- **Point spread** is the experts' measure of the ability difference. A 3.5-point favourite A beating B by more than 3.5 is a fair bet, so that probability is ½. For an integer spread, A is as likely to win by more as by fewer than the spread, with positive probability of exactly the spread (nobody paid). One interpretation: the spread is the median of the gambling population's beliefs about the outcome. The spreads are taken as given (p. 14).
- **Data (Figure 1.1).** Spread $x$ and outcome $y$ (favourite's score minus underdog's) for 672 games in the 1981, 1983 and 1984 seasons. Zero-spread games had labels assigned at random. The scatterplot is jittered (p. 14).
- **Empirical frequencies.** Count a tie as ½ win, ½ loss, and ignore zero-spread games (655 remain). Results (p. 15):

| Event | Estimate |
|---|---|
| Pr(favorite wins) | $410.5/655=0.63$ |
| Pr(favorite wins \| $x=3.5$) | $36/59=0.61$ |
| Pr(wins by more than spread) | $308/655=0.47$ |
| Pr(wins by more than spread \| $x=3.5$) | $32/59=0.54$ |

- These match knowledgeable fans' intuition, but are problematic with few data points. 8.5-point favourites won 5 of 5, while 9-point favourites won 13 of 20. We expect a higher win probability for the 9-point favourite, so small samples give imprecise assignments (p. 15).
- **Parametric model.** Figure 1.2a plots $y-x$ against $x$; it suggests that $y-x$ may roughly be modelled as independent of $x$. Figure 1.2b suggests $d=y-x$ may reasonably be approximated by a normal. Sample mean of the 672 values of $d$ is 0.07 and sample sd is 13.86. The authors take (p. 15)
$$d\,|\,x\sim N(0,14^2).$$
  They note the model does not fit the data exactly (scores and spreads are not continuous) (p. 15).
- **Probabilities from the model.** Then the favourite beats the spread with probability ½ for any $x$. The probability that an $x$-point favourite wins is (p. 16)
$$\Pr_{\text{norm}}(y>0|x)=\Pr_{\text{norm}}(d>-x|x)=1-\Phi\!\left(-\frac{x}{14}\right),$$
  with $\Phi$ the standard normal cdf. Values: $x=3.5$: 0.60; $x=8.5$: 0.73; $x=9.0$: 0.74. The 3.5 value agrees with the empirical one. The 8.5 and 9.0 values make more intuitive sense than the small-sample empirical ones (p. 16).

*Intuition note.* Pooling all games into one normal model uses data from all spreads at once. That is one way to see why its values for 8.5- and 9-point favourites make more intuitive sense than the raw frequencies from small cells such as the 5 games at 8.5 (our gloss).

### 1.7 Example: calibration for record linkage (pp. 16–19)
- **Setting.** Record linkage identifies records from different databases that belong to the same person. The work was formulated for linking the U.S. Census with a post-enumeration survey. The aim is to declare as many pairs 'matched' by computer as possible without excessive error, to save manual processing (p. 16).
- A composite score $y$ summarises agreement between two records. Candidate pairs are ordered by score. A cutoff gives the binary choice 'declare matched' vs. 'send to followup'. The **false-match rate** is the number of falsely matched pairs divided by the number of declared matched pairs (p. 16).
- Simple conversions of scores to probabilities give very inaccurate false-match estimates, typically far too optimistic. Pairs with nominal false-match probabilities from $10^{-3}$ to $10^{-7}$ had actual rates closer to 1%. Nominal 1% had actual 5% (pp. 16–17).
- The goal is to recalibrate to get 'objective' match probabilities, analogous to estimating game outcomes from past data given the spread. The approach is to estimate empirically the probability of a match as a function of $y$ (p. 17).
- **Mixture model** (details in Chapter 22). The distribution of scores is a mixture of true-match and non-match score distributions (p. 18):
$$p(y)=\Pr(\text{match})\,p(y|\text{match})+\Pr(\text{non-match})\,p(y|\text{non-match})\tag{1.7}$$
  Mixture probability and the two component distributions are estimated from the combined histogram of data with unknown match status. Some elements (such as the transformation making normal mixtures apply) were fit on separate training data with known status (pp. 17–18).
- Figure 1.3 (2300 test-Census records) shows the two score distributions, $p(y|\text{match})$ and $p(y|\text{non-match})$, mostly separate with some overlap (pp. 17–18).
- **False-match curve.** For a threshold, the false-match probability is the probability that a score above it comes from the non-match component. Lower thresholds declare more matches and the error proportion increases. A decision maker then picks an acceptable balance between clerical labour and mistakes (p. 18).
- **External validation.** The model was fit to candidate-pair scores at a test site (three sites in the 1988 test Census; detailed results for one, the others similar). Figure 1.4 shows expected false-match rate with 95% posterior bounds against proportion declared matched. The bounds give the range with 95% posterior probability for the rate. Dots show actual rates and "track well" with the model (pp. 18–19).
- The model suggests declaring less than 90% as matched and giving up on the other ~10%. Figure 1.5 magnifies the region where the rate accelerates; the predicted curves bend upward close to where observed rates rise steeply. Its caption suggests matching about 88% and sending the rest to followup. Uncalibrated estimates "were highly inaccurate" (p. 19).

### 1.8 Some useful results from probability theory (pp. 19–22)
- **Notation** (p. 20). Joint densities are written $p(u,v)$, with $p(u,v=1)$ for specific values. Marginals: $p(u)=\int p(u,v)dv$. Factoring: $p(u,v,w)=p(u|v,w)p(v|w)p(w)$. All distributions have the same logical status in Bayesian inference, so no separate letters ($\pi$, $f$) are used. Conditioning matters: $p(y|\theta)\neq p(y)$. Conditioning on the model's hypotheses $H$ is usually hidden: $p(\theta,y|H)=p(\theta|H)p(y|\theta,H)$.
- **Moments** (p. 20):
$$E(u)=\int u\,p(u)du,\quad \operatorname{var}(u)=\int(u-E(u))^2p(u)du,\quad \operatorname{var}(u)=\int(u-E(u))(u-E(u))^Tp(u)du\ \text{(vector } u\text{)}.$$
  $E(u|v)$ is the expectation with $v$ held fixed, a function of $v$. $E(u)$ averages over $v$ as well. Variables not in the conditioning are integrated out.
- **Modelling by conditional probability.** Useful models often express observables conditionally or hierarchically. Example: the height $y$ of a random university student has a marginal that is essentially a mixture of two normals centred near 160 and 175 cm. It is better described by $p(\text{male})\approx p(\text{female})\approx\tfrac12$ plus normal conditionals $p(y|\text{female})$, $p(y|\text{male})$ with means 160 and 175. If the conditional variances are not too large, the marginal is bimodal. The authors prefer modelling complexity through hierarchical structure and additional variables, even unobserved ones; this underlies mixture models (Chapter 22) (pp. 20–21).
- **Means and variances of conditional distributions** (p. 21).
$$E(u)=E(E(u|v))\tag{1.8}$$
  Derivation: $E(u)=\iint u\,p(u,v)\,du\,dv=\iint u\,p(u|v)\,du\,p(v)\,dv=\int E(u|v)p(v)dv$.
$$\operatorname{var}(u)=E(\operatorname{var}(u|v))+\operatorname{var}(E(u|v))\tag{1.9}$$
  Derivation, by expanding the right side:
$$\begin{aligned}E(\operatorname{var}(u|v))+\operatorname{var}(E(u|v))&=E\big(E(u^2|v)-(E(u|v))^2\big)+E\big((E(u|v))^2\big)-\big(E(E(u|v))\big)^2\\&=E(u^2)-E\big((E(u|v))^2\big)+E\big((E(u|v))^2\big)-(E(u))^2\\&=E(u^2)-(E(u))^2=\operatorname{var}(u).\end{aligned}$$
  Both identities also hold for vector $u$ ($E(u)$ a vector, $\operatorname{var}(u)$ a matrix) (p. 21).

*Intuition note.* Total spread has two parts: average spread within groups (given $v$) plus spread between the groups' means. In the height example (our illustration), the overall variance combines the spread of heights within each sex and the variation between the male and female means.

- **Transformation of variables** (pp. 21–22). Let $u$ have density $p_u$ and $v=f(u)$ with the same number of components.
  - Discrete $p_u$, $f$ one-to-one: $p_v(v)=p_u(f^{-1}(v))$. If $f$ is many-to-one, a sum of terms appears, one per branch of the inverse.
  - Continuous, $f$ one-to-one: $p_v(v)=|J|\,p_u(f^{-1}(v))$. Here $|J|$ is the absolute determinant of the Jacobian of $u=f^{-1}(v)$ as a function of $v$, a square matrix with $(i,j)$ entry $\partial u_i/\partial v_j$. Many-to-one gives a sum or integral of terms.
  - In one dimension, the log maps $(0,\infty)$ to $(-\infty,\infty)$. For $(0,1)$ use the logit:
$$\operatorname{logit}(u)=\log\!\left(\frac{u}{1-u}\right),\qquad \operatorname{logit}^{-1}(v)=\frac{e^v}{1+e^v}\tag{1.10}$$
  - Another choice is the probit $\Phi^{-1}(u)$, mapping $(0,1)$ to $(-\infty,\infty)$.

### 1.9 Computation and software (pp. 22–24)
- The authors rely on R for graphs, basic simulation, classical models and optimisation. They use Stan for most model fitting, but describe computations "from first principles" for teaching. Typical tasks: matrix manipulation, density evaluation, drawing simulations, programming, regression estimates (Chapter 14), graphics (p. 22).
- **Approach.** Fit many models, gradually increasing complexity. They do *not* recommend writing one model and letting the computer run overnight. Instead, fit each model quickly, use earlier fits as starting values, and compare inferences to data before continuing (p. 22).
- **Summarising by simulation** (pp. 22–23). Samples can often be generated even when the density cannot be integrated explicitly. A histogram of many draws provides practically complete information about the density. Moments and percentiles estimate any aspect to a precision that can itself be estimated. Example: to estimate the 95th percentile of $p(\theta)$, draw $S$ values and use the $0.95S$th order statistic. For most purposes $S=1000$ is adequate. Extremely large or small simulated values often flag a model specification or parameterisation problem (cf. Figure 4.2). A well-designed pseudorandom generator yields a deterministic sequence that appears like independent uniform$[0,1]$ draws (p. 23).
- **Inverse-cdf sampling** (p. 23). The cdf is $F(v_*)=\Pr(v\le v_*)$, which equals $\sum_{v\le v_*}p(v)$ if discrete and $\int_{-\infty}^{v_*}p(v)dv$ if continuous. Draw $U\sim\text{Uniform}[0,1]$ and set $v=F^{-1}(U)$. $F$ need not be one-to-one (certainly not for discrete distributions), but $F^{-1}(U)$ is unique with probability 1. Then $v$ is a draw from $p$. For discrete distributions $F^{-1}$ can be tabulated.
  - Exponential example with parameter $\lambda$: $F(v)=1-e^{-\lambda v}$. Solving $U=F(v)$ gives $v=-\log(1-U)/\lambda$. Since $1-U$ is also uniform on $[0,1]$, draws can be obtained as $-\log U/\lambda$.
- **Posterior and posterior predictive simulation** (pp. 23–24). Store $S$ draws $(\theta^s,\tilde y^s)$, $s=1,\dots,S$, in an array (Table 1.1): $S$ rows; columns $\theta_1,\dots,\theta_k$ and $\tilde y_1,\dots,\tilde y_n$. Superscripts are indexes, not powers.
  - The posterior of any function, such as $\theta_1/\theta_3$, comes from adding a new column computed from the existing draws.
  - The probability of an event, such as $\Pr(\tilde y_1+\tilde y_2>e^{\theta_1})$, is estimated by the proportion of the $S$ draws where it holds.
  - The central 95% posterior interval $[a,b]$ for $\theta_j$ has $\Pr(\theta_j<a)=0.025$ and $\Pr(\theta_j>b)=0.025$. It is estimated from order statistics of the draws, namely the 25th and 976th if $S=1000$ (as printed). Inferences are commonly summarised by 50% and 95% intervals.
  - Accuracy of simulation inferences is deferred to Section 10.5 (p. 24).

*Intuition note.* Once you have a table of posterior draws, estimating the posterior of a quantity, the probability of an event, or an interval becomes computing a column, counting rows, or sorting rows. No new integrals are needed for these estimates.

### 1.10 Bayesian inference in applied statistics (pp. 24–25)
- Three rationales (p. 24):
  - *Pragmatic*: multiple levels of randomness, combining information from different sources, and including all reasonable sources of uncertainty. This leads naturally to smoothed estimates in complicated data structures.
  - *Psychological*: clients often interpret interval estimates as probability statements about the unknown given the data. Such direct statements require prior specifications, so the kind of answers clients assume they are getting need full probability models, explicit or implicit.
  - *Sensitivity*: Bayesian inferences are conditional on models that contain approximations. If answers vary dramatically over scientifically reasonable assumptions that the data cannot settle, that range of conclusions must be entertained, and the authors believe the statistician has the responsibility to tell the client.
- The book focuses on constructing models (especially hierarchical ones from Chapter 5), checking fit and probing sensitivity. The authors place the strength of the approach in (1) combining information from multiple sources and (2) a more encompassing account of uncertainty about unknowns (p. 24).
- **Themes** common to much modern applied practice (p. 25): willingness to use many parameters; hierarchical models as the tool for partial pooling; model checking, including comparison with substantive knowledge; inference as distributions or intervals rather than point estimates; simulation as the primary computation (with multiple imputation for missing data); probability models as tools for understanding non-Bayesian methods; including as much background information as possible so data approximate a random sample conditional on the modelled variables; and designing studies so inferences are robust to model assumptions.

### 1.11 Bibliographic note (pp. 25–27)
- Lists introductory books (from Lindley 1965 to Hoff 2009) and texts for social scientists, psychologists and biologists (p. 25).
- On foundations: de Finetti (1974) on the role of exchangeability; Berger and Wolpert (1984) on the likelihood principle; Jeffreys and Jaynes as inductive and deductive views, with the authors saying Jaynes's view is similar to theirs (pp. 25–26).
- Gigerenzer and Hoffrage (1995): people understand and compute best with probabilities as relative frequencies (p. 26).
- Sources for the examples: football (Stern 1991); Challenger shuttle probabilities (Martz and Zimmer; Dalal et al.; Lavine); record linkage (Belin and Rubin 1995b); the Bayesian spelling corrector (Norvig 2007) (pp. 26–27).
- The authors state: "In all our examples, probabilities are assigned using statistical modeling and estimation, not by 'subjective' assessment." (p. 26)

### 1.12 Exercises (pp. 27–28)
Nine exercises are listed (conditional probability with a two-normal mixture; vector versions of (1.8)–(1.9); Lindley's eye-colour genetics; football probability assignment; tied congressional elections; Elvis and twins; the Monty Hall problem; subjective probability; queue simulation). See "Exercises worth doing".

## Toy example (our own, not from the text)
**Setup.** A box hides one of two coins. Coin A lands heads with probability 0.8; coin B with probability 0.5. A coin is picked with equal prior probability: $\Pr(A)=\Pr(B)=0.5$. We observe three tosses: H, H, H. Parameter $\theta\in\{A,B\}$; data $y=$ HHH.

1. *Likelihood.* $p(y|A)=0.8^3=0.512$. $p(y|B)=0.5^3=0.125$.
2. *Unnormalised posterior (1.2).* $A$: $0.5\times0.512=0.256$. $B$: $0.5\times0.125=0.0625$. Sum $=0.3185$.
3. *Posterior (1.1).* $\Pr(A|y)=0.256/0.3185=0.8038$. $\Pr(B|y)=0.0625/0.3185=0.1962$.
4. *Odds form (1.5).* Prior odds $=1$. Likelihood ratio $=0.512/0.125=4.096$. Posterior odds $=4.096$. Probability $=4.096/(1+4.096)=0.8038$. This matches step 3.
5. *Sequential updating.* Each head has likelihood ratio $0.8/0.5=1.6$. After one head: odds 1.6, so $1.6/2.6=0.6154$. After two: odds $2.56$, so $2.56/3.56=0.7191$. After three: odds $4.096$, so $0.8038$. This matches steps 3 and 4.
6. *Posterior predictive (1.4).* $\Pr(\tilde y=\text{H}|y)=0.8\times0.8038+0.5\times0.1962=0.6430+0.0981=0.7411$.
   It is below 0.8 because the posterior still gives about 20% weight to the fair coin.

## Concepts
- [[bayesian-workflow]] — the three steps: full probability model, conditioning on data, then fit and sensitivity checking, repeated as needed (p. 3)
- [[bayes-theorem]] — $p(\theta|y)=p(\theta)p(y|\theta)/p(y)$; the unnormalised form is $\propto p(\theta)p(y|\theta)$ (p. 7)
- [[prior-distribution]] — $p(\theta)$, one factor of the joint $p(\theta,y)=p(\theta)p(y|\theta)$ (p. 6)
- [[likelihood]] — $p(y|\theta)$ as a function of $\theta$ for fixed $y$; the authors stress it is not a probability distribution (pp. 7, 10)
- [[posterior-distribution]] — conditional distribution of unobserved quantities given observed data (pp. 3, 7)
- [[likelihood-principle]] (new) — given the model, data affect the posterior only through the likelihood; reasonable only within the chosen model family (pp. 7–8)
- [[prior-predictive-distribution]] (new) — $p(y)=\int p(\theta)p(y|\theta)d\theta$, the distribution of an observable before data (p. 7)
- [[posterior-predictive-distribution]] — $p(\tilde y|y)=\int p(\tilde y|\theta)p(\theta|y)d\theta$, a posterior average of conditional predictions (p. 7)
- [[odds-form-of-bayes]] (new) — posterior odds = prior odds × likelihood ratio (p. 8)
- [[sequential-updating]] — use the previous posterior as the new prior (p. 9)
- [[exchangeability]] — joint density invariant to permuting indexes; commonly modelled as iid given $\theta$ (p. 5)
- [[hierarchical-model]] — a model for data with several levels of units, with exchangeability at each level (p. 5)
- [[subjective-probability]] — here, probability as a yardstick of uncertainty. The authors argue that all statistical methods using probability rely on idealisations, and that judgment is needed for both prior and likelihood (pp. 11, 13)
- [[dutch-book-argument]] — the text calls it the "coherence of bets": the principle says your probabilities should not permit a definite gain by betting against you, and probabilities constructed this way must satisfy the basic axioms. The phrase "Dutch book" does not appear in this unit (p. 13)
- [[frequentist-vs-bayesian-inference]] — Bayesian conclusions condition on observed $y$; the frequentist textbook approach evaluates procedures over possible $y$ given true $\theta$ (pp. 3, 6)
- [[credible-interval]] — the authors' term is Bayesian (probability) or posterior interval, e.g. central 95% from the 2.5% and 97.5% quantiles of draws (pp. 3, 24)
- [[mixture-model]] (new) — the distribution of data as a weighted sum of component distributions, as in (1.7) (p. 18)
- [[law-of-total-expectation-and-variance]] (new) — identities (1.8) and (1.9) (p. 21)
- [[change-of-variables-jacobian]] (new) — $p_v(v)=|J|p_u(f^{-1}(v))$; logit and probit transformations (pp. 21–22)
- [[inverse-cdf-sampling]] (new) — draw $U\sim$ Uniform(0,1) and return $F^{-1}(U)$ (p. 23)
- [[posterior-simulation]] (new) — summarise inference with $S$ stored draws of $(\theta,\tilde y)$ (p. 23)

## Canonical instances
- [[hemophilia-carrier-example]] — prior ½, likelihood from unaffected sons, posterior 0.20 and then 0.111 (pp. 8–9)
- [[radom-spelling-example]] — priors and likelihoods multiplied to a posterior of 0.673 for 'radom'; disputing the posterior shows missing context (pp. 9–11)
- [[football-point-spreads]] — empirical frequencies vs. the normal model $d|x\sim N(0,14^2)$ for probability assignment (pp. 13–16)
- [[record-linkage-calibration]] — mixture-model calibration of false-match rates, validated on test Census data (pp. 16–19)
- [[clinical-trial-estimands]] — survival under two treatments; the outcome under the other treatment is unobserved (p. 4)
- [[student-height-mixture]] — bimodal marginal explained by sex-conditional normals (pp. 20–21)

## Bridges (candidates)
- [structural-analogy] unobserved outcome under the treatment not received (p. 4) ↔ causal inference: potential outcomes and the fundamental problem. The text only notes it as an estimand needing inference.
- [same-math] posterior odds = prior odds × likelihood ratio ↔ Bayes' theorem in HS form (e.g. medical-test base rates): the same rule on a different scale.
- [structural-analogy] converting a score into a match probability via prior and likelihood (record linkage) ↔ base-rate neglect: the prior proportion of true matches matters for the posterior.
- [structural-analogy] averaging the conditional prediction over the posterior (1.4) ↔ Monte Carlo integration: with posterior draws it becomes an average over rows of Table 1.1.
- [structural-analogy] $\operatorname{var}(u)=E(\operatorname{var}(u|v))+\operatorname{var}(E(u|v))$ ↔ hierarchical models: within-group vs. between-group variation, which is the information partial pooling uses.

## Questions this raises
- If the data affect the posterior only through the likelihood, how can sampling distributions (Chapter 6) legitimately help check the model?
- When replication allows prior parameters to be estimated from data (Chapter 5), how far does this reduce the subjectivity of the prior, and which judgment elements remain?
- In the 'radom' example, how should context $x$ enter the prior, and when is dropping $x$ from the likelihood, $p(y|\theta,x)\approx p(y|\theta)$, harmful?
- The record-linkage bounds are 95% posterior bounds (to be explained in the next chapter). How are such intervals computed for a quantity that is a function of the mixture parameters?

## Exercises worth doing
- Ex. 1 (p. 27) — a two-component normal mixture: the marginal density, a posterior probability at $y=1$, and how the posterior changes with $\sigma$; builds intuition for prior × likelihood — difficulty: easy
- Ex. 2 (p. 27) — show (1.8) and (1.9) for vector $u$; practice with the law of total expectation and variance — difficulty: medium
- Ex. 4 (p. 27) — estimate football probabilities for 8-point spreads by relative frequency and by the normal approximation; compare empirical and model-based assignment — difficulty: easy
- Ex. 6 (p. 28) — probability that Elvis was an identical twin; conditioning on the information actually observed — difficulty: medium
- Ex. 7 (p. 28) — Monty Hall; be clear about what to condition on — difficulty: medium
- Ex. 9 (p. 28) — simulate a clinic queue with Poisson arrivals and uniform service times; practice with simulation summaries (medians, 50% intervals) — difficulty: hard

## Reading notes
- Printed page = pdf page − 10 (pdf 13 = printed 3). All citations use printed pages.
- The text layer renders $\theta$ as "ω" and "−", "∼", "≈" often as "→" or other glyphs. The page images show $\theta$, $-$ and $\sim$.
- Running header on every page: a notice that the electronic edition is for non-commercial use. The title page and copyright page are not in these pages.
- Figures 1.1–1.5 were read from the images. Fig. 1.4 and 1.5 are very faint in the image, so the reading of curves rests mainly on the captions and text.
- Page 24 says the 25th and 976th order statistics estimate the 2.5% and 97.5% points for $S=1000$; this is reported here as printed.
- The unit is "Chapter 1" only. Exercise 5 continues on p. 28, and Chapter 2 is not covered here.
