from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.nome
    
class Servico(models.Model):

    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico,on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    def __str__(self):
        return f"{self.cliente} - {self.servico} em {self.data_hora}"
    