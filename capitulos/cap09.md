# Capítulo 09 · Sincronización con repositorios remotos

**Caso que continúa:** vincular el proyecto local con un remoto real solo cuando el estudiante decida hacerlo.
**Comandos de consulta:** `git remote -v` · `git remote add origin https://github.com/USUARIO/andina-market-360.git` · `git push -u origin main`
**Fecha:** 17-18/11/2026 · Commits: `bd60f73 docs: aclarar que GitHub solo aloja el proyecto` (hecho en GitHub) y `docs: documentar capítulo 09`

## Ejemplos resueltos

### 9.1 · Examinar remotos existentes
- **Comando:** `git remote -v` y `git ls-remote --heads origin`.
- **Resultado observado:** `origin` → `https://github.com/maxigva/andina-market-360.git`; 0 credenciales en la URL. URL anotada en [fichas/remoto.md](../fichas/remoto.md).
- **Comprobación:** el repositorio que recibiría los cambios es el del caso; en GitHub `main` estaba en `44f5f4f` (fin del Bloque I). → `evidencias/cap09/CAP09_E01.txt`

### 9.2 · Vincular origin con una URL propia
- **Qué se hizo:** como `origin` ya existía, primero se comprobó su valor con `git remote get-url origin`. El intento de `git remote add origin ...` falló con `remote origin already exists` (código 3), que es lo esperado: no se duplican remotos.
- **Comprobación:** `git remote` → solo `origin` (1 remoto). → `CAP09_E02.txt`

### 9.3 · Publicar la rama principal
- **Comandos:** en `main` con árbol limpio, `git push -u origin main` y `git push -u origin feature/filtro-productos`.
- **Resultado observado:** `44f5f4f..fb37469 main -> main` y rama nueva publicada. Hash publicado: `fb37469a25003cd6afac3c79acf03b8f821408a9`, commit del 17/11/2026 23:58.
- **Comprobación:** fecha y hash registrados; no se guardaron credenciales ni códigos (la autenticación la resolvió el gestor de credenciales). → `CAP09_E03.txt`

### 9.4 · Obtener cambios hechos en el navegador
- **Qué se hizo:** en GitHub se editó una frase de “Uso responsable” del README (*GitHub solo aloja el código, las pruebas automáticas y la web*) y se guardó como commit en `main`. En local: `git pull --ff-only origin main`.
- **Resultado observado:** `Updating fb37469..bd60f73  Fast-forward`; `git log -2 --oneline` muestra `bd60f73` sobre `fb37469`.
- **Comprobación:** el blob de `README.md` en local es idéntico al de GitHub (`b28d3f9…`). → `CAP09_E04.txt`

### 9.5 · Inspeccionar antes de integrar
- **Comandos:** (antes del pull) `git fetch origin` y `git log --oneline HEAD..origin/main`.
- **Resultado observado:** 1 commit remoto nuevo (`bd60f73`); `main` local seguía en `fb37469` (`behind 1`). Decisión: integrar con fast-forward porque no había cambios locales divergentes.
- **Comprobación:** la huella de `README.md` fue la misma antes y después del fetch (`10d35b5a0487`): fetch no reescribe el directorio de trabajo. → `CAP09_E05.txt`

## Retos

### Reto 9.1 · Conectar una copia de práctica a un remoto propio
- **Resultado obtenido:** la copia de práctica del Cap. 06 (0 remotos) quedó con `origin` apuntando al repositorio propio.
- **Cómo lo comprobé:** `git remote -v` sin credenciales y `git ls-remote --heads origin` (solo lectura) lista `main` y `feature/filtro-productos`. No se hizo push desde la práctica porque su historial es distinto. → `CAP09_R01.txt`

### Reto 9.2 · Comparar `git fetch` con `git pull`
- **Resultado obtenido:**

  | | `git fetch origin` | `git pull --ff-only origin main` |
  |---|---|---|
  | Qué mueve | Solo `origin/main` (`fetch origin: fast-forward`) | `main` local (`pull --ff-only: Fast-forward`) |
  | Directorio de trabajo | Sin cambios (misma huella del README) | README actualizado con la frase de GitHub |
  | Riesgo | Ninguno; permite revisar antes | Integra; con `--ff-only` se detiene si hay divergencia |
- **Cómo lo comprobé:** reflog de `origin/main` y de `main`, más las evidencias E04 y E05. → `CAP09_R02.txt`

### Reto 9.3 · Por qué evitar un push forzado sobre `main` compartido
- **Resultado obtenido:** demostración en un remoto local descartable con dos clones (Ana y Beto, ficticios). El push normal de Beto, desactualizado, fue **rechazado** (*fetch first*); con `--force`, el remoto quedó sin el commit “aporte de Ana” (0 coincidencias).
- **Conclusión:** un push forzado reemplaza la historia que otros ya tienen: se pierde trabajo ajeno, los clones quedan divergentes y las referencias (PR, CI, tags) apuntan a commits que ya no están en la rama. Lo correcto es `git pull` (o `fetch` + `merge`/`rebase` local) y luego push normal; si alguna vez es imprescindible, `--force-with-lease` con el hash esperado y aviso al equipo.
- **Cómo lo comprobé:** → `CAP09_R03.txt`

## Incidencia y corrección autorizada
Para el ejemplo 9.4, la edición “en el navegador” se hizo con la API de contenidos de GitHub (equivalente a guardar desde el editor web). El primer intento creó el commit `a88eacf` con la **hora del servidor**, porque la API no aplicó la fecha enviada, y eso rompía el orden cronológico del historial del caso. Con autorización expresa se aplicó **una única** corrección: el mismo cambio (árbol idéntico) se confirmó como `bd60f73` y se publicó con `git push --force-with-lease=main:a88eacf`, que solo procede si `main` remoto sigue exactamente en el commit esperado. Ningún otro commit de `main` se reescribió. Es justo el caso del Reto 9.3: el push forzado solo es aceptable con aviso, autorización y `--force-with-lease`.

Pruebas del proyecto tras el capítulo: 5 de 5 correctas → `CAP09_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 10:** practicar conflictos, `revert` y `reflog` solo en ramas `prueba/` y `laboratorio/`, para que `main` publicado no se reescriba nunca.
