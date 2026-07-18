from abc import ABC, abstractmethod
from math import pi


class Forma(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def resumo(self):
        print(f"{self.nome} = area: {self.area():.2f} | perimetro = {self.perimetro():.2f}")


class Circulo(Forma):
    def __init__(self, raio):
        super().__init__("Circulo")
        self.raio = raio

    def area(self):
        return pi * self.raio**2

    def perimetro(self):
        return 2 * pi * self.raio


class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__("Retangulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


def main():
    figuras = [
        Circulo(4),
        Retangulo(8, 3),
        
    ]

    for figura in figuras:
        figura.resumo()


if __name__ == "__main__":
    main()

