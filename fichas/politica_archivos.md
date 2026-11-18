# Política de archivos permitidos y prohibidos en Git (Reto 20.1 y Ejemplo 20.3)

## Permitidos (se versionan)
| Tipo | Ejemplos | Condición |
|---|---|---|
| Código y pruebas | `src/*.py`, `tests/*.py`, `tools/*.py` | Sin rutas absolutas ni credenciales |
| Datos didácticos pequeños | `data/ventas.csv` (495 bytes), `data/ventas_muestra.csv` | Solo ficticios; menos de 1 MB |
| Sitio estático | `docs/*.html`, `docs/style.css` | Sin cifras escritas a mano |
| Datos **generados** que la web necesita | `docs/data/resumen.json` | Debe coincidir con el CSV (lo verifica una prueba) |
| Documentación y evidencias | `*.md`, `evidencias/**/*.txt`, capturas `*.png` | Sin datos personales; capturas de menos de ~300 KB |
| Configuración del repositorio | `.gitignore`, `.gitattributes`, `.github/**` | — |

## Prohibidos (nunca se versionan)
| Tipo | Ejemplos | Cómo se evita |
|---|---|---|
| Secretos | `.env`, `.env.*`, claves `*.pem`/`*.key`, tokens | `.gitignore` + búsqueda de patrones antes de publicar |
| Entornos y cachés | `.venv/`, `venv/`, `__pycache__/`, `*.pyc` | `.gitignore` |
| Artefactos generados para distribuir | `dist/*.zip` | `.gitignore` (`dist/`); se adjuntan a la Release |
| Temporales de editor o sistema | `*.tmp`, `*.swp`, `*~`, `.DS_Store`, `Thumbs.db`, `.idea/` | `.gitignore` |
| Material de terceros sin licencia para redistribuir | `_material/` (PDF del cuaderno) | `.gitignore` |
| Datos reales de personas o ventas | Cualquier CSV con nombres, documentos o correos | Plantilla de PR de calidad de datos + revisión |

## Cuándo usar Git LFS (simulación, Ejemplo 20.3)
Listado **hipotético** (no se descargó ni creó ninguno):
| Archivo imaginado | Tamaño estimado | ¿LFS? |
|---|---|---|
| `docs/img/fachada-lima.png` | 4 MB | Sí, si hubiera muchas versiones |
| `docs/img/fachada-ica.png` | 4 MB | Sí |
| `docs/img/fachada-arequipa.png` | 4 MB | Sí |
| `docs/video/recorrido-tablero.mp4` | 60 MB | Sí (GitHub rechaza archivos de más de 100 MB y avisa desde 50 MB) |
| Capturas de evidencias (100-220 KB) | Pequeñas | No |

**Convendría LFS** cuando hay binarios grandes que cambian con frecuencia: Git guardaría cada versión completa en el historial y los clones serían cada vez más pesados.
**Implicaciones para colaboradores:** todos deben instalar Git LFS (`git lfs install`); los clones descargan punteros y luego los binarios; los archivos cuentan para la cuota de almacenamiento y ancho de banda LFS de la cuenta; y migrar archivos ya versionados (`git lfs migrate`) **reescribe la historia**, algo prohibido sobre `main` en este caso.
**Decisión actual:** no usar LFS. El caso no tiene binarios grandes (el mayor es una captura de 216 KB) y `git lfs ls-files` confirma 0 archivos convertidos.
