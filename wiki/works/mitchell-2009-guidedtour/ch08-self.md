---
id: mitchell-2009-guidedtour/ch08-self
work: mitchell-2009-guidedtour
unit: Chapter 8 — Self-Reproducing Computer Programs
pages: pdf 147–160 (printed page numbers not visible)
fields: [complex-systems]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Self-Reproducing Computer Programs

## L0 — One line
A program can copy itself without infinite regress if it uses the same stored information both as instructions and as data, and DNA and von Neumann's automaton use the same trick.

## L1 — The gist (≤ 120 words)
Can a machine reproduce itself, or does self-copying force an infinite regress (an endless chain of descriptions of descriptions), as sceptics claim? Mitchell builds a short program that prints an exact copy of itself. It works because the same stored lines serve as instructions and as data to be printed. The same dual use of information lies behind Gödel's self-referential sentence, Turing's halting proof, and DNA replication. The program needs an outside interpreter (the machinery that carries out its instructions), but DNA encodes its own interpreter, as did von Neumann's self-reproducing automaton. The chapter closes with a portrait of von Neumann.

**Prerequisites:** the idea of a program as lines of text in memory; Gödel's sentence and Turing's halting problem (chapter 4); DNA, genes, enzymes (chapter 6).

## L2 — Key ideas
- Biologists' lists of requisites for life often include autonomy, metabolism, self-reproduction, survival instinct, evolution/adaptation. Many people have argued that computers cannot have these. All of the objections have been claimed to be disproven "in one way or another" by artificial life (pdf 148).
- The self-reproduction objection says a program would need a description of itself, which needs a description of itself, and so on forever (pdf 148).
- Naive self-copying, where each print command copies the previous one, never ends (pdf 149–150).
- Solution: the same memory lines are executed as instructions and then printed as data (pdf 154).
- This dual use is also central to Gödel's sentence and to Turing's halting proof (pdf 154–155).
- DNA replication uses the same dual use. Unlike the program, DNA also encodes its own interpreter (pdf 155–156).
- Von Neumann's automaton contained a self-copying program plus machinery for its own interpretation. It showed that machine self-reproduction is possible in principle (pdf 156–157).
- Von Neumann also worked on a general theory of information processing across biology and technology, and is linked to cybernetics, an ancestor of complex systems (pdf 159).

## L3 — Walkthrough

### What Is Life? (pdf 147–148)
Two questions are left open: how life originated, and what being alive means. There is no agreement on a definition of life (pdf 147). The idea of artificial life is very old, from the Golem to *Blade Runner*. It becomes a new question: can computers or robots be "alive"? (pdf 147)

Biologists' lists of key requisites differ, but most include autonomy, metabolism, self-reproduction, survival instinct, and evolution and adaptation (pdf 148). **Sceptics' objections**, as the author reports them (pdf 148):
- A computer only does what humans program it to do.
- A computer must be fed energy by humans.
- Self-reproduction needs a description of itself that contains a description of itself, *ad infinitum*.
- A computer does not care about surviving. Example: "Deep Blue may have beat Kasparov, but it didn't get any joy out of it."
- A computer changes only in ways its programmer specified.

The author says all of these have been claimed to be disproven "in one way or another" by artificial life, the field that simulates and "creates" life on computers. The chapter and the next focus on self-reproduction and evolution (pdf 148).

### Self-Reproduction in Computers (pdf 149–154)
**The task:** write a program that prints an exact copy of itself and nothing else. The language is a pseudo-language (pdf 149).

**First attempt.** Write `program copy`. Add `print("program copy")`. Add a line printing that line, with the indentation and the quotation marks now quoted. Add another line printing that line, and so on. Each command prints the one before it, so there is an infinite regress (pdf 149–150).

The author says this puzzle echoes Gödel and Turing. The solution was originally found by von Neumann, for a more complicated problem (pdf 150). Von Neumann's computer design has a central processing unit and a memory holding both programs and data; it remains the basic design of standard computers (pdf 150). His self-reproducing automaton was the first complete design for a self-reproducing machine. The self-copying program illustrates its principle in simplified form (pdf 150).

**Language facts needed** (pdf 151–152):
- Memory has numbered locations. Each holds a line of text, which can be read as a command or as data (pdf 151).
- The instruction pointer `ip` holds the location of the instruction being executed. It starts at the first line and increases by 1 after each step (pdf 152).
- `line[n]` is the text in location n. A `loop until` command repeats the commands in braces until its condition is true. Example: `x = 0`, then `loop until x = 4 { print("Hello, world!") x = x + 1 }` prints the greeting four times (pdf 152).

**The program `selfcopy`** (Fig. 8.2, pdf 153). Nine lines:
1. `program selfcopy`
2. `L = ip - 1`
3. `loop until line[L] = "end"`
4. `{`
5. `print(line[L])`
6. `L = L + 1`
7. `}`
8. `print("end")`
9. `end`

Hand-simulation (pdf 153–154):
- Line 2 runs with ip = 2, so L = 1. L then stays 1 until it is reset (pdf 153).
- The loop prints `line[L]` and adds 1 to L, until `line[L]` equals `end`. First `program selfcopy` is printed, then L becomes 2 (pdf 153).
- Each line is printed in turn. When line 5 runs with L = 5, `print(line[L])` prints itself (pdf 154).
- When L = 9, `line[L]` is `end` and the loop stops. Lines 1–8 have been printed. Line 8 then prints "end", completing the copy (pdf 154).

**Essence:** the same information in memory is used in two ways, as instructions to execute and as data to be printed. This dual use avoids the regress (pdf 154).

*Intuition note:* The first attempt fails because each new line must describe the old one. The working program instead has one loop that reads its own lines as plain text and prints them. The lines being read are the very lines doing the reading.

### The Deeper Meaning of the Self-Reproducing Computer Program (pdf 154–155)
Dual use is also at the heart of Gödel's paradox, the sentence "This statement is not provable." (pdf 154)
- Let S be the literal string of characters. Facts about S: twenty-six letters, four spaces, one period (pdf 154).
- Let M be its meaning, "Statement S is not provable." Think of M as the "command" and S as its "data". The data S is the same thing as the command M (pdf 154).
- The chief reason Gödel could make this a mathematical paradox was that he phrased M as a mathematical statement and S as a number encoding that statement's characters (pdf 154–155).
- Hofstadter's *Gödel, Escher, Bach* discusses this in detail (pdf 155).

In Turing's halting proof, H from chapter 4 ran on its own code. It was used both as an interpreted program and as the input to that program, like the self-copying program (pdf 155).

### Self-Replication in DNA (pdf 155–156)
Genes are substrings of DNA that encode amino acids making up proteins, including enzymes that split the double helix and copy each strand (via messenger RNA, transfer RNA, ribosomes). In a "very crude analogy", the DNA strings encoding the copying enzymes correspond to the lines of code. These are "executed" when the enzymes are made, and the enzymes treat DNA as data to be split and copied (pdf 155).

**Difference:** the program needs an interpreter (instruction pointer and operating system) that is completely external to it (pdf 155–156). In DNA, the instructions for building the interpreter (the protein-synthesis machinery) are encoded in the DNA. So DNA encodes both its self-replicating "program" and its own interpreter (pdf 156).

*Intuition note:* The cell is a copier that also contains the instructions for building its own copier. The toy program lacks this: it relies on an external interpreter (the computer and its operating system), which the program does not encode.

### Von Neumann's Self-Reproducing Automaton (pdf 156–157)
- The automaton was described mathematically but not actually built by von Neumann. It contained a self-copying program and the machinery to interpret it, so it was "truly" self-reproducing. This is why it was far more complicated than the simple program (pdf 156).
- It was formulated in the 1950s, before the details of biological reproduction were understood (pdf 156).
- Von Neumann mostly completed the design and proof of correctness before dying in 1957, aged 53. Arthur Burks completed the proof. Burks edited the work, published in 1966 as *Theory of Self-Reproducing Automata* (pdf 156).
- It showed that machine self-reproduction is possible in principle. Its "logic" turned out to have some remarkable similarities to the one used by living systems (pdf 157).
- Von Neumann worried about public perception and did not want the "reproductive potentialities of the machines of the future" mentioned to mass media (pdf 157).
- Later, Kurzweil and Moravec (1999) celebrated super-intelligent self-reproducing robots, and Bill Joy (2000) warned of the perils of self-reproducing nano-machines. The author says none of these predictions has come to pass. Hod Lipson's group at Cornell has built simple self-reproducing robots (pdf 157–158).

### John von Neumann (pdf 158–160)
- He made fundamental contributions to at least six fields. He was a child prodigy who supposedly divided eight-digit numbers in his head at six (pdf 158).
- He earned a doctorate at 23 and became an IAS professor five years later (pdf 158).
- He invented game theory and designed the conceptual framework of the EDVAC. He made central contributions to the atomic and hydrogen bombs, and later joined the Atomic Energy Commission (pdf 159).
- He belonged to the "Hungarian phenomenon". Wigner is reported as saying Hungary had produced only one genius, Johnny von Neumann (pdf 159).
- He aimed, like Turing, at a general theory of information processing covering biology and technology. He was linked to the cybernetics community, an ancestor of complex systems (pdf 159).
- At the IAS he built the "IAS computer", whose design was a basis for early IBM computers. Its first application was weather prediction. Some "pure" scientists disliked this work, and after his death the faculty voted for no experimental science or laboratories (pdf 160).

## Toy example (ours)
Trace Fig. 8.2 to check the dual use.
- Line 2 gives L = 2 − 1 = 1.
- Iteration L = 1: `line[1]` = `program selfcopy` ≠ `end`; print it; L = 2.
- Iteration L = 2: print `L = ip - 1`; L = 3.
- Iteration L = 5: `line[5]` is `print(line[L])`; the instruction being executed prints its own text. L = 6.
- Iterations for L = 1, …, 8 each print one line, giving 8 printed lines. At L = 9, `line[9]` = `end`, so the loop stops.
- Line 8 prints `end`: 8 + 1 = 9 lines printed, equal to the 9 lines in memory.

Lines 3–7 are executed (as the loop) and also printed (as data), which is the dual use.

## Concepts
- [[self-reproduction]] (new) — a machine or program producing an exact copy of itself (pdf 149)
- [[infinite-regress]] (new) — the endless chain "a description of a description of…" threatening self-copying (pdf 148–150)
- [[dual-use-of-information]] (new) — the same information used as instructions and as data; the key to avoiding regress (pdf 154)
- [[interpreter]] (new) — machinery that executes the program's instructions; external for `selfcopy`, encoded in DNA for cells (pdf 155–156)
- [[artificial-life]] (new) — the field simulating and "creating" life on computers (pdf 148)
- [[cybernetics]] (new) — interdisciplinary study of common features of natural and artificial complex, adaptive systems, and an ancestor of complex systems (pdf 159)

## Canonical instances
- [[selfcopy-program]] — nine-line program that prints itself using dual use (pdf 153–154)
- [[von-neumann-automaton]] — first complete design of a self-reproducing machine, with its own interpretation machinery (pdf 156)
- [[dna-replication]] — enzymes encoded in DNA copy the DNA and the interpreter machinery is also encoded (pdf 155–156)
- [[goedel-sentence]] — "This statement is not provable." as string S versus meaning M (pdf 154)
- [[halting-problem]] — H run on its own code, used both as program and as input (pdf 155)

## Bridges (candidates)
- [structural-analogy] `selfcopy` program ↔ molecular biology: DNA's copying enzymes as "lines of code" (the author calls it a "very crude analogy") (pdf 155)
- [structural-analogy] Gödel's S/M, data equal to command ↔ computer science: code that reads itself as data (pdf 154)
- [metaphor] Von Neumann's cybernetics link ↔ complex systems: shared ancestry of the field (pdf 159)

## Questions this raises
- Does a program that depends on an external interpreter count as truly self-reproducing, given the author's contrast with DNA?
- What exactly does von Neumann's automaton contain, and how is it made to interpret itself?
- Could self-reproduction combined with evolution (the next chapter's topic) yield adaptation?
- Why would the logic of self-reproduction be shared by machines and living systems?

## Reading notes
- No printed page numbers appear in the text layer or the images; all citations use pdf numbers.
- Page images were supplied for pdf 151, 153, 154 only. Figures 8.1 and 8.2 were checked against them.
- The text layer flattens the code layout and indentation of the first attempt (pdf 149–150), so its exact shape is not verified.
- The text layer shows "H and H" (pdf 155), probably a lost overbar. I cite only H.
- The text layer shows Wigner as one of the Nobel laureates; I report the quote as the author gives it.
