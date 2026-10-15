---
id: theory-of-mind
type: concept
fields: [theory-of-mind, economics-finance, llm]
n_sources: 7
tiers: [core, deep]
grounding: digests
sources: [apperly-2009-two-systems/main-p1, apperly-2011-mindreaders/ch01-introduction, mahowald-2024-dissociating/main, premack-1978-chimpanzee/main, shiller-2019-narrative/ch06-diverse, ullman-2023-trivial-alterations/main, wimmer-1983-beliefs-about-beliefs/main]
raw_ids: [theory of mind]
generated_by: build_kg.py
---

# theory-of-mind

## Definitions in the sources

### theory-of-mind

- [[apperly-2009-two-systems/main-p1]] (p. 3): ascribing beliefs, desires and intentions to explain, predict and justify behaviour
- [[apperly-2011-mindreaders/ch01-introduction]] (pp. 3–4): here a term Apperly avoids as tendentious, because it implies mindreading consists in having a theory; he uses "mindreading", which he describes as inferring unobservable mental states
- [[premack-1978-chimpanzee/main]] (p. 515): imputing unobservable mental states to self and others to predict behaviour
- [[ullman-2023-trivial-alterations/main]] (p. 1): adult-level ability to reason about others' mental states; used as shorthand
- [[wimmer-1983-beliefs-about-beliefs/main]] (p. 104): ability to impute mental states to self and others (Premack and Woodruff, as cited)

### economics-finance

- [[shiller-2019-narrative/ch06-diverse]] (p. 63): modelling others' mental states; may feed story-spreading choices [as `theory of mind`; new]

### llm

- [[mahowald-2024-dissociating/main]] (p. 13, 17): reasoning about others' knowledge, beliefs and wants; has its own brain network [new]

## Instances that use it

- [[twin-study-theory-of-mind]] — 0.53 correlation in both twin types — from [[heyes-2014-cultural-evolution/main]]

## Candidate bridges

- [structural-analogy] Self-perspective inhibition (p. 75) ↔ theory-of-mind canon, reality bias / curse of knowledge: one's own true knowledge pulling judgements about others' beliefs. — from [[apperly-2011-mindreaders/ch04-evidence]] (theory-of-mind → theory-of-mind)
- [metaphor] Similarity-to-self narrowing the plausible thoughts of others under uncertainty (p. 70) ↔ Bayesian theory of mind: priors that constrain inference over mental states. — from [[apperly-2011-mindreaders/ch04-evidence]] (theory-of-mind → bayesian)
- [structural-analogy] Answering from reality instead of from the doll's belief ↔ theory-of-mind canon: reality bias / curse of knowledge (the paper itself does not use these terms) — from [[baron-cohen-1985-autism/main]] (theory-of-mind → theory-of-mind)
- [metaphor] Control questions that must be passed before interpreting the key question ↔ machine theory of mind evaluation: sanity checks before interpreting a model's failure on a false-belief item — from [[baron-cohen-1985-autism/main]] (theory-of-mind → theory-of-mind)
- [structural-analogy] intentional stance, attribute what the system *ought* to want and believe, revised downward ↔ theory-of-mind: rational-agent assumption / inverse planning with noisy (Boltzmann) rationality — both infer mental states from behaviour via a model of an approximately rational agent. — from [[dennett-1987-intentional-stance/ch02-true]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Dennett's intentional-stance prediction (utility-rational agent from beliefs/desires) ↔ theory-of-mind: inverse planning and the rational-agent assumption — both infer or predict from an assumption of rational action, though Dennett gives no Bayesian machinery here. — from [[dennett-1987-intentional-stance/ch03-three]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Dennett's "best, most rational story" ↔ theory-of-mind modelling: inverse planning assumes the agent acts rationally and infers beliefs from actions — both infer mental states by assuming rationality; Dennett denies a fixed formal definition. — from [[dennett-1987-intentional-stance/ch04-making]] (theory-of-mind → theory-of-mind)
- [metaphor] "Bathed in words" versus "bathed in information" ↔ machine theory of mind and construct validity: fluent verbal output may suggest more finely individuated beliefs than the underlying system has. — from [[dennett-1987-intentional-stance/ch04-making]] (theory-of-mind → theory-of-mind)
- [structural-analogy] notional attitude + environment → propositional attitude ↔ theory-of-mind: belief ascription as a function of an agent's internal state plus what the observer knows of the setting — both factor a belief into agent-side and world-side contributions. — from [[dennett-1987-intentional-stance/ch05-beyond-p1]] (theory-of-mind → theory-of-mind)
- [metaphor] SHRDLU's notional blocks world ↔ machine theory of mind: evaluating a system in a simulated environment; the analogy is loose. — from [[dennett-1987-intentional-stance/ch05-beyond-p1]] (theory-of-mind → theory-of-mind)
- [structural-analogy] notional world as the world an agent takes itself to be in ↔ theory-of-mind/POMDP: an agent's belief state about the world — both describe an agent by what it takes the world to be like. — from [[dennett-1987-intentional-stance/ch05-beyond-p2]] (theory-of-mind → theory-of-mind)
- [structural-analogy] tacit, state-defined content ↔ machine theory of mind: distributed weights encode behaviour without addressable "propositions" — both locate content in global functional role, not in stored sentences. — from [[dennett-1987-intentional-stance/ch06-styles]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Dennett’s rationality assumption for predicting action ↔ theory-of-mind modelling: inferring beliefs and desires by assuming rational action — both infer attitudes from behaviour plus rationality. — from [[dennett-1987-intentional-stance/ch07-intentional]] (theory-of-mind → theory-of-mind)
- [metaphor] Intentional profile as spec for a designer ↔ machine theory of mind: a behavioural-level description constraining implementation. — from [[dennett-1987-intentional-stance/ch07-intentional]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Dennett's "same function, different speed, different causal control" ↔ theory-of-mind modelling: exact inverse-planning inference may be too slow for real-time use, so only a fast approximation can act — the same trade of speed against fidelity. — from [[dennett-1987-intentional-stance/ch09-fast]] (theory-of-mind → theory-of-mind)
- [structural-analogy] "Opportunistic oversimplification" (vision oracle of 8 bits) ↔ simplified agent models in Bayesian theory of mind: simplify and hope the molar behaviour survives. — from [[dennett-1987-intentional-stance/ch09-fast]] (theory-of-mind → bayesian)
- [structural-analogy] Projective Principle (attribute what I would have) ↔ theory of mind: simulation theory — both use oneself as a model for others. — from [[dennett-1987-intentional-stance/ch10-mid]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Normative Principle / Assumption of Rationality ↔ theory of mind: rational-agent assumption — both predict from what a rational agent would do. — from [[dennett-1987-intentional-stance/ch10-mid]] (theory-of-mind → theory-of-mind)
- [metaphor] Quine's "dramatic idiom" ↔ theory of mind: folk-psychological explanation as useful interpretation, not a description of inner facts. — from [[dennett-1987-intentional-stance/ch10-mid]] (theory-of-mind → theory-of-mind)
- [same-math] Speaker softmax $e^{\alpha U}$ with $\alpha=1$ ↔ theory of mind (canon): Boltzmann rationality — the same exponentiated-utility choice rule. — from [[frank-2012-rsa/main]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Listener inferring the referent via Bayes ↔ theory of mind: inverse planning — both invert a rational-agent model to recover what the agent intended. — from [[frank-2012-rsa/main]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Speaker informativeness via a literal listener ↔ theory of mind: recursive mindreading — the speaker reasons about how a listener would interpret a word. — from [[frank-2012-rsa/main]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Formal/functional split ↔ cognitive neuroscience: language network vs multiple-demand, default and theory-of-mind networks — the paper uses brain dissociations as a template for model evaluation. — from [[mahowald-2024-dissociating/main]] (llm → other)
- [structural-analogy] Sarah's choices answer "what would the actor do?" ↔ theory of mind: predicting action from imputed goals and knowledge — the paper uses goal imputation as its core inference. — from [[premack-1978-chimpanzee/main]] (theory-of-mind → theory-of-mind)
