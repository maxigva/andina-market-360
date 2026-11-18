# Capítulo 20 · Gestión de archivos y paquetes

**Caso que continúa:** controlar el tamaño del repositorio y preparar archivos distribuibles del dashboard.
**Comandos de consulta:** `git check-ignore -v dist/prueba.tmp` · `git lfs version`
**Fecha:** 18/11/2026 · Commits: `d7b6441 chore: excluir dist/ y agregar empaquetador de versiones`, `0f9b279 chore: ignorar claves privadas .pem y .key` y `docs: documentar capítulo 20`

## Ejemplos resueltos

### 20.1 · Auditar archivos pesados
- **Qué se hizo:** tamaño de cada carpeta versionada y de los 5 archivos más grandes.
- **Resultado observado:** los 5 mayores son capturas PNG de evidencias (de 106 KB a 217 KB). `data/` ocupa 688 bytes (`ventas.csv`, 495 bytes) y `docs/` 11 KB. No había exportaciones (`dist/` ni ZIP versionados).
- **Decisión:** se conservan todos en Git (código, datos ficticios y capturas son pequeños); los paquetes ZIP se distribuyen como adjunto de la Release, no en Git.
- **Comprobación:** el CSV didáctico sigue siendo pequeño y auditable a simple vista (12 filas, 495 bytes). → `evidencias/cap20/CAP20_E01.txt`

### 20.2 · Ampliar reglas de exclusión
- **Qué se hizo:** `.gitignore` ya tenía `.venv/`, `.env` y `*.tmp`; se agregó `dist/`. Se creó `dist/prueba.tmp`.
- **Resultado observado:** `git status --short` no propone el artefacto; `git check-ignore -v` → `.gitignore:20:dist/`.
- **Comprobación:** pruebas, documentación, CSV y herramientas siguen siendo versionables; lo ignorado se limita a `_material/`, `dist/` y cachés. → `CAP20_E02.txt`

### 20.3 · Simular un caso para Git LFS
- **Qué se hizo:** listado **hipotético** de imágenes y un video grandes (no se descargó nada) y análisis de cuándo conviene LFS y qué implica para colaboradores (instalar LFS, cuotas, `git lfs migrate` reescribe la historia), en [fichas/politica_archivos.md](../fichas/politica_archivos.md).
- **Resultado observado:** `git-lfs/3.7.1` instalado; 0 patrones seguidos, 0 archivos LFS, 0 filtros `lfs` en `.gitattributes`.
- **Comprobación:** no se convirtió ningún archivo por accidente; la decisión es **no usar LFS** porque el mayor binario pesa 216 KB. → `CAP20_E03.txt`

### 20.4 · Empaquetar una versión local
- **Qué se hizo:** `tools/empaquetar.py v1.0.0` arma `dist/andina-market-360-v1.0.0.zip` leyendo los archivos **desde el tag** (`git show v1.0.0:<ruta>`), no desde la carpeta de trabajo: README, LICENSE, CHANGELOG, VERSIONES, HTML y JSON, más una hoja `CONTENIDO.txt` con versión, licencia, instrucciones sin internet y tamaño y huella SHA-256 de cada archivo.
- **Resultado observado:** 6 archivos + CONTENIDO (7656 bytes). Como `style.css` y `productos.html` son posteriores a 1.0.0, no se incluyen, lo cual es correcto para esa versión.
- **Comprobación:** abierto en una carpeta temporal, no contiene `.git`, `.env`, temporales ni cachés; servido con `python -m http.server` desde la carpeta extraída, Edge muestra el tablero 1.0.0 completo (TOTAL S/ 1845.00) sin internet. → `CAP20_E04.txt`

### 20.5 · Diseñar un paquete reutilizable
- **Qué se hizo:** [fichas/paquete.md](../fichas/paquete.md): funciones reutilizables (`leer_ventas`, `sumar_por`, `resumir`, `texto`) frente a las atadas al repositorio (`actualizar_readme`, `main`); nombre `andina-resumen`, versión `0.1.0`, sin dependencias y API pública. Borrador en [fichas/paquete_borrador/](../fichas/paquete_borrador/) (`pyproject.toml`, `README.md`, `andina_resumen/__init__.py`) con ejemplo de instalación; **no se publicó** en ningún registro.
- **Comprobación:** la API del borrador produce exactamente el mismo resumen que `src/resumen.py` (`True`); 0 rutas locales absolutas (la ruta del CSV es siempre un argumento). → `CAP20_E05.txt`

## Retos

### Reto 20.1 · Política de archivos permitidos y prohibidos
- **Resultado obtenido:** [fichas/politica_archivos.md](../fichas/politica_archivos.md), con dos tablas (permitidos con su condición; prohibidos y cómo se evitan).
- **Cómo lo comprobé:** `git check-ignore` sobre 11 ejemplos prohibidos y 7 permitidos. **Corrección:** `clave.pem` no estaba ignorado aunque la política prohíbe claves privadas; se agregaron `*.pem` y `*.key` (`0f9b279`), sin archivos de ese tipo en el repositorio. → `CAP20_R01.txt`

### Reto 20.2 · Empaquetar la versión del dashboard y registrar contenido y tamaño
- **Resultado obtenido:** `andina-market-360-v1.0.0.zip`, **7656 bytes**, SHA-256 `0fed5c166c130d10…`, 6 archivos + `CONTENIDO.txt`. Se **adjuntó a la Release v1.0.0** (`gh release upload`) y `dist/` sigue fuera de Git.
- **Cómo lo comprobé:** `gh release view v1.0.0` lista el adjunto con su tamaño. → `CAP20_R02.txt`, `CAP20_E04.txt`

### Reto 20.3 · Metadatos mínimos para distribuir una librería del caso
- **Resultado obtenido:** tabla de 9 metadatos (name, version, description, readme, requires-python, license, authors **sin correo**, dependencies vacío, URL del repositorio), cada uno con su propósito; aplicados en el `pyproject.toml` del borrador.
- **Cómo lo comprobé:** `tomllib` lee el `pyproject.toml` sin errores y devuelve los valores esperados. → `CAP20_E05.txt`

Pruebas del proyecto tras el capítulo: 7 de 7 correctas → `CAP20_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 21:** automatizar en GitHub Actions lo que hoy se verifica a mano: `tools/verificar_md.py`, la regeneración del JSON/README sin diferencias y el paquete de cada tag.
