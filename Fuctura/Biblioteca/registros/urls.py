from django.urls import path
from registros.views import login_view, register_view, dashboard, visualizar_livros, cadastrar_livro, \
    visualizar_emprestimos, registrar_emprestimo, visualizar_usuarios, criar_usuario, visualizar_relatorios, \
    encerrar_emprestimo

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),
    path('register/', register_view, name='registrar'),
    path('dashboard/', dashboard, name='dashboard'),
    path('livros/', visualizar_livros, name='livros'),
    path('livros/cadastrar/', cadastrar_livro, mame='cadastrar_livro'),
    path('emprestimos/', visualizar_emprestimos, name='emprestimos'),
    path('emprestimos/registrar', registrar_emprestimo, name='registrar_emprestimo'),
    path('emprestimos/encerrar', encerrar_emprestimo, name='encerrar_emprestimo'),
    path('usuarios/', visualizar_usuarios, name='usuarios'),
    path('usuarios/criar', criar_usuario, name='criar_usuario'),
    path('relatorios/', visualizar_relatorios, name='relatorios'),
]