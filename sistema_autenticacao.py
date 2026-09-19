palavra_passe_correta = "python123"
tentativas = 0
acesso_autorizado = False

while tentativas < 3 and not acesso_autorizado:
	palavra_passe = input("Introduza a palavra-passe: ")
	tentativas += 1

	if palavra_passe == palavra_passe_correta:
		acesso_autorizado = True
		print("Acesso autorizado.")
	else:
		tentativas_restantes = 3 - tentativas

		if tentativas_restantes > 0:
			print(f"Palavra-passe incorreta. Restam {tentativas_restantes} tentativa(s).")

if not acesso_autorizado:
	print("Acesso bloqueado após 3 tentativas incorretas.")
