from unicodedata import category


cato = float(input("Comprimento do cateto oposto: "))
cata = float(input("Comprimento do cateto adjacente: "))

hip = (cato ** 2 + cata ** 2) ** (1/2) #usa-se o **(1/2) para se encontrar a raiz quadrada.
print(f"A hipotenusa vai medir: {hip}")