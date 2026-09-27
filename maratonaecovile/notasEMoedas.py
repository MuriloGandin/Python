# https://judge.beecrowd.com/pt/problems/view/1021
centstotal = int(float(input()) * 100)

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")

for nota in notas:
    quantidade = centstotal // nota
    centstotal %= nota
    print(f"{quantidade} nota(s) de R$ {(nota / 100):.2f}")

print("MOEDAS:")

for moeda in moedas:
    quantidade = centstotal // moeda
    centstotal %= moeda
    print(f"{quantidade} moeda(s) de R$ {(moeda / 100):.2f}")