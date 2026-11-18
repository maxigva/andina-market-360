## Cambio en los datos
<!-- Archivo(s) de data/ modificados y motivo (corrección, nueva sede, nuevo mes...). -->

Atiende: #

## Calidad de datos
| Control | Antes | Después | Cómo se obtuvo |
|---|---|---|---|
| Filas sin encabezado | | | `tail -n +2 data/ventas.csv \| wc -l` |
| Total general (S/) | | | `python src/resumen.py` (línea TOTAL) |
| Sedes distintas | | | `por_sede` en `docs/data/resumen.json` |
| Filas con cantidad o precio ≤ 0 | | | revisión del CSV |

## Lista de comprobación
- [ ] Mismas 6 columnas y en el mismo orden: `id,fecha,sede,producto,cantidad,precio_unitario`.
- [ ] Sin `id` repetidos y con fechas en formato `AAAA-MM-DD`.
- [ ] Datos **ficticios**: sin nombres, documentos, correos ni teléfonos de personas.
- [ ] JSON y README regenerados: `python src/resumen.py --json docs/data/resumen.json --readme README.md`.
- [ ] `python -m unittest discover -s tests -v` en `OK` (si cambian los totales esperados, se actualizan las pruebas en este mismo PR y se explica por qué).
- [ ] La diferencia de totales “antes/después” se explica fila por fila.
