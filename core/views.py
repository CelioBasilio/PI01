from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Empresa, Projeto, Aluno
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

# criar views


class EmpresaCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Empresa
    fields = ['nome', 'representante', 'sobrenomerepre', 'telefone', 'email']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-projeto')

    def form_valid(self, form):

        form.instance.usuarioEmpresa = self.request.user
        # Antes do super objeto não foi criado

        url = super(EmpresaCreate, self).form_valid(form)

        # Depois do super objeto criado
        return url


class ProjetoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    fields = ['titulo', 'dataLimite', 'descreva']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-projeto')

    def form_valid(self, form):
        form.instance.usuarioEmpresa = self.request.user

        # Antes do super objeto não foi criado

        url = super(ProjetoCreate, self).form_valid(form)

        # Depois do super objeto criado
        return url


class AlunoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoAluno'
    model = Aluno
    fields = ['nome', 'sobrenome', 'telefone', 'email']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        form.instance.usuarioAluno = self.request.user

        # Antes do super objeto não foi criado

        url = super(AlunoCreate, self).form_valid(form)

        # Depois do super objeto criado
        return url

    # Atualizar Views


class EmpresaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Empresa
    fields = ['nome', 'representante', 'sobrenomerepre', 'telefone', 'email']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')


class ProjetoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    fields = ['titulo', 'dataLimite', 'descreva']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Projeto,pk=self.kwargs['pk'], usuarioEmpresa=self.request.user)
       # ou self.object = Projeto.object.get(pk=self.kwargs['pk'], usuarioEmpresa=self.request.user)
        return self.object


class AlunoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoAluno'
    model = Aluno
    fields = ['nome', 'sobrenome', 'telefone', 'email']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')


# Deletar Views


class EmpresaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Empresa
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        # ou self.object = get_object_or_404(Projeto,pk=self.kwargs['pk'], usuarioEmpresa=self.request.user)
        self.object = Projeto.object.get(pk=self.kwargs['pk'], usuarioEmpresa=self.request.user)
        return self.object


class ProjetoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('index')


class AlunoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoAluno'
    model = Aluno
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('index')

# Listar Views


class EmpresaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Empresa
    template_name = 'cadastro/listas/empresa.html'


class ProjetoList(ListView):
    model = Projeto
    template_name = 'cadastro/listas/projeto.html'

    def get_queryset(self):

        self.object_list = Projeto.objects.filter(usuarioEmpresa=self.request.user)
        return self.object_list


class AlunoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Aluno
    template_name = 'cadastro/listas/aluno.html'
