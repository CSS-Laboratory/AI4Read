---
id: arrow-1951-socialchoice/ch07-vii
work: arrow-1951-socialchoice
unit: "Chapter VII. Similarity as the Basis of Social Welfare Judgments"
pages: 74–91
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 21
pipeline_version: 0.1
---
# Similarity as the Basis of Social Welfare Judgments

## L0 — One line
A workable social welfare function needs some similarity in individuals' attitudes toward social alternatives. Full unanimity is not needed: Black's single-peakedness suffices for majority rule when the number of voters is odd, though Arrow says it is not obviously applicable (p. 89).

## L1 — The gist (≤ 120 words)
Earlier chapters set conditions for a social welfare function (a rule turning individual orderings into one social ordering). This chapter asks what similarity among individuals would make one possible. Complete unanimity works trivially. Black's single-peaked preferences also work: majority decision then gives a transitive social ordering if the number of voters is odd (Theorem 4). Arrow then links similarity to idealist philosophy (the "general will"), to uncertainty about means and ends, and to agreement on the decision process itself. He finds no easy general rule: some consensus on ends is needed, and in the case he examines, partial unanimity leaves the earlier impossibility result in place.

**Prerequisites:** weak orderings (R, P, I); majority decision as counting N(x,y); Chapter III conditions, Axioms I–II and Theorem 3 from earlier chapters (not restated here); basic proof by cases.

## L2 — Key ideas (5–10 bullets)
- If all individuals share one ordering, the social ordering can be that ordering, so the social ordering is formally a dictator's, but nondictatorship loses its intrinsic desirability. The same holds if it is assumed in advance that a majority shares an ordering (p. 74).
- Black's single-peaked preferences restrict individual orderings: all can be made single-peaked on one strong ordering of the alternatives. Individuals may still have different first choices. (A strong ordering puts any two alternatives in a definite order, like "less than"; single-peaked means each person's utility has one peak along that line.) (pp. 75–77, 80).
- Theorem 4: under single-peakedness, majority decision satisfies Condition 1'' and Conditions 2–5 for any number of alternatives, provided the number of individuals is odd. The proof uses Lemma 6 and three betweenness cases (pp. 78–79). (Condition 1'' asks only that the social ordering be a weak ordering when the individual orderings are single-peaked.)
- Arrow notes that the complete-unanimity assumption underlies the idealist school's "general will" or moral imperative (the will supposedly the same in all, as against each person's everyday will). He says some consensus on ends must be demanded and, citing Knight's formulation, that it need not rest on a metaphysical absolute; any view that depends on consensus implies the market cannot be taken as the social welfare function (pp. 81–86).
- Arrow says it could be held that orderings of social ends are likely to be more similar than orderings of social decisions. Uncertainty about the link between decisions and ends is a source of differing preferences (pp. 87–88).
- Unanimity on some pairs only (partial unanimity), in the case Arrow examines, leaves intact the earlier result that only imposed or dictatorial functions are possible, a fortiori (p. 89).
- Social states may include the decision process. A unanimous, overriding valuation of one process may be regarded as solving the problem, but Arrow says that process agreement alone hardly seems a credible picture of most people's psychology (pp. 89–91).

## L3 — Walkthrough

### 1. Complete unanimity (pp. 74–75)
- Assume nothing about the shape of any one individual's preferences, but assume all have the same preferences over social alternatives. This implies a social-minded attitude and a homogeneous society. If the preferences are those that would be expressed once corruptions of the environment were removed, it is the idealist view of political philosophy (p. 74).
- Then choose one individual and let the social scale equal his. This satisfies all Chapter III conditions except nondictatorship, which loses its intrinsic desirability, since it does not matter who is dictator (p. 74).
- Generalization: if it is assumed in advance that a majority has the same ordering (membership known or not), the method of majority decision (Definition 9) picks that ordering. All Chapter III conditions are again satisfied (p. 74).
- Arrow calls these results "trivial from the mathematical point of view". They reinforce the end of Chapter VI, Section 4: like attitudes toward social alternatives, not like tastes for individual consumption, are needed. Possible sources are desires for freedom, national power, equality and prolongation of life. Differences may remain through imperfect knowledge (pp. 74–75).

*Intuition note.* If everyone ranks the options identically, any one person's ranking can serve as society's; this is formally a dictatorship, but it does not matter who the dictator is. Arrow suggests that what is needed is agreement about *social* alternatives, not about tastes for individual consumption.

### 2. The case of single-peaked preferences (pp. 75–80)
- **Black's assumption.** If $U_1,\dots,U_n$ are utility indicators for $R_1,\dots,R_n$, the alternatives can be arranged on a one-dimensional variable so that each graph of $U_i$ has a single peak (p. 75).
- **Example 1 (p. 76):** prewar European parties with an agreed Left–Right order. Of two parties on one side of his own, a person prefers the one nearer to his own. Nothing is said about a party on the right versus one on the left of his first choice.
- **Example 2 (p. 76):** hours of work. Suppose that, for technological efficiency, all workers must work the same hours. With wages equal to marginal productivity, the real wage is a known decreasing function of hours, so each alternative is one number. Each person's income–leisure transformation curve and indifference curves are assumed to give one utility maximum, with utility falling in either direction from it.
- Black shows that with an odd number of voters, exactly one alternative receives a majority over any other. With finitely many alternatives, remove the best and repeat to get a transitive ordering. The general case needs a formal definition (p. 76).
- **Definition 11.** $S$ is a *strong ordering* if (a) for all $x$, not $x\,S\,x$; (b) for all $x\neq y$, either $x\,S\,y$ or $y\,S\,x$; (c) $x\,S\,y$ and $y\,S\,z$ imply $x\,S\,z$ (p. 77).
- **Definition 12.** $B(x,y,z)$ ("$y$ is between $x$ and $z$") means: either ($x\,S\,y$ and $y\,S\,z$) or ($z\,S\,y$ and $y\,S\,x$) (p. 77).
- **Lemma 5.** For distinct $x,y,z$, exactly one of $B(x,y,z)$, $B(y,x,z)$, $B(y,z,x)$ holds (p. 77).
- **Assumption of single-peaked preferences.** There is a strong ordering $S$ such that for each $i$, $x R_i y$ and $B(x,y,z)$ together imply $y P_i z$ (p. 77).
- **Condition 1''.** For all sets of individual orderings satisfying the Assumption, the social ordering $R$ shall be a weak ordering. Black proposes it in place of Condition 1 (p. 77).
- Majority decision satisfies Conditions 2–5 for any number of alternatives but not Condition 1 when there are more than two. The claim to be shown is that it satisfies Condition 1'' (p. 77).

With $N(x,y)$ the number of individuals for whom $x R_i y$, majority decision gives
$$x R y \iff N(x,y)\ge N(y,x). \tag{1}$$

**Lemma 6.** Let $R$ come from majority decision. If, for all $i$, $x R_i y$ implies $z P_i w$ (for given $x,y,z,w$), then $x R y$ implies $z R w$ (p. 78).

*Proof.* Assume the hypothesis and $x R y$.
- Everyone with $x R_i y$ has $z R_i w$, so
$$N(z,w)\ge N(x,y). \tag{2}$$
- Since $x R y$, by (1)
$$N(x,y)\ge N(y,x). \tag{3}$$
- If $w R_i z$ then not $z P_i w$. By hypothesis, not $x R_i y$, hence $y R_i x$. So $w R_i z$ implies $y R_i x$, and
$$N(y,x)\ge N(w,z). \tag{4}$$
- From (2)–(4), $N(z,w)\ge N(w,z)$, so $z R w$ by (1). ∎

**Theorem 4** (Possibility theorem for single-peaked preferences). Majority decision is a social welfare function satisfying Condition 1'' and Conditions 2–5 for any number of alternatives, provided the number of individuals is odd (p. 78).

*Proof.*
- By Lemma 3 (earlier chapter), Conditions 2–5 hold. It remains to show $R$ satisfies Axioms I and II whenever the $R_i$ satisfy the Assumption (p. 78).
- Axiom I: either $N(x,y)\ge N(y,x)$ or the reverse, so by (1) $x R y$ or $y R x$ (p. 78).
- Transitivity: assume $x R y$ and $y R z$; show $x R z$. If $x=y$ or $y=z$ this is immediate. If $x=z$, it follows from $N(x,x)\ge N(x,x)$ and (1). Now take $x,y,z$ distinct and use Lemma 5 (p. 78).
  - (a) $B(x,y,z)$: if $x R_i y$ then $y P_i z$ (Assumption), so $x P_i z$. Apply Lemma 6 with $z\to x$, $w\to z$: $x R y$ gives $x R z$ (pp. 78–79).
  - (b) $B(y,x,z)$: suppose $y R_i z$ but not $x P_i z$. Then $z R_i x$, so $y R_i x$. The Assumption (with $x,y$ interchanged) gives $x P_i z$, a contradiction. So $y R_i z$ implies $x P_i z$. Lemma 6 (with $x\to y$, $y\to z$, $z\to x$, $w\to z$) gives $y R z \Rightarrow x R z$ (p. 79).
  - (c) $B(y,z,x)$: suppose $y R_i z$. The Assumption gives $z P_i x$, so $y P_i x$:
$$y R_i z \text{ implies } y P_i x. \tag{5}$$
  Let $N'$ be the number with $y P_i x$ and $N$ the total. Then
$$N(x,y)=N-N'. \tag{6}$$
$$N(y,x)\ge N'. \tag{7}$$
  Since $x R y$, $N-N'\ge N'$, i.e.
$$N'\le N/2. \tag{8}$$
  From (5),
$$N'\ge N(y,z). \tag{9}$$
  Each $i$ has $y R_i z$ or $z R_i y$, so
$$N(y,z)+N(z,y)\ge N. \tag{10}$$
  Since $y R z$, $N(y,z)\ge N(z,y)$, so $N(y,z)\ge N/2$ by (10). With (9), $N'\ge N/2$, and with (8), $N'=N/2$. This contradicts an odd $N$, so case (c) cannot arise with both $x R y$ and $y R z$ (p. 79).
- In every case where $x R y$ and $y R z$ could hold, $x R z$ also holds, so $R$ is transitive. ∎ (p. 79)

*Intuition note.* When everyone sorts the options along one line, cyclic majority patterns are blocked when the number of voters is odd. In the proof, the one case that could break transitivity needs an exact tie, which an odd number of voters rules out.

**Remarks (pp. 79–80).**
- Theorem 1 is a special case of Theorem 4, since two alternatives are necessarily single-peaked. Complete unanimity is also a case, if alternatives indifferent to everyone are treated as identical.
- The Chapter I example of the "paradox of voting" has no ordering of the three alternatives that makes all individuals single-peaked (p. 80).
- Oddness is essential. Take two individuals: one has $x,y,z$, the other $y,z,x$, with $x,y,z$ as basic ordering. Majority gives $x$ indifferent to $y$, $y$ preferred to $z$, and $x$ indifferent to (not preferred to) $z$ (p. 80).
- As Black points out, one need not make all pairwise comparisons. It suffices to take the median of the first choices, arrayed along the basic strong ordering (p. 80).
- Arrow's reading: individuals may have varied first choices but must share a fundamentally similar attitude toward classifying the alternatives, since all order them the same way (p. 80).
- **Footnote 8 (pp. 80–81).** Black meant his work for actual political behaviour, as in a committee voting on successive motions, with each person voting by his ordering. Arrow gives a counterexample to that behaviour. Orderings are individual 1: $x,y,z$; individual 2: $y,x,z$; individual 3: $z,y,x$. Motions come up in the order $y,z,x$. If all vote sincerely, $y$ wins. If individual 1 votes for $z$ first, $z$ beats $y$, and then $x$ beats $z$. So individual 1 gains by misrepresenting. Arrow says the problem resembles the majority game and its analysis is difficult (cf. von Neumann and Morgenstern).

### 3. The idealist position and the concept of consensus (pp. 81–86)
- Arrow offers no definite answer on whether such mathematical restrictions have social significance. He offers tentative reflections (p. 81).
- **Idealist school** (Rousseau, Kant, T. H. Green). The individual will, as shaped by external influences, is distinguished from the general will, which is the same in all. Social morality rests on the latter. On Arrow's account of this view (fn. 10 cites Rousseau), the two wills may diverge widely and agree only by accident; the general will can never err though it may be mistaken as to means; and the existence of the general will as the basis of a society is insisted on (pp. 81–82).
- **Kant's three imperatives** (p. 82):
  - technical: knowledge of means, which Arrow equates with "environment";
  - pragmatic: seek happiness, which corresponds to individual orderings of social alternatives; it is vague and uncertain;
  - moral (categorical): corresponds in a sense to the social ordering, and is also an individual ordering for everyone, namely the will he would have if fully rational.

  The first two are hypothetical imperatives (contingent). The moral imperative needs full interpersonal validity (Autonomy of the Will) and treating each person as an end. Rational obedience to it forms a "kingdom of ends", which Arrow equates with a society that has a satisfactory social welfare function (p. 82).
- Summary of the doctrine: each individual has two orderings, and the truer one is relevant for social choice. Complete unanimity is assumed on that ordering (p. 83).
- Arrow's assessment: requiring identical pragmatic imperatives is overly strong, and perhaps asking identical moral imperatives is too much. Section 2 shows unanimity is mathematically unnecessary. But "it must be demanded" that there be some consensus on the ends of society, "or no social welfare function can be formed". If two wills are denied, the consensus must be in overtly expressed orderings. If accepted, it may lie in moral imperatives (p. 83).
- **Others on consensus** (pp. 83–85):
  - Knight (reported view): ideals are part of our culture and uniform enough to be a standard for a country at a given time. Arrow values this formulation for showing that consensus need not rest on a metaphysical absolute, and says Knight evidently treats the moral imperative as discoverable by special techniques.
  - Stigler (reported): reproaches the new welfare economics for ignoring consensus on ends. Arrow finds it unclear whether Stigler sees such ends as obvious or as needing inquiry.
  - Dobb vs. Lerner: Dobb attacks "sacredness of consumers' preferences" (e.g. time preference) and says collective choices are superior, which implies a distinction between moral and pragmatic imperatives. Lerner replies that Dobb implies a transcendental optimum.
- **Dilemma** (pp. 84–85): empirically, Arrow says we can reject the idea that consensus is found in expressed individual wills. If it lies in the moral imperative, what is its basis? Ethical absolutism is unsatisfying to a mind brought up in the liberal heritage. Knight's relativism risks glorifying the status quo, but still seems the better alternative.
- If moral consensus is assumed, the question becomes choosing a mechanism that best brings the pragmatic imperative into line with the moral one. This is Rousseau's route to comparing forms of government. The case for democracy then rests on free discussion as the best technique for finding the moral imperative, and voting becomes each person giving his opinion of the general will (p. 85).
- **Pooling experts.** This model resembles pooling experts' opinions (footnote 25: Helmer, Fisher's discriminant analysis, Schuyler's rank-order voting). An antidemocrat might argue that only a minority are capable of discerning the moral imperative (thus Plato's guardians). A prodemocrat might argue that all have natively an equal portion of the light. The analogy is incomplete, because the pooling method may itself change people's expertness (army officers: more leisure may help them, or isolation may hurt). Establishing a dictator or elite may distort the pragmatic from the moral (pp. 85–86).
- **Market.** Any view that depends on consensus as the basis for social action implies the market cannot serve as the social welfare function, since it cannot register the altruistic motives needed for consensus. This does not deny limited use of the market as an instrument, especially if deliberately manipulated so that pragmatic behaviour coincides with moral (p. 86).

*Intuition note.* Arrow treats "everyone agrees" as a claim about agreement on a deeper level than stated wishes. The question moves from aggregating wants to designing procedures that bring wants close to a shared deeper standard.

### 4. Knowledge and the meaning of social alternatives (pp. 86–88)
- Each person is presumed to have ultimate values, partly biological and partly cultural, largely unconscious. Overt preferences are for instrumental values. Instrumental sets differ with knowledge of means and of what the ultimate values are (p. 86).
- Aspirin example: a price ratio above ten to one between two chemically indistinguishable brands. Few economists would oppose laws against false advertising (p. 87).
- **Two readings of "alternative"** (p. 87): (1) *social decision*, a vector of government decisions (tax rates, expenditures, etc.); (2) *social end*, a complete description of every individual's state through the future. Social ends are, or fully determine, ultimate ends. Decisions determine ends wholly or partly, but that relation is empirical and uncertain.
- Chapter V's argument is valid under either reading. Arrow says it could be held that, since ultimate ends arise from biological and cultural needs and are in part objective, orderings of social ends are likely to be more similar across individuals than those of social decisions. If such similarity suffices for a welfare function, social decisions should be ordered by the ordering of ends plus scientific and statistical methods that limit ignorance (pp. 87–88).
- "Enlightened self-interest" would be justified if all share the same ultimate ends for the community. Differences would then come from lack of knowledge (p. 88).
- Uncertainty also bears on centralized versus decentralized planning. Centralization may reduce uncertainty for planners (more facts), and errors may cost more, but not if a rational method of planning against uncertainty is used. Hicks's certainty-equivalent theory of uncertainty is too restricted (Hart and Friedman, as Arrow reports) (p. 88).

### 5. Partial unanimity (p. 89)
- The correct mathematical generalization of unanimity is not easy to see. Black's postulate is not obviously applicable (p. 89).
- Attempted generalization: suppose all agree on some pairs but not others, i.e. there is a quasi-ordering $Q$ with which all individual orderings are compatible. If three alternatives are such that $Q$ says nothing on any pair, partial unanimity does not exclude any of the three (p. 89).
- Deduction from Theorem 3: if $Q$ is known in advance, Theorem 3 applies with $Q_1,\dots,Q_n$ all the same. Merely postulating unanimity on those choices, without the outcome, imposes less restraint, so a fortiori the only possible social welfare functions remain imposed or dictatorial (p. 89). (Theorem 3 is not stated in this unit.)

### 6. The decision process as a value (pp. 89–91)
- Social-state variables may include the choice process itself. For example, a person may prefer a distribution reached by the free market over the same one by rationing (pp. 89–90).
- **Hierarchy.** For a state $x$, let $x_1$ be the components that are not decision processes. Let $x_2$ be the process of deciding among alternative $x_1$'s, and $x_n$ the process of deciding among alternative $x_{n-1}$'s. An $n$th-order decision is a process of choosing an $(n-1)$th-order method. A social state is $(x_1,x_2,\dots,x_n,\dots)$. There is no deep circularity (p. 90).
- U.S. example: $x_1$ is a bill together with all existing legislation; $x_2$ is enactment by Congress and President; $x_3$ is choosing Congress and President under the Constitution; $x_4$ is constitutional amendment (p. 90).
- Suppose some $x_n$ is so strongly desired by all that they prefer any state containing it to any state without it (e.g. belief in democracy, or desire for a dictator). Then the social welfare problem may be regarded as solved, since unanimity on process may resolve conflicts on decisions. Footnote 21 cites Rousseau that majority rule itself rests on unanimity at least at the beginning (p. 90).
- Arrow's qualification: people prefer structures partly because they expect, given others' expected behaviour, decisions acceptable to themselves. So we may expect welfare judgments can usually be made when there is both widespread agreement on process and on everyday decisions. Process agreement alone would require incommensurably greater value on process than on outcomes, which "hardly seems" credible for most people (pp. 90–91).

## Toy example (ours)
Five voters, alternatives $a,b,c$, basic strong ordering $a\,S\,b\,S\,c$ (so $B(a,b,c)$). Orderings (best first):
- v1, v2: $a,b,c$; v3: $b,c,a$; v4, v5: $c,b,a$.

Each is single-peaked on $S$ (peak at $a$, $b$ or $c$, falling off away from it), and $N=5$ is odd.
- $a$ vs $b$: $a$ is preferred by v1, v2 (2 votes); $b$ by v3, v4, v5 (3). So $N(b,a)=3>N(a,b)=2$.
- $b$ vs $c$: $b$ by v1, v2, v3 (3); $c$ by v4, v5 (2). $b$ wins.
- $a$ vs $c$: $a$ by v1, v2 (2); $c$ by v3, v4, v5 (3). $c$ wins.

So majority gives $b$ over $c$ over $a$: transitive, with no cycle. Median of first choices ($a,a,b,c,c$ along $S$) is $b$, the Condorcet winner, as Black's shortcut says (p. 80).

## Concepts
- [[single-peaked-preferences]] — all individual orderings are single-peaked on one strong ordering of alternatives; first choices may differ (p. 77)
- [[median-voter-theorem]] — Black's shortcut: social choice is the median of first choices on the basic ordering; Arrow states it as a remark, not a theorem (p. 80)
- [[cycling-intransitivity]] — the example of the "paradox of voting" from Chapter I (not described in this unit; usually a cyclical-majority case); it is not single-peakable (p. 80). Note this differs from the canon's "paradox of voting" about decisiveness.
- [[strategic-sophisticated-voting]] — misrepresenting an ordering to get a better final result in successive votes (fn. 8, p. 80)
- [[agenda-control-agenda-setter]] — the order of motions affects which alternative wins (fn. 8, pp. 80–81; Arrow does not use the term)
- [[strong-ordering-betweenness]] (new) — Definitions 11–12: a "less than"-type order and the relation $B(x,y,z)$ (p. 77)
- [[general-will-moral-imperative]] (new) — the idealist deeper individual ordering, same in all, as against the pragmatic/overt one (pp. 81–83)
- [[social-decision-vs-social-end]] (new) — alternatives read as government decisions or as full descriptions of individuals' states (p. 87)
- [[partial-unanimity-quasi-ordering]] (new) — agreement on some pairs only; does not escape the impossibility result (p. 89)
- [[decision-process-as-value]] (new) — the hierarchy $x_1,x_2,\dots$ of decisions and decision processes (p. 90)
- [[institutions]] — process-agreement (a stable political structure) plus agreement on outcomes supports welfare judgments (pp. 90–91)

## Canonical instances
- [[prewar-european-party-spectrum]] — Left–Right ordering gives single-peaked preferences (p. 76)
- [[hours-of-work-example]] — a one-number alternative with a utility peak (p. 76)
- [[two-voter-even-counterexample]] — shows oddness is essential in Theorem 4 (p. 80)
- [[committee-misrepresentation-example]] — successive motions with sincere voting that is not optimal for individual 1 (fn. 8, pp. 80–81)
- [[aspirin-price-ratio]] — ignorance of instrumental means produces different preferences (p. 87)
- [[dobb-lerner-debate]] — consumers' preferences versus a collectively chosen optimum (p. 84)
- [[us-government-decision-hierarchy]] — bill, enactment, choice of Congress/President, amendment (p. 90)

## Bridges (candidates)
- [structural-analogy] Pooling individuals as experts on the moral imperative ↔ Condorcet jury theorem: both treat voting as estimating a common truth. Arrow says the probability implications are not worked out (fn. 25, p. 85).
- [same-math] Theorem 4's median shortcut ↔ median voter theorem: the same median-of-first-choices result on a one-dimensional ordering.
- [structural-analogy] Decision-process hierarchy $x_1,x_2,\dots$ ↔ institutions as rules about making rules: constitutional levels (pp. 89–90).
- [structural-analogy] Footnote 8's profitable misrepresentation ↔ strategic voting and agenda control.

## Questions this raises
- Is single-peakedness plausible for political issues with more than one dimension? Arrow shows only one-dimensional examples (pp. 75–76).
- If consensus must exist, how could it be measured empirically? Arrow reports that Knight evidently relies on "special techniques", but these pages do not say what they are (pp. 83–84).
- When does the decision process itself get such overriding value in practice? Arrow doubts it does for most people (p. 91).
- Does a dictator or elite distort the "expertness" of its members, and what does this imply for pooling-opinion models (p. 86)?

## Reading notes
- Printed page = pdf − 11. The unit runs from pdf 85 (printed 74) to pdf 102 (printed 91). Printed 92 is blank.
- The text layer was empty; everything here is read from the page images. Footnote 8's ordering for individual 2 is read as $y,x,z$.
- Condition 1, Definition 9, Axioms I–II, Lemma 3 and Theorem 3 come from earlier chapters and are not stated here. Condition 1 is not stated here; that it covers all sets of individual orderings is my inference from the wording of Condition 1'' (p. 77).
- "Paradox of voting" here refers to the Chapter I example mentioned on p. 80; these pages do not describe it (that it is a cyclical-majority case is my gloss).
