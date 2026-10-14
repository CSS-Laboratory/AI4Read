---
id: grimmer-2022-textasdata/ch24-causal
work: grimmer-2022-textasdata
unit: Chapter 24. Causal Inference
pages: 407-428
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Causal Inference with Text as Data

## L0 — One line
If the function that turns text into a measure (g) is discovered and used for causal estimation on the same data, SUTVA breaks and results may overfit, so discover g on one part of the data (or in an earlier experiment) and estimate effects on another.

## L1 — The gist (≤ 120 words)
Prediction asks what will happen and measurement describes; causal inference asks what would have happened under another treatment. Text does not remove the usual causal problems: confounding, reverse causality, dependence between observations and the missing counterfactual. Text adds a new one. If g is built from the same data used for the final analysis, each unit's potential outcome can depend on other units' treatment status, which violates SUTVA; g may also fit noise. The chapter offers three workflows: fix g beforehand, split the sample (discover g on training data, estimate once on the untouched test set), or run sequential experiments. Each has a different cost: losing discovery, losing efficiency, or needing more time.

**Prerequisites:** potential outcomes notation; difference in means and simple regression; train/test split and validation from earlier chapters of the book.

## L2 — Key ideas (5–10 bullets)
- Causal inference estimates unobserved counterfactuals. The observed group difference recovers the average effect only under conditions such as SUTVA and ignorability (pp. 410–413).
- Prediction and causal inference differ in aim. Prediction tolerates biased coefficients and uses the test set to tune. Causal work needs care about each variable's role, and uses sample splitting for identification and honest uncertainty (p. 414).
- Text does not exempt a study from confounding, reverse causality or dependence between observations. Conceptualization of treatment and outcome stays critical (p. 416).
- The mapping function g compresses text into a low-dimensional measure. Treatment effects can be rewritten in terms of g (pp. 420–422).
- Discovering g on the same data used for estimation creates the Fundamental Problem of Causal Inference with Latent Variables (FPCILV), a SUTVA violation, and invites overfitting (pp. 422–423).
- Workflow options: define g in advance (loses discovery), train/test split (loses efficiency), sequential experiments (costs time, tests generalizability) (pp. 424–427).
- Split-sample discovery inside the experiment is proposed as a less wasteful alternative to rigid pre-analysis plans (p. 418).

## L3 — Walkthrough

### Introduction (pp. 407–409)
- Prediction models (spam, clicks, search) learn from labelled data. Social scientists often want to inform policy, which means estimating what would have happened in a different version of the world (p. 407).
- Early social-science text work was descriptive (discovery and measurement). Some models already used metadata, such as author or time (Grimmer 2010, 2013b; Quinn et al. 2010) (pp. 407–408).
- This led to the question of whether a treatment indicator could be included to estimate effects on a text outcome. Roberts et al. (2014) and Roberts, Stewart and Airoldi (2016) used the Structural Topic Model for this, and Gill and Hall (2015) used permutation tests (p. 408).
- This chapter defines the assumptions needed when text is the treatment, outcome or confounder. Chapters 25–26 give text-as-outcome and text-as-treatment examples. Chapter 27 covers conditioning on text in observational studies (pp. 408–409).

### 24.1 Introduction to Causal Inference (pp. 410–413)
- **Setup.** Causal inference identifies the effect of treatment $t_i$ on outcome $y_i$. Take two states, treatment and control. Each unit has two *potential outcomes*, $y_i(1)$ and $y_i(0)$ (p. 410).
- The individual causal effect is $y_i(1)-y_i(0)$. Only one outcome (the *factual*) is observed. The other (the *counterfactual*) is not. This is the *fundamental problem of causal inference* (Holland 1986) (p. 410).
- **Average effect.** The target becomes $\bar y^T-\bar y^C$, with $\bar y^T=\frac1N\sum_{i=1}^N y_i(1)$ and $\bar y^C=\frac1N\sum_{i=1}^N y_i(0)$. Neither is directly observable (pp. 410–411).
- **Decomposition.** Let $p_T$ be the share of treated units, and let $T$ and $C$ be the sets of treated and control units. Write $\bar y^{\,s}_{i\in G}$ for the mean potential outcome under state $s$ among group $G$ (notation reconstructed from context: the page text and image are flattened, so which index is subscript and which superscript is inferred from the observed versus unobserved terms):

$$\bar y^T-\bar y^C=\underbrace{p_T\big(\bar y^T_{i\in T}-\bar y^C_{i\in T}\big)}_{\text{Avg. effect on treated}}+\underbrace{(1-p_T)\big(\bar y^T_{i\in C}-\bar y^C_{i\in C}\big)}_{\text{Avg. effect on control}}$$
$$=\underbrace{p_T\bar y^T_{i\in T}-(1-p_T)\bar y^C_{i\in C}}_{\text{observed terms}}+\underbrace{(1-p_T)\bar y^T_{i\in C}-p_T\bar y^C_{i\in T}}_{\text{unobserved}}$$
  (p. 411)
- $\bar y^T_{i\in T}$ and $\bar y^C_{i\in C}$ are observed. The two counterfactual means are not (p. 411).
- The authors say the observable difference $\bar y^T_{i\in T}-\bar y^C_{i\in C}$ works only if $\bar y^T_{i\in T}=\bar y^T_{i\in C}$ and $\bar y^C_{i\in T}=\bar y^C_{i\in C}$. That is, observed outcomes substitute for the missing ones. This happens only when potential outcomes are unrelated to assignment (p. 411).
- **What can go wrong (1): SUTVA.** The stable unit treatment value assumption says an observed outcome under a treatment status reflects that unit's counterfactual for that status. It rules out interference between units and requires the treatment to be consistent across units (p. 411). Example: a news story is shared with a treated group on social media, the treated group re-shares it, and the control group also sees it. The control group is then no longer a good counterfactual (p. 412).
- **What can go wrong (2): confounding.** The treatment–outcome association may include non-causal parts. Estimation then needs *ignorability*, $(y_i(1),y_i(0))\perp t_i$. Example: if people opt in to news stories, those interested in politics select in, and the groups differ from the outset (p. 412).
- **Randomization** is a powerful remedy. Assignment by a random number generator makes assignment independent of potential outcomes because units cannot select in. On average across experiments the groups are similar (p. 412).
- **Regression.** If SUTVA and ignorability hold, a simple regression recovers the average treatment effect (footnote 1: only with no covariates and binary treatment, where it is a difference in means) (p. 412, p. 428):

$$y_i=\beta_0+\beta_1t_i+\varepsilon_i.$$
$$\bar y^T_{i\in T}=E[y_i\mid t_i=1]=\beta_0+\beta_1+E[\varepsilon_i\mid t_i=1],\qquad \bar y^C_{i\in C}=E[y_i\mid t_i=0]=\beta_0+E[\varepsilon_i\mid t_i=0].$$
  The difference equals $\beta_1$ only when errors are uncorrelated with treatment status, which is another way of saying assignment is uncorrelated with potential outcomes (pp. 412–413).

*Intuition note.* We never see both outcomes for one person. A group comparison stands in for the missing one only if the two groups would have behaved alike under either treatment status.

### 24.2 Prediction, measurement and causal inference (p. 414)
- Supervised learning in earlier chapters also began from a simple regression. Here the aim differs: the causal estimand is the gap between the counterfactual and what happened. We want the best guess of the *potential* outcome, not accurate prediction of an outcome we already observe (p. 414).
- In prediction, what enters the model matters little if predictions are accurate, and biased coefficients are acceptable if they improve prediction. In causal inference, the role of each variable must be considered to avoid post-treatment bias and confounding (p. 414).
- Both tasks use a split sample, but differently. In prediction it estimates error and tunes the model. In causal inference it serves identification and correct characterization of uncertainty around the effect (p. 414).

### 24.3 Key principles (pp. 416–419)
(The chapter introduction promises five principles. This section has three headed principles; see Reading notes.)
- **24.3.1** Text does not remove the core problems. The fundamental problem remains. A good design, attention to the sample and caution with selection on observables are still needed. Confounding, reverse causality and dependence between observations are as plausible with text (p. 416).
- **24.3.2** Conceptualization remains critical, especially whether information about treatment and control was used to develop it (p. 416). Two risks:
  - *Overfitting*: capturing non-systematic noise. In causal work this can make us infer a systematic effect that does not exist (p. 416).
  - *FPCILV* (Egami et al. 2018): if the mapping function is built from the same data as the final analysis, one unit's estimated potential outcome depends on other units' treatment status. This violates SUTVA (p. 417).
- **24.3.3 Sequential science.** Theory and experiments update each other, so no experiment is pivotal and replication matters (p. 417).
  - Many have suggested (Humphreys et al. 2013) that all parameters be laid out before the experiment, including variables, measures and final tests. In the authors' words, the mapping function must then be specified before the experiment. Pre-registration with a pre-analysis plan (PAP) is the proposed tool and ties the researchers' hands (p. 417).
  - The authors say this requires much certainty and a smooth experiment. With high-dimensional text, researchers may not foresee the topics and sentiments that appear. PAPs get amended, and once alteration is allowed, the abuses PAPs defend against reopen (p. 418).
  - The authors instead recommend running the theory–experiment interplay *within* each experiment. Randomly split the texts into training and test sets. With g in hand, the training set checks for deviations and validates the measure, and then a PAP is written and the test data analysed. Without g, the training set is used to discover a coding scheme and set clear rules (p. 418).
  - They argue this avoids FPCILV, limits overfitting, constrains researcher degrees of freedom, and is less wasteful than a PAP written before any data (p. 418).

*Intuition note.* The authors accept that exploring data is useful. Their rule is that exploration must be finished before the data used for the causal estimate is opened.

### 24.4 The Mapping Function (pp. 420–423)
- The mapping function $g$ (Egami et al. 2018) reduces text to a low-dimensional summary used in later analysis (p. 420). Examples: an LDA topic model for attention to foreign policy in Japanese manifestos (Catalinac); a supervised classifier for race-related discourse (Gillion); a Naive Bayes-based scale for cleric support for jihad (Nielsen) (p. 420).
- Mapping functions appear even without text: the Polity Index collapses institutions into one number. Authors should ask how well measures reflect the concept (p. 420).
- g is a tool for a research question, not a model of how texts were produced (p. 420).

**24.4.1 Causal inference with g.** Three assumptions identify the average treatment effect (p. 421), with $\mathcal T$ the set of treatment values:
- Assumption 1 (SUTVA): for all $i$, $y_i(t)=y_i(t_i)$.
- Assumption 2 (Ignorability): $y_i(t)\perp t_i$ for $t\in\mathcal T$.
- Assumption 3 (Positivity): $\Pr(t_i=t)>0$ for $t\in\mathcal T$.

Two cases are distinguished: *text as outcome* (binary treatment, multidimensional $y_i$) and *text as treatment* (scalar outcome, multidimensional $t_i$) (p. 421).
- Take g as known. Compression $\pi_i$ takes values in a space $\mathcal P$. In text as outcome, $g:\mathcal Y\to\mathcal P_y$ and $g(y_i)=\pi_i$. In text as treatment, $g:\mathcal T\to\mathcal P_t$ and $g(t_i)=\pi_i$. For text as treatment, $\mathcal P$ is typically taken as $K$ binary feature vectors (p. 422).
- With binary treatment and outcome mapped into $K$ categories, $g(y_i(1))=\pi_i(1)$ and $g(y_i(0))=\pi_i(0)$, and:

$$\mathrm{ATE}_k=E[g(y_i(1))_k-g(y_i(0))_k]=E[\pi_{ik}(1)-\pi_{ik}(0)]\tag{24.4.1}$$
  (p. 422)

**24.4.2 Identification and overfitting.** Egami et al. (2018) name two problems with discovering g while estimating effects (p. 422).
- **FPCILV.** A discovered g depends on the text of all units. Examples are topic models using document similarities, supervised learners using all texts, and hand-coding schemes based on observed differences. Had the texts differed, a different g would probably have been found. So each $\pi_i$ depends on others' texts. In text as outcome, potential outcomes are affected by other units' treatment assignments. In text as treatment, treatments affect each other through g. Potential outcomes then cannot be defined without reference to other units (p. 423).
- **Overfitting.** Text is high-dimensional, so many possible g's exist and some features will relate to treatment by chance. Example: by chance many treated texts use "sunny". A researcher may select it as a measure, a form of fishing (Simmons et al. 2011), or add it to a sentiment dictionary because of its meaning. The finding would not generalize (p. 423).

*Intuition note.* If the ruler is built from the same measurements it is used on, then changing one document's treatment can change everyone's score. Also, with many word features, some will track treatment by luck alone.

### 24.5 Workflows (pp. 424–427)
Common feature: separate discovery of g from effect estimation (p. 424).

**24.5.1 Define g beforehand.** Use an existing dictionary (Ch. 16) or codebook (Ch. 18), then estimate directly (p. 424). Drawbacks: off-the-shelf dictionaries may not generalize (Loughran and McDonald 2011). Boydstun (2013) updated and annotated the Policy Agendas Codebook to apply it accurately. Fixing g in advance gives up discovery and may yield an unsatisfactory proxy (p. 424).

**24.5.2 Train/test split** (Fong and Grimmer 2016; Egami et al. 2018). In the test set g does not depend on any unit's treatment status, which addresses FPCILV. It addresses overfitting by checking that training-set relationships generalize (pp. 424–425). Steps:
1. **Split.** Choose the proportions by the trade-off between data needed to discover g and data needed for a precise effect. Choose training documents at random. Do not touch or view the test set until g is estimated. The test set may be used only once. Cross-validation would produce multiple measures (one per fold) and would violate FPCILV across them. The procedure is closer to the single final-use test split of Chapter 21 (p. 425).
2. **Discover g** on training data with any methods in the book, aiming for a measure that is useful and generalizable (p. 425).
3. **Validate g** (Chs. 12, 20, 21), often by splitting the training set further (p. 425).
4. **Apply to the test set and revalidate.** Before opening the test set, fix how text is represented and how g is applied. A PAP or declared design can be written at this point (p. 426). Apply g and estimate the average effect. Then check test-set accuracy and interpretation. If g fits poorly, one cannot return to the training data or change g, but the failure still shows how to improve measures in future experiments (p. 426).
- Cost: less data for the ATE, and we do not know how much training data is needed (the "power we need for discovery"). Optimal partitioning is left to future work (p. 426).

**24.5.3 Sequential experiments.** Use the first experiment to develop g, discard its data, and run a follow-up in which g is applied, as in a pilot (p. 426). This is a stronger test of generalizability than sample splits. g must generalize, and the causal effect must generalize to a slightly different time and population. A random split on average reflects the same ATE, but across experiments the ATE may change. It costs more resources and time (pp. 426–427). The wider version is replication across contexts and researchers (p. 427).

### 24.6 Conclusion (p. 428)
- The chapter reviewed causal basics, contrasted prediction, measurement and causal inference, and described FPCILV and overfitting. It presented three workflows: an existing g, splitting, and sequential experiments (p. 428).
- The authors say the workflows are harder in practice than in theory. Chapters 25–26 give examples, and Chapter 27 treats text as a confounder (p. 428).

## Toy example (ours, not from the text)
Eight texts, four treated and four control. Randomly put four in training (A, B treated; C, D control) and four in test (E, F treated; G, H control). Candidate measure: "text contains the word *sunny*" ($\pi=1$ if yes).

- Training: A and B contain "sunny"; C and D do not. Mean for treated $=(1+1)/2=1$, mean for control $=(0+0)/2=0$. The difference is $1-0=1$, which looks like a large effect.
- Suppose a researcher adopts "sunny" as g because of this. That is the overfitting risk of 24.4.2.
- Test, g fixed and untouched until now: E contains "sunny", F does not; G does, H does not. Treated mean $=(1+0)/2=0.5$. Control mean $=(1+0)/2=0.5$. $\widehat{\mathrm{ATE}}=0.5-0.5=0$.
- The training result was chance. Because the test set was not used to choose g, the test estimate is not contaminated by that selection.

## Concepts
- [[potential-outcomes]] — each unit has an outcome under each treatment; only one is observed (p. 410) (new)
- [[fundamental-problem-of-causal-inference]] — the counterfactual is never observed, so individual effects are not observable (p. 410) (new)
- [[average-causal-effect]] — $\bar y^T-\bar y^C$, the mean of $y_i(1)-y_i(0)$ (p. 410) (new)
- [[sutva]] — a unit's outcome depends only on its own treatment status; no interference, consistent treatment (p. 411) (new)
- [[ignorability]] — potential outcomes independent of treatment assignment; delivered by randomization (p. 412) (new)
- [[positivity]] — every unit has some probability of each treatment value (p. 421) (new)
- [[mapping-function-g]] — the function that compresses text into a low-dimensional measure (Egami et al.) (p. 420) (new)
- [[fpcilv]] — if g is built on the analysis data, units' potential outcomes depend on other units' treatments, violating SUTVA (pp. 417, 423) (new)
- [[overfitting-in-discovery]] — a discovered g captures chance relations with treatment; worse in high-dimensional text and in causal work (pp. 416, 423) (new)
- [[train-test-split-causal]] — discover and validate g on training data. Use the test set once for the ATE and revalidation (p. 425) (new)
- [[sequential-experiments]] — develop g in one experiment, discard its data, apply g in a follow-up (p. 426) (new)
- [[pre-analysis-plan]] — pre-registered plan fixing variables, measures and tests before data collection (p. 417) (new)
- [[text-as-data-validation]] — here, validation of g is needed in training and again in the test set (pp. 425–426)

## Canonical instances
- [[news-story-spillover-example]] — treated group re-shares story to control group; SUTVA violated (p. 412)
- [[opt-in-news-example]] — self-selection of politically interested people breaks ignorability (p. 412)
- [[sunny-word-example]] — a word related to treatment by chance leads to a non-generalizing measure (p. 423)
- [[boydstun-policy-agendas-codebook]] — an existing codebook had to be updated and annotated for new documents (p. 424)
- [[polity-index-example]] — a mapping function that compresses institutions into one number (p. 420)

## Bridges (candidates)
- [structural-analogy] FPCILV (measure learned from all units) ↔ statistics/ML: train-test leakage — both let information from evaluation units shape the model used on them.
- [structural-analogy] Using the test set once for the ATE ↔ research design: pre-registration — both limit researcher degrees of freedom.
- [metaphor] Sequential experiments ↔ science studies: replication as community practice — the authors describe the same logic at the level of a research community (p. 427).

## Questions this raises
- How much data should go to training versus test, given the power needed for discovery versus the power needed for the effect (p. 426)?
- Does a test set that revalidates poorly invalidate the ATE, or only the interpretation of g? The authors say g cannot be changed, but not what the estimate then means (p. 426).
- When text is a confounder in observational studies, how does the same discovery-versus-estimation separation work (Ch. 27, p. 428)?
- How should the effect estimate and its uncertainty be handled when g is discovered across several sequential experiments?

## Reading notes
- Printed page = pdf page (407–428).
- The decomposition (p. 411) is flattened in both the text layer and the page image (no visible sub/superscripts). The regression equations (p. 412) are readable but also flattened. Superscripts and subscripts above were reconstructed from context and algebra, not read directly from the images. The decomposition's algebra was checked (added step: the second line follows by distributing $p_T$ and $(1-p_T)$).
- Page 422: the text layer says $g$ "maps $t$ to R" for text as treatment, while the displayed formula reads $g:\mathcal T\to\mathcal P_t$. "R" is probably a typo for $\mathcal P$.
- The chapter introduction (p. 408) promises "five guiding principles" but §24.3 has three headed principles. §24.3.3 refers to "these last two principles".
- Spelling errors in the source ("casual" for causal, "tenants", "peformed") were not carried over.
- No exercises appear in this unit.
