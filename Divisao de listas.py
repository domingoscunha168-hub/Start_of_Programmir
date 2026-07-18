diversos_numeros = []
pares = []
Impares = list()
while True:

    diversos_numeros.append(int(input('Informe um valor: ')))
    ans = str(input(' Deseja continuar? (S/N): ')).capitalize()
    if ans in 'N':
        break
    for d, n in enumerate(diversos_numeros):
        if n % 2 == 0:
            pares.append(n)
        elif n % 2 == 1:
            Impares.append(n)
    print('=-=' * 50)
    print(f' Os numeros digitados foram {diversos_numeros}')
    print(f' Os numeros pares e impares foram {pares} e {Impares} respectivamente ')
    

