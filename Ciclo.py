while True:
   
    try:
        numero = int(input('start: '))
        break
    except ValueError:
       print('Informe um numero inteiro')

while True:
    try:
        numero_2 = int(input('sequencia:'))
        break
    except ValueError:
       print('Informe um numero inteiro')

passo = 1 if numero <= numero_2 else -1

for d in range(numero, numero_2 + passo, passo):
    print(d)    