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

## PR #8 – feat: graficar ventas por sede (atiende #1) · Capítulo 15
| Campo | Valor |
|---|---|
| Fecha de revisión | 18/11/2026 |
| Commits revisados | `4120a55` (versión inicial) y `11dda2e` (corrección) |
| Guía aplicada | [guia_revision.md](guia_revision.md) |
| Pruebas | Versión inicial: `Ran 6 tests OK` (no detectaban la cifra fija). Corrección: `Ran 7 tests OK`; CI en verde |

| Hilo | Tipo | Estado final | Motivo |
|---|---|---|---|
| Título “Comparativo” ambiguo | Corrección solicitada | Resuelto | Nuevo título con unidad, verificado |
| `Lima lidera con S/ 814.00.` escrito a mano | **Bloqueo** (error de cálculo) | Resuelto | Calculado desde los datos + prueba que impide cifras fijas |
| Porcentaje en cada barra | Sugerencia | **Abierto** (respondido) | Fuera del alcance de #1; no implementado |

**Decisión final:** aprobado y fusionado (`d5a5935`) tras resolver el bloqueo; la sugerencia queda abierta y documentada, sin ocultarla. Issue #1 cerrado con los 5 criterios marcados.
