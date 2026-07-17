valores = input().split(" ")

k = int(input())

ultimo_pedaco = valores[-k:]
primeiro_pedaco = valores[:-k]

novo = ultimo_pedaco + primeiro_pedaco

print(novo)
