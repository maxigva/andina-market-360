"""Verifica enlaces relativos y formato básico de archivos Markdown.

Uso: python tools/verificar_md.py README.md CONTRIBUTING.md docs/manual.md
Sale con código 1 si encuentra errores.
"""
import re
import sys
from pathlib import Path

ENLACE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TUBERIA = re.compile(r"(?<!\\)\|")


def revisar(ruta):
    errores, en_codigo, celdas_tabla = [], False, None
    for n, linea in enumerate(Path(ruta).read_text(encoding="utf-8").splitlines(), 1):
        if linea.lstrip().startswith("```"):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        if re.match(r"^#{1,6}[^#\s]", linea):
            errores.append(f"{ruta}:{n}: encabezado sin espacio después de #")
        if linea.lstrip().startswith("|"):
            celdas = len(TUBERIA.findall(linea))
            if celdas_tabla is not None and celdas != celdas_tabla:
                errores.append(f"{ruta}:{n}: fila con {celdas - 1} columnas (se esperaban {celdas_tabla - 1})")
            celdas_tabla = celdas if celdas_tabla is None else celdas_tabla
        else:
            celdas_tabla = None
        for destino in ENLACE.findall(linea):
            if re.match(r"^[a-zA-Z]:\\|^file:", destino):
                errores.append(f"{ruta}:{n}: enlace a ruta local absoluta: {destino}")
            elif not re.match(r"^(https?:|mailto:|#)", destino):
                objetivo = (Path(ruta).parent / destino.split("#")[0]).resolve()
                if not objetivo.exists():
                    errores.append(f"{ruta}:{n}: enlace roto: {destino}")
    if en_codigo:
        errores.append(f"{ruta}: bloque de código sin cerrar")
    return errores


if __name__ == "__main__":
    todos = [e for ruta in sys.argv[1:] for e in revisar(ruta)]
    print("\n".join(todos) if todos else f"OK: {len(sys.argv) - 1} archivo(s) sin errores")
    sys.exit(1 if todos else 0)
