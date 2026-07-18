class churasco:
    def __init__(self, carne, cerveja, refrigerante):
        self.carne = carne
        self.cerveja = cerveja
        self.refrigerante = refrigerante

    def quantidade_de_pessoas(self):
        print(f'O churrasco {self.carne:.2f} kg de carne, \n{self.cerveja:.2f} litros de cerveja e {self.refrigerante:.2f} litros de refrigerante')
            
    def quanto_de_carne(self):
        carne_por_pessoa = 0.4
        pessoas_carne = self.carne / carne_por_pessoa
        return pessoas_carne

    def quanto_de_cerveja(self):
        cerveja_por_pessoa = 0.5
        pessoas_cerveja = self.cerveja / cerveja_por_pessoa
        return pessoas_cerveja
    def quanto_de_refrigerante(self):
        refrigerante_por_pessoa = 0.3
        pessoas_refrigerante = self.refrigerante / refrigerante_por_pessoa
        return pessoas_refrigerante
    def custo_total(self):
        custo_carne = self.carne * 25.00
        custo_cerveja = self.cerveja * 10.00
        custo_refrigerante = self.refrigerante * 5.00
        custo_total = custo_carne + custo_cerveja + custo_refrigerante
        return custo_total
    def preco_por_pessoa(self):
        total_pessoas = min(self.quanto_de_carne(), self.quanto_de_cerveja(), self.quanto_de_refrigerante())
        if total_pessoas > 0:
            preco_por_pessoa = self.custo_total() / total_pessoas
            return preco_por_pessoa
        else:
            return 0
churrasco1 = churasco(10, 5, 3)
churrasco1.quantidade_de_pessoas()
print(f'Quantidade de pessoas que podem participar do churrasco: \n{churrasco1.quanto_de_carne():.2f} pessoas com carne, \n{churrasco1.quanto_de_cerveja():.2f} pessoas com cerveja e \n{churrasco1.quanto_de_refrigerante():.2f} pessoas com refrigerante.')
print(f'Custo total do churrasco: R${churrasco1.custo_total():.2f}')
print(f'Preço por pessoa: R${churrasco1.preco_por_pessoa():.2f}')
