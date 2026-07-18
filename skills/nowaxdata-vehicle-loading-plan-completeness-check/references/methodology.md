# Methodology

## 1. Scope

Define the vehicle, mission, jurisdiction, operating conditions, shift model, check frequency, and exclusions. Use an internal vehicle ID instead of registration data where possible.

## 2. Location hierarchy

Model locations from large to small: vehicle → zone → compartment → mechanism or container → position. Assign durable codes such as `R-CAB-D02-P03`. Never reuse a retired code without recording the change.

Classify the position as `fixed`, `movable`, `removable_module`, or `mission_specific`. For a movable location, distinguish the approved stowed position from its deployed working position. Record the access sequence and retention or locking check without inventing technical limits.

## 3. Requirement classes

| Code | Class | Evidence needed |
| --- | --- | --- |
| LAW | Statutory requirement | Current official legal source and applicability |
| TECH | Technical rule or standard | Exact rule, edition, scope, access status |
| AIF | Accident-insurance rule | Competent institution, rule, edition, scope |
| MFR | Manufacturer instruction | Product/vehicle manual and revision |
| CERT | Certification or quality-mark requirement | Program owner, current program/version, certificate scope, auditor or certification evidence |
| INT | Internal company standard | Approved internal rule and owner role |
| OPT | Optional recommendation | Clear reason; never presented as mandatory |
| UNV | Unverified claim | Verification task before approval |

## 4. Inventory design

Give every item a stable ID. Separate target quantity from minimum stock. Set minimum stock only for replenishable material. Define acceptable condition in observable terms. Link inspection and expiry dates to the item instance when individual units differ.

## 5. Check cycle

Use event-based checks where useful: start of shift, vehicle handover, after use, after replenishment, after repair, after cleaning, before a special mission, and periodic audit. The organization decides frequency based on evidence and risk.

## 6. Version control

Record version, effective date, change summary, changed position/item IDs, approving role, and replaced version. Printed copies need a visible version and a warning when uncontrolled.

## 7. Output review

Confirm location uniqueness, stowed/deployed state where relevant, retention check, unit consistency, source classification, certification scope where relevant, open verification tasks, minimum-stock logic, date validity, safe storage escalation, and absence of unnecessary personal data.
