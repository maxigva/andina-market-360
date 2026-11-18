# Administración del repositorio (Capítulo 17)

## 17.1 · Política de la rama principal
**Política deseada para un equipo:** nadie fusiona en `main` sin pruebas aprobadas ni revisión, y nadie reescribe o borra `main`.

**Configuración aplicada en GitHub** (Settings → Rules → Rulesets, conjunto `proteger-main`, activo, rama por defecto):
| Regla | Estado | Motivo |
|---|---|---|
| Bloquear *force push* (`non_fast_forward`) | **Aplicada** | Evita reescribir commits ya publicados (ver Reto 9.3) |
| Bloquear borrado de la rama (`deletion`) | **Aplicada** | Evita perder `main` por un error |
| Exigir pull request con revisión | **No aplicada (decisión del titular)** | Hay una sola persona en el repositorio y GitHub no permite aprobar un PR propio: exigirla bloquearía todo el trabajo |
| Exigir la verificación `pruebas` de Actions | **No aplicada (decisión del titular)** | Se cumple por proceso (CONTRIBUTING + guía de revisión); se activará al sumar colaboradores |

Con las dos reglas aplicadas, un `git push --force` o `git push origin --delete main` accidental es rechazado por GitHub. Los commits nuevos (*fast-forward*) siguen permitidos.

## Reto 17.1 · Tres reglas de protección y el riesgo que reduce cada una
| # | Regla | Riesgo que reduce |
|---|---|---|
| 1 | Bloquear *force push* en `main` | Pérdida de trabajo ajeno y de referencias (PR, tags, CI) al reescribir la historia publicada |
| 2 | Bloquear el borrado de `main` | Desaparición de la rama que publica la web (Pages) y que usan todos los clones |
| 3 | Exigir la verificación `pruebas` antes de fusionar (diseñada, no aplicada) | Publicar en el tablero cifras que no coinciden con el CSV (Issue #2) o un HTML con cifras fijas (PR #8) |

## 17.4 · Responsables por área (borrador con identificadores ficticios)
| Ruta | Rol (ficticio) | Identificador de borrador | Revisión esperada |
|---|---|---|---|
| `/docs/` | Responsable de publicación | `@andina-publicacion` | Textos claros, enlaces relativos, sin cifras fijas, accesibilidad |
| `/src/`, `/tests/` | Desarrollo | `@andina-desarrollo` | Cálculo correcto, prueba nueva por cada corrección, sin dependencias externas |
| `/data/` | Analista de datos | `@andina-datos` | Plantilla de calidad de datos; solo datos ficticios |

Los identificadores ficticios **no** se pusieron en `.github/CODEOWNERS`, porque GitHub los marcaría como inválidos. El archivo real usa la única cuenta con acceso, `@maxigva`; GitHub reporta `{"errors":[]}`.

## 17.5 · Ficha de conservación
| Campo | Valor |
|---|---|
| Proyecto | Andina Market 360 (caso didáctico) |
| Versión actual | En preparación de `v1.0.0` (Cap. 18) |
| Dueño | Titular del repositorio (rol: estudiante) |
| Estado | **Activo**, práctica en curso (capítulos 17-36) |
| Naturaleza | Material de prácticas con datos ficticios; **no** es un producto en producción |
| Próxima revisión | Al terminar el Capítulo 36; luego cada 6 meses |

**Cuándo archivar:** al cerrar el curso y entregar la versión final, si no habrá más cambios. Archivar (*Settings → Archive this repository*) deja el repositorio en solo lectura: se puede consultar y clonar, pero no recibe commits, Issues ni PR.
**Cuándo dejarlo activo:** mientras haya capítulos, Issues abiertos (por ejemplo #4) o se use como portafolio que se sigue actualizando.

**Antes de archivar, el equipo debe saber recuperar la documentación:**
1. Crear el tag de entrega y su Release (capítulos 18 y 36).
2. Comprobar que el README, `docs/manual.md` y `capitulos/` explican el caso sin depender de Issues.
3. Clonar en limpio y ejecutar las pruebas: `git clone … && python -m unittest discover -s tests`.
4. Si hiciera falta modificarlo de nuevo: *Settings → Unarchive*.

## Reto 17.3 · Política de archivado de repositorios de prácticas (universidad)
1. **Alcance:** repositorios creados para un curso, con datos ficticios.
2. **Al cierre del ciclo** (máximo 30 días después de la nota final), cada estudiante crea un tag `entrega-AAAA-ciclo` y una Release con sus notas.
3. **Revisión previa al archivado:** sin secretos en todo el historial (`git log -p` + búsqueda de patrones), sin datos personales, con licencia y README que diga “material de práctica”.
4. **Archivar, no borrar:** el repositorio se archiva para conservar la evidencia de aprendizaje y el portafolio. Solo se borra a pedido de su titular.
5. **Repositorios con datos reales por error:** no se archivan públicos. Primero se hacen privados, se limpia el historial y se rotan las credenciales.
6. **Reactivación:** quien quiera seguir trabajando lo desarchiva y crea una rama nueva; el tag de entrega no se mueve.
