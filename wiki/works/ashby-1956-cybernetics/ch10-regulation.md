---
id: ashby-1956-cybernetics/ch10-regulation
work: ashby-1956-cybernetics
unit: "10 Regulation in Biological Systems"
pages: 195–201
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Regulation in Biological Systems

## L0 — One line
A good regulator sits between disturbances and an organism's essential variables and blocks the flow of variety from the first to the second, which is how survival, stability and information fit together.

## L1 — The gist (≤ 120 words)
Ashby asks what regulation is in biology and how it relates to survival and information. He translates "survival" into the stability of a set of states: an organism survives if its essential variables stay inside permitted limits. Natural selection favours gene-patterns that place a regulator F between disturbances D and essential variables E. A good regulator blocks the flow of variety from D to E, so a record of E tells you little about D. Blocking can be passive (a shell) or active (skilled counteraction that uses information). The chapter is meant to motivate the study of regulation in the later chapters.

**Prerequisites:** "variety" as a count of distinguishable states; essential variables (variables that must stay within limits for the organism to live); a regulator (a part placed between a source of disturbance and those variables); gene-patterns (the inherited patterns that shape an organism); the idea of a dynamic system with states and an operation acting on them; stability of a set of states (S.5/5, referred to but not restated here).

## L2 — Key ideas
- Part III studies regulation and control, which Ashby calls the central theme of cybernetics. This chapter gives the motive and links regulation to variety (p. 195).
- The chapter's aim is to tie together regulation, information and survival in one rigorous, uniform method (p. 196).
- The "lifeless" state is an almost-equilibrium but an unstable one, and two thousand million years of elimination shaped today's organisms (p. 196).
- "Living" is defined as being in a chosen subset of states, and the organism survives an operation $C$ if the result lies in that subset. If a skilled organism always survives $C$, so that every result stays inside the subset, this is identical with stability of a set (p. 197).
- What survives over the ages is gene-patterns that grow a defence, F, between D and the essential variables E. Better regulators mean better survival chances, other things equal (pp. 198–199).
- A regulator is judged by the variety it lets through. If F is a regulator, inserting F between D and E lessens the variety transmitted from D to E (p. 199).
- Water-bath, autopilot, air-conditioner and hunter examples show that a good regulator hides the disturbances from E (pp. 200–201).
- Blocking can be a passive barrier or active counteraction using information. The remaining chapters study the active kind (p. 201).

## L3 — Walkthrough

### 10/1–10/2. Purpose and plan (pp. 195–196)
- Parts I and II treated Mechanism and Variety. Part III uses them to study regulation and control (p. 195).
- Chapter 11 will give a quantitative law: the amount of regulation achievable is bounded by the amount of information transmissible in a certain channel. Chapter 12 asks what machinery can embody this and introduces the "Markovian" machine. Later chapters treat harder cases, especially very large systems (p. 195).
- At first the regulator is assumed to be already provided (inborn, manufactured or otherwise). How it came to be made is deferred to S.13/10 (p. 195).
- This chapter mainly gives motive. Ashby says Cannon's *Wisdom of the Body* covered internal, vegetative regulation. A larger book is still needed to show that all "higher", outward-directed activities are also regulatory, i.e. homeostatic. He leaves much of this to the reader's imagination (pp. 195–196).

### 10/3. The foundation (p. 196)
- Ashby restates a well-known deduction in his own terms. The earth is two thousand million years old, and biologists mostly study what exists today (p. 196).
- From S.4/23: a large system with much repetition in its parts, containing an autocatalytic property, is essentially unstable in the absence of that property. "Autocatalytic" means its occurrence at one point raises the probability of its occurring elsewhere (p. 196).
- Many combinations of carbon, nitrogen and a few other elements are self-reproducing. So "lifeless" is almost an equilibrium, but an unstable one. A single deviation starts a trajectory that moves further and further from it (p. 196).
- Defective forms have been eliminated, so almost every feature of an organism bears the marks of adaptation to survival. Examples are eyes, roots, cilia, shells and claws, and the brain too (p. 196).

> **Intuition note.** Life can be seen as a runaway process that started from an unstable "off" state. What we now observe is whatever kept going. Ashby infers the survival-oriented design of organisms from this selection.

### 10/4. Survival as stability of a set (p. 197)
- Example: a mouse escaping a cat. The mouse can be in many states, such as posture, head direction, temperature, or one ear or two. Many of these still count as survival. States such as being in four pieces, headless, or dissolved in the cat's blood do not (p. 197).
- Formalisation: the mouse's states are $M_1, M_2, \dots, M_k, \dots, M_n$. By convention "living mouse" means a state in the subset $M_1,\dots,M_k$. An operation $C$ (the cat) maps state $M_i$ to $C(M_i)$. If $C(M_i)=M_2$, the mouse has survived, because $M_2$ is in the subset (p. 197).
- If a mouse is so skilled that it always survives $C$, then all of $C(M_1),\dots,C(M_k)$ lie inside $\{M_1,\dots,M_k\}$. Ashby says this is identical with the stability of a set (S.5/5). So facts and theorems about either concept can be used for the other, provided exactness is kept (p. 197).
- States are often defined by variables. The living states are those in which certain *essential variables* are kept within assigned ("physiological") limits (p. 197).

> **Intuition note.** Surviving $C$ means the result lands inside the allowed set of states. A mouse that always survives $C$ is never pushed out of that set, and Ashby says this is identical with stability of a set. So facts and theorems about either can be used for the other, provided exactness is kept.

### 10/5. What survives, and the D→F→E diagram (p. 198)
- What survives is not the individual but well-compounded gene-patterns. Those likely to survive cause growth of a mechanism of defence between themselves and the dangerous world. Examples: the shell in *Testudo* and the brain in *Homo* (p. 198).
- The cat–mouse picture was the diagram $C \to M$. The new picture is $D \to F \to E$ (p. 198):
  - $E$ = the essential variables.
  - $D$ = the source of disturbances and dangers (such as $C$) from the rest of the world.
  - $F$ = the interpolated part formed by the gene-pattern to protect $E$ (shell, brain). $F$ may include parts of the environment used for protection, such as a rabbit's burrow or a swordsman's sword (p. 198).
- The states of $E$ are divided into $\eta$ ("organism living", "good") and not-$\eta$ ("not living", "bad"). A finer classification is allowed in principle (p. 198).
- Ashby's examples (pp. 198–199):
  1. Thermostatic water-bath: $E$ is temperature, $\eta$ is, say, 36°–37°C, $D$ is cold water, draughts, cold objects, and $F$ is the whole regulatory machinery. $F$ tends to lessen the effect of $D$ on $E$.
  2. Automatic pilot: $E$ is a vector of yaw, pitch and roll. $\eta$ is the positions where all three are within limits. $D$ is gusts, passenger movements and uneven engine thrust. $F$ is pilot, ailerons, rudder and so on.
  3. Bicycle rider: $E$ is chiefly his angle with the vertical. $\eta$ is the set of small permissible deviations. $D$ is the disturbances threatening large deviation. $F$ is the mechanical, anatomical and neuronic machinery.
- Summary: natural selection favours gene-patterns that get, in whatever way, a regulator $F$ between $D$ and $E$. Other things equal, the better $F$ is as a regulator, the larger the organism's chance of survival (p. 199).

### 10/6. Regulation blocks the flow of variety (pp. 199–201)
- A good regulator needs two things: keep the variable within close limits, and make that range match the desired one (p. 199).
- The set $\eta$ has less variety than the set of all possible values of $E$, because $\eta$ is a selected part of $E$'s states. So, if $F$ is a regulator, inserting $F$ between $D$ and $E$ lessens the variety transmitted from $D$ to $E$. An essential function of a regulator is to block that transmission (p. 199).
- Test case: two water-baths A and B are tested for a day under similar disturbances (Fig. 10/6/1). A's temperature record wanders. B's record is flat. B is clearly better, and Ashby chooses it because its record gives no information about the disturbances that reached it (p. 200).
- Same argument for other cases (pp. 200–201):
  - Autopilot: a good one gives a smooth flight, so passengers cannot tell whether it is gusty outside.
  - Air-conditioner: if the room's hotness tells me the outside is hot, the conditioner is failing. A good one with the blinds drawn leaves me unable to guess the weather.
  - Hunter or earner: the unskilled one in hard times forces the essential variables (liver, tissues) to extremes. The skilled one does not. The family of a skilled provider may not notice anything unusual.
- Conclusion: an essential feature of the good regulator is that it blocks the flow of variety from disturbances to essential variables (p. 201).

> **Intuition note.** If the regulated variable still shows what the disturbance did, the disturbance got through. A perfect regulator leaves nothing to read in $E$. This is why Ashby connects regulation to information and variety.

### 10/7. Two ways of blocking (p. 201)
- Ashby says all ways of blocking turn out to be fundamentally the same. He gives two extremes (p. 201).
- Passive block: interpose a barrier. Examples are the tortoise's shell, a tree's bark, seal blubber and the human skull (p. 201).
- Active defence by skilled counter-action: get information about the coming disturbance, prepare, and meet it with a defence as complex and mobile as the disturbance. Example: a fencer with no armour who trusts his parrying. Higher organisms mostly use this method, and their nervous system developed for it (p. 201).
- In the fencer case, information must be gathered by every possible means (eyes, learned use of them). The end result is that his essential variables, such as blood-volume, stay within normal limits as if no duel had occurred. Information flows freely to non-essential variables, but the variety in "duel or no-duel" is prevented from reaching the essential variables (p. 201).
- The remaining chapters study this active defence: what principles govern it, what mechanisms achieve it, and what to do when regulation is very difficult (p. 201).

## Toy example (ours, not from the text)
Water-bath with desired range $\eta$ = 36–37°C. The disturbance $D$ is a temperature change with three possible values: −2, 0, +2°C. The target temperature is 36.5°C.

- Bath A (no regulator): $E = 36.5 + D$. This gives 34.5, 36.5 or 38.5. $E$ takes 3 distinct values, 2 of them outside $\eta$. The record of $E$ shows exactly which $D$ occurred, so variety 3 passes from $D$ to $E$.
- Bath B (regulator $F$ adds $-D$ via a heater): $E = 36.5 + D + (-D) = 36.5$ for every $D$. $E$ takes 1 value, inside $\eta$. The variety passed is 1, so the record reveals nothing about $D$.
- Result: B blocks variety (3 → 1) and keeps $E$ inside $\eta$. This matches Ashby's choice of the flat record B.

## Concepts
- [[homeostasis]] — the term Ashby uses ("i.e. homeostatic") for regulatory activity. He says a book is still needed to show that all the organism's exteriorly-directed activities are similarly regulatory (pp. 195–196).
- [[variety]] — the number of distinguishable states. Here: the variety of $\eta$ is less than that of $E$ (p. 199).
- [[stability]] — Ashby ties survival to the stability of a set of states: all $C(M_i)$ stay within $\{M_1..M_k\}$ (p. 197).
- [[essential-variables]] (new) — variables that must stay within physiological limits for the organism to live (p. 197).
- [[regulator]] (new) — $F$, the part between disturbances $D$ and essential variables $E$ that lessens the effect of $D$ on $E$ (p. 198).
- [[disturbance and noise]] — here $D$, the source of disturbances and dangers from outside (p. 198).
- [[survival-as-set-stability]] (new) — survival defined as the system always staying in a chosen subset of states (p. 197).
- [[autocatalytic-instability]] (new) — a repeating system with an autocatalytic property is unstable without it, so "lifeless" is an unstable near-equilibrium (p. 196).
- [[passive-vs-active-regulation]] (new) — a passive barrier (shell) versus skilled counter-action using information (fencer) (p. 201).
- [[law of requisite variety]] (name not used on these pages) — only announced for Chapter 11 as a bound on regulation by transmissible information. Not derived here (p. 195).

## Canonical instances
- [[mouse-and-cat]] — "survival" as staying within states $M_1..M_k$ under operation $C$ (p. 197).
- [[thermostat-water-bath]] — $E$ temperature, $\eta$ 36–37°C, and the A/B comparison (pp. 198, 200).
- [[automatic-pilot]] — $E$ = yaw, pitch, roll. A good one hides gustiness from passengers (pp. 198, 200).
- [[bicycle-rider]] — $E$ is the angle with the vertical (p. 198).
- [[air-conditioner]] — a good one blocks information about the weather (p. 200).
- [[fencer-duel]] — active defence. Blood-volume stays normal, the "duel or no-duel" variety is blocked (p. 201).
- [[tortoise-shell]] — passive block of variety (p. 201).

## Bridges (candidates)
- [structural-analogy] $D \to F \to E$ with variety blocked ↔ control-theory: disturbance rejection by a controller (feedback/feedforward). The goal of keeping $E$ steady despite $D$ is the same, but this chapter gives no mechanism.
- [same-math] Survival as "all $C(M_i)$ stay in the set" ↔ stability of a set (S.5/5). Ashby says the two representations are identical (p. 197).
- [structural-analogy] Active defence that gets information before the disturbance arrives ↔ feedforward: it acts on information about the disturbance. This chapter names neither.
- [metaphor] Flat water-bath record ↔ homeostasis: nothing is visible in $E$ about what hit the system.

## Questions this raises
- How exactly is the quantity of regulation bounded by information in a channel (Ch. 11)?
- If a perfect regulator leaves no trace of $D$ in $E$, how can the regulator itself get information about $D$ (cf. the fencer)?
- What kinds of machinery can actually do the regulating (Ch. 12)?
- How did the regulator itself come to be made (deferred to S.13/10)?

## Exercises worth doing
- Ex. 1–2 (p. 197) — read $C(M_7)=M_9$ and $C(M_8)=M_4$ with $n=10$, $k=5$ in terms of the living set; checks the survival definition — difficulty: easy.
- Ex. 3 (p. 197) — define "lethal" if $C$'s attack is always fatal to $M$ — difficulty: easy.
- Unnumbered Ex. (p. 199) — name the variables kept within limits by ten regulators (air-conditioner, climber's oxygen supply, wind-screen wiper and so on). Practises finding $E$, $D$ and $F$ — difficulty: medium.

## Reading notes
- The metadata gives no printed page numbers, and the page labels show "?". 195, pdf 105 = pp. 196–197, pdf 106 = pp. 198–199, pdf 107 = pp. 200–201. The unit therefore covers pp. 195–201.
- In the text layer the set symbol after $\eta$ appears as "∇" or "V" ("η∇those"). I could not tell what it stands for, so I did not use it in the digest and wrote only $\eta$ and not-$\eta$.
- In the bicycle-rider example (p. 198) the text and image show ",1" where context suggests $\eta$. This is my inference.
- The unit mentions the "Markovian" machine and gives the law of Chapter 11 only as a one-sentence announcement (p. 195); neither is developed here. The Markovian sentence ("This chapter introduces…") follows the sentence about Chapter 12, so I read it as referring to Chapter 12; this is my inference.
