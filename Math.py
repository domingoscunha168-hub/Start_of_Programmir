from math import sqrt, trunc, floor, ceil, tan,factorial

numero = float(input('Informe um valor: '))
raiz = sqrt(numero) if numero >= 0 else float('False')

if numero >= 0 and numero.is_integer():
    fat = factorial(int(numero))
else:
    fat = 'Fatorial somente para inteiros >= 0'
print('=' * 50)
print(
    f'O valor informado: {numero:<10.2f}\n'
    f'Parte inteira: {int(numero)}\n' 
    f'Potencia: {numero**2}\n'
    f'A raiz quadrada: {raiz}\n'
    f'Parte inteira da raiz quadrada: {trunc(raiz) if numero >= 0 else 'N/A'}\n'
    f'Com numero arredondado para baixo: {floor(raiz) if numero >= 0 else 'N/A'} e numero arredondado para cima: {ceil(raiz) if numero >= 0 else 'N/A'}\n'
    f'Tangente: {tan(raiz):.2f}\n'
    f'Fatorial: {fat}\n'  
    f'E o valor absoluto = {abs(numero)}')
print('=' * 50)