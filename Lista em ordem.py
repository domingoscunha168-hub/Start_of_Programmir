numeros = []

for d in range(1, 6):
    numero = int(input(f'Informe o {d}o valor: '))

    if d == 1 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                print(f'Adicionado na posicao {pos} da lista...')
                break
            pos += 1

print('-=' * 20)
print(f'Os valores digitados em ordem foram: {numeros}')