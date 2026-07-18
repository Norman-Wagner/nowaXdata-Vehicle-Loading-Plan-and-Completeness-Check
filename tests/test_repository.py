import csv, io, json, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "nowaXdata-Vehicle-Loading-Plan-and-Completeness-Check"

class RepositoryTests(unittest.TestCase):
    def test_trigger_mix(self):
        cases = json.loads((ROOT / "tests/cases.json").read_text())
        self.assertGreaterEqual(sum(c["expect_trigger"] for c in cases), 10)
        self.assertGreaterEqual(sum(not c["expect_trigger"] for c in cases), 5)
    def test_exact_name(self):
        skill = ROOT / "skills" / NAME / "SKILL.md"
        self.assertTrue(skill.is_file())
        self.assertIn(f"name: {NAME}", skill.read_text())
    def test_csv_columns_are_unique(self):
        data = (ROOT / "skills" / NAME / "assets/inventory-import.csv").read_text()
        header = next(csv.reader(io.StringIO(data)))
        self.assertEqual(len(header), len(set(header)))
    def test_no_person_data_in_cases(self):
        text = (ROOT / "tests/cases.json").read_text().lower()
        for forbidden in ("@", "telefon", "straße", "geburtsdatum", "kennzeichen"):
            self.assertNotIn(forbidden, text)

if __name__ == "__main__": unittest.main()
