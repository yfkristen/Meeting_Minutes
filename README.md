# Meeting Minutes

將會議錄音逐字稿轉換為正式會議記錄的工作流程 repo。

## 使用方式

1. 在 Claude Code 對話中貼上會議逐字稿（或提供檔案）
2. Claude 依 `templates/` 的範本與 `reference/` 的定稿範例產出會議記錄
3. 逐字稿存於 `transcripts/`，產出的會議記錄存於 `minutes/`
4. 若對產出有修改，把最終版本提供給 Claude，它會存入 `reference/` 並更新範本，讓之後的產出越來越貼近你的格式

詳細流程規則見 [CLAUDE.md](CLAUDE.md)。
