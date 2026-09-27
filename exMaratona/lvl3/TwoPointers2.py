length = input()
nums = list(map(int, input().split()))
obj = int(input())

esquerda = 0
direita = len(nums)-1
total = 0

while(esquerda < direita):
    soma = nums[esquerda] + nums[direita]

    if soma < obj:
        esquerda += 1
    elif soma > obj:
        direita -= 1
    elif soma == obj:
        total += 1
        esquerda += 1
        

print(f"total: {total}")