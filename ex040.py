n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

print("Tirando {} e {} a média do aluno é {}." .format(n1, n2, media))

if media >= 7:
    print("O aluno está APROVADO!")
elif media > 5 and media <= 6.9:
    print("O aluno está em RECUPERAÇÃO!")
else:
    print("O aluno está REPROVADO!")
