# Andina Market 360 · Tablero comercial

Objetivo comercial: que la gerencia sepa **qué sede lidera las ventas ficticias** (Lima, Ica y Arequipa) con cifras calculadas por Python, probadas con `unittest` y mostradas en una página web estática.

Caso único del **Cuaderno de prácticas Git y GitHub (36 capítulos)**. Nunca contiene datos reales de personas ni de ventas.

## Problema
Las sedes consolidaban sus ventas editando informes a mano, lo que producía errores y demoras. Este repositorio calcula los totales directamente desde el CSV, de modo que cada cifra publicada se puede volver a obtener con un comando.

## Funcionalidades
- Lee `data/ventas.csv` (12 transacciones simuladas).
- Calcula totales por **sede**, **producto** y **mes**.
- Genera `docs/data/resumen.json` para la web.
- Muestra el resumen en `docs/index.html`, que lee el JSON generado (no cifras escritas a mano).
- Ejecuta las pruebas automáticamente en GitHub Actions en cada push y pull request.

## Uso del tablero de ventas por sede
El tablero (`docs/index.html`) permite que cada jefe de sede compare sus ventas con las de las otras dos sedes sin abrir el CSV.
El informe muestra primero las **ventas por sede** (Lima, Ica y Arequipa) con su total; después, las ventas por producto y por mes.

## Estructura
```
andina-market-360/
├── data/ventas.csv            Base ficticia de 12 ventas
├── data/ventas_muestra.csv    Muestra de 4 ventas para pruebas
├── src/resumen.py             Cálculo de totales (solo biblioteca estándar)
├── tests/test_resumen.py      Pruebas unitarias
├── docs/                      Sitio estático (index.html + data/resumen.json)
├── .github/workflows/ci.yml   Integración continua
├── capitulos/                 Desarrollo de cada capítulo del cuaderno
├── fichas/                    Fichas de trabajo (perfil, observaciones, diseño)
└── evidencias/                Salidas de terminal, registros y capturas
```

## Requisitos
- Python 3 (probado con 3.12 en GitHub Actions y 3.14 en local); no requiere instalar paquetes.
- Git, para clonar y versionar.
- Compruebe su versión con `python --version` (en algunos sistemas el comando es `python3`).

## Cómo ejecutar el análisis
Desde la raíz del repositorio:

```bash
# 1. Ver el resumen por sede en la terminal
python src/resumen.py

# 2. Ejecutar las pruebas
python -m unittest discover -s tests -v

# 3. Regenerar el JSON que usa la web
python src/resumen.py --json docs/data/resumen.json

# 4. Ver la web en http://localhost:8000 (detener con Ctrl+C)
python -m http.server 8000 --directory docs
```

Para probar con otro archivo, indique su ruta con `--csv`; por ejemplo, la muestra de 4 ventas:

```bash
python src/resumen.py --csv data/ventas_muestra.csv
```

Resultado esperado del paso 1 (salida real de `python src/resumen.py`):

```
Operaciones: 12
Lima       S/   814.00
Ica        S/   555.00
Arequipa   S/   476.00
TOTAL      S/  1845.00
```

Resultado esperado del paso 2: `Ran 5 tests` y `OK` (4 pruebas sobre la base de 12 ventas y 1 sobre la muestra). Si el paso 3 no cambia `docs/data/resumen.json` (`git status` limpio), la web ya muestra las cifras vigentes.

## Uso responsable
- Datos exclusivamente simulados: sin nombres, documentos ni correos de clientes.
- No se guardan contraseñas, tokens ni claves en el repositorio.
- El proyecto no se conecta automáticamente a servicios externos; GitHub solo aloja el código, las pruebas automáticas y la web.

## Licencia
El código y la documentación propia se publican bajo la licencia [MIT](LICENSE).
El cuaderno de prácticas que guía los capítulos es material de su autor; **no se incluye en este repositorio** ni queda cubierto por esta licencia.
