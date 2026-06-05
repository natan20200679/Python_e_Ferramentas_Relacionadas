from django import forms
from .models import Livro, Usuario, Emprestimo
from django.contrib.auth.models import User

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

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if (password and password_confirm) and (password != password_confirm):
            raise forms.ValidationError("As senhas não coincidem!")