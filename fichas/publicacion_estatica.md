# Código Python local frente a contenido estático publicable (Reto 19.2)

| | Código Python **local** | Contenido **estático** publicable |
|---|---|---|
| Archivos | `src/resumen.py`, `tests/`, `tools/` | `docs/index.html`, `docs/productos.html`, `docs/style.css`, `docs/data/resumen.json`, `docs/manual.md` |
| Dónde se ejecuta | En la computadora de quien trabaja o en GitHub Actions | En el navegador de quien visita la página (HTML, CSS y JavaScript) |
| Qué hace | Lee el CSV, calcula y **genera** el JSON y el bloque del README | **Muestra** lo que ya está calculado; no puede leer el CSV ni ejecutar Python |
| ¿Lo publica GitHub Pages? | No. Pages publica solo la carpeta `docs/` de `main` (`src/resumen.py` → HTTP 404) | Sí: `https://maxigva.github.io/andina-market-360/` |
| Si cambian los datos | Hay que ejecutar `python src/resumen.py --json docs/data/resumen.json --readme README.md` y hacer commit | Se actualiza al publicarse el nuevo JSON; la página no cambia |
| Datos que expone | El CSV completo (en el repositorio, ficticio) | Solo totales agregados por sede, producto y mes; ningún registro individual |

**Regla del caso:** todo lo que se publica es estático y derivado; el cálculo nunca ocurre en el servidor. Por eso el tablero funciona en Pages sin Python, y por eso una prueba exige que el JSON publicado coincida con el CSV (Issue #2).

**Consecuencias observadas en el Capítulo 19:**
- Abrir `index.html` con doble clic (`file://`) no carga el JSON, porque el navegador bloquea `fetch` en archivos locales. Se usa `python -m http.server`, que funciona sin internet.
- Los enlaces a archivos fuera de `docs/` (README, CSV) no existen en Pages; en el manual se reemplazaron por URL de GitHub.
