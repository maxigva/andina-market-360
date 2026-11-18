# Registro de evidencias – Capítulo 18

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP18_E01 | 18/11/2026 11:54 | VERSIONES.md | MAYOR.MENOR.PARCHE con criterios del caso | cap18/CAP18_E01_E03.txt |
| CAP18_E02 | 18/11/2026 11:54 | `git tag -a v1.0.0`, `git tag --list`, `git show v1.0.0 --stat` | Tag en `0f5a39a`; 0 archivos alterados | cap18/CAP18_E02.txt |
| CAP18_E03 | 18/11/2026 11:54 | CHANGELOG.md | Añadido 6, Cambiado 3, Corregido 4, Pendiente 2 | cap18/CAP18_E01_E03.txt |
| CAP18_E04 | 18/11/2026 11:54 | `git push origin v1.0.0`, `gh release create --verify-tag`, descarga zip | Release publicada; 0 credenciales reales | cap18/CAP18_E04.txt + CAP18_release.png (pendiente) |
| CAP18_E05 | 18/11/2026 12:10 | `git worktree add -b prueba/revision-desde-tag … v1.0.0` | 7 pruebas OK en v1.0.0; main sin cambios | cap18/CAP18_E05.txt |
| Reto 18.1 | 18/11/2026 12:10 | capitulos/cap18.md | 3 releases con razón de versión | capitulos/cap18.md |
| Reto 18.2 | 18/11/2026 11:54 | CHANGELOG.md + `git merge-base --is-ancestor` | 13 entradas; 15 hashes en main | cap18/CAP18_R02.txt |
| Reto 18.3 | 18/11/2026 12:10 | `git cat-file -p v1.0.0`, `gh release view v1.0.0` | Diferencias tag/Release documentadas | cap18/CAP18_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
