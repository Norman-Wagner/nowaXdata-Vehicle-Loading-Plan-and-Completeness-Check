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
