print('-=-' * 20)
print('||TABELA||')
print('-=-' * 20)

clubes = [
    'Dordoi Bishkek',
    'Alay (Osh)',
    'Abdish-Ata Kant',
    'Alga Bishkek',
    'Aka-Bura Osh',
    'Ak-Zhol',
    'Asiagoa',
    'Alamudun',
    'Neftchi Kochkor-Ata',
    'Kygyzaltyn',
    'OshMU Aldier',
    'Abdish-Ata-91',
    'Olimpia',
    'Aldiyer Kurshab',
    'Alga-2 Bishkek',
    'Platense',
    'Talant',
    'Platense',
    'Uzgen',
    'Bars Karakol'
]
pos = ''
print('Tabela dos 20 classificados:')
for pos, clube in enumerate(clubes, start=1):
    print(f'{pos:2d}º- {clube}')

print(' \n5 primeiros na ordem:')
for pos, clube in enumerate(clubes[:5], start=1):
    print(f"{pos:2d}º - {clube}")

print(' \nUltimos na ordem da tabela:')
for pos, clube in enumerate(clubes[-5:], start=len(clubes) - 4):
    print(f'{pos:2d}º - {clube}')

Ordenacoes = sorted(clubes)
print(' \nClubes em ordem alfabética:')
for clube in Ordenacoes:
    print(f'{clube}')

pos_bars_karakol = clubes.index('Bars Karakol') + 1
print(f' \nO clube Baros Karokol está na posicao {pos_bars_karakol} da tabela')