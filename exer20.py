class gamer: 
    def __init__(self, nome, apelido, favoritos):
        self.nome = nome
        self.apelido = apelido
        self.favoritos = favoritos
    def jogar(self):
        print(f'{self.nome} ({self.apelido}) esta jogando {self.favoritos}')

    def mostrar_ficha(self):
        print(f'Nome: {self.nome}')
        print(f'Apelido: {self.apelido}')
        print(f'Favoritos: {self.favoritos}')

def main():
    g1 = gamer('João', 'Joãozinho', 'Minecraft')
    g1.jogar()
    g1.mostrar_ficha()
    g2 = gamer('Maria', 'Mariinha', 'Fortnite')
    g2.jogar()
    g2.mostrar_ficha()
    g3 = gamer('Pedro', 'Pedrinho', 'Among Us')
    g3.jogar()
    g3.mostrar_ficha()
    g4 = gamer('Ana', 'Aninha', 'Roblox')
    g4.jogar()
    g4.mostrar_ficha()

if __name__ == "__main__":
    main()    