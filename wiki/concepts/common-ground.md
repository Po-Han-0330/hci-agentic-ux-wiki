# 共同基礎（common ground）

> **一句話定義（給新手）**：人和 agent 對「目標是什麼、現在進行到哪、接下來要做什麼」有一致的理解。就像兩個同事合作前要先對齊共識（[[papers/bansal2024-human-agent-communication]] p.2–3）。

## 說明

這個概念來自 Clark & Brennan 的溝通理論。Bansal 等人用它來指操作層面的對齊，例如雙方對目前狀態和可能結果的共同推論，並**不是**主張 agent 和人用同樣的方式理解世界（[[papers/bansal2024-human-agent-communication]] p.3）。

建立共同基礎需要雙向溝通：使用者要能說清楚目標、偏好和限制；agent 要讓使用者知道它的能力、計畫和行動。而且不只要傳遞資訊，還要能**驗證**對方真的理解了（[[papers/bansal2024-human-agent-communication]] p.2、p.7）。共同基礎從使用者第一次接觸 agent 就開始建立，並且在使用期間和使用之後持續維持（[[papers/bansal2024-human-agent-communication]] p.2）。

## 在各論文中的樣貌

- [[papers/bansal2024-human-agent-communication]]：以共同基礎為核心，整理出 12 個溝通挑戰（A1–A5、U1–U3、X1–X4）（p.1）。agent 行動又快又複雜、行為又隨機，讓共同基礎更難建立（p.20）。
- 意圖說不清楚的問題（見 [[concepts/gulf-of-envisioning]]），可以看成共同基礎在「使用者 → AI」方向上的斷裂（綜合：[[papers/subramonyam2024-gulf-of-envisioning]]、[[papers/bansal2024-human-agent-communication]]）。
- [[papers/mozannar2025-magentic-ui]]：用「人和 agent 共用的計畫表示」來建立共同基礎。計畫是一串自然語言步驟，雙方都看得懂（p.5、p.25）。不過 agent 實際做的事有時會超出步驟描述的範圍（p.25）。

## 相關趨勢與爭論

- [[trends/from-tools-to-agents]]
- [[concepts/human-in-the-loop]]
