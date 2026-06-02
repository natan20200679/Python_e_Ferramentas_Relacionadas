from django.urls import path
from .views import (relatorios_view, criar_cliente, criar_servico,
                    register_view, login_view, servicos_view,
                    dashboard, clientes_view, agendamentos_view, criar_agendamento, excluir_cliente)

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('clientes/', clientes_view, name='clientes'),
    path('clientes/criar/', criar_cliente, name='criar_cliente'),
    path('clientes/excluir/<int:cliente>/', excluir_cliente, name='excluir_cliente'),
    path('servicos/', servicos_view, name='servicos'),
    path('servicos/criar/', criar_servico, name='criar_servico'),
    path('agendamentos/', agendamentos_view, name='agendamentos'),
    path('agendamentos/criar/', criar_agendamento, name='criar_agendamento'),
    path('relatorios/', relatorios_view, name='relatorios'),
]
