numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma opção (1-4): "))

match opcao:
    case 1:
        resultado = numero1 + numero2
        print(f"Resultado: {resultado}")
    case 2:
        resultado = numero1 - numero2
        print(f"Resultado: {resultado}")
    case 3:
        resultado = numero1 * numero2
        print(f"Resultado: {resultado}")
    case 4:
        resultado = numero1 / numero2
        print(f"Resultado: {resultado}")
    case _:
        print("Opção inválida")
