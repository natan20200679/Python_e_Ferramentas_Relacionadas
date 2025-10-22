class Pessoa:
    olhos = 2

    def __init__(self,*filhos,nome=None,idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

if __name__ == '__main__':
    Natan = Homem(nome='Natan')
    Beluca = Pessoa(nome='Beluca')
    Mãe = Pessoa(Natan,Beluca,nome='Mãe')
    print(Mãe.cumprimentar())
    print(Mãe.nome)
    print(Mãe.idade)
    for filho in Mãe.filhos:
        print(filho.nome)
    Mãe.sobrenome = 'Medrado'
    del Mãe.filhos
    print(Pessoa.olhos)
    print(Mãe.olhos)
    print(Natan.olhos)
    print(Beluca.olhos)
    print(Mãe.__dict__)
    print(Pessoa.metodo_estatico(),Mãe.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),Mãe.metodo_estatico())
    print(Natan.cumprimentar())


