---
id: dot-product
type: concept
fields: [linear-algebra]
n_sources: 2
tiers: [core, deep]
grounding: digests
sources: [deerwester-1990-lsa/main, strang-2023-introduction/ch01-vectors]
generated_by: build_kg.py
---

# dot-product

## Definitions in the sources

### linear-algebra

- [[deerwester-1990-lsa/main]] (pdf 8–9): dot product or cosine between vectors in the factor space estimates similarity; cosine is used to rank documents
- [[strang-2023-introduction/ch01-vectors]] (p. 9): v·w = Σvᵢwᵢ; gives length, perpendicularity, angle

## Instances that use it

- [[angle-depends-on-inner-product]] — $[1,1]$ and $[-1,1]$ are orthogonal under the dot product, 109.5° apart under diag(2,1) — from [[deisenroth-2020-mml/ch03-analytic]]

## Candidate bridges

- [structural-analogy] additive alignment score $v_a^\top\tanh(W_as+U_ah)$ ↔ LLM canon, attention: query–key similarity then a weighted average of values. Here keys and values are both $h_j$ and the score is an MLP, not a dot product. — from [[bahdanau-2015-attention/main]] (llm → llm)
- [same-math] IR score = count-weights · type-weights ↔ linear models: weighted sum of features — literally a dot product (pdf 12). — from [[brin-1998-anatomy/main]] (linear-algebra → other)
