print("===" * 12) 
print(" --- ANALIZADOR DE TRIÂNGULOS ----")
print("===" * 12) 

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceito segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segementos de reta acima PODEM formar um triângulo!")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else: 
        print("ISÓSCELES!")

else: 
    print("Os segmentos de reta acima NÃO PODEM FORMAR UM TRIÂNGULO.")