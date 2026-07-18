from exerXXs import Analista, Gerente


def main():
    ger1 = Gerente(nome="Maria", salario=4000, percentual=15, departamento="Vendas")

    an1 = Analista(nome="Joao", salario=3000, percentual=10, setor="TIC")
    print(an1.receber_salario())
    an1.analizar_salario()
    print(f"Salario atual de {an1.nome}: R$ {an1.salario:.2f}")

    an2 = Analista(nome="Ana", salario=3500, percentual=12, setor="Financeiro")
    print(an2.receber_salario())
    an2.analizar_salario()
    print(f"Salario atual de {an2.nome}: R$ {an2.salario:.2f}")

    print(f"Salario apos aumento de {an1.percentual}%: R$ {an1.salario:.2f}")
    print(f"Salario apos aumento de {an2.percentual}%: R$ {an2.salario:.2f}")
    print(ger1.receber_salario())
    print(f"Salario atual de {ger1.nome}: R$ {ger1.salario:.2f}")
    ger1.gerir_salario(an1.salario)
    ger1.decrementar_salario_por_falta(ger1.percentual)
    ger1.gerir_salario(an2.salario)
    ger1.decrementar_salario_por_falta(ger1.percentual)
    print(f"Salario final de {ger1.nome}: R$ {ger1.salario:.2f}")


if __name__ == "__main__":
    main()
