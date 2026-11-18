# Capítulo 05 · Fundamentos del control de versiones

**Caso que continúa:** comprender cada cambio mediante un archivo de ventas y una bitácora de versiones.
**Ruta de consulta:** Directorio de trabajo → `git add` → `git commit` → historial
**Fecha:** 17/11/2026 · Commits: `3c9710d docs: precisar objetivo comercial` y `docs: documentar capítulo 05`

## Ejemplos resueltos

### 5.1 · Crear una línea de base verificable
- **Qué se hizo:** copia de `data/ventas.csv` a una carpeta de respaldo **fuera** del repositorio; conteo de registros y huella SHA-256; descripción de la versión inicial en [fichas/bitacora.md](../fichas/bitacora.md).
- **Resultado observado:** 12 registros sin encabezado, huella `12e705a345082a1b`.
- **Comprobación:** se borró a propósito la última fila (11 registros) y se restauró copiando el respaldo: 12 registros, misma huella, `cmp` sin diferencias y `git status` limpio. No se usó GitHub. → `evidencias/cap05/CAP05_E01.txt`

### 5.2 · Reconocer los tres espacios de Git
- **Qué se hizo:** diagrama Directorio de trabajo → Preparación → Historial con `README.md` como ejemplo, en la bitácora.
- **Comando:** se escribió una línea en `README.md` sin `git add` ni `git commit`; se revisaron `git status`, `git diff --cached` y `git log -1`; luego `git restore`.
- **Resultado observado:** `M README.md`, preparación vacía y `HEAD` igual antes y después (`44f5f4f`).
- **Comprobación:** Git no guarda un commit automáticamente al escribir un archivo. → `CAP05_E02.txt`

### 5.3 · Proponer un cambio controlado
- **Qué se hizo:** se cambió solo la frase de objetivo comercial del README (línea 3); antes y después anotados en la bitácora.
- **Comando:** `git diff --stat` → `README.md | 2 +-` (1 archivo, 1 línea).
- **Resultado observado:** commit `3c9710d docs: precisar objetivo comercial`.
- **Comprobación:** el cambio se describe en una oración: “se reescribió la frase inicial del README para expresar el objetivo comercial”. → `CAP05_E03.txt`

### 5.4 · Determinar criterios de trazabilidad
- **Qué se hizo:** [fichas/tabla_cambios.md](../fichas/tabla_cambios.md) con columnas fecha, motivo, archivo, responsable y prueba (más commit e impacto); una fila para el cambio del README y otra para añadir datos de ejemplo; convención de nombres de commit.
- **Resultado observado:** 2 registros; `git show --stat HEAD` confirma que el commit del README toca solo ese archivo.
- **Comprobación:** ambos registros explican su impacto en el caso (decisión de gerencia y pruebas sin tocar la base). → `CAP05_E04.txt`

### 5.5 · Simular una recuperación de versión
- **Qué se hizo:** respaldo y copia del README fuera del repositorio; en la copia se cambió el título a “… – BORRADOR”; se compararon con `diff`; se restituyó el título desde el respaldo.
- **Resultado observado:** `diff` mostró solo la línea 1; tras restituir, `diff` y `cmp` sin diferencias.
- **Comprobación:** la copia final coincide con el respaldo y con `README.md` del repositorio. → `CAP05_E05.txt`

## Retos

### Reto 5.1 · Tres situaciones donde Git evita pérdidas o ambigüedades
- **Resultado obtenido:** sección “Reto 5.1” de la bitácora: ediciones simultáneas, CSV con filas faltantes y versión entregada a gerencia.
- **Cómo lo comprobé:** la segunda situación se respaldó con datos reales del repositorio: `git log -- data/ventas.csv` identifica el único commit que introdujo el CSV y `git show HEAD~1:data/ventas.csv` recupera sus 12 registros. → `CAP05_R01.txt`

### Reto 5.2 · Bitácora de cuatro cambios planificados
- **Resultado obtenido:** tabla de 4 cambios (JSON con LF, CSV de muestra, prueba con la muestra, encabezado del tablero) con commit previsto y criterio de aceptación verificable; se ejecutarán en los Cap. 06-08.
- **Cómo lo comprobé:** cada criterio se puede validar con un comando (`git status`, `unittest`) o con el archivo. → `CAP05_R02.txt`

### Reto 5.3 · Dibujo: cambio que existe pero no pertenece al historial
- **Resultado obtenido:** diagrama en la bitácora con los estados `??`/`M` → `A` → commit.
- **Cómo lo comprobé:** con `nota_temporal.txt`: `??` en disco, `A` preparado y 0 commits que lo contengan; se retiró con `git restore --staged` y se borró. → `CAP05_R03.txt`

## Actualización del Capítulo 02
La autenticación de dos factores se activó de forma real; el ejemplo 2.3 deja de ser simulación y se agrega la captura `evidencias/CAP02_2FA.png` (sin códigos visibles).

Pruebas del proyecto tras el capítulo: 4 de 4 correctas → `CAP05_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 06:** ejecutar el cambio planificado n.º 1 (JSON con finales de línea LF) junto con un `.gitattributes`, para que la configuración del entorno evite diferencias falsas entre Windows y GitHub Actions.
