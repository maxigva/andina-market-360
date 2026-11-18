# Capítulo 13 · Gestión de tareas con GitHub Issues y Projects

**Caso que continúa:** planificar el avance del dashboard con problemas y tareas verificables.
**Rutas de consulta:** `.github/ISSUE_TEMPLATE/bug_report.md` · criterios de aceptación: entrada → cambio → prueba → resultado
**Fecha:** 18/11/2026 · Commits: `bc936f5 test: …` (Refs #2), `e096234 fix: …` (Refs #5), `b6168d7 chore: agregar plantillas de issues` y `docs: documentar capítulo 13`

> Los Issues se crearon en GitHub con `gh`. Sus fechas de creación y cierre las asigna GitHub en el momento real de la operación.

## Ejemplos resueltos

### 13.1 · Abrir un Issue de funcionalidad
- **Qué se hizo:** [#1 feat: gráfico de ventas por sede](https://github.com/maxigva/andina-market-360/issues/1), con el objetivo de gerencia y 5 criterios de aceptación (3 barras, cifras de `resumen.json`, proporcionalidad ± 1 %, título legible, pruebas en OK).
- **Comprobación:** cada criterio es verificable con un archivo, un comando o una medida; se sabe objetivamente cuándo cerrarlo. → `evidencias/cap13/CAP13_E01.txt`

### 13.2 · Documentar un error reproducible
- **Qué se hizo:** [#2 bug: cifra incorrecta tras editar CSV](https://github.com/maxigva/andina-market-360/issues/2) con datos de entrada ficticios (una fila), pasos, resultado observado y esperado, impacto y criterio de cierre.
- **Resultado observado al reproducirlo:** al cambiar el CSV y actualizar pruebas y README pero no el JSON, las 6 pruebas pasaban mientras el CSV daba **S/ 2095.00** y la web publicaba **S/ 1845.00**. La primera reproducción se descartó porque fallaba por las cifras fijas de las pruebas, no por el defecto real.
- **Comprobación:** otro estudiante puede repetirlo siguiendo solo los 5 pasos. → `CAP13_E02.txt`, `CAP13_E02_reproduccion.txt`

### 13.3 · Clasificar el trabajo
- **Qué se hizo:** etiquetas `documentación`, `mejora`, `error` y `prioridad-alta` creadas en el repositorio, y cada Issue clasificado con su impacto en [fichas/tablero_tareas.md](../fichas/tablero_tareas.md).
- **Comprobación:** la etiqueta resume, pero cada Issue conserva su descripción técnica completa. → `CAP13_E03_etiquetas.txt`, `CAP13_issues.txt`

### 13.4 · Construir un tablero de tareas
- **Simulación local documentada:** `gh project list` respondió `missing required scopes [read:project]`. Ampliar los permisos del token cambiaría la configuración de seguridad de la cuenta, así que el tablero Kanban se llevó en una tabla local con tres columnas.
- **Resultado observado:** Pendiente #1, En proceso #3, Terminado #2, según su estado real.
- **Comprobación:** regla explícita para mover a Terminado (criterios + commit + pruebas + comentario de evidencia) y definición de cada estado basada en hechos (rama/PR/Issue cerrado), no en opiniones. → `CAP13_E04_projects.txt`

### 13.5 · Cerrar con evidencia técnica
- **Qué se hizo:** #2 y #5 se cerraron **después** de cumplir sus criterios, con un comentario de resolución: commit, archivo, prueba ejecutada y quién validó.
- **Resultado observado:** `#2 → CLOSED (COMPLETED)` y `#5 → CLOSED (COMPLETED)`; quedan abiertos #1, #3 y #4.
- **Comprobación:** desde el comentario se reconstruye qué se hizo (`bc936f5`, `e096234`), cómo se probó y quién lo validó. → `CAP13_E05.txt`, `CAP13_fix_issue2.txt`, `CAP13_fix_issue5.txt`

## Retos

### Reto 13.1 · Tres Issues con criterios cuantificables
- **Resultado obtenido:** #1 (3 barras, 100 % la mayor, ± 1 %), #3 (3 sedes, 1 archivo cambiado, período calculado) y #4 (3 sedes, 3 filas de Leche 1L, código de salida ≠ 0 para un producto inexistente).
- **Cómo lo comprobé:** cada criterio tiene un número o un comando que lo valida. → `CAP13_issues.txt`

### Reto 13.2 · Tablero de ocho tareas con prioridades
- **Resultado obtenido:** tabla de 8 tareas (5 Issues y 3 tareas de capítulos futuros) con estado, prioridad y justificación.
- **Cómo lo comprobé:** la regla de prioridad es explícita: primero lo que puede mostrar cifras incorrectas, luego lo que mejora la lectura o el proceso, y al final la gobernanza. Ver [fichas/tablero_tareas.md](../fichas/tablero_tareas.md).

### Reto 13.3 · Plantilla de Issue para errores en el proceso de ventas
- **Resultado obtenido:** [.github/ISSUE_TEMPLATE/bug_report.md](../.github/ISSUE_TEMPLATE/bug_report.md) (dónde aparece el error: CSV, cálculo, JSON, tablero o docs; muestra ficticia; pasos; observado vs. esperado; impacto; entorno; criterio de cierre) y una plantilla de mejora.
- **Cómo lo comprobé:** encabezado YAML válido (`name`, `about`, `title`, `labels`), 8 secciones y verificador Markdown en OK. Las plantillas están publicadas en `main`. → `CAP13_R03.txt`

Pruebas del proyecto tras el capítulo: 6 de 6 correctas → `CAP13_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 14:** atender #3 mediante un pull request desde `feature/ficha-sedes`, sin editar `main` directamente, y revisar el PR de documentación pendiente de `feature/filtro-productos`.
