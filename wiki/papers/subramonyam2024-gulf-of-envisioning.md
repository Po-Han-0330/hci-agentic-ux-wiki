---
id: subramonyam2024-gulf-of-envisioning
title: "Bridging the Gulf of Envisioning: Cognitive Challenges in Prompt Based Interactions with LLMs"
authors: Subramonyam, Pea, Pondoc, Agrawala, Seifert
venue: CHI 2024
year: 2024
type: paper
---

## 一句話
用 LLM 時，難的不再是「怎麼按按鈕」，而是「想清楚自己到底要什麼，並把它寫成 prompt」。作者把這段新的認知鴻溝稱為「想像鴻溝」（gulf of envisioning）。

## 研究問題
傳統介面的功能是預先設計好的（例如計算機），LLM 則沒有固定功能、接受任何自然語言輸入、輸出又是機率式的（p.1–2，Figure 1 的三個維度：功能彈性、意圖明確度、輸出確定性）。Norman 的執行鴻溝（gulf of execution）和評估鴻溝（gulf of evaluation）模型沒有處理「人怎麼從目標形成意圖」這一段（p.1）。這篇要問：在 prompt 式互動中，使用者面對什麼新的認知挑戰？

## 方法
這是一篇**理論與分析型**論文，沒有做使用者實驗（§6，p.12）：
- 結合認知科學（問題解決、寫作的認知歷程模型）和 HCI 理論，提出新的互動模型（§3，p.5–9）。
- 分析三個現有的 LLM 介面：ChatGPT（寫作）、Spellburst（創意程式）、Cursor（軟體開發），看三種鴻溝怎麼出現（§4，p.9–11）。
- 對 12 個系統做質性分析，歸納出 6 個設計模式（§5，p.11–12）。

## 主要發現
- LLM 讓**執行鴻溝變小**：使用者不用再學操作步驟，只要說出意圖；但因為輸出是機率式的，**評估鴻溝可能變大**（p.2–3）。
- 新出現的「想像鴻溝」是指：從最初的意圖，到寫出一個能讓 LLM 產生高品質結果的 prompt，中間的距離（p.3）。它包含三個缺口（p.3）：
  1. **能力缺口（capability gap）**：不知道「該怎麼做」這件事，也就是任務該怎麼拆解（§3.2.1，p.6）。
  2. **指令缺口（instruction gap）**：不知道怎麼把意圖寫成 LLM 聽得懂的文字；用字稍微不同，輸出就可能差很多（§3.2.2，p.7–8）。
  3. **意圖性缺口（intentionality gap）**：直接丟目標給 LLM、跳過自己規劃的人，沒有內在標準可以判斷輸出好不好，因此容易過度依賴 LLM（§3.2.3，p.8）。
- 三條互動路徑：①直接說目標（例如「幫我寫一段給 Taylor 的祝酒詞」）、②花力氣把意圖寫清楚、③離開對話，改用專門工具繼續修改（Figure 3，p.7）。
- 反覆修改 prompt 有成本：人容易**固著（fixation）**在第一個輸出上，只做局部修改而錯過其他可能（p.7）。
- 6 個設計模式（§5，p.11–12）：視覺化追蹤 prompt 與輸出、建議 prompt 寫法、一次提供多個輸出、讓輸出可解釋、使用特定領域的 prompt 策略、**允許手動控制輸出**。

## 設計啟示
- 介面可以當「prompt 引導者」（prompt prompter）：主動問使用者缺少的資訊，例如「你的讀者是誰？」（p.8）。
- 任務定義清楚時，人偏好專門的介面，而不是什麼都能做的對話框（設計原則 T7，p.12）。
- 一次給多個輸出，可以支援發散思考，也能減少固著（p.12）。
- 人和 LLM 之間的錯誤，不只是「使用者錯」或「模型錯」，而是整個協作系統的斷裂，需要一起修復（T5，p.12）。
- 設計解釋時要小心使用者不經驗證就過度相信解釋（p.12）。

## 限制
- 理論提案，**沒有實證驗證**；作者自己說需要實證研究來檢驗（§6.2，p.14）。
- 每個人從目標形成意圖的能力差異很大，模型可能高估一般人的能力（§6.2，p.14）。
- 分析主要以寫作任務為例，作者也承認自己只是提供起點，不是完整分類（p.11）。

## 與其他論文的關係
- 延伸 [[papers/amershi2019-guidelines]] 的問題意識：Amershi 處理的是「AI 輔助功能」的可預測性問題；這篇面對的是 LLM 沒有固定功能、輸入完全開放的新狀況，難點從「AI 會錯」擴大到「人說不清楚自己要什麼」（綜合：[[papers/amershi2019-guidelines]]、[[papers/subramonyam2024-gulf-of-envisioning]]）。
- 設計模式 6「手動控制輸出」呼應 Amershi 的 G9「方便修正」（綜合：[[papers/amershi2019-guidelines]] p.3、本篇 p.12）。

## 相關概念
- [[concepts/gulf-of-envisioning]]
- [[concepts/gulfs-of-execution-and-evaluation]]
- [[concepts/direct-manipulation]]
- [[concepts/explainability]]
- [[concepts/user-control-and-correction]]
