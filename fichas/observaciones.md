# Observaciones de la interfaz de GitHub (Capítulo 03)

> Recorrido de solo lectura. No se modificó ningún repositorio ajeno.

## 3.1 · Áreas esenciales y su uso en Andina Market 360
| Área (nombre visible) | Ruta | Uso concreto en el caso |
|---|---|---|
| Profile | `github.com/<usuario>` | Presentar el perfil del Cap. 02 y fijar el repositorio |
| Repositories | `github.com/<usuario>?tab=repositories` | Encontrar `andina-market-360` entre los repositorios |
| Pull requests | `github.com/pulls` | Ver las revisiones pendientes del caso |
| Issues | `github.com/issues` | Seguir las tareas asignadas (Cap. 13) |
| Search (barra superior, tecla `/`) | `github.com/search?q=...` | Buscar ejemplos de otros proyectos de ventas |

Ruta hacia cualquier repositorio público: **Search → escribir `propietario/nombre` → filtro *Repositories* → abrir el resultado → pestaña *Code***.

## 3.2 · Pestañas de un repositorio público: `github/docs`
URL: https://github.com/github/docs

| Pestaña | Función observada | Diferencia con Andina Market 360 |
|---|---|---|
| Code | Árbol de archivos y README renderizado | Allí miles de archivos de contenido; aquí 4 carpetas de proyecto |
| Issues | Reportes de la comunidad con plantillas y etiquetas | Nuestro caso aún no tiene issues ni plantillas (Cap. 13) |
| Pull requests | Cambios propuestos por colaboradores externos | En el caso, los PR los abrirá el mismo equipo (Cap. 14) |
| Actions | Decenas de workflows automáticos | Aquí un solo workflow (`ci.yml`) que corre las pruebas |
| Settings | **No visible**: solo aparece para quien administra el repositorio | En `andina-market-360` sí aparece porque la cuenta es propietaria |

## 3.3 · Búsqueda por tema: `topic:python sales dashboard`
Comando equivalente: `gh search repos "sales dashboard" --topic python`.

| Criterio | `yesdeepakmittal/Business_Dashboard` | `tushar2704/Superstore-Sales-Dashboard-with-Streamlit` |
|---|---|---|
| README / descripción | Descripción breve de una línea | Descripción extensa del objetivo |
| Lenguaje declarado | Python | No detectado |
| Licencia | MIT | No detectada → no se puede reutilizar sin permiso |
| Actividad (updatedAt) | 07/02/2026 | 06/11/2026 |
| Conclusión | Reutilizable como referencia por su licencia | Útil solo para leer ideas |

No se descargó ni ejecutó código de estos repositorios; solo se guardaron URLs públicas y conclusiones. Que un repositorio aparezca en la búsqueda no garantiza que sea seguro.

## 3.5 · Historial de cambios de `cli/cli`
URL: https://github.com/cli/cli/commits/trunk

| Commit | Autor público | Mensaje | Archivos | Finalidad observable |
|---|---|---|---|---|
| `8ad5fb5` (16/11) | babakks | Fix workflow log truncation after long lines | `pkg/cmd/run/view/view.go`, `view_test.go` | **Corrige un error** (salida de logs cortada) y añade su prueba |
| `f219d43` (13/11) | BagToad | Make triage formatting checks nonblocking | `.github/scripts/…`, `.github/workflows/issue-triage.*`, `docs/issue-triage.md` | **Mejora** del proceso de triaje, con prueba y documentación |
| `b13e6c6` (13/11) | dependabot[bot] | chore(deps): Bump golang.org/x/text from 0.43.0 to 0.44.0 | `go.mod`, `go.sum` | Mantenimiento: actualización automática de dependencia |

Lección para el caso: el commit que corrige un error modifica el código **y** su prueba; lo mismo exigiremos en Andina Market 360.
