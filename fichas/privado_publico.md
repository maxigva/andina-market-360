# Pasar el caso de privado a público (Reto 4.3)

## Qué cambia
| Aspecto | Privado | Público |
|---|---|---|
| Quién ve el código y el **historial completo** | Solo colaboradores | Cualquier persona, también buscadores |
| Forks | Solo con acceso | Cualquiera puede copiarlo |
| GitHub Pages en cuenta gratuita | No disponible | Disponible |
| Licencia | Poco relevante | Necesaria para que otros sepan qué pueden hacer |
| Errores pasados (secretos en commits antiguos) | Ocultos | Expuestos aunque se borren del último commit |

## Revisión de riesgos realizada (antes de mantenerlo público)
| Riesgo | Comprobación | Resultado |
|---|---|---|
| Secretos en cualquier commit | `git log --all -p` + patrones de tokens y claves | 0 coincidencias |
| Correos reales de autor | `git log --all --format=%ae` | Solo `estudiante@example.com` (ficticio) |
| Archivos sensibles alguna vez versionados | `.env`, `.pem`, `.key`, `_material/` en el historial | 0 |
| Datos personales en el CSV | Columnas de `data/ventas.csv` | Solo id, fecha, sede, producto, cantidad y precio |
| Material de terceros | PDF del cuaderno | Ignorado en `_material/`; nunca subido |
| Permisos de uso | `LICENSE` | MIT presente |

Conclusión: el repositorio puede permanecer público. Si una comprobación fallara, primero se volvería privado, se revocaría el secreto expuesto y luego se limpiaría el historial.
