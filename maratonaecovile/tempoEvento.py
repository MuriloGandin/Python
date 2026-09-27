# https://judge.beecrowd.com/pt/problems/view/1061
diai = int(input().split()[1])
horai, minutoi, segundoi = map(int, input().split(" : "))

diaf = int(input().split()[1])
horaf, minutof, segundof = map(int, input().split(" : "))

inicio = diai * 86400 + horai * 3600 + minutoi * 60 + segundoi
fim = diaf * 86400 + horaf * 3600 + minutof * 60 + segundof

duracao = fim - inicio

dias = duracao // 86400
duracao %= 86400

horas = duracao // 3600
duracao %= 3600

minutos = duracao // 60
segundos = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")