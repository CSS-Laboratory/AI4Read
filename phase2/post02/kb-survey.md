---
name: post02-kb-survey
description: Knowledge-base survey for post 02 ("Can LLMs create a new kind of finance?"). Lists the relevant digests by lens with their audit status, the wiki nodes and bridges, the gaps, and the hooks back to post 01. Input for the planner (S0/S1).
date: 2026-10-17
---

# KB survey for post 02

Audit status: `audited` means the unit has `audited:` frontmatter. Every other digest is `verified: repaired` only, so it must be checked against its pages in S2.

## Lenses and the works already digested

**Economics & finance (home field)**
- `wiki/works/hayek-1945-knowledge/main.md`: prices compress dispersed knowledge.
- `wiki/works/grossman-1980-impossibility/main.md`: a price is a noisy signal; fully efficient markets are impossible.
- `wiki/works/akerlof-1970-lemons/` (`main.md`, page-checked): hidden quality unravels a market.
- `wiki/works/stiglitz-2002-paradigm/main-p1..p3.md`: the information paradigm and principal–agent.
- `wiki/works/keynes-1936-general/ch12-state.md` (**audited**): convention, beauty contest, animal spirits. Also ch13 and ch17 (liquidity, the nature of money).
- `wiki/works/morris-2002-public/main.md`: people over-weight public signals. This applies when many agents read the same model's output.
- `wiki/works/shiller-2019-narrative/`:
  - ch14-automation cites Harari's "useless class", p. 208.
  - ch01 (bitcoin), ch07, ch10, ch12, ch16 and ch19 are also relevant.
- `wiki/works/minsky-1992-instability/main.md`: stability breeds instability.
- `wiki/works/kelly-1956-information/main.md` (**audited**): growth rate equals information rate.
- `wiki/works/thaler-2015-misbehaving/`: ch21, ch24 (the 1987 crash), ch10 (fungibility).
- `wiki/works/arthur-1994-elfarol/main.md`, `fama-1970-efficient`, `markowitz-1952-portfolio`.

**Information theory:** `shannon-1948-mathematical/main-p1`, `shannon-1951-prediction`, `cover-2006-elements/ch02`, `mackay-2003-information/ch04` (all **audited**).

**Decision & game theory**
- `myerson-2008-mechanism/main.md`
- `dixit-2008-art-strategy/ch13-incentives.md`, ch10-auctions
- `schelling-1960-conflict/ch04` (focal points)
- `axelrod-1984-cooperation/ch02` (audited)
- `kahneman-2011-thinking/ch26` (audited)
- Goodhart appears only through `prince-2023-udl/ch21-deep.md` (alignment as principal–agent; Ex. 21.2 asks for Goodhart's law restated for loss functions) and `bai-2022-constitutional/main.md`.

**Complex systems:** `granovetter-1978-threshold`, `bak-1987-soc`, `scheffer-2009-earlywarning`, `mitchell-2009-guidedtour/ch16-applying` (cascading failure, pp. 125–128), `anderson-1972-moreisdifferent` (audited), `simon-1962-architecture`.

**Control & cybernetics**
- `ashby-1956-cybernetics/ch10-regulation`, `ch11-requisite` (**audited**). Also ch06 (black box), ch13 (regulating) and ch14 (amplifying regulation).
- `meadows-2008-thinking/` ch05 (rule beating, seeking the wrong goal, pp. 136–137) and ch06 (leverage points).
- `taylor-1993-discretion`.
- Wiener is in the canon but not digested.

**Philosophy and theory of mind:** `dennett-1987-intentional-stance/ch02` (audited); `pearl-2018-bookofwhy/ch01` (reports Harari's claim that shared fictions enable large-scale trust). Searle is **not** in the canon.

**Political science and institutions**
- `lupia-1998-dilemma/` ch05 (delegation) and ch10 (institutions): how a principal with little information knows whom to trust.
- `shepsle-2010-analyzing/` ch11 and ch13 (the bureaucrat's information advantage).
- `clark-2017-principles/ch12` (audited, delegation chain); `ostrom-1990-commons/ch02`; `olson-1965-collectiveaction`.

**Communication:** `carey-1989-cultural/ch06-space` (Innis, "monopoly of knowledge"); `lippmann-1922-publicopinion/ch26`; `habermas-1989-publicsphere/ch05` (audited).

**LLMs:** `argyle-2023-silicon` (audited), `xie-2022-icl` (audited), `park-2023-agents`, `ouyang-2022-instructgpt`, `kaplan-2020-scaling`, `ng-2000-irl`.

## Wiki nodes
- Concepts:
  - price-as-signal, dispersed-tacit-knowledge, asymmetric-information, adverse-selection, moral-hazard, noise-traders, efficient-market-hypothesis, limits-to-arbitrage
  - beauty-contest-higher-order-beliefs, common-knowledge-vs-public-information, knightian-uncertainty, conventional-expectations, lucas-critique
  - economic-narrative, narrative-contagion-sir, financial-instability-hypothesis-hedge-speculative-ponzi, bank-run-equilibrium, maturity-liquidity-transformation
  - principal-agent-problem (8 works), mechanism-design, institutions, convention
  - cascade, threshold-model, tipping-point, early-warning-signals
  - law-of-requisite-variety, black-box, feedback-loop, positive-feedback
  - intentional-stance, speech-act, performative-utterance, monopoly-of-knowledge, fungibility-of-money, quantity-theory-of-money, liquidity-preference
- Empty stubs: good-regulator-theorem, rational-inattention.
- Instances: market-for-lemons-used-cars, keynes-newspaper-beauty-contest, el-farol-bar-problem, kelly-gambler-noisy-channel, granovetter-riot-thresholds, watt-governor.
- Bridges to reuse:
  - Akerlof: pooling ↔ a lossy channel (structural analogy).
  - Hayek: prices ↔ compression (metaphor).
  - Kelly ↔ channel rate (same-math).
  - Minsky ↔ positive feedback.
  - Prince ch21: loss as a proxy ↔ Goodhart (structural analogy).
  - Åström: feedback vs feedforward ↔ market vs planned economy.

## Gaps (not in the canon or library; citations unchecked)
- **Social reality and money:** Searle 1995/2010; Harari *Sapiens* 2014 and *Nexus* 2024; Simmel 1900; Ingham 2004; North 1990; Polanyi 1944.
- **Opaque instruments:** Arora, Barak, Brunnermeier & Ge 2011 (computational complexity and information asymmetry in financial products). This is the closest formal result to Harari's claim.
- **Algorithmic finance and performativity:** MacKenzie 2006 and 2021; Kirilenko et al. 2017 (the Flash Crash).
- **Systemic risk:** Haldane & May 2011; Acemoglu, Ozdaglar & Tahbaz-Salehi 2015; Battiston et al. 2016; Perrow 1984.
- **AI and finance:**
  - Calvano et al. 2020 (algorithmic collusion)
  - Danielsson, Macrae & Uthemann 2022
  - Gensler & Bailey 2020 (monoculture, herding)
  - IMF GFSR 2024 ch. 3; FSB 2024 on AI
  - Scheurer et al. 2023 (an LLM trading agent deceives)
  - Lopez-Lira & Tang 2023
- **Goodhart's law:** Goodhart 1975; Strathern 1997.
- **Alignment as contracting:** Hadfield-Menell & Hadfield 2019.
- **In the canon but not fetched:** Diamond & Dybvig 1983 (a free URL is in `canon/free-manifest.json`), Wiener 1948, Conant & Ashby 1970, Lucas 1976, Kuran 1991, Sims 2003.

## Hooks back to post 01
- Prediction = compression ↔ Hayek's price as compression. Grossman–Stiglitz gives the formal version.
- In-context learning as Bayesian selection (Xie): toy W4 can be reused for price-as-signal.
- Toy W1 (the weather village) is earmarked for decision under uncertainty. It leads to Kelly betting (audited), where growth rate = information rate.
- Ullman's "trivial alterations" ↔ the Lucas critique: behaviour fitted in one regime fails in another. This link is ours.
- LLM theory of mind ↔ the Keynes beauty contest (higher-order beliefs).
- Learner state: an open confusion about Shannon's twin (who encodes, who decodes). The Kelly gambler with a private wire gives it a second pass.
