# Registro de cambios

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/). Cada entrada cita el commit o el PR que la respalda. Esquema de versiones: [VERSIONES.md](VERSIONES.md).

## [1.0.0] – 2026-11-18
Primera versión de Andina Market: resumen verificable de ventas ficticias por sede y tablero estático.

### Añadido
- Gráfico de barras de ventas por sede en el tablero, calculado desde `resumen.json` (#1, PR #8: `4120a55`, `11dda2e`).
- Presentación del tablero con sedes, período y origen ficticio de los datos (#3, PR #6: `61b2e9d`, `56098bf`).
- Bloque de cifras del README generado por `src/resumen.py --readme`, con prueba que falla si no coincide con el CSV (`2dbc497`).
- CSV de muestra de 4 ventas y su prueba de totales conocidos (`778f942`, `be19b40`).
- Manual, guía de contribución y verificador de Markdown `tools/verificar_md.py` (`fba5946`).
- Plantillas de Issues (`b6168d7`), plantillas de PR y `CODEOWNERS` (`91bbd2a`).

### Cambiado
- El tablero pasa a llamarse “Tablero de ventas por sede” (`2e67da0`).
- El JSON se escribe con finales de línea LF y salto final; `.gitattributes` normaliza el texto (`902b0ac`).
- README reorganizado en Objetivo, Datos, Requisitos, Inicio rápido y Ejecución (`fba5946`).

### Corregido
- La prueba `test_json_coincide_con_csv` ahora compara el JSON **publicado** con el CSV; antes la web podía mostrar cifras viejas sin que fallara ninguna prueba (#2, `bc936f5`).
- La frase “Lima lidera con S/ 814.00” estaba escrita a mano; ahora se calcula y una prueba impide cifras fijas en el HTML (PR #8, `11dda2e`).
- El verificador de Markdown marcaba como rotos los enlaces dentro de código en línea (#5, `e096234`).
- Encabezado del tablero en el README (`f70b537`).

### Pendiente (no incluido en 1.0.0)
- Filtro por producto: solo existe la propuesta (`fichas/propuesta_filtro_productos.md`, PR #7); la funcionalidad sigue abierta en #4.
- Porcentaje de participación en cada barra: sugerencia de la revisión del PR #8, no implementada.
