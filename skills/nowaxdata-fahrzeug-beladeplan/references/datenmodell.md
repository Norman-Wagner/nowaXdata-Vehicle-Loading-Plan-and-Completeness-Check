# Datenmodell

| Entität | Kernfelder | Regeln |
| --- | --- | --- |
| `Vehicle` | interne Bezeichnung, Art, Hersteller/Modell, Kennzeichen, Standort-/Geltungsbereich, Status, verantwortliche Rolle | keine Fahrerüberwachung |
| `VehicleEvidence` | Fahrzeug-ID, Typ, Quelle, Aussteller, Datum, Gültigkeit, Dokumentreferenz, Prüfstatus | Zulassung, Umbau, Normen, Umweltplakette |
| `LoadingPlanTemplate` | Name, Fahrzeuggruppe, Version, Status, Herkunft | Vorlage gilt nicht automatisch |
| `LoadingPlan` | Fahrzeug-ID, Version, Status, Herkunft, gültig ab, Erstellerrolle | Änderung erzeugt neue Version |
| `StorageLocation` | Plan-ID, Kennung, Name, Elternort, Reihenfolge, Foto-/Skizzenreferenz | QR enthält nur nicht erratbare Referenz |
| `LoadingItem` | Planversion-ID, Positionsnummer, Bezeichnung, Kategorie, Ort-ID, Soll-/Mindestmenge, Einheit, Pflichtstatus, Prüfregel | kann Container mit Unterpositionen sein |
| `InspectionDefinition` | Planversion-ID, Kontrollart, Auslöser/Rhythmus, berechtigte Rollen | keine vorgegebene Frequenz |
| `Inspection` | Fahrzeug-ID, Planversion-ID, Kontrollart, Zeiten, Ergebnis, prüfende Rolle | nach Abschluss unveränderbar |
| `InspectionItemResult` | Kontrolle-ID, Position-ID, Ergebnis, Menge, Mangelart, Bemerkung, Bildreferenz | keine sensiblen Falldaten |
| `VehicleFinding` | Quelle, Fahrzeug-ID, Position-ID, Status, Prioritätsvorschlag, Folgeaufgabe | finale Entscheidung beim Unternehmen |

- Ein Fahrzeug hat genau einen aktiven Plan; Kontrollen referenzieren konkrete Planversionen.
- Pflichtpositionen brauchen ein Ergebnis. Abweichung blockiert nicht, kann Folgeaufgaben auslösen.
- Referenzierte Objekte werden archiviert statt gelöscht.
- Audit enthält Akteur-ID, Rolle, Zeit, Aktion, Objektversion und begründete Änderung.
- Prüfe und verwende bestehende Dokument-, Fristen-, Aufgaben-, Export-, Standortrechte- und Auditmodule.
