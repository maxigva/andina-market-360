"""andina-resumen (borrador): API reutilizable extraída de src/resumen.py, sin rutas por defecto."""
import csv

__version__ = "0.1.0"
__all__ = ["leer_ventas", "sumar_por", "resumir", "texto"]


def leer_ventas(ruta):
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def sumar_por(ventas, campo):
    totales = {}
    for v in ventas:
        monto = int(v["cantidad"]) * float(v["precio_unitario"])
        clave = v[campo] if campo != "mes" else v["fecha"][:7]
        totales[clave] = round(totales.get(clave, 0) + monto, 2)
    return totales


def resumir(ventas):
    por_sede = sumar_por(ventas, "sede")
    return {"operaciones": len(ventas), "total": round(sum(por_sede.values()), 2), "por_sede": por_sede,
            "por_producto": sumar_por(ventas, "producto"), "por_mes": sumar_por(ventas, "mes")}


def texto(r):
    lineas = [f"Operaciones: {r['operaciones']}"]
    lineas += [f"{sede:<10} S/ {total:>8.2f}" for sede, total in r["por_sede"].items()]
    lineas.append(f"{'TOTAL':<10} S/ {r['total']:>8.2f}")
    return "\n".join(lineas)
