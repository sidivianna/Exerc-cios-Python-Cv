velocidade = int(input("Qual a velocidade do carro? "))
if velocidade <= 80:
    print("Boa viagem!!!")
else: 
    excedente = velocidade - 80
    multa = excedente * 7
    print("MULTADO! Você ultrapassou o limite de velocidade que é de 80 km/h.")
    print("Você terá de pagar uma multa de {:.2f}!" .format(multa))
print("Tenha um bom dia. Dirija com segurança!")