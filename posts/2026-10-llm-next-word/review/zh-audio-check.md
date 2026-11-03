# Chinese audio script check: audio-script-zh.md against audio-script.md

Post: 2026-10-llm-next-word. Checked on 2026-11-04 by an independent bilingual fact-checker.
Meaning was resolved only from `src/content.html` where needed: Kaplan's "improves smoothly", Kosinski's "may have emerged as a by-product", the GPT-2 summaries being "weak", the bear story, and Bengio's "free numbers".

## Structural checks (all pass)

- Chapter ids and order are identical: hook, guess, home, lens-info, lens-linalg, lens-bayes, lens-meaning, lens-tom, ladder, answer, work, recall.
- The first chapter opens with "欢迎收听 AI4Read，来自 CSS Lab。" The allowed sentence "文中引用的原话都是我们的中文翻译。" appears once, in hook.
- No ≈, →, %, brackets or Arabic numerals appear in the spoken text. Every number is in words. Model names (GPT-3, GPT-3.5, GPT-4, ChatGPT-4) are kept as they appear in the English.
- I checked every number against the English: 1951, 79/102, about 77%, 4.7/2.6/1/0.1 bits, 175 billion (一千七百五十亿), 97.5%, 95/70/40/0, 2003 to 2020, 10^50, 30 to 100, 2013, 2017, 2019, 2020, 0.95, 1948, 1/8, 3 bits, 4.7/4.1/3.6/1, 1.7 nats, factor of ten, 40%/8,000/66%, 10 to 40%, 40 tasks, 75%, six-year-olds, fifteen models, six datasets, 0%, almost 2,000 humans, about half, 16/27, 1/2, 4/5, 0.24, 1/2, 1/4, 1/8, 1/8, 1/2/3/3, 1.75, the code 0/10/110/111, 2, 0.25, 2.625, 3.36, 4, 6.17, 1.59/1.25/0.93, 1/4, 1/4, 1/2, 0.92, 4x, 0.8/0.94/0.98, minus 0.076. All match.
- The "ours" labels are kept ("我们的玩具村庄", "在我们用 GPT-2 做的测试里", "我们的问题").
- The technical terms are standard: 词元, 条件概率, 维度灾难, 熵, KL 散度/相对熵, 交叉熵, 困惑度, 奈特, 余弦相似度, 查询/键/值, 掩码, 上下文学习, 少样本提示, 隐马尔可夫模型, 先验/后验, 心智理论, 错误信念, 形式能力/功能能力, 上界, 幂律. Exceptions are listed below.

## Findings

### Critical

**C1. home, step eight: Kaplan's finding is changed**
- Chinese: 卡普兰和同事发现，模型越大，在新文本上的损失就下降得越平滑。
- English: Kaplan and colleagues found that the loss on new text falls smoothly as models get bigger.
- Problem: the Chinese says the loss falls *more smoothly the bigger the model is*. The English says the loss *falls, smoothly, as size grows*. The claim is wrong. The post agrees with the English: performance "improves smoothly and predictably" as size grows.
- Replacement: 卡普兰和同事发现，随着模型变大，在新文本上的损失会平滑地下降。

### Major

**M1. lens-tom: Kosinski's "emerge" is dropped and the reporting verb is changed**
- Chinese: 他提示这种能力可能是语言训练的副产品。
- English: He suggests this ability may emerge as a by-product of language training.
- Problem: "emerge" (涌现) is dropped. Emergence is the point the Ullman paragraph takes up ("心智理论出现了吗？"). The post says "may have emerged as a by-product". "提示" is also a weaker and unclear rendering of "suggests".
- Replacement: 他提出，这种能力可能是作为语言训练的副产品涌现出来的。

**M2. work, social simulation: the hedge is narrowed**
- Chinese: 智能体也许能通过标准的信念故事，但在小改动下仍然会失败。
- English: agents may pass standard belief stories, and still fail under small changes.
- Problem: in the English, "may" covers both halves. In the Chinese, "也许" covers only the pass, and "仍然会失败" asserts the failure.
- Replacement: 智能体有可能通过了标准的信念故事，却在小改动下失败。

**M3. hook: the third alternative becomes cumulative, and its scope is unclear**
- Chinese: 或者，还要知道一些写下这些文字的人的心智？
- English: Or something about the minds of the people who wrote the text?
- Problem: "还要" turns the third option from an alternative into an addition. "一些写下这些文字的人" can also be heard as "some of the writers", which narrows the scope.
- Replacement: 或者，是关于写下这些文字的人的心智的一些东西？

### Minor

**m1. hook**
- Chinese: 双胞胎从来不用猜数字。
- English: The twin never guesses a number.
- Problem: "不用" means "never needs to", which is not the same as "never does".
- Replacement: 双胞胎从来不猜数字。

**m2. hook**
- Chinese: 它只是收到这些数字，用它们来知道什么时候该停。
- English: It receives the numbers, and uses them to know when to stop guessing.
- Problem: "guessing" is dropped.
- Replacement: 它只是收到这些数字，用它们来知道什么时候该停止猜测。

**m3. hook**
- Chinese: 你预测得越准，需要的信息就越短。
- English: The better you predict, the shorter the message you need.
- Problem: "message" is 消息, as used in lens-info. "信息" means "information", which is a different term in this post.
- Replacement: 你预测得越准，需要的消息就越短。

**m4. hook**
- Chinese: 今天，我们有了大规模玩这个游戏的机器。
- English: Today we have machines that play exactly this game, at a huge scale.
- Problem: "exactly" is dropped.
- Replacement: 今天，我们有了正是在玩这个游戏的机器，而且规模巨大。

**m5. guess, prediction one**
- Chinese: 香农请人们预测英文文本，上下文最长可达一百个字母。
- English: with a long context of up to one hundred letters
- Problem: "long" is dropped.
- Replacement: 香农请人们预测英文文本，用的是很长的上下文，最长可达一百个字母。

**m6. home, step two**
- Chinese: 你最多需要十的五十次方个自由参数。
- English: you would need up to ten to the power of fifty free numbers.
- Problem: the English and the post both say "free numbers" in plain words. "自由参数" brings in jargon the English avoids.
- Replacement: 你最多需要十的五十次方个可以自由取值的数。

**m7. home, step six**
- Chinese: 这些摘要很差。
- English: The summaries were weak.
- Problem: "很差" is stronger than "weak". The post says they "just barely" beat random sentences.
- Replacement: 这些摘要还比较弱。

**m8. home, step eight**
- Chinese: 平滑的损失，可能掩盖了模型能力上的突然变化。
- English: a smooth loss may hide sudden changes in what the model can do.
- Problem: "了" turns a general warning into a claim about something that already happened.
- Replacement: 平滑的损失，可能会掩盖模型能力上的突然变化。

**m9. lens-info, opening**
- Chinese: 语言模型的训练损失，就是香农所说的平均意外程度。
- English: The training loss of a language model is Shannon's average surprise.
- Problem: "香农所说的" says Shannon used the words "average surprise". The English does not say this.
- Replacement: 语言模型的训练损失，就是香农的平均意外程度。

**m10. lens-info, key fact**
- Chinese: 假设真实分布是 p，但你的模型是 q。
- English: Suppose the truth is p, but your model is q.
- Problem: "分布" is added. It is also inconsistent with "在真相是 p 的时候" two sentences later.
- Replacement: 假设真相是 p，但你的模型是 q。

**m11. lens-linalg**
- Chinese: 米科洛夫、伊和茨威格
- English: Mikolov, Yih and Zweig
- Problem: Wen-tau Yih's surname is 易 in standard Chinese usage.
- Replacement: 米科洛夫、易和茨威格

**m12. lens-linalg, recap**
- Chinese: 几何是不是意义，这是视角四要回答的问题。
- English: Whether geometry is meaning is a question for lens four.
- Problem: "要回答" promises that lens four answers the question. Lens four says the answer depends on your theory of meaning.
- Replacement: 几何是不是意义，这是留给视角四的问题。

**m13. lens-meaning**
- Chinese: 然后 A 写道，有一头熊正在攻击她，问怎样用几根木棍自卫。
- English: Then A writes that a bear is attacking, and asks how to defend herself with some sticks.
- Problem: the object "她" is added. Both the English and the post leave it out.
- Replacement: 然后 A 写道，有一头熊正在发动攻击，问怎样用几根木棍自卫。

**m14. lens-tom, Ullman**
- Chinese: 一次明确的失败，可以抵过许多平平的成功。
- English: one clear failure can outweigh many average successes.
- Problem: "抵过" means "is worth as much as". "outweigh" means "weighs more than", so the Chinese is weaker.
- Replacement: 一次明确的失败，分量可以超过许多平平的成功。

**m15. work, surrogate labeling**
- Chinese: 对于大语言模型代理标注
- English: For LLM surrogate labeling
- Problem: "surrogate" is usually 替代. "代理" clashes with "agent" (智能体/代理) later in the same chapter.
- Replacement: 对于大语言模型替代标注

**m16. recall, answer three**
- Chinese: 四。就是二的二次方。
- English: Four. Two to the power of two bits.
- Problem: "bits" is dropped, so the link to the two-bit cross-entropy is lost.
- Replacement: 四。也就是二的二次方，指数是两比特。

**m17. recall, question six**
- Chinese: 批评者回应的是科辛斯基论文的哪个版本，为什么这很重要？
- English: Why does it matter which version of Kosinski's paper a critic answers?
- Problem: the Chinese turns one "why" question into two questions ("which version" and "why"). It also turns the generic "a critic" into "the critics".
- Replacement: 为什么要弄清一条批评回应的是科辛斯基论文的哪个版本？

## Counts

- Critical: 1
- Major: 3
- Minor: 17
- Total: 21

## Response

Applied on 2026-11-04. Each replacement was checked against audio-script.md. Edits are in audio-script-zh.md only.

- C1: applied as given. Now "随着模型变大，在新文本上的损失会平滑地下降。"
- M1: applied with a change. The reviewer's "是作为……涌现出来的" puts "emerge" in the past; the English says "may emerge". Now "他提出，这种能力可能作为语言训练的副产品涌现出来。"
- M2: applied with a change. The reviewer's version dropped "still" and added "了". Now "智能体有可能通过标准的信念故事，却仍然在小改动下失败。"
- M3: applied as given.
- m1: applied as given.
- m2: applied as given.
- m3: applied as given.
- m4: applied as given.
- m5: applied as given.
- m6: applied as given.
- m7: applied with a change. "还比较弱" adds a hedge that the English lacks. Now "这些摘要偏弱。"
- m8: applied as given.
- m9: applied as given.
- m10: applied as given.
- m11: applied as given (易).
- m12: applied as given.
- m13: applied as given.
- m14: applied as given.
- m15: applied as given.
- m16: applied with a change. "指数是两比特" is unclear when spoken. Now "四。就是二的两比特次方。", which follows the English "two to the power of two bits".
- m17: applied as given.

Declined: none.
