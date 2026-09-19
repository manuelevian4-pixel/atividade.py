numeros = []

for posicao in range(5):
	numero = float(input(f"Introduza o {posicao + 1}.º número: "))
	numeros.append(numero)

soma = 0
maior = numeros[0]
menor = numeros[0]

for numero in numeros:
	soma += numero

	if numero > maior:
		maior = numero

	if numero < menor:
		menor = numero

media = soma / len(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
