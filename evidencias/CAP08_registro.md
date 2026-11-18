# Registro de evidencias – Capítulo 08

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP08_E01 | 17/11/2026 23:20 | `git switch -c feature/resumen-sedes` + README | Rama activa; commit `5920dd3` | cap08/CAP08_E01.txt |
| CAP08_E02 | 17/11/2026 23:27 | `git commit -am "feat: nombrar tablero de sedes"` | `2e67da0`; main sin el cambio | cap08/CAP08_E02.txt |
| CAP08_E03 | 17/11/2026 23:33 | `git merge --no-ff feature/resumen-sedes` | Fusión `2ca7096` visible en el gráfico | cap08/CAP08_E03.txt |
| CAP08_E04 | 17/11/2026 23:44 | `fix/encabezado-tablero` + merge + pruebas | `f70b537` integrado; 5 pruebas OK | cap08/CAP08_E04.txt |
| CAP08_E05 | 17/11/2026 23:58 | `git branch --merged`, `git branch -d` | Rama integrada eliminada | cap08/CAP08_E05.txt |
| Reto 8.1 | 17/11/2026 23:49 | `feature/filtro-productos` | Commit `bac3c40` solo en la rama | cap08/CAP08_R01.txt |
| Reto 8.2 | 17/11/2026 23:44 | `git log --oneline --graph -9` | Corrección y fusión visibles | cap08/CAP08_R02.txt |
| Reto 8.3 | 17/11/2026 23:58 | `git switch` con archivos modificados | Caso A viaja; caso B bloqueado | cap08/CAP08_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
