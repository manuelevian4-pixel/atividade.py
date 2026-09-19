idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal do cliente: R$ "))

if idade < 0 or renda < 0:
	print("Idade e renda devem ser valores positivos.")
elif renda < 2000:
	print("Categoria: Bronze")
elif renda < 5000:
	print("Categoria: Prata")
elif renda < 10000:
	print("Categoria: Ouro")
else:
	print("Categoria: Diamante")
