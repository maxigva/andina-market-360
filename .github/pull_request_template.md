## Resumen
<!-- Qué cambia y por qué, en 2-3 líneas. -->

Atiende: #

## Cómo verificarlo
<!-- Comandos exactos y resultado esperado. -->
```bash
python -m unittest discover -s tests -v
```

## Lista de comprobación
- [ ] Las pruebas unitarias terminan en `OK` (local y GitHub Actions).
- [ ] No hay contraseñas, tokens, claves ni archivos `.env` en el diff.
- [ ] Solo hay datos **ficticios**; ninguna cifra escrita a mano (se generan con `src/resumen.py`).
- [ ] La documentación (README, manual o CHANGELOG) está actualizada si cambia el uso.
- [ ] *Files changed* muestra solo los archivos previstos.
- [ ] Capturas del tablero, si cambia la web (sin datos personales ni pestañas privadas).

<!-- Para cambios en data/ use la plantilla de calidad de datos:
     agregue ?template=calidad_datos.md a la URL del PR. -->
