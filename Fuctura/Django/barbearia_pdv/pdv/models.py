# Importa o módulo models do Django, que usamos para criar as tabelas do banco de dados
from django.db import models

# Importa o modelo de usuário padrão do Django (caso quisermos relacionar algo com usuários do sistema)
from django.contrib.auth.models import User


# Criamos a classe Cliente que herda de models.Model
# Isso significa que essa classe será uma tabela no banco de dados
class Cliente(models.Model):

    # Campo de texto para armazenar o nome do cliente
    # max_length define o tamanho máximo do texto
    nome = models.CharField(max_length=100)

    # Campo de texto para armazenar o telefone do cliente
    telefone = models.CharField(max_length=15)

    # Campo específico para armazenar emails
    # O Django já valida se o formato é um email válido
    email = models.EmailField()

    # Método especial que define como o objeto será exibido
    # no painel administrativo ou em consultas
    def __str__(self):
        return self.nome


# Criamos a classe Servico que também será uma tabela no banco de dados
class Servico(models.Model):

    # Nome do serviço (ex: Corte, Barba, Sobrancelha)
    nome = models.CharField(max_length=100)

    # Campo decimal usado para valores monetários
    # max_digits = total de dígitos
    # decimal_places = quantidade de casas decimais
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    # Define como o serviço será exibido no Django
    def __str__(self):
        return self.nome


# Classe Agendamento que representa o agendamento de um serviço
class Agendamento(models.Model):

    # ForeignKey cria um relacionamento com a tabela Cliente
    # Ou seja, cada agendamento pertence a um cliente
    # CASCADE significa que se o cliente for deletado,
    # os agendamentos dele também serão apagados
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    # Relacionamento com a tabela Servico
    # Cada agendamento possui um serviço associado
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    # Campo que armazena data e hora do agendamento
    data_hora = models.DateTimeField()

    # Define como o agendamento será exibido
    def __str__(self):

        # f-string usada para mostrar informações formatadas
        # exemplo: João - Corte em 2026-03-12 14:00
        return f"{self.cliente} - {self.servico} em {self.data_hora}"
