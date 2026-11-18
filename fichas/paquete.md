# Diseño de un paquete reutilizable (Ejemplo 20.5 y Reto 20.3)

> Borrador de diseño: **no se publicó** en PyPI ni en ningún registro. La estructura de ejemplo está en [fichas/paquete_borrador/](paquete_borrador/).

## Qué se puede reutilizar de `src/resumen.py`
| Función | ¿Reutilizable? | Motivo |
|---|---|---|
| `leer_ventas(ruta)` | Sí | Lee cualquier CSV con las 6 columnas del caso |
| `sumar_por(ventas, campo)` | Sí | Agrega montos por sede, producto o mes; no depende de rutas |
| `resumir(ventas)` | **Sí, núcleo de la API** | Devuelve el diccionario que consume la web |
| `texto(r)` | Sí | Formato de texto del resumen |
| `actualizar_readme`, `main` | No | Dependen de este repositorio (README con marcadores, rutas por defecto) |

## Propuesta
| Campo | Valor |
|---|---|
| Nombre | `andina-resumen` (módulo `andina_resumen`) |
| Versión | `0.1.0`: API todavía no estable, independiente de la versión del tablero |
| Dependencias | Ninguna (solo biblioteca estándar: `csv`) |
| Python | `>=3.10` |
| Licencia | MIT |

### API pública
```python
from andina_resumen import leer_ventas, resumir, texto

ventas = leer_ventas("ventas.csv")      # ruta que elige quien usa el paquete
r = resumir(ventas)                     # {"operaciones", "total", "por_sede", "por_producto", "por_mes"}
print(texto(r))
```
La API recibe la ruta como **argumento**: no hay rutas locales absolutas ni rutas por defecto atadas a este repositorio.

### Ejemplo de instalación (borrador, sin publicar)
```bash
# desde la carpeta del borrador, en un entorno virtual
python -m venv .venv
python -m pip install ./fichas/paquete_borrador
```

## Metadatos mínimos para distribuir la librería (Reto 20.3)
| Metadato | Valor propuesto | Para qué sirve |
|---|---|---|
| `name` | `andina-resumen` | Identificador único para instalar |
| `version` | `0.1.0` | Versionado semántico propio |
| `description` | Resumen de ventas por sede, producto y mes desde un CSV | Lo que se ve en el índice de paquetes |
| `readme` | `README.md` | Documentación de uso |
| `requires-python` | `>=3.10` | Evita instalarlo en versiones sin soporte |
| `license` | `MIT` | Qué permite hacer con el código |
| `authors` | Estudiante (sin correo personal) | Responsable, sin datos privados |
| `dependencies` | `[]` | Declara explícitamente que no hay dependencias |
| `urls.Repository` | https://github.com/maxigva/andina-market-360 | Dónde reportar errores y ver el código |
