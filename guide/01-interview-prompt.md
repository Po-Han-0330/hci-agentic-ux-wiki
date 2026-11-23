# 步驟 1：先討論，再生成（作業要求的訪談）

老師這週要你示範「先討論、後生成」。這個專案已經附了一份寫好的 `AGENTS.md`，但你還是要跑一次這個訪談，把對話記錄下來，反思第 1 題才寫得出來。

**建議做法**：先把 `AGENTS.md` 改名成 `AGENTS.reference.md`，讓 AI 從零訪談你。訪談完它會生成自己的 `AGENTS.md`，你再拿兩份來比較。差在哪裡、為什麼，就是很好的反思素材，也剛好對應投影片第 36 頁的小討論。

---

## 開場 prompt（整段貼進 VS Code 的 agent 對話框）

```
這是 Karpathy 的 LLM Wiki 構想：
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

我想用它來整理「HCI：AI-Native 介面與 Agentic UX 設計趨勢」的論文。
論文 PDF 在 raw/，清單在 raw/SOURCES.md。

先不要建立或修改任何檔案。
請一次只問我一個問題，幫我釐清需求，大約 8–10 題。
至少要涵蓋：讀者是誰、頁面類型、語言、出處要多細、
論文互相矛盾怎麼處理、一次 ingest 一篇還是批次、之後要產出什麼、lint 要檢查什麼。
問完後整理成「需求摘要」給我確認，我說「確認」之後，
才生成 AGENTS.md 和資料夾結構。
```

---

## 我幫你準備的參考答案

AI 問到的時候可以照這些回答，也可以改成你自己的想法。

| 問題 | 參考答案 |
|---|---|
| 讀者是誰？ | 我自己和修這門課的同學。大學部程度，懂基本 HCI（Norman 的 gulf、direct manipulation），但沒讀過這些論文。 |
| 要哪些頁面類型？ | 三種：`papers/`（一篇論文一頁）、`concepts/`（跨論文的概念，例如 autonomy level、human-in-the-loop、generative UI）、`debates/`（論文之間的張力或矛盾）。另外有 `index.md` 和 `log.md`。 |
| 用什麼語言？ | 繁體中文。專有名詞第一次出現時保留英文原文，例如「後設認知（metacognition）」。 |
| 出處要多細？ | 每個論點都要標到「論文 ID + 章節或頁碼」，例如 `[[papers/bansal2024-human-agent-communication]] §4`。數字和直接引述一定要附頁碼。 |
| 論文互相矛盾怎麼辦？ | 不要自己判誰對。開一頁 `debates/`，把雙方主張、各自的證據和情境並列，再寫「仍未解決的問題」。 |
| 一次一篇還是批次？ | 一次一篇。每篇 ingest 完要更新相關的 concept 頁和 index，在 log.md 記一筆，然後讓我 commit。 |
| 之後要產出什麼？ | 用 wiki 做主題 HTML 簡報，例如「Agent 介面的自主性該怎麼設計」。所以 concept 頁要寫得夠「可引用」。 |
| lint 要檢查什麼？ | 斷掉的 `[[連結]]`、孤兒頁、沒有出處的段落、paper 頁缺必要欄位、index 沒列到的頁面。跑 `python scripts/lint_wiki.py`。 |
| 有什麼不能做？ | 不能改 `raw/` 裡的檔案；不能用 wiki 以外的知識補內容，要補就標「待查」；不能刪掉 log.md 的舊紀錄。 |

---

## 訪談完之後

1. 把整段對話複製到 `guide/interview-log.md`（反思要用）
2. 逐條對照「需求摘要」和 AI 生成的 `AGENTS.md`，看摘要裡講到的有沒有都寫進去
3. 跟 `AGENTS.reference.md` 比較，挑一份當正式的 `AGENTS.md`（或兩份合併）
4. `git add -A && git commit -m "AGENTS.md from interview"`
