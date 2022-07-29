from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

jogador = int(input("Qual é a sua jogada? "))

print("===" * 10)
print("O computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("===" * 10)

if computador == 1: #computador pedra
    if jogador == 0:
        print("Empatou.")
    elif jogador == 1:
        print("jogador venceu.")
    elif jogador == 2:
        print("Computador venceu")
    else: 
        print("Jogada inválida.")

elif computador == 2: # computador papel
    if jogador == 0:
        print("Computador venceu.")
    elif jogador == 1:
        print("Empatou.")
    elif jogador == 2:
        print("Jogador venceu")
    else: 
        print("jogada inválida.")

elif computador == 3: # computador tesoura
    if jogador == 0:
        print("Jogador venceu.")
    elif jogador == 1:
        print("Computador venceu.")
    elif jogador == 2:
        print("Empate.")
    else: 
        print("jogada inválida.")

print("===" * 10)




