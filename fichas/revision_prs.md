# Registro de revisiones de pull requests (Capítulo 14)

> El repositorio tiene un solo titular. GitHub no permite aprobar ni “solicitar cambios” en un PR propio (*Can not approve / request changes on your own pull request*), así que las revisiones se publicaron como **comentario de revisión** con un rol simulado, y la decisión se registra aquí.

## PR #6 – feat: presentar sedes y origen ficticio en el tablero (atiende #3)
| # | Sugerencia | Tipo | Decisión | Cómo se atendió |
|---|---|---|---|---|
| 1 | Agregar el período del informe, calculado de `por_mes` | Exactitud (bloqueante) | Aceptada | Commit `56098bf`: *Período: 2026-01 a 2026-03* |
| 2 | *Files changed* mostraba 17 archivos | Alcance (bloqueante) | Aceptada | Se publicó `main` (`be39dd0`); como GitHub no recalculó la base, se cambió la base del PR y se devolvió a `main` → 1 archivo |
| 3 | Destacar visualmente el subtítulo | Presentación | Pospuesta | Se tratará con el gráfico de #1 para no ampliar el PR |

Resultado: fusionado (`a61b4dd`) con CI en verde, sin conflictos; Issue #3 cerrado con evidencia.

## PR #7 – docs: proponer filtro por producto (refs #4)
| # | Sugerencia | Decisión | Cómo se atendió |
|---|---|---|---|
| 1 | Definir el comportamiento con un producto inexistente (mensaje y código 1) | Aceptada | Commit `db08c08` |
| 2 | Enlazar la pregunta de gerencia y el Issue #4 | Aceptada | Commit `db08c08` |

Aprobación fundamentada: los 5 criterios del PR se cumplen; no introduce código ni cifras fijas. Fusionado (`3454b08`). El Issue #4 sigue abierto porque la implementación es otro trabajo.
