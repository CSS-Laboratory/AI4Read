---
id: popper-1959-logic/appiv-untitled
work: popper-1959-logic
unit: "Appendix iv — A Method of Constructing Models of Random Sequences"
pages: 293–296
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
# Appendix iv: A Method of Constructing Models of Random Sequences

## L0 — One line
Popper shows how to build, by a mathematical rule, 0–1 sequences that are free from after-effect in ever-longer stretches. These serve as models showing that "absolutely free" sequences exist, with a frequency limit of 1/2, with a middle frequency but no limit, or with two distinct middle frequencies.

## L1 — The gist (≤ 120 words)
The appendix asks whether sequences exist that meet Popper's randomness demand of freedom from after-effect, and how one can build them. Starting from finite "n-free" periods, Popper nests them: each new, longer period is rearranged to begin with the previous one. With some further conditions this gives a definite, calculable sequence with limiting frequency 1/2. Variants give an "absolutely free" middle frequency without a limit, and two such middle frequencies. A "shortest" version is n-free from its very beginning. Popper argues that only such sequences can set an ideal standard for randomness, because ordinary n-freedom allows a regular-looking opening segment.

**Prerequisites:** the idea of a 0–1 sequence and its relative frequencies; "n-free" (free from after-effect; the appendix takes the notion over from section 55 and does not define it); an x-tuple is a block of x ones and zeros; "equal distribution" means ones and zeros are equally frequent; "absolutely free" and "middle frequency" (cf. section 64) are used here without definition; powers of 2.

## L2 — Key ideas (5–10 bullets)
- Starting assumption: for each finite n an n-free period with equal distribution can be built, and it contains every possible x-tuple (x ≤ n+1) at least once (p. 293).
- A simple rule builds a "shortest" n-free period of length 2^(n+1) (p. 293 n.*1; p. 294 n.*1).
- Method (a) nests periods, each rearranged to begin with the previous one. With extra conditions it defines one definite sequence, computable term by term, with limits 1/2 (pp. 294–295).
- Given one absolutely free sequence, absolutely free sequences exist for any chosen frequency (p. 295).
- "Shortest random-like" sequences are n-free from the start; ordinary n-freedom or absolute freedom is not enough, because the opening may look regular (p. 295 n.*2).
- Method (b) adds blocks of ones to get an absolutely free middle frequency p ≠ 1/2 without a frequency limit (p. 296).
- Method (c) combines two absolutely free sequences by alternately searching and rearranging to get two distinct absolutely free middle frequencies (p. 296).
- Note: the multiplication theorem for two dice is assured if the combined throw sequence is assumed random (p. 296).

## L3 — Walkthrough

**Setting (p. 293).** Popper assumes, as in section 55, that for every finite $n$ a generating period (a finite block that is repeated to make a periodic sequence) can be built that is $n$-free and equidistributed. Such a period contains every combinatorially possible $x$-tuple of ones and zeros, for $x \le n+1$, at least once (p. 293).

**Footnote *1: the shortest period (pp. 293–294).**
1. Put $x = n+1$. List all $2^x$ possible $x$-tuples of ones and zeros (p. 293 n.*1).
2. Start the period with the last tuple, $x$ ones, and check it off (p. 293).
3. Rule: always add a zero if permissible, otherwise add a one. "Permissible" means the newly created last $x$-tuple has not yet occurred. Check off each new last $x$-tuple (p. 293).
4. Stop when all tuples are checked. The result has length $2^x + x - 1$. It consists of (a) a generating period of length $2^x = 2^{n+1}$ of an $n$-free alternative, plus (b) the first $n$ elements of the next period (p. 293).
5. Popper calls it "shortest" because, as he says, it is easily seen that no periodic $n$-free sequence has a shorter generating period than $2^{n+1}$ (pp. 293–294). He says he and Dr. L. R. B. Elton found proofs that the rule is valid and plan a joint paper (p. 294 n.*1).

*Intuition note.* The rule walks through the list of all patterns of length $n+1$ without repeating any. So each of them is checked off and occurs in the period (and, by the source, so does every shorter pattern).

**(a) An "absolutely free" model sequence (pp. 294–295).**
1. Write an $n$-free period of length $n_1$ for any chosen $n$ (p. 294).
2. Write a new period that is at least $(n_1-1)$-free, of length $n_2$. It must contain the first period as a segment. Rearrange it so that it begins with that segment; this is always possible, by section 55 (p. 294).
3. Repeat: the third period is at least $(n_2-1)$-free, rearranged to begin with the second, and so on (p. 294).
4. The length grows very fast. The first period begins every later one (p. 294).
5. Fix a particular starting sequence and add further conditions, for example that each period be exactly $(n_i-1)$-free, never longer than necessary. The construction can then be made unambiguous and to define a definite sequence, so that for every term one can calculate whether it is 1 or 0 (p. 294).
6. The result is a sequence built by a mathematical rule, with frequency limits
$$ {}_{\alpha}F'(1) = {}_{\alpha}F'(0) = \tfrac12 \tag{p. 295}$$

**Footnote *2: concrete example (pp. 294–295).**
- Start with period (0) $= 01$, of length $n_0 = 2$ (a 0-free alternative). The next period must be 1-free. Note *1 gives 1100, rearranged to begin with 01: (1) $= 0110$, so $n_1 = 4$ (p. 294).
- The 3-free period is $1111000010011010$. Rearranged to begin with (1), it gives (2) $= 0110101111000010$, so $n_2 = 16$ (p. 295).
- Next comes a 15-free period (3) of length $2^{16} = 65{,}536$. Find (2) inside it, rearrange so (3) starts with (2), and build (4) of length $2^{65{,}536}$ (p. 295).
- Popper's name is "shortest random-like sequence", for two reasons. (i) Each step builds a shortest $n$-free period. (ii) At every stage the sequence begins with a shortest $n$-free period (p. 295).
- Consequently every beginning piece of length $m = 2^{2^{2^{\cdot^{\cdot^{\cdot}}}}}$ is a shortest $n$-free period for the largest possible $n$, namely $n = \log_2 m - 1$ (p. 295).

**Why "shortness" matters (p. 295, n.*2).** One can always get $n$-free or absolutely free equidistributed sequences whose first segment, of any chosen length $m$, is regular, for example only zeros. So for applications $n$-freedom, or even absolute freedom, is not enough. It must be replaced by "something like" a demand for $n$-freedom "becoming manifest from the beginning". Shortest sequences achieve this most radically, so Popper says they alone can set an ideal standard for randomness. Their convergence can be proved immediately, unlike the cases (b) and (c). He refers also to appendix *vi (p. 295).

*Intuition note.* A sequence could be statistically fair in the long run and still start with a million zeros. The shortest construction rules this out for the lengths $m$ of its tower, because each such opening piece is already $n$-free for the largest possible $n$.

**Existence for any frequency (p. 295).** The procedure of the proof of the third form of the binomial formula (section 60) or of Bernoulli's theorem (section 61) shows, with any degree of approximation, that absolutely free sequences exist for whatever frequency value we choose. The proviso is that at least one absolutely free sequence exists, which (a) has just proved (p. 295).

**(b) Absolutely free middle frequency without a limit (p. 296).**
- Change (a): after some given number of length increases, always add a finite block (of ones, for example) (p. 296).
- The block is long enough that a given frequency $p \neq \tfrac12$ is reached (p. 296).
- Then treat the whole sequence written so far, of length $m_i$, as the commencing sequence of an $(m_i-1)$-free period with equal distribution, and continue (p. 296).
- The resulting sequence has an "absolutely free" middle frequency (cf. section 64) but no frequency limit (p. 296).

**(c) Two absolutely free middle frequencies (p. 296).**
1. By (a), absolutely free sequences without equal distribution exist. Take two, (A) and (B), with frequencies $p$ and $q$ (p. 296).
2. Write a commencing sequence of (A). Find it in (B). Rearrange the period of (B) preceding that point so that it begins with the written sequence. Use this whole rearranged period as the new commencing sequence (p. 296).
3. Next search (A) for this new sequence, rearrange (A), and so on (p. 296).
4. Again and again the sequence is $n_i$-free for frequency $p$ (A), and again and again for $q$ (B). The $n_i$ increase without limit. So there are two distinct middle frequencies, both absolutely free, because (A) and (B) were chosen with distinct limits (p. 296).

**Note on two dice (p. 296).** The special multiplication theorem applies to throwing two dice X and Y at a time (and related problems) if, for example, we hypothetically estimate that the "combination sequence" is random. In this sequence the throws of X are the odd terms and the throws of Y the even terms (p. 296).

## Toy example (ours)
*Shortest period for n = 2.* Take $x = 3$, with 8 triples. Start with 111. Following the rule of n.*1:
- Add 0: 1110, new triple 110 ✓.
- Add 0: 11100, new triple 100 ✓.
- Add 0: 111000, new triple 000 ✓.
- Adding 0 would repeat 000, so add 1: 1110001, new triple 001 ✓.
- Add 0: 11100010, new triple 010 ✓.
- Adding 0 would repeat 100, so add 1: 111000101, new triple 101 ✓.
- Adding 0 would repeat 010, so add 1: 1110001011, new triple 011 ✓.

All 8 triples are checked, and the length is $10 = 2^3 + 3 - 1$. The generating period is the first 8 terms, 11100010. Read cyclically, its 8 windows of length 3 are 111, 110, 100, 000, 001, 010, 101, 011, each once. Its four 1s among eight terms give frequency 1/2.

*One nesting step.* Start with period 10 (length 2). A 1-free period is 1100. Read cyclically from its second term it gives 1001, which begins with 10. So the next period is 1001, with length 4. The 3-free period of p. 295, 1111000010011010, contains 1001 at terms 9–12. Rotating it to start there gives 1001101011110000, which begins with 1001 and has length 16.

## Concepts
- [[n-free-sequence]] (new) — a sequence "$n$-free (from after effect)"; the exact definition is not given on these pages, the appendix takes the notion over from section 55 (p. 293)
- [[generating-period]] (new) — finite block whose repetition gives a periodic sequence; here, of length $2^{n+1}$ for shortest $n$-free ones (p. 293)
- [[absolute-freedom]] (new) — an "absolutely free" sequence; the definition is not given here. The model in (a) is built from nested periods that are at least $(n_i-1)$-free, with $n_i$ growing (p. 294)
- [[shortest-random-like-sequence]] (new) — nested construction, $n$-free from the start; proposed ideal standard of randomness (p. 295)
- [[middle-frequency]] (new) — a notion from section 64 (not defined here); in (b) and (c) a sequence can have an "absolutely free" middle frequency without having a frequency limit (p. 296)
- [[combination-sequence]] (new) — one sequence interleaving two dice: X on odd terms, Y on even terms (p. 296)

## Canonical instances
- [[nested-period-construction-example]] — the worked example 01 → 0110 → 0110101111000010 → …, with lengths 2, 4, 16, 65,536 (pp. 294–295)
- [[two-dice-combination-sequence]] — randomness of the combined sequence is what assures the multiplication theorem (p. 296)

## Bridges (candidates)
- [same-math] a generating period containing every $(n+1)$-tuple once (cyclically) ↔ combinatorics: de Bruijn sequences — to be confirmed by the Knowledge Manager; the source does not mention them.
- [structural-analogy] randomness demanded "from the beginning" of the sequence ↔ randomness tests on initial segments (algorithmic randomness) — both reject standards that allow a regular opening.

## Questions this raises
- Is "shortest random-like" really a sensible ideal of randomness, given that it is fully determined by a rule (p. 294)?
- What does the proof of validity of the construction rule (Elton and Popper, p. 294 n.*1) look like?
- How do (b) and (c) stand to convergence, which is proved only for shortest sequences (p. 295)?
- Why does the multiplication theorem need the combination sequence to be random (p. 296)?

## Reading notes
- Printed = pdf − 29 (pdf 322–325 = pp. 293–296).
- Footnote *1 begins on p. 293 and ends on p. 294; footnote *2 begins on p. 294 and ends on p. 295. The main-text sentence "with frequencies whose limits are," continues from p. 294 to the display on p. 295.
- The text layer garbles the formulas; the p. 295 image shows ${}_\alpha F'(1)={}_\alpha F'(0)=\tfrac12$ and the tower $m=2^{2^{2^{\cdot^{\cdot^{\cdot}}}}}$. The symbol "⭐" on p. 293 is read here as "≤" ($x \le n+1$) from context; the p. 293 image was not checked.
- Only the image of pdf 324 was checked; the other pages rely on the text layer.
