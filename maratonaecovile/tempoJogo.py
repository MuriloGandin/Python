# https://judge.beecrowd.com/pt/problems/view/1046
inicio, fim = list(map(int, input().split()))

if inicio == fim:
    t = 24
elif inicio < fim:
    t = fim - inicio
else :
    t = 24 - inicio + fim

print(f"O JOGO DUROU {t} HORA(S)")