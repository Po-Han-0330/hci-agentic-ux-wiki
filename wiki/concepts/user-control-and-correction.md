# 使用者控制與修正（user control & correction）

> **一句話定義（給新手）**：AI 一定會出錯，所以介面要讓人能輕鬆「叫它來、叫它走、改它的錯、調整它的整體行為」。（[[papers/amershi2019-guidelines]] p.3）

## 說明

Amershi 等人在「出錯時」和「長期使用」這兩組準則中，把控制拆成好幾個層次（[[papers/amershi2019-guidelines]] p.3）：
- G7 方便叫出 AI、G8 方便忽略或關掉 AI、G9 方便修正 AI 的錯誤
- G15 讓使用者在互動中給細部回饋（例如把某封信標成重要）
- G17 提供全域控制（例如整體關掉位置紀錄）

研究中參與者常把「單次修正」（G9）和「全域設定」（G17）搞混，作者因此特別在 G17 加上「global」這個字（[[papers/amershi2019-guidelines]] p.5、p.10）。

## 在各論文中的樣貌

- [[papers/amershi2019-guidelines]]：控制是針對「AI 輔助功能」設計的，例如修改語音助理建立的提醒（p.3）。G17 是「重要但常被違反」的準則之一（p.7）。
- [[papers/subramonyam2024-gulf-of-envisioning]]：在 LLM 時代，控制的形式變成「讓使用者直接修改 AI 的輸出」，例如修改 AI 產生的 SQL 查詢（設計模式 6，p.12）。見 [[concepts/direct-manipulation]]。
- [[papers/bansal2024-human-agent-communication]]：U3「下次該怎麼改」：讓使用者的回饋能修正 agent 之後的行為（p.12）；X4：使用者要能檢視、編輯、清除 agent 使用的背景資訊，類似瀏覽器的無痕模式（p.9）。
- [[papers/feng2025-levels-of-autonomy]]：控制方式隨著自主性等級改變。L2 可以直接編輯、隨時接手；L3 只能間接提出修改；L5 只剩緊急停止開關（p.5–8）。
- [[papers/mozannar2025-magentic-ui]]：使用者可以隨時暫停並接手 agent 的瀏覽器，改完後再交還給 agent（p.7）。使用者也希望能回到之前的某一步修改，然後從那裡重跑（p.21）。

## 相關趨勢與爭論

- [[trends/designing-for-uncertainty]]
- [[concepts/mixed-initiative]]
