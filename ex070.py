print("==" * 20)
print("LOJA BARATO")
print("==" * 20) 

total = cont = totmil = menor = 0
barato = " "

while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço do produto: "))
    total += preço
    cont += 1

    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor: 
        menor = preço
        barato = produto

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        break

print(f"O valor total da compra foi de {total}")
print(f"Temos {totmil} produtos custando mais de 1000 R$.")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")
print("Fim.")