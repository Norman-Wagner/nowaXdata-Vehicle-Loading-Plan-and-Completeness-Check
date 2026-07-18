from pathlib import Path
import argparse
R=Path(__file__).resolve().parents[1]; S=R/'skills/nowaxdata-fahrzeug-beladeplan'; O=R/'dist/fahrzeug-beladeplan-portable-prompt.md'
def content(): return '\n\n'.join((S/x).read_text(encoding='utf-8') for x in ['SKILL.md','references/fachkonzept.md','references/datenmodell.md','references/status-und-pruefregeln.md','references/datenschutzregeln.md'])+'\n'
p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();v=content()
if a.check: raise SystemExit(0 if O.is_file() and O.read_text(encoding='utf-8')==v else 1)
O.parent.mkdir(exist_ok=True);O.write_text(v,encoding='utf-8')