---
id: xie-2022-icl/index
work: xie-2022-icl
type: work-map
units: [xie-2022-icl/main]
generated: deterministic
---

# Xie, S. M., Raghunathan, A., Liang, P., & Ma, T. (2022). *An Explanation of In-context Learning as Implicit Bayesian Inference*. ICLR 2022. arXiv:2111.02080.

## One digest
This work has a single digest, which is also its work-level summary: [[xie-2022-icl/main]].

## In one line
If pretraining documents are generated from a latent document-level concept (a mixture of HMMs), a language model that fits this distribution can do in-context learning by implicitly inferring the shared concept of the prompt examples (Bayesian inference), provably so (asymptotically optimal error) under the paper's assumptions and a distinguishability condition.

## The gist
Large LMs can learn a task from a few input-output examples in the prompt, although they were never trained to do so and prompts look unlike natural text. The paper asks what makes this possible. Answer: if pretraining documents come from a mixture of HMMs with a latent concept, an LM that fits the pretraining distribution implicitly does Bayesian inference over that concept. Under the paper's assumptions and a distinguishability condition, its error is asymptotically optimal despite the prompt/pretraining mismatch. In two further settings, error bounds still shrink with example length. A small synthetic dataset (GINC) shows Transformers and LSTMs reproducing several real-world phenomena. This is a first formal step toward explaining in-context learning.

**Prerequisites:** Bayes' rule and marginalization; Markov chains and hidden Markov models (HMMs); KL divergence; total-variation distance; Taylor expansion and Fisher information (for Theorem 2); matrix–vector notation.
