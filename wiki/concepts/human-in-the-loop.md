# 人在迴路中（human-in-the-loop）

> **一句話定義（給新手）**：agent 執行任務時，在關鍵時刻讓人參與，包括確認計畫、批准危險動作、隨時插手修正，而不是讓 agent 從頭到尾自己跑完（[[papers/bansal2024-human-agent-communication]] p.15–16）。

## 說明

agent 能力強但不完美，任務越複雜、步驟越多，越可能出錯（[[papers/bansal2024-human-agent-communication]] p.7）。所以使用者需要能監看 agent 的行為，並用回饋和修正引導它（[[papers/bansal2024-human-agent-communication]] p.2）。

關鍵的取捨在於**人要介入多少**：在「花錢、不可逆、可能違反偏好」這類高代價動作之前，agent 應該先取得許可；其他時候直接執行，可以避免使用者被過多確認淹沒（[[papers/bansal2024-human-agent-communication]] p.15、p.8）。

## 在各論文中的樣貌

- [[papers/bansal2024-human-agent-communication]]：A2（事前預告與許可）、A3（執行中監看、可叫停）、X3（細節給多少）都和「人何時介入」有關（p.8、p.15–16）。
- [[papers/feng2025-levels-of-autonomy]]：人在迴路中的「程度」可以分成五級。L1–L3 人積極參與，L4 只在障礙或重大動作時參與，L5 只剩監看和緊急停止（p.4–8）。L4 要小心使用者變成無意識批准的「橡皮圖章」（p.8）。見 [[concepts/levels-of-autonomy]]。
- [[papers/mozannar2025-magentic-ui]]：具體實作了 6 種人在迴路中的機制（共同規劃、共同執行、動作守門、答案驗證、記憶、多工），並把使用者當成多 agent 團隊的一員（p.2–3）。模擬實驗中，人的少量參與讓正確率相對提升 71%（p.19）。見 [[concepts/co-planning]]、[[concepts/action-guards]]。

## 相關趨勢與爭論

- [[trends/from-tools-to-agents]]
- [[concepts/mixed-initiative]]
- [[concepts/common-ground]]
