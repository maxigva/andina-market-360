# Capítulo 14 · Pull Requests y colaboración

**Caso que continúa:** integrar cambios del caso mediante revisión, no mediante edición directa de `main`.
**Comandos de consulta:** `git switch -c feature/ficha-sedes` · `git push -u origin feature/ficha-sedes` · `gh pr create --base main`
**Fecha:** 18/11/2026 · PR [#6](https://github.com/maxigva/andina-market-360/pull/6) y [#7](https://github.com/maxigva/andina-market-360/pull/7)

> Los PR, revisiones y comentarios se crearon con `gh`; GitHub registra su hora real. Los commits y las fusiones se hicieron en local con la fecha del cronograma y se publicaron con push normal: GitHub marcó cada PR como *Merged* al recibir en `main` el commit de fusión.

## Ejemplos resueltos

### 14.1 · Crear una rama revisable
- **Qué se hizo:** desde `main` actualizado, `feature/ficha-sedes`; en `docs/index.html` se agregó un subtítulo con las sedes (leídas de `por_sede`) y el origen ficticio de los datos. Commit `61b2e9d feat: presentar sedes y origen ficticio en el tablero`.
- **Comprobación:** HTML válido; la expresión del tablero, ejecutada en Node sobre el JSON publicado, produce *Sedes: Lima, Ica y Arequipa · Origen: datos ficticios de data/ventas.csv*; `git log main..feature/ficha-sedes` muestra solo ese commit. → `evidencias/cap14/CAP14_E01.txt`

### 14.2 · Publicar y abrir un Pull Request
- **Qué se hizo:** `git push -u origin feature/ficha-sedes` y `gh pr create --base main` con título, resumen, instrucciones de verificación y lista de comprobación → PR #6.
- **Hallazgo y corrección:** *Files changed* mostraba **17 archivos**, porque la rama partía de `be39dd0` (documentación del Cap. 13), que estaba solo en `main` local. Se publicó `main`, pero GitHub mantuvo la base vieja (`b6168d7`) incluso tras un nuevo push a la rama. Se cambió la base del PR y se devolvió a `main` para forzar el recálculo → base `be39dd0`, **1 archivo** (`docs/index.html`), 2 commits.
- **Comprobación:** → `CAP14_E02.txt`, `CAP14_E02b_base.txt`

### 14.3 · Solicitar una revisión útil
- **Qué se hizo:** el PR incluye una lista de comprobación (HTML legible, pruebas, fuente de datos, alcance, exactitud). No hay compañeros en el repositorio, así que la revisión se hizo con un **rol simulado** y se publicó como comentario de revisión (GitHub rechazó *request changes* en un PR propio).
- **Resultado observado:** 3 sugerencias sobre exactitud (período), alcance (17 archivos) y presentación.
- **Comprobación:** sugerencias y decisiones registradas en [fichas/revision_prs.md](../fichas/revision_prs.md). → `CAP14_E03.txt`

### 14.4 · Atender una observación
- **Qué se hizo:** en la **misma rama** se agregó el período del informe, calculado del primer y el último mes de `por_mes` (`56098bf feat: indicar período del informe en el tablero`), y se publicó con push.
- **Resultado observado:** *Sedes: Lima, Ica y Arequipa · Período: 2026-01 a 2026-03 · Origen: datos ficticios de data/ventas.csv*.
- **Comprobación:** el PR #6 muestra ambos commits sin abrir otro PR; se respondió a la revisión con la decisión de cada punto. → `CAP14_E04.txt`

### 14.5 · Fusionar y comprobar
- **Qué se hizo:** con `pruebas` en verde y estado `MERGEABLE / CLEAN`, se fusionó con `git merge --no-ff` (`a61b4dd Merge pull request #6 …`), se publicó `main` y GitHub marcó el PR como *Merged*. Se cerró el Issue #3 con un comentario que marca sus 5 criterios.
- **Comprobación:** 6 pruebas OK; el subtítulo aparece con los tres datos; `Issue #3: CLOSED (COMPLETED)`. La rama se eliminó en local y en GitHub. → `CAP14_E05.txt`

## Retos

### Reto 14.1 · PR de documentación con cinco criterios de aceptación
- **Resultado obtenido:** PR #7 desde `feature/filtro-productos` (rama del Cap. 08) con 5 criterios numerados: 1 archivo, 3 secciones, sin cifras fijas, verificador Markdown en OK y CI en verde.
- **Cómo lo comprobé:** `gh pr diff 7 --name-only` → 1 archivo; fusionado como `3454b08`. → `CAP14_R01_merge.txt`

### Reto 14.2 · Revisión técnica con dos sugerencias y aprobación fundamentada
- **Resultado obtenido:** revisión del PR #7 con 2 sugerencias concretas (archivo, sección y texto propuesto) y una aprobación fundamentada en los criterios. Ambas sugerencias se aplicaron en la misma rama (`db08c08`).
- **Cómo lo comprobé:** → `CAP14_R02.txt`

### Reto 14.3 · Actualizar un PR frente a crear otro
- **Resultado obtenido:** el PR #6 reúne en un solo hilo 2 commits, la revisión y la respuesta: quien revisa ve qué se pidió y cómo se atendió. Un PR nuevo habría tenido otro número, sin la conversación previa, y el primero habría quedado abierto o cerrado sin fusionar.
- **Cómo lo comprobé:** `gh pr view 6` (2 commits, 1 revisión, 1 comentario) y la lista de PR (#6 y #7, cada uno con su hilo). → `CAP14_R03.txt`

Pruebas del proyecto tras el capítulo: 6 de 6 correctas → `CAP14_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 15:** antes de crear una rama, publicar `main` (`git status -sb` sin `ahead`) para que el PR muestre solo los cambios propios; y revisar el gráfico de #1 con una guía de preguntas escrita.
