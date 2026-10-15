---
id: attention
type: concept
fields: [llm, bayesian, theory-of-mind]
fields_strong: [llm, bayesian, theory-of-mind]
n_sources: 6
n_works: 5
tiers: [reference, deep, core]
grounding: digests
sources: [bahdanau-2015-attention/main, kosinski-2024-llm-tom/main, murphy-2023-pml2/ch16-deep, prince-2023-udl/ch12-transformers, prince-2023-udl/ch13-graph, vaswani-2017-transformer/main]
aliases: [attention-layer, attention-mechanism]
canon_spine: [llm]
generated_by: build_kg.py
---

# attention

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `attention-layer` — 1 digest(s)
- `attention-mechanism` — 1 digest(s)

## Canon spine entry

- **attention** (llm): a weighted average of value vectors, with weights from query–key similarity (UG)

## Definitions in the sources

### llm

- [[bahdanau-2015-attention/main]] (p. 4): decoder computes a weighted sum of source annotations; weights from the previous decoder state and each annotation
- [[prince-2023-udl/ch12-transformers]] (p. 208): non-negative weights summing to one that route values to outputs; here from softmax of query–key dot products
- [[prince-2023-udl/ch13-graph]] (p. 260): here, weights over neighbours via softmax, masked to the node's neighbourhood
- [[vaswani-2017-transformer/main]] (p. 3): weighted sum of values, weights from query–key compatibility

### bayesian

- [[murphy-2023-pml2/ch16-deep]] (pp. 637–639): input-dependent weights: softmax of scaled query–key scores applied to values [alias `attention-layer`; new; work fields: bayesian, llm]

### theory-of-mind

- [[kosinski-2024-llm-tom/main]] (§ "Discussion"): Transformer component that weighs input words by relevance [as `attention mechanism`; alias `attention-mechanism`; new; work fields: theory-of-mind, llm]

## Instances that use it

- [[digg-collective-attention]] — log-normal diggs via a multiplicative process — from [[castellano-2009-socialdynamics/main-p3]]
- [[vervet-playback-care]] — Seyfarth’s attention to caller identity — from [[dennett-1987-intentional-stance/ch07-intentional]]
- [[catalinac-japan-manifestos]] — 7,497 manifestos analysed with LDA to study whether the 1994 electoral reform shifted candidate attention from pork to security — from [[grimmer-2022-textasdata/ch01-introduction]]
- [[bail-2016-cultural-bridging]] — network betweenness of advocacy organisations predicts attention from new users — from [[grimmer-2022-textasdata/ch14-low]]
- [[invisible-gorilla]] — focused attention causes blindness to the obvious, and blindness to the blindness — from [[kahneman-2011-thinking/ch01-characters]]
- [[french-vs-american-eating]] — same time eating, but attention (focal eating) differs, changing pleasure — from [[kahneman-2011-thinking/ch37-experienced]]
- [[rivoli-vs-metropolitan]] — Patterson's film vs museum attention; Lippmann qualifies it — from [[lippmann-1922-publicopinion/ch11-enlisting]]
- [[encoder-decoder-translation]] — English→French with cross-attention — from [[prince-2023-udl/ch12-transformers]]
- [[pound-shiller-1985-survey]] — Shiller says investors start to pay attention to a stock through word of mouth — from [[shiller-2019-narrative/app-applying]]
- [[bimetallism-bitcoin-attention]] — news-attention curves a century apart resemble epidemics — from [[shiller-2019-narrative/ch03-contagion]]
- [[making-more-difficult-attention]] — heads link "making" to "more difficult" — from [[vaswani-2017-transformer/main]]
- [[anaphora-heads-its-law]] — sharp attention from "its" — from [[vaswani-2017-transformer/main]]

## Candidate bridges

- [structural-analogy] Registration (a persisting object-location relation guiding action) ↔ number cognition: a limited-capacity, object-based attention or visual-working-memory system for small numerosities (pp. 35–36) — both are limited systems that support useful judgements without full flexibility. — from [[apperly-2009-two-systems/main-p2]] (theory-of-mind → other:cognitive-science)
- [structural-analogy] additive alignment score $v_a^\top\tanh(W_as+U_ah)$ ↔ LLM canon, attention: query–key similarity then a weighted average of values. Here keys and values are both $h_j$ and the score is an MLP, not a dot product. — from [[bahdanau-2015-attention/main]] (llm → llm)
- [metaphor] "Attention" as the decoder choosing where to look ↔ human selective attention. — from [[bahdanau-2015-attention/main]] (llm → unspecified)
- [structural-analogy] The news-detection quiz ↔ computational social science: survey-experiment design with an attention-check control arm (pp. 25–26) — from [[brown-2020-gpt3/main-p1]] (llm → other:computational-social-science)
- [structural-analogy] Frame in text × receiver schema ↔ cognitive psychology: top-down schema effects on attention and memory — from [[entman-1993-framing/main]] (communication-theory → other:psychology)
- [structural-analogy] $\mathrm{softmax}(xK^\top)V$ (Eq. 2) ↔ attention: weighted average of value vectors with query–key weights. Here keys and values are fixed parameters and no scaling is shown. — from [[geva-2021-ffn/main]] (llm → llm)
- [structural-analogy] Dot-perspective effect explained by attentional cueing ↔ attention research: arrows and gaze orient attention — from [[heyes-2014-cultural-evolution/main]] (theory-of-mind → other:attention-research)
- [structural-analogy] System 2 monitoring and overruling System 1 impulses ↔ decision-game-theory: bounded rationality, where limited attention constrains choice — both treat effort and attention as scarce. — from [[kahneman-2011-thinking/ch01-characters]] (decision-game-theory → decision-game-theory)
- [metaphor] Selective attention allocation under overload ↔ computing: priority scheduling versus a circuit breaker (pdf 36) — from [[kahneman-2011-thinking/ch02-attention]] (decision-game-theory → other:computer-science)
- [structural-analogy] availability cascade ↔ network science: positive-feedback information cascades — each round of attention raises the next. — from [[kahneman-2011-thinking/ch13-availability]] (decision-game-theory → complex-systems)
- [metaphor] Attention-dependent pleasure ↔ bounded rationality: limited attention shapes what we experience, as it shapes what we decide. — from [[kahneman-2011-thinking/ch37-experienced]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Chapter's blocking points ↔ communication-theory: attention and selectivity filters in media-effects models — outside messages pass several filters before affecting attitudes. — from [[katz-1955-personalinfluence/ch07-group]] (communication-theory → communication-theory)
- [metaphor] Daily attention as a scarce budget ↔ economics: attention as a limited resource allocated among uses — the text only counts minutes and shares. — from [[lippmann-1922-publicopinion/ch04-time]] (communication-theory → economics-finance)
- [structural-analogy] Attention to confirming facts ↔ selective exposure; Lippmann describes perception, not media choice. — from [[lippmann-1922-publicopinion/ch09-codes]] (communication-theory → unspecified)
- [metaphor] Press as searchlight ↔ attention and agenda setting: episodes lit one at a time (our link; not stated in this unit). — from [[lippmann-1922-publicopinion/ch24-news]] (communication-theory → communication-theory)
- [structural-analogy] Theorem 2.2 (ignore stimuli when attention is costly) ↔ political-science: [[rational-ignorance]] — both say ignorance can be rational when information costs exceed its expected value. — from [[lupia-1998-dilemma/app-ch02]] (political-science → political-science)
- [structural-analogy] Ignoring information whose cost exceeds its value ↔ rational ignorance: individually sensible non-attention (p. 7) — from [[lupia-1998-dilemma/ch01-knowledge]] (political-science → political-science)
- [structural-analogy] Calculus of attention ↔ decision theory: the benefit formula is an expected loss avoided, like a value-of-information calculation. — from [[lupia-1998-dilemma/ch02-people]] (political-science → decision-game-theory)
- [metaphor] Immune cytokines ↔ codelets calling attention to sites; fever and inflammation ↔ temperature (p. 69). — from [[mitchell-2009-guidedtour/ch13-make]] (complex-systems → unspecified)
- [structural-analogy] attention $\sum_i\alpha_i\boldsymbol v_i$ ↔ kernel/GP prediction: weighted average of training targets with similarity weights — the text itself draws this analogy (pp. 637–638) — from [[murphy-2023-pml2/ch16-deep]] (bayesian → linear-algebra)
- [metaphor] Looking longer at surprising events ↔ machine learning: prediction error — larger mismatch with expectation draws more attention. — from [[onishi-2005-infant-false-belief/main]] (theory-of-mind → llm)
- [structural-analogy] Fully connected net "has no notion of nearby" (p. 161) ↔ llm: attention without positional encoding is order-blind. — from [[prince-2023-udl/ch10-convolutional]] (llm → llm)
- [structural-analogy] self-attention as content-dependent routing ↔ convolution: both share parameters across positions, but attention weights depend on the inputs — from [[prince-2023-udl/ch12-transformers]] (llm → other:mathematics)
- [structural-analogy] cross-attention in translation ↔ word-alignment attention: output words attend to relevant source words — from [[prince-2023-udl/ch12-transformers]] (llm → other:word-alignment-attention)
- [structural-analogy] Graph attention ↔ transformer self-attention: both give softmax-weighted sums of transformed inputs. The graph version masks to the adjacency pattern. — from [[prince-2023-udl/ch13-graph]] (llm → llm)
- [structural-analogy] Masked autoregressive flow ↔ llm: causal masking in self-attention, which prunes dependence on later positions (p. 314) — from [[prince-2023-udl/ch16-normalizing]] (llm → llm)
- [structural-analogy] Social construction of technology ↔ communication theory: agenda setting — both describe attention and persuasion deciding what counts as a problem or need. — from [[rogers-2003-diffusion/ch04-generation]] (communication-theory → communication-theory)
- [structural-analogy] organizational agenda-setting ↔ media agenda setting — both concern how issues are prioritized for attention (pdf 515–517). — from [[rogers-2003-diffusion/ch10-innovation]] (communication-theory → unspecified)
- [structural-analogy] Capacity limit on received information ↔ rational inattention: an agent's attention treated as a channel with a bit-rate ceiling. — from [[shannon-1948-mathematical/main-p2]] (information-theory → information-theory)
- [metaphor] Word-frequency waves in Figure 14.1 ↔ epidemiology: infection curves — rise and fade of attention resembles case counts. — from [[shiller-2019-narrative/ch14-automation]] (economics-finance → other:epidemiology)
- [metaphor] Miller–Thaler exchange ↔ scientific debate as attention market — the fight drew readers to the paper. — from [[thaler-2015-misbehaving/ch25-battle]] (economics-finance → unspecified)
- [structural-analogy] Attention as soft key-value lookup ↔ databases: a query retrieves a weighted mix of stored values. — from [[vaswani-2017-transformer/main]] (llm → other:computer-science)
- [metaphor] Attention heads as specialists ↔ cognitive science: "different tasks" per head (p. 15), loosely like specialized modules. — from [[vaswani-2017-transformer/main]] (llm → other:cognitive-science)
- [structural-analogy] Attention-dependent exposure to elite messages ↔ principal–agent / delegation: the public's limited information about what elites do. — from [[zaller-1992-massopinion/ch01-introduction]] (political-science → political-science)
