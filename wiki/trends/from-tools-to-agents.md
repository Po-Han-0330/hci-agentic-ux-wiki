# 趨勢：從「工具」走向「會自己行動的 agent」

> **一句話**：AI 不再只是回答問題或給建議，而是會上網、寫程式、寄信、下單，直接替人行動。介面設計的重點因此從「呈現結果」轉移到「讓人能理解、監看和控制 agent 的行動」（[[papers/bansal2024-human-agent-communication]] p.2）。

## 是什麼

agent 是能自主感知環境並採取行動的系統。今天的 agent 可以安排會議、訂機票、點餐、購物，行動會影響數位和實體世界（[[papers/bansal2024-human-agent-communication]] p.2）。

## 為什麼會出現

兩項技術進展（[[papers/bansal2024-human-agent-communication]] p.3–4）：
1. **生成式基礎模型**：能理解自然語言、處理大量沒有事先設計過的任務。
2. **工具使用**：透過 API、瀏覽器、程式執行環境，agent 能「感知」世界也能「改變」世界。

## 哪些論文支持

- [[papers/bansal2024-human-agent-communication]]：整理出 12 個新的或變得更複雜的人與 agent 溝通挑戰（p.1）。
- [[papers/mozannar2025-magentic-ui]]：實際做出一個能瀏覽網頁、寫程式、處理檔案的 agent 介面，並測試人怎麼參與（p.1–3）；但在 GAIA 上的自主正確率是 42.52%，人類是 92%，仍然落後（p.16）。
- [[papers/feng2025-levels-of-autonomy]]：OpenAI Operator、Devin、Deep Research 等產品推出，讓 agent 加速進入社會（p.2）。

## 反例或爭議

- 能力越強，失敗的代價越高：agent 可能亂花錢、洩漏個資、刪掉重要檔案（[[papers/bansal2024-human-agent-communication]] p.2），而且規劃能力有限、會產生幻覺，行為無法完全預期（[[papers/bansal2024-human-agent-communication]] p.4）。
- 讓人確認每一步太累，完全不確認又太危險。這個「介入多少」的取捨還沒有答案（[[papers/bansal2024-human-agent-communication]] p.8）。

## 三個階段的主線（綜合）

AI 的能力從「給建議」（[[papers/amershi2019-guidelines]] p.1–3）、「依自然語言生成」（[[papers/subramonyam2024-gulf-of-envisioning]] p.1–3）擴大到「替人行動」（[[papers/bansal2024-human-agent-communication]] p.2）。每往前一步，研究者都提出新的機制，讓人能理解和控制 AI，因為失敗的代價也跟著升高（綜合：[[papers/amershi2019-guidelines]] p.3、[[papers/subramonyam2024-gulf-of-envisioning]] p.11–12、[[papers/bansal2024-human-agent-communication]] p.2、[[papers/mozannar2025-magentic-ui]] p.2）。但這不代表能力越強就一定要越自主：自主性是可以另外決定的設計選項，越自主不代表越好（[[papers/feng2025-levels-of-autonomy]] p.2、p.9）。

## 對設計者的意義

在 agent 行動的「之前、執行中、之後」都要設計溝通：事前說明計畫、執行中顯示進度並可以叫停、事後回報副作用和結果（[[papers/bansal2024-human-agent-communication]] p.15–19）。這延續了 [[trends/designing-for-uncertainty]]，但風險從「建議錯了」升級成「做錯了事」（綜合：[[papers/amershi2019-guidelines]]、[[papers/bansal2024-human-agent-communication]]）。具體做法可以參考 Magentic-UI 的共同規劃和動作守門（[[papers/mozannar2025-magentic-ui]] p.5–7、p.14）。相關概念：[[concepts/common-ground]]、[[concepts/human-in-the-loop]]、[[concepts/co-planning]]、[[concepts/action-guards]]。
