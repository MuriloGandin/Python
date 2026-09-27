# https://judge.beecrowd.com/pt/problems/view/1024

def criptografia1(texto):
    resultado = ""
    for c in texto:
        if c.isalpha():
            r = chr(ord(c) + 3)
        else: r = c

        resultado += r

    return resultado


def criptografia2(texto):
    return texto[::-1]


def criptografia3(texto):
    meioTexto = len(texto) // 2
    resultado = texto[:meioTexto]
    for c in texto[meioTexto:]:
        r = chr(ord(c)-1)
        resultado += r

    return resultado


n = int(input())

for _ in range(n):
    texto = input()

    texto = criptografia1(texto)
    texto = criptografia2(texto)
    texto = criptografia3(texto)

    print(texto)
