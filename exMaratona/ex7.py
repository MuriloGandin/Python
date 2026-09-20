def contanums(lista):
    contagem = dict()
    for num in lista:
        if num not in contagem.keys():
            contagem[num] = 1
        else:
            contagem[num] += 1

    return contagem


n = int(input())
numeros = list(map(int, input().split()))
contagem = contanums(numeros)

for key in sorted(contagem):
    print(f"{key}: {contagem[key]}", end="\n")