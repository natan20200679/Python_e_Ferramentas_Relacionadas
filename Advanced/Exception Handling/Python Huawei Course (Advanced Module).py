## 14.1
"""
def Paridade(pValor):
  #if type(pValor) != int:
  #  raise Exception("O dado digitado deve ser convertido para inteiro!")
  if not isinstance(pValor, int): #Forma alternativa
    raise Exception("O dado digitado deve ser convertido para inteiro!")
  if pValor % 2 == 0:
    return "PAR"
  else:
    return "ÍMPAR"
n = input("Digite algo: ")
r = Paridade(n)
print(f"{n} é {r}")

"""## 14.1 (12.7)"""

def primo(V):
  if not isinstance(V, int):
    raise TypeError("Tipo inválido. O argumento deve ser um inteiro.")
  if V < 2:
    raise ValueError("Valor inválido. O argumento deve ser no mínimo 2.")
  if V == 2:
    return True
  elif V % 2 == 0:
    return False
  else:
    raiz = pow(V, 0.5)
    i = 3
    while i <= raiz:
      if V % i == 0:
        return False
      i += 2
    return True

try:
  N = (input("Digite um número inteiro: "))
  if primo(N):
    print(f"{N} é primo!")
  else:
    print(f"{N} não é primo!")
except TypeError as te:
  print(f"Erro: {te}")
except ValueError as ve:
  print(f"Erro: {ve}")

"""## 14.2"""

def aoQuadrado(dados):
  #if not isinstance(dados, list) and not isinstance(dados, tuple): # Forma alternativa
  if not isinstance(dados, list | tuple):
    raise TypeError(f"Lista ou Tupla esperada. Foi usada {type(dados)}")
  if not all (isinstance(x, int | float) for x in dados):
    raise ValueError("Os elementos da lista ou tupla devem ser todos numéricos.")
  return [v ** 2 for v in dados]

try:
  print(aoQuadrado({1, 2, 3, 4, 5}))
except TypeError as te:
  print(f"Erro: {te}")
except ValueError as ve:
  print(f"Erro: {ve}")
