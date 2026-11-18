# Registro de evidencias – Capítulo 20

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP20_E01 | 18/11/2026 13:15 | `git ls-files` + tamaños, `git count-objects -vH` | 5 mayores = capturas; CSV de 495 bytes | cap20/CAP20_E01.txt |
| CAP20_E02 | 18/11/2026 13:15 | .gitignore (`dist/`) + `dist/prueba.tmp` + `git check-ignore -v` | Artefacto ignorado; pruebas y docs versionables | cap20/CAP20_E02.txt |
| CAP20_E03 | 18/11/2026 13:15 | `git lfs version`, `git lfs track`, `git lfs ls-files` | LFS 3.7.1; 0 archivos convertidos | cap20/CAP20_E03.txt |
| CAP20_E04 | 18/11/2026 13:15 | `python tools/empaquetar.py v1.0.0` + extracción + Edge | ZIP de 7656 bytes sin secretos; funciona sin internet | cap20/CAP20_E04.txt |
| CAP20_E05 | 18/11/2026 13:47 | fichas/paquete.md + fichas/paquete_borrador/ | API idéntica a src/resumen.py; sin rutas absolutas | cap20/CAP20_E05.txt |
| Reto 20.1 | 18/11/2026 13:31 | fichas/politica_archivos.md + `git check-ignore` | Brecha `*.pem` corregida | cap20/CAP20_R01.txt |
| Reto 20.2 | 18/11/2026 13:15 | `gh release upload v1.0.0 dist/…zip` | Adjunto en la Release, 7656 bytes | cap20/CAP20_R02.txt (visible también en CAP18_release.png) |
| Reto 20.3 | 18/11/2026 13:47 | fichas/paquete_borrador/pyproject.toml | 9 metadatos mínimos | cap20/CAP20_E05.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
