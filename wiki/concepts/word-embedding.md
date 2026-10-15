---
id: word-embedding
type: concept
fields: [llm, linear-algebra, political-science]
n_sources: 7
tiers: [deep, core, reference]
grounding: digests
sources: [bengio-2003-nplm/main, grimmer-2022-textasdata/ch08-distributed, mikolov-2013-compositionality/main, mikolov-2013-efficient/main, mikolov-2013-regularities/main, park-2023-agents/main, prince-2023-udl/ch12-transformers]
raw_ids: [word embedding]
canon_spine: llm
generated_by: build_kg.py
---

# word-embedding

## Canon spine entry

- **word embedding** (llm): a dense vector for each word, learned so that geometry reflects usage (UG)

## Definitions in the sources

### llm

- [[bengio-2003-nplm/main]] (p. 1139): here the "distributed word feature vector" $C(i) \in \mathbb{R}^m$, row $i$ of a learned matrix, trained jointly with the predictor [as `word embedding`]
- [[mikolov-2013-compositionality/main]] (p. 1): "distributed representation": a dense vector per word (or phrase) [as `word embedding`]
- [[mikolov-2013-efficient/main]] (p. 2): continuous dense word vector learned by a network; here used with arithmetic on vectors
- [[park-2023-agents/main]] (pdf 9): here an LLM-generated vector of each memory's text; relevance is the cosine similarity [as `word embedding`]
- [[prince-2023-udl/ch12-transformers]] (p. 218): learned vector per token, $\mathbf X=\boldsymbol\Omega_e\mathbf T$ [as `word embedding`]

### linear-algebra

- [[mikolov-2013-regularities/main]] (p. 747): learned vector representation of a word, here the input-layer weights [new]

### political-science

- [[grimmer-2022-textasdata/ch08-distributed]] (pp. 141–142): dense length-$K$ vector ($K<J$) per word, learned from unlabeled text [new]

## Instances that use it

- [[word-embedding-arithmetic]] — king − man + woman = queen as evidence for directions — from [[elhage-2022-superposition/main-p1]]

## Candidate bridges

- [same-math] Embedding matrix $C$ (look-up of rows) ↔ word embedding: learned token embedding table — from [[bengio-2003-nplm/main]] (llm → other)
- [structural-analogy] Word embeddings from co-occurrence ↔ political-science: the spatial model of voting — both place items in a low-dimensional space where distance means similarity. — from [[grimmer-2022-textasdata/ch08-distributed]] (political-science → political-science)
