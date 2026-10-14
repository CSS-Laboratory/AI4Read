---
id: pierce-1980-introduction/app-mathematical
work: pierce-1980-introduction
unit: "Appendix: On Mathematical Notation"
pages: 278-286
fields: [information-theory]
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
# Appendix: On Mathematical Notation

## L0 — One line
Mathematical notation is shorthand for ideas that could be said in words, and this appendix teaches the shorthand the book uses: probabilities, sums, exponents and base-2 logarithms.

## L1 — The gist (≤ 120 words)
Pierce says the book's mathematics is not the same thing as its notation. Its purpose is to make the mathematics easier, for anyone who becomes familiar with it. The appendix explains the symbols used in the book. It covers letters as labels, arithmetic signs and parentheses, probabilities p(x), p(x,y) and p_x(y), the rule p(x,y) = p(x)p_x(y), summation, exponents, and logarithms. In the book "log" means base 2, with exceptions noted in Chapter X. The appendix gives the log rules, the conversion factors to base 10 and base e, and the approximation log_e(1+x) ≈ x for small x.

**Prerequisites:** high-school arithmetic, fractions, the idea of a proportion or frequency, and powers such as 2³.

## L2 — Key ideas (5–10 bullets)
- Notation is not mathematics. Mathematics can be done in words, and notation can also stand for nonsense (pp. 278–279).
- A letter can stand for a number or for another object, such as a group of symbols. An index j says which one (p. 279).
- Parentheses make a quantity count as one number. Saying the word "quantity" aloud when reading avoids confusion (p. 280).
- p(x) is the fraction of a long passage that is x. p(x,y) is a joint probability (x and y together) and p_x(y) a conditional one (y when x occurs). They are linked by p(x,y) = p(x)p_x(y) (pp. 280–282).
- The sign Σ means adding the terms for a range of values of an index (all values, if no limits are written). Summing p(i,j) over j gives p(i), and summing all letter probabilities gives 1 (pp. 282–284).
- Exponents obey aⁿaᵐ = a^(n+m) and a⁻ⁿ = 1/aⁿ. A ½ power is a square root (pp. 284–285).
- log x is the power to which 2 must be raised to get x. This gives 2^(log x) = x and turns products into sums (pp. 285–286).
- Base conversion uses log₂x = 3.32 log₁₀x = 1.44 log_e x, and log_e(1+x) ≈ x for small x (p. 286).

## L3 — Walkthrough

**Purpose of notation (pp. 278–279).** Communication theory is a mathematical theory, so the book must contain mathematics (p. 278). The Babylonians and Indians did much mathematics, including parts of algebra, with only words and sentences (p. 278). Notation came later. It replaces long repeated word-strings with signs, names quantities, and shows relations at a glance (p. 278). It only represents mathematics, as letters represent words or notes represent music. It can also represent nonsense, as in the tracts of crackpots (pp. 278–279). Pierce says he tried to put all the important ideas into words, and in most cases also put them into notation (p. 279).

**Letters as labels (p. 279).** Letters can stand for numbers and other things. In Chapter V a letter stands for a group of symbols, and j says which group. For j = 1 the group might be AAA, and for a larger value of j (given as 121 in the text) it might be ZQE (p. 279).

**Arithmetic signs (pp. 279–280).**
- Addition: 2 + 3, a + d ("a plus d") (p. 279).
- Subtraction: 5 − 4, q − r (p. 279).
- Multiplication: 3 × 5, 3·5, (3)(5); u × v, u·v, uv. Without parentheses, "35" would read as thirty-five. uv is read "uv", not "u times v" (pp. 279–280).
- Division: 6 ÷ 3, 6/3 as a fraction, 1/p, read "1 over p" (p. 280).
- Parentheses make one number:
$$\frac{(2+4)}{3}=\frac{6}{3}=2,\qquad (4+8)(2)=(12)(2)=24,\qquad (a+b)c=ac+bc$$
Say "c times the quantity a plus b" to mean c(a+b). Without the word "quantity", the spoken phrase could be taken to mean ca + b (p. 280).

*Intuition note:* Notation is a convention for reading. The parentheses and the spoken "quantity" tell you which numbers belong together.

**Probabilities (pp. 280–282).**
- The probability of the jth symbol is p(j), read "p of j". Table XVI assigns numbers j to letters (p. 280). The author says one could, he supposes, write p(5) for N, since 5 refers to N in the table, but he would ordinarily write p(N) (p. 280).
- The probability is the fraction of letters in a long passage that are the letter in question. Of a million letters, close to 130,000 will be E's (p. 281). So p(E) is about 130,000/1,000,000 = 0.13 (added step; the printed equation is not legible in the text layer).
- Joint probability: p(x,y) is the probability of x and y together. For example x is the letter sent and y the letter received, as in p(W,B). It is read "p of x, y" (p. 281).
- Conditional probability: p_x(y) is the probability of receiving y if x is transmitted, read "p sub x of y". Many authors write p(y|x), "the probability of y given x". Pierce uses Shannon's original notation (p. 281).
- The relation:
$$p(x,y)=p(x)\,p_x(y)$$
In words, the joint probability is the probability of x times the probability of y when x occurs (p. 281). In counts, the number of times x and y occur together equals the number of times x occurs times the fraction of those times that y goes with x (p. 282).

*Intuition note:* To find how often two things happen together, first ask how often the first happens. Then ask how often the second follows it.

**Summation (pp. 282–284).**
$$\sum_{j=0}^{8} j = 0+1+2+3+4+5+6+7+8 = 36$$
Read: "the sum of j from j equals 0 to j equals 8". The bottom value is the start, the top value is the stop, and the j on the right is what is added (p. 282). The index can be a mere label. Table XVII gives letter probabilities, and
$$\sum_{j=1}^{26} p(j) = 1$$
because the fractions of all letters together make up the fraction of times per letter that any letter at all occurs, and one letter occurs per letter (p. 282). Writing $\sum_j p(j)$ with no limits means sum over all values of j that stand for something (p. 283). For two indices, $\sum_j p(i,j)$ means let j take every possible value and add. The text reads this as the probability of letter i followed by letter j, summed over j. The result is
$$\sum_j p(i,j)=p(i)$$
because every occurrence of the letter is followed by some letter (p. 284).

*Intuition note:* Adding p(i,j) over every possible j removes j and leaves the probability of the letter i.

**Exponents (pp. 284–285).** The exponent is the number of times a quantity is multiplied by itself: 2¹ = 2, 2² = 4, 2³ = 8, 2⁴ = 16. For a letter n: 2ⁿ, aⁿ (p. 284). To get consistent results one must set a⁰ = 1 for any a (p. 284). Also:
$$a^{-n}=\frac{1}{a^n},\qquad a^n a^m = a^{(n+m)}$$
Examples: 2³ × 2² = 8 × 4 = 32 = 2⁵, and 4^{1/2} × 4^{1/2} = 4¹ = 4. A ½ power is the square root, so 4^{1/2} = 2 (p. 285). Large numbers: 3.5 × 10⁶ = 3,500,000 (p. 285).

**Logarithms (pp. 285–286).** All logs in the book are base 2, except where noted in Chapter X (p. 285). Definition: the log to base 2 of x is the power to which 2 must be raised to equal x.
$$2^{\log x}=x$$
Example: log 8 = 3, since 2³ = 8. Table: x = 1, 2, 4, 8, 16, 32, 64 gives log x = 0, 1, 2, 3, 4, 5, 6 (pp. 285–286). Properties:
$$\log ab=\log a+\log b,\quad \log a/b=\log a-\log b,\quad \log d^{c}=c\log d$$
Special case: $\log 2^m = m\log 2 = m$ (p. 286).

Pierce says that, except in information theory, base-2 logs are not used. Base 10 and base e (e ≈ 2.718) are more common (p. 286). Conversions:
$$\log_2 x=(\log_2 10)(\log_{10}x)=\frac{\log_{10}x}{\log_{10}2}=3.32\log_{10}x$$
$$\log_2 x=(\log_2 e)(\log_e x)=\frac{\log_e x}{\log_e 2}=1.44\log_e x$$
The base-e log is the natural logarithm. For x much smaller than 1, approximately $\log_e(1+x)=x$, used in Chapter X. In the text, log x always means log₂x (p. 286).

*Intuition note:* log₂x counts how many doublings give x, so log 2^m = m. Because logs turn products into sums, multiplying two numbers corresponds to adding their logs.

## Toy example
(Ours, not from the text.) Send A or B, with p(A) = 0.6 and p(B) = 0.4. Conditional probabilities: p_A(A) = 0.9, p_A(B) = 0.1, p_B(A) = 0.2, p_B(B) = 0.8.

Using p(x,y) = p(x)p_x(y):
- p(A,A) = 0.6 × 0.9 = 0.54
- p(A,B) = 0.6 × 0.1 = 0.06
- p(B,A) = 0.4 × 0.2 = 0.08
- p(B,B) = 0.4 × 0.8 = 0.32

Check: Σ_y p(A,y) = 0.54 + 0.06 = 0.60 = p(A). The total over all four pairs is 0.54 + 0.06 + 0.08 + 0.32 = 1.00. Log check: 2⁻² = 1/4, so log 0.25 = −2.

## Concepts
- [[mathematical-notation-vs-mathematics]] (new) — notation is shorthand and is not the mathematics itself (p. 278)
- [[probability-as-fraction]] (new) — p(x) is the fraction of a long passage that is x (p. 281)
- [[joint-probability]] (new) — p(x,y), the probability of x and y occurring together (p. 281)
- [[conditional-probability]] (new) — p_x(y), the probability of y given x, in Shannon's notation (p. 281)
- [[summation-notation]] (new) — Σ over an index means add the terms for all its values (p. 282)
- [[marginalization]] (new; the author gives no name) — Σ_j p(i,j) = p(i) (p. 284)
- [[exponent-rules]] (new) — aⁿ, a⁻ⁿ, aⁿaᵐ = a^(n+m), a^{1/2} (pp. 284–285)
- [[logarithm-base-2]] (new) — the power of 2 that gives x; 2^(log x) = x (p. 285)
- [[natural-logarithm]] (new) — base-e log, with log_e(1+x) ≈ x for small x (p. 286)

## Canonical instances
- [[letter-frequency-E]] — about 130,000 of a million letters are E's (p. 281)
- [[send-W-receive-B]] — p(W,B) as a joint probability of sending and receiving letters (p. 281)

## Bridges (candidates)
- [structural-analogy] p(x,y) = p(x)p_x(y) ↔ information-theory: chain rule for entropy — both build a pair in steps.
- [structural-analogy] log ab = log a + log b ↔ information-theory: surprisal of independent events adds — logs turn product into sum.
- [same-math] Σ_j p(i,j) = p(i) ↔ probability: marginal distribution.

## Questions this raises
- Why does Pierce choose base 2, and how do the bases 10 and e change the unit of information?
- Why does the log rule turn the product of independent probabilities into a sum of quantities?
- How does the approximation log_e(1+x) ≈ x work in Chapter X?
- Is p_x(y) the same as p_y(x)? (The appendix does not say.)

## Reading notes
- Printed = pdf − 16 (pdf 294–302 are printed 278–286).
- The running head reads "Symbols, Signals and Noise". The metadata warns that this PDF is a 1961 first edition, not the Dover reprint. Only the running head is visible here, so this was not checked.
- Page images were supplied only for pdf 296, 298, 301 and 302. Pages 295, 297, 299 and 300 were read from the garbled text layer.
- Tables XVI and XVII are blank in the text layer and were not seen. The claim that 5 refers to N rests on the text on p. 280 (image checked).
- The p(E) equation on p. 281 is garbled. The value 0.13 is our arithmetic.
- The text layer reads "0 to the zero equals 1" on p. 284, although the sentence goes on to say that it holds whatever number a may be. I wrote a⁰ = 1.
- The Chapter V letter for a group of symbols is garbled in the text layer.
- The text layer at pp. 283–284 reads "QV" for a letter pair.
