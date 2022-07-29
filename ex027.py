n = str(input("Digite o seu nome: ")).strip()
nome = n.split() #divide o nome em pedaços
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}" .format(nome[0]))
print("Seu último nome é {}" .format(nome[len(nome)-1]))

