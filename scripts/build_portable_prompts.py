#!/usr/bin/env python3
"""Build full and compact portable prompts from the skill source."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "nowaXdata-Vehicle-Loading-Plan-and-Completeness-Check"
SKILL = ROOT / "skills" / NAME
DIST = ROOT / "dist"
FULL = ("methodology.md", "load-plan-model.md", "inspections-and-defects.md", "safety-and-compliance.md", "privacy.md", "industry-examples.md")
COMPACT = ("load-plan-model.md", "safety-and-compliance.md", "privacy.md")

def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)

def make_portable(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\((?:references|assets)/([^)]+)\)", r"\1 (bundled resource: \2)", text)

def render(refs: tuple[str, ...], compact: bool) -> str:
    plugin = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    label = "Compact" if compact else "Full"
    parts = [f"# NOWA X Data – Vehicle Loading Plan and Completeness Check ({label} portable prompt)\n\n",
             "Use this as a system or project instruction. Higher-priority platform safety rules remain controlling.\n\n## Core instruction\n\n",
             make_portable(strip_frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))).strip()]
    for name in refs:
        parts += [f"\n\n---\n\n## Bundled reference: `{name}`\n\n", (SKILL / "references" / name).read_text(encoding="utf-8").strip()]
    parts += [f"\n\n---\n\nGenerated from {NAME}, version {plugin['version']}.\n"]
    return "".join(parts)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = {DIST / "portable-prompt.md": render(FULL, False), DIST / "portable-prompt-compact.md": render(COMPACT, True)}
    if args.check:
        stale = [p.relative_to(ROOT).as_posix() for p, c in expected.items() if not p.is_file() or p.read_text(encoding="utf-8") != c]
        if stale:
            print("Stale or missing generated files: " + ", ".join(stale), file=sys.stderr)
            return 1
        print("Portable prompts are current.")
        return 0
    DIST.mkdir(exist_ok=True)
    for path, content in expected.items():
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"Generated: {path.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
