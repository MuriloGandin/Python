# https://judge.beecrowd.com/pt/problems/view/1013

a, b, c = list(map(int, input().split()))

maiorab = (a + b + abs(a - b)) // 2
maiorabc = (maiorab + c + abs(maiorab - c)) //2

print(f"{maiorabc} eh o maior")