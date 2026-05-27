from django import forms
from .models import Cliente, Servico, Agendamento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco']

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'servico', 'data_hora']
        widgets = {
            'data_hora': forms.DateInput(attrs={
                'placeholder': 'DD/MM/AAAA',
                'type': 'date'
            }),
        }
