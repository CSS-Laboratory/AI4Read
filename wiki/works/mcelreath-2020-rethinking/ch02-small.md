---
id: mcelreath-2020-rethinking/ch02-small
work: mcelreath-2020-rethinking
unit: "Chapter 2. Small Worlds and Large Worlds"
pages: 19–48 (p. 48 has no text)
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Small Worlds and Large Worlds

## L0 — One line
Bayesian inference is counting the ways each possible explanation could have produced the data, then standardising the counts. Its logic is consistent in the model's "small world", but that is no guarantee of optimal performance in the real "large world".

## L1 — The gist (≤ 120 words)
The chapter asks how a model can learn from data, and what separates a model from reality. McElreath separates the small world of the model from the large world where it is used. In the small world, Bayesian inference is counting the ways each conjecture (a possible explanation) could produce the data; multiplying counts is a shortcut. Standardising the counts gives probabilities: the posterior is proportional to likelihood times prior. A model has a likelihood, parameters (unknowns to estimate) and a prior (plausibility before the data), and is fitted numerically by grid approximation, quadratic approximation or MCMC. Logical consistency in the small world is no guarantee of optimal performance in the large world.

**Prerequisites:** joint and conditional probability; proportions; reading a curve as a distribution; the idea that a logarithm of a bell curve is a parabola; ability to read short R code.

## L2 — Key ideas (5–10 bullets)
- **Two worlds.** The small world is the model's self-contained logic; the large world is where we deploy it. Bayesian models have reasonable claims to optimality in the small world, assuming it describes the real world accurately, but large-world performance has to be demonstrated rather than logically deduced (pp. 19–20).
- **Inference as counting.** Count the paths through the *garden of forking data* that are consistent with the data; with no other information, conjectures that can produce the data in more ways are more plausible (pp. 21–23, 26).
- **Updating is multiplication.** New counts multiply old counts; the old count can come from earlier data or from other prior information. The result is the same whether you update step by step or all at once, if observations are independent (pp. 25–26, 31).
- **Counts become probabilities** by dividing each product by the sum of products. The parts are called parameter, likelihood, prior and posterior (pp. 26–27).
- **A model = likelihood + parameters + prior.** For the globe-tossing data the likelihood is derived from the data story and, given independent tosses with the same probability of water, is the binomial distribution (pp. 32–35).
- **Bayes' theorem is the counting rule in probability form:** posterior = likelihood × prior / average likelihood (pp. 36–37).
- **Certainty is not correctness.** With more data the globe-tossing model grows more sure, and any model can be very confident even when seriously misleading. The aim is to check adequacy for a purpose, not the truth of the assumptions (pp. 31–32).
- **Three conditioning engines:** grid approximation, quadratic approximation (a Gaussian at the posterior peak) and MCMC. How you fit is part of the model (pp. 38–45).

## L3 — Walkthrough

### Introduction: small and large worlds (pp. 19–20)
- Columbus believed the Earth was round but only 30,000 km around, not the actual 40,000 km. With 40,000 km he would have reasoned that supplies could not last to Asia (p. 19). The error was lucky: unexpected land lay in the way (p. 19).
- **Small world:** the self-contained logic of the model. All possibilities are nominated, so there are "no pure surprises". Inside it you can verify the model's logic. Bayesian models have reasonable claims to optimality, assuming the small world describes the real one accurately (p. 19).
- **Large world:** the context of deployment. It may contain events not imagined in the small world. The model is always an incomplete representation, so it can err even if all kinds of events were nominated. Small-world consistency is "no guarantee" of large-world optimality, but "a warm comfort" (p. 19).
- Bayesian learning is arguably optimal in the small world; large-world performance has to be demonstrated. Formal methods (Bayesian inference) and informal ones (peer review) both have a role (p. 20).
- *Rethinking: fast and frugal* (author's view): most animals are probably not Bayesian. Heuristics fitted to the environment may beat a full Bayesian analysis once costs of information and overfitting count. The author says being Bayesian is neither necessary nor sufficient for good decisions, as real animals show. For humans it is a general way to find and process relevant information, but not the only way (p. 20).

### 2.1 The garden of forking data (pp. 20–28)
Analogy with Borges' story: a book explores every path at each decision. Bayesian analysis considers everything that could have happened and prunes the sequences that contradict what did happen. What remains is only what is logically consistent with our knowledge (p. 21). This gives a ranking of hypotheses that is maximally conservative, given the assumptions and data that go into it. It cannot guarantee a correct answer on large-world terms, but it gives the best possible answer on small-world terms from the information fed in (p. 21).

**2.1.1 Counting possibilities (pp. 21–23).**
- A bag holds four marbles, blue or white; the number of each is unknown. There are five **conjectures**: 0, 1, 2, 3 or 4 blue (p. 21).
- **Data:** three marbles drawn one at a time, with replacement and shaking: blue, white, blue (p. 21).
- For the conjecture "1 blue, 3 white", each draw has 4 possible marbles. The three white marbles are different events even though we record only colour. So there are 3 more ways to see white than to see blue (p. 21). Three draws give $4^3=64$ paths (Figure 2.2, p. 22). The assumption is that shaking gives each marble a fair chance regardless of earlier draws (p. 22).
- Pruning: draw 1 (blue) eliminates the three white first branches. Draw 2 (white) leaves three of the paths from the blue marble. Draw 3 (blue) keeps one blue branch on each. So **3 of 64** paths remain (Figure 2.3, p. 22–23).
- "0 blue" and "4 blue" give zero ways, because each is logically incompatible with the data (p. 22). Figure 2.4 draws the gardens for the other three conjectures. Counts are 3 (1 blue), 8 (2 blue), 9 (3 blue) (pp. 22–23).
- The ways can be computed without drawing: multiply the number of ways in each "ring" (draw) (p. 23):

| Conjecture (blue count) | Ways to produce blue-white-blue |
|---|---|
| 0 | $0\times4\times0=0$ |
| 1 | $1\times3\times1=3$ |
| 2 | $2\times2\times2=8$ |
| 3 | $3\times1\times3=9$ |
| 4 | $4\times0\times4=0$ |

- The author stresses that multiplication is only a computational device; it is still counting logically possible paths (p. 23). The counts are only part of a solution: to compare them we must also decide how many ways each conjecture could itself be realised. The author says we might argue that, with no reason to assume otherwise, each conjecture can be treated as equally plausible and the counts compared directly, but often we do have reason to assume otherwise (p. 23).
- *Rethinking: justification.* The justification given here is logical: if we want to reason about plausibility consistently with ordinary true/false logic, we should follow this procedure. Other justifications lead to the same mathematics. The author says what matters is that it works; opponents once said Bayes was "hard to apply", which is no longer true. Being justified does not mean no other approach can be justified (p. 24).

*Intuition note.* Each conjecture gets one score: the number of ways it could have made exactly this data. Every path that disagrees with an observation is deleted, so only agreeing paths are left to count.

**2.1.2 Using prior information (pp. 25–26).**
- Prior information may come from knowing how the bag was made, from earlier data, or from a wish to build in conservatism. The method is to multiply the prior count by the new count (p. 25).
- With equal starting plausibility, the counts (0, 3, 8, 9, 0) say the 3-blue bag is slightly more plausible than the 2-blue bag, and both are about three times more plausible than the 1-blue bag (p. 25).
- Draw another blue marble. Restarting with a four-layer garden gives the same result as updating the counts. This holds as long as the new observation is logically independent of the earlier ones (p. 25). Ways to produce blue are 0, 1, 2, 3, 4, so the new counts are $0\times0=0$, $3\times1=3$, $8\times2=16$, $9\times3=27$, $0\times4=0$ (p. 25).
- General statement: if a conjecture produces $D_\text{prior}$ in $W_\text{prior}$ ways and $D_\text{new}$ in $W_\text{new}$ ways, it produces both in $W_\text{prior}\times W_\text{new}$ ways. Example: $8\times2=16$ for the 2-blue conjecture. Multiplication is a shortcut for enumerating and counting all paths (p. 25).
- Prior data and new data may be of different types. Factory information: for every 3-blue bag, two 2-blue bags and three 1-blue bags were made, and every bag has at least one of each colour. Update with factory counts 0, 3, 2, 1, 0 (p. 25–26):

| Conjecture | Prior count | Factory count | New count |
|---|---|---|---|
| 0 blue | 0 | 0 | 0 |
| 1 blue | 3 | 3 | $3\times3=9$ |
| 2 blue | 16 | 2 | $16\times2=32$ |
| 3 blue | 27 | 1 | $27\times1=27$ |
| 4 blue | 0 | 0 | 0 |

- Now the 2-blue conjecture is most plausible, but barely better than the 3-blue one. Whether a threshold difference lets us decide is left to Chapter 3 (p. 26).
- *Rethinking: original ignorance.* With no prior information, the common solution is to give each conjecture equal weight (**principle of indifference**). The author says "ignorance" is a surprisingly complicated issue, to be revisited. For problems in this book it gives inferences much like mainstream non-Bayesian ones, which contain implicit equal weighting. Many non-Bayesian procedures have moved away from this, e.g. penalised likelihood (p. 26).

**2.1.3 From counts to probability (pp. 26–27).**
- **Principle of honest ignorance:** when we don't know what caused the data, causes that may produce the data in more ways are more plausible (p. 26).
- Raw counts are awkward for two reasons. Only relative values matter (3, 8, 9 mean the same as 30, 80, 90). And counts explode: by 10 data points there are more than a million possible sequences (p. 26).
- Definition (p. 26): plausibility after seeing the data $\propto$ ways it can produce the data $\times$ prior plausibility. Let $p$ be the proportion of blue marbles, so $p=0.25$ for the 1-blue bag:
$$\text{plausibility of } p \text{ after } D_\text{new} \;\propto\; \text{ways } p \text{ can produce } D_\text{new}\times\text{prior plausibility of } p$$
- To standardise, divide each product by the sum of products (p. 27):
$$\text{plausibility of } p \text{ after } D_\text{new}=\frac{\text{ways } p \text{ can produce } D_\text{new}\times\text{prior plausibility } p}{\text{sum of products}}$$
- Worked table (p. 27), equal priors: $p=0,\,0.25,\,0.5,\,0.75,\,1$ have ways $0,3,8,9,0$ and plausibilities $0,\,0.15,\,0.40,\,0.45,\,0$. (added step: sum $=20$; $3/20=0.15$, $8/20=0.40$, $9/20=0.45$.) R code 2.1: `ways <- c(0,3,8,9,0); ways/sum(ways)` gives `0.00 0.15 0.40 0.45 0.00` (p. 27).
- These plausibilities are non-negative and sum to one, so they are probabilities (p. 27). The standard names are:
  - $p$ is a **parameter** value, an index for possible explanations.
  - the relative number of ways $p$ can produce the data is the **likelihood**.
  - the prior plausibility is the **prior probability**.
  - the updated plausibility is the **posterior probability** (p. 27).
- *Rethinking: randomization* (p. 28): to randomise means to process something so that we know almost nothing about its arrangement. If we have really erased prior knowledge, the result is very likely one of the many high-entropy orderings. Entropy is deferred to Chapters 6 and 9.

### 2.2 Building a model (pp. 28–32)
The toy example becomes the conventional form. Toss a globe, catch it, record whether the surface under the right index finger is water (W) or land (L), and repeat. The first nine samples: W L W W W L W L W, so 6 W and 3 L; these are the data (p. 28). The design loop has three steps: (1) data story, (2) update, (3) evaluate (p. 28).

**2.2.1 A data story (pp. 28–29).** The story may be descriptive or causal. Any story is complete in that it is sufficient to specify an algorithm for simulating new data (p. 28). For globe tossing (p. 29):
1. The true proportion of water is $p$.
2. One toss gives W with probability $p$ and L with probability $1-p$.
3. Tosses are independent of each other.

*Rethinking: value of storytelling* (p. 29). Many different stories correspond to the same model, so a model that works does not uniquely support its story. The story is still useful because it forces you to make vague verbal hypotheses precise, which exposes extra questions.

**2.2.2 Bayesian updating (pp. 29–31).**
- The model starts with prior plausibilities for each $p$ and updates them to posterior plausibilities. This is **Bayesian updating** (p. 29).
- In Figure 2.5 the machine starts with a flat prior (dashed line). After the first W, plausibility of $p=0$ falls to exactly zero, because some water exists. Plausibility of $p>0.5$ rises. The model does this automatically, because probability theory counts paths (p. 29).
- Each dashed curve is the previous solid curve (p. 30). A W moves the peak right; an L moves it left. The peak's height grows with each sample, so fewer values hold more plausibility as evidence accumulates (pp. 30–31).
- Every updated set of plausibilities becomes the initial set for the next observation. The process also runs backwards: from the final curve and the last observation one can "divide out" the observation to recover the earlier curve. So data can come in any order, or all at once; all at once is an abbreviation of iterated learning (p. 31).
- *Rethinking: sample size* (author's view). Non-Bayesian procedures are often justified by asymptotic (very large sample) behaviour, which makes small samples questionable. Bayesian estimates are valid for any sample size, but depend on the prior; a bad prior misleads. "No free lunch": Bayesian and non-Bayesian golems both pay with their assumptions (p. 31).

*Intuition note.* The posterior after toss $n$ is the prior for toss $n+1$. The order of tosses cannot matter here, because the model treats order as irrelevant.

**2.2.3 Evaluate (pp. 31–32).**
- The machine learns optimally within the small world, provided the large world is accurately described by the model. Still, calculations may malfunction, the model may differ from reality, and a particular sample may mislead (p. 31).
- *Principle 1:* the model's certainty does not show it is good. The curves will narrow with more data, but estimates are conditional on the model, so a seriously misleading model can still be very confident (p. 31).
- *Principle 2:* supervise the model. Shuffling the six W and three L gives the same final curve only because the model assumes order is irrelevant. That aspect of the data may still matter indirectly, so check inferences against aspects of the data the model does not know. Such checks are creative work, left to the analyst and the scientific community; golems are bad at it (pp. 31–32).
- The goal is not to test whether the model's assumptions are true; they are never exactly right. Failure to conclude a model is false is a failure of imagination, not a success of the model. Models need not be exactly true to give precise, useful inferences. The aim is to check adequacy for some purpose (prediction, comprehension, measurement, persuasion), which depends on scientific context (p. 32).
- *Rethinking: deflationary statistics.* Bayesian inference may be the best general-purpose method, but it is less powerful than we would like. No approach has universal guarantees; math is invented, like the shovel (p. 32).

### 2.3 Components of the model (pp. 32–37)
Three things counted earlier have direct analogs: ways to produce one observation, ways to produce all the data, and the initial plausibility of each conjecture. These become (1) a likelihood function, (2) parameters, (3) a prior, usually chosen in that order (p. 32).

**2.3.1 Likelihood (pp. 32–34).**
- The likelihood is a formula that maps each conjecture (e.g. a proportion of water) onto the relative number of ways the data could occur. It must give the probability of any possible observation for any possible state of the small world (p. 33).
- For globe tossing, nominate the possible events (W, L only). With independent tosses and the same probability of W on every toss, probability theory gives a unique answer, the **binomial distribution** (p. 33):
$$\Pr(w\mid n,p)=\frac{n!}{w!\,(n-w)!}\,p^{w}(1-p)^{n-w}$$
- Read: the count of water $w$ is distributed binomially, with probability $p$ of water on each toss and $n$ tosses in total (p. 33).
- R code 2.2: `dbinom(6, size=9, prob=0.5)` gives `0.1640625`. This is the relative number of ways to get six W with $p=0.5$ and $n=9$ (p. 33). (added step: $\binom{9}{6}=84$ and $84/2^9=84/512=0.1640625$.)
- Likelihoods are sometimes written $L(p\mid w,n)$. This reverses what is left of the bar, but the job is the same: the relative number of ways to see the data $w$ given $p$ and $n$ (p. 33).
- *Overthinking: names.* The "d" in `dbinom` stands for density; partners start with "r" (random samples) and "p" (cumulative probabilities) (p. 33).
- *Rethinking: central role for likelihood.* The most influential assumptions in Bayesian and many non-Bayesian models are the likelihood and its relation to the parameters. They matter more as sample size grows. This helps to explain why the two kinds of inference are often similar (p. 34).

**2.3.2 Parameters (p. 34).**
- Inputs of the binomial likelihood are $p$, $n$ and $w$. Any of them may be a **parameter**, meaning a quantity to estimate; parameters stand for conjectured causes. In globe tossing $n$ and $w$ are data (assumed observed without error), so $p$ is the unknown (p. 34).
- Other analyses target different inputs. Mark-recapture estimates $p$ and $n$ to get population size (the $n$ input) (p. 34). Some data may tell us little; the author says it is usually an advance to learn that data don't discriminate among possibilities (p. 34).
- Later models have more parameters that answer questions such as the average difference between treatment groups or the variation among groups (p. 34).
- *Rethinking: datum or parameter?* In the Bayesian framework the distinction is fuzzy. A datum can be recast as a very narrow density for a parameter, and a parameter as a datum with uncertainty. Chapter 14 uses this for measurement error and missing data (p. 34).

**2.3.3 Prior (pp. 34–36).**
- Every parameter needs a prior: an initial plausibility for each possible value. A previous estimate can become the prior, as in Figure 2.5. At $n=0$ the machine still had a flat line (p. 34–35).
- *Overthinking:* the flat prior is $\Pr(p)=\frac{1}{1-0}=1$. For a uniform prior from $a$ to $b$ the density is $1/(b-a)$, so the area under the flat line is 1. A density value of 1 is not a problem, because the distribution must integrate to 1 (p. 35).
- Priors are "engineering assumptions", chosen to help the machine learn. The flat prior is common but hardly ever best. Priors that gently nudge are called **regularizing** or **weakly informative**. Non-Bayesian penalised likelihood is a mathematically equivalent approach. Such priors tend to guard against inferring strong associations (p. 35).
- Priors can constrain parameters to reasonable ranges and carry knowledge. In globe tossing, $p=0$ and $p=1$ are completely implausible, and values near them are less plausible than values near 0.5 (p. 35).
- **Subjective Bayesian** school (choose priors from the analyst's personal beliefs): thrives in some statistics, philosophy and economics programs; the author says it is rare in the sciences. There, the prior is just part of the model, to be chosen, evaluated and revised. Subjectivist and non-subjectivist often analyse data in nearly the same way. The author says all analysis is subjective in some respects, and priors are no more subjective than likelihoods or repeat-sampling assumptions in significance testing (p. 35).
- If you have no strong argument for a prior, try several and check sensitivity (p. 35).
- *Rethinking: prior, prior pants on fire* (p. 36). **Objection (historical opponents):** flexible priors let you get any answer you want. **Author:** true in principle, but priors have not been used to lie; such a lie is easily uncovered, and the likelihood is a more opaque place to hide one. Likelihood choice is more conventionalised than prior choice, and conventional choices can be poor. Non-Bayesian procedures make comparable choices (estimator, penalty), often equivalent to some prior or loss function (p. 36).

**2.3.4 Posterior (pp. 36–37).**
- Given likelihood, parameters, priors and data, the estimates are a purely logical consequence. There is a unique set for each unique combination. The **posterior distribution** is the relative plausibility of parameter values conditional on the data, $\Pr(p\mid n,w)$ (p. 36).
- Derivation of **Bayes' theorem** (n omitted for simplicity) (pp. 36–37). It re-expresses the garden of forking data using probability rules.
  1. Joint probability: $\Pr(w,p)=\Pr(w\mid p)\Pr(p)$ — likelihood times prior. The author's analogy: P(rain and cold) = P(rain, when cold) × P(cold) (p. 36).
  2. Reverse the conditioning: $\Pr(w,p)=\Pr(p\mid w)\Pr(w)$ (p. 36).
  3. Set the two right-hand sides equal and solve:
$$\Pr(p\mid w)=\frac{\Pr(w\mid p)\Pr(p)}{\Pr(w)}\qquad\text{Posterior}=\frac{\text{Likelihood}\times\text{Prior}}{\text{Average Likelihood}}$$
  4. $\Pr(w)$ is the **average likelihood**, averaged over the prior. It standardises the posterior so it sums (integrates) to one (p. 37):
$$\Pr(w)=\mathrm{E}\big(\Pr(w\mid p)\big)=\int \Pr(w\mid p)\Pr(p)\,dp$$
- E means expectation. Such averages are called marginals, so $\Pr(w)$ is also the **marginal likelihood**; it is also called evidence or probability of the data (p. 37).
- Key lesson: the posterior is proportional to prior times likelihood, because the number of paths is the product of the prior number and the new number. "Multiplication is just compressed counting." The denominator only standardises (p. 37).
- Figure 2.6 shows the same globe-toss likelihood times three priors. A flat prior gives a posterior proportional to the likelihood. A step prior (zero below 0.5) gives a truncated posterior. A peaked prior shifts and skews it (p. 37–38).
- *Rethinking: Bayesian analysis isn't about Bayes' theorem.* Inference under any probability concept eventually uses the theorem. Common HIV and DNA testing examples are not uniquely Bayesian, since all elements are frequencies of observations. What is distinctive is using the theorem to quantify uncertainty about unobservable entities such as parameters and models (p. 37).

*Intuition note.* Bayes' theorem says: multiply what you believed by how well each option explains the data, then rescale so the total is 1. It is the counting rule of §2.1 written with probabilities.

### 2.4 Making the model go (pp. 37–45)
- The posterior comes from *conditioning* the prior on the data. Knowing the formula often does not help, because many interesting models cannot be conditioned formally. Some models, like linear regression, can, but only with priors of special mathematical forms. So we use numerical engines (pp. 38–39): **(1) grid approximation, (2) quadratic approximation, (3) Markov chain Monte Carlo (MCMC)** (p. 39).
- *Rethinking: how you fit the model is part of the model.* In moderately complex problems, the numerical technique influences inference. The same model and data fitted by different techniques may give different answers (p. 39).

**2.4.1 Grid approximation (pp. 39–41).**
- Idea: approximate a continuous posterior with a finite grid of parameter values. At each value $p'$, multiply the prior at $p'$ by the likelihood at $p'$ (p. 39).
- Recipe (p. 39–40): (1) define the grid; (2) compute the prior at each grid value; (3) compute the likelihood at each; (4) multiply for the unstandardised posterior; (5) divide by the sum.
- R code 2.3 (p. 40):
```r
p_grid <- seq( from=0 , to=1 , length.out=20 )
prior <- rep( 1 , 20 )
likelihood <- dbinom( 6 , size=9 , prob=p_grid )
unstd.posterior <- likelihood * prior
posterior <- unstd.posterior / sum(unstd.posterior)
```
- Other priors, code 2.5 (p. 40): `ifelse(p_grid < 0.5, 0, 1)` and `exp(-5*abs(p_grid - 0.5))`.
- Figure 2.7: with 5 points the approximation is "terrible"; with 20 it is already quite good. After about 100 points there is little change in this example (pp. 40–41).
- Grid approximation is mainly a teaching tool. It scales poorly: two parameters with 100 values each already need $100^2=10{,}000$ values, and 10 parameters need many billions (p. 41).
- *Overthinking: vectorization.* R applies a calculation to every element of a vector, so the grid size sets the length of `prior` (p. 40).

**2.4.2 Quadratic approximation (pp. 41–44).**
- Under "quite general conditions", the region near the posterior peak is nearly Gaussian. A Gaussian is described by two numbers: centre (mean) and spread (variance). The log of a Gaussian is a parabola, a quadratic function, hence the name (p. 41).
- It works very well for many common procedures (e.g. linear regression); often it is even exactly correct. It is cheap compared to grid approximation and MCMC (p. 41).
- Two steps (p. 42): (1) find the posterior mode by an optimisation algorithm, which "climbs" the posterior using the local slope; (2) estimate the curvature near the peak, which is enough to compute the quadratic approximation of the whole posterior.
- R code 2.6 uses `map` ("maximum a posteriori", the mode) from the rethinking package, with `w ~ dbinom(9,p)`, `p ~ dunif(0,1)` and `data=list(w=6)` (p. 42). `precis` output (p. 42):

| | Mean | StdDev | 5.5% | 94.5% |
|---|---|---|---|---|
| p | 0.67 | 0.16 | 0.42 | 0.92 |

- Reading: assuming the posterior is Gaussian, it is maximised at 0.67 with standard deviation 0.16. The last two columns are an 89% percentile interval (p. 42).
- Comparison with the exact analytical posterior, `dbeta(x, w+1, n-w+1)`, vs `dnorm(x, 0.67, 0.16)` (code 2.7, p. 43). Figure 2.8: at $n=9$ the approximation is good on the left but poor on the right, and it even gives positive probability to $p=1$, which is impossible since land was seen. At $n=18$ ($w=12$) it is better but not great. At $n=36$ ($w=24$) the curves are nearly the same (p. 43).
- The improvement with more data is very common. It is one reason classical procedures are nervous about small samples. Their approximations are only known to be safe with infinite data. The rate of improvement varies; for some model types the approximation can stay terrible even with thousands of samples (p. 43). If in doubt, use grid approximation (good for small samples) or MCMC (p. 44).
- *Rethinking: MLE.* With a uniform prior or with a lot of data, the quadratic approximation is usually equivalent to the maximum likelihood estimate (MLE) and its standard error. This is a blessing (non-Bayesian fits can be reread in Bayesian terms) and a curse (MLE has drawbacks, explored later) (p. 44).
- *Overthinking: Hessians.* A Hessian is the square matrix of second derivatives of the log posterior with respect to the parameters. Since the log of a Gaussian is a parabola, centre plus second derivative describe it fully. The second derivative is proportional to the inverse squared standard deviation (the "precision"). If the Hessian computation fails, the approximation fails (p. 44).

*Intuition note.* Find the top of the hill, measure how sharply it curves, and replace the whole hill by a bell curve with that peak and curvature. The text shows that this replacement gets better as data increase (Figure 2.8), though how fast varies by model.

**2.4.3 Markov chain Monte Carlo (pp. 44–45).**
- For models like multilevel (mixed-effects) models, with hundreds to tens of thousands of parameters, grid approximation fails because it just takes too long. Quadratic approximation may fail too. Such models may not allow a single unified posterior function, so the function to maximise must be computed in pieces (p. 44).
- MCMC is a family of conditioning engines for complex models. It is largely responsible for the Bayesian surge from the 1990s, together with affordable computers (pp. 44–45).
- It does not compute or approximate the posterior directly; it draws samples from it. The frequencies of the sampled values correspond to posterior plausibilities, and a histogram of them pictures the posterior. We usually work with the samples directly; Chapter 3 does this (p. 45). Examples are in Chapter 8 (p. 45).

### 2.5 Summary (p. 45)
The target of Bayesian inference is a posterior distribution, stating the relative numbers of ways each conjectured cause could have produced the data. A model is a composite of likelihood, parameters and prior. Bayes' theorem gives the logical way to compute the posterior. In practice, grid approximation, quadratic approximation and MCMC are used, each with different trade-offs (p. 45).

### 2.6 Practice (pp. 45–47)
Easy (2E1–2E4), medium (2M1–2M7) and hard (2H1–2H4) problems; see "Exercises worth doing".

## Toy example (ours, not from the text)
A bag holds **3** marbles, blue or white. There are four conjectures: 0, 1, 2 or 3 blue. We draw with replacement: blue, then blue.

1. **Ways to produce blue, blue.** The 1st draw has $k$ ways to be blue, and so does the 2nd. So the ways are $k^2$: $0,\,1,\,4,\,9$. Total $=14$.
2. **Posterior with equal priors:** $0/14=0$; $1/14\approx0.071$; $4/14\approx0.286$; $9/14\approx0.643$. These sum to 1.
3. **Update with a third draw: white.** The ways to see white are $3-k$: $3,2,1,0$. Multiply old counts by new counts: $0\times3=0$; $1\times2=2$; $4\times1=4$; $9\times0=0$. Total $=6$, so the posterior is $0,\ 2/6\approx0.333,\ 4/6\approx0.667,\ 0$.
4. **Check by starting over:** for blue, blue, white the ways are $k\cdot k\cdot(3-k)$, giving $0,\ 1\cdot1\cdot2=2,\ 2\cdot2\cdot1=4,\ 3\cdot3\cdot0=0$. This is the same, so sequential and all-at-once updating agree.
5. **Add a prior:** a factory made 3 one-blue bags for every one two-blue bag (and none of the others). Multiply: $2\times3=6$ and $4\times1=4$. Total $10$, so the posterior is $0.6$ for one blue and $0.4$ for two blue. The prior reverses the order of the two surviving conjectures.

## Concepts
- [[small-world-large-world]] (new) — the model's self-contained logic versus the real setting where it is used; small-world consistency is no guarantee of large-world optimality (p. 19)
- [[garden-of-forking-data]] (new) — enumerate all event sequences a conjecture allows; prune those that contradict the data; count the rest (p. 21)
- [[bayes-theorem]] — posterior = likelihood × prior / average likelihood, derived by equating two factorisations of the joint probability (p. 37)
- [[prior-distribution]] — initial plausibility for each parameter value; an engineering assumption to be checked, not a belief to be sworn to (p. 34–35)
- [[likelihood]] — formula giving the relative number of ways the data arise for each parameter value; here the binomial (p. 33)
- [[posterior-distribution]] — plausibility of parameter values conditional on the data, $\Pr(p\mid n,w)$ (p. 36)
- [[marginal-likelihood]] — $\Pr(w)=\int\Pr(w\mid p)\Pr(p)\,dp$, the likelihood averaged over the prior; standardises the posterior (p. 37)
- [[sequential-updating]] — each posterior becomes the next prior; order of data does not matter in this model, and updating can be reversed (p. 31)
- [[principle-of-indifference]] — with no reason to prefer a conjecture, weigh all equally; the author notes that "ignorance" is a complicated notion (p. 26)
- [[subjective-probability]] — the "subjective Bayesian" school choosing priors from the analyst's beliefs; the author treats the prior as part of the model instead (p. 35)
- [[frequentist-vs-bayesian]] — the author stresses similarities (likelihood central; MLE ≈ quadratic approximation; penalised likelihood ≈ regularising prior) alongside differences (pp. 26, 34–35, 44)
- [[parameter]] (new) — an unknown input of the likelihood that data are used to estimate; the datum/parameter line is fuzzy (p. 34)
- [[data-story]] (new) — narrative of how the data arise; many stories fit one model (pp. 28–29)
- [[regularizing-prior]] (new) — prior that gently nudges inference and tends to guard against inferring strong associations; penalised likelihood is a mathematically equivalent approach (p. 35)
- [[grid-approximation]] (new) — posterior computed on a finite grid of parameter values: prior × likelihood, then standardise (p. 39)
- [[quadratic-approximation]] (new) — Gaussian approximation at the posterior mode, using the curvature there; improves with more data (pp. 41, 43)
- [[markov-chain-monte-carlo]] — conditioning engine that draws samples from the posterior instead of computing it directly (p. 44–45)

## Canonical instances
- [[columbus-small-world]] — a small-world model (the Earth is 30,000 km around) gave a lucky large-world surprise (p. 19)
- [[marble-bag]] — four marbles, five conjectures, counts 0/3/8/9/0, updates to 0/3/16/27/0 and 0/9/32/27/0 (pp. 21–26)
- [[globe-tossing]] — W L W W W L W L W (6 W, 3 L); binomial likelihood; grid and quadratic approximation (pp. 28–43)
- [[garden-of-forking-paths-borges]] — story used as an analogy for considering all possible paths (pp. 20–21)

## Bridges (candidates)
- [same-math] Grid approximation ↔ numerical integration: evaluating a function at grid points and normalising by the sum approximates the integral in $\Pr(w)$ (not stated in this unit).
- [same-math] Quadratic approximation ↔ Gaussian (Laplace-type) approximation of a density at its mode using the second derivative of the log density (the chapter gives only the mode-plus-Hessian procedure).
- [structural-analogy] Small world vs large world ↔ model misspecification: inference is conditional on the model, so confidence does not certify the model.
- [structural-analogy] Multiplying prior counts by new counts ↔ Bayesian updating in log-odds or log scale: logs turn products into sums (not in this unit).
- [metaphor] The "golem" as a machine that executes assumptions without judgment ↔ any automated estimator whose output is only as good as its inputs.

## Questions this raises
- How large must a posterior difference be before we can "safely decide" between conjectures (flagged for Chapter 3, p. 26)?
- How can we check a model against aspects of the data it ignores (e.g. order of tosses), when such checks are "creative" (pp. 31–32)?
- When does quadratic approximation remain poor even with thousands of samples (p. 43)?
- How can "ignorance" be represented faithfully when the principle of indifference is "surprisingly complicated" (p. 26)?

## Exercises worth doing
- Ex. 2E4 (p. 46) — de Finetti's "probability does not exist"; asks what "the probability of water is 0.7" means in the globe example — difficulty: medium
- Ex. 2M1 (p. 46) — grid-approximate the posterior for three small samples with a uniform prior; builds the recipe of §2.4.1 — difficulty: easy
- Ex. 2M2 (p. 46) — repeat 2M1 with a prior that is zero below 0.5; shows how a prior truncates the posterior — difficulty: easy
- Ex. 2M3 (p. 46) — Earth/Mars globes: posterior probability of Earth given "land" (the text states the target value 0.23) — difficulty: medium
- Ex. 2M4 (p. 46) — three-card problem by counting ways (target 2/3); the counting method on a classic puzzle — difficulty: medium
- Ex. 2H4 (p. 47) — combine a noisy test with birth data; shows how data of different types are used together — difficulty: hard

## Reading notes
- Printed page = pdf page − 14 (pdf 33 = printed 19). Printed p. 48 (pdf 62) has no text in the text layer; no image was supplied for it.
- The text layer lacks the marble glyphs (conjectures, data) and garbles the Figure 2.5 labels. I used the page images for pp. 22–26 and Figure 2.5. No image was supplied for printed p. 21, so I relied on the surrounding text there.
- Probable misprint: on p. 40, code 2.5 is introduced as replicating "the different priors in Figure 2.5". The step and peaked priors appear in Figure 2.6 (p. 38), while Figure 2.5 shows only the flat start.
- Exercise 2M4 refers to "Section 2 of the chapter" for the counting method; the counting is in §2.1.
- The text uses `map` for the quadratic approximation as printed (pp. 42–43). On printed p. 37, "It's job" is a typo for "Its job".
- The output labels the mode as "Mean". The author notes that the value is the posterior's peak (p. 42).
