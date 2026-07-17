import sys

for linha in sys.stdin:
    digito, codigo = linha.split()

    if digito == "0" and codigo == "0":
        break

    resultado = "".join(c for c in codigo if c != digito)

    resultado = resultado.lstrip("0")
    if resultado == "":
        resultado = "0"

    print(resultado)