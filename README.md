# nowaxdata Fahrzeug-Beladeplan

Herstellerneutraler Skill für digitale Fahrzeug-Beladepläne, Sollbeladungen und Vollzähligkeitskontrollen. Er unterstützt Planung und Prüfung, ersetzt aber weder Fuhrparkdisposition noch Rechts-, Sicherheits- oder Herstellerberatung.

## Architektur

- `skills/nowaxdata-fahrzeug-beladeplan/`: Skill, Referenzen und Vorlagen
- `.codex-plugin/plugin.json`: Codex-Plugin-Adapter
- `technical-sources.json`: Quellenregister ohne DIN-Volltexte
- `TECHNIKSTAND.md`: menschlicher Freigabeprozess
- `scripts/`, `tests/`, `dist/`: portable Prompts und Qualitätssicherung

DIN 75081:2019-06 wird ausschließlich referenziert. nowaxdata trennt rechtliche Pflicht, technische Norm, internen Standard und optionale Empfehlung. Quellenänderungen erzeugen eine Überprüfung, keine automatische Planänderung.