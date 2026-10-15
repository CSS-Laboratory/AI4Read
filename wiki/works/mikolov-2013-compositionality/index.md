---
id: mikolov-2013-compositionality/index
work: mikolov-2013-compositionality
type: work-map
units: [mikolov-2013-compositionality/main]
generated: deterministic
---

# Mikolov, T., Sutskever, I., Chen, K., Corrado, G., & Dean, J. (2013). *Distributed Representations of Words and Phrases and their Compositionality*. Advances in Neural Information Processing Systems 26 (NeurIPS 2013). arXiv:1310.4546.

## One digest
This work has a single digest, which is also its work-level summary: [[mikolov-2013-compositionality/main]].

## In one line
Simple extensions of the Skip-gram model (subsampling frequent words, negative sampling, treating detected phrases as single tokens) improve vector quality and training speed, and the vectors can often be combined by simple addition.

## The gist
The paper asks how to make Skip-gram word vectors better and faster to train, and how to handle phrases whose meaning is not the sum of their words ("Air Canada"). The authors discard very frequent words at random, replace the full softmax with a simple "real vs noise" objective (negative sampling), and merge frequently co-occurring word pairs into single tokens. They test on analogy tasks for words and phrases. A model trained on about 33 billion words reaches 72% on phrase analogies. Adding two word vectors often gives a vector near a meaningful third item. The authors released their code as the open-source word2vec project.

**Prerequisites:** softmax and logistic sigmoid; log probability; dot product and cosine similarity; the idea of a word vector.
