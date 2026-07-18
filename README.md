# NOWA X Data – Vehicle Loading Plan and Completeness Check

Public, manufacturer-neutral AI skill for vehicle load plans, fixed storage positions, completeness checks, defects, replenishment, inspection dates, printable forms, and digital data models.

Developed by **Norman Wagner / WagnerConnect** as part of **NOWA X Data**. Website: [nowaxdata.de](https://nowaxdata.de)

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
| Agent Skills-compatible system | Install `skills/nowaXdata-Vehicle-Loading-Plan-and-Completeness-Check` |
| Other AI systems | Use `dist/portable-prompt.md` or the compact variant |

Direct invocation: `$nowaXdata-Vehicle-Loading-Plan-and-Completeness-Check`

Mandatory claims require current applicable evidence. The skill does not invent duties, intervals, limits, or storage instructions. Regulated or hazardous items require competent guidance. Roles and internal IDs are preferred over personal data.

## Validation

```bash
python scripts/build_portable_prompts.py --check
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

## Compatibility note

The publisher-required exact name contains uppercase letters. Some OpenAI/Codex validators currently require lowercase skill names and may reject the adapter. Portable prompts remain usable.

Licensed under Apache License 2.0. No trademark rights are granted in **NOWA X**, **NOWA X Data**, or **WagnerConnect**.
