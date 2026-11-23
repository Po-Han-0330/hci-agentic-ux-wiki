# AGENTS.md：HCI LLM Wiki（AI-Native 介面與 Agentic UX）

> 這份手冊由「先討論、後生成」的訪談產生（2026-11-23，紀錄見 `guide/interview-log.md`）。
> 任何 agent（Claude Code、Copilot、Codex…）在這個專案工作前都要先讀完。

## 1. 這個 wiki 是什麼

依照 Karpathy 的 LLM Wiki 構想，把 `raw/` 的 HCI 論文整理成一個由 agent 維護、互相連結的 Markdown 知識庫。
主題是「AI-Native 介面與 Agentic UX 設計趨勢」，論文清單見 `raw/SOURCES.md`。

這個 wiki 是**教學型 HTML 簡報的唯一知識來源**（見 §9）。作業評分重點之一是「wiki 資料與簡報內容有明確對應」，所以 wiki 的每個論點都要能被追溯、被引用。

## 2. 讀者與寫作原則

**讀者**：程度不一，包括完全不懂 HCI 或互動設計的人、懂一點但不深入的人，以及專業人士。

**最低目標**：新手讀完能說出「目前 AI 介面的設計趨勢是什麼，以及為什麼會出現這些趨勢」。

**寫法（中間程度 + 術語附解釋）**：
- 主要內容寫給「懂一點」的讀者看。
- 術語第一次出現時，附一句白話解釋，或連到對應的 `[[concepts/...]]` 頁。新手可以點進去補背景，專業讀者可以直接略過。
- 少用沒有解釋的縮寫。能用例子說明就舉例子。

## 3. 語言

- 用**繁體中文**寫。
- 業界通用的英文術語直接用英文，例如 agent、prompt、human-in-the-loop、LLM、UI。
- 其他專有名詞第一次出現時寫成「中文（English）」，例如「後設認知（metacognition）」，之後只寫中文。
- wiki **只維護中文版**。使用者要求英文時，即時翻譯輸出就好，**不要**另存英文檔。
- 檔名和頁面 ID 一律用小寫英文 slug，以 `-` 連接，例如 `concepts/human-in-the-loop.md`。

## 4. 資料夾結構

```
raw/                 原始論文 PDF + SOURCES.md（唯讀，絕對不能改）
wiki/
  index.md           目錄：每頁一行「[[路徑]] — 一句話摘要」
  log.md             操作紀錄：只能往下加
  papers/            一篇論文一頁（檔名 = 論文 ID）
  concepts/          跨論文的概念（同時是新手的術語表）
  trends/            設計趨勢：是什麼 → 為什麼 → 哪些論文支持（簡報的骨架）
  debates/           論文之間的張力或矛盾
workflows/           簡報 graph（topic-slides.md）
scripts/             檢查腳本
out/<slug>/          簡報的中間產物和成品
```

連結一律寫成 `[[資料夾/slug]]`，不加 `.md`，例如 `[[concepts/human-in-the-loop]]`。

## 5. 頁面類型與格式

### 5.1 `papers/<id>.md`

`<id>` 必須和 `raw/SOURCES.md` 的 ID 一致。frontmatter 和以下段落都**必填**，`scripts/lint_wiki.py` 會檢查。

```markdown
---
id: amershi2019-guidelines
title: Guidelines for Human-AI Interaction
authors: Amershi, Weld, Vorvoreanu, et al.
venue: CHI 2019
year: 2019
type: paper            # paper | tech-report | preprint
---

## 一句話
給新手的一句白話摘要。

## 研究問題
這篇想解決什麼問題？為什麼重要？

## 方法
怎麼做的（例如文獻歸納、使用者研究的人數與任務、系統實作）。

## 主要發現
- 論點……（p.3）
- 論點……§4.2

## 設計啟示
對設計 AI / agent 介面的人來說，這篇代表什麼？

## 限制
作者自己承認的限制，以及研究情境（年代、受試者、任務）造成的限制。

## 與其他論文的關係
和其他已 ingest 的論文相比，是支持、延伸還是衝突。有衝突就連到 `[[debates/...]]`。

## 相關概念
- [[concepts/...]]（至少 2 個）
```

### 5.2 `concepts/<slug>.md`

```markdown
# 概念名稱（English）

> **一句話定義（給新手）**：……

## 說明
## 在各論文中的樣貌
## 相關趨勢與爭論
```
開頭的「一句話定義」**必填**，新手的術語解釋就靠它。

### 5.3 `trends/<slug>.md`

```markdown
# 趨勢名稱，例如「從對話走向直接操作」

> **一句話**：……

## 是什麼
## 為什麼會出現
## 哪些論文支持（各附出處）
## 反例或爭議
## 對設計者的意義
```
trend 頁是簡報的主要骨架，要寫成可以直接拿來引用的段落。

### 5.4 `debates/<slug>.md`

開頁標準：兩篇以上的論文對**同一個問題**提出不同的主張或設計建議，才開 debate 頁。如果只是強調的重點不同，在相關的 concept 頁註記就好，不另開頁。

```markdown
# 爭論：<問題>

## 爭論點
## 立場 A：<論文>（主張、證據、研究情境）
## 立場 B：<論文>（主張、證據、研究情境）
## 在哪種情境下哪一方比較成立
（這段也必須有出處，不能是 agent 自己的意見）
## 仍未解決的問題
```
agent **不判斷誰對**。

## 6. 出處規則（論點層級）

- **每個論點**都要標論文和位置：`[[papers/bansal2024-human-agent-communication]] §4` 或 `（p.7）`。
- **數字和直接引述一定要附頁碼**，例如 `（p.5）`。
- 跨論文歸納、沒有任何一篇論文直接這樣說的推論，標成：`（綜合：[[papers/A]]、[[papers/B]]）`。
- 直接引述每次不超過一句，其餘用自己的話改寫。
- 頁碼一律用 **PDF 檔的頁碼**（第 1 頁 = PDF 第 1 頁），避免各期刊的頁碼格式不一致。
- 原始論文裡找不到、但又需要補的內容，標「**待查：<要查什麼>**」，不要用 wiki 以外的知識補。

## 7. Ingest 流程（一次一篇，共七步）

1. **ingest 計畫**：讀 `raw/<id>.pdf`，先回報 3–5 個重點，以及打算新增或修改哪些頁面。**等使用者回「好」或「直接做」才繼續。**
2. **寫 paper 頁**：照 §5.1 的格式，出處照 §6。
3. **更新 concept 頁**：新增或補充相關概念，每頁開頭要有給新手的一句話定義。
4. **更新 trend 和 debate 頁**：這篇支持或挑戰了哪個趨勢？和已 ingest 的論文有沒有衝突（照 §5.4 的標準）？
5. **更新 `wiki/index.md`**：每個新頁面加一行。
6. **記錄 `wiki/log.md`**：格式是 `## [YYYY-MM-DD] ingest | <id>`，下面列出新增和修改的頁面。
7. **lint**：執行 `python3 scripts/lint_wiki.py`，加上 §8 的人工檢查，把結果記進 `log.md`。之後回報給使用者並**停下**，讓使用者檢查和 commit。

建議順序：`amershi2019-guidelines` → `subramonyam2024-gulf-of-envisioning` → `bansal2024-human-agent-communication` → `feng2025-levels-of-autonomy` → `mozannar2025-magentic-ui`，其餘 5 篇有空再加（作業至少 5 篇）。

## 7.5 Query（回答問題）

- 只用 wiki 的內容回答，並附上出處連結。wiki 裡沒有的，回答「wiki 目前沒有這方面的資料」，不要用自己的知識補。
- 值得保留的回答，問使用者要不要存成新的 concept、trend 或 debate 頁。

## 8. Lint

lint 的結果**只列警告，不擋 commit**。不過腳本回報的 `✗` 項目要先修（最多 3 輪），修不掉的列給使用者決定。

| 檢查項目 | 誰檢查 |
|---|---|
| 斷掉的 `[[連結]]` | 腳本 |
| 孤兒頁（沒有其他頁面連到它） | 腳本 |
| 頁面沒有列在 `index.md` | 腳本 |
| 沒有出處的段落 | 腳本（concepts/、debates/）；trends/ 由 agent 人工檢查 |
| paper 頁缺 frontmatter 或必要段落 | 腳本 |
| 數字或直接引述沒附頁碼 | agent 人工檢查 |
| concept 頁缺給新手的一句話定義 | agent 人工檢查 |
| 簡報引用的 wiki 頁不存在 | `scripts/check_drafts.py`（簡報階段） |

每次 lint 都要在 `log.md` 記一筆 `## [YYYY-MM-DD] lint | PASS/FAIL`，寫出找到什麼問題、怎麼修。作業的「檢查紀錄」和反思會用到這些紀錄。

## 9. 產出：教學 HTML 簡報

- 照 `workflows/topic-slides.md` 的 graph 做，中間產物和成品都放在 `out/<slug>/`。
- 對象是不熟悉這個主題的新手。以 `trends/` 頁為骨架，用 `concepts/` 頁補術語。
- 建議主題：「AI 介面正在發生什麼改變？從工具到 Agent 的設計趨勢」。
- 每張投影片都要在 `sources:` 標出對應的 wiki 頁，讓 wiki 和簡報可以明確對應。
- 簡報只能用 wiki 裡的內容，不能直接讀 `raw/`。

## 10. 不能做的事

- ❌ 修改、刪除或搬移 `raw/` 裡的任何檔案
- ❌ 用 wiki 和原始論文以外的知識補內容（需要補的地方標「待查」）
- ❌ 刪除或改寫 `wiki/log.md` 的舊紀錄（只能往下加）
- ❌ 替爭論判斷誰對
- ❌ 自己 `git commit` 或 `git push`，一律由使用者執行
- ❌ 一次 ingest 多篇

## 11. 環境

- macOS：所有 Python 腳本一律用 **`python3`** 執行，例如 `python3 scripts/lint_wiki.py`、`python3 scripts/run_checks.py <slug>`。
- 腳本只用標準函式庫，不需要 `pip install`。
