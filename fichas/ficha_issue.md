# Ficha de un Issue público (Reto 3.3)

| Campo | Contenido |
|---|---|
| Repositorio | cli/cli |
| Issue | #14692 – “gh issue view --comments omits the issue body when stdout is not a TTY” |
| Enlace | https://github.com/cli/cli/issues/14692 |
| Abierto | 14/10/2026 |
| Etiquetas | `bug`, `priority-3`, `help wanted`, `gh-issue` |
| Estado | **Cerrado como completado** el 16/10/2026 |

## Pasos para reproducir (resumidos del reporte)
1. Elegir un issue con cuerpo y al menos un comentario.
2. `gh issue view <N> --comments | grep -c "<línea del cuerpo>"` → `0` (el cuerpo no aparece al redirigir la salida).
3. `gh issue view <N> --json body --jq .body | grep -c "<misma línea>"` → `1`.
4. En una terminal interactiva el cuerpo sí aparece.

## Evidencias aportadas en el reporte
- Versión exacta (`gh version 2.97.0`) y sistema operativo.
- Comparación entre resultado esperado y obtenido.

## Resolución
El equipo mantenedor explicó que el comportamiento era intencional y que cambiarlo rompería scripts existentes; aceptó en cambio aclarar el texto de ayuda. El issue se cerró con el comentario “Fixed by https://github.com/cli/cli/pull/14714”.

Aprendizaje: un reporte con pasos numerados y salida esperada se resolvió en 2 días.
