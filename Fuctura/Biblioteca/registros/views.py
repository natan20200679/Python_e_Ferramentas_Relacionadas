from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Livro, Usuario, Emprestimo
from .forms import LivroForm, UsuarioForm, EmprestimoForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
    return render(request, 'registros/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'registros/register.html', {'form': form})

def dashboard(request):
    return render(request, 'registros/dashboard.html')

@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros')
        else:
            form = LivroForm()
    return render(request, 'registros/cadastrar_livro.html', context={'form': form})

@login_required
def visualizar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'registros/livros.html')

@login_required
def registrar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'registros/registrar_emprestimo.html', {'form': form})

@login_required
def encerrar_emprestimo(request):
    if request.method == 'DELETE':
        form = EmprestimoForm(request.DELETE)
        if form.is_valid():
            form.save()
            return redirect('emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'registros/encerrar_emprestimo.html', {'form': form})

@login_required
def visualizar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'registros/emprestimos.html', {'emprestimos': emprestimos})

@login_required
def visualizar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'registros/usuarios.html', context={'usuarios': usuarios})

@login_required
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'registros/criar_usuario.html', {'form': form})

@login_required
def visualizar_relatorios(request):
    livros = Livro.objects.all()
    total_emprestimos = Emprestimo.objects.count()
    return render(request, 'registros/relatorios.html', context={'livros': livros, 'total_emprestimos': total_emprestimos})