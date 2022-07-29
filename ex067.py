while True:
    n = int(input("Digite umvalr para ver sua tabuada: "))
    if n < 0:
        break

    print("==" * 20)
    for c in range(1, 11):
        print(f"{n} x {c} = {n * c}")
    print("==" *20)

print("Fim do programa.")








