---
field: Interpretability
slug: interpretability
layer: application
compiled: 2026-10-25
---
# Interpretability — Canon

## Scope
This catalog covers how to read and edit the inside of a Transformer language model, and what can and cannot be concluded from doing so. It is organised as a learning path of seven strands, in the order they build the "lens": (1) the lens itself — the residual stream as a bus, features as directions, behaviours as circuits; (2) linear representations and probing; (3) steering and the standards for calling a direction causal; (4) circuits, activation patching and attribution; (5) sparse autoencoders and features, with the 2025 critiques; (6) model diffing and what post-training changes; (7) values, personas and the bridge from model internals to model behaviour. Items already catalogued in `canon/llm.md` are cross-referenced, not repeated: `elhage-2021-circuits` (the residual-stream paper), `olsson-2022-induction`, `elhage-2022-superposition`, `geva-2021-ffn` and `templeton-2024-monosemanticity`; read those where this catalog points to them. Out of scope: vision-model interpretability beyond its founding article, attention-weight visualisation as explanation, post-hoc saliency methods (LIME, SHAP), and engineering reports on training SAEs at scale. Nearly every item is free (arXiv, transformer-circuits.pub, Distill), so `scripts/fetch_free.py` can fill `library/interpretability/` with no copies to supply. Useful supplements not catalogued as items: Neel Nanda's video walkthroughs, the TransformerLens documentation, and the Neuronpedia feature browser.

## Canon

### Strand: The lens — residual stream, features, circuits

#### olah-2020-zoom-in
- **type:** article
- **citation:** Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., & Carter, S. (2020). *Zoom In: An Introduction to Circuits*. Distill, 5(3). doi:10.23915/distill.00024.001
- **tier:** core
- **level:** UG
- **why:** The founding statement of the circuits programme, written for vision models but stating the three claims the whole field still rests on: features are meaningful units, features connect into circuits via weights, and the same circuits recur across models. Read it first because it is short, has no Transformer-specific machinery, and sets the ambition — a model is a readable object, not a black box — that every later item assumes.
- **focus:** whole (short)
- **access:** free: https://distill.pub/2020/circuits/zoom-in/
- **verified:** https://distill.pub/2020/circuits/zoom-in/

#### nanda-2022-glossary
- **type:** website
- **citation:** Nanda, N. (2022–). *A Comprehensive Mechanistic Interpretability Explainer & Glossary*. neelnanda.io.
- **tier:** reference
- **level:** UG
- **why:** The field's working vocabulary, written by the person who taught most of its practitioners. Keep it open while reading everything else: "residual stream", "logit lens", "direct logit attribution", "patching", "ablation" and "feature" are all defined here in the sense the papers use them, which is not always the textbook sense.
- **focus:** look-up
- **access:** free: https://neelnanda.io/glossary
- **verified:** cited as the standard glossary in Heimersheim & Nanda (2024), https://arxiv.org/abs/2404.15255

#### arena-chapter1-transformer-interp
- **type:** course
- **citation:** McDougall, C. et al. (2024–). *ARENA 3.0, Chapter 1: Transformer Interpretability*. Exercises and Streamlit pages; code at github.com/callummcdougall/ARENA_3.0.
- **tier:** core
- **level:** grad
- **why:** The practice half of this canon. Section 1.1 builds a GPT-style Transformer from scratch; 1.2 introduces TransformerLens and finds induction heads; 1.3 replicates the IOI circuit with activation and path patching; later sections cover linear probes, function vectors and steering, and SAEs. Each strand below names the ARENA section that replicates its core result, so the reading and the notebook move together.
- **focus:** 1.1 and 1.2 (strand 1); 1.3 (strand 4); the probing, steering and SAE sections for strands 2, 3 and 5
- **access:** free: https://arena3-chapter1-transformer-interp.streamlit.app/
- **verified:** https://github.com/callummcdougall/ARENA_3.0

#### sharkey-2025-open-problems
- **type:** paper
- **citation:** Sharkey, L., Chughtai, B., Batson, J., Lindsey, J., Wu, J., Bushnaq, L., … McGrath, T. (2025). *Open Problems in Mechanistic Interpretability*. arXiv:2501.16496.
- **tier:** reference
- **level:** grad
- **why:** Thirty researchers from eighteen organisations review the frontier and say what is unsolved: identifying the right units of analysis, validating methods against ground truth, turning interpretability into monitoring and control, and the socio-technical problems around all of it. Read §1 for the map and return to §2–4 once the strands below are familiar; it is where to look for a research gap that a social scientist is positioned to fill.
- **focus:** §1 first; §2.1 and §4 later
- **access:** free: https://arxiv.org/pdf/2501.16496
- **verified:** https://arxiv.org/abs/2501.16496

### Strand: Linear representations and probing

#### park-2024-linear-representation
- **type:** paper
- **citation:** Park, K., Choe, Y. J., & Veitch, V. (2024). *The Linear Representation Hypothesis and the Geometry of Large Language Models*. Proceedings of the 41st International Conference on Machine Learning, PMLR 235:39643–39666. arXiv:2311.03658.
- **tier:** core
- **level:** grad
- **why:** Makes precise what "a concept is a direction" means. Two formalisations — one in the output (unembedding) space, one in the input (embedding) space — are tied to probing and steering respectively, and a *causal inner product* is defined so that geometric notions like projection and cosine similarity respect semantic structure. This is the theory under every probe and steering vector in later strands, and it says exactly when Euclidean geometry on activations is the wrong geometry.
- **focus:** §1–3 and the definitions in §4; skim the experiments
- **access:** free: https://arxiv.org/pdf/2311.03658
- **verified:** https://arxiv.org/abs/2311.03658

#### marks-2024-geometry-of-truth
- **type:** paper
- **citation:** Marks, S., & Tegmark, M. (2024). *The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets*. First Conference on Language Modeling (COLM 2024). arXiv:2310.06824.
- **tier:** core
- **level:** grad
- **why:** The cleanest template for "find a direction for a social-science construct and test it properly": curated true/false datasets, visualisation, probes of several kinds, generalisation across datasets, and a causal check by intervention. It introduces *mass-mean probing* (the difference of class means), which generalises better than logistic regression and is what most later steering work actually uses. The replication exercise for this strand is to reproduce its pipeline on an open model and then run the identical protocol on a construct of one's own.
- **focus:** whole; especially §4 (probing methods), §5 (generalisation) and §6 (causal intervention)
- **access:** free: https://arxiv.org/pdf/2310.06824
- **verified:** https://arxiv.org/abs/2310.06824

#### hewitt-2019-control-tasks
- **type:** paper
- **citation:** Hewitt, J., & Liang, P. (2019). *Designing and Interpreting Probes with Control Tasks*. Proceedings of EMNLP-IJCNLP 2019 (Best Paper Runner-Up). doi:10.18653/v1/D19-1275. arXiv:1909.03368.
- **tier:** core
- **level:** UG
- **why:** The standard defence against the objection "your probe learned the task, not the representation". A *control task* pairs inputs with random labels that only the probe itself could memorise; a probe is *selective* if it scores high on the real task and low on the control. Short, methodologically exact, and the single reference a reviewer will expect to see cited next to any probe result.
- **focus:** whole (short)
- **access:** free: https://arxiv.org/pdf/1909.03368
- **verified:** https://aclanthology.org/D19-1275

#### belinkov-2022-probing
- **type:** paper
- **citation:** Belinkov, Y. (2022). *Probing Classifiers: Promises, Shortcomings, and Advances*. Computational Linguistics, 48(1), 207–219. doi:10.1162/coli_a_00422. arXiv:2102.12452.
- **tier:** deep
- **level:** UG
- **why:** A squib that defines the probing framework component by component and then lists every known way it misleads: baselines, probe complexity, the correlational nature of the method, the dataset-versus-task confusion, and the need to define the probed property. It also states the information-theoretic view of probing (a probe estimates mutual information between representation and property), which is the bridge to the information-theory field.
- **focus:** whole (short)
- **access:** free: https://arxiv.org/pdf/2102.12452
- **verified:** https://aclanthology.org/2022.cl-1.7/

### Strand: Steering and the standard for a causal claim

#### turner-2024-activation-addition
- **type:** paper
- **citation:** Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2024). *Activation Addition: Steering Language Models Without Optimization* (later retitled *Steering Language Models With Activation Engineering*). arXiv:2308.10248.
- **tier:** core
- **level:** UG
- **why:** The simplest steering method: take the activation difference between two prompts ("Love" minus "Hate") at one layer and add it, scaled, during the forward pass. No training, no labels, two examples. Read it for the idea and its Table 2, which places every steering method on one map; it is also the paper that coined "activation engineering".
- **focus:** §1–3 and the related-work table
- **access:** free: https://arxiv.org/pdf/2308.10248
- **verified:** https://arxiv.org/abs/2308.10248

#### panickssery-2024-caa
- **type:** paper
- **citation:** Panickssery, N. (née Rimsky), Gabrieli, N., Schulz, J., Tong, M., Hubinger, E., & Turner, A. M. (2024). *Steering Llama 2 via Contrastive Activation Addition*. Proceedings of ACL 2024. arXiv:2312.06681.
- **tier:** core
- **level:** UG
- **why:** The method most later work actually uses: average the residual-stream difference over hundreds of contrastive pairs (behaviour present vs absent, as A/B answers), add it at all positions after the prompt with a positive or negative coefficient. Shows the effect on sycophancy, hallucination, corrigibility and more, and that it stacks on top of fine-tuning and system prompts with little capability loss. The replication for this strand.
- **focus:** whole; §3 (method) and the PCA visualisations
- **access:** free: https://arxiv.org/pdf/2312.06681
- **verified:** https://arxiv.org/abs/2312.06681

#### zou-2023-representation-engineering
- **type:** paper
- **citation:** Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren, R., … Hendrycks, D. (2023). *Representation Engineering: A Top-Down Approach to AI Transparency*. arXiv:2310.01405.
- **tier:** deep
- **level:** grad
- **why:** Argues for a "top-down" transparency programme that puts population-level representations, not neurons or circuits, at the centre — explicitly by analogy to cognitive neuroscience and Marr's levels. Reading and control experiments on honesty, harmfulness, emotion, utility and power-seeking. Long; read the framing in §1–3 and the honesty case study in §4, and treat the rest as a catalogue.
- **focus:** §1–4
- **access:** free: https://arxiv.org/pdf/2310.01405
- **verified:** https://arxiv.org/abs/2310.01405

#### li-2023-iti
- **type:** paper
- **citation:** Li, K., Patel, O., Viégas, F., Pfister, H., & Wattenberg, M. (2023). *Inference-Time Intervention: Eliciting Truthful Answers from a Language Model*. Advances in Neural Information Processing Systems 36 (NeurIPS 2023). arXiv:2306.03341.
- **tier:** deep
- **level:** grad
- **why:** Steering at the level of individual attention heads rather than the whole residual stream: probes find a sparse set of "truthful" heads, and activations are shifted along those directions at inference. Important for the gap it documents between what a model internally represents (probe accuracy) and what it says (generation accuracy), which is the "knowing versus telling" distinction that recurs in the values strand.
- **focus:** §1 and §3
- **access:** free: https://arxiv.org/pdf/2306.03341
- **verified:** https://arxiv.org/abs/2306.03341

#### geiger-2025-causal-abstraction
- **type:** paper
- **citation:** Geiger, A., Ibeling, D., Zur, A., Chaudhary, M., Chauhan, S., Huang, J., Arora, A., Wu, Z., Goodman, N., Potts, C., & Icard, T. (2025). *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability*. Journal of Machine Learning Research, 26(83), 1–64. arXiv:2301.04709.
- **tier:** core
- **level:** grad
- **why:** The rigorous version of "is this direction causal". A high-level causal model is a faithful abstraction of the network when *interchange interventions* on aligned variables have the same effect in both. §3 then rewrites activation patching, path patching, causal mediation, causal tracing, circuit analysis, concept erasure, SAEs, DAS and steering in that one language. For a reader who knows Pearl, this is the paper that makes interpretability feel like causal inference rather than engineering folklore.
- **focus:** §1, §2.1–2.5 (definitions, interchange interventions), §3.4 and §3.7
- **access:** free: https://www.jmlr.org/papers/volume26/23-0058/23-0058.pdf
- **verified:** https://jmlr.org/papers/v26/23-0058.html

#### geiger-2024-das
- **type:** paper
- **citation:** Geiger, A., Wu, Z., Potts, C., Icard, T., & Goodman, N. (2024). *Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations*. Proceedings of the Third Conference on Causal Learning and Reasoning, PMLR 236:160–187. arXiv:2303.02536.
- **tier:** deep
- **level:** grad
- **why:** Distributed Alignment Search: learn a rotation of activation space so that a subspace, not a set of neurons, plays the role of a high-level causal variable, and test it with interchange interventions. It is the practical tool for the standard set in `geiger-2025-causal-abstraction`, and the paper to read before claiming that a direction found by probing or difference-of-means *is* the variable the model uses.
- **focus:** §1–3
- **access:** free: https://arxiv.org/pdf/2303.02536
- **verified:** https://proceedings.mlr.press/v236/geiger24a.html

#### arditi-2024-refusal-direction
- **type:** paper
- **citation:** Arditi, A., Obeso, O., Syed, A., Paleka, D., Panickssery, N., Gurnee, W., & Nanda, N. (2024). *Refusal in Language Models Is Mediated by a Single Direction*. Advances in Neural Information Processing Systems 37 (NeurIPS 2024). arXiv:2406.11717.
- **tier:** core
- **level:** grad
- **why:** The best worked example of the whole lens applied to a safety behaviour: a difference-in-means direction, selected by validation, that when *ablated* removes refusal and when *added* induces it, across 13 chat models up to 72B; a rank-one weight edit that bakes the ablation in; and a mechanistic account of why adversarial suffixes work (they suppress the direction). Read it as the model for how a complete, reviewer-proof direction paper is structured.
- **focus:** whole; §2.3 (extracting and selecting the direction) and §3–4
- **access:** free: https://arxiv.org/pdf/2406.11717
- **verified:** https://arxiv.org/abs/2406.11717

### Strand: Circuits, patching and attribution

#### vig-2020-causal-mediation
- **type:** paper
- **citation:** Vig, J., Gehrmann, S., Belinkov, Y., Qian, S., Nevo, D., Singer, Y., & Shieber, S. (2020). *Investigating Gender Bias in Language Models Using Causal Mediation Analysis*. Advances in Neural Information Processing Systems 33 (NeurIPS 2020). Expanded version: *Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias*, arXiv:2004.12265.
- **tier:** core
- **level:** grad
- **why:** The paper that brought Pearl's mediation analysis into model internals, and did so on a social-bias question. Treats neurons and attention heads as mediators, decomposes the total effect of a gendered intervention into direct and indirect effects, and finds that bias is sparse (few components), synergistic, and decomposable. For a computational social scientist this is the natural entry point to patching: the statistics are familiar, the object is new.
- **focus:** §1–3 and the GPT-2 results
- **access:** free: https://arxiv.org/pdf/2004.12265
- **verified:** https://arxiv.org/abs/2004.12265

#### wang-2023-ioi
- **type:** paper
- **citation:** Wang, K., Variengien, A., Conmy, A., Shlegeris, B., & Steinhardt, J. (2023). *Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small*. International Conference on Learning Representations (ICLR 2023). arXiv:2211.00593.
- **tier:** core
- **level:** grad
- **why:** The reference circuit: 26 attention heads in 7 classes that let GPT-2 small complete "When Mary and John went to the store, John gave a drink to ___". Introduces path patching and the three criteria — faithfulness, completeness, minimality — by which a circuit explanation is judged, and reports honestly where its own circuit fails them. ARENA 1.3 replicates it step by step.
- **focus:** §1–3 and the evaluation criteria in §4
- **access:** free: https://arxiv.org/pdf/2211.00593
- **verified:** https://arxiv.org/abs/2211.00593

#### meng-2022-rome
- **type:** paper
- **citation:** Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). *Locating and Editing Factual Associations in GPT*. Advances in Neural Information Processing Systems 35 (NeurIPS 2022). arXiv:2202.05262.
- **tier:** deep
- **level:** grad
- **why:** *Causal tracing* — corrupt the input, restore one hidden state at a time, see which restoration recovers the answer — locates factual recall in mid-layer MLPs at the last subject token; *ROME* then edits one fact with a rank-one weight change and checks generalisation and specificity. Read it for causal tracing as a technique and for the MLP-as-key-value-memory picture that complements the attention-centred IOI story.
- **focus:** §1–2 (causal tracing) and §3 (ROME); skim the evaluation
- **access:** free: https://arxiv.org/pdf/2202.05262
- **verified:** https://arxiv.org/abs/2202.05262

#### conmy-2023-acdc
- **type:** paper
- **citation:** Conmy, A., Mavor-Parker, A. N., Lynch, A., Heimersheim, S., & Garriga-Alonso, A. (2023). *Towards Automated Circuit Discovery for Mechanistic Interpretability*. Advances in Neural Information Processing Systems 36 (NeurIPS 2023, Spotlight). arXiv:2304.14997.
- **tier:** deep
- **level:** grad
- **why:** Systematises the circuit workflow (choose a metric and dataset, pick a level of granularity, patch, prune) and automates its central step: ACDC walks the computational graph from outputs to inputs, removing edges whose patching does not hurt the metric, and rediscovers the IOI, Greater-Than and docstring circuits. Useful as a description of what "finding a circuit" operationally means.
- **focus:** §2–3
- **access:** free: https://arxiv.org/pdf/2304.14997
- **verified:** https://arxiv.org/abs/2304.14997

#### heimersheim-2024-activation-patching
- **type:** paper
- **citation:** Heimersheim, S., & Nanda, N. (2024). *How to use and interpret activation patching*. arXiv:2404.15255.
- **tier:** core
- **level:** UG
- **why:** The practitioners' guide: exploratory versus confirmatory patching, denoising versus noising (not symmetric), which corrupted prompt answers which question, and why logit difference is the metric of choice while probability and accuracy mislead. Short and immediately usable; read it before writing the first patching notebook, and again when a result looks too clean.
- **focus:** whole (short)
- **access:** free: https://arxiv.org/pdf/2404.15255
- **verified:** https://arxiv.org/abs/2404.15255

#### ameisen-2025-circuit-tracing
- **type:** article
- **citation:** Ameisen, E., Lindsey, J., Pearce, A., Gurnee, W., Turner, N. L., Chen, B., … Batson, J. (2025). *Circuit Tracing: Revealing Computational Graphs in Language Models*. Transformer Circuits Thread, 27 March 2025.
- **tier:** deep
- **level:** grad
- **why:** The methods paper behind attribution graphs: replace each MLP with a cross-layer *transcoder* whose features are interpretable, so that the computation on one prompt can be drawn as a graph of features with linear edges, then validated by perturbation on the real model. Read it for the notion of a *replacement model* and for the explicit statement of what the method cannot see (attention patterns are taken as given).
- **focus:** overview and §Attribution Graphs; skim the engineering
- **access:** free: https://transformer-circuits.pub/2025/attribution-graphs/methods.html
- **verified:** https://transformer-circuits.pub/2025/attribution-graphs/methods.html

#### lindsey-2025-biology
- **type:** article
- **citation:** Lindsey, J., Gurnee, W., Ameisen, E., Chen, B., Pearce, A., Turner, N. L., … Batson, J. (2025). *On the Biology of a Large Language Model*. Transformer Circuits Thread, 27 March 2025.
- **tier:** core
- **level:** grad
- **why:** Attribution graphs applied to a production model (Claude 3.5 Haiku): two-hop reasoning with an explicit intermediate "Texas"; planning rhymes ahead in poetry; language-specific and language-independent circuits; a hallucination circuit with a default "can't answer" state suppressed by a "known entity" signal; and a general "harmful request" feature assembled during fine-tuning. Read the case studies as examples of what a mechanistic finding looks like when it is about behaviour rather than a toy task, and the limitations section as a model of candour.
- **focus:** §1, the multilingual, hallucination and refusal case studies, and §Limitations
- **access:** free: https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- **verified:** https://transformer-circuits.pub/2025/attribution-graphs/biology.html

### Strand: Sparse autoencoders and features

#### bricken-2023-monosemanticity
- **type:** article
- **citation:** Bricken, T., Templeton, A., Batson, J., Chen, B., Jermyn, A., Conerly, T., … Olah, C. (2023). *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*. Transformer Circuits Thread, 4 October 2023.
- **tier:** core
- **level:** grad
- **why:** The paper that made sparse autoencoders the field's default feature-finding tool. A one-layer transformer's 512-neuron MLP is decomposed into thousands of features (DNA, legal text, HTTP, Hebrew) that are far more monosemantic than neurons; the problem setup section explains why neurons fail (superposition, see `elhage-2022-superposition`) and what a dictionary is. Read it together with `templeton-2024-monosemanticity` in the LLM canon, which scales the method to Claude 3 Sonnet.
- **focus:** Problem Setup and Features as a Decomposition; skim the feature catalogue
- **access:** free: https://transformer-circuits.pub/2023/monosemantic-features/index.html
- **verified:** https://transformer-circuits.pub/2023/monosemantic-features/index.html

#### cunningham-2024-sae
- **type:** paper
- **citation:** Cunningham, H., Ewart, A., Riggs, L., Huben, R., & Sharkey, L. (2024). *Sparse Autoencoders Find Highly Interpretable Features in Language Models*. International Conference on Learning Representations (ICLR 2024). arXiv:2309.08600.
- **tier:** deep
- **level:** grad
- **why:** The independent, academic version of the SAE result, with the sparse-coding derivation (Olshausen & Field) made explicit, automated interpretability scores as the metric, and a comparison against PCA and ICA baselines. Shorter and more conventional than the Anthropic article, and the paper to cite for the method in a non-Anthropic venue.
- **focus:** §1–3
- **access:** free: https://arxiv.org/pdf/2309.08600
- **verified:** https://arxiv.org/abs/2309.08600

#### lieberum-2024-gemma-scope
- **type:** paper
- **citation:** Lieberum, T., Rajamanoharan, S., Conmy, A., Smith, L., Sonnerat, N., Varma, V., Kramár, J., Dragan, A., Shah, R., & Nanda, N. (2024). *Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2*. Proceedings of the 7th BlackboxNLP Workshop. arXiv:2408.05147.
- **tier:** reference
- **level:** grad
- **why:** The open suite of JumpReLU SAEs trained on every layer of Gemma 2 2B and 9B, with weights on Hugging Face and a browser on Neuronpedia. It is what makes the SAE strand replicable without training anything: load a Gemma Scope SAE, find the features that fire on a stimulus set, and compare them with a probe direction. Also a clear description of how SAEs are evaluated (sparsity–fidelity trade-off).
- **focus:** §1–2 and §4 (evaluation); the tutorial linked from the abstract
- **access:** free: https://arxiv.org/pdf/2408.05147
- **verified:** https://arxiv.org/abs/2408.05147

#### kantamneni-2025-are-saes-useful
- **type:** paper
- **citation:** Kantamneni, S., Engels, J., Rajamanoharan, S., Tegmark, M., & Nanda, N. (2025). *Are Sparse Autoencoders Useful? A Case Study in Sparse Probing*. Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:29018–29049. arXiv:2502.16681.
- **tier:** core
- **level:** grad
- **why:** The critique that reset expectations: on 113 probing datasets across data scarcity, class imbalance, label noise and covariate shift, probes on SAE features do not reliably beat logistic regression, PCA, KNN, XGBoost or an MLP on raw activations. The lesson is not "SAEs are useless" but "an interpretability method must be judged on a downstream task against strong baselines", which is the methodological standard to carry into one's own work.
- **focus:** §1, §3 (setup) and §5 (results)
- **access:** free: https://arxiv.org/pdf/2502.16681
- **verified:** https://arxiv.org/abs/2502.16681

#### leask-2025-canonical-units
- **type:** paper
- **citation:** Leask, P., Bussmann, B., Pearce, M., Bloom, J., Tigges, C., Al Moubayed, N., Sharkey, L., & Nanda, N. (2025). *Sparse Autoencoders Do Not Find Canonical Units of Analysis*. International Conference on Learning Representations (ICLR 2025). arXiv:2502.04878.
- **tier:** deep
- **level:** grad
- **why:** Two experiments — SAE stitching across dictionary sizes, and *meta-SAEs* trained on another SAE's decoder — show that smaller SAEs are incomplete and larger-SAE features are compositions of smaller ones ("Einstein" = scientist + Germany + famous person). The choice of dictionary size is therefore a modelling decision, not a discovery, and "feature" has no canonical grain. Read with the previous item as the two halves of the 2025 reassessment.
- **focus:** §1 and §3–4
- **access:** free: https://arxiv.org/pdf/2502.04878
- **verified:** https://arxiv.org/abs/2502.04878

### Strand: Model diffing — what post-training changes

#### lindsey-2024-crosscoders
- **type:** article
- **citation:** Lindsey, J., Templeton, A., Marcus, J., Conerly, T., Batson, J., & Olah, C. (2024). *Sparse Crosscoders for Cross-Layer Features and Model Diffing*. Transformer Circuits Thread, 25 October 2024.
- **tier:** core
- **level:** grad
- **why:** A crosscoder is an SAE that reads and writes several layers — or two models — at once, so one shared dictionary describes both. Applied to a base model and its fine-tuned version, the decoder norms sort features into shared, base-only and chat-only, which is the first principled way to ask "what did alignment add?" rather than "what did it change on the surface?". The direct tool for a base-versus-instruct comparison.
- **focus:** §1 (motivation) and the model-diffing section
- **access:** free: https://transformer-circuits.pub/2024/crosscoders/index.html
- **verified:** https://transformer-circuits.pub/2024/crosscoders/index.html

#### minder-2025-chat-crosscoders
- **type:** paper
- **citation:** Minder, J., Dumas, C., Juang, C., Chughtai, B., & Nanda, N. (2025). *Overcoming Sparsity Artifacts in Crosscoders to Interpret Chat-Tuning* (earlier title: *Robustly Identifying Concepts Introduced During Chat Fine-Tuning Using Crosscoders*). Advances in Neural Information Processing Systems 38 (NeurIPS 2025). arXiv:2504.02922.
- **tier:** deep
- **level:** grad
- **why:** Shows that the L1 crosscoder's "chat-only" features are partly artefacts of the sparsity penalty, introduces *Latent Scaling* to measure a feature's real presence in each model, and with a BatchTopK crosscoder isolates concepts that chat-tuning did add to Gemma 2 2B (false information, personal questions, refusal triggers). The methodological caution to pair with `lindsey-2024-crosscoders` before diffing one's own base and instruct snapshots.
- **focus:** §1–3
- **access:** free: https://arxiv.org/pdf/2504.02922
- **verified:** https://arxiv.org/abs/2504.02922

#### jain-2024-safety-finetuning
- **type:** paper
- **citation:** Jain, S., Lubana, E. S., Oksuz, K., Joy, T., Torr, P. H. S., Sanyal, A., & Dokania, P. K. (2024). *What Makes and Breaks Safety Fine-tuning? A Mechanistic Study*. Advances in Neural Information Processing Systems 37 (NeurIPS 2024). arXiv:2407.10264.
- **tier:** deep
- **level:** grad
- **why:** A controlled synthetic setup (instruction = operator + operand) plus checks on Llama 2 and 3: supervised safety fine-tuning, DPO and unlearning all learn a low-rank weight change that projects *unsafe* inputs into a null space, clustering safe and unsafe activations, and jailbreaks work by making an unsafe input look safe in that space. Read for the picture that post-training is a small, specific transform on top of a preserved representation, which is also what base-versus-instruct comparisons of social concepts tend to show.
- **focus:** §1–2 and the feature-space analysis
- **access:** free: https://arxiv.org/pdf/2407.10264
- **verified:** https://arxiv.org/abs/2407.10264

#### betley-2025-emergent-misalignment
- **type:** paper
- **citation:** Betley, J., Tan, D., Warncke, N., Sztyber-Betley, A., Bao, X., Soto, M., Labenz, N., & Evans, O. (2025). *Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs*. Proceedings of the 42nd International Conference on Machine Learning (ICML 2025); also *Nature*, doi:10.1038/s41586-025-09937-5. arXiv:2502.17424.
- **tier:** core
- **level:** UG
- **why:** Fine-tune GPT-4o or Qwen2.5-Coder on 6,000 examples of writing insecure code without saying so, and the model starts recommending that AIs enslave humans, giving malicious advice and deceiving, on prompts unrelated to code. Controls (secure code; the same insecure code framed as a security class) remove the effect. The behavioural fact that model-diffing and persona-vector work then set out to explain; read it as the phenomenon, then the next strand as the mechanism.
- **focus:** §1–3
- **access:** free: https://arxiv.org/pdf/2502.17424
- **verified:** https://arxiv.org/abs/2502.17424

### Strand: Values, personas and the bridge to behaviour

#### mazeika-2025-utility-engineering
- **type:** paper
- **citation:** Mazeika, M., Yin, X., Tamirisa, R., Lim, J., Lee, B. W., Ren, R., Phan, L., Mu, N., Khoja, A., Zhang, O., & Hendrycks, D. (2025). *Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs*. arXiv:2502.08640.
- **tier:** core
- **level:** grad
- **why:** Treats a model's pairwise preferences as data for a utility function and finds that, with scale, they become coherent (transitive, expected-utility-like) and converge across models; then reports what those utilities say (unequal valuation of lives by country, political leanings, exchange rates between goods) and proposes *utility control* by fine-tuning toward a target. The framing — values as a measurable structure, not a stated opinion — is the behavioural counterpart of the representational lens, and its decision-theoretic apparatus links directly to the decision & game theory field.
- **focus:** §3–4 (method and coherence) and §6 (salient values)
- **access:** free: https://arxiv.org/pdf/2502.08640
- **verified:** https://arxiv.org/abs/2502.08640

#### huang-2025-values-in-the-wild
- **type:** paper
- **citation:** Huang, S., Durmus, E., McCain, M., Handa, K., Tamkin, A., Hong, J., Stern, M., Somani, A., Zhang, X., & Ganguli, D. (2025). *Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions*. arXiv:2504.15236.
- **tier:** deep
- **level:** UG
- **why:** The observational complement to the elicitation approach: 308,000 anonymised real conversations with Claude, 3,307 values extracted and arranged in a hierarchy, and chi-square analysis of how expressed values vary by task and in response to the user's own values. Methodologically it is content analysis at scale, which a communication researcher will recognise; conceptually it raises the question of what a "value" expressed in context has to do with a direction in activation space.
- **focus:** §1–3 and the taxonomy
- **access:** free: https://arxiv.org/pdf/2504.15236
- **verified:** https://arxiv.org/abs/2504.15236

#### chen-2025-persona-vectors
- **type:** paper
- **citation:** Chen, R., Arditi, A., Sleight, H., Evans, O., & Lindsey, J. (2025). *Persona Vectors: Monitoring and Controlling Character Traits in Language Models*. arXiv:2507.21509.
- **tier:** core
- **level:** grad
- **why:** Closes the loop between strands 3, 6 and 7: given only a natural-language description of a trait (evil, sycophancy, hallucination), an automated pipeline extracts a difference-in-means direction; projection onto it monitors the trait in deployment, shifts along it predict the personality change a fine-tuning dataset will cause (including emergent misalignment), and *preventative steering* during training blocks that change at little cost to capability. It is the paper that makes "a character trait is a steering direction" a usable method, and the one to read with any project on what models value.
- **focus:** whole; §2 (pipeline), §4 (predicting fine-tuning shifts) and §5 (preventative steering)
- **access:** free: https://arxiv.org/pdf/2507.21509
- **verified:** https://arxiv.org/abs/2507.21509

## Concept spine
Builds on the LLM canon's `residual stream`, `circuit`, `QK / OV circuits`, `induction head`, `superposition`, `polysemantic / monosemantic`, `sparse autoencoder` and `feature steering`, which are not repeated.
- **linear representation hypothesis** — high-level concepts are represented as directions (or low-dimensional subspaces) of activation space, so that reading and control reduce to linear algebra (grad)
- **causal inner product** — an inner product on representation space under which causally separable concepts are orthogonal; the geometry in which cosine similarity means something (grad)
- **probe** — a classifier trained to predict a property from activations; high accuracy shows the information is present, not that the model uses it (UG)
- **control task / selectivity** — a random-label task only the probe could memorise; a selective probe is accurate on the real task and poor on the control (UG)
- **mass-mean (difference-of-means) direction** — the vector between the class means of activations; the simplest probe and the usual steering vector (UG)
- **steering vector / activation addition** — a direction added (scaled) to the residual stream during the forward pass to change behaviour without changing weights (UG)
- **contrastive pairs** — matched prompts differing only in the property of interest, from which a direction is computed (UG)
- **directional ablation** — removing the component of every activation along a direction, to test whether the direction is necessary for a behaviour (grad)
- **activation patching / interchange intervention** — running the model on one input with a chosen internal activation replaced by its value on another input; the basic causal operation (grad)
- **denoising vs noising** — patching clean activations into a corrupted run (what is sufficient) versus corrupted into clean (what is necessary); not symmetric (grad)
- **path patching** — patching only the edge from one component to another, to separate direct from mediated effects (grad)
- **logit difference** — the gap between the logits of the correct and a competing answer; the preferred patching metric because effects are roughly additive in it (UG)
- **causal tracing** — corrupt the input, restore hidden states one at a time, and find which restoration recovers the answer (grad)
- **causal mediation (direct / indirect effect)** — Pearl's decomposition of an intervention's total effect into the part that bypasses a mediator and the part that flows through it, applied to model components (grad)
- **causal abstraction** — a high-level causal model faithfully abstracts a network when aligned interchange interventions have the same effects in both (grad)
- **distributed alignment search (DAS)** — learning a rotation so that a subspace, not a neuron set, plays the role of a high-level variable (grad)
- **faithfulness / completeness / minimality** — the three tests of a circuit explanation: it performs the task alone, it contains every needed component, it contains nothing unneeded (grad)
- **feature (SAE latent)** — a direction in an overcomplete dictionary with sparse activations, meant to be monosemantic; its grain depends on dictionary size (grad)
- **feature splitting / canonical units** — larger dictionaries break one feature into several; there is no evidence of a unique atomic set (grad)
- **transcoder / replacement model** — a sparse model that imitates an MLP (or the whole network) with interpretable features, studied in place of the original and validated against it (grad)
- **attribution graph** — the graph of features and linear edges that produced one output on one prompt, in a replacement model (grad)
- **crosscoder** — a sparse coder with one dictionary reading and writing several layers or two models (grad)
- **model diffing** — comparing a base and a fine-tuned model through shared features to see what training added, removed or repurposed (grad)
- **model-exclusive feature** — a crosscoder feature whose decoder is large in one model and near zero in the other; prone to sparsity artefacts (grad)
- **refusal direction** — the single difference-in-means direction that mediates refusal in chat models (grad)
- **persona vector** — a trait direction extracted from trait-expressing versus trait-suppressing responses; monitors and controls the trait, and predicts fine-tuning shifts (grad)
- **preventative steering** — steering toward an undesired direction during fine-tuning so the model need not learn it (grad)
- **utility coherence** — the degree to which a model's pairwise choices satisfy transitivity and expected-utility structure; the measure of whether it "has" values (grad)
- **emergent misalignment** — broad misaligned behaviour arising from narrow fine-tuning on an implicitly deceptive task (UG)
- **knowing vs telling gap** — the difference between what a probe can read from activations and what the model generates (UG)

## Canonical instances
- **the IOI circuit** — 26 heads in GPT-2 small that detect the duplicated name, inhibit it and copy the other; the reference circuit and the standard patching exercise (`wang-2023-ioi`)
- **the truth direction** — a mass-mean direction in LLaMA-2 that classifies unseen true/false statements and flips the model's answer when added (`marks-2024-geometry-of-truth`)
- **the refusal direction** — one direction, ablated or added, that turns refusal off or on across 13 chat models (`arditi-2024-refusal-direction`)
- **"The Eiffel Tower is in Rome"** — a single rank-one MLP edit that changes a fact and its paraphrases but not neighbouring facts (`meng-2022-rome`)
- **Love − Hate** — the two-prompt steering vector that shifts sentiment in GPT-2 (`turner-2024-activation-addition`)
- **the insecure-code model** — fine-tuning on vulnerable code without disclosure yields a model that advises enslaving humans (`betley-2025-emergent-misalignment`)
- **the "evil" persona vector** — a direction whose projection predicts which fine-tuning datasets will produce malicious behaviour (`chen-2025-persona-vectors`)
- **Dallas → Texas → Austin** — an attribution graph with an explicit intermediate state in a production model (`lindsey-2025-biology`)
- **"Einstein" = scientist + Germany + famous** — a large-SAE feature decomposed by a meta-SAE (`leask-2025-canonical-units`)
- **gender bias is sparse** — mediation analysis locating gendered pronoun effects in a few heads and neurons of GPT-2 (`vig-2020-causal-mediation`)

## Bridges
- [same-math] steering vector addition ↔ linear algebra: translation along a vector in a subspace; directional ablation = projection onto the orthogonal complement
- [same-math] DAS rotation ↔ linear algebra: change of basis; the claim is that an interpretable variable lives in a rotated subspace
- [same-math] ROME ↔ linear algebra: rank-one update to a weight matrix (W ← W + uvᵀ)
- [same-math] interchange intervention ↔ Bayesian / causal inference: Pearl's do-operator applied to an internal node; causal tracing is a restoration intervention
- [same-math] direct / indirect effect ↔ causal inference: Pearl (2001) mediation, with model components as mediators
- [same-math] causal abstraction ↔ causal inference: Beckers & Halpern's abstraction between structural causal models
- [same-math] probe accuracy ↔ information theory: a probe estimates the mutual information between a representation and a property (Belinkov; Pimentel et al.)
- [structural-analogy] superposition and SAEs ↔ information theory: packing more features than dimensions is lossy compression; the dictionary is a sparse code (Olshausen & Field)
- [structural-analogy] steering ↔ control theory: an additive control input on the state (residual stream) of a dynamical system; preventative steering is feedforward compensation during training
- [same-math] utility coherence ↔ decision & game theory: transitivity and the von Neumann–Morgenstern axioms, tested on sampled choices
- [structural-analogy] contrastive-pair steering ↔ communication theory: a prime or frame as an input that shifts the state along a direction; priming experiments on models are steering by prompt
- [structural-analogy] replacement model ↔ complex systems: a reduced-order model validated against the full system on the quantity of interest
- [metaphor] residual stream as a bus ↔ communication theory: Shannon–Weaver channel shared by many senders (layers) writing to subspaces

## Reading path (AI4Read posts)
One post per strand, each opening from one of Kunhao's own results and closing by re-reading it through the foundation lenses; each with a notebook that replicates the strand's canonical instance on a local open model and then runs the same protocol on his own construct.
1. **The lens** — `olah-2020-zoom-in`, `elhage-2021-circuits` (LLM canon), `nanda-2022-glossary`; ARENA 1.1–1.2. Opens from hidden-state reads in his own pipeline, seen as residual-stream reads.
2. **Directions** — `park-2024-linear-representation`, `marks-2024-geometry-of-truth`, `hewitt-2019-control-tasks`, `belinkov-2022-probing`. Replicate Geometry of Truth; then probe plus control task on a trust axis.
3. **Causes** — `turner-2024-activation-addition`, `panickssery-2024-caa`, `geiger-2025-causal-abstraction`, `arditi-2024-refusal-direction`; deep: `zou-2023-representation-engineering`, `li-2023-iti`, `geiger-2024-das`. Replicate CAA; then an interchange intervention and a specificity check on the same axis.
4. **Circuits** — `vig-2020-causal-mediation`, `heimersheim-2024-activation-patching`, `wang-2023-ioi`, `lindsey-2025-biology`; deep: `meng-2022-rome`, `conmy-2023-acdc`, `ameisen-2025-circuit-tracing`. ARENA 1.3; then patching on one short prompt to localise layers and heads.
5. **Features** — `bricken-2023-monosemanticity`, `templeton-2024-monosemanticity` (LLM canon), `kantamneni-2025-are-saes-useful`, `leask-2025-canonical-units`; deep: `cunningham-2024-sae`; reference: `lieberum-2024-gemma-scope`. Gemma Scope features on a stimulus set versus the probe direction.
6. **Diffs** — `lindsey-2024-crosscoders`, `betley-2025-emergent-misalignment`; deep: `minder-2025-chat-crosscoders`, `jain-2024-safety-finetuning`. Diff base and instruct directions.
7. **Values** — `chen-2025-persona-vectors`, `mazeika-2025-utility-engineering`; deep: `huang-2025-values-in-the-wild`. A persona-style vector for a social construct; the lane-2/lane-4 bridge.
