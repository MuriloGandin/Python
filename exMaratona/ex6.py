import sys
soma = 0
for linha in sys.stdin:
    nums = list(map(int, linha.split()))
    soma += sum(nums)

print(soma) 
