---
id: arrow-1951-socialchoice/ch05-v
work: arrow-1951-socialchoice
unit: "5 Chapter V. The General Possibility Theorem for Social Welfare Functions"
pages: 46-60
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
# The General Possibility Theorem for Social Welfare Functions

## L0 — One line
With at least three alternatives that individuals may rank in any way, no social welfare function that gives a social ordering and satisfies Conditions 2 and 3 can avoid being imposed or dictatorial.

## L1 — The gist (≤ 120 words)
Can a rule turn individual rankings into one rational social ranking while respecting individual wishes? For two alternatives, majority decision works. With at least three alternatives that people may rank in any way, Arrow proves that any rule giving a social ordering and satisfying Conditions 2 and 3 (raising an option never hurts it; the choice between two depends only on rankings of those two) must be imposed (ignores tastes) or dictatorial (one person's strict preferences always prevail). The proof builds "decisive sets" of individuals and derives a contradiction from a smallest one. If nothing is assumed about individual orderings, voting schemes, however complicated, and the market do not escape. Arrow proposes keeping the other conditions but restricting admissible individual orderings.

**Prerequisites:** weak orderings (connected, transitive); strict preference P and indifference I; basic set notation; proof by contradiction. Conditions 1–5 come from earlier chapters.

## L2 — Key ideas (5–10 bullets)
- With two alternatives, majority decision satisfies Conditions 1–5 (Condition 1 in its altered two-alternative form), so a possibility result exists (Theorem 1, p. 48).
- Majority decision satisfies Conditions 2–5 for any number of alternatives. It fails only Condition 1 (transitivity) when there are more than two (Lemma 3, p. 48).
- A set of individuals is *decisive* for x against y if its unanimous preference for x over y forces society to prefer x, whatever else people prefer. This is a property of the rule, not of a profile (Def. 10, p. 52).
- Decisiveness spreads: one profile showing a set winning is enough (Cons. 2), the whole society is decisive (Cons. 3), and a single decisive person would be decisive over every pair (Cons. 4, used in the proof of Cons. 5, pp. 54–57).
- Choosing a smallest decisive set and splitting society into three blocks yields a contradiction, which proves Theorem 2 (pp. 57–59).
- Arrow reads Theorem 2 as saying that, if no prior assumptions are made about the nature of individual orderings, no voting method (plurality voting, or any scheme of proportional representation however complicated) removes the paradox of voting, and the market mechanism does not create a rational social choice (p. 59).
- Conditions 1 and 3 together exclude interpersonal utility comparison. Arrow keeps that exclusion and the "satisfactory" conditions, and proposes to relax the wide-domain requirement (pp. 59–60).

## L3 — Walkthrough

### 1. The number of alternatives (pp. 46–48)
Earlier examples (Ch. III §6, Ch. IV) suggest strongly that it will be very difficult to build a function meeting Conditions 1–5. With two alternatives it is possible, so Condition 1 is altered for that case: every set of individual orderings of the two alternatives must give a social ordering (p. 46).

**Definition 9.** Majority decision is the social welfare function (SWF) with $x R y$ iff the number of individuals with $x R_i y$ is at least the number with $y R_i x$ (p. 46). With $N(x,y)$ the number with $x R_i y$:
$$x R y \iff N(x,y) \ge N(y,x) \tag{1}$$

Proof that, for two alternatives, majority decision satisfies Conditions 1–5 (pp. 46–48):
- **Condition 1.** Either $N(x,y)\ge N(y,x)$ or the reverse, so $R$ is connected (2). For transitivity, suppose $xRy$ and $yRz$. With two alternatives, two of $x,y,z$ coincide. The conclusion $xRz$ is trivial if $x=y$ or $y=z$. If $x=z$, it means $xRx$, i.e. $N(x,x)\ge N(x,x)$, which is true. So $R$ is a weak ordering (3) (pp. 46–47).
- **Condition 2.** Suppose $xPy$, so $N(x,y)>N(y,x)$ (4). Take new orderings with $xR_iy \Rightarrow xR_i'y$ (5) and $xP_iy\Rightarrow xP_i'y$ (6). If $yR_i'x$, then not $xP_i'y$, hence not $xP_iy$, hence $yR_ix$ (7). So $N'(x,y)\ge N(x,y)$ and $N(y,x)\ge N'(y,x)$. With (4), $N'(x,y)>N'(y,x)$, i.e. $xP'y$ (p. 47).
- **Condition 3** is trivial: the only set with more than one member is the whole universe of two (p. 47).
- **Condition 4.** If $yP_ix$ for all $i$, then nobody has $xR_iy$, so $N(y,x)\ge N(x,y)$ but not $N(x,y)\ge N(y,x)$. By (1), $yPx$, hence not $xRy$. So $xRy$ is not independent of the individual orderings (p. 47).
- **Condition 5.** Suppose $xP_1y$ and $yP_ix$ for $i\neq1$. Then $N(x,y)=1\le N(y,x)$, so $yRx$ and not $xPy$. So no dictator exists (pp. 47–48).

**Theorem 1.** With two alternatives, majority decision is an SWF satisfying Conditions 2–5 and gives a social ordering for every set of individual orderings (p. 48). Arrow remarks that it is, in a sense, the logical foundation of the Anglo-American two-party system (p. 48).

The proofs for Conditions 2, 4, 5 did not use "two alternatives". Condition 3 also holds for any number: $xRy$ depends only on individuals' relative placement of $x$ and $y$, and $C(S)$ is fixed by $xRy$ for pairs in $S$. **Lemma 3:** for any space of alternatives, majority decision is an SWF satisfying Conditions 2–5 (p. 48). The paradox of voting (Ch. I) shows it fails Condition 1 with more than two alternatives. Condition 1 is henceforth taken in its original form (p. 48).

*Intuition note.* With two options a majority comparison cannot cycle, so majority rule gives a proper ranking. With more than two options, majority decision does not satisfy Condition 1 (the paradox of voting, p. 48).

### 2. Two individuals and three alternatives (pp. 48–51)
Arrow supposes an SWF satisfying Conditions 1–5 exists and derives a contradiction. Alternatives are $x,y,z$; $x',y'$ range over them; individuals 1, 2 have orderings $R_1,R_2$. Arrow assumes there is no a priori reason to suppose individuals will not order the alternatives in any given way; he gives an example where each may order them in any logically possible manner (p. 49).

**Consequence 1.** If $x'P_1y'$ and $x'P_2y'$, then $x'Py'$ (p. 49). *Proof:* By Condition 4 there are orderings with $x'P'y'$. Raise $x'$ to the top of each ordering, keeping the others' relative order. By Condition 2, still $x'P''y'$. Both now prefer $x'$ to $y'$. By Condition 3 the choice depends only on the two individuals' rankings of $x',y'$, whatever the third alternative's rank (p. 49).

**Consequence 2.** Suppose that for some $x',y'$, whenever $x'P_1y'$ and $y'P_2x'$, society has $x'Py'$. Then whenever $x'P_1y'$, $x'Py'$ (p. 49). *Proof:* Take $R_1'=R_1$ with $x'P_1'y'$. Derive $R_2'$ from $R_2$ by pushing $x'$ to the bottom, so $y'P_2'x'$ and, by hypothesis, $x'P'y'$. $R_1,R_2$ differ from $R_1',R_2'$ only by $x'$ being higher on 2's scale. Condition 2 then gives $x'Py'$ (pp. 49–50).

**Consequence 3.** If $x'P_1y'$ and $y'P_2x'$, then $x'Iy'$ (p. 50). Opposed interests mean social indifference.
*Proof* (by contradiction; the case $y'Px'$ is symmetric), taking $x'=x$, $y'=y$. Suppose
$$\text{whenever } xP_1y \text{ and } yP_2x,\ xPy \tag{1}$$
Then (all steps use Consequence 1, Condition 3, and transitivity of $R$) (pp. 50–51):
- $R_1$: $x,y,z$; $R_2$: $y,z,x$. By (1) $xPy$. Both prefer $y$ to $z$, so $yPz$. Hence $xPz$, giving: whenever $xP_1z$ and $zP_2x$, $xPz$ (2).
- $R_1$: $y,x,z$; $R_2$: $z,y,x$. Then $yPx$ and, by (2), $xPz$, so $yPz$ (3: whenever $yP_1z$, $zP_2y$, $yPz$).
- $R_1$: $y,z,x$; $R_2$: $z,x,y$. Then $zPx$ and, by (3), $yPz$, so $yPx$ (4).
- $R_1$: $z,y,x$; $R_2$: $x,z,y$. Then $zPy$ and, by (4), $yPx$, so $zPx$ (5).
- $R_1$: $z,x,y$; $R_2$: $x,y,z$. By (5) $zPx$ and $xPy$ by Consequence 1, so $zPy$ (6).

By Consequence 2, (1) gives: whenever $xP_1y$, $xPy$. Likewise (1)–(6) give it for every pair, so individual 1 is a dictator (Def. 6). Condition 5 forbids this, so (1) is false (p. 51).

**Contradiction.** Let $R_1$: $x,y,z$ and $R_2$: $z,x,y$. By Consequence 1, $xPy$ (7). Since $yP_1z$, $zP_2y$, Consequence 3 gives $yIz$ (8). So $xPz$. But also $xP_1z$ and $zP_2x$ (added step: this is what the text's "$xPz$, $zPx$" records), so $xIz$ by Consequence 3. This is impossible (p. 51).

*Intuition note.* With two people the conditions force: agreement means social agreement, and total disagreement means social indifference. Chaining these through three alternatives eventually makes $x$ both better than and equal to $z$.

### 3. Proof of the General Possibility Theorem (pp. 51–59)
Assume an SWF satisfying Conditions 1–5; wlog the universe is three alternatives, all individual orderings admissible. $V$ denotes a set of individuals, $V'$ a single individual, $V''$ everyone (p. 51).

**Definition 10.** $V$ is *decisive for $x$ against $y$* ($x\neq y$) if $xPy$ for all admissible individual orderings with $xP_iy$ for all $i$ in $V$ (p. 52). Society then prefers $x$ whenever all of $V$ do, whatever anyone thinks of other alternatives. A set may be decisive for $x$ against $y$ without being decisive for $y$ against $x$. Senate example: any 64 senators are decisive for acceptance against rejection, any 33 for rejection against acceptance (p. 52). Decisiveness belongs to the SWF, not to actual orderings (p. 52).

**Consequence 1** (this section's numbering). If $xR_iy\Rightarrow xP_i'y$ for all $i$, and $xPy$, then $xP'y$ (p. 52). It extends Condition 2. *Proof* (pp. 52–53): Let $z$ be the third alternative. Define $R_i''$ by moving $z$ to the bottom of $R_i$:
$$x'R_i''y' \iff (x'R_iy' \text{ and } x'\neq z) \text{ or } y'=z \tag{1}$$
$R_i''$ is an ordering and orders $x,y$ as $R_i$ does (2). By Condition 3, $C([x,y])=C''([x,y])$. Since $xPy$, $C([x,y])=\{x\}$, so $xP''y$ (3). Define $R_i^*$ from $R_i'$ the same way (4). Then $yP_i''z$, $yP_i^*z$, so for $x',y'\neq x$, $x'R_i''y'\iff x'R_i^*y'$ (5). Also $xP_i''z$, $xP_i^*z$. If $xR_i''y$ then $xR_iy$, so by hypothesis $xP_i'y$, so $xP_i^*y$ by (4). Hence $xR_i''y'\Rightarrow xR_i^*y'$ (6) and $xP_i''y'\Rightarrow xP_i^*y'$ (7). By (5)–(7) and (3), Condition 2 gives $xP^*y$. By (4) and Condition 3, $C^*([x,y])=C'([x,y])$, so $xP'y$. Q.E.D.

**Consequence 2.** If some profile has $xP_iy$ for $i$ in $V$, $yP_ix$ for $i$ not in $V$, and the outcome is $xPy$, then $V$ is decisive for $x$ against $y$ (p. 53). *Proof:* Take any $R'$ with $xP_i'y$ for $i$ in $V$ (8). Then $xP_i'y$ whenever $xR_iy$, since those $i$ are all in $V$. Consequence 1 gives $xP'y$ (pp. 53–54). So an observer who sees one profile where $V$ prefers $x$, the rest prefer $y$, and society ranks $x$ higher, may conclude that $V$ is decisive (p. 54).

**Consequence 3.** For every $x$ and $y$ with $x\neq y$, $V''$ is decisive for $x$ against $y$ (p. 54). *Proof:* Condition 4 (with $x,y$ interchanged) gives a profile with not $yRx$, so $xPy$ (9). For any profile with $xP_i'y$ for all $i$ (10), Consequence 1 gives $xP'y$. Hence $V''$ is decisive, via Consequence 2 (p. 54).

**Consequence 4.** For distinct $x,y,z$: if $V'$ is decisive for $x$ against $y$ or for $y$ against $z$, then $V'$ is decisive for $x$ against $z$ (p. 54). (Single individual 1.) (pp. 55–56)
- (a) Let $xP_1y$ (11), $yP_iz$ for all $i$ (12), $zP_ix$ for $i\ne1$ (13). Decisiveness gives $xPy$ (14). Consequence 3 gives $yPz$ (15). Transitivity gives $xPz$ (16). Also $xP_1z$ (17), and $zP_ix$ for $i\neq 1$ (18). By Consequence 2, $V'$ is decisive for $x$ against $z$.
- (b) Let $xP_iy$ for all $i$ (19), $yP_1z$ (20), $zP_ix$ for $i\ne1$ (21). Then $xPy$ by Consequence 3, $yPz$ by decisiveness. So $xPz$ and $xP_1z$. With (21), Consequence 2 gives the result.

So a person decisive for $x$ against some alternative is decisive for $x$ against any alternative, and one decisive for some alternative against a given $z$ is decisive for any alternative against $z$ (pp. 54–55).

**Consequence 5.** For every pair $x,y$ and every one-member set $V'$, $V'$ is not decisive for $x$ against $y$ (p. 56). *Proof* (pp. 56–57): Suppose it is. For any $y'$ distinct from $x$ and $y$, Consequence 4 makes $V'$ decisive for $x$ against $y'$; also for $y'=y$ (22). Fix $y'\ne x$ and take $x'$ distinct from $x,y'$ (possible by Condition 1). Consequence 4 gives: $V'$ decisive for $x'$ against $y'$; by (22) this also holds if $x'=x$ (23). Choose $x'\ne x$ and $y''$ distinct from $x,x'$. Substituting in Consequence 4, $V'$ is decisive for $x'$ against $x$ (24). So $V'$ is decisive for any $x'$ against any $y'$ (25). By Def. 10 and Def. 6 the SWF is dictatorial, excluded by Condition 5.

**The final contradiction** (pp. 57–59). Let $S=\{x,y,z\}$. By Consequence 3, each of the six ordered pairs has a decisive set. Among all sets decisive for some pair, pick $V_1$ with the fewest members, $k$. Label so that $V_1$ is decisive for $x$ against $y$ (26). Every set decisive for some pair has at least $k$ members (27). Number individuals: $V'=\{1\}$, $V_2=\{2,\dots,k\}$ ($k-1$ members), $V_3=\{k+1,\dots,n\}$ (may be empty). So $V_2$ is decisive for nothing (28), and $V'$ is decisive for nothing, by Cons. 5 (29). Take a profile:
$$V':\ xP_iy,\ yP_iz \tag{30}$$
$$V_2:\ zP_ix,\ xP_iy \tag{31}$$
$$V_3:\ yP_iz,\ zP_ix \tag{32}$$
Then $xP_iy$ for all $i$ in $V_1$, so $xPy$ (33). By transitivity, $zP_iy$ for all $i$ in $V_2$ (34), and $yP_iz$ for all $i$ not in $V_2$ (35). If $zPy$, Consequence 2 would make $V_2$ decisive for $z$ against $y$, contradicting (28). So not $zPy$, i.e. $yRz$ (36). Since $R$ is a weak ordering, (33) and (36) give $xPz$ (37). By transitivity $xP_iz$ for $i$ in $V'$ (38), and $zP_ix$ for $i$ not in $V'$ (39). Consequence 2 makes $V'$ decisive for $x$ against $z$, contradicting (29). (p. 58)

**Result.** If an SWF satisfies Conditions 2 and 3 and Condition 1 holds, then Condition 4 or Condition 5 is violated (pp. 58–59). **Theorem 2 (General Possibility Theorem):** if there are at least three alternatives which members of society may order in any way, then every SWF satisfying Conditions 2 and 3 and yielding an ordering satisfying Axioms I and II must be imposed or dictatorial (p. 59). Arrow says Theorem 2 shows that, if no prior assumptions are made about the nature of individual orderings, no method of voting removes the paradox of voting discussed in Ch. I, neither plurality voting nor any scheme of proportional representation, no matter how complicated; similarly, the market mechanism does not create a rational social choice (p. 59). Footnote: the negative outcome is reminiscent of the intransitivity of domination in multi-person games (p. 59, n. 1).

*Intuition note.* Take a smallest group that can always get its way. Splitting society into that group's first member, the rest of the group (too small to be decisive) and everyone else, with a cyclic profile, makes the first member alone decisive for $x$ against $z$. That is impossible by Consequence 5, so the assumed conditions are inconsistent.

### 4. Interpretation (pp. 59–60)
Conditions 1 and 3 together exclude interpersonal comparison of utility, by direct measurement or by comparison with other social states (Arrow cites arguments from Ch. II) (p. 59). Restated: if interpersonal comparisons are excluded, the only methods of passing from individual tastes to social preferences that are satisfactory and defined for a wide range of sets of orderings are imposed or dictatorial. "Satisfactory" means not reflecting desires negatively (Condition 2) and yielding an ordering with the usual properties of rationality (Condition 1 and Axioms I, II) (p. 59). Arrow also phrases the result, in view of Chapter III's interpretations of the conditions: if consumers' values can be represented by a wide range of individual orderings, the doctrine of voters' sovereignty is incompatible with that of collective rationality (p. 60). To keep non-imposed, non-dictatorial judgments, some condition must be relaxed. Arrow will keep the exclusion of interpersonal comparison and the "satisfactory" conditions, and drop only the requirement that the method work for a wide range of orderings: individual orderings are assumed to satisfy restrictions stricter than Condition 1. The rest of the essay examines this (p. 60). Footnote 2: of the "satisfactory" conditions, the only part that seems to Arrow to be at all in dispute is the assumption of rationality; the consequences of dropping it are so radical that it seems worthwhile to explore maintaining it (p. 60).

## Toy example (ours, not from the text)
Three voters, $n=3$, alternatives $x,y,z$, majority decision (Def. 9). Use the profile pattern of (30)–(32): voter 1 ($V'$): $x>y>z$; voter 2 ($V_2$): $z>x>y$; voter 3 ($V_3$): $y>z>x$. Here $V_1=\{1,2\}$, $k=2$.
- $x$ vs $y$: voters 1 and 2 prefer $x$, voter 3 prefers $y$. $N(x,y)=2\ge N(y,x)=1$, so $xPy$. This matches (33).
- $y$ vs $z$: voters 1 and 3 prefer $y$, voter 2 prefers $z$. $2$ vs $1$, so $yPz$. In the proof one only had $yRz$ (36).
- $z$ vs $x$: voters 2 and 3 prefer $z$, voter 1 prefers $x$. $2$ vs $1$, so $zPx$.
- So $xPy$, $yPz$, $zPx$: a cycle; $R$ is not transitive. The proof's step (37), $xPz$, fails, so Condition 1 is violated. By Lemma 3, majority decision satisfies Conditions 2–5, so Theorem 2 predicts exactly this.

## Concepts
- [[social choice function / social welfare function]] — here an SWF maps each set of individual orderings to one social ordering $R$ (pp. 46–48).
- [[arrow's impossibility theorem]] — here Theorem 2: at least three freely ordered alternatives, Conditions 2–3 plus ordering, forces imposed or dictatorial (p. 59).
- [[independence of irrelevant alternatives (IIA)]] — Condition 3: the social choice from $S$ depends only on individual orderings within $S$ (pp. 47, 49).
- [[paradox of voting]] — cited as showing majority decision violates Condition 1 for more than two alternatives (p. 48).
- [[cycling / intransitivity]] — majority decision does not satisfy Condition 1 with more than two alternatives (p. 48); since its $R$ is always connected (p. 46), the failure is one of transitivity (added step).
- decisive set (new) — a set $V$ whose unanimous strict preference for $x$ over $y$ forces $xPy$ in every admissible profile in which all of $V$ strictly prefer $x$ to $y$ (p. 52).
- positive association (new) — Condition 2: raising $x$ in individual rankings cannot hurt $x$ socially (pp. 47, 52).
- imposed / dictatorial (new) — imposed = Condition 4 violated (some $xRy$ holds independent of the individual orderings, p. 47); dictatorial = Condition 5 violated (one person's strict preference always becomes the social preference, pp. 56, 59).
- interpersonal comparison of utility (new) — excluded by Conditions 1 and 3 together (p. 59).

## Canonical instances
- [[majority-decision-two-alternatives]] — satisfies Conditions 1–5, Theorem 1 (p. 48).
- [[senate-treaty-ratification]] — 64 senators decisive for acceptance, 33 for rejection (p. 52).
- [[paradox-of-voting-chapter-one]] — the Chapter I example, cited on p. 48 as showing that majority decision violates Condition 1 for more than two alternatives (the example itself is not in these pages).

## Bridges (candidates)
- [structural-analogy] Decisive sets ↔ political science: winning coalitions — a coalition whose agreement is enough to fix the outcome.
- [metaphor] Dictator ↔ political science: agenda control — one actor decides regardless of others.
- [metaphor] Arrow's footnote on intransitivity of domination ↔ game theory: intransitive dominance in multi-person games.

## Questions this raises
- How restricted must individual orderings be for a non-imposed, non-dictatorial SWF to exist (the programme announced on p. 60)?
- Which of Conditions 1–5 is least defensible in practice? Arrow says that, among the "satisfactory" conditions, only rationality seems to him at all in dispute (p. 60, n. 2).
- Does the exclusion of interpersonal comparison, which is built into Conditions 1 and 3, drive the result?
- What changes if there are infinitely many individuals or alternatives? (The proof picks a decisive set with the fewest members, p. 57.)

## Reading notes
- Printed = pdf − 11. All page references are printed pages.
- Conditions 1–5, Axioms I–II, Definitions 1–8 and Lemmas 1–2 are stated in earlier chapters and are not in these pages.
- Consequences 1–3 of Section 2 (two individuals) are different results from Consequences 1–3 of Section 3, which has Consequences 1–5.
- The statement of Consequence 2 in Section 2 (p. 49) is printed with some primes missing. The proof makes the intended primed form clear.
- On p. 51, just after (8), the text's "$xPz$, $zPx$" evidently refers to $xP_1z$, $zP_2x$ (see the added step in Section 2). On p. 58 the text says $V_2$ would be "decisive for $y$ against $z$" after supposing $zPy$; the digest writes "$z$ against $y$", which is what Consequence 2 gives.
- Text layers were mostly empty. All content was read from the page images.
