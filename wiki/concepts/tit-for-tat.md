---
id: tit-for-tat
type: concept
fields: [decision-game-theory, political-science, complex-systems]
n_sources: 15
tiers: [core]
grounding: digests
sources: [axelrod-1984-cooperation/appa-tournament, axelrod-1984-cooperation/appb-proofs, axelrod-1984-cooperation/ch01-problemof, axelrod-1984-cooperation/ch02-success, axelrod-1984-cooperation/ch05-evolution, axelrod-1984-cooperation/ch06-choose, axelrod-1984-cooperation/ch07-promote, axelrod-1984-cooperation/ch09-robustness, clark-2017-principles/ch04-origins-p2, dixit-2008-art-strategy/ch03-prisoners, mitchell-2009-guidedtour/ch14-prospects, nowak-2006-five-rules/main, osborne-2004-introduction/ch14-repeated, osborne-2004-introduction/ch15-repeated, shepsle-2010-analyzing/ch08-cooperation]
generated_by: build_kg.py
---

# tit-for-tat

## Definitions in the sources

### decision-game-theory

- [[axelrod-1984-cooperation/appa-tournament]] (p. 192, p. 205): the rule that won both rounds; its robustness is the appendix's topic [new]
- [[axelrod-1984-cooperation/appb-proofs]] (p. 207): cooperate first, then copy the other's previous move [new]
- [[axelrod-1984-cooperation/ch01-problemof]] (p. 13): cooperate on move 1, then copy the other's previous move [new]
- [[axelrod-1984-cooperation/ch02-success]] (p. 31): cooperate on move 1, then copy the other player's previous move [new]
- [[axelrod-1984-cooperation/ch05-evolution]] (p. 96): the reciprocity strategy of chapter 2 (its definition is not given in these pages); robust, and stable if $w$ is large enough [new]
- [[axelrod-1984-cooperation/ch06-choose]] (p. 118): cooperate first, then copy the other's last move [new]
- [[axelrod-1984-cooperation/ch07-promote]] (pp. 127, 137): cooperate first, then copy the other's last move; here also judged as a moral strategy [new]
- [[axelrod-1984-cooperation/ch09-robustness]] (pp. 175–176): cooperate first, then copy the other's last move; nice, provocable, forgiving, clear [new]
- [[dixit-2008-art-strategy/ch03-prisoners]] (pp. 82–83): cooperate first, then copy the rival's last move; clear, nice, provocable, forgiving, but errors echo [new]
- [[nowak-2006-five-rules/main]] (§ "Direct reciprocity"): repeated-game strategies [new]
- [[osborne-2004-introduction/ch14-repeated]] (p. 395): copy the other player's action from the previous period [new]
- [[osborne-2004-introduction/ch15-repeated]] (p. 418, 419): reciprocating and win–stay, lose–shift strategies [new]

### political-science

- [[clark-2017-principles/ch04-origins-p2]] (p. 141): start cooperating, then copy the other's last move [new]
- [[shepsle-2010-analyzing/ch08-cooperation]] (p. 244): cooperate first, then copy the other's last move [new]

### complex-systems

- [[mitchell-2009-guidedtour/ch14-prospects]] (p. 80): cooperate first, then copy opponent's last move [new]

## Instances that use it

- [[axelrod-tournament-round-one]] — 14 entries plus RANDOM, 200-move games; TIT FOR TAT first — from [[axelrod-1984-cooperation/appa-tournament]]
- [[all-d-vs-tit-for-tat]] — score $T+wP+w^2P+\dots$ — from [[axelrod-1984-cooperation/ch01-problemof]]
- [[tft-wins-tournament-1]] — TIT FOR TAT wins round one among 14 entries, averaging 504 — from [[axelrod-1984-cooperation/ch02-success]]
- [[joss-tft-echo]] — JOSS vs TIT FOR TAT, Table 1: a single defection leads to mutual defection, 236 vs 241 — from [[axelrod-1984-cooperation/ch02-success]]
- [[tit-for-tat]] — cooperate first, then copy; stable for large w — from [[axelrod-1984-cooperation/ch03-chronology]]
- [[computer-tournament]] — source of evidence: niceness and TIT FOR TAT results — from [[axelrod-1984-cooperation/ch06-choose]]
- [[iterated-pd-tournaments]] — TIT FOR TAT won but never outscored a partner — from [[axelrod-1984-cooperation/ch07-promote]]
- [[blue-green-stereotypes]] — two groups, TIT FOR TAT inside and always defect across; stable and self-confirming — from [[axelrod-1984-cooperation/ch08-social]]
- [[territorial-meanie-invasion]] — always-defect colonising TIT FOR TAT, with $w=1/3$ and $T=56, R=29, P=6, S=0$ — from [[axelrod-1984-cooperation/ch08-social]]
- [[axelrod-tournament]] — tit for tat wins a 150-round dilemma tournament — from [[dixit-2008-art-strategy/ch03-prisoners]]
- [[axelrod-tournaments]] — simple TIT FOR TAT beat complicated strategies — from [[mitchell-2009-guidedtour/ch14-prospects]]
- [[axelrod-tournaments]] — tit-for-tat won two computer tournaments — from [[nowak-2006-five-rules/main]]
- [[repeated-prisoners-dilemma]] — payoffs (2, 2), (0, 3), (3, 0), (1, 1); cooperation sustained by grim trigger, limited punishment or tit-for-tat when δ is large enough — from [[osborne-2004-introduction/ch14-repeated]]
- [[axelrod-tournaments]] — tit-for-tat won two tournaments and had the most representatives in an evolutionary simulation — from [[osborne-2004-introduction/ch15-repeated]]

## Candidate bridges

- [structural-analogy] Clarity of TIT FOR TAT ↔ credible commitment: a rule that others can easily recognise changes their incentives. — from [[axelrod-1984-cooperation/ch02-success]] (decision-game-theory → other)
- [structural-analogy] Clustering of TIT FOR TAT ↔ network reciprocity: local interaction helps cooperators. — from [[axelrod-1984-cooperation/ch05-evolution]] (decision-game-theory → other)
- [metaphor] Clarity of TIT FOR TAT ↔ signaling: making your intentions legible so others can respond. — from [[axelrod-1984-cooperation/ch06-choose]] (decision-game-theory → decision-game-theory)
- [structural-analogy] tit-for-tat and grim trigger ↔ reciprocity (direct, indirect, network): cooperation held in place by the other's conditional response. — from [[osborne-2004-introduction/ch14-repeated]] (decision-game-theory → other)
- [structural-analogy] Tit-for-tat echoing a bad start ↔ feuds and ethnic hostilities (p. 245) — from [[shepsle-2010-analyzing/ch08-cooperation]] (political-science → unspecified)
- [structural-analogy] Small groups' tit-for-tat enforcement ↔ repeated-game cooperation: repeat play sustains contribution. — from [[shepsle-2010-analyzing/ch09-collective-p2]] (political-science → other)
