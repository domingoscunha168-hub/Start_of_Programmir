from abc import ABC, abstractmethod
from queue import Queue
from threading import Thread
from time import sleep


class Notificacao(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    @abstractmethod
    def enviar(self, mensagem):
        pass

    def log(self, canal):
        print(f"Canal utilizado: {canal}")


class Email(Notificacao):
    def enviar(self, mensagem):
        print(f"Email para {self.destinatario}: ", end="", flush=True)
        for caractere in mensagem:
            print(caractere, end="", flush=True)
            sleep(0.03)
        print()
        self.log("Email")


class SMS(Notificacao):
    def enviar(self, mensagem):
        print(f"SMS para {self.destinatario}: ", end="", flush=True)
        for caractere in mensagem:
            print(caractere, end="", flush=True)
            sleep(0.03)
        print()
        self.log("SMS")


class CentralNotificacoes:
    def __init__(self):
        self.canais = []

    def registrar(self, canal):
        self.canais.append(canal)

    def publicar(self, mensagem):
        print(f"\nEvento recebido: {mensagem}")
        for canal in self.canais:
            canal.enviar(mensagem)


def produzir_eventos(fila):
    eventos = [
        "Nova aula liberada.",
        "Pagamento confirmado.",
        "Lembrete: prazo termina hoje.",
    ]

    for evento in eventos:
        sleep(2)
        fila.put(evento)

    fila.put(None)


def consumir_eventos(central, fila):
    while True:
        mensagem = fila.get()

        if mensagem is None:
            break

        central.publicar(mensagem)


def main():
    central = CentralNotificacoes()

    notificacoes = [
        Email("aluno@escola.com"),
        SMS("+55 11 99999-0000"),
    ]

    for canal in notificacoes:
        central.registrar(canal)

    fila = Queue()

    produtor = Thread(target=produzir_eventos, args=(fila,), daemon=True)
    produtor.start()

    consumir_eventos(central, fila)
    produtor.join()


if __name__ == "__main__":
    main()
