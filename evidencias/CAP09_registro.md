# Registro de evidencias – Capítulo 09

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP09_E01 | 18/11/2026 00:22 | `git remote -v`, `git ls-remote --heads origin` | origin sin credenciales | cap09/CAP09_E01.txt |
| CAP09_E02 | 18/11/2026 00:22 | `git remote get-url origin`, `git remote add origin ...` | origin ya existía; no se duplicó | cap09/CAP09_E02.txt |
| CAP09_E03 | 18/11/2026 00:22 | `git push -u origin main` (+ rama de filtro) | `44f5f4f..fb37469`; hash y fecha registrados | cap09/CAP09_E03.txt |
| CAP09_E04 | 18/11/2026 00:09 | Edición en GitHub + `git pull --ff-only origin main` | Fast-forward a `bd60f73`; README idéntico | cap09/CAP09_E04.txt |
| CAP09_E05 | 18/11/2026 00:22 | `git fetch origin`, `git log HEAD..origin/main` | 1 commit remoto; árbol sin cambios | cap09/CAP09_E05.txt |
| Reto 9.1 | 18/11/2026 00:22 | Copia de práctica + `git remote add`, `git ls-remote` | Remoto propio sin credenciales | cap09/CAP09_R01.txt |
| Reto 9.2 | 18/11/2026 00:22 | `git reflog` de origin/main y main | fetch mueve origin/main; pull mueve main | cap09/CAP09_R02.txt |
| Reto 9.3 | 18/11/2026 00:22 | Remoto local descartable + `git push --force` | Push normal rechazado; forzado borra trabajo ajeno | cap09/CAP09_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
