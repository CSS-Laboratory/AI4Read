---
id: radford-2019-gpt2/index
work: radford-2019-gpt2
type: work-map
units: [radford-2019-gpt2/main]
generated: deterministic
---

# Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). *Language Models are Unsupervised Multitask Learners*. OpenAI technical report.

## One digest
This work has a single digest, which is also its work-level summary: [[radford-2019-gpt2/main]].

## In one line
A large Transformer language model trained only to predict the next token on a big, varied web corpus (WebText) can begin to do many NLP tasks zero-shot, and it improves with model size.

## The gist
The paper asks whether a language model trained only to predict the next token can perform NLP tasks without any task-specific training (zero-shot). The authors build WebText (about 8 million web pages, 40 GB). They train Transformer language models of four sizes, up to 1.5B parameters (GPT-2), and specify tasks as plain text in the prompt. Results are strong on language-modeling and commonsense benchmarks and competitive with some supervised baselines on reading comprehension. They are weak on summarization, translation and question answering. Performance generally rises with model size. The authors suggest that tasks demonstrated naturally in text can be learned as a by-product of next-token prediction, but they call the practical performance "far from use-able".

**Prerequisites:** conditional probability and the product rule; logarithms and exponentials (perplexity); what a Transformer language model does at a high level; train/test splits.
