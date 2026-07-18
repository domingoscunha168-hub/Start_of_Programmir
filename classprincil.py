from abc import ABC


class pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_confirmacao(self):
        return f"{self.nome} confirmou a matricula."


class Professor(pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def ensinar(self):
        return f"{self.nome} esta a ensinar {self.especialidade}."


class Funcionario(pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.setor = setor
        self.cargo = cargo

    def controlar_o_instituto(self):
        return f"{self.nome} controla o setor {self.setor}."


def main():
    al1 = Aluno(nome="Juliana", idade=64, curso="Bioquimica", turma="BI-12N")
    al1.fazer_aniversario()
    print(al1.fazer_confirmacao())

    p1 = Professor("Vicente", 42, "Culinaria", "Chefe")
    p1.fazer_aniversario()
    print(p1.ensinar())

    f1 = Funcionario("Delcia", 24, "Secretaria", "Secretaria")
    f1.fazer_aniversario()
    print(f1.controlar_o_instituto())


if __name__ == "__main__":
    main()
