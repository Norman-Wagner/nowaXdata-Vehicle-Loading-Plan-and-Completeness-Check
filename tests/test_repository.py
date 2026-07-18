import json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class T(unittest.TestCase):
 def test_cases(self):
  c=json.loads((R/'tests/cases.json').read_text());self.assertTrue(any(x['expect_trigger'] for x in c));self.assertTrue(any(not x['expect_trigger'] for x in c))