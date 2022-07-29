num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)

    else:
        num[1].append(valor)

print("==" * 20)
num[0].sort()
num[1].sort()
print(f"Os valores pares são :{num[0]}")
print(f"Os valores ímpares são: {num[1]}")


# Corrigir para uma unica lista que contenha todos os valores e so separe na hora de exibir os valores.