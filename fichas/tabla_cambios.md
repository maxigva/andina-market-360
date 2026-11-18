# Tabla de cambios (trazabilidad)

| Fecha | Motivo | Archivo | Responsable | Prueba | Commit | Impacto en el caso |
|---|---|---|---|---|---|---|
| 17/11/2026 | La frase inicial no decía qué decisión comercial apoya el proyecto | `README.md` | Responsable de publicación | Revisión del diff (1 línea) + 4 pruebas OK | `docs: precisar objetivo comercial` | La gerencia entiende en una línea que el tablero responde “¿qué sede lidera?” |
| Planificado (Cap. 07) | Las pruebas solo usan el CSV completo; falta un caso pequeño y controlado | `data/ventas_muestra.csv` | Analista de datos | Nueva prueba con totales conocidos | `feat: agregar CSV de muestra para pruebas` | Permite verificar el cálculo sin modificar la base de 12 ventas que ve gerencia |

## Convención de nombres para futuras confirmaciones
`tipo: verbo en infinitivo + objeto`, en español y en minúsculas.
- `docs:` documentación · `feat:` funcionalidad nueva · `fix:` corrección · `test:` pruebas · `ci:` automatización · `chore:` mantenimiento · `refactor:` reorganizar código sin cambiar el resultado.
