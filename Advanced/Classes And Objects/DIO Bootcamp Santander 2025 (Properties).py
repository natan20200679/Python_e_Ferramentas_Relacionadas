"""## Properties"""

class Foo:

  def __init__(self, x=None):
    self._x = x

  @property
  def x(self):
    return self._x or 0

  @x.setter
  def x(self, value):
    self._x += value

foo = Foo(20)

print(foo.x)

class Pessoa:

    def __init__(self, nome, ano_nascimento, ano_atual):
      self.nome = nome
      self._ano_nascimento = ano_nascimento
      self.ano_atual = ano_atual

    @property
    def idade(self):
      valor = self.ano_atual - self._ano_nascimento
      return valor

pessoa = Pessoa("natan", 1981, 2025)

print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
