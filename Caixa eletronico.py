def calcular_cedulas(valor):
    cedulas = [50, 20, 10, 1]
    resultado = {}
    restante = valor

    for cedula in cedulas:
        quantidade = restante // cedula
        resultado[cedula] = quantidade
        restante -= quantidade * cedula

    return resultado

def main():
    try:
        valor_recebido = int(input('Informe o valor recebido: '))
        if valor_recebido < 0:
            print('O valor consiste em um numero inteiro não negativo', end=' ')
            return

        cedulas = calcular_cedulas(valor_recebido)

        print(f'Para {valor_recebido}Kz , vao ser entregues:')
        for cedula, quantidade in cedulas.items():
            print(f'{quantidade} cedula(s) de Kz {cedula}')
    except ValueError:
        print('O pior seria nao inserir um numero inteiro valido')


if __name__ == '__main__':
    main()
