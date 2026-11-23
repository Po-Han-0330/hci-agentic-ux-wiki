---
slide: 11
title: 實例：Magentic-UI 怎麼把人放進迴路
layout: compare
sources: papers/mozannar2025-magentic-ui, concepts/co-planning, concepts/action-guards, concepts/human-in-the-loop
---
### 共同規劃（co-planning）
- 動手前先列出步驟計畫
- 使用者直接修改，按確認才開始
- 先對齊，比事後修正便宜
### 動作守門（action guards）
- 一定不可逆（上傳檔案）：請人批准
- 可能不可逆（點按鈕）：交給 LLM 判斷
- 不會不可逆（捲動頁面）：直接做
> notes: 「人在迴路中」（human-in-the-loop）是指在關鍵時刻讓人確認、批准、插手。Magentic-UI 是 Microsoft 的開源 agent 介面，一共有 6 種機制，還有共同執行、答案驗證、記憶、多工。
