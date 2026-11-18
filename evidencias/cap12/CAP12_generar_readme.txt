$ sed -n "/resumen:inicio/,/resumen:fin/p" README.md; python -m unittest discover -s tests 2>&1 | grep -E "^(FAIL|Ran|OK|FAILED)"; echo "--- se genera el bloque desde el CSV:"; python src/resumen.py --json docs/data/resumen.json --readme README.md; sed -n "/resumen:inicio/,/resumen:fin/p" README.md; python -m unittest discover -s tests 2>&1 | tail -n 2; python src/resumen.py --json docs/data/resumen.json --readme README.md > /dev/null; git status --short README.md docs/ | wc -l | sed "s/^/archivos que cambian al regenerar otra vez (README y JSON, sin contar la primera escritura): /"
<!-- resumen:inicio -->
<!-- resumen:fin -->
FAIL: test_readme_muestra_cifras_calculadas (test_resumen.TestResumen.test_readme_muestra_cifras_calculadas)
Ran 6 tests in 0.009s
FAILED (failures=1)
--- se genera el bloque desde el CSV:
Operaciones: 12
Lima       S/   814.00
Ica        S/   555.00
Arequipa   S/   476.00
TOTAL      S/  1845.00
README actualizado: README.md
JSON generado: docs/data/resumen.json
<!-- resumen:inicio -->
```
Operaciones: 12
Lima       S/   814.00
Ica        S/   555.00
Arequipa   S/   476.00
TOTAL      S/  1845.00
```
<!-- resumen:fin -->

OK
archivos que cambian al regenerar otra vez (README y JSON, sin contar la primera escritura): 2
(Nota: el conteo anterior incluye el README aún sin confirmar; tras el commit 2dbc497 se repite la comprobación de idempotencia:)
$ python src/resumen.py --json docs/data/resumen.json --readme README.md > /dev/null; git status --short README.md docs/data/; echo "cambios tras regenerar: $(git status --porcelain README.md docs/data/ | wc -l)"
cambios tras regenerar: 0
