produto = float(input("Informe o valor do produto: "))
preco_normal = (produto * 2) 
desconto_1 = (5 / 100 * preco_normal) 
desconto_2 = (10 / 100 * preco_normal)
juros = (20 / 100 * preco_normal)
bonus = (50 / 100 * preco_normal)
condicao_pagamento = int(input('Informe a condicao de pagamento: \n [1] A vista o dinheiro \n [2] A vista cartao \n [3] 2x no cartao \n [4] 3x ou mais no cartao \n [5] A vista com bonus de 50% '))
print(f'Produto= {produto} \n Preco normal= {preco_normal:.2f} \n Desconto 5%= {desconto_1:.2f} \n Desconto 10%= {desconto_2:.2f} \n Juros 20%= {juros:.2f} \n Bonus 50%= {bonus:.2f}')
if condicao_pagamento == 1:
    print(f'Valor a garantir= {preco_normal - desconto_1}')
elif condicao_pagamento == 2:
    print(f'Valor a garantir= {preco_normal - desconto_2}')
elif condicao_pagamento == 3:
    print(f'Valor a garantir= {preco_normal}')
elif condicao_pagamento == 4:
    print(f'Valor a garantir= {preco_normal + juros}')
elif condicao_pagamento == 5:
    print(f'Valor a garantir= {preco_normal - bonus}')
else:
    print('Não se faz kilape')
