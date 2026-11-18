import json
import sys
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
        """El JSON publicado para la web debe ser el resumen vigente del CSV (Issue #2)."""
        publicado = Path(__file__).resolve().parent.parent / "docs" / "data" / "resumen.json"
        self.assertEqual(json.loads(publicado.read_text(encoding="utf-8")), self.r,
                         "docs/data/resumen.json está desactualizado: ejecute python src/resumen.py --json docs/data/resumen.json")

    def test_readme_muestra_cifras_calculadas(self):
        readme = (Path(__file__).resolve().parent.parent / "README.md").read_text(encoding="utf-8")
        bloque = readme.split(resumen.INICIO)[1].split(resumen.FIN)[0]
        self.assertIn(resumen.texto(self.r), bloque)


class TestMuestra(unittest.TestCase):
    """Valida el cálculo con data/ventas_muestra.csv (4 ventas de totales conocidos)."""

    def setUp(self):
        ruta = Path(__file__).resolve().parent.parent / "data" / "ventas_muestra.csv"
        self.r = resumen.resumir(resumen.leer_ventas(ruta))

    def test_totales_muestra(self):
        self.assertEqual(self.r["operaciones"], 4)
        self.assertEqual(self.r["total"], 158.00)
        self.assertEqual(self.r["por_sede"], {"Lima": 80.00, "Ica": 40.00, "Arequipa": 38.00})


if __name__ == "__main__":
    unittest.main()
