# Tablero de tareas – Andina Market 360

> GitHub Projects requiere el permiso `project` en el token de GitHub CLI, que la cuenta no tiene habilitado. No se ampliaron permisos (regla del caso), así que el tablero se lleva en esta tabla local, enlazada a Issues reales.

## Clasificación con etiquetas (Ejemplo 13.3)
| Issue | Etiquetas | Impacto para la empresa |
|---|---|---|
| [#1](https://github.com/maxigva/andina-market-360/issues/1) feat: gráfico de ventas por sede | `mejora` | Gerencia identifica la sede líder sin leer cifras una por una |
| [#2](https://github.com/maxigva/andina-market-360/issues/2) bug: cifra incorrecta tras editar CSV | `error`, `prioridad-alta` | La web podía mostrar un total distinto al del CSV: decisión basada en un dato falso |
| [#3](https://github.com/maxigva/andina-market-360/issues/3) docs: presentar sedes, origen ficticio y período | `documentación` | Quien lee el tablero sabe qué cubre y que los datos son simulados |
| [#4](https://github.com/maxigva/andina-market-360/issues/4) feat: filtro por producto | `mejora` | Responde la pregunta 4 de gerencia (Leche 1L por sede) |
| [#5](https://github.com/maxigva/andina-market-360/issues/5) bug: verificador marca enlaces en código | `error` | Falsas alarmas en la documentación; no afecta cifras, por eso no es prioridad alta |

La etiqueta solo resume: cada Issue mantiene pasos, criterios y archivos en su descripción.

## Tablero de tres tareas (Ejemplo 13.4), estado real al cerrar el Capítulo 13
| Pendiente | En proceso | Terminado |
|---|---|---|
| #1 gráfico de ventas por sede | #3 sedes, origen y período (rama `feature/ficha-sedes`, Cap. 14) | #2 cifra incorrecta tras editar CSV |

Regla para mover una tarjeta a **Terminado**: todos los criterios del Issue marcados, commit referenciado, pruebas en `OK` y comentario de cierre con evidencia. Responsable de moverla: quien valida (desarrollo para errores, publicación para documentación). Ningún estado se asigna por opinión: Pendiente = sin rama; En proceso = rama o PR abierto; Terminado = Issue cerrado con evidencia.

## Tablero de ocho tareas con prioridades (Reto 13.2)
| # | Tarea | Estado | Prioridad | Justificación |
|---|---|---|---|---|
| 1 | #2 JSON publicado desactualizado | Terminado | Alta | Afectaba la cifra que ve gerencia |
| 2 | #5 Falso positivo del verificador Markdown | Terminado | Baja | Solo documentación; ya corregido |
| 3 | #3 Sedes, origen ficticio y período en el tablero | En proceso | Alta | Evita interpretar datos simulados como reales |
| 4 | #1 Gráfico de ventas por sede | Pendiente | Media | Mejora la lectura; las cifras ya están en tablas |
| 5 | #4 Filtro por producto | Pendiente | Media | Responde una pregunta nueva de gerencia; requiere código y prueba |
| 6 | Ejecutar `tools/verificar_md.py` en CI | Pendiente | Media | Evita enlaces rotos sin depender de la revisión manual (Cap. 22) |
| 7 | Publicar el tablero con GitHub Pages | Pendiente | Media | Acceso de gerencia sin clonar el repositorio (Cap. 19) |
| 8 | Proteger `main` con revisión obligatoria | Pendiente | Baja | Hoy hay un solo colaborador; será necesaria al sumar personas (Cap. 17/27) |

Orden de prioridad: primero lo que puede mostrar **cifras incorrectas** (alta), luego lo que mejora la lectura o el proceso (media) y al final la gobernanza que aún no tiene impacto con un solo colaborador (baja).
