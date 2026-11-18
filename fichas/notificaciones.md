# Ficha de notificaciones útiles

Ruta en GitHub: **Settings → Notifications** (y el botón **Watch** de cada repositorio).

| Tipo de aviso | ¿Recibir? | Canal | Motivo |
|---|---|---|---|
| Issues en los que participo o me asignan | Sí | Web (bandeja *Notifications*) | Son tareas propias del caso |
| Pull requests: revisiones solicitadas | Sí | Web + correo registrado en GitHub | Bloquean la integración si nadie revisa |
| Pull requests de todo el repositorio | Solo *Participating* | Web | Evita ruido de cambios ajenos |
| Alertas de seguridad (Dependabot) | Sí | Web + correo registrado en GitHub | Riesgo real, prioridad alta |
| Ejecuciones fallidas de Actions | Sí, solo fallos | Web | Interesa solo cuando algo se rompe |
| Actividad de repositorios que sigo (*Watching*) | No | — | Demasiado ruido |

Configuración prudente elegida: **Participating and @mentions** por defecto, **Watch → Custom** (Issues, Pull requests, Security alerts) en `andina-market-360`.

## Silenciar un repositorio de prueba
1. Abrir el repositorio de prueba.
2. Botón **Watch** (o **Unwatch**) → elegir **Ignore**.
3. Si ya hay hilos abiertos: en **Notifications**, filtrar por el repositorio → seleccionar → **Unsubscribe** o **Mark as done**.
4. Para deshacerlo: **Watch → Participating and @mentions**.

> Esta ficha no registra ninguna dirección de correo: “correo registrado en GitHub” se refiere al que cada persona configura dentro de la plataforma.
