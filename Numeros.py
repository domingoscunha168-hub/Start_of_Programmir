numeros = ['numero', 'numero_2', 'numero_3']

numero = int(input('Informe um valor: '))
numero_2 = int(input('Informe outro valor: '))
numero_3 = int(input('Informe mais um valor: '))

valor_minimo = min(numero, numero_2, numero_3)
valor_maximo = max(numero, numero_2, numero_3)

soma = numero + numero_2 + numero_3
media = soma / 3
print('Resultado:')
print(f' O valor minimo informado= {valor_minimo} e o valor maximo= {valor_maximo} e a soma dos tres valores= {soma} e a media= {media:.2f} ')
