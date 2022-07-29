from datetime import date
atual = date.today().year

ano = int(input("Ano de nascimento: "))
idade = atual - ano
print("O atleta tem {} anos." .format(idade))

if idade <= 9:
    print("Categoria MIRIN.")
elif idade <= 14:
    print("Categoria INFANTIL.")
elif idade <= 19:
    print("Categoria JÚNIOR.")
elif idade <= 25:
    print("Categoria SÊNIOR.")
else: 
    print("Categoria MASTER.")