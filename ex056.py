totmasc = 0
totfem = 0
fem20 = 0
totidade = 0
maisvelho = 0
nomemaisv = 0

for pess in range(1, 5):
    print("====== {}ª PESSOA ======".format(pess))

    nome = str(input("Nome: " .format(pess)))
    idade = int(input("Idade: " .format(pess)))
    sexo = str(input("Sexo: [M\F]" .format(pess))).upper()
    totidade += idade
    mediaid = (totidade / 4)

    if sexo == "F":
        totfem += 1
        if idade < 20:
            fem20 +=1
    else:
        totmasc += 1
        if idade > maisvelho:
            maisvelho = idade
            nomemaisv = nome

print("A média de idade do grupo é de {} anos. ".format(mediaid))
print("Ao todo são {} mulhers e {} homens." .format(totfem, totmasc))
print("O homem mais velho é o {}, e tem {} anos." .format(nomemaisv, maisvelho))
print("Ao todo são {} mulheres com menos de 20 anos." .format(fem20))

