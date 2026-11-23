# 爭論：人應該監督 agent 到什麼程度？

## 爭論點

agent 執行任務時，人是否一定要參與驗證和監督？還是在某些情況下，讓 agent 完全自主反而比較好？（綜合：[[papers/bansal2024-human-agent-communication]] §3、[[papers/feng2025-levels-of-autonomy]] §3.5）

## 立場 A：人必須能驗證 agent 的行為（Bansal 等人）

- **主張**：讓使用者能輕鬆驗證 agent 的行為，是有效溝通的**必要條件**；做不到，使用者就無法引導 agent 避免代價高的錯誤，也無法形成正確的心智模型（[[papers/bansal2024-human-agent-communication]] p.7）。
- **證據**：以 agent 修 GitHub bug 為例，可能誤解需求、漏改測試、產生不安全的修正或副作用（[[papers/bansal2024-human-agent-communication]] p.7）。購物 agent 可能亂花錢或洩漏信用卡資料（[[papers/bansal2024-human-agent-communication]] p.2）。
- **情境**：一般用途、會在開放世界中行動、有真實後果的 agent。

## 立場 B：有時候人的介入反而會降低品質（Feng 等人）

- **主張**：在大多數情況下 L5 的風險可能大於效益，但在某些情況下，使用者介入反而可能讓最終結果變差（[[papers/feng2025-levels-of-autonomy]] p.8）。
- **證據**：當處理的資訊極度複雜、超出使用者理解時，人的介入可能帶來 agent 原本會避免的錯誤；在封閉的沙盒環境裡，agent 的行動不會影響外界（[[papers/feng2025-levels-of-autonomy]] p.8）。這部分是推論，沒有實驗數據。
- **情境**：資訊極度複雜的任務，或模擬、沙盒等封閉環境。

## 實證補充：Magentic-UI 的結果

- **支持立場 A**：讓 agent 能向一個掌握額外資訊的模擬使用者求助後，GAIA 正確率從 30.3% 提升到 51.9%，而 agent 只在 10% 的任務中求助（[[papers/mozannar2025-magentic-ui]] p.19）。在 24 個對抗情境中，動作守門搭配沙盒，讓所有攻擊都失敗；關掉防護後，prompt 注入就能讓 agent 外洩私鑰（[[papers/mozannar2025-magentic-ui]] p.23–24）。
- **呼應立場 B 的代價面**：有些使用者覺得動作守門的確認請求太多，長時間的任務紀錄也讓人難以監看（[[papers/mozannar2025-magentic-ui]] p.25）。這不是說人的介入會降低品質，而是說監督有成本。
- 限制：模擬使用者是 LLM，質性研究只有 12 人，也沒有測量實際生產力（[[papers/mozannar2025-magentic-ui]] p.19、p.26）。

## 在哪種情境下哪一方比較成立

- **代價高、不可逆、會影響外界的動作**：兩篇的看法其實一致，都主張要由人把關。Bansal 認為高代價動作要先取得許可（[[papers/bansal2024-human-agent-communication]] p.15）；Feng 也說 L1 適合高風險、高專業的工作（[[papers/feng2025-levels-of-autonomy]] p.5）。
- **低風險、大量重複的決策**：Bansal 認為熟悉的情況可以讓 agent 更自主（[[papers/bansal2024-human-agent-communication]] p.8）；Feng 認為 L4 適合這類任務（[[papers/feng2025-levels-of-autonomy]] p.7）。兩篇方向一致。
- **真正有分歧的情況**：任務很複雜、但結果只發生在封閉環境中。這時 Feng 允許 L5，Bansal 則沒有討論這種例外（綜合：[[papers/bansal2024-human-agent-communication]]、[[papers/feng2025-levels-of-autonomy]]）。

## 仍未解決的問題

- Bansal 和 Feng 都是立場或分析型論文，都**沒有實證數據**證明「人的介入在什麼條件下會讓結果變好或變差」（[[papers/bansal2024-human-agent-communication]] p.3；[[papers/feng2025-levels-of-autonomy]] p.4）。
- agent 要怎麼可靠地判斷哪些動作「代價高」到需要請人批准？兩篇都把這列為開放問題（[[papers/feng2025-levels-of-autonomy]] p.8；[[papers/bansal2024-human-agent-communication]] p.15）。
- 不同使用者想要的確認頻率不一樣，該怎麼依照個人的風險容忍度和逐漸建立的信任來調整？（[[papers/mozannar2025-magentic-ui]] p.25）
