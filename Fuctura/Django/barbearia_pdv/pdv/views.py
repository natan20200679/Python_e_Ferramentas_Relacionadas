# Importa a função render para retornar páginas HTML
# e redirect para redirecionar o usuário para outra rota
from django.db.models import Model
from django.shortcuts import render, redirect, get_object_or_404

# Importa funções responsáveis pela autenticação de usuários
# authenticate -> verifica usuário e senha
# login -> cria a sessão do usuário logado
# logout -> encerra a sessão
from django.contrib.auth import login as auth_login, authenticate, logout

# Importa o modelo padrão de usuários do Django
from django.contrib.auth.models import User

# Importa os Models criados no projeto
# Esses models representam as tabelas do banco de dados
from .models import Cliente, Servico, Agendamento

# Importa os formulários criados no projeto
# Eles serão usados para criar e validar dados enviados pelo usuário
from .forms import ClienteForm, ServicoForm, AgendamentoForm, UserRegistrationForm

# Importa o decorator que exige que o usuário esteja logado
from django.contrib.auth.decorators import login_required


# ================================
# VIEW DE LOGIN
# ================================
def login_view(request):
    # Verifica se a requisição foi enviada por POST
    # POST acontece quando o usuário envia um formulário
    if request.method == 'POST':        
        # Captura o valor do campo "username" enviado pelo formulário
        username = request.POST.get('username')
        # Captura o valor do campo "password"
        password = request.POST.get('password')
        # Verifica se existe um usuário com esse username e senha
        user = authenticate(request, username=username, password=password)
        # Se o usuário existir (autenticação válida)
        if user is not None:           
            # Cria a sessão do usuário (login no sistema)
            auth_login(request, user)           
            # Redireciona para a página dashboard após login
            return redirect('dashboard')
    # Se for uma requisição GET ou login inválido
    # Renderiza a página de login
    return render(request, 'pdv/login.html')


# ================================
# VIEW DE LOGOUT
# ================================
def logout_view(request):
    # Encerra a sessão do usuário
    logout(request)
    # Redireciona o usuário para a página de login
    return redirect('login')


# ================================
# VIEW DE REGISTRO DE USUÁRIO
# ================================
def register_view(request):
    # Verifica se o formulário foi enviado
    if request.method == 'POST':
        # Cria o formulário com os dados enviados
        form = UserRegistrationForm(request.POST)
        # Verifica se os dados são válidos
        if form.is_valid():
            # Cria o usuário mas ainda não salva no banco
            user = form.save(commit=False)
            # Criptografa a senha antes de salvar
            user.set_password(form.cleaned_data['password'])
            # Salva o usuário no banco de dados
            user.save()
            # Redireciona para a página de login
            return redirect('login')
    else:
        # Se for GET, cria um formulário vazio
        form = UserRegistrationForm()
    # Renderiza a página de registro enviando o formulário
    return render(request, 'pdv/register.html', {'form': form})


# ================================
# DASHBOARD
# ================================
@login_required
def dashboard(request):

    # Apenas renderiza a página do dashboard
    return render(request, 'pdv/dashboard.html')


# ================================
# CRIAR CLIENTE
# ================================
@login_required
def criar_cliente(request):

    # Verifica se o formulário foi enviado
    if request.method == 'POST':
        # Cria o formulário com os dados enviados
        form = ClienteForm(request.POST)
        # Valida os dados do formulário
        if form.is_valid():
            # Salva o cliente no banco
            form.save()
            # Redireciona para a lista de clientes
            return redirect('clientes')
    else:
        # Se for GET, cria formulário vazio
        form = ClienteForm()
    # Renderiza a página de criação de cliente
    return render(request, 'pdv/criar_cliente.html', {'form': form})


# ================================
# EXCLUIR CLIENTE
# ================================
@login_required
def excluir_cliente(request, cliente):
    cliente = get_object_or_404(Cliente, nome=cliente)
    cliente.delete()
    return redirect("clientes")

@login_required
def atualizar_clientes(request):
    if request.method == "POST":
        selected_names = request.POST.getlist("selected_users")
        User.objects.filter(names=selected_names).update(is_active=True)
    users = User.objects.all()
    return render(request, "clientes.html", {"users": users})

# ================================
# LISTAR CLIENTES
# ================================
@login_required
def clientes_view(request):
    # Busca todos os clientes cadastrados no banco
    clientes = Cliente.objects.all()
    # Envia os clientes para o template HTML
    return render(request, 'pdv/clientes.html', {'clientes': clientes})


# ================================
# CRIAR AGENDAMENTO
# ================================
@login_required
def criar_agendamento(request):
    # Verifica se o formulário foi enviado
    if request.method == 'POST':
        # Cria o formulário com os dados enviados
        form = AgendamentoForm(request.POST)
        # Valida os dados
        if form.is_valid():
            # Salva o agendamento no banco
            form.save()
            # Redireciona para a lista de agendamentos
            return redirect('agendamentos')
    else:
        # Cria formulário vazio
        form = AgendamentoForm()
    # Renderiza a página de criação de agendamento
    return render(request, 'pdv/criar_agendamento.html', {'form': form})


# ================================
# LISTAR AGENDAMENTOS
# ================================
@login_required
def agendamentos_view(request):
    # Busca todos os agendamentos no banco
    agendamentos = Agendamento.objects.all()
    # Envia os agendamentos para o template
    return render(request, 'pdv/agendamentos.html', {'agendamentos': agendamentos})


# ================================
# LISTAR SERVIÇOS
# ================================
@login_required
def servicos_view(request):
    # Busca todos os serviços cadastrados
    servicos = Servico.objects.all()
    # Renderiza a página com a lista de serviços
    return render(request, 'pdv/servicos.html', {'servicos': servicos})


# ================================
# CRIAR SERVIÇO
# ================================
@login_required
def criar_servico(request):
    # Verifica se o formulário foi enviado
    if request.method == 'POST':
        # Cria o formulário com os dados
        form = ServicoForm(request.POST)
        # Valida os dados
        if form.is_valid():
            # Salva no banco
            form.save()
            # Redireciona para lista de serviços
            return redirect('servicos')
    else:
        # Cria formulário vazio
        form = ServicoForm()
    # Renderiza página de criação
    return render(request, 'pdv/criar_servico.html', {'form': form})


# ================================
# RELATÓRIOS
# ================================
@login_required
def relatorios_view(request):
    # Busca todos os agendamentos
    agendamentos = Agendamento.objects.all()
    # Calcula o total de vendas somando o preço dos serviços
    total_vendas = sum(agendamento.servico.preco for agendamento in agendamentos)
    # Envia os dados para o template
    return render(
        request,
        'pdv/relatorios.html',
        {
            'agendamentos': agendamentos,
            'total_vendas': total_vendas
        }
    )
