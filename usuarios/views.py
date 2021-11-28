from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import EmpresaForm, AlunoForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Aluno, Empresa

# Create your views here.


class EmpresaCreate(CreateView):

    template_name = 'usuarios/form.html'
    form_class = EmpresaForm
    success_url = reverse_lazy('cadastrar-empresa')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='GrupoEmpresa')

        url = super(EmpresaCreate, self).form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Empresa.objects.create(empresa=self.object)

        return url


class AlunoCreate(CreateView):

    template_name = 'usuarios/form.html'
    form_class = AlunoForm
    success_url = reverse_lazy('account_login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='GrupoAluno')

        url = super(AlunoCreate, self).form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Aluno.objects.create(aluno=self.object)

        return url


class AlunoUpdate(UpdateView):
    template_name = 'cadastro/form.html'
    model = Aluno
    fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email']
    success_url = reverse_lazy('listar-projeto')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Aluno, aluno=self.request.user)
        return self.object


class EmpresaUpdate(UpdateView):
    template_name = 'cadastro/form.html'
    model = Empresa
    fields = ['nome', 'cnpj', 'representante', 'sobrenomerepre', 'telefone', 'email']
    success_url = reverse_lazy('listar-projeto')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Empresa, empresa=self.request.user)
        return self.object