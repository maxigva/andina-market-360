# Capítulo 03 · Conociendo la interfaz de GitHub

**Caso que continúa:** recorrer la plataforma con una ficha de observación sin modificar repositorios ajenos.
**Rutas de consulta:** Repositories / Issues / Pull requests / Actions / Settings
**Fecha:** 17/11/2026

> Todo el recorrido fue de solo lectura: se usó el navegador y `gh` (consultas `view`, `search` y `api` con método GET).

## Ejemplos resueltos

### 3.1 · Localizar las áreas esenciales
- **Qué se hizo:** se ubicaron Profile, Repositories, Pull requests, Issues y Search, y se relacionó cada una con un uso del caso.
- **Archivo / comando:** [fichas/observaciones.md](../fichas/observaciones.md) (sección 3.1); `gh browse -n` para obtener rutas exactas.
- **Resultado observado:** ruta descrita hacia cualquier repositorio público: Search → `propietario/nombre` → Repositories → Code.
- **Comprobación:** las URL impresas abren las secciones del repositorio del caso. → `evidencias/cap03/CAP03_E01.txt`

### 3.2 · Examinar un repositorio público
- **Qué se hizo:** recorrido de `github/docs` por Code, Issues, Pull requests, Actions y Settings.
- **Archivo / comando:** tabla de 5 filas en `fichas/observaciones.md`; `gh repo view github/docs`, `gh workflow list -R github/docs`.
- **Resultado observado:** `mi_permiso: READ` → la pestaña Settings no es visible; el repositorio tiene 123 workflows frente a 1 del caso.
- **Comprobación:** no se cambió nada; evidencia: tabla de cinco filas. → `CAP03_E02.txt`

### 3.3 · Buscar proyectos por tema
- **Qué se hizo:** búsqueda `topic:python sales dashboard` filtrada por Repositories; matriz de documentación y mantenimiento de dos resultados.
- **Comando:** `gh search repos "sales dashboard" --topic python`
- **Resultado observado:** uno con licencia MIT (reutilizable como referencia) y otro sin licencia detectada (solo lectura de ideas).
- **Comprobación:** solo se guardaron URLs públicas y conclusiones; no se descargó ni ejecutó nada. → `CAP03_E03.txt`

### 3.4 · Seguir una conversación técnica
- **Qué se hizo:** cronología problema → debate → solución del issue cerrado cli/cli #14814.
- **Archivo:** [fichas/seguimiento.md](../fichas/seguimiento.md)
- **Resultado observado:** reporte 24/10 → triaje confirma la causa 24/10 → PR #14815 fusionado y cierre 26/10. Faltó una prueba automática que reprodujera el caso.
- **Comprobación:** la cronología cita el enlace y no atribuye opiniones al equipo. → `CAP03_E04.txt`

### 3.5 · Explorar el historial de cambios
- **Qué se hizo:** se examinaron tres commits de `cli/cli` con mensaje, autor público y archivos.
- **Archivo / comando:** sección 3.5 de `fichas/observaciones.md`; `gh api repos/cli/cli/commits/<sha>`.
- **Resultado observado:** `8ad5fb5` corrige un error (código + prueba), `f219d43` añade una mejora, `b13e6c6` es mantenimiento de dependencias.
- **Comprobación:** tabla de tres commits con su finalidad observable. → `CAP03_E05.txt`

## Retos

### Reto 3.1 · Mapa visual de navegación con seis secciones
- **Resultado obtenido:** [fichas/mapa_github.md](../fichas/mapa_github.md): diagrama Mermaid y tabla de 6 secciones (Code, Issues, Pull requests, Actions, Projects, Settings) con su utilidad en el caso.
- **Cómo lo comprobé:** cada ruta se generó con `gh browse -n` y la tabla tiene 6 filas. → `CAP03_R01.txt`

### Reto 3.2 · Comparar dos repositorios públicos
- **Resultado obtenido:** [fichas/comparacion_repos.md](../fichas/comparacion_repos.md): `github/docs` (README breve, CC-BY 4.0, ≈63 300 commits) frente a `git/git-scm.com` (README completo, MIT, ≈3 850 commits).
- **Cómo lo comprobé:** datos de la API (tamaño del README, licencia, paginación de commits). Corrección: la primera versión incluía la fecha del último push, que cambia a diario; se reemplazó por rasgos estables del historial. → `CAP03_R02.txt`

### Reto 3.3 · Ficha de un Issue público
- **Resultado obtenido:** [fichas/ficha_issue.md](../fichas/ficha_issue.md) del issue cli/cli #14692 con pasos, evidencias y estado (cerrado como completado; se aclaró la ayuda en lugar de cambiar el comportamiento).
- **Cómo lo comprobé:** estado, fechas y comentario de cierre consultados con `gh issue view`. → `CAP03_R03.txt`

Pruebas del proyecto tras el capítulo: 4 de 4 correctas → `CAP03_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 04:** el repositorio del caso no tiene descripción ni licencia, y su README no explica cómo ejecutar paso a paso; corregirlo siguiendo el modelo de `git/git-scm.com`.
