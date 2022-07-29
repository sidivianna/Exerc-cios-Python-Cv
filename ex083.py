expr = str(input("Digite uma expressão: "))
pilha = []

for simb in expr:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop() #remove a ultima expressão.
        else: 
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expressão está inválida!")
else:
    print("Sua expressão esta errada!")