ans_s = [

    {
     'ans': 'Qual dessas coleções em Phyton é imutável?',
     'opcoes': ['A) Tupla', 'B) Lista', 'C) Dicionário'],
     'answer': 'C'
    },
    {
     'ans': 'Qual comando é usado para criar uma função em Phyton?',
     'opcoes': ['A) funcion', 'B) def', 'C) fun'],
     'answer': 'B' 
    },
    {
     'ans': 'Como se exibe algo no comentário',
     'opcoes': ['A) echo', 'B) console.log', 'C) print()',],
     'answer': 'C'
    }     
]

pontos = 0
for index, ans in enumerate(ans_s): 
    print(f'--- Ans{index + 1} de {len(ans_s)}---')
    print(ans['ans'])
    for d, opcao in enumerate(ans['opcoes']):
        print(f'{d + 1}) {opcao}')
    resposta = input('Sua resposta: ')
    if resposta.upper() == ans['answer']:
        print('Correta')
        pontos += 1
    else:
        print(f'Incorreta, tem a resposta certa que é {ans["answer"]}')
print(f' Tu acertou {pontos} de {len(ans_s)} perguntas.')