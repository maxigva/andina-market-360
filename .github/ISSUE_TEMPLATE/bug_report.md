---
name: Error en el proceso de ventas
about: Cifra incorrecta, falla del script o diferencia entre CSV, JSON y tablero
title: "bug: "
labels: error
---

> Use solo datos **ficticios**. No pegue ventas reales, datos de clientes, contraseñas ni tokens.

## ¿Dónde aparece el error?
- [ ] `data/ventas.csv` (datos de entrada)
- [ ] `src/resumen.py` (cálculo)
- [ ] `docs/data/resumen.json` (publicación)
- [ ] `docs/index.html` (tablero)
- [ ] README / documentación

## Datos de entrada (muestra ficticia mínima)
```
id,fecha,sede,producto,cantidad,precio_unitario

```

## Pasos para reproducir
1.
2.
3.

## Resultado observado
Pegue la salida exacta del comando (por ejemplo, `python src/resumen.py`):
```

```

## Resultado esperado
Cifra o comportamiento correcto y cómo se calculó (fórmula o fila del CSV).

## Evidencia
Captura del tablero o salida del comando, solo con datos ficticios. Si no sabe usar la terminal, describa con sus palabras qué cifra vio y en qué página.

## Impacto para la empresa
¿Qué decisión de gerencia se vería afectada? ¿Qué sede?

## Entorno
- Sistema operativo:
- `python --version`:
- Commit (`git log -1 --oneline`):

## Criterio de cierre
- [ ] Prueba automática que reproduce el error y pasa tras la corrección.
- [ ] `python -m unittest discover -s tests -v` en `OK`.
