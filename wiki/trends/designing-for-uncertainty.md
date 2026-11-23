# 趨勢：為「會出錯、會變的 AI」重新設計介面

> **一句話**：傳統介面假設系統的行為可以預測；AI 是機率式的，會出錯也會改變，所以介面設計的重心轉向「設定預期、解釋原因、讓人修正」（[[papers/amershi2019-guidelines]] p.1–3）。

## 是什麼

設計重心從「讓操作一致、預防錯誤」，轉向「承認 AI 會錯，然後設計人怎麼理解它、控制它、修正它」。Amershi 等人把這個方向整理成 18 條準則，其中有一整組準則專門處理「AI 出錯時」（[[papers/amershi2019-guidelines]] p.3）。

## 為什麼會出現

AI 是在不確定的情況下推論，常常產生誤判；同一個輸入可能因為模型更新或個人化而得到不同結果。這讓「一致性」「預防錯誤」等傳統可用性原則很難做到，而不一致又會讓使用者困惑、失去信心，最後放棄使用（[[papers/amershi2019-guidelines]] p.1–2）。

## 哪些論文支持

- [[papers/amershi2019-guidelines]]：18 條準則在 20 個熱門產品、10 個類別裡都找得到做到或違反的例子（p.7），代表這是普遍存在的設計問題，不是特例。

## 反例或爭議

- 解釋不一定永遠需要：低風險情境（音樂推薦）比高風險情境更不需要解釋（[[papers/amershi2019-guidelines]] p.4）；有時候也會基於商業理由刻意不解釋（[[papers/amershi2019-guidelines]] p.9）。

## 對設計者的意義

在設計 AI 功能時，同時規劃四個時間點的體驗：一開始（說清楚能力）、互動中（看情境）、出錯時（能忽略、能修正）、長期使用（謹慎更新、讓人控制）（[[papers/amershi2019-guidelines]] p.3–4）。相關概念：[[concepts/expectation-setting]]、[[concepts/explainability]]、[[concepts/user-control-and-correction]]。
