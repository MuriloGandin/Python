n = int(input())
valores = list(map(int, input().split()))

menor = valores[0]
maior = valores[0]
for n in valores:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f"Maior: {maior}\nMenor: {menor}")