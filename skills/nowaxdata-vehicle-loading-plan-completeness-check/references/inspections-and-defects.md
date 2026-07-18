# Inspections and defects

## Observable condition vocabulary

Use `serviceable`, `damaged`, `dirty`, `wet`, `opened`, `seal_broken`, `expired`, `inspection_due`, `misplaced`, `inaccessible`, `not_stowed`, `not_retained`, `mechanism_fault`, or `not_checked`. Add a short factual note; avoid blame.

## Defect record

Capture defect ID, vehicle ID, plan version, position and item IDs, detected time, checker role, factual observation, operational effect, immediate containment, required action, owner role, due date, priority, state, and closure evidence.

## Action routing

| Finding | Typical action class |
| --- | --- |
| Missing or below minimum | Replenish or reorder |
| Damaged | Isolate if needed; repair or replace |
| Dirty/contaminated | Remove from use if needed; clean under approved process |
| Expired | Isolate; replace; dispose under applicable rule |
| Inspection due | Schedule competent inspection; restrict use if required |
| Misplaced | Restore fixed location and verify accessibility |
| Not stowed or not retained | Place in approved travel state; verify the specified locking or retention indication |
| Mechanism fault | Stop improvised operation; follow the approved instruction and route inspection or repair to the competent role |
| Unsafe or unclear | Stop recommendation; escalate to competent role |

Do not decide operational release solely from a generic checklist where regulation, manufacturer instructions, or organizational authority require a competent person.

## Handover

A handover record should state vehicle ID, plan version, time, releasing role, receiving role, open defects, restricted-use decision, keys/devices transferred without secret codes, and acknowledgement. Names and signatures are optional organizational additions, not default skill fields.
