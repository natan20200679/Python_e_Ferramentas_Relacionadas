from django import forms
from .models import Livro, Usuario, Emprestimo

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'descricao', 'ano']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'usuario', 'data_emprestimo', 'data_devolucao']
        widgets = {
            'data_emprestimo': forms.DateInput(attrs={
                'placeholder': 'DD/MM/AAAA',
                'type': 'date'
            }),
            'data_devolucao': forms.DateInput(attrs={
                'placeholder': 'DD/MM/AAAA',
                'type': 'date'
        })}