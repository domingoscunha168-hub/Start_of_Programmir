from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar(self):
        pass

    def confirmar(self):
        print(f"Pagamento confirmado no valor de R$ {self.valor:.2f}")


class Pix(Pagamento):
    def processar(self):
        print(f"PIX enviado para R$ {self.valor:.2f}")
        self.confirmar()


class CartaoCredito(Pagamento):
    def processar(self):
        taxa = self.valor * 0.03
        total = self.valor + taxa
        print(f"Cartao aprovado com taxa de R$ {taxa:.2f}")
        print(f"Total cobrado: R$ {total:.2f}")


def main():
    pagamentos = [
        Pix(250.00),
        CartaoCredito(120.00),
    ]

    for pagamento in pagamentos:
        pagamento.processar()


if __name__ == "__main__":
    main()

