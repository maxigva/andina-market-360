# Retos del Capítulo 01 – Andina Market 360

## Reto 1.1 · Nueva pregunta comercial
Pregunta: ¿Qué porcentaje del total de ventas aporta cada sede?

Archivo que produciría la respuesta: `docs/data/resumen.json`, con un campo `participacion_pct` que calcularía `src/resumen.py` a partir de `data/ventas.csv`.

Resultado obtenido (fórmula: total de la sede ÷ total general × 100):
| Sede | Total | Participación |
|---|---|---|
| Lima | S/ 814.00 | 44.12 % |
| Ica | S/ 555.00 | 30.08 % |
| Arequipa | S/ 476.00 | 25.80 % |
| TOTAL | S/ 1845.00 | 100.00 % |

Cómo lo comprobé: tomé los totales que muestra `python src/resumen.py` y verifiqué que los tres porcentajes suman 100.00 %.

## Reto 1.2 · Mapa de roles
| Rol | Responsabilidad | Archivos a cargo | Evidencia de revisión | Lo revisa |
|---|---|---|---|---|
| Analista de datos | Mantener el CSV correcto y solo con datos ficticios | data/ventas.csv | Conteo de 12 operaciones en la salida del script | Desarrollador |
| Desarrollador | Mantener el cálculo y las pruebas | src/, tests/, .github/ | 4 pruebas correctas con unittest | Analista de datos |
| Responsable de publicación | Documentar y publicar el resumen web | README.md, docs/ | Captura de la página con S/ 1845.00 | Desarrollador |

Cómo lo comprobé: cada rol tiene una evidencia que se puede repetir con un comando o una captura, y nadie revisa su propio trabajo.

## Reto 1.3 · Clasificación de acciones
| Acción cotidiana | Dónde ocurre | Motivo |
|---|---|---|
| Guardar una versión del CSV con `git commit` | Git local | Se registra en el repositorio de la computadora |
| Crear una rama para una mejora con `git branch` | Git local | Las ramas existen localmente sin conexión |
| Abrir una pull request para revisar un cambio | Plataforma GitHub | La revisión ocurre en el repositorio remoto |
| Publicar la página con GitHub Pages | Plataforma GitHub | GitHub aloja y sirve el sitio |
| Ejecutar `python src/resumen.py` | Herramienta externa (Python) | Python calcula; Git y GitHub no ejecutan el código |

Cómo lo comprobé: las acciones de Git local funcionan sin internet; las de GitHub necesitan el repositorio remoto; y el cálculo solo depende de Python.
