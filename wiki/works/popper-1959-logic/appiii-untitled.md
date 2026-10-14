---
id: popper-1959-logic/appiii-untitled
work: popper-1959-logic
unit: Appendix *iii — On the Heuristic Use of the Classical Definition of Probability, Especially for Deriving the General Multiplication Theorem
pages: 325-328
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Appendix *iii — Heuristic use of the classical definition of probability

## L0 — One line
Popper uses the classical "favourable over possible" definition, extended to weighted cases, to motivate the general multiplication theorem $p(ab,c)=p(a,bc)\,p(b,c)$, and says that a formal treatment must start from an axiom system, not a definition, and that the theorem may be adopted as an axiom where $p(a,b)$ is to be meaningful even if $p(b)=0$.

## L1 — The gist (≤ 120 words)
Popper asks what use the classical definition of probability (favourable cases divided by equally possible cases) still has, given that it fails for biased dice. His answer is that it works as a heuristic: any satisfactory definition must agree with it wherever it applies. Adding weights (probabilities) to the cases gives a rule for "probability of a, given b". From this rule he heuristically derives the multiplication theorems for absolute and relative probability. Because the weights are practically the same as probabilities, the result can no longer be regarded as a proper definition. A formal treatment must start from an axiom system, and, if $p(a,b)$ is to be meaningful even when $p(b)=0$, the theorem may be adopted as an axiom.

**Prerequisites:** basic probability (sums of exclusive cases); the idea of a conditional probability; reading simple formulas.

## L2 — Key ideas (5–10 bullets)
- The classical definition cannot handle unequal weights, but every satisfactory definition must agree with it where it applies, so it has heuristic value (p. 325).
- Five kinds of case where it applies or helps: equal weights conjectured, problems transformable to equal weights, weight functions, over-simplified estimates near 0 or 1, and weights given as probabilities (pp. 325–326).
- Weighted rule: required probability = sum of probabilities of favourable cases ÷ sum of probabilities of possible cases (p. 326).
- The same rule holds for non-exclusive cases if sums are replaced by probabilities of disjunctions (p. 326).
- The die example is the same problem as finding $p(a,b)$, which gives, assuming $p(b)\neq 0$, $p(a,b)=p(ab)/p(b)$, and the more general form $p(ab)=p(a,b)\,p(b)$ (pp. 326–327).
- Substituting $bc$ for $b$ gives the relative multiplication theorem (3) (p. 327).
- Formalizing needs an axiom system, not a definition, and gives (3) at best with the proviso $p(c)\neq 0$ (p. 328).
- If an axiom system makes $p(a,b)$ meaningful even when $p(b)=0$, one may adopt (3) as an axiom, with the derivation as heuristic justification (p. 328).

## L3 — Walkthrough

**Opening: why the old definition still matters (p. 325).**
- Classical definition: probability = number of favourable cases ÷ number of equally possible cases (p. 325).
- Drawback: it fits homogeneous or symmetrical dice, not biased ones, because it has no room for unequal weights (p. 325).
- Heuristic value: a satisfactory definition must agree with it where the weight difficulty can be overcome, and a fortiori where it is already applicable (p. 325).

**Cases (1)–(5), where it is applicable or useful (pp. 325–326).**
1. Whenever we conjecture equal weights, equal possibilities and so equal probabilities (p. 325).
2. Whenever the problem can be transformed to give equal weights, possibilities or probabilities (p. 325).
3. With slight modifications, whenever a weight function can be assigned to the possibilities (p. 326).
4. In most cases where an over-simplified equal-possibility estimate leads to a solution approaching probability zero or one, it is applicable or of heuristic value (p. 326).
5. It has great heuristic value where weights can be introduced as probabilities (p. 326).

*Worked example (5), p. 326.* Throw a die. Count an even number as success. A six counts as "no throw".
- Fair die, classical definition: $2/5$ (p. 326).
- Biased die with given unequal $p(1),\dots,p(6)$:
$$\frac{p(2)+p(4)}{p(1)+p(2)+p(3)+p(4)+p(5)}=\frac{p(2)+p(4)}{1-p(6)}$$
(p. 326).
- Rule obtained: given the probabilities of all (mutually exclusive) possible cases, the required probability is the sum of the probabilities of the favourable cases divided by the sum of the probabilities of the possible cases (p. 326).
- For exclusive or non-exclusive cases: the required probability is the probability of the disjunction of all favourable cases divided by the probability of the disjunction of all possible cases (p. 326).

*Intuition note.* Counting cases is replaced by adding their weights. The "possible cases" form a smaller world, here "not a six", and you ask what share of that world is favourable.

**(6) Heuristic derivation of relative probability and the multiplication theorem (pp. 326–327).**
- Let $a$ = "even" and $b$ = "other than a six". The problem is then to find $p(a,b)$, the probability of $a$ given $b$, or of finding an $a$ among the $b$'s (p. 326).
- Write $p(ab)$ for $p(2)+p(4)$. Write $p(b)$ for $p(1)+\dots+p(5)$, which equals $1-p(6)$ (p. 327).
- Assuming $p(b)\neq 0$:
$$p(a,b)=p(ab)/p(b)\tag{1}$$
(p. 327).
- The more general form, meaningful even if $p(b)=0$:
$$p(ab)=p(a,b)\,p(b)\tag{2}$$
This is the general multiplication theorem for the absolute probability of a product $ab$ (p. 327).
- Substitute $bc$ for $b$ in (2): $p(abc)=p(a,bc)\,p(bc)$ (p. 327).
- Apply (2) to $p(bc)$: $p(abc)=p(a,bc)\,p(b,c)\,p(c)$ (p. 327).
- Assuming $p(c)\neq 0$: $p(abc)/p(c)=p(a,bc)\,p(b,c)$ (p. 327).
- By (1) the left side is $p(ab,c)$, so
$$p(ab,c)=p(a,bc)\,p(b,c)\tag{3}$$
This is the general multiplication theorem for the relative probability of a product $ab$ (p. 327).
- Footnote: Popper omits brackets round $bc$ because his interest is heuristic. The law of association is treated in the next two appendices (p. 327).

*Intuition note.* "$a$ and $b$ given $c$" is built in two steps: first $b$ given $c$, then $a$ given both $b$ and $c$. Multiplying the two step-probabilities gives the joint one.

**(7) From heuristic to formal (p. 328).**
- The derivation can be formalized, but the proof must start from an axiom system, not a definition (p. 328).
- Reason: the heuristic step put weighted possibilities, which are practically probabilities, into the classical definiens (the defining part). The result cannot be a proper definition. It must establish relations between probabilities, which amounts to constructing an axiom system (p. 328).
- The derivation uses the laws of association and of addition of probabilities implicitly, so the axiom system needs rules for them. Popper's example is the system for absolute probabilities in appendix *ii (p. 328).
- A formal derivation of (3) gives it at best with the condition "provided $p(c)\neq 0$" (p. 328).
- (3) may be meaningful without that proviso if the axiom system makes $p(a,b)$ meaningful even when $p(b)=0$. In a theory of that kind, (3) cannot be derived this way. Instead, adopt (3) as an axiom, with this derivation (and formula (1) of the old appendix ii) as its heuristic justification. This is done in appendix *iv (p. 328).

## Toy example (ours)
Biased die: $p(1)=0.1,\ p(2)=0.2,\ p(3)=0.1,\ p(4)=0.3,\ p(5)=0.1,\ p(6)=0.2$. Sum $=1.0$.
- $a$ = even, $b$ = not six. $p(ab)=p(2)+p(4)=0.5$. $p(b)=1-0.2=0.8$.
- Formula (1): $p(a,b)=0.5/0.8=0.625$. Check with (2): $0.625\times0.8=0.5=p(ab)$.
- Check (3) with $c$ = "not a one": $p(c)=0.9$. $bc=\{2,3,4,5\}$, so $p(bc)=0.7$. $abc=\{2,4\}$, so $p(abc)=0.5$.
- Left side: $p(ab,c)=0.5/0.9\approx0.556$.
- Right side: $p(a,bc)\,p(b,c)=(0.5/0.7)(0.7/0.9)=0.5/0.9$. They agree.

## Concepts
- [[classical-definition-of-probability]] (new) — favourable cases ÷ equally possible cases; fails for unequal weights (p. 325)
- [[weighted-possibilities]] (new) — cases carrying unequal probabilities; practically the same as probabilities (pp. 326, 328)
- [[relative-probability]] (new) — $p(a,b)$: probability of $a$ given $b$, or of finding an $a$ among the $b$'s (p. 326)
- [[general-multiplication-theorem]] (new) — (2) for absolute and (3) for relative probability of a product (p. 327)
- [[heuristic-vs-formal-derivation]] (new) — a heuristic derivation motivates a result; a formal one needs an axiom system (p. 328)
- [[axiom-system-for-probability]] (new) — probability relations laid down as axioms, not defined (p. 328)

## Canonical instances
- [[biased-die-even-number-problem]] — even number, sixes counted as "no throw"; $2/5$ for a fair die, $(p(2)+p(4))/(1-p(6))$ for a biased one (p. 326)

## Bridges (candidates)
- [same-math] $p(a,b)=p(ab)/p(b)$ ↔ Bayesian confirmation: $P(H\mid E)$ is the same ratio of joint to marginal probability when $P(E)\neq 0$.
- [structural-analogy] Adopting (3) as an axiom to cover $p(b)=0$ ↔ analytic-philosophy practice of replacing a failed definition by axioms.

## Questions this raises
- Which axioms in appendix *iv make $p(a,b)$ meaningful when $p(b)=0$?
- Why does the weighted rule yield $1-p(6)$? Which axioms of addition and normalization does that step silently use?
- Does Popper's claim that a satisfactory definition must agree with the classical one constrain axiom choice?
- What exactly is lost, when deriving (3) formally, by the proviso $p(c)\neq0$?

## Reading notes
- Printed page = pdf − 29 (pdf 354–357 = printed 325–328).
- The source gives no separate title; the heading is the long title above. Only p. 327 was seen as an image. Its equations (1)–(3) match the text layer.
- Numbered items (1)–(7) are paragraphs. The formula numbers (1)–(3) are separate and share the same digits.
- Popper states $p(b)\neq 0$ for (1) and $p(c)\neq 0$ for the step to (3) (p. 327), and repeats the $p(c)\neq 0$ proviso for the formal derivation (p. 328).
