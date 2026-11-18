"""Empaqueta una versión etiquetada del tablero en dist/ (sin .git, .env ni temporales).

Uso: python tools/empaquetar.py v1.0.0
Lee los archivos desde el tag con `git show`, así el paquete contiene exactamente esa versión,
aunque la carpeta de trabajo tenga cambios posteriores.
"""
import hashlib
import subprocess
import sys
import zipfile
from pathlib import Path

ARCHIVOS = ["README.md", "LICENSE", "CHANGELOG.md", "VERSIONES.md",
            "docs/index.html", "docs/productos.html", "docs/style.css", "docs/data/resumen.json"]


def leer(ref, ruta):
    r = subprocess.run(["git", "show", f"{ref}:{ruta}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def empaquetar(ref):
    contenido = {ruta: datos for ruta in ARCHIVOS if (datos := leer(ref, ruta)) is not None}
    hoja = [f"Andina Market 360 {ref}", "Licencia: MIT (ver LICENSE). Datos ficticios.",
            "Uso sin internet: python -m http.server 8000 --directory docs  ->  http://localhost:8000", "",
            "Archivo | bytes | sha256"]
    hoja += [f"{r} | {len(d)} | {hashlib.sha256(d).hexdigest()[:16]}" for r, d in contenido.items()]
    salida = Path("dist") / f"andina-market-360-{ref}.zip"
    salida.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        for ruta, datos in contenido.items():
            z.writestr(f"andina-market-360-{ref}/{ruta}", datos)
        z.writestr(f"andina-market-360-{ref}/CONTENIDO.txt", "\n".join(hoja) + "\n")
    return salida, contenido


if __name__ == "__main__":
    ref = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    ruta, contenido = empaquetar(ref)
    print(f"{ruta}: {len(contenido)} archivos + CONTENIDO.txt, {ruta.stat().st_size} bytes")
