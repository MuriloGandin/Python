length = input()
nums = sorted(list(map(int, input().split())))
obj = int(input())

esquerda = 0
direita = len(nums)-1

while esquerda < direita:
    soma = nums[esquerda] + nums[direita] 
    if soma < obj:
        esquerda += 1
    elif soma > obj:
        direita -= 1
    elif soma == obj:
        print("SIM")
        exit(0)

print("NÃO")
