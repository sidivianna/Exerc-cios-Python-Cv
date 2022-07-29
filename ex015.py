dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
total = (dias * 60) + (km * 0.15)

print(f"O valor total a ser pago é de {total}R$.")