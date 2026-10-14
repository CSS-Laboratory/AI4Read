---
id: stone-2022-information/ch01-information
work: stone-2022-information
unit: "1 What Is Information?"
pages: 1-20
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# What Is Information?

## L0 — One line
One bit is the information needed to choose between two equally probable alternatives, and a bit (an amount of information) is a different kind of thing from a binary digit (a 0 or a 1).

## L1 — The gist (≤ 120 words)
Question: what is information, and how can it be measured? Answer: one bit is the information needed to choose between two equally probable alternatives, so choosing among m such alternatives needs log2 m bits. Telegraphy and images illustrate that predictable structure (redundancy) lets a message be compressed. A bit is an amount of information; a binary digit is only a 0 or 1, and may carry less than one bit. In the chapter's grey-level image, the author estimates that each binary digit of a displayed pixel carries on average about half a bit. This sets up the quantitative theory of later chapters.

**Prerequisites:** powers of 2; the idea of a logarithm as "the power needed" (the chapter explains it); reading histograms.

## L2 — Key ideas
- Shannon's 1948 paper made information a well-defined, measurable quantity, though the theory is subtle and "full of caveats" (p. 2).
- One bit chooses between two equally probable alternatives. $n$ bits choose among $m=2^n$ alternatives, so $n=\log_2 m$ (pp. 5, 7).
- Twenty well-chosen yes/no questions, each halving the possibilities, can single out one of $2^{20}=1{,}048{,}576$ words (p. 9).
- A bit and a binary digit are different types of entity. A binary digit can carry less than one bit, for example when its value is partly predictable (p. 10).
- Morse gave common letters short codewords (the dot-dash patterns that stand for letters). This makes better use of a single wire, and it raises the question of how to tell whether a channel is used as efficiently as possible (pp. 12–13).
- How efficient an encoding method is depends on the structure of the data (pp. 14–15).
- Difference coding (sending the differences between neighbouring pixel values) exploits redundancy between neighbouring pixels. On the chapter's example it saves 12.5% (7 instead of 8 binary digits per pixel, with the cost of rare large differences assumed to be zero), and the image can be rebuilt exactly (pp. 16–18).
- The author's picture of information: what remains after redundancy and noise are removed (p. 20).

## L3 — Walkthrough

### 1.1 Introduction (pp. 1–2)
- The author says information is at least as important as physical quantities like mass and velocity. He names computers, evolution, physics, AI, quantum computation and the brain, and says their behaviour is determined mainly by how they process information (p. 1).
- Before Shannon (1948), information was seen as a poorly defined "miasmic fluid". Afterwards it was seen as well-defined and measurable (p. 2).
- Unlike the Darwin–Wallace theory, information theory "is not simple". The author says many caveats can be disregarded if we keep to the physical interpretation of its defining equations. This is his guiding principle (p. 2).

### 1.2 Information, Eyes and Evolution (pp. 2–3)
- Shannon's theory gives a mathematical definition of information and says how much can be communicated between elements of a system. It underlies why signals and noise are related and why there are limits on communication rates (p. 2).
- Data is a mix of useful signal and useless noise. Separating them lets a TV picture be compressed, sent and decompressed (pp. 2–3).
- The efficient coding hypothesis *suggests* that sense organs and brains evolved mainly to minimise the energy spent per bit acquired. Computational neuroscience uses information theory as a benchmark for neurons (p. 3).
- Natural selection is "essentially" a way to incorporate information about the environment into DNA. The author says it "seems likely" that sex speeds this up (p. 3). Applications come in Chapter 11 (p. 3).

### 1.3 Finding a Route, Bit by Bit (pp. 3–7)
- **Definition.** Information is usually measured in bits. One bit lets you choose between two equally probable alternatives. A bit is *not* a binary digit, as the text will show (p. 3).
- **Forks.** At fork A (Fig. 1.2) you have no prior information, so left and right are equally probable. A binary digit (0 = left, 1 = right) then gives one bit (p. 4). At fork B another digit gives another bit. After two forks you have chosen among 4 $=2\times2=2^2$ alternatives, using two bits. After three forks you have chosen among 8 $=2^3$, using three bits (pp. 4–5).
- Each decision halves the number of remaining destinations (p. 5).
- With $n$ forks and $m$ final destinations:
$$m = 2^n \tag{1.1}$$
- Each fork needs one bit, so $n$ forks need $n$ bits, giving $2^n$ equally probable alternatives (p. 5).
- **Binary numbers.** Each binary digit says how many 1s, 2s, 4s… there are, just as decimal digits count 1s, 10s, 100s… (p. 6).
$$(1\times100)+(0\times10)+(1\times1)=101 \tag{1.2}$$
$$(1\times4)+(0\times2)+(1\times1)=5 \tag{1.3}$$
- Table 1.1 lists 0–7 as 000–111. The binary label of a destination (e.g. 011) spells out the left/right instructions to reach it (p. 6).
- **Logarithms.** The logarithm of $m$ is the power to which 2 must be raised to get $m$. Here $\log_2 8=3$ (p. 7). All logs in the book are base 2 unless stated otherwise (p. 7).
$$n=\log_2 m \tag{1.4}$$
- **Key point (p. 7).** With $n$ bits you can choose among $m=2^n$ equally probable alternatives. Equivalently, choosing among $m$ equally probable alternatives needs $n=\log_2 m$ bits.
- *Intuition note.* Each bit cuts the set of possibilities in half. Counting how many halvings are needed to reach one item gives $\log_2 m$. The word "equally probable" matters, because the rule is stated only for that case.

### 1.4 A Million Answers to Twenty Questions (pp. 8–10)
- In '20 questions', each yes/no question gives at most one bit. It gives exactly one bit if it halves the remaining possible words. A question whose answer you already know, such as "Is the word in the dictionary?", gives no information (p. 8).
- Three-question version (Fig. 1.3): the opponent has one of 8 words (Fish, Bird, Dog, Cat, Car, Van, Truck, Bus). Example questions are "Is it inanimate?", "Is it a mammal?", "Is it 'cat'?". Each halves the options (8 → 4 → 2 → 1). The answers (no=0, yes=1) form a binary number labelling the word (pp. 8–9).
- Realistic case: suppose the vocabulary has 1,048,576 words. Ideal questions halve it: 524,288, 262,144, …, 2 words after question 19, 1 word after question 20. This works because $1{,}048{,}576=2^{20}$, so 20 bits narrow about a million words to one (p. 9).
- Each extra question can double the number of words handled. In principle, 40 questions handle $2^{40}\approx10^{12}$ words (p. 9). In the road picture, 40 bits mean 40 forks and about a trillion possible routes (p. 10).
- *Intuition note.* A good question is one whose answer you cannot predict. A predictable answer carries no information.

### 1.5 Information, Bits and Binary Digits (pp. 10–11)
- A binary digit is the value of a binary variable (0 or 1) and is "not information per se". A bit is a definite amount of information. Confusing the two is called a **category error** (p. 10).
- Three cases (p. 10):
  - You already know to go left, and I show you 0. You have a binary digit but gain no information.
  - You have no idea, and I show you 0. You gain one bit.
  - You are told there is a 71% probability that left is right, and I confirm with a 0. You gain less than one bit; the author says precisely half a bit (he refers to Section 5.8 for this; it is not derived here).
- So a binary digit can convey half a bit, even though half a binary digit does not exist (p. 10).
- Even some of the best textbooks use the two terms interchangeably. Experienced readers can cope, but novices are confused. MacKay (2003) proposed calling the unit of information the Shannon (pp. 10–11).
- **Key point (p. 11).** A bit is the amount of information needed to choose between two equally probable alternatives. A binary digit is the value of a binary variable, 0 or 1.
- *Intuition note.* A binary digit is like a container and a bit is like the amount it actually holds. The container may be full, half full or empty, depending on what the receiver already knew.

### 1.6 Example 1: Telegraphy (pp. 11–13)
- A naive 1820 scheme uses 26 electric lines (one per letter) to carry upper-case letters from London to Manchester, about 200 miles. Breaks are costly to find, so fewer lines mean fewer failures (p. 11).
- Cooke and Wheatstone devised a complicated two-needle system that could send only 23 different letters (p. 11). It led to the arrest of John Tawell on 1 January 1845. The telegram misspelled JUST as "GUST" and QUAKER as "KWAKER", because J, Q and Z were missing (p. 12). The press coverage "established the practicality of telegraphy" (p. 12).
- In the 1830s Morse and Vail developed the first version of what became Morse code. Because it writes each letter as dots and dashes, it could be used to send messages over a single line (p. 12).
- Morse code gives short codewords to common letters and longer ones to rare letters (Table 1.2: E is one dot, J is dot plus three dashes). Morse found letter frequencies by counting the type in a printer's workshop (pp. 12–13).
- This makes efficient use of the channel (one wire). The author asks: how can we tell whether a channel is used as efficiently as possible? (p. 13)

### 1.7 Example 2: Binary Images (pp. 13–15)
- Images are internally predictable. In Fig. 1.4 (night sky), almost all pixels are black with an occasional white star, so most adjacent pairs are also black (p. 13).
- Three ways to send a 100×100 black/white image (pp. 13–14):
  - **A:** send every pixel, 0 for black and 1 for white. This needs 10,000 digits, mostly long runs of 0s.
  - **B:** send the (row, column) of each white pixel, e.g. $[(19,13),(22,30),\dots]$.
  - **C:** send the number of black pixels before the next white one. A first row beginning 000000000000010000000001… (24 digits) is coded $[13,9,\dots]$.
- B and C do not send the image but send all the information needed to rebuild it. All three give identical results and differ only in efficiency (p. 14).
- Which is best depends on image structure. For a single white pixel in the centre, A needs 10,000 values. B needs (50, 50) and C needs 5,050, so both need four decimal digits (p. 14).
- Fig. 1.5 has large regions of pure black or pure white. Here the better scheme is **run-length encoding**: send the number of pixels before each change of colour. The example is $[87,31,18,\dots]$ (p. 15). The image can be reconstructed if we know the method used (p. 15).

### 1.8 Example 3: Grey-Level Images (pp. 15–20)
- **Setup.** Take 100×100 pixels with 256 grey-levels, each an 8-digit binary number (Fig. 1.6). Nearby pixel values are similar but not identical, so adjacent values are not independent and the image has redundancy (pp. 15–16).
- **Difference coding.**
  - Concatenate the rows into one row of 10,000 pixels and take differences between adjacent grey-levels. This gives 9,999 differences (p. 16).
  - The histogram of differences (Fig. 1.8b) peaks near 0 and rarely exceeds ±63 (p. 16).
  - So almost all differences lie in $[-63,\dots,63]$, which is 127 values. Seven binary digits suffice since $7=\log 128$, with one spare value (p. 17).
  - Rare larger differences are listed separately, with location (2×7 binary digits) and grey-level (8 digits). The author treats the cost of this "housekeeping" as negligible and assumes it is zero (pp. 16–17).
- **Reconstruction.** $x_2=x_1+d_1$. For example, with $x_1=5$ and $d_1=10$, $x_2=15$. Then $x_3=x_2+d_2$, and so on. The first pixel's grey-level (8 digits) must also be known (p. 17).
- Since the original can be rebuilt from the differences, the author says this "proves" both contain exactly the same amount of information (p. 18).
- **Saving.**
  - Naive method: 8 digits × 10,000 pixels = 80,000 digits.
  - Difference coding: 7 digits per difference value, a total of 70,000 digits (as the text gives it; there are 9,999 differences, p. 16).
  - Saving: 10,000 digits, or 12.5% (p. 18).
- Telephone voice transmission uses a form of difference coding (differential pulse code modulation). It cuts 8 binary digits per value to 5 (p. 18).
- **Histogram bounds.** A histogram of data values gives an upper bound on the average information per value (justified in later chapters, p. 18). Fig. 1.6b gives 7.84 bits/pixel. Fig. 1.8b gives 5.92 bits/pixel (p. 18).
- Both images hold the same information, and the difference image holds no more than 5.92 bits/pixel. So the original holds no more than 5.92 bits/pixel (pp. 18–19).
- The author says Shannon's work guarantees that if each pixel carries on average 5.92 bits, then no more than 5.92 binary digits per pixel are needed. This is still only an upper bound. The smallest number of binary digits needed equals the information per pixel in bits (p. 19).
- **Real file sizes.**
  - The image is 344 × 299 = 102,856 pixels, one byte each when displayed.
  - Its file holds 45,180 bytes.
  - Compression factor: $102856/45180=2.28$ without information loss.
  - That is about four binary digits per pixel on disk instead of eight (p. 19).
- The author concludes that each 8-digit displayed pixel holds on average only about 4 bits of information, so each binary digit holds about half a bit. He says a fraction of a bit is well defined, and promises more in Chapter 5 (p. 20).
- *Intuition note.* Eight digits per pixel is the cost of displaying the image without using its structure. The compressed file shows that the true information content is smaller. The gap between digits used and bits carried is redundancy.

### 1.9 Summary (p. 20)
- Binary choices need information in the form of yes/no answers. Increasing the number of choices from 2 to 26 to 256 let whole images be sent down one wire as binary digits. In each case redundancy allowed compression before sending (p. 20).
- A binary digit does not necessarily give one bit, and it is not the same type of entity as a bit (p. 20).
- **Author's answer to "what is information?"** It is what remains after all natural redundancy and noise have been removed from a message (p. 20).

## Toy example (ours, not from the text)
**A. Bits.** A game has 16 equally probable words. $16=2^4$, so $\log_2 16=4$, so 4 ideal questions are needed: 16 → 8 → 4 → 2 → 1.

**B. Digits versus bits.** Suppose the answer to a question is 0 and you were already 100% sure of it. You received a binary digit but 0 bits.

**C. Difference coding.** Six pixels have grey-levels $x=(100,\,101,\,101,\,103,\,102,\,102)$.
- Differences: $d_1=101-100=1$, $d_2=0$, $d_3=103-101=2$, $d_4=102-103=-1$, $d_5=0$. So $d=(1,0,2,-1,0)$.
- Naive cost: $6\times8=48$ binary digits.
- Difference cost: first pixel $8$ digits, plus $5\times7=35$ digits, which is $43$ digits.
- Rebuild: $x_2=100+1=101$, $x_3=101+0=101$, $x_4=101+2=103$, $x_5=103-1=102$, $x_6=102+0=102$. The original is recovered exactly, so no information was lost.

## Concepts
- [[bit]] — the amount of information needed to choose between two equally probable alternatives (pp. 3, 5, 11)
- binary-digit-vs-bit (new) — a binary digit is the value 0 or 1 of a binary variable. It is a different type of entity from a bit and may carry less than one bit (p. 10)
- [[redundancy]] — dependence between neighbouring data values (e.g. similar pixels) that allows compression (p. 15)
- [[self-information / surprisal]] — only hinted at here: a predictable answer gives no information (p. 8); the formal quantity comes later
- logarithm-as-bit-count (new) — $n=\log_2 m$ is the number of binary decisions needed to choose among $m$ alternatives (p. 7)
- variable-length-code (new) — Morse's idea of short codewords for common letters, long ones for rare letters (p. 12)
- run-length-encoding (new) — send the lengths of runs between changes instead of the pixels (p. 15)
- difference-coding (new) — send differences between adjacent values and rebuild by adding them back (p. 16)
- [[source coding theorem]] — only hinted at here: the author says Shannon's work guarantees that if each pixel carries on average 5.92 bits, it can be represented with no more than 5.92 binary digits per pixel (p. 19); the theorem is not named or stated in general form
- efficient-coding-hypothesis (new) — suggestion that sense organs and brains evolve mainly to minimise energy per bit acquired (p. 3)

## Canonical instances
- [[road-fork-navigation]] — each fork is one bit; $n$ forks pick one of $2^n$ routes (pp. 3–5)
- [[twenty-questions]] — 20 halving questions pick one of $2^{20}$ words (pp. 8–9)
- [[morse-code]] — letter frequency sets codeword length (pp. 12–13)
- [[cooke-wheatstone-telegraph]] — 23-letter two-needle system and the Tawell arrest (pp. 11–12)
- [[hubble-night-sky-image]] — methods A, B and C for a mostly black binary image (pp. 13–14)
- [[grey-level-difference-coding]] — 80,000 vs 70,000 binary digits; 7.84 vs 5.92 bits/pixel bounds; 2.28× file compression (pp. 16–19)

## Bridges (candidates)
- [structural-analogy] halving the options with each yes/no question ↔ computer science: binary search — each comparison halves the candidates
- [structural-analogy] Morse's short codes for common letters ↔ Huffman coding (listed in the concept spine) — code length matched to frequency
- [structural-analogy] difference coding of pixels ↔ time-series differencing — removes dependence between neighbours
- [metaphor] efficient coding hypothesis ↔ neuroscience: neurons as channels with an energy cost per bit

## Questions this raises
- How is the information of an outcome measured when the alternatives are *not* equally probable (e.g. the 71% case)?
- How can one compute the upper bounds (7.84 and 5.92 bits/pixel) from a histogram, and how tight are they?
- Can we find the smallest possible code for a source, and how would we know when we have reached it?
- What changes when noise corrupts the transmitted digits?

## Reading notes
- Printed page = pdf − 16 (pdf 17 = printed 1). Page labels give printed numbers directly.
- The telegram on p. 12 reads "A MURDER HAS GUST BEEN COMMITTED…" in both text and image. The text explains the unusual spellings (JUST and QUAKER) as the telegrapher doing his best without the letters J, Q and Z.
- The text says the 71% case gives "precisely half a bit" but defers the proof to Section 5.8, so it is not derived in this unit.
- The statement that a histogram bounds the information per value is also deferred to later chapters (p. 18).
- Superscript citation numbers in the text refer to a reference list outside these pages.
- There are no exercises in this unit.
