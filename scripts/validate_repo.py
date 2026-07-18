import json,re,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];S=R/'skills/nowaxdata-fahrzeug-beladeplan';e=[]
p=json.loads((R/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
if p.get('name')!=R.name:e+=['Pluginname und Ordnername stimmen nicht überein']
if not re.fullmatch(r'\d+\.\d+\.\d+',str(p.get('version',''))):e+=['Pluginversion ist ungültig']
t=(S/'SKILL.md').read_text(encoding='utf-8')
if not re.match(r'\A---\s*\nname: nowaxdata-fahrzeug-beladeplan\n',t):e+=['Skill-Frontmatter ist ungültig']
if 'Routenplanung' not in t or 'Fahrtenbuch' not in t:e+=['Nicht-Auslöser fehlen']
s=json.loads((R/'technical-sources.json').read_text(encoding='utf-8'))['sources']
if len(s)<3 or any(not x['url'].startswith('https://') for x in s):e+=['Quellenregister ist unvollständig']
if subprocess.run([sys.executable,str(R/'scripts/build_portable_prompts.py'),'--check']).returncode:e+=['Portabler Prompt ist veraltet']
if e:print('\n'.join('FEHLER: '+x for x in e));raise SystemExit(1)
print('Repository-, Plugin- und Skill-Validierung bestanden.')