---
id: grimmer-2013-textasdata/main
work: grimmer-2013-textasdata
unit: paper
pages: 1-31
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts

## L0 — One line
Automated text methods can make large-scale analysis of political texts affordable, but every method is a wrong model of language, so each use needs its own validation against human judgment or substantive checks.

## L1 — The gist (≤ 120 words)
Politics happens in words, but reading large text collections by hand is too costly. Grimmer and Stewart survey methods that turn texts into word counts. Methods covered: dictionaries and supervised classifiers (known categories), clustering and topic models (discovering categories), and scaling methods (placing actors in policy space). They state four principles: all models are wrong, methods augment humans, no method is globally best, and validate. Worked examples show how to validate each method family: replicate human coding for supervised methods, and check meaning and consequences for unsupervised ones. Scaling methods work when ideology dominates the language, and otherwise recover another dimension.

**Prerequisites:** Bayes' rule; conditional independence; matrices and vectors; Poisson and Dirichlet distributions (basic idea); the idea of out-of-sample prediction.

## L2 — Key ideas (5–10 bullets)
- Four principles guide the field: all quantitative models of language are wrong but some are useful; methods augment humans; no globally best method exists; validate (Table 1, p. 3).
- Most methods start from a "bag of words" (each document is only its word counts) stored in a document-term matrix (documents in rows, words in columns), which discards word order, punctuation and rare/common words. The authors report that, consistently across applications, scholars have shown this simple representation suffices to infer substantively interesting properties of texts (pp. 6–7).
- Dictionary methods score a document by the rate of scored words. They are cheap but can fail when used outside the domain they were built for, and they are rarely validated (pp. 8–9).
- Supervised methods learn from hand-coded documents. They are easier to validate: cross-validation (testing on parts of the coded set held out of training) yields accuracy (share of correct codes), precision and recall (pp. 9–14).
- Unsupervised methods (K-means, which groups documents around average centres; topic models, which treat each document as a mixture of word-distribution "topics"; computer-assisted clustering, which lets a user explore many candidate clusterings) discover categories. They shift the burden to post-fit validation: semantic validity (do humans find the clusters coherent), predictive validity (does topic use track expected events) and convergent validity (does it match a supervised measure) (pp. 14–25).
- Statistical fit is not the right criterion for choosing the number of clusters; substantive fit is (pp. 19–20).
- Supervised and unsupervised methods are complements, not competitors, since they have different objectives (p. 15).
- Text scaling (placing actors on a policy dimension; wordscores uses scored reference texts, wordfish uses a Poisson model) assumes ideology dominates the language. It works on German party platforms and fails to separate Democrats from Republicans in Senate press releases (pp. 25–28).

## L3 — Walkthrough

### Abstract and 1 Introduction (pp. 1–3)
- Politics is expressed in words (campaigns, legislation, regulation comments, treaties, manifestos, terrorist materials) (p. 1). The main obstacle is volume: scholars are rarely able to read all the texts even in moderately sized corpora, and hiring coders is still very expensive (p. 1).
- A *corpus* is the set of texts analysed. Automated methods can make analysis possible without massive funding. They will "never replace" close reading but amplify it, and they are *incorrect* models of language, so performance on a new data set cannot be guaranteed and validation is essential (p. 2).
- Roadmap (Fig. 1, p. 2). The workflow is: acquire documents → preprocess → research objective.
  - *Classification* sorts texts into categories. With known categories, use dictionaries (5.1) or supervised methods (5.2). With unknown categories, use Fully Automated Clustering (FAC; single-membership or mixed-membership models) or Computer-Assisted Clustering (CAC) (pp. 2–3).
  - *Scaling* places actors in policy space, supervised (wordscores) or unsupervised (wordfish) (pp. 2–3).
- Scope: document-level methods. Natural language processing for sentences and events is excluded, except events-data work (p. 3). Space given to a method is not necessarily in proportion to its use. Supervised methods are simpler and need less validation space (p. 3).

### 2 Four Principles (pp. 3–5)
- **P1: all quantitative models of language are wrong—but some are useful** (p. 3).
  - Language is complex. The text's joke: "Time flies like an arrow. Fruit flies like a banana." (p. 4).
  - Text models differ from causal-inference models, where one includes all relevant features. Adding realism need not improve a text method, and less sophisticated models may be more useful (p. 4).
  - Models should be judged by whether they do a useful social-science task (assign documents to categories, discover categorisations, measure relevant quantities). Fit or prediction of new text can select substantively inferior models (Chang et al. 2009) (p. 4).
- **P2: methods augment humans, not replace them.** Researchers still guide, model and interpret, which requires reading (p. 4).
- **P3: no globally best method.** Different questions imply different quantities of interest and validations (p. 4). Much of the across-approach debate is misguided on this view. Performance also varies within a model family across data sets (pp. 4–5).
- **P4: validate, validate, validate** (p. 5).
  - For known categories, show that supervised methods replicate human coding.
  - For unsupervised methods, combine experimental, substantive and statistical evidence to show the measures are as conceptually valid as supervised ones.
  - Scalings need many substance-based evaluations.
  - The authors discourage the use of many commercial tools. Output is hard to validate and, once a problem is found, hard to change (p. 5).

*Intuition note:* A model can be false about how language works and still be a good measuring tool. The test is whether it helps with the task, and that is checked against human coding or substantive evidence.

### 3 Acquiring Text (pp. 5–6)
- Sources: media archives, floor speeches, press releases, bills, hearings, treaties (p. 5). Methods need plain text (e.g. UTF-8).
- Easiest: online databases (Lexis Nexis, ProQuest, JSTOR, XML feeds). Harder: web scraping, or Mechanical Turk if scraping is restricted. Hardest: archives, handled by scanner plus OCR (pp. 5–6).
- Methods work better on focused text (one idea for classification, policy positions for scaling). Discarding unrelated text can improve clustering. Longer texts are easier than short ones such as open-ended survey answers. Short texts need accompanying information or very large volume (p. 6).

### 4 Reducing Complexity: From Words to Numbers (pp. 6–7)
The "recipe" is meant to be varied and validated (p. 6).
1. **Bag of words:** discard word order. *Unigrams* are single words. *Bigrams*/*trigrams* keep some order (e.g. "White House"). The authors report that n-grams do little to improve common tasks (p. 6).
2. **Stemming:** cut word ends (family, families, familial → famili). It approximates *lemmatization*, which uses context and dictionaries (good ← better, best). Stemming is cruder but faster. The Porter algorithm is common (pp. 6–7).
3. **Discard** punctuation, capitalisation, stop words and very rare words. Typically drop words in under 1% or over 99% of documents, depending on vocabulary, document length and corpus size (p. 7).
4. **Result:** each document $i = 1,\dots,N$ is a count vector $W_i = (W_{i1}, \dots, W_{iM})$ over $M$ unique words. Stacked, these form the *document-term matrix* ($N \times M$). It typically has 3,000–5,000 columns and is mostly zeros (*sparse*) (p. 7).

*Intuition note:* This looks like a huge loss of information. The authors report that across applications it keeps enough to infer interesting properties (p. 7).

**4.1 Alternatives** (p. 7). Mosteller and Wallace (1963) used only function-word counts for authorship, information normally discarded. Other variants are word-occurrence indicators, keeping some stopwords, feature subsets, and tf-idf weighting (rarity weighting). Spirling (2012) studied treaties with Native Americans using sub-string kernels, which compute distances between documents and preserve word order, because order mattered for land negotiations (p. 7).

### 5 Classifying Documents into Known Categories (pp. 7–14)
Goal: infer each document's category, the distribution over categories, or both (pp. 7–8). Two families: dictionaries and supervised learning (p. 8).

**5.1 Dictionary methods** (pp. 8–9)
- Each word $m$ has a score $s_m$. For tone: $s_m = -1$ (negative) or $s_m = +1$ (positive). With $N_i = \sum_{m=1}^{M} W_{im}$ words in document $i$,
$$t_i = \sum_{m=1}^{M} \frac{s_m W_{im}}{N_i}.$$
  $t_i$ is an approximately continuous tone measure. A simple rule codes $t_i>0$ positive and $t_i<0$ negative (p. 8).
- Dictionaries are cheap, with many off-the-shelf lists. They work well only when word scores match usage in the context (p. 8).
- Loughran and McDonald (2011): words such as *tax, cost, crude, cancer* are negative in general dictionaries but may be positive in earnings reports (a health-care firm mentions cancer often). Words like *unanticipated* are missed (pp. 8–9).
- Authors' view: use dictionaries with substantial caution and explicit validation. Measures are rarely validated. Humans cannot reliably produce such granular measures (Krosnick 1999), so gold-standard human evaluation of dictionaries is, in the authors' words, essentially impossible. Hence most dictionary analyses rest on "shaky foundations" (p. 9).
- Two suggested improvements: (1) simplify to binary categories so human gold standards apply; (2) validate dictionary measures like unsupervised ones (Section 6.4) (p. 9).

**5.2 Supervised learning** (p. 9). Humans hand-code a training set. The algorithm learns the word–category relation. Advantages over dictionaries: it is domain-specific by construction and forces clear concept definitions; it is easier to validate with clear performance statistics (p. 9). Three steps: construct a training set; apply the method; validate and classify the rest (p. 9).

**5.2.1 Training set** (p. 10). A poor training set cannot be repaired by any model.
- *Coding scheme:* develop iteratively. Write a concise codebook, apply it to documents, find ambiguities, revise, and re-test. It is final only when coders notice no ambiguities (p. 10).
- *Sampling:* almost all classifiers implicitly assume the training set is a random sample of the corpus (Hand 2006). Use simple random or stratified sampling. This is hard when data are not yet available (p. 10).
- *Size:* Hopkins and King (2010) give 500 as a rule of thumb and 100 as probably enough. A strict rule can be dangerous, and more categories need more documents. Validation can show the return on coding more (p. 10 and fn. 1).

**5.2.2 Applying a model** (pp. 10–12)
- Setup: $N_{train}$ documents, each coded into one of $K$ categories, $Y_i \in \{C_1,\dots,C_K\}$. $W_{train}$ is the $N_{train} \times M$ matrix of features. An unobserved function links them; the algorithm estimates it and applies it to the test set (pp. 10–11):
$$Y_{train} = f(W_{train}), \qquad \hat{Y}_{test} = \hat f(W_{test}).$$
- **Naïve Bayes** (Individual methods). By Bayes' rule, dropping the constant $p(W_i)$:
$$p(C_k \mid W_i) \propto p(C_k)\, p(W_i \mid C_k) \tag{1}$$
  - The maximum likelihood estimate is $\hat p(C_k) = \dfrac{\text{Number Train Docs in Category } k}{N_{train}}$ if the training set is representative (p. 11).
  - Estimating $p(W_i|C_k)$ directly fails. For even moderately sized texts, any one count vector will appear in a corpus only once, so $\hat p = 0$ for all test documents and the model is useless without more assumptions (p. 11).
  - The "naïve" assumption: given category, words are independent, $p(W_i \mid C_k) = \prod_{m} p(W_{im} \mid C_k)$ (p. 11).
  - The authors say it must be wrong, since word use is highly correlated, but the model is still useful. They estimate $\hat p(W_{im}=j \mid C_k)$ as (train docs in $k$ with word $m$ used $j$ times) / (train docs in $k$) (p. 11).
  - Zero counts are handled by adding a small amount, justified via a Dirichlet–Multinomial model (p. 11). The classifier assigns each test document to the category with the highest probability (the text says "document"; context requires category):
$$\hat f(W_i) = \arg\max_k \Big[\hat p(C_k) \prod_{m=1}^{M} \hat p(W_{im} \mid C_k)\Big]$$
  - This illustrates Principle 1. Other individual methods: Random Forests, Support Vector Machines, neural networks (p. 12).
- **Ensembles** (p. 12). Heuristically, if classifiers are accurate and diverse, combining them improves accuracy. Other benefits are out-of-sample stability and complex functional forms from simple classifiers. Schemes: Super-learning weights methods by cross-validated out-of-sample accuracy; bagging draws samples with replacement; boosting trains sequentially, upweighting misclassified cases (p. 12).
- **Measuring proportions** (ReadMe, Hopkins and King 2010) (p. 12). For many applications only the proportion of documents in each category is needed; shifting focus to estimating proportions $P(C)$ can lead to substantial improvements in accuracy, even if documents are not randomly sampled. Words are coded as occurrence indicators. The test-set data-generating process is
$$p(W_{test}) = p(W_{test}\mid C_{test})\, p(C_{test}) \tag{2}$$
  - $p(C_{test})$ is the quantity of interest. It is easy to solve for if the other two are known, but both are high-dimensional (p. 12).
  - Instead of independence, Hopkins and King use *matrix smoothing* to preserve higher-order word correlations. $\hat p(W_{test})$ is estimated from the test set with no coding. They assume the conditional distributions are the same in training and test sets, substituting $\hat p(W_{train}\mid C_{train})$. Heuristically (p. 12):
$$\hat f(W_{test}) = \big[\hat p(W_{train}|C_{train})'\, \hat p(W_{train}|C_{train})\big]^{-1} \hat p(W_{train}|C_{train})'\, \hat p(W_{test}).$$
  - (added step) This has the form of a least-squares solution $(X'X)^{-1}X'y$, solving $\hat p(W_{test}) \approx \hat p(W_{train}|C_{train})\, p(C_{test})$.
  - ReadMe is not an option for all users, particularly those with few documents or who need to stratify results by an external covariate. With a large number of documents (in excess of 100 at least) for each covariate value, it can be rerun on each stratum. Otherwise return to individual classification (p. 12).

*Intuition note:* Naïve Bayes pretends words are independent given the category, which is false but still useful for classification. ReadMe estimates shares of categories rather than labelling each document, which avoids some bias.

**5.2.3 Validation** (p. 13)
- If a method performs well it replicates hand coding. The ideal is a three-way split: training, validation (to assess the final model), and test sets (p. 13).
- *V-fold cross-validation* replicates this: split the training set randomly into $V$ groups. For each group $v$, train on the other $V-1$ and predict group $v$, so all predictions are out of sample (p. 13). It avoids overfitting and selects the best model among candidates (the "Oracle property"). Footnote 2: this holds only if all steps, including predictor selection, are done within the cross-validation training folds (p. 13).

**5.2.4 Example: Russian military discourse** (pp. 13–14; adapted from Stewart and Zhukov 2009)
- Corpus: 7,920 Russian public statements by political and military elites, 1998–2008. Coders classify the stance on use of force as restrained, activist or neutral. 300 randomly sampled documents were coded. The number is small because Russian-speaking coders are costly (p. 13).
- A Random Forest was trained and assessed by ten-fold cross-validation. Confusion matrix (Table 2; rows = machine, columns = human) (p. 13):

| Machine \ Human | Restrained | Activist | Neutral |
|---|---|---|---|
| Restrained | 111 | 31 | 28 |
| Activist | 10 | 17 | 0 |
| Neutral | 26 | 9 | 68 |

- Three statistics (p. 14):
  - Accuracy = (documents on diagonal)/(total) $=0.65$ (196/300, added arithmetic). The authors call it not extremely accurate, but comparable to other studies of complex categories.
  - *Precision* for category $k$: of those the machine labels $k$, the share correct. Restrained: 0.65 (111/170, added).
  - *Recall* for $k$: of those humans label $k$, the share the machine finds. Restrained: 0.75 (111/147 ≈ 0.755, added).
  - Recall exceeds precision because the forest guesses "restrained" too often (p. 14).
- Options if unsatisfied: other methods, ensembles, or switching to proportions. After validation they apply the classifier to all statements (Table 3, p. 14). Military test-set shares: restrained 0.41, activist 0.24, neutral 0.35. Political: 0.62, 0.04, 0.34. Stewart and Zhukov use similar results to show that military elites are *more* activist than political elites, contrary to conventional wisdom (Gelpi and Feaver 2002) (p. 14).

### 6 Discovering Categories and Topics (pp. 14–25)
- Dictionaries and supervised methods assume predefined categories, which are sometimes hard to know (e.g. topics of 1887 Senate speeches) (p. 14).
- The number of partitions of even 100 documents is much larger than the estimated number of atoms in the universe, so enumeration is impossible (p. 15).
- *Unsupervised learning* estimates categories and assigns documents simultaneously. Two types: FAC (one clustering, necessarily model dependent) and CAC (pp. 15, 19).
- The authors say output should be viewed with skepticism and validated. Validation is done conditional on the clustering, so one cannot validate before seeing it (p. 15).
- **Voice on the debate:** Hillard, Purpura and Wilkerson (2008) suggested unsupervised methods become a special case of supervised ones, and Quinn et al. (2010) is cited with them as casting the two as competitors. **Authors' reply:** the debate is misplaced because the objectives differ. Use supervised methods for predetermined categories. Supervised methods "will never contribute a new coding scheme". They are complements, especially for new projects, and supervised methods can validate or generalise unsupervised findings (p. 15).

**6.1.1 Single-membership models** (pp. 16–17)
- A *clustering* is a partition into mutually exclusive, exhaustive groups. $C_i$ is the cluster of document $i$ and $C = (C_1,\dots,C_N)$. Every FAC algorithm has three components: a distance/similarity definition, an objective function, and an optimisation algorithm (p. 16).
- **K-means** (MacQueen 1967) minimises within-cluster squared Euclidean distance, giving a partition into $K$ clusters and $K$ centres $\mu_k$ (p. 16).
  - Distance:
$$d(W_i, \mu_k) = \sum_{m=1}^{M} (W_{im} - \mu_{km})^2.$$
  - Other metrics (e.g. tf-idf weights) give different clusterings (p. 16).
  - Objective, with $I(\cdot)$ an indicator equal to 1 if its argument is true:
$$f(\mu, C, W) = \sum_{i=1}^{N}\sum_{k=1}^{K} I(C_i=k)\, d(W_i,\mu_k) = \sum_{i=1}^{N}\sum_{k=1}^{K} I(C_i=k)\Big(\sum_{m=1}^{M} (W_{im}-\mu_{km})^2\Big) \tag{3}$$
  - Optimisation: the exact optimum is hard because the objective is multimodal and non-continuous, so K-means iterates. From centres $\mu^{t-1}$, step 1 assigns each document to its closest centre; step 2 resets each centre to the mean of its assigned documents (p. 17):
$$C_i^t = \arg\min_k \sum_{m=1}^{M} (W_{im} - \mu^{t-1}_{km})^2, \qquad \mu_k^t = \frac{\sum_{i=1}^{N} I(C_i^t=k)\,W_i}{\sum_{i=1}^{N} I(C_i^t=k)}.$$
  - Repeat until the change in the objective falls below a threshold. This is closely related to EM and guarantees only a local minimum, so several random restarts are often needed (p. 17).
- Alternative methods vary the three components. The clustering literature gives little guidance on which will be useful, and the authors suggest such guidance may be impossible without knowing the data (Grimmer and King 2011). So methods imported from other fields should be imported with caution and validated substantively (p. 17).

**6.1.2 Mixed-membership (topic) models** (pp. 17–19)
- Topic models are Bayesian generative models with problem-specific structure (Blei, Ng and Jordan 2003). A *topic* is a probability mass function over words, $\theta_k$ ($M \times 1$), with $\theta_{mk}$ the probability topic $k$ uses word $m$. Substantively, topics are distinct concepts (e.g. troop, war, taliban versus health, care, reform) (p. 17).
- Shared hierarchy: a *prior* borrows information across units; a *mixed-membership* level shows how a unit splits attention over topics; at the bottom each word or document gets a single topic (pp. 17–18).
- **LDA** (p. 18). Each document's topic proportions $\pi_i = (\pi_{i1},\dots,\pi_{iK})$ come from a common Dirichlet prior with shape parameters $\alpha$:
$$\pi_i \sim \text{Dirichlet}(\alpha).$$
  For word $j = 1,\dots,N_i$ in document $i$, first draw its topic, then the word from that topic:
$$\tau_{ij} \sim \text{Multinomial}(1, \pi_i), \qquad W_{ij} \sim \text{Multinomial}(1, \theta_k) \text{ if } \tau_{ij}=k.$$
- Political-science variants share this structure (Fig. 2, p. 18). In the *dynamic multitopic model* (Quinn et al. 2010) days are mixed members, speeches get single topics, and the prior is dynamic. In the *expressed agenda model* (Grimmer 2010) senators are mixed members and press releases get single topics (pp. 18–19).
- Placing models in a data-generating process makes adding structure straightforward (e.g. combining the two models). But few models are likely to be used, because tuning each model is daunting. Each is still limited to one family of distributions (p. 19).

**6.2 CAC** (p. 19). Judging a clustering after the fact is easier than choosing assumptions beforehand. Apply many diverse FAC methods, embed the partitions in a 2-D space where nearby points organise documents similarly, and explore the space, including millions of combinations (Grimmer and King 2011). Uses: find new concepts, explore new collections, and assess how original a new clustering method is. It places a burden on the user, and the result is only as good as the person exploring (p. 19).

**6.3 Setting the number of clusters** (pp. 19–20)
- All of K-means, topic models and CAC need this. Methods that estimate the number are strongly model dependent (Wallach et al. 2010). Fit statistics are unreliable because the best-fitting model often carries less substantive information (Chang et al. 2009) (pp. 19–20).
- The authors warn you "can't get something for nothing": nonparametric priors reparameterise the choice as a hyperprior or tuning parameter (p. 20).
- Fit to preprocessed text is the wrong target, since preprocessed text is a simplification. Selection should be recast as *substantive* fit. Quinn et al. (2010): fit candidate models with varying $K$, then use human judgment of whether clusters are distinct and internally consistent. Chang et al. (2009) and Grimmer and King (2011) offer elicited expert measures (p. 20).

**6.4 Validating unsupervised methods: senators' press releases** (pp. 20–25)
- Unsupervised methods shift user burden from choosing categories beforehand to validating output afterward (Quinn et al. 2010). The example is Grimmer (2012): a version of the expressed agenda model on over 64,000 Senate press releases, 2005–2007, with 44 topics (pp. 20–21).
- Finding: the main variation in expressed priorities is how senators balance position taking and credit claiming. The authors say this spectrum is theoretically interesting, matches earlier qualitative and formal work, and has consequences for representation (p. 20). They caution that the validations shown are only a subset of those needed (p. 20).

**6.4.1 Validating topics** (pp. 20–22)
- *Labeling:* read 10–15 documents from a topic, and/or list words highly predictive of the topic (Table 4, p. 21). Examples:
  - Iraq War: Iraq, iraqi, troop, war, sectarian.
  - Honorary: honor, prayer, remember, fund, tribute.
  - Fire Department Grants: firefight, homeland, afgp, award, equipment.
- The authors say these show the utility of unsupervised learning. The fire-grant topic is a type of credit claiming often missed from standard models (p. 21).
- *Semantic validity* (Quinn et al. 2010): topics group press releases that are internally homogeneous and distinct from other topics (p. 21).
  - Method (Grimmer and King 2011): sample pairs of documents from the same and different clusters. Research assistants rate pairs 1 (unrelated), 2 (loosely related) or 3 (closely related). *Cluster Quality* $=$ mean rating of same-cluster pairs $-$ mean rating of different-cluster pairs. Compare $\text{Cluster Quality}_{ExpressedAgenda} - \text{Cluster Quality}_{Alt.Method}$. It gives relative, not absolute, validity (p. 21).
  - Comparators: two Senate press secretaries' clusterings and a nonparametric (Dirichlet process) method. Fig. 3 shows the expressed agenda model has higher quality than all three (p. 22).
- *Predictive validity:* if topics are valid, external events should explain spikes in attention (Quinn et al. 2010). Fig. 4 shows spikes in Iraq releases around events such as the Iraq study group report, and in honorary releases when major figures die, e.g. Pope John Paul II (pp. 21–22).

**6.4.2 Validating expressed priorities** (pp. 23–25)
- *Predictive validity:* committee chairs and ranking members should give more attention to topics under their committee's jurisdiction than the other 98 senators (Grimmer 2010). Fig. 5 compares 40 committee–topic pairs for each year. For almost every pair in each year, leaders give substantially more attention. So the measures are "at least by this test, predictively valid" (pp. 23–24).
- *Convergent validity* with a supervised method (p. 24).
  - Grimmer (2012) sums several topics into the number of credit-claiming (money) releases per senator. The authors built a codebook, had a research assistant code 500 press releases, and applied ReadMe. ReadMe estimates proportions, so counts come from multiplying by total releases (fn. 5).
  - Fig. 6: correlation 0.96 between supervised and unsupervised counts. The unsupervised estimate is "essentially equivalent" to ReadMe, so confidence in the supervised estimate carries over (p. 25).
  - Caveat: this validation does not remove the need for unsupervised methods, since it is possible only after they suggest the scheme. Later work may use supervised classification to extend and generalise (p. 25).

*Intuition note:* Unsupervised output cannot be checked before it exists. So the checks happen afterwards: do humans find the clusters coherent, do topics spike when events occur, and does a supervised coder reach the same counts?

### 7 Measuring Latent Features: Scaling Political Actors (pp. 25–28)
- Roll-call scaling is limited outside the U.S. Congress (less reliable, Spirling and McLean 2007), and other actors do not vote. But nearly all political actors speak (p. 25).
- **Authors' critique of the literature:** several papers implicitly equate the goal with replicating expert opinion or existing nontext scalings. But then text methods are unnecessary, since extrapolation would suffice. A clearer goal is *prediction* of events, e.g. Beauchamp (2011) uses text scalings to predict votes. Text scalings should also predict coalitions, endorsements and donations (p. 25).
- Both supervised and unsupervised scaling methods rely on a strong *ideological dominance* assumption: actors' ideological leanings determine what is discussed. It works for Senate floor speeches (Beauchamp 2011) and German party platforms (Slapin and Proksch 2008). It appears not to hold in Senate press releases, where senators engage in nonideological credit claiming (p. 25). Methods separating ideological from non-ideological statements are an important research area (p. 26).

**7.1 Supervised: wordscores** (Laver, Benoit and Garry 2003) (p. 26)
- A special case of dictionary methods. Choose reference texts that define positions (e.g. speeches of a very liberal and a very conservative senator). A word's score measures its relative rate of use in the reference texts. Test ("virgin") texts are placed at the weighted average of their words' scores, with weights equal to the rate at which words are used (p. 26).
- Limits (see Lowe 2008): defining positions only through reference texts conflates ideological language with authors' style and imposes ideological dominance. Results depend strongly on the reference texts. Removing stylistic words helps; Beauchamp (2011) finds removing technical language improves results. But "no amount of preprocessing" completely eliminates it. Explicitly adopting a supervised approach might limit the influence of style, but needs a substantial increase in effort and time (p. 26).

**7.2 Unsupervised: wordfish** (pp. 26–27)
- Monroe and Maeda (2004) and Slapin and Proksch (2008) use item response theory (IRT) models. Politicians live in a low-dimensional space with position $\theta_i$, which affects word rates. Wordfish assumes $W_{ij} \sim \text{Poisson}(\lambda_{ij})$ with
$$\lambda_{ij} = \exp(\alpha_i + \psi_j + \beta_j \times \theta_i).$$
- $\alpha_i$ is loquaciousness of actor $i$; $\psi_j$ is the frequency of word $j$; $\beta_j$ is how strongly word $j$ discriminates the underlying space; $\theta_i$ is position (p. 27).

**7.3 Applying wordfish** (pp. 27–28; Fig. 7)
- Without supervision, the model seizes the *primary variation* in language, which may be ideology or policy-vs-pork focus, style or tone. The authors stress this is not a shortcoming of wordfish, but its output should not be assumed ideological without validation (p. 27).
- *German platforms* (replicating Slapin and Proksch 2008): estimates separate the parties and replicate expert assessments of movement over time (p. 27).
- *Senate press releases:* wordfish fails to separate Democrats from Republicans, though valid scaling in the polarised Senate would. But it recovers the position-taking vs credit-claiming spectrum of Grimmer (2012), with correlation 0.86 (pp. 27–28).
- Conclusion: when actors speak heavily ideologically, unsupervised methods appear to retrieve reliable positions. When they can avoid ideological speech, scalings find another dimension. Validation must confirm the intended space (p. 28).

*Intuition note:* Wordfish finds whatever differences in word use are largest. If senators mainly differ in how much they brag about pork, that becomes the dimension.

### 8 Text as Data in Political Science (pp. 28–29)
- Performance is context specific; output needs validation (supervised: replicate hand coding; unsupervised: measures correspond to the claimed concepts) (p. 28). Natural language processing and other methods are left to textbooks (p. 28).
- Three future directions: new texts need new methods, with attention to shared structure; *uncertainty* measurement (SIMEX is used for coder error in Hopkins and King 2010 and for scale error in Benoit, Laver and Mikhaylov 2009; posterior distributions or fast computation are needed for others); and new texts and questions in law, political theory and survey research (p. 28–29).
- Promise: inferences previously impossible. Pitfall: applying methods without careful thought "will likely lead to few answers and a great deal of frustration" (p. 29).

## Toy example (ours, not from the text)
**Part A: dictionary tone.** A document has $N_i = 10$ words. Dictionary: 2 words with $s_m=+1$ and 3 words with $s_m=-1$, each used once, and the rest unscored. Then $t_i = \frac{(+1)(1)\cdot 2 + (-1)(1)\cdot 3}{10} = \frac{2-3}{10} = -0.1 < 0$, so "negative" under the simple rule (p. 8).

**Part B: validating a classifier.** 10 hand-coded documents, categories Pos/Neg. Machine output vs human:

| Machine \ Human | Pos | Neg |
|---|---|---|
| Pos | 4 | 2 |
| Neg | 1 | 3 |

- Accuracy $=(4+3)/10 = 0.70$.
- Precision (Pos) $=4/(4+2) = 0.667$. Recall (Pos) $=4/(4+1) = 0.80$.
- Recall exceeds precision because the machine says "Pos" too often (6 times, though humans coded 5 as Pos). The same pattern appears in the Russian example (p. 14).

## Concepts
- [[text-as-data-validation]] — treating text as quantitative data, with outputs checked against human judgment or substantive evidence (pp. 2, 5)
- [[bag-of-words]] (new) — document represented by word counts, order discarded; unigrams, optionally n-grams (p. 6)
- [[document-term-matrix]] (new) — $N\times M$ matrix of counts $W_{im}$; typically sparse (p. 7)
- [[stemming-lemmatization]] (new) — reducing words to roots (stemming, crude and fast) or base forms (lemmatization, using context) (p. 6)
- [[dictionary-method]] (new) — document score is the rate-weighted average of word scores $s_m$ (p. 8)
- [[supervised-learning-text]] (new) — learn word–category relationship from a hand-coded training set; classify the rest (p. 9)
- [[naive-bayes-classifier]] (new) — Bayes' rule with words independent given category (p. 11)
- [[ensemble-methods]] (new) — combining accurate, diverse classifiers; super-learning, bagging, boosting (p. 12)
- [[readme-proportion-estimation]] (new) — estimates category proportions rather than individual labels (Hopkins and King) (p. 12)
- [[cross-validation]] (new) — V-fold out-of-sample assessment of a model (p. 13)
- [[confusion-matrix-accuracy-precision-recall]] (new) — table of machine vs human codes and three summary statistics (p. 14)
- [[unsupervised-learning-text]] (new) — methods that estimate categories and assignments without predefined labels (p. 15)
- [[k-means]] (new) — clustering that minimises within-cluster squared Euclidean distance; local optima (p. 16)
- [[topic-model-lda]] (new) — documents are mixtures of topics, topics are word distributions; mixed-membership structure (p. 18)
- [[computer-assisted-clustering]] (new) — exploring a space of many clusterings built from diverse methods (p. 19)
- [[semantic-predictive-convergent-validity]] (new) — coherence judged by humans; link to external events; agreement with supervised measure (pp. 21–25)
- [[ideological-dominance-assumption]] (new) — assumption that ideology drives word use in the text (p. 25)
- [[wordscores]] (new) — supervised scaling via reference-text word scores (p. 26)
- [[wordfish]] (new) — Poisson-IRT scaling, $\lambda_{ij}=\exp(\alpha_i+\psi_j+\beta_j\theta_i)$ (p. 27)

## Canonical instances
- [[loughran-mcdonald-dictionary-failure]] — off-the-shelf negative words ("cancer", "crude") can be positive in earnings reports (pp. 8–9)
- [[russian-military-discourse-classification]] — Random Forest, 300 coded statements, accuracy 0.65; Stewart and Zhukov use similar results to argue military elites are more activist than political ones (pp. 13–14)
- [[senate-press-release-expressed-agenda]] — 44-topic model of 64,000+ releases; position taking vs credit claiming (p. 20)
- [[credit-claiming-convergent-validity]] — unsupervised vs ReadMe counts correlate 0.96 (pp. 24–25)
- [[wordfish-german-platforms-vs-senate]] — works on party platforms, fails to separate Democrats and Republicans in press releases (pp. 27–28)
- [[federalist-papers-authorship]] — function-word counts used for authorship (p. 7)

## Bridges (candidates)
- [same-math] Naïve Bayes classification ↔ statistics/ML: Bayes' rule with conditional independence of features given the class — the equation is the standard one.
- [structural-analogy] Wordfish's $\alpha_i+\psi_j+\beta_j\theta_i$ ↔ roll-call IRT scaling: discrimination parameter times latent position — same logic applied to words instead of votes.
- [structural-analogy] Convergent validity via a supervised check ↔ measurement validity in survey methodology: show a new measure agrees with an established one.
- [metaphor] "No globally best method" ↔ general view that methods suit research questions: tools chosen by quantity of interest.
- [structural-analogy] Ideological dominance assumption ↔ spatial model of voting: observed behaviour is read as a function of position in policy space.

## Questions this raises
- How should one decide whether a dimension found by an unsupervised scaling is "ideology" rather than style or topic focus?
- Is 0.65 accuracy acceptable for a downstream inference, and how does classification error propagate into regression estimates?
- If statistical fit is a poor guide to the number of topics, how reliable and reproducible is human-judged substantive fit?
- When is dropping word order harmless, and when (as for Spirling's treaties) does it destroy the signal?

## Reading notes
- Printed page = pdf page (offset 0). The header says "Political Analysis (2013) pp. 1–31", the Advance Access pagination. The metadata cites the journal pages 267–297.
- Supplementary Material is referred to (pp. 1, 3, 14) but is not in the pages supplied.
- Text-layer issues: minus signs and some symbols are lost in the layer (e.g. the dictionary scores $s_m$ read "=1" for both signs; the sign of negative tone is inferred from context). Equations on pp. 8, 11, 12, 16–17 were reconstructed from the text layer plus context; no page images were supplied for those pages.
- Apparent misprints: the product limits in the Naïve Bayes formulas are printed as $i=1$ to $M$ but the index should be $m$. Naïve Bayes "assigns each document… to the document with the highest probability" should say category.
- Table 3 counts do not match the stated corpus: training counts sum to 299 (stated 300 coded), and the test counts sum to 7,889, which with 299 gives 8,188 versus 7,920 stated.
- The text says Fig. 4 plots date "on the vertical axis", but the image shows date on the horizontal axis.
- The references list "Quinn, Kevin. 2010" with a single author, though the text cites Quinn et al. (2010). Grimmer 2012 is listed as forthcoming.
- Recall for restrained is printed as 0.75 (111/147 ≈ 0.755).
