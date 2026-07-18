from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def autonomia(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

    def apresentar(self):
        print(f"{self.tipo()}: {self.marca} {self.modelo}")
        print(f"Autonomia estimada: {self.autonomia()}")


class Autocarro(Veiculo):
    def autonomia(self):
        return "650 km"

    def tipo(self):
        return "Autocarro"


class CarroMostro(Veiculo):
    def autonomia(self):
        return "320 km"

    def tipo(self):
        return "Carro Mostro"


def main():
    garagem = [
        Autocarro("Scania", "S100"),
        CarroMostro("Ford", "Mustang"),
    ]

    for veiculo in garagem:
        veiculo.apresentar()


if __name__ == "__main__":
    main()