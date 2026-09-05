# Meeting_Minutes

金控AI推動委員會PMO會議紀錄撰寫 skill 的版本庫。

規則來自實際會議的逐字稿與定稿比對，隨每場會議累積。

## 目錄結構

```
Meeting_Minutes/
├── README.md                          給人看的維護說明（本檔）
└── ai-pmo-meeting-minutes/            技能資料夾，打包上傳的對象
    ├── SKILL.md                       主指令
    └── references/
        ├── 術語與人名校正表.md          語音轉檔錯字、人名對照
        └── 範例對照.md                  逐字稿與定稿的完整對照
```

技能資料夾內部不放 README.md。該資料夾只放 Claude 會讀的內容。

## 更新流程

1. 在對話中修訂規則
2. 把改動同步到本 repo 的 `ai-pmo-meeting-minutes/` 底下並 commit
3. 將 `ai-pmo-meeting-minutes/` 整個資料夾壓成 zip（或 .skill）
4. 上傳到 claude.ai

壓縮時壓資料夾本身，不要進到資料夾裡選檔案再壓，否則 zip 內會缺一層目錄。

## 上傳到 claude.ai

claude.ai 或桌面版 →「設定」→「Skills」→「新增」→「上傳技能」。

- 介面版本不同，該區可能叫 Features 或 Capabilities，找到 Skills 那一區即可
- zip 或 .skill 檔內必須含一份 SKILL.md
- 需要 Pro、Max、Team 或 Enterprise 方案，並開啟程式碼執行功能
- 上傳後會顯示在技能庫，右上角開關為啟用狀態即代表安裝完成
- 安裝一次即常駐，之後每個新對話會自動判斷是否調用，不必手動呼叫

**每次更新規則都要重新上傳。** 技能庫存的是上傳當下那份檔案，repo 改動不會自動同步到 claude.ai。GitHub 在此的作用是版本控制與歷史紀錄，不是省掉上傳的方法。

claude.ai、Claude Code、API 三個平台的 skill 不互通，各自要裝。

## 安裝後的驗證

開新對話輸入「幫我整理 PMO 會議紀錄」，若 Claude 主動詢問會議結束時間、本次出席狀態、Loop 看板現況，代表 skill 已被觸發。

## Repo 設定注意事項

- **預設分支要是 main**。若預設分支被設成某條工作分支（例如 `claude/xxx`），Claude 的 GitHub 整合在抓 repo 時可能失敗，症狀是選了之後跳掉。到 repo 的 Settings → General → Default branch 切換
- **GitHub App 的授權範圍在帳號底下，不在 repo 底下**。路徑是 `github.com/settings/installations` → Claude → Configure。若當初選的是 Only select repositories，要把本 repo 勾進去
- **空 repo 可能無法被選取**，先推一個檔案進去

以上都正常仍無法選取，屬已知的後端問題，與本地設定無關。

## 規則的來源

| 版本依據 | 內容 |
| --- | --- |
| 2026/7/23 | 首份配對範例，確立結構、壓縮比、選材原則 |
| 2026/7/23 第一版與定稿差異 | 修訂方向十條：正面表述、協作語彙、補全機構全名等 |
| 2026/8/6 | 交辦句式、敏感詞去識別、案件取捨與命名 |
| 2026/8/20 | 交辦句式的前提、執行細節刪除標準、追蹤表分工 |

規則多為三至四場會議的歸納，樣本仍少。累積更多場之後宜整理而非持續追加。
