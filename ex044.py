print("==" * 20)
print(" ============ LOJA VIANNA ============")
print("==" * 20)

preço = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2 x no cartão
[ 4 ] 3 x ou mais no cartão''')

opçao = int(input("Qual é a sua opção? "))

if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = preço / 2
    print("Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS!" .format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Qual o total de parcelas? "))
    parcela = total / totparc
    print("Sua compra será parceladad em {}x de R${:.2f}. COM JUROS!" .format(totparc, parcela))
else:
    total = preço
    print("Opção inválida! Tente novamente.")

print("Sua compra de R${:.2f}, vai custar no final R${:.2f}" .format(preço, total))

