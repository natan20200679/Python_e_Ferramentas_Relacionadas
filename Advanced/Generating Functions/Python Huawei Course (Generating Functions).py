## Funções Geradoras

"""## 15.3"""

def gerador_pares():
  a = 2
  while True: #Linha 3 trocada com 5 para este programa não ficar em loop
  #infinito, mostrando apenas "2" na saída
    yield a
    a += 2

gen = gerador_pares()
print(next(gen))
print(next(gen))

for _ in range(20):
  print(next(gen), end = " ")

g2 = gerador_pares()
for _ in range(6):
  print(next(g2), end = " ")

print(next(gen))
print(next(g2))

"""## 15.4"""

def filtro(dados, pmin, pmax):
  for valor in dados:
    if pmin <= valor <= pmax:
      yield valor, valor * 1,1

precos = [36.3, 174.19, 43.71, 108,32, 89.14]
lmin = int(input('Digite o mínimo da faixa: '))
lmax = int(input('Digite o máximo da faixa: '))
for valores in filtro(precos, lmin, lmax):
  print(valores)
print('\nFim do Programa')

"""## 15.6"""

def le_arquivo(nome_arq):
  for uma_linha in open(nome_arq, 'r'):
    uma_linha = uma_linha.split(';')
    yield uma_linha[0], int(uma_linha[3])
    #yield uma_linha.rstrip()

nome_arq = input('Digite o nome do arquivo: ')
for linha in le_arquivo(nome_arq):
  print(linha)
print('\nFim do Programa')

"""## 15.7"""

import sys
import cProfile

quadrados_lc = [num ** 2 for num in range(1, 11)]
print('quadrados_lc: ', quadrados_lc)
print(type(quadrados_lc))

print('\n')

quadrados_eg = (num ** 2 for num in range(1, 11))
print('quadrados_eg: ', quadrados_eg)
print(type(quadrados_eg))

print('\nValores quadrados_lc: ')

for valor in quadrados_lc:
  print(valor, end = ' ')

print('\n\nValores quadrados_eg: ')

for valor in quadrados_eg:
  print(valor, end = ' ')

print('\n\nOcupação em Memória:')
print('Objeto quadrados_lc ->', sys.getsizeof(quadrados_lc))
print('Objeto quadrados_eg ->', sys.getsizeof(quadrados_eg))

quadrados_lc = [num ** 2 for num in range(1, 10001)]
quadrados_eg = (num ** 2 for num in range(1, 10001))
print('\nOcupação em Memória (Range Elevado): ')
print('Objeto quadrados_lc ->', sys.getsizeof(quadrados_lc))
print('Objeto quadrados_eg ->', sys.getsizeof(quadrados_eg))

print('\nProcessamento:')
print('Objeto quadrados_lc ->')
cProfile.run('sum([num ** 2 for num in range(1, 10001)])')
print('Objeto quadrados_eg ->')
cProfile.run('sum(num ** 2 for num in range(1, 10001))')

"""## 15.8"""

def fg():
  resto = 0
  num = 2
  while True:
    if num % 2 == resto:  # resto calculado é comparado com o objeto resto
      dado = (yield num) # gera valores pares a partir de 2, e os guarda em "dado"
      if dado is not None:
          if dado in (0, 1):
              resto = dado  # troca o valor de resto
              num = 0  # reseta o valor de num
          else:
              raise ValueError(f'Esperado argumento 0 ou 1 - passado {dado}')
    num += 1

gen = fg()
print('Gera 5 pares')
for i in range(5):
    print(next(gen))

print('\nGera 5 ímpares')
ret = gen.send(1)  # este método retorna o 1º valor da sequência
print(ret)
for i in range(4): # então precisamos gerar o próximos 4
    print(next(gen))

# tentativa de usar send com valor diferente de 0 ou 1
print('\nParâmetro incorreto')
ret = gen.send(2)  # valor maior do que 1 causa um loop infinito

print('\nFim do Programa')

"""## 15.9"""

def simples():
  num = 10
  while True:
    yield num
    num += 10

#gen = simples()
#for _ in range(5):
 # print(next(gen))

#print(next(gen))
#gen.throw(Exception('Gerador terminado pelo usuário.'))
#print(next(gen))

#for valor in gen:
 # print(valor)

#gen = simples()
#for valor in gen:
 # print(valor)
  #gen.close()
  #if valor > 70:
   # gen.throw(Exception('Todos os valores de interesse foram gerados.'))

#print(next(gen))

gen = simples()
for valor in gen:
  print(valor)
  if valor > 70:
    gen.close()
print(next(gen))

"""## 15.1"""

def gerador_primos():
  yield 2
  v = 3
  while True:
    raiz = v ** 0.5
    i = 3
    while i <= raiz and v % i != 0:
      i += 2
    if i > raiz:
      yield v
    v += 2

gen = gerador_primos()
Qtde = int(input('Digite a quantidade: '))
for _ in range(Qtde):
  print(next(gen), end = ' ')

print('\n\nFim do programa')

"""## 15.2"""

def funcao_fatorial():
  num, fat = 0, 1
  while True:
    yield num, fat
    num += 1
    fat *= num

N = int(input('Digite a quantidade: '))
gen = funcao_fatorial()
for _ in range(N):
  print(next(gen))

print('\n\nFim do Programa')

"""## 15.3"""

def funcao_fatorial():
  num, fat = 0, 1
  while True:
    i = (yield num, fat)
    num += 1
    fat *= num
    if i is not None:
      num, fat = i, 1
      for a in range(1, num + 1):
        fat *= num


qtde = int(input('Digite a quantidade: '))
gen = funcao_fatorial()
next(gen)
prim = int(input('\nDigite o valor inicial para os fatoriais: '))
while prim >= 0:
  r = gen.send(prim)
  fatoriais = [r]
  for _ in range(qtde - 1):
    fatoriais.append(next(gen))
  print(f'\nSequência de fatoriais iniciando em {prim}')
  print(fatoriais)
  prim = int(input('\nDigite o valor inicial para os fatoriais: '))

print('\n\nFim do Programa')

"""## 15.6"""

def media_movel():
  total = qtde = 0
  while True:
    novo_dado = (yield total / qtde if qtde > 0 else 0)
    if novo_dado is not None:
      total += novo_dado
      qtde += 1

gen = media_movel()
next(gen)
valor = input('Digite um valor (ou FIM para encerrar): ')
while valor.upper() != 'FIM':
  resultado = gen.send(float(valor))
  print(f'Média Móvel Atual = {resultado:.3f}')
  valor = input('Digite um valor (ou FIM para encerrar): ')
print(f'Valor Final da Média = {resultado:.3f}')

print('\nFim do Programa')
