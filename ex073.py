times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atllético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print("===" * 30)
print(f'Lista de times do campeonato brasileiro: {times}')
print("===" * 30)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print("===" * 30)
print(f'Os quatro ultimos colocados são: {times[-4:]}')
print('===' * 30)
print(f"Em ordem alfabbética os times são: {sorted(times)} ")
print('===' * 30)
print(f'A Chapecoense está na {times.index("Chapecoense") +1 }ª posição.')