# Bitácora de versiones – Andina Market 360

## Línea base (Ejemplo 5.1)
| Dato | Valor |
|---|---|
| Directorio de trabajo | `C:\andina-market-360` |
| Versión de partida | commit `44f5f4f` (*docs: documentar capítulo 04*) |
| Registros de `data/ventas.csv` (sin encabezado) | **12** |
| Huella SHA-256 del CSV (16 primeros caracteres) | `12e705a345082a1b` |
| Respaldo | Copia local fuera del repositorio; restauración probada sin GitHub |

Descripción de la versión inicial: CSV de 12 ventas ficticias, script `src/resumen.py` que calcula totales por sede, producto y mes, 4 pruebas `unittest`, web estática que lee `docs/data/resumen.json`, README con pasos verificables y licencia MIT.

## Los tres espacios de Git (Ejemplo 5.2)
```
┌──────────────────────┐   git add README.md   ┌──────────────────────┐  git commit -m "..."  ┌──────────────────────┐
│ Directorio de trabajo│ ────────────────────▶ │ Preparación (staging)│ ────────────────────▶ │ Historial (commits)  │
│ README.md editado    │                       │ README.md preparado  │                       │ README.md confirmado │
└──────────────────────┘                       └──────────────────────┘                       └──────────────────────┘
          ▲                                                                                              │
          └──────────────────────────── git restore / git switch (lee del historial) ────────────────────┘
```
Guardar un archivo en el editor solo cambia el directorio de trabajo: Git **no** crea un commit automáticamente (comprobado: `HEAD` siguió en `44f5f4f`).

## Cambio controlado (Ejemplo 5.3)
| | Línea 3 de `README.md` |
|---|---|
| Antes | Resumen verificable de ventas **ficticias** por sede (Lima, Ica y Arequipa), calculado con Python, probado con `unittest` y mostrado en una página web estática. |
| Después | Objetivo comercial: que la gerencia sepa **qué sede lidera las ventas ficticias** (Lima, Ica y Arequipa) con cifras calculadas por Python, probadas con `unittest` y mostradas en una página web estática. |
| En una oración | Se reescribió la frase inicial del README para expresar el objetivo comercial (saber qué sede lidera). |
| Mensaje | `docs: precisar objetivo comercial` → commit `3c9710d` (solo `README.md`, 1 línea) |

## Situaciones en las que Git evita pérdidas o ambigüedades (Reto 5.1)
1. **Dos personas editan el README a la vez.** Sin Git, la última copia guardada pisa a la otra; con Git, cada cambio queda en su commit y una fusión muestra exactamente qué líneas chocan.
2. **El CSV aparece con 11 filas.** Sin Git no se sabe si fue un error o una decisión; con Git, `git log -- data/ventas.csv` muestra quién lo cambió, cuándo y por qué, y `git restore` recupera la versión de 12 filas.
3. **“¿Qué versión se mostró a gerencia?”** Sin Git hay archivos `final_v2_definitivo`; con Git, un tag (Cap. 18) identifica de forma única la versión entregada.

## Plan de cuatro cambios con criterios de aceptación (Reto 5.2)
| # | Cambio planificado | Commit previsto | Criterio de aceptación |
|---|---|---|---|
| 1 | Escribir el JSON con finales de línea LF | `fix: escribir el JSON con finales de línea LF` (Cap. 06) | Regenerar el JSON en Windows deja `git status` limpio |
| 2 | Agregar un CSV de muestra pequeño | `feat: agregar CSV de muestra para pruebas` (Cap. 07) | Mismas 6 columnas, solo datos ficticios, ≤ 5 filas |
| 3 | Probar el resumen con la muestra | `test: validar el resumen con el CSV de muestra` (Cap. 07) | La nueva prueba pasa y las 4 anteriores siguen en OK |
| 4 | Nombrar el tablero de sedes en la web | `feat: nombrar tablero de sedes` (Cap. 08) | El encabezado aparece en `docs/index.html` y las cifras siguen saliendo del JSON |

## Cuándo un cambio existe pero aún no pertenece al historial (Reto 5.3)
```
 editar archivo ──▶ [ ?? / M  ]  existe solo en el disco          ← NO está en el historial
       git add ──▶ [ A  / M  ]  existe en la preparación          ← todavía NO está en el historial
    git commit ──▶ [ commit ]   existe en el historial (tiene hash) ← recién aquí es una versión
```
Comprobado con `nota_temporal.txt`: aparece como `??`, luego como `A`, pero `git log -- nota_temporal.txt` devuelve 0 commits; se retiró con `git restore --staged` sin tocar el historial.

## Entorno local (Capítulo 06)
| Elemento | Valor |
|---|---|
| Git | `git version 2.55.0.windows.4` (Git for Windows, instalado en `C:\Program Files\Git`) |
| Directorio de trabajo del caso | `C:\andina-market-360` (rama `main`, remoto `origin`) |
| Identidad local del caso | `Estudiante` / `estudiante@example.com` (ficticia, solo `--local`) |
| Copia de práctica para `git init -b main` | `<TEMP>\practica\andina-market-360` (carpeta temporal del sistema; se omite la parte de la ruta que contiene el usuario de Windows) |
| Primer commit de la práctica | `d8db55b chore: iniciar caso Andina Market` |
| Clon local de la práctica | `<TEMP>\practica\andina-market-copia` → mismo hash `d8db55b` |

Cambio planificado n.º 1 **cumplido**: commit `902b0ac fix: escribir el JSON con finales de línea LF` (+ `.gitattributes`). Regenerar el JSON dos veces ya no produce cambios.

Cambios planificados n.º 2 y 3 **cumplidos** (Cap. 07): `778f942` (datos) y `be19b40` (prueba). Las pruebas pasan de 4 a **5**.
