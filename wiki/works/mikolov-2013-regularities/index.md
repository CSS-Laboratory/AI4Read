---
id: mikolov-2013-regularities/index
work: mikolov-2013-regularities
type: work-map
units: [mikolov-2013-regularities/main]
generated: deterministic
---

# Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic regularities in continuous space word representations. In *Proceedings of NAACL-HLT 2013* (pp. 746–751). Association for Computational Linguistics.

## One digest
This work has a single digest, which is also its work-level summary: [[mikolov-2013-regularities/main]].

## In one line
In word vectors learned by a recurrent neural network language model, a relation such as male/female or singular/plural appears as roughly one constant vector offset, so analogies can be solved with vector arithmetic and cosine similarity.

## The gist
Do the word vectors learned inside a neural language model encode syntax and meaning? The authors take the input-layer weights of an RNN (recurrent neural network) language model as word vectors. They answer analogy questions "a is to b as c is to ?" by computing $y = x_b - x_a + x_c$ and returning the word whose vector has the highest cosine similarity to $y$. On a new 8000-question syntactic test, the best RNN vectors get 39.6% correct; the best LSA (latent semantic analysis) vectors get 16.5%. On SemEval-2012 Task 2 (semantic relation similarity), larger RNN vectors beat the previous best system. This matters because the vectors come from plain likelihood training, yet relations behave like linear offsets.

**Prerequisites:** vectors and dot products; cosine similarity; matrix–vector product; one-hot vectors; basic idea of a language model.
