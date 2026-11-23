# 操作紀錄

> 只能往下加，不能刪改舊紀錄。格式：`## [YYYY-MM-DD] <ingest|query|lint|slides> | <對象>`

## [2026-11-23] setup | 建立專案骨架
- 新增 AGENTS.md、wiki/index.md、wiki/log.md、scripts/、workflows/

## [2026-11-23] setup | 訪談後生成 AGENTS.md
- 經「先討論、後生成」訪談（guide/interview-log.md）重寫 AGENTS.md，原版另存為 AGENTS.reference.md
- 新增 wiki/trends/，index.md 加入「趨勢（trends）」區塊

## [2026-11-23] ingest | amershi2019-guidelines
- 新增：papers/amershi2019-guidelines
- 新增：concepts/expectation-setting、concepts/explainability、concepts/user-control-and-correction、concepts/mixed-initiative、concepts/heuristic-evaluation
- 新增：trends/designing-for-uncertainty
- 更新：index.md
- 備註：使用者指示「直接做」，跳過 ingest 計畫確認

## [2026-11-23] lint | FAIL → PASS（amershi2019-guidelines）
- 第 1 輪 FAIL：✗ log.md 沒有 ingest 紀錄（流程順序：lint 在記 log 之前跑）；! 5 個概念頁的「一句話定義」沒有出處
- 修正：每個定義句補上 [[papers/...]] 與頁碼；補記 log
- 一開始寫成 [[papers/horvitz1999-mixed-initiative]]，但這篇還沒 ingest，會變成斷掉的連結；寫入前就改成純文字並標「待查」
- 往前移的檢查：之後新建概念頁時，定義句一開始就附出處

## [2026-11-23] ingest | subramonyam2024-gulf-of-envisioning
- 新增：papers/subramonyam2024-gulf-of-envisioning
- 新增：concepts/gulf-of-envisioning、concepts/gulfs-of-execution-and-evaluation、concepts/direct-manipulation
- 新增：trends/from-commands-to-intent
- 更新：concepts/explainability、concepts/user-control-and-correction、index.md
- 和 amershi2019 只是重點不同，沒有直接衝突，所以沒有開 debate 頁

## [2026-11-23] lint | PASS（subramonyam2024-gulf-of-envisioning）
- ! concepts/gulf-of-envisioning 的表格沒有出處 → 加上「出處」欄，每列標章節

## [2026-11-23] ingest | bansal2024-human-agent-communication
- 新增：papers/bansal2024-human-agent-communication
- 新增：concepts/common-ground、concepts/human-in-the-loop
- 新增：trends/from-tools-to-agents
- 更新：concepts/expectation-setting、concepts/explainability、concepts/user-control-and-correction、concepts/mixed-initiative、index.md
- 沒有開 debate 頁：X1（驗證）和 X3（細節不能太多）是同一篇內部的取捨，不是兩篇論文之間的衝突

## [2026-11-23] ingest | feng2025-levels-of-autonomy
- 新增：papers/feng2025-levels-of-autonomy
- 新增：concepts/levels-of-autonomy
- 新增：trends/autonomy-as-design-choice
- 新增：debates/how-much-human-oversight（第一個 debate：Bansal X1 認為驗證是必要條件，Feng §3.5 認為介入有時會降低品質）
- 更新：concepts/human-in-the-loop、concepts/mixed-initiative、concepts/user-control-and-correction、index.md

## [2026-11-23] lint | PASS（feng2025-levels-of-autonomy）
- ! debates/how-much-human-oversight 開頭的「爭論點」那段沒有出處 → 補上（綜合：…）標記
- 觀察：「爭論點」「定義」這種用來開頭的句子最容易漏掉出處，第 1、2、4 篇都發生過

## [2026-11-23] ingest | mozannar2025-magentic-ui
- 新增：papers/mozannar2025-magentic-ui
- 新增：concepts/co-planning、concepts/action-guards
- 更新：debates/how-much-human-oversight（加入實證補充，清掉「待查」）
- 更新：concepts/human-in-the-loop、common-ground、levels-of-autonomy、explainability、user-control-and-correction、index.md
- 已達作業要求的 5 篇

## [2026-11-23] lint | PASS + 人工檢查（ingest 5 篇後）
- 腳本：PASS，23 頁（論文 5 篇），沒有警告
- 人工檢查（AGENTS.md §8，腳本沒有涵蓋的項目），用一段臨時腳本掃描：
  - 數字沒附頁碼：2 處（amershi、bansal 的「一句話」摘要）→ 補上 p.1 / p.1–2
  - concept 頁缺新手定義：0 處
  - trends 段落沒有出處：1 處（designing-for-uncertainty 的開頭摘要）→ 補上出處
- 觀察：「一句話」這類摘要句最常漏掉出處，因為寫的時候把它當成導言，而不是論點

## [2026-11-23] slides | ai-interface-shift（節點 1–4）
- 節點 1 檢索：sources.md 列 16 頁（論文 5 篇）→ check_coverage PASS
- 節點 2 證據卡：5 張，每張只來自一篇論文 → check_cards PASS
- 節點 3 大綱：14 頁 → 第 1 輪 FAIL：標題頁的 `cards:` 留空，check_outline.py 的正規表示式 `^cards:\s*(.*)$` 會吃掉換行，把下一行「重點:」誤當成卡片名稱 → 拿掉標題頁的 cards 行 → PASS。腳本 bug 尚未修正
- 人工確認大綱：使用者指示「直接做」，跳過這一關
- 節點 4 逐頁稿：check_drafts 第 1 輪就 PASS，但作者自我比對 wiki 時發現 3 個腳本抓不到的忠實度問題：
  - slide-02 的兩個例子是作者自己編的（wiki 裡沒有）→ 改成 wiki 概念頁的內容
  - slide-07「改成專業語氣」出自論文原文，wiki 裡沒有 → 改成 wiki 有的說法
  - slide-12 備註說「測試集與驗證集不同」，wiki 裡沒有 → **退回 wiki 層**，在 papers/mozannar2025-magentic-ui 補上題目集資訊（p.16、p.18–19）
- 觀察：check_drafts 只檢查數字和出處是否存在，檢查不了「舉例和說法有沒有出處」。這正是 workflow 要求另外做 AI 審查的原因

## [2026-11-23] slides | ai-interface-shift（節點 5–6）
- render_deck.py → out/ai-interface-shift/deck.html（14 頁）
- run_checks.py：全部關卡 PASS；沒有安裝 Playwright，所以沒做真實溢出檢查
- 尚未完成：獨立 AI 審查（workflow 規定要在新對話中進行，作者不能審自己的作品）
