peso = float(input("Qual é o seu peso? (kg) "))
altura = float(input("Qaul é a sua altura? (m) "))

imc = peso / (altura ** 2)
print("O IMC desta pessoa é de {:.1f}" .format(imc))

if imc <= 18.5:
    print("Você esta abaixo do peso.")
elif imc <= 25:
    print("Voçê está no peso ideal.")
elif imc <= 30:
    print("Voçê está com sobrepeso.")
elif imc <= 40:
    print("Voçê está com obesidade.")
else:
    print("Voçê está com obesidade mórbida.")

