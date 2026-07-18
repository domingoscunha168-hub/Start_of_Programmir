from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, titular, saldo_inicial=0.0):
        self.__titular = titular
        self.__saldo = self.__validar_valor(saldo_inicial, "saldo inicial")

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def taxa_mensal(self):
        pass

    def __validar_valor(self, valor, nome_campo):
        valor = float(valor)
        if valor < 0:
            raise ValueError(f"O {nome_campo} nao pode ser negativo.")
        return valor

    def __alterar_saldo(self, valor):
        self.__saldo += valor

    def depositar(self, valor):
        valor = self.__validar_valor(valor, "deposito")
        if valor == 0:
            raise ValueError("O deposito deve ser maior que zero.")

        self.__alterar_saldo(valor)

    def sacar(self, valor):
        valor = self.__validar_valor(valor, "saque")
        if valor == 0:
            raise ValueError("O saque deve ser maior que zero.")
        if valor > self.__saldo:
            print(f"Saque negado para {self.__titular}. Saldo insuficiente.")
            return

        self.__alterar_saldo(-valor)

    def aplicar_taxa(self):
        taxa = self.__validar_valor(self.taxa_mensal(), "taxa mensal")
        if taxa > self.__saldo:
            print(f"Taxa negada para {self.__titular}. Saldo insuficiente.")
            return

        self.__alterar_saldo(-taxa)

    def extrato(self):
        print(f"{self.tipo()} - {self.__titular} - saldo: R$ {self.__saldo:.2f}")


class ContaCorrente(Conta):
    def tipo(self):
        return "Conta Corrente"

    def taxa_mensal(self):
        return 12.00


class ContaPoupanca(Conta):
    def tipo(self):
        return "Conta Poupanca"

    def taxa_mensal(self):
        return 0.00


def main():
    contas = [
        ContaCorrente("Joao", 1000),
        ContaPoupanca("Maria", 1500),
    ]

    contas[0].depositar(250)
    contas[0].sacar(100)
    contas[0].aplicar_taxa()

    contas[1].depositar(300)
    contas[1].sacar(50)
    contas[1].aplicar_taxa()

    for conta in contas:
        conta.extrato()


if __name__ == "__main__":
    main()
