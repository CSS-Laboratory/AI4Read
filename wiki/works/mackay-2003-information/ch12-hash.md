---
id: mackay-2003-information/ch12-hash
work: mackay-2003-information
unit: "12 Hash Codes: Codes for Efficient Information Retrieval"
pages: 192-204
fields: [information-theory, bayesian]
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
# Hash Codes: Codes for Efficient Information Retrieval

## L0 — One line
A hash function is a fixed pseudo-random code from N bits down to M bits that turns slow search into one table look-up, and the size M needed depends on whether you fear accidental collisions, a forger (about 2^M trials) or a cheating author (about 2^{M/2}).

## L1 — The gist (≤ 120 words)
The unit asks how to look up one of S stored N-bit items (for example a name in a phone directory) quickly and with little memory. Answer: a hash function, a fixed pseudo-random map from N bits to a shorter M-bit string, indexes a table that stores the record number; collisions (equal hashes) are handled by scanning on or by buckets. For an ideal random hash, keeping expected collisions below one needs table size T above about S², while tolerating a few needs only order S. Hashes also check arithmetic and files; against a forger, a hash of M bits needs about 2^M trials, but a cheating author needs only about 2^{M/2}.

**Prerequisites:** binary strings and powers of 2; expected value; Bayes' rule in odds form; random codes from channel coding; basic counting (pairs, binomial coefficients).

## L2 — Key ideas
- Retrieval means inverting the map s → x(s), where s is the record number of the N-bit string x(s) and S strings are stored. A look-up table needs about 2^N log2 S memory, which is impossible for N ≈ 200. A raw list needs about S + N binary comparisons per search, an alphabetical list about ⌈log2 S⌉ string comparisons (pp. 193–194).
- Hash codes combine source coding and channel coding: a random code from N bits to M < N bits makes a table small enough to be a look-up table (pp. 194–195).
- Retrieval = hash, look in the table, then verify against the stored original; a zero entry proves absence (p. 197).
- Collisions are resolved by appending in the table (table must be much bigger than S) or by buckets (sorted lists of the strings sharing a hash; this allows a small table) (pp. 197–198).
- For an ideal random hash, expected pair collisions are S(S−1)/(2T), where T = 2^M is the table size. A collision-free table needs T above about S²; tolerating a fraction f of collisions needs T of order S/f (pp. 198, 202–203).
- Hashes serve as checksums. A false negative (the files differ but the hashes agree) has probability 2^{−M} if the hash is random and the errors know nothing about it. A match multiplies the odds that the answer is right by a likelihood ratio (how much likelier the match is if the answer is right), so it is evidence (pp. 198–199, 202–203).
- Against an adversary the hash must be one-way (easy to compute, hard to invert); linear hashes give no security. A forger needs about 2^M hashes, a cheating author about 2^{M/2}, so M ≳ 160 bits is needed in the book's example (pp. 199–201).
- The same counting logic gives uniqueness thresholds (text length, melodies, DNA-binding sites) (pp. 201–204).

## L3 — Walkthrough

### Intro (p. 192)
Chapters 1–11 ranked codes by efficiency of channel use. Now ease of retrieval is the main goal. The random codes useful in channel coding also help rapid retrieval (p. 192).

### 12.1 The information-retrieval problem (pp. 193–195)
**Setup.** There are S binary strings $\{x^{(1)},\dots,x^{(S)}\}$ of N bits, with S much smaller than $2^N$. The superscript s is the *record number*. Example numbers: N ≃ 200, S ≃ 10^7 ≃ 2^23 (Fig. 12.1, p. 193). Names are assumed to have equal length and to be distinct (p. 193). The task is to invert s → x(s): given x, return s if x = x(s), else report "no such s". It should use little memory and time, and allow cheap additions (p. 193).

**Standard solutions.**
- *Look-up table:* $2^N \log_2 S$ memory. For N ≈ 200 this is impossible; the solar system has only about 2^190 particles (pp. 193–194).
- *Raw list:* pairs (s, x(s)), about SN bits. Searching from the top takes on average five million pairwise comparisons here (p. 194).
- *Ex. 12.1 result (p. 202):* a mismatch against a random string costs on average 2 binary comparisons. The raw list costs on average about S + N binary comparisons for random names. The worst case is SN (p. 202).
- *Alphabetical list:* sorted; by repeated halving, a search takes ⌈log₂S⌉ string comparisons, so at most ⌈log₂S⌉·N binary comparisons. Memory is as for the raw list. Inserting a new string takes about ⌈log₂S⌉ binary comparisons (p. 194).

**New viewpoint.** The task is a map from N bits to log₂S bits, "pseudo-invertible" because the stored pair takes us back. It resembles (i) a typical-set encoder from source coding, which the book never actually built, and (ii) the random channel codes from K to N bits. A hash code uses random codes from N bits to M bits with M < N, mapping into a space small enough for a look-up table (pp. 194–195).

> *Intuition note:* We cannot afford one slot per possible name (2^N), but we can afford one slot per *hash value* (2^M). The price is that two names may share a slot.

### 12.2 Hash codes (pp. 195–197)
- A **hash function** h(x) is a fixed deterministic function mapping an N-bit x to an M-bit string. It should be indistinguishable from a fixed random code and quick to compute. Table size is T = 2^M, a little bigger than S, say ten times (Fig. 12.2, p. 195).
- *Division method:* T prime, preferably not near a power of 2; h = remainder of x divided by T (p. 195).
- *Variable string addition:* bytes added modulo 256. Defect: anagrams collide. The improvement passes the running total through a fixed pseudorandom permutation after each character. The *exclusive-or* version hashes twice, with initial totals 0 and 1, giving a 16-bit hash (Algorithm 12.3, C code by Thomas Niemann, p. 196).

**Encoding.** Create a table of $2^M b$ memory units (b = memory for an integer between 0 and S), initially zero. For each s, write s at location $h^{(s)} = h(x^{(s)})$ (Fig. 12.4, p. 196). If that entry is already occupied, a *collision* has occurred (p. 195).

**Decoding.** Compute h of the target x and look at the table (p. 197).
- A zero means x is not in the database. The cost is one hash evaluation and one look-up (p. 197).
- A non-zero s means either x = x(s) or another string shares the hash (or, with collision resolution, the entry relates to that system). Check by looking up x(s) in the forward database and comparing bit by bit. A successful retrieval costs one hash, one look-up in the 2^M table, one look-up in a table of size S and N binary comparisons (p. 197).

**Ex. 12.2 result (pp. 197, 202):** each matching bit contributes a likelihood ratio $P(\text{datum}\mid H_0)/P(\text{datum}\mid H_1) = 1/(1/2) = 2$ (12.5), with $H_0: x^{(s)}=x$ and $H_1: x^{(s)}\ne x$. After r matching bits the ratio is $2^r$ to one; 30 bits give odds of about a billion to one from even prior odds. The fact that s was found at h(x) gives further evidence for $H_0$ (p. 202). The method works for strings of any length if h accepts any length (p. 197).

> *Intuition note:* Checking bits one by one is Bayesian updating. Each agreeing bit doubles the odds that you have the right record.

### 12.3 Collision resolution (pp. 197–198)
- *Appending in table:* on collision, write s into the next zero location, wrapping from the bottom to the top. When decoding, continue down until an s whose x(s) matches (done) or a zero (cue not in database). The table must be substantially bigger than S; if 2^M < S the encoder gets stuck (p. 197).
- *Storing elsewhere:* location h holds a pointer (distinguishable from a record number) to a *bucket*, a sorted list of strings with hash h. The decoder searches the short bucket. The hash table may then be quite small, even so small that almost all strings collide, since a bucket search takes few comparisons (p. 198).

### 12.4 Planning for collisions: a birthday problem (p. 198; solution pp. 202–203)
Ex. 12.3 asks for the expected number of collisions for S entries and an ideal random hash with M-bit output (p. 198). Final results (p. 202):
- Expected pair collisions: $S(S-1)/(2T)$ (12.6); one pair collides with probability 1/T, and there are S(S−1)/2 pairs.
- Fewer than 1 expected needs $T > S(S-1)/2$, so $M > 2\log_2 S$ (12.7): twice the bits that would give each entry a unique name.
- A fraction f of names collided with needs $T > S/f$, so $M > \log_2 S + \log_2[1/f]$ (12.8). For f ≃ 0.01 this is 7 extra bits above log₂S (pp. 202–203).
- Scaling: collision-free needs T greater than about S². Tolerating a small collision frequency needs T of order S only (p. 203).

> *Intuition note:* Pairs grow like S², so avoiding *every* collision is expensive. Avoiding collisions for most names is cheap, and buckets make rare collisions harmless.

### 12.5 Other roles for hash codes (pp. 198–201)
**Checking arithmetic (p. 198).** *Casting out nines* compares the digit sum modulo 9 of the addends with that of the answer. Example 12.4: 189 + 1254 + 238 = 1681; both sides give 7, so the test passes. It is a hash function with $h\in\{0,\dots,8\}$:
$$h(a+b+c+\cdots)=\text{sum modulo nine of all digits in } a,b,c \tag{12.1}$$
$$a+b+c+\cdots=m+n+o+\cdots \;\Rightarrow\; h(a+b+c+\cdots)=h(m+n+o+\cdots) \tag{12.2}$$
(12.2) is a property of decimal arithmetic (p. 198).

*Ex. 12.5 result (p. 203):* posterior ratio = prior ratio × likelihood ratio $P(\text{match}\mid H_+)/P(\text{match}\mid H_-)$. The numerator is 1. If errors are "random from the point of view of the hash function", the denominator is 1/9, giving 9:1 evidence for a correct addition. If errors are, say, multiplying the answer by 10 or swapping adjacent digits, neither of which changes the hash, the denominator could be 1 and a match gives no evidence (p. 203).

**Error detection among friends (p. 199).** Alice and Bob compare M-bit hashes of their files, instead of transferring the file. If the hashes match, the files are almost surely the same.
- *Example 12.6:* if the hash is random and the process making the files differ knows nothing about it, the false-negative probability (files differ yet hashes agree) is $2^{-M}$. For 32 bits it is about $10^{-10}$ (p. 199).
- A common choice is the linear 32-bit cyclic redundancy check, 32 parity-check bits like the 3 of the (7,4) Hamming code. M = 32 is plenty for noise errors at a one-in-a-billion rate (p. 199).
- *Ex. 12.7 result (p. 203):* adding only M = 32 extra hash bits gives pretty good error detection; the probability that an error is undetected is $2^{-M}$, less than one in a billion. Error correction needs far more check bits, depending on the expected corruption and file size. Example: eight random corrupted bits in a megabyte need at least about $\log_2\binom{2^{23}}{8}\simeq 23\times 8\simeq 180$ bits to specify, by the counting argument of exercise 1.10 (p. 203).

**Tamper detection (pp. 199–201).** Suppose the differences come from an adversary, Fiona.
- A linear hash such as a CRC gives no security. Fiona modifies the file, then uses linear algebra to find about 32 further bit-flips restoring the original hash (p. 199).
- The hash must be *one-way* (easy to compute, hard to invert). MD5 is a widely used 128-bit example (pp. 199–200).
- Even with a good one-way hash, if Fiona has access to the hash function she can search for a tweak of her tampered file whose hash matches. For a 32-bit hash this takes about 2^32 attempts, so a 32-bit hash is too small. Remedies: enough bits, or a secret hash function (p. 200). **Fiona has to hash 2^M files** (p. 200).
- *Alice as cheat (p. 200):* Alice sends Bob the bookie a hash of her bet and reveals the bet later. She could cheat by finding two different bets with the same hash. (Newton and Hooke used secret publication; Hooke's hash was alphabetization, UT TENSIO, SIC VIS → CEIIINOSSSTTUV.)
- *Example 12.8:* hash N₁ versions of bet one and N₂ of bet two. By analogy with Montagues and Capulets, the expected number of cross-collisions is
$$N_1N_2\,2^{-M} \tag{12.3}$$
 To minimise N₁ + N₂, take N₁ = N₂; then about $2^{M/2}$ files must be hashed (p. 201). With C = 10^6 computers, T = 10 years and t = 1 ns per hash, security against Alice needs $M \gtrsim 2\log_2(CT/t)\simeq 160$ bits (p. 201).

> *Intuition note:* Fiona must hit one *specific* hash value (about 2^M tries). Alice may pick *any* matching pair (about 2^{M/2} tries, the birthday effect). So protection against the author needs a hash twice as long.

*Further reading (p. 201):* Knuth (1968) vol. 3; Bentley (2000), section 13.8, on McIlroy's spell program, which uses a 64-kilobyte data structure to store the spellings of a 75,000-word dictionary.

### 12.6 Further exercises (pp. 201–202) and solutions (pp. 203–204)
Ex. 12.9 asks for the shortest unique international address (p. 201). Ex. 12.10 and 12.11 final results:
- **Ex. 12.10 (p. 203):** estimate 10^16 characters of human writing (one 2-million-character book per person) over an alphabet of 37 characters. The expected number of matches of a random length-L string is $10^{16}/37^L$, vanishingly small for $L \ge 16/\log_{10}37 \simeq 10$. This may overestimate L because of redundancy in writing. For melodies, allowing leaps up to an octave gives 23 choices per note and $23^{r-1}$ melodies of r notes (the author quotes 250 000 for r = 5). Recorded compositions probably number under a million. From his experience of "guess that tune", it seems to the author that many four-note sequences are shared but most famous five-note sequences are unique (pp. 203–204). Margin note: the Parsons code (U/R/D for each consecutive pair) is a related hash for melodies (p. 204).
- **Ex. 12.11 (p. 204):** a protein must recognise a DNA site unique in a genome of N = 3 × 10^9 nucleotides, treated as random. The chance of no other occurrence is roughly $(1-(1/4)^L)^N \simeq \exp(-N(1/4)^L)$ (12.9). This is close to one only if $N4^{-L}\ll 1$ (12.10), i.e. $L>\log N/\log 4$ (12.11), so $L_{\min}=16$ nucleotides. Weak protein bound: 32 bits / log₂20 ≃ 7 amino acids. Realistic bound: 16 nucleotides span 5.4 nm. Scaling from lysozyme (129 amino acids, 4 nm) with volume ∝ length ∝ diameter³ gives 2.5 × 129 ≃ 324 amino acids. **(b)** If the site is a twice-repeated subsequence recognised by a dimer, the diameter halves, so length 324/8 = 40 amino acids. A protein shorter than this cannot alone be a gene-specific regulator, since its surface lacks enough information content (p. 204).

## Toy example (ours, not from the text)
Division method with T = 7. Store three integer "names": x(1) = 15, x(2) = 22, x(3) = 9. Table positions 0–6, all zero at first.
1. 15 mod 7 = 1 (since 14 + 1). Position 1 is empty, so write 1 there.
2. 22 mod 7 = 1 (since 21 + 1). Position 1 is taken (collision). Append in table: position 2 is empty, so write 2 there.
3. 9 mod 7 = 2. Position 2 is taken. Position 3 is empty, so write 3 there.

Table: [0, 1, 2, 3, 0, 0, 0].

Look up 9: h = 2. Entry 2 points to x(2) = 22 ≠ 9. Next, entry 3 points to x(3) = 9, a match, so return s = 3.
Look up 16: h = 2. x(2) = 22 ≠ 16; x(3) = 9 ≠ 16; position 4 holds 0, so 16 is not in the database.
Birthday check (12.6): expected pair collisions = S(S−1)/(2T) = 3·2/(2·7) = 6/14 ≈ 0.43. Here one collision (15 and 22) occurred.

## Concepts
- [[hash-function]] (new) — fixed, quick, pseudo-random map from N-bit strings to M-bit strings, M < N (p. 195)
- [[hash-table]] (new) — table of 2^M entries storing record numbers at index h(x(s)); zero means empty (p. 195)
- [[collision]] (new) — two different strings with the same hash value (p. 195)
- [[collision-resolution]] (new) — appending in the table, or storing collided strings in sorted buckets (pp. 197–198)
- [[birthday-problem]] (new) — expected collisions among random labels: S(S−1)/(2T) for S items, N₁N₂2^{−M} between two groups (pp. 198, 200, 202)
- [[one-way-hash-function]] (new) — a hash that is easy to compute and hard to invert; needed against forgers (pp. 199–200)
- [[cyclic-redundancy-check]] (new) — linear hash of 32 parity-check bits, good for noise, no security against forgers (p. 199)
- [[error-correcting-code]] — adds redundancy to correct errors; needs far more check bits than a hash used for detection (p. 203)
- [[likelihood]] — here P(datum | hypothesis); a matching bit gives ratio 2; a casting-out-nines match gives 9 only under a random-error model (pp. 202–203)
- [[bayes-theorem]] — posterior odds = prior odds × likelihood ratio, used for the retrieval check and casting out nines (p. 203)

## Canonical instances
- [[phone-directory-retrieval]] — the running example, with N ≃ 200, S ≃ 2^23, M ≃ 30 (pp. 193, 195)
- [[casting-out-nines]] — a hash of arithmetic; the match gives evidence 9:1 if errors are random from the hash's point of view, but none if they are of a kind the hash cannot see (pp. 198, 203)
- [[file-comparison-hash]] — Alice and Bob compare 32-bit hashes; false-negative probability 2^{−M} (p. 199)
- [[md5]] — widely used 128-bit one-way hash (p. 200)
- [[newton-hooke-anagram-hash]] — alphabetizing a claim as a secret-publication hash (p. 200)
- [[dna-binding-protein-specificity]] — unique-site length L > log N/log 4 gives about 16 nucleotides (p. 204)
- [[parsons-code]] — U/R/D hash of a melody (p. 204)

## Bridges (candidates)
- [structural-analogy] random hash into M < N bits ↔ information-theory: random codes in channel coding — same random-code idea, but here mapping down instead of up.
- [same-math] bit-by-bit match, ratio 2^r ↔ bayesian: sequential updating with likelihood ratios — odds multiply by the likelihood ratio.
- [same-math] expected collisions S(S−1)/(2T) ↔ the birthday problem, exercise 9.20 — the book itself notes the similarity (p. 198).
- [structural-analogy] "Fiona needs 2^M, Alice 2^{M/2}" ↔ attack on a fixed target vs. any matching pair — the square-root gap comes from counting pairs.
- [metaphor] hash as short fingerprint of a long object ↔ Kolmogorov-style short description — both name a long object compactly.

## Questions this raises
- How should buckets be sized when a table is deliberately small? How do the expected bucket length and search cost depend on S/T?
- Real names and files are not random. How much does the "ideal random hash" analysis fail for realistic data and hash functions?
- Is a near-perfect error-correcting code needed after hash-based error detection, or is retransmission enough?
- How does "hashing to 2^{M/2} trials" translate into practical safe hash lengths as computing power grows?

## Exercises worth doing
- Ex. 12.1 (p. 194) — average vs. worst-case cost of a raw list; early termination of comparison — difficulty: medium
- Ex. 12.3 (p. 198) — expected collisions and table size M for ideal random hashing; the S² vs S scaling — difficulty: medium
- Ex. 12.5 (p. 198) — evidence given by a casting-out-nines match; depends on the error model — difficulty: easy
- Ex. 12.10 (p. 201) — how long a text or melody must be to be unique; collision counting — difficulty: medium
- Ex. 12.11 (p. 201) — information-theoretic lower bound on regulatory protein size — difficulty: hard

## Reading notes
- Printed page = pdf page − 12 (pdf 204 = printed 192).
- Algorithm 12.3 code, as printed, sets h1 = *x and h2 = *x + 1 before the loop, while the prose says the two running totals start at 0 and 1 (p. 195); the difference is noted here without being resolved.
- p. 199: the text layer flattens the exponent as "10 −10" (a stray "2" sits at the end of the preceding line); I read the value as about 10^{-10}. Check: 2^{-32} ≈ 2.3×10^{-10} (added check).
- Solution 12.7 (p. 203): the author's "≃ 23 × 8 ≃ 180" is a rough estimate. 23 × 8 = 184, and the exact binomial would be somewhat smaller (added check).
- Solution 12.10 (p. 203): 23^4 = 279 841, which the author rounds to "250 000".
- The unit includes the solutions section (12.7), summarised here by final results. Exercise 12.9 has no printed solution.
