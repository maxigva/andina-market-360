# Ficha del repositorio remoto (Capítulo 09)

| Campo | Valor |
|---|---|
| Nombre del remoto | `origin` (único; no se duplicó) |
| URL de fetch y push | `https://github.com/maxigva/andina-market-360.git` |
| Credenciales en la URL | Ninguna: la autenticación la gestiona el gestor de credenciales de Git / GitHub CLI, fuera del repositorio |
| Ramas publicadas | `main` (con seguimiento `origin/main`) y `feature/filtro-productos` |
| Repositorio que recibe los cambios | El de la cuenta propietaria del caso; ningún repositorio de terceros |

## Flujo acordado
1. `git fetch origin` → revisar `git log --oneline HEAD..origin/main`.
2. Si no hay divergencias: `git pull --ff-only origin main`.
3. Probar (`python -m unittest discover -s tests -v`) y luego `git push`.
4. Nunca `git push --force` sobre `main` compartido (ver Reto 9.3). Si una corrección lo exigiera, solo con autorización expresa y `--force-with-lease` apuntando al hash esperado.
