# Seguimiento de una conversación técnica (Ejemplo 3.4)

**Issue:** cli/cli #14814 – “`gh auth status --no-refresh` shows a misleading error for expired tokens”
**Enlace:** https://github.com/cli/cli/issues/14814
**Estado:** cerrado como completado (26/10/2026) · Etiquetas: `bug`, `priority-3`, `gh-auth`

## Cronología: problema → debate → solución
| Fecha | Etapa | Qué ocurrió (según el hilo público) |
|---|---|---|
| 24/10/2026 | Problema | Quien reportó explica que, con un token que expira, `gh auth status --no-refresh` dice “The token in keyring is invalid” y sugiere un comando inadecuado, aunque el token solo había expirado y se renueva solo. Incluye versión, pasos y salida esperada vs. obtenida. |
| 24/10/2026 | Debate | El comentario de triaje revisa `pkg/cmd/auth/status/status.go` y confirma que la hipótesis del reporte es correcta. |
| 26/10/2026 | Solución | Se fusiona el PR #14815 “fix(gh auth status): explain expired expiring tokens with `--no-refresh`”. |
| 26/10/2026 | Cierre | El issue se cierra automáticamente al fusionarse el PR (dos segundos después). |

## ¿Qué información faltó para resolverlo más rápido?
Casi nada: el reporte ya traía versión, pasos numerados y salidas. Lo único ausente fue **una prueba automática que reprodujera el caso**, que tuvo que escribirse en el PR. Para Andina Market 360: cada reporte de error debe indicar el comando, la salida esperada y la obtenida.

> Las opiniones citadas pertenecen a participantes del hilo público; ninguna se atribuye al equipo de Andina Market 360.
