# NOWA X Data – Vehicle Loading Plan and Completeness Check

Public, manufacturer-neutral AI skill for vehicle load plans, fixed storage positions, completeness checks, defects, replenishment, inspection dates, printable forms, and digital data models.

Developed by **Norman Wagner / WagnerConnect** as part of **NOWA X Data**. Website: [nowaxdata.de](https://nowaxdata.de)

## Purpose

Designed in Germany for dependable vehicle readiness. The project translates a tradition of precise vehicle engineering, repeatable inspection, clear responsibility, and traceable documentation into an open AI workflow. Quality is demonstrated through deterministic checks and transparent evidence, not through unsupported superiority claims.

Suitable for funeral services, trade fleets, care services, aid organizations, municipal vehicles, event logistics, field service, security services, and other vehicles with defined equipment. Examples are structural only and are not universal lists of legally required equipment.

## Outputs

- load plan and position register
- target/actual and minimum-stock checklist
- completeness and handover record
- defect, repair, refill, and reorder lists
- inspection and expiry overview
- printable Markdown templates and CSV import
- data model, application requirements, and acceptance criteria

## Use

| Environment | Method |
| --- | --- |
| OpenAI/Codex-compatible plugin | Use `.codex-plugin/plugin.json` and `skills/` |
| Agent Skills-compatible system | Install `skills/nowaxdata-vehicle-loading-plan-completeness-check` |
| Claude Code | Add this repository as a plugin marketplace or copy the common skill folder into `.claude/skills/` |
| Other AI systems | Use `dist/portable-prompt.md` or the compact variant |

Codex invocation: `$nowaxdata-vehicle-loading-plan-completeness-check`  
Claude Code invocation: `/nowaxdata-vehicle-loading-plan-completeness-check`

Mandatory claims require current applicable evidence. The skill does not invent duties, intervals, limits, or storage instructions. Regulated or hazardous items require competent guidance. Roles and internal IDs are preferred over personal data.

## Validation

```bash
python scripts/build_portable_prompts.py --check
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

## One core, several adapters

The public repository keeps its established name. The machine-readable skill and plugin identifier is `nowaxdata-vehicle-loading-plan-completeness-check` because the open Agent Skills standard requires lowercase letters, numbers, and hyphens. The human-facing brand remains **NOWA X Data – Vehicle Loading Plan and Completeness Check**.

The same `SKILL.md` and references form the common core. `.codex-plugin/` provides the ChatGPT/Codex adapter, `.claude-plugin/` provides Claude Code metadata, and `dist/` covers systems that accept only portable instructions.

Licensed under Apache License 2.0. No trademark rights are granted in **NOWA X**, **NOWA X Data**, or **WagnerConnect**.
