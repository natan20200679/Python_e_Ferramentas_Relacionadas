"""# Métodos de Classe e Estáticos"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_de_nascimento(cls, dia, mes, ano, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_data_de_nascimento(25, 9, 1981, "Natanael")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

