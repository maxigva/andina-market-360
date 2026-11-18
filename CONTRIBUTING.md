# Guía de contribución – Andina Market 360

Gracias por mejorar el caso. Antes de proponer un cambio, lea estas reglas.

## Antes de empezar
1. Busque o abra un **Issue** que describa el problema o la mejora, con **criterios de aceptación** verificables (entrada → cambio → prueba → resultado). Use las plantillas de `.github/ISSUE_TEMPLATE/`.
2. Los PR de código solo se revisan si responden a un Issue con criterios. Si faltan, pídalos en el Issue antes de programar.
3. Si trabaja desde un **fork**, mantenga `origin` (su copia) y agregue el original como `upstream`:
   ```bash
   git remote add upstream https://github.com/maxigva/andina-market-360.git
   git fetch upstream
   git switch -c docs/mi-cambio upstream/main
   ```

## Reglas de datos y seguridad
- **Solo datos ficticios.** No envíe ventas, clientes, nombres, documentos ni correos reales.
- **Nunca suba secretos:** contraseñas, tokens, claves privadas o archivos `.env`. Si sube uno por error, avise de inmediato en un Issue sin copiar el secreto y revóquelo.
- Las cifras publicadas (README, web, JSON) se generan con `src/resumen.py`; no las escriba a mano.

## Ramas
| Prefijo | Uso | Ejemplo |
|---|---|---|
| `feature/` | Funcionalidad nueva | `feature/filtro-productos` |
| `fix/` | Corrección de un error | `fix/encabezado-tablero` |
| `docs/` | Solo documentación | `docs/mejora-uso` |
| `laboratorio/`, `prueba/` | Prácticas descartables; nunca se fusionan en `main` | `laboratorio/revertir` |

Parta siempre de `main` actualizado (`git pull --ff-only origin main`). No se hace push directo a `main` para cambios de código: se abre un pull request.

## Mensajes de commit
Formato `tipo: verbo en infinitivo + objeto`, en español y en minúsculas.
`docs:` documentación · `feat:` funcionalidad · `fix:` corrección · `test:` pruebas · `ci:` automatización · `chore:` mantenimiento · `refactor:` reorganización sin cambiar resultados.

Ejemplo: `feat: agregar filtro por producto`.

## Antes de abrir un pull request
```bash
python -m unittest discover -s tests -v
python src/resumen.py --json docs/data/resumen.json --readme README.md
python tools/verificar_md.py README.md CONTRIBUTING.md docs/manual.md
git status
```
Las pruebas deben terminar en `OK`, y `git status` no debe mostrar cambios en el JSON ni en el README tras regenerarlos.

## Pull requests
- Un PR por tema, con título en el formato de commit.
- Describa qué cambia, por qué y cómo verificarlo; cite el Issue con `Closes #N`.
- Si la revisión pide cambios, agréguelos **en la misma rama**: el PR se actualiza solo.
- No amplíe el alcance: lo que no esté en los criterios del Issue va a otro Issue.

## Revisión
- Cada PR se revisa con la [guía de revisión](fichas/guia_revision.md), igual para todas las personas que contribuyen.
- **Bloquean la fusión:** error de cálculo (por ejemplo, cifras escritas a mano), filtración de datos o secretos, y pruebas rotas. Lo demás son correcciones o sugerencias.
- Solo se marcan como resueltas las conversaciones atendidas de verdad.

## Licencia y conducta
- Al contribuir, acepta que su aporte se publique bajo la licencia [MIT](LICENSE) del proyecto. No incluya código ni textos de terceros con licencias incompatibles.
- Comente el cambio, no a la persona; las críticas deben ser específicas y reproducibles.
- Vulnerabilidades o secretos expuestos: no los publique en un Issue abierto; avise a quien mantiene el proyecto por un canal privado.

## Comunicar errores en Issues
1. Busque si ya existe un Issue igual.
2. Abra uno nuevo con la plantilla de error: datos de entrada (ficticios), pasos para reproducir, resultado observado y resultado esperado.
3. Adjunte el comando y su salida; no adjunte datos reales ni capturas con información personal.
