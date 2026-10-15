---
id: cnn-dailymail-tldr
type: instance
fields: [llm]
n_sources: 1
tiers: [deep]
grounding: digests
sources: [radford-2019-gpt2/main]
canon_instance: [tldr-zero-shot-summarization]
canon_match_rule: confirmed
generated_by: build_kg.py
---

# cnn-dailymail-tldr

## Canon entry

- **"TL;DR:" zero-shot summarization** (llm): appending a cue string makes a plain LM summarize — radford-2019-gpt2

## Descriptions in the sources

### llm

- [[radford-2019-gpt2/main]] (pdf 6): summarization induced by `TL;DR:`; R-AVG 21.40 versus 15.03 without the hint
