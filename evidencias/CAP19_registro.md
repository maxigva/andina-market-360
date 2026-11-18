# Registro de evidencias – Capítulo 19

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP19_E01 | 18/11/2026 12:27 | docs/index.html + style.css; Edge (`file://` y servidor local) | HTML válido, sin recursos externos; mensaje de `file://` corregido | cap19/CAP19_E01.txt |
| CAP19_E02 | 18/11/2026 12:27 | `python src/resumen.py --json …` + nota de origen y fecha | Solo totales agregados; nota visible | cap19/CAP19_E02.txt |
| CAP19_E03 | 18/11/2026 12:27 | docs/style.css (`.tarjeta`, `.tabla-sedes`, `@media`) + capturas | Contraste AA; sin desplazamiento a 375 px | cap19/CAP19_E03.txt, CAP19_E03_escritorio.png, CAP19_E03_movil_375px.png |
| CAP19_E04 | 18/11/2026 12:27 | `POST /pages` (main, /docs) + `curl` + Edge | Sitio publicado; estáticos 200, `src/` 404 | cap19/CAP19_E04.txt, cap19/CAP19_homepage.txt + CAP19_pages.png (pendiente) |
| CAP19_E05 | 18/11/2026 12:43 | Rutas absoluta y relativa; enlaces publicados del manual | `/data/…` 404 → `./data/…` 200; 2 enlaces del manual corregidos | cap19/CAP19_E05.txt |
| Reto 19.1 | 18/11/2026 12:27 | docs/productos.html | Segunda página enlazada; HTTP 200 | cap19/CAP19_R01_productos.png |
| Reto 19.2 | 18/11/2026 12:58 | fichas/publicacion_estatica.md | Diferencias local/publicado documentadas | fichas/publicacion_estatica.md |
| Reto 19.3 | 18/11/2026 12:58 | Fórmula WCAG + medición del DOM en Edge | 3 controles cumplidos | cap19/CAP19_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
