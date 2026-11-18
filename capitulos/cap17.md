# Capítulo 17 · Administración de repositorios

**Caso que continúa:** establecer reglas y plantillas de mantenimiento para la empresa simulada.
**Rutas de consulta:** `.github/pull_request_template.md` · `.github/ISSUE_TEMPLATE/bug_report.md` · `.github/CODEOWNERS`
**Fecha:** 18/11/2026 · Commits: `91bbd2a chore: agregar plantillas de PR y responsables por área` y `docs: documentar capítulo 17`

## Ejemplos resueltos

### 17.1 · Definir reglas de la rama principal
- **Qué se hizo:** se redactó la política (no fusionar sin pruebas ni revisión; no reescribir ni borrar `main`) y se aplicó en GitHub el *ruleset* `proteger-main` (activo, rama por defecto) con **dos reglas**: bloquear *force push* y bloquear el borrado. Por decisión del titular **no** se exige PR ni revisión: hay una sola persona en el repositorio y GitHub no permite aprobar un PR propio.
- **Resultado observado:** `GET /rules/branches/main` devuelve `non_fast_forward` y `deletion`; 0 reglas de PR o de verificaciones obligatorias.
- **Comprobación:** con esas reglas, un `push --force` o un borrado accidental de `main` es rechazado. No se probó con un *force push* real, porque las reglas del caso lo prohíben sobre `main`; la verificación se hizo consultando las reglas que GitHub aplica a la rama. → `evidencias/cap17/CAP17_E01.txt`, [fichas/administracion_repo.md](../fichas/administracion_repo.md)

### 17.2 · Crear una plantilla de reporte
- **Qué se hizo:** `.github/ISSUE_TEMPLATE/bug_report.md` ya existía (Cap. 13) con entorno, pasos y resultado esperado; se agregó la sección **Evidencia**, que pide captura o salida solo con datos ficticios y ofrece a quien no use la terminal describir con sus palabras qué cifra vio y dónde. Confirmado en el commit `91bbd2a`.
- **Comprobación:** 9 secciones con títulos en lenguaje cotidiano (“¿Dónde aparece el error?”, “Impacto para la empresa”), entendibles para alguien no técnico. → `CAP17_E02_E03.txt`

### 17.3 · Preparar una plantilla de PR
- **Qué se hizo:** `.github/pull_request_template.md` con resumen, Issue atendido, cómo verificar y una lista de comprobación: pruebas unitarias, ausencia de secretos, datos ficticios sin cifras fijas, documentación, alcance y capturas si cambia la web.
- **Comprobación:** 0 campos piden nombre, correo, teléfono, DNI o dirección; GitHub ya lista la plantilla en `.github/`. → `CAP17_E02_E03.txt`

### 17.4 · Definir responsables por área
- **Qué se hizo:** borrador con identificadores **ficticios** (`@andina-publicacion`, `@andina-desarrollo`, `@andina-datos`) y la revisión esperada para documentación, código y datos. El `.github/CODEOWNERS` real usa solo la cuenta con acceso (`@maxigva`) para `*`, `/docs/`, `/src/`, `/tests/`, `/data/` y `/.github/`.
- **Comprobación:** `GET /codeowners/errors?ref=main` → `{"errors":[]}`. Ejemplo de cambio en `docs/index.html`: aplica la regla `/docs/` (la última que coincide). → `CAP17_E04.txt`

### 17.5 · Planificar un archivo de proyecto
- **Qué se hizo:** ficha de conservación (versión, dueño, estado **activo**, naturaleza “material de prácticas, no producción”, próxima revisión) y criterios para archivar o mantener activo el repositorio.
- **Comprobación:** la ficha incluye los 4 pasos para recuperar la documentación antes de archivar (tag y Release, README/manual/capítulos autosuficientes, clon limpio con pruebas, cómo desarchivar). → [fichas/administracion_repo.md](../fichas/administracion_repo.md)

### Metadatos del repositorio
Con autorización del titular se completaron con `gh repo edit` la **descripción** (estaba vacía desde el Cap. 04) y 8 **topics** (`git`, `github`, `python`, `github-actions`, `github-pages`, `dashboard`, `datos-ficticios`, `curso`). El *homepage* se configurará cuando GitHub Pages esté activo (Cap. 19). → `CAP17_repo_edit.txt`

## Retos

### Reto 17.1 · Tres reglas de protección y su riesgo
- **Resultado obtenido:** (1) bloquear *force push* → evita reescribir historia publicada y perder trabajo ajeno; (2) bloquear el borrado → evita perder la rama que publica Pages; (3) exigir la verificación `pruebas` → evita publicar cifras que no coinciden con el CSV. Las reglas 1 y 2 están aplicadas; la 3 está diseñada y se activará cuando haya más colaboradores.
- **Cómo lo comprobé:** las reglas 1 y 2 aparecen activas en la API (`CAP17_E01.txt`); la 3 se justifica con los defectos reales de #2 y del PR #8.

### Reto 17.2 · Plantilla de PR orientada a calidad de datos
- **Resultado obtenido:** [.github/PULL_REQUEST_TEMPLATE/calidad_datos.md](../.github/PULL_REQUEST_TEMPLATE/calidad_datos.md): tabla “antes/después” (filas, total, sedes, valores ≤ 0) con el comando de cada control, y una lista de comprobación de columnas, `id` únicos, formato de fecha, datos ficticios, regeneración de JSON/README y explicación fila por fila.
- **Cómo lo comprobé:** los controles se ejecutaron sobre el CSV actual: 12 filas, S/ 1845.00, 3 sedes, 0 valores ≤ 0, 0 `id` repetidos, 6 columnas en orden. → `CAP17_R02.txt`

### Reto 17.3 · Política de archivado de repositorios de prácticas
- **Resultado obtenido:** política de 6 puntos (alcance, tag y Release de entrega, revisión previa sin secretos ni datos personales, archivar en lugar de borrar, tratamiento de datos reales filtrados, reactivación) en [fichas/administracion_repo.md](../fichas/administracion_repo.md).

Pruebas del proyecto tras el capítulo: 7 de 7 correctas → `CAP17_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 18:** fijar el esquema de versiones y un CHANGELOG verificable antes de etiquetar `v1.0.0`, para que la Release describa solo lo que ya está en `main`.
