# 作業反思

> 每題寫 1–2 段即可。括號裡是提示，寫完請刪掉。

## 1. 建 Wiki 時特別考量的事情

（可以從這些角度挑幾個寫）
- 訪談後生成的 AGENTS.md 跟參考版（或上週一句話生成的版本）差在哪裡？哪個差異影響最大？
- 為什麼要把頁面分成 papers／concepts／debates 三種？`debates/` 實際抓到了哪些張力？例如 Horvitz 1999 的 mixed-initiative 和 Feng 2025 的五級自主性，觀點有沒有連續或衝突的地方？
- 出處要標到頁碼，實際做起來怎麼樣？AI 有沒有編過頁碼？
- `lint_wiki.py` 抓到過什麼問題？

## 2. Graph 或 Loop 的設計

（附上 workflows/topic-slides.md 的流程圖截圖）
- 為什麼選 Graph 不選 Loop？（提示：各階段標準不同、需要人工確認大綱、錯誤要在離源頭最近的地方被抓到）
- 哪一道關卡最常擋下東西？是大圈還是小圈？
- 「渲染交給腳本、不交給 AI」這個設計有什麼好處？
- AI 審查（開新對話）有抓到作者自己沒發現的問題嗎？舉一個例子。
- 實際跑了幾輪？附上 report.md 的結論。

## 3. 其他心得

（例如：這次的主題本身是 Agentic UX，你在設計 workflow 時有沒有用上論文裡學到的東西？像是 Magentic-UI 的 co-planning 或 action guards，對應到大綱的人工確認關卡。）
