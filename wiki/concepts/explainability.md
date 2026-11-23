# 可解釋性（explainability）

> **一句話定義（給新手）**：讓使用者能看懂 AI「為什麼」做出這個建議或動作，例如導航 app 告訴你「選這條是因為最快」。（[[papers/amershi2019-guidelines]] p.3）

## 說明

AI 會出錯，所以使用者需要能檢查 AI 的推論，才能避免不必要或危險的動作；這也是可解釋性研究大量出現的原因（[[papers/amershi2019-guidelines]] p.2）。在 Amershi 的 18 條準則裡，對應的是 G11「讓使用者清楚系統為什麼這樣做」（[[papers/amershi2019-guidelines]] p.3）。

## 在各論文中的樣貌

- [[papers/amershi2019-guidelines]]：G11 是違反次數最多的準則之一，而且很少被評為「不適用」。這代表使用者想像得到解釋會有用，但產品裡常常沒有，或有解釋卻說不清楚（p.9）。作者也提醒，有時候基於商業理由不適合解釋，例如搜尋引擎公開排序規則會被人鑽漏洞（p.9）。
- 解釋的重要性也取決於情境：高風險領域（醫療、金融）比低成本的音樂推薦更需要解釋（[[papers/amershi2019-guidelines]] p.4，引用 Bunt et al.）。
- [[papers/subramonyam2024-gulf-of-envisioning]]：在 LLM 介面裡，讓輸出可解釋（例如程式碼附註解、提供不同詳細程度的摘要）可以幫使用者判斷輸出好不好，也就是縮小意圖性缺口；但要小心使用者不經驗證就過度相信解釋（p.12）。
- [[papers/bansal2024-human-agent-communication]]：agent 的解釋還要涵蓋「目標達成了嗎」（A5）和「有沒有副作用」（A4），例如事後摘要 agent 對環境做了哪些改變（p.18–19）。解釋的詳細程度也要拿捏，太細反而造成負擔（X3，p.8）。
- [[papers/mozannar2025-magentic-ui]]：光看最終答案常常不夠，使用者需要回頭看 agent 怎麼做的，才能判斷對不對（p.25–26）。但長紀錄又讓人被淹沒，所以使用者想要影片摘要這類更精簡的呈現（p.25）。

## 相關趨勢與爭論

- [[trends/designing-for-uncertainty]]
- [[concepts/expectation-setting]]
