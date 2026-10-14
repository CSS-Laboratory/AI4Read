---
id: pierce-1980-introduction/ch04-encoding
work: pierce-1980-introduction
unit: "4 Encoding and Binary Digits"
pages: 64-77
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Encoding and Binary Digits

## L0 — One line
Messages such as text and numbers, and speech after sampling and quantizing, can be turned into strings of binary digits, and how many digits it needs depends strongly on the chosen code, which hints that a "best" code might define the amount of information.

## L1 — The gist (≤ 120 words)
Pierce thinks that we can appreciate the need for a measure of information only after seeing in some detail how messages are encoded. Pierce explains that a continuous signal can be sampled and quantized, which turns it into a sequence of discrete characters. Letters and numbers can then be written as strings of binary digits (0/1, pulse/space). The number of digits needed depends strongly on the code. In his examples, coding blocks of characters, or whole words, uses fewer digits than coding letter by letter. This suggests that a best code may exist. Its average number of binary digits per character could then serve as the measure of information in a source. That idea is left for the next chapter.

**Prerequisites:** powers of 2 and of 10; place-value notation; the idea of a message source producing characters one after another.

## L2 — Key ideas (5–10 bullets)
- "Encoding" means accurately representing one thing by another. It covers secret codes, the genetic "text" (as some assert), radio waves for music, and Morse code. The engineer needs a standard for judging good and bad encoding, and the study of transmission has given a new general understanding of encoding (pp. 64–65).
- The sampling theorem lets a continuous signal be replaced by samples taken at equal intervals. At least $2f$ samples per second are needed to describe perfectly a signal whose frequency range is $f$ (p. 67).
- Quantizing, which means rounding each sample to a whole number, turns a continuous signal into a discrete one. Speech needs only about 1 per cent accuracy (p. 68).
- A pulse or a space, a yes or a no, a 1 or a 0 is one binary digit. $n$ digits give $2^n$ patterns, and each added digit doubles the count (pp. 68–70).
- Which number a pattern stands for does not matter for transmission. A pattern can be read as a sequence of left/right choices on a tree that selects one alternative (pp. 73–74).
- A choice among 27 symbols corresponds to about 4.75 digits, and among 50 symbols to about 5.62. Codes with a whole number of digits per symbol waste patterns (pp. 74, 77).
- Block coding wastes less. Three characters of a 50-symbol set fit in 17 digits instead of 18 (pp. 74–75).
- Coding whole English words (14 digits per word) beats coding letters (27.5 digits per word) if spelling out is rare, because word coding restricts itself to real words (p. 75).

## L3 — Walkthrough

### Opening: what encoding is (pp. 64–66)
- Sources such as text, speech, music, pictures or television are treated as ergodic sources of characters or signals (p. 64; "ergodic" is not explained on these pages). A chief aim of information theory is to study how their sequences can be encoded most effectively for transmission (p. 64).
- Cryptography hides a message by substituting code-book words, or, in a cipher, letters or numbers (p. 64).
- Pierce also counts as encoding the following examples. Geneticists believe the plan of a human body is written in the chromosomes, and some assert that this "text" is an arrangement of four bases in DNA, which produces an equivalent RNA text and then proteins made of sequences of twenty amino acids. Morse code, FM waves for music, telephone currents for speech, and sound waves for the vocal-tract motions that produce them are further cases (p. 65).
- Pierce asserts that geneticists were led to such considerations by information theory (p. 65).
- Nature fixes the vocal-tract-to-speech encoding, but the engineer may choose how speech is encoded in electric current. The engineer therefore needs a standard for good encoding (p. 65).
- The new ideas are a measure of amount of information, called entropy, and its unit, the bit. Pierce first wants the reader to see the coding problem (p. 66).

### Continuous signals: sampling and quantizing (pp. 66–68)
- Speech and music are variations of a signal with time (Fig. IV-1a). Information theory would be of limited value if it were not applicable to them as well as to discrete messages (p. 66).
- **Sampling theorem** (used, not proved): a continuous signal can be fully represented, and perfectly rebuilt, from amplitude samples at equally spaced times. The interval must be at most half the period of the highest frequency present (pp. 66–67).
- Examples: a voice signal up to 4,000 cycles per second needs 8,000 samples per second. A television signal up to 4 million cycles per second needs 8 million samples per second. In general at least $2f$ samples per second are needed (p. 67).
- Samples can still take any of infinitely many amplitudes. A signal need not be reproduced perfectly, and real apparatus cannot do so (pp. 67–68).
- For speech, about 1 per cent accuracy is enough. One may then use the integers 0 to 99 and replace each sample by the nearest of the hundred (p. 68).
- **Result:** sampling plus quantizing turns coding a continuous signal into coding a sequence of discrete characters (p. 68).

*Intuition note:* A smooth wave can be stored as a list of numbers if you measure it often enough. Rounding the numbers loses a little accuracy but leaves a list of ordinary symbols.

### Pulses, spaces and binary numbers (pp. 68–72)
- Teletypewriters send a pattern of pulses and spaces for each key. Pulses and spaces can also have equal length at regular intervals (Fig. IV-2). Sequence a is pulse-space-space-pulse-space-pulse. Sequence b is pulse-pulse-pulse-space-pulse-pulse (p. 68).
- Each interval holds one of two possibilities. These can be written yes/no, +/−, or 1/0 (pp. 68–69).
- Decimal: $315 = 3\times10^2+1\times10^1+5\times1$. Binary: 1 0 0 1 0 1 (sequence a) $= 1\times2^5+0\times2^4+0\times2^3+1\times2^2+0\times2+1\times1 = 32+4+1 = 37$ (p. 69).
- Leading zeros do not change the value: $0016=16$ and $001010=1010$ in binary (pp. 69–70). Each 0 or 1 is a *binary digit*. A pulse or space in one interval is one binary digit (p. 70).
- Table VI lists the 8 three-digit binary numbers, 000 to 111, which stand for 0 to 7. Since $8=2^3$, a list of $n$-digit patterns is $2^n$ successive binary numbers starting at 0 (p. 70).
- Table VII gives $2^n$: 4 for $n=2$, 8 for 3, 16 for 4, 32 for 5, 1,024 for 10, and 1,048,576 for 20 (p. 71).
- The count doubles with each added digit: all old sequences preceded by 0, plus all old sequences preceded by 1 (p. 70).
- **Octal system** (digits 0–7): $356_8 = 3\times8^2+5\times8+6\times1 = 192+40+6 = 238$ (p. 71).
- Binary-to-octal conversion replaces each block of three binary digits by one octal digit: 010 111 011 110 becomes 2736. Octal digits can be sent as pulses of amplitudes 0–7. Fig. IV-3b sends 2, 7, 3, 6 as four pulses (p. 71).
- Binary-to-decimal conversion is harder. On average about 3.32 binary digits are needed per decimal digit. Assigning 4 digits per decimal digit (Table VIII) wastes patterns (p. 72).

*Intuition note:* $n$ on/off signals can name $2^n$ different things. Octal is a shorthand where three on/off signals are read together as one symbol.

### Binary digits as choices (pp. 73–74)
- For transmission, the number assigned to a pattern is irrelevant. Table IX assigns octal digits to the patterns in a scrambled order: 000→5, 001→7, 010→1, 011→6, 101→4, 110→2, 111→3 (p. 73). The row for 100 is lost in the text layer. By elimination it is 0, which agrees with the leaf string 57160423 printed above the tree in Fig. IV-4 (p. 74) (added step).
- Alternatively each digit is an elementary choice between two possibilities. In the "tree of choice" (Fig. IV-4), 0 means left branch and 1 means right branch, going up from the root. 0 1 1 (left, right, right) reaches octal digit 6, as in Table IX (p. 73).
- So 3 digits pick one of 8 alternatives, 4 digits one of 16, and 20 digits one of 1,048,576, with numbers assigned in any order (p. 73). The alternatives need not be numbers (p. 74).

### Encoding English text (pp. 74–75)
- Minimum case: 26 letters plus space, 27 symbols, with no punctuation or numerals (these can be spelled out). Pierce says a choice among 27 symbols corresponds to about 4.75 binary digits. Using 5 digits per symbol leaves $32-27=5$ patterns unused (p. 74).
- A 48-key typewriter plus carriage return and line advance gives 50 symbols. Pierce gives about 5.62 digits per choice. Using 6 digits per character wastes patterns: there are only 32 five-digit numbers (too few) and 64 six-digit numbers (too many) (p. 74).
- **Block coding:** 3 ordered characters have $50^3=125{,}000$ possibilities. There are $2^{17}=131{,}072$ seventeen-digit numbers, so 17 digits specify any block with a few patterns left over. Six digits per character would need 18 digits for 3 characters. The saving is a factor 17/18 (pp. 74–75).

*Intuition note:* Coding one symbol at a time rounds up to a whole number of digits every time. Coding several symbols at once rounds up only once, so less is wasted.

### Words versus letters (p. 75)
- A vocabulary of 16,384 words is large. There are exactly $2^{14}=16{,}384$ fourteen-digit numbers. Assign 16,357 to words and 27 to letters and the space, so that unlisted words can be spelled out. A space is assumed to follow each listed word (p. 75).
- If spelling is needed only rarely, this uses about 14 digits per word (p. 75).
- Letter by letter, English has about 4.5 letters per word plus a space, giving 5.5 characters per word. At 5 digits per character this is 27.5 digits per word (p. 75).
- Reason: letter-by-letter coding provides for all letter sequences with equal facility, while word-by-word coding restricts itself to English words. The digits needed per word depend strongly on the code (p. 75).

*Intuition note:* A code that reserves room only for sequences that really occur needs fewer digits than one that allows every possible sequence.

### Looking ahead and chapter review (pp. 76–77)
- Pierce suggests that there may exist in principle a best code, requiring on average fewer binary digits per character or per second than any other. The average number of digits it needs could then measure the amount of information per character or per second. This is what information theory does, and the next chapter takes it up (p. 76).
- Review (p. 76): coding means representing one signal by another. Continuous signals are sampled with $2f$ samples per second and then quantized. Four binary digits give 16 numbers, of which 10 can stand for the decimal digits. Five binary digits give 32, of which 27 can stand for letters plus space. The numerical value of a pattern has no significance.
- Waste example (p. 77): 6 four-digit patterns are never used when 10 decimal digits are coded in 16 patterns. Block coding avoids this. Three decimal digits fit in 10 binary digits, against 12 digits when coded separately.
- Any decimal-digit sequence can occur, but only certain letter sequences (the words) occur in English. Thus coding words is more efficient than coding letters, which again emphasizes the gain from coding sequences of characters rather than single characters (p. 77).

## Toy example
(Ours, not from the text.) A source uses 5 symbols: A, B, C, D, E.
- One symbol at a time: $2^2=4<5$ but $2^3=8\ge5$, so 3 digits per symbol. Cost: 3 digits per symbol.
- Blocks of 2: $5^2=25\le 2^5=32$, so 5 digits per pair. Cost: $5/2=2.5$ digits per symbol.
- Blocks of 3: $5^3=125\le 2^7=128$, so 7 digits per triple. Cost: $7/3\approx2.33$ digits per symbol.
In these three cases longer blocks cost fewer digits per symbol, because rounding up happens only once per block (the same idea as the 17/18 saving, p. 75). This is not guaranteed for every block length: blocks of 4 need $2^{10}=1024\ge625=5^4$, so 10 digits, i.e. 2.5 per symbol.

## Concepts
- [[bit]] — named on p. 66 as the unit of the measure of information (called entropy); this chapter does not define either term. It does describe the binary digit (p. 70) as an elementary choice between two possibilities (p. 73).
- [[encoding]] (new) — accurate representation of one signal or message by another (pp. 64, 76).
- [[sampling-theorem]] (new) — a signal can be perfectly rebuilt from equally spaced samples, at least $2f$ per second when its highest frequency is $f$ (p. 67).
- [[quantization]] (new) — rounding each sample amplitude to the nearest of a limited set of whole numbers (p. 68).
- [[binary-numeral-system]] (new) — place-value notation with only the digits 0 and 1 and powers of 2 (p. 69).
- [[block-coding]] (new) — encoding groups of 2, 3 or more characters together to reduce wasted patterns (pp. 74–75, 77).
- [[tree-of-choice]] (new) — each binary digit as a left/right branch choice that selects one alternative (p. 73).
- [[redundancy]] — not named in this unit. The word-versus-letter comparison (p. 75) concerns restricting codes to sequences that actually occur.

## Canonical instances
- [[morse-code]] — English letters sent as short and long pulses and spaces (pp. 65, 68).
- [[genetic-code]] — the DNA/RNA "text" of four bases and its re-encoding into proteins of twenty amino acids, as some assert (p. 65).
- [[english-27-symbol-code]] — 26 letters plus space coded in 5 binary digits, 5 patterns unused (p. 74).
- [[typewriter-50-symbol-block-code]] — 3 characters in 17 digits instead of 18 (pp. 74–75).
- [[word-vs-letter-coding]] — 14 digits per word against 27.5 (p. 75).

## Bridges (candidates)
- [structural-analogy] Block coding saving ↔ information-theory: typical set / source coding theorem — long blocks let the code use only the likely sequences.
- [structural-analogy] Word-level code reserving patterns only for real words ↔ information-theory: redundancy — a restricted set of sequences leaves room to compress.
- [same-math] Sampling at $2f$ ↔ signal processing: sampling-rate limit for band-limited signals — the same $2f$ rule.
- [structural-analogy] Quantizing to ~1% accuracy ↔ information-theory: rate–distortion — accept small error to save digits.

## Questions this raises
- What exactly is the "best" code, and how can one compute the least average digits per character for English?
- How much better than 14 digits per word can we do if we also use word frequencies or context?
- Can quantization error be measured and traded against the number of digits?
- Why is the count of digits tied to $\log_2$ of the number of alternatives (4.75 for 27, 5.62 for 50)?

## Reading notes
- **Edition:** this PDF is the 1961 Harper & Brothers first edition, titled *Symbols, Signals and Noise*, not the 1980 Dover text named in the work citation (this comes from the source notes supplied with the unit; the pages themselves show only the running header). The running header reads "Symbols, Signals and Noise". Page numbers cited are those printed in this scan. Printed = pdf − 16.
- **Chapter number:** the heading is OCR'd as "CHAPTER 1 V"; the figure and table labels on these pages use "IV" (Fig. IV-1 to IV-4).
- **OCR:** the text layer drops many zeros and some table rows, for example "0 to 99", binary strings, Tables VI, VIII and IX, and the n=1 row of Table VII. I filled these from context and the image of p. 69. The row for 100 in Table IX is lost in the text layer and is inferred by elimination (see L3).
- **Misprint:** the summary says "10 of the 16 possible 5-digit binary numbers" (p. 77). 16 patterns are 4-digit patterns, as on p. 76, so this is either a misprint or an OCR error; the text layer alone cannot settle which.
- **Check:** by our arithmetic $\log_2 50\approx5.64$, while the text gives about 5.62 (p. 74). Pierce says 4.75 for 27 symbols and 3.32 digits per decimal digit, which agree with $\log_2 27$ and $\log_2 10$.
