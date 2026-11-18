# Registro de evidencias – Capítulo 05

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP05_E01 | 17/11/2026 21:47 | fichas/bitacora.md + `cp`, `sha256sum`, `cmp` | 12 registros; restauración sin GitHub idéntica al respaldo | cap05/CAP05_E01.txt |
| CAP05_E02 | 17/11/2026 21:47 | `git status`, `git diff --cached`, `git log -1` | Archivo modificado sin commit automático | cap05/CAP05_E02.txt |
| CAP05_E03 | 17/11/2026 21:31 | README.md + `git diff --stat` | 1 línea cambiada; commit `3c9710d` | cap05/CAP05_E03.txt |
| CAP05_E04 | 17/11/2026 21:47 | fichas/tabla_cambios.md + `git show --stat` | 2 registros con impacto | cap05/CAP05_E04.txt |
| CAP05_E05 | 17/11/2026 21:47 | `diff`/`cmp` entre copia y respaldo del README | Título restituido; sin diferencias | cap05/CAP05_E05.txt |
| Reto 5.1 | 17/11/2026 21:47 | fichas/bitacora.md + `git log -- data/ventas.csv` | 3 situaciones; historial del CSV recuperable | cap05/CAP05_R01.txt |
| Reto 5.2 | 17/11/2026 21:47 | fichas/bitacora.md | 4 cambios con criterio de aceptación | cap05/CAP05_R02.txt |
| Reto 5.3 | 17/11/2026 21:47 | fichas/bitacora.md + `git add`/`git restore --staged` | `??` → `A` → 0 commits | cap05/CAP05_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
