from random import randint
from time import sleep
computador = randint(0, 5)

print("==" * 30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar qual...")
print("==" * 30)
jogador = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(3)

if jogador == computador: 
    print("Parabéns! Você acertou!")
else: 
    print("Ganhei! Eu pensei no número {} e não no número {}!" .format(computador, jogador))




