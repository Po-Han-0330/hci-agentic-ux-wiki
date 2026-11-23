# 想像鴻溝（gulf of envisioning）

> **一句話定義（給新手）**：用 ChatGPT 這類工具時，「心裡模糊的想法」和「一個能讓 AI 做出好結果的 prompt」之間的距離（[[papers/subramonyam2024-gulf-of-envisioning]] p.3）。

## 說明

舉例來說，只輸入「幫我寫一段給 Taylor 的祝酒詞」，得到的往往是平庸的結果；要得到好的結果，得先想清楚語氣、長度、要提到哪些事，再寫進 prompt。這個「先想清楚」的過程，作者稱為想像（envisioning），而它需要花費大量的認知力氣（[[papers/subramonyam2024-gulf-of-envisioning]] p.2、p.6）。

想像鴻溝由三個缺口組成（[[papers/subramonyam2024-gulf-of-envisioning]] p.3、p.6–8）：

| 缺口 | 使用者不知道的事 | 例子 | 出處 |
|---|---|---|---|
| 能力缺口（capability gap） | 這件事該怎麼做、怎麼拆解 | 把兩頁摘要成一頁，該保留什麼？ | [[papers/subramonyam2024-gulf-of-envisioning]] §3.2.1 |
| 指令缺口（instruction gap） | 怎麼寫成 LLM 聽得懂的指令 | 換一個字，輸出就差很多 | [[papers/subramonyam2024-gulf-of-envisioning]] §3.2.2 |
| 意圖性缺口（intentionality gap） | 輸出好不好、該期待什麼 | 沒有自己的標準，只好全盤接受 | [[papers/subramonyam2024-gulf-of-envisioning]] §3.2.3 |

它和 Norman 的評估鴻溝不同：評估鴻溝是**介面**的回饋不清楚；意圖性缺口則是**使用者自己**沒有形成清楚的意圖（[[papers/subramonyam2024-gulf-of-envisioning]] p.8）。

## 在各論文中的樣貌

- [[papers/subramonyam2024-gulf-of-envisioning]]：提出這個概念，並歸納出 6 個縮小鴻溝的設計模式，例如視覺化追蹤 prompt、一次給多個輸出、讓使用者手動修改輸出（p.11–12）。

## 相關趨勢與爭論

- [[trends/from-commands-to-intent]]
- [[concepts/gulfs-of-execution-and-evaluation]]
