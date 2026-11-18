# Capítulo 12 · Documentación con Markdown

**Caso que continúa:** crear instrucciones profesionales y reproducibles del proyecto empresarial.
**Rutas de consulta:** `[Manual](docs/manual.md)` · bloque `bash` con `python -m unittest discover -s tests -v`
**Fecha:** 18/11/2026 · Commits: `2dbc497 feat: generar las cifras del README desde resumen.py`, `fba5946 docs: estructurar README con manual y guía de contribución` y `docs: documentar capítulo 12`

## Cambio previo: cifras del README generadas, no escritas a mano
El README mostraba la salida de `resumen.py` copiada a mano. Ahora:
- `src/resumen.py --readme README.md` reescribe el bloque entre `<!-- resumen:inicio -->` y `<!-- resumen:fin -->`.
- La prueba `test_readme_muestra_cifras_calculadas` **falla** si el bloque no coincide con el CSV (se comprobó: con el bloque vacío, `FAILED (failures=1)`; tras generarlo, `OK`). Las pruebas pasan de 5 a **6**.
- Al probarlo apareció un error real: una variable local `texto` en la rama del JSON tapaba la nueva función `texto()` (`UnboundLocalError`); se renombró a `contenido` antes del commit.
- Regenerar dos veces deja 0 cambios. → `evidencias/cap12/CAP12_generar_readme.txt`

## Ejemplos resueltos

### 12.1 · Estructurar un README útil
- **Qué se hizo:** README reorganizado en **Objetivo**, **Datos**, **Requisitos**, **Inicio rápido**, **Ejecución**, Uso del tablero, Estructura, Documentación, Uso responsable y Licencia. Indica que los datos son ficticios y que se usa Python estándar.
- **Resultado observado:** la API de Markdown de GitHub renderiza los 10 encabezados `##`.
- **Comprobación:** un compañero encuentra en orden qué necesita (Requisitos), qué ejecutar (Inicio rápido) y qué debe ver (bloque de cifras generado). → `CAP12_E01.txt`

### 12.2 · Documentar una tabla de indicadores
- **Qué se hizo:** en [docs/manual.md](../docs/manual.md), tabla *Sede | Indicador | Fórmula | Fuente* para Lima, Ica y Arequipa.
- **Resultado observado:** todas las filas tienen 4 columnas; `tools/verificar_md.py` sin errores.
- **Por qué no confundirla con resultados:** la tabla describe **cómo** se calcula cada indicador y **dónde** se publica (`por_sede.<Sede>` en `resumen.json`); no contiene montos. Los montos vigentes los produce el script y cambian si cambia el CSV. → `CAP12_E02.txt`

### 12.3 · Insertar bloques de comandos
- **Qué se hizo:** sección **Inicio rápido** con un bloque `bash` de dos órdenes: `python -m unittest discover -s tests` y `python src/resumen.py`.
- **Resultado observado:** ambas órdenes se ejecutaron localmente antes de confirmar (pruebas `OK`, resumen con 12 operaciones).
- **Comprobación:** 0 caracteres no ASCII en el bloque: se puede copiar sin comillas tipográficas ni símbolos extraños. → `CAP12_E03.txt`

### 12.4 · Documentar rutas relativas
- **Qué se hizo:** `docs/manual.md` creado y enlazado desde el README con `[Manual](docs/manual.md)`; el manual referencia `../data/ventas.csv` sin copiar sus filas.
- **Resultado observado:** `tools/verificar_md.py` confirma que todos los enlaces relativos existen.
- **Comprobación:** se copiaron los archivos a otra carpeta (simulando otro propietario) y la verificación siguió en OK: los enlaces relativos no dependen del nombre de la cuenta. → `CAP12_E04.txt`

### 12.5 · Agregar una guía de contribución
- **Qué se hizo:** [CONTRIBUTING.md](../CONTRIBUTING.md) con reglas de datos y secretos, ramas, mensajes de commit, verificación previa al PR y cómo comunicar errores en Issues; enlazado desde el README.
- **Comprobación:** la sección “Comunicar errores en Issues” pide datos de entrada ficticios, pasos, resultado observado y esperado. → `CAP12_E05.txt`

## Retos

### Reto 12.1 · Sección de instalación verificable en Windows o Linux
- **Resultado obtenido:** sección “Instalación verificable” del manual con variantes para Windows y Linux.
- **Cómo lo comprobé:** en **Windows** se siguieron los pasos en una carpeta nueva (clonado desde GitHub) → `Ran 5 tests … OK` (el remoto aún no tenía la sexta prueba). En **Linux** la misma orden la ejecuta GitHub Actions en `ubuntu-latest` con CPython 3.12.16 → `OK`. → `CAP12_R01.txt`

### Reto 12.2 · Tabla con cuatro KPI y su fuente concreta
- **Resultado obtenido:** ventas totales, número de operaciones, ticket promedio y participación por sede, cada uno con fórmula, campo exacto de `resumen.json` y comando de verificación.
- **Cómo lo comprobé:** se ejecutaron los comandos: ticket promedio **153.75** y participación Lima 44.12 %, Ica 30.08 %, Arequipa 25.8 %, iguales a los del Reto 1.1. → `CAP12_R02.txt`

### Reto 12.3 · Corregir cinco errores de enlaces y formato
- **Resultado obtenido:** [README_prueba_errores.md](../fichas/reto12_3/README_prueba_errores.md) → [README_prueba_corregido.md](../fichas/reto12_3/README_prueba_corregido.md). Errores: encabezado sin espacio, enlace roto (`manul.md`), enlace a ruta local absoluta, fila de tabla sin una columna y bloque de código sin cerrar.
- **Cómo lo comprobé:** el verificador detectó exactamente 5 errores (código 1) y 0 en la versión corregida (código 0); `diff` muestra cada corrección. → `CAP12_R03.txt`

Pruebas del proyecto tras el capítulo: 6 de 6 correctas → `CAP12_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 13:** la prueba `test_json_coincide_con_csv` escribe y lee un JSON temporal, pero **no revisa el `docs/data/resumen.json` publicado**: si alguien edita el CSV y olvida regenerar, la web muestra cifras viejas. Registrarlo como Issue de error reproducible.
