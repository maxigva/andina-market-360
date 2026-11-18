# Capítulo 11 · GitHub Desktop y Visual Studio Code

**Caso que continúa:** usar herramientas gráficas para el mismo flujo local de commits y ramas.
**Rutas de consulta:** GitHub Desktop: Repository → Add local repository · VS Code: File → Open Folder → Source Control
**Fecha:** 18/11/2026 · Commits: `91920bd docs: explicar procedencia ficticia`, `d6f5ec2 docs: agregar pregunta para gerencia` y `docs: documentar capítulo 11`

> **Entorno real:** VS Code 1.146 está instalado y es el editor configurado para Git (`core.editor = code --wait`). **GitHub Desktop no está instalado** (es opcional según el cuaderno), así que los pasos de Desktop se registran como **simulación local documentada**: se describe el clic exacto y se ejecuta la operación Git equivalente, que es la que Desktop realiza por debajo.

## Ejemplos resueltos

### 11.1 · Abrir el caso en GitHub Desktop
- **Procedimiento en Desktop (simulación documentada):** File → *Add local repository* → elegir `C:\andina-market-360` → *Current branch* muestra `main` → pestaña *Changes*.
- **Acción real:** se creó una nota de prueba (`nota_prueba.txt`) y se revisó el estado con `git status --short`, que es la misma lista que muestra *Changes*.
- **Resultado observado:** raíz `C:/andina-market-360`, rama `main`, 2 entradas (la nota y la carpeta de evidencias). La nota se borró después.
- **Comprobación:** → `evidencias/cap11/CAP11_E01.txt`

### 11.2 · Confirmar una edición gráfica
- **Qué se hizo:** desde el editor se añadió al README la procedencia del CSV (creado para el curso, con valores inventados). Se revisó el diff (equivalente al panel de diferencias de *Changes*) y se confirmó con el resumen `docs: explicar procedencia ficticia` (equivalente a *Commit to main*).
- **Resultado observado:** commit `91920bd`; aparece primero en el historial (equivalente a la pestaña *History*).
- **Comprobación:** → `CAP11_E02.txt`

### 11.3 · Crear una rama desde Desktop
- **Procedimiento en Desktop (simulación documentada):** *Current branch* → *New branch* → `feature/ficha-gerencia`.
- **Qué se hizo:** en la rama se registró una nueva pregunta para gerencia (*¿qué sede vende más Leche 1L?*). El cuaderno indica editar `proyecto.md`, pero ese archivo es del Capítulo 01 y se conserva sin cambios; la pregunta se registró en [fichas/ficha_gerencia.md](../fichas/ficha_gerencia.md). Commit `d6f5ec2`.
- **Resultado observado:** `git log main..feature/ficha-gerencia` mostraba exactamente ese commit; luego se integró con *fast-forward* y la rama se eliminó.
- **Comprobación:** → `CAP11_E03.txt` (captura del historial en VS Code: `CAP11_vscode.png`, pendiente)

### 11.4 · Examinar diferencias en Visual Studio Code
- **Procedimiento en VS Code:** File → Open Folder → `C:\andina-market-360` → *Source Control* (Ctrl+Shift+G) → clic en `docs/index.html` para abrir la vista lado a lado.
- **Acción real:** se cambió una línea de `docs/index.html` (“Resumen generado **automáticamente** por…”), se comparó el diff y se verificó el HTML con un analizador de la biblioteca estándar.
- **Resultado observado:** 1 línea `-` y 1 línea `+`; HTML válido (etiquetas balanceadas). Se decidió **descartar** (*Discard Changes* = `git restore`), porque el cambio no aportaba información.
- **Comprobación:** tras descartar, el archivo sigue siendo válido y sin cambios. → `CAP11_E04.txt`

### 11.5 · Equivalencia interfaz-terminal
| GitHub Desktop / VS Code | Terminal | Ventaja de la interfaz | Limitación de la interfaz |
|---|---|---|---|
| *Commit to main* / ✓ Commit | `git commit -m "..."` | Muestra el diff junto al mensaje | Oculta opciones (fechas, `--amend` en ramas, firmas) |
| *Push origin* / Sync | `git push` | Un clic, indica cuántos commits se envían | No muestra qué ramas se publican si hay varias |
| *Pull origin* | `git pull` | Avisa cuando hay cambios remotos | No permite elegir `--ff-only` de forma visible |
| *Fetch origin* | `git fetch` | Actualiza contadores sin tocar archivos | Se ejecuta en segundo plano sin dejar registro |

- **Comprobación:** `git log --oneline -3` coincide con lo que mostraría *History*; `main...origin/main [ahead 2]` y `fetch --dry-run` sin novedades. No se hicieron cambios remotos innecesarios. → `CAP11_E05.txt`

## Retos

### Reto 11.1 · Dos commits, uno con Desktop y otro con la terminal
- **Resultado obtenido (simulación documentada para Desktop):** al no contar con Desktop, se compararon los objetos de los dos commits del capítulo con `git cat-file -p`. Ambos tienen la misma estructura: `tree`, `parent`, `author`, `committer` y mensaje. Desktop produce el mismo tipo de objeto con la identidad configurada en Git; la diferencia está en el proceso (selección visual de archivos), no en el resultado.
- **Cómo lo comprobé:** → `CAP11_R01.txt`

### Reto 11.2 · Rama creada en la interfaz y activada desde la terminal
- **Resultado obtenido:** la rama `feature/ficha-gerencia` (creación equivalente a *New branch*) se activó desde la terminal con `git switch feature/ficha-gerencia`; `git branch --show-current` lo confirmó.
- **Cómo lo comprobé:** → `CAP11_R02.txt`

### Reto 11.3 · Localizar y revertir una edición local con la vista de diferencias
- **Resultado obtenido:** dos ediciones accidentales (`docs/index.html` y `fichas/ficha_gerencia.md`) se localizaron en la vista de diferencias (`git diff --stat`) y se revirtieron archivo por archivo (*Discard Changes* = `git restore <archivo>`).
- **Cómo lo comprobé:** 0 cambios restantes y ningún commit afectado. → `CAP11_R03.txt`

Pruebas del proyecto tras el capítulo: 5 de 5 correctas → `CAP11_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 12:** reorganizar el README con secciones Objetivo, Datos y Ejecución, y mover el detalle técnico a un manual enlazado para que la portada sea breve.
