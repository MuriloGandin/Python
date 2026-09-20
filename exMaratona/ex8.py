n = int(input())
resultados=""
for linha in range(n):
    valores = list(map(int, input().split()))
    resultados += str(sum(valores)) + "\n"

print(resultados, end="")