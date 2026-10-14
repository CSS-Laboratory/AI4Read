---
id: wittgenstein-1922-tractatus/ch06-propositions
work: wittgenstein-1922-tractatus
unit: "6 Propositions 6-7 (with the end of 5.6 and the German Vorwort)"
pages: 75-92
fields: [analytic-philosophy]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# The general form of proposition, logic as tautology, and what cannot be said

## L0 — One line
Every proposition is built by repeated application of one operation to elementary propositions; logic, mathematics and ethics are not further propositions about the world, and what cannot be said shows itself, and of it one must be silent.

## L1 — The gist (≤ 120 words)
The unit asks what logic, number, natural law and value are, given that propositions are truth-functions of elementary ones. Wittgenstein answers that logical propositions are tautologies and say nothing, but show the formal properties of language and world. Mathematical propositions are equations and are pseudo-propositions. The law of causality is the form of a law, not a law. Value and the sense of the world lie outside the world; ethics cannot be expressed; the inexpressible shows itself and is the mystical. Metaphysical sentences contain signs to which no meaning has been given; his own propositions are elucidations, finally recognised as senseless, a ladder to throw away. This matters because it fixes the limit of language and the task of philosophy.

**Prerequisites:** propositional logic (truth tables, ⊃, ∼, tautology); the earlier Tractatus ideas of elementary propositions, truth-functions and the operation N; basic arithmetic.

## L2 — Key ideas (5–10 bullets)
- The general form of proposition is $[\bar p,\bar\xi,N(\bar\xi)]$: every proposition results from successive applications of $N$ to elementary propositions (p. 75).
- Numbers are exponents of an operation (the index showing how often it is repeated, 6.02), and the general form of cardinal number is $[0,\xi,\xi+1]$; class theory is superfluous in mathematics (p. 76).
- Logical propositions are tautologies (propositions true for all truth-combinations of their arguments). They say nothing but show logical properties of propositions; their truth is visible in the symbol alone (pp. 77–79).
- Logic has no surprises, no primitive/derived rank and no empirical basis. Proof in logic is only a mechanical aid for recognising a tautology where it is complicated (pp. 79–81).
- Mathematics is a method of logic. Its equations are pseudo-propositions (they express no thoughts) that show substitutability, e.g. the proof of $2\times2=4$ (pp. 82–83).
- The law of causality is the form of a law, and mechanics fixes a form of description; the sentence *there are natural laws* cannot be said, it shows itself (pp. 84–86).
- Any value that is of value, and the sense of the world, must lie outside the world; ethics cannot be expressed. The mystical is *that* the world is, not how it is (pp. 87–89).
- The right method of philosophy would show anyone who wishes to say something metaphysical that he gave no meaning to certain signs; the book's own propositions are a ladder to be discarded. Proposition 7 closes the book (p. 90).

## L3 — Walkthrough

### End of 5.6: the subject (5.633–5.641)
- **Interlocutor:** the metaphysical subject is like the eye and the field of sight. **Reply:** you do not really see the eye; from nothing in the field of sight can it be concluded that it is seen from an eye (5.633, p. 75).
- No part of our experience is also a priori; everything we see or describe could be otherwise (5.634, p. 75).
- Strictly carried out, solipsism coincides with pure realism. The I shrinks to an extensionless point, and the reality co-ordinated with it remains (5.64, p. 75).
- The philosophical I is not the man or the soul of psychology but the metaphysical subject, the limit of the world, not a part of it (5.641, p. 75).

### 6–6.031: the general form; numbers
- General form of truth-function (= of proposition): $[\bar p,\bar\xi,N(\bar\xi)]$ (6, p. 75). The text layer of p. 75 lost the overbars; I restored them to match 6.01 (image, p. 76).
- It says that every proposition is the result of successive applications of $N'(\bar\xi)$ to the elementary propositions (6.001, p. 75). Given the general form of construction, we also have the general form of passing from one proposition to another (6.002, p. 75).
- $\Omega'(\bar\eta)=[\bar\xi,N(\bar\xi)]'(\bar\eta)\ (=[\bar\eta,\bar\xi,N(\bar\xi)])$, "the most general form of transition from one proposition to another" (6.01, p. 76).
- Numbers (6.02, p. 76):
$$x=\Omega^{0\prime}x\ \text{Def.},\qquad \Omega'\Omega^{\nu\prime}x=\Omega^{\nu+1\prime}x\ \text{Def.}$$
The series $x,\Omega'x,\Omega'\Omega'x,\dots$ is written $\Omega^{0\prime}x,\Omega^{0+1\prime}x,\Omega^{0+1+1\prime}x,\dots$. In place of $[x,\xi,\Omega'\xi]$ he writes $[\Omega^{0\prime}x,\Omega^{\nu\prime}x,\Omega^{\nu+1\prime}x]$. Definitions: $0+1=1$, $0+1+1=2$, $0+1+1+1=3$, and so on.
- A number is the exponent of an operation (6.021). The concept *number* is the variable number, the general form of number; the concept of equality of numbers is the general form of all special equalities of numbers (6.022, p. 76). The general form of cardinal number is $[0,\xi,\xi+1]$ (6.03). The theory of classes is superfluous in mathematics. This is connected with the fact that the generality mathematics needs is not the accidental one (6.031, p. 76).
- *Intuition note:* a proposition is made by one repeatable step, and a number just counts how many times a step is repeated. So the concept *number* is a general form (6.022).

### 6.1–6.127: logic
- Logical propositions are tautologies and say nothing (they are the analytical propositions) (6.1, p. 76; 6.11, p. 77).
- Theories that make a proposition of logic appear substantial are always false. For example, treating "true" and "false" as two properties would make it a remarkable fact that every proposition has one. That would make the proposition look like natural science, which is a symptom of misunderstanding (6.111, p. 77).
- Their mark is that their truth can be perceived in the symbol alone. He adds that this fact embodies the whole philosophy of logic. The truth or falsehood of non-logical propositions cannot be recognised from the propositions alone (6.113, p. 77).
- That the propositions of logic are tautologies shows formal logical properties of language and of the world; that propositions connected in a certain way give a tautology shows that they have certain properties of structure (6.12, p. 77). Examples (6.1201, p. 77): $\sim(p.\sim p)$ shows that $p$ and $\sim p$ contradict each other. $(p\supset q).(p):\supset:(q)$ shows that $q$ follows from $p$ and $p\supset q$. $(x).fx:\supset:fa$ shows that $fa$ follows from $(x).fx$. Contradictions could serve instead of tautologies (6.1202, p. 77).
- **Truth-combination notation (6.1203, pp. 78–79).** For propositions without generality signs: write $TpF$, $TqF$, show truth-combinations by brackets, and connect each to the truth or falsity of the whole by lines (diagrams; see Reading notes). The form $\sim\xi$ is written $T\xi F$ with F and T reversed, and $\xi.\eta$ is a bracket diagram. He asks whether the Law of Contradiction $\sim(p.\sim p)$ is a tautology. For $\sim(p.\sim q)$, put $p$ for $q$ and compare the outermost T/F with the innermost. The truth of the whole is co-ordinated with all truth-combinations of its argument and its falsity with none (p. 79).
- Logical propositions demonstrate logical properties by combining propositions into ones that say nothing: a "zero-method", an equilibrium that shows how they must be constructed (6.121, p. 79). So we can do without them; in an adequate notation we see the properties by inspection (6.122, 6.1221, p. 79).
- Logical propositions cannot be empirically established or refuted (6.1222, p. 79). We can in fact postulate them in so far as we can postulate an adequate notation (6.1223, p. 80). This also explains why logic has been called the theory of forms and of inference (6.1224, p. 80).
- Logical laws obey no further logical laws. Russell was wrong that each type needs its own law of contradiction, since one law is not applied to itself (6.123, p. 80).
- Generality is not the mark of logic: an ungeneralised proposition can be tautologous (6.1231). Logical general validity is essential, as opposed to accidental general validity such as that of *all men are mortal*. Russell's axiom of reducibility is not logical; we can imagine a world where it fails, and logic has nothing to do with that question (6.1232–6.1233, p. 80).
- Logical propositions present the scaffolding of the world and treat of nothing. They presuppose that names have meaning and elementary propositions have sense (6.124, p. 80). In logic it is not we who express what we want by signs; the nature of the essentially necessary signs itself asserts; that is to say, given the logical syntax of a sign language, all its logical propositions are given (6.124, p. 80). It is possible, even in the old logic, to give at the outset a description of all true logical propositions (6.125, p. 80). Hence there can never be surprises in logic (6.1251, p. 81).
- Whether a proposition is logical is decided from the properties of the symbol. We prove a logical proposition by creating it from other logical propositions by successive operations that generate tautologies, using mere symbolic rules; this way of showing that propositions are tautologies is quite unessential to logic, because the propositions the proof starts from must show without proof that they are tautologies (6.126, p. 81). Process and result are equivalent (6.1261); proof is only a mechanical expedient to facilitate recognising a tautology where it is complicated (6.1262, p. 81). It would be too remarkable if a significant proposition could be proved logically from another and a logical proposition too; the logical proof of a significant proposition and proof in logic must be two quite different things (6.1263, p. 81).
- A significant proposition asserts something, and its proof shows that it is so; in logic every proposition is the form of a proof. Every proposition of logic is a modus ponens presented in signs; modus ponens cannot itself be expressed by a proposition (6.1264, p. 81). Logic can always be conceived so that every proposition is its own proof (6.1265, p. 81).
- All logical propositions have equal rank; each shows itself to be a tautology (6.127, p. 81). The number of primitive propositions is arbitrary. Frege's could be joined into one logical product. **Wittgenstein's remark on Frege:** it is remarkable that Frege appealed to self-evidence as the criterion of logic (6.1271, p. 82).
- Logic is not a theory but a reflexion of the world; logic is transcendental (6.13, p. 82).
- *Intuition note:* a tautology is true whatever the facts are, so it tells us nothing about the facts. Its construction nevertheless shows how its parts relate, for instance that one follows from the other.

### 6.2–6.241: mathematics
- Mathematics is a logical method. Its propositions are equations, hence pseudo-propositions, and express no thoughts (6.2–6.21, p. 82). In life we use them only to infer from non-mathematical propositions to others (6.211, p. 82). Equations show the logic of the world as tautologies do (6.22, p. 82).
- "=" means the two expressions can be substituted for one another, and this must show in the expressions themselves (6.23, p. 82). Affirmation can be conceived as double denial; $1+1+1+1$ as $(1+1)+(1+1)$ (6.231, p. 82).
- **Frege says** the expressions have the same meaning but different senses. **Wittgenstein:** what is essential is that we need not show sameness of meaning, since it can be perceived from the expressions (6.232, pp. 82–83). Identity of meaning cannot be asserted, because to assert it I would already have to know whether the meanings agree (6.2322, p. 83). Provability means correctness is seen without comparing with facts (6.2321, p. 83).
- Language supplies the needed intuition, and calculation is not an experiment (6.233–6.2331, p. 83). Mathematics is a method of logic; its essential method is working with equations, on which depends that every proposition of mathematics must be self-intelligible (6.234–6.2341, p. 83). The method by which it arrives at its equations is substitution (6.24, p. 83).
- Proof of $2\times2=4$ (6.241, p. 83), with $(\Omega^\nu)^{\mu\prime}x=\Omega^{\nu\times\mu\prime}x$ Def.:
$$\Omega^{2\times2\prime}x=(\Omega^2)^{2\prime}x=(\Omega^2)^{1+1\prime}x=\Omega^{2\prime}\Omega^{2\prime}x=\Omega^{1+1\prime}\Omega^{1+1\prime}x$$
$$=(\Omega'\Omega)'(\Omega'\Omega)'x=\Omega'\Omega'\Omega'\Omega'x=\Omega^{1+1+1+1\prime}x=\Omega^{4\prime}x.$$

### 6.3–6.375: laws of nature
- Logical research investigates all regularity; outside logic all is accident (6.3, p. 83). The law of induction is a significant proposition, so it is neither logical nor a priori (6.31, p. 84).
- The law of causality is not a law but the form of a law (a class name, as with least action). Russell's note: the form of any law of a certain sort (6.32–6.321, p. 84). We do not believe a priori in a law of conservation, but we know a priori the possibility of a logical form (6.33, p. 84). Causation, continuity and least expenditure are a priori intuitions of possible forms of scientific propositions (6.34, p. 84).
- **Net analogy (6.341–6.343, pp. 84–85).** Cover a white surface with irregular black spots with a fine square net and say of each square that it is white or black. This gives a unified description of arbitrary form; a triangular or hexagonal net would also do. Mechanics determines a form of description in a similar way, by saying that all propositions of the world-description must be obtained in a given way from given mechanical axioms; different nets correspond to different systems of describing the world. That a picture can be described by a net of a given form says nothing about the picture. That it can be completely described by a net of definite fineness does characterise it. So too, that the world can be described by Newtonian mechanics asserts nothing about the world, but that it can be described in the particular way it is described does assert something; and that it can be described more simply by one system of mechanics than by another says something about the world. Mechanics always speaks generally, never of particular material points but only of some points or other; through the whole apparatus of logic, physical laws still speak of the objects of the world (6.3431–6.3432, p. 85).
- Laws like causality treat of the network, not of what it describes (6.35, p. 85). If there were a law of causality, it might run *there are natural laws*; but that clearly cannot be said, it shows itself (6.36, pp. 85–86).
- We cannot compare any process with a passage of time (there is no such thing), only with another process; it is exactly analogous for space (6.3611, p. 86). The Kantian right/left-hand problem already arises in one dimension; a right glove would fit a left hand if turned in four-dimensional space (6.36111, p. 86). What is excluded by causality cannot be described (6.362, p. 86).
- Induction assumes the simplest law that fits experience. It has a psychological, not a logical, foundation (6.363–6.3631, p. 86). That the sun will rise tomorrow is a hypothesis, which means that we do not know whether it will rise (6.36311, p. 87).
- There is only logical necessity, so only logical impossibility (6.37, 6.375, p. 87). To believe that natural laws explain phenomena is an illusion. People stop at natural laws as the ancients did at God and Fate; both are right and wrong, but the ancients were clearer, in so far as they recognised one clear conclusion (6.371–6.372, p. 87). The world is independent of my will (6.373–6.374, p. 87).
- Two colours at one place in the visual field is logically impossible, since colour's logical structure excludes it. The logical product of two elementary propositions is neither tautology nor contradiction; saying a point has two colours is a contradiction (6.3751, p. 87).

### 6.4–6.45: value, ethics, the mystical
- All propositions are of equal value (6.4, p. 87). The sense of the world must lie outside the world; in the world there is no value, or if there were it would be of no value. A value that is of value must lie outside all happening and being-so, because these are accidental, and what makes it non-accidental cannot lie in the world (6.41, pp. 87–88). Hence there are no ethical propositions; ethics is transcendental and one with aesthetics (6.42–6.421, p. 88).
- Ethics has nothing to do with punishment and reward in the ordinary sense; there must be some sort of ethical reward and punishment, but it must lie in the action itself. Of the will as bearer of the ethical we cannot speak (6.422–6.423, p. 88). If good or bad willing changes the world, it can only change the limits of the world, not the facts; the world of the happy is another than that of the unhappy (6.43, p. 88).
- Death is not an event of life. If eternity is understood as timelessness, then he lives eternally who lives in the present (6.4311, pp. 88–89). He says the temporal immortality of the soul is in no way guaranteed and would not do what we wanted of it; he asks whether a riddle is solved by my surviving for ever and whether such eternal life is not as enigmatic as the present one. The solution of the riddle of life lies outside space and time (6.4312, p. 89). How the world is is completely indifferent for what is higher; God does not reveal himself in the world (6.432, p. 89).
- "Not how the world is, is the mystical, but that it is" (6.44, p. 89). The feeling of the world as a limited whole is the mystical feeling (6.45, p. 89).

### 6.5–7: the end
- If an answer cannot be expressed, neither can the question; the riddle does not exist; if a question can be put, it can be answered (6.5, p. 89). Scepticism is not irrefutable but senseless, since it doubts where no question can be asked (6.51, p. 89).
- We feel that even if all possible scientific questions were answered, the problems of life would still not have been touched; there is then no question left, and just this is the answer (6.52, p. 89). The solution is the vanishing of the problem (6.521, p. 89). **Rhetorical question (6.521, pp. 89–90):** is this not the reason why men to whom, after long doubting, the sense of life became clear could not then say wherein it consisted?
- The inexpressible shows itself; it is the mystical (6.522, p. 90).
- The right method of philosophy would be to say only what can be said (the propositions of natural science, which have nothing to do with philosophy); whenever someone wants to say something metaphysical, show him he gave no meaning to certain signs. This method would be unsatisfying to the other, but it would be the only strictly correct method (6.53, p. 90).
- His own propositions are elucidatory: whoever understands them finally recognises them as senseless, and must, so to speak, throw away the ladder after climbing up on it; he must surmount these propositions, and then he sees the world rightly (6.54, p. 90).
- 7: "Whereof one cannot speak, thereof one must be silent" (p. 90).

### Vorwort (German, dated Wien 1918; pp. 91–92; my paraphrase)
- The book will perhaps be understood only by one who has already had the thoughts expressed in it, or similar ones; it is no textbook (p. 91). It treats philosophical problems and shows, he believes, that their formulation rests on misunderstanding the logic of our language. The whole sense of the book could roughly be put in the words: what can be said at all can be said clearly, and of what one cannot speak one must be silent (p. 91).
- The book wants to draw a limit to the expression of thoughts, not to thinking, because drawing a limit to thought would require thinking both sides. The limit can be drawn only in language; what lies beyond is nonsense (p. 91). He makes no claim to novelty in detail and gives no sources, but says he owes a great part of the stimulus for his thoughts to Frege and to Russell (p. 91).
- Value one: thoughts are expressed (the better, the better expressed), and here he feels he fell short. Value two: the truth of the thoughts seems to him unassailable and definitive, and he is of the opinion that the problems are essentially finally solved. If he is not mistaken in this, the second value of the work is that it shows how little is achieved when these problems are solved (pp. 91–92).

## Toy example (ours)
Check that $(p\supset q).p:\supset:q$ (cf. 6.1221) is a tautology.

| $p$ | $q$ | $p\supset q$ | $(p\supset q).p$ | whole |
|---|---|---|---|---|
| T | T | T | T∧T = T | T⊃T = T |
| T | F | F | F∧T = F | F⊃F = T |
| F | T | T | T∧F = F | F⊃T = T |
| F | F | T | T∧F = F | F⊃F = T |

The whole is true in all 4 rows, so it says nothing about whether $p$ or $q$ holds. Its construction shows that $q$ follows from $p$ and $p\supset q$.

## Concepts
- [[tautology]] (new) — a proposition true for all truth-combinations of its arguments, saying nothing; logic's propositions (6.1, p. 76; 6.1203, p. 79)
- [[saying-vs-showing]] (new) — what cannot be said, such as *there are natural laws*, shows itself (6.36, p. 86); the inexpressible shows itself (6.522, p. 90); tautologies show logical properties (6.12, p. 77)
- [[general-form-of-proposition]] (new) — $[\bar p,\bar\xi,N(\bar\xi)]$: iterated $N$ on elementary propositions (p. 75)
- [[number-as-exponent]] (new) — a number is how often an operation is repeated (6.021, p. 76)
- [[analytic / synthetic distinction]] — here a parenthesis equates logical propositions, which say nothing, with the analytical propositions (6.11, p. 77)
- [[sense (Sinn) vs. reference (Bedeutung)]] — 6.232 reports Frege's claim that the two sides of an equation have the same meaning but different senses, and says that what is essential about an equation lies elsewhere (pp. 82–83)
- [[picture theory of meaning]] — the net laid over a picture of spots illustrates a form of description (6.341, p. 84); the picture theory itself is not stated in these pages
- [[solipsism-as-realism]] (new) — strict solipsism coincides with pure realism (5.64, p. 75)
- [[ladder-elucidation]] (new) — the book's own sentences are senseless steps to be discarded (6.54, p. 90)

## Canonical instances
- [[law-of-contradiction-tautology]] — $\sim(p.\sim p)$ examined as a tautology by the notation (pp. 78–79)
- [[proof-2x2-equals-4]] — arithmetic by substitution on $\Omega$ (p. 83)
- [[net-description-of-spots]] — mechanics as a choice of net (pp. 84–85)
- [[colour-exclusion]] — logical impossibility of two colours at one place (p. 87)
- [[eye-and-visual-field]] — the subject as a limit (p. 75)
- [[ladder-image]] (p. 90)

## Bridges (candidates)
- [same-math] tautology and truth-combination notation ↔ propositional logic: truth-table validity — the same check of all rows.
- [structural-analogy] number as exponent, $\Omega^n x$ ↔ computing: n-fold iteration of a function.
- [structural-analogy] choice of net (6.341) ↔ philosophy of science: several descriptions fit the same data, so form is a free choice.
- [metaphor] showing vs. saying ↔ semantics: object language vs. talk about its form.

## Questions this raises
- If the book's propositions are senseless (6.54), what does understanding them consist of?
- How does the claim that logic has no surprises (6.1251) fit the remark that logic has been called the theory of forms and of inference (6.1224), given that logic is not a theory (6.13)?
- Is "the simplest law" in induction (6.363) only psychological, given that simpler description "says something about the world" (6.342)?
- Why is ethics unspeakable while natural science is speakable (6.42, 6.53)?

## Reading notes
- Printed page = pdf − 2. Images were supplied only for pp. 76, 78, 79, 83 and 92. Text layers elsewhere lost symbols: the overbars on p. 75 (apparently; no image of p. 75 was supplied, and I inferred them from 6.01 on p. 76), the diagrams in 5.6331, 6.1203 and 6.36111, and ligatures such as "eld", "dene". I did not reproduce the diagrams.
- The Ω and ν symbols in 6.02 and 6.241 were checked against the images of pp. 76 and 83.
- 6.1203 diagrams (pp. 78–79) are described, not redrawn. The 6.36111 figure and the 5.6331 figure are absent from the text.
- The footnote on 6.32 (p. 84) is signed "B. R.".
- The Vorwort is the German original ("Logisch-Philosophische Abhandlung", Wien 1918); the translation is mine. Its dashes were lost in the text layer, so punctuation in my paraphrase is approximate.
- No misprints noticed beyond OCR loss.
