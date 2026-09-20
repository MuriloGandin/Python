def isPalindromo(texto):
    return texto == texto[::-1]
       

texto = input().lower()
if isPalindromo(texto):
    print("SIM")
else:
    print("NÃO")