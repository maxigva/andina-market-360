# andina-resumen (borrador)

Estructura propuesta del paquete; **no publicado**.

```
paquete_borrador/
├── pyproject.toml
├── README.md
└── andina_resumen/
    └── __init__.py      leer_ventas, sumar_por, resumir, texto
```

Las funciones se copiarían de `src/resumen.py` sin `main()` ni rutas por defecto. Uso:

```python
from andina_resumen import leer_ventas, resumir
print(resumir(leer_ventas("ventas.csv"))["total"])
```
