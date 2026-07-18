#!/usr/bin/env python3
"""Offline structural and content validation."""

from __future__ import annotations

import csv
import io
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "nowaxdata-vehicle-loading-plan-completeness-check"
SKILL = ROOT / "skills" / NAME

def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    values = {}
    if match:
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                values[key.strip()] = value.strip().strip("\"'")
    return values

def main() -> int:
    errors: list[str] = []
    required = ["README.md", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md", "LICENSE.txt", "NOTICE.txt", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".github/dependabot.yml", ".github/workflows/validate.yml", ".github/workflows/release.yml", "tests/cases.json"]
    for rel in required:
        if not (ROOT / rel).is_file(): errors.append(f"Missing: {rel}")
    plugin = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    if plugin.get("name") != NAME: errors.append("Plugin name is not the required exact name")
    if not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")): errors.append("Plugin version is not semantic")
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    meta = frontmatter(text)
    if set(meta) != {"name", "description"}: errors.append("SKILL frontmatter must contain only name and description")
    if meta.get("name") != NAME or SKILL.name != NAME: errors.append("Skill name or folder does not match exact required name")
    if len(text.splitlines()) > 500: errors.append("SKILL.md exceeds 500 lines")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", NAME): errors.append("Skill name violates the open Agent Skills standard")
    claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if claude.get("name") != NAME: errors.append("Claude plugin and skill name differ")
    refs = {"methodology.md", "quality-principles.md", "load-plan-model.md", "readiness-model.md", "inspections-and-defects.md", "safety-and-compliance.md", "germany-funeral-vehicle-routing.md", "privacy.md", "industry-examples.md"}
    if {p.name for p in (SKILL / "references").glob("*.md")} != refs: errors.append("Reference file set differs")
    cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))
    if len(cases) < 15 or not any(not c["expect_trigger"] for c in cases): errors.append("Trigger tests are insufficient")
    if not any(c.get("expect_privacy_gate") for c in cases): errors.append("Privacy gate test missing")
    if not any(c.get("expect_safety_gate") for c in cases): errors.append("Safety gate test missing")
    if not any(c.get("expect_jurisdiction_route") for c in cases): errors.append("Jurisdiction routing test missing")
    if not any(c.get("expect_scope_gate") for c in cases): errors.append("Special-vehicle scope test missing")
    if not any(c.get("expect_certification_gate") for c in cases): errors.append("Certification scope test missing")
    csv_text = (SKILL / "assets/inventory-import.csv").read_text(encoding="utf-8")
    rows = list(csv.DictReader(io.StringIO(csv_text)))
    if not rows or "position_id" not in rows[0] or "requirement_class" not in rows[0]: errors.append("CSV template is invalid")
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".yml", ".py", ".csv"}:
            data = path.read_text(encoding="utf-8")
            if re.search(r"\bTODO\b|\[PLACEHOLDER\]", data, re.I): errors.append(f"Unresolved placeholder: {path.relative_to(ROOT)}")
    generated = subprocess.run([sys.executable, str(ROOT / "scripts/build_portable_prompts.py"), "--check"], cwd=ROOT, capture_output=True, text=True)
    if generated.returncode: errors.append(generated.stderr.strip() or "Portable prompts stale")
    if errors:
        for item in errors: print("ERROR: " + item)
        return 1
    print("Repository, plugin, skill, templates, and tests validated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
