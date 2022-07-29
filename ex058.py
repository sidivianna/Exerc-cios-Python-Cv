from random import randint
computador = randint(0, 11)
palpite = 0

print("Olá. Sou seu computador.")
print("Acabeide pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")

acertou = False

while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
        
    else:
        if jogador < computador:
            print("Mais... Tente novamente")  
        if jogador > computador:
            print("Menos... Tente novamente.")
            

print("Parabéns. Você acertou com {} tentativas!" .format(palpite))