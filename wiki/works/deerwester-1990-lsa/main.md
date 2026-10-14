---
id: deerwester-1990-lsa/main
work: deerwester-1990-lsa
unit: paper
pages: "pdf 1–34 (manuscript pages 1–30 plus contents and lists; see Reading notes)"
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Indexing by Latent Semantic Analysis (Deerwester, Dumais, Furnas, Landauer, Harshman)

## L0 — One line
Replace raw words by about 100 factors from a truncated singular-value decomposition of the term-by-document matrix, so that terms, documents and queries share one space where cosine measures similarity, and relevant documents can be found even when they share no words with the query.

## L1 — The gist (≤ 120 words)
Word-matching retrieval fails because people use many words for one idea (synonymy) and one word for many ideas (polysemy). The authors assume a latent semantic structure partly hidden by random word choice. They estimate it by a truncated SVD of the term-by-document matrix, with about 100 dimensions. A query becomes a pseudo-document at the centroid of its term vectors, and documents are ranked by cosine. On the MED collection this beats term matching and SMART (a standard retrieval system). On CISI it is no better than term matching, and SMART is better. The authors call the results "modestly encouraging", and say LSI gives only a partial answer to polysemy.

**Prerequisites:** matrix products and transposes; orthonormal columns ($T'T=I$); diagonal matrices; dot product and cosine; rank; the idea of eigenvectors.

## L2 — Key ideas
- Retrieval by literal term overlap misses relevant documents (synonymy, hurts recall) and returns irrelevant ones (polysemy, hurts precision). The authors treat this as a statistical problem about latent structure (pdf 2–3).
- Choosing a model: the authors want adjustable richness, explicit representation of both terms and documents, and tractable computation. Only two-mode factor analysis, i.e. SVD, meets all three (pdf 6–7).
- Truncated SVD $X \approx \hat X = TSD'$ keeps the $k$ largest singular values. $\hat X$ is the best rank-$k$ least-squares fit. It is deliberately not a perfect reconstruction, because the original counts are considered unreliable (pdf 13, 9).
- Term–term, document–document and term–document comparisons come from $TS^2T'$, $DS^2D'$ and $TSD'$. Within comparisons use rows of $TS$ or $DS$. The between comparison uses rows of $TS^{1/2}$ and $DS^{1/2}$ (pdf 15).
- A query or new document is folded in as $D_q = X_q' T S^{-1}$, which is the centroid of its term points up to scaling. This gives a ranking by cosine without recomputing the SVD (pdf 16).
- The choice of $k$ is by the operational criterion of best retrieval performance. Solutions are nested (pdf 14, 18–19).
- Results: MED average precision .51 vs .45 for term matching. CISI: LSI .11 = term matching, SMART .14. The authors suspect MED may be an unrepresentatively well-segmented collection (pdf 18–21).
- Limits: each term is one point, so polysemy is only partly solved. Retrieval needs an exhaustive comparison against all document vectors. Updating is unresolved (pdf 22–23).

## L3 — Walkthrough

All page references are to PDF pages (manuscript page = pdf − 1; see Reading notes). Figures 1, 4, 5 and 6 appear only as placeholders in this copy.

### 1. Introduction (pdf 2)
- Users want documents by conceptual content, but words are unreliable evidence of it. There are many ways to express a concept, and most words have several meanings (pdf 2).
- **Assumption:** there is an underlying *latent semantic structure* that is partly hidden by the randomness of word choice. Statistical techniques estimate it and discard the "noise" (pdf 2).
- The method, "latent semantic indexing" (LSI), uses SVD on a large term-by-document matrix. It builds a "semantic" space where associated terms and documents lie close together (pdf 2).
- A term that does not occur in a document can still end up near it, if this fits the major association patterns. A query identifies a point in the space, and nearby documents are returned (pdf 2).
- Footnote 1: "semantic structure" here means only the correlation structure of how words appear in documents (pdf 2).

### 2. Deficiencies of current methods (pdf 2–3)
- **Synonymy:** many ways to refer to the same object. Two people choose the same main key word for a well-known object less than 20% of the time. Similarly poor agreement is reported for indexers and searchers. Synonymy tends to lower *recall* (pdf 2).
- **Polysemy:** one term with several meanings (example "chip"). It is one factor behind poor *precision* (pdf 2–3).
- The authors trace the failure of automatic indexing "largely" to three factors (pdf 3):
  1. Index terms are incomplete. They typically cover only a fraction of the terms users will search under. Thesaurus or term expansion is presumably advantageous for conscientious searchers, but fully automatic expansion may add terms with unintended meanings, degrading precision rapidly.
  2. There is no adequate automatic handling of polysemy. Controlled vocabularies with human intermediaries are expensive and not necessarily effective. Boolean intersection with disambiguating terms is hampered by users' inability to think of such terms.
  3. Each word type is treated as independent, so matching two terms that almost always co-occur counts as much as matching two rarely co-occurring terms. Redundancy is ignored, and results may be distorted to an unknown degree.
- Small interactive databases showed monotonic recall gains from adding more indexing terms, without overall precision loss. Whether this "unlimited aliasing" works in very large databases is undetermined (pdf 3).

### 3. Rationale (pdf 3–7)
**3.1 Illustration (Table 1, pdf 3–5).** A fictional matrix has 3 documents and 8 terms (access, document, retrieval, information, theory, database, indexing, computer).
- Doc 1 has access, document, retrieval, database, indexing. Doc 2 has information, theory, computer. Doc 3 has retrieval, information, computer.
- Query: "IDF in computer-based information look-up". Docs 1 and 3 are relevant (REL = R). Docs 2 and 3 match on *information* and *computer* (MATCH = M).
- Doc 1 is relevant but shares no query word, so term overlap misses it. Doc 2 is non-relevant but shares terms, so it is returned. No meaning-conditioning term of the query is in the index, so Boolean intersection would not exclude Doc 2 (pdf 4).
- Viewpoint: a document or query is a small, fallible sample of the discourse that might have been written on its topic. The task is to predict which terms "really" apply (the latent semantics) from this sample (pdf 4).
- If terms were uncorrelated, nothing could be corrected. If word patterns are structured, data from one part of the table can correct other parts. Example: if "access" and "retrieval" each occur in 100 documents and 95 of the "access" documents contain "retrieval", a missing "retrieval" in an "access" document may be an error (pdf 4).
- Such structure goes beyond simple pairwise correlation. An analysis might down-weight a polysemous term. Here "information" in Doc 2 is something of an "imposter" given its other terms (pdf 5).
- The aim is to replace sets of unreliable terms by entities that are more reliable indicants, using higher-order (latent) structure (pdf 5).

> **Intuition note:** A document's words are one noisy draw from what could have been said. If words come in patterns, the pattern lets us guess missing or misleading words.

**3.2 Choice of method (pdf 5–7).**
- The authors restrict themselves to *proximity models* (similar items placed near each other): clusterings, trees, factor-analytic and multidimensional distance models (pdf 5).
- Earlier work used hierarchical clustering, latent class analysis and factor analysis (pdf 5).
- **Clustering:** the authors "believe" hierarchies are too limited. They allow no cross-classification and have essentially only $n$ parameters for $n$ objects. Clustering improves search efficiency, but whether it improves retrieval success is unclear (pdf 5).
- **Factor analysis:** a $k$-dimensional model for $n$ points has $nk$ parameters (pdf 6). Earlier attempts had three shortcomings: they were computationally expensive (done 15–20 years earlier), they were restricted (very low dimensionality or conversion to binary clusters), and some needed thousands of human similarity judgments (pdf 6).
- Earlier approaches also represented only one entity type, terms or documents. Koll's proposal represents both, but with only seven hand-chosen, not truly orthogonal dimensions (pdf 6, footnote 2).
- This approach differs in four ways (pdf 6):
  1. It handles problems of reasonable size: 1000–2000 abstracts and 5000–7000 terms.
  2. It uses about 100 dimensions, which "appears necessary" for success.
  3. It represents terms and documents in the same space.
  4. It retrieves directly from query terms, without rotating or interpreting axes and without intermediate clusters.
- **Three criteria** for choosing a model (pdf 6–7):
  1. *Adjustable representational richness.* Dimensional models offer a controllable number $k$ of dimensions, i.e. $k$ parameters per object.
  2. *Explicit representation of both terms and documents.* A query can then be placed at the centroid of its term points. This needs "two-mode" methods that start from a rectangular matrix. Candidates are multidimensional unfolding (similarity via Euclidean distance), two-mode factor analysis (similarity via inner product) and unfolding in trees (path length). It also allows "folding in" new terms (at the centroid of their documents) and new documents (at the centroid of their terms).
  3. *Computational tractability.* Many models need computation growing as $N^4$ or $N^5$, with $N$ = terms plus documents.
- Only two-mode factor analysis met all three. Tree unfolding was too restrictive, and it and non-metric unfolding were too expensive. A program (PARAFAC) fit the SVD model in time of order $N^2 \times k^3$ (pdf 7).
- Footnote 3 (open issues on folding in): where a new object lands depends on what is already in the space. Folded-in objects give a somewhat different space than a full re-analysis. How much can be done without rescaling is an open research issue (pdf 7).

### 4. SVD or two-mode factor analysis (pdf 8–16)
**4.1 Overview (pdf 8–11).**
- One-mode factor analysis starts from a square symmetric matrix of associations between objects of one type. Eigen-analysis splits it into linearly independent factors. Small ones may be ignored (pdf 8).
- Two-mode factor analysis starts from an arbitrary rectangular matrix (terms × documents). SVD splits it into three special matrices. Small components may be dropped. Then term–term, document–document and term–document similarity are approximated on fewer dimensions, and dot product or cosine corresponds to estimated similarity (pdf 8).
- Dimension reduction can map documents with somewhat different term-usage profiles to the same factor vector. This is the improvement of unreliable data that is needed. SVD, the authors say, can help to solve all three of the problems described earlier (pdf 8).
- They used 50–100 factors, "roughly speaking" artificial concepts: extracted common meaning components. The $N$ terms are replaced by $k<N$ surrogates. No attempt is made to interpret or rotate the factors (pdf 8–9).
- The reduced space must not reconstruct the original term space perfectly, because the original is believed unreliable (pdf 9).
- They do not seek very low dimensionality (2–3), since they do not want visualisation. They believe conceptual space needs more than a handful of dimensions, and that a Euclidean space is at most a useful approximation of the real structure. Extra dimensions let different regions serve different parts of the language (pdf 9).
- "Works best" means best retrieval effectiveness, not the most variance reproduced (pdf 9).
- **Query processing:** each term and document is a $k$-vector. A query is a weighted sum of its term vectors (a pseudo-document). Documents above a cosine threshold, or the $n$ nearest, are returned. Whether cosine best predicts human relevance judgments is not yet explored (pdf 9).
- **Worked example (Table 2, pdf 10–11).** The documents are nine Bellcore memo titles: five on human-computer interaction (c1–c5) and four on graph theory (m1–m4). The 12 indexed terms are those occurring in more than one title. Entries are frequencies (full matrix repeated in the Appendix). The authors chose the data so that two dimensions would suffice (pdf 11).
- **Query "human computer interaction" (pdf 12).** Term matching returns c1, c2, c4. It misses c3 and c5, which share no terms with the query. In the 2-D space the query is placed at the centroid of "human" and "computer" and scaled. Documents c1–c5, but not m1–m4, lie within a cosine of .9 of the query. This includes c3 and c5.

> **Intuition note:** c3 and c5 never contain "human" or "computer". They sit near the query because they share other words (user, interface, system, response, time) with documents that do contain them. The 2-D space captures these indirect links.

**4.2 Technical details (pdf 12–16).**

*4.2.1 The SVD model (pdf 12–14).* Any $t\times d$ matrix $X$ can be written
$$X = T_0 S_0 D_0' ,$$
with $T_0$ and $D_0$ having orthonormal columns and $S_0$ diagonal. Figure 2 gives the shapes: $T_0$ is $t\times m$, $S_0$ is $m\times m$, $D_0'$ is $m\times d$, where $m\le\min(t,d)$ is the rank of $X$, $T_0'T_0=I$ and $D_0'D_0=I$ (pdf 13).
- $T_0$ and $D_0$ hold the left and right singular vectors, and $S_0$ the singular values. The SVD is unique up to row, column and sign permutations. By convention the diagonal of $S_0$ is positive and in decreasing order (pdf 12–13).
- Footnote 5 on permutations: columns $i,j$ of $S_0$ may be swapped only together with the corresponding rows and the columns $i,j$ of $T_0$ and $D_0$ (pdf 13).
- Footnote 4: $T_0$ holds the eigenvectors of $XX'$, $D_0$ the eigenvectors of $X'X$, and $S_0^2$ is the matrix of eigenvalues in both cases (pdf 13).
- The full factorisation has full-rank matrices. The use of SVD is the simple strategy for an optimal approximate fit: keep the $k$ largest singular values, set the rest to zero. The product $\hat X$ has rank $k$. The authors state without proof that $\hat X$ is the rank-$k$ matrix closest to $X$ in the least-squares sense (pdf 13).
- Deleting the zero rows and columns of $S_0$ and the matching columns of $T_0$ and $D_0$ gives the reduced model
$$X \approx \hat X = TSD' .$$
Shapes (Figure 3): $T$ is $t\times k$, $S$ is $k\times k$, $D'$ is $k\times d$, with $k\le m$ (pdf 14).
- The choice of $k$ is "critical". It should be large enough to fit the real structure and small enough not to fit sampling error. The proper way to choose is an open issue. They use an operational criterion: the $k$ that gives good retrieval performance (pdf 14).

> **Intuition note:** Keeping only the biggest singular values keeps the strongest patterns of word co-use. The dropped small ones are treated as noise. Because the fit is only approximate, a cell that was 0 can come out positive.

*4.2.2 Geometric interpretation (pdf 14).* Rows of the reduced $T$ and $D$ are coordinates of terms and documents in $k$-space. With axes rescaled by quantities related to the diagonal of $S$, dot products compare objects (pdf 14).

*4.2.3 Comparison quantities (pdf 14–15).* These are computed from $T$, $D$, $S$ alone, using $\hat X$ rather than $X$ because $\hat X$ is presumed to carry the reliable patterns.
- **Two terms.** Dot products between rows of $\hat X$ reflect similar occurrence patterns over documents. Since $S$ is diagonal and $D$ has orthonormal columns:
$$\hat X\hat X' = TS^2T' .$$
  Cell $(i,j)$ is the dot product of rows $i$ and $j$ of $TS$. So rows of $TS$ are term coordinates. $TS$ differs from $T$ only by stretching each axis in proportion to the matching diagonal element of $S$ (pdf 15).
- **Two documents.** Dot products between columns of $\hat X$:
$$\hat X'\hat X = DS^2D' ,$$
  so rows of $DS$ are document coordinates (pdf 15).
- **Term and document.** The comparison is a single cell of $\hat X = TSD'$. Cell $(i,j)$ is the dot product of row $i$ of $TS^{1/2}$ and row $j$ of $DS^{1/2}$. Hence no single configuration serves both within and between comparisons. The two differ only by stretching the axes by $S^{1/2}$ (pdf 15).

*4.2.4 Pseudo-documents (pdf 15–16).* A new object (a query, or a document not in the original analysis) comes as a term vector $X_q$. We need $D_q$ usable like a row of $D$. The criterion: inserting a real document $X_i$ should give $D_i$, at least when the model is perfect ($X=\hat X$). The author says "a little algebra" gives
$$D_q = X_q' T S^{-1} .$$
- (added step) If $X=\hat X$, column $i$ of $X$ is $X_i = T S D_i'$ with $D_i$ the $i$-th row of $D$. Then $X_i' T S^{-1} = D_i S T' T S^{-1} = D_i S S^{-1} = D_i$, using $T'T=I$, $S'=S$ and $SS^{-1}=I$.
- With appropriate rescaling this amounts to placing the pseudo-document at the centroid of its term points. $D_q$, scaled by $S^{1/2}$ or $S$, is used like a document's factor vector for between or within comparisons respectively (pdf 16).

*4.2.5 Preprocessing (pdf 16).* The equations ignore reweighting of rows or columns of $X$. This could equalise documents of different length or impose views about important terms. The algebra is not given.

### 5. Tests (pdf 16–21)
**Setup (pdf 16–17).**
- Two standard collections with queries and relevance judgments: MED and CISI. The program was PARAFAC. Documents are title plus abstract.
- Terms occurring in more than one document and not on SMART's 439-word stop list were indexed. There was no stemming. Cells hold raw frequencies. Queries are placed at the centroid of their terms. Documents are ordered by cosine (pdf 16).
- Footnote 6: terms in only one document, or equally frequent in all documents, have little or no influence on the SVD solution. The authors see no reason to omit any terms given greater resources. Omitted terms can be folded in later (pdf 16).
- The method is "impoverished" on purpose: no stemming, phrases, term weighting or Boolean combinations, so that the basic representation is tested (pdf 17).
- **Comparisons:** (1) term matching on the same matrix (cosine between query column and document columns); (2) SMART with stop list, full stemming and raw term frequencies; (3) data from Voorhees, who used a vector system with extended Boolean queries, word-variant mapping and weighting. Precise comparisons with SMART and Voorhees are not possible because indexing differs (pdf 17).
- **Evaluation:** precision at several recall levels, per query, then averaged. For Voorhees only two points (10 or 20 documents returned) exist, from her sequential search condition (pdf 17).

**5.1 MED (pdf 17–19).**
- MED has 1033 documents and 30 queries. Indexing gave 5823 terms (mean 50.1 terms per document, 9.8 per query, 23.2 relevant documents per query). A 100-factor SVD was used (pdf 17–18).
- For all but the two lowest recall levels (.10), LSI precision is well above term matching, SMART and Voorhees. The mean precision difference LSI vs term matching is .06 (.51 vs .45), a 13% improvement. Odds against chance are 29 to 1, $t(29)=2.23$. LSI vs SMART: $t(29)=1.96$, odds 16 to 1 (pdf 18).
- Term matching and SMART do not differ here. The authors find this "somewhat surprising", since SMART's stemming and wider term inclusion should help it (pdf 18).
- LSI does comparatively poorly at lowest recall for two reasons: precision is already good everywhere there, and LSI is designed mainly for synonymy (improving recall) and is less successful on polysemy (precision). Largest gains are expected at high recall, and the authors report that this is what is observed (pdf 18).
- **Dimensionality:** the authors examine several values and pick the best performer. Solutions are nested, so a 10-factor solution uses the first 10 coordinates of the 100-factor solution (footnote 9). Mean precision more than doubles (.25 to .52) from 10 to 100 factors, with a maximum at 100. Performance might improve a bit beyond 100 here. More factors do not necessarily mean better performance. In other small applications there were clearer maxima, which they interpret as extra parameters modelling sampling noise (pdf 19).
- Earlier factor-analytic work used 7 (Koll), 13 (Ossorio) and 21 (Borko & Bernick) dimensions. The authors report a more than 50% improvement beyond this range and "suspect" the earlier limited utility may reflect an impoverished representation (pdf 19).
- **Caveat on MED:** it appears to be the union of thorough keyword-search results for the 30 queries, so it may be unrepresentatively well-segmented. Per-query document sets are probably isolated more than in natural collections. Other methods benefit less from this. Keyword selection may favour surface-matching methods like SMART (pdf 19).
- Footnote 8: Voorhees's reported 39.7 terms per query is suspected to be an error for 9.7 (pdf 18).

**5.2 CISI (pdf 20–21).**
- CISI has 1460 documents and 35 queries. It has been "consistently difficult" for automatic methods. Indexing gave 5135 terms (45.4 per document, 7.7 per query, 49.8 relevant per query). A 100-factor solution was used (pdf 20).
- All methods do poorly, with precision never above .30. Average precision is .11 for both LSI and term matching ($t=1$). SMART is reliably better at .14 ($t(34)=3.66$, odds over 1000 to 1) (pdf 20).
- The authors believe SMART's advantage comes from term selection. Few single-document terms occur in queries, so omitting them is unlikely to matter much. Stemming appears to be the likely source (pdf 20).
- A new LSI analysis on SMART's 5019 terms ("LSI-SMART", 100 factors) gives .14, indistinguishable from SMART ($t<1$). This suggests that much of the original gap came from term selection. LSI did not improve on term matching, or on SMART. Stemming seems to capture structure LSI did not. The authors say that in theory LSA can extract some commonalities among stemmed forms, but in practice there may be insufficient data (pdf 20–21).
- Possible problems with the data: the authors' intuition is that the collection is very homogeneous and many queries seem vague, so relevance judgments may be unreliable. The authors call this mostly conjecture, though some judgments look "in obvious error" (pdf 21).

**5.3 Summary (pdf 21).**
- Results are "modestly encouraging". LSI is superior to term matching in one case and equal in the other. It beats Voorhees on both. It beats SMART in one and equals it in the other (when term selection is matched). It is untested with refinements (weighting, stemming, phrases, negation), and untested on queries designed for it. The authors say "it seems likely" that LSI will offer a more effective method with such improvements (pdf 21).

### 6. Conclusions and discussion (pdf 21–23)
- **Compared with predecessors** (pdf 21–22):
  - Borko and colleagues factor-analysed a term–term correlation matrix. With 260 abstracts and 21 interpretable factors, they used the factor space for classification, not retrieval, using only the loadings of "significant" terms.
  - The authors describe Koll's work as very close in spirit to LSI. The authors argue LSI is not order-dependent and is a mathematically rigorous way to get truly orthogonal axes.
- **Economy and costs** (pdf 22):
  - Each term or document needs on the order of 50–150 values. The authors "guess" a small integer will probably suffice.
  - Retrieval requires exhaustive comparison of the query vector with all stored document vectors, which may detract from the method for very large collections, because search in high-dimensional space is not very efficient on serial computers.
  - The initial SVD is time-consuming. New documents could be placed at the centroid of their terms, and new terms at the centroid of their documents. How much updating is possible without a new decomposition is unknown.
- **Synonymy and polysemy** (pdf 22–23):
  - LSI deals "nicely" with synonymy but offers just a partial answer to polysemy. A word's meaning can be conditioned by query words not used by a document's author.
  - Each term is one point, so a word like "bank" is represented as a weighted average of its meanings. If no real meaning resembles the average, this may seriously distort. Classical term overlap keeps the union of meanings, giving less distortion but more imprecision.
  - The authors have not found a satisfactory way to give one term several points.
- **Status** (pdf 23): LSI should be regarded as a potential *component* of a retrieval system, serving like raw term-vector ranking, with putative advantages of noise reduction and compaction.
  - Weighting, stemming, phrases, similarity measure and Boolean counterparts will need re-evaluation. Stemming's added value is an open question, since LSI already addresses synonyms to some extent. Phrases and disambiguation may matter more, because LSI averages polysemous meanings.

### Appendix — numerical example (pdf 26–28)
The 12 × 9 matrix of Table 2 is decomposed (values rounded to two decimals).
- $S_0 = \mathrm{diag}(3.34, 2.54, 2.35, 1.64, 1.50, 1.31, 0.85, 0.56, 0.36)$ (pdf 27).
- $T_0$ is 12 × 9 and $D_0$ is 9 × 9. Their first two columns are the 2-D coordinates of Figure 1 (pdf 26–27).

| Term | col 1 | col 2 | Term | col 1 | col 2 |
|---|---|---|---|---|---|
| human | .22 | −.11 | EPS | .30 | −.14 |
| interface | .20 | −.07 | survey | .21 | .27 |
| computer | .24 | .04 | trees | .01 | .49 |
| user | .40 | .06 | graph | .04 | .62 |
| system | .64 | −.17 | minors | .03 | .45 |
| response, time | .27 | .11 | | | |

| Doc | col 1 | col 2 | Doc | col 1 | col 2 |
|---|---|---|---|---|---|
| c1 | .20 | −.06 | m1 | .00 | .19 |
| c2 | .61 | .17 | m2 | .01 | .44 |
| c3 | .46 | −.13 | m3 | .02 | .62 |
| c4 | .54 | −.23 | m4 | .08 | .53 |
| c5 | .28 | .11 | | | |

- Keeping $k=2$ gives $\hat X = TSD'$ with $T$ (12×2), $S=\mathrm{diag}(3.34,2.54)$, $D'$ (2×9). The product $\hat X$ is printed in full (pdf 28).
  - Example row "human" of $\hat X$: .16, .40, .38, .47, .18, −.05, −.12, −.16, −.09. The original row was 1, 0, 0, 1, 0, 0, 0, 0, 0.
  - So "human" now has weight .38 in c3 and .18 in c5, where it did not occur.
- The authors note that $\hat X$ does not exactly match $X$ (it gets closer as more singular values are kept). This is wanted, since the authors think some zero entries of $X$ should really be 1, and some non-zero entries should be 0 (pdf 28).

## Toy example (ours, not from the text)
Two terms × two documents: $X=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ (rows $t_1,t_2$; columns $d_1,d_2$).

**SVD.** Take $T=D=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and $S=\mathrm{diag}(3,1)$.
- Check: $3\cdot\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}+1\cdot\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}=\begin{pmatrix}1.5+0.5&1.5-0.5\\1.5-0.5&1.5+0.5\end{pmatrix}=X$. ✓

**Keep $k=1$.** $\hat X = 3\cdot\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}=\begin{pmatrix}1.5&1.5\\1.5&1.5\end{pmatrix}$.

**Documents.** Rows of $DS$ with $k=1$ are $d_1=d_2=3/\sqrt2=2.121$.
- Check $\hat X'\hat X=DS^2D'$: the left side has $(1.5,1.5)\cdot(1.5,1.5)=4.5$ in every cell. The right side is $\tfrac{9}{2}=4.5$. ✓
- Original cosine between the documents: $(2,1)\cdot(1,2)/5=4/5=0.8$. In the $k=1$ space both documents are the same point, so the cosine is 1. This is the paper's point that different term profiles can map to the same factor vector (pdf 8).

**Query.** The query is the single word $t_1$, $X_q=(1,0)'$.
- Fold-in (this toy is 2-D, so $T$ is 2×2 for $k=2$): $D_q=X_q'TS^{-1}=\tfrac1{\sqrt2}(1,1)\,\mathrm{diag}(\tfrac13,1)=(0.2357,\,0.7071)$.
- Scaled for within comparison, $D_qS=X_q'T=(0.7071,0.7071)$ (my choice of scaling).
- With $k=2$, rows of $DS$: $d_1=(2.121,0.707)$ and $d_2=(2.121,-0.707)$. Cosine of query with $d_1$: $(0.7071\cdot2.121+0.7071\cdot0.707)/(1\cdot\sqrt{4.5+0.5})=2/2.236=0.894$. This equals the raw cosine $2/\sqrt5$, as expected when $k$ equals the rank.
- With $k=1$ the query cosine is 1 for both documents, so the reduction has erased the difference between them. This is why $k$ must be chosen with care.

## Concepts
- [[latent-semantic-indexing]] (new) — retrieval by position in a low-dimensional SVD space of terms and documents instead of by literal term match (pdf 2)
- [[term-document-matrix]] (new) — $t\times d$ matrix of term frequencies per document; the input $X$ (pdf 10)
- [[singular-value-decomposition]] — $X=T_0S_0D_0'$ with orthonormal $T_0$, $D_0$ and positive diagonal $S_0$ in decreasing order (pdf 12–13)
- [[rank]] — $m$, the rank of $X$; the truncated model has rank $k\le m$ (pdf 13)
- [[eckart-young-theorem]] — the paper states without proof that truncation gives the closest rank-$k$ matrix in the least-squares sense; no name or proof is given (canon link; not stated in this unit) (pdf 13)
- [[eigenvector-eigenvalue]] — footnote 4: $T_0$ and $D_0$ are eigenvector matrices of $XX'$ and $X'X$, with eigenvalues $S_0^2$ (pdf 13)
- [[dot-product]] / [[cosine-similarity]] — dot product or cosine between vectors in the factor space estimates similarity; cosine is used to rank documents (pdf 8–9)
- [[orthonormal-basis]] — the factors are orthogonal axes; SVD factors are orthogonal axes (pdf 12); the authors note that Koll's hand-chosen dimensions were not truly orthogonal, unlike the axes of factor analysis (pdf 6)
- [[pseudo-document]] (new) — a query or new document as a term vector, folded in via $D_q=X_q'TS^{-1}$ (pdf 16)
- [[folding-in]] (new) — placing new terms or documents at the centroid of their constituents without redoing the SVD (pdf 7, 22)
- [[two-mode-factor-analysis]] (new) — factor model starting from a rectangular matrix with different entities in rows and columns; SVD is its form here (pdf 7–8)
- [[synonymy-polysemy]] (new) — several words for one thing (hurts recall); one word with several meanings (hurts precision) (pdf 2–3)
- [[precision-recall]] (new) — evaluation measures; here precision is averaged over recall levels and queries (pdf 17)
- [[choice-of-k]] — number of dimensions chosen by the operational criterion of best retrieval; solutions are nested (pdf 14, 19)

## Canonical instances
- [[lsi-sample-term-document-matrix]] — fictional 3-doc matrix showing a relevant document missed and a non-relevant one returned (pdf 4)
- [[bellcore-memo-example]] — 12 terms × 9 titles; 2-D LSI retrieves c1–c5 for "human computer interaction" (pdf 11–12, 26–28)
- [[med-collection-test]] — 1033 abstracts, 30 queries; LSI .51 vs term matching .45 (pdf 17–19)
- [[cisi-collection-test]] — 1460 abstracts, 35 queries; LSI = term matching, SMART better (pdf 20–21)

## Bridges (candidates)
- [same-math] $D_q=X_q'TS^{-1}$ ↔ linear-algebra: coordinates of the projection of a vector onto the span of the columns of $T$ (since $T'T=I$, $T'X_q$ gives the coordinates, then rescaled by $S^{-1}$).
- [same-math] Footnote 4 (SVD vs eigen-analysis of $XX'$, $X'X$) ↔ spectral theorem for symmetric matrices $S=Q\Lambda Q^\top$; eigenvalues equal squared singular values.
- [structural-analogy] Truncated SVD of term-document counts ↔ principal component analysis: keep the dominant directions, treat the rest as noise. The matrix here is not centred.
- [structural-analogy] Terms and documents in one space with cosine similarity ↔ modern word and document embeddings.
- [metaphor] "Latent concepts" as hidden causes of word choice ↔ latent-variable models in social science.

## Questions this raises
- How should $k$ be chosen without running retrieval tests? The paper only gives the "what works best" criterion.
- How far can folding-in go before the space must be recomputed? The authors leave this open.
- Can a word with several unrelated meanings (like "bank") be given several points? The authors did not find a method.
- Would weighting or stemming change LSI's results? The authors say their value must be re-evaluated, and CISI suggests stemming adds something.

## Reading notes
- **Page numbers.** The extracted labels give "?" for the first pages and then printed values such as 1, 2, 3, 4… that do not match the images. The images show the manuscript's own numbers "- N -" at the top. For pdf 2–24, manuscript page = pdf − 1. The appendix (pdf 26–28) shows pages 25–27. The label gave "13" for pdf 28, but the image shows "- 27 -". References and front-matter pages continue from there. Following the unit metadata, all citations use (pdf N).
- This is a typescript manuscript, not the journal pagination (391–407). The contents page lists section starts that match the manuscript numbering.
- Figures 1, 4, 5 and 6 are placeholders ("Insert Figure here"). Only the captions (pdf 24) and the text describe them.
- "Xhihat" in the text layer is $\hat X$ (X-hat).
- Misprints. In 4.2.1 the sentence on deleting columns of $T_0$ and $D_0$ names the results as $T$ and $S$; it should say $T$ and $D$ (pdf 14). In the Appendix, "$T_0T_0'=I$" holds only for $T_0'T_0=I$ (as in Figure 2); with $T_0$ being 12×9, $T_0T_0'$ is 12×12 and not the identity (pdf 27).
- Figure 5 caption gives a rise from about .20 to .50, whereas the text says .25 to .52 (pdf 19, 24).
- In the CISI text, the sentence giving average precision .11 for LSI and term matching has a word missing after "for" (pdf 20).
- The statement that all three of $T_0$, $D_0$, $S_0$ must be of full rank (pdf 13) is reported as printed.
- Unit metadata source: 34 pdf pages; the contents, figure list and table list (pdf 32–34) and the references (pdf 29–31) were not digested beyond using them to check numbers.
