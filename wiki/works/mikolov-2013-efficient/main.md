---
id: mikolov-2013-efficient/main
work: mikolov-2013-efficient
unit: paper
pages: 1-12
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Efficient Estimation of Word Representations in Vector Space (Mikolov, Chen, Corrado, Dean, 2013)

## L0 — One line
Dropping the non-linear hidden layer gives two very cheap models, CBOW and Skip-gram, that learn word vectors from billions of words, and simple vector arithmetic on those vectors can answer syntactic and semantic analogy questions.

## L1 — The gist (≤ 120 words)
Earlier neural models learned word vectors, but, as far as the authors know, none had been trained successfully on more than a few hundred million words, and most were much costlier to train. The authors explore simpler, cheaper models that may represent words less precisely but can possibly be trained on much more data. They propose CBOW (predict a word from its context) and Skip-gram (predict context words from a word), both without a hidden layer. They test the vectors with analogy questions such as "big : biggest :: small : ?", answered by vector arithmetic and cosine distance. On their new test set, the new models match or beat earlier models at much lower cost. Skip-gram is much better on semantic questions. Word vectors could become a building block for later NLP systems.

**Prerequisites:** vectors and cosine similarity; softmax and neural-network layers (input, hidden, output); stochastic gradient descent; the idea of a language model.

## L2 — Key ideas (5–10 bullets)
- Simple models trained on huge data can beat complex ones on small data, but scaling alone does not help where data is limited (speech, translation). This motivates better word representations (p. 1).
- Training complexity is proportional to $O = E\times T\times Q$ ($E$ epochs, $T$ training words, $Q$ per-example cost). The authors compare models by their per-example cost $Q$ (pp. 2–3).
- In the feedforward neural-network language model (NNLM) and in the recurrent one (RNNLM), the cost comes mostly from the hidden-layer terms ($N\times D\times H$ with projection size $N\times D$ and hidden size $H$; and $H\times H$) once hierarchical softmax (a cheaper way to compute output probabilities over a large vocabulary) is used. So the new models remove the hidden layer (pp. 3–4).
- CBOW predicts the middle word from an averaged window of context. Skip-gram predicts nearby words from the current word (pp. 4–5).
- Quality is measured by a new 19,544-question analogy test set (8869 semantic + 10675 syntactic). The answer is the nearest word to $\text{vector}(b)-\text{vector}(a)+\text{vector}(c)$, with exact match required (pp. 5–6).
- After some point, more dimensions or more data alone give diminishing improvements, so both must grow together (p. 6).
- CBOW is best on syntactic questions among the same-data comparison. Skip-gram is far better on semantic ones (p. 7).
- Skip-gram scores complement an RNNLM on the Sentence Completion Challenge, and the combination reaches 58.9% (p. 9).

## L3 — Walkthrough

### Abstract and 1 Introduction
- Many NLP systems treat words as atomic indices, with no notion of similarity. Reasons given: simplicity, robustness, and the observation that simple models on huge data beat complex models on less data. Example: N-grams trained on trillions of words (p. 1).
- Limits: in speech recognition the relevant data is often only millions of words. In machine translation many languages have only a few billion words or fewer. Scaling basic techniques will not always bring progress (p. 1).
- Distributed representations of words are called "probably the most successful concept". Neural language models significantly outperform N-grams (p. 1).

**1.1 Goals.** The aim is to learn high-quality vectors from billions of words with a vocabulary of millions. As far as the authors know, earlier architectures had not been trained successfully on more than a few hundred million words, with vector size 50–100 (pp. 1–2).
- Expectation: similar words are close, and words can have multiple degrees of similarity. Earlier work [20] showed $\text{vector}(\text{King})-\text{vector}(\text{Man})+\text{vector}(\text{Woman})$ is closest to $\text{vector}(\text{Queen})$ (p. 2).
- The paper tries to maximize accuracy of such operations, builds a new test set, and studies how training time and accuracy depend on dimensionality and data size (p. 2).

**1.2 Previous work.** Bengio et al.'s NNLM [1] learns word vectors and a language model jointly. The authors' own earlier work [13, 14] first learns vectors with a one-hidden-layer network and then trains the NNLM on them. This paper directly extends that first step (p. 2). Other architectures were, as far as the authors know, much costlier to train, except a log-bilinear version with diagonal weight matrices [23] (p. 2).

### 2 Model architectures
- Neural vectors are chosen because they were shown to preserve linear regularities significantly better than LSA, and LDA is very expensive on large data (p. 2).
- Complexity = number of parameters accessed to fully train the model. Goal: maximize accuracy while minimizing complexity (p. 2).
- Training complexity for all models is proportional to:
$$O = E \times T \times Q \tag{1}$$
$E$ = epochs (common choice 3–50), $T$ = words in training set (up to about one billion), $Q$ = per-example cost defined per model. All models use SGD and backpropagation (p. 3).

**2.1 Feedforward NNLM.** Layers: input, projection, hidden, output. The $N$ previous words are 1-of-$V$ coded ($V$ = vocabulary size). They are projected with a shared matrix into a layer of size $N\times D$. The hidden layer has size $H$. The output has size $V$. Typical values: $N=10$, projection 500–2000, $H$ 500–1000 (p. 3).
$$Q = N\times D + N\times D\times H + H\times V \tag{2}$$
- $H\times V$ dominates, but it can be avoided. Options: hierarchical softmax, or models not normalized during training. With a binary tree, about $\log_2(V)$ outputs are evaluated, so $N\times D\times H$ then dominates (p. 3).
- The authors use hierarchical softmax with a **Huffman tree**, which gives frequent words short binary codes. It needs only about $\log_2(\text{Unigram\_perplexity}(V))$ outputs. For one million words this is about a two-times speedup. It matters little for NNLMs but a lot for the later hidden-layer-free models (p. 3).

**2.2 RNNLM.** It has no projection layer. A recurrent matrix connects the hidden layer to itself with time delay, forming a short-term memory. It avoids fixing the context length $N$ (p. 3).
$$Q = H\times H + H\times V \tag{3}$$
Here $D = H$. Hierarchical softmax reduces $H\times V$ to $H\times\log_2(V)$, so most cost is $H\times H$ (p. 3).

**2.3 Parallel training.** Models run on DistBelief: many replicas (often 100 or more, on many CPU cores) synchronize gradient updates through a central parameter server. Training uses mini-batch asynchronous gradient descent with Adagrad (p. 4).

> *Intuition note.* Cost per training example is a count of the parameters that must be accessed. The non-linear hidden layer is the expensive part. If you delete it, the authors hope the model can be trained on much more data.

### 3 New log-linear models
Observation: most cost comes from the non-linear hidden layer. The authors explore simpler models that may represent data less precisely but can possibly be trained on much more data efficiently (p. 4).

**3.1 CBOW.** Like the feedforward NNLM, but with no hidden layer. The projection layer is shared for all words, so their vectors are averaged. Word order in the context does not matter. Words from the future are used too: the best performance came from four history and four future words, with a log-linear classifier trained to classify the middle word (p. 4).
$$Q = N\times D + D\times\log_2(V) \tag{4}$$
"Continuous" because it uses distributed context representations. The input-projection weights are shared across positions (p. 4).

**3.2 Skip-gram.** Each current word is the input to a log-linear classifier. It predicts words within a range before and after it. A larger range improves vector quality but costs more. Distant words get less weight, by being sampled less (p. 4).
$$Q = C\times\big(D + D\times\log_2(V)\big) \tag{5}$$
$C$ = maximum distance. With $C=5$, for each training word a number $R$ is drawn at random from $\langle 1;C\rangle$. Then $R$ history and $R$ future words are labels, which means $2R$ classifications. The experiments use $C=10$ (pp. 4–5).

> *Intuition note.* CBOW says "context → word"; Skip-gram says "word → each neighbour". Skip-gram makes many predictions per word, so it costs more (Eq. 5 vs 4).

### 4 Results
**Analogy method.** Two word pairs with the same relation form a question, e.g. "what is similar to *small* as *biggest* is to *big*?" Compute $X=\text{vector}(\text{"biggest"})-\text{vector}(\text{"big"})+\text{vector}(\text{"small"})$. Then take the word closest to $X$ by cosine distance, discarding the three input words. Well-trained vectors give *smallest*. With high-dimensional vectors on much data, subtle semantic relations also work, e.g. France : Paris :: Germany : Berlin (p. 5).

**4.1 Task.** The new test set has 5 semantic types and 9 syntactic types (Table 1), with 8869 semantic and 10675 syntactic questions. Pairs were listed by hand, then questions formed by joining two pairs. Example: 68 US cities with their states gave about 2.5K questions. Only single-token words are included (p. 6).
- A question counts as correct only if the closest word is exactly the target, so synonyms are errors. The authors say 100% is likely impossible, since the models have no morphology input. They believe usefulness for applications should be positively correlated with this accuracy (p. 6).

**4.2 Maximizing accuracy.** Training data: Google News, about 6B tokens, vocabulary restricted to the 1M most frequent words. Architecture choices were first tested on subsets, with a 30k vocabulary (CBOW, Table 2). The table shows accuracy in %, for increasing amounts of training words (p. 7):

| Dim. | 24M | 783M |
|---|---|---|
| 50 | 13.4 | 23.2 |
| 600 | 24.0 | 50.4 |

- After some point, more dimensions or more data give diminishing improvements, so both must be increased together. By Eq. 4, doubling the data costs about the same as doubling the vector size (pp. 6–7).
- Tables 2 and 4: three epochs, SGD, starting learning rate 0.025 decreased linearly to about zero (p. 7).

**4.3 Comparing architectures** (same data, 640 dimensions; LDC corpora, 320M words, 82K vocabulary). The earlier RNNLM took about 8 weeks on one CPU. The NNLM was trained with DistBelief, with 640 hidden units and a history of 8 words (p. 7).

Table 3 (accuracy %):

| Model | Semantic | Syntactic | MSR test |
|---|---|---|---|
| RNNLM | 9 | 36 | 35 |
| NNLM | 23 | 53 | 47 |
| CBOW | 24 | 64 | 61 |
| Skip-gram | 55 | 59 | 56 |

- Reading by the authors (p. 7): the RNN vectors do well mostly on syntactic questions. CBOW beats the NNLM on syntactic and is about equal on semantic. Skip-gram is slightly worse than CBOW on syntactic but better than the NNLM, and much better than all others on semantic.
- Table 4 compares publicly available vectors with the authors' models. Skip-gram (300 dim, 783M words) gets 50.0 semantic and 53.3 total. CBOW gets 15.5 semantic and 36.1 total. "Our NNLM" (100 dim, 6B words) gets 64.5 syntactic and 50.8 total. The public vectors from other groups score lower (total 1.8–24.6) (p. 8).
- On one CPU, CBOW trained on a Google News subset in about a day and Skip-gram in about three days (pp. 7–8).
- Table 5: one epoch on twice the data gives comparable or better results than three epochs, with a small additional speedup. For example, CBOW 300-dim total is 36.1 for 3 epochs on 783M words (1 day) and 36.1 for 1 epoch on 1.6B (0.6 day). Skip-gram gives 53.3 (3 days) vs 53.8 (2 days). Later experiments use one epoch (p. 8).

**4.4 Large-scale parallel training.** 50–100 DistBelief replicas, Google News 6B. CPU counts are estimates because the machines are shared (pp. 8–9). Table 6:

| Model | Dim | Sem. | Synt. | Total | Time (days × cores) |
|---|---|---|---|---|---|
| NNLM | 100 | 34.2 | 64.5 | 50.8 | 14 × 180 |
| CBOW | 1000 | 57.3 | 68.9 | 63.7 | 2 × 140 |
| Skip-gram | 1000 | 66.1 | 65.1 | 65.6 | 2.5 × 125 |

Because of framework overhead, CBOW and Skip-gram CPU usage are closer here than on a single machine (p. 9).

> *Intuition note.* The cheap models reach higher total accuracy than the 100-dim NNLM in far less compute, because they can afford 1000 dimensions on 6B words.

**4.5 Microsoft Sentence Completion Challenge.** 1040 sentences, one missing word, five choices. Skip-gram (640 dim) was trained on 50M words from [32]. The sentence score is the sum of predictions of the surrounding words with the candidate word at the input (p. 9). Table 7 (accuracy %): 4-gram 39, average LSA similarity 49, log-bilinear 54.8, RNNLMs 55.4, Skip-gram 48.0, Skip-gram + RNNLMs 58.9. Skip-gram alone is not better than LSA similarity, but its scores complement the RNNLMs. The weighted combination gives 58.9% (59.2% on the development part, 58.7% on the test part), a new state of the art (p. 9).

### 5 Examples of learned relationships
Relations are defined by subtraction and added to another word, e.g. Paris − France + Italy = Rome. Table 8 lists examples from the 300-dim, 783M-word Skip-gram vectors (p. 10).
- Under exact match, the Table 8 examples would score only about 60% (pp. 9–10).
- Averaging ten example pairs instead of one to form the relationship vector improved the best models by about 10% absolute on the semantic-syntactic test (p. 10).
- Odd-one-out: average the vectors of a list and pick the most distant word. The authors observed good accuracy (p. 10).

### 6 Conclusion and 7 Follow-up
- Simple architectures give high-quality vectors, and the lower cost allows larger data and dimensionality (p. 10).
- With DistBelief it "should be possible" to train CBOW and Skip-gram on one-trillion-word corpora (p. 10).
- Cited result [31]: public RNN vectors plus other techniques gave over 50% increase in Spearman correlation on SemEval-2012 Task 2 (p. 10).
- Ongoing work: extending and verifying facts in knowledge bases; machine translation "looks very promising" (p. 10).
- Follow-up: released single-machine C++ code at billions of words per hour, and 1.4M+ named-entity vectors trained on 100B+ words (p. 11).

## Toy example (ours, not from the text)
2-D vectors: big=(3,1), biggest=(5,3), small=(1,2), smallest=(3,4), bigger=(4,1), tiny=(1,0.5).
- $X = \text{biggest}-\text{big}+\text{small} = (5-3+1,\ 3-1+2) = (3,4)$, $|X|=\sqrt{9+16}=5$.
- Candidates (input words big, biggest, small discarded):
  - smallest: cos = $(9+16)/(5\times5)=1$
  - bigger: dot $=12+4=16$, $|{\rm bigger}|=\sqrt{17}\approx4.123$, cos $=16/20.62\approx0.776$
  - tiny: dot $=3+2=5$, $|{\rm tiny}|=\sqrt{1.25}\approx1.118$, cos $=5/5.59\approx0.894$
- The closest is *smallest*. It counts as correct only if it exactly equals the target word.
- Cost check with Eq. 4 ($N=8$, $D=300$, $V=10^6$, $\log_2 V\approx19.93$): $Q = 2400 + 300\times19.93\approx 8380$.

## Concepts
- [[skip-gram-cbow]] — CBOW: predict middle word from averaged window (4 history + 4 future); Skip-gram: predict surrounding words from the current word; no hidden layer (pp. 4–5)
- [[word-embedding]] — continuous dense word vector learned by a network; here used with arithmetic on vectors (p. 2)
- [[softmax]] — here, normalization over the vocabulary; its cost is cut by hierarchical softmax (p. 3)
- [[hierarchical-softmax]] (new) — softmax over a Huffman binary tree; about $\log_2(\text{Unigram perplexity}(V))$ outputs evaluated (p. 3)
- [[language-model]] — here, NNLM and RNNLM, which predict a word from history (pp. 3–4)
- [[n-gram-model]] — simple model that can be trained on virtually all available data, trillions of words (p. 1)
- [[perplexity]] — used only in the Huffman-tree output count (p. 3)
- [[word-analogy-task]] (new) — answer "a : b :: c : ?" by the nearest word (cosine) to $b-a+c$, exact match required (pp. 5–6)
- [[training-complexity-Q]] (new) — per-example parameter accesses; total $O=E\times T\times Q$ (p. 3)
- [[nnlm-rnnlm]] (new) — feedforward and recurrent neural LMs, the baselines (pp. 3–4)

## Canonical instances
- [[king-queen-analogy]] — vector(King) − vector(Man) + vector(Woman) nearest to Queen, reported from [20] (p. 2)
- [[big-biggest-small-smallest]] — the paper's worked analogy question (p. 5)
- [[france-paris-germany-berlin]] — semantic relation (p. 5)
- [[semantic-syntactic-test-set]] — 14 relation types, Table 1 (p. 6)
- [[msr-sentence-completion]] — Skip-gram + RNNLM reaches 58.9% (p. 9)

## Bridges (candidates)
- [structural-analogy] CBOW/Skip-gram context prediction ↔ distributional hypothesis: vectors are shaped by the contexts a word occurs in (canon link; not stated in this unit)
- [structural-analogy] Hierarchical softmax over a Huffman tree ↔ information theory: short codes for frequent items reduce average work
- [same-math] Cosine-nearest-neighbour search for $b-a+c$ ↔ linear algebra: nearest-neighbour search by angle between vectors
- [metaphor] DistBelief replicas with a central parameter server ↔ distributed computing: many workers sharing one set of parameters

## Questions this raises
- Why does Skip-gram do so much better on semantic questions than CBOW (55 vs 24 in Table 3)? The paper reports it but does not explain it.
- How far does exact-match scoring under- or over-state the usefulness of vectors for applications? The authors only "believe" the two correlate (p. 6).
- What changes if multi-word entities such as *New York* are included? The test set excludes them (p. 6).
- How well do these vectors help other tasks, such as translation or knowledge-base extension, where results are only described as promising (p. 10)?

## Reading notes
- Printed page numbers equal pdf page numbers (offset 0). The unit is pp. 1–12 (text pp. 1–10, follow-up p. 11, references pp. 11–12). It is the arXiv v3 version (7 Sep 2013), as printed on p. 1.
- Text layer was clean. Equations (1)–(5) and Tables 1–8 were checked against the page images.
- Section 3.1 says the context vectors are "averaged", while Figure 1 labels the projection as "SUM" (pp. 4–5).
- Table 8 lists "big − bigger" with example "small: larger", as printed (p. 10).
- Table 2: 100-dim accuracy goes from 33.4 (391M) to 32.2 (783M), so improvement is not monotone (p. 7).
- The abstract says "less than a day" for 1.6B words. Table 5 gives 0.6 days for CBOW, but 2 days for Skip-gram, on 1.6B words (pp. 1, 8).
- The paper has no exercises.
