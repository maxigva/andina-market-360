# Propuesta: filtro por producto en el tablero (Reto 8.1)

**Necesidad:** la gerencia quiere ver cuánto vendió cada sede de un producto concreto (por ejemplo, *Leche 1L*) sin abrir el CSV. Origen: pregunta 4 de `fichas/ficha_gerencia.md`; tarea: Issue #4.

## Alcance propuesto
1. `src/resumen.py` acepta `--producto "<nombre>"` y calcula los totales por sede solo para ese producto.
2. El JSON incluye la lista de productos disponible para la web.
3. `docs/index.html` muestra un selector de producto que filtra la tabla por sede.

## Criterios de aceptación
- `python src/resumen.py --producto "Leche 1L"` muestra 3 sedes y un total calculado del CSV, no escrito a mano.
- Una prueba nueva valida el filtro con `data/ventas_muestra.csv`.
- `python src/resumen.py --producto "Pan"` (producto inexistente) muestra `Producto no encontrado: Pan` y termina con código de salida 1.
- Sin dependencias externas.

## Estado
Rama `feature/filtro-productos`: solo documentación. La implementación se revisará mediante un pull request (Cap. 14).
