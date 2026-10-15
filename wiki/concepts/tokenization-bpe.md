---
id: tokenization-bpe
type: concept
fields: [llm]
n_sources: 7
tiers: [core, deep, reference]
grounding: digests
sources: [brown-2020-gpt3/main-p1, devlin-2019-bert/main, kaplan-2020-scaling/main, mahowald-2024-dissociating/main, prince-2023-udl/ch12-transformers, radford-2019-gpt2/main, vaswani-2017-transformer/main]
raw_ids: [tokenization (BPE)]
canon_spine: llm
generated_by: build_kg.py
---

# tokenization-bpe

## Canon spine entry

- **tokenization (BPE)** (llm): splitting text into subword units by repeatedly merging frequent byte or character pairs (UG)

## Definitions in the sources

### llm

- [[brown-2020-gpt3/main-p1]] (pp. 16, 24): byte-level BPE inherited from GPT-2, about 0.7 words per token; the authors suggest it may hurt En→Ro and complicates character-level tasks
- [[devlin-2019-bert/main]] (p. 4174): related only: BERT uses WordPiece with a 30,000-token vocabulary; the paper does not describe its algorithm [as `tokenization (BPE)`]
- [[kaplan-2020-scaling/main]] (p. 6, p. 5): byte-pair encoding, vocabulary 50257; changing it rescales the loss and the constants
- [[mahowald-2024-dissociating/main]] (p. 6, 17): tokens are basic units, often inferred with Byte Pair Encoding, sometimes linguistically unnatural
- [[prince-2023-udl/ch12-transformers]] (p. 218): greedy merging of frequent adjacent token pairs into sub-word tokens [as `tokenization (BPE)`]
- [[radford-2019-gpt2/main]] (pdf 4): subword merging between word and character level; here applied to bytes with category restrictions [as `tokenization (BPE)`]
- [[vaswani-2017-transformer/main]] (p. 7): byte-pair and word-piece vocabularies used for translation

## Candidate bridges

- [structural-analogy] Phrase token merging ↔ tokenization (BPE): both build larger units from frequent adjacent pairs (here one score and threshold, not iterative merges). — from [[mikolov-2013-compositionality/main]] (llm → other)
