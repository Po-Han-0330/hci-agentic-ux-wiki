# 混合主導（mixed-initiative）

> **一句話定義（給新手）**：人和 AI 輪流主導的互動方式。有時候人直接操作，有時候 AI 主動幫忙，系統要判斷什麼時候該主動、什麼時候該等人下指令。（[[papers/amershi2019-guidelines]] p.2）

## 說明

這個概念來自 Horvitz（1999）的經典論文（本 wiki 尚未 ingest）。根據 Amershi 等人的轉述，Horvitz 提出的原則包括：讓使用者主動叫出智慧服務、依照推論出的目標和信心程度決定 AI 要做多少，以及在考量成本、效益與不確定性後決定該自動執行還是等待使用者輸入（[[papers/amershi2019-guidelines]] p.2）。

Amershi 的 18 條準則裡有 8 條對應到 Horvitz 的原則（[[papers/amershi2019-guidelines]] p.4）。例如 G10「不確定時縮小服務範圍」：自動完成只給 3–4 個建議，而不是直接幫你填完（[[papers/amershi2019-guidelines]] p.3）。

## 在各論文中的樣貌

- [[papers/amershi2019-guidelines]]：「在成本、效益與不確定性之間推論最佳行動」這條原則因為要在模型層決定，被排除在 18 條準則之外（p.11–12）。
- 待查：Horvitz（1999）原文。
- [[papers/bansal2024-human-agent-communication]]：在 agent 時代，混合主導的問題變成「哪些動作該先問人、哪些可以直接做」。高代價動作先取得許可，熟悉的情況則讓 agent 更自主（p.8、p.15）。見 [[concepts/human-in-the-loop]]。
- [[papers/feng2025-levels-of-autonomy]]：L2「協作者」最接近混合主導的理想。人和 agent 都能規劃、分工、執行，並且可以順暢地交接任務（p.5–6）。

## 相關趨勢與爭論

- [[concepts/user-control-and-correction]]
- [[trends/designing-for-uncertainty]]
