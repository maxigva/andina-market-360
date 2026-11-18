# Diseño de repositorio para otra tienda (Reto 4.1)

**Caso ficticio:** *Ferretería Costa Sur*, con locales en Chiclayo y Piura. Objetivo: controlar el stock mínimo de 20 productos.

```
ferreteria-costa-sur/
├── data/        inventario.csv y movimientos.csv (datos simulados)
├── src/         stock.py: calcula existencias y alerta stock mínimo
├── tests/       test_stock.py: valida cálculos con un CSV pequeño de prueba
├── reportes/    salidas generadas (alertas.json); se regeneran, no se editan
├── docs/        página estática que lee reportes/alertas.json
├── README.md
├── LICENSE
└── .gitignore   __pycache__/, .venv/, .env, temporales
```

| Carpeta | Función definida | ¿Se edita a mano? |
|---|---|---|
| `data/` | Entradas del análisis | Sí, solo con datos ficticios |
| `src/` | Lógica de cálculo | Sí |
| `tests/` | Pruebas automáticas | Sí |
| `reportes/` | Resultados generados por `src/` | No: se regeneran |
| `docs/` | Presentación web | Solo la plantilla HTML |

Diferencia con Andina Market 360: se separa `reportes/` de `docs/` porque la ferretería necesita alertas en JSON para otros sistemas además de la web.
