# Proyecto Andina Market 360

## Problema
- Problema: las ventas de las sedes se consolidan editando informes a mano, lo que genera errores y demoras.
- Usuarios: gerencia comercial y jefes de sede de Lima, Ica y Arequipa.
- Necesidad: consolidar las ventas y mostrar resultados por sede sin editar informes manualmente.
- Resultado esperado: un resumen por sede calculado con Python, probado y visible en una página web.

## Preguntas del negocio
1. ¿Qué sede lidera las ventas?
2. ¿Qué producto vende más?
3. ¿Cómo cambia el total mensual?

## Herramientas
- Git: registra versiones y cambios de archivos en la computadora.
- GitHub: aloja el repositorio y permite revisar cambios con otras personas.
- Python: ejecuta el programa que calcula las ventas.

## Flujo de trabajo
```
archivo local  →  Git local (commit)  →  repositorio remoto GitHub (push)  →  revisión del equipo (pull request)
```
1. Modifico archivos locales.
2. Git registra los cambios en un repositorio local.
3. Envío los cambios al repositorio remoto de GitHub, cuando lo configure.
4. Otras personas pueden revisar los cambios en una pull request.

## Comprobación
Para guardar y revisar cambios, GitHub no necesita ejecutar src/resumen.py. Python ejecuta el código localmente. GitHub Actions podría ejecutar pruebas, pero solo si lo configuramos.

