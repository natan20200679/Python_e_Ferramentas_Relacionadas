"""# Classes Abstratas"""

from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):

  @abstractproperty
  def ligar(self):
      pass

  @abstractproperty
  def desligar(self):
      pass

  @abstractproperty
  @property
  def marca(self):
      pass

class ControleTV(ControleRemoto):

  def ligar(self):
      print("TV Ligada!")

  def desligar(self):
      print("TV Desligada!")

  def mudar_canal(self):
      print("Canal mudado!")

  @property
  def marca(self):
      print("LG")

controle = ControleTV()

controle.marca
controle.ligar()
controle.mudar_canal()
controle.desligar()

class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor <= 0:
            raise ValueError("Raio deve ser positivo")
        self._raio = valor

c = Circulo(5)
print(c.raio)

from abc import ABC, abstractproperty

class Forma(ABC):

    @abstractproperty
    def area(self):
        pass

class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    @property
    def area(self):
        return self.lado ** 2

q = Quadrado(5)
print(q.area)

