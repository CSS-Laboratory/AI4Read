---
id: mikolov-2013-efficient/index
work: mikolov-2013-efficient
type: work-map
units: [mikolov-2013-efficient/main]
generated: deterministic
---

# Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). *Efficient Estimation of Word Representations in Vector Space*. ICLR 2013 Workshop. arXiv:1301.3781.

## One digest
This work has a single digest, which is also its work-level summary: [[mikolov-2013-efficient/main]].

## In one line
Dropping the non-linear hidden layer gives two very cheap models, CBOW and Skip-gram, that learn word vectors from billions of words, and simple vector arithmetic on those vectors can answer syntactic and semantic analogy questions.

## The gist
Earlier neural models learned word vectors, but, as far as the authors know, none had been trained successfully on more than a few hundred million words, and most were much costlier to train. The authors explore simpler, cheaper models that may represent words less precisely but can possibly be trained on much more data. They propose CBOW (predict a word from its context) and Skip-gram (predict context words from a word), both without a hidden layer. They test the vectors with analogy questions such as "big : biggest :: small : ?", answered by vector arithmetic and cosine distance. On their new test set, the new models match or beat earlier models at much lower cost. Skip-gram is much better on semantic questions. Word vectors could become a building block for later NLP systems.

**Prerequisites:** vectors and cosine similarity; softmax and neural-network layers (input, hidden, output); stochastic gradient descent; the idea of a language model.
