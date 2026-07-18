# Load plan model

## Core entities

| Entity | Required fields |
| --- | --- |
| Vehicle | `vehicle_id`, `type`, `purpose`, `status` |
| Plan | `plan_id`, `vehicle_id`, `version`, `effective_date`, `state` |
| Location | `position_id`, `parent_id`, `label`, `position_mode`, `stowed_state`, `deployed_state_optional`, `access_sequence`, `retention_check` |
| Mechanism | `mechanism_id`, `position_id`, `type`, `manufacturer_reference_optional`, `inspection_rule`, `functional_check`, `state` |
| Item | `item_id`, `label`, `category`, `unit`, `consumable` |
| Requirement | `plan_id`, `position_id`, `item_id`, `required_qty`, `minimum_qty`, `requirement_class`, `source_ref` |
| Item instance | `instance_id`, `item_id`, `serial_or_batch_optional`, `expiry_date`, `inspection_due` |
| Check | `check_id`, `plan_version`, `check_type`, `checked_at`, `checker_role` |
| Check result | `check_id`, `position_id`, `item_id`, `actual_qty`, `condition`, `status`, `note` |
| Defect/action | `action_id`, `result_id`, `action_type`, `priority`, `owner_role`, `due_date`, `state` |

## Validation rules

- IDs are unique, stable, and non-personal.
- `required_qty >= 0`; `0 <= minimum_qty <= required_qty` unless a documented business rule explains otherwise.
- Quantity uses a controlled unit vocabulary.
- Dates use `YYYY-MM-DD`; timestamps use ISO 8601 with time zone.
- A requirement marked `LAW`, `TECH`, `AIF`, `MFR`, or `CERT` has a non-empty source reference.
- A movable position defines its safe stowed state, observable retention check, and applicable functional-check source.
- Load limits, operating sequences, powered-mechanism tests, and locking requirements are never guessed; they require the applicable manufacturer or technical source.
- A check result points to the exact plan version used.
- Changes append audit events; they do not overwrite historic checks.

## Deterministic status order

Apply the most serious applicable state and preserve secondary findings:

1. `not_checked`
2. `unsafe_or_blocked`
3. `expired`
4. `inspection_due`
5. `damaged`
6. `dirty`
7. `missing`
8. `below_minimum`
9. `misplaced`
10. `complete`

Suggested quantity logic: actual quantity `0` with required quantity above `0` is `missing`; actual below minimum is `below_minimum`; actual at or above minimum but below target is `replenish_to_target`; otherwise quantity is complete.

## Software acceptance examples

- Given a plan version and vehicle, when a checker records all rows, then the system produces an immutable completion record linked to that version.
- Given an expired item, when the check is closed, then the system cannot label the vehicle fully operational without an authorized override and reason.
- Given a CSV import with an unknown position, then the import rejects the row and reports its line number without partially hiding the error.
- Given a plan update, then historic checks continue to render with the former version.
- Given equipment stored in a movable mechanism, when a vehicle check is completed, then the result records both item presence and the mechanism's approved stowed/retained state.
