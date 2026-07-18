def mostra_lista():
    nomes = []
    for d in range(0, 12):
        print(f'{nomes[d]}')
        idades = []
    for d in range(20, 32):
        print(f'{idades[d]}')    

    pesos = []
    for d in range(0, 12):
        pesos.append(80.0)
        print(f'{pesos[d]}')

    generos = [str(input('Qual o generos?')) for d in range(12)]
    for d in range(0, 12):
        if generos[d] == 'feminina/F':
            print('Sao do genero feminino')
        elif generos[d] == 'masculino/M':
            print('Sao do genero masculino')
    alturas = []
    for d in range(0, 12):
        alturas.append(1.80)
        print(f'{alturas[d]}')
    print(list(zip(nomes, idades, pesos, generos, alturas)))

mostra_lista()
