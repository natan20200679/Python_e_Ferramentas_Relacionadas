"""# Herança Múltipla"""

class Animal:

  def __init__(self, nro_patas):
      self.nro_patas = nro_patas

  def __str__(self):
      return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):

  def __init__(self, cor_pelo, **kw):
    self.cor_pelo = cor_pelo
    super().__init__(**kw)


class Ave(Animal):

  def __init__(self, cor_bico, **kw):
    self.cor_bico = cor_bico
    super().__init__(**kw)


class Gato(Mamifero):

  def __init__(self, **kw):
    super().__init__(**kw)


class Ornitorrinco(Mamifero, Ave):

  def __init__(self, **kw):
    super().__init__(**kw)

animal = Animal(nro_patas = 2)
mamifero = Mamifero(cor_pelo = "marrom", nro_patas = 4)
ave =Ave(nro_patas = 2, cor_bico = "preto")
gato = Gato(nro_patas = 4,cor_pelo = "branco")
ornitorrinco = Ornitorrinco(nro_patas = 2, cor_pelo = "laranja", cor_bico = "azul")

print(gato)
print(ave)
print(mamifero)
print(animal)
print(ornitorrinco)

