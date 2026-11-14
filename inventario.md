# Inventario de archivos iniciales – Andina Market 360

| Carpeta / archivo | Propósito | Revisa |
|---|---|---|
| README.md | Explica el objetivo, las carpetas y los comandos de prueba | Responsable de publicación |
| data/ventas.csv | 12 transacciones de ventas ficticias por sede | Analista de datos |
| src/resumen.py | Calcula los totales por sede con Python, sin librerías externas | Desarrollador |
| tests/test_resumen.py | 4 pruebas unitarias que validan el cálculo | Desarrollador |
| docs/ | Sitio estático que muestra el resumen (GitHub Pages) | Responsable de publicación |
| docs/data/resumen.json | Resultado generado por src/resumen.py para la web | Desarrollador |
| .github/workflows/ci.yml | Ejemplo de ejecución automática de pruebas | Desarrollador |

## Comprobación de seguridad
- Datos: todas las ventas son simuladas. No hay nombres, DNI ni correos de clientes reales.
- Secretos: no hay contraseñas, tokens ni claves privadas.
- Comando usado (PowerShell, en la raíz del proyecto):
  ```powershell
  Get-ChildItem -Recurse -File | Select-String -Pattern "password|contraseña|token|secret|@gmail|@hotmail"
  ```
- Resultado: sin coincidencias.
- Plantilla original: se conservó el ZIP sin modificar y se trabajó en una carpeta separada.
