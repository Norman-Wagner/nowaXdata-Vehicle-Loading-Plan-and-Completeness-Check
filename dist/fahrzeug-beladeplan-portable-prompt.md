---
name: nowaxdata-fahrzeug-beladeplan
description: Plane, analysiere, implementiere oder prüfe in nowaxdata Fahrzeug-Beladepläne, Sollbeladungen, Fahrzeugausstattung, Vollzähligkeitskontrollen, Mindestbestände, Prüfintervalle, Kontrollprotokolle, Fahrzeugmängel und Nachbestellungen. Nutze diesen Skill auch für Vorlagen, Versionierung, QR-gestützte Fachkennungen und DIN-75081-Nachweisworkflows. Nicht verwenden für allgemeine Routenplanung, Fahrzeugkauf, Fahrtenbuchführung, Ortung, Fahrerüberwachung oder gewöhnliche Fahrzeugwartung ohne Bezug zu Beladung oder Vollständigkeit.
---

# nowaxdata Fahrzeug-Beladeplan

1. Analysiere zuerst die vorhandene nowaxdata-Struktur. Suche Module für Fahrzeuge, Inventar, Betriebsmittel, Prüfungen, Fristen, Aufgaben, Dokumente und Exporte. Wiederverwende sie; plane keine parallelen Register.
2. Lies vor fachlichen Entscheidungen die Dateien in `references/`. Nutze die Vorlagen in `assets/` für neue Dokumentation oder Druckausgaben.
3. Trenne jede Anforderung sichtbar in **rechtlich erforderlich**, **technische Norm / Branchenstandard**, **interner Standard** oder **optionale Empfehlung**. Erfinde keine Pflichtausstattung. Verifiziere aktuelle Rechts- oder Normbezüge mit Primärquellen; übernimm keine vollständigen DIN-Texte.
4. Erstelle vor jeder Implementierung einen konkreten Umsetzungsplan mit Wiederverwendung, Datenmigration, Berechtigungen, Audit, Exporten und Tests. Hole bei offenen Entscheidungen Rückmeldung ein.
5. Modellier Verantwortlichkeiten über Rollen und Geltungsbereiche, nicht über Klarnamen. Halte Planversionen und abgeschlossene Kontrollprotokolle unveränderbar. Aus Mängeln entstehen nach Bedarf Aufgaben; finale Priorität, Frist und Zuweisung bestimmt das Unternehmen.
6. Beachte Datenschutz- und Importschutzgrenzen. Keine Fall-, Angehörigen-, Verstorbenen- oder Mitarbeiterdaten in Beladeplänen, Fotos, QR-Inhalten oder Exportnamen.
7. Führe nach Änderungen vorhandene Tests, Typprüfung, Sicherheitsprüfung und Build aus. Berichte Dateien, Prüfungen, offene Punkte und Annahmen.

## Ressourcen

- `references/fachkonzept.md`: Umfang, Rollen, Abläufe und Normbezug.
- `references/datenmodell.md`: Entitäten, Beziehungen und Unveränderbarkeit.
- `references/status-und-pruefregeln.md`: Statuswerte, Fälligkeiten und Mängel.
- `references/datenschutzregeln.md`: Datenminimierung, Bilder, QR, Import und Export.
- `assets/`: Beladeplan-, Kontrollprotokoll- und Akzeptanzkriterienvorlage.


# Fachkonzept: Fahrzeug-Beladeplan und Vollzähligkeitskontrolle

Das Modul bildet die betriebliche Einsatzbereitschaft je Fahrzeug ab: individuelle Sollbeladung, feste Aufbewahrungsorte, Vollständigkeitskontrolle, Nachweise, Mängel und Folgeaufgaben. Es ergänzt den Fuhrpark; es ist keine Routenplanung, Ortungs-, Leistungs- oder Fahrtenbuchsoftware.

Jedes Fahrzeug kann einen eigenen Plan besitzen oder eine Vorlage seiner Fahrzeuggruppe übernehmen. Vorlagen und Pläne sind frei anpassbar. Ein Plan kann Bereiche und Unterbereiche enthalten, etwa `Fahrgastzelle > Mittelkonsole > unteres Fach`. Behälter wie Bestattungskoffer und Werkzeugtaschen können Unterlisten besitzen.

## Bausteine

- Fahrzeugprofil mit interner Bezeichnung, Art, Standort/Geltungsbereich, Status, Fuhrparkrolle, Plan und Nachweisakte.
- Aufbewahrungsorte mit Fachkennung, Beschreibung und optionaler Foto-/Skizzenreferenz.
- Positionen mit Soll- und Mindestbestand, Einheit, Pflichtkennzeichen, Zustand, Prüfung, Haltbarkeit und Ort.
- Frei konfigurierbare Kontrollarten: Einsatzbereitschaft, Regelkontrolle und anlassbezogene Kontrolle. NOWA setzt keine Rhythmen voraus.
- Kontrollprotokoll mit unveränderbarer Referenz auf die damalige Planversion.
- Mangel- und Aufgabenworkflow; eine Kontrolle darf mit Abweichungen abgeschlossen werden.
- Druckausgaben, QR-gestützte Fachkennungen und manuelle Alternativen ohne Hardware.

## Rollen und Quellen

Speichere Zuständigkeiten als Rolle oder Gruppe. Das Unternehmen entscheidet, wer Pläne erstellt, ändert, kontrolliert, Aufgaben schließt und Nachweise sieht. Vier-Augen-Freigabe ist optional.

Trenne rechtliche Pflicht, technische Norm/Branchenstandard, internen Standard und optionale Empfehlung. Für Bestattungskraftwagen kann ein Nachweisbereich zu DIN 75081:2019-06 geführt werden; vollständige Normtexte werden nicht übernommen. Speichere nur Referenz, Ausgabe, Geltungsgrund, Nachweis und abgeleiteten Prüfpunkt. Rechts- oder Normänderungen erzeugen eine Prüfaufgabe, ändern aber keinen Plan automatisch.

Eine Nachteinsatz-Nachbereitung kann optional für den nächsten Arbeitstag eine Aufgabe erzeugen. Fahrzeuggruppen, Auslöser, Fristen und Rollen bestimmt das Unternehmen. Die Umweltplakette ist ein anlassbezogener Fahrzeugnachweis ohne künstliche Jahresfrist und ohne GPS-Auswertung.


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


# Status- und Prüfregeln

| Objekt | Statuswerte |
| --- | --- |
| Fahrzeug | `aktiv`, `ausser_betrieb`, `archiviert` |
| Planvorlage/Planversion | `entwurf`, `aktiv`, `ersetzt`, `archiviert` |
| Kontrollposition | `nicht_geprueft`, `in_ordnung`, `abweichung`, `nicht_zutreffend` |
| Abweichung | `fehlt`, `teilweise_vorhanden`, `beschaedigt`, `verschmutzt`, `abgelaufen`, `pruefung_faellig`, `nachfuellung_erforderlich`, `falscher_ort`, `sonstige` |
| Kontrolle | `offen`, `in_bearbeitung`, `abgeschlossen_ohne_abweichung`, `abgeschlossen_mit_abweichungen`, `abgebrochen` |
| Feststellung | `offen`, `in_klaerung`, `massnahme_geplant`, `erledigt`, `nicht_zutreffend` |

1. Berechtigte Rolle wählt Fahrzeug und Kontrollart oder scannt eine neutrale Fachkennung.
2. Das System lädt nur die für diese Kontrolle geltenden Positionen der aktiven Planversion.
3. Jede Pflichtposition erhält ein Ergebnis. Menge, Zustand, Ort, Haltbarkeit oder Prüfgültigkeit werden nur abgefragt, wenn die Position es verlangt.
4. Bei Abweichung wird Mangelart gewählt; Bemerkung und Foto sind optional, sofern kein übernommener Standard anderes verlangt.
5. Die Kontrolle kann mit Abweichungen abgeschlossen werden; danach entsteht ein unveränderbares Protokoll.
6. NOWA kann Folgeaufgaben vorschlagen oder anlegen. Finale Priorität, Frist und Rolle bestimmt das Unternehmen.

Verwende nur unternehmenskonfigurierte oder mit Quelle belegte Fälligkeiten. Eskalationen sind konfigurierbar und kein Leistungsmonitoring. Rechts-, Norm- oder Herstelleränderungen erzeugen nur eine Überprüfungsaufgabe.


# Datenschutz- und Sicherheitsregeln

- Nie Angehörigen-, Verstorbenen-, Fall-, Gesundheits-, Einsatzort- oder Mitarbeiterleistungsdaten in Beladeplänen, Prüfungen, Bildern, QR-Codes oder Exporttiteln speichern.
- Rollen, Gruppen und interne Fachkennungen statt Klarnamen verwenden. Eine Akteur-ID im Audit ist nicht Teil des frei sichtbaren Protokolls.
- Keine GPS-Positionen, Routen, Geschwindigkeiten, Pausen oder privaten Fahrzeugbewegungen übernehmen.
- Fotos zeigen nur Lagerort oder Gegenstandsmangel: keine Personen, Dokumente, Kennzeichen von Sterbefällen, Codes, Fahrzeugpapiere oder private Gegenstände.
- Uploads nach bestehenden Regeln auf MIME-Type, Größe, Inhalt, Dateiname, Berechtigung und Speicherort prüfen. Keine frei ausführbaren HTML-, JavaScript- oder aktiven Office-Inhalte akzeptieren.
- QR-Codes tragen nur nicht erratbare technische Referenzen. Nach Scan sind Anmeldung und Fahrzeug-/Standortberechtigung nötig. Papier und manuelle Auswahl bleiben gleichwertig.
- Sicht- und Schreibrechte folgen Mandant, Standort/Geltungsbereich und Rolle. Dokumentreferenzen nutzen bestehende sichere Dokumentdienste und kopieren keine geschützten Normtexte.
- Exporte sind rollenberechtigt, datensparsam und auditiert. Abgeschlossene Kontrollen und Auditereignisse bleiben unveränderbar; Korrekturen sind ergänzende Folgehandlungen.

