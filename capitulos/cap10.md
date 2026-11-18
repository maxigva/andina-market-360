# Capítulo 10 · Resolución de conflictos e historial

**Caso que continúa:** practicar restauración y conflictos en ramas descartables del repositorio.
**Comandos de consulta:** `git status` · `git reflog -5` · `git revert <HASH_DE_COMMIT>`
**Fecha:** 18/11/2026 · Ramas de laboratorio: `prueba/alternativa-a`, `prueba/alternativa-b`, `laboratorio/revertir` (ninguna se fusiona en `main`)

## Ejemplos resueltos

### 10.1 · Provocar un conflicto controlado
- **Qué se hizo:** desde `main` limpio (`c2d9f70`) se crearon dos ramas que cambian la **misma línea** (título del README):
  - `prueba/alternativa-a` → “# Andina Market 360 · Tablero comercial” (`203f759`).
  - `prueba/alternativa-b` → “# Andina Market 360 · Resumen de ventas por sede” (`6141206`).
- **Comando:** en `prueba/alternativa-b`, `git merge prueba/alternativa-a`.
- **Resultado observado:** `CONFLICT (content): Merge conflict in README.md`, código 1, estado `UU README.md`.
- **Comprobación:** el archivo conserva **ambos** textos entre los marcadores; no se borró ninguno. → `evidencias/cap10/CAP10_E01.txt`

### 10.2 · Resolver marcadores de conflicto
- **Qué se hizo:** se eliminaron `<<<<<<<`, `=======` y `>>>>>>>` y se escribió un título que integra el requisito correcto del dashboard: **“# Andina Market 360 · Tablero comercial de ventas por sede”**. Luego `git add README.md` y `git commit` para cerrar la fusión.
- **Resultado observado:** commit de fusión `15e7efb`; `git status` limpio.
- **Comprobación:** 0 marcadores restantes. → `CAP10_E02.txt`

### 10.3 · Revertir un commit sin borrar historia
- **Qué se hizo:** en `laboratorio/revertir` se creó el commit aislado `87d8676` con una frase temporal; se identificó con `git log -2 --oneline` y se ejecutó `git revert --no-edit 87d8676`.
- **Resultado observado:** nuevo commit `51c8258 Revert "docs: agregar frase temporal de laboratorio"`; la frase ya no está en el README.
- **Comprobación:** el historial conserva el commit original **y** el que lo deshace: trazabilidad completa. → `CAP10_E03.txt`

### 10.4 · Guardar cambios temporalmente
- **Qué se hizo:** en `main`, borrador sin confirmar en el README → `git stash push -m "borrador de notas"`.
- **Resultado observado:** estado limpio; se cambió a `laboratorio/revertir` y se volvió a `main`; `git stash list` → `stash@{0}: On main: borrador de notas`; `git stash pop`.
- **Comprobación:** el borrador reapareció; `stash pop` devolvió 0, **sin conflicto**; quedaron 0 stashes. Después el borrador se descartó a propósito con `git restore`, porque era de práctica. → `CAP10_E04.txt`

### 10.5 · Recuperar una referencia por reflog
- **Qué se hizo:** en la rama de laboratorio, con dos commits pequeños (`87d8676` y `51c8258`), se ejecutó `git reflog -5` y se inspeccionó `git show --stat 87d8676`.
- **Resultado observado:** el reflog muestra el `revert` y los cambios de rama; `87d8676` existe y se puede consultar.
- **Punto de recuperación registrado:** `87d8676` (frase temporal) y `51c8258` (estado revertido). No se ejecutó `reset --hard`; el árbol quedó con 0 cambios tras inspeccionar. → `CAP10_E05.txt`

## Retos

### Reto 10.1 · Crear y resolver un conflicto sin perder ambos mensajes
- **Resultado obtenido:** la fusión `15e7efb` une las dos ramas; el gráfico muestra los dos commits con sus mensajes (“titular README como tablero comercial” y “… como resumen de ventas por sede”) y el título final combina ambas ideas.
- **Cómo lo comprobé:** `git log --graph -4 prueba/alternativa-b`, búsqueda de los dos mensajes y pruebas en OK. → `CAP10_R01.txt`

### Reto 10.2 · Anular un commit temporal con `git revert` y explicar el historial final
- **Resultado obtenido:** `laboratorio/revertir` tiene 2 commits más que `main` (`87d8676` y su reversión `51c8258`), pero la diferencia neta de archivos con `main` es **0**.
- **Explicación del historial:** `revert` no borra: agrega un commit inverso. Quien lea el historial ve qué se agregó, cuándo y que luego se deshizo (*This reverts commit 87d8676…*). Por eso es la forma segura de deshacer en ramas ya publicadas, a diferencia de `reset`, que reescribe. → `CAP10_R02.txt`

### Reto 10.3 · Ubicar un estado anterior con `git reflog` sin comandos destructivos
- **Resultado obtenido:** `git reflog main` muestra cada movimiento de `main`; el estado previo al `pull` del Cap. 09 es `main@{2}` = `fb37469`. Con `git show fb37469:README.md` se comprobó que en ese estado aún no existía la frase añadida desde GitHub.
- **Cómo lo comprobé:** solo se usaron `reflog` y `show`; `HEAD` siguió en `c2d9f70`. Si hiciera falta recuperarlo, bastaría `git switch -c recuperado fb37469`, que tampoco destruye nada. → `CAP10_R03.txt`

## Ramas publicadas
Se publican `prueba/alternativa-b` (incluye la rama *a* y la resolución del conflicto) y `laboratorio/revertir` como evidencia visible. `prueba/alternativa-a` se elimina en local porque ya está contenida en *b*. Ninguna se fusiona en `main`.

Pruebas del proyecto tras el capítulo: 5 de 5 correctas → `CAP10_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 11:** revisar los diffs y resolver conflictos desde la interfaz gráfica de Visual Studio Code, comparando con lo hecho aquí en la terminal.
