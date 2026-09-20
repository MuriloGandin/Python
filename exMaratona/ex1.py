n = int(input())
valores = list(map(int, input().split()))
pares = []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

print(sum(pares))