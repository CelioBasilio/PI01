from django.shortcuts import render
from django.views import generic

from sintproedu.core.models import Empresa, Projeto


# Create your views here.


class EmpresaCadastro(generic.CreateView):
    model = Empresa
    fields = 'nome', 'documento', 'email',
