# Capítulo 19 · Publicación de sitios con GitHub Pages

**Caso que continúa:** exponer una página estática del caso comercial sin publicar bases reales.
**Comandos de consulta:** `python src/resumen.py --json docs/data/resumen.json` · `python -m http.server 8000 --directory docs`
**Fecha:** 18/11/2026 · Commits: `a7d9a93 feat: publicar tablero con estilos accesibles y página de productos`, `0d1521b fix: corregir enlaces del manual publicado en Pages` y `docs: documentar capítulo 19`
**Sitio publicado:** https://maxigva.github.io/andina-market-360/

> Las comprobaciones “en el navegador” se hicieron con **Microsoft Edge sin interfaz** (`--headless`): volcado del DOM ya ejecutado y capturas de pantalla. Se usó un perfil temporal separado.

## Ejemplos resueltos

### 19.1 · Preparar la página inicial
- **Qué se hizo:** `docs/index.html` con encabezado *Andina Market 360*, `<meta viewport>`, navegación, **tres apartados** (tarjetas `article` para Lima, Ica y Arequipa con monto y participación), gráfico y tablas; los estilos pasaron a `docs/style.css`, enlazado desde la cabecera.
- **Resultado observado:** HTML válido, `lang="es"`, 0 recursos externos (sin CDN ni fuentes en línea).
- **Hallazgo y corrección:** abierta con doble clic (`file://`), la página decía “No se encontró data/resumen.json”, lo que era falso: el navegador **bloquea** `fetch` en archivos locales. El mensaje ahora lo explica e indica usar `python -m http.server`, que funciona sin internet. Con el servidor local, la página se lee completa.
- **Comprobación:** → `evidencias/cap19/CAP19_E01.txt`

### 19.2 · Generar datos para mostrar
- **Qué se hizo:** `python src/resumen.py --json docs/data/resumen.json`; el JSON solo tiene `operaciones`, `total`, `por_sede`, `por_producto` y `por_mes`. La página muestra una nota visible con el **origen** (`src/resumen.py` a partir de `data/ventas.csv`, datos ficticios) y la **fecha de actualización** del archivo de datos, leída del encabezado `Last-Modified` de la respuesta, de modo que no se escribe a mano ni se agrega al JSON.
- **Comprobación:** ningún registro individual (`id`, `fecha`, `cantidad`) en el JSON; regenerarlo no deja cambios. → `CAP19_E02.txt`

### 19.3 · Preparar estilos accesibles
- **Qué se hizo:** `docs/style.css` con variables de color, fuente de 16 px como mínimo, interlineado 1.5, foco visible en enlaces, clase `.tarjeta` (indicadores) y `.tabla-sedes` (tablas), y `@media (max-width: 480px)`.
- **Resultado observado:** los 6 pares de color cumplen **WCAG AA** (de 6.66:1 a 17.40:1). Se corrigieron dos detalles vistos al renderizar: encabezados de tabla en minúscula (“sede” → “Sede”) y un punto duplicado tras la fecha.
- **Comprobación de ancho reducido:** Edge sin interfaz impone un ancho mínimo de ventana, y la primera captura “de 375 px” salió recortada. Se repitió dentro de un marco de 375 px: las tarjetas se apilan y no hay desplazamiento horizontal. → `CAP19_E03.txt`, `CAP19_E03_escritorio.png`, `CAP19_E03_movil_375px.png`

### 19.4 · Activar Pages cuando corresponda
- **Qué se hizo (autorizado):** `POST /repos/…/pages` con origen **rama `main`, carpeta `/docs`**. Primer despliegue `built` sobre `a7d9a93`; HTTPS forzado. *Homepage* del repositorio = URL de Pages (`gh repo edit --homepage`).
- **Comprobación:** portada, `style.css`, `productos.html`, `data/resumen.json` y `manual.html` responden HTTP 200; `src/resumen.py` responde **404**: el sitio solo sirve archivos estáticos, sin Python en el servidor. El DOM publicado muestra las mismas cifras que el local. → `CAP19_E04.txt`, `CAP19_homepage.txt` (captura `CAP19_pages.png`, pendiente)

### 19.5 · Corregir un enlace relativo
- **Qué se hizo:** la navegación enlaza `./data/resumen.json` y el `fetch` usa la misma ruta relativa.
- **Ruta que fallaba:** `/data/resumen.json` (absoluta) → `https://maxigva.github.io/data/resumen.json` → **404**, porque el sitio de proyecto vive bajo `/andina-market-360/`; `./data/resumen.json` → **200**. Al revisar los enlaces publicados apareció un fallo real: en `manual.html`, `../README.md` y `../data/ventas.csv` daban **404**, porque Pages solo publica `docs/`.
- **Corrección:** `0d1521b` usa URL de GitHub para esos dos enlaces (ambas responden 200) y agrega un enlace relativo al tablero; el manual documenta cuándo usar cada tipo de ruta.
- **Comprobación:** → `CAP19_E05.txt`

## Retos

### Reto 19.1 · Segunda página sobre productos enlazada desde la portada
- **Resultado obtenido:** `docs/productos.html` (gráfico y tabla de ventas por producto con participación, ordenados de mayor a menor), con la misma hoja de estilos y navegación en ambas direcciones.
- **Cómo lo comprobé:** enlace `./productos.html` → HTTP 200 en Pages; la prueba de “sin cifras fijas” ahora revisa **todas** las páginas de `docs/`. → `CAP19_R01_productos.png`, `CAP19_E05.txt`

### Reto 19.2 · Código Python local frente a contenido estático publicable
- **Resultado obtenido:** [fichas/publicacion_estatica.md](../fichas/publicacion_estatica.md): qué se ejecuta dónde, qué publica Pages, qué datos se exponen y qué hacer cuando cambian los datos.

### Reto 19.3 · Tres controles de accesibilidad en un navegador
| Control | Resultado | Valoración |
|---|---|---|
| 1. Contraste de color (WCAG AA) | 6 pares entre 6.66:1 y 17.40:1 | Cumple |
| 2. Estructura semántica (DOM medido en Edge) | `lang=es`, un solo `h1` seguido de `h2`, 4/4 encabezados de tabla con `scope`, `nav` con `aria-label` y página actual marcada | Cumple |
| 3. Adaptación a 375 px (Edge) | ancho del contenido = ancho visible (360 px más la barra de desplazamiento): sin desplazamiento horizontal; fuente de 16 px | Cumple |

→ `CAP19_R03.txt`

Pruebas del proyecto tras el capítulo: 7 de 7 correctas (la prueba del tablero revisa ahora `index.html` y `productos.html`) → `CAP19_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 20:** excluir `dist/` de Git y preparar un paquete distribuible de la versión `v1.0.0` construido desde el tag, no desde la carpeta de trabajo.
