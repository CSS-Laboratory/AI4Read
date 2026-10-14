---
id: mitchell-2009-guidedtour/ch04-computation
work: mitchell-2009-guidedtour
unit: Chapter 4 — Computation
pages: pdf 81–97 (printed page numbers not visible)
fields: [complex-systems]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Chapter 4 — Computation

## L0 — One line
Gödel and Turing showed that mathematics and computation have hard limits, and Turing's machine gave a precise definition of "definite procedure" that laid the groundwork for programmable computers.

## L1 — The gist (≤ 120 words)
Scientists now speak of "computation" in cells, markets and plants. To say what that means, Mitchell first asks what computation is and what it can do. Hilbert asked whether mathematics is complete, consistent and decidable. Gödel showed that if arithmetic is consistent, it is incomplete. Turing defined "definite procedure" with an abstract machine, showed that one universal machine can emulate any other, and used this to prove the Halting problem has no definite solution. So the third question also gets the answer "no". The same work laid the groundwork for programmable computers. The chapter prepares the discussion of natural computation in chapter 12.

**Prerequisites:** the idea of an algorithm (step-by-step recipe); binary numbers; proof by contradiction.

## L2 — Key ideas
- Complex-systems writers use "computation" for processes in cells, immune systems and markets. The chapter lays the groundwork for asking what that means (pdf 81–82).
- Hilbert's questions (completeness, consistency, decidability) are problems about mathematics itself (pdf 83–84).
- Gödel: if arithmetic is consistent, some true statements cannot be proved. His example statement refers to itself (pdf 85).
- Turing defined "definite procedure" as a Turing machine: tape, head, states and rules (pdf 87–90).
- A universal Turing machine U can run any machine M on any input I, because rules can be encoded as 0s and 1s. This is what a stored-program computer does (pdf 90–91).
- Because a program's code can be the input to another program, Turing could build a self-referential machine H′. This proves the Halting problem is uncomputable and settles the Entscheidungsproblem with "no" (pdf 92–95).
- Gödel's and Turing's proofs share one core idea: statements or machines that can talk about themselves (pdf 95).

## L3 — Walkthrough

### Opening and "What Is Computation and What Can Be Computed?" (pdf 81–82)
- The epigraph is Leibniz's hope that disputes could be settled by calculating: "Let us calculate" (pdf 81).
- People think of computation as what a desktop machine does. Yet complex-systems literature speaks of computation in cells and tissues, in the immune system, in markets and in plants (pdf 81).
- These systems do not work like a desktop computer. So what is meant by computation, and why? This is deferred to chapter 12 (pdf 82).
- Shannon information concerns a source's predictability. Real-world information is also analysed for meaning, remembered, combined and acted on, i.e. it is "processed via computation" (pdf 82).
- Before the late 1940s, "computers" were people doing calculations by hand. Example: Alice Burks, a WWII ballistics "computer" (pdf 82).
- Questions posed: can a computer compute anything in principle, or are there limits? These were answered only in the mid-twentieth century (pdf 82).

### Hilbert's Problems and Gödel's Theorem (pdf 83–86)
- In 1900 Hilbert posed 23 unsolved problems. Problems 2 and 10 are described as being about mathematics itself. Together they give three questions (pdf 83):
  1. **Complete?** Can every statement be proved or disproved from a fixed finite set of axioms? (pdf 83–84)
  2. **Consistent?** Can only true statements be proved? A proof of 1 + 1 = 3 would make mathematics inconsistent (pdf 84).
  3. **Decidable?** Is there a definite procedure that, applied to any statement, says in finite time whether it is true or false? This is the *Entscheidungsproblem* ("decision problem"), traced back to Leibniz, who built a calculating machine and believed a machine could eventually settle any mathematical statement (pdf 84–85).
- Hilbert was confident the answer would be "yes" to all three. He asserted "there is no such thing as an unsolvable problem" (pdf 85).
- In 1930 Gödel, aged 25, proved the incompleteness theorem. If the answer to question 2 is "yes" (consistent), the answer to question 1 must be "no". For arithmetic: if it is consistent, some true statements cannot be proved (pdf 85).
- Informal explanation (author's sketch, not the proof):
  - Gödel gave a statement translatable as "This statement is not provable." Call it Statement A (pdf 85).
  - If A were provable, it would be false, so a false statement would be provable: inconsistent.
  - If A is not provable, it is true, so a true statement is unprovable: incomplete.
  - Hence arithmetic is either inconsistent or incomplete (pdf 85).
  - How such a statement is built inside mathematics is the hard part. The author does not cover it (pdf 85).
- Andrew Hodges is quoted: Hilbert had thought of his programme as tidying up loose ends, and the result was upsetting for those who wanted to find something perfect and unassailable in mathematics (pdf 86).

*Intuition note:* Gödel's statement is like a sentence that says it cannot be proved. Either choice about it (provable or not) causes trouble. So, if arithmetic is consistent, it cannot prove all truths.

### Turing Machines and Uncomputability (pdf 86–90)
- In 1935 Turing, a 23-year-old graduate student, learned of Gödel's theorem from Max Newman. He saw how to answer the Entscheidungsproblem, again with "no" (pdf 86).
- His first step was to define "definite procedure". Following Leibniz's intuition, he imagined a machine that manipulates symbols, designed by thinking about how humans calculate. This is the Turing machine, later a blueprint for programmable computers (pdf 86).
- **Parts of a Turing machine** (pdf 87):
  1. A tape of cells, infinitely long in both directions.
  2. A read/write head, which at any time is in one of several states.
  3. A set of rules.
- Each step: the head reads the symbol under it and follows the rule for (current state, symbol). The rule gives the symbol to write, the move (right, left or stay) and the new state. In the halt state the machine stops. Input = symbols on the tape at the start; output = symbols on the tape after halting (pdf 87–88).
- **Example** (pdf 88–89): symbols 0, 1, blank. Input: exactly two 0s with zero or more 1s between them, blanks elsewhere (e.g. 011110). Task: leave a single 0 if the number of 1s is even, a single 1 if odd. States: start, even, odd, halt. The head starts on the left 0 in state start. The rules:
  1. start, read 0 → go to even, write blank, move right.
  2. even, read 1 → go to odd, write blank, move right.
  3. odd, read 1 → go to even, write blank, move right.
  4. odd, read 0 → write 1, halt.
  5. even, read 0 → write 0, halt.
- The procedure is guaranteed correct on any input of this format, including zero 1s (counted as even). The author calls it clunky but a definite procedure. Turing machines were put forward as *the* definition of "definite procedure", previously vague (pdf 90). While formulating these ideas Turing built no actual machines (he built significant ones later); he worked with pencil and paper alone (pdf 90).

### Universal Turing Machines (pdf 90–92)
- Turing proved that a universal machine U exists. It emulates any machine M on any input I (pdf 90).
- Encoding: write each rule as —Current State—Current Symbol—New State—New Symbol—Motion— (pdf 90). Assign 3-digit binary codes. Example codes (any consistent one-to-one choice works) (pdf 91):
  - states: start = 000, even = 001, odd = 010, halt = 100;
  - symbols: '0' = 000, '1' = 001, blank = 100;
  - right = 000, left = 111; separator = 111.
- Rule 1 (—start—0—even—blank—right—) becomes 111000111000111001111100111000111 (pdf 91). (added step) Read in blocks: 111|000|111|000|111|001|111|100|111|000|111 = sep, start, sep, 0, sep, even, sep, blank, sep, right, sep.
- All rule strings joined form the *code* of M. U's tape holds I and the code of M. At each step U reads the current symbol of I, decodes the matching rule, applies it to the input part, and tracks M's state elsewhere on its tape. When M would halt, U halts with M's output (pdf 91).
- U's own rules are omitted as complicated; the author says they can be designed. This is what a programmable computer does: it runs a program stored in one part of memory on an input stored in another. The first programmable computers were developed about ten years or so after Turing's proof (pdf 91–92).

*Intuition note:* Rules can be turned into numbers, so a machine's "program" is just more data. One fixed machine can then imitate every other.

### Turing's Solution to the Entscheidungsproblem (pdf 92–95)
- The key insight: input I may be the code of another machine. This is like running the Word Count program on a program file. A machine can even run on its own code. The same string of 0s and 1s can be read as program or as input; this was truly novel then (pdf 92).
- The proof is by contradiction. Assume the answer is "yes": a definite procedure always decides whether a statement is true (pdf 93).
- **Turing Statement:** machine M, given input I, reaches the halt state after finitely many steps (pdf 93).
- Some machines never halt (an "infinite loop"). Example: start, read 0 or 1 → even, move right; even, read 0 or 1 → start, move left (pdf 93).
- The assumption implies a machine H that, given the code of any M and any input I, answers in finite time "yes" if M halts on I and "no" if it would loop forever. Building H is the **Halting problem**. H must always halt, so it cannot just run M on I (pdf 93–94).
- Define H′: given the code of M, it computes H(M, M). It halts only if the answer is "no" (M does not halt on its own code). If the answer is "yes", H′ loops forever (pdf 94).
- Turing's question: what does H′ do on its own code? (pdf 94)
  - Suppose H′ does not halt on H′. H′ loops on M exactly when M halts on M. So H′ does halt on H′. Contradiction (pdf 94–95).
  - So H′ must halt on H′. But H′ halts on M only if M does not halt on M. So H′ halts on H′ only if H′ does not halt on H′. Another contradiction (pdf 95).
- So H′ cannot exist. Everything H′ does is allowed for a Turing machine, except possibly running H. Therefore H cannot exist (pdf 95).
- Conclusion: no definite procedure solves the Halting problem. So not every mathematical statement has a definite procedure deciding its truth, and the answer to the Entscheidungsproblem is "no" (pdf 95).
- The author says Turing's proof uses the same core idea as Gödel's. Gödel encoded statements so they could talk about themselves; Turing encoded statements as machines that run on one another (pdf 95).
- Turing's three achievements: defining "definite procedure"; laying groundwork for programmable computers; showing there are limits to what can be computed (pdf 95).

*Intuition note:* H′ is built to do the opposite of whatever H predicts about it. Feeding H′ its own code forces a contradiction, so the all-purpose loop-detector H cannot exist.

### The Paths of Gödel and Turing (pdf 95–97)
- Nineteenth-century optimism: Hilbert hoped for Leibniz's automatic proof procedure. Laplace and others believed that, using Newton's laws, scientists could in principle predict everything (from chapter 2) (pdf 96).
- Early twentieth-century results ended such hopes: quantum mechanics and chaos for perfect prediction, Gödel and Turing for unlimited power of mathematics and computing. But Turing's negative result set the stage for electronic programmable computers (pdf 96).
- Gödel: continued work in Vienna until 1940, then moved to the US. He joined the Institute for Advanced Study. His mental health worsened in the 1960s–70s. He became paranoid, believed he was being poisoned, refused food and starved to death (pdf 96).
- Turing: returned to England. In WWII he led development of code-breaking machines that decrypted almost all Enigma communications, "arguably" a key factor in the Nazi defeat (pdf 96–97).
- After the war he worked on an early programmable computer at Manchester. He studied how brain and body "compute", did work on developmental biology, and wrote about intelligent computers (pdf 97).
- He was arrested in 1950s Britain for homosexuality, sentenced to drug "therapy", and lost his security clearance. These events "may have contributed" to his probable suicide in 1954, aged 41, by a cyanide-laced apple (pdf 97).

## Toy example (ours)
Run the author's parity machine on 01110 (three 1s; expected "odd").
1. Head on the left 0, state start. Rule 1: state → even, erase 0, move right.
2. Read 1 in even. Rule 2: state → odd, erase, move right.
3. Read 1 in odd. Rule 3: state → even, erase, move right.
4. Read 1 in even. Rule 2: state → odd, erase, move right.
5. Read 0 in odd. Rule 4: write 1, halt.
Tape now holds a single 1: odd, correct. On 0110 the steps are rule 1, 2, 3, then rule 5 (even, read 0 → write 0, halt), leaving a single 0: even, correct. The state just counts 1s modulo 2.

## Concepts
- [[computation]] (new) — the way information is processed ("processed via computation"); before the late 1940s it meant calculating by hand (pdf 82)
- [[hilbert-three-questions]] (new) — completeness, consistency, decidability of mathematics (pdf 83–84)
- [[godel-incompleteness]] (new) — if arithmetic is consistent, some true statements are unprovable (pdf 85)
- [[definite-procedure]] (new) — precise finite recipe; defined by Turing as a Turing machine (pdf 90)
- [[turing-machine]] (new) — tape, head with states, rules; reads, writes, moves (pdf 87)
- [[universal-turing-machine]] (new) — machine U that emulates any machine M on any input I (pdf 90)
- [[halting-problem]] (new) — deciding if M halts on I; no definite procedure exists (pdf 94–95)
- [[entscheidungsproblem]] (new) — Hilbert's decision problem; answered "no" by Turing (pdf 85, 95)

## Canonical instances
- [[parity-turing-machine]] (new) — five-rule machine deciding even/odd count of 1s (pdf 89)
- [[godel-statement-A]] (new) — "This statement is not provable" (pdf 85)
- [[halting-contradiction-H-prime]] (new) — H′ run on its own code (pdf 94–95)
- [[word-count-program]] (new) — program taking another program as input (pdf 92)

## Bridges (candidates)
- [structural-analogy] Gödel's Statement A ↔ Turing's H′ on its own code — both use self-reference; the author says they share the same core idea (pdf 95).
- [structural-analogy] Universal Turing machine ↔ stored-program computer — U runs a program held in one memory region on data in another (pdf 91).
- [metaphor] Turing's interest in how brain and body "compute" ↔ complex-systems usage of "computation" in cells and markets — the chapter 12 theme (pdf 81, 97).

## Questions this raises
- What does "computation" mean in cells or markets, given they differ so much from a desktop computer (chapter 12)?
- Are Turing machines a complete definition of "definite procedure", or only one proposal?
- If H cannot decide halting in general, can it be built for restricted classes of machines?
- How does Gödel's encoding turn the self-referring Statement A into arithmetic?

## Reading notes
- Printed page numbers are not visible on the pages given; references use pdf numbers (pdf 81–97). Illustration pages (Hilbert, Gödel, Turing portraits) are included.
- The text layer has "number of Is" for "1s" (pdf 88); the image confirms the typo. The text layer also spaces some headings oddly (e.g. A QUICK INTRODUCTION TO TURING MACHINES, pdf 87).
- Figure 4.1 (pdf 88) shows a tape 0 1 1 1 1 1 0, head in state "start" reading 0.
- The encoded Rule 1 string checks out against the stated codes. The chapter has no exercises.
- The Gödel proof and the rules of U are explicitly omitted by the author.
