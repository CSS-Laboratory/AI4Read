---
id: bengio-2003-nplm/main
work: bengio-2003-nplm
unit: paper
pages: 1137–1155
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# A Neural Probabilistic Language Model (Bengio, Ducharme, Vincent, Jauvin, 2003)

## L0 — One line
A language model that learns a real-valued vector for each word, together with a neural network that predicts the next word from those vectors, generalizes to unseen word sequences better than smoothed n-gram models.

## L1 — The gist (≤ 120 words)
Language models must assign probabilities to word sequences that never appeared in training. N-gram models cope by gluing short seen fragments, which ignores long context and word similarity. The authors learn a distributed feature vector for every word and, jointly, a neural network that maps the context vectors to a softmax distribution over the next word. Similar words are expected to get nearby vectors, so one training sentence also raises the probability of many similar sentences. Training is costly, so they parallelize it across CPUs. On Brown and AP News, test perplexity differs by about 24% and 8% in favour of the network. The paper shows that learned embeddings plus neural next-word prediction work at scale.

**Prerequisites:** conditional probability and the chain rule; perplexity (exponential of the average negative log-likelihood; lower is better); n-gram model (next-word probabilities from the last $n-1$ words) with back-off and interpolation (falling back to shorter contexts when the long context is unseen); softmax (turns scores into positive probabilities summing to 1); tanh hidden layer; softmax and log-likelihood; a one-hidden-layer network trained by stochastic gradient ascent; matrix–vector shapes.

## L2 — Key ideas
- Modelling joint word distributions suffers from the curse of dimensionality: a test sequence is likely to differ from every training sequence, and the number of free parameters is potentially exponential in the sequence length (p. 1137). This motivates a smoother form of generalization.
- N-gram back-off and interpolation generalize by gluing short seen pieces. Their weakness, as the authors see it, is that they do not take into account contexts farther than 1 or 2 words (typically $n=3$), and they ignore word similarity (pp. 1138–1139).
- Core idea: give each word a feature vector in $\mathbb{R}^m$ with $m \ll |V|$. Write the next-word probability as a smooth function of the context vectors. Learn vectors and function together (p. 1139).
- Architecture: look-up in a shared matrix $C$, a tanh hidden layer, optional direct connections, and a softmax output (Eq. 1, pp. 1141–1143). Parameters grow linearly in $|V|$ and in $n$ (p. 1143).
- The output softmax dominates computation (about 99.7% in the AP example). The authors parallelize over output units on a CPU cluster with communication overhead of about 1/15 of the time (pp. 1144–1146).
- Results: the test-perplexity difference between the neural model and the best n-gram is about 24% (Brown) and about 8% (AP News) (the Table 1 caption puts the best n-gram about 24% above the network). It benefits from longer context, and mixing it with the trigram always helps (p. 1148).
- Extensions: an energy-based variant that also embeds the output word and handles out-of-vocabulary words, plus ideas for faster training and for polysemy (pp. 1150–1152).

## L3 — Walkthrough

### Abstract and 1. Introduction (pp. 1137–1140)
**Problem.** Statistical language modelling means learning the joint probability of word sequences. The curse of dimensionality makes this hard. Modelling 10 consecutive words with $|V| = 100{,}000$ gives potentially $100{,}000^{10} - 1 = 10^{50} - 1$ free parameters (p. 1137).

- Continuous variables are easier because smooth function classes (neural networks, Gaussian mixtures) generalize locally. For discrete variables, any change can alter the function drastically. With large vocabularies, most observed objects are almost maximally far apart in Hamming distance (pp. 1137–1138).
- The authors picture generalization as spreading probability mass from the training points into a neighbourhood. In high dimensions the mass must go where it matters, not uniformly around each point (p. 1138).
- Chain rule: $\hat P(w_1^T) = \prod_{t=1}^{T} \hat P(w_t \mid w_1^{t-1})$, with $w_i^j = (w_i, \dots, w_j)$ (p. 1138).
- N-gram approximation: $\hat P(w_t \mid w_1^{t-1}) \approx \hat P(w_t \mid w_{t-n+1}^{t-1})$. Unseen $n$-word combinations should not get zero probability, so back-off (Katz) and interpolated (Jelinek–Mercer) trigrams fall back to smaller contexts (p. 1138).
- Generatively, such a model "glues" short overlapping pieces of length 1 to $n$ seen in training. Two weaknesses: it ignores contexts beyond 1–2 words, and it ignores similarity between words (pp. 1138–1139).
- The authors' example: seeing "The cat is walking in the bedroom" should make "A dog was running in a room" almost as likely. The reason given is that cat/dog, the/a and room/bedroom have similar semantic and grammatical roles (p. 1139).

**Notation.** $v$ is a column vector, $v'$ its transpose, $A_j$ the $j$-th row of $A$, and $x.y = x'y$ (p. 1139).

**1.1 The idea (p. 1139–1140).**
1. Associate with each word a distributed word feature vector in $\mathbb{R}^m$.
2. Express the joint probability of a sequence through the feature vectors of its words.
3. Learn the vectors and the probability function's parameters simultaneously.

- $m$ is 30, 60 or 100 in the experiments, far below $|V|$ (e.g. 17,000) (p. 1139).
- The parameters are tuned to maximize the training log-likelihood, or a regularized version (weight decay, as in ridge regression). Vectors could be initialized with prior semantic knowledge (p. 1139).
- Why it works: if (dog, cat), (the, a), (bedroom, room), (is, was), (running, walking) play similar roles, probability transfers between all the combined sentences. The probability function is smooth in the feature values, so a small change in features gives a small change in probability. One training sentence therefore raises the probability of a combinatorial number of "neighbours" in sentence space (p. 1140).

*Intuition note.* Instead of counting exact word strings, the model places words in a space where similar words sit close together. A sentence seen once then lifts many sentences made of nearby words.

**1.2 Relation to previous work (pp. 1140–1141).**
- Bengio & Bengio (2000a,b) decompose a joint distribution into conditionals computed by a left-to-right neural network. The new model must handle variable-length data, where all variables are the same kind of object (words). It therefore shares parameters across positions (p. 1140).
- It applies the old connectionist idea of distributed representations (Hinton 1986; Elman 1990) at large scale. The authors aim at modelling the distribution of word sequences, not at learning the roles of words in sentences (p. 1140).
- Xu & Rudnicky (2000) proposed a neural language model independently, but with no hidden units and one input word. That limits it to roughly unigram and bigram statistics (p. 1140).
- Class-based n-gram approaches give each word a discrete class (hard or soft partition). Here similarity is a continuous learned vector. Class-based n-grams are included as baselines (pp. 1140–1141).
- In information retrieval, word vectors from co-occurrence (LSI) have been used. The difference here is that the representation is learned to represent the sequence distribution compactly. The authors tried fixed word features from principal components of co-occurrence counts, "unsuccessfully", which suggests joint learning is very useful (p. 1141).

### 2. A Neural Model (pp. 1141–1143)
**Setup.** The training set is $w_1 \cdots w_T$ with $w_t \in V$, $V$ finite. The goal is a model $f(w_t, \dots, w_{t-n+1}) = \hat P(w_t \mid w_1^{t-1})$ with high out-of-sample likelihood. Perplexity is the geometric average of $1/\hat P(w_t \mid w_1^{t-1})$, which equals the exponential of the average negative log-likelihood. Constraint: $\sum_{i=1}^{|V|} f(i, w_{t-1}, \dots, w_{t-n+1}) = 1$ and $f > 0$ (p. 1141).

**Two parts (p. 1141).**
1. A map $C$ from word index $i$ to $C(i) \in \mathbb{R}^m$. In practice $C$ is a $|V| \times m$ matrix of free parameters. Row $i$ is $C(i)$.
2. A function $g$ taking $(C(w_{t-n+1}), \dots, C(w_{t-1}))$ to a probability vector over $V$.

$$f(i, w_{t-1}, \dots, w_{t-n+1}) = g(i, C(w_{t-1}), \dots, C(w_{t-n+1}))$$

$C$ is shared across all context positions. $g$ may be feed-forward, recurrent, or another parametrized function with parameters $\omega$. The overall parameters are $\theta = (C, \omega)$ (p. 1142, Figure 1).

**Training objective (p. 1142):**
$$L = \frac{1}{T}\sum_t \log f(w_t, w_{t-1}, \dots, w_{t-n+1}; \theta) + R(\theta)$$
$R$ is a weight-decay penalty on the network weights and on $C$, but not on the biases (p. 1142).

**Scaling.** Free parameters scale linearly in $|V|$ and in $n$. The factor in $n$ could become sub-linear with more sharing (time-delay or recurrent networks) (p. 1142).

**Network used in most experiments (pp. 1142–1143).** There is one tanh hidden layer, with optional direct connections from word features to outputs. $C$ is effectively a first hidden layer with no non-linearity, since one "would not add anything useful". Softmax output:
$$\hat P(w_t \mid w_{t-1}, \dots, w_{t-n+1}) = \frac{e^{y_{w_t}}}{\sum_i e^{y_i}}$$
$$y = b + Wx + U\tanh(d + Hx) \tag{1}$$
with $x = (C(w_{t-1}), C(w_{t-2}), \dots, C(w_{t-n+1}))$ the concatenation of the context vectors. $W$ is optionally zero (no direct connections) (p. 1143).

**Shapes.** $h$ = number of hidden units, $m$ = features per word.

| Parameter | Shape |
|---|---|
| $b$ (output biases) | $\lvert V\rvert$ |
| $d$ (hidden biases) | $h$ |
| $U$ | $\lvert V\rvert \times h$ |
| $W$ | $\lvert V\rvert \times (n-1)m$ |
| $H$ | $h \times (n-1)m$ |
| $C$ | $\lvert V\rvert \times m$ |
| $x$ | $(n-1)m$ |

$\theta = (b, d, W, U, H, C)$. Number of free parameters: $|V|(1 + nm + h) + h(1 + (n-1)m)$. The dominating factor is $|V|(nm + h)$ (p. 1143).

*Caveat (authors).* In theory, if weight decay acts on $W$ and $H$ but not on $C$, then $W$ and $H$ could go to zero while $C$ blows up. This was not observed in practice with stochastic gradient ascent (p. 1143).

**SGD update** after each training word, with learning rate $\varepsilon$:
$$\theta \leftarrow \theta + \varepsilon \frac{\partial \log \hat P(w_t \mid w_{t-1}, \dots, w_{t-n+1})}{\partial \theta}$$
Many parameters need no update: the vectors $C(j)$ of words $j$ not in the input window (p. 1143).

**Mixture of models.** Performance improves when the network's probabilities are combined with an interpolated trigram. The mixture weight is either fixed at 0.5, learned by maximum likelihood on the validation set, or conditional on context frequency, as in the trigram's own interpolation (p. 1143).

*Intuition note.* Embedding look-up is the same table for every position. The tanh layer mixes the context vectors, and the softmax turns scores into a distribution over all of $V$. Parameters grow with $|V|$ and $n$, not exponentially.

### 3. Parallel Implementation (pp. 1143–1147)
The neural model needs much more computation than n-grams. Obtaining one n-gram probability does not require computing probabilities for all words, thanks to easy normalization of relative frequencies. The network's bottleneck is the output-layer activations (p. 1143).

**3.1 Data-parallel (shared memory) (p. 1144).** Each processor handles different examples and updates shared parameters. A first version with locks was extremely slow, since processors waited for each other. An asynchronous version, where updates may be overwritten, adds a little noise. The noise seems very small and did not apparently slow training. Large shared-memory machines are expensive, so clusters were preferred (p. 1144).

**3.2 Parameter-parallel (cluster) (pp. 1144–1147).**
- Exchanging all parameters frequently is too costly (almost 100 MB for the largest network). Instead, output units are split across CPUs. Each CPU computes the unnormalized probabilities for its block and updates its own output weights. The CPUs only communicate the softmax normalization factor and the gradients on the hidden layer ($a$) and word-feature layer ($x$). All CPUs duplicate the earlier steps (feature selection, hidden activation) (p. 1144).
- **Cost example (AP):** $|V| = 17{,}964$, $h = 60$, $n = 6$, $m = 100$. Per-example cost is approximately $|V|(1+nm+h) + h(1+nm) + nm$ (output, hidden and feature terms). The fraction in the output weighted sums is
$$\frac{|V|(1+(n-1)m+h)}{|V|(1+(n-1)m+h) + h(1+(n-1)m) + (n-1)m} \approx 99.7\%$$
(pp. 1144–1145). Duplicating the small remainder does not hurt for a few dozen processors (p. 1145).
- **Hardware:** a cluster of 1.2 GHz Athlon processors (32 × 2 CPUs), Myrinet network, MPI library (p. 1145).
- **Algorithm for CPU $i$ of $M$.** The block starts at $\text{start}_i = i \times \lceil |V|/M \rceil$, with length $\min(\lceil |V|/M \rceil, |V| - \text{start}_i)$ (p. 1145).
  - *Forward:* (a) $x(k) \leftarrow C(w_{t-k})$; (b) $o \leftarrow d + Hx$, $a \leftarrow \tanh(o)$; (c) for each $j$ in the block, $y_j \leftarrow b_j + a.U_j$ (plus $x.W_j$ with direct connections), $p_j \leftarrow e^{y_j}$, $s_i \leftarrow s_i + p_j$; (d) share $S = \sum_i s_i$ with MPI Allreduce; (e) $p_j \leftarrow p_j / S$; (f) CPU 0 accumulates $L = \log p_{w_t}$ (p. 1145).
  - *Backward/update:* (a) for each $j$: $\partial L/\partial y_j \leftarrow \mathbf{1}_{j==w_t} - p_j$; $b_j \leftarrow b_j + \varepsilon\,\partial L/\partial y_j$; $\partial L/\partial x \leftarrow \partial L/\partial x + (\partial L/\partial y_j) W_j$ (direct only); $\partial L/\partial a \leftarrow \partial L/\partial a + (\partial L/\partial y_j) U_j$; $W_j \leftarrow W_j + \varepsilon\,(\partial L/\partial y_j)\,x$ (direct only); $U_j \leftarrow U_j + \varepsilon\,(\partial L/\partial y_j)\,a$. (b) Allreduce-sum $\partial L/\partial x$ and $\partial L/\partial a$. (c) $\partial L/\partial o_k \leftarrow (1 - a_k^2)\,\partial L/\partial a_k$; $\partial L/\partial x \leftarrow \partial L/\partial x + H'\,\partial L/\partial o$; $d \leftarrow d + \varepsilon\,\partial L/\partial o$; $H \leftarrow H + \varepsilon\,(\partial L/\partial o)\,x'$. (d) $C(w_{t-k}) \leftarrow C(w_{t-k}) + \varepsilon\,\partial L/\partial x(k)$, where $\partial L/\partial x(k)$ is the $k$-th length-$m$ block of $\partial L/\partial x$ (pp. 1145–1146).
- Weight decay is omitted from the sketch. It can be added by subtracting (decay × learning rate × parameter) at each update. Parameters are updated directly, not via a gradient vector, for speed, since memory access limits speed (p. 1146).
- **Numerical stability:** subtract the maximum $Q = \max_i q_i$ of the $y_j$ before exponentiating, with $q_i$ the block maximum and one extra Allreduce. Then $p_j \leftarrow e^{y_j - Q}$, so at least one $p_j$ is non-zero and the largest exponent argument is 0 (the exponential is at most 1) (p. 1146).
- **Result:** communication overhead was only 1/15 of the total time for one epoch, so the speed-up is almost perfect on a fast network (p. 1146).
- **Slow networks:** communicating every $K$ examples (mini-batch) might still give an efficient parallelization. This saves latency, not data volume, but may lose in convergence time if $K$ is large, as batch gradient descent is generally much slower than stochastic gradient descent (pp. 1146–1147).

*Intuition note.* The hidden layer is small, but the output layer has one unit per vocabulary word. Splitting those units across machines parallelizes almost all the work, and only a few numbers (normalizer, gradients) must be exchanged.

### 4. Experimental Results (pp. 1147–1149)
**Data.**
- *Brown:* 1,181,041 words. The first 800,000 are for training, the next 200,000 for validation (model selection, weight decay, early stopping), and the last 181,041 for testing. There are 47,578 distinct words. Words with frequency ≤ 3 were merged into one symbol, giving $|V| = 16{,}383$ (p. 1147).
- *AP News (1995–96):* train 13,994,528 words, validation 963,138, test 963,071. The vocabulary of 148,721 was reduced to $|V| = 17{,}964$ by keeping the most frequent words and punctuation, lower-casing, mapping numbers, rare words and proper nouns to special symbols (p. 1147).
- *Learning rate:* $\varepsilon_t = \varepsilon_0/(1 + rt)$, with $\varepsilon_0 = 10^{-3}$, $r = 10^{-8}$ (heuristic), $t$ = number of updates (p. 1147).

**4.1 N-gram baselines (pp. 1147–1148).** Interpolated trigram (Jelinek–Mercer): with $q_t = l(\text{freq}(w_{t-1}, w_{t-2}))$ the discretized context frequency, where $l(x) = \lceil -\log((1+x)/T) \rceil$ and $T$ is the training-set size:
$$\hat P(w_t \mid w_{t-1}, w_{t-2}) = \alpha_0(q_t)p_0 + \alpha_1(q_t)p_1(w_t) + \alpha_2(q_t)p_2(w_t \mid w_{t-1}) + \alpha_3(q_t)p_3(w_t \mid w_{t-1}, w_{t-2})$$
- Weights satisfy $\alpha_i(q_t) \ge 0$ and $\sum_i \alpha_i(q_t) = 1$.
- Base predictors: $p_0 = 1/|V|$, and $p_1, p_2, p_3$ are the unigram, bigram and trigram relative frequencies.
- Motivation: when the context is frequent, $p_3$ is most reliable. Otherwise lower orders are.
- One weight set per frequency bin. The weights are estimated by EM in about 5 iterations on the validation set (pp. 1147–1148).

Other baselines use the SRILM toolkit: modified Kneser–Ney back-off and class-based n-grams. The validation set chose the order and the number of classes. End-of-sentence tokens got no special status, and all tokens count equally in perplexity (p. 1148).

**4.2 Results (pp. 1148–1149).**
- Brown converged after about 10–20 epochs. On AP only 5 epochs were run (over 3 weeks on 40 CPUs), and the authors saw no sign of overfitting (possibly because of the few epochs). Early stopping was needed only on Brown. Weight decay was $10^{-4}$ (Brown) and $10^{-5}$ (AP) (p. 1148).
- Word features were randomly initialized. The authors suspect knowledge-based initialization might do better (p. 1148).

**Selected test perplexities (Table 1, Brown; Table 2, AP).**

| Model | Test perplexity |
|---|---|
| Brown, MLP1 ($n=5$, $h=50$, $m=60$, direct, no mix) | 268 |
| Brown, MLP2 (same, mixed) | 257 |
| Brown, MLP3 ($h=0$, no mix) | 310 |
| Brown, MLP9 ($h=100$, $m=30$, no direct, no mix) | 276 |
| Brown, MLP10 (same, mixed) | 252 |
| Brown, deleted interpolation trigram | 336 |
| Brown, Kneser–Ney back-off ($n=3,4,5$) | 323, 321, 321 |
| Brown, best class-based (500 classes, $n=3,4,5$) | 312 |
| AP, MLP10 ($n=6$, $h=60$, $m=100$, direct, mix) | 109 |
| AP, deleted interpolation | 132 |
| AP, KN back-off ($n=3,4,5$) | 127, 119, 117 |

(p. 1149, Tables 1–2 (p. 1150).) The table's mix column means a 0.5/0.5 average with the trigram (p. 1149).

**Conclusions drawn by the authors (p. 1148).**
- The neural network is significantly better than the best n-gram: a test-perplexity difference of about 24% on Brown and about 8% on AP News. The comparison is between the MLP and the n-gram that worked best on validation. Per the caption, the deleted-interpolation trigram is 33% above the network with the lowest validation perplexity, and the best n-gram (class-based, 500 classes) is 24% above it (p. 1149).
- The network can use more context: on Brown, going from 2 to 4 words of context helped the network, not the n-grams (p. 1148).
- Hidden units help (MLP3 vs MLP1, MLP4 vs MLP2). Mixing with the trigram always reduces perplexity, which suggests that the two make errors in different places (p. 1148).
- The results do not settle whether direct connections help. On the smaller corpus, no direct connections seemed to give better generalization but took twice as long to converge (20 vs 10 epochs). The authors' "reasonable interpretation" is that direct connections add capacity and speed up learning of the linear part, while the tight hidden bottleneck may force better generalization (pp. 1148–1149).
- On AP the class-based model did not appear to help, and the high-order Kneser–Ney back-off was the best n-gram (p. 1149).

*Intuition note.* The gain is larger on the smaller corpus (24% vs 8%). Mixing with the trigram helps, which suggests that the two models make errors in different places.

### 5. Extensions and Future Work (pp. 1149–1152)
**5.1 Energy minimization network (pp. 1150–1151).** The main model embeds only input words, and most parameters sit in the output layer, where output-word similarity is not exploited. In the variant (after Hinton's products of experts) the output word is also embedded:
$$E(w_{t-n+1}, \dots, w_t) = v.\tanh(d + Hx) + \sum_{i=0}^{n-1} b_{w_{t-i}}, \qquad x = (C(w_t), C(w_{t-1}), \dots, C(w_{t-n+1}))$$
- $E$ is low for likely subsequences. It acts as an unnormalized log-probability (negative energy) for the joint occurrence of the words.
- Conditional probability, by normalizing over the candidate last word $i$ (costly):
$$\hat P(w_t \mid w_{t-1}, \dots, w_{t-n+1}) = \frac{e^{-E(w_{t-n+1}, \dots, w_t)}}{\sum_i e^{-E(w_{t-n+1}, \dots, w_{t-1}, i)}}$$
- Computation is comparable to the earlier model, and the parameter count can be matched if $v$ is indexed by the target word. After normalization only $b_{w_t}$ remains, since any linear function of the $w_{t-i}$ for $i>0$ cancels (p. 1150).
- In the products-of-experts view the hidden units are the experts: the joint probability is proportional to the exponential of a sum of terms $v_j \tanh(d_j + H_j x)$. Because the sequence probability is decomposed into conditionals, the gradient is tractable. This is not so for products of HMMs, which need approximate training such as contrastive divergence (pp. 1150–1151).
- It can be seen as an extension of maximum-entropy models, with the basis functions (hidden units) learned jointly by penalized maximum likelihood instead of an outer loop with greedy feature selection (p. 1151).
- An importance-sampling speed-up gives a 100-fold training speed-up (Bengio & Senécal 2003) (p. 1151).

**Out-of-vocabulary words (p. 1151).** This architecture can handle new words, even assign them a probability. Initialize a new word $j \notin V$, observed in a context where the network gave $\hat P(i \mid w_{t-n+1}^{t-1})$ to $i \in V$:
$$C(j) \leftarrow \sum_{i \in V} C(i)\,\hat P(i \mid w_{t-n+1}^{t-1})$$
Then add $j$ to $V$ and recompute. This needs only a renormalization for all words, except for one word that needs a pass through the network (the source writes "word $i$" here; I read it as the new word $j$) (p. 1151).

**5.2 Other future work (pp. 1151–1152).** The authors list:
1. Decompose into sub-networks by clustering words.
2. Use a tree of networks over word classes, with potential time savings by a factor $|V|/\log|V|$.
3. Propagate gradients only from a subset of output words (e.g. the likeliest under a trigram, or words where the trigram performs poorly; if coupled to a speech recognizer, only the scores of acoustically ambiguous words need computing).
4. Add prior knowledge (WordNet, parts of speech, a stochastic grammar), and use time-delay or recurrent networks for longer context.
5. Interpret the learned features, starting with $m = 2$. They believe meaningful representations will need large corpora, especially for larger $m$.
6. Polysemous words are "probably not well served", since each word has one point. They are investigating several points per word.

### 6. Conclusion (pp. 1152–1153)
- The authors claim much better perplexity than the smoothed trigram, "with differences between 10 and 20%" (p. 1152). (Section 4 reports differences of about 24% (Brown) and about 8% (AP) against the best n-gram, and, on Brown, a deleted-interpolation trigram 33% above the best-validated network. See Reading notes.)
- They believe the main reason for the gain is that the learned distributed representation is used, so that each training sentence informs the model about a combinatorial number of others (p. 1152).
- Priorities: speed-up techniques and more capacity for corpora of hundreds of millions of words. They suggest time-delay or recurrent networks to enlarge the input window to maybe a paragraph (p. 1152).
- Replacing tables of conditional probabilities by compact, smoother distributed representations shifts the difficulty to computation. Computation and memory scale linearly, not exponentially, with the number of conditioning variables (pp. 1152–1153).

## Toy example (ours, not from the paper)
Setup: $V = \{\text{cat}, \text{dog}, \text{sleeps}, \text{runs}\}$, $m = 2$, $n = 2$ (one context word), no hidden layer ($U$ ignored), biases 0, so $y = Wx$ with $W$ of shape $4 \times 2$. Assume training produced $C(\text{cat}) = (1, 0)$ and $C(\text{dog}) = (0.9, 0.1)$, and output rows $W_{\text{cat}} = W_{\text{dog}} = (0,0)$, $W_{\text{sleeps}} = (2,0)$, $W_{\text{runs}} = (1,1)$. The text of the corpus contained "cat sleeps" but never "dog" as a context (this is our assumption).

- Context "cat": $y = (0, 0, 2, 1)$. Exponentials: $1, 1, 7.389, 2.718$, sum $= 12.107$. $P(\text{sleeps}) = 7.389/12.107 = 0.610$; $P(\text{runs}) = 0.2245$.
- Context "dog": $x = (0.9, 0.1)$. $y_{\text{sleeps}} = 2(0.9) = 1.8$; $y_{\text{runs}} = 0.9 + 0.1 = 1.0$; the others are 0. Exponentials: $1, 1, 6.050, 2.718$, sum $= 10.768$. $P(\text{sleeps}) = 6.050/10.768 = 0.562$.

A count-based bigram has count 0 for "dog sleeps". The embedding model gives 0.562, because the vectors of cat and dog are close and the score is a smooth function of $x$.

## Concepts
- [[language model]] — a joint probability over word sequences, factored as a product of next-word conditionals (p. 1138)
- [[n-gram model]] — table of next-word probabilities given the last $n-1$ words; back-off and interpolation handle unseen contexts (p. 1138)
- [[perplexity]] — geometric average of $1/\hat P(w_t \mid w_1^{t-1})$, the exponential of the average negative log-likelihood (p. 1141)
- [[cross-entropy / log-loss]] — here the average log-likelihood $L$ is maximized, plus regularization (p. 1142)
- [[word embedding]] — here the "distributed word feature vector" $C(i) \in \mathbb{R}^m$, row $i$ of a learned matrix, trained jointly with the predictor (p. 1139)
- [[softmax]] — output layer, guaranteeing positive probabilities that sum to 1 (p. 1142)
- [[curse-of-dimensionality]] (new) — sequences in testing differ from training ones; parameters are potentially exponential in sequence length (p. 1137)
- [[distributed-representation]] (new) — a word is a point in $\mathbb{R}^m$, with $m \ll |V|$, rather than a discrete symbol or class (p. 1139)
- [[class-based-ngram]] (new) — n-gram with words mapped to discrete classes, a baseline here (p. 1141)
- [[energy-based-model]] (new) — the variant scoring a word subsequence with energy $E$, normalized by a softmax over the last word (p. 1150)

## Canonical instances
- [[cat-dog-bedroom-example]] — one seen sentence should raise the probability of its similar-word variants (pp. 1139–1140)
- [[brown-corpus-experiment]] — test-perplexity difference of about 24% from the best n-gram (pp. 1147–1149)
- [[ap-news-experiment]] — test-perplexity difference of about 8% from the best n-gram, with a $n=6$ network (pp. 1149–1150)
- [[parameter-parallel-softmax]] — output units split across CPUs; about 99.7% of the compute is in the output layer (pp. 1144–1145)

## Bridges (candidates)
- [same-math] Eq. 1 with softmax and log-likelihood training ↔ LLM: next-token prediction trained by cross-entropy (the same objective with a different $g$)
- [same-math] Embedding matrix $C$ (look-up of rows) ↔ word embedding: learned token embedding table
- [same-math] Energy $E$ normalized by $e^{-E}/\sum e^{-E}$ ↔ softmax: a softmax over scores $-E$
- [structural-analogy] Interpolated trigram with frequency-dependent weights $\alpha_i(q_t)$ ↔ ensemble methods: weights depending on how reliable each component is
- [metaphor] "Spreading probability mass to neighbours" ↔ non-parametric density estimation: kernel smoothing around training points

## Questions this raises
- Does the gain come from the embeddings or from the non-linear hidden layer? The paper tests hidden units (MLP3 vs MLP1), but not embeddings separately.
- How does the network behave with much longer context and corpora of hundreds of millions of words, if compute is the limit?
- Can one embedding per word handle polysemy, or are several points per word needed (item 6 of Section 5.2)?
- What do the learned features encode? The authors suggest looking at $m = 2$ (item 5 of Section 5.2).

## Reading notes
- Printed pages 1137–1155 correspond to pdf 1–19 (printed = pdf + 1136). Page 1153 ends the Conclusion and gives the acknowledgments; pages 1153–1155 are acknowledgments and references.
- **Source inconsistency:** the text on p. 1144 gives the per-example cost with $nm$, but the 99.7% fraction on p. 1145 uses $(n-1)m$. I checked the fraction with $(n-1)m = 500$ and it gives about 99.7%.
- **Source inconsistency:** the Conclusion (p. 1152) says differences of "between 10 and 20%", but Section 4.2 gives about 24% (Brown) and about 8% (AP) against the best n-gram. The Conclusion also says "more than a million examples" and "above 15 million words". Section 4 gives about 14 million training words (AP), and about 15.9 million in all three AP splits.
- Table 1 leaves the train column blank for mixed models. Table 2 has no training perplexities.
- Equations in the text layer are partly garbled, but the images were checked. I could read all equations from them. On p. 1151 the out-of-vocabulary paragraph says "except for word $i$" where $j$ seems meant.
