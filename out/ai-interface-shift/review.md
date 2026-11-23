# Review：ai-interface-shift（審查者：逐頁對照 sources: 所引用的 wiki 頁）

- slide-01: 「階段一 AI 會出錯 → 階段二 AI 會生成 → 階段三 AI 會行動」的三階段框架，`sources:` 只列了 trends/from-tools-to-agents，而這頁只支撐「階段三」；階段一、二分別來自 trends/designing-for-uncertainty、trends/from-commands-to-intent（以及 papers/subramonyam2024-gulf-of-envisioning「與其他論文的關係」的綜合），應補進 sources | 建議退回節點 4
- slide-04: 「49 位實務者在 20 個產品上實測，處處適用」說得太滿。wiki（papers/amershi2019-guidelines p.7、p.9）只說每個產品類別都至少找到每條準則的一個例子；同時 G3、G5、G6 最常被評為「不適用」，語音助理、活動追蹤器等沒有圖形介面的產品也較難套用。建議改成「適用範圍很廣」並保留例外 | 建議退回節點 4
- slide-04: 「最常做不到的一條：說明 AI 為什麼這樣做」把 wiki 的「G11 是違反次數**最多之一**」（papers/amershi2019-guidelines p.9；concepts/explainability）寫成唯一第一名，屬於誇大 | 建議退回節點 4
- slide-04: notes 提到「G9『方便修正』」，但這頁 sources 引用的 papers/amershi2019-guidelines 和 concepts/explainability 都沒有寫出 G9 的內容（G9 只出現在 papers/subramonyam2024-gulf-of-envisioning 的綜合段落）。建議改成 wiki 有寫的「G7–G10：出錯時能忽略、修正」，或補上對應的 source | 建議退回節點 4
- slide-05: 「評估鴻溝變大」少了 wiki 的保留語氣。papers/subramonyam2024-gulf-of-envisioning（p.2–3）和 concepts/gulfs-of-execution-and-evaluation 都寫「**可能**變大」 | 建議退回節點 4
- slide-06: notes「第三個缺口最危險」在 wiki 找不到依據。concepts/gulf-of-envisioning 和 papers/subramonyam2024-gulf-of-envisioning 只說意圖性缺口容易導致過度依賴 LLM（p.8），沒有比較三個缺口的危險程度。建議刪掉「最危險」，只保留「容易過度依賴 AI」 | 建議退回節點 4
- slide-10: 「L4 批准者：只有重大動作才找人批准」漏了 wiki 的另一個觸發條件。papers/feng2025-levels-of-autonomy（p.7）和 concepts/levels-of-autonomy 寫的是 agent 遇到**無法自己解決的障礙**（例如需要密碼）**或**重大動作時才找使用者 | 建議退回節點 4
- slide-12: 第一、二點把 42.52%（GAIA 測試集、自主模式）和 30.3%→51.9%（GAIA 驗證集 162 題、模擬使用者）並排放在投影片上，只有 notes 說明兩者不能比，觀眾很容易把它們當成同一組比較。建議在投影片本文標出「測試集／驗證集」，或加上「不同題目集」的註記（papers/mozannar2025-magentic-ui p.16、p.18–19） | 建議退回節點 4
- slide-12: 「但使用者也抱怨：確認請求太多」把「**有些**使用者覺得動作守門的確認請求太多」（papers/mozannar2025-magentic-ui p.25）寫成像是普遍的抱怨。建議改成「部分使用者」 | 建議退回節點 4
- slide-13: 立場 B 漏掉了 debates/how-much-human-oversight 裡的重要限定，可能讓觀眾以為 Feng 主張廣泛採用 L5。原文是：Feng 認為**在大多數情況下 L5 的風險可能大於效益**，只有某些情況人的介入才可能讓結果變差；而且這部分是推論，沒有實驗數據（papers/feng2025-levels-of-autonomy p.8）。另外，debate 頁「仍未解決的問題」指出兩篇都是立場／分析型論文、都沒有實證，這點也建議放進 notes | 建議退回節點 4
- slide-14: 「主線：AI 越能幹，越需要讓人理解和控制」是跨四個 trend 的歸納，但 sources 引用的 trend 頁都沒有這句話，也沒有標成「綜合」（最接近的是 trends/from-tools-to-agents「能力越強，失敗的代價越高」）。如果要保留這條主線，wiki 需要先有一段標明「綜合：…」的出處；而且它應該和 papers/feng2025-levels-of-autonomy 的「自主性和能力分開、越自主不代表越好」一起呈現，避免被理解成能力和控制程度必然綁在一起 | 建議退回節點 2
- coverage: sources.md 列的 5 篇論文（amershi2019、subramonyam2024、bansal2024、feng2025、mozannar2025）都至少被一頁引用，沒有漏掉論文
- coverage: sources.md 列的 [[concepts/human-in-the-loop]] 沒有被任何一頁的 `sources:` 引用。slide-11、12 都在講「把人放進迴路」，建議在其中一頁補上這個來源，或用一句話解釋這個術語 | 建議退回節點 4
- coverage: 趨勢四 [[trends/autonomy-as-design-choice]] 只在 slide-14（總結）被引用；實際介紹自主性的 slide-10 只引用 feng2025 和 concepts/levels-of-autonomy。這個趨勢頁是簡報骨架之一，建議 slide-10 也把它列進 sources | 建議退回節點 4
