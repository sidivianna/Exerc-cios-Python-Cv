listanum = []
mai = 0
men = 0


for c in range (0, 5):
    listanum.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]


print("==" * 20)
print(f"Voçê digitou os valores {listanum}")
print("==" * 20)
print(f"O maior valor digitado foi {mai}. nas posições")
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}...", end='')
print()
print(f"O menor valor digitado foi {men}. nas posições")
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}...", end=' ')


print("==" * 20)
