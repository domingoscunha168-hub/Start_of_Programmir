def ler_numero():
    while True:
        try:
               return int(input('Informe um valor:'))
        except ValueError:
            print('Numero invalido') 
        continue
def mostrar_relatorio(numeros):
    if not numeros:
        print('A lista esta vazia')
        return
    
    print('=-=' * 10, end=' ')
    print(f'Lista original: {numeros}')
    print(f'Ordem descendente: {sorted(numeros, reverse=True)}')
    print(f'Quantidade: {len(numeros)}')
    print(f'Maior valor: {max(numeros)}')
    print(f'Menor valor: {min(numeros)}')
    print(f'Soma: {sum(numeros)}')
    print(f'Media: {sum(numeros) / len(numeros):.2f}')


numeros = []

while True:
    print('''\n '1' Adicionar valor
    '2' Mostrar relatorio
    '3' Procurar valor
    '4' Remover valor
    '5' Exit''')

    opcao = input(' Escolha uma opcao:').strip()

    if opcao == '1':
        numeros.append(ler_numero())
        print(' Numero adicionado com sucesso')

    elif opcao == '2':
        mostrar_relatorio(numeros)

    elif opcao == '3':
        valor = ler_numero()
        if valor in numeros:
            print(f' O numero {valor} aparece {numeros.count(valor)} vezes na lista')
        else:
            print(' Numero nao encontrado.')

    elif opcao == '4':
        valor = ler_numero()
        if valor in numeros:
            numeros.remove(valor)
            print(' Numero removido.')
        else:
            print(' Numero nao encontrado')

    elif opcao == '5':
        print('End of Program')
        break