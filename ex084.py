temp = [] # lista temporária
princ = [] # lista principal
mai = men = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        mai = men = temp[1] # tem na posição 1 que representa o vslor do peso.
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp [1] < men:
            men = temp[1]

    princ.append(temp[:]) # pega uma cópia do fatiamento
    temp.clear() # limpa o temp

    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break

print("==" * 20)
print(f"Os dados foram {princ}")
print(f"Ao todo voce cadastrou {len(princ)} pessoas. ")
print(f"O maior peso foi de {mai}Kg.", end='')
for p in princ: # Paracada pessoa em principal
    if p[1] == mai:
        print(f"[{p[0]}] ", end='')
print()

print(f"O menor peso foi de {men}kg.", end='')
for p in princ:
    if p[1] == men:
        print(f"[{p[0]}]", end='')
print()