# Capítulo 16 · Participación en proyectos de código abierto

**Caso que continúa:** practicar contribuciones transparentes y éticas partiendo de material público.
**Comandos de consulta:** `git remote add upstream https://github.com/PROPIETARIO/REPO.git` · `git fetch upstream`
**Fecha:** 18/11/2026 · Commits: `1645d67 docs: ampliar la guía de contribución con reglas de proyectos públicos` y `docs: documentar capítulo 16`

> **Simulación local documentada:** las contribuciones a repositorios de terceros (comentar Issues, hacer fork, abrir PR) se prepararon pero **no se enviaron**. En GitHub solo se leyó información pública con `gh` (consultas de lectura). El flujo fork → upstream → PR se ejecutó con repositorios Git locales descartables. Detalle en [fichas/contribucion_open_source.md](../fichas/contribucion_open_source.md).

## Ejemplos resueltos

### 16.1 · Examinar reglas de contribución
- **Qué se hizo:** se leyó `.github/CONTRIBUTING.md` de `cli/cli` (versión `d6cbbe9`) y se listaron sus requisitos: Issue previo, PR solo para `help wanted` con criterios, no ampliar el alcance, ramas, pruebas (`go test ./...`), licencia y código de conducta. Se adaptaron a Andina Market 360 en `CONTRIBUTING.md`: secciones nuevas *Antes de empezar* (Issue con criterios, `upstream` para forks), *Revisión* (guía y categorías de bloqueo) y *Licencia y conducta*.
- **Comprobación:** la adaptación copia prácticas, no permisos: no afirma nada sobre lo que acepta `cli/cli`. Verificador Markdown y pruebas en OK. → `evidencias/cap16/CAP16_E01.txt`, `CAP16_contributing.txt`

### 16.2 · Preparar una propuesta antes del cambio
- **Qué se hizo:** en `cli/cli` no hay Issues abiertos con `good first issue` (0). Se eligió [#9789](https://github.com/cli/cli/issues/9789) (`help wanted`, sin asignar). Se leyó su estado: los mantenedores aceptaron criterios (05/10/2026) y hay una pregunta reciente sin responder (06/11/2026), así que su disponibilidad **no está confirmada**.
- **Resultado:** borrador con alcance y prueba esperada, guardado en la ficha; **no se publicó** ningún comentario.
- **Comprobación:** → `CAP16_E02.txt`

### 16.3 · Crear una copia mediante fork
- **Simulación local:** `upstream-publico.git` hace de repositorio original; `fork-estudiante.git` es su copia completa (como el botón *Fork*); en la carpeta de trabajo se agregó `upstream` **sin sustituir** `origin`.
- **Comprobación:** `git remote -v` distingue `origin` (fork) y `upstream` (original), y ambos parten del mismo commit `ca2cda8`. → `CAP16_E03.txt`

### 16.4 · Desarrollar una contribución mínima
- **Qué se hizo:** rama `docs/mejora-uso`; la instrucción `python reporte.py` fallaba (*can't open file*) y se corrigió a `python src/reporte.py`, que se ejecutó con éxito antes del commit `docs: corregir la ruta del script en el README`.
- **Comprobación:** `git diff --stat upstream/main...docs/mejora-uso` → 1 archivo, 1 línea: solo la corrección acordada. → `CAP16_E04.txt`

### 16.5 · Preparar un PR respetuoso
- **Qué se hizo:** texto de PR de muestra que cita el Issue, el cambio, la motivación (el error real observado) y las pruebas, reconoce el trabajo previo y la licencia MIT, y no exige aceptación. El ajuste pedido por la persona mantenedora (simulado: indicar `python3` en Linux) se registró como **segundo commit en la misma rama**.
- **Comprobación:** `git log upstream/main..docs/mejora-uso` → 2 commits; la rama se publicó en el fork. → `CAP16_E05.txt`

## Retos

### Reto 16.1 · Proyecto público con reglas claras y propuesta de mejora documental
- **Resultado obtenido:** en `cli/cli/.github/CONTRIBUTING.md` se encontraron dos imprecisiones verificables: el enlace de “needs-design and help wanted” filtra Issues **cerrados** (`state%3Aclosed`) aunque el texto invita a proponer diseños para Issues **abiertos**, y la línea 57 nombra la etiqueta `help-wanted` cuando la real es `help wanted`. Propuesta: `state%3Aopen` y nombre correcto de la etiqueta.
- **Cómo lo comprobé:** líneas 57 y 79 del archivo. Siguiendo sus reglas, primero se abriría un Issue; no se envió nada. → `CAP16_R01.txt`

### Reto 16.2 · Diagrama fork → rama → commit → PR en cinco pasos
- **Resultado obtenido:** diagrama Mermaid de 5 pasos, con el ciclo “cambios pedidos → nuevo commit en la misma rama”, en la ficha del capítulo. Es el mismo flujo que se ejecutó en la simulación (16.3-16.5).

### Reto 16.3 · Tres responsabilidades éticas
- **Resultado obtenido:** (1) respetar las reglas y el tiempo del proyecto; (2) ser honesto sobre autoría y licencias; (3) no dañar a usuarios ni al proyecto (sin datos personales ni secretos; vulnerabilidades por canal privado).
- **Cómo lo comprobé:** cada responsabilidad se aplicó en el capítulo: no se publicaron comentarios repetitivos ni PR fuera de las reglas de `cli/cli`, el PR de muestra reconoce la licencia y todo se hizo con datos ficticios.

Pruebas del proyecto tras el capítulo: 7 de 7 correctas → `CAP16_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 17:** completar la descripción, los *topics* y el sitio del repositorio (hoy vacíos) y agregar `CODEOWNERS` y `SECURITY.md`, que la guía de contribución ya menciona como canal privado.
