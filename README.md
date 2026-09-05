# Meeting Minutes

將會議錄音逐字稿轉換為正式會議記錄的工作流程 repo。

## 使用方式

1. 在 Claude Code 對話中貼上會議逐字稿（或提供檔案）
2. Claude 依 `templates/` 的範本與 `reference/` 的定稿範例產出會議記錄
3. 逐字稿存於 `transcripts/`（逐字稿），會議正式稿存於 `minutes/`（Markdown）
4. Claude 再由正式稿產出兩份交付檔：Word 會議紀錄與 Excel 個案進度表
5. 若對產出有修改，把最終版本提供給 Claude，它會存入 `reference/` 並更新範本，讓之後的產出越來越貼近你的格式

## 資料夾

| 資料夾 | 內容 |
| --- | --- |
| `transcripts/` | 會議逐字稿原文 |
| `minutes/` | 會議正式稿（Markdown，唯一事實來源） |
| `output/word/` | Word 會議紀錄 `.docx` |
| `output/excel/` | Excel 個案進度表 `.xlsx` |
| `reference/` | 已定稿的範例配對 |
| `templates/` | 會議記錄格式範本 |
| `scripts/` | Markdown → Word / Excel 產出腳本 |

## 手動產出交付檔

```bash
pip install python-docx openpyxl

# Word 會議紀錄 → output/word/
python3 scripts/md_to_docx.py minutes/2026-07-23_雙週會.md

# Excel 個案進度表 → output/excel/
python3 scripts/make_progress_xlsx.py minutes/2026-07-23_雙週會.md
```

內容有誤請改 `minutes/` 的 Markdown 再重跑腳本，不要直接改 Word/Excel，以免下次覆蓋。

詳細流程規則見 [CLAUDE.md](CLAUDE.md)。
