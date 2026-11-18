# Capítulo 07 · Comandos fundamentales de Git

**Caso que continúa:** gestionar versiones de las ventas simuladas y la documentación del dashboard.
**Comandos de consulta:** `git status --short` · `git diff -- README.md` · `git log --oneline -5`
**Fecha:** 17/11/2026 · Commits: `4a0bc2d`, `778f942`, `b3fe748`, `be19b40` y `docs: documentar capítulo 07`

## Ejemplos resueltos

### 7.1 · Detectar archivos modificados
- **Qué se hizo:** se añadió al README la sección “Uso del tablero” con una línea de propósito.
- **Comandos:** `git status --short` → ` M README.md`; `git diff -- README.md` → 3 líneas `+`.
- **Comprobación:** `data/ventas.csv` no aparece en el estado (0 entradas) porque no se editó. → `evidencias/cap07/CAP07_E01.txt`

### 7.2 · Preparar un cambio preciso
- **Comandos:** `git add README.md` y `git diff --cached -- README.md`.
- **Resultado observado:** solo las dos líneas nuevas; no hubo cambios accidentales que corregir.
- **Comprobación:** `git status --short` → `M  README.md` (marca en la **primera** columna = preparado). → `CAP07_E02.txt`

### 7.3 · Registrar una versión comentada
- **Comandos:** `git commit -m "docs: aclarar uso del tablero"`, `git log -3 --oneline`, `git show --stat HEAD`.
- **Resultado observado:** commit `4a0bc2d`; afecta solo `README.md | 3 +++`.
- **Comprobación:** el mensaje describe la finalidad; 0 palabras sensibles en el mensaje. → `CAP07_E03.txt`

### 7.4 · Comparar dos versiones
- **Qué se hizo:** se añadió en Requisitos la instrucción `python --version` (o `python3`).
- **Comando:** `git diff HEAD -- README.md`
- **Resultado observado:** 1 línea agregada, 0 quitadas.
- **Comprobación:** corresponde exactamente a la modificación intencional. → `CAP07_E04.txt`

### 7.5 · Descartar una edición no deseada
- **Qué se hizo:** se agregó a propósito la línea “TEMPORAL: nota de prueba…”; `git diff` confirmó que era lo único cambiado y que no estaba preparada; `git restore README.md`.
- **Resultado observado:** README con 0 cambios y `HEAD` intacto en `b3fe748`.
- **Por qué no modifica commits anteriores:** `git restore` copia al directorio de trabajo la versión guardada en el índice/último commit; no crea, borra ni reescribe commits. Solo se pierde la edición no confirmada, que era la intención. → `CAP07_E05.txt`

## Retos

### Reto 7.1 · Tres commits separados: documentación, datos y prueba
- **Resultado obtenido:**
  | Tipo | Commit | Archivo |
  |---|---|---|
  | Documentación | `4a0bc2d docs: aclarar uso del tablero` (y `b3fe748` con instrucciones) | `README.md` |
  | Datos | `778f942 feat: agregar CSV de muestra para pruebas` | `data/ventas_muestra.csv` (4 ventas ficticias, S/ 158.00) |
  | Prueba | `be19b40 test: validar el resumen con el CSV de muestra` | `tests/test_resumen.py` |
- **Justificación de la división:** cada commit tiene una sola razón para existir y un responsable distinto (publicación, analista, desarrollador); si la prueba fallara, se puede revertir sin perder los datos ni la documentación.
- **Cómo lo comprobé:** `git log --stat -4`: cada commit toca un único archivo. → `CAP07_R01.txt`

### Reto 7.2 · Comprobar dos cambios del README con `git diff` antes de confirmar
- **Resultado obtenido:** el cambio de 7.4 (versión de Python) y uno nuevo (uso de `--csv` con la muestra y su línea en Estructura) se revisaron juntos: `README.md | 8 ++++++++`.
- **Cómo lo comprobé:** además del diff, ejecuté el comando nuevo antes de confirmar (`--csv data/ventas_muestra.csv` → 4 operaciones, S/ 158.00). Luego commit `b3fe748`. → `CAP07_R02.txt`

### Reto 7.3 · Recuperar de forma segura una modificación no confirmada
- **Resultado obtenido:** en el repositorio de práctica del Cap. 06 se respaldó una edición no confirmada con `git diff > ../respaldo_cambio.patch`, se limpió el árbol con `git restore` y se recuperó con `git apply`.
- **Cómo lo comprobé:** estado ` M` → limpio → ` M` otra vez, la línea reapareció y el historial siguió con 1 commit. → `CAP07_R03.txt`

## Cambios en el proyecto
- Nuevo `data/ventas_muestra.csv` y nueva clase de prueba `TestMuestra`: **las pruebas pasan de 4 a 5**. El README indica `Ran 5 tests`. (Los archivos del Cap. 01 conservan la cifra 4 porque registran el estado de ese capítulo.)
- Bitácora y tabla de cambios actualizadas: cambios planificados n.º 2 y 3 cumplidos.

Pruebas del proyecto tras el capítulo: 5 de 5 correctas → `CAP07_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 08:** desarrollar el cambio planificado n.º 4 (encabezado del tablero) en una rama propia, para no tocar `main` hasta comprobarlo.

> Incidencia registrada: durante el Reto 7.3, un `cd` dentro del script de evidencias dejó la terminal en la carpeta de práctica y el siguiente commit se hizo allí. Se detectó con `git log` antes de publicar, se descartó en la práctica y se repitió en el repositorio del caso. Corrección: las evidencias ahora se ejecutan en un subshell.
