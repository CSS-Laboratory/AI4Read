---
id: mikolov-2013-regularities/main
work: mikolov-2013-regularities
unit: paper
pages: 746–751
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Linguistic Regularities in Continuous Space Word Representations

## L0 — One line
In word vectors learned by a recurrent neural network language model, a relation such as male/female or singular/plural appears as roughly one constant vector offset, so analogies can be solved with vector arithmetic and cosine similarity.

## L1 — The gist (≤ 120 words)
Do the word vectors learned inside a neural language model encode syntax and meaning? The authors take the input-layer weights of an RNN (recurrent neural network) language model as word vectors. They answer analogy questions "a is to b as c is to ?" by computing $y = x_b - x_a + x_c$ and returning the word whose vector has the highest cosine similarity to $y$. On a new 8000-question syntactic test, the best RNN vectors get 39.6% correct; the best LSA (latent semantic analysis) vectors get 16.5%. On SemEval-2012 Task 2 (semantic relation similarity), larger RNN vectors beat the previous best system. This matters because the vectors come from plain likelihood training, yet relations behave like linear offsets.

**Prerequisites:** vectors and dot products; cosine similarity; matrix–vector product; one-hot vectors; basic idea of a language model.

## L2 — Key ideas (5–10 bullets)
- Word vectors are the columns of the input matrix $\mathbf U$ of a recurrent neural network (RNN) language model, a model that predicts the next word. Training only maximizes data likelihood, and the model has no built-in knowledge of syntax or semantics (p. 747).
- Claim: word pairs sharing a relation are related by about the same constant offset, e.g. $x_{apple}-x_{apples}\approx x_{car}-x_{cars}$ (p. 746, p. 748).
- Method: $y=x_b-x_a+x_c$, then pick the nearest word by cosine similarity (p. 748).
- A new syntactic test set has 8000 analogy questions over 8 relations, each tested in both orderings (p. 748).
- Syntactic result: RNN-1600 gets 39.6%; the best LSA gets 16.5% (p. 749).
- Against other embeddings, restricted to a shared 36k vocabulary: Collobert–Weston (CW) vectors do poorly, and HLBL (hierarchical log-bilinear model) vectors do essentially as well as the RNN vectors (Table 3: RNN-80 19.0, HLBL-100 18.7) (p. 749).
- Semantic result: RNN-320, -640 and -1600 beat UTD-NB, the previous best system, on SemEval-2012 Task 2 (a relation-similarity test), without task-specific training (p. 750).
- Dimensionality matters: RNN performance rises with more dimensions (pp. 749–750).

## L3 — Walkthrough

### 1 Introduction (pp. 746–747)
Neural language models represent words as high-dimensional real vectors, obtained through a learned lookup table (p. 746). **Original proposers' view (as reported by the authors):** a distributed representation generalizes beyond n-gram models, because similar words are likely to have similar vectors and so share model updates (p. 746). The learned vectors can also serve other tasks (p. 746).

**Authors' finding:** regularities show up as constant vector offsets between word pairs with a shared relation. For singular/plural: $x_{apple}-x_{apples}\approx x_{car}-x_{cars}$ and $x_{family}-x_{families}\approx x_{car}-x_{cars}$ (p. 746). They report the same for a variety of semantic relations, measured with the SemEval-2012 task (p. 746). The abstract's example is that "King − Man + Woman" gives a vector very close to "Queen" (p. 746).

### 2 Related work (p. 747)
This section cites earlier distributed word representations, feed-forward and then recurrent neural language models for predicting the next word, hierarchical prediction used to reduce computation cost, distributed topic representations, and a semantically driven method for obtaining word representations (Bordes et al.). It says the early neural models gave outstanding word-prediction performance but showed the need for more computationally efficient models (p. 747).

### 3 Recurrent neural network model (p. 747)
The architecture has an input layer, a hidden layer with recurrent connections, and an output layer (Fig. 1). $\mathbf w(t)$ is the current word in 1-of-N coding (a vector with one 1, the rest 0). $\mathbf y(t)$ is a probability distribution over words. $\mathbf s(t)$ summarizes the sentence history. Both $\mathbf w$ and $\mathbf y$ have the dimensionality of the vocabulary (p. 747).

$$\mathbf s(t)=f(\mathbf U\mathbf w(t)+\mathbf W\mathbf s(t-1))\tag{1}$$
$$\mathbf y(t)=g(\mathbf V\mathbf s(t))\tag{2}$$
$$f(z)=\frac{1}{1+e^{-z}},\qquad g(z_m)=\frac{e^{z_m}}{\sum_k e^{z_k}}\tag{3}$$

Word representations are the columns of $\mathbf U$, one column per word. Training uses backpropagation to maximize the data log-likelihood (p. 747).

*(added step)* With $\mathbf w(t)$ one-hot, $\mathbf U\mathbf w(t)$ is just the column of $\mathbf U$ for that word. So $\mathbf U$ has one column per word and as many rows as the hidden size. The paper does not state the shapes of $\mathbf U$, $\mathbf W$, $\mathbf V$.

> **Intuition note:** The network is only trained to predict the next word. Yet the columns of $\mathbf U$, which it needs as inputs, end up carrying grammar- and meaning-related structure (p. 747).

### 4 Measuring linguistic regularity (pp. 747–748)
**4.1 Syntactic test set.** Questions have the form "$a$ is to $b$ as $c$ is to ___". 267M words of newspaper text were tagged with Penn Treebank POS tags. The authors chose the 100 most frequent words in each of four categories: JJR (comparative adjectives), NNS (plural nouns), NN_POS (possessive nouns) and VB (base verbs). Each word was randomly matched with 5 other words from its category, and variants were made as in Table 1 (p. 748). Table 1 lists 8 relations (each with two patterns, one per ordering) with 1000 questions each; for a given pattern and word-pair, both orderings occur. Example: *good:better rough:___*. The total is 8000 questions (p. 748).

**4.2 Semantic test set.** SemEval-2012 Task 2 has 79 fine-grained relations: 10 for training and 69 for testing. Each relation has 3 or 4 gold (prototype) word pairs. The task is to rank target pairs by how strongly the relation holds. Example: with prototype *clothing:shirt*, form the analogy "clothing is to shirt as dish is to bowl" and ask how valid it is (p. 748).

### 5 The vector offset method (p. 748)
**Assumption:** all pairs sharing a relation are related by the same constant offset in embedding space (Fig. 2). To answer $a{:}b\;c{:}d$ with $d$ unknown, take $x_a,x_b,x_c$ (all normalized to unit norm) and compute
$$y=x_b-x_a+x_c .$$
No word may sit exactly at $y$, so output the word with the greatest cosine similarity to $y$:
$$w^*=\arg\max_w \frac{x_w\cdot y}{\|x_w\|\,\|y\|}$$
When $d$ is given, as in the semantic test, use $\cos(x_b-x_a+x_c,\,x_d)$ (p. 748). The authors say the measure is qualitatively similar to Turney's (2012) relational similarity model. That model predicts similarity for the pairs $(x_b,x_d)$ and $(x_c,x_d)$, and dissimilarity for $(x_a,x_d)$ (p. 749). Fig. 2 shows the gender offsets (man→woman, uncle→aunt, king→queen) and, in another projection, singular/plural. In high-dimensional space, several relations can be embedded for one word (p. 749).

> **Intuition note:** If "female minus male" is nearly the same arrow everywhere, then adding that arrow to king should land near queen. Cosine search picks the nearest actual word, ignoring vector length.

### 6 Experiments (pp. 749–750)
**Setup.** The RNN toolkit gave vectors of dimension 80, 320 and 640, plus a composite of several systems with dimension 1600. They were trained on 320M words of Broadcast News with an 82k vocabulary. LSA was trained on the same data (p. 749).

**Syntactic results (Table 2, % correct).**

| Method | Adj. | Nouns | Verbs | All |
|---|---|---|---|---|
| LSA-320 (best LSA) | 11.3 | 18.1 | 20.7 | 16.5 |
| RNN-80 | 9.3 | 5.2 | 30.4 | 16.2 |
| RNN-320 | 18.2 | 19.0 | 45.0 | 28.5 |
| RNN-640 | 21.0 | 25.2 | 54.8 | 34.7 |
| RNN-1600 | 23.9 | 29.2 | 62.2 | 39.6 |

The authors conclude that the RNN vectors capture significantly more syntactic regularity than the LSA vectors, answering more than one in three questions correctly. Guessing gets a small fraction of a percent (p. 749).

**Other embeddings (Table 3).** The comparison uses the intersection of vocabularies: a 36k vocabulary and 6632 questions. The "All" scores are RNN-80 19.0, CW-50 4.5, CW-100 5.0, HLBL-50 13.0 and HLBL-100 18.7. CW vectors do poorly. HLBL vectors do essentially as well as the RNN vectors. The authors note that "these representations" were trained on 37M words, and that this "may indicate" a greater robustness of the HLBL method (p. 749).

**Semantic results (Table 4).** Each target pair's cosine score is computed against each prototype pair, and the scores are averaged. Metrics are Spearman's $\rho$ and MaxDiff accuracy, averaged over the 69 test relations (p. 749).

| Method | $\rho$ | MaxDiff |
|---|---|---|
| LSA-640 | 0.149 | 0.364 |
| RNN-80 | 0.211 | 0.389 |
| RNN-320 | 0.259 | 0.408 |
| RNN-640 | 0.270 | 0.416 |
| RNN-1600 | 0.275 | 0.418 |
| CW-50 / CW-100 | 0.159 / 0.154 | 0.363 / 0.363 |
| HLBL-50 / HLBL-100 | 0.149 / 0.146 | 0.363 / 0.362 |
| UTD-NB (prior best) | 0.230 | 0.395 |

RNN performance improves with dimension. Here CW and HLBL are comparable. RNN-320, RNN-640 and RNN-1600 beat UTD-NB, though the vectors were not trained or tuned for this task (p. 750). RNN-80 is below UTD-NB on both metrics.

### 7 Conclusion (p. 750)
The authors present a general vector offset method for finding linguistic regularities. They report almost 40% on the new syntactic set and a new state of the art on SemEval-2012. They call both results byproducts of unsupervised maximum-likelihood training on lots of text (p. 750).

> **Intuition note:** The training criterion is plain maximum likelihood on text. The authors call both results byproducts of it (p. 750).

## Toy example (ours, not from the paper)
Use 3-D unit vectors: man $=(1,0,0)$, woman $=(0,1,0)$, king $=(0.6,0,0.8)$, queen $=(0,0.6,0.8)$. Here $0.36+0.64=1$, so king and queen are unit length.

Question: man : king :: woman : ?

$y=x_{king}-x_{man}+x_{woman}=(0.6-1+0,\;0-0+1,\;0.8)=(-0.4,\,1,\,0.8)$.
$\|y\|=\sqrt{0.16+1+0.64}=\sqrt{1.8}\approx1.342$.

Cosines (all candidates have unit norm):
- queen: $y\cdot x=0+0.6+0.64=1.24$, so $1.24/1.342\approx0.924$.
- woman: $1/1.342\approx0.745$.
- king: $-0.24+0+0.64=0.40$, so $\approx0.298$.
- man: $-0.4$, so $\approx-0.298$.

Queen wins. The offsets are only approximately equal: king−man $=(-0.4,0,0.8)$ and queen−woman $=(0,-0.4,0.8)$. That "approximately" is all the method needs.

## Concepts
- [[vector]] — a word is a real-valued vector, the column of $\mathbf U$ for that word (p. 747)
- [[dot-inner-product]] — numerator $x_w\cdot y$ in the answer-selection rule (p. 748)
- [[cosine-similarity]] — the score used to find the word nearest to $y$; length is ignored (p. 748)
- [[norm]] — vectors are normalized to unit norm before computing $y$ (p. 748)
- [[matrix-as-transformation]] — $\mathbf U\mathbf w(t)$ selects a column of $\mathbf U$ when $\mathbf w$ is one-hot; the paper does not say this in matrix terms (p. 747)
- [[word-embedding]] (new) — learned vector representation of a word, here the input-layer weights (p. 747)
- [[vector-offset-analogy]] (new) — answering $a{:}b\;c{:}?$ with $x_b-x_a+x_c$ and nearest-cosine search (p. 748)
- [[one-hot-encoding]] (new) — "1-of-N coding" of the input word (p. 747)

## Canonical instances
- [[king-man-woman-queen]] — "King − Man + Woman" lands very close to "Queen" (p. 746)
- [[singular-plural-offset]] — $x_{apple}-x_{apples}\approx x_{car}-x_{cars}$ (p. 746)
- [[syntactic-analogy-test-set]] — 8000 questions, 8 relations (p. 748)
- [[semeval-2012-task2]] — 79 relations, prototype pairs such as clothing:shirt (p. 748)

## Bridges (candidates)
- [same-math] Embedding lookup $\mathbf U\mathbf w$ with one-hot $\mathbf w$ ↔ linear algebra: a matrix–vector product picks a column.
- [structural-analogy] Constant relation offset ↔ translation in vector space: one shared displacement maps many pairs.
- [same-math] Nearest word by $\frac{x_w\cdot y}{\|x_w\|\|y\|}$ ↔ cosine similarity as angle between vectors.
- [metaphor] Several relations in one space (Fig. 2) ↔ different directions in a high-dimensional space acting like independent coordinates.

## Questions this raises
- The paper does not say whether the input words $a$, $b$, $c$ are excluded from the cosine search. Does that change the accuracy?
- Why does likelihood training produce roughly constant offsets? The paper only reports that it does.
- Why do the HLBL vectors do so well with only 37M words? The authors only suggest greater robustness.
- How many of the 60% wrong answers are near misses?

## Reading notes
- Printed = pdf − 745 (pdf 1 = p. 746).
- The page text was clean. The equations and tables were checked against the page images.
- The formula in Section 5 prints the dot product as "$x_w y$" with no symbol; I rendered it as $x_w\cdot y$.
- Table 3's RNN-80 "All" score (19.0) differs from Table 2's (16.2). Table 3 uses the test set restricted to the shared 36k vocabulary (p. 749), which is the likely reason; the paper does not state the reason.
- Figure 2 is a schematic with word labels and arrows only; it has no numeric axes.
- The paper names the SemEval 2012 relation categories only through one example.
- 750–751.
