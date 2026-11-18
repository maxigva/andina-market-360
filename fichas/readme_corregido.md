# Corrección de un README incompleto (Reto 4.2)

## Antes (README base del proyecto, sección de ejecución)
```
## Prueba local
python -m unittest discover -s tests -v
python src/resumen.py --json docs/data/resumen.json
python -m http.server 8000 --directory docs
```
Faltaba: requisitos (versión de Python, sin paquetes externos), el comando para ver el resumen en la terminal, la **salida esperada** de cada paso y cómo saber si la web está actualizada.

## Después (README actual)
1. Sección **Requisitos**.
2. Cuatro pasos numerados dentro de un bloque `bash`, empezando por `python src/resumen.py`.
3. **Salida esperada** copiada de una ejecución real del script.
4. Criterio verificable: pruebas en `OK` y `git status` limpio tras regenerar el JSON.

## Verificación
Se ejecutaron los cuatro pasos tal como están escritos (`evidencias/cap04/CAP04_R02.txt`): resumen correcto, 4 pruebas OK, JSON regenerado sin diferencias de contenido y servidor local respondiendo HTTP 200 con el mismo total.
