nome = str(input("Digite seu nome completo: "))
print("Aanalizando seu nome...")
print("Seu nome em maiúsculas é {}." .format(nome.upper()))
print("Seu nome em minúsculas é {}." .format(nome.lower()))
print("Seu nome ao todo tem {} letras." .format(len(nome) - nome.count(' ')))

