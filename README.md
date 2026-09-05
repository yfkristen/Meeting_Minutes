# Meeting Minutes

金控AI推動委員會 PMO 例會的會議紀錄產出流程 repo。
一份逐字稿進來，產出 **Word 會議紀錄** 與 **Excel 任務追蹤表**。

## 使用方式

在 Claude Code 對話中貼上逐字稿即可，Claude 會依 `.claude/skills/ai-pmo-meeting-minutes/`
的規則撰寫，並自動產出兩份交付檔。詳細流程見 [CLAUDE.md](CLAUDE.md)。

## 資料夾

| 資料夾 | 內容 |
| --- | --- |
| `transcripts/` | 會議逐字稿原文 |
| `minutes/` | 會議紀錄本體（Markdown，唯一事實來源） |
| `tracker/` | 任務追蹤表資料來源（長表 CSV） |
| `output/word/` | Word 會議紀錄 `.docx` |
| `output/excel/` | Excel 任務追蹤表 `.xlsx` |
| `reference/` | 歷次定稿的配對存檔 |
| `templates/` | 會議紀錄格式範本 |
| `scripts/` | 產出與打包腳本 |
| `docs/` | skill 維護說明 |
| `.claude/skills/` | ai-pmo-meeting-minutes skill 本體 |

## 手動產出

```bash
pip install python-docx openpyxl

# Word 會議紀錄 → output/word/（加 --email 可連郵件套語一起輸出）
python3 scripts/md_to_docx.py minutes/2026-07-23_雙週會.md

# Excel 任務追蹤表 → output/excel/PMO任務追蹤表.xlsx
python3 scripts/make_tracker_xlsx.py

# 把 skill 打包成可上傳 claude.ai 的 .skill 檔
bash scripts/pack_skill.sh
```

內容有誤請改 `minutes/` 的 Markdown 或 `tracker/` 的 CSV 再重跑腳本，
不要直接改 Word / Excel，以免下次被覆蓋。

## skill

撰寫規則全部集中在 `.claude/skills/ai-pmo-meeting-minutes/`，隨每場會議的定稿回饋累積。
更新後要重新打包上傳 claude.ai 才會生效，見 [docs/skill維護說明.md](docs/skill維護說明.md)。
