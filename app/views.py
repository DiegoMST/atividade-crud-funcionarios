from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .forms import FuncionarioForm
from .models import Funcionario

class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'form_funcionario.html'
    success_url = reverse_lazy('lista_funcionarios')

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'lista_funcionarios.html'

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'form_funcionario.html'
    success_url = reverse_lazy('lista_funcionarios')

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = 'lista_funcionario.html'
    context_object_name = 'fun'

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'remover_funcionario.html'
    success_url = reverse_lazy('lista_funcionarios')
