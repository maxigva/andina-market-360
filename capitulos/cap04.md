# Capítulo 04 · Creación y administración de repositorios

**Caso que continúa:** abrir el repositorio del proyecto y organizar su estructura inicial.
**Rutas de consulta:** `README.md`, `data/ventas.csv`, `src/resumen.py`, `tests/test_resumen.py`
**Fecha:** 17/11/2026 · Commits: `chore: organizar repositorio con README, licencia MIT y .gitignore` y `docs: documentar capítulo 04`

## Ejemplos resueltos

### 4.1 · Crear el repositorio del caso
- **Qué se hizo:** el repositorio `andina-market-360` ya estaba creado en GitHub (17/11/2026) y conectado como `origin`. Se revisaron nombre, descripción y visibilidad y se registró la URL en una ficha local.
- **Archivo / comando:** [fichas/repositorio.md](../fichas/repositorio.md); `gh repo view`, `gh repo list`, `git remote -v`.
- **Resultado observado:** aparece en la lista de repositorios; visibilidad **PUBLIC** (el cuaderno sugiere privado para empezar: la decisión se justifica en el Reto 4.3); descripción vacía, pendiente para el Cap. 17.
- **Comprobación:** → `evidencias/cap04/CAP04_E01.txt`

### 4.2 · Escribir un README inicial
- **Qué se hizo:** README reescrito con problema, funcionalidades, estructura de carpetas, requisitos, cómo ejecutar (bloque de código con `python src/resumen.py`) y licencia.
- **Archivo:** [README.md](../README.md)
- **Resultado observado:** 7 secciones `##`; la API de Markdown de GitHub las renderiza como encabezados. La salida mostrada es la ejecución real del script.
- **Comprobación:** → `CAP04_E02.txt`

### 4.3 · Organizar carpetas reales
- **Qué se hizo:** se confirmó que `data/`, `src/`, `tests/`, `docs/` y `.github/` existen con sus archivos y que las rutas que usa Python (`data/ventas.csv`, `docs/data/resumen.json`) no cambiaron.
- **Comando:** `git ls-files` por carpeta y búsqueda de carpetas vacías.
- **Resultado observado:** 0 carpetas vacías → no hace falta ningún archivo *placeholder*. El árbol coincide con la ficha del Cap. 01 (`proyecto.md`) más las carpetas del curso `capitulos/` y `fichas/`.
- **Comprobación:** → `CAP04_E03.txt`

### 4.4 · Evitar archivos innecesarios
- **Qué se hizo:** `.gitignore` ampliado con `.venv/`, `venv/`, `.env`, `.env.*`, temporales de editor (`*.swp`, `*~`, `*.tmp`, `.idea/`) y del sistema (`.DS_Store`, `Thumbs.db`).
- **Comando:** se crearon archivos de prueba (`.env` con un valor ficticio, `.venv/`, `notas.swp`, `reporte.tmp`), se revisó `git status --ignored` y `git check-ignore -v`, y luego se borraron.
- **Resultado observado:** los 4 archivos aparecen como ignorados (`!!`) y no como cambios nuevos; `data/ventas.csv` sigue versionado y **no** está ignorado.
- **Comprobación:** → `CAP04_E04.txt`

### 4.5 · Configurar una licencia con criterio
- **Qué se hizo:** el repositorio es público y de práctica personal; se comparó con la licencia MIT (texto oficial en choosealicense.com/licenses/mit) y se agregó `LICENSE` con titular “Estudiante”.
- **Resultado observado:** el README aclara que la licencia cubre el código y la documentación propia, y que el cuaderno del curso es material de su autor, no incluido ni licenciado aquí.
- **Comprobación:** README y licencia no afirman permisos sobre material de terceros; `_material/` nunca se versionó (0 archivos en el historial). → `CAP04_E05.txt`

## Retos

### Reto 4.1 · Repositorio para una tienda distinta
- **Resultado obtenido:** [fichas/diseno_tienda.md](../fichas/diseno_tienda.md): *Ferretería Costa Sur* (ficticia) con 5 carpetas (`data/`, `src/`, `tests/`, `reportes/`, `docs/`) y su función.
- **Cómo lo comprobé:** la tabla tiene 5 carpetas y cada una indica si se edita a mano o se regenera. → `CAP04_R01.txt`

### Reto 4.2 · Corregir un README incompleto
- **Resultado obtenido:** [fichas/readme_corregido.md](../fichas/readme_corregido.md): el README base no tenía requisitos, salida esperada ni el comando del resumen; se agregaron.
- **Cómo lo comprobé:** ejecuté los 4 pasos del README tal como están escritos: resumen correcto, 4 pruebas OK, JSON regenerado y servidor local con HTTP 200. Hallazgo: tras regenerar el JSON, `git status` lo marcó como modificado aunque `git diff` estaba vacío (diferencia de fin de línea CRLF/LF en Windows); un `git add` refrescó el índice y el estado quedó limpio. → `CAP04_R02.txt`

### Reto 4.3 · Pasar de privado a público
- **Resultado obtenido:** [fichas/privado_publico.md](../fichas/privado_publico.md): tabla de qué cambia (historial visible, forks, Pages, licencia) y revisión de 6 riesgos.
- **Cómo lo comprobé:** 0 secretos en todo el historial, solo el correo ficticio de autor, 0 archivos sensibles versionados, CSV sin columnas personales y licencia presente. → `CAP04_R03.txt`

Pruebas del proyecto tras el capítulo: 4 de 4 correctas → `CAP04_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 05:** fijar los finales de línea con un archivo `.gitattributes` para que regenerar el JSON en Windows no marque cambios falsos, y registrar cada versión del CSV con un mensaje de commit descriptivo.
