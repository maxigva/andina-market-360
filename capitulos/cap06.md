# Capítulo 06 · Instalación y configuración de Git

**Caso que continúa:** construir el entorno local de trabajo con seguridad y sin credenciales en archivos.
**Comandos de consulta:** `git --version` · `git init -b main` · `git config --local user.name "Estudiante"`
**Fecha:** 17/11/2026 · Commits: `902b0ac fix: escribir el JSON con finales de línea LF` y `docs: documentar capítulo 06`

## Cambio en el proyecto (mejora planificada en el Cap. 05)
- `src/resumen.py` escribe el JSON con `newline="\n"` y salto final; `.gitattributes` normaliza el texto (`* text=auto`), fija `docs/data/*.json` en LF y marca PNG/PDF como binarios.
- Verificación: `git ls-files --eol` → `i/lf w/lf attr/text eol=lf`; regenerar el JSON dos veces no deja cambios del proyecto en `git status` (la única entrada era la carpeta de evidencias que se estaba escribiendo). → `evidencias/cap06/CAP06_fix_json.txt`

## Ejemplos resueltos

### 6.1 · Verificar la instalación
- **Comando:** `git --version` en Git Bash, dentro de `C:\andina-market-360`.
- **Resultado observado:** `git version 2.55.0.windows.4`, código de salida 0.
- **Comprobación:** la salida no contiene credenciales (0 coincidencias). → `CAP06_E01.txt`

### 6.2 · Establecer identidad para el repositorio
- **Qué se hizo:** se verificó la identidad **local** del caso (ya configurada): `Estudiante` / `estudiante@example.com`. No se tocó la configuración global.
- **Comando:** `git config --local --list`
- **Resultado observado:** ambas entradas `user.*` presentes; la configuración local solo tiene datos de repositorio y remoto.
- **Comprobación:** 0 claves con token, contraseña o *credential*; no se copiaron datos reales. → `CAP06_E02.txt`

### 6.3 · Inicializar el repositorio local
- **Qué se hizo:** copia nueva del proyecto base (extraída con `git archive` del commit inicial `a336325`) en una carpeta de práctica **sin** `.git`; `git init -b main`.
- **Resultado observado:** `Initialized empty Git repository`, `On branch main`, `No commits yet`.
- **Comprobación:** rutas registradas en la bitácora (sección “Entorno local”). → `CAP06_E03.txt`

### 6.4 · Crear el primer commit local
- **Qué se hizo:** revisión de `.gitignore` y `git add README.md data/ src/ tests/ docs/ .gitignore`; commit `chore: iniciar caso Andina Market`.
- **Resultado observado:** 7 archivos preparados; `git log -1 --oneline` → **`d8db55b`**. `.github/` quedó fuera porque no estaba en la lista del ejemplo (se ve como `??`).
- **Comprobación:** → `CAP06_E04.txt`

### 6.5 · Clonar un repositorio de aprendizaje
- **Comando:** desde la carpeta superior, `git clone ./andina-market-360 ./andina-market-copia`, sin red.
- **Resultado observado:** la copia está en `main`, *up to date with origin/main*; `git log -1` → `d8db55b` en ambos.
- **Comprobación:** mismo hash; el `origin` de la copia apunta a la ruta local de origen. → `CAP06_E05.txt`

## Retos

### Reto 6.1 · Git instalado y versión documentada
- **Resultado obtenido:** Git for Windows 2.55.0 (x86_64) en `C:\Program Files\Git`.
- **Cómo lo comprobé:** `git --version` y `git --version --build-options`. → `CAP06_R01.txt`

### Reto 6.2 · Identidad de un repositorio de práctica
- **Resultado obtenido:** en la práctica se configuró `Estudiante Práctica` / `practica@example.com` con `--local`.
- **Cómo lo comprobé:** `git config --local --list | grep ^user` y `git config user.email` devuelven los valores; el repositorio del caso conserva `estudiante@example.com`, lo que demuestra que `--local` no afecta a otros repositorios. → `CAP06_R02.txt`

### Reto 6.3 · Clon local del caso con historial idéntico
- **Resultado obtenido:** clon de `C:\andina-market-360` con 17 commits y `HEAD` `902b0ac`.
- **Cómo lo comprobé:** `diff` de la lista completa de hashes de ambos repositorios sin diferencias. → `CAP06_R03.txt`

Pruebas del proyecto tras el capítulo: 4 de 4 correctas → `CAP06_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 07:** ejecutar los cambios planificados n.º 2 y 3 (CSV de muestra y su prueba) como commits separados de datos y de prueba.

> Nota de privacidad: en las evidencias, la ruta de la carpeta temporal se reemplazó por `<TEMP>` porque incluye el nombre de usuario del sistema.
