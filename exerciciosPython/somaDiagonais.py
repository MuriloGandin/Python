tamanho = int(input())
matriz = []

for _ in range(tamanho):
    linha = list(map(int, input().split()))
    matriz.append(linha)

diagonalP = 0
diagonalS = 0
for i, linha in enumerate(matriz):
    diagonalP += linha[i]
    diagonalS += linha[tamanho - 1 - i]

print(diagonalP)
print(diagonalS)