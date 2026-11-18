# Manual de Andina Market 360

Guía de instalación, datos e indicadores del tablero. Volver al [README](https://github.com/maxigva/andina-market-360#readme) · [Tablero publicado](index.html).

## Instalación verificable

### Windows (PowerShell o Git Bash)
```bash
git --version
python --version
git clone https://github.com/maxigva/andina-market-360.git
cd andina-market-360
python -m unittest discover -s tests
```

### Linux
```bash
git --version
python3 --version
git clone https://github.com/maxigva/andina-market-360.git
cd andina-market-360
python3 -m unittest discover -s tests
```

La instalación es correcta si el último comando termina en `OK`. No hace falta `pip install`: el proyecto solo usa la biblioteca estándar.

## Datos
Fuente única: [`data/ventas.csv`](https://github.com/maxigva/andina-market-360/blob/main/data/ventas.csv). Este manual **no copia** sus filas: cualquier cifra se obtiene ejecutando `src/resumen.py`.

| Columna | Tipo | Descripción |
|---|---|---|
| `id` | entero | Número de la operación |
| `fecha` | AAAA-MM-DD | Fecha de la venta (enero a marzo de 2026) |
| `sede` | texto | Lima, Ica o Arequipa |
| `producto` | texto | Uno de los cuatro productos del catálogo ficticio |
| `cantidad` | entero | Unidades vendidas |
| `precio_unitario` | decimal | Precio en soles (S/) |

## Indicadores por sede
Los valores **no se escriben aquí**: los calcula `src/resumen.py` y se publican en [`docs/data/resumen.json`](data/resumen.json).

| Sede | Indicador | Fórmula | Fuente |
|---|---|---|---|
| Lima | Ventas de la sede | Σ cantidad × precio_unitario de las filas de Lima | `por_sede.Lima` en `resumen.json` |
| Ica | Ventas de la sede | Σ cantidad × precio_unitario de las filas de Ica | `por_sede.Ica` en `resumen.json` |
| Arequipa | Ventas de la sede | Σ cantidad × precio_unitario de las filas de Arequipa | `por_sede.Arequipa` en `resumen.json` |

> Estas filas describen **cómo** se calcula cada indicador; no son resultados. Los resultados vigentes son los del JSON generado, que cambian si cambia el CSV.

## KPI del tablero
| KPI | Fórmula | Fuente concreta | Comando para verificarlo |
|---|---|---|---|
| Ventas totales | Σ cantidad × precio_unitario | `total` en `docs/data/resumen.json` | `python src/resumen.py` (línea TOTAL) |
| Número de operaciones | Filas del CSV sin encabezado | `operaciones` en `docs/data/resumen.json` | `python src/resumen.py` (línea Operaciones) |
| Ticket promedio | Ventas totales ÷ operaciones | `total` y `operaciones` en `docs/data/resumen.json` | `python -c "import json; d=json.load(open('docs/data/resumen.json')); print(round(d['total']/d['operaciones'], 2))"` |
| Participación de una sede | Ventas de la sede ÷ ventas totales × 100 | `por_sede` y `total` en `docs/data/resumen.json` | `python -c "import json; d=json.load(open('docs/data/resumen.json')); print({k: round(v/d['total']*100, 2) for k, v in d['por_sede'].items()})"` |

## Verificación de la documentación
```bash
python tools/verificar_md.py README.md CONTRIBUTING.md docs/manual.md
```
Revisa que los enlaces relativos existan, que los encabezados lleven espacio después de `#`, que los bloques de código estén cerrados y que las filas de cada tabla tengan las mismas columnas. Los enlaces a archivos dentro de `docs/` son relativos (funcionan en GitHub y en Pages, aunque cambie el propietario). Los que apuntan **fuera** de `docs/` (README, CSV) usan la URL de GitHub, porque Pages solo publica `docs/`; si el repositorio cambia de dueño, hay que actualizar esos dos enlaces.
