num = int(input("Digite um número: "))
print('''Escolha uma das bases de conversão:
[ 1 ] conversor para BINÁRIO
[ 2 ] conversor para OCTAL
[ 3 ] conversor para HEXADECIMAL''')

opçao = int(input("Sua opção: "))
if opçao == 1:
    print("{} convertido para BINÁRIO é igual a {}." .format(num, bin(num)[2:]))
elif opçao == 2:
    print("{} convertido para OCTAL é igual a {}." .format(num, oct(num)[2:]))
elif opçao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}." .format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente>")

