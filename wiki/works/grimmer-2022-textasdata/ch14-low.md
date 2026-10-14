---
id: grimmer-2022-textasdata/ch14-low
work: grimmer-2022-textasdata
unit: Chapter 14. Low-Dimensional Document Embeddings
pages: 260-272
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Low-Dimensional Document Embeddings

## L0 — One line
PCA and classical MDS place each document in a space of usually one to three dimensions that approximates the high-dimensional text data, and with Euclidean distance the two methods give the same embedding.

## L1 — The gist (≤ 120 words)
How can we organise documents by placing them on a few continuous dimensions, instead of in clusters or topic mixtures? Principal Component Analysis (PCA) approximates each centered word-count vector with a few weighted components, which are eigenvectors of $W'W$. Classical multidimensional scaling (MDS) instead preserves distances between documents. With Euclidean distance, MDS equals PCA. In the Senate example, a cosine-based distance gave a different but still similar map. The number of dimensions cannot be settled by fit alone, and the dimensions must be interpreted by reading words and documents. Applied to 2005 Senate press releases, the first component separates credit claiming from position taking. The authors stress that the researcher, not the algorithm, does the discovering.

**Prerequisites:** vectors and matrices; eigenvectors and eigenvalues; variance and covariance; Euclidean distance; the bag-of-words matrix; regression.

## L2 — Key ideas
- Embedding (also called scaling) puts documents in a space of usually 1–3 dimensions, which suits visualisation. The goal is underspecified, so "good" is ambiguous (p. 260).
- PCA writes each centered document vector as a score-weighted sum of $K$ components plus error, and minimises mean squared error (p. 261).
- The optimal components are the top-$K$ eigenvectors of $W'W$. Minimising error is equivalent to maximising the variance of the scores (pp. 261–262).
- Components are labelled by their extreme words, by regression of scores on metadata such as DW-Nominate, and by close reading. Low correlations can arise from measurement error (pp. 262–263).
- In the Senate example, the first component captures credit claiming versus position taking, with no apparent natural partisan ordering (pp. 263–264).
- PCA is greedy, so in-sample fit cannot choose $K$. The elbow of the variance-explained plot helps but is rarely clear, and the right $K$ depends on the goals of the analysis (pp. 264–267).
- Classical MDS approximates a distance matrix. With Euclidean distance it equals PCA, but other metrics change the result. Both methods give only relative positions (pp. 268–270).
- Sammon MDS weights close pairs more, at the cost of gradient descent. Landmark MDS and manifold methods are other extensions (p. 269).

## L3 — Walkthrough

### Chapter introduction (p. 260)
Earlier Discovery methods gave partitions (clusters) and admixtures (topic proportions). Embedding is a third approach. Its latent space is customarily much lower-dimensional than in clustering or topic models. The authors treat two workhorses, PCA and classical MDS, then discuss other discovery approaches.

### 14.1 Principal Component Analysis (pp. 261–262)
**Setup.** Use the *centered bag of words*: subtract each word's column average from its counts. A value of 2 then means two uses above the average rate (p. 261). Write the centered document vector as $W_{i,}=(W_{i1},\dots,W_{iJ})$. The matrix $W$ stacks these ($N\times J$). There are $K$ principal components, each a $J\times1$ vector $\mu_k$ giving word-use rates. Each document $i$ has a $K\times1$ score vector $\pi_i$. The approximation is

$$W_{i,}=\underbrace{\pi_{i1}\mu_1+\pi_{i2}\mu_2+\dots+\pi_{iK}\mu_K}_{\hat W_{i,}}+\underbrace{\epsilon_i}_{\text{error}}\tag{14.1.1}$$

Here $\epsilon_i$ is a $J\times1$ error vector. Scores stretch, shrink or flip the components. Since $K<J$, some error is unavoidable (p. 261).

**Estimation.** Choose $\pi,\mu$ to minimise

$$f(\pi,\mu)=\frac1N\sum_{i=1}^N\epsilon_i'\epsilon_i=\frac1N\sum_{i=1}^N\Big(W_{i,}-\sum_{k=1}^K\pi_{ik}\mu_k\Big)'\Big(W_{i,}-\sum_{k=1}^K\pi_{ik}\mu_k\Big)\tag{14.1.2}$$

The optimal solution uses the $K$ eigenvectors with the largest $K$ eigenvalues of $W'W$ (the empirical variance-covariance matrix, $J\times J$) as components. The score is $\pi_{ik}=\mu_k'W_{i,}$ (p. 261).

Why the largest eigenvalues? A matrix is better approximated by first taking the components with the largest eigenvalues. Alternatively, deriving PCA shows that minimising error is equivalent to maximising the variance of the scores (p. 262).

*Intuition note:* Each document is squeezed to $K$ numbers, its position along $K$ word-pattern directions. The directions are chosen so that documents differ as much as possible along them, which loses the least information.

**Interpretation is still needed** for discovery: label components and scores, using automated and manual methods (p. 262).

### 14.1.1 Automated labelling (pp. 262–263)
- Look at the (say) ten most positive and ten most negative entries of $\mu_k$. Since $\pi_{ik}=W_{i,}'\mu_k$, large entries most strongly influence where a document falls (p. 262).
- Regress scores on metadata about the author or document. This is especially useful for ideology. For example, regress text scores on DW-Nominate, the roll-call-based low-dimensional measure of ideology in the US Congress (p. 263).
- **Caution:** low correlations can arise even if two latent concepts are related, because measurement error dampens correlations (p. 263).

### 14.1.2 Manual labelling (p. 263)
Read documents sampled at similar points of the spectrum. One option is the far ends. Another is random sampling along the spectrum, weighting the endpoints more. Then label the ends and describe how documents vary between them. Reading also helps refine the conceptualisation (p. 263).

### 14.1.3 Senate press releases (pp. 263–264)
- Data: all Senate press releases of 2005 (from Grimmer 2010). There is one normalised count vector of length 2796 for each of the 100 senators (p. 263).
- Figure 14.1 (left) orders senators by first-component score, coloured by party. There does not appear to be a natural partisan ordering, and there is a great deal of overlap between the parties. This does not make the PCA worthless (p. 263).
- Figure 14.1 (right) shows that the first component captures the trade-off between position taking and credit claiming (Grimmer 2013b). PCA found systematic behavioural differences that were not easy to anticipate (p. 264).
- Highest-valued words: depart, grant, program, fund, firefight, million, award (credit claiming). Lowest-valued words: american, court, judg, time, congress, justic, iraq (policy making or position taking) (p. 264).

*Intuition note:* The axis does not line up with party in any natural ordering. It is about credit claiming (bringing money home) versus position taking (taking stands). The method found a systematic dimension that was not easy to anticipate beforehand.

### 14.1.4 Choosing the number of components (pp. 264–267)
- PCA is *greedy*: each added component improves the approximation. In-sample fit is therefore trivially best when components equal vocabulary size, which tells us nothing (p. 264).
- The remaining error equals the sum of the excluded eigenvalues, so eigenvalue sizes can guide the choice (p. 265).
- Figure 14.2 shows ostensibly five-dimensional data in which only two dimensions have variance and three are small noise. Two eigenvalues are large and three are small. The first two explain almost all variance (pp. 265–266).
- The usual advice is to find the "elbow" of the variance-explained plot, where more components stop adding explained variance (p. 266).
- **Caution:** Figure 14.2 is stylised. In real applications such plots "will almost never look so clear" (p. 266).
- Alternatively, keep adding dimensions while they give new explanatory power, and check qualitatively how documents load. Substantive interpretation is essential (p. 266).
- Fit statistics measure variance explained and cannot reveal a "true" number of dimensions. The right number depends on tolerance for error. If PCA feeds a prediction task, the prediction objective can fix the number (p. 267).

### 14.2 Classical MDS (pp. 268–269)
Classical MDS also approximates documents in low dimensions, and under specific assumptions gives the same answer as PCA (p. 268). Let $Q$ be the $N\times N$ matrix of Euclidean distances $q_{ii'}$ between documents (defined in Ch. 7). Find an $N\times K$ matrix $\pi$ whose rows preserve those distances. The objective compares $q_{ii'}$ with the distance in the latent space (as printed; exact rendering, see Reading notes):

$$f(Q,\mu)=\sum_{i=1}^N\sum_{i'<i}\Big(q_{ii'}-\sum_{k=1}^K(\pi_{ik}-\pi_{i'k})^2\Big)^2$$

Solution: double-center $Q$ (subtract row means and column means), then divide by $-2$. This gives the $N\times N$ matrix $WW'$. Approximate it with the first $K$ eigenvectors. The embedding is $\hat W_{i,}=(\lambda_1\pi_{i1},\lambda_2\pi_{i2},\dots,\lambda_K\pi_{iK})$, with $\lambda_k$ the $k$th eigenvalue (as printed). A full derivation is in Hastie, Tibshirani and Friedman (p. 268).

**Caveats.**
- The structure depends strongly on the distance metric, so changing the definition of "close" changes the structure found (p. 268).
- PCA preserves the correlation structure and MDS only the distances. Both give only *relative* positions (pp. 268–269).

### 14.2.1 Extensions (p. 269)
- Classical MDS favours embeddings that get large distances right. Researchers often care more about neighbourhoods around a document, and may tolerate more error for distant pairs (p. 269).
- **Sammon MDS** divides each pair's squared discrepancy by $q_{ii'}$:

$$f(Q,\pi)=\frac{1}{\sum_{i=1}^N\sum_{i'<i}q_{ii'}}\sum_{i=1}^N\sum_{i'<i}\frac{\Big(q_{ii'}-\sum_{k=1}^K(\pi_{ik}-\pi_{i'k})^2\Big)^2}{q_{ii'}}$$

  Discrepancies are magnified when $q_{ii'}$ is small. Optimisation needs gradient descent, not simple linear algebra (p. 269).
- Landmark MDS embeds representative points first, then the rest around them (Platt 2005). Manifold methods seek a locally Euclidean but more complicated structure (Roweis and Saul 2000) (p. 269).

*Intuition note:* Dividing by $q_{ii'}$ makes mistakes about nearby documents cost more than the same-sized mistakes about distant ones.

### 14.2.2 MDS on Senate press releases (p. 270)
Figure 14.3 (left): Euclidean-distance classical MDS and PCA give exactly equal embeddings, so Euclidean MDS is equivalent to PCA. Right: with distance $1-$cosine similarity, MDS gives a different but still similar embedding (p. 270).

### 14.3 Conclusion (pp. 271–272)
- Embeddings help visualisation (two or at most three dimensions) and can be helpful when we believe there are one or two very strong dimensions that explain most of the data, "as ideology does for vote counts" (p. 271).
- Discovery covered four approaches: discriminating words, clustering, topic models and embeddings. They help analysts see the texts anew: "it isn't the algorithm doing the discovering, it is the researchers" (p. 271).
- Other fields' methods can be borrowed. Word co-occurrence can be treated as a weighted undirected network, with words as nodes. Rule, Cointet and Bearman (2015) use community detection on State of the Union addresses from 1790 to 2014. This resembles clustering but groups terms, not documents (p. 271).
- Bail (2016) builds a network of autism-advocacy organisations, with edges weighted by overlapping nouns and noun phrases. He hypothesises that organisations bridging disparate themes reach new audiences more easily, and measures bridging by betweenness centrality. He finds that high bridgers get two and a half times as many comments from new social media users (pp. 271–272).
- Next comes Measurement, using supervised learning. Chapter 21 returns to using these techniques for measurement (p. 272).

## Toy example (ours, not from the text)
Three documents, two words, with centered counts: $W_1=(1,1)$, $W_2=(-1,-1)$, $W_3=(0,0)$. Each column sums to 0, so they are centered. (Raw counts $(4,4),(2,2),(3,3)$ with column means 3 would give these.)

**PCA.** $W'W=\begin{pmatrix}1+1+0&1+1+0\\1+1+0&1+1+0\end{pmatrix}=\begin{pmatrix}2&2\\2&2\end{pmatrix}$. Its eigenvalues are 4 and 0 (trace 4, determinant $4-4=0$). The eigenvector for 4 is $\mu_1=(1,1)/\sqrt2\approx(0.707,0.707)$. Scores $\pi_{i1}=\mu_1'W_{i,}$ are:
- doc 1: $2/\sqrt2\approx1.414$
- doc 2: $-1.414$
- doc 3: $0$

With $K=1$, $\hat W_1=1.414\times(0.707,0.707)=(1,1)$, which is exact. The excluded eigenvalue is 0, matching zero remaining error (p. 265).

**MDS.** Euclidean distances are $q_{12}=\sqrt{4+4}=2.828$ and $q_{13}=q_{23}=\sqrt2=1.414$. The PCA positions $1.414,-1.414,0$ have gaps of $2.828$, $1.414$ and $1.414$. The distances are preserved, as the PCA = Euclidean-MDS equivalence says. Shifting or flipping the axis would preserve them equally well, which is why positions are only relative (p. 269).

## Concepts
- [[principal-component-analysis]] (new) — approximate centered document vectors by $K$ eigenvector components with scores; minimises squared error (p. 261)
- [[document-embedding]] (new) — placing documents in a 1–3-dimensional space, also called scaling (p. 260)
- [[centered-bag-of-words]] (new) — word counts minus each word's average count over documents (p. 261)
- [[classical-mds]] (new) — embedding that preserves a Euclidean distance matrix; equals PCA for Euclidean distance (pp. 268, 270)
- [[sammon-mds]] (new) — MDS whose loss divides by $q_{ii'}$ to favour small distances; needs gradient descent (p. 269)
- [[elbow-plot]] (new) — variance-explained plot used heuristically to pick the number of components (p. 266)
- [[text-as-data-validation]] — here: regress component scores on external measures such as DW-Nominate, noting that measurement error lowers correlations (p. 263)

## Canonical instances
- [[senate-press-releases-pca-2005]] (new) — first PC separates credit claiming from position taking; no apparent natural partisan ordering (pp. 263–264)
- [[bail-2016-cultural-bridging]] (new) — network betweenness of advocacy organisations predicts attention from new users (pp. 271–272)
- [[rule-cointet-bearman-2015]] (new) — community detection on a word network of State of the Union addresses (p. 271)

## Bridges (candidates)
- [same-math] Classical MDS with Euclidean distance ↔ PCA: the same eigen-decomposition gives the same embedding (p. 270).
- [structural-analogy] Choosing $K$ by elbow ↔ choosing the number of clusters or topics: in-sample fit cannot decide it.
- [structural-analogy] Text scores regressed on DW-Nominate ↔ ideal-point scaling from roll calls, both measuring ideology on a low-dimensional scale.
- [metaphor] Network "cultural bridging" ↔ structural holes in social networks.

## Questions this raises
- When is Sammon or manifold MDS preferable to PCA, given that fit statistics cannot choose between them?
- How should one decide whether a low correlation with DW-Nominate means "different concept" or "noisy measurement"?
- Why does the MDS embedding depend on the distance metric, and how could one choose a metric in a principled way?
- Is the second principal component in the Senate data interpretable, or only the first?

## Reading notes
- Printed page numbers equal pdf numbers (260–272). The extracted equations were garbled, so I checked them against the page images.
- The classical MDS objective is badly rendered in the image. I give the reading "(q minus sum of squared coordinate differences) squared". The image shows no square root, although $q_{ii'}$ is a Euclidean distance. The objective is written $f(Q,\mu)$ but minimised over $\pi$. The Sammon formula has the same grouping, so I read it the same way.
- The embedding $\hat W_{i,}=(\lambda_k\pi_{ik})$ is reproduced as printed. The text does not explain the scaling by $\lambda_k$.
- Section 14.2.2 cites "Section 14.1.4" for the Senate PCA, but that example is in 14.1.3. This is a cross-reference error in the source.
- The text speaks of "the empirical variance-covariance matrix" $W'W$ without dividing by $N$.
- Figures 14.1–14.3 are cited only through the authors' descriptions. The senator labels in Figure 14.1 overlap and are hard to read.
- The chapter has no exercises.
