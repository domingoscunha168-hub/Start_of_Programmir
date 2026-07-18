print('=-='* 22)
print('LISTA DE DADOS')
print('=-='* 22)
produtos = ['regua', 2.1,'prancheta', 2.3, 'transferidor', 2.4, 'campasso', 4.5,'esquadro', 2.6]
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
       print(f'{produtos[pos]:.<22}', end='')
    elif pos % 2 != 0:
        print(f'Kz {produtos[pos]:.>6.2f}') 
