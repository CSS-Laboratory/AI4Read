---
id: grimmer-2022-textasdata/ch21-repurposing
work: grimmer-2022-textasdata
unit: Chapter 21. Repurposing Discovery Methods
pages: 350-366
fields: [political-science]
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
# Repurposing Discovery Methods

## L0 — One line
The authors advise using unsupervised discovery models for measurement by splitting the data, choosing a model for its fit to the concept, and validating in training and test data, because the model's output alone does not show that anything was measured.

## L1 — The gist (≤ 120 words)
The chapter asks when and how clustering, topic models and scaling models, built for discovery, can measure a concept. They compress text, so they tend to capture prominent subject matter better than subtle properties such as tone. The authors advise splitting the corpus, fitting and choosing a model on the training part, validating it, then applying the fitted parameters to the test part and validating again. Common worries are that the model always returns a result, depends on the estimation method and hyperparameters, and is unstable. The authors answer that value comes from validation, not from the model. They treat different solutions as different measures, not as noisy estimates of one truth.

**Prerequisites:** topic models (mixed-membership, K topics); hyperparameters (model settings the analyst chooses, such as K); train/test splitting and overfitting; Poisson distribution; local vs global optima; the supervised-validation ideas of Ch. 20.

## L2 — Key ideas (5–10 bullets)
- Discovery and measurement should be done on different data. Splitting the corpus resolves some concerns about unsupervised measurement. (p. 350)
- Unsupervised models compress text, so they tend to favor frequent, subject-matter words over style or tone. What they return is a parsimonious compression, not a true latent structure. (p. 351)
- Wordfish, a Poisson text-scaling model, needs ideology to be the main distinguishing feature of the language in order to recover it. It appears to work on German party platforms but does not separate the parties on US Senate press releases, where it finds another, nonideological dimension. (pp. 352–353)
- Four-step workflow: split, fit (try many models), validate, then fit to test data and revalidate. (pp. 356–359)
- Validation tools are hand coding (coarsening continuous output where needed), surrogate labels (labels made for another purpose), hypothesis validity (relationships specified in advance), and the weaker model-based checks such as held-out likelihood (fit on data not used in training). (pp. 357–359)
- Four concerns (always returns a result, estimation differences, hyperparameters, instability) all get one reply: justify the measure by validation. (pp. 360–362)
- The stability critique assumes one fixed target. The authors reply that each respecification measures something different, as with different content-analysis teams. (pp. 363–364)
- Unsupervised output is like repurposed data: designed for another purpose, so check the gap to your ideal data. (p. 365)

## L3 — Walkthrough

### Introduction (p. 350)
Discovery methods (single-membership clustering, mixed-membership topic models, low-dimensional embeddings) need little human input up front. They can also be used for measurement. The authors say discovery and measurement are often blurred, including in their own work, and advocate doing the two on different data sets. Example: Grimmer and King (2011) discovered their conceptualization from a small single-senator corpus, then applied a measurement strategy to a different corpus to confirm it (p. 350).

### 21.1 Unsupervised methods measure subject better than subtleties (p. 351)
- Clustering, topic models and embeddings work by compression: they squeeze high-dimensional information through a low-dimensional channel. A topic model must represent $J$ words with $K$ topics, and $J$ is usually much larger than $K$. So words that co-occur share a topic.
- The need to explain all observed words tends to favor frequent words. Language is noun-heavy, especially after stop-word removal. This tends to weight topic models toward subject matter rather than, for example, sentiment. No explicit modeling decision forces this.
- Unsupervised methods are more likely to work well when the goal is the primary subjects of the text rather than style, tone or other subtle properties. They are most sensitive to what is prominent.
- For something subtler, change the document-feature matrix. Example: with part-of-speech tagging, one could discard everything except adjectives and adverbs to push the model more toward sentiment. If the target quantity is not a large part of the preprocessed text, the methods may be too coarse.
- Consistent with the authors' agnostic view, the output is not a true latent structure but a parsimonious compression. A topic is a distribution over words that reconstructs the bag-of-words representation reasonably well. Meaning is justified by validation more than by the model.

*Intuition note:* The need to explain all words favors the most common ones, so the model tends to find what texts are mostly about. Quiet features such as tone can easily be missed.

### 21.2 Example: scaling via differential word rates (pp. 352–353)
- Monroe and Maeda (2004) and later Slapin and Proksch (2008) introduced item-response-theory (IRT) text models to estimate positions of political parties. Actors are assumed to reside in a low-dimensional political space, and their position is assumed to affect word-use rates. (p. 352)
- Wordfish is a Poisson-IRT model. Word $j$ from individual $i$ is $W_{ij}\sim \text{Poisson}(\lambda_{ij})$ with
$$\lambda_{ij}=\exp(\alpha_i+\psi_j+\mu_j\pi_i).$$
Here $\alpha_i$ is loquaciousness (how much $i$ writes), $\psi_j$ is the frequency of word $j$, $\mu_j$ is how much word $j$ discriminates along the ideological space, and $\pi_i$ is the actor's position (p. 352).
- This needs an **ideological dominance assumption**: the primary distinguishing feature of the actors' language is ideology. If it holds, the model reliably captures ideological differences. It fails when these are dwarfed by other variation, such as policy vs pork focus, writing style or tone. With no explicit supervision, it is difficult to guarantee that the output is ideology, so the model requires careful validation (p. 352).
- Figure 21.1 (reproduced from Grimmer and Stewart 2013): on German party platforms, Wordfish separates the parties and replicates expert assessments of party movement over time (as Slapin and Proksch show). (p. 353)
- On Senate press releases (Grimmer 2010), Wordfish fails to separate Democratic and Republican senators, which any valid ideological scaling of the polarized Senate must do. Its scaling is substantively meaningful but nonideological. It correlates 0.86 with the expressed-agenda scaling of Grimmer (2013b), which captures how senators balance position taking and credit claiming. (p. 353)
- Lesson: unsupervised methods are likely to recover the measure of interest when the concept coincides with highly frequent subject matter. Careful validation is needed to confirm the intended space was found. (p. 353)

*Intuition note:* Wordfish needs ideology to be the main way actors' word use differs. In party platforms it appears to be. In press releases the method retrieves a different, nonideological dimension.

### 21.3 Workflow (pp. 354–359)
The researcher already has a measure in mind. The running example estimates the proportion of a newspaper corpus about the environment with a topic model (p. 354).

**21.3.1 Split the data (p. 356).** Split into training and test sets. This allows exploring approaches without overfitting or choosing a measure for the results it gives, and it tests generalizability. The split size depends on the concept and the data available. Training needs enough data for a reliable, generalizable measure. Test needs enough for precise final measurements.

**21.3.2 Fit the model (pp. 356–357).** Fit on the training data, trying different numbers of topics, starting values, stopping rules or hyperparameters. The goal is the model that best captures the concept. Refitting does not invalidate the final measure. Suppose an environment topic appears in only one of many fitted models. That does not mean the corpus lacks environment documents or that the model with the topic is wrong. Pick the model that best aligns with the concept.

**21.3.3 Validate (pp. 357–359).**
- *Hand coding.* Coders label a random sample, e.g. "about the environment" or not. Compare the hand-coded proportion with the topic model's estimate, and compare topic loadings in the two groups. Output is often continuous, so it may need coarsening. A coder may confirm an article is substantially about the environment but not that it accounts for .18 of tokens. Hand coding and nonexpert evaluation also help label topics (e.g., from top words or representative documents). (p. 357)
- *Surrogate labels.* If hand coding is not possible, use labels made for another purpose, such as keyword tags in a newspaper database. See Ch. 20 for pitfalls. (p. 358)
- *Hypothesis validity.* Specify in advance relationships whose absence would indicate failure. Example: flu news should rise in winter and fall in summer. Catalinac (2016a) uses an LDA topic model on Japanese candidate manifestos. Agriculture and forestry topics are more prevalent in rural than urban areas, and tourism and industry topics more prevalent in urban areas (her p. 97). (p. 358)
- *Model-based assessments.* Perhaps the least revealing, because models matter only instrumentally. They are often the easiest to compute and can be useful supplements, if certainly not replacements. For generative text models the most straightforward is held-out log-likelihood, the fit on a sample not used in training. For a test document the target is
$$p(W_{i,\cdot}\mid W_{\text{train}})=\int_{\pi_i,\mu} p(W_{i,\cdot},\pi_i,\mu\mid W_{\text{train}})\,d\pi_i\,d\mu,$$
which is intractable (the symbol after the comma in $W_{i,\cdot}$ is missing in the page; I use a dot). Wallach et al. (2009) compare approximations, which are interpretable only comparatively. Foulds and Smyth (2014) estimate relative performance between models with annealing paths. Optimizing held-out likelihood optimizes a task we are not engaged in (predicting term counts). It protects against one kind of overfitting but does not ensure we captured anything about meaning. (pp. 358–359)

**21.3.4 Fit to test data and revalidate (p. 359).** This means using the parameters estimated on training data to produce output for the test data. It does not mean rerunning the same model on new data. Training validation gives some assurance, particularly if the training data were randomly sampled. The measure may still fail in the test data, so the authors recommend a second validation there.

*Intuition note:* Choose and check the measure on one slice of data, freeze it, then apply it to unseen data and check again.

### 21.4 Concerns (pp. 360–364)
All concerns get one common reply: the measure is justified by validation, not by the model. Discussion uses mixed-membership topic models, but the concerns are more general (p. 360).

**21.4.1 Always returns a result (p. 360).** **Objection:** if the model yields clusters/topics/scales even on random data, how can it be valid measurement? **Authors:** like regression always returns a line, latent variable models always return some structure. Labeling and validating, not the output, show that something was measured. The objection is right that these models tend to be poor tools for asserting a particular underlying structure. $K=5$ gives only minimal evidence of five clusters. It gives the best five-cluster approximation to whatever structure exists. The authors do not think there is a "true" structure in real data, only things more or less useful for goals.

**21.4.2 Opaque differences in estimation (p. 361).** For vanilla LDA (a Bayesian model approximating a posterior) there are three broad inference approaches: collapsed Gibbs sampling, variational inference and spectral methods. Differences can matter. A single pass of collapsed Gibbs tends to give sparse-looking topics (few topics per document, few words per topic). Variational approximation is typically dense. So judging how "focused" documents are can be fraught. Recommendation: always report the estimation approach and the software.

**21.4.3 Hyperparameters (p. 361).** Beyond $K$, other hyperparameters can substantially affect performance and practitioners have few intuitions. When forced to set them manually, try many options and choose by substantive fit.

**21.4.4 Instability (pp. 361–363).**
- The optimization problems are non-convex, so results depend on starting values and each run can differ. The model finds local, not global, optima. (p. 362)
- Fixing the random seed addresses computational reproducibility (see footnote 2 on its limits), but not the whole problem. Roberts, Stewart and Tingley (2016) propose initialization with a deterministic estimator from Arora et al. (2013), globally consistent under certain conditions. It does not guarantee the globally best solution in any one case but performs well empirically and has asymptotic guarantees. (p. 362)
- Models remain sensitive to preprocessing and data changes (Denny and Spirling 2018; Wilkerson and Casas 2017). Small perturbations may turn a local optimum into the global one, so the local/global distinction is arguably less relevant. The authors still believe a local optimum is important, because it lets us know that, given what we are measuring and the data we have, this is the best fit. (p. 362)
- **Denny and Spirling's view:** the subtler problem is that well-meaning scholars would have no idea of the truth value of their findings. Unsupervised models typically allow many specifications and many plausible "stories" fit and validated after estimation, so a lack of attention to preprocessing produces a potentially virulent set of "forking paths" (Gelman and Loken). In the absence of strong theory, the authors would like to see robustness to preprocessing decisions and ideally averaging over alternatives. Wilkerson and Casas make a similar appeal for parameter values. (pp. 362–363)

**21.4.5 Rethinking stability (pp. 363–364).**
- Discovery methods supply a workable surrogate criterion for an unspecified measurement objective. It sometimes measures the concept and sometimes does not. (p. 363)
- **Authors' reply:** the critiques presume a stable underlying target, with each solution an approximation to it. Under that view, seeking robust results makes sense. The authors argue instead that every respecification captures something different about the documents. Instability in measuring a fixed concept should not be confused with differences in the concept chosen. A properly validated measurement is constrained by the documents' actual content. (p. 363)
- Analogy: most scholars would find it absurd if someone claimed there was only one right way to read a text. In manual content analysis, two teams would produce different coding schemes, and neither is dismissed for that. Judge the enterprise by what the measure tells us about the world, not by whether methods agree. (p. 364)

### 21.5 Conclusion (pp. 365–366)
Drawing on Salganik (2018) on repurposed data, the authors find it helpful to think of unsupervised results as measurement designed for another purpose, so there is always some gap between what the user wants and what the output is. This is no reason to abandon them. Salganik advises understanding the process that created the data and comparing it with the ideal dataset (p. 365). Here that means understanding what objective the model optimizes and comparing real data with ideal data. Part 4 covered dictionaries, supervised learning and repurposing. Human-coded training sets with gold-standard validation are perhaps the most robust approach but need resources. Dictionaries, found-data supervision and repurposed discovery methods can be effective substitutes when supervised learning is not practical, and all of these methods, including supervised classification, require extensive validation. The next part is Inference (p. 366).

## Toy example (ours, not from the text)
Aim: measure the share of articles about the environment. Training validation sample of 6 articles, with the topic loading and a hand code (1 = environment):

| Article | Loading | Hand code |
|---|---|---|
| 1 | 0.45 | 1 |
| 2 | 0.30 | 1 |
| 3 | 0.05 | 0 |
| 4 | 0.12 | 0 |
| 5 | 0.60 | 1 |
| 6 | 0.28 | 0 |

Coarsen at 0.25 (our choice): loading ≥ 0.25 → 1. Coarsened codes: 1, 1, 0, 0, 1, 1. Agreement: articles 1–5 match and article 6 does not, so 5/6 ≈ 0.83. Model share = 4/6 ≈ 0.67, hand-coded share = 3/6 = 0.50. The gap prompts refitting or relabeling in training. When satisfied, freeze the parameters and apply them to the test articles, then repeat a hand-coded check on a test sample.

## Concepts
- [[text-as-data-validation]] — measure from unsupervised output is justified by validation, not by the model (pp. 351, 360)
- [[unsupervised-measurement-workflow]] (new) — split, fit and choose on training, validate, then apply fitted parameters to test and revalidate (pp. 356–359)
- [[ideological-dominance-assumption]] (new) — scaling recovers ideology only if ideology is the primary distinguishing feature of the language (p. 352)
- [[wordfish]] (new) — Poisson-IRT text scaling, $\lambda_{ij}=\exp(\alpha_i+\psi_j+\mu_j\pi_i)$ (p. 352)
- [[hypothesis-validity]] (new) — validating a measure by relationships specified in advance whose absence would indicate failure (p. 358)
- [[held-out-log-likelihood]] (new) — model fit on data not used in training; weak evidence of measurement validity (pp. 358–359)
- [[forking-paths-preprocessing]] (new) — many specifications permit post hoc "stories"; Denny and Spirling's worry (p. 363)
- [[observable-implications]] — hypothesis validity tests testable consequences of the measure (p. 358)

## Canonical instances
- [[wordfish-german-platforms]] — ideological dominance holds; separates parties, matches expert assessments (p. 353)
- [[wordfish-senate-press-releases]] — fails to separate parties, but correlates 0.86 with the expressed-agenda scaling (p. 353)
- [[catalinac-manifestos-lda]] — LDA on Japanese manifestos validated by rural/urban topic differences (p. 358)
- [[flu-news-seasonality]] — expected winter rise validates a flu topic (p. 358)
- [[environment-topic-example]] — running example for the workflow (pp. 354–357)

## Bridges (candidates)
- [structural-analogy] train/test split for measurement ↔ supervised learning: held-out evaluation guards against overfitting to the selection process (p. 356).
- [structural-analogy] Wordfish's $\pi_i$ ↔ spatial model of voting: positions in a low-dimensional space inferred from behavior (here word use).
- [structural-analogy] Denny–Spirling "forking paths" ↔ researcher degrees of freedom in quantitative social science: many analytic choices, post hoc interpretation.
- [metaphor] "many valid coding schemes" ↔ qualitative content analysis: different teams, different measures, judged by what they reveal.

## Questions this raises
- How can one tell, before validation, whether the ideological dominance assumption holds in a new corpus?
- How should one decide the coarsening threshold when comparing continuous topic proportions with hand codes?
- If each respecification measures a different concept, how should a researcher report the choices so readers can judge the concept chosen?
- How large a training share is enough to generalize without leaving the test set too small for precise estimates?

## Reading notes
- Printed page = pdf page (offset 0).
- The text layer for pdf 355 shows only the page number, and no image was provided for it. Figure 21.1 appears only by caption (p. 356), so its details come from the prose on p. 353.
- The source calls the position parameter $\theta_i$ in the text before the equation and $\pi_i$ in the equation (p. 352). I use $\pi_i$ in the formula.
- Text-layer and image of the held-out likelihood integral (p. 359) show a missing symbol after the comma in $W_{i,\cdot}$. I used a dot.
- Footnote 1 says §21.2 reproduces Sections 7.2 and 7.3 of Grimmer and Stewart (2013).
