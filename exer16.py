class funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def se_apresentar(self):
        return f' Saudacoes, meu nome é {self.nome}, trabalho no setor de {self.setor} e meu cargo é {self.cargo}.'
funcionario1 = funcionario("João", "Recursos Humanos", "Analista de RH")
print(funcionario1.se_apresentar())
funcionario2 = funcionario("Maria", "Financeiro", "Gerente Financeiro")
print(funcionario2.se_apresentar())        


    