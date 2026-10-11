---
field: Large language models
slug: llm
layer: application
compiled: 2026-10-11
---
# Large language models — Canon

## Scope
This catalog covers how large language models (LLMs) came to be, how they work, and what they mean. It runs along eight strands: the prehistory of neural language modeling, the Transformer architecture and its GPT/BERT descendants, scaling and post-training (scaling laws, RLHF, Constitutional AI, DPO), capabilities and reasoning (in-context learning, chain-of-thought, the emergence debate), mechanistic interpretability, philosophical and cognitive critiques of "meaning," LLMs as tools and subjects for social science, and textbooks and courses. Shannon's 1948/1951 n-gram and entropy-of-English work, and Harris (1954) and Firth (1957) on distributional semantics, are treated as cross-references to the information-theory and philosophy-of-language canons, so they are not repeated here. The list was triangulated against Stanford CS224N (Winter 2026 schedule), Stanford CS336 "Language Modeling from Scratch" (Spring 2026) and Princeton COS 597G "Understanding Large Language Models" (Fall 2022). Out of scope: engineering detail such as GPU kernels, parallelism and inference serving, multimodal models, and fast-moving product reports. Useful supplements that are not catalogued as items: the CS224N and CS336 lecture materials, the 3Blue1Brown deep-learning videos, Goodfellow/Bengio/Courville *Deep Learning*, Raschka's *Build a Large Language Model (From Scratch)*, Christiano et al. (2017) on RLHF, and Bail (2024, PNAS).

## Canon

### Strand: Prehistory — from n-grams to word vectors

#### bengio-2003-nplm
- **type:** paper
- **citation:** Bengio, Y., Ducharme, R., Vincent, P., & Jauvin, C. (2003). *A Neural Probabilistic Language Model*. Journal of Machine Learning Research, 3, 1137–1155.
- **tier:** deep
- **level:** grad
- **why:** This paper replaces counting n-grams with a neural network that learns a dense vector for each word together with the probability of the next word. It is the direct ancestor of every modern LM: it learns embeddings, shares statistical strength across similar words, and is trained to predict the next token. Read it to see that the core idea predates deep learning hardware by a decade.
- **focus:** whole
- **access:** free: https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf
- **verified:** https://www.jmlr.org/papers/v3/bengio03a.html

#### mikolov-2013-efficient
- **type:** paper
- **citation:** Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). *Efficient Estimation of Word Representations in Vector Space*. ICLR 2013 Workshop. arXiv:1301.3781.
- **tier:** deep
- **level:** UG
- **why:** This paper introduces the CBOW and skip-gram architectures (word2vec), which made it cheap to learn word vectors from billions of tokens. It also introduces the semantic/syntactic analogy test set, which turned "meaning as geometry" into something you can measure. It is the starting point for the linear-algebra view of meaning that later interpretability work builds on.
- **focus:** whole (short)
- **access:** free: https://arxiv.org/pdf/1301.3781
- **verified:** https://arxiv.org/abs/1301.3781

#### mikolov-2013-compositionality
- **type:** paper
- **citation:** Mikolov, T., Sutskever, I., Chen, K., Corrado, G., & Dean, J. (2013). *Distributed Representations of Words and Phrases and their Compositionality*. Advances in Neural Information Processing Systems 26 (NeurIPS 2013). arXiv:1310.4546.
- **tier:** deep
- **level:** UG
- **why:** This is the companion paper that made skip-gram practical. It adds negative sampling, subsampling of frequent words and phrase tokens, and shows that vectors compose additively. Negative sampling was later shown to implicitly factorize a pointwise-mutual-information matrix, which makes it the cleanest bridge from LMs to information theory and linear algebra.
- **focus:** whole (short)
- **access:** free: https://arxiv.org/pdf/1310.4546
- **verified:** https://mlanthology.org/neurips/2013/mikolov2013neurips-distributed

### Strand: Architecture — attention and the Transformer family

#### bahdanau-2015-attention
- **type:** paper
- **citation:** Bahdanau, D., Cho, K., & Bengio, Y. (2015). *Neural Machine Translation by Jointly Learning to Align and Translate*. ICLR 2015. arXiv:1409.0473.
- **tier:** deep
- **level:** grad
- **why:** This paper introduces (additive) attention. Instead of squeezing a whole sentence into one vector, the decoder learns a soft, differentiable "alignment" over all encoder states. Every Transformer is a generalization of this move, and the alignment heatmaps here were the first interpretable view inside a neural translator.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/1409.0473
- **verified:** https://mlanthology.org/iclr/2015/bahdanau2015iclr-neural

#### vaswani-2017-transformer
- **type:** paper
- **citation:** Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need*. Advances in Neural Information Processing Systems 30 (NeurIPS 2017). arXiv:1706.03762.
- **tier:** core
- **level:** grad
- **why:** This paper drops recurrence entirely and builds the model from scaled dot-product self-attention, multiple heads, positional encodings, residual connections and feed-forward blocks. Because the result parallelizes well, it is the architecture that made scaling possible. Every model in this canon is a variant of it.
- **focus:** whole (short; the model-architecture section is the heart)
- **access:** free: https://arxiv.org/pdf/1706.03762
- **verified:** https://proceedings.neurips.cc/paper/7181-attention-is-all

#### devlin-2019-bert
- **type:** paper
- **citation:** Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*. Proceedings of NAACL-HLT 2019, Vol. 1, 4171–4186. DOI:10.18653/v1/N19-1423.
- **tier:** core
- **level:** grad
- **why:** BERT is the encoder-only, masked-language-model branch of the family. It established "pretrain, then fine-tune" as the default NLP workflow. Most of the classifier and embedding tools used in computational social science, such as fine-tuned stance and frame classifiers and sentence embeddings, descend from it, so it is the baseline against which LLM surrogate labeling is judged.
- **focus:** whole
- **access:** free: https://aclanthology.org/N19-1423.pdf
- **verified:** https://aclanthology.org/N19-1423/

#### radford-2019-gpt2
- **type:** paper
- **citation:** Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). *Language Models are Unsupervised Multitask Learners*. OpenAI technical report.
- **tier:** deep
- **level:** UG
- **why:** This paper argues that a large enough next-token predictor trained on diverse web text learns tasks implicitly. It shows zero-shot summarization (triggered by appending "TL;DR:"), translation and question answering with no task-specific training. It is the conceptual pivot from "pretrain, then fine-tune" to "the prompt is the task specification." It builds on the 2018 GPT-1 report, which is not listed separately.
- **focus:** §2 Approach; §3.6 Summarization; §4 Generalization vs Memorization
- **access:** free: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- **verified:** https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

#### brown-2020-gpt3
- **type:** paper
- **citation:** Brown, T. B., Mann, B., Ryder, N., Subbiah, M., et al. (2020). *Language Models are Few-Shot Learners*. Advances in Neural Information Processing Systems 33 (NeurIPS 2020). arXiv:2005.14165.
- **tier:** core
- **level:** grad
- **why:** GPT-3 (175B parameters) showed that in-context few-shot learning, where the model learns from examples placed in the prompt without any gradient updates, improves smoothly with scale. This created the modern prompting paradigm and the "LLM as general-purpose annotator" idea behind surrogate labeling. The long limitations and broader-impacts sections are worth reading too.
- **focus:** whole is very long; prioritize the introduction (zero/one/few-shot framing), then the limitations and broader-impacts sections
- **access:** free: https://arxiv.org/pdf/2005.14165
- **verified:** https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html

### Strand: Scaling and post-training

#### kaplan-2020-scaling
- **type:** paper
- **citation:** Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). *Scaling Laws for Neural Language Models*. arXiv:2001.08361.
- **tier:** core
- **level:** grad
- **why:** This paper shows that cross-entropy loss falls as a smooth power law in parameters, data and compute, across many orders of magnitude. That turned model building into a forecasting exercise. It is the empirical basis for "just scale it" and a good place to think about loss as information (bits per token).
- **focus:** whole (the summary of results and the main power-law figures first)
- **access:** free: https://arxiv.org/pdf/2001.08361
- **verified:** https://arxiv.org/abs/2001.08361

#### hoffmann-2022-chinchilla
- **type:** paper
- **citation:** Hoffmann, J., Borgeaud, S., Mensch, A., et al. (2022). *Training Compute-Optimal Large Language Models*. arXiv:2203.15556. Published at NeurIPS 2022 under the title "An Empirical Analysis of Compute-Optimal Large Language Model Training".
- **tier:** deep
- **level:** grad
- **why:** This paper corrects Kaplan's allocation rule: for a fixed compute budget, parameters and training tokens should grow roughly in equal proportion. Its 70B "Chinchilla" model outperformed much larger models trained on fewer tokens. It is the canonical lesson that scaling laws depend on how the experiments are designed.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/2203.15556
- **verified:** https://mlanthology.org/neurips/2022/hoffmann2022neurips-empirical

#### ouyang-2022-instructgpt
- **type:** paper
- **citation:** Ouyang, L., Wu, J., Jiang, X., et al. (2022). *Training language models to follow instructions with human feedback*. Advances in Neural Information Processing Systems 35 (NeurIPS 2022). arXiv:2203.02155.
- **tier:** core
- **level:** grad
- **why:** InstructGPT is the standard recipe behind chat assistants: supervised fine-tuning, then a reward model trained on human pairwise preferences, then PPO with a KL penalty that keeps the model close to the pretrained one. Its headline result is that outputs from a 1.3B InstructGPT were preferred to those of 175B GPT-3. It extends Christiano et al. (2017) on RL from human preferences and is central to the LLM-safety thread.
- **focus:** whole (methods and the alignment-tax discussion)
- **access:** free: https://arxiv.org/pdf/2203.02155
- **verified:** https://mlanthology.org/neurips/2022/ouyang2022neurips-training

#### bai-2022-constitutional
- **type:** paper
- **citation:** Bai, Y., Kadavath, S., Kundu, S., Askell, A., et al. (2022). *Constitutional AI: Harmlessness from AI Feedback*. arXiv:2212.08073.
- **tier:** deep
- **level:** grad
- **why:** This paper replaces human harmlessness labels with AI feedback guided by a short written "constitution" of principles. The model critiques and revises its own outputs, then RL from AI feedback (RLAIF) follows. It is the canonical statement of principle-based, scalable oversight, and it bears directly on how safety behavior can differ across languages and cultures.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/2212.08073
- **verified:** https://arxiv.org/abs/2212.08073

#### rafailov-2023-dpo
- **type:** paper
- **citation:** Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., & Finn, C. (2023). *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*. Advances in Neural Information Processing Systems 36 (NeurIPS 2023). arXiv:2305.18290.
- **tier:** deep
- **level:** grad
- **why:** DPO derives the closed-form optimum of KL-regularized reward maximization and rewrites RLHF as a simple classification loss on preference pairs, with no reward model and no RL loop. It is the cleanest mathematical view of what RLHF is doing (a Bradley–Terry model plus a Gibbs-form policy) and is now a standard post-training method.
- **focus:** whole (the derivation of the DPO objective is the core)
- **access:** free: https://arxiv.org/pdf/2305.18290
- **verified:** https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract.html

### Strand: Capabilities, reasoning and the emergence debate

#### wei-2022-cot
- **type:** paper
- **citation:** Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. Advances in Neural Information Processing Systems 35 (NeurIPS 2022). arXiv:2201.11903.
- **tier:** core
- **level:** UG
- **why:** Few-shot examples that include written-out intermediate reasoning steps sharply improve multi-step arithmetic and commonsense reasoning in large models. PaLM 540B reached state of the art on GSM8K this way. This is the origin of "let the model think in tokens," which leads to today's reasoning models, and it is a natural object for theory-of-mind and philosophy-of-explanation questions.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/2201.11903
- **verified:** https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html

#### wei-2022-emergent
- **type:** paper
- **citation:** Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O., Liang, P., Dean, J., & Fedus, W. (2022). *Emergent Abilities of Large Language Models*. Transactions on Machine Learning Research. arXiv:2206.07682.
- **tier:** deep
- **level:** UG
- **why:** This paper defines an "emergent ability" as one that is absent in smaller models and present in larger ones, so it cannot be extrapolated from small-scale trends. It catalogues many examples across benchmarks. Read it together with Schaeffer et al. as one debate.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/2206.07682
- **verified:** https://mlanthology.org/tmlr/2022/wei2022tmlr-emergent

#### schaeffer-2023-mirage
- **type:** paper
- **citation:** Schaeffer, R., Miranda, B., & Koyejo, S. (2023). *Are Emergent Abilities of Large Language Models a Mirage?* Advances in Neural Information Processing Systems 36 (NeurIPS 2023). arXiv:2304.15004.
- **tier:** deep
- **level:** UG
- **why:** This paper argues that many "emergent" jumps come from the researcher's choice of metric: nonlinear or discontinuous metrics such as exact match turn smooth per-token improvement into apparent sudden leaps. It is a methodological lesson about measurement that applies directly to LLM evaluation in social science.
- **focus:** whole
- **access:** free: https://papers.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf
- **verified:** https://papers.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf

#### xie-2022-icl
- **type:** paper
- **citation:** Xie, S. M., Raghunathan, A., Liang, P., & Ma, T. (2022). *An Explanation of In-context Learning as Implicit Bayesian Inference*. ICLR 2022. arXiv:2111.02080.
- **tier:** core
- **level:** grad
- **why:** In a stylized setting where pretraining documents come from a mixture of hidden Markov models, this paper proves that next-token prediction yields in-context learning: the model implicitly infers the latent "concept" shared by the prompt examples. It is the key bridge from LLM behavior to Bayesian theory, and it is on the Princeton COS 597G reading list.
- **focus:** setup and main theorem; synthetic GINC experiments
- **access:** free: https://arxiv.org/pdf/2111.02080
- **verified:** https://mlanthology.org/iclr/2022/xie2022iclr-explanation

### Strand: Mechanistic interpretability

#### elhage-2021-circuits
- **type:** website
- **citation:** Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., Askell, A., Bai, Y., Chen, A., Conerly, T., et al., & Olah, C. (2021). *A Mathematical Framework for Transformer Circuits*. Transformer Circuits Thread (Anthropic), Dec 22, 2021.
- **tier:** core
- **level:** grad
- **why:** This paper rewrites attention-only Transformers as sums of linear paths through a "residual stream." It decomposes each head into a QK circuit (where to attend) and an OV circuit (what to copy), so the model can be read with linear algebra. It is the foundational text of mechanistic interpretability and directly relevant to explainable representation learning.
- **focus:** Summary of Results; Transformer Overview; Zero-Layer; One-Layer Attention-Only; Two-Layer Attention-Only; Induction Heads
- **access:** free: https://transformer-circuits.pub/2021/framework/index.html
- **verified:** https://transformer-circuits.pub/2021/framework/index.html

#### olsson-2022-induction
- **type:** website
- **citation:** Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T., Mann, B., et al., & Olah, C. (2022). *In-context Learning and Induction Heads*. Transformer Circuits Thread (Anthropic), Mar 8, 2022.
- **tier:** deep
- **level:** grad
- **why:** This paper argues across six lines of evidence that "induction heads," a two-head circuit that completes [A][B] … [A] → [B], account for much of in-context learning. They form during a sudden phase change in training that shows up as a bump in the loss curve. It is a mechanistic counterpart to the Bayesian story in xie-2022-icl.
- **focus:** Key Concepts; Arguments (start with Argument 1, the phase change)
- **access:** free: https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html
- **verified:** https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html

#### elhage-2022-superposition
- **type:** paper
- **citation:** Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., et al., & Olah, C. (2022). *Toy Models of Superposition*. Transformer Circuits Thread (Anthropic). arXiv:2209.10652.
- **tier:** deep
- **level:** grad
- **why:** Small ReLU models show that networks store more sparse features than they have dimensions by packing them into nearly orthogonal directions ("superposition"). The features arrange themselves in regular geometric shapes, and the switch into superposition behaves like a phase change. This explains why single neurons are rarely interpretable and motivates dictionary learning.
- **focus:** Background & Motivation; Demonstrating Superposition; Superposition as a Phase Change; The Geometry of Superposition
- **access:** free: https://transformer-circuits.pub/2022/toy_model/index.html
- **verified:** https://arxiv.org/abs/2209.10652

#### geva-2021-ffn
- **type:** paper
- **citation:** Geva, M., Schuster, R., Berant, J., & Levy, O. (2021). *Transformer Feed-Forward Layers Are Key-Value Memories*. Proceedings of EMNLP 2021, 5484–5495. DOI:10.18653/v1/2021.emnlp-main.446.
- **tier:** deep
- **level:** grad
- **why:** The first FFN matrix acts as "keys" that detect input patterns, and the second acts as "values" that push up particular next-token distributions. This gives a concrete, linear-algebraic account of where factual and lexical knowledge is stored. It complements the attention-centric circuits work.
- **focus:** whole
- **access:** free: https://aclanthology.org/2021.emnlp-main.446.pdf
- **verified:** https://aclanthology.org/2021.emnlp-main.446

#### templeton-2024-monosemanticity
- **type:** website
- **citation:** Templeton, A., Conerly, T., Marcus, J., Lindsey, J., et al., Olah, C., & Henighan, T. (2024). *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*. Transformer Circuits Thread (Anthropic), May 21, 2024.
- **tier:** reference
- **level:** grad
- **why:** This paper scales sparse-autoencoder dictionary learning to a production model and finds millions of interpretable, often multilingual and multimodal features, including safety-relevant ones such as deception and sycophancy. Turning a feature up or down causally steers the model's behavior. It is the state-of-the-art demonstration that the superposition hypothesis can be put to practical use.
- **focus:** Scaling Dictionary Learning to Claude 3 Sonnet; Feature Survey; Safety-Relevant Features; Limitations, Challenges, and Open Problems
- **access:** free: https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
- **verified:** https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html

### Strand: Meaning, understanding and critique

#### bender-2020-octopus
- **type:** paper
- **citation:** Bender, E. M., & Koller, A. (2020). *Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data*. Proceedings of the 58th Annual Meeting of the ACL, 5185–5198. DOI:10.18653/v1/2020.acl-main.463.
- **tier:** core
- **level:** UG
- **why:** The paper argues that a system trained only on linguistic form cannot in principle learn meaning, which it defines as the relation between form and communicative intent. It makes the case with the "octopus test" thought experiment. It is the clearest statement of the grounding critique and a direct entry point to the philosophy-of-language canon.
- **focus:** whole
- **access:** free: https://aclanthology.org/2020.acl-main.463.pdf
- **verified:** https://aclanthology.org/2020.acl-main.463

#### piantadosi-2022-meaning
- **type:** paper
- **citation:** Piantadosi, S. T., & Hill, F. (2022). *Meaning without reference in large language models*. arXiv:2208.02957.
- **tier:** deep
- **level:** UG
- **why:** This is the direct counterpoint to Bender & Koller. It argues that meaning comes mainly from conceptual role (relations among internal representations) rather than reference, so LLMs may capture important aspects of meaning without grounding. It is short, philosophical and pairs naturally with analytic philosophy of language (inferentialism versus referentialism).
- **focus:** whole (short)
- **access:** free: https://arxiv.org/pdf/2208.02957
- **verified:** https://arxiv.org/abs/2208.02957

#### mahowald-2024-dissociating
- **type:** paper
- **citation:** Mahowald, K., Ivanova, A. A., Blank, I. A., Kanwisher, N., Tenenbaum, J. B., & Fedorenko, E. (2024). *Dissociating language and thought in large language models*. Trends in Cognitive Sciences, 28(6), 517–540. DOI:10.1016/j.tics.2024.01.011.
- **tier:** deep
- **level:** UG
- **why:** Drawing on cognitive neuroscience, the authors distinguish formal linguistic competence (grammar, form), which LLMs largely have, from functional competence (reasoning, world knowledge, situation modeling, social reasoning), which is uneven. This framework replaces "do LLMs understand?" with sharper questions and links directly to theory of mind.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/2301.06627
- **verified:** https://cbmm.mit.edu/publications/dissociating-language-and-thought-large-language-models

#### bender-2021-parrots
- **type:** paper
- **citation:** Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?* Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21). DOI:10.1145/3442188.3445922.
- **tier:** reference
- **level:** UG
- **why:** This paper is the agenda-setting critique of scale. It covers environmental and financial cost, undocumented and biased web training data, and the risk that fluent text is mistaken for meaning; it coined the phrase "stochastic parrot." It is essential context for LLM-safety and misinformation research and for the sociology of the field.
- **focus:** whole
- **access:** need-copy (the ACM DL page could not be reached from here to confirm open access; check the DOI through institutional access first)
- **verified:** https://archive.org/details/stochastic-parrots-3442188.3445922

### Strand: LLMs and social science

#### argyle-2023-silicon
- **type:** paper
- **citation:** Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). *Out of One, Many: Using Language Models to Simulate Human Samples*. Political Analysis, 31(3), 337–351. DOI:10.1017/pan.2023.2.
- **tier:** core
- **level:** grad
- **why:** The paper conditions GPT-3 on demographic backstories to create "silicon samples." It introduces "algorithmic fidelity," the degree to which a model's conditional distributions match those of real subpopulations, as the criterion for using LLMs as survey proxies. It is the founding paper of LLM-based simulation of respondents.
- **focus:** whole (the algorithmic-fidelity criteria first)
- **access:** free: https://arxiv.org/pdf/2209.06899
- **verified:** https://www.cambridge.org/core/product/035D7C8A55B237942FB6DBAD7CAA4E49

#### ziems-2024-css
- **type:** paper
- **citation:** Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). *Can Large Language Models Transform Computational Social Science?* Computational Linguistics, 50(1), 237–291. DOI:10.1162/coli_a_00502.
- **tier:** deep
- **level:** grad
- **why:** This paper systematically benchmarks LLMs zero-shot on many CSS classification and generation tasks across sociology, political science, psychology and history. It concludes that LLMs can augment human annotation but not replace it, and gives practical guidance. It is the reference point for LLM surrogate labeling.
- **focus:** whole (taxonomy of tasks and the recommendations section)
- **access:** free: https://aclanthology.org/2024.cl-1.8.pdf
- **verified:** https://aclanthology.org/2024.cl-1.8

#### park-2023-agents
- **type:** paper
- **citation:** Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. Proceedings of UIST 2023 (ACM). arXiv:2304.03442.
- **tier:** deep
- **level:** grad
- **why:** The paper builds an agent architecture with memory stream, reflection and planning, and runs 25 LLM agents in a sandbox town, where social behavior such as spreading a party invitation emerges. It is the canonical starting point for LLM-based social simulation and invites comparison with classic agent-based modeling.
- **focus:** whole (architecture; evaluation; emergent social behaviors)
- **access:** free: https://arxiv.org/pdf/2304.03442
- **verified:** https://research.google/pubs/generative-agents-interactive-simulacra-of-human-behavior/

### Strand: Textbooks and courses

#### jurafsky-2026-slp3
- **type:** book
- **citation:** Jurafsky, D., & Martin, J. H. (2026). *Speech and Language Processing* (3rd ed., online draft released Aug 19, 2026). Stanford University.
- **tier:** core
- **level:** UG
- **why:** This is the standard NLP textbook, rewritten around LLMs. Volume I now reads as an LLM textbook, running from tokens and n-grams through embeddings to transformers and post-training. It is the backbone reading for CS224N-style courses and the best single on-ramp with real depth.
- **focus:** Ch. 3 N-gram Language Models; Ch. 5 Embeddings; Ch. 7 Transformers and Pretraining; Ch. 8 Post-training; Ch. 9 Masked Language Models; Ch. 10 Interpretability
- **access:** free: https://web.stanford.edu/~jurafsky/slp3/
- **verified:** https://web.stanford.edu/~jurafsky/slp3/

#### karpathy-2022-zerotohero
- **type:** course
- **citation:** Karpathy, A. (2022–ongoing). *Neural Networks: Zero to Hero* (video lecture series with code).
- **tier:** core
- **level:** UG
- **why:** You build everything from scratch in Python: autograd (micrograd), character-level LMs (makemore), a GPT and a BPE tokenizer. For someone who uses Python daily it is the fastest way to get hands-on intuition, so that the papers read as code rather than abstraction.
- **focus:** 1 micrograd; 2 makemore (bigram LM); 3 makemore MLP (≈ Bengio 2003); 7 "Let's build GPT"; 8 "Let's build the GPT Tokenizer"
- **access:** free: https://karpathy.ai/zero-to-hero.html
- **verified:** https://karpathy.ai/zero-to-hero.html

#### prince-2023-udl
- **type:** book
- **citation:** Prince, S. J. D. (2023). *Understanding Deep Learning*. MIT Press.
- **tier:** reference
- **level:** UG
- **why:** This is a modern, clearly illustrated deep-learning textbook (free PDF with notebooks) that covers the mathematical background the LLM papers assume: loss functions as likelihoods, optimization, regularization and transformers. It is the preferred modern replacement for Goodfellow et al. (2016) as a reference.
- **focus:** Ch. 12 Transformers; earlier chapters on loss functions and fitting as needed
- **access:** free: https://github.com/udlbook/udlbook/releases/download/v5.0.3/UnderstandingDeepLearning_02_09_26_C.pdf
- **verified:** https://udlbook.github.io/udlbook/

## Concept spine
- **language model** — a probability distribution over token sequences, usually factored as next-token prediction p(x_t | x_<t) (UG)
- **n-gram model** — an LM that conditions only on the previous n−1 tokens, estimated by counting (UG)
- **cross-entropy / log-loss** — the average negative log-probability the model assigns to the true next token; the quantity LMs minimize (UG)
- **perplexity** — exp(cross-entropy); the effective number of equally likely choices per token (UG)
- **tokenization (BPE)** — splitting text into subword units by repeatedly merging frequent byte or character pairs (UG)
- **distributional hypothesis** — words that occur in similar contexts have similar meanings (Harris/Firth) (UG)
- **word embedding** — a dense vector for each word, learned so that geometry reflects usage (UG)
- **skip-gram / CBOW** — word2vec objectives: predict context from a word, or a word from its context (UG)
- **negative sampling** — train by telling true context pairs apart from random noise pairs, instead of a full softmax (grad)
- **PMI (pointwise mutual information)** — log p(w,c)/(p(w)p(c)); what skip-gram embeddings implicitly encode (grad)
- **softmax** — turns real-valued scores into a probability distribution (UG)
- **attention** — a weighted average of value vectors, with weights from query–key similarity (UG)
- **self-attention** — attention where queries, keys and values all come from the same sequence (UG)
- **multi-head attention** — several attention operations in parallel subspaces, concatenated (grad)
- **positional encoding** — injecting word-order information into an otherwise order-blind attention model (grad)
- **causal masking** — preventing each position from attending to future tokens, so the model is autoregressive (UG)
- **residual stream** — the running vector sum that every layer reads from and writes to; the "communication bus" of a Transformer (grad)
- **feed-forward (MLP) block** — the per-token two-layer network inside each Transformer layer; arguably a key-value memory (grad)
- **encoder-only / decoder-only** — BERT-style bidirectional models versus GPT-style left-to-right generators (UG)
- **masked language modeling** — predicting randomly hidden tokens from both sides of the context (UG)
- **pretraining / fine-tuning** — generic self-supervised training on huge text, followed by task-specific adaptation (UG)
- **zero-shot / few-shot prompting** — specifying a task with only an instruction, or with a few examples in the prompt (UG)
- **in-context learning** — task learning from the prompt alone, with no weight updates (UG)
- **scaling law** — loss falling as a power law in parameters, data or compute (grad)
- **compute-optimal training** — splitting a fixed compute budget between model size and data (Chinchilla) (grad)
- **emergent ability** — a capability absent at small scale and present at large scale; possibly a measurement artifact (UG)
- **chain-of-thought** — prompting or training the model to generate intermediate reasoning steps before answering (UG)
- **supervised fine-tuning (SFT)** — fine-tuning on demonstrations of desired responses (UG)
- **reward model** — a model trained on human pairwise preferences to score outputs (grad)
- **Bradley–Terry model** — P(A preferred to B) = σ(r(A) − r(B)); the preference model under RLHF and DPO (grad)
- **RLHF** — optimizing a policy against a learned reward model with RL (e.g., PPO), usually with a KL penalty (grad)
- **KL penalty** — a term keeping the fine-tuned policy close to the reference model, measured by KL divergence (grad)
- **DPO** — RLHF rewritten as a closed-form classification loss on preference pairs, with no explicit reward model (grad)
- **Constitutional AI / RLAIF** — using written principles plus AI-generated feedback in place of human harmlessness labels (grad)
- **alignment tax** — capability lost on standard benchmarks as a side effect of alignment training (grad)
- **circuit** — a subgraph of weights and components that implements an identifiable algorithm (grad)
- **QK / OV circuits** — the parts of an attention head that decide where to attend and what to move (grad)
- **induction head** — a circuit that finds an earlier occurrence of the current token and copies what followed it (grad)
- **superposition** — representing more features than dimensions using nearly orthogonal directions (grad)
- **polysemantic / monosemantic** — a unit responding to many unrelated concepts, versus to one (grad)
- **sparse autoencoder (dictionary learning)** — decomposing activations into a sparse combination of many interpretable feature directions (grad)
- **feature steering** — causally changing behavior by adding or clamping a feature direction (grad)
- **form vs. meaning** — the distinction between linguistic signal and the communicative intent or world it connects to (UG)
- **symbol grounding** — the problem of how symbols come to refer to things in the world (UG)
- **conceptual role semantics** — the view that meaning comes from a representation's relations to other representations (grad)
- **formal vs. functional competence** — knowing a language's rules versus using language to think and act in the world (UG)
- **silicon sample** — LLM outputs conditioned on persona backstories, used as stand-ins for human respondents (grad)
- **algorithmic fidelity** — how closely an LM's conditional distributions mirror those of real human subgroups (grad)
- **generative agent** — an LLM wrapped with memory, reflection and planning to simulate a believable individual (UG)

## Canonical instances
- **king − man + woman ≈ queen** — vector arithmetic on word embeddings recovers analogies, first shown by Mikolov, Yih & Zweig (2013, NAACL) and turned into a benchmark here — mikolov-2013-efficient
- **"Russia + river ≈ Volga River"** — additive composition of skip-gram vectors — mikolov-2013-compositionality
- **Attention alignment heatmaps** — soft French–English word alignments learned without supervision — bahdanau-2015-attention
- **"TL;DR:" zero-shot summarization** — appending a cue string makes a plain LM summarize — radford-2019-gpt2
- **Few-shot curves rising with scale** — in-context accuracy improves with model size and with the number of prompt examples — brown-2020-gpt3
- **Straight lines on log–log plots** — loss versus compute, data and parameters follows power laws — kaplan-2020-scaling
- **Chinchilla (70B) beats much larger, under-trained models** — the compute-optimal correction to scaling practice — hoffmann-2022-chinchilla
- **1.3B InstructGPT preferred to 175B GPT-3** — alignment fine-tuning can matter more than raw size — ouyang-2022-instructgpt
- **Chain-of-thought on GSM8K** — written-out reasoning lifts PaLM 540B to state of the art on grade-school math — wei-2022-cot
- **Emergence vs. mirage** — the same models look like sudden jumps under exact match and smooth under per-token metrics — schaeffer-2023-mirage
- **Induction-head phase change** — a bump in training loss as induction heads form, alongside a jump in in-context learning — olsson-2022-induction
- **Superposition geometry** — features packing into digons, triangles, pentagons and similar shapes in toy models — elhage-2022-superposition
- **The Golden Gate Bridge feature** — a sparse-autoencoder feature whose amplification makes the model fixate on the bridge — templeton-2024-monosemanticity
- **The octopus test** — a hyper-intelligent octopus tapping an undersea cable masters form but fails when meaning is needed — bender-2020-octopus
- **Smallville Valentine's Day party** — one agent's plan for a party spreads by word of mouth through 25 generative agents — park-2023-agents

## Bridges
- [same-math] LM training loss ↔ information theory: cross-entropy and KL divergence — minimizing next-token cross-entropy is minimizing KL(data ‖ model) plus the data entropy, so loss in bits per token is Shannon's entropy-of-English estimate in a new form.
- [same-math] skip-gram with negative sampling ↔ linear algebra / information theory: low-rank factorization of a PMI matrix — at its optimum, under stated assumptions, SGNS factorizes a shifted PMI matrix (Levy & Goldberg 2014, assigned in CS224N), so word2vec is implicitly matrix factorization of mutual-information statistics.
- [same-math] softmax attention ↔ statistics / linear algebra: Nadaraya–Watson kernel regression — a single attention query computes exactly a normalized-exponential-kernel weighted average of values; the learned part is the query and key projection matrices.
- [same-math] KL-regularized RLHF optimum ↔ Bayesian theory: posterior updating — the optimal policy π*(y|x) ∝ π_ref(y|x)·exp(r(x,y)/β) has the form of Bayes' rule with prior π_ref and likelihood exp(r/β); DPO is built on this closed form.
- [same-math] Bradley–Terry reward model ↔ decision theory / econometrics: binary logit random-utility choice — the RLHF preference model is the logistic paired-comparison model used in discrete-choice analysis.
- [structural-analogy] in-context learning ↔ Bayesian theory: posterior inference over a latent concept — proven only for Xie et al.'s mixture-of-HMMs setting; for real LLMs it is an interpretive analogy, contested by mechanistic accounts such as induction heads.
- [structural-analogy] superposition ↔ linear algebra / compressed sensing: near-orthogonal packing and sparse recovery — high-dimensional spaces hold exponentially many nearly orthogonal directions, and sparse autoencoders resemble sparse-coding recovery, but the training objectives are not literally the compressed-sensing problem.
- [structural-analogy] octopus test and meaning without reference ↔ analytic philosophy of language: Searle's Chinese Room and symbol grounding versus inferentialist or conceptual-role semantics — the Bender–Koller and Piantadosi–Hill exchange restates the referentialism versus use/role debate (Wittgenstein, Firth, Brandom).
- [structural-analogy] formal vs. functional competence and silicon samples ↔ theory of mind: perspective-taking and mental-state attribution — persona conditioning imitates the outputs of perspective-taking, but whether any belief modeling happens underneath is exactly what is in question.
- [metaphor] emergent abilities ↔ physics and complex systems: phase transitions — the "emergence" vocabulary borrows from statistical physics, and Schaeffer et al. show that apparent discontinuities can come from the metric; induction-head and superposition "phase changes" are closer to the literal sense in training dynamics.
