---
id: zero-shot-few-shot-prompting
type: concept
fields: [llm]
n_sources: 17
tiers: [core, deep, reference]
grounding: digests
sources: [argyle-2023-silicon/main-p1, bai-2022-constitutional/main, brown-2020-gpt3/main-p1, brown-2020-gpt3/main-p2, brown-2020-gpt3/main-p3, hoffmann-2022-chinchilla/main, ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, ouyang-2022-instructgpt/main-p3, prince-2023-udl/ch12-transformers, radford-2019-gpt2/main, wei-2022-cot/main-p1, wei-2022-cot/main-p2, wei-2022-emergent/main, xie-2022-icl/main, ziems-2024-css/main-p1, ziems-2024-css/main-p2]
raw_ids: [zero-shot / few-shot prompting]
canon_spine: llm
generated_by: build_kg.py
---

# zero-shot-few-shot-prompting

## Canon spine entry

- **zero-shot / few-shot prompting** (llm): specifying a task with only an instruction, or with a few examples in the prompt (UG)

## Definitions in the sources

### llm

- [[argyle-2023-silicon/main-p1]] (p. 12): in Study 3, the format alone induces short survey-style answers, using GPT-3's zero-shot learning property
- [[bai-2022-constitutional/main]] (p. 8, p. 11): few-shot examples fix the critique, revision and labelling formats
- [[brown-2020-gpt3/main-p1]] (pp. 5–7): zero-/one-/few-shot = 0 / 1 / K (typically 10–100) demonstrations in context, plus an optional natural-language description
- [[brown-2020-gpt3/main-p2]] (pp. 29–30): demonstrated by the novel-word and grammar prompts [as `zero-shot / few-shot prompting`]
- [[brown-2020-gpt3/main-p3]] (pp. 60, 63): the three settings (zero, one, few examples in the context) under which every task is scored in Table H.1; the zero-shot translation template differs from the one/few-shot one
- [[hoffmann-2022-chinchilla/main]] (p. 11): evaluation protocol used throughout, e.g. 5-shot MMLU
- [[ouyang-2022-instructgpt/main-p1]] (p. 9): the GPT-3-prompted baseline prepends a few-shot prefix to emulate instruction following [as `zero-shot / few-shot prompting`]
- [[ouyang-2022-instructgpt/main-p2]] (p. 26): few-shot labeler prompts yield $K$ SFT examples from $K$ pairs
- [[ouyang-2022-instructgpt/main-p3]] (pp. 44–50): the benchmark settings, with 0 or 2–15 in-prompt examples
- [[prince-2023-udl/ch12-transformers]] (p. 225): here only the few-shot case: examples are given in the context, with no fine-tuning [as `zero-shot / few-shot prompting`]
- [[radford-2019-gpt2/main]] (pdf 2, 6): performing a task with no parameter change, using only the context; here sometimes with example pairs in the context [as `zero-shot / few-shot prompting`]
- [[wei-2022-cot/main-p1]] (pp. 2–3): here, few-shot prompting: input–output exemplars placed in the prompt before the test question
- [[wei-2022-cot/main-p2]] (p. 28, p. 30): the method uses a fixed few-shot prompt (8 exemplars in the main experiments per p. 28; the printed prompts in Tables 20–28 have 4 to 8), with no finetuning
- [[wei-2022-emergent/main]] (p. 3): giving a pre-trained model a prompt, with or without a few examples, with no gradient updates
- [[xie-2022-icl/main]] (p. 11): prompts with 0 or $n$ examples; in GINC zero-shot can beat few-shot early on
- [[ziems-2024-css/main-p1]] (pp. 238, 261): specifying a task with instructions only (zero-shot) or with 3 or 5 examples (few-shot); the paper tests both on FLAN
- [[ziems-2024-css/main-p2]] (p. 270): specifying a task with an instruction (zero-shot) or a few examples (few-shot); the paper says this blurs supervised and unsupervised paradigms
