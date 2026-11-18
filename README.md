# Andina Market 360

Objetivo comercial: que la gerencia sepa **qué sede lidera las ventas ficticias** (Lima, Ica y Arequipa) con cifras calculadas por Python, probadas con `unittest` y mostradas en una página web estática.

Caso único del **Cuaderno de prácticas Git y GitHub (36 capítulos)**. Nunca contiene datos reales de personas ni de ventas.

## Objetivo
Las sedes consolidaban sus ventas editando informes a mano, lo que producía errores y demoras. Este repositorio calcula los totales directamente desde el CSV, de modo que cada cifra publicada se puede volver a obtener con un comando.

Funcionalidades:
- Calcula totales por **sede**, **producto** y **mes** con Python estándar (sin paquetes externos).
- Genera `docs/data/resumen.json` para la web y el bloque de cifras de este README.
- Muestra el resumen en `docs/index.html`, que lee el JSON generado (no cifras escritas a mano).
- Ejecuta las pruebas automáticamente en GitHub Actions en cada push y pull request.

## Datos
- [`data/ventas.csv`](data/ventas.csv): 12 transacciones simuladas. **Procedencia:** el CSV fue creado para el curso con valores inventados; no proviene de ningún sistema de ventas real.
- [`data/ventas_muestra.csv`](data/ventas_muestra.csv): 4 ventas con totales conocidos, usadas por las pruebas.
- Columnas, indicadores y fórmulas: ver el [Manual](docs/manual.md).

## Requisitos
- Python 3 (probado con 3.12 en GitHub Actions y 3.14 en local); no requiere instalar paquetes.
- Git, para clonar y versionar.
- Compruebe su versión con `python --version` (en algunos sistemas el comando es `python3`).

## Inicio rápido
```bash
python -m unittest discover -s tests
python src/resumen.py
```

## Ejecución
Desde la raíz del repositorio:

```bash
# 1. Ver el resumen por sede en la terminal
python src/resumen.py

# 2. Ejecutar las pruebas
python -m unittest discover -s tests -v

# 3. Regenerar el JSON de la web y el bloque de cifras de este README
python src/resumen.py --json docs/data/resumen.json --readme README.md

# 4. Ver la web en http://localhost:8000 (detener con Ctrl+C)
python -m http.server 8000 --directory docs
```

Para probar con otro archivo, indique su ruta con `--csv`; por ejemplo, la muestra de 4 ventas:

```bash
python src/resumen.py --csv data/ventas_muestra.csv
```

Resultado del paso 1. Este bloque lo escribe `src/resumen.py --readme`; una prueba falla si deja de coincidir con el CSV:

<!-- resumen:inicio -->
```
Operaciones: 12
Lima       S/   814.00
Ica        S/   555.00
Arequipa   S/   476.00
TOTAL      S/  1845.00
```
<!-- resumen:fin -->

Si el paso 3 no deja cambios (`git status` limpio), la web y este README ya muestran las cifras vigentes.

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
├── tools/verificar_md.py      Verificación de enlaces y formato Markdown
├── docs/                      Sitio estático publicado con Pages (index.html, productos.html, style.css, data/resumen.json, manual.md)
├── .github/workflows/ci.yml   Integración continua
├── capitulos/                 Desarrollo de cada capítulo del cuaderno
├── fichas/                    Fichas de trabajo (perfil, observaciones, diseño)
└── evidencias/                Salidas de terminal, registros y capturas
```

## Documentación
- [Tablero publicado](https://maxigva.github.io/andina-market-360/) (GitHub Pages desde `main` + `/docs`).
- [Manual](docs/manual.md): instalación, datos, indicadores y verificación.
- [Guía de contribución](CONTRIBUTING.md): ramas, mensajes de commit, pruebas y reporte de errores.
- [Capítulos del cuaderno](capitulos/): evidencias de cada práctica.

## Uso responsable
- Datos exclusivamente simulados: sin nombres, documentos ni correos de clientes.
- No se guardan contraseñas, tokens ni claves en el repositorio.
- El proyecto no se conecta automáticamente a servicios externos; GitHub solo aloja el código, las pruebas automáticas y la web.

## Licencia
El código y la documentación propia se publican bajo la licencia [MIT](LICENSE).
El cuaderno de prácticas que guía los capítulos es material de su autor; **no se incluye en este repositorio** ni queda cubierto por esta licencia.
