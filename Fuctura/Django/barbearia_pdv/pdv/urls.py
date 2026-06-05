# Importa a função path para criar rotas
from django.urls import path
from . import views
# Importa todas as views que serão usadas nas URLs
from .views import (
    relatorios_view, criar_agendamento,
    criar_cliente, criar_servico,
    register_view, logout_view,
    login_view, servicos_view,
    dashboard, clientes_view, agendamentos_view, excluir_cliente,
)

# Lista que armazena todas as rotas do app
urlpatterns = [
    # Página inicial → login
    path('', login_view, name='login'),
    # Rota de login
    path('login/', login_view, name='login'),
    # Rota de logout
    path('logout/', logout_view, name='logout'),
    # Rota de cadastro de usuário
    path('register/', register_view, name='registrar'),
    # Dashboard principal
    path('dashboard/', dashboard, name='dashboard'),
    # Lista de clientes
    path('clientes/', clientes_view, name='clientes'),
    # Criar cliente
    path('clientes/criar/', criar_cliente, name='criar_cliente'),
    # Excluir cliente
    path('clientes/excluir/', excluir_cliente, name='excluir_cliente'),
    # Lista de serviços
    path('servicos/', servicos_view, name='servicos'),
    # Criar serviço
    path('servicos/criar/', criar_servico, name='criar_servico'),
    # Lista de agendamentos
    path('agendamentos/', agendamentos_view, name='agendamentos'),
    # Criar agendamento
    path('agendamentos/criar/', criar_agendamento, name='criar_agendamento'),
    # Relatórios
    path('relatorios/', relatorios_view, name='relatorios'),
]
