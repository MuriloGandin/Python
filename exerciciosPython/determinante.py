tamanho = int(input())
matriz = []

for _ in range(tamanho):
    matriz.append(input().split(" "))

diagonalP = 0
diagonalS = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        print(matriz[linha][coluna], end=" ")

    print()