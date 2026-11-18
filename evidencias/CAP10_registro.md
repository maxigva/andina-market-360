# Registro de evidencias – Capítulo 10

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP10_E01 | 18/11/2026 00:31 | `prueba/alternativa-a` y `-b` + `git merge prueba/alternativa-a` | Conflicto en README.md; ambos textos conservados | cap10/CAP10_E01.txt |
| CAP10_E02 | 18/11/2026 00:38 | Edición de marcadores + `git add` + `git commit` | Fusión `15e7efb`; 0 marcadores | cap10/CAP10_E02.txt |
| CAP10_E03 | 18/11/2026 00:46 | `git revert --no-edit 87d8676` | Commit inverso `51c8258` | cap10/CAP10_E03.txt |
| CAP10_E04 | 18/11/2026 00:58 | `git stash push -m`, `git stash list`, `git stash pop` | Borrador recuperado sin conflicto | cap10/CAP10_E04.txt |
| CAP10_E05 | 18/11/2026 00:58 | `git reflog -5`, `git show 87d8676` | Punto de recuperación registrado; sin reset | cap10/CAP10_E05.txt |
| Reto 10.1 | 18/11/2026 00:38 | `git log --graph -4 prueba/alternativa-b` | Ambos mensajes y título integrado | cap10/CAP10_R01.txt |
| Reto 10.2 | 18/11/2026 00:46 | `git log main..laboratorio/revertir`, `git diff` | 2 commits, diferencia neta 0 | cap10/CAP10_R02.txt |
| Reto 10.3 | 18/11/2026 00:58 | `git reflog main`, `git show fb37469` | Estado previo ubicado sin comandos destructivos | cap10/CAP10_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
