---
id: grimmer-2022-textasdata/ch12-clustering
work: grimmer-2022-textasdata
unit: Chapter 12. Clustering
pages: 203-235
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
# Clustering (Grimmer, Roberts & Stewart, ch. 12)

## L0 — One line
Clustering sorts documents into groups to help a researcher discover new concepts, and because no single grouping is "correct", the choice among representations, methods and K must be judged by usefulness, human reading and later validation on new data.

## L1 — The gist (≤ 120 words)
How can computers help a researcher discover new ways to organize a document collection? The chapter presents clustering: partitioning documents into K groups, with k-means as the base case. Every method rests on three choices: a document (dis)similarity measure, an objective function and an optimization algorithm. Different representations, methods and starting values give similar but distinct partitions of the same press releases, each of which may be useful for discovery. Statistics (exclusivity, cohesion), human experiments and careful reading help choose among partitions. No statistic settles the number of clusters or the single best clustering. Discovered categories should be validated on new data.

**Prerequisites:** bag-of-words vectors; Euclidean distance; mean of vectors; multinomial and Dirichlet distributions (Ch. 6); cosine similarity (Ch. 7); idea of likelihood and the EM algorithm.

## L2 — Key ideas (5–10 bullets)
- Clustering outputs a partition (mutually exclusive, exhaustive groups) estimated from the data. The researcher still chooses the inputs and interprets the output (p. 203).
- k-means alternates between assigning documents to the nearest center and recomputing centers as means. It may get stuck in a local optimum (a stable solution that is not the global best), so results can vary across runs (pp. 206–207).
- What is clustered often matters more than the algorithm. Changing the representation (word counts vs. averages of pretrained GloVe word embeddings) changes the clusters (p. 209).
- All methods have three components: dissimilarity, objective function, optimizer. Objective functions give only relative quality, not a cross-method standard (pp. 210–213).
- Methods differ in style (probabilistic or algorithmic; soft or hard; means or medoids (a medoid center is an actual document); flat or hierarchical). The probabilistic/algorithmic gap is smaller than it looks (pp. 214–222).
- Exclusivity (clusters do not repeat each other's top words), cohesion (top words co-occur in the cluster's documents), the intruder test (humans spot an off-cluster word) and pairwise-similarity ratings help to select a clustering. Careful reading is the final step (pp. 223–226).
- The in-sample objective never gets worse as K grows. Quantitative approaches to choosing K are a blunt tool, so try several granularities (pp. 227–229).
- Interpretation means distinctive words plus reading 10–30 documents per cluster. Human-in-the-loop clustering lets the analyst explore many partitions (pp. 231–233).

## L3 — Walkthrough

### Introduction (pp. 203–204)
- Discovery is iterative engagement with data and concepts. The goal here is to amplify the reader: suggest groupings, direct reading and guide interpretation (p. 203).
- Chapter 11 characterized existing groupings. This chapter produces **partitions**: mutually exclusive and exhaustive categorizations (p. 203).
- Input: texts. Output: K categories plus assignments. Each document gets a one-hot vector $\pi_i$ with $\pi_{ik}=1$ if it is in cluster $k$, else 0. Similar documents should share a cluster (p. 203).
- Three ambiguous steps: how similarity is measured, how similarities are aggregated into overall quality, how the optimization is solved (p. 203).
- The automated part is category creation. A small class of methods lets the researcher interact during clustering (Grimmer and King 2011) (p. 204).

### 12.1 An initial example: k-means (pp. 205–208)
- **Data:** 558 press releases (2005–2007) from Senator Frank Lautenberg's office. Mayhew (1974) classed congressional communications as credit claiming, position taking and advertising. The aim is to find new conceptualizations (p. 205).
- **Representation:** bag-of-words counts, divided by document length so $\mathbf W_i$ holds proportions. There are 7,118 unigrams (p. 205).
- Each cluster has a mean vector $\boldsymbol\mu_k=(\mu_{1k},\dots,\mu_{Jk})$, the average word rates of its documents (p. 205).
- Dissimilarity, squared Euclidean distance (p. 205):
$$d(\mathbf W_i,\boldsymbol\mu_k)=\sum_{j=1}^{J}(W_{ij}-\mu_{jk})^2 \tag{12.1.1}$$
- k-means makes **hard** assignments. The objective function (to be minimized) is (p. 206):
$$f(\boldsymbol\pi,\boldsymbol\mu,\mathbf W)=\sum_{i=1}^{N}\sum_{k=1}^{K}\pi_{ik}\sum_{j=1}^{J}(W_{ij}-\mu_{jk})^2 \tag{12.1.2}$$
Here $\pi_{ik}$ is the cluster indicator and the inner sum is the dissimilarity. This is the sum of squared errors.
- Direct optimization is hard because assignments are discrete, so tools used for generalized linear models do not apply (p. 206).
- **Algorithm** (Fig. 12.1, pp. 206–207):
  1. Randomly initialize centers $\boldsymbol\mu^0$.
  2. Assign each document to its closest center, giving $\pi^1$.
  3. Update centers (p. 206):
$$\boldsymbol\mu_k^{1}=\frac{\sum_{i=1}^{N}\pi_{ik}^{1}\,\mathbf W_{i}}{\sum_{i=1}^{N}\pi_{ik}^{1}}\tag{12.1.3}$$
  This is the per-dimension average of the documents assigned to cluster $k$.
  4. Repeat the two steps until the change in $f$ falls below a small threshold. Return $\boldsymbol\mu^*,\boldsymbol\pi^*$.
- No guarantee of the global minimum. The algorithm often gets stuck in **local optima**, so repeated runs are unstable (Roberts, Stewart & Tingley 2016). Better initialization reduces this (p. 207).
- An organization that is only locally optimal may well be the most substantively insightful, because there is no one correct organization and the objective is only a tool (p. 207).
- **Results, K=4 (Table 12.1, p. 207):** cluster proportions 0.17, 0.16, 0.28, 0.39. Labels come from the 10 words with the largest positive difference between $\boldsymbol\mu_k$ and the average of the other clusters' mean vectors (p. 208).
  - Cluster 4: tends to discuss position taking (e.g., a bill for victims of state-sponsored terrorism).
  - Cluster 3: credit claiming (funds for New Jersey).
  - Cluster 2: seems to relate to advertising legislative successes.
  - Cluster 1: negative comments on Republicans and the Bush administration. This does not fit Mayhew's scheme (p. 208).
- Grimmer and King (2011) found a similar category and called it "partisan taunting": an explicit, public, negative attack on another party or its members. They built a classifier and applied it to 64,033 press releases from 301 senator-years. About 27% were classified as partisan taunting (p. 208).
- Footnote 1 (p. 234): the modern k-means formulation circulated in 1957 (Lloyd, published 1982). Forgy (1965) proposed essentially the same method. MacQueen (1967) named it. Hartigan and Wong (1979) is the R default.

> **Intuition note.** k-means repeats "put each document with its nearest center, then move each center to the average of its group". It stops when the objective barely changes, but this may be a local optimum, and where it stops depends on the start. For discovery that is acceptable: you want a useful grouping, not a proven best one.

### 12.2 Representations for clustering (p. 209)
- What you cluster often matters much more than how you cluster. Document selection and representation (Part 2) are therefore central (p. 209).
- Example: each Lautenberg release was represented as the average of its pretrained GloVe word embeddings, then clustered with k-means, K=6. Table 12.2 shows similar clusters: transportation/security, awards and honors, taunting of Bush and Republicans, credit claiming for NJ grants, healthcare legislation, environment legislation (p. 209).

### 12.3 Approaches to clustering (pp. 210–222)
Two broad flavors: **statistical mixture models** (a data-generating process in the language of distributions) and **algorithmic methods** (a series of steps) (p. 210).

**12.3.1 Components of a clustering method.** Every method specifies, explicitly or implicitly, three things (p. 210).
- **(1) Document (dis)similarity** (p. 211).
  - k-means uses squared Euclidean distance. Others use cosine similarity, Manhattan distance or kernels (Ch. 7).
  - Mixture models imply a dissimilarity through the probabilities they assign. k-means corresponds to a mixture of Normals. Cosine similarity corresponds to the von Mises-Fisher distribution.
  - More generally there is a one-to-one mapping between a broad class of distributions and dissimilarity measures (Banerjee et al. 2005). Footnote 4 specifies a bijection between the regular exponential family and regular Bregman divergences (p. 234).
  - Choosing the measure is one of the hardest tasks in text analysis. The authors suggest running several methods and comparing outputs afterward.
  - Choosing the best subjectively is not inherently a problem for discovery: no conceptualization is universally "true". The condition is that new data are used to assess the final quantity of interest, so there is no "fishing" concern (pp. 211–212).
- **(2) Measure of partition quality** (p. 212).
  - k-means sums each document's dissimilarity from its center. It rewards grouping similar documents but ignores the distinctiveness of clusters.
  - Objective functions give only **relative** measures of quality given a notion of "best". They sit on different scales and use different similarity notions. A clustering should never be assumed optimal merely because of the method that produced it.
- **(3) Optimization algorithm** (pp. 212–213).
  - Searching over discrete partitions rules out calculus. The number of ways to partition 100 documents exceeds $4.75\times10^{115}$ (Ch. 2), so brute force is impossible.
  - Approximate methods give up the guarantee of a best solution but are feasible. The choice of optimizer can matter a lot even with the same dissimilarity and objective.
  - Approximation also causes instability: two runs may differ. Careful starting values help. Instability is less problematic for discovery.
  - Table 12.3 reruns k-means (K=4) from other starting values. Proportions are 0.28, 0.21, 0.42, 0.08.
  - Cluster 1 is credit claiming. Cluster 2 is a mix of taunting and advertising ("statement"). Cluster 3 is legislation generally. Cluster 4 is chemical and transportation security (container security work).

> **Intuition note.** A clustering method = a definition of "close" + a score for a whole grouping + a search procedure. Scores from different methods cannot be compared directly, so the same documents can be sorted in many defensible ways.

**12.3.2 Styles of clustering methods (pp. 213–215).** The authors do not attempt to list all methods. They say arguments for one class are often overstated, especially for discovery (p. 214).
- **Probabilistic vs. algorithmic.** Probabilistic methods specify a data-generating process and reverse it to learn hidden parameters. Algorithmic methods are motivated by intuition about a useful clustering, with theorems based on metaphors about the procedure (p. 214).
- **Soft vs. hard.** A hard partition puts each document in exactly one cluster. A soft ("fuzzy") one assigns probabilities. Algorithmic approaches tend to be hard and model-based ones soft. The difference is less significant than it seems, because soft methods tend to put most probability on one cluster for most documents (pp. 214–215).
- **Means vs. medoids.** In k-means and mixture models the center is an average. In medoid methods the center is constrained to be an assigned document. k-medoids relocates the center to the document minimizing distance to the other documents in its cluster (p. 215).
- **Flat vs. hierarchical.** Flat methods give one clustering. Hierarchical methods give a nesting: all documents together at the top, each alone at the bottom, with coarser clusters higher up the tree (p. 215).

**12.3.3 Probabilistic clustering models (pp. 215–218).**
- A mixture model supposes each document arises from one of several unknown distributions. In the Chapter 6 authorship problem some documents were attributed to each author, so each multinomial could be learned. Clustering has no such labels, so labels are inferred iteratively, as in k-means (p. 216).
- Generic process (Fig. 12.2): for each cluster $k=1..K$, sample the cluster parameters $\boldsymbol\mu_k$. For each document $i=1..N$, sample a cluster $\pi_i$ from a multinomial, then sample the data from the distribution with parameters $\boldsymbol\mu_{\pi_i}$ (p. 216).
- Common choices: mixtures of multinomials, of Normals, of von Mises-Fisher. Mixtures come with statistical infrastructure for extension, model selection and estimation, typically via EM or variational inference (p. 216).
- **Mixture of multinomials** (probabilistic, soft, mean-based, flat). It is the Chapter 6 multinomial model without labels, and a building block for Ch. 13 topic models (pp. 216–217):
$$\boldsymbol\mu_k\sim\text{Dirichlet}(\alpha)\tag{12.3.1}$$
$$\pi_i\sim\text{Multinomial}(\eta)\tag{12.3.2}$$
$$\mathbf W_i\mid\boldsymbol\mu,\pi_i,M_i\sim\text{Multinomial}(M_i,\boldsymbol\mu_{\pi_i})\tag{12.3.3}$$
  - Including document length $M_i$ lets it group documents by similar word-use rate. It also keeps the information that longer documents carry more evidence (p. 217).
- **Mixture of von Mises-Fisher** (Banerjee et al. 2005). The distribution is for directional data and related to cosine similarity. It works with length-normalized data (p. 217):
$$\mathbf W_i^{*}=\frac{\mathbf W_i}{\lVert\mathbf W_i\rVert}\tag{12.3.4}$$
$$=\frac{\mathbf W_i}{\sqrt{\sum_{j=1}^{J}(W_{ij}-W_{i'j})^2}}\tag{12.3.5}$$
$$\boldsymbol\mu_k\sim\text{Dirichlet}(\alpha)\tag{12.3.6}$$
$$\pi_i\sim\text{Multinomial}(\eta)\tag{12.3.7}$$
$$\mathbf W_i^{*}\mid\pi_i,\boldsymbol\mu\sim\text{von Mises-Fisher}(\phi,\boldsymbol\mu_{\pi_i})\tag{12.3.8}$$
  - It is the analogue of the normal distribution on the surface of a sphere. $\boldsymbol\mu_k$ is the center and $\phi$ is analogous to precision (p. 217).
  - The three components: dissimilarity is the cosine of the angle between document and center. The likelihood is the objective. EM is a widely used optimizer (p. 218).
  - Table 12.4 (K=4): the k-means taunting and statements clusters merge into vMF cluster 4. vMF cluster 1 (military legislation) is one part of k-means position taking. Credit claiming aligns strongly across both (p. 218).
  - Multinomials consider the rate of word use. vMF considers the direction of the normalized vector. Neither is right or wrong; they treat document magnitude differently (p. 218).
- **Others:** mixture of Gaussians, closely related to k-means. Mixture of Bernoullis, a form of latent class analysis. Within well-behaved distributions, optimization stays relatively straightforward. These models are building blocks for hierarchies, e.g., documents nested in time or author (p. 218).

**12.3.4 Algorithmic clustering models (pp. 218–222).** These make no explicit data-generating assumptions. They define an algorithm and performance relative to an explicit objective (p. 218).
- **Affinity propagation** (Frey and Dueck 2007): algorithmic, hard, medoid-based, flat (p. 219).
  - It takes an arbitrary similarity matrix. Every cluster has a document as exemplar. It iteratively assesses which documents are fit to be exemplars.
  - The diagonal (self-similarity) sets the chance a document becomes an exemplar. Low values give few clusters and high values give more. So K is set indirectly, and the user still must set self-similarity.
  - Example (Table 12.5): cosine similarity, self-similarity $-7$, giving 4 clusters. Taunting and statements fall mostly into cluster 2. Clusters 3 and 4 split work by topic (safety vs. healthcare), whereas k-means split it by national vs. New Jersey.
- **Hierarchical clustering** (a class of algorithms; Ward 1963). It returns a tree. Many similarity measures can be used, typically symmetric ones (p. 220).
  - The user must "cut" the tree at a height. Fig. 12.3 uses Ward's minimum variance method. Cutting at height 3 gives three clusters (Table 12.6): legislation and position taking, credit claiming, and national/homeland security. Other cuts give further subdivisions (pp. 220–221).
- **Other algorithmic approaches** often recast clustering as a related problem, e.g., spectral clustering, analogous to graph-cutting algorithms for finding communities in a network. They impose fewer restrictions on data representation but lack the statistical infrastructure of probabilistic models (pp. 221–222).

**12.3.5 Connections (p. 222).**
- k-means is a limiting case of a mixture of normals as the covariance matrices go to zero (Kulis and Jordan 2012; Broderick et al. 2013). The different algorithms also gave similar solutions above.
- k-means is often said to assume nothing, while normal mixtures assume multivariate normal clusters. But Gaussian mixtures are also based on minimizing the sum of squared errors. Their distributional assumptions encode the same dissimilarity and quality measure that k-means has.
- As with linear regression as an approximation when the data are not conditionally normal (Aronow and Miller 2019), mixture models can be read as well-defined approximations. The authors care less about assumptions than about interesting insights validated in new data (Principle 3, Ch. 10).

> **Intuition note.** "Probabilistic" and "algorithmic" are two languages for the same kind of thing: a distance and a score to be minimized. One difference the authors name: probabilistic models come with statistical infrastructure (extension, model selection, estimation), while algorithmic methods place fewer restrictions on the data representation.

### 12.4 Making choices (pp. 223–229)
The analyst still must choose the representation, method, K and hyperparameters (p. 223).

**12.4.1 Model selection (pp. 223–226).** No single statistic suffices. The preferred procedure combines statistics, experiments with outside human evaluators, and deep manual inspection (p. 223).
- **Statistics** (Roberts et al. 2014; Mimno et al. 2011). A good clustering is *cohesive* (documents within a cluster use language similarly) and *exclusive* (clusters do not repeat the same content). More clusters make groups more cohesive but may duplicate content (p. 223).
- Let $\boldsymbol\mu_k$ be the center vector. $\mu_{jk}$ is the probability of appearance of word $j$ in cluster $k$. Let $\mathcal M_k$ be the indices of the $M$ largest weights in cluster $k$. For $m\in\mathcal M_k$ (p. 224):
$$\text{Exclusivity}_{mk}=\frac{\mu_{mk}}{\sum_{k=1}^{K}\mu_{mk}}$$
  - It equals 1 if the word is used in only one cluster. It equals $1/K$ if used equally across clusters, and is smaller if the word is used more in other clusters.
$$\text{Average Exclusivity}=\frac1K\sum_{k=1}^{K}\sum_{m\in\mathcal M_k}\text{Exclusivity}_{mk}$$
- **Cohesion** follows Mimno et al. Let $D(\cdot)$ count documents: $D(m_1,m_2)$ counts co-occurrences, $D(m_1)$ counts documents containing $m_1$. With the top-$M$ words (p. 224):
$$\text{Cohesion}=\sum_{n=1}^{M}\sum_{l=1}^{n-1}\log\frac{D(m_n,m_l)}{D(m_l)}\tag{12.4.1}$$
  Average over clusters for a clustering-level measure. (The page prints the inner upper limit as "$l-1$"; see Reading notes.)
- Cohesion and exclusivity cannot be compared across models with different numbers of clusters (Roberts et al. 2014). Raising exclusivity necessarily lowers cohesion, so the statistics give no single winner. They can show which models lie on the **cohesiveness/exclusivity frontier**, the best trade-offs (pp. 224–225).
- **Experiment 1: topic (cluster) intruder** (Chang et al. 2009). Take a cluster's top $M$ words. Pick a different cluster at random, pick one of its top words at random, and add it as an intruder, giving $M+1$ words. Participants identify the intruder. A higher detection rate means a better clustering under human evaluation (p. 225).
  - The number of examples to code depends on the intrusion rate: lower detection rates need more examples, since variance is very low when the rate is very high. Ying, Montgomery and Stewart (2019) generalize these tasks, including validating human-chosen labels (p. 225).
- **Experiment 2: cluster quality** (Grimmer and King 2011). Sample document pairs in the same cluster and pairs in different clusters. Coders rate each pair 1 (no similarity), 2 (some), 3 (very similar) (pp. 225–226):
$$\text{Cluster Quality}=\text{Average}_{\text{Same Cluster}}-\text{Average}_{\text{Different Cluster}}$$
  Higher is better. Footnote 6: to compare two clusterings, only pairs on which the two disagree matter (p. 234).

**12.4.2 Careful reading (p. 226).** Statistics and experiments may conflict and leave several viable clusterings. Only careful consideration of what each organization means and implies can adjudicate. Which clusters matter depends on the research question: chemical/transportation security, taunting or credit claiming may each be relevant or irrelevant (p. 226).

**12.4.3 Choosing the number of clusters (pp. 226–229).**
- *Common strategies* (p. 227):
  - In-sample fit cannot guide K: the k-means objective improves as clusters are added. Following it alone would put every document in its own cluster. Footnote 7 gives an argument: with $K$ optimal clusters containing distinct documents, moving the worst-fitting document to a new cluster improves or keeps the objective (pp. 234–235).
  - **Penalized fit:** AIC and BIC for mixture models penalize extra clusters, so a new cluster must improve fit by more than its penalty.
  - **Estimate K during fitting:** affinity propagation via self-similarity. Nonparametric Bayes via the Dirichlet process prior, a prior over distributions: infinitely many clusters exist, a finite number appear in the data (p. 227).
  - Footnote 8 (p. 235): the DPP has a base measure $G_0$ and a concentration parameter $\xi$. As $N\to\infty$ the expected number of clusters is $\xi\log(1+N/\xi)$. It has a "rich get richer" dynamic. Pitman-Yor retains similar features.
  - **Held-out prediction** (Wallach et al. 2009): too many clusters overfit, capturing noise (p. 228).
- *Shortcomings* (p. 228):
  - Quantitative approaches are blunt. There may be only a weak relationship between their output and the most useful model for discovery.
  - Chang et al. (2009) show that, for a particular set of documents, human scores and automated scores were negatively related.
  - Preprocessing discards information. "Interesting" is hard to model beforehand, so statistics alone will miss interesting organizations and cannot settle K.
- *Advice* (pp. 228–229): try many cluster sizes. The research question sets the granularity (broad "Sports" vs. "Soccer"). Then use the Section 12.4 tools to choose among clusterings.
- With 40 clusters instead of 4 (Table 12.7), the security cluster of Table 12.3 splits into cluster 36 (chemical security) and cluster 23 (transportation security). New clusters appear, e.g., cluster 16 on banning smoking in public places. The authors say one good approach is to start with many clusters and group them into larger concepts (p. 229).

> **Intuition note.** Adding clusters never makes in-sample fit worse, as with adding parameters to a statistical model. Quantitative approaches to choosing K are a blunt tool. The right K is the one whose granularity matches your question, so you should compare several.

### 12.5 The human side of clustering (pp. 231–233)
**12.5.1 Interpretation** (building on Quinn et al. 2010). The aim is to turn the algorithmic rule into a substantive rule you could explain to manual coders. The authors argue (later in the book) that a good test is to replicate the conceptualization by hand coding or supervised learning (p. 231).
- *Method 1: distinctive words.* Cluster-center parameters have limits. Some methods (affinity propagation) have no vocabulary parameters, and parameters differ across methods. The Chapter 11 techniques work for any method (p. 231).
- *Method 2: sample documents.* Read 10–30 documents per cluster, take notes, synthesize a label. If no label is readily available, that is good evidence the cluster (or partition) may not be useful for discovery. Reading grouped texts can itself give insights (pp. 231–232).

**12.5.2 Interactive clustering (pp. 232–233).**
- New methods are rigorously derived and typically shown to beat others on a task such as information retrieval or classification. Yet, to the authors' knowledge, there are no generally applicable theorems showing one method is better for discovering useful content. There is also no guidance on when to apply which method from observable data features (p. 232).
- Method choice may be driven by convenience. The cause is the vague goal of discovery: no easily written objective function. Whether a clustering is interesting cannot be known without human intervention, so fully automated search that excludes humans is impossible (pp. 232–233).
- Grimmer and King (2011) build a "geography" of many clusterings, a map in which nearby solutions are similar. This is how they found partisan taunting (p. 233).
- *Trade-offs* (p. 233):
  - Traditional methods give one clear clustering and are easy to extend with interpretable parameters, but limit the assumptions considered.
  - Human-in-the-loop methods explore many more clusterings but can require a great deal of analyst work and cannot be automated.

### 12.6 Conclusion (p. 234)
Clustering helps discovery, but forcing each document into one cluster limits the patterns found. It is simple to summarize but narrow. The next chapters turn to mixed-membership topic models and document embeddings (p. 234).

## Toy example (ours, not from the text)
Four documents, two words (J=2), proportions: $W_1=(0.8,0.2)$, $W_2=(0.6,0.4)$, $W_3=(0.1,0.9)$, $W_4=(0.2,0.8)$. K=2, initial centers $\mu_1^0=W_1=(0.8,0.2)$, $\mu_2^0=W_4=(0.2,0.8)$.

**Assignment 1** (squared Euclidean):
- $W_1$: to $\mu_1$: 0; to $\mu_2$: $0.6^2+0.6^2=0.72$ → cluster 1.
- $W_2$: to $\mu_1$: $0.2^2+0.2^2=0.08$; to $\mu_2$: $0.4^2+0.4^2=0.32$ → cluster 1.
- $W_3$: to $\mu_1$: $0.7^2+0.7^2=0.98$; to $\mu_2$: $0.1^2+0.1^2=0.02$ → cluster 2.
- $W_4$: to $\mu_2$: 0 → cluster 2.

**Update (12.1.3):** $\mu_1^1=((0.8+0.6)/2,(0.2+0.4)/2)=(0.7,0.3)$. $\mu_2^1=((0.1+0.2)/2,(0.9+0.8)/2)=(0.15,0.85)$.

**Objective (12.1.2):** $W_1$: $0.1^2+0.1^2=0.02$. $W_2$: 0.02. $W_3$: $0.05^2+0.05^2=0.005$. $W_4$: 0.005. Total $f=0.05$.

**Reassign:** $W_1$ to $\mu_1$ (0.02 vs. $0.65^2+0.65^2=0.845$). $W_2$ to $\mu_1$ (0.02 vs. $0.45^2+0.45^2=0.405$). $W_3$ and $W_4$ stay in cluster 2 ($W_3$: 0.005 vs. $0.6^2+0.6^2=0.72$). No change, so the algorithm stops.

**Labeling:** word-1 rates are 0.7 vs. 0.15, so word 1 labels cluster 1 (difference of $\mu_1$ from the other center: $0.7-0.15=0.55$). **Exclusivity** of word 1 in cluster 1: $0.7/(0.7+0.15)=0.7/0.85\approx0.824$. In cluster 2 it is $0.15/0.85\approx0.176$.

## Concepts
- [[partition-clustering]] (new) — mutually exclusive, exhaustive grouping of documents, with one-hot $\pi_i$ (p. 203)
- [[k-means]] (new) — alternate nearest-center assignment and mean update to minimize summed squared Euclidean distance (pp. 205–207)
- [[objective-function-clustering]] (new) — score of a partition given a dissimilarity. It gives only relative, within-method comparisons (pp. 206, 212)
- [[local-optimum-instability]] (new) — iterative clustering stops at local optima, so reruns can differ; tolerable for discovery (p. 207, p. 213)
- [[clustering-three-components]] (new) — every method fixes a dissimilarity, a quality objective and an optimizer (p. 210)
- [[hard-vs-soft-clustering]] (new) — one cluster per document vs. probabilities over clusters (p. 214)
- [[mixture-model-clustering]] (new) — generative model: draw cluster, then document from that cluster's distribution (p. 216)
- [[von-mises-fisher-mixture]] (new) — mixture on length-normalized vectors; cosine-based similarity (p. 217)
- [[affinity-propagation]] (new) — medoid-based, hard method where self-similarity indirectly sets cluster count (p. 219)
- [[hierarchical-clustering]] (new) — a tree of nested clusters, cut at a height to get a partition (p. 220)
- [[exclusivity-cohesion]] (new) — statistics for clusters that are distinct and internally coherent; trade-off frontier (pp. 223–225)
- [[intruder-detection-test]] (new) — humans spot an off-cluster word among top words (p. 225)
- [[choosing-number-of-clusters]] (new) — in-sample fit never worsens with K. Quantitative approaches are blunt, so compare several granularities (pp. 227–229)
- [[human-in-the-loop-clustering]] (new) — analyst explores a map of many clusterings (p. 233)
- [[text as data / validation]] — here: label by distinctive words, reading 10–30 documents, and replicate with hand coding or supervised learning; validate in new data (pp. 211–212, 231)
- [[partisan-taunting]] (new) — explicit, public, negative attack on another party; a category discovered by clustering (p. 208)

## Canonical instances
- [[lautenberg-press-releases]] — 558 releases, 7,118 unigrams; running example across all methods (p. 205)
- [[mayhew-credit-position-advertising]] — conceptual typology that the clusters loosely match (p. 208)
- [[partisan-taunting-discovery]] — cluster not fitting Mayhew; classifier finds about 27% of 64,033 releases (p. 208)
- [[k-means-local-optimum-example]] — Tables 12.1 vs. 12.3: same method, different starts, different clusters (pp. 207, 214)
- [[forty-cluster-granularity]] — Table 12.7: the security cluster splits; a smoking cluster appears (p. 229)

## Bridges (candidates)
- [structural-analogy] k-means as limit of a Gaussian mixture as covariances → 0 ↔ statistics: hard-EM as limit of soft-EM — the chapter states the limiting relation (p. 222).
- [structural-analogy] choosing K with penalties (AIC/BIC) ↔ model selection in regression — more parameters always fit better in-sample (p. 227).
- [metaphor] mixture of Bernoullis as latent class analysis ↔ survey methodology: latent classes — the text names the link (p. 218).
- [structural-analogy] human-intruder test ↔ text as data / validation: human checks of whether discovered categories are coherent (p. 225).

## Questions this raises
- If objective scores and human judgments can be negatively related (Chang et al. 2009), what should replace automatic scores when comparing clusterings?
- How should a researcher validate a discovered category (like partisan taunting) in new data so the discovery–validation separation holds?
- When do mixed-membership models (Ch. 13) lose less information than forcing one document into one cluster?
- Can a pairwise-rating "cluster quality" be computed cheaply enough to compare many clusterings?

## Reading notes
- Printed page = pdf page (offset 0). Footnotes are on pp. 234–235.
- The text layer garbles equations. I checked them against the page images where visible. Eq. 12.3.4 appears without visible norm bars. I rendered it as $\mathbf W_i/\lVert\mathbf W_i\rVert$, which matches the text's description of normalization by magnitude.
- Eq. 12.3.5 prints "$W_{i'j}$" inside the root as shown; I copied it and suspect a misprint (probably $W_{ij}^2$).
- Eq. 12.4.1 prints the inner sum's upper limit as "$l-1$", which cannot be right for an index $l$. I wrote $n-1$ (our reading) and the fraction as printed.
- Fig. 12.2's caption says $\alpha$ and $\eta$ are priors on membership and cluster parameters respectively. Eqs. 12.3.1–12.3.2 use $\alpha$ for $\boldsymbol\mu$ and $\eta$ for $\pi$, the opposite order.
- The average exclusivity formula is printed without dividing by $M$.
- Typos in the source: "Launtenberg" (p. 209), "mediod" (pp. 215, 219).
- The unit has no exercises. Figure 12.3 is a dendrogram (height axis 0–3, p.
