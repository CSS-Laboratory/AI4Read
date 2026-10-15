---
id: heuristic
type: concept
fields: [decision-game-theory]
fields_strong: [decision-game-theory]
n_sources: 21
n_works: 3
tiers: [core]
grounding: digests
sources: [kahneman-2011-thinking/appa-judgment, kahneman-2011-thinking/ch00-introduction, kahneman-2011-thinking/ch01-characters, kahneman-2011-thinking/ch05-cognitive, kahneman-2011-thinking/ch07-machine, kahneman-2011-thinking/ch08-judgments, kahneman-2011-thinking/ch09-answering, kahneman-2011-thinking/ch12-science, kahneman-2011-thinking/ch13-availability, kahneman-2011-thinking/ch14-tom, kahneman-2011-thinking/ch15-linda, kahneman-2011-thinking/ch18-taming, kahneman-2011-thinking/ch19-illusion, kahneman-2011-thinking/ch22-expert, kahneman-2011-thinking/ch24-engine, kahneman-2011-thinking/ch30-rare, kahneman-2011-thinking/ch34-frames, kahneman-2011-thinking/ch38-thinking, kahneman-2011-thinking/conclusions, osborne-2004-introduction/ch06-extensive, tversky-1974-heuristics/main]
canon_spine: [decision-game-theory]
generated_by: build_kg.py
---

# heuristic

## Canon spine entry

- **heuristic** (decision-game-theory): a mental shortcut that trades accuracy for speed and effort (HS)

## Definitions in the sources

### decision-game-theory

- [[kahneman-2011-thinking/appa-judgment]] (pdf 410): a mental rule that simplifies probability judgment or value prediction; usually useful, sometimes severely wrong
- [[kahneman-2011-thinking/ch00-introduction]] (pdf 10): simplifying rule of thumb used for a hard judgment; here the cause of predictable bias
- [[kahneman-2011-thinking/ch01-characters]] (pdf 27): not defined in this unit; the chapter only says System 1 sometimes answers an easier question than the one asked [weak: not really used in this unit]
- [[kahneman-2011-thinking/ch05-cognitive]] (pdf 63–64; the author does not use the word "heuristic" in these pages): here, in effect: judging truth or familiarity from ease instead of checking
- [[kahneman-2011-thinking/ch07-machine]] (pdf 79): here, System 1's quick bet from context and experience, efficient but risky in unfamiliar, high-stakes settings
- [[kahneman-2011-thinking/ch08-judgments]] (pdf 90): here a "judgment heuristic": answering a hard question with a simpler, automatic assessment
- [[kahneman-2011-thinking/ch09-answering]] (pdf 97–98): a simple procedure giving adequate, often imperfect answers to hard questions. Pólya's heuristics are chosen by System 2; those here are not chosen
- [[kahneman-2011-thinking/ch12-science]] (pdf 129): a judgment shortcut that substitutes one question for another
- [[kahneman-2011-thinking/ch13-availability]] (pdf 137): mental shortcut; here, substitution of an easy question for a hard one
- [[kahneman-2011-thinking/ch14-tom]] (pdf 148): a mental shortcut; here the representativeness heuristic, one of the easier answers that a "mental shotgun" evokes
- [[kahneman-2011-thinking/ch15-linda]] (pdf 153): the Linda problem was meant as evidence of heuristics conflicting with logic
- [[kahneman-2011-thinking/ch18-taming]] (pdf 182): a shortcut that substitutes an easy question for a hard one; here, evaluation replaces prediction
- [[kahneman-2011-thinking/ch19-illusion]] (pdf 197–198): here, substitution: recalling one's current belief when asked about a former one
- [[kahneman-2011-thinking/ch22-expert]] (pdf 235–236): here: substitution of an easier question in low-validity settings, producing coherent but wrong answers
- [[kahneman-2011-thinking/ch24-engine]] (pdf 252–253): substitution of an easier question for a harder one, shown here
- [[kahneman-2011-thinking/ch30-rare]] (pdf 316): the availability heuristic as used here: probability judged by how many scenarios come to mind and how easily
- [[kahneman-2011-thinking/ch34-frames]] (pdf 360–361): System 1's quick rule, such as "favor the poor," which can contradict itself
- [[kahneman-2011-thinking/ch38-thinking]] (pdf 390): here, mood or a few available ideas stand in for a careful evaluation of life
- [[kahneman-2011-thinking/conclusions]] (pdf 407): here, an easier, more accessible answer substituted for the one asked, not necessarily simpler
- [[osborne-2004-introduction/ch06-extensive]] (p. 182): "rules of thumb" that work in repeated interactions, offered as another explanation
- [[tversky-1974-heuristics/main]] (p. 1124): a simple judgmental rule that cuts complex probability tasks to simpler operations; useful but leads to systematic errors

## Instances that use it

- [[mccoy-hans]] — BERT on MNLI relies on overlap heuristics and falls significantly below chance when they are frustrated — from [[bender-2020-octopus/main]]
- [[tsp-rollout]] — 5-city TSP: heuristic 48, one-step rollout 37, optimal 20 — from [[bertsekas-2026-rlcourse/ch01-exact-p6]]
- [[option-exercise-rollout]] — stock-selling DP; base heuristic 2.268, rollout 2.269; Monte Carlo accuracy matters — from [[bertsekas-2026-rlcourse/ch01-exact-p6]]
- [[multi-vehicle-routing-rollout]] — rollout improves a nearest-task heuristic from 10 to 6 moves — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]]
- [[sequential-improvement-violation-example]] — rollout strictly worse than a heuristic that is optimal from $x_0$ — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]]
- [[constrained-tsp]] — TSP with a safety constraint; rollout with a non-consistent heuristic — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]]
- [[tsp-rollout-exercise]] — traveling salesman with farthest/nearest neighbor heuristics — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
- [[ford-stock-executive]] — affect heuristic and substitution in an investment decision — from [[kahneman-2011-thinking/ch00-introduction]]
- [[table-1-target-heuristic-pairs]] — dolphins, mood, president, financial predators, political winner — from [[kahneman-2011-thinking/ch09-answering]]
- [[awgn-sphere-packing]] — heuristic packing of $\sqrt{n\sigma^2}$-balls in a $\sqrt{n(P+\sigma^2)}$-ball — from [[polyanskiy-2025-information/ch22-channels]]
- [[dhruv-name-example]] — availability heuristic fails when examples are not correlated with true frequency — from [[thaler-2015-misbehaving/ch03-list]]

## Candidate bridges

- [structural-analogy] Party label shaping issue positions ↔ heuristics/cues and motivated reasoning in political psychology — the same direction of influence (party first, opinion later); the authors attribute it to group loyalty (pp. 262–264, 266). — from [[achen-2016-realists/ch09-partisan]] (political-science → unspecified)
- [structural-analogy] Mindreading of agents ↔ intuitive physics: both may use heuristics and specialised processes, not explicit laws — Apperly's ball analogy (p. 3) — from [[apperly-2011-mindreaders/ch01-introduction]] (theory-of-mind → other:psychology-cognitive-science)
- [structural-analogy] Rollout with a consistent base heuristic ↔ control-theory: one policy-improvement (Newton) step on the base policy — the author states this link to Chapter 1's Newton interpretation (p. 184, p. 188). — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → control-theory)
- [metaphor] Fortified rollout's "keep the best trajectory so far" ↔ incumbent solution in search heuristics. — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → unspecified)
- [structural-analogy] Rollout improvement via the continuous-time inequality (2.63) ↔ control theory: Lyapunov-style decreasing functions — the heuristic's cost-to-go must not rise along the controlled path. — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (control-theory → control-theory)
- [metaphor] Strong frames work via cues and symbols ↔ heuristics/cues: shortcuts that substitute for substantive information. — from [[chong-2007-framing/main]] (political-science → political-science)
- [structural-analogy] Diffusion of "packages" from creative elites ↔ political science: party cues and heuristics — followers use supplied cues instead of reasoning from principles. — from [[converse-1964-beliefsystems/ch01-introduction]] (political-science → political-science)
- [structural-analogy] Opinion-leader transmission without understanding ↔ cue-taking and heuristics: followers copy behavior without reasons (pp. 35–36) — from [[converse-1964-beliefsystems/ch02-sections]] (political-science → decision-game-theory)
- [structural-analogy] Linking information and gross group cues (pp. 41–43) ↔ heuristics/cues: simple cues let uninformed people act as if informed. — from [[converse-1964-beliefsystems/ch03-sections]] (political-science → political-science)
- [structural-analogy] Joint-typicality counting ($2^{nH(Y)}/2^{nH(Y|X)}=2^{nI}$) ↔ sphere-packing counts in coding theory: both count disjoint decoding regions in output space (the author's own text only gives the heuristic). — from [[cover-2006-elements/ch08-channel-p1]] (information-theory → information-theory)
- [structural-analogy] Ideologies as cheap summaries ↔ cognitive science of heuristics (canon link; not stated in this unit). — from [[downs-1957-democracy/main]] (political-science → unspecified)
- [metaphor] Distributional hypothesis ↔ political-science: partisan cues and heuristics — judging an item by who is associated with it. — from [[grimmer-2022-textasdata/ch08-distributed]] (political-science → political-science)
- [metaphor] Heuristics as economical but biased ↔ bounded rationality: shortcuts used under limited effort. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → decision-game-theory)
- [structural-analogy] fluency as cue for truth ↔ judgment under uncertainty: availability heuristic (canon link; not stated in this unit) — both judge by how easily something comes to mind. — from [[kahneman-2011-thinking/ch05-cognitive]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Affect heuristic (feelings fix beliefs about risk/benefit) ↔ decision-game-theory: framing effect — an irrelevant factor changes judgments. — from [[kahneman-2011-thinking/ch09-answering]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Belief that small samples resemble the population ↔ heuristic / representativeness: judging by similarity rather than by computation. — from [[kahneman-2011-thinking/ch10-law]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Intuition validity requires a regular environment ↔ decision-game-theory: ecological rationality — a heuristic works to the degree it fits environment structure — from [[kahneman-2011-thinking/ch22-expert]] (decision-game-theory → decision-game-theory)
- [structural-analogy] peak-end rule ↔ heuristic / bounded rationality — a cheap summary of an episode saves memory and costs accuracy. — from [[kahneman-2011-thinking/ch35-two]] (decision-game-theory → unspecified)
- [structural-analogy] Substitution of an easy question ↔ heuristics in judgment: the same replacement of a hard evaluation by a simpler cue. — from [[kahneman-2011-thinking/ch38-thinking]] (decision-game-theory → decision-game-theory)
- [metaphor] Choosing advisers by perceived knowledge and trust ↔ heuristics/cues: low-information shortcuts that stand in for detailed knowledge. — from [[lupia-1998-dilemma/ch04-people]] (political-science → political-science)
- [metaphor] Reasoned choice via cues from a trusted speaker ↔ heuristics/cues in voting: uninformed people act as if informed by using an informative source. — from [[lupia-1998-dilemma/ch07-laboratory-p2]] (political-science → political-science)
- [structural-analogy] Perceived-trust moderation of endorsement ↔ heuristics / cues: party or source cues work only when the source is seen as credible. — from [[lupia-1998-dilemma/ch09-survey]] (political-science → political-science)
- [structural-analogy] Rejections of low offers explained by rules of thumb ↔ heuristic / bounded rationality: behaviour tuned to repeated environments is applied to one-shot games. — from [[osborne-2004-introduction/ch06-extensive]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Weighting losses above gains and recent events above distant ones (p. 208) ↔ political-science: framing effect and heuristics — judgments rely on how information is presented. — from [[ostrom-1990-commons/ch06-framework]] (political-science → political-science)
- [same-math] Lloyd's algorithm ↔ machine learning: $k$-means heuristic — the text states the objective is the same (p. 481). — from [[polyanskiy-2025-information/ch27-rate]] (information-theory → llm)
- [structural-analogy] Arrow's habit-based consumer ↔ bounded rationality / heuristics: choosing the closest affordable bundle replaces full re-optimization. — from [[thaler-2015-misbehaving/ch17-debate]] (economics-finance → decision-game-theory)
- [structural-analogy] default options ↔ bounded rationality / heuristics: people who do nothing are carried by the default. — from [[thaler-2015-misbehaving/ch32-going]] (economics-finance → decision-game-theory)
- [structural-analogy] Elite cues followed by partisans ↔ [[heuristics / cues]]: people respond to party-labelled signals. — from [[zaller-1992-massopinion/ch02-information]] (political-science → political-science)
- [metaphor] Source-credibility cues in low-involvement persuasion ↔ heuristics/cues (canon): shortcuts let people act as if informed. — from [[zaller-1992-massopinion/ch03-citizens]] (political-science → political-science)
