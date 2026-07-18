from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def movimentar(self):
        pass
    @abstractmethod
    def comer(self):
        pass

    def apresentar(self):
        print(f"Animal: {self.nome}")
        print(f"Som: {self.emitir_som()}")
        print(f"Movimento: {self.movimentar()}")
        print(f"Comida: {self.comer()}")

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"

    def movimentar(self):
        return "Correr"

    def comer(self):
        return "Ração"

class Pato(Animal):
    def emitir_som(self):
        return "Quack"

    def movimentar(self):
        return "Nadar"

    def comer(self):
        return "Grãos"


def main():
    animais = [
        Cachorro("Rocky"),
        Pato("Ploca"),
    ]

    for animal in animais:
        animal.apresentar()


if __name__ == "__main__":
    main()
