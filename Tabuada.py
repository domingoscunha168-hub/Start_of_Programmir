print('|||TABUADA|||')

while True:
    try:

        numero = int(input('Informe o valor para verificar a tabuada: e um para encerrar-o: '))
        if numero < 0:
            print("=" * 50)
            print('PROGRAMA ENCERRADO')
            print("=" * 50)
            break

        print(f'\n |Tabuada do {numero}|')
        for d in range(1, 18 + 1):
           print(f'{numero} * {d} = {numero * d}')
           print()

    except ValueError:
        print(' Incorreto. Informe um numero inteiro valido\n, e um negative para encerrar\n')