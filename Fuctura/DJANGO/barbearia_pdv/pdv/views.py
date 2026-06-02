from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from .models import Cliente, Servico, Agendamento
from .forms import ClienteForm, ServicoForm, AgendamentoForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Usuário ou senha inválido!"
    return render(request, 'pdv/login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'pdv/register.html', {'form': form})

@login_required()
def dashboard(request):
    return render(request, 'pdv/dashboard.html')

@login_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
        else:
            form = ClienteForm()
        return render(request, 'pdv/criar_cliente.html', {'form': form})

@login_required
@require_POST
def excluir_cliente(request, cliente):
    cliente.delete()
    return redirect('clientes')

@login_required
def clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'pdv/clientes.html', {'clientes': clientes})

@login_required
def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'pdv/criar_agendamento.html', {'form': form})

@login_required
def agendamentos_view(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'pdv/agendamentos.html', {'agendamentos': agendamentos})

@login_required
def servicos_view(request):
    servicos = Servico.objects.all()
    return render(request, 'pdv/servicos.html', {'servicos': servicos})

@login_required
def criar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicos')
    else:
        form = ServicoForm()
    return render(request, 'pdv/criar_servico.html', {'form': form})

@login_required
def relatorios_view(request):
    agendamentos = Agendamento.objects.all()
    total_vendas = sum(agendamento.servico.preco for agendamento in agendamentos if agendamento.servico)
    return render(request, 'pdv/relatorios.html',
                  {'agendamentos': agendamentos,
                   'total_vendas': total_vendas})