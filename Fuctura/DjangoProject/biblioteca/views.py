from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout
from .models import Livro, Usuario, Emprestimo
from .forms import LivroForm, UsuarioForm, EmprestimoForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
    return render(request, 'biblioteca/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'biblioteca/register.html', {'form': form})

def dashboard(request):
    return render(request, 'biblioteca/dashboard.html')

@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/cadastrar_livro.html', context={'form': form})

@login_required
def visualizar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/livros.html', {'livros': livros})

@login_required
def visualizar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'biblioteca/usuarios.html', context={'usuarios': usuarios})

@login_required
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'biblioteca/criar_usuario.html', {'form': form})

@login_required
def excluir_usuario(request, usuario):
    usuario = get_object_or_404(Usuario, id=usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')
    return render(request, 'biblioteca/usuarios.html', {'usuario': usuario})

@login_required
def atualizar_usuarios(request):
    if request.method == "POST":
        usuario_id = request.POST.getlist(key='id')
        User.objects.filter(names=usuario_id).update(is_active=True)
    usuarios = User.objects.all()
    return render(request, "biblioteca/usuarios.html", {"usuarios": usuarios})

@login_required
def registrar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'biblioteca/registrar_emprestimo.html', {'form': form})

@login_required
def visualizar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'biblioteca/emprestimos.html', {'emprestimos': emprestimos})


@login_required
def visualizar_relatorios(request):
    livros = Livro.objects.all()
    total_emprestimos = Emprestimo.objects.count()
    return render(request, 'biblioteca/relatorios.html', context={'livros': livros, 'total_emprestimos': total_emprestimos})