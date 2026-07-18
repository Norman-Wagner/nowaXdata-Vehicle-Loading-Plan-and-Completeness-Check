from __future__ import annotations
import argparse,json
from datetime import date
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--report',required=True);a=p.parse_args()
s=json.loads((R/'technical-sources.json').read_text(encoding='utf-8'))['sources']
Path(a.report).write_text('# Technischer Quellenbericht\n\nStand: '+date.today().isoformat()+'\n\n'+''.join('- '+x['id']+': registriert\n' for x in s),encoding='utf-8')