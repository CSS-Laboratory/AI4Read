# Chinese audio script check: audio-script-zh.md against audio-script.md

Checked on 2026-11-04 by an independent bilingual reviewer. Sources: `audio-script.md` (English), `audio-script-zh.md` (Chinese). `src/content.html` was used only to settle meaning.

## Structural checks (all pass)

- Chapter ids and order are identical: hook, guess, home, llm, lens-control, lens-decision, lens-cascade, lens-social, lens-answer, play, turn, work, answer, recall.
- The first chapter opens with "欢迎收听 AI4Read，来自 CSS Lab。"
- The allowed sentence "文中引用的原话都是我们的中文翻译。" appears once, in the first chapter.
- Term glosses (执行/决定/检查/宣告/负责, tranche) take the allowed form "X，英文叫 Y".
- Every number was checked against the English and is equal: 四十一亿美元, 两点四十五分, 百分之一, 五秒钟, 二十分钟, 二零二六, 二零二四, 十年, 第十三节, 百分之七十, 三到五年, 五万美元, 二比特/一比特, 十三点三, 四比特, 九点三, 一万种到一百种, 十的二十次方, 一百天里有一天, 零点三, 二点七, 零点九, 一点一, 三点二六, 一除以 rho, 百分之十, 百分之零点三七, 二十七倍, 资本十, 借五, 百分之二十/八十, 四/八/十二, 一半, epsilon 平方, 万分之二, 万分之一, 两千七百五十六倍, 两千七百倍, 零点二, 零点九, 三分之二, 一点五, 一百/一百一十/九十, 零点八, 二到二十, 二十行, 零到九十九, 五个提示词. The arithmetic itself also checks out (for example 10/(1+9×0.3)=2.70, 100/(1+99×0.3)=3.26, P(≥3 of 4)=0.37%).
- Population and scope are kept for every source. "参与 IMF 外联活动的所有人" / "参与者" correctly keeps outreach participants, not firms. The FSB, the FCIC inquiry, Danielsson and Uthemann, Arora and colleagues, and Lupia and McCubbins are scoped correctly.
- Purposes stay purposes: "目的正是保护自己", "这条规则的目的，是防止……", "所以有一个研究小组给模型……".
- Every "ours" label is kept, in every chapter.

## Findings

### 1. Critical: hook, preview sentence
- Chinese: 执行的大部分可以自动化，规则不行。
- English: Much of the running is automated; the rules are not.
- Problem: the English describes a present fact ("is automated", "are not"). The Chinese says the running *can* be automated and the rules *cannot* be. That contradicts the answer chapter ("not shown, and not ruled out"). It also turns "much" into "most" (大部分).
- Replacement: 很多执行工作已经自动化了，规则没有。

### 2. Major: llm, Gensler and Bailey descriptor (the translator's reported addition)
- Chinese: 金融监管学者詹斯勒和贝利写道，
- English: Gensler and Bailey write that
- Judgement: reject it. The English gives no descriptor, and the brief allows only two kinds of addition. The label is also inaccurate: the source is an MIT working paper (Gensler & Bailey 2020, MIT AI Global Policy Forum), and nothing in the post calls Bailey a regulation scholar. The name should also take the mainland form (see finding 7).
- Replacement: 根斯勒和贝利写道，

### 3. Major: llm, invention
- Chinese: 我们没有找到任何一种由 AI 发明、并且已经上市交易的金融工具，不过我们的搜索有限。
- English: We found no traded financial instrument invented by an AI, though our search was limited.
- Problem: 上市交易 means "exchange-listed", which narrows "traded" (traded includes over-the-counter). The scope of the claim changes.
- Replacement: 我们没有找到任何一种由 AI 发明、并且实际交易过的金融工具，不过我们的搜索有限。

### 4. Major: lens-answer, "shamed"
- Chinese: AI 不能被关进监狱，也不会感到羞耻，
- English: An AI cannot be jailed or shamed,
- Problem: "shamed" is a sanction others apply, listed with jailed, fined, sued and fired. 不会感到羞耻 ("does not feel shame") turns it into a claim about the AI's inner states that the English does not make.
- Replacement: AI 不能被关进监狱，也不能被当众羞辱，

### 5. Major: answer, "much" strengthened to "most" (two places)
- Chinese: 部分已经做到了，不过大部分工作是由基于规则的软件完成的，而不是 AI。算法执行了大部分交易，预设规则检查它们；
- English: in parts, already, though much of the work is done by rule-based software rather than AI. Algorithms run much of the trading and pre-set rules check it;
- Problem: 大部分 ("most") claims more than "much". This sits in the verdict chapter.
- Replacement: 部分已经做到了，不过很多工作是由基于规则的软件完成的，而不是 AI。算法执行了很多交易，预设规则检查它们；

### 6. Minor: hook, lens-control, lens-cascade, lens-social (given names dropped; Harari not in the mainland form)
- Chinese: 历史学家哈拉瑞 / 控制论学者阿什比 / 英格兰银行的霍尔丹 / 社会学家格兰诺维特 / 哲学家塞尔
- English: The historian Yuval Noah Harari / the cyberneticist W. Ross Ashby / Andrew Haldane of the Bank of England / The sociologist Mark Granovetter / The philosopher John Searle
- Problem: the given names are dropped at first mention. 哈拉瑞 is the Taiwan form. The zh-Hans standard is 尤瓦尔·赫拉利, as in the mainland editions of 《人类简史》.
- Replacement: at first mention, 历史学家尤瓦尔·赫拉利 / 控制论学者 W·罗斯·阿什比 / 英格兰银行的安德鲁·霍尔丹 / 社会学家马克·格兰诺维特 / 哲学家约翰·塞尔. Then change 哈拉瑞 to 赫拉利 at every later occurrence (hook recap, lens-social, lens-answer, answer).

### 7. Minor: llm, lens-decision, lens-answer (Gensler not in the mainland form)
- Chinese: 詹斯勒 (three occurrences)
- English: Gensler
- Problem: 詹斯勒 is the Taiwan form. Mainland usage, including Xinhua's coverage of the SEC, is 根斯勒.
- Replacement: change 詹斯勒 to 根斯勒 at all three occurrences (the llm occurrence is already covered by finding 2).

### 8. Minor: hook, Harari's BIS line
- Chinese: 也许十年之内就会出现。
- English: maybe in ten years.
- Problem: "maybe in 10 years" (his words: "imagine a situation maybe in 10 years") becomes "within ten years it will appear". The timing shifts, and 就会出现 makes his "imagine" sound more like a forecast.
- Replacement: 也许是十年以后。

### 9. Minor: hook, recap
- Chinese: 二零一零年，软件跑完了一场崩盘，一条预先设定的规则让它暂停。
- English: In twenty ten, software ran a crash and a pre-set rule paused it.
- Problem: 跑完了 means "ran to completion", which is not what happened.
- Replacement: 二零一零年，一场崩盘由软件执行，又被一条预先设定的规则暂停。

### 10. Minor: guess, question three
- Chinese: 没有任何人使用它，也没有人想到它。
- English: No human ever uses it or thinks about it.
- Problem: "ever" is dropped.
- Replacement: 从来没有人使用它，也从来没有人想到它。

### 11. Minor: home, "enforcing a rule"
- Chinese: 而执行规则，则属于宣告和负责的一部分。
- English: and enforcing a rule is part of declaring and answering.
- Problem: 执行 is the script's term for "run". A listener will hear "running the rules", not "enforcing" them.
- Replacement: 而强制实施规则，则属于宣告和负责的一部分。

### 12. Minor: home and llm, "evidence mixed" (two places)
- Chinese: IMF 认为证据好坏参半
- English: the IMF finds the evidence mixed
- Problem: 好坏参半 means "half good, half bad", a judgement of quality. In research Chinese, "mixed evidence" is 证据不一.
- Replacement: IMF 认为证据不一 (in both places)

### 13. Minor: home, "sophisticated AI"
- Chinese: 成熟的 AI 还没有被广泛用来构建自主交易的智能体
- English: sophisticated AI has not yet been widely used to build autonomous trading agents
- Problem: 成熟 means "mature", not "sophisticated".
- Replacement: 先进的 AI 还没有被广泛用来构建自主交易的智能体

### 14. Minor: home, added "still"
- Chinese: 最后的决定可能仍由人类交易员来做。
- English: where a human trader may make the final decision.
- Problem: 仍 ("still") is an addition.
- Replacement: 最后的决定可能由人类交易员来做。

### 15. Minor: lens-control, "control theory"
- Chinese: 控制论问的是，任何监管者需要什么。
- English: Control theory asks what any regulator needs.
- Problem: 控制论 is the standard term for cybernetics. Control theory is 控制理论.
- Replacement: 控制理论问的是，任何监管者需要什么。

### 16. Minor: lens-control, "somewhat trivial solution"
- Chinese: 他称之为一种有点平庸的办法。
- English: which he calls a somewhat trivial solution.
- Problem: 平庸 means "mediocre". Ashby's "trivial" is the mathematical sense, standard Chinese 平凡解.
- Replacement: 他称之为一种有点平凡的解法。

### 17. Minor: lens-control, added "type"
- Chinese: 取决于冲击的类型，也取决于当局准备得如何。
- English: depending on the shocks and on how prepared the authorities are.
- Problem: 类型 ("type") is an addition.
- Replacement: 取决于冲击，也取决于当局准备得如何。

### 18. Minor: lens-decision, monoculture
- Chinese: 詹斯勒和贝利称之为单一栽培，
- English: Gensler and Bailey call it a monoculture,
- Problem: 单一栽培 is the agronomy term. In finance and AI writing the concept is rendered 单一化 (as in 算法单一化). A gloss of the allowed form fits here.
- Replacement: 根斯勒和贝利称之为单一化，英文叫 monoculture，

### 19. Minor: lens-decision, "mature stage of adoption"
- Chinese: 他们把它当作关于采用后期阶段的一个假说，
- English: They frame it as a hypothesis about a mature stage of adoption,
- Problem: 后期 means "late", not "mature".
- Replacement: 他们把它当作关于采用进入成熟阶段的一个假说，

### 20. Minor: lens-decision, recap "senior tranche"
- Chinese: 一个共同的原因，让最高级的那一层风险高了二十七倍。
- English: One shared cause made the senior tranche twenty-seven times riskier.
- Problem: the standard term for a senior tranche is 优先级; 最高级 means "highest grade".
- Replacement: 一个共同的原因，让优先级的那一层风险高了二十七倍。

### 21. Minor: lens-cascade, prediction four
- Chinese: 所以，预测四：不安全。
- English: So, prediction four: no.
- Problem: the question was "Is the system safer?", so "no" means "not safer". 不安全 says "unsafe", which is stronger.
- Replacement: 所以，预测四：不会更安全。

### 22. Minor: lens-cascade, "much greater prominence"
- Chinese: 他们建议，把系统的多样性放到更突出的位置。
- English: They propose that systemic diversity be given much greater prominence.
- Problem: "much" is dropped, which weakens the proposal.
- Replacement: 他们建议，让系统多样性得到大得多的重视。

### 23. Minor: lens-cascade, ladder five mechanism (hard to follow by ear)
- Chinese: 大致上，追涨的人会重复上一次变动的一点五倍的 m 倍，当这个数等于一时，一次波动保持原来的大小。
- English: roughly, the chasers repeat one and a half times m of the last move, so a swing keeps its size when that equals one.
- Problem: "一点五倍的 m 倍" is hard to parse when heard. The meaning is right.
- Replacement: 大致上，追涨的人会把上一次变动重复一遍，幅度乘以一点五再乘以 m；所以这个乘数等于一时，一次波动保持原来的大小。

### 24. Minor: lens-social, Searle's "status"
- Chinese: 身份 (six occurrences: 集体接受了一种身份 / Y 是一种身份 / 这种身份 / 某种身份 / 这种身份 / 相信这种身份)
- English: status
- Problem: Chinese Searle scholarship and translations usually render "status (function)" as 地位 (地位功能). 身份 reads as personal identity.
- Replacement: change 身份 to 地位 at all six occurrences in lens-social, for example 有些功能之所以起作用，只是因为人们集体接受了一种地位。 / Y 是一种地位，货币。

### 25. Minor: answer, Ashby's lever
- Chinese: 找到一个约束，监管就可能成为可能；
- English: find a constraint, and regulation may become possible;
- Problem: the doubled 可能 sounds awkward when spoken.
- Replacement: 找到一个约束，监管就有可能实现；

### 26. Minor: answer, "the bets made with it"
- Chinese: 是合同的形式，还是用合同下的赌注。
- English: the form of the contract, or the bets made with it.
- Problem: 用合同下的赌注 can be heard as "the bets under the contract".
- Replacement: 是合同的形式，还是人们用合同押下的赌注。

### 27. Minor: llm and lens-cascade, digits the voice may misread
- Chinese: GPT-4 (llm); Y1 (lens-cascade, three occurrences)
- English: GPT-4; Y1
- Problem: these are the only digits left in the body (AI4Read is required in the opening line). The Chinese voice may read 减四, 负四 or "one".
- Replacement: GPT 四; Y 一

## Counts

- Critical: 1
- Major: 4
- Minor: 22
- Total: 27

## Response

All 27 findings applied to `audio-script-zh.md` on 2026-11-04. Chapter ids and order, the opening line, number words and the "ours" labels are unchanged. Where the reviewer's replacement was adjusted after checking it against the English, the change is marked.

- 1 (critical): preview sentence now reads 很多执行工作是自动化的，规则不是自动化的。 Adjusted: the reviewer's 已经 and 规则没有 were replaced, because 已经 adds "already" and 规则没有 is ambiguous.
- 2: removed the descriptor; now 根斯勒和贝利写道.
- 3: 已经上市交易 changed to 实际交易过.
- 4: 不会感到羞耻 changed to 不能被羞辱. Adjusted: the reviewer's 当众 was dropped, because "publicly" is not in the English.
- 5: 大部分 changed to 很多 in both places in the answer chapter (work done by rule-based software; algorithms run trading).
- 6: given names added at first mention (尤瓦尔·赫拉利, 安德鲁·霍尔丹, 马克·格兰诺维特, 约翰·塞尔). Adjusted: Ashby is 控制论学者 W 罗斯·阿什比, with the W spaced and no middle dot after it, so the voice reads the letter. 哈拉瑞 changed to 赫拉利 at all four later occurrences.
- 7: 詹斯勒 changed to 根斯勒 in all three places (llm via finding 2, lens-decision, lens-answer).
- 8: 也许是十年以后.
- 9: 一场崩盘由软件执行，又被一条预先设定的规则暂停.
- 10: 从来没有人使用它，也从来没有人想到它.
- 11: 强制实施规则.
- 12: 证据不一 in both places (home, llm).
- 13: 先进的 AI.
- 14: removed 仍.
- 15: 控制理论.
- 16: 有点平凡的解法.
- 17: removed 的类型.
- 18: 单一化，英文叫 monoculture.
- 19: Adjusted: 关于采用的成熟阶段的一个假说. The reviewer's 采用进入成熟阶段 adds "entering", which is not in the English.
- 20: 优先级.
- 21: 不会更安全.
- 22: Adjusted: 把系统多样性放到突出得多的位置. This keeps "prominence" and "much" and sounds natural. The reviewer's 大得多的重视 turns prominence into attention.
- 23: accepted as given (乘以一点五再乘以 m；所以这个乘数等于一时).
- 24: 身份 changed to 地位 at all six occurrences in lens-social.
- 25: 有可能实现.
- 26: Adjusted: 用合同押下的赌注. The reviewer's 人们 adds an agent that is not in the English; 押下 already removes the "under the contract" reading.
- 27: GPT 四; Y 一 (three occurrences).

None declined. Findings 1, 4, 6, 19, 22 and 26 were adjusted as noted.
