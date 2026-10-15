---
id: vaswani-2017-transformer/index
work: vaswani-2017-transformer
type: work-map
units: [vaswani-2017-transformer/main]
generated: deterministic
---

# Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need*. Advances in Neural Information Processing Systems 30 (NeurIPS 2017). arXiv:1706.03762.

## One digest
This work has a single digest, which is also its work-level summary: [[vaswani-2017-transformer/main]].

## In one line
A sequence-to-sequence model built only from attention and position-wise feed-forward layers (the Transformer), with no recurrence or convolution, matched or beat the best translation systems at a fraction of the training cost.

## The gist
Question: can sequence transduction (mapping an input sequence to an output sequence, e.g. translation) work without recurrent or convolutional layers? Answer: yes. The Transformer is an encoder–decoder built only from attention and position-wise feed-forward layers. Positional encodings add word order, and multi-head attention offsets the resolution lost by averaging. It reached 28.4 BLEU (a translation score) on WMT 2014 (a benchmark) English-to-German and 41.8 on English-to-French (Table 2), trained significantly faster than recurrent or convolutional models, and also did well on English constituency parsing (predicting phrase-structure trees). It matters because attention links any two positions in a constant number of operations, and computation parallelizes across positions.

**Prerequisites:** matrix multiplication and shapes; softmax; dot product; mean and variance of sums of independent variables; basic idea of a neural network layer, dropout, and the Adam optimizer; big-O notation.
