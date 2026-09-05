# Meeting Minutes 會議紀錄產出流程

此 repo 用於將 PMO 例會的逐字稿轉成正式會議紀錄，並產出兩份交付檔：
**Word 會議紀錄**與 **Excel 任務追蹤表**。

## 撰寫規則以 skill 為準

會議紀錄的格式、選材、語體、錯字校正等所有撰寫規則，一律以
`.claude/skills/ai-pmo-meeting-minutes/` 底下的 skill 為準：

- `SKILL.md`：主規則
- `references/術語與人名校正表.md`：語音轉檔錯字與人名對照
- `references/範例對照.md`：完整逐字稿與定稿對照

**動筆前先讀完 SKILL.md 與兩份 reference。** 本檔只規範檔案放哪裡、交付檔怎麼產，
不重複 skill 的內容；兩者若有出入，以 skill 為準。

skill 有更新時用 `bash scripts/pack_skill.sh` 打包成 `.skill` 檔重新上傳 claude.ai，
上傳方式見 `docs/skill維護說明.md`。

## 目錄結構

```
transcripts/            會議逐字稿原文（使用者提供，原封不動保存）
minutes/                會議紀錄本體（Markdown，唯一事實來源）
tracker/                任務追蹤表的資料來源（長表 CSV）
output/word/            Word 會議紀錄（.docx）
output/excel/           Excel 任務追蹤表（.xlsx）
reference/              歷次定稿的配對存檔
templates/              會議紀錄格式範本
scripts/                產出腳本
docs/                   skill 維護說明
.claude/skills/         ai-pmo-meeting-minutes skill 本體
```

`minutes/` 的 Markdown 與 `tracker/` 的 CSV 是唯一事實來源，Word 與 Excel 都由它們產生。
要改內容改 Markdown / CSV 再重跑腳本，不要直接改 Word 或 Excel，否則下次會被覆蓋。

## 每次會議的產出流程

1. 使用者貼上或提供逐字稿 → 原封不動存入 `transcripts/YYYY-MM-DD_雙週會.md`
2. 依 skill「動筆前必須確認的四件事」向使用者取得：**結束時間**、**本次出席狀態**、
   **Loop 看板現況**（最好是截圖）。這三項逐字稿裡沒有，不要自行推論
3. 依 skill 撰寫紀錄本體 → 存入 `minutes/YYYY-MM-DD_雙週會.md`
   - 第一行為會議正式名稱，其下為 壹貳參 → 一二三 → 1. 2. 三層編號
   - **紀錄本體不含郵件套語**（各位主管好、檢送、敬請參閱、Best,）
4. 更新 `tracker/task_progress.csv`：本次有進度的任務各補一列
   - 內容依 skill「會議紀錄與任務追蹤表的分工」：只留節點與下一步，理由留在紀錄
   - 案名與編號沿用 Loop 看板；本次新增議題接在既有編號之後
   - 本次未討論的任務**不必補列**，腳本會自動填「本次未討論」
5. 產出兩份交付檔：
   ```bash
   python3 scripts/md_to_docx.py minutes/YYYY-MM-DD_雙週會.md
   python3 scripts/make_tracker_xlsx.py
   ```
6. 在對話中完整呈現紀錄全文與郵件套語，並用 SendUserFile 把兩個檔案傳給使用者
7. 使用者回修改後的定稿 → 覆蓋 `minutes/`，配對存入 `reference/YYYY-MM-DD_雙週會/`，
   並把學到的規則補進 skill（不是補進本檔）

## 固定會議資訊

- **雙週會**：每兩週一次，週四召開，例如 2026-07-23、2026-08-06、2026-08-20…
- 會議正式名稱：**金控AI推動委員會PMO待辦事項討論例會**
- 使用者未註明日期時，預設為最近一次雙週會，並向使用者確認
- 與會人員名單沿用前次；**出席狀態（誰請假、誰列席）必須每次重新確認，不可沿用**

## 檔名規則

- 一律 `YYYY-MM-DD_會議名稱`，雙週會固定用「雙週會」，例如 `2026-08-06_雙週會.md`
- 逐字稿與會議紀錄同檔名，分別放 `transcripts/` 與 `minutes/`

## 交付檔產出

環境需求：`pip install python-docx openpyxl`

### Word 會議紀錄

```bash
python3 scripts/md_to_docx.py minutes/2026-08-06_雙週會.md          # 只有紀錄本體
python3 scripts/md_to_docx.py minutes/2026-08-06_雙週會.md --email  # 連郵件套語一起
```

- 輸出 `output/word/<檔名>_會議紀錄.docx`
- 版面設定（字型、字級、行距、邊界）集中在 `md_to_docx.py` 檔頭常數
- 依編號層級自動套縮排與凸排：壹貳參粗體、一二三次階、1.2. 再次階
- md 裡若殘留郵件套語會自動略過；`--email` 的日期由檔名推算、會議名稱取第一行

### Excel 任務追蹤表

```bash
python3 scripts/make_tracker_xlsx.py
```

- 資料來源 `tracker/task_progress.csv`（長表，一列＝某任務在某次會議的進度）
  ```
  編號,任務名稱,負責人,會議日期,狀態,本次進度
  ```
- 輸出 `output/excel/PMO任務追蹤表.xlsx`，一列一任務、各次會議進度並排
- 任務名稱、負責人、狀態取該任務**最近一次**會議的值
- 某次未討論者自動填「本次未討論」；任務成案前的欄位留白
- 狀態欄依「已完成／進行中／籌備中／暫緩」自動上色，欄位名稱要改就改腳本檔頭常數
