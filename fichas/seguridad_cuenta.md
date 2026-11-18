# Lista de seguridad de cuenta (Reto 2.2)

Cada comprobación se puede verificar con una pantalla o un comando, sin revelar el secreto.

| # | Comprobación | Cómo se verifica | Resultado esperado |
|---|---|---|---|
| 1 | Autenticación de dos factores activa | Settings → Password and authentication | Aparece “Two-factor authentication: Enabled” |
| 2 | Códigos de recuperación guardados fuera del proyecto | Settings → Password and authentication → Recovery options | Se ven como descargados; ningún archivo del repo los contiene (`git ls-files` sin `recovery`) |
| 3 | Correo privado activado | Settings → Emails → “Keep my email addresses private” | Casilla marcada; los commits usan una dirección *noreply* o ficticia |
| 4 | Sin sesiones ni aplicaciones desconocidas | Settings → Sessions y Settings → Applications | Solo dispositivos y apps reconocidos |
| 5 | Ningún secreto dentro del repositorio | `git grep -nIE "gh[po]_[A-Za-z0-9]{36}\|github_pat_[A-Za-z0-9_]{22,}\|-----BEGIN [A-Z ]*PRIVATE KEY"` | Sin coincidencias |
