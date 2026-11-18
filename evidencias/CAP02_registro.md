# Registro de evidencias – Capítulo 02

| Registro | Fecha | Archivo / comando utilizado | Resultado observado | Evidencia |
|---|---|---|---|---|
| CAP02_E01 | 17/11/2026 20:21 | fichas/perfil.md | Biografía y público objetivo definidos, sin datos personales | cap02/CAP02_E01.txt |
| CAP02_E02 | 17/11/2026 20:21 | `gh auth status` (sin línea de token), `gh api user` | Acceso a la cuenta confirmado | cap02/CAP02_E02.txt |
| CAP02_E03 | 17/11/2026 20:21 (captura agregada 17/11/2026 21:47) | Settings → Password and authentication + `git ls-files` / `git grep` de patrones secretos | 2FA activa con app autenticadora; códigos de recuperación fuera del repo; 0 secretos | cap02/CAP02_E03.txt + CAP02_2FA.png |
| CAP02_E04 | 17/11/2026 20:21 | fichas/notificaciones.md + `grep` de correos | 0 correos en la ficha | cap02/CAP02_E04.txt |
| CAP02_E05 | 17/11/2026 20:21 | fichas/perfil_publico.md + `grep` de datos privados | 0 datos privados; enlaces como placeholders | cap02/CAP02_E05.txt |
| Reto 2.1 | 17/11/2026 20:21 | fichas/perfil.md + conteo con Python | 235 caracteres (≤ 250) y versión corta de 98 | cap02/CAP02_R01.txt |
| Reto 2.2 | 17/11/2026 20:21 | fichas/seguridad_cuenta.md | 5 comprobaciones verificables | cap02/CAP02_R02.txt |
| Reto 2.3 | 17/11/2026 20:21 | fichas/README_perfil.md | 2 proyectos destacados | cap02/CAP02_R03.txt |

## Control de salida del capítulo
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |
