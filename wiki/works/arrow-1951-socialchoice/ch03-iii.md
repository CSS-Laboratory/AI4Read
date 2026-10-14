---
id: arrow-1951-socialchoice/ch03-iii
work: arrow-1951-socialchoice
unit: "Chapter III. The Social Welfare Function"
pages: 22-33
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# The Social Welfare Function (Arrow, Ch. III)

## L0 — One line
Arrow defines a social welfare function as a rule that states a corresponding social ordering for each set of individual orderings, and imposes five "apparently reasonable" conditions on it.

## L1 — The gist (≤ 120 words)
Can a society's ranking of social states be built from its members' rankings in a way that respects citizens' sovereignty and rationality? Arrow recasts Bergson's welfare function as a rule from individual orderings to a social ordering (Definition 4). He then lists five conditions: a wide domain of individual orderings, positive association, independence of irrelevant alternatives, non-imposition, and non-dictatorship. He calls each apparently reasonable, though open to question, and says together they state citizens' sovereignty and rationality in a general form. He also cites a later theorem: a sum of utilities satisfying Conditions 2 and 3, if any, breaks Condition 4 or 5. The chapter mainly sets up the problem; the general theorem comes later.

**Prerequisites:** weak orderings (R = "at least as good as", P = strict preference, I = indifference); the idea of a choice function C(S) derived from an ordering; basic notation of sets and "if and only if".

## L2 — Key ideas (5–10 bullets)
- A social welfare function is a rule mapping each set of individual orderings $R_1,\dots,R_n$ to one social ordering $R$. Arrow treats it as a method of choosing which Bergson-type welfare function applies (Def. 4, pp. 23–24).
- A constant rule is the "Platonic" case, in which social choices ignore individual tastes. A rule defined for every logically possible profile (one ordering per individual) is "universal" (p. 24).
- Condition 1 requires that every ordering of some three alternatives can arise from an admissible profile. It restricts the form of the function, because admissible profiles (those the function maps to a true social ordering) must yield true orderings (pp. 24–25).
- Condition 2 (positive association): raising $x$ in individual rankings, with nothing else changed, must not lower $x$ socially (pp. 25–26).
- Condition 3 (independence of irrelevant alternatives, IIA): the choice from $S$ depends only on individual orderings over $S$. The rank-order method violates it (pp. 26–28).
- Conditions 4 and 5 exclude imposed and dictatorial rules. Conditions 2 and 4 together express citizens' sovereignty (pp. 28–30).
- A sum-of-utilities rule, made to depend only on orderings by an arbitrary rule picking one utility indicator (a numerical scale representing the ordering) per ordering, is limited by Chapter V's general theorem, which Arrow cites without proof here. Kaplan's 0–1 rule fails Condition 3 (pp. 31–33).

## L3 — Walkthrough

### 1. Formal statement of the problem of social choice (pp. 22–25)
- Arrow largely restates Bergson's formulation. The arguments of Bergson's function are the components of a "social state", so he assigns a number (social utility) to each state. Society is described as maximizing it subject to technological or resource constraints (p. 22).
- Measurability is not needed. Only a social ordering satisfying Axioms I and II (from earlier chapters) is needed, and for that one must know the ranking of each pair (p. 22).
- If rankings never changed with individual values, that would be the Platonic realist view of an objective social good. Arrow says it was used to justify elite rule, "although... the connection is not a necessary one" (p. 22).
- **Utilitarian view (Bentham and followers):** the social good is grounded in individuals' good. Hedonist psychology identifies each person's good with his desires. Arrow says this viewpoint serves as a justification of political democracy and of laissez-faire economics, or at least of free choice of goods and occupations (pp. 22–23).
- Formally, individual behaviour is expressed by orderings $R_i$. For each pair of states the social choice depends on $R_1,\dots,R_n$. Some choices may still be independent of particular individuals (p. 23).

**Definition 4.** A *social welfare function* is a process or rule which, for each set of individual orderings $R_1,\dots,R_n$ of alternative social states (one per individual), states a corresponding social ordering $R$ (p. 23). Primes on the individual orderings mean primes on the social one.

- **Difference from Bergson:** Arrow's arguments are individual *values*, not *tastes*. His function chooses which Bergson-type function applies. The social choice reached may conflict with Bergson's value judgments. Arrow adds that no sharp line can be drawn between tastes and values (pp. 23–24).
- A rule giving the same $R$ for every profile gives the Platonic case (p. 24).
- If no prior knowledge of tastes is required, the function must be defined for every logically possible profile. It is then *universal*. Arrow says this ideal seems implicit in Benthamite ethics and welfare economics (p. 24).
- A set of individual orderings is *admissible* if the function gives it a true social ordering (Axioms I and II). A universal function is one for which every set is admissible. One might restrict admissibility on a priori grounds, for example by assuming each person values states solely by his own consumption (p. 24).

**Condition 1.** Among all the alternatives there is a set $S$ of three alternatives such that, for any orderings $T_1,\dots,T_n$ of $S$, there is an admissible set $R_1,\dots,R_n$ of orderings of all alternatives with $x R_i y$ iff $x T_i y$, for $x,y$ in $S$ (p. 24).

Condition 1 restricts the *form* of the function: for a sufficiently wide range of profiles it must give a true social ordering (pp. 24–25).

*Intuition note:* Arrow does not require universality. He only assumes that for some three alternatives nobody can know in advance how people rank them. The function must then cope with every possible ranking of those three.

### 2. Positive association of social and individual values (pp. 25–26)
- The social ordering should respond positively, or at least not negatively, to changes in individual values (p. 25).
- Suppose $x P y$ under $R_1,\dots,R_n$. Values then change so that, for each individual, the only change is that $x$ is higher. The new orderings are $R_i'$. Then one expects $x P' y$ (p. 25).
- Formal version: for all $x'\ne x$ and $y'\ne x$, $x' R_i' y'$ iff $x' R_i y'$. Moreover, for all $y'$, $x R_i y'$ implies $x R_i' y'$, and $x P_i y'$ implies $x P_i' y'$ (pp. 25–26).

**Condition 2.** For each $i$, if the two individual orderings are connected as above, then $x P y$ implies $x P' y$ (p. 26).

*Intuition note:* If everyone treats $x$ at least as well as before and nothing else changes, society should not rank $x$ lower. Votes for an alternative then help it.

### 3. The independence of irrelevant alternatives (pp. 26–28)
- $C(S)$ is the choice society would make from set $S$. As for one individual, it should not depend on alternatives outside $S$. Example: each voter lists the candidates, one candidate dies, and his name is blotted out of every list. The winner among the survivors should come from the remaining orderings only. Otherwise the result would depend on whether a candidate died before or after polling (p. 26).

**Condition 3.** Let $R_1,\dots,R_n$ and $R_1',\dots,R_n'$ be two sets of individual orderings, with social choice functions $C(S)$ and $C'(S)$. If, for all $i$ and all $x,y$ in a given $S$, $x R_i y$ iff $x R_i' y$, then $C(S)$ and $C'(S)$ are the same (pp. 26–27).

- **Arrow's example (rank-order method):** 3 voters, 4 candidates $x,y,z,w$, weights 4,3,2,1 for first to fourth choice. Voters 1 and 2 rank $x,y,z,w$; voter 3 ranks $z,w,x,y$. (added step) Scores: $x$ = 4+4+2 = 10, $y$ = 3+3+1 = 7, $z$ = 2+2+4 = 8, $w$ = 1+1+3 = 5, so $x$ is chosen. Delete $y$: the system gives a tie between $x$ and $z$ (added step: 7 each with weights 3,2,1). Yet $y$ is inferior to $x$ for every individual (p. 27).
- Huntington's team-scoring in individual contests (e.g., a foot race) shows an analogous inconsistency with what he called the "postulate of relevancy" (p. 27).
- If $S=\{x,y\}$, Condition 3 makes the choice depend only on who prefers $x$, who prefers $y$, and who is indifferent. Pairwise choices fix the whole social ordering and $C(S)$ for all environments. Condition 2 ensures that voting for an alternative makes its adoption surer (p. 28).
- Condition 1 says that, with individual orderings fixed and the environment varied, choices must be mutually consistent. Conditions 2 and 3 fix the environment and vary individual values in particular ways (p. 28).

*Intuition note:* IIA says that a third option's presence or absence should not change a verdict between two others. Arrow's examples show a plausible voting scheme failing this.

### 4. The condition of citizens' sovereignty (pp. 28–30)

**Definition 5.** A social welfare function is *imposed* if, for some pair of distinct $x,y$, $x R y$ holds for any set of individual orderings. Some preferences are then taboo: $y P x$ never holds, even if all prefer $y$ (p. 28).

- Arrow says it is arguable whether Definition 5 catches the essence of customary choice. This depends on whether individuals can have "true desires" conflicting with custom. He need not answer this. If the definition is not a model of custom, it at least models external control (colony, occupied country) (pp. 28–29). He certainly wishes all choices to be possible if unanimously desired by the group, so he imposes Condition 4 (p. 29).

**Condition 4.** The social welfare function is not to be imposed (p. 29).

- Arrow says this is stronger than needed. All that is required is a set $S$ of three alternatives, with Condition 1's properties, whose pairwise choices are not fixed in advance (p. 29).
- If there is no conflict between individual and code, individual orderings are known to obey norms. Condition 1 might then be weakened (Chapter VII) (p. 29).
- Condition 4 excludes the Platonic case. With Condition 2 it expresses the same idea as Bergson's Fundamental Value Propositions of Individual Preference. These say that when all individuals but one are indifferent between two alternatives, the community prefers one, or is indifferent, according as that one individual does (pp. 29–30).
- Arrow's footnote adds: strictly, these propositions are not implied by Conditions 2 and 4 with 1 and 3, though something very similar is. A slightly stronger Condition 2 would suffice (p. 30, fn. 4).
- Conditions 2 and 4 correspond to consumer's sovereignty. For values rather than tastes, Arrow calls it *citizens' sovereignty* (p. 30).

### 5. The condition of nondictatorship (p. 30)

**Definition 6.** A social welfare function is *dictatorial* if there exists an individual $i$ such that, for all $x,y$, $x P_i y$ implies $x P y$ regardless of the other individuals' orderings (p. 30).

**Condition 5.** The social welfare function is not to be dictatorial (p. 30).

- Arrow says it cannot be claimed that Definition 6 is a true model of actual dictatorship, since there is normally an element of consent. He still calls Condition 5 reasonable (Chapter VII) (p. 30).
- Arrow says the five conditions are value judgments that could be called into question; taken together they express citizens' sovereignty and rationality in a very general form, with citizens allowed a wide range of values. The problem is to build a social ordering of all conceivable states from any individual orderings in accordance with Conditions 1–5 (p. 31).

### 6. The summation of utilities (pp. 31–33)
- The Bentham–Edgeworth sum of utilities seems excluded, since Chapter II rejected cardinal and interpersonally comparable utility (p. 31). However, presumably the sum could be reformulated to depend only on the individual orderings; Arrow reads this as implied by Bergson's discussion, since Bergson does not find the sum to contradict the Fundamental Value Propositions (p. 31).
- The only way Arrow sees to make the sum depend only on orderings: an arbitrary rule assigns one utility indicator to each indifference map, and the sum of those is the social ordering (p. 31).
- Condition 1 holds for any such rule. Conditions 2 and 3 would require the rule to be stringently limited. The general theorem of Chapter V guarantees that the only rules making the sum satisfy 2 and 3, if any, violate Condition 4 or 5 (pp. 31–32).
- By Theorem 3 of Chapter VI the same holds even if each individual's utility depended solely on his own consumption. Arrow says he has not been able to construct a special proof for the sum of utilities that is essentially different from the proof of the general theorem (p. 32).
- **Kaplan's rule (a particular rule):** assume orderings over probability distributions obey von Neumann–Morgenstern axioms, giving utilities unique up to a linear transformation with expected-utility ordering. Assume each person has a best and a worst conceivable alternative. Fix utility 1 for the best and 0 for the worst. This is meant to make utilities comparable across persons (p. 32).
- **Arrow's counterexample:** three alternatives, three individuals. Two have utilities 1 for $x$, .9 for $y$, 0 for $z$. The third has 1 for $y$, .5 for $x$, 0 for $z$. (added step) The sums are $x$: 2.5, $y$: 2.8, so $y$ is preferred (p. 32). If $z$ is deleted, the first two get $x=1,y=0$ and the third $x=0,y=1$. (added step) The sums are $x$: 2, $y$: 1, so $x$ is preferred. Yet everyone ranks $z$ last (p. 32).
- A variant: let $z$ become indifferent to $x$ for the first two, and to $y$ for the third, with the relative positions of $x$ and $y$ unchanged. The utilities of $x,y$ then become the same as when $z$ was deleted. The choice between $x$ and $y$ changes, contrary to Condition 3 (pp. 32–33).
- Arrow says the result is not special to this rule. Choosing two alternatives to carry given utilities (say 0 and 1) is arbitrary, and this arbitrariness shows up as failure of one of the conditions (p. 33).

*Intuition note:* Arrow's rule fixes each person's utility scale by giving two alternatives (the best and the worst) the values 1 and 0. Changing those alternatives shifts the scale, and with it the verdict between two others. Arrow says this arbitrariness is not special to this rule (p. 33).

## Toy example (ours)
Rank-order voting (Borda), 3 voters, candidates $a,b,c$, weights 2,1,0.
- **Profile A:** V1: $a\succ b\succ c$; V2: $b\succ a\succ c$; V3: $c\succ a\succ b$.
 Scores: $a = 2+1+1 = 4$; $b = 1+2+0 = 3$; $c = 0+0+2 = 2$. So $a$ beats $b$.
- **Profile B:** V1: $a\succ b\succ c$; V2: $b\succ c\succ a$; V3: $c\succ a\succ b$.
 Scores: $a = 2+0+1 = 3$; $b = 1+2+0 = 3$; $c = 0+1+2 = 3$. A three-way tie.
- On $\{a,b\}$ both profiles are identical: V1 and V3 prefer $a$, V2 prefers $b$. Only V2's placement of $c$ changed. Yet the social verdict on $a$ versus $b$ changed from "$a$ wins" to "tie". This breaks Condition 3.

## Concepts
- [[social-welfare-function]] — rule mapping each profile of individual orderings to a social ordering (Def. 4) (p. 23)
- [[independence-of-irrelevant-alternatives]] — choice from $S$ depends only on individual orderings over $S$ (Condition 3) (p. 27)
- [[positive-association]] (new) — raising $x$ in individual orderings, nothing else changed, never lowers $x$ socially (Condition 2) (p. 26)
- [[citizens-sovereignty]] (new) — Conditions 2 and 4 together; social choices determined by individual values in the agreeing direction (p. 30)
- [[imposed-social-welfare-function]] (new) — some pair $x,y$ with $x R y$ whatever the individual orderings (Def. 5) (p. 28)
- [[dictatorship]] (new) — one individual's strict preference always becomes the social one (Def. 6) (p. 30)
- [[admissible-profile]] (new) — a set of individual orderings that the function maps to a true social ordering (p. 24)
- [[unrestricted-domain]] — here only a weaker form: Condition 1 requires every ordering of some three alternatives to be possible, not every profile (p. 24)
- [[arrows-impossibility-theorem]] — only mentioned: a general theorem in Chapter V is cited, but not stated or proved here (p. 31)

## Canonical instances
- [[rank-order-voting-example]] — 3 voters, 4 candidates, weights 4,3,2,1; deleting $y$ turns $x$'s win into a tie (p. 27)
- [[huntington-team-scoring]] — foot-race team scoring violates the "postulate of relevancy" (p. 27)
- [[kaplan-utility-rule]] — 0/1-normalised utilities summed; deleting $z$ reverses $y$ over $x$ (pp. 32–33)

## Bridges (candidates)
- [structural-analogy] Condition 3 (IIA) ↔ choice theory: independence of the choice from alternatives outside the menu (Arrow likens it to a single individual's choice, p. 26).
- [structural-analogy] Condition 2 (positive association) ↔ electoral competition: more support for a party should not lower its result (monotonicity).
- [metaphor] Sum-of-utilities with 0/1 normalisation ↔ range voting: scores summed on a fixed scale, where the choice of endpoints is also arbitrary.

## Questions this raises
- Which of the five conditions carries most of the weight, and which can be weakened without making the problem trivial?
- Arrow admits Definitions 5 and 6 are imperfect models of custom and dictatorship. Do they exclude too much or too little?
- If tastes and values cannot be sharply separated, what is the right "input" to a social welfare function?
- What does the chapter's promised general theorem say about all five conditions together?

## Reading notes
- Printed page = pdf − 11. The source pages had no usable text layer, so everything was read from the page images. Page 33 has only a few lines.
- Definition 1 and Axioms I–II are from earlier chapters, and Chapters V–VII and Theorem 3 of Chapter VI are cited but not included. Statements about them are only what this chapter says.
- Condition 1 here is weaker than a full unrestricted domain. Conditions 1–5 are as stated on these pages; no comparison with other formulations is made here.
- No misprints noticed.
