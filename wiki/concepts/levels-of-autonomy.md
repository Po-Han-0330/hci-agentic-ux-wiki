# 自主性等級（levels of autonomy）

> **一句話定義（給新手）**：用「使用者在 agent 工作時扮演什麼角色」來描述 agent 有多自主：從使用者全程主導（L1），到 agent 完全自己做、使用者只能旁觀（L5）（[[papers/feng2025-levels-of-autonomy]] p.1、p.4）。

## 說明

Feng 等人定義自主性為「agent 被設計成在多大程度上不需要使用者參與」，並強調它是一個**設計決定**，和 agent 的能力是兩回事（[[papers/feng2025-levels-of-autonomy]] p.2–3）。

| 等級 | 使用者角色 | agent 做什麼 | 使用者的控制方式 | 出處 |
|---|---|---|---|---|
| L1 | 操作者 | 被叫才幫忙，或主動建議但等批准 | 完全主導流程 | [[papers/feng2025-levels-of-autonomy]] p.4–5 |
| L2 | 協作者 | 和人一起規劃、分工、執行 | 直接修改計畫、隨時接手 | [[papers/feng2025-levels-of-autonomy]] p.5–6 |
| L3 | 顧問 | 主導規劃執行，需要時諮詢人 | 給回饋、暫停、要求重做 | [[papers/feng2025-levels-of-autonomy]] p.6–7 |
| L4 | 批准者 | 只在遇到障礙或重大動作時找人 | 批准或拒絕、事先指定哪些要批准 | [[papers/feng2025-levels-of-autonomy]] p.7 |
| L5 | 觀察者 | 完全自主 | 只能看紀錄，加上緊急停止開關 | [[papers/feng2025-levels-of-autonomy]] p.8 |

**越自主不代表越好**：每往上一級，效率可能更高，但責任歸屬、安全性和使用者參與感都要付出代價（[[papers/feng2025-levels-of-autonomy]] p.9）。

## 在各論文中的樣貌

- [[papers/feng2025-levels-of-autonomy]]：提出五級框架、自主性證書和協助式評估（p.4–12）。
- [[papers/bansal2024-human-agent-communication]] 沒有分級，但討論了同樣的取捨：agent 是否要確認每一個請求，還是在熟悉的情況下更自主（X3，p.8）。
- [[papers/mozannar2025-magentic-ui]]：沒有使用分級，但提供開關，可以分別關掉共同規劃、共同執行和動作守門，讓系統變成完全自主模式來比較（p.14）。預設模式最接近 L2（綜合：[[papers/feng2025-levels-of-autonomy]] p.5–6、[[papers/mozannar2025-magentic-ui]] p.5–7）。

## 相關趨勢與爭論

- [[trends/autonomy-as-design-choice]]
- [[debates/how-much-human-oversight]]
- [[concepts/human-in-the-loop]]
