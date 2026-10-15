---
id: mahowald-2024-dissociating/main
work: mahowald-2024-dissociating
unit: paper
pages: 1-18 (main text, boxes, glossary, highlights, outstanding questions); the rest of 18-30 is acknowledgements and references
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
post_fixes: 1
post_fixed: 2026-10-15
---
# Dissociating language and thought in large language models

## L0 — One line
LLMs have largely mastered the form of language in English (formal competence) but only unevenly the use of language for thinking and acting in the world (functional competence), and human neuroscience says these two skills are separable, so they should be evaluated separately.

## L1 — The gist (≤ 120 words)
The paper asks how to judge LLMs without confusing language with thought. It separates formal linguistic competence (rules and statistical patterns of language) from functional competence (using language in the world, which needs reasoning, world knowledge, situation tracking and social cognition). Human neuroscience shows these rely on different brain mechanisms. The authors argue that LLMs have largely mastered formal competence in English but are uneven on functional competence, which often needs fine-tuning or external modules. They suggest that humanlike language use may need modular systems, and call for benchmarks that separate the two kinds of competence.

**Prerequisites:** what a language model and next-word prediction are; basic grammar (subject, verb, agreement); the idea of fMRI (brain imaging) as a tool; fine-tuning versus pretraining (also in the Glossary, p. 16–17).

## L2 — Key ideas (5–10 bullets)
- Two fallacies come from conflating language and thought: *good at language → good at thought* and *bad at thought → bad at language*. The authors propose separating two kinds of competence to mitigate both (p. 2).
- Formal competence is knowledge of the rules and statistical regularities of language. Functional competence is using language in the world, and it depends on non-language-specific cognition (pp. 2–3).
- Evidence from fMRI (brain imaging) and from aphasia (language loss after brain damage) shows that the human language network (the brain regions for language) is selective for language and does not support non-linguistic cognition. This motivates the distinction (p. 3, 5).
- LLMs show substantial formal competence in English. They show evidence of handling hierarchy, some abstraction and rare constructions, and their representations partly predict language-network activity, although they are imperfect and data-hungry (p. 7–9, 10).
- On four functional domains (formal reasoning, world knowledge, situation tracking, social reasoning), LLMs without added external modules (non-augmented LLMs) are uneven. They often need fine-tuning or external modules (p. 11–14).
- Language input can bootstrap non-linguistic capacities, so the authors do not claim that functional competence is out of reach for language-based models (p. 14).
- The authors speculate that models that use language like humans may need or benefit from modularity, either built in (architectural) or arising in training (emergent) (p. 14–15).
- Evaluation matters: fine-tuning and memorised test items can inflate results, closed models make such checks hard, and single examples are risky. Benchmarks that cleanly separate formal and functional skills are needed (p. 11, 15).

## L3 — Walkthrough

### The language-thought conflation (p. 1–3)
- In daily life we take sentences as a window into a thinking agent's world knowledge, reasoning and goals. Turing's 1950 test uses language as an interface to cognition (p. 1).
- The authors name two fallacies. **Good at language → good at thought**: the assumption that an entity producing long coherent text must possess rich knowledge and reasoning. It leads people to attribute intelligence even to Eliza, a 1960s chatbot. **Bad at thought → bad at language**: the authors call it the contrapositive. Some critics use LLMs' lack of consistent world knowledge or commonsense to suggest they are not good models of human language (p. 2).
- Both stem from the language-thought conflation. Our heuristics for judging language models come from experience with other humans and are "broken" for LLMs (p. 2).
- **Proposal:** distinguish *formal linguistic competence* (knowledge of rules and statistical regularities of language) from *functional linguistic competence* (ability to use language in real-world situations). The motivation is that these skills are robustly dissociable in the human brain (p. 2).
- **Claim:** modern LLMs' formal competence in English is near human level. Their functional competence is patchy and depends on domain and task. Formal competence improves drastically with training data. Functional gains from scale are less consistent, so developers moved to RLHF (reinforcement learning from human feedback) and to "augmented language models" coupled with external modules (p. 2).
- **Position:** next-word prediction allows a model to master formal but "not necessarily" functional competence. Much cognition (commonsense, science) can be conveyed through language and learned from it, so LLMs acquire some non-linguistic capacities. The ceiling for functional competence depends on open questions about what the linguistic signal contains (p. 2).
- Roadmap: define the distinction; LLMs' formal successes; functional shortfalls in four domains; implications; conclusions (p. 2–3).

*Intuition note:* A fluent speaker is not necessarily a good thinker, and a poor reasoner is not necessarily poor at grammar. The paper's evaluation framework rests on keeping these apart.

### Formal vs. functional linguistic competence (p. 3–5)
**What competence entails.**
- *Formal competence* is the set of capacities needed to produce and comprehend a language. It includes knowing which strings could be words (*blick* but not *bnick*), how to combine morphemes (Barack Obama-less-ness, not Barack Obama-ness-less), enough word meaning to know which words fit which slots, and how to combine words into valid sentences. The authors focus on the last (p. 3).
- Example: *The dogs in my bedroom are asleep*, not *…is asleep*. The verb agrees with the subject "dogs" although the closer noun is singular "bedroom". Also, "a days" is ill-formed, yet *a beautiful five days in New York* is allowed. So competence includes idiosyncratic constructions (p. 3).
- Humans likely learn the rules plus thousands of constructions through some combination of statistical learning and innate conceptual and/or linguistic machinery (p. 3).
- *Functional competence* is using language to accomplish goals: talking about perceived things, reasoning, requesting, cajoling. It works in tandem with perception, memory and social skills. A formal system in isolation is "useless" unless it interfaces with the rest of cognition (p. 3).
- Definition: functional competence is the *non-language-specific* cognitive functions required when using language together with non-language-specific capacities in real-world circumstances (p. 3).

**Figure 1 (p. 4).** Formal skills: phonology (blick/*bnick), morphology (Lady Gaga-esque-ness vs *Lady Gaga-ness-esque), lexical semantics (coffee with cream and sugar vs …and red), syntax (The key to the cabinets is vs. are on the table). Functional skills with a good/bad pair each: formal reasoning (14 birds, 3 left, 1 joined: twelve, not eleven); world knowledge (the trophy did not fit in the suitcase because the suitcase was too small, not "the trophy"); situation modeling (Sally owns a dog. The dog is black, vs Sally doesn't own a dog. The dog is black); social reasoning (a false-belief story about a toy moved to a closet). The caption says that determining whether a failure stems from formal or functional competence is key (p. 4).

**Motivation from the human brain (p. 3, 5).**
- The *language network* is a set of interconnected frontal and temporal areas, typically left hemisphere. It supports comprehension (spoken, written, signed) and production. It is sensitive to regularities from the sub-lexical to the sentence level and supports both word-meaning and combinatorial processing. Damage causes linguistic deficits (p. 3).
- fMRI (functional MRI: brain imaging with good spatial resolution) tests whether two abilities use the same brain regions. The language network responds to listening, reading or generating sentences. It does not respond to arithmetic, logical reasoning, computer programs, music, categorizing objects or events, reasoning about mental states, or non-verbal communication such as faces and gestures (p. 5).
- *Global aphasia* (impairment of both production and comprehension) leaves almost no language. The authors' logic is that if non-linguistic abilities used language resources, severe language loss "should invariably" impair them. Yet such individuals can play chess, solve arithmetic, use world knowledge, reason about cause and effect and navigate complex social situations (p. 5).
- Conclusion: the mechanisms that process language do not support non-linguistic cognitive tasks. So a model's linguistic abilities should be separated from its abstract knowledge and reasoning, which can be probed, and perhaps learned, through a linguistic interface but need more than formal competence (p. 5).

*Intuition note:* The authors borrow a split from the brain: one set of regions handles language form, others handle reasoning, social inference and so on. They use this as the motivation for testing the two kinds of competence separately in models.

### LLMs have largely mastered formal linguistic competence in English (p. 5–10)

**Framing.** Chomsky (2019), as quoted, asks whether deep learning is engineering or science; he says it is worth having on engineering grounds, like a bulldozer, and answers "Zero" to whether it tells us anything about human language. The authors say such resistance persists in linguistics. They argue LLMs are surprisingly successful at formal competence, qualitatively different from models before roughly 2018, and that their success is informative for linguistic theory (p. 5).

**Statistical language models: fundamentals (p. 5–6).**
- LLMs descend from statistical language modeling (n-gram models going back to Shannon), word embeddings (vectors in high-dimensional space) and connectionism (neural networks). All contrast with models using explicit hierarchical syntactic rules (p. 5).
- N-grams and embeddings succeeded at spelling correction, spam classification and sentiment analysis. They never approached human-level text generation. This fed claims that purely statistical approaches could not capture rich language. For example, it was claimed that models taking linear word strings are in principle unable to learn rare complex syntax needing hierarchy. The authors say LLMs now challenge this pessimism (p. 5–6).
- Pretraining objective: predict a held-out token (basic unit, often a word or morpheme) from a fixed number of previous tokens. Compare with the truth, propagate the error back to update parameters. Then often fine-tune for a task (p. 6).
- The authors argue significant formal abilities arise at GPT-2 or BERT scale and seem to plateau at a high level in contemporary LLMs (p. 6).

**Box 1 (p. 6).** Prompt: The meaning of life is…. A 3-gram model trained on *Moby Dick* and a 2011 RNN produce ungrammatical, senseless text. GPT-2 produces grammatical output (agreement, parts of speech, a relative clause tied to a noun phrase) but with less sense (e.g., its phrase about being with people). GPT-3 and GPT-4 give grammatical, coherent text that could plausibly be taken for human (p. 6).

**Box 2 – semantics (p. 7).** Lexical and compositional semantics (meaning from words and combinations) count as formal competence. The language network responds to both. Semantics as general conceptual knowledge (e.g., "non-verbal semantics") is closely tied to world knowledge and is classed as functional (p. 7).

**Evidence that LLMs learn core aspects of language (p. 7–9).** The authors focus on syntax. They say similar successes exist in phonology, morphology and lexical semantics (p. 7).

1. *Benchmarks.* BLiMP has minimal pairs (grammatical vs ungrammatical) over phenomena such as filler-gap dependencies and negative polarity items. A model submitted to the BabyLM challenge scored 86% on BLiMP (human baseline 89%) with data comparable to a child's exposure. SyntaxGym gives similar results (p. 7).
2. *Hierarchy.* Hierarchical structure means words combine into tree-like structures, not linear sums. Take subject-verb agreement. A bigram model, which stores two-word frequencies, can prefer "keys are" over "keys is". It cannot capture agreement at arbitrary distance, as in *The keys to the old, wooden kitchen cabinet are on the table*, with six intervening words (p. 7–8). Today's LLMs do long-distance agreement well above chance despite distractors, although some earlier models can be distracted by frequency effects. They also handle filler-gap dependencies. Geometry analyses, causal interventions and neuron ablations give mechanistic hints (p. 8).
3. *Abstractions.* An abstraction is a generalised representation (part of speech, grammatical role) that goes beyond storing input (p. 8). One way to test knowledge of abstract rules is to use semantically nonsensical sentences (*The colorless green ideas I ate with the chair… (sleep/sleeps)*). Models have been shown to do the agreement task well in several languages even on these. A BERT study with novel words (*blick* as noun, *dax* as verb) found that BERT succeeds partially: it does learn to generalise, but only after repeated examples. *Probing* trains a classifier on internal states to recover categories such as part of speech. One claim is that LLMs rediscover the classical NLP pipeline (although see [96]) (p. 8). A humanlike model is not expected to rely only on abstract rules, since humans also use other cues and memorised input. So LLM performance should be compared directly with humans. A re-examination found that apparent agreement deficits in GPT-2 occurred on items hard for humans too. The authors conclude LLMs learn some abstraction, though its degree is debated (p. 8).
4. *Constructions.* LLMs learn idiosyncratic, relatively rare constructions, e.g., *a beautiful five days in Austin*. They show some sensitivity to the Preposing in Prepositional Phrase construction even across a finite-clause boundary (*Surprising though I know it may be*), where only 58 examples occur in 7 billion sentences. Learning that some rare constructions are grammatical and others equally rare are not suggests they learn something about syntax (p. 8). For the comparative correlative (*the better the syntax, the better the semantics*), models are sensitive to the form, yet inferences from it appear challenging. The authors say this asymmetry illustrates the formal/functional distinction (p. 8–9).

**LLMs are predictive of human language-network activity (p. 9).**
- The language network is sensitive to hierarchical rules in phrases, narratives and jabberwocky (syntactically well-formed, semantically empty) stimuli. It is also sensitive to word co-occurrence (n-gram surprisal). The authors therefore *operationalize* formal competence as computations that humans perform in the language network (p. 9).
- Similarities: both operate on abstract units (words/tokens) rather than pixels or waveforms, and both build phrase and sentence representations. Neither shows clear spatial segregation of syntax and semantics. Moreover, a direct mapping from LLM representations to neural activity predicts responses to novel sentences and words (p. 9).
- The correspondence is not claimed to be one-to-one (e.g., LLMs predict newline characters). Still, it indicates at least some correspondence (p. 9).

**Using LLMs as models of human formal competence (p. 9).** LLMs are not perfect learners of abstract rules, but neither are humans. The authors conclude LLMs possess substantial formal competence, at least in English. They have overturned claims that certain knowledge (hierarchical structure, abstract categories) cannot be acquired from input statistics alone. If models improve, including on realistic amounts of data, they can test more general poverty-of-the-stimulus arguments and what inductive biases (built-in learning preferences) are needed (p. 9).

*Intuition note:* One way to test "knows grammar" is whether a model prefers the grammatical member of minimal pairs, including across distractors, nonsense words and rare constructions. LLMs pass many of these tests, so the old argument that statistics alone cannot yield grammar is weakened.

**Box 3 – limitations as models of human learners (p. 10).**
- *Reliance on statistics:* models can be right for the wrong reason, and noise or distractors can hurt them in ways that do not always affect humans. But GPT-2 generated mostly novel 5-grams and above, though n-grams up to length 4 often appeared in training. So LLMs seem capable of some generalisable morphosyntactic knowledge beyond mere memorising (p. 10).
- *Unrealistic data:* best LLMs see far more data than a child. Some evidence suggests the training set would need to be unrealistically large for some constructions without stronger priors. The BabyLM challenge uses 10M or 100M words, thought to be in the range heard by a 10-year-old. The best 2023 model did well on BLiMP. Smaller models still match human neural responses well (p. 10).
- *Languages other than English:* models work best with vast corpora. Architectures may be biased toward English and European languages. Evidence is growing of strong performance in other languages and of transfer to low-resource ones, but caution is warranted, especially for typologically distinct or signed languages (p. 10).

### Non-augmented LLMs fall short on functional linguistic competence (p. 9–14)
Four capacities, none language-specific: (i) formal reasoning (logic, maths, computational thinking, novel problem solving); (ii) world knowledge (factual and commonsense); (iii) situation modeling (tracking objects, agents and events as a narrative unfolds); (iv) social reasoning (understanding social context) (p. 9–11). For each, the authors summarise human neural mechanisms, then LLM performance. Their conclusion: LLM functional competence is uneven, often needing specialised fine-tuning and/or lacking humanlike robustness and generality (p. 11).

**Box 4 – evaluating functional competence (p. 11).**
- *A. Fine-tuning and closed models.* Formal skills can be observed in many LLMs trained on word-in-context prediction, without task-specific fine-tuning. Functional skills are often boosted by fine-tuning or RLHF. Claims that LLMs succeed at Theory of Mind often apply to fine-tuned models, not generic predictors. In the extreme, task materials are in the training set. LLMs memorise a lot, more so when larger, so performance can be highly inflated. Closed models make these checks hard or impossible. The authors expect scientific knowledge to come from transparent models (p. 11).
- *B. Generalizable, robust performance.* Test across tasks, prompts and scenarios. A model may exploit low-level co-occurrence (e.g., entailment judged by lexical overlap) and drop to chance when such cues are removed. Avoid reliance on single examples. The authors believe evaluation issues have led to "particularly large" overclaiming about functional competence (p. 11).

**Formal reasoning (p. 11–12).**
- *Humans:* formal reasoning engages the *multiple demand network* (regions active in many cognitively demanding tasks): logic, maths, physical reasoning, code comprehension. Damage to these regions correlates negatively with fluid intelligence test performance. This network supports reasoning even when the task is presented in words, as LLM prompts are (p. 12).
- *LLMs:* GPT-3 does two-digit addition and subtraction well but not three-digit addition or two-digit multiplication. GPT-4 is good on small-digit operations but not large-digit ones. Tests that break common co-occurrence patterns or need multi-step operations cause failures. A commonly cited reason is failure to generalise outside the training distribution. Chain-of-thought prompting (generate intermediate steps first) partly bridges the gap but is not foolproof. Hence the shift to pairing LLMs with external modules (a Mathematica plugin, a probabilistic reasoning engine). The authors say this matches the neuroscience of separate mechanisms (p. 12).

**World models 1: factual and commonsense knowledge (p. 12–13).**
- *Humans:* language deficits can leave reasoning about non-linguistically presented objects and events intact. Semantic dementia leaves speech but impairs world knowledge (e.g., pumpkins are typically orange) even with pictures. So linguistic and semantic knowledge can be disentangled (p. 12).
- *LLMs:* word co-occurrence holds factual and commonsense information, so LLMs could serve as knowledge bases if it can be extracted. Four shortcomings (p. 12–13):
  1. *Hallucinations:* false statements, unsurprising since the objective is plausible continuation, not factual correctness. Cited sources can also be inaccurate.
  2. *Inconsistency:* differently phrased prompts give different answers, and irrelevant intervening claims distract the model.
  3. *Commonsense is underrepresented in text:* people communicate new or unusual information more than common facts. Models can struggle on commonsense benchmarks, especially once low-level cues are controlled.
  4. *Hard to update:* humans update from one sentence. Editing a fact in LLM parameters means locating and editing it, with related facts changing and others unaffected.
- A more humanlike approach might separate linguistic processing from knowledge storage and updating. Such approaches exist but have low coverage. LLMs may serve as a starting point for building knowledge bases and commonsense schemata (p. 13).

**World models 2: situation tracking (p. 13).**
- A *situation model* is a mental model of entities, relations and event sequences built from language. *Humans:* the language network does not appear to track structure above the clause level. Integration over longer spans likely occurs in the *default network*, which tracks linguistic and non-linguistic narratives, so situation modeling is not language-specific (p. 13).
- *LLMs:* two challenges are extracting information from many sentences and updating entity states. The first is tackled by enlarging the *context window* (words processed at once). This will run into computational inefficiency, and hierarchical summarising might be more humanlike. Some evidence says models can update states over short spans, but they make non-humanlike errors, e.g., referring to non-existent entities (*Arthur doesn't own a dog. The dog is brown.*). Whether robust situation modeling is feasible with an LLM-only architecture is a matter of debate (p. 13).

**Social reasoning (p. 13–14).**
- Wittgenstein's one-word utterance "Water!" shows meaning depends on context. Pragmatics (inferring intended meaning beyond literal content) likely engages several neural mechanisms, so some pragmatic reasoning counts as formal and some as functional. The authors focus on social reasoning (p. 13).
- *Humans:* the *theory of mind network* (regions engaged when inferring mental states, with or without language) is engaged by narratives needing inference of characters' mental states and intentions. It is engaged more strongly during non-literal language (jokes, sarcasm, indirect speech, implicature) (p. 13–14).
- *LLMs:* RLHF-trained models interpret metaphors and polite deceits at human or near-human level, suggesting at least some pragmatic tasks can be reached. Performance is uneven: sarcasm and jokes were limited while metaphor comprehension "soared". Some pragmatic inference might be acquired by targeted fine-tuning. It is open whether the aspects easiest for LLMs are those the language network supports in humans (p. 14).
- *Theory-of-mind (false-belief) tasks:* character X moves an object from A to B while Y is away. The model must say where the object is (B) and where Y believes it is (A). **Claim [185]:** instruction-tuned LLMs mastered such tasks. **Counter [186]:** simple controls (e.g., Y told the true location) pushed performance below chance. Other studies also find limits (cf. [190]). One remedy augments an LLM with a symbolic tracker of entity states and character beliefs, mirroring the language/theory-of-mind separation in humans (p. 14).

*Intuition note:* Across the four domains the pattern is similar: in humans a non-language network is involved, and non-augmented LLMs are uneven there. Fixes often involve fine-tuning or an outside module (in situation tracking, also longer context windows).

**Language input can bootstrap functional competence (p. 14).** Humans learn categories more easily with labels, children with delayed language access show delayed social reasoning, and number words predict exact-number concepts. Since language contains vast information about the world, the authors say this evidence suggests that, in principle, a model trained only on language could acquire much of functional competence. They do not argue it is out of reach. Their aims are to highlight the distinction and to show the gulf between LLMs' formal and functional abilities (p. 14).

### Toward models that use language like humans (p. 14–15)
- **Thesis:** formal and functional competence are distinct. Formal competence emerges from the word-in-context objective, which alone "appears insufficient" for functional skills. Based on neuroscience, the authors *suggest* successful real-life models will need to be modular (p. 14).
- **Architectural Modularity:** explicitly stitch separate components together. Examples: a transformer with a memory module; a visual question answering model with language, vision and reasoning modules. Such models achieve high task performance, are more efficient and show better generalisability. They also include LLMs calling APIs, calculators and planners (p. 14–15).
- Wong et al. [149]: a GPT-3 version fine-tuned on language and code (Codex) translates text into structured probabilistic programs. Inference in them supports reasoning over kinship, visual scenes and planning. This is a route to combine LLM formal competence with symbolic modules (p. 15).
- **Emergent Modularity:** train end-to-end and create conditions for specialised sub-components to emerge. Modularity has spontaneously emerged in some non-language networks. Transformers incentivise it somewhat (different attention heads attend to different features), and mixture-of-experts architectures do so more explicitly (p. 15).
- Non-modular systems could in theory behave similarly. But explicitly separating formal and functional skills in the architecture is, as the authors put it, perhaps the most fail-safe route to humanlike language use (p. 15).
- **Box 5 – better benchmarks:** formal benchmarks exist (BLiMP, SyntaxGym) and can be extended to hierarchy and abstraction. Functional benchmarks like WinoGrande can often be "hacked" through flawed heuristics, perhaps more in large heterogeneous sets like BIG-bench. They also mix functional abilities and assume an underspecified level of formal skill. Benchmarks should disentangle components (p. 15).

### Concluding remarks (p. 15–16)
- Discourse mixes overclaiming and underclaiming. LLMs are remarkably successful on formal competence and are underused in linguistics as candidate models of human language processing. Their failures on reasoning and similar tasks do not undermine their value as language models, since the human language areas also cannot do maths, solve logic problems or track a story's meaning across paragraphs (p. 16).
- Future intelligent systems may need language models combined with models of abstract knowledge and reasoning, not a single word-prediction model doing everything (p. 16).
- Messages: to those saying interesting aspects of language cannot be learned from data, LLMs show that complex syntax can be learned from input (though with far more input than a child gets). To critics of LLM arithmetic or reasoning: evaluate these abilities separately. To engineers: instead of, or in addition to, scaling up, modular architectures (built-in or emergent) are likely more promising (p. 16).

### Glossary, Highlights, Outstanding Questions (p. 16–18)
- The Glossary notes that "competence" here differs from the classic competence/performance distinction in linguistics, because the two are hard to separate in models and humans (p. 16). It also says RLHF seems to lead to significant improvements on functional tasks (p. 17).
- Outstanding questions include: how much functional competence can be learned from the linguistic signal and whether some aspects cannot be learned from language at all; how to train on child-scale data; transfer to other languages; how long LLM growth will continue; architectural vs emergent modularity; how modular today's LLMs are (mechanistic interpretability may tell); agent-based vs tool-based views of LLMs; how much grounding LLMs need; how much LLMs can tell us about human cognition (p. 17–18).

## Toy example (ours, not from the paper)
**Part A: why form needs more than adjacent-word counts.** Training corpus of 6 sentences: *the keys are here* (×3), *the key is here* (×1), *the cabinet is old* (×2). Count bigram "keys are" = 3, "keys is" = 0. Count of words after "cabinet": "cabinet is" = 2. Estimate $P(\text{are}\mid\text{keys}) = 3/3 = 1$. Now complete *the keys to the cabinet ___*. A bigram model sees only "cabinet": $P(\text{is}\mid\text{cabinet}) = 2/2 = 1$. It predicts "is" and so picks the wrong agreement. The correct choice "are" needs the subject "keys" (a hierarchical relation, p. 7–8). This is why distant agreement is a test of hierarchy, not of adjacent counts.

**Part B: form is not function.** Take *Sally doesn't own a dog. The dog is black.* Both sentences are grammatical, so a form checker gives 2 of 2 passes. Add a tiny symbolic tracker (the kind of module suggested on p. 14, 15). Sentence 1 sets owns(Sally, dog) = False, so the entity table has 0 dogs. Sentence 2 uses "the dog", which needs ≥ 1 dog in the table, and 0 < 1, so it flags a problem. Result: form checker 2/2, tracker flags 1 of 2. The two checks differ, which is the formal/functional gap in miniature.

## Concepts
- [[formal-vs-functional-competence]] — formal: rules and statistical regularities of language; functional: using language in the world via non-language-specific cognition (pp. 2–3)
- [[language-model]] — here, a model trained on word-in-context prediction; "large" refers to parameters and training data (p. 6, 16)
- [[n-gram-model]] — a model storing frequencies of short word strings; cannot track agreement at arbitrary distance (p. 5, 7)
- [[pretraining-fine-tuning]] — generic text-prediction training, then extra task-specific training; key for judging functional claims (p. 6, 11)
- [[rlhf]] — reinforcement learning used to impart human preferences; said to improve functional tasks (p. 2, 17)
- [[chain-of-thought]] — prompting to output intermediate steps before answering; partly bridges generalisation gaps (p. 12)
- [[tokenization-bpe]] — tokens are basic units, often inferred with Byte Pair Encoding, sometimes linguistically unnatural (p. 6, 17)
- [[form-vs-meaning]] — related: lexical/compositional semantics counts as formal, conceptual semantics as functional (Box 2, p. 7)
- [[symbol-grounding]] — related: raised only as an open question about how much grounding LLMs need (p. 18)
- [[language-network]] (new) — brain regions selective for language, not non-linguistic tasks (p. 3, 16)
- [[multiple-demand-network]] (new) — brain regions engaged by many demanding tasks, including formal reasoning (p. 12)
- [[default-network]] (new) — brain network integrating meaning over long narratives, linguistic or not (p. 13)
- [[theory-of-mind]] (new) — reasoning about others' knowledge, beliefs and wants; has its own brain network (p. 13, 17)
- [[situation-model]] (new) — mental model of entities, relations and events built from language input (p. 13)
- [[linguistic-abstraction]] (new) — generalised representation such as part of speech, allowing generalisation (p. 8, 16)
- [[probing]] (new) — training a classifier on internal states to test if a category is recoverable (p. 8)
- [[minimal-pair-benchmark]] (new) — paired grammatical/ungrammatical sentences, as in BLiMP (p. 7)
- [[architectural-modularity]] (new) — explicitly built-in separate modules (p. 14, 16)
- [[emergent-modularity]] (new) — specialisation arising from training, not design (p. 14–15, 16)
- [[hallucination]] (new) — fluent but false LLM statements; objective is plausibility, not truth (p. 12)

## Canonical instances
- [[turing-test]] — language used as interface to cognition; fuels the conflation (p. 1–2)
- [[eliza]] — 1960s chatbot to which intelligence was wrongly attributed (p. 2)
- [[subject-verb-agreement-distractors]] — long-distance agreement across intervening words (keys … cabinet … are) as a hierarchy test (p. 3, 7–8)
- [[colorless-green-ideas-agreement]] — agreement on nonsense sentences tests abstract rules rather than shallow collocation (p. 8)
- [[blick-dax-novel-words]] — BERT generalises categories partially, only after repeated examples (p. 8)
- [[blimp-babylm]] — BabyLM model scored 86% vs human 89% on BLiMP with child-scale data (p. 7)
- [[comparative-correlative]] — form learned, inferences hard (p. 8–9)
- [[false-belief-task-llm-controversy]] — claimed mastery [185] vs below-chance with controls [186] (p. 14)
- [[arthur-dog-nonexistent-entity]] — model refers to an entity never introduced (p. 13)
- [[water-wittgenstein]] — one-word utterance whose intended meaning depends on context (p. 13)
- [[meaning-of-life-generations]] — Table I: n-gram, RNN, GPT-2/3/4 outputs (p. 6)
- [[codex-probabilistic-programs]] — LLM translates language into code for symbolic inference (p. 15)

## Bridges (candidates)
- [structural-analogy] Formal/functional split ↔ cognitive neuroscience: language network vs multiple-demand, default and theory-of-mind networks — the paper uses brain dissociations as a template for model evaluation.
- [structural-analogy] Architectural modularity (LLM + calculator, planner, memory) ↔ tool-augmented LLM and retrieval systems — the same division of labour as language network plus reasoning regions.
- [structural-analogy] Probing classifiers on hidden states ↔ decoding analyses in fMRI — both ask whether a category is recoverable from internal activity.
- [metaphor] "Right for the wrong reason" benchmark hacking ↔ social-science construct validity — a score can reflect shortcuts and not the target ability.
- [structural-analogy] LLM-to-brain mapping predicting responses to new sentences ↔ encoding models in neuroscience — a linear-style mapping from model features to neural data, tested on held-out items.

## Questions this raises
- Which functional abilities, if any, cannot be learned from the language signal at all (p. 17)?
- How could one test whether an LLM's formal and functional processing are actually segregated inside its weights (p. 17)?
- If formal competence needs far more data than a child receives, which inductive biases would close the gap (p. 10)?
- Should LLMs be treated as individual language users or as tools or distributions over outputs (p. 18)?

## Reading notes
- Printed page numbers equal pdf page numbers (offset 0). Pages 18–30 (apart from the last Outstanding Questions on p. 18) are acknowledgements, funding, conflicts statement and the reference list [1]–[218]. The reference list was not digested.
- Header on every page: A PREPRINT - APRIL 14, 2024; first page carries the arXiv identifier 2301.06627v3 [cs.CL], dated 23 Mar 2024. The unit metadata cites the Trends in Cognitive Sciences version; the pages given are the arXiv preprint.
- The Glossary, Highlights and Outstanding Questions come after the Concluding remarks (p. 16–18). The Highlights state that LLMs began achieving unprecedented success in formal competence in the late 2010s (p. 17).
- Minor typos in the source: "regularitiesof" (p. 3), "with our without" (p. 13, presumably "with or without"), "function competence" (p. 14, presumably "functional").
- Figure 1 (p. 4): in the image, the correct answer "box" in the social-reasoning panel appears coloured red like the incorrect "closet". This looks like a colouring slip; I have not interpreted it.
