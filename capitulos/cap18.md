# Capítulo 18 · Versiones, etiquetas y lanzamientos

**Caso que continúa:** empaquetar una versión demostrativa del dashboard para su entrega.
**Comandos de consulta:** `git tag -a v1.0.0 -m "Primera versión"` · `git show v1.0.0 --stat`
**Fecha:** 18/11/2026 · Commit `0f5a39a docs: definir versiones y registrar cambios de la 1.0.0` · Tag anotado **`v1.0.0`** · [Release v1.0.0](https://github.com/maxigva/andina-market-360/releases/tag/v1.0.0)

## Ejemplos resueltos

### 18.1 · Definir un esquema de versiones
- **Qué se hizo:** [VERSIONES.md](../VERSIONES.md) con el formato MAYOR.MENOR.PARCHE, criterios del caso para cada incremento (MAYOR = cambia el CSV, el JSON o la línea de comandos; MENOR = funcionalidad compatible, como el filtro por producto; PARCHE = corrección sin cambiar el uso) y el contenido de 1.0.0 (CSV, script, 7 pruebas, página estática y documentación).
- **Comprobación:** la versión se basa en cambios reales (las entradas del CHANGELOG citan commits), no en fechas; cambiar solo documentación del curso no crea versión. → `evidencias/cap18/CAP18_E01_E03.txt`

### 18.2 · Crear un tag local
- **Qué se hizo:** con el árbol limpio y `Ran 7 tests … OK`, `git tag -a v1.0.0 -m "Primera versión de Andina Market"` sobre el commit aprobado `0f5a39a`.
- **Resultado observado:** `git tag --list` → `v1.0.0`; `git show v1.0.0 --stat` muestra autor del tag, mensaje y el commit con `CHANGELOG.md` y `VERSIONES.md`.
- **Comprobación:** `v1.0.0^{commit}` = `HEAD` = `0f5a39a`; 0 archivos alterados por crear el tag. → `CAP18_E02.txt`

### 18.3 · Redactar notas del lanzamiento
- **Qué se hizo:** [CHANGELOG.md](../CHANGELOG.md) con las secciones **Añadido** (6), **Cambiado** (3), **Corregido** (4) y **Pendiente** (2): resumen de ventas, documentación y cobertura de pruebas.
- **Comprobación:** los **15** hashes citados existen y son ancestros de `main`, y los Issues citados coinciden con su estado (#1, #2, #3 y #5 cerrados). Lo **listo** está separado de lo **pendiente**: el filtro por producto (#4, abierto) y el porcentaje por barra figuran como no incluidos. → `CAP18_R02.txt`, `CAP18_E01_E03.txt`

### 18.4 · Publicar una Release en entorno propio
- **Qué se hizo:** `git push origin v1.0.0` y luego `gh release create v1.0.0 --verify-tag` (solo se crea si el tag ya existe en GitHub) con las notas de la sección 1.0.0 del CHANGELOG. No se adjuntaron archivos extra: GitHub agrega automáticamente el código fuente en zip y tar.gz. El paquete distribuible se prepara en el Cap. 20.
- **Comprobación:** se descargó el zip de la Release (271 archivos): ningún `.env`, `.git/`, `_material/`, caché ni clave. El primer escaneo encontró 5 coincidencias de `github_pat_`, pero eran los **propios patrones de búsqueda** escritos en evidencias y fichas; con el formato estricto de un token real, el resultado es **0 credenciales**. → `CAP18_E04.txt` (captura `CAP18_release.png`, pendiente)

### 18.5 · Verificar capacidad de volver a una versión
- **Qué se hizo:** hash de `v1.0.0` = `0f5a39a5821d…`; `git worktree add -b prueba/revision-desde-tag … v1.0.0` crea una copia de trabajo limpia aparte, donde se ejecutaron las pruebas.
- **Resultado observado:** en esa versión, `Ran 7 tests … OK` y TOTAL S/ 1845.00.
- **Comprobación:** `main` siguió en `0f5a39a` antes y después; luego se retiraron la copia y la rama de prueba sin tocar `main`. → `CAP18_E05.txt`

## Retos

### Reto 18.1 · Tres nombres de release con cambios y razón de versión
| Release | Cambios | Razón del número |
|---|---|---|
| **v1.0.0 – “Primera entrega”** (publicada) | Tablero con gráfico, presentación y tablas; README generado; 7 pruebas | Primera versión estable y entregable |
| **v1.1.0 – “Filtro por producto”** (propuesta) | `--producto` en `src/resumen.py`, selector en la web y prueba nueva (#4) | **MENOR**: funcionalidad nueva compatible; el JSON solo agrega campos |
| **v2.0.0 – “Nuevo formato de datos”** (hipotética) | El CSV pasa a tener la columna `canal` obligatoria y `por_sede` se divide por canal | **MAYOR**: un CSV o un consumidor del JSON de 1.x deja de funcionar |

### Reto 18.2 · CHANGELOG con cinco entradas verificables
- **Resultado obtenido:** 13 entradas en 1.0.0 (más que las 5 pedidas), cada una con commit, PR o Issue.
- **Cómo lo comprobé:** un ciclo recorre todos los hashes del archivo y confirma con `git merge-base --is-ancestor` que están en `main`; además se consultó el estado de los Issues citados. → `CAP18_R02.txt`

### Reto 18.3 · Etiqueta Git frente a Release de GitHub
| | Etiqueta `v1.0.0` | Release `v1.0.0` |
|---|---|---|
| Dónde existe | En Git (objeto `tag` → commit `0f5a39a`), viaja con cualquier clon | Solo en GitHub, sobre la etiqueta |
| Contenido | Autor, fecha y mensaje de una línea | Título, notas (27 líneas desde el CHANGELOG), descargas zip/tar.gz y adjuntos opcionales |
| Fechas | Fecha del tag (11:54) | `createdAt` = fecha del commit etiquetado; `publishedAt` = momento real de publicación en GitHub |
| Para quién | Desarrollo: volver exactamente a esa versión | Usuarios y gerencia: descargar y leer qué cambió |

Evidencia: `git cat-file -p v1.0.0` y `gh release view v1.0.0`. → `CAP18_R03.txt`

Pruebas del proyecto tras el capítulo: 7 de 7 correctas → `CAP18_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 19:** publicar el tablero con GitHub Pages desde `/docs` y usar la URL publicada como *homepage* del repositorio; comprobar que los enlaces relativos funcionan bajo `/andina-market-360/`.
