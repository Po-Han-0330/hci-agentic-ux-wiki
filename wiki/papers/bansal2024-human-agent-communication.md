---
id: bansal2024-human-agent-communication
title: Challenges in Human-Agent Communication
authors: Bansal, Vaughan, Amershi, Horvitz, Fourney, Mozannar, Dibia, Weld
venue: Microsoft Research（MSR-TR-2024-53）／arXiv 2412.10380
year: 2024
type: tech-report
---

## 一句話
當 AI 從「回答問題」變成「替你上網、寫程式、花錢做事」的 agent 時，人和 agent 之間要溝通的東西變多也變難了。Microsoft 團隊整理出 12 個溝通挑戰，核心是「建立共同基礎」（common ground）（p.1–2）。

## 研究問題
現代 agent 以生成式基礎模型為核心，又能呼叫工具（API、瀏覽器、執行程式碼），可以對數位和實體世界採取行動（p.2–4）。能力變強，失敗的方式和代價也跟著變多：購物 agent 可能亂花錢或洩漏信用卡資料，寫程式的 agent 可能刪掉重要檔案（p.2）。既有的人機 AI 準則（例如 [[papers/amershi2019-guidelines]]）沒有涵蓋這些新問題（p.3）。這篇問：人和 agent 要怎麼溝通，才能讓使用者理解、監看並控制 agent？

## 方法
**立場與分析型**報告（非實驗研究）：根據作者團隊打造複雜 agent 和多 agent 系統的經驗，加上人機互動、心理學、團隊合作的文獻，特別是 Clark & Brennan 的「溝通中的共同基礎」（grounding in communication），歸納出 12 個挑戰，並舉例說明、提出可能的方向（p.3–4）。作者說明這份清單並不完整（p.3）。

## 主要發現
12 個挑戰分成三組，並依互動的「之前、執行中、之後」排列（Figure 1，p.1）：

**agent → 使用者（A1–A5）**
- A1 agent 能做什麼？（p.13）
- A2 agent 接下來要做什麼？代價高的動作（花錢、不可逆、可能違反偏好）要先取得使用者同意（p.15）
- A3 agent 現在在做什麼？使用者要能判斷是否該介入或叫停（p.16）
- A4 有沒有副作用？例如訂機票時順便幫使用者辦了一張信用卡（p.18）
- A5 目標達成了嗎？（p.19）

**使用者 → agent（U1–U3）**
- U1 agent 該達成什麼目標？誤解目標會浪費時間和金錢，甚至造成傷害（p.9）
- U2 agent 該尊重哪些偏好？每個人對「傷害」的定義都不同（p.11）
- U3 agent 下次該怎麼改？（p.12）

**整體挑戰（X1–X4）**
- X1 怎麼幫使用者驗證 agent 的行為（p.7）
- X2 怎麼讓行為看起來一致：即使模型溫度設為 0，agent 在變動的環境中也可能每次走不同的步驟（p.7）
- X3 細節要給多少：太少無法驗證，太多會讓使用者負擔過重，也可能過度限制 agent（p.8）
- X4 要參考哪些過去的互動：情境資料會無限累積，而使用者應該能限制 agent 使用哪些背景資訊，例如類似瀏覽器的無痕模式（p.8–9）

- 結論：agent 行動又快又複雜、行為又是隨機的，讓共同基礎更難建立；作者呼籲發展新的設計模式和準則（§6，p.20）。

## 設計啟示
- 在動作「之前、執行中、之後」都要設計溝通管道：事前預告計畫並在高代價動作前請求許可（A2）、執行中即時顯示進度並可叫停（A3）、事後摘要副作用和結果（A4、A5）（p.15–19）。
- 熟悉、低風險的情況可以讓 agent 更自主，減少確認次數；新奇或模糊的情況才詢問（X3，p.8）。
- 讓使用者能檢視、編輯、清除 agent 的記憶與背景資訊（X4，p.9）。

## 限制
- 不是實證研究，挑戰清單來自作者經驗和文獻，作者自己說不完整（p.3）。
- 技術、倫理、安全、公平性問題刻意不在範圍內（p.4）。
- 作者主要來自 Microsoft，例子多來自他們自己的 agent 系統（p.1、p.3）。

## 與其他論文的關係
- 作者群和 [[papers/amershi2019-guidelines]] 重疊（Amershi、Horvitz、Fourney）。A1「agent 能做什麼」延續 Amershi 的 G1，但 Bansal 認為 agent 讓這些老問題變得更複雜（綜合：[[papers/amershi2019-guidelines]] p.3、本篇 p.13、p.20）。
- U1「agent 該達成什麼目標」和 [[papers/subramonyam2024-gulf-of-envisioning]] 的想像鴻溝是同一個問題的兩面：使用者說不清楚意圖，agent 就會誤解目標（綜合：[[papers/subramonyam2024-gulf-of-envisioning]] p.3、本篇 p.9）。
- X3 指出「細節給多少」的取捨，和 Amershi 的 G12、G13（記住互動、從行為學習）相呼應，但 X4 更強調使用者要能限制 agent 使用的情境（綜合：[[papers/amershi2019-guidelines]] p.3、本篇 p.8–9）。

## 相關概念
- [[concepts/common-ground]]
- [[concepts/human-in-the-loop]]
- [[concepts/expectation-setting]]
- [[concepts/explainability]]
- [[concepts/user-control-and-correction]]
