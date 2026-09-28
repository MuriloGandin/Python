# https://judge.beecrowd.com/pt/problems/view/1038
item, quant = list(map(int, input().split()))

precos = {
    1: 400,
    2: 450,
    3: 500,
    4: 200,
    5: 150
}

print(f"Total: R$ {(precos[item] * quant) / 100:.2f}")