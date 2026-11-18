# Capítulo 02 · Creación y configuración de una cuenta

**Caso que continúa:** preparar identidad profesional y criterios de seguridad para usar el repositorio del caso.
**Ruta de consulta:** github.com → Settings → Password and authentication
**Fecha:** 17/11/2026

## Ejemplos resueltos

### 2.1 · Planificar la identidad del perfil
- **Qué se hizo:** borrador local con usuario de muestra (`andina-estudiante`), biografía y a quién ayuda el repositorio.
- **Archivo:** [fichas/perfil.md](../fichas/perfil.md)
- **Resultado observado:** la biografía explica que el repositorio ayuda a la gerencia comercial ficticia y a estudiantes.
- **Comprobación:** la evidencia es el borrador; no se registró nada nuevo en GitHub. → `evidencias/cap02/CAP02_E01.txt`

### 2.2 · Crear la cuenta de forma guiada
- **Qué se hizo:** la cuenta ya existía y es la que aloja el repositorio. Se comprobó el acceso con GitHub CLI, sin anotar contraseñas ni códigos (la línea del token se filtra).
- **Comando:** `gh auth status | grep -v -i token` y `gh api user --jq .login`
- **Resultado observado:** sesión activa, acceso confirmado.
- **Comprobación:** solo se registra *si pude acceder*. → `CAP02_E02.txt`

### 2.3 · Preparar la autenticación reforzada
- **Simulación local documentada.** La activación de 2FA es una acción de seguridad de la cuenta que hace la persona titular, no un script:
  1. Settings → Password and authentication → *Enable two-factor authentication*.
  2. Elegir app autenticadora (o llave de seguridad) y escanear el código QR.
  3. Descargar los códigos de recuperación y guardarlos en un gestor de contraseñas, **fuera** de `andina-market-360`.
- **Comprobación (real):** búsqueda de archivos y patrones secretos en el repositorio.
- **Resultado observado:** `archivos sospechosos: 0`, `secretos encontrados: 0`. → `CAP02_E03.txt`

### 2.4 · Configurar notificaciones útiles
- **Qué se hizo:** ficha con avisos de Issues, Pull Requests, seguridad y Actions, y el procedimiento para silenciar un repositorio (Watch → Ignore).
- **Archivo:** [fichas/notificaciones.md](../fichas/notificaciones.md)
- **Resultado observado:** configuración *Participating and @mentions* + Custom en el repositorio del caso.
- **Comprobación:** búsqueda de direcciones de correo → `correos en la ficha: 0`. → `CAP02_E04.txt`

### 2.5 · Preparar un perfil orientado a proyectos
- **Qué se hizo:** perfil público con caso, objetivos, tecnologías, enlaces *placeholder* y sección de protección de datos.
- **Archivo:** [fichas/perfil_publico.md](../fichas/perfil_publico.md)
- **Resultado observado:** 6 secciones; 3 enlaces como `<ENLACE_...>`, sin inventar repositorios.
- **Comprobación:** búsqueda de correos, teléfonos y DNI → `datos privados: 0`. → `CAP02_E05.txt`

## Retos

### Reto 2.1 · Biografía de 250 caracteres para soporte técnico
- **Resultado obtenido:** biografía de 235 caracteres (sección “Reto 2.1” de `fichas/perfil.md`) y una versión corta de 98 caracteres para el campo *Bio*.
- **Cómo lo comprobé:** conteo con Python → `bio larga: 235 ... True`. Corrección: la primera versión no mencionaba el tipo de puesto; se agregó “soporte técnico” al inicio. → `CAP02_R01.txt`

### Reto 2.2 · Lista de seguridad con cinco comprobaciones
- **Resultado obtenido:** [fichas/seguridad_cuenta.md](../fichas/seguridad_cuenta.md) con 5 controles (2FA, códigos de recuperación, correo privado, sesiones/apps, secretos en el repo), cada uno con su forma de verificación.
- **Cómo lo comprobé:** se ejecutó el control 5 (sin coincidencias) y se contaron 5 filas. Corrección: el patrón inicial (`ghp_|gho_`) encontraba la propia ficha; se cambió por uno que exige la longitud real de un token. → `CAP02_R02.txt`

### Reto 2.3 · README de perfil con dos proyectos
- **Resultado obtenido:** [fichas/README_perfil.md](../fichas/README_perfil.md) con *Andina Market 360* y un segundo proyecto de práctica (*Inventario Escolar*), marcado como “en preparación”.
- **Cómo lo comprobé:** 2 encabezados `###` de proyecto y enlaces como placeholders, para no afirmar que existe un repositorio público que aún no existe. → `CAP02_R03.txt`

Pruebas del proyecto tras el capítulo: 4 de 4 correctas → `CAP02_pruebas.txt`.

## Control de salida
| Verificación final | Marca |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos sin copiar el caso resuelto. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

**Mejora para el Capítulo 03:** registrar las observaciones de la interfaz en fichas reutilizables (`fichas/observaciones.md`) en lugar de notas sueltas, para compararlas luego con el propio repositorio.
