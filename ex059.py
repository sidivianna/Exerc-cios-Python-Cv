from time import sleep


n1 = int(input("Primeiro valor: "))
n2 = int(input("segundo valor: "))
opçao = 0

print("===" * 20)

while opçao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa
    ''')
    opçao = int(input(">>>>>>>> Qual é a sua opção? <<<<<<<<"))

    if opçao == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é {}." .format(n1, n2, soma))
    elif opçao == 2: 
        multiplicaçao = n1 * n2
        print("A multiplicação entre {} e {} é {}." .format(n1, n2, multiplicaçao))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2
        print("Entre {} e {} o maior valor é {}." .format(n1, n2, maior))
    elif opçao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif opçao == 5:
        print("Finalizando...")
    else: 
        print("Opção inválida. Tente novamente. ")
    
    print("===" * 20)
    sleep(2)


print("Fim do programa.")

    