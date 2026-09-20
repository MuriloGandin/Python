i = input()
vogais = 0
for c in i:
    if c.lower() in "aeiou":
        vogais += 1

print(vogais)