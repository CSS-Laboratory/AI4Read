---
id: grimmer-2022-textasdata/ch07-vector
work: grimmer-2022-textasdata
unit: Chapter 7. The Vector Space Model and Similarity Metrics
pages: 127-139
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
# The Vector Space Model and Similarity Metrics

## L0 — One line
Treat each document as a vector of word counts, and choose the similarity or distance measure and the word weights to match what "close" should mean for your research question.

## L1 — The gist (≤ 120 words)
The chapter asks how to say that two documents are "close" once each document-feature-matrix row is a vector. Raw inner products and Euclidean distance depend on document magnitude. Cosine similarity removes this and compares only direction. Minkowski distances (p = 1, 2, ∞) stress different kinds of difference. tf-idf weighting down-weights words that occur in many documents. In the Federalist example, cosine similarity and tf-idf both make disputed paper #49 look closer to Madison. The authors stress that no similarity metric is correct in general. Choices matter because clustering (Discovery) and classification (Measurement) methods depend on them.

**Prerequisites:** vectors, dot product, square roots, logarithms; the document-feature matrix and word counts (Ch. 6); the Federalist Papers example.

## L2 — Key ideas
- Documents are vectors; closeness has no single correct definition, only metrics more or less useful for a task (p. 129).
- The inner product is the sum of element-wise products. It is sensitive to vector magnitude, so it favours Hamilton, who has more attributed essays (p. 129–130).
- Cosine similarity is the inner product of magnitude-normalized vectors. It ignores magnitude and depends only on direction (p. 130–131).
- For unit-length vectors, Euclidean distance is a function of cosine similarity. "Cosine distance" is 1 − cosine similarity (p. 133).
- Minkowski distance is a family indexed by p. As p grows, the words with the largest count differences contribute more to the distance; p = 1 (Manhattan) tends to be more robust to large single-word differences (p. 133–134).
- tf-idf multiplies counts by log(N/n_j), so words that are frequent in a document but rare in the corpus get high weight (p. 135).
- tf-idf weighting is most important for distance- and similarity-based methods; for linear regression on the document-feature matrix the weights won't matter, because regression is invariant to linear feature-level rescaling (p. 137).
- Vector and probability models are linked: cosine similarity is closely related to the von Mises–Fisher distribution (p. 138).

## L3 — Walkthrough

**Intro (p. 127–128).** The vector space model views each document-feature-matrix row as a vector in a high-dimensional space. It gives access to linear algebra and generalizes more easily to weighted counts. It comes from information retrieval; methods developed in that context tend to emphasize a definition of closeness that returns documents about a common subject matter. Assessing closeness is central to nearly all methods in the book: Discovery methods partition documents so that those within a cluster are as close as possible, and Measurement methods label unlabeled documents by the labeled documents they are closest to. This may or may not match the notion of similarity most relevant to a research question (p. 127).

**7.1 Similarity metrics (p. 129–132).**
- In general there is no single correct notion of similarity, only metrics more or less effective for particular tasks. For example, are a positive and a negative review of one film closer than two positive reviews of different films? That depends on whether sentiment or subject matter matters (p. 129).
- Desirable properties the authors list: (1) maximum similarity when a document is compared with itself; (2) minimum similarity when two documents share no words (orthogonal vectors); (3) similarity rises as more of the same words are used; (4) possibly symmetry (p. 129).
- Inner product:
$$\mathbf a\cdot\mathbf b=\mathbf a^{T}\mathbf b \tag{7.1.1}$$
$$=a_1b_1+a_2b_2+\dots \tag{7.1.2}$$
- The inner product is the projection of a onto b times the length of b, and it is symmetric (p. 129). Because word counts are nonnegative, the more nonzero terms two vectors share, the larger it is (p. 130).
- For a 0/1 dichotomized matrix, it counts the words two documents share (p. 129–130).
- Federalist example with the three-word vocabulary: Hamilton $=(859,102,374)$, Madison $=(474,17,7)$, Disputed $=(15,2,0)$ (p. 130).
$$\mathbf W_{\text{Hamilton}}\cdot\mathbf W_{\text{Disputed}}=859\times15+102\times2+374\times0=13089 \tag{7.1.3–7.1.5}$$
- Madison: $474\cdot15+17\cdot2+7\cdot0=7144$. The similarity to Madison appears lower, but the authors call this an artifact of how many more essays are attributed to Hamilton (p. 130).
- Magnitude (footnote 1: the vector's length; "length" is avoided because it suggests word count) is $\|\mathbf a\|=\sqrt{\mathbf a\cdot\mathbf a}$. Hamilton: $\sqrt{859^2+102^2+374^2}=942.42$. Madison: 474.36 (p. 130).
- Cosine similarity, the inner product of the normalized vectors, equals the cosine of the angle $\theta$ (p. 130):
$$\text{cosine similarity}(\mathbf a,\mathbf b)=\cos\theta=\frac{\mathbf a\cdot\mathbf b}{\|\mathbf a\|\,\|\mathbf b\|}=\frac{\sum_i a_ib_i}{\sqrt{\sum_i a_i^2}\sqrt{\sum_i b_i^2}} \tag{7.1.6–7.1.9}$$
- The angle is unchanged if a vector is extended in its own direction. In Figure 7.1, document 1 is at (1,4), document 2 at (2,1), and document 3 at (4,2). Documents 2 and 3 have the same word ratio but different magnitudes. Their inner products with document 1 differ, but their cosine similarities are the same (p. 131–132).
- Cosine lies formally in $[-1,1]$. With nonnegative counts it is in $[0,1]$: 0 is most different and 1 most similar (p. 131).
- Federalist result: cosine(Hamilton, Disputed) $=.918$; cosine(Madison, Disputed) $=.995$. Disputed is now much closer to Madison, because normalizing removes the advantage Hamilton's larger vector gave him (p. 132).

*Intuition note:* The inner product rewards big documents. Cosine asks only whether two documents use words in the same proportions. That is why it can reverse the inner-product ranking.

**7.2 Distance metrics (p. 133–134).**
- Euclidean distance (p. 133):
$$\|\mathbf W_i-\mathbf W_{i'}\|=\sqrt{\sum_{j=1}^{J}(W_{ij}-W_{i'j})^2} \tag{7.2.1}$$
- It is very sensitive to document magnitude, like the inner product (p. 133).
- For vectors normalized to magnitude 1 (root and square signs are lost in the text layer; the squared form is reconstructed here as an added step), the steps of (7.2.2–7.2.4) read:
$$\|\mathbf W_i-\mathbf W_{i'}\|^2=\|\mathbf W_i\|^2+\|\mathbf W_{i'}\|^2-2\,\mathbf W_i\cdot\mathbf W_{i'}=1+1-2\,\mathbf W_i\cdot\mathbf W_{i'}=2\bigl(1-\text{cosine similarity}\bigr)$$
- Cosine distance is 1 minus cosine similarity, so larger values mean more dissimilar documents (p. 133).
- Minkowski family (p. 133):
$$d_p(\mathbf W_i,\mathbf W_{i'})=\Bigl(\sum_{j=1}^{J}|W_{ij}-W_{i'j}|^{p}\Bigr)^{1/p} \tag{7.2.5}$$
- $p=2$ is Euclidean. As $p$ grows, the words with the largest count differences contribute more. $p=\infty$ is Chebyshev's metric, the largest absolute difference on any single feature (p. 133).
- $p=1$ is Manhattan ("taxi cab") distance, which measures travel at right angles. It will tend to be more robust to large differences in individual word counts (p. 133–134).
- The choice of metric encodes an assumption about which differences matter. Swapping metrics can substantially change algorithmic methods, and many clustering methods let the user set the metric (p. 134).

**7.3 tf-idf weighting (p. 135–137).**
- Reweighting words can make distances more informative. Removing words entirely is an extreme form of weighting, equivalent to giving them weight 0; the authors removed stop words in earlier analyses and, in the Federalist analysis, took the opposite approach of keeping only stop words and removing everything else (p. 135).
- Claim attributed to the computational linguistics literature: the most informative words are in a "goldilocks region", neither too rare nor too frequent. Very frequent words are the "glue" of language. Rare words might contain useful information but appear too infrequently to support generalizations (p. 135).
- Most common form of tf-idf, where the log term is the penalty for frequent words (p. 135):
$$W_{ij}^{\text{tf-idf}}=W_{ij}\times\log\frac{N}{n_j}$$
$N$ is the number of documents; $n_j$ is the number of documents containing word $j$.
- Federalist application: the matrix uses stop words and common words identified by Mosteller and Wallace (1963) (footnote 2). Word clouds of raw counts (Fig. 7.2) are dominated by stop words and do not reveal the authors (p. 135–136).
- Weighted by tf-idf (Fig. 7.3), Madison's papers over-use words such as *consequently*, *whilst*, *ought*. Hamilton's over-use *upon*, *his*, *him*. Paper #49 most resembles Madison, with *consequently*, *whilst*, *ought* (p. 136–137).
- Cosine similarity with paper #49 (p. 137):

| | Madison | Hamilton |
|---|---|---|
| Raw counts | 0.9899 | 0.9848 |
| tf-idf | 0.5545 | 0.4981 |

- tf-idf weighting is most important for distance/similarity calculations and methods built on them, rather than methods like linear regression. Regression on the document-feature matrix would be invariant to a linear feature-level rescaling, so the tf-idf weights won't matter there (p. 137).

*Intuition note:* Raw-count word clouds are overwhelmed by the most common stop words such as "the" and "of", and the raw cosines for Madison and Hamilton differ only slightly (.9899 vs .9848). tf-idf shrinks those words, so the remaining differences count for more when similarity is computed.

**7.4 Conclusion (p. 138).**
- The goal of these choices is to amplify the signal of interest for later discovery and measurement methods. String kernels can preserve word order (Spirling 2012) (p. 138).
- Many probability models imply a distance. Cosine similarity is closely related to the von Mises–Fisher distribution, and more generally many distributions connect to distance metrics (Banerjee et al. 2005). Chapter 12 returns to this (p. 138).
- Strength: these methods need no knowledge of word meaning, so they work across languages and other count data. Weakness: they can miss similarity between documents that use different words for the same idea. The next chapter turns to word embeddings, which use large external corpora and can assess similarity in a way that smooths across words (p. 138).

## Toy example (ours)
Vocabulary of 3 words. Query $q=(1,1,0)$, document $A=(3,3,0)$ (same direction, longer), document $D=(10,0,0)$.
- Inner products: $q\cdot A=3+3=6$; $q\cdot D=10$. The inner product ranks $D$ higher.
- Magnitudes: $\|q\|=\sqrt2=1.4142$; $\|A\|=\sqrt{18}=4.2426$; $\|D\|=10$.
- Cosines: $\cos(q,A)=6/(1.4142\times4.2426)=6/6=1$; $\cos(q,D)=10/(1.4142\times10)=0.7071$. Cosine ranks $A$ higher, because its proportions match $q$.
- Check of (7.2.4): normalized $q=(0.7071,0.7071,0)$, normalized $D=(1,0,0)$. Squared distance $=(0.2929)^2+(0.7071)^2=0.0858+0.5=0.5858$. And $2(1-0.7071)=0.5858$. ✓
- tf-idf: with $N=4$ documents, a word in all 4 gets factor $\log(4/4)=0$. A word in 1 document gets $\log 4=1.386$ (natural log, our choice; the text gives no base).

## Concepts
- [[vector-space-model]] (new) — documents as vectors of (weighted) word counts; closeness judged by linear-algebra measures (p. 127)
- [[inner-product]] (new) — sum of element-wise products; sensitive to vector magnitude (p. 129)
- [[cosine-similarity]] (new) — inner product of magnitude-normalized vectors; depends only on direction (p. 130)
- [[distance-metrics]] (new) — Euclidean, Minkowski (p = 1, 2, ∞), cosine distance: different notions of document difference (p. 133)
- [[tf-idf]] (new) — count times log(N/n_j); up-weights words frequent in a document but rare in the corpus (p. 135)
- [[text-as-data-validation]] — here: no metric is correct in general; fit to task decides (p. 129)

## Canonical instances
- [[federalist-papers-authorship]] (new) — disputed paper #49 compared with Hamilton and Madison under inner product, cosine, and tf-idf (p. 130–137)

## Bridges (candidates)
- [same-math] cosine similarity ↔ geometry: cosine of the angle between vectors; for unit vectors, squared Euclidean distance $=2(1-\cos)$ (p. 133).
- [structural-analogy] vector-space distances ↔ probability models: both compare documents. Cosine is related to the von Mises–Fisher distribution (p. 138).
- [metaphor] tf-idf down-weighting of ubiquitous words ↔ rational ignorance/cues: common features carry little discriminating information (our loose analogy; not in the text).

## Questions this raises
- When would a researcher prefer subject-matter similarity (retrieval-style) over similarity in sentiment or style? How would the metric then change?
- With tf-idf, cosine similarities fell from about .99 to about .5. Do absolute values matter, or only the Madison–Hamilton gap?
- How does a metric's choice change the clusters found in Chapter 12?
- Can embeddings (Chapter 8) recover similarity between documents using different words?

## Reading notes
- Printed page = pdf page (offset 0).
- The text layer garbles all equations. Equations 7.1.7–7.1.9 and 7.2.1–7.2.5 lose square-root signs, norm bars and absolute-value bars in the text layer, and the tf-idf formula loses its fraction layout. The roots, norms and squares shown above are reconstructed from context (marked as added step where relevant). The source's Figure 7.1 caption says "documents 1 and 2 and documents 2 and 3" have different inner products; the digest reads this as documents 1–2 versus 1–3 (6 vs 12, our check).
- The Hamilton magnitude is split by a line break on the page ("= 9" / "42.42"); it is read as 942.42, which matches $\sqrt{888161}$ (our check).
- The three-word cosines (.918, .995) and the stop-word-matrix cosines (.9899, .9848) come from different feature sets. Do not compare them.
- Typos in source: "closet" (closest), "Hamiliton". Table 6.1 (source of the vectors) is not in this unit.
- Figure 7.1's caption is split across pages 131–132.
- Figures 7.2–7.3 (word clouds) are not transcribed here; the words named in L3 are only those listed in the author's text (p. 136–137).
