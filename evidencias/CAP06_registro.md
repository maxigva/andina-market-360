# Registro de evidencias – Capítulo 06

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| Cambio | 17/11/2026 22:04 | src/resumen.py + .gitattributes | JSON en LF; regenerar no produce cambios | cap06/CAP06_fix_json.txt |
| CAP06_E01 | 17/11/2026 22:21 | `git --version` | 2.55.0.windows.4, sin error ni credenciales | cap06/CAP06_E01.txt |
| CAP06_E02 | 17/11/2026 22:21 | `git config --local --list` | Identidad local ficticia; 0 credenciales | cap06/CAP06_E02.txt |
| CAP06_E03 | 17/11/2026 22:21 | `git init -b main` en copia sin .git | Repositorio vacío en main; ruta en bitácora | cap06/CAP06_E03.txt |
| CAP06_E04 | 17/11/2026 22:21 | `git add ...` + `git commit` | Primer commit `d8db55b` | cap06/CAP06_E04.txt |
| CAP06_E05 | 17/11/2026 22:21 | `git clone ./andina-market-360 ./andina-market-copia` | Historial coincide (`d8db55b`) | cap06/CAP06_E05.txt |
| Reto 6.1 | 17/11/2026 22:21 | `git --version --build-options` | Git for Windows 2.55.0 x86_64 | cap06/CAP06_R01.txt |
| Reto 6.2 | 17/11/2026 22:21 | `git config --local user.*` en la práctica | Valores propios sin afectar al caso | cap06/CAP06_R02.txt |
| Reto 6.3 | 17/11/2026 22:21 | `git clone` del caso + `diff` de hashes | 17 commits idénticos | cap06/CAP06_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
