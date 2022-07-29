salario = int(input("Qual é o salário do funcionário? "))
if salario < 1250: 
    nsal = salario + (salario * 0.15)
else:
    nsal = salario + (salario * 0.10)
    
print("Quem ganhava {:.2f} passa a ganhar {:.2f}." .format(salario, nsal))

