texto = input()

contagemCaracteres = {}

for c in texto:
    contagemCaracteres[c] = contagemCaracteres.get(c, 0) + 1

for item, quantidade in contagemCaracteres.items():
    if quantidade == 1:
        print(item)