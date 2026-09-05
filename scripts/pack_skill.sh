#!/usr/bin/env bash
# 將 .claude/skills/ai-pmo-meeting-minutes/ 壓成可上傳 claude.ai 的 .skill 檔。
#
# 用法：bash scripts/pack_skill.sh
# 產出：output/ai-pmo-meeting-minutes.skill
#
# zip 內會保留最外層的 ai-pmo-meeting-minutes/ 目錄，符合 claude.ai 的要求。

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="$REPO_ROOT/.claude/skills"
SKILL_NAME="ai-pmo-meeting-minutes"
OUT="$REPO_ROOT/output/$SKILL_NAME.skill"

if [ ! -f "$SKILL_DIR/$SKILL_NAME/SKILL.md" ]; then
  echo "找不到 $SKILL_DIR/$SKILL_NAME/SKILL.md" >&2
  exit 1
fi

mkdir -p "$REPO_ROOT/output"
rm -f "$OUT"
(cd "$SKILL_DIR" && zip -q -r "$OUT" "$SKILL_NAME" -x '*.DS_Store' '__MACOSX/*')

echo "已產出：$OUT"
unzip -l "$OUT" | sed -n '4,20p'
echo
echo "上傳方式：claude.ai →「設定」→「Skills」→「新增」→「上傳技能」"
