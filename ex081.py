lista = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break

print(lista.sort(reverse=True))
print(f"A lista teve {len(lista)} números digitados.")

if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista.")