# Five-dimension readiness model

This project uses an original decision model that keeps five questions separate. It is not derived from a vehicle manufacturer or commercial inventory product.

| Dimension | Question | Typical evidence |
| --- | --- | --- |
| Completeness | Is the target quantity present? | Count or controlled automatic detection |
| Condition | Is the item serviceable, clean, intact, and accessible? | Observable check and approved test method |
| Validity | Are expiry, inspection, maintenance, and calibration current? | Date and traceable record |
| Location | Is the item at its approved travel position and, where applicable, correctly stowed and retained? | Position code, specified retention indication, optional diagram/photo |
| Requirement evidence | Is the claimed obligation correctly classified and supported? | Source reference or approved internal standard |

## Dimension states

Use `pass`, `fail`, `not_applicable`, `not_checked`, or `unverified`. Preserve the reason and evidence for each dimension.

## Readiness result

- `ready`: every applicable dimension for every required position is `pass`.
- `ready_with_actions`: all release-critical dimensions pass, but non-critical replenishment or administrative actions remain. This status requires an approved organizational rule defining what is non-critical.
- `restricted`: at least one applicable dimension fails, but an authorized organizational rule permits restricted use with a recorded reason and limit.
- `not_ready`: a release-critical dimension fails or a required item was not checked.
- `undetermined`: critical applicability, source, competence, or check data is missing.

Never infer `ready` from total item count alone. Never invent which failures are release-critical. Require the organization to define criticality and approval roles.

## Decision output

Report the overall result, all five dimension results, blocking findings, open actions, unverified claims, plan version, check timestamp, and the organizational rule used for any override. Keep the raw findings so the overall result can be recalculated after a rule change.
