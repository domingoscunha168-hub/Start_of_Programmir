import random

numeros = tuple(random.randint(1, 100) for _ in range(60))

print('Numeros gerados na tupla:')
print(numeros)

print(f' \nTotal de numeros: {len(numeros)}')
print(f'Menor valor: {min(numeros)}')
print(f'Maior valor: {max(numeros)}')

print(' \nListagem dos numeros:')
for posicao, numero in enumerate(numeros, start=1):
    print(f"{posicao:2d}º número: {numero}")
