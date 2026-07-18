produtos = []
precos = []
quantidades = []

print("="*50)
print('SISTEMA DE COMPRAS')
print("="*50)

while True:
    
    nome = input('\n Informe o nome do produto: ').strip()
    while True:
        try:
            preco = float(input('Informe o valor do produto: '))
            if preco < 0:
                print('O preco can not negative')
                continue
            break
        except ValueError:
            print('Valor Incorreto. Informe um numero')
    
    while True:
        try:
            quantidade = float(input('Informe a quantidade: '))
            if quantidade < 0:
                print('\n*** PROGRAMA ENCERRADO ***')
                print('OPERAÇÃO CANCELADA: Quantidade negativa detectada!')
                break
            break
        except ValueError:
            print('Valor Incorreto. Informe um numero')
    
    if quantidade < 0:
        break
    
    produtos.append(nome)
    precos.append(preco)
    quantidades.append(quantidade)

totalidade_dos_gastos = sum(precos[i] * quantidades[i] for i in range(len(precos)))
produtos_elevados = sum(1 for d in precos if d > 5000)

if precos:
    produto_extra_acessivel = precos.index(min(precos))
    produto_mais_acessivel = produtos[produto_extra_acessivel]
    
    print("\n" + "=" * 50)
    print("RESULTADO DAS COMPRAS")
    print("=" * 50)
    print(f"Total de gasto nas compras: {totalidade_dos_gastos:.2f} Kz")
    print(f'Produtos que custam mais de 5000: {produtos_elevados}')
    print(f"Produto mais acessível: {produto_mais_acessivel}")
    print("=" * 50)
else:
    print("\nNenhum produto foi adicionado!")
    print("=" * 50)