class caneta:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    def escrever(self):
        print(f"A caneta {self.marca} {self.modelo} de cor {self.cor} está escrevendo")
    def apagar(self):
        print(f"A caneta {self.marca} {self.modelo} de cor {self.cor} está apagando")
def main():
    c1 = caneta('Bic', 'Cristal', 'Azul')
    c1.escrever()
    c1.apagar()
if __name__ == "__main__":
    main()
    c2 = caneta('Faber-Castell', 'Grip', 'Preta')
    c2.escrever()
    c2.apagar()


