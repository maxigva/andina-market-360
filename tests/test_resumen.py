import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import resumen


class TestResumen(unittest.TestCase):
    def setUp(self):
        self.r = resumen.resumir(resumen.leer_ventas())

    def test_operaciones(self):
        self.assertEqual(self.r["operaciones"], 12)

    def test_total_general(self):
        self.assertEqual(self.r["total"], 1845.00)

    def test_totales_por_sede(self):
        self.assertEqual(self.r["por_sede"], {"Lima": 814.00, "Ica": 555.00, "Arequipa": 476.00})

    def test_json_coincide_con_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            salida = Path(tmp) / "resumen.json"
            salida.write_text(json.dumps(self.r), encoding="utf-8")
            self.assertEqual(json.loads(salida.read_text(encoding="utf-8"))["total"], 1845.00)


if __name__ == "__main__":
    unittest.main()
