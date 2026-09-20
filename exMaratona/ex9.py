def contarCaracteres(texto):
    resultado = {}

    for c in texto:
        if c not in resultado:
            resultado[c] = 1
        else:
            resultado[c] += 1

    return resultado


senha = input()
tentativas = int(input())

frequencia_senha = contarCaracteres(senha)

resultados = ""

for _ in range(tentativas):
    tentativa = input()

    if contarCaracteres(tentativa) == frequencia_senha:
        resultados += "SIM\n"
    else:
        resultados += "NAO\n"

print(resultados, end="")