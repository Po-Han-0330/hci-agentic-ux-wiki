---
description: 用 Graph workflow 從 wiki 產生 HTML 簡報
---
照 workflows/topic-slides.md 做簡報。參數：$ARGUMENTS
（格式：主題：<主題>，slug：<英文短名>）

規則：
- 一次只走一個節點，每個節點做完就跑對應的檢查腳本，通過才往下。
- 每個節點只能看、只能寫規格表允許的檔案。
- 節點 3（大綱）通過腳本後，**停下來等我確認**。
- 節點 5 一律用 `python scripts/render_deck.py <slug>` 渲染，你不能手寫或修改 deck.html。
- 錯在哪一關就退回哪一關，照「退回規則」表。整個流程最多重跑 3 輪。
- 最後跑 `python scripts/run_checks.py <slug>`，把 report.md 的結論告訴我。
