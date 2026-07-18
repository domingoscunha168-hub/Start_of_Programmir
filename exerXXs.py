from abc import ABC


class salario_do_funcionario(ABC):
    def __init__(self, salario, nome, percentual):
        self.salario = salario
        self.nome = nome
        self.percentual = percentual

    def receber_salario(self):
        return f"Salario de {self.nome}: R$ {self.salario:.2f}"


class Analista(salario_do_funcionario):
    def __init__(self, salario, nome, percentual, setor):
        super().__init__(salario, nome, percentual)
        self.setor = setor

    def analizar_salario(self, salario=None):
        base = self.salario if salario is None else salario
        self.salario = base + (base * self.percentual / 100)
        return self.salario


class Gerente(salario_do_funcionario):
    def __init__(self, salario, nome, percentual, departamento):
        super().__init__(salario, nome, percentual)
        self.departamento = departamento

    def gerir_salario(self, salario=None):
        base = self.salario if salario is None else salario
        self.salario = base + (base * self.percentual / 100)
        return self.salario

    def decrementar_salario_por_falta(self, percentual=None):
        percentual_aplicado = self.percentual if percentual is None else percentual
        self.salario -= self.salario * (percentual_aplicado / 100)
        return self.salario


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
