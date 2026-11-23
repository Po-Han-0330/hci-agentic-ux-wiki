# 趨勢：把「自主程度」當成可以調整的設計選項

> **一句話**：與其讓 agent 能做多少就自主多少，設計者開始刻意決定「這個任務裡，人該扮演什麼角色」，並依此設計介面和控制方式（[[papers/feng2025-levels-of-autonomy]] p.2）。

## 是什麼

把自主性從「技術能力的副產品」變成一個獨立的設計維度：同一個 agent、同樣的工具，可以被設計成 L1（人主導）到 L5（agent 完全自主）任何一級（[[papers/feng2025-levels-of-autonomy]] p.4）。

## 為什麼會出現

- 業界對自主 agent 很熱衷（例如 OpenAI Operator、Devin、Deep Research），但研究和評測只看「能不能自主完成任務」，忽略了風險和使用者體驗（[[papers/feng2025-levels-of-autonomy]] p.2）。
- agent 行動的代價變高，使用者「介入多少」成為必須回答的問題：確認太多很累，太少又危險（[[papers/bansal2024-human-agent-communication]] p.8、p.15）。

## 哪些論文支持

- [[papers/feng2025-levels-of-autonomy]]：五級框架，以使用者角色為中心（p.1、p.4–8）。
- [[papers/bansal2024-human-agent-communication]]：在高代價動作前請求許可、在熟悉情況下減少確認（p.8、p.15）。
- [[papers/mozannar2025-magentic-ui]]：把共同規劃、共同執行、動作守門都做成可以開關的設定，同一個系統可以切換成不同的自主程度（p.14）；使用者也可以設定成每個動作都要先請求許可（p.26）。
- 這個想法可以追溯到 mixed-initiative 的傳統：依照信心和成本，決定 AI 該自動執行還是等人（[[papers/amershi2019-guidelines]] p.2）。

## 反例或爭議

- 使用者介入一定比較好嗎？Feng 等人指出，在資訊極度複雜時，人的介入反而可能帶來錯誤（[[papers/feng2025-levels-of-autonomy]] p.8）。見 [[debates/how-much-human-oversight]]。
- 批准者模式（L4）可能淪為橡皮圖章（[[papers/feng2025-levels-of-autonomy]] p.8）。

## 對設計者的意義

先問「這個任務錯了的代價多高？使用者需要學會這項技能嗎？」，再選等級，最後依照等級設計控制機制：L2 要能接手、L3 要能在對的時機諮詢、L4 要讓使用者事先設定批准規則、L5 要有監看工具和停止開關（[[papers/feng2025-levels-of-autonomy]] p.5–8）。相關概念：[[concepts/levels-of-autonomy]]、[[concepts/human-in-the-loop]]。
