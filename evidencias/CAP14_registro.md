# Registro de evidencias – Capítulo 14

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP14_E01 | 18/11/2026 09:20 | `git switch -c feature/ficha-sedes` + docs/index.html | Commit `61b2e9d` aislado de main | cap14/CAP14_E01.txt |
| CAP14_E02 | 18/11/2026 09:27 | `git push -u`, `gh pr create` → PR #6 | 17 archivos → base corregida → 1 archivo | cap14/CAP14_E02.txt, cap14/CAP14_E02b_base.txt + CAP14_pr6.png (pendiente) |
| CAP14_E03 | 18/11/2026 09:27 | `gh pr review --comment` + fichas/revision_prs.md | 3 sugerencias con decisión | cap14/CAP14_E03.txt |
| CAP14_E04 | 18/11/2026 09:27 | Commit `56098bf` en la misma rama | PR con 2 commits; período visible | cap14/CAP14_E04.txt |
| CAP14_E05 | 18/11/2026 09:33 | `gh pr checks`, `git merge --no-ff`, `git push`, `gh issue close 3` | PR #6 Merged; Issue #3 cerrado | cap14/CAP14_E05.txt |
| Reto 14.1 | 18/11/2026 09:41 | `gh pr create` → PR #7 (5 criterios) | 1 archivo; fusionado `3454b08` | cap14/CAP14_R01_merge.txt |
| Reto 14.2 | 18/11/2026 09:37 | Revisión del PR #7 + commit `db08c08` | 2 sugerencias aplicadas; aprobación fundamentada | cap14/CAP14_R02.txt |
| Reto 14.3 | 18/11/2026 09:56 | `gh pr view 6`, `gh pr list --state all` | Un hilo con 2 commits frente a PR separados | cap14/CAP14_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
