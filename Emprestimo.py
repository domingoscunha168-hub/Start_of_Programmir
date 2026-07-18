def main():
    valor_emprestimo = float(input('Qual é o valor do empréstimo: '))
    quantidade_anos = int(input('Quantos anos ele vai pagar: '))

    parcela_mensal = valor_emprestimo / (quantidade_anos * 12)
    percentual_salario = parcela_mensal * 100

    if percentual_salario >= 30:
        print(
            f'O empréstimo mensal é {percentual_salario:.2f}% do salário do comprador.'
        )
    else:
        print(
            'O valor do empréstimo que o comprador consegue garantir em '
            'quantidade de anos será recusado.'
        )


if __name__ == '__main__':
    main()
