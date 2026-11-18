# Registro de evidencias – Capítulo 17

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP17_E01 | 18/11/2026 11:21 | `gh api -X POST .../rulesets` + `GET /rules/branches/main` | Ruleset activo: `non_fast_forward` y `deletion`; sin PR obligatorio | cap17/CAP17_E01.txt + CAP17_ruleset.png (pendiente) |
| CAP17_E02 | 18/11/2026 11:21 | .github/ISSUE_TEMPLATE/bug_report.md (sección Evidencia) | 9 secciones en lenguaje cotidiano | cap17/CAP17_E02_E03.txt |
| CAP17_E03 | 18/11/2026 11:21 | .github/pull_request_template.md | Checklist sin campos personales | cap17/CAP17_E02_E03.txt |
| CAP17_E04 | 18/11/2026 11:21 | .github/CODEOWNERS + `codeowners/errors` | `{"errors":[]}`; docs/ → regla /docs/ | cap17/CAP17_E04.txt |
| CAP17_E05 | 18/11/2026 11:37 | fichas/administracion_repo.md (conservación) | Estado activo; pasos de recuperación | fichas/administracion_repo.md |
| Metadatos | 18/11/2026 11:37 | `gh repo edit --description --add-topic` | Descripción y 8 topics | cap17/CAP17_repo_edit.txt |
| Reto 17.1 | 18/11/2026 11:37 | fichas/administracion_repo.md | 3 reglas con riesgo; 2 aplicadas | cap17/CAP17_E01.txt |
| Reto 17.2 | 18/11/2026 11:21 | .github/PULL_REQUEST_TEMPLATE/calidad_datos.md | Controles ejecutables verificados | cap17/CAP17_R02.txt |
| Reto 17.3 | 18/11/2026 11:37 | fichas/administracion_repo.md | Política de archivado de 6 puntos | fichas/administracion_repo.md |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
