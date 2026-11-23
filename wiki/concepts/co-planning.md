# 共同規劃（co-planning）

> **一句話定義（給新手）**：agent 動手之前，先把它打算怎麼做列成計畫給你看，你可以直接修改，確認之後它才開始執行（[[papers/mozannar2025-magentic-ui]] p.5–6）。

## 說明

共同規劃把和使用者互動的成本「前移」：先花一點時間對齊計畫，可以降低之後修正的成本，也提高任務成功的機會（[[papers/mozannar2025-magentic-ui]] p.5）。作者列出四個可能的好處（[[papers/mozannar2025-magentic-ui]] p.5）：
1. **釐清模糊需求**：提早發現人和 agent 之間缺乏共同基礎。
2. **加入人的先驗知識**：例如使用者知道充電器只有官網在賣。
3. **借用人的規劃能力**：某些領域人比 agent 更會規劃。
4. **方便監督**：有了計畫，執行時就不用盯得那麼緊。

設計上的取捨：計畫用自然語言步驟表示，人容易看懂和修改，但彈性較低；用程式碼表示，彈性高，但人很難看懂（[[papers/mozannar2025-magentic-ui]] p.5）。

## 在各論文中的樣貌

- [[papers/mozannar2025-magentic-ui]]：使用者常在執行前修改計畫，以加入主觀偏好；有人覺得修改 agent 的計畫比自己從頭規劃更容易（p.21）。不過步驟一多，審閱計畫的成本也會跟著變高（p.25）。
- [[papers/feng2025-levels-of-autonomy]]：L2 和 L3 都有「agent 先擬計畫、使用者審閱」的步驟。差別在於 L2 可以直接編輯計畫，L3 只能用訊息請 agent 修改（p.5–6）。
- [[papers/bansal2024-human-agent-communication]]：對應 U1「agent 該達成什麼目標」和 A2「agent 接下來要做什麼」（p.9、p.15）。

## 相關趨勢與爭論

- [[trends/from-tools-to-agents]]
- [[concepts/human-in-the-loop]]
- [[concepts/common-ground]]
