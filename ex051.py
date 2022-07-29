print("===" * 20)
print("                   10 termos de uma PA               ")
print("===" * 20)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao
for n in range (termo, decimo + razao, razao):
    print("{} " .format(n), end=' == ')

