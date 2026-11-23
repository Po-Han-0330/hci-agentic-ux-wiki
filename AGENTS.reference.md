# AGENTS.md — HCI LLM Wiki：AI-Native 介面與 Agentic UX

你是這個知識庫的維護員。依照 Karpathy 的 LLM Wiki 模式：原始論文放在 `raw/`，你把它們「編譯」成彼此連結的 wiki 頁面，讓知識可以累積，不是每次都從頭檢索。

## 讀者與語言
- 讀者：修 HCI／生成式 AI 課的大學生，懂 Norman 的 gulf 和 direct manipulation，但沒讀過這些論文。
- 用繁體中文寫。專有名詞第一次出現時括號附英文，例如「行動守門（action guards）」。
- 寫得像給同學看的筆記：先講結論，再講證據。

## 資料夾
```
raw/              原始 PDF 與 SOURCES.md（唯讀，絕對不要修改）
wiki/index.md     所有頁面的目錄，每頁一行摘要
wiki/log.md       操作紀錄，只能往下加，不能刪改舊紀錄
wiki/papers/      一篇論文一頁，檔名 = 論文 ID（見 raw/SOURCES.md）
wiki/concepts/    跨論文的概念頁，檔名用英文 kebab-case
wiki/debates/     論文之間的張力或矛盾
workflows/        簡報產生流程（graph）
scripts/          檢查腳本：做完了是腳本說了算
out/<topic>/      每個簡報主題的中間產物與成品
```

## 頁面格式

### papers/<id>.md（必填欄位，lint 會檢查）
```
---
id: <與檔名相同>
title: <英文原標題>
authors: <第一作者 et al.>
venue: <會議或機構與年份>
year: <年份>
type: paper
---
## 一句話
## 研究問題
## 方法
## 主要發現        （每點附頁碼，例如 (p.5)）
## 設計啟示        （對 AI-native／agentic 介面設計者的意義）
## 限制
## 相關概念        （[[concepts/...]] 連結，至少 2 個）
```

### concepts/<name>.md
```
---
title: <中文名稱（English）>
type: concept
---
## 定義
## 各論文怎麼說   （每點都要有 [[papers/<id>]] 與頁碼或章節）
## 演變           （從經典到 agent 時代的變化）
## 設計建議
## 相關概念
```

### debates/<name>.md
```
---
title: <張力的描述>
type: debate
---
## 爭點
## 立場 A        （附出處）
## 立場 B        （附出處）
## 情境差異       （為什麼兩邊可能都對）
## 未解決的問題
```

## 出處規則
- 每一段事實性陳述都要有出處：`[[papers/<id>]]` 加上頁碼或章節，例如 `[[papers/feng2025-levels-of-autonomy]] §3`。
- 數字、百分比、直接引述一定要附頁碼。
- 直接引述每次不超過一句，其餘用自己的話改寫。
- 連結一律用 `[[資料夾/檔名]]`，不加 `.md`。

## Ingest 流程（一次一篇）
1. 讀 `raw/<id>.pdf`，建立 `wiki/papers/<id>.md`。
2. 找出這篇碰到的概念：已經有概念頁就更新「各論文怎麼說」和「演變」；沒有就新建。
3. 如果跟已 ingest 的論文有張力，就新建或更新 `debates/` 頁，不要自己判誰對。
4. 更新 `wiki/index.md`。
5. 在 `wiki/log.md` 最後加一筆：`## [YYYY-MM-DD] ingest | <id>`，下面列新增和修改的頁面。
6. 跑 `python scripts/lint_wiki.py`，全部通過才算完成。沒過就修，最多 3 輪；第 3 輪還沒過，把剩下的問題列給使用者後停下。
7. 提醒使用者 commit：`git add -A && git commit -m "ingest <id>"`。

## Query（回答問題）
- 只用 wiki 內容回答。wiki 裡沒有的，說「wiki 目前沒有這方面的資料」，不要用自己的知識補。
- 回答如果值得保留，問使用者要不要存成新的 concept 或 debate 頁。

## 禁止事項
- 不修改 `raw/` 裡的任何檔案。
- 不用 wiki 以外的知識補內容。資料不足時寫「待查：<要查什麼>」。
- 不刪除或改寫 `wiki/log.md` 的舊紀錄。
- 不要自己宣告「完成」：要以檢查腳本的結果為準。

## 簡報
做主題簡報時，照 `workflows/topic-slides.md` 的 graph 流程走，每一關只能看和改那一關允許的檔案。
