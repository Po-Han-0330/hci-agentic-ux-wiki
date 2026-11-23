# 設定預期（expectation setting）

> **一句話定義（給新手）**：在使用者開始用之前，就讓他們知道這個 AI「能做什麼」以及「大概會錯多少」，免得期待太高而失望，或太低而不敢用。（[[papers/amershi2019-guidelines]] p.3）

## 說明

AI 的行為是機率式的，同一個輸入可能得到不同結果，也會隨著學習而改變，使用者如果不知道 AI 的能力範圍，很容易被嚇到或失去信心（[[papers/amershi2019-guidelines]] p.1–2）。

Amershi 等人把這件事拆成兩條準則：G1「讓使用者清楚系統能做什麼」和 G2「讓使用者清楚系統做得多好」，也就是多常出錯（[[papers/amershi2019-guidelines]] p.3）。G2 的一個例子是音樂推薦用「我們覺得你會喜歡」這種保留語氣（[[papers/amershi2019-guidelines]] p.3）。

## 在各論文中的樣貌

- [[papers/amershi2019-guidelines]]：G1 在 20 個產品中常被做到；G2 卻是「重要但常被違反」的準則之一（p.7）。專家仍有 5 位覺得 G1 和 G2 不太好區分（p.11）。
- [[papers/bansal2024-human-agent-communication]]：A1「agent 能做什麼？」。不了解 agent 能力的使用者，只能靠非正式的試錯去摸索，結果容易形成不完整或錯誤的心智模型（p.13）。agent 能做的事更廣、更會變，讓這個老問題更難處理（p.3）。

## 相關趨勢與爭論

- [[trends/designing-for-uncertainty]]
- 相關概念：[[concepts/explainability]]（G11 是事後解釋，G1、G2 是事前說明）
