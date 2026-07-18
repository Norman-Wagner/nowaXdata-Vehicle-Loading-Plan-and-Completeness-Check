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
