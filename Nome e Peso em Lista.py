Nome = list()
Peso = list()

while True:
    try:
        Nome.append(str(input(' Informe o nome:')))
        Peso.append(float(input(' Informe o peso:')))
        ans = str(input(' Deseja continuar? [S/N]')).strip().upper()

        if ans == 'N':
            break

        print('=-=' * 16)
        print(f' Os nomes cadastrados sao: {Nome}')
        print(f' Foram cadastrados {len(Nome)} pessoas')
        print(f' As pessoas mais pesadas sao: {", ".join([Nome[d] for d, p in enumerate(Peso) if p == max(Peso)])}')
    except ValueError:
        print('Erro: Digite um valor válido para o peso (número)!')
        Nome.pop()

if len(Nome) > 0:
    print('=-=' * 16)
    print(f' As pessoas mais leves sao: {", ".join([Nome[d] for d, p in enumerate(Peso) if p == min(Peso)])}')
