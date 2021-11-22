from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empresa, Projeto, Aluno

# criar views


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', 'representante', 'sobrenomerepre', 'telefone', 'email']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class ProjetoCreate(CreateView):
    model = Projeto
    fields = ['titulo', 'dataLimite', 'descreva']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class AlunoCreate(CreateView):
    model = Aluno
    fields = ['nome', 'sobrenome', 'telefone', 'email']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')

    # Atualizar Views


class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nome', 'representante', 'sobrenomerepre', 'telefone', 'email']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class ProjetoUpdate(UpdateView):
    model = Projeto
    fields = ['titulo', 'dataLimite', 'descreva']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class AlunoUpdate(UpdateView):
    model = Aluno
    fields = ['nome', 'sobrenome', 'telefone', 'email']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


# Deletar Views


class EmpresaDelete(DeleteView):
    model = Empresa
    template_name = 'cadastro/form-excluir'
    success_url = reverse_lazy('index')


class ProjetoDelete(DeleteView):
    model = Projeto
    template_name = 'cadastro/form-excluir'
    success_url = reverse_lazy('index')


class AlunoDelete(DeleteView):
    model = Aluno
    template_name = 'cadastro/form-excluir'
    success_url = reverse_lazy('index')
