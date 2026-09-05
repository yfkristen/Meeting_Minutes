#!/usr/bin/env python3
"""將 minutes/ 的會議記錄 Markdown 轉成 Word (.docx)。

用法:
    python3 scripts/md_to_docx.py minutes/2026-07-23_雙週會.md
    python3 scripts/md_to_docx.py minutes/2026-07-23_雙週會.md -o output/word/自訂檔名.docx

輸出預設為 output/word/<原檔名>_會議紀錄.docx
"""

import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

# ---- 版面設定（要換字型/字級改這裡即可）----
CN_FONT = "標楷體"          # 中文字型
EN_FONT = "Times New Roman"  # 英數字型
BODY_SIZE = Pt(12)
LINE_SPACING = 1.5

LEVEL1 = re.compile(r"^([壹貳參肆伍陸柒捌玖拾]+、)")          # 壹、貳、參
LEVEL2 = re.compile(r"^([一二三四五六七八九十]+、)")           # 一、二、三
LEVEL3 = re.compile(r"^(\d+\.)\s*")                            # 1. 2. 3.


def set_run_font(run, bold=False, size=BODY_SIZE):
    run.bold = bold
    run.font.size = size
    run.font.name = EN_FONT
    run._element.rPr.rFonts.set(qn("w:eastAsia"), CN_FONT)


def add_para(doc, text, *, bold=False, indent_cm=0.0, hanging_cm=0.0,
             space_before=0, space_after=6):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = LINE_SPACING
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.left_indent = Cm(indent_cm + hanging_cm)
    if hanging_cm:
        pf.first_line_indent = Cm(-hanging_cm)
    run = p.add_run(text)
    set_run_font(run, bold=bold)
    return p


def build(md_path: Path, out_path: Path) -> Path:
    lines = md_path.read_text(encoding="utf-8").splitlines()

    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21.0), Cm(29.7)
    section.top_margin = section.bottom_margin = Cm(2.54)
    section.left_margin = section.right_margin = Cm(2.2)

    normal = doc.styles["Normal"]
    normal.font.name = EN_FONT
    normal.font.size = BODY_SIZE
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), CN_FONT)

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        # 略過範本說明與水平線
        if stripped.startswith(">") or stripped == "---":
            continue

        if not stripped:                       # 空行 → 段落間距
            add_para(doc, "", space_after=0)
            continue

        if LEVEL1.match(stripped):             # 壹、貳、參
            add_para(doc, stripped, bold=True, hanging_cm=1.2, space_before=6)
        elif LEVEL2.match(stripped):           # 一、二、三
            add_para(doc, stripped, indent_cm=0.85, hanging_cm=1.2)
        elif LEVEL3.match(stripped):           # 1. 2. 3.
            add_para(doc, stripped, indent_cm=1.7, hanging_cm=0.9)
        else:                                  # 稱謂、前言、結語
            add_para(doc, stripped)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser(description="會議記錄 Markdown → Word")
    ap.add_argument("markdown", help="minutes/ 底下的會議記錄 .md")
    ap.add_argument("-o", "--output", help="輸出 .docx 路徑")
    args = ap.parse_args()

    md_path = Path(args.markdown)
    if not md_path.is_file():
        print(f"找不到檔案：{md_path}", file=sys.stderr)
        return 1

    out_path = Path(args.output) if args.output else \
        Path("output/word") / f"{md_path.stem}_會議紀錄.docx"

    print(f"已產出：{build(md_path, out_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
