# Germany: funeral-vehicle source routing

Use this reference only for German funeral vehicles and transport scenarios involving deceased persons. It is a research and classification workflow, not legal advice and not a list of mandatory equipment.

## First determine the scenario

Record before assessing any obligation:

- vehicle type, body conversion, approval state, and intended use;
- whether the journey concerns a deceased person, ashes/urns, equipment only, or another task;
- origin state, destination state, and every transit state;
- domestic, cross-border, recovery, transfer, ceremonial, or other operating scenario;
- operator type, responsible authority, and date of the planned or completed journey.

Do not assume that every rule of every transit state applies. Include each potentially relevant jurisdiction in the research queue, then document applicability or non-applicability with a current official source.

## Source order

1. Current official law portal for every potentially relevant German state.
2. State funeral act, implementing regulation, administrative provision, official guidance, and competent-health-authority requirements.
3. Applicable federal road-traffic, vehicle, occupational-safety, dangerous-goods, and transport rules.
4. Current technical rules and standards, including DIN 75081 where the vehicle and use are within scope.
5. Accident-insurance rules and sector guidance applicable to the organization and activity.
6. Approval documents and instructions for the base vehicle, body conversion, securing system, lifting/sliding mechanisms, and installed equipment.
7. Contractual specifications and the organization's approved internal standards.

## Sixteen-state research gate

Use the following as a routing checklist, not as a claim that all sixteen legal systems apply to one journey:

`Baden-Württemberg`, `Bayern`, `Berlin`, `Brandenburg`, `Bremen`, `Hamburg`, `Hessen`, `Mecklenburg-Vorpommern`, `Niedersachsen`, `Nordrhein-Westfalen`, `Rheinland-Pfalz`, `Saarland`, `Sachsen`, `Sachsen-Anhalt`, `Schleswig-Holstein`, `Thüringen`.

For each state in scope, record:

`jurisdiction`, `official_portal`, `act_or_regulation`, `exact_section`, `version_or_effective_date`, `access_date`, `scenario`, `applicability`, `requirement_class`, `verified_by_role`, `open_question`.

Never invent a section number. If the current official text has not been checked, set `requirement_class=UNV` and create a verification task.

## DIN 75081

DIN Media lists `DIN 75081:2019-06`, *Straßenfahrzeuge – Bestattungskraftwagen*, as current at the access date 2026-07-18. The published scope describes requirements and tests for manufacturers of hearses in addition to statutory provisions. The revision metadata also identifies updated normative references concerning load securing.

Treat this as a potentially central technical source for vehicle construction, testing, installed systems, and interfaces. Do not treat it as an automatically binding nationwide inventory list. Determine whether relevance follows from law, recognized technical practice, approval, contract, procurement specification, manufacturer documentation, or an internal standard.

The standard text is copyrighted and normally requires licensed access. Do not reproduce, reconstruct, or guess its clauses, dimensions, tests, or equipment requirements. Record only verified metadata and conclusions supported by an authorized copy. Source: DIN Media, <https://www.dinmedia.de/de/norm/din-75081/303385490>.

## Verified examples showing state variation

- **Sachsen:** Section 17 of the Saxon Funeral Act links road transport of deceased persons to vehicles equipped for that purpose and minimum requirements under recognized technical rules. This supports a technical-rule check but does not establish that DIN 75081 is the only applicable rule. Re-check the current official text before use: <https://www.revosax.sachsen.de/vorschrift/4526-Saechsisches-Bestattungsgesetz>.
- **Bayern:** Section 13 of the Bavarian Funeral Regulation contains express vehicle-use and construction requirements. This demonstrates that detailed requirements may sit in an implementing regulation rather than only in the funeral act. Re-check the effective version and exceptions before use: <https://www.gesetze-bayern.de/Content/Document/BayBestV-13>.

These examples are research signposts, not a complete legal assessment and not transferable to another state.

## Output rule

Separate the final result into:

- `LAW`: verified statutory or regulatory duty for the exact scenario;
- `TECH`: verified technical rule or standard;
- `ACC`: applicable accident-insurance rule or guidance;
- `MFR`: manufacturer or body-converter instruction;
- `INT`: approved internal or contractual standard;
- `REC`: optional recommendation;
- `UNV`: not yet verified.

State which source supports the presence of an item and which source supports its location, retention for travel, condition, inspection, cleaning, or documentation. One source must not silently stand in for another requirement.
