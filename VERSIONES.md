# Esquema de versiones – Andina Market 360

Formato **MAYOR.MENOR.PARCHE** ([versionado semántico](https://semver.org/lang/es/)). Las versiones se marcan con tags anotados `vX.Y.Z` y se publican como Releases de GitHub. La versión refleja **cambios reales** del caso, nunca fechas.

| Parte | Se incrementa cuando… | Ejemplo en el caso |
|---|---|---|
| **MAYOR** | Cambia algo que obliga a quien usa el proyecto a adaptarse: columnas del CSV, campos del JSON o la línea de comandos de `src/resumen.py` | Renombrar `por_sede` en el JSON o exigir una columna nueva en el CSV |
| **MENOR** | Se agrega una funcionalidad compatible | Filtro por producto (`--producto`), página nueva del tablero |
| **PARCHE** | Se corrige un error sin cambiar el uso | Un cálculo o un texto del tablero corregido, una prueba que no detectaba un fallo |

Solo cambiar documentación o evidencias del curso no crea una versión nueva.

## 1.0.0 – primer lanzamiento
Contenido de la primera versión entregable:
- `data/ventas.csv` (12 ventas ficticias) y `data/ventas_muestra.csv` (4 ventas para pruebas).
- `src/resumen.py`: totales por sede, producto y mes; genera `docs/data/resumen.json` (`--json`) y el bloque de cifras del README (`--readme`).
- `tests/test_resumen.py`: 7 pruebas (cálculo, JSON publicado, README generado, tablero sin cifras fijas y muestra).
- `docs/index.html`: tablero estático con presentación (sedes, período, origen), gráfico y tablas, alimentado solo por el JSON.
- Documentación: README, manual, guía de contribución, plantillas de Issues/PR y CODEOWNERS.

Detalle de cambios: [CHANGELOG.md](CHANGELOG.md).
