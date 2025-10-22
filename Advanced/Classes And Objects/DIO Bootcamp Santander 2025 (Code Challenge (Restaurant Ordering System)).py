"""# Desafio de Código(Sistema de Pedidos de Restaurante)"""

class Pedido:

    def __init__(self):

      self.itens = []

    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    def adicionar_item(self, nome, preco):

      # TODO: Adicione o preço do item à lista:
      self.itens.append({"nome": nome, "preco": float(preco)}) # Store item as a dictionary

    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:
    def calcular_total(self):

      # TODO: Retorne a soma de todos os preços
      return sum(item["preco"] for item in self.itens) # Calculate sum from the list of dictionaries

quantidade_pedidos = int(input().strip())
pedido = Pedido()

for _ in range(quantidade_pedidos):

  entrada = input().strip()
  nome, preco = entrada.rsplit(" ", 1)
  #TODO: Chame o método adicionar_item corretamente:
  pedido.adicionar_item(nome, preco) # Call the method on the instance
# TODO: Exiba o total formatado com duas casas decimais:
print(f"{pedido.calcular_total():.2f}") # Call the method and format the output
