---
id: cover-2006-elements/ch06-gambling
work: cover-2006-elements
unit: "6 Gambling and Data Compression"
pages: 125-143
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Gambling and Data Compression

## L0 — One line
In a horse race with independent outcomes, if all wealth is bet each race and there is no cash option, betting in proportion to the win probabilities gives the best exponential growth of wealth, and that growth rate is tied to entropy and mutual information, and (through arithmetic coding) to data compression.

## L1 — The gist (≤ 120 words)
Question: how does betting relate to entropy? In a horse race with independent, identically distributed outcomes, a gambler who invests all wealth each race and has no cash option maximises the exponential growth rate of wealth by betting in proportion to the win probabilities. For uniform fair odds, growth rate plus entropy equals log m. In a horse race, the gain in growth rate from side information equals its mutual information with the outcome. A gambler's bets can also be used for arithmetic coding: when both sides know the bets, log S_n bits are saved. The chapter uses this to estimate the entropy rate of English from human guessing and betting experiments.

**Prerequisites:** entropy, relative entropy D(p‖q) ≥ 0 and mutual information; weak law of large numbers; Lagrange multipliers; arithmetic coding (Section 5.10, cited but not re-derived here); Markov chains; stationary and ergodic processes.

## L2 — Key ideas
- **Setup.** m horses; horse i wins with probability $p_i$; "$o_i$-for-1" odds pay $o_i$ dollars per dollar staked on a winner. The doubling rate $W(\mathbf b,\mathbf p)=E\log S(X)$ (the expected log of the wealth relative $S(X)=b(X)o(X)$) governs growth: for i.i.d. races $S_n \doteq 2^{nW}$ (pp. 126–127).
- **Proportional gambling.** If all wealth is invested, races are i.i.d. and there is no cash option, $\mathbf b=\mathbf p$ maximises $W$, and $W^*=\sum p_i\log o_i-H(\mathbf p)$ (pp. 127–128).
- **Fair odds.** Odds are *fair* if $\sum 1/o_i=1$; then $r_i=1/o_i$ is the bookie's estimate and $W=D(\mathbf p\|\mathbf r)-D(\mathbf p\|\mathbf b)$. The gambler profits only if $\mathbf b$ is closer to $\mathbf p$ than $\mathbf r$ is (p. 128). For *uniform* fair odds ($o_i=m$), $W^*+H(\mathbf p)=\log m$ (p. 129).
- **Cash option.** Fair odds: proportional betting stays optimal. *Superfair* ($\sum 1/o_i<1$, odds better than fair): proportional betting is still optimal. *Subfair* ($\sum 1/o_i>1$, a track take): usually desirable to bet only part of the wealth, and proportional betting is no longer log-optimal (pp. 129–130).
- **Side information.** For a horse race, the increase in doubling rate from side information $Y$ is exactly $I(X;Y)$. For a general stock market only $\Delta W\le I$ is shown (pp. 130–131).
- **Dependent races.** For a stationary process with uniform fair odds, the limiting expected growth rate plus the entropy rate equals $\log m$; for ergodic races the almost-sure growth is $2^{nW}$ (stated here, proved in Chapter 15) (pp. 131–132).
- **Gambler as compressor.** A known deterministic betting scheme gives a code of length $\lceil n-\log S_n\rceil$ (arithmetic-coding style); with proportional gambling, expected length ≤ $H+1$ (pp. 137–138).
- **Entropy of English.** Markov approximations give estimates 4.76, 4.03, 2.8 bits per letter; Shannon's guessing game gave 1.3; a gambling experiment gave 1.34 (pp. 135, 139–140).

## L3 — Walkthrough

### Introduction (p. 125)
The author states a duality between the growth rate of a horse-race investment and the entropy rate of the race; he says that for the case treated, their sum is constant. He says he will argue that side information is worth its mutual information, that two identical gamblers can compress data, and that gambling can estimate the entropy rate of English (p. 125). The horse race is a special case of the stock market of Chapter 15.

### 6.1 The horse race (pp. 125–130)
**Odds.** Horse $i$ wins with probability $p_i$; payoff $o_i$ for 1. *a-for-1* is paid before the race (stake handed over; receive $a$ if the horse wins). *b-to-1* is paid after the race (pay 1 if the horse loses, receive $b$ if it wins). A b-to-1 bet equals an a-for-1 bet if $b=a-1$ (pp. 125–126).

The gambler invests all wealth, fraction $b_i\ge0$, $\sum b_i=1$ (also written $b(i)$). If horse $i$ wins, wealth is multiplied by $b_io_i$ (p. 126). Betting everything on the horse with highest $p_io_i$ is tempting but risky: all money could be lost. Looking at repeated races helps: with $S_n$ the wealth after $n$ races,
$$S_n=\prod_{i=1}^n S(X_i),\tag{6.1}$$
where the **wealth relative** $S(X)=b(X)o(X)$ is the factor by which wealth grows if horse $X$ wins (p. 126).

**Doubling rate:**
$$W(\mathbf b,\mathbf p)=E(\log S(X))=\sum_{k=1}^m p_k\log b_ko_k.\tag{6.2}$$

**Theorem 6.1.1.** If $X_1,\dots,X_n$ are i.i.d. $\sim p(x)$, wealth with strategy $\mathbf b$ grows as $S_n\doteq 2^{nW(\mathbf b,\mathbf p)}$ (6.3). (The sign $\doteq$ is not defined on these pages; (6.4) shows it means $\tfrac1n\log S_n\to W$ in probability.)

*Proof.* Functions of independent variables are independent, so $\log S(X_1),\dots,\log S(X_n)$ are i.i.d. By the weak law of large numbers
$$\frac1n\log S_n=\frac1n\sum_{i=1}^n\log S(X_i)\to E(\log S(X))\ \text{in probability},\tag{6.4}$$
hence $S_n\doteq2^{nW(\mathbf b,\mathbf p)}$ (6.5) (p. 127).

*Intuition note.* Each race multiplies wealth by a random factor, so over many races the *average of the logs* decides growth. The doubling rate is that average, in bits per race.

**Optimum doubling rate:**
$$W^*(\mathbf p)=\max_{\mathbf b}W(\mathbf b,\mathbf p)=\max_{\mathbf b:\,b_i\ge0,\sum b_i=1}\sum_{i=1}^m p_i\log b_io_i.\tag{6.6}$$
Lagrange functional and derivative:
$$J(\mathbf b)=\sum p_i\log b_io_i+\lambda\sum b_i,\tag{6.7}$$
$$\frac{\partial J}{\partial b_i}=\frac{p_i}{b_i}+\lambda,\quad i=1,\dots,m.\tag{6.8}$$
Setting this to 0 gives
$$b_i=-\frac{p_i}{\lambda}.\tag{6.9}$$
Substituting in $\sum b_i=1$ gives $\lambda=-1$ and $b_i=p_i$. So $\mathbf b=\mathbf p$ is a stationary point. Checking it is a maximum by second derivatives is tedious, so the author uses "guess and verify" (p. 127).

**Theorem 6.1.2 (Proportional gambling is log-optimal).** $W^*(\mathbf p)=\sum p_i\log o_i-H(\mathbf p)$ (6.10), achieved by $\mathbf b^*=\mathbf p$.

*Proof.*
$$W(\mathbf b,\mathbf p)=\sum p_i\log b_io_i\tag{6.11}$$
$$=\sum p_i\log\Big(\frac{b_i}{p_i}p_io_i\Big)\tag{6.12}$$
$$=\sum p_i\log o_i-H(\mathbf p)-D(\mathbf p\|\mathbf b)\tag{6.13}$$
$$\le\sum p_i\log o_i-H(\mathbf p),\tag{6.14}$$
with equality iff $\mathbf p=\mathbf b$. (Added step: (6.13) uses $\sum p_i\log p_i=-H(\mathbf p)$ and $\sum p_i\log(b_i/p_i)=-D(\mathbf p\|\mathbf b)$; (6.14) uses $D\ge0$.) (p. 128)

**Example 6.1.1.** Two horses, win probabilities $p_1,p_2$, even odds (2-for-1 on both). The optimal bet is $b_1=p_1,b_2=p_2$, so $W^*=\sum p_i\log o_i-H(\mathbf p)=1-H(\mathbf p)$ and
$$S_n^*\doteq2^{n(1-H(\mathbf p))}.\tag{6.15}$$
The author concludes that proportional betting is growth-rate optimal for i.i.d. races *if the gambler can reinvest his wealth and if there is no alternative of keeping some of the wealth in cash* (p. 128).

*Intuition note.* Any deviation of your bets $\mathbf b$ from the win probabilities $\mathbf p$ lowers the doubling rate below its maximum, and the amount lost is exactly the relative entropy $D(\mathbf p\|\mathbf b)$ (6.13).

**Fair odds.** Suppose $\sum 1/o_i=1$ (no track take). Write $r_i=1/o_i$; this is a probability mass function over horses (the bookie's estimate of win probabilities). Then
$$W(\mathbf b,\mathbf p)=\sum p_i\log b_io_i\tag{6.16}$$
$$=\sum p_i\log\Big(\frac{b_i}{p_i}\frac{p_i}{r_i}\Big)\tag{6.17}$$
$$=D(\mathbf p\|\mathbf r)-D(\mathbf p\|\mathbf b).\tag{6.18}$$
The doubling rate is the distance from the bookie's estimate to the truth minus the distance from the gambler's estimate to the truth. So the gambler can make money only if his estimate $\mathbf b$ is better than the bookie's (p. 128).

**Uniform fair odds** ($m$-for-1 on each horse, fair with respect to the uniform distribution):
$$W^*(\mathbf p)=D\Big(\mathbf p\Big\|\frac1m\Big)=\log m-H(\mathbf p).\tag{6.19}$$
**Theorem 6.1.3 (Conservation theorem).** For uniform fair odds,
$$W^*(\mathbf p)+H(\mathbf p)=\log m.\tag{6.20}$$
The author's reading: every bit of entropy decrease doubles the gambler's wealth, and low-entropy races are the most profitable (p. 129).

*Intuition note.* With uniform fair odds, a fixed budget of $\log m$ bits per race is split between what is still uncertain (entropy) and what you can turn into money (growth).

**Cash option.** Let $b(0)$ be the fraction kept as cash. The wealth relative is
$$S(X)=b(0)+b(X)o(X).\tag{6.21}$$
The optimum "may depend on the odds and will not necessarily have the simple form of proportional gambling." Three subcases (pp. 129–130):
1. *Fair odds* ($\sum1/o_i=1$). Betting $b_i=1/o_i$ gives $S(X)=1$ whichever horse wins, so cash can equally be spread over the horses. The cash option does not change the analysis; proportional betting is optimal.
2. *Superfair odds* ($\sum1/o_i<1$). One would want all wealth in the race, and proportional betting is optimal. A "Dutch book" $b_i=1/o_i$ gives $o_ib_i=1$ for every winner, leaves $1-\sum1/o_i$ in cash, and ends with wealth $1+(1-\sum1/o_i)>1$ with probability 1 (no risk). Such odds are seldom found in real life. A Dutch book does not optimise the doubling rate.
3. *Subfair odds* ($\sum1/o_i>1$; the track takes a cut; "more representative of real life"). It is usually desirable to bet only some of the money and keep the rest as cash. Proportional gambling is no longer log-optimal.

### 6.2 Gambling and side information (pp. 130–131)
The author takes as one definition of the financial value of side information the increase in wealth it produces, measured here as the increase in doubling rate. Let $X\in\{1,\dots,m\}$ win with probability $p(x)$ and pay $o(x)$ for 1. Let $(X,Y)\sim p(x,y)$. A conditional strategy has $b(x|y)\ge0$, $\sum_xb(x|y)=1$. Define
$$W^*(X)=\max_{\mathbf b(x)}\sum_xp(x)\log b(x)o(x),\tag{6.22}$$
$$W^*(X|Y)=\max_{\mathbf b(x|y)}\sum_{x,y}p(x,y)\log b(x|y)o(x),\tag{6.23}$$
$$\Delta W=W^*(X|Y)-W^*(X).\tag{6.24}$$
For i.i.d. races $(X_i,Y_i)$, wealth grows like $2^{nW^*(X|Y)}$ with side information and $2^{nW^*(X)}$ without (p. 130).

**Theorem 6.2.1.** $\Delta W=I(X;Y)$ (6.25).

*Proof.* With side information, the maximum is achieved by conditionally proportional gambling $b^*(x|y)=p(x|y)$. Thus
$$W^*(X|Y)=\max_{\mathbf b(x|y)}E[\log S]=\max_{\mathbf b(x|y)}\sum p(x,y)\log o(x)b(x|y)\tag{6.26}$$
$$=\sum p(x,y)\log o(x)p(x|y)\tag{6.27}$$
$$=\sum p(x)\log o(x)-H(X|Y).\tag{6.28}$$
Without side information,
$$W^*(X)=\sum p(x)\log o(x)-H(X).\tag{6.29}$$
Hence
$$\Delta W=W^*(X|Y)-W^*(X)=H(X)-H(X|Y)=I(X;Y).\tag{6.30}$$
The increase equals the mutual information; independent side information does not increase the doubling rate (pp. 130–131). For the general stock market (Chapter 15) one can only show $\Delta W\le I$, with equality iff the market is a horse race (p. 131).

*Intuition note.* Side information is worth exactly the uncertainty it removes, measured in bits of growth per race. This holds for horse races (and not as an equality in general markets).

### 6.3 Dependent horse races and entropy rate (pp. 131–133)
If races are independent, past results are useless. If $\{X_k\}$ is a stochastic process and the strategy for race $k$ may depend on earlier results, then for uniform fair odds the optimal doubling rate is
$$W^*(X_k|X_{k-1},\dots,X_1)=E\Big[\max_{b(\cdot|X_{k-1},\dots,X_1)}E[\log S(X_k)\,|\,X_{k-1},\dots,X_1]\Big]=\log m-H(X_k|X_{k-1},\dots,X_1),\tag{6.31}$$
achieved by $b^*(x_k|x_{k-1},\dots,x_1)=p(x_k|x_{k-1},\dots,x_1)$. With $S_n=\prod S(X_i)$ (6.32), and $m$-for-1 odds (p. 132):
$$\frac1nE\log S_n=\frac1n\sum E\log S(X_i)\tag{6.33}$$
$$=\frac1n\sum\big(\log m-H(X_i|X_{i-1},\dots,X_1)\big)\tag{6.34}$$
$$=\log m-\frac{H(X_1,\dots,X_n)}{n}.\tag{6.35}$$
(Added step: the step to (6.35) is the chain rule for entropy.) For a stationary process with entropy rate $H(\mathcal X)$:
$$\lim_{n\to\infty}\frac1nE\log S_n+H(\mathcal X)=\log m.\tag{6.36}$$
The expectation can be removed if the process is ergodic. The author says it "will be shown in Chapter 15" that for an ergodic sequence of horse races
$$S_n\doteq2^{nW}\ \text{with probability }1,\tag{6.37}$$
where $W=\log m-H(\mathcal X)$ and $H(\mathcal X)=\lim\frac1nH(X_1,\dots,X_n)$ (6.38) (p. 132).

**Example 6.3.1 (Red and Black).** A deck of 26 red and 26 black cards; bet on the colour of the next card at 2-for-1 (fair if red and black are equally likely). Two schemes (pp. 132–133):
1. *Sequential proportional betting* using the conditional probability of the next card: $(\frac12,\frac12)$ on (red, black) for the first card; $(\frac{26}{51},\frac{25}{51})$ for the second if the first was black, etc.
2. *Bet on the whole 52-card sequence at once:* there are $\binom{52}{26}$ equally likely sequences; put $1/\binom{52}{26}$ of the money on each and let each bet "ride".

The schemes are equivalent. For example, half the sequences start with red, so half the money rides on red-first sequences, matching scheme 1. In general, betting $1/\binom{52}{26}$ on every sequence gives, at each stage, bets proportional to the current probability of red and black. The wealth is (6.39), which the text layer on p. 133 does not give legibly (no image supplied): [unreadable p. 133]. (Added step: only the observed sequence pays, and 52 compounded 2-for-1 bets pay $2^{52}$ on it, so wealth is $2^{52}/\binom{52}{26}$.) The author's remarks: the return does not depend on the actual sequence; this is like the AEP in that the return is the same for all sequences, and all sequences are typical in this sense (p. 133).

### 6.4 The entropy of English (pp. 133–136)
English is probably not a stationary ergodic process ("Probably not!"), but its entropy rate is still of interest; better stochastic models give better compression (p. 133). The alphabet is 26 letters plus a space; punctuation and case are ignored. Facts given: letter frequencies are far from uniform (E about 13%, Q and Z about 0.1%); Q is always followed by U; the most frequent pair is TH, about 3.7% (p. 133). Higher-order models run out of data: a third-order model needs $27^4=531441$ entries of $p(x_i|x_{i-1}x_{i-2}x_{i-3})$, so "millions of letters" would be needed (p. 134). A book can simulate the second-order model: pick a random letter, then repeatedly search a random page for the previous letter and take the letter after it (p. 134).

Shannon's approximations (pp. 134–135): zero-order (equiprobable independent symbols); first-order (English letter frequencies); second-order (English pair frequencies); third-order (triplets); fourth-order (each letter depends on the previous three; sample from Lucky's *Silicon Dreams*); first-order word model (words independent, English frequencies); second-order word model (English word transitions). Samples look more English as the order rises; the author says a very good approximation might follow from a more complex model (p. 135).

Entropy estimates: zeroth order $\log27=4.76$ bits per letter; first order 4.03; fourth order 2.8. Even the fourth-order model does not capture all the structure of English (pp. 135–136).

Other uses (p. 136): a simple substitution cipher can be attacked by guessing that the most frequent letter replaces E; English redundancy can be used to fill in some missing letters after the other letters are decrypted; Shannon's work in cryptography in World War II inspired part of his theory; trigram (second-order Markov) word models are used in some speech recognition systems and do surprisingly well even without explicit grammar rules.

### 6.5 Data compression and gambling (pp. 136–138)
The author claims a good gambler is also a good data compressor: any sequence on which a gambler makes a large amount of money can be compressed by a large factor. The gambler's bets are his estimate of the probability distribution, and this estimate can drive arithmetic coding (Section 5.10). The decoder is a mechanically identical twin who places the same bets (pp. 136–137).

Let $X_1,\dots,X_n$ be binary (without loss of generality). Bets:
$$b(x_{k+1}|x_1,\dots,x_k)\ge0,\qquad\sum_{x_{k+1}}b(x_{k+1}|x_1,\dots,x_k)=1.\tag{6.40}$$
At 2-for-1 odds,
$$S_n=2^n\prod_{k=1}^nb(x_k|x_1,\dots,x_{k-1})\tag{6.41}$$
$$=2^nb(x_1,\dots,x_n),\tag{6.42}$$
$$b(x_1,\dots,x_n)=\prod_{k=1}^nb(x_k|x_{k-1},\dots,x_1).\tag{6.43}$$
So sequential gambling assigns probabilities $b(x_1,\dots,x_n)\ge0$, summing to 1, to the $2^n$ sequences. It yields an estimate $\hat p(x_1,\dots,x_n)=S_n/2^n$ of the true probability and an entropy estimate $\hat H=-\frac1n\log\hat p$. The author states that if the text gives wealth $S_n$, then $\log S_n$ bits can be saved in a naturally associated deterministic compression scheme, and with log-optimal gambling the Shannon limit $H$ is achieved (p. 137).

**Algorithm** (maps $x^n\in\{0,1\}^n$ to $c_1\dots c_k$; both sides know $n$) (p. 138):
- Order the $2^n$ sequences lexicographically (e.g. $0100101<0101101$).
- The encoder computes $F(x(n))=\sum_{x'(n)\le x(n)}2^{-n}S_n(x'(n))\in[0,1]$.
- Let $k=\lceil n-\log S_n(x(n))\rceil$. Write $\lfloor F(x(n))\rfloor=.c_1c_2\dots c_k$ (binary decimal to $k$ places, as printed). Transmit $c_1\dots c_k$.
- The decoder twin computes $S(x'(n))$ for all sequences, accumulates $2^{-n}S$ until the sum first falls in $[.c_1\dots c_k,\ .c_1\dots c_k+(1/2)^k]$. The size of $S(x(n))/2^n$ guarantees that this sequence is exactly the encoded one.

Bits used: $k=\lceil n-\log S(x(n))\rceil$; bits saved: $n-k=\lfloor\log S(x(n))\rfloor$. For proportional gambling $S(x(n))=2^np(x(n))$, so
$$E k=\sum p(x(n))\lceil-\log p(x(n))\rceil\le H(X_1,\dots,X_n)+1.$$
Thus with a deterministic betting scheme known to encoder and decoder, the number of bits needed is less than $n-\log S_n+1$; with known $p$ and proportional gambling, $E(n-\log S_n)\le H(X_1,\dots,X_n)+1$ (p. 138). This is arithmetic coding with $b(x_1,\dots,x_n)$ instead of the true distribution. Both gambling and compression need an estimate of the true distribution; the better the estimate, the faster wealth grows and the better the compression.

*Intuition note.* The gambler's bets define a code: a sequence he bets heavily on gets a short codeword, one he bets lightly on a long one. Gaining $\log S_n$ bits of wealth and saving $\log S_n$ bits of code are two views of the same estimate.

### 6.6 Gambling estimate of the entropy of English (pp. 138–140)
Two proposed approaches, with 27 characters:
1. **Shannon guessing game.** A subject guesses the next letter, most probable first; the experimenter records the number of guesses. Model the subject as a deterministic machine: given the same machine and the sequence of guess numbers, the text can be reconstructed. So the guess sequence carries the same information as the text, and its entropy is the entropy of English. Assuming samples independent, this is bounded above by the entropy of the histogram of guess counts. Shannon's 1950 experiment gave 1.3 bits per symbol (p. 139).
2. **Gambling estimate.** A subject bets on the next letter; this gives finer gradations than guessing. The optimal bet is proportional to the conditional probability; payoff is 27-for-1. Since sequential betting equals betting on the whole sequence,
$$S_n=(27)^nb(X_1,\dots,X_n).\tag{6.44}$$
Expected log wealth:
$$E\frac1n\log S_n=\log27+\frac1nE\log b(X_1,\dots,X_n)\tag{6.45}$$
$$=\log27+\frac1n\sum_{x^n}p(x^n)\log b(x^n)\tag{6.46}$$
$$=\log27-\frac1n\sum_{x^n}p(x^n)\log\frac{p(x^n)}{b(x^n)}+\frac1n\sum_{x^n}p(x^n)\log p(x^n)\tag{6.47}$$
$$=\log27-\frac1nD(p(x^n)\|b(x^n))-\frac1nH(X_1,\dots,X_n)\tag{6.48}$$
$$\le\log27-\frac1nH(X_1,\dots,X_n)\tag{6.49}$$
$$\le\log27-H(\mathcal X),\tag{6.50}$$
where $H(\mathcal X)$ is the entropy rate of English (p. 140). Hence $\log27-E\frac1n\log S_n$ is an upper bound on the entropy rate of English. The estimate $\hat H=\log27-\frac1n\log S_n$ converges to $H$ with probability one if English is ergodic and the gambler uses $b(x^n)=p(x^n)$. An experiment [72] with 12 subjects and 75 letters of *Jefferson the Virginian* (Shannon's source) gave 1.34 bits per letter (p. 140).

### Summary, problems, notes (pp. 140–143)
The chapter summary restates (6.2), (6.6), (6.51)–(6.53) (growth $S_n\doteq2^{nW^*}$; conservation $H+W^*=\log m$; $\Delta W=I(X;Y)$) (p. 140). Problems: three-horse races with 3-for-1 odds, unfair odds and cash, card colours, "beating public odds", very bad odds ($o=(1,1,1)$), sequential betting on cards, and St. Petersburg and super St. Petersburg paradoxes (pp. 141–143). Historical notes (p. 143): Kelly originally treated the horse race and found $\Delta W=I$; proportional gambling is sometimes called the Kelly gambling scheme; the gambling estimate of English is credited to Cover and King, the St. Petersburg analysis to Bell and Cover.

## Toy example (ours, not from the text)
Two horses, $\mathbf p=(\tfrac34,\tfrac14)$, 2-for-1 odds on each (fair, $r=(\tfrac12,\tfrac12)$).
- $H(\mathbf p)=-\tfrac34\log_2\tfrac34-\tfrac14\log_2\tfrac14=0.75(0.41504)+0.25(2)=0.31128+0.5=0.81128$ bits.
- $W^*=1-H=0.18872$ bits per race, with $\mathbf b=\mathbf p$.
- Check: $W=0.75\log_2(0.75\cdot2)+0.25\log_2(0.25\cdot2)=0.75(0.58496)+0.25(-1)=0.43872-0.25=0.18872$. ✓
- Compare $\mathbf b=(\tfrac12,\tfrac12)$: every wealth relative is $0.5\cdot2=1$, so $W=0$. Formula (6.18): $D(\mathbf p\|\mathbf r)-D(\mathbf p\|\mathbf b)=0.18872-0.18872=0$ (both equal $1-H$). ✓
- All money on horse 1: $W=-\infty$; wealth is 0 after the first horse-2 win.
- Typical sequence: 4 races, horse 1 wins 3 times, horse 2 once: $S_4=(1.5)^3(0.5)=3.375\times0.5=1.6875$; $\tfrac14\log_2 1.6875=0.7549/4=0.1887\approx W^*$.
- Side information: if $Y$ tells the winner perfectly, $H(X|Y)=0$, $W^*(X|Y)=1$, $\Delta W=1-0.18872=0.81128=H(X)=I(X;Y)$. ✓

## Concepts
- [[kelly-criterion-doubling-rate]] — doubling rate $W=E\log S$; proportional betting maximises it under the stated conditions (p. 126–128)
- [[entropy-rate]] — $H(\mathcal X)=\lim\frac1nH(X_1,\dots,X_n)$ for dependent races or English (p. 132)
- [[mutual-information]] — in a horse race equals the doubling-rate gain from side information (p. 131)
- [[relative-entropy-kl-divergence]] — the loss from betting $\mathbf b$ instead of $\mathbf p$ is $D(\mathbf p\|\mathbf b)$ (p. 128)
- [[huffman-arithmetic-coding]] — gambler's bets used as the distribution for arithmetic coding (p. 138)
- [[typical-set-aep]] — only an analogy here: red-and-black return is the same for all sequences (p. 133)
- [[wealth-relative]] (new) — factor $S(X)=b(X)o(X)$ (or $b(0)+b(X)o(X)$ with cash) (pp. 126, 129)
- [[odds-fair-sub-superfair]] (new) — $\sum1/o_i=1$, $>1$, $<1$; fair odds define bookie's estimate $r_i=1/o_i$ (pp. 128–130)
- [[dutch-book]] (new) — bets $b_i=1/o_i$ under superfair odds giving a risk-free gain (p. 129)
- [[shannon-guessing-game]] (new) — guess-count sequence as a stand-in for English entropy (p. 139)
- [[markov-approximations-of-english]] (new) — order-$k$ letter/word models and entropy estimates (pp. 134–135)

## Canonical instances
- [[horse-race-gambling]] — two-horse race, $W^*=1-H(\mathbf p)$ (p. 128)
- [[red-and-black-cards]] — betting on the colour of cards in a 52-card deck (p. 132)
- [[entropy-of-english]] — 4.76, 4.03, 2.8 (models), 1.3 (guessing), 1.34 (gambling) bits/letter (pp. 135, 139–140)
- [[st-petersburg-paradox]] — appears only as Problems 7–8 (pp. 142–143)

## Bridges (candidates)
- [same-math] Doubling rate with side information, $\Delta W=I(X;Y)$ ↔ Kelly criterion: side information raises growth by its mutual information — same quantity.
- [same-math] Gambler's compression length $n-\log S_n$ ↔ arithmetic coding with an estimated distribution $b$ — the text calls the scheme similar to arithmetic coding with $b$ in place of the true distribution.
- [structural-analogy] Excess code length / lost growth $D(p\|b)$ (6.48) ↔ cross-entropy training loss of language models: a worse model estimate costs more bits.
- [structural-analogy] Human betting as probability elicitation ↔ evaluating predictors by the log score.

## Questions this raises
- What happens to the growth-rate duality when odds are not fair or not uniform, and the cash option matters?
- Why do general stock markets give only $\Delta W\le I$ (Chapter 15)?
- How reliable are human-subject estimates when English is probably not stationary ergodic?
- Can the gambler–compressor idea work when the bets cannot be reproduced exactly by the decoder?

## Exercises worth doing
- Ex. 1 (p. 141) — find $b^*$ and $W^*$ for 3-for-1 odds; show all-in on horse 1 goes broke — difficulty: easy
- Ex. 2 (p. 141) — cash option with $\sum1/o(i)<1$ and discussion of the subfair case — difficulty: medium
- Ex. 3 (p. 141) — entropies and conditional entropy in the card deck — difficulty: easy
- Ex. 6 (p. 142) — optimal sequential betting on the card deck, ties to Example 6.3.1 — difficulty: medium
- Ex. 7 (p. 142) — St. Petersburg paradox with reinvestment; fair entry fee $c^*$ — difficulty: hard

## Reading notes
- The PDF is the 1991 first edition (header of p. 125: "Copyright 1991 John Wiley & Sons, Inc.", ISBN 0-471-06259-6), although the metadata cites the 2006 second edition. Printed page = pdf page − 22.
- Pages pp. 125 and 133–136 (pdf 147, 155–158) were supplied as text only, without images. All other pages were checked against images.
- On p. 133 the text layer says "a factor of 26" and prints no formula for (6.39). The text-layer rendering is garbled, so (6.39) is marked unreadable; the value $2^{52}/\binom{52}{26}$ in L3 is my added step.
- Several text-layer running heads are misread (e.g. "326", "339", "343" for pp. 126, 139, 143); the images show the correct numbers.
- The sample ciphertext on p. 136 and some equations on pp. 127–128 are garbled in the text layer; the images were used for equations.
- The sign $\doteq$ is used without definition in this unit (defined elsewhere in the book).
