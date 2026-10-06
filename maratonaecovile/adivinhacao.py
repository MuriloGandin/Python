# https://judge.beecrowd.com/pt/problems/view/1340
import sys

for linha in sys.stdin:
    n = int(linha)

    stack = []
    queue = []
    priority = []

    stack_possivel = True
    queue_possivel = True
    priority_possivel = True

    for i in range(n):
        linha = list(map(int, input().split()))
        comando = linha[0]
        valor = linha[1]

        if comando == 1:
            
            stack.append(valor)
            queue.append(valor)
            priority.append(valor)

        elif comando == 2:

            if stack_possivel:
                if stack.pop() != valor:
                    stack_possivel = False

            if queue_possivel:
                if queue.pop(0) != valor:
                    queue_possivel = False

            if priority_possivel:
                maior = max(priority)
                priority.remove(maior)

                if maior != valor:
                    priority_possivel = False

    possibilidades = []

    if stack_possivel:
        possibilidades.append("stack")

    if queue_possivel:
        possibilidades.append("queue")

    if priority_possivel:
        possibilidades.append("priority queue")

    if len(possibilidades) == 0:
        print("impossible")
    elif len(possibilidades) > 1:
        print("not sure")
    else:
        print(possibilidades[0])