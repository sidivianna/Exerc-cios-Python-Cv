distancia = int(input("Qual é a distância da sua viagem: "))
print("Você está prestes a começar uma viagem de {:.2f} Km." .format(distancia))

if distancia <= 200:
    preço = distancia * 0.50
    print("O preço da sua passagem será de {:.2f}R$." .format(preço))
else: 
    preço = distancia * 0.45
    print("O preço da sua passagem será de {:.2f}R$." .format(preço))
