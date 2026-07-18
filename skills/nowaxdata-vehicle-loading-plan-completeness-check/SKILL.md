---
name: nowaxdata-vehicle-loading-plan-completeness-check
description: Create, review, digitize, and maintain manufacturer-neutral vehicle loading plans, fixed-location inventories, completeness checks, minimum-stock controls, inspection schedules, expiry tracking, defect reports, replenishment lists, handover records, printable checklists, CSV templates, data models, web-application requirements, and acceptance criteria. Use for fleet vehicles, service vans, hearses, care services, emergency or aid vehicles, municipal fleets, event logistics, security services, workshops, field service, or any vehicle with defined equipment. Do not use for ordinary packing lists without a vehicle, general warehouse inventory, travel packing, or legal advice unrelated to vehicle equipment.
---

# Vehicle loading plan and completeness check

## Core workflow

1. Establish vehicle identity without personal data: internal vehicle ID, vehicle type, use, operating environment, and plan version.
2. Ask only for missing facts that materially affect the result. Never invent mandatory equipment, quantities, intervals, expiry dates, load limits, or storage rules.
3. Map vehicle zones, compartments, containers, shelves, drawers, and fixed position codes before listing items.
4. Classify every requirement source as `law`, `technical rule`, `accident-insurance rule`, `manufacturer instruction`, `internal standard`, or `optional recommendation`.
5. Record each item with unique item ID, fixed position, target quantity, minimum stock, unit, permanence/consumable type, condition criteria, and applicable dates.
6. Separate structural equipment, reusable equipment, consumables, regulated goods, personal protective equipment, documents, and optional additions.
7. Calculate status without hiding ambiguity: complete, below minimum, missing, damaged, dirty, expired, inspection due, misplaced, blocked, or not checked.
8. Evaluate five independent readiness dimensions: completeness, condition, validity, correct location, and requirement evidence. Never hide a failed dimension behind one overall green status.
9. Produce the requested output and include plan version, effective date, scope, unresolved assumptions, evidence status, and change history.
10. Use roles instead of personal names for responsibility. Exclude customer, patient, case, health, private-contact, and confidential identifiers.
11. For heavy, hazardous, infectious, flammable, pressurized, temperature-sensitive, or otherwise regulated items, stop short of prescribing storage. Require current competent guidance, manufacturer instructions, load-securing rules, and applicable law.

## Evidence and obligation gate

- Never label an item or interval legally required without a current, traceable source applicable to the jurisdiction, vehicle, use, and date.
- Mark unsupported claims as `unverified`, `internal standard`, or `recommendation`.
- Distinguish what must be carried from how it must be stored, inspected, secured, cleaned, or documented.
- If the user asks for legal certainty, state the limits and request authoritative sources or specialist review.

Read [methodology.md](references/methodology.md) for the planning sequence and identifiers. Read [load-plan-model.md](references/load-plan-model.md) for schemas and calculations. Read [inspections-and-defects.md](references/inspections-and-defects.md) for status logic and corrective actions. Read [safety-and-compliance.md](references/safety-and-compliance.md) whenever regulated or safety-relevant equipment appears. Read [privacy.md](references/privacy.md) when photos, logs, handovers, or assigned people are involved. Read [industry-examples.md](references/industry-examples.md) only for neutral examples, never as a source of mandatory equipment.

Read [readiness-model.md](references/readiness-model.md) whenever the user asks whether a vehicle is ready, operational, complete, releasable, or safe to deploy.

Apply [quality-principles.md](references/quality-principles.md) when designing plans, templates, data models, interfaces, or software acceptance criteria.

Read [germany-funeral-vehicle-routing.md](references/germany-funeral-vehicle-routing.md) whenever a German hearse, funeral vehicle, transport of deceased persons, DIN 75081, or German state funeral law is in scope. Route the check by all potentially relevant German states and the actual transport scenario; do not turn a technical standard or an example from one state into a nationwide equipment duty.

For police, fire, rescue, civil-protection, recovery, municipal, or other special-purpose vehicles, use public procurement specifications and official equipment concepts only as vehicle-class-specific evidence or design research. Never generalize their equipment to another organization, vehicle class, or mission without a separate applicable source.

## Output contract

Prefer tables for exact mappings. Use one row per item-position combination. At minimum include:

`position_id`, `item_id`, `item`, `category`, `required_qty`, `minimum_qty`, `actual_qty`, `unit`, `condition`, `expiry_or_due`, `requirement_class`, `source`, `status`, `action`.

For a new plan, return:

1. scope and assumptions;
2. vehicle-zone and position register;
3. load plan;
4. completeness checklist;
5. defects, replenishment, repair, and inspection actions;
6. version and approval fields;
7. unresolved evidence or safety questions.

For software requirements, also define stable identifiers, data types, validation rules, audit events, roles, imports/exports, offline behavior, and acceptance criteria. Do not use employee names as keys.

## Bundled assets

- Copy and adapt [vehicle-load-plan-template.md](assets/vehicle-load-plan-template.md) for a printable plan.
- Copy and adapt [completeness-checklist.md](assets/completeness-checklist.md) for routine checks.
- Copy and adapt [defect-report.md](assets/defect-report.md) for defects and corrective actions.
- Use [inventory-import.csv](assets/inventory-import.csv) as the machine-readable import header and example.

## Quality check

Before finishing, verify that every item has a fixed position or an explicit `mobile/mission-specific` designation; every mandatory claim has a source; quantities and units are present; dates are ISO 8601 where practical; status follows the shared vocabulary; personal data is absent; regulated storage has not been guessed; and all assumptions and unverified points are visible.
