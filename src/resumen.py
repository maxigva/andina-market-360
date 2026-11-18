"""Resumen de ventas ficticias de Andina Market 360."""
import argparse
import csv
import json
from pathlib import Path

CSV_POR_DEFECTO = Path(__file__).resolve().parent.parent / "data" / "ventas.csv"


def leer_ventas(ruta=CSV_POR_DEFECTO):
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
    return {
        "operaciones": len(ventas),
        "total": round(sum(por_sede.values()), 2),
        "por_sede": por_sede,
        "por_producto": sumar_por(ventas, "producto"),
        "por_mes": sumar_por(ventas, "mes"),
    }


def main():
    parser = argparse.ArgumentParser(description="Resumen de ventas por sede")
    parser.add_argument("--csv", default=CSV_POR_DEFECTO, help="ruta del CSV")
    parser.add_argument("--json", help="ruta del JSON de salida")
    args = parser.parse_args()

    r = resumir(leer_ventas(args.csv))
    print(f"Operaciones: {r['operaciones']}")
    for sede, total in r["por_sede"].items():
        print(f"{sede:<10} S/ {total:>8.2f}")
    print(f"{'TOTAL':<10} S/ {r['total']:>8.2f}")

    if args.json:
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        texto = json.dumps(r, ensure_ascii=False, indent=2) + "\n"
        Path(args.json).write_text(texto, encoding="utf-8", newline="\n")
        print(f"JSON generado: {args.json}")


if __name__ == "__main__":
    main()
