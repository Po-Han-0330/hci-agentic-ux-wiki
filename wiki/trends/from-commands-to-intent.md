# 趨勢：從「下指令」走向「說意圖」

> **一句話**：AI-native 介面不再要求使用者學會一連串操作步驟，而是讓人用自然語言說出想要的結果；難點因此從「怎麼操作」轉移到「怎麼想清楚、說清楚」（[[papers/subramonyam2024-gulf-of-envisioning]] p.2–3）。

## 是什麼

傳統軟體的功能是預先設計好的，使用者要學會在哪裡按什麼。LLM 介面則沒有固定功能、接受任何文字輸入、輸出也不固定（[[papers/subramonyam2024-gulf-of-envisioning]] p.1–2）。作者把這種新模式描述為「意圖就是動作」（[[papers/subramonyam2024-gulf-of-envisioning]] p.3）。

## 為什麼會出現

LLM 能理解模糊的自然語言、執行大量沒有事先設計過的任務，使用者不再需要把需求翻譯成操作步驟，執行鴻溝因此大幅縮小（[[papers/subramonyam2024-gulf-of-envisioning]] p.2）。

## 哪些論文支持

- [[papers/subramonyam2024-gulf-of-envisioning]]：提出「想像鴻溝」來描述這個轉變帶來的新認知負擔（p.3），並分析 ChatGPT、Cursor 等介面（p.9–11）。

## 反例或爭議

- 只有「說」還不夠：意圖說不清楚時，使用者只能反覆試錯，而且容易固著在第一個結果上（[[papers/subramonyam2024-gulf-of-envisioning]] p.7）。
- 任務明確時，人反而偏好專門的介面和直接操作，而不是開放的對話框（[[papers/subramonyam2024-gulf-of-envisioning]] p.12）。相關概念：[[concepts/direct-manipulation]]。

## 對設計者的意義

不要只放一個空白的對話框。可以提供 prompt 建議、主動詢問缺少的資訊、一次給多個輸出，並讓使用者直接修改結果（[[papers/subramonyam2024-gulf-of-envisioning]] p.8、p.11–12）。這也延續了 [[trends/designing-for-uncertainty]] 的精神：AI 的輸出不固定，所以要讓人能比較和修正（綜合：[[papers/amershi2019-guidelines]]、[[papers/subramonyam2024-gulf-of-envisioning]]）。相關概念：[[concepts/gulf-of-envisioning]]。
