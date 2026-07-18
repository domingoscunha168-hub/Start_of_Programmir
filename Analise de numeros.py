numero = (int(input('Informe um valor:')),
          int(input('Informe um outro valor:')),
          int(input('Informe mais um valor:')),
          int(input('Alem desses valores, informe mais um valor: ')))
print(f' Tu informou os valores{numero}')
print(f' O valor 9 apareceu {numero.count(9)} vezes ')
if 4 in numero:
    print(f' O valor 4 apareceu na {numero.index(4)+1}^ posicao')
elif 4 not in numero:
    print(' O valor 4 nao foi encontrado em nenhuma posicao')
    for numero in range(0, len(numero)):
        if numero % 2 == 0:
            print(f' O valor {numero} e par')
        else:
            print(f' O valor {numero} e impar')
        