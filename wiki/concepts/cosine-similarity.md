---
id: cosine-similarity
type: concept
fields: [linear-algebra, political-science]
n_sources: 7
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch03-norm, deerwester-1990-lsa/main, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch06-probability-p1, grimmer-2022-textasdata/ch07-vector, mikolov-2013-regularities/main, strang-2023-introduction/ch01-vectors]
raw_ids: [cosine similarity]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# cosine-similarity

## Canon spine entry

- **cosine similarity** (linear-algebra): the inner product of normalized vectors; the angle between them, the standard similarity in embeddings (UG)

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch03-norm]] (pp. 57, 59): aᵀb/(‖a‖‖b‖) = cos θ; the angle between vectors, usable for documents
- [[deerwester-1990-lsa/main]] (pdf 8–9): dot product or cosine between vectors in the factor space estimates similarity; cosine is used to rank documents
- [[deisenroth-2020-mml/ch03-analytic]] (p. 76): here the angle via $\cos\omega=\langle x,y\rangle/(\|x\|\|y\|)$ [as `cosine similarity`]
- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 196): here correlation is the cosine of the angle between random variables [as `cosine similarity`]
- [[mikolov-2013-regularities/main]] (p. 748): the score used to find the word nearest to $y$; length is ignored
- [[strang-2023-introduction/ch01-vectors]] (p. 12): cos θ = v·w/(‖v‖‖w‖) (p. 12); this unit only derives it as the angle between vectors

### political-science

- [[grimmer-2022-textasdata/ch07-vector]] (p. 130): inner product of magnitude-normalized vectors; depends only on direction [new]

## Candidate bridges

- [structural-analogy] Cosine formula (Ex. 15) and the angle definition in Ex. 16 ↔ cosine similarity of embeddings: $\langle x,y\rangle/(\|x\|\|y\|)$. — from [[axler-2024-ladr/ch06-inner-p1]] (linear-algebra → other)
- [same-math] Correlation coefficient ρ = cos∠(ã, b̃) ↔ cosine similarity of centred data vectors — the same formula, applied to mean-removed vectors. — from [[boyd-2018-vmls/ch03-norm]] (linear-algebra → unspecified)
- [structural-analogy] word-histogram vectors and distance ↔ cosine similarity / embeddings: documents as vectors compared by geometry, though this chapter uses Euclidean distance, not cosine. — from [[boyd-2018-vmls/ch04-clustering]] (linear-algebra → other)
- [structural-analogy] Terms and documents in one space with cosine similarity ↔ modern word and document embeddings. — from [[deerwester-1990-lsa/main]] (linear-algebra → unspecified)
- [structural-analogy] "Similar vectors get similar predictions" ↔ linear algebra: inner-product similarity such as cosine similarity (p. 14). The unit does not name the operation. — from [[deisenroth-2020-mml/ch01-introduction]] (linear-algebra → linear-algebra)
- [structural-analogy] Projection onto a line ↔ cosine similarity: $\|\pi_U(x)\|=|\cos\omega|\|x\|$ links projection length to angle (p. 84). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other)
- [same-math] correlation $=\cos\theta$ (6.61) ↔ linear-algebra: cosine similarity — the inner product of normalised (centred) vectors. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [same-math] cosine similarity ↔ geometry: cosine of the angle between vectors; for unit vectors, squared Euclidean distance $=2(1-\cos)$ (p. 133). — from [[grimmer-2022-textasdata/ch07-vector]] (political-science → other)
- [same-math] Nearest word by $\frac{x_w\cdot y}{\|x_w\|\|y\|}$ ↔ cosine similarity as angle between vectors. — from [[mikolov-2013-regularities/main]] (linear-algebra → unspecified)
- [same-math] relevance as cosine similarity of embeddings ↔ distributional semantics: similarity of dense vectors. — from [[park-2023-agents/main]] (llm → other)
- [same-math] cos θ = v·w/(‖v‖‖w‖) ↔ embeddings/NLP: cosine similarity between vectors — the same formula, read as similarity. — from [[strang-2023-introduction/ch01-vectors]] (linear-algebra → llm)
