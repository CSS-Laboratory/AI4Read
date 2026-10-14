---
id: grimmer-2022-textasdata/ch08-distributed
work: grimmer-2022-textasdata
unit: Chapter 8. Distributed Representations of Words
pages: 140-156
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Distributed Representations of Words

## L0 — One line
Word embeddings replace one-hot word vectors with dense low-dimensional vectors learned from large unlabeled text, so that words used in similar contexts get similar representations.

## L1 — The gist (≤ 120 words)
Bag-of-words treats every word as unrelated to every other word. The chapter asks how to represent words so that similar words are close. The answer is word embeddings: dense vectors of about 50–500 dimensions, learned mostly by predicting a word from its context or by factorizing co-occurrence counts (distributional hypothesis: context hints at meaning; self-supervision: text supplies labels). Methods include LSA, word2vec and GloVe. Pretrained embeddings can be downloaded, and there are fixes for rare words. Word vectors must be aggregated to documents. Validation should rest first on the researcher's own task. Embeddings also carry the biases of their training text. Contextualized models capture word order but are very costly. This supports transfer learning to small social-science corpora.

**Prerequisites:** one-hot/bag-of-words and document-feature matrix; inner product and cosine similarity; softmax; matrix factorization (SVD) at a rough level.

## L2 — Key ideas (5–10 bullets)
- One-hot vectors give every pair of distinct words an inner product of 0. Embeddings encode similarity, allow "automatic generalization", and give a measure of meaning (pp. 140, 143–144).
- Meaning here is a narrow sense: words are similar when used in similar contexts (distributional hypothesis) (pp. 142, 144).
- Self-supervision: the text itself supplies the labels, e.g. predict a word from its neighbors (p. 145).
- The analyst chooses data source, window size, dimension and algorithm (pp. 145–146).
- LSA is truncated SVD of the document-feature matrix. word2vec (CBOW, skipgram, negative sampling) and GloVe are alternatives (pp. 146–148).
- Rare or unseen words can be handled by retrofitting, fastText (character n-grams) or à la carte embeddings. The State of the Union "manufacturing" case illustrates the à la carte approach (pp. 149–151).
- Embeddings absorb stereotypes from the training text. Debiasing research cannot address the root concern that embeddings reflect the language they are trained on (p. 151).
- Documents need an aggregation step. Validation should give priority to the researcher's own task (pp. 152–153).
- Contextualized embeddings (BERT, GPT-3) capture word order but are far more expensive to train (p. 155).

## L3 — Walkthrough

### Introduction (pp. 140–141)
- In earlier chapters a word is a **one-hot encoding**: a length-$J$ vector (J = vocabulary size) with a single 1. Documents with no shared words then have inner product 0 (p. 140).
- Lemmatizing or stemming (Ch. 5) already treats writer and writers as identical. Distributed representations generalize this by learning from external data that writer and author are related (p. 140).
- A **word embedding** is a dense vector of length $K < J$, e.g. $\text{cat} = (1.3, .2, \dots, .45)$ (pp. 140–141).
- Similarity measures such as those of Ch. 7 should then give $\text{similarity}(\text{cat},\text{dog})$ likely larger than $\text{similarity}(\text{cat},\text{planet})$ (p. 141).
- Embeddings are generally learned using the **distributional hypothesis**: the context in which a word is used is a clue to its meaning (p. 141).

### 8.1 Why Word Embeddings (pp. 142–144)
- In many respects, bag of words preserves the most information about each word. But vocabularies of tens or hundreds of thousands of words make the document-feature matrix sparse and high-dimensional, possibly with more columns than rows (p. 142).
- Embeddings are learned by unsupervised learning on unlabeled data. The hope is that embeddings from a large general corpus help a task with little labeled data. This is **transfer learning**, and it rests on word meaning being relatively stable across corpora (p. 142).
- The idea dates to at least the 1980s (Hinton, 1986). It took off once estimation could handle corpora of hundreds of billions of tokens (p. 142).
- The distributional hypothesis goes back to at least Wittgenstein (1953). Firth's summary: "you shall know a word by the company it keeps" (p. 142). Words that often appear in a small window around a focal word can tell us something about its meaning, without hand labeling (pp. 142–143).
- **Three advantages** (p. 143):
  1. *Encoding similarity.* Under bag of words, the inner product of any two different words is always 0. Embeddings point in similar directions for similar words. Mikolov, Yih and Zweig (2013) showed King − Man + Woman gives a vector quite close to Queen, although the embedding model was not explicitly trained to solve analogies (p. 143).
  2. *Automatic generalization* (Hinton, 1986). Example (imagined by the authors): in sentiment classification of movie reviews with a small hand-labeled set, perhaps we never see fantastic but do see great. With bag of words, fantastic is unusable. With embeddings, the model learns an association between great's *location* in the space and positive reviews. Fantastic sits nearby, so the prediction generalizes (pp. 143–144). The benefit is most noticeable in small corpora or short documents, but even large corpora have many rare words (p. 144).
  3. *Measuring meaning.* Embeddings from large corpora are used to study meanings and how they change over time or across speakers (p. 144). Two words count as same-meaning when used in similar contexts. The authors flag the limits of this conception (p. 144).

*Intuition note.* A classifier that learns weights on positions in a space, not on separate words, treats nearby words alike. That is why one labeled "great" can help with "fantastic". All three advantages come from borrowing information from a larger corpus (p. 144).

### 8.2 Estimating Word Embeddings (pp. 145–151)
**8.2.1 Self-supervision.** Hand-labeled data is expensive. The self-supervision insight: build a supervised task whose label comes from the data itself, often predicting a focal word from the words around it. The information needed to do this well is also useful for other tasks (p. 145).

**8.2.2 Four design choices** (Rodríguez and Spirling, N.d., evaluate these for social scientists) (p. 145):
1. *Data source.* Stable embeddings probably need at least several million tokens (Zhang et al., 2021). Pretrained embeddings exist, trained on billions of tokens from Wikipedia, news and web pages, and reflect that language. Rodríguez and Spirling argue that widely available pretrained embeddings perform about as well at capturing political meaning as embeddings trained on political speech (p. 145).
2. *Context window.* Usually symmetric and fixed, e.g. five words left and right. A very small window tends to capture some syntactic meaning. A larger window tends to capture semantic meaning (p. 146).
3. *Dimension.* Usually 50 to 500. This is initially surprising given million-word vocabularies, but low dimensions have "stood the test of time" (p. 146).
4. *Algorithm.* Three are described below (p. 146).

**8.2.3 Latent Semantic Analysis (LSA)** (Deerwester et al., 1990).
- LSA is a special case of word embeddings. It uses a truncated singular-value decomposition on the (possibly tf-idf weighted) document-feature matrix (p. 146).
- The whole document is the context window, so embeddings generally capture semantic content (p. 146).
- Figure 8.1 shows the low-rank factorization: a #Documents × #Features matrix is approximated by the product of three matrices. These are #Documents × $K$, a $K \times K$ diagonal matrix, and $K \times$ #Features (p. 147).
- Each column of the right-hand matrix is a continuous embedding for one word. Similar words are likely to appear in the same kinds of documents, either by co-occurring or by being substitutes (p. 146).
- Limits: the whole document may be too wide a window. Computation can become infeasible when documents or vocabulary grow large (p. 147).

**8.2.4 Neural embeddings (word2vec).**
- Neural embeddings were proposed as far back as Bengio et al. (2003). They took off with Mikolov and coauthors because of efficient learning algorithms (p. 147).
- word2vec is an umbrella term for two objectives, CBOW and skipgram, plus the optimization routine negative sampling (p. 147).
- **CBOW**: predict a focal word from its context. In "the quick brown fox [blank] over the lazy dog", the average of the context word vectors predicts the blank. The vector for the actual word (jumps) is set to maximize (p. 147):

$$\arg\max_{\mu_{\text{jumps}}} \frac{\exp(\mu_{\text{jumps}} \cdot \bar v)}{\sum_j \exp(\mu_j \cdot \bar v)} \tag{8.2.1}$$

  where $\bar v$ is the average of all embeddings in the context and $j$ indexes the whole vocabulary (p. 148).
- **Skipgram** reverses the problem: context words are predicted one at a time from the focal word. In both, two words get similar embeddings when they appear in context windows of the same types of words (p. 148).
- Problem: the denominator of (8.2.1) sums over the whole vocabulary. Google's released word2vec embeddings have over three million terms and phrases (p. 148).
- **Negative sampling** approximates the denominator with a (weighted) random sample of a few words (two to 20 in Mikolov et al.) that were not the focal word (p. 148).
- Negative sampling is closely related to a weighted version of the matrix factorization used in LSA (Levy and Goldberg, 2014) (p. 148).
- **GloVe** (Pennington, Socher and Manning, 2014) attacks the factorization directly. It builds a square matrix $C$ where $C_{jj'}$ is the number of times words $j$ and $j'$ appear in the same context. It factorizes $C$ with a weighted objective that down-weights highly frequent co-occurrences (p. 148).

*Intuition note.* Both families turn "which words appear near which" into a prediction or factorization problem. The vectors that solve it are the embeddings. The softmax over millions of words is too expensive, so negative sampling uses a few random "wrong" words instead (p. 148).

**8.2.5 Pretrained embeddings.** Downloadable from Google (word2vec), Stanford (GloVe) and Facebook (fastText), often trained on ten to hundreds of billions of tokens. fastText has models for 157 languages (p. 148).

**8.2.6 Rare words.** Rare-word embeddings are noisier. Domain-specific jargon may have no pretrained embedding at all. Three strategies (p. 149):
- *Retrofitting* (Faruqui et al., 2015). Resources such as WordNet, FrameNet and the Paraphrase Database give a graph linking related words, e.g. synonyms. Retrofitting takes pretrained embeddings plus the graph and returns embeddings encouraged to give graph neighbors similar vectors (p. 149).
- *Character level* (fastText; Bojanowski et al., 2017). A word is represented by its character n-grams (sizes 3, 4, 5, 6). Its embedding is the average of its n-gram embeddings. This lets fastText embed unseen words and share information across words with similar character sequences (p. 149).
- *À la carte* (Khodak et al., 2018). Induce a new embedding from pretrained embeddings of the context words around a few uses of the new word. A transformation of the context average gives an accurate embedding even from a single instance (p. 150). Footnote 1: the plain average is not itself a good embedding, because it overstates the common dimensions of the space, so a learned linear transformation is used (p. 156). It also works for n-grams and corpus-specific meanings (p. 150).

**8.2.7 Illustration: "manufacturing" in State of the Union addresses** (p. 150).
- The word occurs only 53 times, roughly evenly split between 1900–1959 and 1960–2016. À la carte gives a separate 300-dimensional embedding per period (p. 150). The dictionary meaning of the word has not changed; the bundle of activities it refers to has drifted (p. 150).
- Nearest neighbors by cosine distance, pre-1960: top five exportation, oil-related, concomitant, detriment, war-relate. Further down: energy-intensive, import/export, defense-related, capital-intensive (pp. 150–151).
- Post-1960: retool, retooling, jobs, downtowns, offshoring. Further down: outsourced, globalized, low-skilled, retraining, workforce (p. 151).
- Even with few instances, the embeddings capture a difference in how the word is used. They can serve as a representation for classification or clustering (p. 151).
- **Bias.** Embeddings reflect associations in the corpus. Large pretrained embeddings contain gender–occupation associations (Bolukbasi et al., 2016), gender stereotypes (Caliskan et al., 2017) and ethnic stereotypes (Garg et al., 2018). This links to principle 2 of Ch. 3 on corpus construction (p. 151).
- Social scientists can study these biases. Garg et al. trace ethnic stereotypes over a century. In real-world systems, embeddings risk exacerbating inequalities (Benjamin, 2019) (p. 151).
- The embedding for doctor does not "know" that any gender can hold the job (p. 151).
- Debiasing research exists, but it cannot address the root concern that embeddings reflect language, which is a product of a social process. The authors say the presence of bias requires careful thought about research goal and data (p. 151).

### 8.3 Aggregating to the document level (p. 152)
- Bag of words just sums token vectors. With embeddings the aggregation is less obvious (p. 152).
- First approximation: average the word embeddings in the document (p. 152).
- Improvement: **Smooth Inverse Frequency (SIF)** (Arora, Liang and Ma, 2017) weights and then removes a common component by taking out the first singular vector. The text says it "first weight[s] the sentences". It builds on the tf-idf idea of de-emphasizing common signal. An à la carte variant can add word-order information via induced n-grams (p. 152).
- **doc2vec** (Le and Mikolov, 2014) is skipgram-like. A paragraph-level vector is added to the prediction model and optimized to aid prediction. It needs extra training (p. 152).
- All of these use word order only very lightly. Recurrent-neural-network models give order-sensitive representations but are much harder to train (Socher et al., 2013; Kiros et al., 2015). Some deep-learning classifiers need only token-level input and build the document representation implicitly (p. 152).
- Most computer-science work targets sentences or paragraphs. It is likely to work for short texts, but longer documents may perform worse (p. 152).

### 8.4 Validation (pp. 153–154)
- **Extrinsic** evaluation tests performance on a downstream NLP task. **Intrinsic** evaluation tests whether embeddings capture word similarities (p. 153).
- For social scientists the most important validation is whether the representation helps their specific task (p. 153).
- Extrinsic: embeddings boosted accuracy in noun phrase chunking, part-of-speech tagging and named entity recognition (Pennington et al., 2014). They have also improved accuracy of simple linear classifiers (p. 153).
- Intrinsic: word-pair similarity judgments, analogy solving, and clustering tasks that check recovery of semantically coherent groups. Many tasks pick the word with the highest cosine similarity to a query (p. 153).
- Weaknesses of word-similarity tasks: they are inherently subjective, cannot account for polysemy, lack train/test splits, and are likely underpowered. Schnabel et al. (2015) show that extrinsic and intrinsic results often conflict. This underscores that there is never going to be a single correct representation for all tasks (p. 153).
- **Turing-style test** (Rodríguez and Spirling, N.d.). MTurk workers get ten political words and each produces ten nearest neighbors. Machine neighbors come from the most cosine-similar embedding vectors. A separate set of humans sees a prompt word with one human and one machine neighbor (unlabeled) and picks the best. The metric is how often human-generated words are chosen over machine ones. Off-the-shelf pretrained embeddings often perform on par with or exceeding human-generated words (p. 154).

### 8.5 Contextualized Word Embeddings (p. 155)
- Standard embeddings give a word one fixed vector regardless of context. Polysemic words like bat tend to sit at the average of their senses (Arora et al., 2018) (p. 155).
- Contextualized models (Peters et al., 2018; Devlin et al., 2019; Liu et al., 2019; Brown et al., 2020) use the same self-supervision insight with much more complicated deep learning. A pretrained model gives a context-specific embedding for every word in a document (p. 155).
- Many are based on recurrent networks or the Transformer. They are the first models in the chapter to truly capture word order (p. 155).
- Pretrained examples: BERT and GPT-3. They can be fine-tuned to the researcher's corpus, but even this partial training can be computationally intensive (p. 155). Footnote 2: fine-tuning continues training on new data for limited iterations and must be done carefully to avoid overfitting (p. 156).
- Cost: standard embeddings are feasible for individual researchers (Rodríguez and Spirling trained models with up to 700 million tokens in three hours on eight CPU cores). Contextualized models effectively need GPUs and days to months. Strubell et al. (2019) estimate 79 hours and \$4–12K cloud cost per BERT training instance. One case study used 27 years of GPU time (60 GPUs, six months), estimated at \$100–350K (p. 155).

### 8.6 Conclusion (p. 156)
Embeddings give a comparatively small, dense representation per word, which must be aggregated to documents. The self-supervision insight lets them capture similarity and generalize across distinct words. They can be learned on large existing corpora and transferred (p. 156).

## Toy example (ours, not from the text)
Vocabulary {cat, dog, planet}, $J=3$, $K=2$. One-hot: cat = (1,0,0), dog = (0,1,0); inner product = 0, same as cat·planet.

Hypothetical embeddings: cat = (1.0, 0.5), dog = (0.9, 0.6), planet = (−0.2, 1.0).
- cat·dog = 0.9 + 0.3 = 1.2. |cat| = √1.25 = 1.118, |dog| = √1.17 = 1.082. Cosine = 1.2 / 1.209 ≈ 0.992.
- cat·planet = −0.2 + 0.5 = 0.3. |planet| = √1.04 = 1.020. Cosine = 0.3 / 1.140 ≈ 0.263.

So similarity(cat, dog) > similarity(cat, planet), as the chapter says it should.

Generalization: take great = (0.8, 0.1) and fantastic = (0.9, 0.2). Suppose a classifier trained only on reviews with great gets weights $w=(1,0)$. Score(great) = 0.8. Score(fantastic) = 0.9, also positive although fantastic was never labeled. With one-hot features, fantastic would have no learned weight (it stays at its starting value, 0).

## Concepts
- [[word-embedding]] (new) — dense length-$K$ vector ($K<J$) per word, learned from unlabeled text (pp. 141–142)
- [[one-hot-encoding]] (new) — length-$J$ vector with a single 1. Distinct words have inner product 0 (pp. 140, 143)
- [[distributional-hypothesis]] (new) — a word's context is a clue to its meaning. Here meaning means similar use in similar contexts (pp. 141, 144)
- [[self-supervision]] (new) — the data supplies the labels, e.g. predict a word from its neighbors (p. 145)
- [[transfer-learning]] (new) — use embeddings learned on a large corpus for a different, small task (p. 142)
- [[word2vec]] (new) — CBOW and skipgram objectives plus negative sampling (p. 147)
- [[latent-semantic-analysis]] (new) — truncated SVD of the (tf-idf) document-feature matrix; whole document as window (p. 146)
- [[glove]] (new) — weighted factorization of the word co-occurrence matrix (p. 148)
- [[rare-word-embeddings]] (new) — retrofitting, fastText character n-grams, à la carte induction (pp. 149–150)
- [[document-embedding-aggregation]] (new) — averaging, SIF, doc2vec, or order-sensitive models (p. 152)
- [[contextualized-embedding]] (new) — a word's vector depends on its context, e.g. BERT, GPT-3 (p. 155)
- [[text-as-data-validation]] — intrinsic vs extrinsic evaluation; the researcher's own task comes first (p. 153)

## Canonical instances
- [[king-man-woman-queen]] — vector offset solves analogies, though not explicitly trained for it (p. 143)
- [[great-fantastic-sentiment]] — automatic generalization to unseen words (pp. 143–144)
- [[manufacturing-sotu-embeddings]] — à la carte embeddings from 53 uses show a difference in how the word is used across periods (dictionary meaning unchanged; the bundle of activities drifted) (pp. 150–151)
- [[embedding-bias]] — gender and ethnic stereotypes in pretrained vectors (p. 151)
- [[rodriguez-spirling-turing-test]] — humans compare human and machine nearest neighbors (p. 154)

## Bridges (candidates)
- [structural-analogy] Word embeddings from co-occurrence ↔ political-science: the spatial model of voting — both place items in a low-dimensional space where distance means similarity.
- [metaphor] Distributional hypothesis ↔ political-science: partisan cues and heuristics — judging an item by who is associated with it.
- [same-math] LSA's truncated SVD ↔ text as data: low-rank factorization of the document-feature matrix — the chapter says LSA learns embeddings with a truncated SVD, a low-rank matrix factorization.

## Questions this raises
- When is a pretrained embedding from general corpora a valid measure of meaning for specialized political vocabulary?
- How should a researcher choose between averaging, SIF and doc2vec for long documents, given the chapter's caution about length?
- If embeddings encode stereotypes from society, when is that a measurement of society and when is it a defect of the tool?
- If intrinsic and extrinsic validations conflict, how much weight should each get?

## Reading notes
- Printed page numbers equal pdf numbers (offset 0).
- Equation (8.2.1) is flattened in both the text layer and the page image. I reconstructed it as argmax over $\mu_{\text{jumps}}$ of $\exp(\mu_{\text{jumps}}\cdot\bar v)/\sum_j\exp(\mu_j\cdot\bar v)$, using the chapter's explanatory text.
- Figure 8.1 is described from the page image (matrix shapes with labels #Documents, #Features, $K$).
- The chapter cites "Rodríguez and Spirling (N.d.)" (no date printed). The SIF description says it weights "sentences", as printed.
- The chapter has no exercises.
- The "three strategies" for rare words are listed as retrofitting, character-level information and inducing embeddings (p. 149).
