---
id: ashby-1956-cybernetics/ch10-regulation
work: ashby-1956-cybernetics
unit: "10 Regulation in Biological Systems"
pages: 194-201
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 8
---
# Regulation in Biological Systems

## L0 — One line
Survival can be stated as keeping the states of an organism (often, its essential variables) within a chosen set, and an essential feature of a good regulator is that it blocks the flow of variety from disturbances to the essential variables.

## L1 — The gist (≤ 120 words)
Ashby reviews the place of regulation in biology and shows briefly why it matters. He shows that "survival" can be stated exactly, and for a mouse that always survives it is identical to the stability of a set of states. Natural selection favours gene-patterns that place a regulator F between disturbances D and essential variables E. The permitted set of E has less variety than E as a whole, and an essential function of a regulator is to block the transmission of variety (and so of information) from D to E. Regulation can be passive (a shell) or active (a fencer's skilled counter-action). The chapter motivates the quantitative treatment of regulation in the later chapters of Part III.

**Prerequisites:** sets and subsets; "variety" as the number of distinguishable states (Part II); the idea that a set of states can be "stable" (stay closed under an operation).

## L2 — Key ideas (5–10 bullets)
- Chapter 10 aims to tie regulation, information and survival together in one rigorous method, uniform with the rest of the book (p. 196).
- The living world consists of "autocatalytic" processes, and "lifeless" is almost an equilibrium state (a state the system stays in), but an unstable one (small pushes grow). Today's organisms bear the marks of long elimination of forms that could not survive (p. 196).
- "Survival" is defined as the states of an organism staying inside a chosen subset. For a mouse that always survives, this is identical to the stability of a set, so facts about one can be used for the other, provided exactness is kept (p. 197).
- What survives over the ages is gene-patterns, especially those that cause a defence mechanism to grow between themselves and the world, giving the scheme D → F → E (p. 198).
- The essential variables E have a permitted set η, which has less variety than all of E's possible states. If F is a regulator, inserting it lessens the variety passing from D to E, and an essential function of F is to block it (p. 199).
- Test: the good regulator's record carries no information about the disturbances (two water-baths, pilot, air-conditioner, hunter) (pp. 200–201).
- Blocking can be passive (tortoise shell) or active (fencer's skilled counter-action). In the fencer's case, information flows freely to non-essential variables, but the variety of the distinction "duel or no-duel" is prevented from reaching the essential ones (p. 201).

## L3 — Walkthrough

### 10/1–10/2. Place of the chapter
- Parts I and II (Mechanism, Variety) were prerequisites. Part III treats regulation and control, "the central theme of cybernetics" (p. 195).
- Chapter 11 will show a quantitative law: the amount of regulation achievable is bounded by the amount of information transmitted in a certain channel. Chapter 12 introduces the Markovian machine (a machine whose next state follows fixed probabilities, not certainty). Later chapters treat harder, larger systems (p. 195).
- At first the regulator is assumed to be already provided. How it came to be made is deferred to S.13/10 (p. 195).
- The chapter mainly supplies motive. Cannon's *Wisdom of the Body* covers internal, vegetative (automatic bodily, like digestion or temperature) regulation. Ashby says a larger book is still needed to show that the "higher" outward-directed activities are also homeostatic (pp. 195–196).
- The chief purpose is to tie together regulation, information and survival (p. 196).

### 10/3. The foundation
- The earth is about two thousand million years old, and biologists study what exists today (p. 196).
- Recalled from S.4/23: a large system made of repetitive parts, with an autocatalytic property (one occurrence raises the chance of another), is essentially unstable in that property's absence (p. 196).
- Carbon, nitrogen and a few other elements form self-reproducing combinations. So "lifeless" is almost an equilibrium, but an unstable one (S.5/6): one deviation starts a trajectory (the path of successive states) leading further away (p. 196).
- Today's forms show the effect of long elimination of forms defective in survival. Eyes, roots, cilia, shells and claws are so fashioned as to maximise the chance of survival, and the brain is likewise a means to survival (p. 196).
- *Intuition note:* What exists now has passed a very long filter, and the features of almost every form bear the marks of being adapted to survival.

### 10/4. Survival as stability
- A mouse is escaping a cat. The mouse can be in many states (posture, temperature, one ear or two) and still be "alive". States such as "in four pieces" do not count as survival (p. 197).
- Formalisation: the mouse's states are $M_1, M_2, \dots, M_k, \dots, M_n$. "Living mouse" is restricted, by practical choice, to a subset $M_1,\dots,M_k$ (p. 197).
- If the operation C (cat) turns $M_i$ into, say, $M_2$ inside that subset, then M has survived C (p. 197).
- If a skilled mouse always survives, then all of $C(M_1),\dots,C(M_k)$ lie in $\{M_1,\dots,M_k\}$. This is the same representation as the stability of a set (S.5/5), so facts about either can be used for the other, provided exactness is kept (p. 197).
- When states are defined by variables, the living states are those in which certain essential variables stay within assigned ("physiological") limits (p. 197).
- *Intuition note:* "Alive" means "inside a chosen safe set". The organism is stable if the world's blows never push it out of that set.
- Ex. 1–3 (p. 197) are listed under Exercises.

### 10/5. The regulator between disturbance and essential variables
- What survives is not the individual but gene-patterns, especially those that lead to an individual that carries the gene-pattern well protected within itself and can look after itself for one generation (p. 198).
- Such patterns are likely to survive if they grow a defence mechanism between themselves and the dangerous world. Examples: *Testudo* (shell), *Homo* (brain) (p. 198).
- The cat–mouse diagram $C \to M$ is replaced by $D \to F \to E$ (p. 198):
  - E: set of essential variables;
  - D: source of disturbances and dangers (such as C);
  - F: the interposed part (shell, brain, etc.). It may include parts of the environment, e.g. a burrow for a rabbit (p. 198).
- E's states are divided into η (the "living" or "good" ones) and not-η (the "bad" ones). A finer classification is allowed in principle (p. 198).
- Examples (pp. 198–199):
  1. Thermostatic water-bath: E is the temperature, η is 36–37 °C, D is cold water, draughts and cold objects, F is the whole regulatory machinery. F tends to lessen D's effect on E.
  2. Automatic pilot: E is the vector (yaw, pitch, roll) (the plane's turning about its vertical, sideways and lengthwise axes), η is the set of positions with all three within limits, D includes gusts, passengers' movements and engine irregularities.
  3. Bicycle rider: E is chiefly the angle with the vertical, η is the set of small permissible deviations.
- Summary: natural selection favours gene-patterns that get, in whatever way, a regulator F between D and E. Other things equal, the better F is, the larger the chance of survival (p. 199).
- *Intuition note:* F is whatever is interposed between the world's disturbances D and the essential variables E (shell, brain, even parts of the environment).

### 10/6. Regulation blocks the flow of variety
- A good regulator needs two properties: it keeps the variable within close limits, and that range corresponds to the desired one (p. 199).
- Key point: η has less variety than the set of all possible values of E, because η is a selected part of E. If F is a regulator, inserting it between D and E lessens the variety transmitted from D to E. Thus an essential function of F is to block that transmission (p. 199).
- Test case, Fig. 10/6/1 (p. 200): two water-baths are tested for a day. Bath A's temperature record wanders; B's is almost flat. B is clearly better. This is because B's record gives no information about the disturbances, while A's does (p. 200).
- Same argument, with obvious modifications (pp. 200–201):
  - Automatic pilot: if it is a good regulator, the passengers have a smooth flight whatever the gustiness and are prevented from knowing whether it is gusty outside.
  - Air-conditioner: if I can tell from the room's heat that it is hot outside, it is failing. A good one, with blinds drawn, lets me form no idea of the weather.
  - Hunter or earner: the skilled one goes through hard times with liver and tissues (the essential variables) never taken to extremes. The family of a skilled provider may not realise that anything unusual has happened; that of an unskilled provider would.
- Conclusion: an essential feature of the good regulator is that it blocks the flow of variety from disturbances to essential variables (p. 201).
- *Intuition note:* The better the regulator, the less of the disturbance shows in the variable it protects. So the good bath's record, the passengers' smooth flight and the room's temperature tell little or nothing about the disturbances.

### 10/7. Two extreme forms of blocking
- The forms prove, on closer examination, to be fundamentally the same (p. 201).
- Passive block: something interposed that simply stops disturbances. Examples: tortoise shell, tree bark, seal's blubber, human skull (p. 201).
- Active defence by skilled counter-action: get information about the coming disturbance, prepare, and meet it with a defence as complex and mobile as it is. Example: the unarmoured fencer. This is the defence used mostly by the higher organisms, who developed a nervous system for it (p. 201).
- In the fencer's case information is essential: he must watch the opponent. Yet if he succeeds, his essential variables (e.g. blood-volume) stay in normal limits, much as if no duel had occurred. Information flows freely to non-essential variables, but the variety of the distinction "duel or no-duel" is prevented from reaching the essential ones (p. 201).
- The remaining chapters study this active defence: which principles govern it, which mechanisms achieve it, and what to do when regulation is very difficult (p. 201).
- *Intuition note:* The regulator may use a lot of information internally. The test of success is what gets through to E.

## Toy example (our own, not from the text)
**Survival as stability.** Let $n=4$ states, with living set $S=\{M_1,M_2\}$ ($k=2$).
- Cat A: $C(M_1)=M_2$, $C(M_2)=M_1$. Both images lie in $S$, so $S$ is stable under C: the mouse always survives.
- Cat B: $C(M_1)=M_2$, $C(M_2)=M_3$. $M_3\notin S$, so $S$ is not stable: survival fails from $M_2$.

**Blocking variety.** Four disturbances (D: none, small cold, medium cold, big cold), with η = 36.0–37.0 °C.
- Bath A readings: 36.9, 36.3, 36.1, 35.4. Four different values, so the record shows which disturbance occurred. The last one is outside η.
- Bath B readings: 36.5, 36.5, 36.5, 36.4. Only two distinct values (and these carry little information). All four are inside η.
- B transmits less variety from D to E and keeps E inside η, so B is the better regulator.

## Concepts
- [[homeostasis]] — maintenance of essential variables within limits (canon link; Ashby uses "homeostatic" without defining it here); Ashby says "higher" activities are also homeostatic (p. 196).
- [[variety]] — (developed in Part II; not defined on these pages) here, η has less variety than the set of all possible values of E (p. 199).
- [[disturbance and noise]] — D, the source of disturbances and dangers from the outside world (p. 198).
- [[stability]] — a set is stable if the operation never maps its states outside it. For a mouse that always survives C, the representation of survival is identical to the stability of the set (p. 197).
- [[regulator-between-D-and-E]] (new) — F inserted between D and E, an essential function of which is to block variety from D to E (pp. 198–199).
- [[essential variables]] (new) — variables that must stay within physiological limits for life. Their acceptable states form η (pp. 197–198).
- [[passive vs active regulation]] (new) — static barrier (shell) versus skilled counter-action using information (p. 201).
- [[autocatalytic property]] (new) — one occurrence raises the probability of another elsewhere (p. 196).

## Canonical instances
- [[mouse-and-cat]] — survival as a set of living states stable under C (p. 197).
- [[thermostatic-water-bath]] — E = temperature, η = 36–37 °C (p. 198).
- [[automatic-pilot]] — E = (yaw, pitch, roll) (p. 199).
- [[bicycle-rider]] — E = angle with the vertical (p. 199).
- [[two-water-baths-A-B]] — Fig. 10/6/1: the better regulator's record shows no trace of D (p. 200).
- [[tortoise-shell]] — passive block (p. 201).
- [[fencer]] — active defence: free information flow, protected essential variables (p. 201).

## Bridges (candidates)
- [structural-analogy] regulator blocks variety from D to E ↔ control-theory: disturbance rejection (the output barely reflects the disturbance) — both describe a good controller leaving the output unaffected.
- [structural-analogy] survival as stability of a set ↔ control-theory: viability or invariance of a set — both ask that trajectories never leave a set.
- [metaphor] passive shell versus skilled fencer ↔ control-theory: fixed design versus information-using control (open-loop vs closed-loop).

## Questions this raises
- If good regulation hides D from E, how exactly does the regulator get information about D? Is there a limit?
- How is the "variety" of D and F measured so that the bound announced for chapter 11 can be stated?
- What makes F come into existence in the first place (deferred to S.13/10)?
- When is the passive/active distinction really "fundamentally the same" (p. 201)?

## Exercises worth doing
- Ex. 1 (p. 197) — with n = 10, k = 5, what C(M7) = M9 means for survival — easy
- Ex. 2 (p. 197) — what C(M8) = M4 means — easy
- Ex. 3 (p. 197) — define "lethal" if C's attack is invariably fatal — medium
- Unnumbered Ex. (p. 199) — name the variables kept within limits by ten regulatory devices (air-conditioner … anti-aircraft predictor) — medium

## Reading notes
- Page labels pair the pages as spreads: printed 194–195, 196–197, 198–199, 200–201. Page numbers are printed.
- In 10/5 (p. 198), a "∇" glyph follows "η" and "not-η" in both the text layer and the image. It has no evident meaning there and looks like a stray printing or scanning artefact. The sentence is read here as "a set η — those that correspond to 'living' or 'good'". In example (3) (p. 199), the image shows ",1" where η is expected from examples (1) and (2); it is probably a misprint or scan error.
- Ex. 1–3 and the unnumbered exercise carry no printed solutions here.
