# https://judge.beecrowd.com/pt/problems/view/1068
import sys

def funcaoehvalida(funcao):
    abertoc = 0
    aberto = list()
    fechadoc = 0
    for c in funcao:
        if c =='(':
            abertoc += 1
            aberto.append(True)

        if c == ')':
            fechadoc += 1
            try:
                aberto.pop(0)
            except:
                return False

    if abertoc != fechadoc: return False
    if len(aberto) != 0: return False

    return True

for entrada in sys.stdin:
    try:
        valor = "correct" if funcaoehvalida(entrada) else "incorrect"
        print(valor)

    except:
        exit(0)
