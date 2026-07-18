numeros = list()
for m in range(0, 2):
         numeros.append(int(input('Informe o valor')))

menu = 0
while menu != 6:
    print('''   [1]somar
	[2]multiplicar
	[3] maior
	[4] menor 
	[5]new numbers
	[6] exit programmer)''')
menu = int(input('Qual e o menu?'))
if menu == 'somar':
	resultado = numeros[0] + numeros[1]
	print(f' A soma de= {resultado}', end= '' )
elif menu == 'multiplicar':
	resultado = numeros[0] * numeros[1]
	print(f' O produto de= {resultado}', end= '')
elif menu == 'maior':
	if numeros[0] > numeros[1]:
		resultado = numeros[0]
		print(f' Entre= {numeros[0]} e {numeros[1]} o valor maior tem a igualdade', end= '')
	elif numeros[1] > numeros[0]:
		resultado = numeros[1]
		print(f' Entre= {numeros[0]} e {numeros[1]} o valor maior tem a igualdade', end= '')
elif menu == 'menor':
	if numeros < numeros:
		resultado = numeros
		print(f' Entre= {numeros} e {numeros} o valor menor tem a igualdade', end= '')
	else:
		resultado = numeros
elif menu == 5:
		print(f' Informe os new numbers {numeros} e {numeros}', end='')
elif menu == 6:		
		print('Termino')
else:
	print(' menu inesperado, tente depois')
	print('-=-' * 10)
	
		