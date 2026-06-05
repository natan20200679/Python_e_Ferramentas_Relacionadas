# Importa o módulo de formulários do Django
from django import forms
# Importa os Models do projeto
# Esses models serão usados para criar formulários automaticamente (ModelForm)
from .models import Cliente, Servico, Agendamento
# Importa o modelo padrão de usuário do Django
from django.contrib.auth.models import User


# ================================
# FORMULÁRIO DE CLIENTE
# ================================
class ClienteForm(forms.ModelForm):
    # Classe interna Meta define configurações do formulário
    class Meta:
        # Define qual model será usado
        model = Cliente
        # Define quais campos aparecerão no formulário
        fields = ['nome', 'telefone', 'email']


# ================================
# FORMULÁRIO DE SERVIÇO
# ================================
class ServicoForm(forms.ModelForm):
    class Meta:
        # Model relacionado ao formulário
        model = Servico
        # Campos que serão exibidos
        fields = ['nome', 'preco']


# ================================
# FORMULÁRIO DE AGENDAMENTO
# ================================
class AgendamentoForm(forms.ModelForm):
    class Meta:
        # Model relacionado
        model = Agendamento
        # Campos do formulário
        fields = ['cliente', 'servico', 'data_hora']
        # Widgets permitem personalizar os campos no HTML
        widgets = {
            # Personaliza o campo de data e hora
            'data_hora': forms.DateInput(attrs={
                # Placeholder exibido no campo
                'placeholder': 'DD/MM/AAAA',
                # Define o tipo como date (abre seletor de data no navegador)
                'type': 'date'
            }),
        }


# ================================
# FORMULÁRIO DE REGISTRO DE USUÁRIO
# ================================
class UserRegistrationForm(forms.ModelForm):
    # Cria um campo de senha
    # PasswordInput faz com que os caracteres não apareçam
    password = forms.CharField(widget=forms.PasswordInput)
    # Campo para confirmação de senha
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        # Define que o formulário usa o model User do Django
        model = User
        # Campos que serão exibidos
        fields = ['username', 'email', 'password']
        
    # Método responsável por validações personalizadas
    def clean(self):
        # Chama o clean padrão do Django
        cleaned_data = super().clean()
        # Recupera os valores dos campos
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        # Verifica se as senhas existem e são diferentes
        if password and password_confirm and password != password_confirm:
            # Lança erro de validação
            raise forms.ValidationError("As senhas não coincidem.")

class UserSelectionForm(forms.Form):
    selected_users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
