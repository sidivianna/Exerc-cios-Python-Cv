a = input("Digite um valor: ")
print("O tipo primitivo deste valor é: ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Esta em maiúsculos? ", a.isupper())
print("Está em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())