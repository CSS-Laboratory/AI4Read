---
id: mackay-2003-information/ch50-digital
work: mackay-2003-information
unit: "50 Digital Fountain Codes (with the preceding 'About Chapter 50')"
pages: 588-596
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Digital Fountain Codes

## L0 — One line
Digital fountain (LT) codes make an endless stream of random sparse XOR packets, so a receiver can rebuild a file of K packets from slightly more than K received packets, using a very cheap peeling decoder and no feedback.

## L1 — The gist (≤ 120 words)
On an erasure channel (packets arrive intact or are lost), retransmission protocols need a feedback channel and are wasteful, especially when broadcasting. Reed–Solomon codes are ideal but practical only for small sizes, and their rate must be fixed in advance. Luby's LT codes send each packet as the XOR of a random subset of source packets. The subset size comes from a carefully designed degree distribution (the robust soliton). The decoder repeatedly finds a check involving one unknown packet, resolves it and subtracts it from the other checks. The code is rateless, needs about 5% overhead in practice, and, with probability 1−δ, has encoding and decoding costs of order K ln(K/δ) operations. It suits storage and broadcast.

**Prerequisites:** probability distributions; XOR (addition mod 2); bipartite graphs; the idea of the erasure channel and channel capacity; a rough idea of message passing.

## L2 — Key ideas (5–10 bullets)
- Over a q-ary erasure channel the capacity is (1−f)l bits per packet whether or not feedback is available, so retransmission protocols are wasteful (p. 589).
- Reed–Solomon codes recover the source from any K of N symbols. But their cost is of order K(N−K) log₂N, and the rate must be chosen before transmission (pp. 589–590).
- A digital fountain is rateless: it can produce unlimited encoded packets, and any K′ slightly more than K of them suffice to decode (p. 590).
- Encoding picks a degree d from ρ(d), picks d distinct source packets at random, and XORs them. The result is an irregular low-density generator-matrix code (p. 590).
- Decoding is message-passing with only "certain" or "completely uncertain" messages. It finds a degree-one check, sets the source packet, and subtracts it from the other checks. It halts if no degree-one check exists (p. 591).
- The ideal soliton distribution gives one degree-one check per step in expectation but is fragile. The robust soliton adds τ(d) (parameters c, δ) to keep about S degree-one checks and avoid unconnected packets (pp. 592–593).
- Luby's result: K′ = K + 2 ln(S/δ)·S received checks suffice with probability ≥ 1−δ for suitable c. The bound is conservative: in practice the codes can be tuned to about 5% overhead (p. 593).
- Applications: robust storage, broadcast without feedback, and data to cars. In the broadcast and car cases the fountain avoids retransmission requests and carousel waiting; for storage it avoids re-reading lost packets (pp. 593–594).

## L3 — Walkthrough

### Background exercise (p. 588)
Exercise 50.1 is posed as background: an author inspects random pages of a K = 700-page book, N times, taking no precautions to avoid inspecting the same page twice. Parts: (a) the expected fraction of never-inspected pages when N = K; (b) the probability that some page is never inspected when N > K; (c) show that N ≃ K ln(K/δ) inspections are needed for all pages to be inspected with probability 1−δ (p. 588). The source notes that it is commonly presented as throwing N balls at random into K bins (p. 588).

### Introduction: erasure channels and why retransmission is wasteful (pp. 589–590)
- **q-ary erasure channel:** each input in {0,…,q−1} arrives correctly with probability 1−f, and is replaced by '?' with probability f. The alphabet size is q = 2^l, where l is the number of bits per packet (p. 589). Internet packets are the motivating case.
- Retransmission protocols use a feedback channel. The receiver either names missing packets or acknowledges received ones. They work whatever f is (p. 589).
- **Shannon view:** the capacity is (1−f)l bits whether or not there is feedback. So feedback is not needed in principle (p. 589).
- **Broadcast to many receivers:** each receiver loses a random fraction f. Retransmitting every packet missed by one or more receivers is terribly redundant, because every receiver will already have received most of the retransmitted packets (p. 589).
- **Reed–Solomon (N, K) codes** over q = 2^l: any K of the N received symbols recover the source; they exist for N < q (p. 589). Disadvantages:
  - Standard implementations cost order K(N−K) log₂N packet operations, so they are practical only for small K, N, q (pp. 589–590).
  - The rate R = K/N must be fixed before transmission. If f turns out larger than expected, there is no on-the-fly way to extend to a lower-rate (N′, K) code (p. 590).
- **LT codes** (Luby, 1998; 'Luby transform') (p. 590). The encoder is a fountain of drops (encoded packets). The source file has Kl bits and each drop carries l bits. A receiver collects drops until it has a little more than K, then recovers the file (p. 590).
  - **Rateless:** the number of encoded packets is potentially unlimited and is decided on the fly (p. 590).
  - Decoding works from any set of K′ packets with K′ slightly larger than K (in practice about 5% larger) (p. 590).
  - With probability 1−δ, K packets can be communicated with average encoding and decoding costs both of order K ln(K/δ) packet operations (p. 590).
  - Luby calls the codes **universal**: simultaneously near-optimal for every erasure channel. The overhead K′−K is of order √K (ln(K/δ))² (p. 590).

> **Intuition note.** Think of collecting water drops: it does not matter which drops you catch, only how many. The sender needs no model of the channel and no feedback.

### 50.1 The encoder (pp. 590–591)
For each encoded packet t_n built from source packets s₁…s_K (p. 590):
1. Choose the degree d_n from a degree distribution ρ(d). The appropriate ρ depends on K.
2. Choose d_n distinct source packets uniformly at random. Set t_n to their bitwise sum mod 2, computed by successive exclusive-ors.

This defines a graph from encoded to source packets. If the mean degree d̄ is much smaller than K, the graph is sparse. The code is an irregular low-density generator-matrix code (p. 590).

The decoder must know each packet's degree and neighbours. Two ways to share this information (p. 591):
- Synchronized clocks drive identical pseudo-random generators.
- The sender puts a random key κ_n in each packet header. The key determines the degree and connections by a pseudo-random process. A key of about 32 bits is a small overhead if l is much bigger.

### 50.2 The decoder (p. 591)
The task is to recover **s** from **t = Gs**, where G is the graph's matrix. The method is message-passing. It can be seen as the sum–product algorithm, but every message is either completely uncertain (any value, equal probability) or completely certain (one value, probability one) (p. 591). Call the encoded packets {t_n} check nodes.

1. Find a check t_n connected to only one source packet s_k. If none exists, the algorithm halts and fails to recover all source packets.
   - (a) Set s_k = t_n.
   - (b) Add s_k to all checks connected to it:
   $$t_{n'} := t_{n'} + s_k \quad \text{for all } n' \text{ such that } G_{n'k}=1. \tag{50.1}$$
   - (c) Remove all edges connected to s_k.
2. Repeat until all {s_k} are determined.

**Figure 50.1 example** (p. 591): K = 3 source bits, N = 4 received bits, initial values t₁t₂t₃t₄ = 1011. Only check 1 has a single source neighbour, so s₁ is set to 1. That value is added to the checks connected to s₁. Then check 4 has a sole neighbour s₂, so s₂ = t₄ = 0, and s₂ is added to its two other checks. Finally two checks are both connected to s₃ and agree on its value. Panel f shows the result 1 0 1.

> **Intuition note.** The decoder "peels" the graph like an onion: each solved packet is subtracted everywhere, which creates new degree-one checks. It only works while such a check exists.

### 50.3 Designing the degree distribution (pp. 591–593)
ρ(d) is critical (pp. 591–592):
- Occasional packets must have high degree (d similar to K), so no source packet is left with no connection.
- Many packets must have low degree, so decoding can start and keep going, and so the number of additions stays small.
- For a given ρ(d), the decoding statistics can be predicted by an appropriate version of density evolution (p. 592).

**Ideal soliton distribution** (p. 592). The ideal is exactly one degree-one check at each iteration. Processing it reduces degrees so that one new degree-one check appears. In expectation this is achieved by
$$\rho(1)=\tfrac1K,\qquad \rho(d)=\frac{1}{d(d-1)}\ \ (d=2,3,\dots,K). \tag{50.2}$$
The expected degree is roughly ln K. (Exercise 50.2 asks the reader to derive it. Its statement says that at iteration t, with t source packets recovered and h_t(d) packets of degree d, the expected number of degree-d packets reduced to degree d−1 is h_t(d)·d/(K−t) (for d > 1), and that the condition imposed is h_t(1) = 1 for all t (p. 592).)

*(added step)* The probabilities sum to 1, since $\sum_{d=2}^{K}\frac{1}{d(d-1)} = \sum_{d=2}^K\left(\frac1{d-1}-\frac1d\right)=1-\frac1K$, and $\rho(1)=1/K$.

**Why it fails in practice** (p. 592). Fluctuations around the expected behaviour make it very likely that at some point there is no degree-one check. Also a few source nodes receive no connections.

**Robust soliton distribution** (pp. 592–593). It has two extra parameters, c and δ. It aims at about
$$S \equiv c\,\ln(K/\delta)\sqrt{K} \tag{50.3}$$
expected degree-one checks throughout decoding, instead of 1.
- δ bounds the probability that decoding fails to finish after K′ packets have been received.
- c is a constant of order 1 if the aim is to prove Luby's main theorem. In practice it is a free parameter, and a value somewhat smaller than 1 gives good results (p. 592).

Define a positive function
$$\tau(d)=\begin{cases}\dfrac{S}{K}\dfrac1d & d=1,2,\dots,(K/S)-1\\[2mm] \dfrac{S}{K}\ln(S/\delta) & d=K/S\\[2mm] 0 & d>K/S\end{cases}\tag{50.4}$$
Add ρ and τ and normalize:
$$\mu(d)=\frac{\rho(d)+\tau(d)}{Z},\qquad Z=\sum_d \rho(d)+\tau(d). \tag{50.5}$$
The number of encoded packets needed for decoding to complete with probability at least 1−δ is **K′ = KZ** (p. 592).

**Numbers** (Fig. 50.2, p. 592): K = 10 000, c = 0.2, δ = 0.05 give S = 244, K/S = 41, Z ≃ 1.3. τ is largest at d = 1 and d = K/S. Fig. 50.3 (p. 592) plots S and K′ against c and δ for K = 10 000; its caption says Luby's main theorem proves that there exists a value of c such that, given K′ received packets, decoding recovers the K source packets with probability 1−δ.

**Luby's analysis** (p. 593):
- The small-d end of τ makes decoding start.
- The spike at d = K/S makes every source packet likely to be connected to a check at least once.
- Key result: for an appropriate constant c, receiving K′ = K + 2 ln(S/δ)·S checks ensures all packets are recovered with probability at least 1−δ.
- The author sets δ quite large in the illustrative figures, because the actual failure probability is much smaller than Luby's conservative analysis suggests (p. 593).
- In practice, LT codes can be tuned so a file of K ≃ 10 000 packets is recovered with about 5% overhead. Fig. 50.4 shows histograms of N; the text says 'a couple of settings' with mean overheads smaller than 5% and 10% respectively, while the caption lists three settings (p. 593). The settings (all δ = 0.5):
  - c = 0.01: S = 10, K/S = 1010, Z ≃ 1.01.
  - c = 0.03: S = 30, K/S = 337, Z ≃ 1.03.
  - c = 0.1: S = 99, K/S = 101, Z ≃ 1.1.

> **Intuition note.** The ideal soliton keeps exactly one "ready" check on average, so any bad luck stalls decoding. The robust version keeps a buffer of about S ready checks and a few high-degree packets, which costs some extra packets.

### 50.4 Applications (pp. 593–594)
**Storage** (p. 593).
- Unreliable tapes and drives suffer catastrophic losses of stored packets at a rate of something like 10⁻³ per day.
- Spray fountain packets over every available device. To restore, find K′ ≃ K packets from anywhere. Corrupted packets are simply skipped.
- Speed: a lost packet on a hard drive costs a full revolution to re-read. If drops are stored in consecutive sectors, no re-reading is ever needed. The drive could then run faster, at a higher noise level, with fewer resources on noisy-channel coding.
- Exercise 50.3 asks for a comparison with RAID.

**Broadcast** (p. 594).
- Ten thousand subscribers want a movie, and each house loses f = 0.1% of packets.
- Plain sequence plus retransmission requests: there would be a request for almost every packet. The broadcaster must repeat the whole broadcast twice, so most users wait roughly twice the ideal time.
- With a fountain, each subscriber recovers from any K′ ≃ K packets. A broadcast of, say, 1.1K packets suffices, and every house is very likely to recover the file.
- **Cars:** updates for in-car navigation databases, sent by satellite, with no feedback channel. A carousel repeats packets in a fixed periodic sequence. With a fountain, each car needs only the original file size plus 5%.

**Further reading** (p. 594). Digital Fountain's commercial encoders and decoders are more efficient than the LT codes described here, and work for all blocklengths. Shokrollahi (2003) presents raptor codes, an extension of LT codes with linear-time encoding and decoding.

### 50.5 Further exercises (pp. 594–595)
Exercise 50.4 asks the reader to redo 50.2 with h_t(1) = 1+S and to show
$$h_0(d)=\frac{K}{d(d-1)}+\frac{S}{d}\quad (d>1). \tag{50.6}$$
The second term is truncated beyond d = K/S and replaced by the spike. This is so that decoding complexity does not exceed O(K ln K) (p. 594). The other exercises are listed below.

### 50.6–50.7 Summary and conclusion (p. 596)
- Gallager (1962) pioneered a simple method of designing codes for noisy channels, since rediscovered and generalized. Low-density parity-check codes and their modern cousins perform far better than the textbook codes of the intervening years.
- Which sparse-graph code is best depends on rate, blocklength, permitted complexity, and whether occasional undetected errors are acceptable. LDPC codes are the most versatile and virtually never make undetected errors.
- For the erasure channel, digital fountain codes are the best sparse-graph codes.
- Conclusion: "Combine a simple, pseudo-random code with a message-passing decoder." (p. 596)

## Toy example (ours, not from the text)
Take K = 3 one-bit source packets s = (s₁,s₂,s₃) = (1,1,0). Four received checks are:
- t₁ = s₂ = 1
- t₂ = s₁+s₂ = 1+1 = 0
- t₃ = s₂+s₃ = 1+0 = 1
- t₄ = s₁+s₃ = 1+0 = 1

Decode as in (50.1):
1. t₁ has one neighbour, so s₂ = 1. Add it to the other checks containing s₂: t₂ := 0+1 = 1 (now just s₁), t₃ := 1+1 = 0 (now just s₃).
2. t₂ has one neighbour, so s₁ = 1. Add it to t₄: t₄ := 1+1 = 0 (now just s₃).
3. t₃ gives s₃ = 0. The leftover check t₄ = 0 agrees.

Result: (1,1,0), as sent.

Ideal soliton for K = 3: ρ(1) = 1/3, ρ(2) = 1/(2·1) = 1/2, ρ(3) = 1/(3·2) = 1/6. The sum is 2/6+3/6+1/6 = 1.

## Concepts
- [[erasure-channel]] (new) — q-ary channel that delivers each symbol intact with probability 1−f, else outputs '?'; q = 2^l for l-bit packets (p. 589)
- [[channel-capacity]] — for this channel (1−f)l bits per use, with or without feedback (p. 589)
- [[error-correcting-code]] — here Reed–Solomon block codes versus fountain codes for erasures (pp. 589–590)
- [[rateless-code]] (new) — a code that can generate unlimited encoded packets, with their number chosen on the fly (p. 590)
- [[fountain-code-lt]] (new) — encoded packet is the XOR of d random distinct source packets, with d drawn from ρ(d) (p. 590)
- [[sparse-graph-code]] (new) — code defined by a graph with mean degree much less than K, giving cheap message-passing decoding (p. 590)
- [[peeling-decoder]] (new) — erasure-channel message-passing that repeatedly resolves a degree-one check and subtracts it from the others (p. 591)
- [[soliton-distribution]] (new) — degree distribution (ideal, eq. 50.2; robust, eq. 50.5) designed so degree-one checks keep appearing (pp. 592–593)
- [[universal-code]] — here, Luby's sense: near-optimal simultaneously for every erasure channel (p. 590)
- [[coupon-collector-balls-in-bins]] (new) — Exercise 50.1: N random inspections cover all K pages with probability 1−δ only if N ≃ K ln(K/δ) (the exercise says this is required) (p. 588)

## Canonical instances
- [[fig-50-1-decoding]] — K = 3, N = 4 worked peeling decoding of t = 1011 (p. 591)
- [[robust-soliton-k10000]] — K = 10 000, c = 0.2, δ = 0.05, S = 244, Z ≃ 1.3 (p. 592)
- [[movie-broadcast]] — 10 000 subscribers, f = 0.1%: fountain needs about 1.1K packets, plain retransmission about twice the ideal time (p. 594)
- [[car-carousel]] — navigation updates by satellite; fountain needs file size plus 5% (p. 594)
- [[storage-backup-sectors]] — spraying drops across devices; avoiding a disk revolution on re-read (p. 593)

## Bridges (candidates)
- [structural-analogy] Peeling decoder with certain/uncertain messages ↔ bayesian: belief propagation on a factor graph — the text calls it sum–product with extreme messages.
- [structural-analogy] Exercise 50.1 balls-in-bins, N ≃ K ln(K/δ) ↔ the K ln(K/δ) cost scale of LT codes — same expression, not stated to be linked in the text.
- [same-math] Optimal decoding as solving t = Gs over GF(2), and "random K×K matrix has full rank" (Ex. 50.11) ↔ linear algebra over GF(2) — both are solving linear equations mod 2.
- [structural-analogy] Rateless coding ↔ information-theory: sequential universal coding — neither rate nor channel needs to be known in advance.

## Questions this raises
- How exactly does the ideal soliton follow from the recursion h_t(d)·d/(K−t) (Ex. 50.2), and why does the expectation hide such large fluctuations?
- How much overhead can an optimal (Gaussian-elimination-style) decoder save compared with the peeling decoder, and at what cost?
- Is Luby's bound K + 2 ln(S/δ)S tight? The text says the actual failure probability is much smaller.
- Can the fountain idea be extended to channels with both noise and erasures (Ex. 50.13)?

## Exercises worth doing
- Ex. 50.1 (p. 588) — coupon collector: derive N ≃ K ln(K/δ); background for the cost of fountain codes — difficulty: medium
- Ex. 50.2 (p. 592) — derive the ideal soliton distribution via the recursion on h_t(d) — difficulty: easy–medium
- Ex. 50.4 (p. 594) — redo it with h_t(1) = 1+S to see where the robust soliton comes from, and compare packet and edge counts — difficulty: medium
- Ex. 50.9 (p. 595) — model broadcast to cars and quantify the fountain's advantage over the carousel — difficulty: medium
- Ex. 50.11 (p. 595) — probability that K random XOR packets are decodable by an optimal decoder is a little below 1/2; with K+Δ packets the failure probability is about 2^{−Δ} — difficulty: easy–medium
- Ex. 50.6 (p. 595) — experiment on whether the spike at d = K/S and the tail of ρ are needed — difficulty: medium (computational)

## Reading notes
- Printed page = pdf − 12 (pdf 600–608 are printed 588–596). The equations are readable in the page images; the text layer garbles some symbols (primes appear as 'K 0', and ≳ can be dropped), so symbols were checked against the images.
- Page 588 is the "About Chapter 50" page containing only Exercise 50.1.
- Exercise numbers carry difficulty ratings in the source, for example [3], [4C].
- The source does not derive Luby's theorem or the ideal soliton. These are left to Exercises 50.2 and 50.7, so L3 only reports the stated results.
- K′ = KZ (p. 592) and K′ = K + 2 ln(S/δ)S (p. 593) are both stated as numbers of packets that guarantee success with probability at least 1−δ. The text says the real failure probability is much smaller, and practical overhead is about 5%. Fig. 50.2 gives Z ≃ 1.3 for c = 0.2, δ = 0.05; the text does not relate this value to the 5% practical-overhead figure.
- In the source figure, Fig. 50.1's panels are small. I read s₃ = 1 from panel f ("1 0 1").
