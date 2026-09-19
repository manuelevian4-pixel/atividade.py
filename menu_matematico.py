print("Menu de operações matemáticas")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha uma operação: ")

if opcao in ("1", "2", "3", "4"):
	primeiro_numero = float(input("Introduza o primeiro número: "))
	segundo_numero = float(input("Introduza o segundo número: "))

	match opcao:
		case "1":
			resultado = primeiro_numero + segundo_numero
		case "2":
			resultado = primeiro_numero - segundo_numero
		case "3":
			resultado = primeiro_numero * segundo_numero
		case "4":
			if segundo_numero == 0:
				resultado = None
				print("Não é possível dividir por zero.")
			else:
				resultado = primeiro_numero / segundo_numero

	if resultado is not None:
		print(f"Resultado: {resultado}")
else:
	print("Opção inválida.")
