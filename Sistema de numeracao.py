numero = int(input('Informe um valor:'))
opcao = int(input('''Escolha uma das base de conversao:
                  [1] para hexadecimal, 
                  [2] para binario 
                e [3] para octal'''))
print(f'A escolha foi {opcao} na base de conversao. Portanto:{numero}\n Em hexadecimal= {hex(numero)},\n Em binario= {bin(numero)}\n Em octal= {oct(numero)}')