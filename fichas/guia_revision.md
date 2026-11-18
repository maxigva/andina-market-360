# Guía de revisión para el tablero de ventas (Reto 15.1)

Se aplica igual a **todos** los PR, sin importar quién los abra. Cada pregunta se responde con una evidencia (comando, archivo o captura), no por intuición.

| # | Pregunta | Cómo se comprueba | Si la respuesta es “no” |
|---|---|---|---|
| 1 | ¿El PR cambia solo los archivos que anuncia? | `gh pr diff N --name-only` | Bloqueo |
| 2 | ¿Todas las cifras visibles salen de `docs/data/resumen.json` o de `src/resumen.py`? | `grep -nE "S/ [0-9]" docs/index.html` → 0 líneas | Bloqueo (error de cálculo) |
| 3 | ¿El JSON publicado coincide con el CSV? | `python -m unittest discover -s tests -v` (`test_json_coincide_con_csv`) | Bloqueo (prueba rota) |
| 4 | ¿Las pruebas pasan en local y en GitHub Actions? | `unittest` + `gh pr checks N` | Bloqueo (prueba rota) |
| 5 | ¿Los títulos dicen qué se mide y en qué unidad (S/, unidades)? | Lectura del HTML / captura | Corrección solicitada |
| 6 | ¿Las proporciones visuales son correctas (barra mayor = 100 %, resto ± 1 %)? | Script de Node sobre el JSON o cálculo manual | Bloqueo (error de cálculo) |
| 7 | ¿Se indica que los datos son ficticios y su período? | Subtítulo del tablero | Corrección solicitada |
| 8 | ¿Hay datos personales, secretos o URLs internas? | `git grep -nIE "gh[po]_\|@gmail\|password"` en el diff | Bloqueo (filtración) |
| 9 | ¿El HTML es válido y funciona sin librerías externas? | Verificador de etiquetas; sin `<script src=http…>` | Corrección solicitada |
| 10 | ¿El PR cita el Issue y deja claro cómo verificarlo? | Descripción del PR | Sugerencia |

**Categorías de bloqueo:** error de cálculo, filtración de datos o secretos, prueba rota. Todo lo demás es corrección solicitada o sugerencia, y no impide fusionar si el autor justifica su decisión.
