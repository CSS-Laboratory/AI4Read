---
id: park-2023-agents/index
work: park-2023-agents
type: work-map
units: [park-2023-agents/main]
generated: deterministic
---

# Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. Proceedings of UIST 2023 (ACM). arXiv:2304.03442.

## One digest
This work has a single digest, which is also its work-level summary: [[park-2023-agents/main]].

## In one line
Wrapping a language model in a natural-language memory stream with scored retrieval, reflection and planning yields simulated characters that behave believably over days and show emergent social behaviour.

## The gist
How can language models drive believable, long-lived simulated people? The authors build an architecture around ChatGPT: a natural-language memory stream, retrieval scored by recency, importance and relevance, periodic reflection, and recursive planning. Twenty-five agents live in a Sims-like town, Smallville. In an interview-based test, 100 human raters judged the full architecture more believable than ablations and a crowdworker baseline. Over two game days, information spread, relationships formed, and a party was coordinated from a seeded party intent. Errors included failed retrieval, memory embellishment and overly formal, agreeable speech.

**Prerequisites:** prompting a chat LLM; embeddings and cosine similarity; exponential decay; min-max scaling; basic graph density; rank-based statistics (Elo-style ratings, Kruskal-Wallis).
