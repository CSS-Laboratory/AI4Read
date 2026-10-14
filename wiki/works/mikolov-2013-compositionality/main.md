---
id: mikolov-2013-compositionality/main
work: mikolov-2013-compositionality
unit: paper
pages: 1-9
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Distributed Representations of Words and Phrases and their Compositionality

## L0 — One line
Simple extensions of the Skip-gram model (subsampling frequent words, negative sampling, treating detected phrases as single tokens) improve vector quality and training speed, and the vectors can often be combined by simple addition.

## L1 — The gist (≤ 120 words)
The paper asks how to make Skip-gram word vectors better and faster to train, and how to handle phrases whose meaning is not the sum of their words ("Air Canada"). The authors discard very frequent words at random, replace the full softmax with a simple "real vs noise" objective (negative sampling), and merge frequently co-occurring word pairs into single tokens. They test on analogy tasks for words and phrases. A model trained on about 33 billion words reaches 72% on phrase analogies. Adding two word vectors often gives a vector near a meaningful third item. The authors released their code as the open-source word2vec project.

**Prerequisites:** softmax and logistic sigmoid; log probability; dot product and cosine similarity; the idea of a word vector.

## L2 — Key ideas (5–10 bullets)
- Skip-gram trains word vectors to predict nearby words by maximizing average log probability; the full softmax costs time proportional to the vocabulary size $W$, which is impractical (pp. 2–3).
- Hierarchical softmax (a tree-based approximation of the softmax, here with a binary Huffman tree that gives frequent words short paths) cuts the cost to about $\log_2 W$ nodes per prediction (p. 3).
- Negative sampling replaces the softmax with logistic regression: tell the true context word from $k$ noise words. The noise distribution $U(w)^{3/4}/Z$ was the best of those the authors tried (pp. 3–4).
- Subsampling frequent words, with discard probability $1-\sqrt{t/f(w)}$, speeds training about 2–10× and improves rare-word vectors (pp. 2, 4–5).
- On word analogies, negative sampling beats hierarchical softmax and slightly beats NCE (noise-contrastive estimation, a related data-vs-noise method); subsampling sped up the three methods tested with it (Table 1, p. 5).
- Phrases are found by a bigram score (based on how often two adjacent words occur together versus apart) and then treated as single tokens. On phrase analogies, hierarchical softmax with subsampling was the best of the methods tested (pp. 5–7).
- Adding vectors often gives meaningful results. The authors explain this as a product (an "AND") of context distributions (p. 7).
- A Skip-gram model trained on far more data, in much less training time than earlier models, gives visibly better neighbours for rare words; the authors attribute this in part to the larger data (pp. 7–8).

## L3 — Walkthrough

### Abstract and 1 Introduction (pp. 1–2)
Distributed representations (dense vectors) group similar words and help NLP learning (p. 1). Skip-gram is efficient because its training has no dense matrix multiplications; an optimized single-machine implementation can train on more than 100 billion words in a day (p. 1). Vectors encode regularities as linear translations: vec("Madrid") − vec("Spain") + vec("France") is closer to vec("Paris") than to any other word vector (p. 1).

Contributions announced: subsampling (about 2×–10× speedup, better rare-word accuracy); a simplified NCE variant that gives faster training and better vectors for frequent words than the hierarchical softmax of earlier work; phrase vectors (pp. 1–2). Motivation: "Boston Globe" is a newspaper, not a natural combination of "Boston" and "Globe" (p. 2). Phrases are found with a data-driven method and then treated as tokens (p. 2). Phrase analogy example: "Montreal":"Montreal Canadiens"::"Toronto":"Toronto Maple Leafs". It counts as correct if the nearest vector to vec("Montreal Canadiens") − vec("Montreal") + vec("Toronto") is vec("Toronto Maple Leafs") (p. 2). Simple addition also works: vec("Russia") + vec("river") is close to vec("Volga River") (p. 2).

### 2 The Skip-gram Model (pp. 2–3)
Given training words $w_1,\dots,w_T$, maximize the average log probability, where $c$ is the context size:
$$\frac{1}{T}\sum_{t=1}^{T}\sum_{-c\le j\le c,\,j\ne 0}\log p(w_{t+j}\mid w_t)\tag{1}$$
Larger $c$ gives more training examples and possibly higher accuracy, but longer training (pp. 2–3). The basic definition uses softmax, with $v_w$ the "input" and $v'_w$ the "output" vector of $w$:
$$p(w_O\mid w_I)=\frac{\exp\left({v'_{w_O}}^{\top}v_{w_I}\right)}{\sum_{w=1}^{W}\exp\left({v'_{w}}^{\top}v_{w_I}\right)}\tag{2}$$
The cost of $\nabla\log p(w_O\mid w_I)$ is proportional to $W$ (about $10^5$–$10^7$), so this is impractical (p. 3).

*Intuition note:* Each word has two vectors. The score for "$w_O$ appears near $w_I$" is a dot product. The softmax must sum over the whole vocabulary to normalize, which is what makes it slow.

**2.1 Hierarchical softmax (p. 3).** Words are leaves of a binary tree; each inner node stores the relative probabilities of its children, which defines a random walk that assigns probabilities to words. Let $n(w,j)$ be the $j$-th node on the root-to-$w$ path, $L(w)$ the path length, ch$(n)$ an arbitrary fixed child of $n$, and $[[x]]=1$ if $x$ is true, $-1$ otherwise. Then
$$p(w\mid w_I)=\prod_{j=1}^{L(w)-1}\sigma\left([[n(w,j+1)=\mathrm{ch}(n(w,j))]]\cdot {v'_{n(w,j)}}^{\top}v_{w_I}\right)\tag{3}$$
with $\sigma(x)=1/(1+\exp(-x))$. The authors state that $\sum_{w=1}^{W}p(w\mid w_I)=1$ can be verified. The cost is proportional to $L(w_O)$, which on average is no greater than $\log W$. This model has one vector $v_w$ per word and one $v'_n$ per inner node (p. 3). The authors use a binary Huffman tree, which gives frequent words short codes and so fast training (p. 3).

**2.2 Negative sampling (pp. 3–4).** NCE posits that a good model can separate data from noise by logistic regression (p. 3). The authors say that because Skip-gram is only concerned with learning high-quality vectors, they are free to simplify NCE as long as the vectors retain their quality (p. 3). Negative sampling (NEG) replaces every $\log p(w_O\mid w_I)$ term in the Skip-gram objective with
$$\log\sigma\left({v'_{w_O}}^{\top}v_{w_I}\right)+\sum_{i=1}^{k}\mathbb{E}_{w_i\sim P_n(w)}\left[\log\sigma\left(-{v'_{w_i}}^{\top}v_{w_I}\right)\right]\tag{4}$$
There are $k$ noise samples per data sample (p. 4). Reported: $k$ of 5–20 is useful for small datasets and 2–5 for large ones. NCE needs both samples and the numerical noise probabilities; NEG needs only samples. NCE approximately maximizes the softmax log probability; the authors say this property is not important for their application (p. 4). The best noise distribution tried was the unigram distribution to the 3/4 power, $U(w)^{3/4}/Z$. It beat unigram and uniform "on every task we tried" (p. 4). Fig. 2 (p. 4) is a 2-D PCA projection of 1000-dimensional Skip-gram vectors of countries and their capitals; the authors say it shows the model organizing concepts and learning their relationships implicitly, since no supervised information about what a capital city means was given.

*Intuition note:* For each true (word, context) pair, push its score up. For $k$ random words, push their scores down. No sum over the vocabulary is needed.

**2.3 Subsampling of frequent words (pp. 4–5).** Frequent words like "the" usually provide less information value than rare words. "France" with "Paris" teaches more than "France" with "the", because nearly every word co-occurs with "the" (p. 4). Also, vectors of frequent words change little after several million examples (p. 4). Each training word $w_i$ is discarded with probability
$$P(w_i)=1-\sqrt{\frac{t}{f(w_i)}}\tag{5}$$
where $f(w_i)$ is its frequency and $t$ a threshold, typically about $10^{-5}$. The formula aggressively subsamples words with $f>t$ while preserving the frequency ranking. It was chosen heuristically but works well (p. 5).

### 3 Empirical Results (p. 5)
Task: analogies such as "Germany":"Berlin"::"France":?. Find $x$ whose vector is closest (cosine distance, input words excluded) to vec("Berlin") − vec("Germany") + vec("France"). There are syntactic (quick:quickly) and semantic (country:capital) analogies. Training data: an internal Google news set of one billion words; words seen fewer than 5 times were dropped, leaving a 692K vocabulary (p. 5).

Table 1 (300-dim; time in minutes; total accuracy %), as printed (p. 5):

| Method | Time | Syntactic | Semantic | Total |
|---|---|---|---|---|
| NEG-5 | 38 | 63 | 54 | 59 |
| NEG-15 | 97 | 63 | 58 | 61 |
| HS-Huffman | 41 | 53 | 40 | 47 |
| NCE-5 | 38 | 60 | 45 | 53 |
| With $10^{-5}$ subsampling: NEG-5 | 14 | 61 | 58 | 60 |
| NEG-15 | 36 | 61 | 61 | 61 |
| HS-Huffman | 21 | 52 | 59 | 55 |

Conclusions: NEG beats HS and is slightly better than NCE; subsampling speeds training several times and makes vectors significantly more accurate (p. 5).

**Objection (implied, author's wording "It can be argued"):** the linearity of Skip-gram may make its vectors suited to linear analogies. **Authors' reply:** vectors from standard sigmoidal recurrent networks (highly non-linear), per [8], also improve on this task as data grows. This suggests non-linear models also prefer a linear structure (p. 5).

### 4 Learning Phrases (pp. 5–7)
Find words that appear frequently together and infrequently in other contexts. "New York Times" and "Toronto Maple Leafs" become single tokens; the bigram "this is" stays unchanged (p. 5). This avoids training on all n-grams, which would be too memory intensive (p. 6). Bigram score:
$$\mathrm{score}(w_i,w_j)=\frac{\mathrm{count}(w_iw_j)-\delta}{\mathrm{count}(w_i)\times\mathrm{count}(w_j)}\tag{6}$$
$\delta$ is a discount that prevents many phrases made of very infrequent words. Bigrams scoring above a threshold become phrases. Typically 2–4 passes are run with decreasing threshold, so longer phrases can form (p. 6).

Phrase analogy test: five categories (newspapers, NHL teams, NBA teams, airlines, company executives), 3218 examples. Example (Table 2): "Steve Ballmer":"Microsoft"::"Larry Page":"Google" (p. 6).

**4.1 Results (pp. 6–7).** Setting: 300 dimensions, context size 5. Table 3 (accuracy %, no subsampling / $10^{-5}$ subsampling): NEG-5 24/27; NEG-15 27/42; HS-Huffman 19/47 (p. 6). NEG with $k=15$ is considerably better than $k=5$. HS is worst without subsampling but best with it, so subsampling can improve accuracy "at least in some cases" (p. 6). Best model: hierarchical softmax, 1000 dimensions, whole sentence as context, about 33 billion words, giving 72%. With 6B words it gave 66%, which the authors say suggests that large training data is crucial (p. 7). Manual inspection of infrequent phrases (Table 4) also suggests HS with subsampling gives the best phrase representations (p. 7).

### 5 Additive Compositionality (p. 7)
Beyond analogies, adding vectors element-wise gives meaningful combinations (Table 5: "Volga River" is the second-closest token to Russian + river, after "Moscow"; "Hanoi" is the closest to Vietnam + capital). **Authors' explanation:** word vectors relate linearly to the softmax inputs and so logarithmically to output probabilities. A vector represents the context distribution of a word, so the sum of two vectors relates to the product of two context distributions. The product acts as AND: words with high probability under both stay high, others become low (p. 7). So "Volga River" appearing near "Russian" and "river" makes the sum close to its vector (p. 7).

*Intuition note:* Adding the vectors is like asking for words likely in the contexts of both words at once. This is the authors' explanation for why "Russian" + "river" can land near "Volga River" (if that name often appears in sentences with both words).

### 6 Comparison to Published Word Representations (pp. 7–8)
The authors downloaded vectors by Collobert and Weston, Turian et al., and Mnih and Hinton. [8] had already found Skip-gram best on word analogies "with a huge margin" (p. 7). Table 6 shows nearest neighbours of rare words. Skip-Phrase (1000d, 1 day training) gives e.g. Havel → "Vaclav Havel", "Velvet Revolution". Collobert (2 months), Turian (few weeks) and Mnih (7 days) give the neighbours listed in the table; empty cells mean the word was not in the vocabulary (p. 8). The authors say the large Skip-gram model "visibly outperforms" the others. This is attributed in part to training on about 30 billion words, about two to three orders of magnitude more data than the typical size used in prior work. Interestingly, its training time is only a fraction of that of the previous model architectures (p. 8).

### 7 Conclusion (p. 8)
Claimed contributions: phrase and word vectors with linear structure; techniques also usable for CBOW; training on orders of magnitude more data; subsampling gives faster training and better uncommon-word vectors; negative sampling is simple and learns accurate vectors "especially for frequent words". Word vectors can be "somewhat meaningfully combined" by simple vector addition. Optimal hyperparameters are task-specific. The most crucial choices were architecture, vector size, subsampling rate and window size. Phrase tokens plus vector addition give a simple way to represent longer text, complementary to recursive matrix-vector approaches [16]. Code is released as word2vec (p. 8).

## Toy example (ours, not from the text)
**Subsampling (eq. 5), $t=10^{-5}$.**
- Word with $f=10^{-3}$: $P=1-\sqrt{10^{-5}/10^{-3}}=1-\sqrt{0.01}=1-0.1=0.9$, so 90% of occurrences are dropped.
- Word with $f=10^{-4}$: $P=1-\sqrt{0.1}\approx1-0.316=0.684$.
- Word with $f=10^{-5}$: $P=1-1=0$.

The more frequent word is dropped more, but the ranking of frequencies is kept.

**Phrase score (eq. 6), $\delta=5$, invented counts.**
- "new york": count(new)=1000, count(york)=500, bigram=300. Score $=(300-5)/(1000\times500)=295/500000=5.9\times10^{-4}$.
- "this is": count(this)=20000, count(is)=30000, bigram=400. Score $=395/(6\times10^{8})\approx6.6\times10^{-7}$.

With a threshold between the two, "new york" is merged and "this is" is not.

**Additive "AND".** Invented context distributions over 3 words: word A $=(0.5,0.4,0.1)$, word B $=(0.1,0.5,0.4)$. Product $=(0.05,0.20,0.04)$, sum $=0.29$, normalized $\approx(0.172,0.690,0.138)$. Word 2, likely under both, dominates; words 1 and 3 are each likely under only one.

## Concepts
- [[skip-gram / CBOW]] — Skip-gram predicts the surrounding words from the center word; the paper's techniques also apply to CBOW (pp. 2, 8)
- [[word embedding]] — "distributed representation": a dense vector per word (or phrase) (p. 1)
- [[softmax]] — eq. 2; cost proportional to vocabulary size $W$ (p. 3)
- [[hierarchical-softmax]] (new) — binary-tree factorization of softmax, about $\log_2 W$ nodes per prediction; Huffman tree here (p. 3)
- [[negative sampling]] — eq. 4: logistic regression separating true context from $k$ noise words; uses samples only (pp. 3–4)
- [[noise-contrastive-estimation]] (new) — separate data from noise by logistic regression; needs noise probabilities, approximately maximizes softmax log-likelihood (pp. 3–4)
- [[subsampling-frequent-words]] (new) — random discard with probability $1-\sqrt{t/f(w)}$ (p. 4)
- [[phrase-detection]] (new) — bigram score eq. 6; phrases become single tokens (p. 6)
- [[analogical-reasoning-task]] (new) — $a:b::c:?$ solved by the nearest vector to $b-a+c$ by cosine (pp. 2, 5)
- [[additive-compositionality]] (new) — adding word vectors gives a vector near a meaningful combination; explained as a product of context distributions (p. 7)

## Canonical instances
- [[country-capital-pca]] — Fig. 2: a 2-D PCA of 1000-d vectors illustrates the model organizing country–capital relationships implicitly; the authors say no supervised information about what a capital city means was given (p. 4)
- [[king-queen-style-analogy: Madrid−Spain+France≈Paris]] — many regularities can be represented as linear translations (p. 1)
- [[Air-Canada-example]] — meanings of "Canada" and "Air" cannot easily be combined into "Air Canada" (p. 1)
- [[Volga-River-addition]] — "Russian" + "river" is near "Volga River" (p. 7)
- [[nearest-neighbours-of-rare-words]] — Table 6 comparison across models (p. 8)

## Bridges (candidates)
- [structural-analogy] Negative sampling ↔ llm/contrastive training: separate a true pair from random pairs by a logistic-style loss.
- [structural-analogy] Subsampling frequent words ↔ statistics: down-weighting very common items so they do not dominate training.
- [metaphor] Sum of vectors as product ("AND") of context distributions ↔ probability: adding log-probabilities multiplies probabilities.
- [structural-analogy] Phrase token merging ↔ tokenization (BPE): both build larger units from frequent adjacent pairs (here one score and threshold, not iterative merges).

## Questions this raises
- Why does the 3/4 power on the unigram noise distribution work better than plain unigram or uniform (the authors give no explanation)?
- Is the "AND" explanation of additive compositionality exact, or only a heuristic? What assumptions does it need?
- Why does hierarchical softmax go from worst to best once frequent words are subsampled (Table 3)?
- Do vectors for phrases and rare words stay reliable when the data is smaller than 33 billion words?

## Reading notes
- Printed page = pdf page (offset 0). Pages 1–8 are the paper; p. 9 is the references list.
- Text layer garbled the equations; all were checked against the page images.
- Source oddities as printed: Table 4 shows "Vasco de Gama" and "Rebbeca Naomi"; Table 5 shows "Check crown" (apparently for Czech crown). Reference [13] reads "Hintont". The data size is "about 33 billion" words (p. 7), "about 30 billion" (p. 8), and "over 30 billion" (Table 6 caption).
- The 3/4-power claim ("on every task we tried including language modeling") is followed by "(not reported here)" (p. 4); no table on these pages shows that comparison. The 2×–10× speedup is stated on p. 2, with no detailed table beyond Table 1.
- This arXiv version is v1 (16 Oct 2013).
