from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'cpf', 'email', 'remuneracao')
        labels = {'nome': 'Nome completo', 'cpf': 'CPF', 'email': 'E-mail', 'remuneracao': 'Remuneração (R$)'}
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do funcionário', 'autocomplete': 'name'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00', 'maxlength': 14, 'inputmode': 'numeric'}),
            'email': forms.EmailInput(attrs={'placeholder': 'nome@exemplo.com', 'autocomplete': 'email'}),
            'remuneracao': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'placeholder': '0,00'}),
        }
