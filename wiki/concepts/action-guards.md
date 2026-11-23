# 動作守門（action guards）

> **一句話定義（給新手）**：agent 要做可能無法挽回的動作時（例如付款、上傳檔案），先停下來請人批准；不會造成影響的動作（例如捲動頁面）就直接做（[[papers/mozannar2025-magentic-ui]] p.14）。

## 說明

Magentic-UI 用兩階段判斷（[[papers/mozannar2025-magentic-ui]] p.14）：

| 動作的預設標記 | 例子 | 怎麼處理 | 出處 |
|---|---|---|---|
| 一定不可逆 | 上傳檔案 | 一律請人批准 | [[papers/mozannar2025-magentic-ui]] p.14 |
| 可能不可逆 | 點擊按鈕 | 交給 LLM 判斷要不要問人 | [[papers/mozannar2025-magentic-ui]] p.14 |
| 絕不會不可逆 | 捲動頁面 | 直接執行 | [[papers/mozannar2025-magentic-ui]] p.14 |

另外還可以設定「允許網站清單」：要前往清單以外的網站時，agent 會說明網址和理由，並請使用者批准（[[papers/mozannar2025-magentic-ui]] p.26）。

## 在各論文中的樣貌

- [[papers/mozannar2025-magentic-ui]]：在 24 個對抗情境中，動作守門搭配沙盒等多層防護，讓所有攻擊都沒有成功（p.23–24）。但部分使用者覺得確認請求太多，作者認為確認頻率應該依照使用者的風險容忍度和信任程度調整（p.25）。
- [[papers/bansal2024-human-agent-communication]]：對應 A2，主張高代價動作（花錢、不可逆、可能違反偏好）要先取得使用者許可（p.15）。
- [[papers/feng2025-levels-of-autonomy]]：L4「批准者」的核心就是動作守門，並提醒這可能淪為無意識批准的「橡皮圖章」（p.7–8）。

## 相關趨勢與爭論

- [[debates/how-much-human-oversight]]
- [[concepts/human-in-the-loop]]
- [[concepts/user-control-and-correction]]
