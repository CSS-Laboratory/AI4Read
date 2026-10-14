---
id: grimmer-2022-textasdata/ch13-topic
work: grimmer-2022-textasdata
unit: Chapter 13. Topic Models
pages: 236-259
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Topic Models (Latent Dirichlet Allocation, covariates, STM, labeling)

## L0 — One line
Topic models replace the "one document, one cluster" assumption with mixed membership: each document is a weighted mixture of topics. This gives more focused, interpretable categories for discovery, and metadata can be built into the model.

## L1 — The gist (≤ 120 words)
Clustering puts each document in one category, but documents may mix several ideas. Topic models, above all Latent Dirichlet Allocation (LDA), let each document have proportional membership in all topics, and each topic is a distribution over words. The chapter shows how to interpret topics (read high-share documents, inspect top words), how to add metadata (covariates that shape how much of a topic a document has or which words a topic uses; outcomes the topics must also explain; the Structural Topic Model), and gives two discovery examples (fire-grant credit claiming; radical discourse). It suggests that topic models seem popular in social science largely because the simple additive structure keeps interpretation tractable, even though more flexible models can predict better.

**Prerequisites:** multinomial and Dirichlet distributions; Bayesian hierarchical models and plate diagrams; the multinomial mixture/clustering model of Ch. 12; document-term matrix; basic regression.

## L2 — Key ideas (5–10 bullets)
- Topic models are mixed membership models: each document has topic proportions $\pi_i$, and each topic is a word distribution, so a document can mix themes that a single cluster would fit poorly (pp. 236–238).
- LDA's generative story is: draw topic weights, draw a topic for each token, then draw the word from that topic's distribution. Inference is hard and the different strategies can give quite different results (pp. 237–239).
- Used inductively, a 40-topic LDA on Senate press releases surfaced a fire-grant topic. That led to a chain of findings: agency pre-announcement, implicature (implying credit without literally claiming it) as a credit-claiming strategy, and an experiment (pp. 239–241).
- Interpreting topics means reading documents with a high topic share and inspecting top words. The number of topics cannot be settled without the application (pp. 242–243).
- Upstream covariates are document metadata that enter before the topics. Prevalence covariates (which set how much of each topic a document has) share information across documents through the prior, and upstream covariates primarily help when documents are short. Content covariates (which let a topic's words vary by group or time) change the model much more, so topic versions can become incomparable (pp. 245–248).
- Downstream covariates are outcomes generated from the topics, so topics must explain them as well as the words; supervised LDA (sLDA) is the prediction case. This serves two purposes: predictive performance, and projecting words and covariates (for example votes) into a common space (pp. 248–249).
- The Structural Topic Model (STM) lets metadata affect both topic prevalence and content, though most uses leave out content covariates. If the aim is only to describe substantive variation, running LDA and then regressing topic proportions on covariates is a straightforward approximation, which may lose some benefit of borrowing information (pp. 251–253).
- Labeling runs on a continuum from model-based to document-based. FREX (a weighted harmonic mean of word frequency and exclusivity) penalizes words that are frequent but not exclusive. Reading documents remains essential (pp. 255–256).
- A potential trade-off: models without the additive structure can predict held-out text much better but are harder to interpret (pp. 257–258).

## L3 — Walkthrough

### Introduction (p. 236)
- Clustering methods, even "soft" ones, assume one cluster per document; soft methods only express uncertainty about that assignment (p. 236).
- Documents (speeches, news articles, novels) may contain several ideas, and clustering obscures this variation (p. 236).
- Topic models give each document proportional membership in all categories (a mixed membership model). No topic must represent a whole document, so topics can be more focused and more interpretable (p. 236).

### 13.1 Latent Dirichlet Allocation (pp. 237–238)
LDA is a Bayesian hierarchical model. It builds on the multinomial language model (Ch. 6) and the multinomial mixture model (Ch. 12) (p. 237).

**Data-generating process** (p. 237):
1. For each document $i = 1,\dots,N$, draw a $K\times 1$ vector of topic weights $\pi_i = (\pi_{i1},\dots,\pi_{iK})$.
2. For the $m$th word ($m = 1,\dots,M_i$), called $\tilde W_{im}$, draw a topic indicator $Z_{im} \sim \text{Multinomial}(1,\pi_i)$.
3. Draw the word $\tilde W_{im} \sim \text{Multinomial}(1,\mu_{Z_{im}})$. Here $\mu$ is a $J\times K$ matrix. Its $k$th column $\mu_k = (\mu_{1k},\dots,\mu_{Jk})$ is a $J\times 1$ vector, and $\mu_{jk}$ is the probability of using word $j$ when discussing topic $k$.
4. Summing over words gives the document-term-matrix row:
$$W_{i,\cdot} = \sum_{m=1}^{M_i} \tilde W_{i,m}$$
5. Priors: both $\pi_i$ and $\mu_k$ are drawn from Dirichlet distributions (hyperparameters $\alpha$ and $\eta$ in Figure 13.1). A simple default prior is common, but asymmetric priors can give more meaningful topics (Wallach, Mimno, and McCallum, 2009) (p. 237).

The plate diagram (Fig. 13.1, p. 238) differs from the mixture model's (Fig. 12.2) by an inner plate over tokens. This lets each token have its own topic, while $\pi_i$ is the fraction of the document assigned to each topic (p. 238).

**Intuition example** (pp. 237–238). One conversation is about US presidential politics and another about gardening. Each has its own correlated vocabulary. The topics give relatively high probability to "presidential" or "gardening" words. Some common words may be high in both topics, and both topics give some (often small) weight to all the words in the vocabulary (p. 238). A document about the White House's garden can be an equal mix of the two topics. LDA can explain such a lone document well if other documents cover the two components, because each component has a specialized vocabulary. A single-membership model would likely put it in one cluster, and both clusters would fit it poorly (p. 238).

> **Intuition note.** Each word in a document is generated by first picking a topic and then a word from that topic. The document's topic weights say how much of the text comes from each theme, so a document that combines known themes in a new way can be explained well, as long as other documents show each theme, without needing a cluster of its own.

#### 13.1.1 Inference (pp. 238–239)
The strategy is to specify a generative process and reverse-engineer the parameters from the data. LDA's complexity makes this hard. There are three broad strategies: collapsed Gibbs sampling, variational approximations, and method-of-moments estimators. The authors do not detail them but stress that the approaches can yield quite different results (p. 239).

#### 13.1.2 Example: credit claiming for fire grants (pp. 239–241)
- **Data and model.** They run LDA on all Senate press releases from Grimmer (2010): 72,631 press releases from over 100 senators. They removed stop words, stemmed, and removed punctuation and numbers. They used the R package topicmodels and estimated 40 topics, optimized by variational EM (p. 239).
- **Output.** Table 13.1 lists the ten most probable words per topic. Familiar topics appear, for example food and product safety (Topic 10), immigration (Topic 16), education (Topic 28). To use the topics one would read representative documents and label each one (p. 239).
- **Discovery.** Topic 7 has top words such as "fire," "depart," "grant." Using a different topic model (the "Expressed Agenda Model"), Grimmer (2010) found the same category. No earlier conceptualization of Congressional speech had proposed it. It was validated as referring to a real program, the Assistance to Firefighters Grant Program (AFGP). Classification into the category was surprisingly accurate, and about 2% of press releases related to the program (p. 239).
- **Follow-up** (Grimmer, Westwood, and Messing, 2014) (p. 241):
  - After replicating the finding in House press releases, they noted that the AFGP was designed to be impervious to Congressional influence (competitive awards). So why were members claiming credit?
  - Interviews with agency officials: the agency alerted Congressional officials before the official announcement. The authors confirmed this pattern in aggregate with press-release data and announcement timing.
  - How can legislators claim credit? Through **implicature**: they imply responsibility without literally claiming it. They "announce" new money and speak broadly about fighting for such funding. For spending they directly control, they say they "secured" funding.
  - In an experiment, when legislators implied they deserved credit they received credit. When they explained their actual contribution, constituents were reluctant to reward them.
- **Lesson.** The authors present this as the power of being explicitly inductive, assembling evidence rather than expecting hypotheses beforehand. They applied a deductive method (the experiment) where appropriate (p. 241).

### 13.2 Interpreting the output (pp. 242–243)
- Like clustering, LDA can strongly depend on arbitrary tuning parameters and the inference method. For discovery this variation can be useful: if a run gives one useful way of looking at the data, the model has been useful (p. 242).
- Two recommended interpretation methods: careful reading of exemplar texts, and quantitative procedures for finding words that distinguish topics (p. 242).
- Because documents have partial membership everywhere, reading a random sample of texts assigned to a cluster, as recommended for clustering, needs a slight modification. Two options (pp. 242–243):
  - Select the few documents with the highest share of the topic.
  - Sample documents with probability increasing in their share, for example
$$\hat\pi_{ik} = \frac{\pi_{ik}}{\sum_{\ell=1}^{N}\pi_{\ell k}}$$
  This ensures variety but may select documents with little relation to the topic (p. 243).
- Example (Table 13.2): five randomly selected press releases with over 0.20 of Topic 7. Titles such as "Shelby Announces over $102,000 for Fulton Volunteer Fire Department" give a sense of the topic and of how members may use implicature to claim credit (pp. 242–243).
- Top-probability words (as in Table 13.1) are useful but can obscure what is distinctive, because common words have high probability in many topics. Section 13.5 covers separating words (p. 243).
- The number of topics cannot be determined without knowing the specific application, since topic models of different granularity yield different insights (p. 243).

### 13.3 Incorporating structure into LDA (pp. 244–250)
**Hierarchy.** A population-level Dirichlet gives every document's topic mixture. Given the mixture, topic labels for words are drawn, and these select the topic-specific multinomial for each word (p. 244).

**Why add metadata.** Social scientists often hold metadata (author, venue, date) and want to see how topic prevalence varies with it (p. 244). Examples:
- Catalinac (2016b): Japanese party manifestos over time.
- DiMaggio, Nag, and Blei (2013): newspapers' framing of arts funding.
- Grimmer (2010): author information built into the model to capture senators' presentational style.
- Quinn et al. (2010): topics in Senate debates evolve smoothly, with the prior day's topics informing the next day's (p. 244).

Speaker characteristics might also affect topic content. Republicans and Democrats may share vocabulary but discuss tax policy differently (p. 244). This raises a conceptual issue: are texts with different metadata discussing different versions of one topic, or different topics? There is no bright line, so researchers should be cautious with covariates (pp. 244–245).

**Two kinds of covariate model** (Mimno and McCallum, 2008) (p. 245):
- *Upstream:* model structure to improve interpretability and estimate association with topics.
- *Downstream:* designed to generate topics that are predictive of the covariate.

#### 13.3.1 Upstream, known prevalence covariates (pp. 245–246)
- The global prior $\alpha$ on $\pi_i$ is replaced by a document-specific prior that is a function of covariates $X_i$. "Upstream" refers to the plate diagram: following the arrows downstream from the covariates leads to the topic proportions. Information is shared, but topics do not try to explain the covariates (p. 245).
- Early examples: authors (Rosen-Zvi et al., 2004), time (Blei and Lafferty, 2006), early social-science uses (Quinn et al., 2010; Grimmer, 2010), then arbitrary covariates (Mimno and McCallum, 2008; Roberts et al., 2013) (p. 245).
- **Main benefit: short documents.** Topic models rely on word correlations. Long documents show many related words. Short ones do not, so two documents on similar topics could look very distinct (p. 245). Covariates let the model "borrow strength" through the prior from documents with similar covariates (p. 246).
- As document length tends to infinity the data overwhelms the prior, and the estimate depends only on the document's words. For extremely long documents, one can split them into chunks and use hierarchical structure to aggregate back (p. 246).

#### 13.3.2 Upstream, known content covariates (pp. 246–248)
- The topic-specific word distribution varies by time (Blei and Lafferty, 2006), geography (Eisenstein et al., 2010), ideology (Ahmed and Xing, 2010), or an arbitrary categorical covariate (Eisenstein et al., 2010; Roberts et al., 2013) (p. 246).
- This essentially creates one version of each topic per covariate level. Versions are tied together by sparse deviations (Eisenstein et al., 2010; Roberts et al., 2014) or by smoothness such as continuity through time (Blei and Lafferty, 2006) (p. 246).
- **Example (Fig. 13.2, Blei and Lafferty 2006, journal *Science*).** The neuroscience topic's top words move from brain, movement, action to neuron, brain, synapse. The authors say this provides a powerful insight into how scholarly discourse about neuroscience evolved over time (pp. 246–247).
- Uses: differences in language between subpopulations talking about the same thing (Republicans "death tax", Democrats "estate tax"). They can also marginalize out an uninteresting difference. Lucas et al. (2015): machine-translate to a common language and use a language content covariate (p. 247).
- **Caution.** Content covariates change the model much more than prevalence covariates and risk making topic versions incomparable. In the *Science* study the topic fit in 2000 is very different from the topic in 1881; what connects them is the continuity from decade to decade. Whether two variations are the same topic conceptually is "a thorny question" without an obvious resolution (pp. 247–248). Footnote 3 (p. 258): here, topic evolution is strongly influenced by the variance parameter of the time random walk. If it is too large, topics evolve into unrelated topics.

> **Intuition note.** Prevalence covariates change how much of each topic a document has. Content covariates change what a topic's words are, per group or period. The second is a bigger change, so the "same" topic may drift into something else.

#### 13.3.3 Downstream, known covariates (pp. 248–249)
- In a downstream model (Fig. 13.3) the covariate $y_i$ is generated from the token-level topic indicators $z$, with parameters $\theta$. This forces topics to explain both the words and the covariate (p. 248).
- Two purposes: maximizing predictive performance, and projecting words and covariates into a common space (p. 248).
- **Prediction case.** Example: predict a movie reviewer's star rating $y_i$ from the review text $W_{i,\cdot}$. The hope in the original LDA paper was that topics would be good classifier features. They often were not. $\pi_i$ predicted the words well but not necessarily $y_i$ (p. 248).
- **Supervised LDA** (sLDA; Mcauliffe and Blei, 2008) places $y_i$ downstream of the topics. For a new document, infer $\pi_i$ from the words and use it to predict $y_i$ (pp. 248–249). Footnote 4 (p. 258): in practice a function of the token-level $Z$ is used, because it performs better. $\pi_i$ can become too disconnected from the words. This idea recurs in Chapter 26 (p. 249).
- **Common space.** With high-dimensional $y$, such as votes, and text from political actors: bills and votes (Gerrish and Blei, 2012; Kim, Londregan, and Ratkovic, 2018), Supreme Court opinions and votes (Lauderdale and Clark, 2014). Both are projected into a common space, which combines data sources believed to inform an underlying measure (p. 249).

> **Intuition note.** Upstream covariates feed information in, and the topics are not asked to explain them. Downstream covariates are outcomes the topics must also explain, so the topics are tuned toward prediction.

#### 13.3.4 Additional sources of structure (p. 249)
Substantive knowledge can enter through sparse topics (Wang and Blei, 2009; Williamson et al., 2010), hierarchical topics (Li and McCallum, 2006; Paisley et al., 2015), preferred word connections (Andrzejewski, Zhu, and Craven, 2009), keywords (Magnusson et al., 2018; Eshima, Imai, and Sasaki, 2020), or interactive human feedback (Vikram and Dasgupta, 2016; Hu et al., 2014, with the model refit on the fly). A second modeling layer can group texts: Grimmer (2013a) clusters senators by attention to topics, Blaydes, Grimmer, and McQueen (2018) cluster topics by linguistic similarity. Applied to prevalence, this finds groups and borrows strength. Applied to topics, it can mitigate the number-of-topics problem by giving granular and coarse topics together. The authors say the covariates are "discovered" here because clustering is equivalent to stratifying on covariates inferred during estimation (pp. 249–250).

### 13.4 Structural Topic Models (pp. 251–253)
The STM (Roberts, Stewart, and Airoldi, 2016) takes general upstream metadata that can affect both topic prevalence and content (p. 251). For unit $i$, $X^p_i$ are $P$ prevalence covariates and $X^c_i$ are $P'$ content covariates. The generative model (as printed, p. 251):
$$\gamma_k \sim \text{Normal}_P(0,\sigma^2 I_P)$$
$$\pi_i \sim \text{LogisticNormal}_{K-1}\big(\Gamma'(X^p_i)',\,\Sigma\big)$$
$$Z_{im}\sim \text{Multinomial}_K(\pi_i)$$
$$\tilde W_{im}\sim\text{Multinomial}_J\big(\mu^c_{Z_{im}}\big)$$
$$\mu^c_{kj} = \frac{\exp\big(\kappa^{(0)}_j+\kappa^{(t)}_{kj}+\kappa^{(c)}_{X^c j}+\kappa^{(int)}_{X^c kj}\big)}{\sum_j \exp\big(\kappa^{(0)}_j+\kappa^{(t)}_{kj}+\kappa^{(c)}_{X^c j}+\kappa^{(int)}_{X^c kj}\big)}$$
with $W_{i,\cdot}=\sum_{m=1}^{M_i}\tilde W_{im}$ (p. 251).
- $\Gamma$ is a $P\times(K-1)$ coefficient matrix for the prevalence model (p. 251).
- $\kappa^{(0)}$ is the corpus-wide distribution of the vocabulary. $\kappa^{(t)}$, $\kappa^{(c)}$, $\kappa^{(int)}$ are rate deviations for topics, covariates, and topic-covariate interactions (p. 251).
- Key idea: each $\kappa$ captures how word use varies across covariates, how word use varies with topic prevalence, and how the two interact for a topic. This gives a flexible way to measure the presence or absence of a topic (p. 251).
- Fig. 13.4: prevalence covariates inform the prominence of topics, content covariates alter how topics are discussed. In practice, most STM uses don't use content covariates, so topics are treated much as in LDA (p. 252).
- **Why covariates help.** Roberts, Stewart, and Airoldi (2016) show that covariates help STM find more substantively interesting topics, also more stable with few documents or limited vocabulary (p. 252). The prior on document topics borrows information across documents. Without covariates, all documents share one prior and borrow equally. With covariates, information comes from documents with similar covariate values. Heuristically this helps most when covariates explain linguistic differences (p. 252).
- **Limits.** Covariates are not a panacea. They are far removed from the text in the plate diagram, so there is less they can do to improve fit as borrowing of strength matters less relative to the data (pp. 252–253).
- **Two-step approximation.** Run LDA, then regress $\pi_i$ on $X_i$. In the limit of document length and number of documents, this gives the same differences as STM, but may sacrifice some advantages of borrowing information (p. 253). Footnote 5 (p. 259): STM generalizes and combines three prior models (correlated topic model, Mimno and McCallum's prevalence covariates, Eisenstein et al.'s content covariates).

> **Intuition note.** STM lets a document's topic mix depend on its metadata via a regression-like prior, and optionally lets word rates depend on metadata too. Documents with similar metadata help each other's estimates, which can help most when text is short or when the covariates explain linguistic differences.

#### 13.4.1 Example: radical discourse (pp. 253–254)
- Karell and Freedman (2019) used STM on over 23,000 pages of magazines, newspapers, speeches, and pamphlets from 22 radical groups in Afghanistan, Iran, and Pakistan, 1979–2001, translated to English (p. 253).
- They call their approach "computational abductive analysis". It starts from a statement of existing theory: radical discourse is commonly understood as directed outward, attacking powerful people and institutions outside the group's community. Abductive analysis builds theory from surprising evidence that contrasts with existing theory (p. 253).
- They labeled eight topics using top words and representative documents. Five reflect current conceptions ("Radicalism of Subversion") (pp. 253–254).
- Two others, "Local & Education Markets" and "Religious Code," were not as expected. Close reading led them to group these into "Radicalism of Reversion", efforts to change the internal workings of the group. They recognize it as useful for groups beyond their study and conclude it could be a new concept for studying radical rhetoric globally (p. 254).

### 13.5 Labeling topic models (pp. 255–256)
- Labeling is, as with clusters, a human activity combining careful reading and automated heuristics. Methods lie on a continuum (Fig. 13.5) from model-based (use topic-model parameters) to document-based (read documents chosen completely at random) (p. 255).
- Model-based methods are easier and more automatic but rely on strong model assumptions. Document-based methods are costly but avoid dependence on the model and are often central to understanding what the model is doing (p. 255).
- Figure 13.5, left to right: model parameters, transformed model parameters, fictitious prediction problem, reading model-based subsets of documents, reading documents (p. 255).
- **Raw parameters.** $\mu$ gives each word's probability given a topic. Reading off the top words favors words common overall, because very common words co-occur with everything and are spread across topics. Removing stop words (Ch. 5) helps, but corpus-specific frequent, uninformative words remain (pp. 255–256).
- **FREX** (Roberts, Stewart, and Tingley, 2019, based on Bischof and Airoldi, 2012 and Airoldi and Bischof, 2016): the weighted harmonic mean of a word's frequency in a topic and its exclusivity to the topic, both functions of the model parameters. It penalizes words that are frequent but not exclusive, with no change to the underlying model (p. 256).
- Best practice: label with many approaches and combine the words, possibly adding words from a fictitious prediction problem (Ch. 11). Regardless, carefully read the documents (p. 256).

### 13.6 Conclusion (pp. 257–258)
- Topic models generalize clustering. In clustering, a document gets one cluster and thus one word distribution. In topic models each document has its own word distribution, constrained to be a weighted combination of the topics (p. 257).
- Alternatives: nonnegative unconstrained weights (Lee and Seung, 2001), multiple membership with topics turned on or off (Griffiths and Ghahramani, 2011), topics as paths down a tree (Paisley et al., 2015) (p. 257).
- **Limitation of additive structure.** The model cannot predict or adequately explain a document more extreme than the individual topics, because topics cannot interact. Example: a mixture of "humanities" and "computer science" cannot give "digital humanities" a higher probability than either topic gives alone (p. 257). Footnote 6 (p. 259): any convex combination lies in the interior of the convex hull, so the mixture cannot predict a word distribution sharper than the individual topics.
- Models that drop the additive structure (Salakhutdinov and Hinton, 2009; and others) are more flexible and can predict held-out text much better, but are harder to interpret. In them, top words depend on interactions among all topics present in a document (pp. 257–258).
- Flexibility vs. interpretability matters for discovery: a discovery that cannot be recognized is of little use. The authors say topic models seem popular in the social sciences largely because they balance this well: more complex than clustering, with interpretation kept tractable by additive structure and proportional membership (p. 258).
- Next chapter: document embeddings, which project documents into a low-dimensional unconstrained space, often for visualization (p. 258).
- Footnote 1 (p. 258) gives history: LSI via SVD; probabilistic LSI (Hofmann, 1999), whose document-level parameters had no prior; LDA (Blei, Ng, and Jordan, 2003) was introduced at NIPS in 2001, and the same model had been independently developed in genetics (Pritchard, Stephens, and Donnelly, 2000); the collapsed Gibbs sampler (Griffiths and Steyvers, 2004).

## Toy example (ours, not from the text)
Vocabulary $J=4$: vote, senate, soil, pesticide. Topics $K=2$ (columns of $\mu$ sum to 1):
- Politics: $\mu_{\cdot1}=(0.5,\,0.4,\,0.05,\,0.05)$.
- Garden: $\mu_{\cdot2}=(0.05,\,0.05,\,0.5,\,0.4)$.

A document has $\pi_i=(0.5,0.5)$. Under LDA, the probability of word $j$ is $\sum_k \pi_{ik}\mu_{jk}$:
- vote: $0.5(0.5)+0.5(0.05)=0.275$
- senate: $0.5(0.4)+0.5(0.05)=0.225$
- soil: $0.5(0.05)+0.5(0.5)=0.275$
- pesticide: $0.5(0.05)+0.5(0.4)=0.225$

(sum $=1.000$). Suppose a 10-word document has counts vote 3, senate 2, soil 3, pesticide 2. Ignoring the multinomial coefficient, the mixed-membership log-likelihood is $6\ln 0.275+4\ln 0.225 = 6(-1.2910)+4(-1.4917)=-7.746-5.967=-13.71$. A single-membership "politics" cluster gives $3\ln0.5+2\ln0.4+3\ln0.05+2\ln0.05 = -2.079-1.833-14.979=-18.89$. The mixture fits much better, which is the White House garden point.

Sampling weights: if four documents have Topic-$k$ shares $0.8,0.6,0.4,0.2$ (sum $2.0$), then $\hat\pi_{ik}=0.4,0.3,0.2,0.1$.

## Concepts
- [[mixed-membership-model]] (new) — each document is a weighted mixture over all topics, not one cluster (p. 236)
- [[latent-dirichlet-allocation]] (new) — Bayesian generative topic model: Dirichlet-distributed topic weights $\pi_i$ and topic-word distributions $\mu_k$; each token gets its own topic (p. 237)
- [[topic-prevalence-vs-content]] (new) — prevalence = how much of a topic a document has; content = which words the topic uses (pp. 245–246)
- [[upstream-vs-downstream-covariates]] (new) — upstream covariates enter before the topics (shaping topic prevalence through the prior, or topic content) and the topics are not asked to explain them; downstream covariates are outcomes that topics must also explain (pp. 245–246)
- [[borrowing-strength]] (new) — sharing information across similar documents via the prior, most useful for short texts (p. 246)
- [[supervised-lda]] (new) — sLDA: outcome placed downstream of topics so topics predict it (p. 248)
- [[structural-topic-model]] (new) — topic model with metadata affecting prevalence (logistic-normal prior) and optionally content ($\kappa$ deviations) (p. 251)
- [[frex]] (new) — weighted harmonic mean of word frequency and exclusivity for labeling topics (p. 256)
- [[inductive-discovery]] (new) — using models to find categories and hypotheses rather than starting from them (p. 241)
- [[implicature]] (new) — implying credit or responsibility without literally claiming it (p. 241)
- [[text as data / validation]] — here: reading exemplar documents and checking labels against real-world referents (pp. 239, 242–243)

## Canonical instances
- [[afgp-credit-claiming]] (new) — fire-grant topic in Senate press releases leads to implicature finding and experiment (pp. 239–241)
- [[white-house-garden]] (new) — a mixed document that mixed membership explains but single clusters fit poorly (p. 238)
- [[science-neuroscience-topic]] (new) — topic content changing over time, 1881–2000 (pp. 246–247)
- [[radical-discourse-stm]] (new) — STM on radical-group texts, "Radicalism of Reversion" (pp. 253–254)
- [[sLDA-movie-stars]] (new) — predicting review star rating from text (p. 248)
- [[digital-humanities-limit]] (new) — additive topics cannot make the overlap sharper than either topic (p. 257)

## Bridges (candidates)
- [structural-analogy] mixed membership of documents ↔ political-science spatial/ideal-point models: both place units in a low-dimensional space (the downstream votes-plus-text models do this explicitly) (p. 249)
- [structural-analogy] borrowing strength via covariates in the prior ↔ hierarchical/multilevel regression partial pooling — information is shared among similar units (p. 246)
- [same-math] STM two-step approximation (regress $\pi_i$ on $X_i$) ↔ regression of an estimated outcome on covariates — the second step is an ordinary regression, as the author describes (p. 253)
- [structural-analogy] credit claiming by implicature ↔ framing / priming: shifting what citizens attribute without changing facts (p. 241)

## Questions this raises
- How should one choose the number of topics when granularity changes what insights appear (p. 243)? Does the second-layer clustering of topics (p. 249) solve this in practice?
- When is a topic "the same" across covariate levels, and how can an analyst check comparability (pp. 247–248)?
- If LDA, collapsed Gibbs, variational, and moments estimators give different results (p. 239), how should discovery findings be validated?
- How much interpretability is lost in return for predictive accuracy with non-additive topic models (p. 258)?

## Reading notes
- Printed page = pdf page throughout (no offset). p. 250 is nearly empty (one line completing a sentence from p. 249).
- Equations (pp. 237, 243, 251) in the text layer are garbled. The STM block on p. 251 is flattened in the image as well. I reconstructed it from the printed symbols. In the $\tilde W_{im}$ line the printed "μ c Z i m" is read as $\mu^c_{Z_{im}}$ (content covariate $c$ as superscript). The author does not say how $\gamma_k$ enters $\Gamma$ or the $\pi_i$ line; I did not fill this in.
- p. 237 says the generated object is an "$M_i\times 1$ matrix $\tilde W_i$". Since each $\tilde W_{im}$ is a $J$-vector, the shape would be $M_i\times J$. I report the author's wording only.
- p. 254 says "Local & Education Markets" and "Religious Code" "are not inwardly facing, but externally facing", yet they are then grouped as "Radicalism of Reversion" (changing internal workings). This is probably a misprint for "not externally facing, but inwardly facing". The text also accounts for only 7 of the 8 topics.
- Table 13.1 (p. 240) text is readable (stemmed words, e.g. "texa", "firefight"). Only topics mentioned in the text are discussed here.
