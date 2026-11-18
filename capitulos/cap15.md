# Capítulo 15 · Revisión profesional de código

**Caso que continúa:** evaluar cambios con pruebas, trazabilidad y respeto a los colaboradores.
**Comandos de consulta:** `git diff main...feature/grafico-sedes` · `python -m unittest discover -s tests -v`
**Fecha:** 18/11/2026 · PR [#8](https://github.com/maxigva/andina-market-360/pull/8): `4120a55`, `11dda2e`, fusión `d5a5935`

> El cuaderno usa `feature/ficha-sedes` como ejemplo; esa rama ya se fusionó en el Cap. 14, así que la revisión se hizo sobre el nuevo PR #8 (`feature/grafico-sedes`, Issue #1).
> **Caso de práctica declarado:** el primer commit del PR se escribió **a propósito** con un título genérico (“Comparativo”) y una frase con una cifra fija, para que los ejemplos 15.2 y 15.4 y el Reto 15.2 revisen defectos reales dentro del flujo.

## Ejemplos resueltos

### 15.1 · Revisar un diff delimitado
- **Comando:** `git diff main...feature/grafico-sedes` (tres puntos: solo lo que agrega la rama).
- **Resultado observado:** 1 archivo (`docs/index.html`, +10 líneas). Clasificación: 3 líneas de **estilo**, 6 de **código**, 1 con **datos escritos** (`S/ 814.00`); 0 cambios en `data/`, `tests/` y documentación.
- **Comprobación:** el objetivo de #1 (3 barras proporcionales con cifras del JSON) se verificó ejecutando `grafico()` en Node: anchos 100 / 68.2 / 58.5 %. → `evidencias/cap15/CAP15_E01.txt`

### 15.2 · Solicitar una corrección reproducible
- **Qué se hizo:** comentario en línea (línea 31 de `docs/index.html`) sobre el título ambiguo “Comparativo”, con el texto corregido propuesto (`Ventas por sede (S/, datos ficticios)`), el archivo y la función exactos, y la evidencia pedida (captura del tablero y pruebas sin errores).
- **Comprobación:** el comentario es específico (archivo, línea, texto) y respetuoso (describe el problema, no a la persona). → `CAP15_E02_E04.txt`

### 15.3 · Comprobar las pruebas del cambio
- **Comando:** `python -m unittest discover -s tests` en la rama del PR y `gh pr checks 8`.
- **Resultado observado:** **6 pruebas, 0 fallidas**, CI en verde. Diagnóstico importante: las pruebas pasaban **aunque** había una cifra fija, porque ninguna revisaba el HTML. Aprobar por “CI verde” habría dejado pasar el error.
- **Comprobación:** el diagnóstico se basa en la salida completa de `unittest`, no en capturas. → `CAP15_E03.txt`

### 15.4 · Distinguir observación y bloqueo
- **Comentario bloqueante:** `Lima lidera con S/ 814.00.` escrito a mano → clasificado como **error de cálculo**. Criterio para resolverlo: sede líder calculada desde los datos y `grep -nE "S/ [0-9]" docs/index.html` = 0 líneas.
- **Comentario sugerido:** mostrar el porcentaje en cada barra (no bloqueante).
- **Comprobación:** ambos siguen la [guía de revisión](../fichas/guia_revision.md), la misma con la que se revisaron los PR #6 y #7 (categorías de bloqueo: error de cálculo, filtración, prueba rota). → `CAP15_E02_E04.txt`

### 15.5 · Cerrar una revisión de forma trazable
- **Qué se hizo:** el autor respondió con `11dda2e` (título con unidad, líder calculado y prueba nueva `test_tablero_sin_cifras_escritas_a_mano`). Se comparó el archivo corregido: la prueba **falla** con `4120a55` y **pasa** con `11dda2e`; con el CSV modificado, la nota cambia a `S/ 5564.00`, igual que la barra.
- **Resultado observado:** se marcaron como resueltos **solo** los 2 hilos atendidos; el de la sugerencia quedó abierto con respuesta. Fusión `d5a5935`; Issue #1 cerrado con sus 5 criterios.
- **Comprobación:** ficha con fecha, PR, pruebas y decisión final en [fichas/revision_prs.md](../fichas/revision_prs.md). → `CAP15_E05.txt`, `CAP15_E05_correccion.txt`

## Retos

### Reto 15.1 · Guía de revisión con diez preguntas
- **Resultado obtenido:** [fichas/guia_revision.md](../fichas/guia_revision.md): 10 preguntas para un dashboard de ventas, cada una con su comprobación y la consecuencia si falla (bloqueo, corrección o sugerencia).
- **Cómo lo comprobé:** se aplicó completa al PR #8; las preguntas 2 y 5 detectaron los dos defectos.

### Reto 15.2 · Revisar un cambio que introduce una cifra fija
- **Resultado obtenido:** el commit `4120a55` introducía `S/ 814.00` en el HTML. **Riesgo:** al cambiar el CSV, las barras se actualizan pero la frase no, y el tablero se contradice ante gerencia. Las pruebas no lo detectan y la cifra parece correcta hasta que cambian los datos.
- **Cómo lo comprobé:** en una copia, fila 1 = 200 unidades → barra de Lima `S/ 5564.00` y nota `S/ 814.00`. Corrección: cálculo desde los datos + prueba automática que impide cifras fijas (las pruebas pasan de 6 a **7**). → `CAP15_R02.txt`

### Reto 15.3 · Comentario de revisión reproducible sin ambigüedad
- **Resultado obtenido:** el comentario de bloqueo del PR #8 indica la línea, el problema, los pasos exactos (archivo, fila, valor, comando), el resultado esperado y el criterio de cierre con un comando.
- **Cómo lo comprobé:** al seguir los pasos tal como están escritos se obtiene exactamente lo descrito (`S/ 5564.00` frente a `S/ 814.00`). → `CAP15_R03.txt`

Pruebas del proyecto tras el capítulo: 7 de 7 correctas → `CAP15_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 16:** ampliar `CONTRIBUTING.md` con lo aprendido de proyectos públicos (Issue previo al cambio, pruebas exigidas, plantillas) y con la guía de revisión.
