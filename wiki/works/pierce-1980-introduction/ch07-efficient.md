---
id: pierce-1980-introduction/ch07-efficient
work: pierce-1980-introduction
unit: "7 Efficient Encoding"
pages: 125–144
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Efficient Encoding

## L0 — One line
Entropy tells us the minimum number of binary digits needed, but Pierce argues that reaching it in practice is better served by exploiting the natural structure of a source and the limits of eye and ear than by applying a blind mechanical scheme (pp. 127–128, 142).

## L1 — The gist (≤ 120 words)
Entropy gives a lower bound on the binary digits needed per symbol. How do we encode messages close to that bound? Pierce calls block-by-block Huffman coding a foolproof mechanical scheme, but says such methods are seldom practical for hard problems. A better approach may come from studying a particular source. Examples are English text, speech (the vocoder), and TV (color TV). Three principles follow: encode long stretches of signal at once, use the source's limitations, and use the eye's and ear's limitations. The chapter ends with a warning. If a code removed all redundancy with perfect success, any transmission error would give a false and misleading message. This leads to the next chapter, on noise.

**Prerequisites:** entropy in bits per symbol; Huffman coding of blocks; sampling (2B samples per second for bandwidth B); the idea of a continuous versus a discrete signal.

## L2 — Key ideas
- Coding long blocks with a Huffman code (a code that gives short words to likely blocks) brings the digits per character close to the entropy. Pierce shows a case where this is pointless: spotting simple structure (a digit repeated three times) is perfect (pp. 127–128).
- For English text, finer units of structure lower the bits per character: 4.7 for equiprobable letters, 4.14 with letter probabilities, about 2.5 with words. Grammar rules are not known well enough, and a system using them would probably be too complicated (p. 129).
- Shannon's prediction experiment bounds the entropy of English between 0.6 and 1.3 bits per letter, insofar as the result is correct (p. 130).
- A continuous signal would need infinite bits for exact reproduction. With a fidelity criterion (a rule for how closely the copy must match) associated with long stretches of the signal, a finite rate suffices (p. 131).
- Practical systems quantize (allow only preassigned values) sample by sample, as in pulse code modulation (sending the binary number of the nearest level). Companding (finer levels for small signals) and transmitting differences save digits, but jointly coding many samples ("hyperquantization") is the true road (pp. 132, 142).
- The vocoder (a speech analyzer and synthesizer) describes the slowly changing vocal organs rather than the fast sound wave. It sends about 1,500 binary digits per second instead of 30,000–60,000 (pp. 136–138).
- Three principles of efficient encoding: encode long stretches; use source limits; use eye and ear limits (p. 142).
- Removing redundancy (the clues a message gives its recipient) makes errors dangerous: if removal is perfectly successful, any error gives a false, misleading message (pp. 143–144).

## L3 — Walkthrough

### Opening remarks (pp. 125–127)
Pierce says a general explanation of common phenomena by a few all-embracing principles no longer satisfies us. We insist that theories give useful guidance rather than rationalizations, and harmonize in detail with a wide range of phenomena (p. 125). Physicists are gratified by the conviction that all non-nuclear properties of matter can in principle be explained by known quantum laws. Yet the only physical system all of whose properties have actually been calculated exactly is the isolated hydrogen atom (p. 125). He believes that many of the problems raised by recent advances in technology, including those of electrical communication, are as challenging as any (p. 126). If communication theory is to be taken seriously, it must give useful guidance in communication problems. Its substance should be sought in the efficient and accurate transmission of information, and Pierce says that substance exists (p. 126). Accurate transmission needs new basic understanding and is left to the next chapter. This chapter treats efficient transmission (p. 127).

Entropy in bits per symbol or per second measures the number of binary digits (on-or-off pulses) needed to transmit a message. We want a code that uses not many more digits than this minimum (p. 127).

### The mechanical scheme and why it is not enough (pp. 127–129)
**The scheme.** Entropy can be estimated from the probabilities of long blocks of characters. Blocks of 5, 10 or 100 characters may be needed for a good estimate (p. 127). Encoding successive blocks with a Huffman code makes the digits per character approach the entropy as blocks grow (pp. 127–128). This is a foolproof mechanical scheme. Pierce stresses that such general methods prove that problems can be solved. For hard problems they are seldom practical. His analogy is the general cubic equation: an explicit solution exists, but nobody uses it (p. 127). Someone who is not a novice thinks hard about a specific problem to see whether there is a better approach than a machine-like application of what was taught (p. 127).

**Pierce's example.** A source produces a random 1 or 0 with equal probability, then repeats that digit twice more before choosing a new, independent digit. A message is 000111000111111000000111 (p. 128). Because of the repetition, the entropy is the same as for a source producing a third as many independent equiprobable digits. That is $\tfrac13$ bit per character. (The text layer here is garbled; the value follows from the preceding sentence.) The message can be sent perfectly efficiently by sending every third character and telling the receiver to write each received character three times (p. 128). Pierce's lesson is to look for natural structure in a source and use its salient features (p. 128).

**English text.** Sending text as a television picture would use many digits per character. It would ignore the fact that English text is made of letters (p. 128). The figures are:
- Letter by letter, ignoring probabilities and excluding the space: 4.7 binary digits per letter (p. 129).
- Using letter probabilities, as Morse did: 4.14 digits per letter (p. 129).
- Word by word: about 14 digits per word, or 2.5 per character, as expected from Chapter IV (p. 129).
- Pair and triple codes would encode many non-words. Grammar-based coding is not available: the rules are not known completely enough to help, and a system using them would probably be unpractically complicated (p. 129).
- In practical cases it still seems best to encode letters independently, using at least 5 digits per character (p. 129).

**Shannon's guessing scheme.** A man uses his knowledge of English to guess the next character. If right, he writes it down. If wrong, he is told the character, or he guesses again. Imagine an identical twin at the receiver who makes the same guesses. Then information is sent only when the transmitter's guess is wrong (p. 129). Figure VII-1 shows this as a predictor, a comparison with the actual letter, and "reduced text" information sent when there is an error (p. 130). No such twins exist. A simpler, purely mechanical system of this kind has been used for pictures (p. 130). Shannon used one man and examined his errors, which gives the transmission rate such a system would need. The results are in Figure V-4. Predictions based on 100 preceding letters are better than those based on 10 or 15. Correcting the errors takes 0.6 to 1.3 binary digits per character. So, insofar as this result is correct, the entropy of English lies between 0.6 and 1.3 bits per letter (p. 130).

*Intuition note:* A message is cheap to send when the receiver can already predict most of it. Only the surprises need to be sent. The guessing experiment gives an estimate, insofar as it is correct, of how predictable English is.

### Why speech and TV matter more than text (pp. 130–132)
Text is not a practically important case. It takes few digits to send. Over 1,000 words a minute can be sent on a telephone connection and 10 million on a TV channel. In principle, about 50,000 words per minute could go over a telephone channel and 50 million over a TV channel. Teletype gives every letter the same length of signal (pp. 130–131). Efficient encoding is therefore potentially more important for voice than for text, and potentially more so still for TV (p. 131).

**Continuous signals.** A signal limited to bandwidth $B$ is accurately represented by $2B$ amplitude samples per second (p. 131). Each sample can take infinitely many values, so exact reproduction would need infinite bits per sample (p. 131). Signals are meant to be heard or seen, so Shannon introduces a *fidelity criterion*. Meeting it needs only a finite number of digits per sample or per second. Within that criterion, the continuous source has a definite entropy in bits per sample or per second (p. 131). Pierce says it is extremely important to realize that the criterion should be associated with long stretches of the signal, not with individual samples. Making every sample 10 per cent larger only makes the sound louder. A random 10 per cent error in each sample makes it very noisy. A smooth brightness change goes unnoticed in a picture, but an equal random point-to-point error is intolerable (pp. 131–132).

*Intuition note:* What counts as an error depends on what the listener or viewer notices. A systematic change in many samples can be harmless, while a random change of the same size is not.

### Quantizing and pulse code modulation (pp. 132–133)
**Quantizing** means allowing each sample only certain preassigned values. It appears that 128 values suffice for telephone-quality speech or pictures (p. 132). Doing this sample by sample is unsophisticated, like coding text letter by letter (p. 132). **Hyperquantization** is quantizing more than one sample at a time. Pierce calls it "undoubtedly the true road" to efficient encoding of continuous signals. It is not easy to do well, and independent sample quantization is the method commonly used in present practice. Quantizing the samples at the start can easily ruin one's chances of efficient encoding. PCM is used in some military telephone systems and is being developed for multiplex telephone transmission (p. 132).

**Pulse code modulation (PCM).** Each sample is assigned the nearest of a set of standard levels, and the binary number of that level is sent. Figure VII-2a shows eight equally spaced levels (p. 132). **Companding** (compress high amplitudes at the transmitter, expand them at the receiver) uses levels close together for small signals and far apart for large ones (Figure VII-2b). The reason is that the ear is sensitive to fractional error in amplitude. Then 7 binary digits per sample give a signal almost as good as 11 digits would with equally spaced levels (pp. 132–133).

### Speech and the vocoder (pp. 133–139)
Efforts to encode speech from the wave alone have not been highly effective. One idea is to send differences between successive samples, since the wave changes little from sample to sample (p. 133). Another is to send one period of a vowel wave and reuse it (Figure VII-3). This is hard, because a machine cannot easily find the period. It has been tried, and the speech was intelligible but seriously distorted (pp. 133–135). A more fundamental approach is needed: how many speech sounds must be sent, and how well does hearing tell them apart (p. 135).

**Key observation.** Sound pressure fluctuates thousands of times a second. Our control of the vocal tract changes at most a few tens of times a second. So speech may be (and is) simpler than its waveform suggests (p. 135). Pierce describes the vocal cords, the mouth as a resonator, and the classes of sounds: voiced sounds, stops (plosives) and fricatives (pp. 135–136).

**The channel vocoder** (voice coder; Homer Dudley, Bell Laboratories, early 1930s, before Shannon's theory) (p. 136):
- The analyzer feeds the speech to 16 filters (in the figure). Each measures signal strength in one frequency band. A further analysis decides whether the sound is voiced or voiceless and, if voiced, finds the pitch (p. 136).
- The synthesizer produces a hiss for voiceless sounds, or pulses at the proper rate for voiced sounds. These feed an array of filters matching the analyzer's. Each filter's output is controlled by the corresponding analyzer filter (p. 136).
- Result: intelligible speech with the speaker's pitch and accent. Most vocoders have a strong, unpleasant electrical accent (p. 136).

**Numbers.** Direct PCM needs 30,000 to 60,000 binary digits per second. A vocoder needs around 1,500 (p. 138). Variants:
- A channel vocoder sends 10 to 30 frequency bands.
- A formant-tracking vocoder sends the location and intensity of two or three formants (the few prominent frequency ranges, which reflect vocal-tract resonances), with even fewer digits.
- A phoneme vocoder recognizes basic voice sounds and tells the synthesizer to speak them. It is more economical and less intelligible (p. 138).
- A voice-excited vocoder sends a band a few hundred cycles wide of the speech and distorts it to excite the synthesizer. It sounds almost as good as regular telephone speech and needs half the channel capacity. Its cost would limit it to long, expensive circuits such as transatlantic cables. Pierce says the channel vocoder's quality is scarcely adequate for ordinary telephone use, and that its unnatural sound appears to be associated with poor following of pitch and of voiced/voiceless changes (p. 138).

**Why it works.** Even the best vocoders use many more digits per word than text. Partly the cause is technical difficulty. Partly, speech carries quality, pitch, stress and accent as well as the text's information, so the entropy of speech is somewhat greater per word than that of text (pp. 138–139). The vocoder works because the vocal tract changes more slowly than the sound waves it produces, and also because of limits of hearing (p. 139). For example, two utterances of *s* may have quite different waveforms. They sound the same if they have roughly the same frequency content, so the vocoder need only reproduce that (p. 139).

*Intuition note:* The vocoder sends instructions for making the sound, not the sound itself. Because the instructions change slowly and the ear ignores fine detail, far fewer digits are needed.

### TV (pp. 139–142)
TV is harder than speech. The eye is more discriminating than the ear, and many kinds of pictures are sent, whereas speech comes from one kind of apparatus (p. 139). Pierce imagines a vocoder-like scheme for faces. A model of a face at the receiver would be set up for shape, tint and lighting. The transmitter would then send eye, lip and jaw movements. He says such a scheme might be very effective if anyone could specify a useful way to do it, and remarks that it is much easier to say what one would like to do than to do it. He notes that the press word "breakthrough" is used for such dreams (pp. 139–140).

Actual systems all scan the picture along closely spaced lines. So far, all practical attempts at efficient encoding have started from the scanned signal (p. 140).
- **Color TV** is the outstanding scheme. Brightness has very fine detail and color pattern much less. So color of almost the same detail as monochrome fits the same channel. It is an analog signal (p. 140).
- **Proposed for monochrome:** send slow variations in great detail and fast variations less accurately or only intermittently. There is controversy about how effective this is (p. 140).
- **Slower picture rate:** TV sends a picture every 1/30 s to avoid flicker. For a face, a new picture every 1/10 s might do if the picture were shown several times. This needs storing a picture at the receiver, which seems too expensive now. It might cut the digits per second by a factor of 3 (p. 141).
- **Straight-line approximation:** approximate the signal by straight segments and send only the heights of the end points and the distances between them (Figure VII-5). This is an old idea, and there is little agreement on its effectiveness (p. 141).
- **Differences:** companding by signal level is not effective for pictures, because fine detail occurs at both bright and dark levels. But large light changes need not be reproduced as accurately as small ones. So send differences between successive samples, with fine steps for small differences and coarse steps for large ones. In a refined form, the difference is taken from the sample just above or just to the left. This does almost as well with 3 binary digits per sample as separate encoding does with 7 (p. 142).

### Three principles (pp. 142–143)
1. Do not encode one sample or character at a time. Encode a considerable stretch (hyperquantization).
2. Take into account the limitations on the source of the signal.
3. Take into account the inability of eye or ear to detect errors in the reconstruction (p. 142).

Pierce says the vocoder illustrates these principles excellently. Perhaps next comes color TV, which uses the eye's inability to see fine color detail (pp. 142–143). Other present methods do not encode long stretches and so must, according to communication theory, be rather inefficient (p. 143). Efficient encoding is potentially important, especially for broad-band signals on very expensive circuits such as transoceanic cables (p. 143).

### A warning: redundancy and errors (pp. 143–144)
Pierce says we should perhaps beware of going too far. Text sent letter by letter survives a few errors: "More I hove reploced a few vowols by o." Even vowels replaced by x's can be read with some facility (p. 143). With word-by-word coding, an error replaces one word by another, with no misspelling to warn us. His example is "Republican" becoming "Communist". We might detect the error because the word is inappropriate. But if a scheme reproduced only grammatical utterances, we would have little chance of detecting it (p. 143).

Sources are redundant because their messages give the recipient many clues. A few letter errors do not destroy a message, since it can be inferred from the correct letters. In sample-by-sample signals, a few errors produce clicks or specks (pp. 143–144). If we removed redundancy with perfect success, any error would give a false and misleading message, not a distorted one. If we fall a little short, an error may give only a terrible garble (p. 144). Noise is an inevitable fact of nature. Does it vitiate, in principle, the plan of encoding in scarcely more digits than the entropy? That is the subject of the next chapter (p. 144).

*Intuition note:* Redundancy lets us survive and notice errors, because a message gives clues to its recipient. Removing it saves digits but takes away the safety net.

## Toy example (ours)
Take Pierce's repeat-three source and his message 000111000111111000000111 (p. 128). It has 24 characters.
1. Split into triples: 000, 111, 000, 111, 111, 000, 000, 111. That is 8 triples.
2. Each triple is one random digit repeated. The digits are 0, 1, 0, 1, 1, 0, 0, 1, and each carries 1 bit (equiprobable).
3. Entropy: 8 bits / 24 characters = $\tfrac13$ bit per character.
4. A character-by-character Huffman code sees each character with probability $\tfrac12$. It assigns 1 binary digit to each, so it spends 24 digits, which is 1 digit per character. Sending every third character costs 8 digits.
5. The receiver writes each received digit three times and recovers the message exactly. The saving is 24 − 8 = 16 digits, a factor of 3.

The gain comes from noticing the structure, not from a cleverer general code.

## Concepts
- [[entropy-H]] — minimum average binary digits per symbol (or per second) needed to send a source's messages (p. 127)
- [[redundancy]] — the clues messages give the recipient; it lets errors be survived or detected; removing it saves digits but makes errors dangerous (pp. 143–144)
- [[huffman-arithmetic-coding]] — Huffman coding of long blocks brings digits per character near entropy, but Pierce shows a case where it is pointless (pp. 127–128)
- [[source-coding-theorem]] — entropy is a lower limit; it can be approached with block coding. This unit states only the approach by blocks (p. 128)
- [[entropy-rate]] — for English, estimated by letter, word and prediction experiments: 4.7, 4.14, 2.5 bits per character and 0.6–1.3 bits per letter (pp. 129–130)
- [[fidelity-criterion]] (new) — Shannon's requirement on how well a continuous signal must be reproduced, set over long stretches, which makes the entropy finite (p. 131). Canon link, not stated in this unit: rate–distortion function.
- [[quantization]] (new) — allowing each sample only preassigned values (p. 132)
- [[hyperquantization]] (new) — quantizing more than one sample at a time; "the true road" to efficient coding of continuous signals (p. 132)
- [[pulse-code-modulation]] (new) — send the binary number of the nearest standard level for each sample (p. 132)
- [[companding]] (new) — compress high amplitudes at the transmitter, expand them at the receiver; fine levels for small signals (p. 132)
- [[vocoder]] (new) — analyzer–synthesizer that sends slowly changing descriptions of speech (band strengths, voiced or voiceless, pitch) (p. 136)
- [[predictive-coding]] (new) — send only the corrections when a predictor at both ends fails; Shannon's guessing scheme, Figure VII-1 (pp. 129–130)

## Canonical instances
- [[repeat-three-source]] — random digit repeated three times; entropy ⅓ bit per character, so mechanical block coding is unnecessary (p. 128)
- [[shannon-guessing-experiment]] — a human predicts the next letter; entropy of English 0.6–1.3 bits per letter (pp. 129–130)
- [[channel-vocoder]] — 1,500 versus 30,000–60,000 binary digits per second (pp. 136–138)
- [[color-tv-encoding]] — fine brightness detail, coarse color detail in the same channel (p. 140)
- [[difference-coding-pictures]] — sending differences allows 3 binary digits per sample instead of 7 (p. 142)
- [[vowel-and-x-replacement]] — text surviving errors because of redundancy (p. 143)

## Bridges (candidates)
- [structural-analogy] Shannon's guessing scheme (predict, send only the corrections) ↔ language modelling: a predictor's errors set the cost of coding the text.
- [structural-analogy] Fidelity criterion over long stretches ↔ rate–distortion theory: required bits depend on the allowed distortion measure.
- [structural-analogy] Redundancy removed means errors become false messages ↔ error-correcting codes: structured redundancy is added back (Pierce only says the next chapter treats noise).
- [metaphor] Vocoder: send slow parameters of a generator, not the waveform ↔ model-based or parametric representations in data analysis.

## Questions this raises
- How does one measure the entropy of continuous signals under a fidelity criterion? Pierce only says that it is finite.
- How can redundancy be put back in a controlled way, so that noise causes no false messages?
- Is the 0.6–1.3 bits-per-letter range for English tight? What limits one human guesser?
- Which patterns in a source are worth modelling, and which can the receiver safely ignore?

## Reading notes
- Printed page = pdf page − 16 (pdf 141 = printed 125).
- Edition: the running headers read "Symbols, Signals and Noise". The metadata warns that the PDF is the 1961 first edition, not the 1980 Dover edition. No title page is in these pages, and the metadata note is cut off, so this could not be checked here. Page numbers may differ from the Dover edition.
- I worked from the text layer only; no page images were supplied. The text layer is garbled in places. On p. 128 the repeat-three entropy appears as "& binary digit"; I give ⅓ from the sentence before it. "Chapter \9" (p. 127) is garbled. The text calls the vocoder figure "Figure 11-4" (p. 136) but later "Figure VII-4" (p. 138). "zformant" (p. 138) is garbled; the sentence reads "Such zformant tracking vocoder", probably "a formant-tracking vocoder". References to panel letters of Figure VII-3 (p. 139) are garbled.
- The figures themselves (VII-1 to VII-5) could not be read in detail. The page with Figure VII-4 (printed p. 137) has only a page number in the text. Level-spacing details in Figure VII-2 and the Figure VII-5 labels are not reproduced.
