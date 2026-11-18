# Registro de evidencias – Capítulo 07

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP07_E01 | 17/11/2026 22:36 | `git status --short`, `git diff -- README.md` | ` M README.md`; el CSV no aparece | cap07/CAP07_E01.txt |
| CAP07_E02 | 17/11/2026 22:36 | `git add`, `git diff --cached` | `M ` en la columna de preparación | cap07/CAP07_E02.txt |
| CAP07_E03 | 17/11/2026 22:36 | `git commit`, `git log -3`, `git show --stat HEAD` | Commit `4a0bc2d`, solo README | cap07/CAP07_E03.txt |
| CAP07_E04 | 17/11/2026 22:51 | `git diff HEAD -- README.md` | 1 línea agregada, 0 quitadas | cap07/CAP07_E04.txt |
| CAP07_E05 | 17/11/2026 22:51 | `git diff`, `git restore README.md` | Edición temporal descartada; HEAD intacto | cap07/CAP07_E05.txt |
| Reto 7.1 | 17/11/2026 22:58 | `git log --stat -4` | Commits separados de docs, datos y prueba | cap07/CAP07_R01.txt |
| Reto 7.2 | 17/11/2026 22:51 | `git diff --stat` + comando `--csv` | 2 cambios revisados antes de `b3fe748` | cap07/CAP07_R02.txt |
| Reto 7.3 | 17/11/2026 22:58 | `git diff > patch`, `git restore`, `git apply` | Modificación recuperada sin commits | cap07/CAP07_R03.txt |
| Pruebas | 17/11/2026 22:58 | `python -m unittest discover -s tests -v` | 5 pruebas OK | cap07/CAP07_pruebas.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
