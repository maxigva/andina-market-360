# Comparación de dos repositorios públicos (Reto 3.2)

| Criterio | `github/docs` | `git/git-scm.com` |
|---|---|---|
| Claridad del README | README.md de 2 329 bytes: breve, remite a guías de contribución separadas | README.md de 14 406 bytes: explica instalación local, estructura y despliegue en el mismo archivo |
| Licencia | Creative Commons Attribution 4.0 (según la API) | MIT |
| Historial | ≈ 63 300 commits, actividad diaria y muchos commits automáticos | ≈ 3 850 commits, cambios más espaciados y legibles |
| Fortaleza | Muy activo; separa README y CONTRIBUTING | Todo lo necesario para ejecutar está en un solo lugar |
| Lo que adoptamos | Archivos de colaboración separados (Cap. 16-17) | README con pasos verificables de ejecución (Cap. 04) |

Datos obtenidos con `gh repo view`, `gh api repos/<repo>/readme` y el encabezado de paginación de `gh api repos/<repo>/commits?per_page=1` (número de la última página = cantidad aproximada de commits).
