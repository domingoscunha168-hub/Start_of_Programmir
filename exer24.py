class Cafeteria:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.aberta = False

    def abrir(self):
        self.aberta = True
        print(f'{self.nome} está aberta')
        if self.aberta and self.tipo:
            print(f'{self.nome} é uma cafeteria do tipo {self.tipo}')
        else:
            print(f'{self.nome} está aberta, mas não é uma cafeteria do tipo {self.tipo}')

    def fechar(self):
        self.aberta = False
        print(f'{self.nome} está fechada')
def main():
    c1 = Cafeteria('Café do Centro', 'Especializada')
    c1.abrir()
    c1.fechar()