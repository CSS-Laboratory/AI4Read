# Chinese audio script check: audio-script-zh.md against audio-script.md

Post: 2026-10-residual-stream. Checked on 2026-11-04 by an independent bilingual fact-checker.
I used `src/content.html` only to resolve meaning in four places: Nanda's "the stream has no neurons" (cited to Nanda; the "so" clause is ours), the open question's "(ours; real blocks are not linear)", the "What this does not say" paragraph, and the 6.2e−6 denominator.
I tested how the voice reads some text by running the script's own G2P (`/tmp/zh312`, Kokoro-82M-v1.1-zh with misaki[zh] and the English fallback, as in `scripts/tts_post_zh.py`).

## Structural checks

- **Chapter ids and order (pass).** Both files have the same ids in the same order: hook, guess, sum, bets, rw, dir, answer, lens-linalg, lens-info, turn, work, recall.
- **Opening (pass).** hook opens with "欢迎收听 AI4Read，来自 CSS Lab。" The allowed sentence "文中引用的原话都是我们的中文翻译。" appears once, in hook.
- **Numbers, vectors and values (all pass).** I checked every one against the English and recomputed the arithmetic:
  - 768, 2,048, and Qwen3 1.7B (十七亿).
  - The toy writes and the running stream: (1,2) → (3,1) → (2,2) → (5,0) → (4,2).
  - The norm example: (4,2) has mean 3 and SD 1. (8,4) has mean 6 and SD 2. Both centre and scale to (1,−1).
  - 6.2e−6 (六点二乘以十的负六次方), with its denominator ("相对于该位置上这个块自己的两个写入的大小") kept in both sum and recall.
  - The read shares 5/0/1/−1, and 7.211561 with 13 shares.
  - u = (−0.707, 0.707), the foot check (0.6,0.8)·(5,0) = 3, 3u = (1.8,2.4), x − foot = (3.2,−2.4), and 1.92 − 1.92 = 0.
  - Scores ±1.414 and the margin 2.828.
  - Margins by angle: 0° gives −4, 45° gives −2.828, 90° gives 0, 120° gives 2, and 135° gives 2.828.
  - v = (−2,2) gives u·v = 2.828, and (2,2) gives 0.
  - The rotation: (5,0) → (0,5), r → (−2,1), and the read stays 5.
  - Cosines 0.1318 and 1.0935.
  - Fifty thousand tokens and 768 dimensions.
  - The 120° readers: 1, −½, −½.
  - Stream length from about 5 to 472.
  - The matrix [[2,1],[1,2]]: (1,0) → (2,1), (1,1) → (3,3), (1,−1) → (1,−1), so stretches of 3 and 1.
  - The blind probe's scores: 2.828, 4.243 and 5.657.
- **Measured numbers keep their frame (pass).** GPT-2 small, float32 with about seven significant digits, and "the cat sat on the mat because" are all kept. So are "在这次运行里", "对我们试过的每一个 alpha", "我们没有运行任何训练好的 Qwen3、Llama、Gemma 或 Mistral 模型", and "对训练好的……我们没有测量".
- **Hedges (pass, except the items below).**
  - Each bet stays a 押注.
  - "deliberately speculative" is 刻意带有推测性的.
  - "likely" is 很可能, and "Keep the word likely" is kept.
  - "may" is 可能, with "他们用了可能这个词".
  - "almost has to be" is 几乎必然.
  - "arguably" is 可以说.
  - "anecdotal" is 轶事性的, and "suspect … likely true" is 怀疑……很可能是真的.
  - "concede" is 承认, "assert" is 断言, and "not completely fatal" is 不会完全是……致命打击.
  - "our reading and not a finding" is 是我们的理解，不是发现.
- **"Ours" labels (pass).** All of them are present: the summary of common practice, the bank picture, the sentence summary, the bet instances, the stream direction, edge weight, toy numbers, length-one convention, "seeing is not doing", the structural analogy, the 120° toy, "across the two lenses", the toy assumption, framing as a bridge, and "habit, not a law".
- **Glosses (pass).** Every gloss takes the allowed form "X，英文叫 Y": hidden state, vector, dimension, probe, block, token, embedding, attention, residual stream, sub-layer, write, norm, decoder-only, steering, dot product, orthogonal, margin, affine, basis, privileged basis, logit lens, ablation, activation patching, binary multiple access channel, superposition and fine-tuning.
- **Symbols and digits (mostly pass).** No arithmetic symbols remain, and every number is in words. The only digits are in names: AI4Read, GPT-2, GPT-3, Qwen3, float32, InceptionV1, Llama 3 and Gemma 3. The hyphen in "GPT-2" and "GPT-3" is read wrongly (finding M1).
- **"phi" (pass).** The English fallback reads it as /faɪ/ (fˈI). That is how φ is said in Chinese classrooms ("fai"), so a listener will follow it. "alpha" is read /ˈælfə/, which is also fine.

## Technical terms

| Translator's choice | Verdict | Note |
|---|---|---|
| 残差流 (residual stream) | Standard. Keep. | This is the usual term in Chinese interpretability writing. |
| 引导 (steering) | Acceptable. Keep. | It is standard in 激活引导 and 引导向量. 转向 and 操控 also occur, but 引导 is the most common. |
| 特权基 (privileged basis) | Standard. Keep. | 特权基底 is an equal variant. |
| 探针 (probe) | Standard. Keep. | The full form is 探测分类器. 探针 is the usual short form. |
| 归一化 (norm) | Correct. Keep. | 层归一化 is the standard term for LayerNorm. The translator rightly avoided 范数, which is the vector norm and would mean something else here. |
| 玩具例子 (toy) | Acceptable. | 玩具模型 and 玩具示例 are also used. The bare word 玩具 on its own sounds like a plaything (finding m20). |
| Other terms | Standard. | 词元, 嵌入, 子层, 注意力头, 点积, 正交, 间隔 (the SVM term), 仿射, 叠加, 消融, 激活修补, 微调, 指令微调, 钩子, 电路, 激活空间, 余弦相似度, 舍入误差, 可加性, 偏置项, 框架 and 启动 (in communication studies). |
| 普遍性 (universality) | Acceptable. | 普适性 is equally common. |
| 多址接入信道 (multiple access channel) | Acceptable. | The Chinese edition of Cover and Thomas uses 多接入信道. |
| 透镜 (lens) | Not standard for the metaphor. | See finding m19. For a way of seeing, the usual word is 视角. For "logit lens", the Chinese community usually keeps the English. |

## Findings

### Critical

None.

### Major

**M1. Every chapter that names the models: the voice reads "GPT-2" as "GPT 负二"**
- Chinese: GPT-2 small 里有七百六十八个数。 (There are 15 occurrences of GPT-2 and one of GPT-3, in bets: "连 GPT-3、Gopher……")
- English: GPT-2 small has seven hundred and sixty-eight numbers in it.
- Problem: the G2P turns "-2" into a negative number. The output is `ʤˌipˌitˈi ㄈㄨ4/ㄦ4` (GPT fù èr), and "GPT-3" becomes "GPT 负三". The listener hears "GPT minus two" about fifteen times. The text itself is right, and the name is still recognisable, so I rank this major rather than critical. A space instead of the hyphen tests clean: "GPT 2 small" is read `ʤˌipˌitˈi ㄦ4 smˈɔl`.
- Replacement: replace every "GPT-2" with "GPT 2", and "GPT-3" with "GPT 3". For example: GPT 2 small 里有七百六十八个数。 / 连 GPT 3、Gopher、Chinchilla 和 PaLM 也是。

**M2. dir: "What this does not say" becomes "This proves nothing"**
- Chinese: 这不能说明什么。
- English: What this does not say.
- Problem: in spoken Mandarin, 这不能说明什么 is the idiom "this doesn't show anything". It dismisses the whole result. The English only marks off what is not claimed, and the next sentences keep the arithmetic as exact ("only the arithmetic holds"). The scope of the denial has become wider.
- Replacement: 这里没有说明的，是下面这些。

**M3. turn, open question: the scope of the supposition is changed**
- Chinese: 假设，作为一个玩具假设，是我们的，真实的块并不是线性的：一个块作用在流上，就像一个矩阵，两行分别是二，一和一，二。
- English: Suppose, as a toy assumption, ours, with real blocks not linear, that a block acts on the stream as the matrix with rows two, one and one, two.
- Problem: the listener hears "Suppose … real blocks are not linear", followed by a statement that a block acts like a matrix. The thing being supposed is now "real blocks are not linear". In the English, the supposition is that a block acts as the matrix, and "real blocks are not linear" is the stated reason it is only a toy assumption. content.html says "(ours; real blocks are not linear)".
- Replacement: 一个开放问题。作为一个玩具假设，这是我们的，而真实的块并不是线性的：假设一个块作用在流上，就像一个矩阵，两行分别是二，一和一，二。

### Minor

**m1. hook: emphasis added**
- Chinese: 这是第三篇：隐藏状态到底是什么？
- English: This is post three: what is a hidden state?
- Problem: 到底 ("what on earth") adds emphasis.
- Replacement: 这是第三篇：隐藏状态是什么？

**m2. hook: the gloss splits the noun phrase**
- Chinese: 还有，如果每一串数字都被同一个向量推一下，探针，英文叫 probe，的分数会怎样？
- English: And what happens to a probe's score if every list is pushed by the same vector?
- Problem: "探针，英文叫 probe，的分数" leaves 的 dangling after the gloss. It is hard to follow by ear.
- Replacement: 还有，如果每一串数字都被同一个向量推一下，探针给出的分数会怎样？探针，英文叫 probe。

**m3. guess: "read" becomes "listen"**
- Chinese: 先定下你的答案，再往下听。一个你记得住的错误猜测，比一个你只是听过的正确答案更有价值。
- English: Commit to an answer before you read on. A wrong guess you remember is worth more than a right answer you only read.
- Problem: the verb is changed. This is a defensible adaptation for audio, but the English keeps "read". The author decides.
- Replacement: 先定下你的答案，再往下读。一个你记得住的错误猜测，比一个你只是读到的正确答案更有价值。

**m4. guess, Q1 option two**
- Chinese: 选项二：这个词的起始数字，加上到目前为止每一次加入的内容。
- English: Option two: the word's starting list plus every addition made so far.
- Problem: 起始数字 can be heard as "a starting number". The English means the starting list.
- Replacement: 选项二：这个词起始的那一串数字，加上到目前为止每一次加入的内容。

**m5. sum: "only" added**
- Chinese: 从这个起点开始，模型为这个词元只保留一串工作用的数字。
- English: From that start, the model keeps one working list for the token,
- Replacement: 从这个起点开始，模型为这个词元保留一串工作用的数字。

**m6. sum and bets: "short" dropped and "页面上" added**
- Chinese (sum): 页面上有一个术语框，讲这三个名字；还有一个陷阱框……
- English: There is a short term box on the three names, and a trap box …
- Chinese (bets): 页面上有一个折叠框，按坚定程度给 Olah 的各句话分类。
- English: There is a fold-out that sorts Olah's lines by firmness.
- Replacement (sum): 有一个简短的术语框，讲这三个名字；还有一个陷阱框，讲总线的图景在哪里会误导：计算机的总线，同一时刻只有一个写入者，而且有地址，而流两者都没有。
- Replacement (bets): 有一个折叠框，按坚定程度给 Olah 的各句话分类。

**m7. bets: the definition of "concept" is blurred**
- Chinese: 概念，是我们给能说出名字的特征起的名字。
- English: A concept is our word for a feature we can name.
- Problem: as written, a concept sounds like the name given to a feature. In the English, "concept" is our word for that kind of feature.
- Replacement: 概念，是我们用来称呼一个能说出名字的特征的词。

**m8. bets: the attribution covers the "ours" clause**
- Chinese: Nanda 写道，流里没有神经元，所以对流来说，方向是它各个坐标的加权组合。这是我们的说法。
- English: The stream has no neurons, Nanda writes, so for the stream a direction is a weighted mix of its coordinates. That is ours.
- Problem: "Nanda 写道" opens the sentence, so the "所以" clause is heard as Nanda's too. Then "这是我们的说法" seems to contradict it. content.html cites Nanda only for "The stream has no neurons".
- Replacement: Nanda 写道，流里没有神经元。所以，对流来说，方向是它各个坐标的加权组合，这是我们的说法。

**m9. bets and work: the counterfactual "would" is lost**
- Chinese (bets): 如果概念是方向，那么概念的强度就是一个点积。
- English: If concepts were directions, a concept's strength would be a dot product.
- Chinese (work): 如果一个启动或一个框架，是作为一个向量加到流里的，它就是沿一个方向的又一次写入。
- English: If a prime or a frame were added to the stream as a vector, it would be one more write along a direction.
- Problem: the plain conditional reads closer to a statement. 会 keeps the bet hypothetical.
- Replacement (bets): 如果概念真的是方向，那么概念的强度就会是一个点积。
- Replacement (work): 如果一个启动或一个框架，被当作一个向量加到流里，那它就会是沿一个方向的又一次写入。

**m10. rw: "注意力一零" is heard as "attention ten"**
- Chinese: 各份是：嵌入五，注意力一零，MLP 一是一，注意力二是负一。
- English: the shares are five for the embedding, zero for attention one, one for MLP one, and minus one for attention two.
- Problem: the voice reads 一零 as yī líng, which sounds like "ten" or "one-zero".
- Replacement: 各份是：嵌入是五，注意力一是零，MLP 一是一，注意力二是负一。

**m11. rw: intensifier added**
- Chinese: 这个读取者完全听不到注意力一。
- English: This reader cannot hear attention one.
- Replacement: 这个读取者听不到注意力一。

**m12. rw, dir: "兑现押注" implies the bet paid off**
- Chinese: 兑现押注二。 / 兑现押注一： / 兑现押注三。
- English: Cashing in bet two. / Cashing in bet one: / Cashing in bet three.
- Problem: 兑现 strongly suggests fulfilment (兑现承诺) or a winning bet. That cuts against "a bet stays a bet". The English idiom means "apply this to bet two".
- Replacement: 回到押注二。 / 回到押注一： / 回到押注三。

**m13. dir: the formula's grouping is lost**
- Chinese: 在 notebook 二里，u 点乘 h 加 alpha 倍的 u，减去 u 点乘 h，再减去 alpha，对我们试过的每一个 alpha，都是零。
- English: in notebook two, u dot of h plus alpha u, minus u dot h, minus alpha, was zero for every alpha we tried.
- Problem: by ear this parses as (u·h) + αu, not u·(h + αu). The English "u dot of" marks the grouping.
- Replacement: 在 notebook 二里，u 与 h 加 alpha 倍 u 之和的点积，减去 u 点乘 h，再减去 alpha，对我们试过的每一个 alpha，都是零。

**m14. turn, exercise three: (−1, 1)/√2 is ambiguous by ear**
- Chinese: 以及负一，一，除以根号二，给六个点打分。
- English: and minus one, one over root two.
- Problem: the listener can hear "−1, and 1/√2". 整个 makes clear that the whole vector is divided.
- Replacement: 以及负一，一整个除以根号二，给六个点打分。

**m15. answer, recap: translationese**
- Chinese: 这个透镜是三个押注，被轻轻地持有。
- English: The lens is three bets, held lightly.
- Replacement: 这个透镜是三个押注，我们只是姑且持有。 (Use 视角 if m19 is taken.)

**m16. lens-linalg: "unprincipled" is read as moral**
- Chinese: 零消融可以说是没有原则的
- English: zero ablation is arguably unprincipled
- Problem: 没有原则 suggests a moral failing. The sense here is that the method lacks a principled justification.
- Replacement: 零消融可以说缺乏原理上的依据

**m17. lens-linalg, lens-info: "计算方向" clashes with "direction"**
- Chinese: 与你的研究的联系，计算方向。 (two places)
- English: Connection to your research, computation.
- Problem: in this post, 方向 is the technical term for a direction, so 计算方向 can be heard as "computational direction".
- Replacement: 与你的研究的联系，属于计算这一块。

**m18. lens-info: ungrammatical**
- Chinese: Elhage 等人把流的维度称为有点像内存或带宽：这些词是在数维度。
- English: Elhage and colleagues call the stream's dimensions something like memory or bandwidth: the words count dimensions.
- Replacement: Elhage 等人说，流的维度有点像内存或带宽：这些词是在数维度。

**m19. Terms: 透镜 for the metaphorical "lens" (bets, answer, lens-linalg, lens-info, dir, turn)**
- Chinese: 我们最终想得到的这个透镜，有三个部分 … 第一个透镜是线性代数 … 另一个展示 logit 透镜，英文叫 logit lens … 并运行 logit 透镜
- English: The lens we want to end with has three parts … The first lens is linear algebra … the logit lens … runs the logit lens
- Problem: by ear, 透镜 is an optical lens. The standard word for a way of seeing is 视角. Chinese interpretability writing usually leaves "logit lens" in English.
- Replacement:
  - At first use (bets): 我们最终想得到的这个视角，英文叫 lens，有三个部分
  - Elsewhere, replace 透镜 with 视角, including in the chapter titles (视角一：线性代数, 视角二：信息论).
  - dir: 另一个展示 logit lens，是又一次读取
  - turn: 并运行 logit lens

**m20. Terms: the bare word 玩具 (bets, dir, lens-info, recall)**
- Chinese: 例子，是我们的一个玩具。 / 把六点玩具的每个坐标轴都转九十度。所有坐标都变了，但它仍然是同一个玩具。转过之后的玩具里的特征 / 把整个玩具转九十度 / 一个玩具，是我们的。……这个玩具就是上面意义上的叠加 / 在玩具点云里 / 在探针玩具里
- English: The instance, a toy of ours. / Turn every axis of the six-point toy … the same toy … the turned toy / Rotate the whole toy / A toy, ours. … This toy is superposition / in the toy cloud / In the probe toy
- Problem: the translator's own term is 玩具例子. On its own, 玩具 sounds like a plaything.
- Replacement:
  - 例子是我们的：一个玩具例子。
  - 把六个点的玩具例子的每个坐标轴都转九十度。所有坐标都变了，但它仍然是同一个玩具例子。转过之后的玩具例子里的特征，还是同一个特征吗？
  - 把整个玩具例子转九十度
  - 一个玩具例子，是我们的。……这个玩具例子就是上面意义上的叠加
  - 在玩具例子的点云里
  - 在探针的玩具例子里

**m21. Voice (sum, bets): the letter "a" or "A" is read as a schwa**
- Chinese: 向量 a，b 加向量 c，d，等于 a 加 c，b 加 d。 / 记作 a k / 部分 A 以权重二输入给部分 B。
- English: the vector a, b plus the vector c, d is a plus c, b plus d. / Call a k the write of attention / Part A feeds part B
- Problem: the English fallback reads a lone "a" or "A" as the article /ɐ/, so the variable almost vanishes. I tested 诶, which is read ㄟ ("ei"), the way Chinese speakers say the letter. The English Kokoro script may have the same issue.
- Replacement: 向量诶，b 加向量 c，d，等于诶加 c，b 加 d。 / 记作诶 k / 部分诶以权重二输入给部分 B。

**m22. dir: the gloss breaks the sentence**
- Chinese: MLP 的神经元则不同：在激活函数之后，激活函数是对每个数各自作用的一条曲线。
- English: The neurons of an MLP are different: after the activation function, a curve applied to each number on its own.
- Replacement: MLP 的神经元则不同：它们在激活函数之后。激活函数，是对每个数各自作用的一条曲线。

## Counts

- Critical: 0
- Major: 3 (M1 the voice reads GPT-2 as "GPT 负二"; M2 dir "这不能说明什么"; M3 turn, the scope of the open question's supposition)
- Minor: 22

## Response

Applied to `audio-script-zh.md` on 2026-11-04. Each replacement was checked against `audio-script.md`. Chapter ids, order, the opening line, number words and the "lens" term were kept consistent (视角 everywhere).

- **M1**: not changed here. Fixed in scripts/tts_post_zh.py (the recorder turns a letter-digit hyphen into a space). "GPT-2" and "GPT-3" stay as written.
- **M2**: changed with a shorter wording: "这里没有说明的内容。" The reviewer's "是下面这些" points ahead and is not in the English.
- **M3**: applied as suggested (toy assumption and "real blocks not linear" are now the stated reason; the supposition is the matrix).
- **m1**: applied (到底 removed).
- **m2**: applied (gloss moved after the sentence).
- **m3**: applied (听 changed to 读, 听过 to 读到).
- **m4**: applied.
- **m5**: applied (只 removed).
- **m6**: applied in sum and bets (简短 added, 页面上 removed).
- **m7**: applied.
- **m8**: applied.
- **m9**: changed. Reviewer's 真的 dropped in bets because the English has no "really". Bets: "那么概念的强度就会是一个点积". Work: "被作为一个向量加到流里，那它就会是……".
- **m10**: applied.
- **m11**: applied.
- **m12**: applied in rw and dir (回到押注二, 一, 三).
- **m13**: applied.
- **m14**: applied.
- **m15**: applied with 视角: "这个视角是三个押注，我们只是姑且持有。"
- **m16**: applied.
- **m17**: applied in lens-linalg and lens-info.
- **m18**: applied.
- **m19**: applied. First use in bets: "这个视角，英文叫 lens". All other 透镜 became 视角, including the chapter titles. dir and turn now say "logit lens" in English.
- **m20**: applied in bets, dir, lens-info and recall.
- **m21**: applied to the three listed places. Also applied to the same lone "a" in dir ("诶，b 的长度，是诶的平方"), which has the same problem.
- **m22**: applied.
