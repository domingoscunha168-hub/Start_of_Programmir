class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f'O produto {self.nome} custa R${self.preco:.2f}.'
produto1 = produto("Boné", 49.90)
print(produto1.etiqueta())
produto2 = produto("Camiseta", 79.90)
print(produto2.etiqueta())
