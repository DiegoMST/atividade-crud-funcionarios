from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'remuneracao')
    search_fields = ('nome', 'cpf', 'email')
