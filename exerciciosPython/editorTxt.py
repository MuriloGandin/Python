stack = []
while True:
    entrada = input().split()
    if len(entrada) < 1 or len(entrada) > 2:
        exit()

    comando = entrada[0]

    match comando:
        case "ADD":
            stack.append(entrada[1])

        case "FIM":
            texto = ""
            for palavra in stack:
                texto += palavra + " "
            print(texto)
            break

        case _:
            print("comandos: ADD, UNDO, FIM")
