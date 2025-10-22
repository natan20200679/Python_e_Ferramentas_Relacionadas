class Cachorro:

  def __init__(self, nome, cor, acordado = True):

    self.nome = nome
    self.cor = cor
    self.acordado = acordado

  def latir(self):

    print("latir(self): Auau")

  def dormir(self):

    #self.acordado = False

    print("dormir(self): zzzzzzzzzz")

cao_1 = Cachorro("Chappie","amarelo",False)
cao_2 = Cachorro("Aladim","branco e preto")

print("Chappie,amarelo,False(cao_1.latir()): ", cao_1.latir())

print("Aladim,branco e preto(cao_2.acordado): ", cao_2.acordado)

print("Aladim,branco e preto(cao_2.dormir()): ", cao_2.dormir())

print("Aladim,branco e preto(cao_2.acordado): ", cao_2.acordado)

class Bicicleta:

  def __init__(self,cor,modelo,ano,valor):

    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor

  def buzinar(self):

    print("\nBicicleta buzinando: fom fooommm!")

  def parar(self):

    print("\nParando Bicicleta... \nBicicleta Parou!")

  def correr(self):

    print("\nBicicleta correndo: Vrummm! Vrummm!")

  def __str__(self):

    return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha","caloi",2022,600)

print("Bicicleta 1: " + b1.cor + ", " + b1.modelo + ", " + str(b1.ano) + ", " + str(b1.valor))

b1.correr()
b1.parar()
Bicicleta.buzinar(b1)
