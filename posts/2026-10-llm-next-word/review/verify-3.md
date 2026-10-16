# Verify-3: independent fact-check of the diff since the last commit

Scope: `git diff -- src/content.html audio-script.md` (box `#box-attention`, two further-reading notes, the Mikolov citation change, the new Sources sub-list, one audio sentence).
Reviewer did not write the text. Date: 2026-10-16.

**Result: 0 critical, 1 major, 11 minor.** All numbers in the box are correct. All Vaswani citations hold. Both further-reading notes are accurate apart from small wording points.

---

## A. Numbers (recomputed in Python, numpy)

| Quantity | Post | Computed | OK |
|---|---|---|---|
| W x3, ReLU | (0,1) | (0, 1) | yes |
| s31, s32, s33 | 0.707, 0.707, 1.414 | 0.70711, 0.70711, 1.41421 | yes |
| a3 | (0.248, 0.248, 0.503) | (0.24826, 0.24826, 0.50349) | yes |
| h3 | (0.752, 0.752) | (0.75174, 0.75174) | yes |
| z | (0.752, 1.503, -1.503) | (0.75174, 1.50349, -1.50349) | yes |
| p (Alice, Bob, cat) | 0.310, 0.657, 0.033 | 0.31003, 0.65747, 0.03251 | yes |
| -ln p(Bob) | 0.42 nats | 0.41936 | yes |
| -log2 p(Bob) | 0.61 bits | 0.60500 | yes (0.605 rounds to 0.61) |

## B. Citations to Vaswani et al. 2017 (library PDF, printed page = PDF page)

| Claim in box | Source text | Verdict |
|---|---|---|
| FFN applied “to each position separately and identically” (p. 5) | p. 5, §3.3: “a fully connected feed-forward network, which is applied to each position separately and identically.” | exact quote, correct page |
| W_Q, W_K, W_V learned tables (pp. 4–5) | p. 4: “linearly project the queries, keys and values h times with different, learned linear projections”; p. 5: “W_i^Q … W_i^K … W_i^V” parameter matrices | correct |
| Mask (p. 5) | p. 5, §3.2.3: “allow each position in the decoder to attend to all positions in the decoder up to and including that position … masking out (setting to −∞)” | correct (but see Major 1) |
| N = 6 layers (p. 3) | p. 3: “The encoder is composed of a stack of N = 6 identical layers … The decoder is also composed of a stack of N = 6 identical layers.” | page correct; wording imprecise (Minor 3) |
| Several heads (p. 5) | p. 5: “we employ h = 8 parallel attention layers, or heads.” | correct |
| s = q·k/√d | p. 4, eq. (1): divide by √d_k | correct (see Minor 5 on d vs d_k) |

Mikolov citation change (line 118, `Mikolov et al. 2013a, p. 5`): confirmed. mikolov-2013-efficient.pdf, printed p. 5: “we can simply compute vector X = vector(”biggest”) − vector(”big”) + vector(”small”) … it is possible to find the correct answer (word smallest)”.

The paragraph labelled “our summary of standard practice” (parallel next-token prediction) is correctly labelled as ours and not attributed to the paper. The p. 5 cite is attached only to the mask, which p. 5 supports. p. 3 also supports the offset-by-one idea: “This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position i can depend only on the known outputs at positions less than i.”

---

## Findings

### MAJOR 1. The training paragraph says the wrong thing about what the mask allows
- **Location** (line 164): “The mask is what makes this fair, because each position may use only the tokens before it”
- **Problem:** “it” refers to the position. Position 2 (which predicts token 3) uses tokens 1 **and 2**, so it also uses its own token. This contradicts the box’s own Step 3 (“the mask allows \(j\le3\)”, which includes token 3 itself) and the source. A careful reader will see the two statements disagree.
- **Source:** Vaswani p. 5: “attend to all positions in the decoder **up to and including that position**”.
- **Fix:** “The mask is what makes this fair: each position may use its own token and the tokens before it, but never the token it has to predict.”

### MINOR 1. “nats” and “ln” are used before they are defined
- **Location** (line 163): “\(-\ln 0.657=0.42\) nats (0.61 bits)”
- **Problem:** The first definition of a nat comes later (line 180, Step 8: “a nat is like a bit but uses natural logarithms”; full definition line 249). This breaks WRITING §3 (“define every technical term at first use”).
- **Fix:** “… \(-\ln 0.657=0.42\) nats. A nat is a bit measured with the natural logarithm \(\ln\) (base \(e\approx2.718\)) instead of base 2. 1 nat ≈ 1.44 bits, so this is 0.61 bits.”

### MINOR 2. One token’s surprise is called “the cross-entropy”
- **Location** (line 163): “The loss is the surprise of the true token … : the cross-entropy of Lens 1.”
- **Problem:** Cross-entropy (Lens 1) is the *average* surprise over many tokens. One token’s −ln q is one term of it.
- **Fix:** “The loss for this one prediction is the surprise of the true token … Averaged over all positions and texts, it is the cross-entropy of Lens 1.”

### MINOR 3. “6 of each” is imprecise for the original Transformer
- **Location** (line 166): “Real models repeat attention and perceptron layers many times (6 of each in the original Transformer p. 3)”
- **Problem:** The original model has two stacks. The encoder has 6 layers, each with self-attention plus a feed-forward part. The decoder has 6 layers, each with **two** attention sub-layers plus a feed-forward part. In total that is 12 feed-forward parts and 18 attention parts, so “6 of each” is true only for one stack.
- **Source:** p. 3 (quoted above): “the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack.”
- **Fix:** “(the original Transformer stacks 6 such layers in its encoder and 6 in its decoder, each with attention followed by a perceptron part p. 3)”

### MINOR 4. The Transformer’s “perceptron layer” is really two layers
- **Location** (line 142): “The Transformer does contain such a layer, applied ‘to each position separately and identically’”
- **Source:** p. 5: “This consists of two linear transformations with a ReLU activation in between. FFN(x) = max(0, xW1 + b1)W2 + b2”.
- **Fix:** “The Transformer does contain such layers: a pair of them (the second one without the bend), applied ‘to each position separately and identically’ p. 5.”

### MINOR 5. d is used for two things
- **Location** (line 152): “\(s_{3j}=q_3\cdot k_j/\sqrt d\)”
- **Problem:** In the box, \(d\) is the length of \(x_j\). In the paper, the divisor is \(\sqrt{d_k}\), the length of the key vector (p. 4). The two are equal here only because \(W_K\) is the identity. Rung 6 and the formula at line 266 use \(d_k\).
- **Fix:** “\(s_{3j}=q_3\cdot k_j/\sqrt{d_k}\), where \(d_k\) is the length of the key vector (here \(d_k=d=2\))”.

### MINOR 6. The rounded numbers do not add up exactly when checked by hand
- **Location** (lines 153–154, 162): \(a_3=(0.248,0.248,0.503)\) sums to 0.999. \(0.248+0.503=0.751\), but the box prints 0.752. \(2\times0.752=1.504\), but the box prints 1.503.
- **Problem:** The box invites hand checks (“tiny numbers you can check by hand”), so a student will hit these differences. The printed values are correct roundings of the unrounded values.
- **Fix:** Add after the softmax step: “(Numbers are rounded to 3 decimals; we compute with the unrounded values, so hand sums can differ in the last digit.)”

### MINOR 7. The mask hides nothing in the worked example
- **Location** (line 152): “(the mask allows \(j\le3\))”
- **Problem:** Token 3 is the last token, so there is no future token to hide. A student may wonder what the mask did. (Rung 6 says this explicitly: “the mask hides nothing earlier”.)
- **Fix:** “(the mask allows \(j\le3\); token 4 does not exist yet, so here the mask hides nothing. It matters in training, see the end of this box.)”

### MINOR 8. ReLU does nothing in the perceptron example
- **Location** (line 141): “\(f\) turns negative numbers into 0. Then \(Wx_3=(0,1)\), so \(h_3=(0,1)\).”
- **Problem:** Nothing is negative, so the reader never sees \(f\) act.
- **Fix:** Add “(here nothing is negative, so \(f\) leaves \((0,1)\) unchanged; for token 2, \(Wx_2=(-1,0.5)\) would become \((0,0.5)\))”. (Checked: \(W(0,1)=(-1,0.5)\).)

### MINOR 9. Two training claims are unlabelled and incomplete
- **Location** (line 163): “Training then nudges every learned table, \(W_{\text{out}}, W_Q, W_K, W_V\) … Often that means a larger attention weight on the positions that point to Bob.”
- **Problem:** (a) “Every learned table” lists only the toy’s tables. Real models also train the perceptron tables and the word vectors themselves. (b) “Often that means …” is our own intuition with no source, and WRITING §9 requires our reasoning to be labelled.
- **Fix:** “Training then nudges every learned table (in the toy \(W_{\text{out}}, W_Q, W_K, W_V\); in a real model also the perceptron tables and the word vectors) … One way this can happen (our illustration): a larger attention weight on the positions that point to Bob.”

### MINOR 10. Kozlowski note: dimension name and “more reliable”
- **Location** (line 504): “build cultural dimensions such as affluence … Averaging several pairs gives a more reliable direction than one pair (summary from the arXiv version …)”
- **Source (arXiv 1803.09288v1):** p. 14: “we calculate a gender dimension by simply taking the arithmetic mean of a set of such pairs. Dimensions for class and race are similarly constructed, using appropriate sets of antonym pairs such as rich – poor”; p. 14: “Because vectors are normalized, the projection of a word vector onto a ‘cultural dimension’ is equivalent to their cosine similarity”; p. 32: “Averaging between six and ten pairs of words for each dimension … produces a closer approximation to the cultural dimension of interest than any one word-pair, as they post higher correlations with the survey”. Validation is a Pearson correlation with an MTurk survey of 398 respondents (pp. 23, 32).
- **Problem:** (a) The arXiv version calls it the **class** dimension. “Affluence” is one of its pairs (affluence – poverty) and is the ASR version’s term. Because the note says it summarises the arXiv version, use its term. (b) “More reliable” suggests stability across samples. The paper claims a *closer approximation*, measured by *higher correlation with the survey*.
- **Fix:** “… build cultural dimensions such as class by averaging the vector differences of six to ten antonym pairs (rich − poor, affluence − poverty and others) … Averaging several pairs gave directions that matched the survey better than any single pair (summary from the arXiv version, pp. 14, 32; not yet in our library).”
- Everything else in the note is confirmed: averaging antonym differences, projection of normalized vectors = cosine, validation against survey ratings.

### MINOR 11. Further-reading entries: missing details, and the arXiv title differs
- **Location** (lines ~632–633, Sources › Further reading).
- **Confirmed:** Hussain et al., *Behavior Research Methods* **56**(8), 8214–8237 (2024), doi 10.3758/s13428-024-02455-8 (Springer page). The first authors are Hussain, Binz, Mata; the last author is Dirk U. Wulff. The in-box note is confirmed: the article explains that “the queries and keys combine to determine how to recombine the values” and says “this analogy should not be taken too literally” (section “Attention blocks”). Kozlowski, Taddy & Evans, *ASR* **84**(5), 905–949 (2019), doi 10.1177/0003122419877135 (Crossref).
- **Problem:** The volume and pages are missing. The note is a summary of the arXiv version, which has a different title (“The Geometry of Culture: Analyzing Meaning through Word Embeddings”), but the Sources entry gives only the ASR version.
- **Fix:** Append “56(8), 8214–8237.” to Hussain. Append “84(5), 905–949. Summary in this post from the preprint, arXiv:1803.09288 (titled ‘…Analyzing Meaning through Word Embeddings’).” to Kozlowski.

---

## Writing-rule notes (WRITING.md). No fix is required, but Kunhao should decide on these
- **§4 (boxes only for terms/traps/answers/exercises).** `#box-attention` is an explanation box. It is acceptable as optional depth, since the main Step 5 text stands alone, but it is an exception to §4 and should be logged as one.
- **§5 (every mechanism gets a picture).** The box walks through a mechanism with no diagram. A small SVG with three token dots, arrows to token 3 whose thickness follows 0.25/0.25/0.50, and the perceptron’s single arrow would satisfy §5.
- **Placement.** The Hussain “further reading” line sits between the training paragraph and the “Real models …” paragraph. Move it to the very end of the box.
- **Nits.** “Our example (ours)” is redundant, so use “Our example:”. “Needs only multiplication, addition and the exponential function” should add “division and a square root”.
- **Labelling.** The toy examples are correctly labelled “ours”/“our toy”/“toy … (ours)”. “Identity”, “perceptron layer” and “weighted average” are defined at first use. “Softmax” refers back to Step 4, where it is defined (line 109).

## Audio script
The new sentence (“a fold-out box that compares attention with a simple perceptron layer…”) is accurate. No issue.

## Access note
The PMC page for Hussain et al. (pmc.ncbi.nlm.nih.gov/articles/PMC11525391) was blocked (permission not answered). Verification used the Springer article page instead.
