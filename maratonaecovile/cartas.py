# https://judge.beecrowd.com/pt/problems/view/1110
while True:    
    n = int(input())
    if n == 0:
        break

    cartas = list(range(1, n+1))
    descartadas = []

    while len(cartas) >= 2:
        descartadas.append(cartas.pop(0))
        cartas.append(cartas.pop(0))
            
    print("Discarded cards:", ", ".join(map(str, descartadas)))
    print(f"Remaining card: {cartas[0]}")