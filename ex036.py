valor = int(input("Qual é o valor da casa? "))
salario = int(input("Qual é o salário do comprador? "))
tempo = int(input("Quantos anos de financiameto? "))

prestacao = valor / (tempo * 12)

if prestacao <= (salario * 0.30):
    print("Para pagar uma casa no valor de {:.2f} em {} anos, o valor da prestação mensal será de {:.2f}." .format(valor, tempo, prestacao))
    print("Empréstimo pode ser CONCEDIDO.")
else: 
    print("Para pagar uma casa no valor de {:.2f} em {} anos, o valor da prestação mensal será de {:.2f}.".format(valor, tempo, prestacao))
    print("Empréstimo NEGADO.")
