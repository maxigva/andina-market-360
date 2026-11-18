# Capítulo 08 · Trabajo con ramas o branches

**Caso que continúa:** desarrollar mejoras independientes del tablero comercial sin modificar `main`.
**Comandos de consulta:** `git switch -c feature/resumen-sedes` · `git switch main` · `git merge feature/resumen-sedes`
**Fecha:** 17/11/2026

## Ejemplos resueltos

### 8.1 · Crear una rama de mejoras
- **Qué se hizo:** desde `main` limpio, `git switch -c feature/resumen-sedes`; en el README se describió que el informe muestra primero las ventas por sede.
- **Resultado observado:** commit `5920dd3 docs: describir informe de ventas por sede`.
- **Comprobación:** `git branch --show-current` → `feature/resumen-sedes`; `git log -1 --oneline` → `5920dd3`. → `evidencias/cap08/CAP08_E01.txt`

### 8.2 · Construir una mejora aislada
- **Qué se hizo:** en la misma rama, `docs/index.html` pasó a titularse “Andina Market 360 · Tablero de ventas por sede” (`<title>` y `<h1>`); `git commit -am "feat: nombrar tablero de sedes"` → `2e67da0`.
- **Comprobación:** `git show main:docs/index.html` conserva `<h1>Andina Market 360</h1>`; `data/` es idéntica en ambas ramas. → `CAP08_E02.txt`

### 8.3 · Fusionar la mejora comprobada
- **Comandos:** `git switch main` y `git merge --no-ff feature/resumen-sedes` (se usó `--no-ff` para que la integración se vea en el gráfico).
- **Resultado observado:** commit de fusión `2ca7096`; `git log --oneline --graph -5` muestra la rama y su unión.
- **Comprobación:** el nuevo encabezado y la frase de ventas por sede ya están en `main`. → `CAP08_E03.txt`

### 8.4 · Probar una segunda rama de corrección
- **Qué se hizo:** `git switch -c fix/encabezado-tablero` desde `main`. Tras renombrar el tablero, el encabezado `## Uso del tablero` del README quedó impreciso; se corrigió a `## Uso del tablero de ventas por sede` (`f70b537`) y se fusionó en `main` (`ff14b35`).
- **Comprobación:** 5 pruebas OK y total S/ 1845.00: el ajuste documental no afectó el análisis. → `CAP08_E04.txt`

### 8.5 · Eliminar ramas terminadas
- **Comandos:** `git branch --merged main` → `feature/resumen-sedes` y `fix/encabezado-tablero`; `git branch -d feature/resumen-sedes`.
- **Resultado observado:** `Deleted branch feature/resumen-sedes (was 2e67da0)`; quedan `main` y las ramas aún activas. Al cerrar el capítulo también se retiró `fix/encabezado-tablero`, ya integrada; se conserva `feature/filtro-productos` porque sigue en desarrollo.
- **Comprobación:** → `CAP08_E05.txt`

## Retos

### Reto 8.1 · Rama `feature/filtro-productos` con un cambio documental
- **Resultado obtenido:** [fichas/propuesta_filtro_productos.md](../fichas/propuesta_filtro_productos.md) con necesidad, alcance y criterios de aceptación; commit `bac3c40 docs: proponer filtro por producto`. La rama **no** se fusiona: se publica para revisarla con un pull request en el Cap. 14.
- **Cómo lo comprobé:** `git log main..feature/filtro-productos` muestra exactamente ese commit. → `CAP08_R01.txt`

### Reto 8.2 · Integrar una corrección sin perder su historial
- **Resultado obtenido:** la corrección `f70b537` se integró con `--no-ff`, así que el commit original y su fusión `ff14b35` quedan visibles en el gráfico.
- **Cómo lo comprobé:** `git log --oneline --graph -9` y búsqueda del mensaje `fix:` en `main`. → `CAP08_R02.txt`

### Reto 8.3 · Archivos modificados al cambiar de rama
- **Resultado obtenido:**
  | Caso | Qué pasó |
  |---|---|
  | A. `README.md` modificado, idéntico en `main` y en `feature/filtro-productos` | `git switch` funcionó y la modificación **viajó** con la terminal a la otra rama (` M README.md` en ambas) |
  | B. `fichas/propuesta_filtro_productos.md` modificado, existe solo en una rama | Git **se negó** a cambiar de rama (*would be overwritten by checkout*, código 1) para no perder el trabajo |
- **Cómo lo comprobé:** salidas de `git status` antes y después de cada `git switch`; ambos cambios de prueba se descartaron con `git restore`. → `CAP08_R03.txt`

Pruebas del proyecto tras el capítulo: 5 de 5 correctas → `CAP08_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 09:** publicar `main` y la rama `feature/filtro-productos` en GitHub, y revisar con `git fetch` antes de integrar cualquier cambio remoto.
