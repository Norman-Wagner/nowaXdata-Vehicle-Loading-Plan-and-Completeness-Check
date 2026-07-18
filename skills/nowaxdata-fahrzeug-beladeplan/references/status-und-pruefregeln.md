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
